import requests
import pandas as pd
import datetime
import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Google Sheet setup
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
credentials = ServiceAccountCredentials.from_json_keyfile_name("service_account_key.json", scope)
gc = gspread.authorize(credentials)

# Opening Google Sheet
spreadsheet = gc.open("crypto-data") 
 
# Access the first sheet
worksheet = spreadsheet.sheet1  

# Function to fetch cryptocurrency data
def fetch_crypto_data():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 50,
        "page": 1
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Failed to fetch data: {e}")
        return None

# Function to update Google Sheets
def update_google_sheet(dataframe):
    
    try:
        # Convert DataFrame to list of lists
        rows = [dataframe.columns.tolist()] + dataframe.values.tolist()
        worksheet.clear()  # Clear existing data
        worksheet.update(rows)  # Write new data
        print(f"Google Sheet updated successfully at {datetime.datetime.now()}")
        
    except Exception as e:
        print(f"Failed to update Google Sheet: {e}")

while True:
    crypto_data = fetch_crypto_data()

    if crypto_data:
        df = pd.DataFrame(
            crypto_data,
            columns=["name", "symbol", "current_price", "market_cap", "total_volume", "price_change_percentage_24h"]
        )

        # Rename columns
        df = df.rename(columns={
            "name": "Cryptocurrency Name",
            "symbol": "Symbol",
            "current_price": "Current Price (USD)",
            "market_cap": "Market Capitalization",
            "total_volume": "24h Trading Volume",
            "price_change_percentage_24h": "24h Price Change (%)"
        })

        # Added a timestamp column
        df["Timestamp"] = datetime.datetime.now()

        # Convert to string
        df["Timestamp"] = df["Timestamp"].astype(str)
        
        # Update Google Sheets
        update_google_sheet(df)
    else:
        print("No data fetched.")

    # Wait for 5 minutes before the next update
    time.sleep(300)

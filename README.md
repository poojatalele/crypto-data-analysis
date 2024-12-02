# Crypto Data Analysis

## Features
- Fetches live data for the top 50 cryptocurrencies.
- Analyzes key metrics like market capitalization, trading volume, and 24-hour price changes.
- Updates a Google Sheet in real-time with automated updates every 5 minutes.

## Setup Instructions

1. Clone the Repository
   
`git clone https://github.com/poojatalele/crypto-data-analysis.git`

`cd crypto-data-analysis`

## Setup Google Sheets API
- Go to the Google Cloud Console.
- Create a new project and enable the Google Sheets API and Google Drive API.
- Create a service account and download the JSON key file.
- Save the JSON file in the project directory and rename it to service_account_key.json.

## Share Your Google Sheet
- Create a Google Sheet and name it crypto-data.
- Share the sheet with the service account email i.e client_email (found in the JSON key file) and give it Editor access.

## Run the Script
Start the script to fetch, analyze, and update the data

`python main.py`

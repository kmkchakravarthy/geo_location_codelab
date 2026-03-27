# Geo Location Search App

A simple Flask web application that allows users to search for geo locations using OpenStreetMap Nominatim API (free, no API key required) and view them on Google Maps.

## Setup

1. Create and activate a virtual environment:
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the app:
   ```
   python app.py
   ```

4. Open your browser to `http://127.0.0.1:5001/`

## Usage

- Enter a location name in the search box.
- Select from the list of matching locations.
- You will be redirected to Google Maps showing the selected location.

## Note

This app uses OpenStreetMap Nominatim API, which is free but has rate limits (1 request per second). For heavy usage, consider a paid API.
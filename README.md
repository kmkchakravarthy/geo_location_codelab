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

## Publishing to GitHub

1. Initialize Git repository (if not already done):
   ```
   git init
   ```

2. Add files and commit:
   ```
   git add .
   git commit -m "Initial commit: Geo location search app"
   ```

3. Create a new repository on GitHub:
   - Go to [GitHub.com](https://github.com) and log in.
   - Click "New repository".
   - Name it (e.g., `geo_location_codelab`).
   - Make it public or private.
   - Do not initialize with README or .gitignore.
   - Click "Create repository".

4. Add remote and push:
   ```
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
   git push -u origin main
   ```
   - Replace `YOUR_USERNAME` and `YOUR_REPO_NAME` with your actual GitHub details.
   - **Authentication**: GitHub requires a Personal Access Token (PAT) instead of your password.
     - Go to [GitHub Settings > Developer settings > Personal access tokens > Tokens (classic)](https://github.com/settings/tokens).
     - Click "Generate new token (classic)".
     - Give it a name (e.g., "Geo App Push").
     - Select scopes: Check "repo" (full control of private repositories).
     - Click "Generate token" and copy it.
     - When prompted for password during push, paste the token (not your GitHub password).

## Cloning the Repository

To clone and run this app on another machine or directory:

1. Open a terminal and navigate to your desired directory:
   ```
   cd /path/to/your/directory
   ```

2. Clone the repository:
   ```
   git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
   ```
   - Replace `YOUR_USERNAME` and `YOUR_REPO_NAME` with the actual values (e.g., `kmkchakravarthy/geo_location_codelab`).

3. Navigate into the cloned directory:
   ```
   cd YOUR_REPO_NAME
   ```

4. Follow the Setup steps above to run the app.
from flask import Flask, render_template, request, redirect, url_for, session
import requests
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Change this to a random secret key

GOOGLE_API_KEY = 'AIzaSyB3QsFbozo9bRE9E_gXoV1SiznK1Z06QwM'
# GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')  # Set your Google API key as environment variable

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        location = request.form['location']
        return redirect(url_for('search', location=location))
    return render_template('index.html')

@app.route('/search/<location>')
def search(location):
    # Using OpenStreetMap Nominatim API (free, no key required)
    url = f"https://nominatim.openstreetmap.org/search?format=json&q={location}&limit=10"
    headers = {'User-Agent': 'GeoSearchApp/1.0'}
    print(f"Requesting URL: {url}")  # Debugging line
    response = requests.get(url, headers=headers)
    data = response.json()
    
    if data:
        results = data
        session['results'] = results
        return render_template('results.html', results=results, location=location)
    else:
        print("API Response:", data)
        return "Error: No results found"

@app.route('/select/<int:index>')
def select(index):
    results = session.get('results', [])
    if index < len(results):
        result = results[index]
        lat = float(result['lat'])
        lng = float(result['lon'])
        maps_url = f"https://www.google.com/maps/@{lat},{lng},15z"
        return redirect(maps_url)
    return "Invalid selection"

if __name__ == '__main__':
    app.run(debug=True, port=5001)
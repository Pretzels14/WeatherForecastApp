from flask import Flask, render_template, request, jsonify
import requests


app = Flask(__name__)

# OpenWeather API Key
API_KEY = "975ff7bb9b8d75baf9d4e47d59742f74"


# Route to render the home page
@app.route('/')
def home():
    return render_template('main.html')

# Route to process user inpu
@app.route('/weather', methods=['POST'])
def weather():
    city = request.form.get('city', '').strip()

    if not city:
        return jsonify({"error": "Please enter a city name."}), 400


    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"

    try:

        response = requests.get(url)
        response.raise_for_status()


        data = response.json()
        forecast = [

        ]

        # Return the forecast data as JSON
        return jsonify({"city": data["city"]["name"], "forecast": forecast})

    except requests.exceptions.RequestException as e:
        return jsonify({"error": "Unable to fetch weather data. Re-Enter the City Name."}), 500


# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)

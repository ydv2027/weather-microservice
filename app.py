from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Replace with your WeatherAPI.com API key
API_KEY = '1181625477ce4fb084a192150251002'
BASE_URL = 'http://api.weatherapi.com/v1/current.json'

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({'error': 'City parameter is required'}), 400

    try:
        # Make a request to WeatherAPI.com
        response = requests.get(f'{BASE_URL}?key={API_KEY}&q={city}')
        response.raise_for_status()
        data = response.json()

        # Extract temperature from the response
        temperature = data['current']['temp_c']
        return jsonify({'city': city, 'temperature': temperature})
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
const locationInput = document.getElementById('locationInput');
const unitSelection = document.getElementById('unitSelection');
const fetchWeatherBtn = document.getElementById('fetchWeatherBtn');
const weatherDisplay = document.getElementById('weatherDisplay');

const API_KEY = process.env.api_key;

function fetchWeather() {
    const location = locationInput.value;
    const units = unitSelection.value;

    if (!location) {
        alert('Please enter a city location!');
        return;
    } 
    const url = `https://api.openweathermap.org/data/2.5/weather?q=${location}&units=${units}&appid=${API_KEY}`;
    fetch(url)
        .then(response => {
            if (!response.ok) throw new Error('Location not found');
            return response.json();
        })
        .then(data => displayWeather(data, units))
        .catch(error => {
            weatherDisplay.innerHTML = `<p>${error.message}</p>`;
        });
}

function displayWeather(data, units) {
    const temperature = data.main.temp;           // Assigns temperature
    const feelsLike = data.main.feels_like;       // Assigns feels-like temperature
    const description = data.weather[0].description; // Weather description
    const humidity = data.main.humidity;          // Humidity percentage
    const windSpeed = data.wind.speed;            // Wind speed
    const unitSymbol = units === 'metric' ? '°C' : '°F'; // Temperature unit
    const speedUnit = units === 'metric' ? 'm/s' : 'mph'; // Wind speed unit

    weatherDisplay.innerHTML = `
        <h2>Weather in  ${data.name}</h2>
        <p>${description.charAt(0).toUpperCase() + description.slice(1)}</p>
        <p>Temperature: ${temperature}${unitSymbol}</p>
        <p>Feels Like: ${feelsLike}${unitSymbol}</p>
        <p>Humidity: ${humidity}</p>
        <p>Wind Speed: ${windSpeed}${speedUnit}</p>
    `;
}

fetchWeatherBtn.addEventListener('click', fetchWeather);
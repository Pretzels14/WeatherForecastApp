document.getElementById('weather-form').addEventListener('submit', async function (e) {
    e.preventDefault();

    const city = document.getElementById('city').value;
    const forecastDiv = document.getElementById('forecast');
    forecastDiv.innerHTML = "Loading...";

    try {
        const response = await fetch('/weather', {
            method: 'POST',
            headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
            body: new URLSearchParams({ city: city })
        });

        const data = await response.json();

        if (response.ok) {
    }
});
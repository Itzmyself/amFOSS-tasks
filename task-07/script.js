document.getElementById("getWeather").addEventListener("click", () => {
    const location = document.getElementById("location").value;
    if (!location) {
      alert("Please enter a location!");
      return;
    }
  
      const apiKey = "c30f286d56d1f8960d6f2581be4d478e";
      const url = `https://api.openweathermap.org/data/2.5/weather?q=${location}&appid=${apiKey}&units=metric`;

    fetch(url)
      .then(response => {
        if (!response.ok) {
          throw new Error("Location not found");
        }
        return response.json();
      })
      .then(data => {
        const resultDiv = document.getElementById("result");
        resultDiv.innerHTML = `
          <p><strong>Location:</strong> ${data.name}</p>
          <p><strong>Temperature:</strong> ${data.main.temp}°C</p>
          <p><strong>Weather:</strong> ${data.weather[0].description}</p>
        `;
      })
      .catch(error => {
        alert(error.message);
      });
  });
  
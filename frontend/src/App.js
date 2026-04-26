import React, { useState, useEffect } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [formData, setFormData] = useState({
    Location: 0,
    Temp9am: 28,
    Humidity9am: 72,
    Pressure9am: 1012,
    RainToday: 0
  });

  const [result, setResult] = useState("");
  const [history, setHistory] = useState([]);

  const handleChange = (e) => {
    const { name, value } = e.target;

    setFormData({
      ...formData,
      [name]: Number(value)
    });
  };

  const handleRainToday = (value) => {
    setFormData({
      ...formData,
      RainToday: value
    });
  };

  const fetchHistory = async () => {
    try {
      const response = await axios.get(
        "https://weather-mlops-project.onrender.com/history"
      );

      setHistory(response.data.history);
    } catch (error) {
      console.error("History fetch failed:", error);
    }
  };

  const handleSubmit = async () => {
    try {
      const response = await axios.post(
        "https://weather-mlops-project.onrender.com/predict",
        formData
      );

      setResult(response.data.prediction);

      // Refresh history after prediction
      fetchHistory();

    } catch (error) {
      console.error(error);
      setResult("Prediction failed");
    }
  };

  useEffect(() => {
    fetchHistory();
  }, []);

  return (
    <div className="container">
      <h1>☁ Weather Prediction Dashboard</h1>

      <select
        name="Location"
        onChange={handleChange}
        className="input"
        defaultValue="0"
      >
        <option value="0">Albury</option>
        <option value="1">Badgerys Creek</option>
        <option value="2">Cobar</option>
        <option value="3">Coffs Harbour</option>
        <option value="4">Moree</option>
        <option value="5">Newcastle</option>
        <option value="6">Norah Head</option>
        <option value="7">Norfolk Island</option>
        <option value="8">Penrith</option>
        <option value="9">Richmond</option>
        <option value="10">Sydney</option>
        <option value="11">Sydney Airport</option>
        <option value="12">Wagga Wagga</option>
        <option value="13">Williamtown</option>
        <option value="14">Wollongong</option>
        <option value="15">Canberra</option>
        <option value="16">Tuggeranong</option>
        <option value="17">Mount Ginini</option>
        <option value="18">Ballarat</option>
        <option value="19">Bendigo</option>
        <option value="20">Sale</option>
        <option value="21">Melbourne Airport</option>
        <option value="22">Melbourne</option>
        <option value="23">Mildura</option>
        <option value="24">Nhil</option>
        <option value="25">Portland</option>
        <option value="26">Watsonia</option>
        <option value="27">Dartmoor</option>
        <option value="28">Brisbane</option>
        <option value="29">Cairns</option>
        <option value="30">Gold Coast</option>
        <option value="31">Townsville</option>
        <option value="32">Adelaide</option>
        <option value="33">Mount Gambier</option>
        <option value="34">Nuriootpa</option>
        <option value="35">Woomera</option>
        <option value="36">Albany</option>
        <option value="37">Witchcliffe</option>
        <option value="38">Pearce RAAF</option>
        <option value="39">Perth Airport</option>
        <option value="40">Perth</option>
        <option value="41">Salmon Gums</option>
        <option value="42">Walpole</option>
        <option value="43">Hobart</option>
        <option value="44">Launceston</option>
        <option value="45">Alice Springs</option>
        <option value="46">Darwin</option>
        <option value="47">Katherine</option>
        <option value="48">Uluru</option>
      </select>

      <input
        className="input"
        name="Temp9am"
        placeholder="Temperature (°C)"
        value={formData.Temp9am}
        onChange={handleChange}
      />

      <input
        className="input"
        name="Humidity9am"
        placeholder="Humidity (%)"
        value={formData.Humidity9am}
        onChange={handleChange}
      />

      <input
        className="input"
        name="Pressure9am"
        placeholder="Pressure (hPa)"
        value={formData.Pressure9am}
        onChange={handleChange}
      />

      <div className="radio-group">
        <p>Did it rain today?</p>

        <button
          type="button"
          className={formData.RainToday === 1 ? "active" : ""}
          onClick={() => handleRainToday(1)}
        >
          Yes
        </button>

        <button
          type="button"
          className={formData.RainToday === 0 ? "active" : ""}
          onClick={() => handleRainToday(0)}
        >
          No
        </button>
      </div>

      <button
        className="predict-btn"
        type="button"
        onClick={handleSubmit}
      >
        Predict Weather
      </button>

      {result && (
        <div className="result-card">
          <h2>{result}</h2>
        </div>
      )}

      <div className="history-section">
        <h2>Recent Predictions</h2>

        {history.length === 0 ? (
          <p>No prediction history yet.</p>
        ) : (
          history.slice(0, 5).map((item) => (
            <div key={item.id} className="history-card">
              <p><strong>Location ID:</strong> {item.location}</p>
              <p><strong>Temp:</strong> {item.temperature} °C</p>
              <p><strong>Humidity:</strong> {item.humidity}%</p>
              <p><strong>Prediction:</strong> {item.prediction}</p>
            </div>
          ))
        )}
      </div>
    </div>
  );
}

export default App;


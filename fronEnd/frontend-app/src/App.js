// src/App.js

import React, { useState, useEffect } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [version, setVersion] = useState("");

  useEffect(() => {
    // Replace 'backend-url' with the actual URL of your backend API endpoint.
    const backendUrl = "http://backend_ms:3000/api/version";

    const fetchData = async () => {
      try {
        const response = await axios.get(backendUrl);
        console.log(response.data);
        setVersion(response.data.version);
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    };

    fetchData();
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <h1>Frontend Microservice</h1>
        <p>Backend Version: {version}</p>
      </header>
    </div>
  );
}

export default App;

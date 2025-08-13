import "./App.css";
import React, { useEffect, useState } from "react";

function App() {
  const [mensaje, setMensaje] = useState("");

  useEffect(() => {
    fetch("http://localhost:5000/")
      .then((response) => response.text())
      .then((data) => setMensaje(data));
  }, []);

  return (
    <div>
      <h1>APP DEL CLIMA</h1>
      <p>{mensaje}</p>
    </div>
  );
}

export default App;

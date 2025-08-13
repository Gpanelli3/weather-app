import React, { useState } from "react";

function FiveDays() {
  const [ciudad, setCiudad] = useState("");
  const [clima, setClima] = useState(null);

  const fetchFiveDays = async () => {
    console.log("Consultando...");
    try {
      const response = await fetch("http://localhost:5000/fiveDays/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ ciudad }),
      });
      const data = await response.json();
      console.log(data); // Verifica la respuesta aquí
      setClima(data);
    } catch (error) {
      setClima({ error: "Error al consultar el clima" });
    }
  };

  return (
    <div>
      <input
        type="text"
        value={ciudad}
        onChange={(e) => setCiudad(e.target.value)}
        placeholder="Ingresa una ciudad"
      />
      <button onClick={fetchFiveDays} disabled={!ciudad}>
        Consultar clima 5 días
      </button>
      {clima && clima.pronostico && (
        <div>
          <p>Ciudad: {clima.ciudad}</p>
          {clima.pronostico.map((dia, idx) => (
            <div key={idx}>
              <p>Fecha: {dia.fecha}</p>
              <p>Temperatura: {dia.temperatura}°C</p>
              <p>Descripción: {dia.descripcion}</p>
              <hr />
            </div>
          ))}
        </div>
      )}
      {clima && clima.error && <p>{clima.error}</p>}
    </div>
  );
}

export default FiveDays;

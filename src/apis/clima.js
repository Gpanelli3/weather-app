import React, { use, useEffect, useState } from "react";

function Clima() {
  const [ciudad, setCiudad] = useState("");
  const [clima, setClima] = useState(null);
  const [loading, setLoading] = useState(false);

  const consultarClima = async () => {
    setLoading(true);

    fetch("http://localhost:5000/weather/clima", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ ciudad: "Rosario" }),
    })
      .then((res) => res.json())
      .then((data) => setCiudad(data));

    try {
      const response = await fetch("http://localhost:5000/weather/clima", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ ciudad }),
      });
      const data = await response.json();
      setClima(data);
    } catch (error) {
      setClima({ error: "Error al consultar el clima" });
    }
    setLoading(false);
  };
  console.log(clima);

  return (
    <div>
      <input
        type="text"
        value={ciudad}
        onChange={(e) => setCiudad(e.target.value)}
        placeholder="Ingresa una ciudad"
      />
      <button onClick={consultarClima} disabled={loading}>
        {loading ? "Consultando..." : "Consultar Clima"}
      </button>
      {clima && (
        <div>
          {clima.error ? (
            <p>{clima.error}</p>
          ) : (
            <div>
              <p>Ciudad: {clima.ciudad}</p>
              <p>Temperatura: {clima.temperatura}°C</p>
              <p>Descripción: {clima.descripcion}</p>
            </div>
          )}
        </div>
      )}
    </div>
  );
}

export default Clima;

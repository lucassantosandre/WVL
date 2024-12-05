import React, { useState } from "react";
import axios from "axios";

function Home() {
  const [file, setFile] = useState(null);
  const [response, setResponse] = useState("");
  const [errorMessage, setErrorMessage] = useState("");

  // Define a URL da API com base no ambiente
  const API_URL =
    process.env.NODE_ENV === "development"
      ? "http://localhost:8000" // Ambiente local (fora do Docker)
      : "http://backend:8000"; // Ambiente Docker (usando o nome do serviço)

  const handleUpload = async () => {
    if (!file) {
      setErrorMessage("Please select a file before uploading.");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
      const res = await axios.post(`${API_URL}/analyze`, formData);
      setResponse(JSON.stringify(res.data, null, 2)); // Formata a resposta JSON
      setErrorMessage(""); // Limpa mensagens de erro
    } catch (error) {
      console.error("Upload Error:", error); // Log do erro no console
      setErrorMessage(
        "Failed to upload the file. Please check your connection or try again."
      );
    }
  };

  return (
    <div style={{ padding: "20px", fontFamily: "Arial, sans-serif" }}>
      <h1>Pose Analysis</h1>
      <input
        type="file"
        onChange={(e) => {
          setFile(e.target.files[0]);
          setResponse(""); // Limpa a resposta anterior ao selecionar novo arquivo
          setErrorMessage(""); // Limpa mensagem de erro anterior
        }}
      />
      <button
        onClick={handleUpload}
        style={{
          marginTop: "10px",
          padding: "10px 20px",
          backgroundColor: "#007bff",
          color: "white",
          border: "none",
          borderRadius: "4px",
          cursor: "pointer",
        }}
      >
        Upload
      </button>
      {response && (
        <div
          style={{
            marginTop: "20px",
            padding: "10px",
            backgroundColor: "#f0f0f0",
            borderRadius: "4px",
            whiteSpace: "pre-wrap",
          }}
        >
          <strong>Response:</strong>
          <pre>{response}</pre>
        </div>
      )}
      {errorMessage && (
        <p style={{ color: "red", marginTop: "10px" }}>{errorMessage}</p>
      )}
    </div>
  );
}

export default Home;

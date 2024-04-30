import React, { useState } from 'react';
import './App.css';


const UploadComponent = () => {
    // State variable to store the response from the backend
  const [uploadResponse, setUploadResponse] = useState('');
  const [selectedFile, setSelectedFile] = useState(null);


  const handleFileChange = (event) => {
    setSelectedFile(event.target.files[0]);
  };

  // Function to handle file upload
  const handleFileUpload = async (event) => {
    // Create a FormData object to store the file
    const formData = new FormData();
    formData.append('file', selectedFile);

    // Send a POST request to the Django backend
    try {
      const response = await fetch('http://127.0.0.1:8000/upload/', {
        method: 'POST',
        body: formData,
      });
      
      if (response.ok) {
        // File uploaded successfully
        const responseData = await response.json();
        setUploadResponse(responseData.message);
      } else {
        // Error handling if the upload fails
        console.log(response.headers);
        setUploadResponse('Error uploading file. Please try again later.');
      }
    } catch (error) {
      
      console.error('Error:', error);
      setUploadResponse('An error occurred. Please try again later.');
    }
  };
  return (
    <div style={{ background:'linear-gradient(180deg, rgba(0, 0, 255, 0.6), rgba(0, 0, 255, 0))', padding: '2rem', borderRadius: '1rem', textAlign: 'center', fontWeight: 'bold' }}>
        
        <p style={{ fontSize: '2rem', color: 'black', padding: '1.25rem' }}>Upload Your File and Ask me!</p>
        <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', gap: '1rem' }}>
          <input
            type="file"
            onChange={handleFileChange}
            style={{ fontSize: '0.875rem', color: 'black', padding: '0.5rem 1rem', borderRadius: '9999px', border: 'none', fontWeight: 'bold', backgroundColor: 'white', cursor: 'pointer' }}
          />
          <button
            style={{ width: '50%', backgroundColor: 'black', borderRadius: '9999px', fontFamily: 'Roboto', fontWeight: 'bold', color: 'white', fontSize: '1.25rem', padding: '0.5rem', cursor: 'pointer' }}
            onClick={handleFileUpload}
          >
            Upload
          </button>
        </div>

        {/* Display the response from the backend */}
        <div>{uploadResponse}</div>

        </div>
  );
};

export default UploadComponent;
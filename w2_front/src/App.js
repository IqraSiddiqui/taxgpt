import React from 'react';
import './App.css';
import ChatComponent from './ChatComponent';
import UploadComponent from './UploadComponent';



function App() {

  return (
    <div style={{ background: 'linear-gradient(180deg, rgba(0, 0, 0, 0), rgba(0, 150, 0, 0.6))', height: '100vh', width: '100vh', display: 'flex', justifyContent: 'center', alignItems: 'center', flexDirection: 'column' }}>
    <UploadComponent/>
    <ChatComponent/>
    </div>
  );
}

export default App;

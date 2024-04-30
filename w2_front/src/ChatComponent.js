import React, { useState } from 'react';
import './App.css';


const ChatComponent = () => {
    const [prompt, setPrompt] = useState('');
    const [response, setResponse] = useState('');

    const handleSubmit = async () => {
        try {
            const response = await fetch('http://127.0.0.1:8000/chat/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ prompt }),
            });
            const data = await response.json();
            console.log(data)
            const lines = data.response.split('\n');
            let answer = '';
            lines.forEach(line => {
                if (line.startsWith('Answer:')) {
                    answer = line.substring('Answer:'.length).trim();
                    return;
                }
            });
            setResponse(answer);
        } catch (error) {
            console.error('Error:', error);
        }
    };

    return (
        <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', gap: '1rem' }}>
            <input style={{ width: '100%', marginBottom: '0.5rem', borderRadius: '9999px' }} type="text" value={prompt} onChange={(e) => setPrompt(e.target.value)} />
            <button style={{ width: '50%', backgroundColor: 'black', borderRadius: '9999px', fontFamily: 'Roboto', fontWeight: 'bold', color: 'white', fontSize: '0.8rem', padding: '0.3rem', cursor: 'pointer' }}
            onClick={handleSubmit}>Ask Me!</button>
            {response && <div style={{ fontFamily: 'Roboto', fontWeight: 'bold', color: 'black' }}>Answer: <br></br>{response}</div>}
        </div>
    );
};

export default ChatComponent;

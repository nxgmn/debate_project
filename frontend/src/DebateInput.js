import React, { useState } from 'react';
import axios from 'axios';

const DebateInput = () => {
    const [topic, setTopic] = useState('');
    const [response, setResponse] = useState('');
    const [loading, setLoading] = useState(false);

    const handleSubmit = async (e) => {
        e.preventDefault();
        setLoading(true);
        try {
            const res = await axios.post('http://localhost:5000/run-debate', { topic });
            setResponse(res.data.output); // Assuming the backend returns the debate output
        } catch (error) {
            console.error('Error running debate:', error);
            setResponse('An error occurred. Please try again.');
        } finally {
            setLoading(false);
        }
    };

    return (
        <div>
            <h1>Debate Generator</h1>
            <form onSubmit={handleSubmit}>
                <label>
                    Topic:
                    <input
                        type="text"
                        value={topic}
                        onChange={(e) => setTopic(e.target.value)}
                        placeholder="Enter a debate topic"
                        required
                    />
                </label>
                <button type="submit" disabled={loading}>
                    {loading ? 'Running...' : 'Run Debate'}
                </button>
            </form>
            {response && (
                <div>
                    <h2>Debate Output:</h2>
                    <p>{response}</p>
                </div>
            )}
        </div>
    );
};

export default DebateInput;

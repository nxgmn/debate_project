import React, { useState } from 'react';
import axios from 'axios';

const DebateResponses = () => {
    const [responses, setResponses] = useState([]);
    const [loading, setLoading] = useState(false);

    const fetchDebateResponses = async () => {
        setLoading(true);
        try {
            const response = await axios.post('http://localhost:5000/run-debate');
            setResponses([response.data.output]); // Assuming the output is a single string
        } catch (error) {
            console.error('Error fetching debate responses:', error);
        } finally {
            setLoading(false);
        }
    };
    

    return (
        <div>
            <h1>Debate Responses</h1>
            <button onClick={fetchDebateResponses}>Fetch Responses</button>
            {loading && <p>Loading...</p>}
            <ul>
                {responses.map((res, index) => (
                    <li key={index}>{res}</li>
                ))}
            </ul>
        </div>
    );
};

export default DebateResponses;

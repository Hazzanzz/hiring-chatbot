import React, { useState } from 'react';
import axios from 'axios';

function Dashboard() {
    const [cvData, setCvData] = useState({});
    const [questions, setQuestions] = useState([]);
    const [feedback, setFeedback] = useState("");

    const handleCvUpload = async (event) => {
        const file = event.target.files[0];
        const formData = new FormData();
        formData.append('cv', file);

        const response = await axios.post('/cv/analyze', formData);
        setCvData(response.data);
    };

    const handleResponse = async (response) => {
        const questionResponse = await axios.post('/candidate/question', { response });
        setFeedback(questionResponse.data.feedback);
        setQuestions(questionResponse.data.questions);
    };

    return (
        <div>
            <input type="file" onChange={handleCvUpload} />
            {questions.map(q => <div key={q}>{q}</div>)}
            <input type="text" onChange={(e) => handleResponse(e.target.value)} />
            <div>{feedback}</div>
        </div>
    );
}

export default Dashboard;

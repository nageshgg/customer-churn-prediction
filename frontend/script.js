document.getElementById('churn-form').addEventListener('submit', async (e) => {
    e.preventDefault(); // Prevent the default form submission

    // Get all form data
    const formData = new FormData(e.target);
    const data = {};

    // Map form IDs to API model fields and convert types
    data.gender = formData.get('gender');
    data.SeniorCitizen = parseInt(formData.get('SeniorCitizen'));
    data.Partner = formData.get('Partner');
    data.Dependents = formData.get('Dependents');
    data.tenure = parseInt(formData.get('tenure'));
    data.PhoneService = formData.get('PhoneService');
    data.MultipleLines = formData.get('MultipleLines');
    data.InternetService = formData.get('InternetService');
    data.OnlineSecurity = formData.get('OnlineSecurity');
    data.OnlineBackup = formData.get('OnlineBackup');
    data.DeviceProtection = formData.get('DeviceProtection');
    data.TechSupport = formData.get('TechSupport');
    data.StreamingTV = formData.get('StreamingTV');
    data.StreamingMovies = formData.get('StreamingMovies');
    data.Contract = formData.get('Contract');
    data.PaperlessBilling = formData.get('PaperlessBilling');
    data.PaymentMethod = formData.get('PaymentMethod');
    data.MonthlyCharges = parseFloat(formData.get('MonthlyCharges'));
    data.TotalCharges = parseFloat(formData.get('TotalCharges'));

    // Send a POST request to the API
    try {
        const response = await fetch('http://127.0.0.1:8000/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        if (!response.ok) {
            const errorData = await response.json();
            console.error('API Error:', errorData);
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const result = await response.json();
        
        // Display the prediction result
        document.getElementById('result').innerHTML = 
            `Prediction: <strong>${result.prediction}</strong><br>
            Probability of Churn: <strong>${(result.churn_probability * 100).toFixed(2)}%</strong>`;

    } catch (error) {
        console.error('Error:', error);
        document.getElementById('result').innerHTML = 'An error occurred. Please try again. Check the console for details.';
    }
});
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import joblib
import pandas as pd

# Define the input data model using Pydantic
class CustomerData(BaseModel):
    gender: str
    SeniorCitizen: int
    Partner: str
    Dependents: str
    tenure: int
    PhoneService: str
    MultipleLines: str
    InternetService: str
    OnlineSecurity: str
    OnlineBackup: str
    DeviceProtection: str
    TechSupport: str
    StreamingTV: str
    StreamingMovies: str
    Contract: str
    PaperlessBilling: str
    PaymentMethod: str
    MonthlyCharges: float
    TotalCharges: float

# Initialize the FastAPI app
app = FastAPI()

# Define the list of allowed origins
origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "http://127.0.0.1:5500", # Add the origin where your HTML file is served
    "file://" # Allow requests from a local file
]

# Add the most robust CORS middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods, including OPTIONS for preflight
    allow_headers=["*"],  # Allow all headers, which is crucial for preflight
)

# Load the trained model, scaler, and feature names once at startup for efficiency
try:
    model = joblib.load('churn_prediction_model.joblib')
    scaler = joblib.load('scaler.joblib')
    # Get the feature names from the model itself
    model_features = model.feature_names_in_
except FileNotFoundError:
    print("Error: Model or scaler file not found. Please ensure 'churn_prediction_model.joblib' and 'scaler.joblib' are in the same directory.")
    model = None
    scaler = None
    model_features = []

# Create the prediction endpoint
@app.post("/predict")
def predict_churn(customer: CustomerData):
    if not model or not scaler:
        return {"error": "Model files not loaded. Please check the server logs."}

    # Convert the Pydantic model to a dictionary
    data_dict = customer.dict()

    # Create a DataFrame from the dictionary
    input_df = pd.DataFrame([data_dict])
    
    # Feature Encoding
    categorical_cols = [
        'gender', 'Partner', 'Dependents', 'PhoneService', 'MultipleLines', 
        'InternetService', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 
        'TechSupport', 'StreamingTV', 'StreamingMovies', 'Contract', 
        'PaperlessBilling', 'PaymentMethod'
    ]
    input_df = pd.get_dummies(input_df, columns=categorical_cols, drop_first=True)

    # Ensure input_df has all the columns the model expects, fill missing with 0
    input_df = input_df.reindex(columns=model_features, fill_value=0)

    # Scale numerical features
    numerical_cols = ['tenure', 'MonthlyCharges', 'TotalCharges']
    input_df[numerical_cols] = scaler.transform(input_df[numerical_cols])

    # Make the prediction
    prediction = model.predict(input_df)
    probability = model.predict_proba(input_df)[0][1] # Probability of churn (class 1)

    # Return the prediction and probability
    result = {
        'prediction': 'Churn' if prediction[0] == 1 else 'No Churn',
        'churn_probability': probability
    }
    return result

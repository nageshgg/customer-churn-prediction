End-to-End Customer Churn Prediction Project
This project demonstrates a complete, end-to-end machine learning pipeline for predicting customer churn. It includes a data processing and model training backend, a REST API built with FastAPI to serve the model, and a simple frontend for user interaction.

The goal of this project is to showcase the entire process of taking a machine learning model from a Jupyter notebook to a production-like environment.

Project Components
Machine Learning (.ipynb): Data preprocessing, exploratory data analysis (EDA), model training, and evaluation using Python libraries like pandas, scikit-learn, matplotlib, and seaborn.

API (api.py): A RESTful API built with FastAPI that loads the trained model and scaler, handles incoming requests, validates data, and returns a churn prediction.

Frontend (frontend/): A user-friendly web interface created with HTML, CSS, and vanilla JavaScript that allows users to input customer data and see the real-time prediction from the API.

Installation
Clone the Repository:

git clone [https://github.com/your-username/your-repository-name.git](https://github.com/your-username/your-repository-name.git)
cd your-repository-name

Create a Virtual Environment and activate it:

python -m venv venv
# On Windows
.\venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate

Install the Required Libraries:

pip install pandas scikit-learn matplotlib seaborn jupyterlab fastapi "uvicorn[standard]" python-multipart joblib

Run the Jupyter Notebook:
Start a JupyterLab server and run through the notebook to train the model and generate the churn_prediction_model.joblib and scaler.joblib files.

jupyter-lab

How to Run the Project
Ensure you have completed all the installation steps and trained the model.

Start the API Server:
Open a terminal in the project's root directory and run the FastAPI server.

uvicorn api:app --reload

The API will be live at http://127.0.0.1:8000.

Start the Frontend Server:
Open a new terminal, navigate to the frontend folder, and start a simple HTTP server.

cd frontend
python3 -m http.server

The frontend will be live at http://localhost:8000.

Access the Application:
Open your web browser and go to http://localhost:8000. You can now enter customer data into the form and get a real-time churn prediction from the machine learning model.

Data
The dataset used in this project is the Telco Customer Churn dataset, a publicly available dataset from Kaggle. It contains information about a telecommunications company's customers and whether they churned or not.

License
This project is licensed under the MIT License
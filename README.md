# Data Science Project: Tangelo

This project demonstrates the end-to-end process of a data science project, from initial data exploration to model deployment using the FastAPI framework. The goal of the project is to showcase how to explore a dataset, preprocess it, train a machine learning model, and create an API for making predictions.

## Project Structure

The project is organized into the following sections:

1. **Exploration Notebook**: The `.data/exploration.ipynb` notebook provides an in-depth analysis of the dataset, including data visualization, statistical summaries, and initial insights.

2. **Transformation**: The `.data/transformation.ipynb` notebook focuses on data preprocessing and transformation. 

3. **Training**: The `.data/training.ipynb` notebook train a machine learning model on the preprocessed data using scikit-learn. It also includes hyperparameter tuning and model evaluation.

4. **API Deployment**: The `api.py` script contains the code for deploying the trained model as a FastAPI web API. Users can send input data to the API for making predictions.

## Environment Setup

To replicate the environment for this project, follow these steps:

1. Clone this repository.
2. Create an environment and activate it.
3. Install the required packages using the `requirements.txt`


## Running the API

To test the deployed API, follow these steps:

1. Ensure you have activated the virtual environment.
2. Open a terminal in the project directory.
3. Run the following command to start the FastAPI server: `uvicorn api:app --reload`
4. Open your web browser and go to: [http://127.0.0.1:8000/docs]
5. In the API documentation interface, use the POST function to test the API using the provided `test_dataset.json` file. 



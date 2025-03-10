# Assessment-Task
Here's the code for the `README.md` file as used previously:

```markdown
# House Price Prediction Project

This project implements a machine learning model for predicting house prices using the California Housing Dataset.

## Project Structure

- `main.ipynb`: Jupyter Notebook containing data preprocessing, model training, and evaluation.
- `app.py`: Flask application for serving predictions.
- `Dockerfile`: Dockerfile for containerizing the application.
- `requirements.txt`: List of required Python packages.
- `best_house_price_model.joblib`: Trained Random Forest model.
- `scaler.joblib`: Scaler used for feature scaling.
- `report.pdf`: Project report.

## Running the Project

1. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

2. **Run the Jupyter Notebook:**
   ```
   jupyter notebook main.ipynb
   ```

3. **Run the Flask application:**
   ```
   python app.py
   ```

4. **Test the API:**
   Use CURL or Postman to send a POST request to `http://localhost:5000/predict` with a JSON payload like:
   ```json
   {
       "features": [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1]
   }
   ```

5. **Containerize the application (optional):**
   ```
   docker build -t house-price-predictor .
   docker run -p 5000:5000 house-price-predictor
   ```


## Author

PRIYANSHU BHATIA```


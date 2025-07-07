import warnings
warnings.filterwarnings("ignore")
import joblib
import os

# ✅ Load model
model_path = os.path.join(os.path.dirname(__file__), '..', 'models', 'risk_model.pkl')
model = joblib.load(model_path)
print("✅ Model loaded.")

# ✅ Sample input (make sure these values match your training features)
sample_input = [[1, 50000, 2, 30]]  # Example: [employment_status_encoded, income, number_of_defaults]

# ✅ Make prediction
prediction = model.predict(sample_input)
print("📊 Input:", sample_input)
print("🔍 Prediction:", "High Risk" if prediction[0] == 1 else "Low Risk")

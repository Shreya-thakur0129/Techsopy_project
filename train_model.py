import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import joblib

# Generate synthetic dataset
np.random.seed(42)
n_samples = 500

# Synthetic features
ages = np.random.randint(20, 65, size=n_samples)
employment_status = np.random.choice(['Employed', 'Unemployed'], size=n_samples, p=[0.7, 0.3])
annual_income = np.random.normal(60000, 15000, size=n_samples).astype(int)
annual_income = np.clip(annual_income, 20000, 120000)  # clamp to realistic values
num_defaults = np.random.poisson(1.2, size=n_samples)
num_defaults = np.clip(num_defaults, 0, 5)

# Risk label generation rule
risk = []
for emp, inc, defs, age in zip(employment_status, annual_income, num_defaults, ages):
    if emp == 'Unemployed' or defs > 2 or inc < 40000:
        risk.append(1)  # High risk
    else:
        risk.append(0)  # Low risk

# Assemble into DataFrame
df = pd.DataFrame({
    'age': ages,
    'employment_status': employment_status,
    'annual_income': annual_income,
    'num_defaults': num_defaults,
    'risk': risk
})

# Encode employment_status
df['employment_status'] = df['employment_status'].apply(lambda x: 1 if x == 'Employed' else 0)

# Features and target
X = df[['employment_status', 'annual_income', 'num_defaults', 'age']]
y = df['risk']

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Save model
joblib.dump(model, 'models/risk_model.pkl')

print("✅ Model trained on synthetic data and saved as 'risk_model.pkl'")

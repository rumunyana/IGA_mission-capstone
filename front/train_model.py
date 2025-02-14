import pandas as pd
import numpy as np
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Generate Sample Data
data = {
    "Grade": np.random.randint(50, 100, 100),
    "Attendance": np.random.randint(70, 100, 100),
    "Interest_Math": np.random.randint(1, 5, 100),
    "Interest_Science": np.random.randint(1, 5, 100),
    "Age": np.random.randint(14, 18, 100),
    "Optimal_Track": np.random.choice([0, 1, 2, 3], 100)  # 0: STEM, 1: Humanities, 2: Arts, 3: Business
}

df = pd.DataFrame(data)

# Train-Test Split
X = df.drop(columns=["Optimal_Track"])
y = df["Optimal_Track"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate Model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")

# Save Model
joblib.dump(model, "model_rf.joblib")
print("Model saved as model_rf.joblib")

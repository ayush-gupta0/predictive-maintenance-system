import pandas as pd
import mlflow
import dagshub
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score

# Connect to DagsHub
dagshub.init(repo_owner="ayush-gupta0", repo_name="predictive-maintenance-system", mlflow=True)

def train_model():
    df = pd.read_csv('data/sensor_data.csv')
    X = df[['temp', 'vibration', 'pressure']]
    y = df['target']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    
    with mlflow.start_run(run_name="PdM_Baseline"):
        model = RandomForestClassifier(n_estimators=100)
        model.fit(X_train, y_train)
        
        f1 = f1_score(y_test, model.predict(X_test))
        mlflow.log_metric("f1_score", f1)
        mlflow.sklearn.log_model(model, "maintenance_model")
        print(f"✅ Training complete. F1 Score: {f1:.4f}")

if __name__ == "__main__":
    train_model()
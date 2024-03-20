from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib

# Generate synthetic dataset
# Generate synthetic dataset
X, y = make_classification(
    n_samples=100,           # Total number of samples
    n_features=5,            # Total number of features
    n_informative=3,         # Number of informative features (adjust as needed)
    n_redundant=1,           # Number of redundant features (adjust as needed)
    n_clusters_per_class=1,  # Number of clusters per class
    random_state=42
)


# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Choose model (Logistic Regression)
model = LogisticRegression()

# Train model
model.fit(X_train, y_train)

# Save model to file
joblib.dump(model, 'train-model.joblib')

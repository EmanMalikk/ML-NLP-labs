from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import KFold, cross_val_score

X, y = load_iris(return_X_y=True)

clf = LogisticRegression(random_state=42)

k_folds = KFold(n_splits = 7)

scores = cross_val_score(clf, X, y, cv = k_folds)

print("Cross Validation Scores: ", scores)
print("Average CV Score: ", scores.mean())
print("Number of CV Scores used in Average: ", len(scores))

# Display the performance for each fold
for i, result in enumerate(scores):
    print(f"Fold {i + 1} Accuracy: {result:.2f}")
import numpy as np

# Example predictions from three models
preds_model1 = np.array([0.8, 0.2, 0.6])
preds_model2 = np.array([0.7, 0.3, 0.5])
preds_model3 = np.array([0.9, 0.1, 0.7])

# Define weights for each model based on their performance
weights = [0.4, 0.3, 0.3]

# Calculate the weighted average of the predictions
blended_preds = np.average([preds_model1, preds_model2, preds_model3], weights=weights, axis=0)

print("Blended Predictions:", blended_preds)

# testing 
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import SelectKBest, mutual_info_classif
from sklearn.ensemble import RandomForestClassifier


def predict_stress_level(field1, field2, field3, field4):
    # Load data
    df = pd.read_csv("SaYoPillow.csv")

    # Rename columns for better readability
    df.columns = [
        "snoring range",
        "respiration rate",
        "body temperature",
        "limb movement rate",
        "blood oxygen levels",
        "eye movement",
        "number of hours of sleep",
        "heart rate",
        "Stress Levels",
    ]

    # Split data into features (x) and target (y)
    x = df.drop(columns=["Stress Levels"])
    y = df["Stress Levels"]

    # Perform feature selection using SelectKBest
    kbest = SelectKBest(mutual_info_classif, k=4)
    x_selected = kbest.fit_transform(x, y)

    # Get selected feature indices
    selected_indices = kbest.get_support(indices=True)

    # Define the user input
    user_input = [field1, field2, field3, field4]

    # Train the Random Forest model with selected features
    model = RandomForestClassifier()
    model.fit(x_selected, y)

    # Predict stress level using user input
    predicted_stress_level = model.predict([user_input])[0]
    return predicted_stress_level

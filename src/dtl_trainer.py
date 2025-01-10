import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, confusion_matrix

def create_predictor():
    dataFrame = pd.read_csv('src/dataset.csv')

    label_encoder = LabelEncoder()
    dataFrame['anomaly'] = label_encoder.fit_transform(dataFrame['anomaly'])

    encoded_dataFrame = pd.get_dummies(dataFrame, columns=['txn_type', 'pattern', 'age'], drop_first=True)

    X = encoded_dataFrame.drop(columns=['anomaly'])
    y = encoded_dataFrame['anomaly']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    classifier = DecisionTreeClassifier(criterion='entropy', max_depth=5, random_state=42)
    classifier.fit(X_train, y_train)

    y_prediction = classifier.predict(X_test)

    # print("Accuracy:", accuracy_score(y_test, y_prediction))

    # print("Confusion Matrix:\n", confusion_matrix(y_test, y_prediction))

    # visualiser for the predictor
    # plt.figure(figsize=(12, 8))
    # plot_tree(classifier, filled=True, feature_names=X.columns, class_names=['high_risk', 'low_risk', 'moderate_risk'], rounded=True)
    # plt.show()

    return classifier, dataFrame
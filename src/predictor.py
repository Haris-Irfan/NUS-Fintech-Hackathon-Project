from dtl_trainer import create_predictor
import pandas as pd

def make_prediction(amount: int, txn_type : str, login_freq : int, sess_dur : int, pattern : str, age : str):
    risk_predictor, dataFrame = create_predictor()

    dataFrame.loc[len(dataFrame)] = {
        "amount": amount,
        "txn_type": txn_type,
        "login_freq": login_freq,
        "sess_dur": sess_dur,
        "pattern": pattern,
        "age": age
    }

    encoded_dataFrame = pd.get_dummies(dataFrame, columns=['txn_type', 'pattern', 'age'], drop_first=True)
    X = encoded_dataFrame.drop(columns=['anomaly'])

    # return ['High Risk', 'Low Risk', 'Moderate Risk'][risk_predictor.predict(X)[-1]]
    return risk_predictor.predict(X)[-1]
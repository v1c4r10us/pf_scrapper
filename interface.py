import pickle
from datetime import datetime

def predict_price():
    str_d1 = '2022/10/03' #Limit day in train
    str_d2 = datetime.today().strftime('%Y/%m/%d') #Today
    d1 = datetime.strptime(str_d1, "%Y/%m/%d")
    d2 = datetime.strptime(str_d2, "%Y/%m/%d")

    delta=d2-d1

    #Prediction
    steps=delta.days
    price_for_today=0.0
    with open('forecaster.pkl', 'rb') as f:
        forecaster=pickle.load(f)
        price_for_today=round(forecaster.predict(steps=steps).iloc[-1],2)
    f.close()

    return price_for_today

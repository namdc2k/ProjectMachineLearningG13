import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import joblib
from sklearn import preprocessing as pre, svm
from sklearn.model_selection import train_test_split


df = pd.read_csv("input/weatherVip.csv")

fileModel = ''


def prediction(type):
    global valueY
    if not type:
        return "Xin kiểm tra loại cần dự đoán"
    else:
        x = np.array(df.drop([type, 'dateTime'], axis=1))
        y = df[type]

        # split into a training and testing set
        x_train, x_test, y_train, y_test = train_test_split(
            x, y, test_size=0.1)

        scaler = pre.StandardScaler().fit(x_train)
        x_train_scaled = scaler.transform(x_train)
        x_test_scaled = scaler.transform(x_test)
        print("Loading model.....")
        # Do not recompute if possible
        if type == 'tem':
            fileModel = 'modelTem.pkl'
            valueY = "°c"
        elif type == 'rain':
            fileModel = 'modelRain.pkl'
            valueY = "mm"
        elif type == 'cloud':
            fileModel = 'modelCloud.pkl'
            valueY = "%"
        elif type == 'wind':
            fileModel = 'modelWind.pkl'
            valueY = "km/h"
        elif type == 'gust':
            fileModel = 'modelGust.pkl'
            valueY = "km/h"
        try:
            SVR_model = joblib.load(fileModel)
        except:
            print("Failed, training model.....")
            SVR_model = svm.SVR(C=100,gamma=0.1).fit(
                x_train_scaled, y_train)
            joblib.dump(SVR_model, fileModel)

        print("Testing the model...")

        predict_y_array = SVR_model.predict(x_test_scaled)
        score = SVR_model.score(x_test_scaled, y_test)

        print("Score of", score)

        print("Plotting the model")

        y_test_np = np.array(y_test[0:100])

        plt.plot(y_test_np, color='g', label="Actual " + type)
        plt.plot(predict_y_array[0:100], color='r', label="Predicted " + type)

        plt.xlabel('day')
        plt.ylabel(valueY)
        plt.title(type + ' forecast')
        plt.legend()
        plt.show()

ans = True
while ans:
    print("""
    1.Nhiệt độ(°c)
    2.Mực nước mưa(mm)
    3.Mây(%)
    4.Tốc độ gió(km/h)
    5.Gió giật(km/h)
    """)
    ans = input("Chọn loại cần dự báo ")
    if ans == "1":
        prediction('tem')
    elif ans == "2":
        prediction('rain')
    elif ans == "3":
        prediction('cloud')
    elif ans == "4":
        prediction('wind')
    elif ans == "5":
        prediction('gust')
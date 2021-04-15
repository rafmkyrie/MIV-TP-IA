from PIL import Image 
import numpy as np
import glob
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

def get_paths(path):
    ''' Fonction qui retourne les chemins des images présentes dans le répertoire dont le path est donné en paramètre '''
    return glob.glob(path+"\\*.png")

def get_lowest_white_pixel(path):
    img = Image.open(path)  
    img = np.array(img)
    result = np.where(img == 255)
    rows = result[0]
    columns = result[1]
    y = np.max(rows)
    x = columns[np.argmax(rows)]

    return x, y


def get_data(path):
    ''' Fonction qui retourne les données récupérées des images '''
    imgs = get_paths(path)

    Xs = []
    Ys = []

    for img in imgs:
        x, y = get_lowest_white_pixel(img)
        Xs.append(x)
        Ys.append(y)
     
    return np.array(Xs), np.array(Ys)


if __name__ == '__main__':
    x_train, y_train = get_data("sequence\\Train")
    x_train = x_train.reshape(-1, 1)

    model = LinearRegression()
    model.fit(x_train, y_train)

    a = model.coef_[0]
    bias = model.intercept_

    print(a)
    print(bias)

    y_train_pred = model.predict(x_train)
    MSE_Train = mean_squared_error(y_train,y_train_pred)
    print("MSE error with training set : " + str(MSE_Train))


    # Test model 
    x_test, y_test = get_data("sequence\\Test")
    x_test = x_test.reshape(-1, 1)

    y_pred = model.predict(x_test)
    MSE_Test = mean_squared_error(y_test, y_pred)
    print("MSE error with testing set : " + str(MSE_Test))

    plt.scatter(x_train, y_train, color="blue")
    plt.scatter(x_test, y_test, color="red")
    plt.scatter(x_test, y_pred, color="orange")
    x = np.linspace(0, 260, 1000)

    plt.plot(x, a*x+bias, color="green")
    plt.show()

    

"""
 Puntos:

1) Specify which Machine Learning problem are you solving..........................(cada quien)

We are solving a binary classification problem using support vector machines, first we have a dataset consisting of 
7 dimensional vectors with the information of "date","Temperature","Humidity","Light","CO2","HumidityRatio","Occupancy"
The goal is implementing a support vector machines model for predicting the "Occupancy" given the other 6 data.
For this we will check if the dataset is linearly separable, for correctly implementing support vector machines.

2) Provide a short summary of the features and the labels you are working on.......

lets see the relation between each feature and the "Occupancy". it is important because we need to be sure we use adecuate features
for predicting occupancy. If there was a feature that had nothing to do with occupancy then we should not take it into account in our model.
the features we wil be working on are: 
"date": (format: date time year-month-day hour:minute:second) important data because it can be related with the normal values of "Temperature","Humidity" and "Light",
because these may vary during the day so we will consider for our model the hour in the day where the 7 data was recorded.

"Temperature": temperatue is related with occupancy because humans breath can increase temperature in a room.
(in Celsius)

"Humidity": humidity increases with the number of persons in a room, so it is related with occupancy.
(Relative Humidity, %)

"Light" : an occupied room may have the light turned on".
( light in lux)

"CO2":  the levels of CO2 increase with the more people there are in a room.
(CO2, in ppm)

"HumidityRatio": Humidity Ratio, Derived quantity from temperature and relative humidity, in kgwater-vapor/kg-air

Occupancy, 0 or 1, 0 for not occupied, 1 for occupied status


3) Please answer the following questions: 
    a) Are these datasets linearly separable?................................. .... 
    b) Are these datasets randomly chosen (mirar tiempo).........................   (se tiene una idea) 
    c) The sample size is enough to guarantee generalization...................... (toca buscar algun teorema)

4) Provide an explanation how and why the code is working......................... 
5) Show some examples to illustrate that the method is working properly............  (evaluarlo para ejemplos del data test)

6) Provide quantitative evidence for generalization using the provided dataset.....
"""

"""SVM_SKlearn   Are these datasets linearly separable? """
# for checking data is linearly separable, lets see if an svm can overfit perfectly the dataset
import pandas as pd
import numpy as np
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
import math

"""
 Los datos que se usan son de esta forma:
X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
y = np.array([1, 1, 2, 2])
from sklearn.svm import SVC
clf = make_pipeline(StandardScaler(), SVC(gamma='auto'))
clf.fit(X, y)
"""
#### preparando el dataset

a = pd.read_csv('C:/Users/sergi/OneDrive/Escritorio/MathforML/datatraining.csv', encoding='utf-8')
data_dict = np.array(a)

for i in range(len(data_dict)):
    data_dict[i][0] = (data_dict[i][0].split(","))

class0 = []
class1 = []
#ingeniería de características. usando solo la hora del día del dato de la fecha, porque puede tener incidencia en niveles de humedad base
fechas = []
# funcion para pasar horas minutos y segundos a minutos-
def hms_to_s(s):
    t = 0
    for u in s.split(':'):
        t = 60 * t + int(u)
    t = t/60
    t = round(t)
    return t
#fin funcion

for i in range(len(data_dict)):
    del data_dict[i][0][0]
    fechas.append(data_dict[i][0][0])
    fechas[i] = fechas[i].split( )
    del fechas[i][0]
    fechas[i] = ''.join(fechas[i])
    fechas[i] = fechas[i].replace('"', '')
    fechas[i] = hms_to_s(fechas[i])
    
    del data_dict[i][0][0]
    if data_dict[i][0][5] == "0":
        class0.append(data_dict[i][0])
    else:
        class1.append(data_dict[i][0])




for i in range(len(class0)):
   del class0[i][-1]
for i in range(len(class1)):
   del class1[i][-1]
for i in range(len(class0)):
    for j in range(len(class0[i])):
        class0[i][j] = float(class0[i][j])
for i in range(len(class1)):
    for j in range(len(class1[i])):
        class1[i][j] = float(class1[i][j])

# el dataset está separado en dos clases, ahora hay que crear un vector de etiquetas de la forma y = [1,1,1,1,...,1,-1,-1,-1,...,-1] 
# donde el numero de 1´s sea len(class0) y el numero de -1´s len(class1) y luego unir las dos clases en un solo vector de 
# caracteríaticas (X = [...]) (esto se hace para poder meter el dataset en sklearn.svm)

y = []

for i in range(len(class0)):
    y.append(1)
for i in range(len(class1)):
    y.append(-1)


X = class0 + class1


y = np.array(y)
X = np.array(X)

#print( "lenght of X is: ", len(X))  
#print( "lenght of y is: ", len(y))   # X y y ya tienen la misma longitud.


# implementación del svm:
#Punto 3
clf = make_pipeline(StandardScaler(), SVC(gamma='auto'))
clf.fit(X, y)

predict_X = clf.predict(X)

if predict_X.all() == y.all():
    print("el modelo predice perfectamente todos los x del entrenamiento (overfit), por lo tanto el dataset es linealmente separable")
else:
    print("el modelo no predice bien algun ejemplo del dataset")

# fin del punto de linearly separable 


# FALTA: b) Are these datasets randomly chosen and c) The sample size is enough to guarantee generalization.
# Punto 5
# Show some examples to illustrate that the method is working properly. 
""" usaremos el conjunto que está en el dataset (datatest) para dar algunos ejemplos de que el modelo está funcionando bien
"""

# punto 6
# veamos si el modelo generaliza  

""" lo que haremos es separar el dataset en dos conjuntos x_test, x_train, y_test, y_train 
luego entrenamos el modelo con el conjunto train y lo evaluamos en los ejemplos del conjunto test
# una vez se tienen los conjuntos de datos separados:
clf.fit(x_train, y_train)
predict = clf.predict(x_test)
print('Predicted Values from Classifier:', predict)
print('Actual Output is:', y_test)
print('Accuracy of the model is:', clf.score(x_test, y_test))
"""

data_test = pd.read_csv("C:/Users/sergi/OneDrive/Escritorio/MathforML/datatest.csv", encoding='utf-8') 
# le haremos el mismo proceso anterior al datatest

data_dict_test = np.array(data_test)
for i in range(len(data_dict_test)):
    data_dict_test[i][0] = (data_dict_test[i][0].split(","))
class0_test = []
class1_test = []
for i in range(len(data_dict_test)):
    del data_dict_test[i][0][0]
    del data_dict_test[i][0][0]
    if data_dict_test[i][0][5] == "0":
        class0_test.append(data_dict_test[i][0])
    else:
        class1_test.append(data_dict_test[i][0])
for i in range(len(class0_test)):
   del class0_test[i][-1]
for i in range(len(class1_test)):
   del class1_test[i][-1]
for i in range(len(class0_test)):
    for j in range(len(class0_test[i])):
        class0_test[i][j] = float(class0_test[i][j])
for i in range(len(class1_test)):
    for j in range(len(class1_test[i])):
        class1_test[i][j] = float(class1_test[i][j])
y_test = []
for i in range(len(class0_test)):
    y_test.append(1)
for i in range(len(class1_test)):
    y_test.append(-1)
X_test = class0_test + class1_test
y_test = np.array(y_test)
X_test = np.array(X_test)
#print( "lenght of X_test is: ", len(X_test))  
#print( "lenght of y_test is: ", len(y_test))   # X_test y y_test ya tienen la misma longitud. 


#clf.fit(X, y)  (ya lo corrimos antes) 
predict = clf.predict(X_test)


#veamos en que datos el modelo se está equivocando para predecir Y_test
indices_diferentes = []
n=0
while n < len(predict): 
    if predict[n] != y_test[n]:
        indices_diferentes.append(n)
    n = n+1
print("el modelo se equivoca en los siguientes indices de datos", indices_diferentes)
""" output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,21, 22, 834, 835, 836, 837, 838, 839, 840, 841, 842, 843, 844, 845,
846, 847, 848, 849,850, 851, 852, 853, 854, 855, 856, 857, 858, 859, 860, 861, 862, 863, 864, 865, 866, 867,868, 869, 870, 871, 1677, 1678, 1679, 1680,
1681, 1682, 1683, 1684, 1685, 1686, 1687, 1688, 1689, 1690, 1691, 1692, 1896, 2601, 2602]"""


print('Accuracy of the model in the Test set is:', clf.score(X_test, y_test)) """output: Accuracy of the model in the Test set is: 0.9699812382739212"""
if clf.score(X_test, y_test) > 0.95:
    print(" luego el modelo es capaz de generalizar en datos no vistos anteriormente")




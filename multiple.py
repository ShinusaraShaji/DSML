from sklearn.model_selection import train_test_split
from sklearn import linear_model
import pandas as pd
from sklearn.metrics import r2_score
df=pd.read_excel('knn/data.xlsx')
X=df[['Weight','Volume']]
y=df[['CO2']]
X=X.values
y=y.values
x_train,x_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=0)
print("Training Data(X):\n",x_train)
print("Training Labels(y):\n",y_train)
regr=linear_model.LinearRegression()
regr.fit(x_train,y_train)
predictedCO2=regr.predict([[2300,1300]])
print("\nPredicted CO2 for[2300,1300]:",predictedCO2)
score=regr.score(x_test,y_test)
print("\nModel R2 Score:",round(score,2))
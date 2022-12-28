import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor 

df=pd.read_csv('marks.csv')

X=df.drop(['Marks'],axis=1).copy().values 
y=df['Marks'].copy().values
X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=209)

model=RandomForestRegressor() 
model.fit(X_train,y_train) 
print(model.score(X_test,y_test))#0.9895706355256967

#print(model.predict(X_test))
#print(y_test)

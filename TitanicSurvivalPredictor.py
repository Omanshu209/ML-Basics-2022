import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier

df=pd.read_csv("train3.csv")
df["Male"]=df["Sex"]=="male"
df=df.dropna()
X=df[["PassengerId","Pclass" , "Male" ,"Fare", "Age", "Parch" ,"SibSp"]].values
y=df["Survived"].values
X_train,X_test,y_train,y_test = train_test_split(X,y,random_state=209)
modelNo=3
prediction=0
predictionArr=[]
S1=""
inputBool=""

arrAI=[["PassengerId","Pclass" , "Male" ,"Fare", "Age", "Parch" ,"SibSp"]]

model=RandomForestClassifier()
model.fit(X_train,y_train)

def TitanicAIDetails():
	global arrAI
	for i in range(7):
	   if i!=2:
	   	arrAI[0][i]=float(input(f"Enter {arrAI[0][i]} : "))
	   else:
	   	inputBool=input("Enter whether your gender is male(True/False) : ")
	   	if inputBool.lower()=="true":
	   		arrAI[0][i]=True
	   	elif inputBool.lower()=="false":
	   		arrAI[0][i]=False
    		
def TitanicAIPredict():
	global model,arrAI,predictionArr,prediction
	predictionArr=model.predict(arrAI)
	if predictionArr[0]==1:
	   print("AI : Luckily, Passenger with the entered details would have survived the Tinatic Disaster !")
	elif predictionArr[0]==0:
	   print("AI : Unfortunately, Passenger with the entered details would have not survived the Tinatic Disaster !")
    
def TitanicAIModel():
	global model,modelNo
	modelNo=int(input("Enter the model you want to use in numerical value \n\t(1 -- Logistic Regression Model\n\t2 -- Decision Tree Model\n\t3 -- Random Forest Model(default)\n\t4 -- Neural Network)\n : "))
	if modelNo==1:
	   model=LogisticRegression()
	elif modelNo==2:
	   model=DecisionTreeClassifier()
	elif modelNo==3:
	   model=RandomForestClassifier()
	elif modelNo==1:
	   model=MLPClassifier()
	model.fit(X_train,y_train)
	print(f"Model changed to {model}")
    
run=True
while run:
	print("********************")
	S1=input("Welcome to Titanic AI Predictor !\nDo you want to continue with the Random Forest Model? (y/n) : ")
	if S1=='n':
		TitanicAIModel()
	else:
		pass
	TitanicAIDetails()
	TitanicAIPredict()
	arrAI=[["PassengerId","Pclass" , "Male" ,"Fare", "Age", "Parch" ,"SibSp"]]
	print("********************")

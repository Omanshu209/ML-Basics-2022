# Creating an AI(Machine Learning Model) in just 4 lines(excluding the comments) as fast as possible!
from sklearn.linear_model import LinearRegression
MODEL = LinearRegression()
MODEL.fit([[15,6],[21,17],[89,9]],[21,38,98])# training the model with a very small dataset
print(f"SUM : {round(MODEL.predict([[int(input('Enter 1st number : ')),int(input('Enter 2nd number : '))]])[0],2)}")
# time taken : 1 minute 17 seconds(Excluding the time taken for writing the comments) [Developed by Omanshu]

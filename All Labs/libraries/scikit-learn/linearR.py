from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

x=[[1],[2],[3],[4],[5]]
y=[20,40,60,80,100]

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)

print("x_train", x_train)

model=LinearRegression()
model.fit(x_train,y_train)

y_pred=model.predict(x_test)
print("y_pred", y_pred)

mse=mean_squared_error(y_test,y_pred)
print(f'Mean Squared Error: {mse:.2f}')

print("slope", model.coef_)
print("intercept", model.intercept_)
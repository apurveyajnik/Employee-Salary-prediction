import pandas as pd
from math import sqrt
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.linear_model import LinearRegression

train = pd.read_excel('train.xlsx',sheetname=0)
#dropping id and salary
X_train = train.drop(['ID','Salary'],axis=1)

# keeping only numerical data
X_train = X_train._get_numeric_data()

y_train = train.Salary

print(y_train.shape)
print(X_train.shape)

clf = LinearRegression()
clf = clf.fit(X_train,y_train)


test = pd.read_excel('test.xlsx',sheetname=0)

X_test = test.drop(['ID','Salary'],axis=1)

X_test = X_test._get_numeric_data()
y_test = test.Salary

#r_sqr = clf.score(X_test,y_test)
y_pred = clf.predict(X_test)

#mae = mean_absolute_error(y_test,y_pred)
#mse = sqrt(mean_squared_error(y_test, y_pred))
#print(mse)

pd.DataFrame({'ID':test.ID,'Salary':y_pred}).to_excel('result1.xlsx',index=False)

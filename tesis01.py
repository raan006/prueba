from sklearn.datasets import make_regression
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split

X, y = make_regression(random_state=0)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

reg = GradientBoostingRegressor(random_state=0)

reg.fit(X_train, y_train)

reg.predict(X_test[1:])

reg.score(X_test, y_test)

print('\n')

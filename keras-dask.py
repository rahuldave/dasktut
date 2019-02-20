from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from dask_ml.model_selection import GridSearchCV
from dask.distributed import Client
from sklearn.externals import joblib


def simple_nn(hidden_neurons):
  model = Sequential()
  model.add(Dense(hidden_neurons, activation='relu', input_dim=30))
  model.add(Dense(1, activation='sigmoid'))
  model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
  return model

param_grid = {'hidden_neurons': [100, 200, 300]}
if __name__=='__main__':
	client = Client()
	cv = GridSearchCV(KerasClassifier(build_fn=simple_nn, epochs=100), param_grid)
	X, y = load_breast_cancer(return_X_y=True)
	X_train, X_test, y_train, y_test = train_test_split(X, y)
	with joblib.parallel_backend("dask", scatter=[X_train, y_train]):
		cv.fit(X_train, y_train)
	print(f'Best Accuracy for {cv.best_score_:.4} using {cv.best_params_}')

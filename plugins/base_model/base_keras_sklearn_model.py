from keras.models import Sequential 
from keras.layers import Dense 
from keras.layers import Dropout

from keras.wrappers.scikit_learn import KerasClassifier

from keras.optimizers import SGD

from keras.callbacks import ModelCheckpoint
from keras.callbacks import Callback

import numpy

import sklearn
from sklearn.cross_validation import StratifiedKFold
from sklearn.cross_validation import cross_val_score

class LossHistory(Callback):
    def on_train_begin(self, logs={}):
        self.losses = []

    def on_batch_end(self, batch, logs={}):
        self.losses.append(logs.get('loss'))


class BaseKerasModel(object):

    def load_data(self):
        seed = 7
        numpy.random.seed(seed) # Load the dataset
        dataset = numpy.loadtxt("pima-indians-diabetes.csv", delimiter=",") 
        X = dataset[:,0:8] 
        Y = dataset[:,8]
        return X, Y
    
    def create_model(self):
        # Define and Compile 
        model = Sequential()
        model.add(Dense(12, input_dim=8, init='uniform', activation='relu')) 
        model.add(Dense(8, init='uniform', activation='relu'))
        model.add(Dense(1, init='uniform', activation='sigmoid'))
        model.add(Dropout(0.2))
    
        sgd = SGD(lr=0.1, momentum=0.9, decay=0.0001, nesterov=True) # learning rate schedule
        model.compile(loss='binary_crossentropy', optimizer=sgd, metrics=['accuracy']) # Fit the model
        #model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy']) # Fit the model
        return model
    
    def init_model(self, method="single"):
        if method == "cross_val":
            model = KerasClassifier(build_fn=self.create_model, nb_epoch=150, batch_size=10)
        elif method == "single":
            model = self.create_model()
        return model
    
    def train_model(self, model, X, Y, method="single"):
        if method == "single":
            ## fit once:
            checkpoint = ModelCheckpoint('weights.{epoch:02d}-{acc:.2f}.hdf5', monitor='acc', save_best_only=False)
            history = LossHistory()
            callbacks_list = [checkpoint]
            callbacks_list = [checkpoint, history]
            history = model.fit(X, Y, nb_epoch=10, batch_size=10, callbacks=callbacks_list) # Evaluate the model
            scores = model.evaluate(X, Y)
            print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
            print history.history
        
        elif method == "cross_val":
            ## use cross_validation:
            kfold = StratifiedKFold(y=Y, n_folds=10, shuffle=True, random_state=seed)
            
            results = cross_val_score(model, X, Y, cv=kfold)
            print results
            results_mean = results.mean()
            print results_mean
    
    def process(self):
        X, Y = self.load_data()
        method = "single"
        model = self.init_model(method=method)
        self.train_model(model, X, Y, method=method)

    
def process_from_checkpoint():
    X, Y = load_data()
    method = "single"
    model = init_model(method=method)
    train_model(model, X, Y, method=method)


if "__main__" == __name__:
    haha = BaseKerasModel()
    haha.process()
    exit(0)

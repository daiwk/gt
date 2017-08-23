import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Merge, Reshape
from keras.layers import Embedding
from keras.layers import LSTM
import numpy as np

def multi_input_model(model):
    model_displayid = Sequential()
    embedding_size = 16
    max_displayid = 300000
    model_displayid.add(Embedding(max_displayid, output_dim=embedding_size, input_shape=(1,)))

    model_adid = Sequential()
    max_adid = 220000
    model_adid.add(Embedding(max_adid, output_dim=embedding_size, input_shape=(1,)))

    model_entityids = Sequential()
    max_entityid = 4000000
    model_entityids.add(Embedding(max_entityid, output_dim=embedding_size, input_shape=(10,)))

    model.add(Merge([model_displayid, model_adid, model_entityids], mode='concat', concat_axis=1))
    model.add(Dense(1, activation='sigmoid'))
    model.compile(loss='binary_crossentropy',
                  optimizer='rmsprop',
                  metrics=['accuracy'])


if __name__ == "__main__":
    # rand 300 training examples
    x_train_displayid = np.random.randint(30000,size=(300,1))
    x_train_adid = np.random.randint(220000,size=(300,1))
    x_train_entityids = np.random.randint(4000000,size=(300,10))
    y_train = np.random.randint(1,size=(300,1+1+10,1))
    print y_train.shape
    
    model = Sequential()
    multi_input_model(model)

   
    model.fit([x_train_displayid, x_train_adid, x_train_entityids], y_train, batch_size=16, epochs=10)
#    score = model.evaluate([x_test_1, x_test_2], y_test, batch_size=16)
#    print score

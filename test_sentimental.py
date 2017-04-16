'''Train a recurrent convolutional network on the stock news sentiment
classification task.

'''
import numpy as np
from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.layers import Embedding
from keras.layers import LSTM
from keras.layers import Convolution1D, MaxPooling1D
import pickle

# Embedding
max_features = 20001
maxlen = 100
embedding_size = 128

# Convolution
filter_length = 5
nb_filter = 64
pool_length = 4

# LSTM
lstm_output_size = 70

# Training
batch_size = 30
nb_epoch = 2

'''
Note:
batch_size is highly sensitive.
Only 2 epochs are needed as the dataset is very small.
'''

print('Loading data...')


XDATA = pickle.load(open('pickles/currnews/train_Xtrain_01.pickle','rb'))
yDATA = pickle.load(open('pickles/currnews/train_ytrain_01.pickle','rb'))
XDATA = XDATA+pickle.load(open('pickles/currnews/train_Xtrain_02.pickle','rb'))
yDATA = yDATA+pickle.load(open('pickles/currnews/train_ytrain_02.pickle','rb'))
XDATA = XDATA+pickle.load(open('pickles/currnews/train_Xtrain_03.pickle','rb'))
yDATA = yDATA+pickle.load(open('pickles/currnews/train_ytrain_03.pickle','rb'))

# uncomment this for spliting XDATA
# l_data = len(XDATA)
# print "Size of corpus: ",l_data
#
# train_size = 9*(l_data/10)
#
# print train_size
#
# X_train = XDATA[:train_size]
# X_test = XDATA[train_size:]
#
# y_train = yDATA[:train_size]
# y_test = yDATA[train_size:]

X_train = XDATA
X_test = pickle.load(open('pickles/currnews/train_Xtrain_04.pickle','rb'))

y_train = yDATA
y_test = pickle.load(open('pickles/currnews/train_ytrain_04.pickle','rb'))


print len(X_train),'training sequences'
print len(X_test),'testing sequences'

print('Pad sequences (samples x time)')
X_train = sequence.pad_sequences(X_train, maxlen=maxlen)
X_test = sequence.pad_sequences(X_test, maxlen=maxlen)
print('X_train shape:', X_train.shape)
print('X_test shape:', X_test.shape)

print('Build model...')

model = Sequential()
model.add(Embedding(max_features, embedding_size, input_length=maxlen))
model.add(Dropout(0.25))
model.add(Convolution1D(nb_filter=nb_filter,
                        filter_length=filter_length,
                        border_mode='valid',
                        activation='relu',
                        subsample_length=1))
model.add(MaxPooling1D(pool_length=pool_length))
model.add(LSTM(lstm_output_size))
model.add(Dense(1))
model.add(Activation('sigmoid'))

model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

print('Train...')
model.fit(X_train, y_train, batch_size=batch_size, nb_epoch=nb_epoch,
          validation_data=(X_test, y_test))
score, acc = model.evaluate(X_test, y_test, batch_size=batch_size)
print('\nTest score:', score)
print('Test accuracy:', acc)

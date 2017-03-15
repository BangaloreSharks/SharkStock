'''Train a recurrent convolutional network on the IMDB sentiment
classification task.

Gets to 0.8498 test accuracy after 2 epochs. 41s/epoch on K520 GPU.
'''
import numpy as np
np.random.seed(1337)  # for reproducibility

from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.layers import Embedding
from keras.layers import LSTM
from keras.layers import Convolution1D, MaxPooling1D
import pickle


# Embedding
max_features = 50000
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
X_train = pickle.load(open('pickles/news_index/X_train/WIKI_GE'))
y_train = pickle.load(open('pickles/news_index/y_train/WIKI_GE'))
print(len(X_train))
#-----------------------------------------------------
t = pickle.load(open('pickles/news_index/X_train/WIKI_AGN'))
y = pickle.load(open('pickles/news_index/y_train/WIKI_AGN'))
X_train = X_train + t
y_train = y_train + y
print len(t),len(y)
t = pickle.load(open('pickles/news_index/X_train/WIKI_BSRR'))
y = pickle.load(open('pickles/news_index/y_train/WIKI_BSRR'))
X_train = X_train + t
y_train = y_train + y
print len(t),len(y)
t = pickle.load(open('pickles/news_index/X_train/WIKI_MAN'))
y = pickle.load(open('pickles/news_index/y_train/WIKI_MAN'))
X_train = X_train + t
y_train = y_train + y
print len(t),len(y)
t = pickle.load(open('pickles/news_index/X_train/WIKI_MAR'))
y = pickle.load(open('pickles/news_index/y_train/WIKI_MAR'))
X_train = X_train + t
y_train = y_train + y
print len(t),len(y)
t = pickle.load(open('pickles/news_index/X_train/WIKI_REMY'))
y = pickle.load(open('pickles/news_index/y_train/WIKI_REMY'))
X_train = X_train + t
y_train = y_train + y
print len(t),len(y)
t = pickle.load(open('pickles/news_index/X_train/WIKI_XPO'))
y = pickle.load(open('pickles/news_index/y_train/WIKI_XPO'))
X_train = X_train + t
y_train = y_train + y
print len(t),len(y)

#-----------------------------------------------------

X_test = pickle.load(open('pickles/news_index/X_train/WIKI_NOC'))
y_test = pickle.load(open('pickles/news_index/y_train/WIKI_NOC'))


print(len(X_train), 'train sequences')
print(len(X_test), 'test sequences')
#
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
print('Test score:', score)
print('Test accuracy:', acc)

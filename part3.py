import pandas as pd
import numpy as np

from tensorflow.python.keras.preprocessing.text import Tokenizer
from tensorflow.python.keras.preprocessing.sequence import pad_sequences

from keras.models import Sequential
from keras.layers import Dense, Embedding, LSTM, GRU
from keras.layers.embeddings import Embedding

#actionable sentences
dfTrue = pd.read_csv("C:/Users/Nikhil/Desktop/actionItemDetection/finaloutputTrue.txt", sep="\n", header=None,error_bad_lines=False)
dfTrue.columns = ['sentences']
#not actionable sentences
dfFalse = pd.read_csv("C:/Users/Nikhil/Desktop/actionItemDetection/finaloutputFalse.txt", sep="\n", header=None,error_bad_lines=False)
dfFalse.columns = ['sentences']
#testing data set
dfTest = pd.read_csv("C:/Users/Nikhil/Desktop/actionItemDetection/train.csv", sep="|",error_bad_lines=False)


dfTest['is_actionitem'] = dfTest.is_actionitem.astype('str')
#print(dfTest.head(10))
dfTest['is_actionitem'] = dfTest['is_actionitem'].map({' True' : '1', ' False': '0'})
dfTest['is_actionitem'] = dfTest.is_actionitem.astype('object')
#print(dfTest.dtypes)
#print(dfTest.head())

#adding new column as 1
target = []
for i in range(len(dfTrue)):
    target.append("1")
dfTrue['outputval'] = target
#print(len(target))

#adding new column as 0
target = []
for i in range(len(dfFalse)):
    target.append("0")
#print(len(target))
dfFalse['outputval'] = target

#append two dataframes
df = dfTrue.append(dfFalse, ignore_index = True)    
#shuffle dataframe
df = df.sample(frac=1).reset_index(drop=True)
#print(df.head(10))
#print(df.shape)

x_train = df.sentences
x_test = dfTest.sentence
y_train = df.outputval
y_test = dfTest.is_actionitem

print("**************************")
print(x_train.head())
print(x_train.shape)
print("**************************")
print(x_test.head())
print(x_test.shape)
print("**************************")
print(y_train.head())
print(y_train.shape)
print("**************************")
print(y_test.head())
print(y_test.shape)


tokenizer_obj = Tokenizer()

abc = []
for i in x_train:
    abc.append(str(i))
x_train = abc

abc = []
for i in x_test:
    abc.append(str(i))
x_test = abc

total_reviews = x_train + x_test

abc = []
for i in total_reviews:
    abc.append(str(i))
total_reviews = abc

tokenizer_obj.fit_on_texts(x_train)
#print("#################")
#print(len(x_train),len(x_test),len(total_reviews))

# pad sequences
max_length = 30 # try other options like mean
# define vocabulary size
vocab_size = len(tokenizer_obj.word_index) + 1
#print("*************")
#print(vocab_size)

X_train_tokens =  tokenizer_obj.texts_to_sequences(x_train)
X_test_tokens = tokenizer_obj.texts_to_sequences(x_test)


#print("******X_train_tokens************")
#print(X_train_tokens[67])
#print(X_train_tokens[17])

#print(X_train_tokens[844])
#print(X_test_tokens[91])

#print(len(X_train_tokens))
#print(len(X_test_tokens))

X_train_pad = pad_sequences(X_train_tokens, maxlen=max_length, padding='post')
X_test_pad = pad_sequences(X_test_tokens, maxlen=max_length, padding='post')

EMBEDDING_DIM = 50

print('Build model...')

model = Sequential()
model.add(Embedding(vocab_size, EMBEDDING_DIM, input_length=max_length))
model.add(GRU(units=32,  dropout=0.2, recurrent_dropout=0.2))
model.add(Dense(1, activation='sigmoid'))

# try using different optimizers and different optimizer configs
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])



print('Summary of the built model...')
print(model.summary())


print('Train...')

print("******************")
print(X_train_pad.shape)
print(y_train.shape)


#training
model.fit(X_train_pad, y_train, batch_size=128, epochs=25, validation_data=(X_test_pad, y_test), verbose=2)

#testing
print('Testing...')
score, acc = model.evaluate(X_test_pad, y_test, batch_size=128)

print('Test score:', score)
print('Test accuracy:', acc)

print("Accuracy: {0:.2%}".format(acc))
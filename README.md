# actionItemDetection


part1.py
1. Read csv file into dataframe(read message data only)
2. Extract mail content only since we don't need any mail details
3. There is raw data in mail content other than simple sentences. Filter this raw data.
4. Using Nltk sentence tokenizer, split the email data paragraphs into sentences.
   Preprocessing:
   a.Remove the sentences which contains links, different symbols(like ~~~, ----, *****, >>, ==).
   b.Also remove sentences with has less than 3 words and greater than 25 words.
   Before preprocessing sentence count was 6627371 where as after preprocessing count is 3672744
5. Save this preprocessed sentences into a file.


Rules for actionable sentences:
1. Sentence start with VB(go,do,make)
2. Sentence start with VB_Phrase
		Examples of verb phrases:
		VB-Phrase: {<RB><VB>}          (carefully drive)
		VB-Phrase: {<UH><,>*<VB>}      (Bah ! go get) some work
		VB-Phrase: {<UH><,><VBP>}      (Great ! have fun)    
		VB-Phrase: {<NN.?>+<,>*<VB>}   (Virat, please mail) me the docs 
		VB-Phrase: {<DT><,>*<VB>}      (Just carefully listen)
                VB-Phrase: {<PRP><VB>}         (you stop) this
3. sentence starts with "please"
4. sentence containing "please" 


part2.py
1. Read data from a file which is created in part1.py
2. Classify sentences into true value(actionable) and false value(non-actionable) sentences according to rules described above.
3. For time being only 50000 sentences for each class has been classified.
4. Classified sentence data saved into two different files for true value(actionable) and false value(non-actionable) sentences.


part3.py
Following is the flow for objective 2:
1. Text data
2. Embedding
3. Deep Network(GRU)
4. Fully connected layer 
5. Output layer(sigmoid)
6. Final output

Summary of the built model...
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
embedding_3 (Embedding)      (None, 30, 50)            1673150   
_________________________________________________________________
gru_3 (GRU)                  (None, 32)                7968      
_________________________________________________________________
dense_3 (Dense)              (None, 1)                 33        
=================================================================
Total params: 1,681,151
Trainable params: 1,681,151
Non-trainable params: 0
_________________________________________________________________
None
Train...
******************
(98486, 30)
(98486,)
Train on 98486 samples, validate on 1520 samples
Epoch 1/25
 - 182s - loss: 0.3617 - acc: 0.7993 - val_loss: 0.7880 - val_acc: 0.7750
Epoch 2/25
 - 170s - loss: 0.0851 - acc: 0.9762 - val_loss: 0.9968 - val_acc: 0.7743



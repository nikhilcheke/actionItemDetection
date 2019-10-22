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
 


Rules for actionable sentences:
1. Sentence start with MD(can,could)
2. Sentence start with VB(go,do,make)
3. Sentence start with VB_Phrase
		Examples of verb phrases:
		VB-Phrase: {<RB><VB>}          (carefully drive)
		VB-Phrase: {<UH><,>*<VB>}      (Bah ! go get) some work
		VB-Phrase: {<UH><,><VBP>}      (Great ! have fun)    
		VB-Phrase: {<NN.?>+<,>*<VB>}   (Virat, please mail) me the docs 
		VB-Phrase: {<DT><,>*<VB>}      (Just carefully listen)
4. sentence starts with "please"
5. sentence containing "please" 



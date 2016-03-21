# JEECUnbabelChallenge
Participation on the JEEC Unbabel Challenge.

At [JEEC16](http://jeec.tecnico.pt/jeec16/) (a Electrical and Computer Engineering event organized by the student at [Técnico](tecnico.ulisboa.pt)) [Unbabel](https://unbabel.com/) went to give a talk and proposed a challenge to the students attendine. We (João Almeida and Ricardo Martins) decided to participate, this repository contains all the work we did during the 11-day Challenge, from 11/03/2016 to 21/03/2016.

####Goal: 
Create a ML classifier to distinguish between machine translations and human translations.

####Data Used:
The available dataset consisted of about [20K labeled phrases](https://github.com/Joao-M-Almeida/JEECUnbabelChallenge/blob/master/Data/OficialData/training.txt). And the final test set of [3220 phrases to classify](https://github.com/Joao-M-Almeida/JEECUnbabelChallenge/blob/master/Data/OficialData/test_blind.txt).

####Scripts:

- [FeatureGen](https://github.com/Joao-M-Almeida/JEECUnbabelChallenge/blob/master/Scripts/FeatureGen.ipynb): Script to calculate Handmade features created with the intention to find translater errors;
- [ClassifiersTest](https://github.com/Joao-M-Almeida/JEECUnbabelChallenge/blob/master/Scripts/ClassifiersTest.ipynb): Script to test different classifiers on the training data and then fine tune their parameters. Created from the template at [DataScienceTools](https://github.com/Joao-M-Almeida/DataScienceTools);
- [ClassifyTestSet](https://github.com/Joao-M-Almeida/JEECUnbabelChallenge/blob/master/Scripts/ClassifyTestSet.ipynb): Script to train the final classifier and generate the predictions for the test set;
- [ProcessTextIntoSamples](https://github.com/Joao-M-Almeida/JEECUnbabelChallenge/blob/master/Scripts/ProcessTextIntoSamples.ipynb): Script to transform external text into usable text samples;
- [PostTag](https://github.com/Joao-M-Almeida/JEECUnbabelChallenge/blob/master/Scripts/post_tag.py): Set of functions to convert phrases into a n-gram POS tagged representation of the text;
- [FirstTests](https://github.com/Joao-M-Almeida/JEECUnbabelChallenge/blob/master/Scripts/First_tests.ipynb): Mix of testing and POS tagging; **TODO:** clean up;

####Approach:
- **TODO**: Explain approach.

####Final Result:
  Voting Classifier based on LDA, LogisticRegression and AdaBoost, cross validation score of (55.0 +/- 1.6)% .

#####Packages required:
- [Jupyter Notebook](http://jupyter.org/)
- [Pandas](http://pandas.pydata.org/)
- [Scikit-learn](http://scikit-learn.org/)
- [SciPy](http://www.scipy.org/)
- [NumPy](http://www.numpy.org/)
- [NLTK](http://www.nltk.org/)

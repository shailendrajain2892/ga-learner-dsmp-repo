### Project Overview

 This dataset was generated using HRSC nadir panchromatic image h0905_0000 taken by the Mars Express spacecraft. The images is located in the Xanthe Terra, centered on Nanedi Vallis and covers mostly Noachian terrain on Mars. The image had a resolution of 12.5 meters/pixel.

Problem statement
Determine if the instance is a crater or not a crater. 1=Crater, 0=Not Crater


### Learnings from the project

 we should try all the possilble classifier on the dataset and check its score. To determine which classifier gives the best score for our dataset. 


### Approach taken to solve the problem

 1. Load the dataset, splitted the data into train and test
2. Applied simple Logistic regression model and checked its score
3. Applied Decison Tree model, cheked and compared its score with previous classifer to determine wheter this classifire provides better preformance or not
3. Applied Random forest model, cheked and compared its score with previous classifer to determine wheter this classifire provides better preformance or not
4. Applied Bagging and Voting classifire as well, cheked and compared their score with previous classifer to determine wheter this classifire provides better preformance or not
5. After apply all the models, found out Random Forest classifier gives best result


### Challenges faced

 - Challenge - performance was not up to the mark with simple logistic regression model 
- Solution - applied different classifiers to improve its performance



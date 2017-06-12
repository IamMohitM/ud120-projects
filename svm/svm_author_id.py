#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess

from sklearn import svm
from sklearn.metrics import accuracy_score
### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels

features_train, features_test, labels_train, labels_test = preprocess()

clf=svm.SVC(C=10000,kernel="rbf")
###Here we're training it with a smaller dataset. Smaller datasets decrease the accuracy
#features_train = features_train[:len(features_train)/100]
#labels_train = labels_train[:len(labels_train)/100]
t0 = time()
clf.fit(features_train,labels_train)
print "training time:", round(time()-t0, 3), "s"
t0 = time()
pred=clf.predict(features_test)
print "Predicting time:", round(time()-t0, 3), "s"
count=0
for p in pred:
    if(p==1):
        count+=1

print count

#print accuracy_score(pred,labels_test)



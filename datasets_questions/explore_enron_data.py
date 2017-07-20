#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""
def greatest(a1, a, b1, b):
    if(a>b):
        return a1,a
    else:
        return b1,b

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
# names = pickle.load(open("../final_project/poi_names.txt", "rb"))

keys=enron_data.keys()
# print names
print enron_data
print len(enron_data[keys[0]])

#print enron_data


#print keys
# b1,b=greatest("COLWELL WESLEY", enron_data["COLWELL WESLEY"]["total_payments"],"FASTOW ANDREW S",enron_data["FASTOW ANDREW S"]["total_payments"])
# print b1,b
# print greatest("SKILLING JEFFREY K", enron_data["SKILLING JEFFREY K"]["total_payments"],b1,b)
#print enron_data["FASTOW ANDREW S"]["total_payments"]
count=0
c=0
#COLWELL WESLEY
for k in keys:
     if(enron_data[k]["poi"]==True):
        c+=1
        if(enron_data[k]["total_payments"]=="NaN"):
            count+=1
    # if (enron_data[k]["email_address"] != "NaN"):
    #     c+= 1

#print p
# for k in keys:
#    if(enron_data[k]["total_payments"]=="NaN"):
#        count+=1

#print len(enron_data)
print count
print c
#print ((count+10)*100)/146

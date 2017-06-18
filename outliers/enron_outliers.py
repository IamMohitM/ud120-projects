#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

def greatest(a, b):
    if(b=="NaN"):
        b=0
    if(a>b):
        return a
    else:
        return b
### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]
data_dict.pop("TOTAL",0) #Because the sum of the values(training data) shouldn't be included.
data = featureFormat(data_dict, features)
print data_dict
keys=data_dict.keys()
max_sal=data_dict[keys[0]]["salary"]
max_bon=data_dict[keys[0]]["bonus"]
key_sal=keys[0]
key_bon=keys[0]
# for k in keys:
#     max_sal=greatest(max_sal,data_dict[k]["salary"])
#     if(max_sal==data_dict[k]["salary"]):
#         key_sal=k
#     max_bon=greatest(max_bon,data_dict[k]["bonus"])
#     if(max_bon==data_dict[k]["bonus"]):
#         key_bon=k
names=[]

for k in keys:
    if( data_dict[k]["salary"]=="NaN"):
        continue
    if(data_dict[k]["salary"]>1000000):
        names.append([k,data_dict[k]["salary"]])

print "names is", names
print len(names)
#print "Count is",count
print "Length is",len(data_dict)
# print max_sal
# print key_sal
# print max_bon
# print key_bon

#print data_dict[key_sal]
for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()
### your code below




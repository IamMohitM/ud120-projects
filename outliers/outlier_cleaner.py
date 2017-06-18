# !/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where
        each tuple is of the form (age, net_worth, error).
    """
    # print predictions,ages,net_worths

    per = (len(predictions)) - (len(predictions)/10)
    print per
    cleaned_data = []
    print predictions
    for p in range(0, per, 1):
        a=(predictions[p], ages[p], net_worths[p])
        print "a is ",a
        cleaned_data.append(a)

    print "cleaned data is, ",cleaned_data,len(cleaned_data)
    ### your code goes here
    return cleaned_data


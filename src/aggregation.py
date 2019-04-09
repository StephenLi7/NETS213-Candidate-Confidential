############################################################
# NETS 213: FINAL PROJECT AGGREGATION
############################################################

import pandas as pd
from collections import Counter


def aggregate_important(mturk_res):

    labels = []
    counts = Counter()

    for index,row in mturk_res.iterrows():
        for i in range(1, 5):
            important = row['Answer._' + str(i)]
            counts[important] += 1

    for count in counts:
        newTuple = (count,counts[count])
        labels.append(newTuple)

    return labels

def sort_by_importance(tuples):
    tuples_sorted = sorted(tuples, key=lambda x: x[1])
    topics = []
    for tuple in tuples_sorted:
        topic = tuple[0]
        topics.add(topic)

    return topics



#


# Your main function

def main():
    # Read in CVS result file with pandas
    # PLEASE DO NOT CHANGE
    mturk_res = pd.read_csv('data.csv')
    tuples = aggregate_important(mturk_res)
    list = sort_by_importance(tuples)
    print(list)




    # Call functions and output required CSV files

if __name__ == '__main__':
    main()

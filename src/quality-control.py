############################################################
# NETS 213: FINAL PROJECT QUALITY CONTROL
############################################################

import pandas as pd


#Adds a score column to the data file that includes the worker's score for the predetermined gold-standard questions
def determine_score(mturk_res):
    worker_scores = [];
    for x in mturk_res.index:
        worker_score = 0;
        gold_score1 = mturk_res.loc(x, Input.val1); # example target: 7-9
        gold_score1_min = 7;
        gold_score1_max = 9;
        gold_score2 = mturk_res.loc(x, Input.val5); # example target: 2-4
        gold_score2_min = 2;
        gold_score2_max = 4;
        gold_score3 = mturk_res.loc(x, Input.val8); # example target: 7-9
        gold_score3_min = 7;
        gold_score3_max = 9;
        if gold_score1 >= gold_score1_min and gold_score1 <= gold_score1_max:
            worker_score += 1;
        elif gold_score1 < gold_score1_min:
            if (gold_score1_min - gold_score1) > 1:
                worker_score -= 1;
            else:
                continue;
        elif gold_score1 > gold_score1_max:
            if (gold_score1 - gold_score1_max) > 1:
                worker_score -= 1;
            else:
                continue;
        if gold_score2 >= gold_score2_min and gold_score2 <= gold_score2_max:
            worker_score += 1;
        elif gold_score2 < gold_score2_min:
            if (gold_score2_min - gold_score2) > 1:
                worker_score -= 1;
            else:
                continue;
        elif gold_score2 > gold_score2_max:
            if (gold_score2 - gold_score2_max) > 1:
                worker_score -= 1;
            else:
                continue;
        if gold_score3 >= gold_score3_min and gold_score3 <= gold_score3_max:
            worker_score += 1;
        elif gold_score3 < gold_score3_min:
            if (gold_score3_min - gold_score3) > 1:
                worker_score -= 1;
            else:
                continue;
        elif gold_score3 > gold_score3_max:
            if (gold_score3 - gold_score3_max) > 1:
                worker_score -= 1;
            else:
                continue;
         
        worker_scores[x] = worker_score; 
    mturk_res[gold_score] = worker_scores;
    return mturk_res;
 
def main():
    mturk_res = pd.read_csv('data.csv')
    mturk_res = determine_score(mturk_res)
 
if __name__ == '__main__':
    main()
    
                
                
                
           
        

import math 

def caculate_f1_score(tp, fp, fn):
    inputs = {'tp' : tp,'fp' : fp, 'fn' : fn }
    are_all_positive = True
    for i, value in inputs.items():
        if not isinstance(value, int):
            print(f'{i} must be int')
            return
        if value <= 0:
            are_all_positive = False
    if not are_all_positive:
        print('tp and fp and fn must be greater than zero')
        return

    # Caculate Precision, Recall, and F1-Score
    precision   = tp/(tp + fp)
    recall      = tp/(tp + fn)
    f1_score    = 2*(precision * recall)/(precision + recall)

    # Print results
    print('Precision is', precision)
    print('Recall is'   , recall)
    print('F1-Score is' , f1_score)
    
tp = int(input())
fp = int(input())
fn = int(input())
caculate_f1_score(tp, fp, fn)
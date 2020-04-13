# venus
1. system: involving several def-function related to backtest(generate a postion、test its return rate...)
2. dg(cython form for datagenerate): alternative way to create derivative data from original data(while some famous derivative data like
   KD value、revenue's yoy...have already been calculated and restored as npy film,and thus don't need to use 'dg')
3. answer: where we revise filter for position-generating、show the dashboard of strategy imported.

other:
1. test: used for testing whether datagenerate work or not.
2. viewnpy: check whether the npy film we create is consistent with true data. 

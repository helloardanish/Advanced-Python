"""
Problem :
PredictingaFingerCount 

A little girl counts from 1 to 1000 using the ﬁngers of her left hand as follows.
She starts by calling her thumb 1,the ﬁrstﬁnger 2,middleﬁnger 3, ringﬁnger 4,and littleﬁnger 5.
Then she reverses direction,calling the ring ﬁnger 6, middleﬁnger 7, the ﬁrst ﬁnger 8,and her thumb 9,after which she calls her ﬁrst ﬁnger
10, and so on. If she continues to count in this manner, on which ﬁnger will she stop?
"""

N = int(input())
Ans = N % 8
if Ans == 1:
    print('Thumb')
elif Ans == 2 or Ans == 0:
    print('First finger')
elif Ans == 3 or Ans == 7:
    print('Middle finger')
elif Ans == 4 or Ans == 6:
    print('Ring finger')
else:
    print('Little finger')

'''
Created on 4 Nov 2015

@author: Lilian Blot
'''

def maxHeartRate(age):
    return int(208 - 0.7 * age)

INTERVAL        = 'Interval Training'
AEROBIC         = 'Aerobic Training'
THRESHOLD       = 'Threshold Training' 
COUCH_PATATOE   = 'Couch Training'

def zone(age,rate):
    maxRate = maxHeartRate(age)
    if(rate < 0.5 * maxRate):
        return COUCH_PATATOE
    elif (0.5 * maxRate <= rate < 0.7 * maxRate):
        return AEROBIC
    elif (0.7 * maxRate <= rate < 0.9 * maxRate):
        return THRESHOLD
    else:
        return INTERVAL
    

def main():
    for age in range(15,90, 5):
        print(" max heart rate per minute at %2d years old is %3d beats per minute."%(age,maxHeartRate(age)))
        
main()
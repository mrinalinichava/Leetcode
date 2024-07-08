'''
leetcode : https://leetcode.com/problems/merge-intervals/description/
'''

def mergeIntervals(intervals):
    intervals.sort(key = lambda x:x[0])
    output = []

    print(intervals)
    for interval in intervals:
        if(not output or output[-1][1]<interval[0]):
            output.append(interval)
        else:
            output[-1][1]= max(output[-1][1],interval[1])
    return output

intervals = [[1,3],[8,10],[15,18],[2,6]]
print(mergeIntervals(intervals))
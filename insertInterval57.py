
def insert(intervals, newInterval) -> list:
    res = []

    for i in range(len(intervals)):
        print('i', i)
        print('newInterval[1] < intervals[i][0]', newInterval[1] < intervals[i][0], 'newInterval[1]', newInterval[1], 'intervals[i][0]', intervals[i][0])
        print('newInterval[0] > intervals[i][1]', newInterval[0] > intervals[i][1], 'newInterval[0] ', newInterval[0], 'intervals[i][1]', intervals[i][1])
        if newInterval[1] < intervals[i][0]:
            res.append(newInterval)
            print('res + intervals[i:]', res + intervals[i:], 'res', res, 'intervals[i:]', intervals[i:])
            return res + intervals[i:]

        elif newInterval[0] > intervals[i][1]:
            print('intervals[i]', intervals[i])
            res.append(intervals[i])
            print('res', res)
        else:
            print('min(newInterval[0], intervals[i][0])', min(newInterval[0], intervals[i][0]), 'max(newInterval[1], intervals[i][1])', max(newInterval[1], intervals[i][1]))
            print('newInterval[0]', newInterval[0], 'intervals[i][0]', intervals[i][0])
            print('newInterval[1]', newInterval[1], 'intervals[i][1]', intervals[i][1])
            newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
            print('newInterval', newInterval)
    res.append(newInterval)
    print('res', res)
    return res


intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]

print(insert(intervals, newInterval))


def merge(intervals) -> list:
    intervals.sort(key = lambda i : i[0])
    print('sort intervals:', intervals)
    output = [intervals[0]]

    print('output', output)

    for start, end in intervals[1:]:
        print('start:', start, 'end:', end)
        lastEnd = output[-1][1]
        print('lastEnd = output[-1][1]', lastEnd)
        print('is start <= lastEnd', start <= lastEnd)
        if start <= lastEnd:
            print('lastEnd: ', lastEnd, 'end: ', end)
            output[-1][1] = max(lastEnd, end)
            print('output[-1][1]', output[-1][1])
        else:
            print('start and end', start, end)
            output.append([start, end])
            print('output11111', output)
    print('output22222', output)
    return output


intervals = [[2,6], [1,3], [15,18], [8,10]]
print(merge(intervals))
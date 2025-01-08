function merge(intervals) {
    intervals.sort((a, b) => a[0] - b[0]);
    let results = [intervals[0]]

    for (const [start, end] of intervals) {
        let lastEnd = results[results.length-1][1]
        if (lastEnd >= start) {
            results[results.length-1][1] = Math.max(lastEnd, end);
        }else {
            results.push([start, end])
        }
    }
    return results
}

let intervals = [[2,6], [1,3], [15,18], [8,10]];
console.log(merge(intervals))
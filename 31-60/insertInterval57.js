function insertInterval(intervals, newInterval) {
    let res = []
    for (let i = 0; i < intervals.length; i++) {
        if (newInterval[0] > intervals[i][1]) res.push(intervals[i]);
        else if (newInterval[1] < intervals[i][0]) {
            res.push(newInterval);
            return res.concat(intervals.slice(i));
        }
        else newInterval = [Math.min(newInterval[0], intervals[i][0]), Math.max(newInterval[1], intervals[i][1])];
    }
    res.push(newInterval);
    return res;
}

let intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]];
let newInterval = [4,8]

console.log(insertInterval(intervals, newInterval))
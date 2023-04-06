/**
 * @param {number[][]} intervals
 * @return {number[][]}
 */
var merge = function(intervals) {
    if (!intervals || !intervals.length) {
        return [];
    }
    intervals.sort((a, b) => {
        return a[0] - b[0]
    });    
    let res = [intervals[0]];

    
    for (let i = 1; i < intervals.length; i++) {
        let start1 = res[res.length - 1][0];
        let end1 = res[res.length - 1][1];
        let start2 = intervals[i][0];
        let end2 = intervals[i][1];
        
        if (end1 >= start2) {
            res[res.length - 1] = [start1, Math.max(end1, end2)];
        } else {
            res.push(intervals[i]);
        }
    }
    
    return res;    
};

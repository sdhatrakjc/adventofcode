"use strict";
exports.__esModule = true;
var fs = require("fs");
var input = fs.readFileSync('./2022/day4/input.txt', 'utf-8')
    .trim()
    .split('\n');
/*
    Fully Overlap :
    1. Left[1] <= Right[1] && Left[0] >= Right[0]
    2. Right[1] <= Left[1] && Right[0] >= Left[0]

    Partial overlap :
    3. Left[0] <= Right[1] && Right[1] <= Left[1]
    4. Left[0] <= Right[0] && Right[0] <= Left[1]
*/
var result1 = 0;
var result2 = 0;
input.forEach(function (el, i) {
    var ranges = el.split(",").map(function (n) { return n.split("-").map(function (x) { return parseInt(x); }); });
    if (ranges[0][1] <= ranges[1][1] && ranges[0][0] >= ranges[1][0]) {
        result1++;
        result2++;
    }
    else {
        if (ranges[1][1] <= ranges[0][1] && ranges[1][0] >= ranges[0][0]) {
            result1++;
            result2++;
        }
        else {
            // Else part for result 2 (To include partial overlap)
            if (ranges[0][0] <= ranges[1][1] && ranges[1][1] <= ranges[0][1]) {
                result2++;
            }
            else {
                if (ranges[0][0] <= ranges[1][0] && ranges[1][0] <= ranges[0][1]) {
                    result2++;
                }
            }
        }
    }
});
console.log("Result part 1", result1);
console.log("Result part 2", result2);

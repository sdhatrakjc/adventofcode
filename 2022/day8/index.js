"use strict";
exports.__esModule = true;
var fs_1 = require("fs");
var input = (0, fs_1.readFileSync)('./2022/day8/input.txt', "utf-8").toString().split("\n");
input.pop();
// part 1
function isVisible(x, y) {
    var h = input[y][x];
    var visible = true;
    for (var x2 = x - 1; x2 >= 0; x2--) {
        if (input[y][x2] >= h) {
            visible = false;
            break;
        }
    }
    if (visible)
        return true;
    visible = true;
    for (var x2 = x + 1; x2 < input[0].length; x2++) {
        if (input[y][x2] >= h) {
            visible = false;
            break;
        }
    }
    if (visible)
        return true;
    visible = true;
    for (var y2 = y - 1; y2 >= 0; y2--) {
        if (input[y2][x] >= h) {
            visible = false;
            break;
        }
    }
    if (visible)
        return true;
    visible = true;
    for (var y2 = y + 1; y2 < input.length; y2++) {
        if (input[y2][x] >= h) {
            visible = false;
            break;
        }
    }
    return visible;
}
var visible = 0;
for (var x = 0; x < input.length; x++) {
    for (var y = 0; y < input[0].length; y++) {
        if (isVisible(x, y))
            visible++;
    }
}
console.log("Result part 1", visible);
// part 2
function scenicScore(x, y) {
    var h = input[y][x];
    var left = 0;
    for (var x2 = x - 1; x2 >= 0; x2--) {
        left++;
        if (input[y][x2] >= h)
            break;
    }
    var right = 0;
    for (var x2 = x + 1; x2 < input[0].length; x2++) {
        right++;
        if (input[y][x2] >= h)
            break;
    }
    var up = 0;
    for (var y2 = y - 1; y2 >= 0; y2--) {
        up++;
        if (input[y2][x] >= h)
            break;
    }
    var down = 0;
    for (var y2 = y + 1; y2 < input.length; y2++) {
        down++;
        if (input[y2][x] >= h)
            break;
    }
    return left * right * up * down;
}
var maxScore = -Infinity;
for (var x = 1; x < input.length - 1; x++) {
    for (var y = 1; y < input[0].length - 1; y++) {
        var score = scenicScore(x, y);
        if (score > maxScore)
            maxScore = score;
    }
}
console.log("Result part 2", maxScore);

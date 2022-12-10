"use strict";
exports.__esModule = true;
var fs = require("fs");
var input = fs.readFileSync('./2022/day03/input.txt', 'utf-8')
    .trim()
    .split('\n');
var result1 = 0;
input.forEach(function (el, i) {
    var r1 = el.slice(0, el.length / 2);
    var r2 = el.slice(el.length / 2);
    var item = checkTwoRuckSacks(r1, r2).split('')[0];
    result1 += calculateSum(item);
});
console.log("Result part 1", result1);
var result2 = 0;
for (var i = 0; i < input.length; i += 3) {
    var ruckSacks = [input[i], input[i + 1], input[i + 2]];
    var item = checkItems(ruckSacks)[0];
    result2 += calculateSum(item);
}
console.log("Result part 1", result2);
function checkItems(ruckSacks) {
    var lastItems = ruckSacks[0];
    for (var i = 1; i < ruckSacks.length; i++) {
        lastItems = checkTwoRuckSacks(lastItems, ruckSacks[i]);
    }
    return lastItems;
}
function calculateSum(item) {
    var sub = 96;
    if (item === item.toUpperCase())
        sub = 38;
    return item.charCodeAt(0) - sub;
}
function checkTwoRuckSacks(r1, r2) {
    var items = [];
    var _loop_1 = function (item) {
        if (r2.split('').some(function (item2) { return item === item2; })) {
            if (!items.includes(item))
                items.push(item);
        }
    };
    for (var _i = 0, _a = r1.split(''); _i < _a.length; _i++) {
        var item = _a[_i];
        _loop_1(item);
    }
    return items.join('');
}

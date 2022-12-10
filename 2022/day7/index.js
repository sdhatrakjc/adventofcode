"use strict";
var _a;
exports.__esModule = true;
var fs_1 = require("fs");
var input = (0, fs_1.readFileSync)('./2022/day7/input.txt', "utf-8").toString().split(/\r?\n/);
input.pop();
var path = [];
var sizes = new Map();
for (var _i = 0, input_1 = input; _i < input_1.length; _i++) {
    var l = input_1[_i];
    if (l.startsWith('$ cd')) {
        var d = l.substring(5);
        if (d === '/') {
            path = [];
        }
        else if (d === '..') {
            path.pop();
        }
        else {
            path.push(d);
        }
    }
    else if (!l.startsWith('$')) {
        var s = l.split(" ")[0];
        if (s != "dir") {
            for (var i = 0; i <= path.length; i++) {
                var p = '/' + path.slice(0, i).join('/');
                sizes.set(p, Number(s) + ((_a = sizes.get(p)) !== null && _a !== void 0 ? _a : 0));
            }
        }
    }
}
// part 1
var result1 = Array.from(sizes.values())
    .filter(function (v) { return v <= 100000; })
    .reduce(function (x, y) { return x + y; }, 0);
console.log("Result part 1", result1);
// part 2
var needed = sizes.get('/') - 40000000;
var result2 = Math.min.apply(Math, Array.from(sizes.values()).filter(function (v) { return v >= needed; }));
console.log("Result part 2", result2);

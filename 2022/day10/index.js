"use strict";
exports.__esModule = true;
var fs_1 = require("fs");
var input = (0, fs_1.readFileSync)('./2022/day10/input.txt', "utf-8").toString().split("\n");
input.pop();
var x = 1;
var res = [];
input.forEach(function (el) {
    var command = el.split(" ");
    res.push(x);
    if (command[0] === "addx") {
        res.push(x);
        x += Number(command[1]);
    }
});
var signalStrength = 0;
for (var i = 19; i < res.length; i += 40) {
    signalStrength += res[i] * (i + 1);
}
console.log("Result part 1", signalStrength);
var row = "";
for (var i = 0; i < res.length; i++) {
    if (Math.abs((i % 40) - res[i]) <= 1) {
        console.log(Math.abs((i % 40)), res[i]);
        row += "#";
    }
    else {
        row += ".";
    }
    // New cycle
    if (i % 40 == 39) {
        console.log(row);
        row = "";
    }
}

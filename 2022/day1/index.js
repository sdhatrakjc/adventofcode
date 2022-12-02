"use strict";
exports.__esModule = true;
var fs = require("fs");
var input = fs.readFileSync('./2022/day1/input.txt', 'utf-8')
    .trim()
    .split('\n');
var elveCalories = [0];
input.forEach(function (el) {
    if (el !== '') {
        elveCalories[elveCalories.length - 1] += parseInt(el);
    }
    else {
        elveCalories.push(0);
    }
});

// Part 1 : find the max value in elveCalories
var maxCalories = Math.max.apply(Math, elveCalories);
console.log("Result part 1", maxCalories);

// Part 2 : get the sum of the top three carriers
var caloriesTopThreeElves = elveCalories.sort(function (a, b) { return b - a; }).slice(0, 3).reduce(function (a, b) { return a + b; });
console.log("Result part 2", caloriesTopThreeElves);

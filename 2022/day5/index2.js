"use strict";
exports.__esModule = true;
exports.x = void 0;
var fs = require("fs");
exports.x = "";
var Stack = /** @class */ (function () {
    function Stack() {
        this.items = [];
    }
    Stack.prototype.push = function (item) {
        this.items.push(item);
    };
    Stack.prototype.pushBack = function (item) {
        this.items.unshift(item);
    };
    Stack.prototype.pop = function () {
        return this.items.pop();
    };
    Stack.prototype.peek = function () {
        return this.items[this.items.length - 1];
    };
    return Stack;
}());
var input = fs.readFileSync('./2022/day5/input.txt', 'utf-8')
    .split('\n\n');
var stackCount = Math.ceil(input[0].split('\n')[0].length / 4);
var stacks = [];
for (var i = 0; i < stackCount; ++i) {
    var stack = new Stack();
    stacks.push(stack);
}
var starting = input[0].trimEnd().split('\n');
for (var _i = 0, starting_1 = starting; _i < starting_1.length; _i++) {
    var line = starting_1[_i];
    var crates = new Array().fill("", stackCount);
    var j = 0;
    for (var i = 0; i < line.length; i += 4) {
        var crate = line.slice(i, i + 4)[1];
        crates[j] = line.slice(i, i + 4)[1];
        if (crate !== " ") {
            stacks[j].pushBack(crate);
        }
        ++j;
    }
}
var instructions = input[1].trimEnd().split('\n');
// Part 2 
var result2;
for (var _a = 0, instructions_1 = instructions; _a < instructions_1.length; _a++) {
    var instruction = instructions_1[_a];
    var line = instruction.split(' ');
    var count = parseInt(line[1]);
    // need to adjust the indexing
    var start = parseInt(line[3]) - 1;
    var end = parseInt(line[5]) - 1;
    var tempStack = new Stack();
    for (var i = 0; i < count; ++i) {
        tempStack.push(stacks[start].pop());
    }
    for (var i = 0; i < count; ++i) {
        stacks[end].push(tempStack.pop());
    }
}
result2 = stacks.map(function (s) { return s.peek(); }).join('');
console.log("Result part 2", result2);

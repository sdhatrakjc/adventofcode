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
var input = fs.readFileSync('./2022/day05/input.txt', 'utf-8')
    .split('\n\n');
var stackCount = Math.ceil(input[0].split('\n')[0].length / 4);
var stacks = [];
for (var i = 0; i < stackCount; ++i) {
    // Part 1 
    var stack1 = new Stack();
    stacks.push(stack1);
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
// Part 1
var result1;
var stacks1 = Object.assign({}, stacks);
// Part 2 
var result2;
var stacks2 = stacks;
for (var _a = 0, instructions_1 = instructions; _a < instructions_1.length; _a++) {
    var instruction = instructions_1[_a];
    var line = instruction.split(' ');
    var count = parseInt(line[1]);
    var start = parseInt(line[3]) - 1;
    var end = parseInt(line[5]) - 1;
    for (var i = 0; i < count; ++i) {
        stacks1[end].push(stacks1[start].pop());
    }
}
for (var _b = 0, instructions_2 = instructions; _b < instructions_2.length; _b++) {
    var instruction = instructions_2[_b];
    var line = instruction.split(' ');
    var count = parseInt(line[1]);
    // need to adjust the indexing
    var start = parseInt(line[3]) - 1;
    var end = parseInt(line[5]) - 1;
    // there is probably a better way, but this was super fast to implement
    var tempStack = new Stack();
    for (var i = 0; i < count; ++i) {
        tempStack.push(stacks2[start].pop());
    }
    for (var i = 0; i < count; ++i) {
        stacks2[end].push(tempStack.pop());
    }
}
result1 = stacks1.map(function (s) { return s.peek(); }).join('');
console.log("Result part 1", result1);
result2 = stacks2.map(function (s) { return s.peek(); }).join('');
console.log("Result part 1", result2);

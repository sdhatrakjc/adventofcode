"use strict";
var __spreadArray = (this && this.__spreadArray) || function (to, from, pack) {
    if (pack || arguments.length === 2) for (var i = 0, l = from.length, ar; i < l; i++) {
        if (ar || !(i in from)) {
            if (!ar) ar = Array.prototype.slice.call(from, 0, i);
            ar[i] = from[i];
        }
    }
    return to.concat(ar || Array.prototype.slice.call(from));
};
exports.__esModule = true;
var fs_1 = require("fs");
var input = (0, fs_1.readFileSync)('./2022/day6/input.txt', "utf-8").toString().split("");
var findMarker = function (distinctChars) {
    return (input
        .map(function (_, index) { return input.slice(index, index + distinctChars); })
        .findIndex(function (stream) {
        return stream.every(function (char, index) {
            var copyDataStream = __spreadArray([], stream, true);
            copyDataStream.splice(index, 1);
            if (copyDataStream.includes(char))
                return false;
            return true;
        });
    }) + distinctChars);
};
console.log("Result part 1", findMarker(4));
console.log("Result part 2", findMarker(14));

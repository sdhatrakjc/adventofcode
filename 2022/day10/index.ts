import { readFileSync } from 'fs';

const input = readFileSync('./2022/day10/input.txt', "utf-8").toString().split("\n")
input.pop()

let x = 1
const res : number[] = []
input.forEach(el => {
    let command: string[] = el.split(" ")
    res.push(x)
    if (command[0] === "addx"){
        res.push(x)
        x += Number(command[1])
    }
});

let signalStrength = 0
for (let i = 19; i < res.length; i+=40){
    signalStrength += res[i] *(i+1)
}
console.log(`Result part 1`, signalStrength);

let row = ""
for (let i = 0; i < res.length; i++) {
    if (Math.abs((i % 40) - res[i]) <= 1) {
        console.log(Math.abs((i % 40)), res[i])
        row += "#"
    } else {
        row += "."
    }

    // New cycle
    if (i % 40 == 39) {
        console.log(row)
        row = ""
    }
}

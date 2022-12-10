import { readFileSync } from 'fs';

const input = readFileSync('./2022/day07/input.txt', "utf-8").toString().split(/\r?\n/);
input.pop()

let path: string[] = []
const sizes = new Map<string, number>()
for (const l of input) {
    if (l.startsWith('$ cd')) {
        const d = l.substring(5)
        if (d === '/') {
            path = []
        } else if (d === '..') {
            path.pop()
        } else {
            path.push(d)
        }
    } else if (!l.startsWith('$')) {
        const [s] = l.split(" ")
        if (s != "dir") {
            for (let i = 0; i <= path.length; i++) {
                const p = '/' + path.slice(0, i).join('/')
                sizes.set(p, Number(s) + (sizes.get(p) ?? 0))
            }
        }
    }
}

// part 1
let result1 = Array.from(sizes.values())
    .filter(v => v <= 100000)
    .reduce((x, y) => x + y, 0)
console.log(`Result part 1`, result1);

// part 2
const needed = sizes.get('/')! - 40000000
let result2 = Math.min(...Array.from(sizes.values()).filter(v => v >= needed))
console.log(`Result part 2`, result2);

import { log } from 'console';
import * as fs from 'fs';
export const x = "";

class Stack {
    private items: any[] = [];
    push(item: any) {
        this.items.push(item);
    }
    pushBack(item: any) {
        this.items.unshift(item);
    }
    pop() {
        return this.items.pop();
    }
    peek() {
        return this.items[this.items.length - 1];
    }
}

const input = fs.readFileSync('./2022/day05/input.txt', 'utf-8')
				.split('\n\n')
				
const stackCount = Math.ceil(input[0].split('\n')[0].length / 4);
const stacks: Stack[] = [];

for (let i = 0; i < stackCount; ++i) {
    const stack = new Stack();
	stacks.push(stack);
}

let starting = input[0].trimEnd().split('\n');

for (let line of starting) {
    const crates: string[] = new Array<string>().fill("", stackCount);
    let j = 0;
    for (let i = 0; i < line.length; i += 4) {
        const crate = line.slice(i, i + 4)[1];
        crates[j] = line.slice(i, i + 4)[1];
        if (crate !== " ") {
            stacks[j].pushBack(crate);
        }
        ++j;
    }
}

const instructions = input[1].trimEnd().split('\n');


// Part 2 
let result2: string

for (let instruction of instructions) {
    const line = instruction.split(' ');

    const count = parseInt(line[1]);

    // need to adjust the indexing
    const start = parseInt(line[3]) - 1;
    const end = parseInt(line[5]) - 1;

    let tempStack = new Stack();
    for (let i = 0; i < count; ++i) {
        tempStack.push(stacks[start].pop());
    }
    for (let i = 0; i < count; ++i) {
        stacks[end].push(tempStack.pop());
    }
}

result2 = stacks.map((s) => s.peek()).join('')
console.log(`Result part 2`, result2);

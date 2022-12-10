import * as fs from 'fs';

const input = fs.readFileSync('./2022/day03/input.txt', 'utf-8')
	.trim()
	.split('\n');

let result1: number = 0; 
input.forEach((el: string, i: number) => {
    const r1: string = el.slice(0, el.length / 2);
    const r2: string = el.slice(el.length/2);
    let item = checkTwoRuckSacks(r1, r2).split('')[0];
    result1 += calculateSum(item)
   
});
console.log(`Result part 1`, result1);

let result2: number = 0;
for(let i:number = 0; i < input.length; i += 3){
    const ruckSacks: string[] = [input[i], input[i+1], input[i+2]];
    const item: string = checkItems(ruckSacks)[0];
    result2 += calculateSum(item)
}
console.log(`Result part 1`, result2);


function checkItems(ruckSacks: string[]){
    let lastItems: string = ruckSacks[0];
    for (let i: number = 1; i < ruckSacks.length; i++){
        lastItems = checkTwoRuckSacks(lastItems, ruckSacks[i]);
    }
    return lastItems;
}

function calculateSum(item: string){
    let sub: number = 96;
    if(item === item.toUpperCase()) sub = 38;
    return item.charCodeAt(0) - sub
}

function checkTwoRuckSacks(r1: string, r2: string) {
    const items: string[] = []
    for(const item of r1.split('')){
        if(r2.split('').some((item2) => item === item2)){
            if(!items.includes(item)) items.push(item)
        }
    }
    return items.join('');
}

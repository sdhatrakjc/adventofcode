import * as fs from 'fs';

const input = fs.readFileSync('./2022/day04/input.txt', 'utf-8')
	.trim()
	.split('\n');


/*
	Fully Overlap : 
	1. Left[1] <= Right[1] && Left[0] >= Right[0]
	2. Right[1] <= Left[1] && Right[0] >= Left[0]

	Partial overlap : 
	3. Left[0] <= Right[1] && Right[1] <= Left[1]
	4. Left[0] <= Right[0] && Right[0] <= Left[1]
*/
let result1: number = 0; 
let result2: number = 0;
input.forEach((el: string, i: number) => {
	var ranges = el.split(",").map(n => n.split("-").map(x => parseInt(x)));

	if (ranges[0][1] <= ranges[1][1] && ranges[0][0] >= ranges[1][0]) {
        result1++;
		result2++;
    } else {
        if (ranges[1][1] <= ranges[0][1] && ranges[1][0] >= ranges[0][0]) {
            result1++;
			result2++;
        }else{
			// Else part for result 2 (To include partial overlap)
			if (ranges[0][0] <= ranges[1][1] && ranges[1][1] <= ranges[0][1]) {
                result2++;
            } else {
                if (ranges[0][0] <= ranges[1][0] && ranges[1][0] <= ranges[0][1]) {
                    result2++;
                }
            }
		}
    }
});
console.log(`Result part 1`, result1);
console.log(`Result part 2`, result2);

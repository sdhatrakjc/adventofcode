import { readFileSync } from 'fs';

const input = readFileSync('./2022/day9/input.txt', "utf-8").toString().split("\n")
input.pop()

function visitLocation(knots: number[][]){
    let tailVisitedLocations: string[] = ['0,0'];
    input.forEach(el => {
        let instruction : string[] = el.split(" ")
        const direction = instruction[0];
        let distance = parseInt(instruction[1]);
    
        while(distance > 0) {
            moveKnot(knots[0], direction);
            
            for (let j = 1; j < knots.length; j++) {
                if(!areKnotsTouching(knots[j-1], knots[j])) {
                    moveTailTowardsHead(knots[j], knots[j-1]);
                    if(j == knots.length - 1) {
                        tailVisitedLocations.push(knots[j][0] + ',' + knots[j][1]); 
                    }
                }else{
                    break;
                }
            }
    
            distance -=1;
        }
    });
    return tailVisitedLocations
}


function moveKnot(knot:number[], direction: string){
    switch(direction) {
      case 'L':
        knot[0] -= 1;
        return;
      case 'R':
        knot[0] += 1;
        return;
      case 'D':   
        knot[1] -= 1;
        return;
      case 'U':
        knot[1] += 1;
        return;
      default:
        console.log('wrong direction', direction);
    }
  }

function moveTailTowardsHead(tail: number[], head: number[]) {
    // 3-4 = -1 x 
    // 0-2 = -1 y
    const xDistance = head[0] - tail[0];
    const yDistance = head[1] - tail[1];
  
    // 2 to the right
    if(xDistance == 2 && yDistance == 0) {
        moveKnot(tail, 'R');
    // 2 to the left
    } else if (xDistance == -2 && yDistance == 0) {
        moveKnot(tail, 'L');
    // 2 up
    } else if (yDistance == 2 && xDistance == 0) {
        moveKnot(tail, 'U');
    // 2 down
    } else if (yDistance == -2 && xDistance == 0) {
        moveKnot(tail, 'D');
    } else if(xDistance > 0 && yDistance > 0) {
        moveKnot(tail, 'R');
        moveKnot(tail, 'U');
    } else if(xDistance > 0 && yDistance < 0) {
        moveKnot(tail, 'R');
        moveKnot(tail, 'D');
    } else if(xDistance < 0 && yDistance > 0) {
        moveKnot(tail, 'L');
        moveKnot(tail, 'U');
    } else if(xDistance < 0 && yDistance < 0) {
        moveKnot(tail, 'L');
        moveKnot(tail, 'D');
    }
  }

function areKnotsTouching(knot1:number[], knot2:number[]): boolean {
    // 4,1 && 3,0
    // 1, 4, 1
    const a = Math.abs(knot1[0] - knot2[0]);
    const b = Math.abs(knot1[1] - knot2[1]);
    if(knot1[1] == knot2[1]){
        return a <= 1
    }else if(knot1[0] == knot2[0]){
        return b <= 1
    }else {
        return a <= 1 && b <= 1
    }
}

const knots1 = [
    [0, 0], //head
    [0, 0]  //tail
]
let tailVisitedLocationsPart1 = visitLocation(knots1)
let result1 = Array.from(new Set(tailVisitedLocationsPart1)).length
console.log(`Result part 1`, result1);


const knots2 = []
for (let step = 0; step < 10; step++) {
    knots2.push([0,0]) 
}
let tailVisitedLocationsPart2 = visitLocation(knots2)
let result2 = Array.from(new Set(tailVisitedLocationsPart2)).length
console.log(`Result part 2`, result2);

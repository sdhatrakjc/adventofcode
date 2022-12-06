import { readFileSync } from 'fs';

const input = readFileSync('./2022/day6/input.txt', "utf-8").toString().split("");

const findMarker = (distinctChars: number) => {
  return (
    input
      .map((_, index) => input.slice(index, index + distinctChars))
      .findIndex((stream) => {
        return stream.every((char, index) => {
          const copyDataStream = [...stream];
          copyDataStream.splice(index, 1);
          if (copyDataStream.includes(char)) return false;
          return true;
        });
      }) + distinctChars
  );
};

console.log(`Result part 1`, findMarker(4));
console.log(`Result part 2`, findMarker(14));

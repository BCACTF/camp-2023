// I'm a bit too lazy to do it in C rn

const { readFileSync } = require("fs");
const { join: joinPaths } = require("path");

const flag = readFileSync(joinPaths(__dirname, "./flag.txt"), "utf-8");

const readline = require("readline");

const term = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

const isYOrN = (x) => ["y", "n"].includes(x.toLowerCase());

const ask = (message) => new Promise(r => term.question(message, r));

let hoursGoneBy = 0;
let distance = 0;
let speed = 0;
const loop = async () => {
    console.log("Hours gone by: " + hoursGoneBy);
    console.log("Distance travelled: " + distance + " miles");
    hoursGoneBy += 1;
    distance += speed >>> 0;
    distance |= 0;
    if (distance === -1) {
        console.log("How did you get so far so fast??");
        console.log("I guess you deserve the flag");

        console.log(flag);
        return setTimeout(() => process.exit(1), 200);
    }

    let answer;
    do {
        answer = await ask("Do you want to change the speed? (Y or N):");
    } while (isYOrN(answer) === false);

    if (answer === "Y") {
        let newSpeed = (parseInt(await ask("Enter new speed: ")) | 0);
        
        if (newSpeed > 100) {
            console.log("Haha. The speed is too fast");
            console.log("Slowing to 100 mph");
            newSpeed = 100;
        }

        // cast unsigned js
        newSpeed >>>= 0;

        console.log("New speed: " + newSpeed);
    }


    setTimeout(() => loop(), 1000);
}
let fs = require("fs");

function joinGroups(array) {
    let newArray = [];
    let currentText = "";
    for(const line of array){
        line == "" ? (newArray.push(currentText), currentText = ""): currentText += line + " ";
        if(array.indexOf(line) == array.length - 1){
            currentText += line;
            newArray.push(currentText);
        }
    }
    return newArray;
}

function splitUsers(group){
    return group.slice(0, -1).split(" ");
}

function countAnswers(group){
    const counted = [];
    const allAnswered = [];
    for(const user of group){
        let answers = user.split("");
        for(const answer of answers){ //for each answer the user put
            if(!counted.includes(answer)){ // if the letter wasn't already counted
                if(group.every((user) => user.includes(answer))){
                    allAnswered.push(answer);
                }
                counted.push(answer);
            }
        }
    }
    return allAnswered.length;
}

const main = async () => {
    let file = await fs.readFileSync('./input.txt', 'utf8');
    let array = file.split("\r\n"); // stupid windows
    let groups = joinGroups(array);
    let count = 0;
    for(const group of groups){
        let users = splitUsers(group);
        let allAnswered = countAnswers(users);
        count += allAnswered;
    }
    console.log(count);
    console.log("done");
}

main(); 

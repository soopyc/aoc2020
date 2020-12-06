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

function tallyAnswers(group){
    const current = [];
    for(const answer of group){
        if(!current.includes(answer))
            current.push(answer);
    }
    return current.length;
}

const main = async () => {
    let file = await fs.readFileSync('./input.txt', 'utf8');
    let array = file.split("\r\n"); // stupid windows
    let groups = joinGroups(array);
    let count = 0;
    for(const group of groups){
        let answers = group.replace(/\s/g, '');
        answers = tallyAnswers(answers);
        count += answers;
    }
    console.log(count);
    console.log("done");
}

main(); 

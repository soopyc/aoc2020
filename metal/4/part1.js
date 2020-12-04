let fs = require("fs");

function joinCredentials(array) {
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

function parseData(string){
    let data = {};
    let array = string.split(" ");
    array.pop();
    for(const entry of array) {
        let entryValues = entry.split(":");
        data[entryValues[0]] = entryValues[1];
    }
    return data;
}

function checkData(data){
    if(Object.values(data).length == 8)
        return true;
    if(Object.values(data).length == 7 && data.hasOwnProperty("cid"))
        return true;
    return false;
}

const main = async () => {
    let file = await fs.readFileSync('./input.txt', 'utf8');
    let array = file.split("\r\n"); // stupid windows
    let credentials = joinCredentials(array);
    let count = 0;
    for(const credential of credentials){
        if(checkData(parseData(credential)))
            count++;
    }
    console.log(count);
    console.log("done");
}

main(); 

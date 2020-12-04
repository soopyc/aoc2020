let fs = require("fs");
const { parse } = require("path");
const { pid } = require("process");

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
    if(Object.values(data).length == 7 && !data.hasOwnProperty("cid"))
        return true;
    return false;
}

function validData(data){
    for(const field in data){
        switch(field){
            case "byr":
                if(data.byr <= 1920 || data.byr >= 2002 || data.byr.length != 4)
                    return false;
            case "iyr":
            case "eyr":
            case "hgt":
            case "hcl":
            case "ecl":
                const colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
                if(!colors.includes(data.ecl))
                    return false;
            case "pid":
                if(data.pid.length != 9)
                    return false;
            default:
                return true;
        }
    }
}

const main = async () => {
    let file = await fs.readFileSync('./input.txt', 'utf8');
    let array = file.split("\r\n"); // stupid windows
    let credentials = joinCredentials(array);
    let count = 0;
    for(const credential of credentials){
        let data = parseData(credential)
        if(checkData(data))
            if(validData(data))
                count++;
    }
    console.log(count);
    console.log("done");
}

main(); 

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
    if(Object.values(data).length == 7 && !data.hasOwnProperty("cid"))
        return true;
    return false;
}

function validData(data){
    for(const field in data){
        //console.log(field)
        switch(field){
            case "byr":
                if(data.byr < 1920 || data.byr > 2002 || data.byr.length != 4){
                    return false;
                }
                break;
            case "iyr":
                if(data.iyr < 2010 || data.iyr > 2020 || data.byr.length != 4){
                    return false;
                }
                break;
            case "eyr":
                if(data.eyr < 2020 || data.eyr > 2030 || data.eyr.length != 4){
                    return false;
                }
                break;
            case "hgt":
                //console.log(data.hgt)
                if(!/[0-9]{2,3}(in|cm)/.test(data.hgt)){
                    return false;
                }
                const string = data.hgt;
                const unit = string.substring(string.length-2,string.length);
                const value = string.slice(0, -2);
                switch(unit){
                    case "in":
                        if(value < 59 || value > 76){ 
                            console.log("test1");
                            return false;
                        }
                        break;
                    case "cm":
                        if(value < 150 || value > 193){
                            console.log("test");
                            return false;
                        }
                        break;
                }
                break;
            case "hcl":
                if(!/#[0-9a-f]{6}/.test(data.hcl)){
                    return false;
                }
                break;
            case "ecl":
                const colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"];
                if(!colors.includes(data.ecl)){
                    return false;
                }
                break;
            case "pid":
                if(data.pid.length != 9){
                    return false;
                }
                break;
        }
    }
    return true;
}

const main = async () => {
    let file = await fs.readFileSync('./input.txt', 'utf8');
    let array = file.split("\n");
    let credentials = joinCredentials(array);
    let count = 0;
    for(const credential of credentials){
        let data = parseData(credential);
        if(checkData(data)){
            if(validData(data)){
                count++;
            }
        }
    }
    console.log(count);
    console.log("done");
}

main(); 

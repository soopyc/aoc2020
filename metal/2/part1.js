let fs = require("fs");

function getPolicyData(policy){
    let array = policy.split("-");
    let splitSecondArg = array[1].split(" ")
    array[1] = splitSecondArg[0];
    array[2] = splitSecondArg[1];
    return {
        min: array[0],
        max: array[1],
        char: array[2]
    }
}

function countInString(char, string){
    let count = 0;
    for(let i = 0; i < string.length; i++){
        if(string.charAt(i) == char){
            count++;
        }
    }
    return count;
}

const main = async () => {
    
    let file = await fs.readFileSync('./input.txt', 'utf8');
    let array = file.split("\n");
    let count = 0;
    for(let i = 0; i < array.length; i++) {
        let split = array[i].split(":");
        let policy = split[0];
        let password = split[1].substr(1);
        let policyData = getPolicyData(policy);
        const occurrences = countInString(policyData.char, password)
        if(occurrences >= policyData.min && occurrences <= policyData.max){
            count++;
        }
    }
    console.log(count);
    console.log("done");
}

main(); 

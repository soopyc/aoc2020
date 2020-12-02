let fs = require("fs");

function getPolicyData(policy){
    let array = policy.split("-");
    let splitSecondArg = array[1].split(" ")
    array[1] = splitSecondArg[0];
    array[2] = splitSecondArg[1];
    return {
        first: array[0],
        second: array[1],
        char: array[2]
    }
}

function checkPassword(policy, password){
    let firstSlot = policy.first-1;
    let secondSlot = policy.second-1;
    let char = policy.char;
    let hasFirst = password.charAt(firstSlot) == char ? true : false;
    let hasSecond = password.charAt(secondSlot) == char ? true : false;
    if(hasFirst && !hasSecond)
        return true;
    if(!hasFirst && hasSecond)
        return true;
    return false;
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
        if(checkPassword(policyData, password))
            count++;
    }
    console.log(count);
    console.log("done");
}

main(); 

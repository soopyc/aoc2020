let fs = require("fs");
let axios = require("axios");

const main = async () => {
    
    let file = await fs.readFileSync('./numbers.txt', 'utf8');
    let array = file.split("\n");
    for(let i = 0; i < array.length; i++) {
        let number = parseInt(array[i]);
        for(let j = i; j < array.length; j++){
            let number2 = parseInt(array[j])
            for(let x = 0; x < array.length; x++){
                let number3 = parseInt(array[x]);
                if(number + number2 + number3 == 2020){
                    console.log(`1st number: ${number}\n2nd number: ${number2}\n3rd number: ${number3}\nanswer: ${number*number2*number3}`);
                    break;
                }
            }
        }
    }
    console.log("done");
}

main(); 
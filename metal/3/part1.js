let fs = require("fs");

function getColumn(current) {
    return (current+3) % 31
}

const main = async () => {
    let file = await fs.readFileSync('./input.txt', 'utf8');
    let array = file.split("\n");
    let column = 3;
    let count = 0;
    for(let i = 1; i < array.length; i++) {
        let square = array[i].charAt(column);
        column = getColumn(column);
        if(square == "#"){
            count++;
        }
    }
    console.log(count);
    console.log("done");
}

main(); 

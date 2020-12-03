let fs = require("fs");

function getColumn(current, right) {
    return (current+right) % 31
}

function getTrees(array, right, down){ 
    let column = right; //3
    let count = 0;
    for(let i = down; i < array.length; i += down) { // down is 1
        let square = array[i].charAt(column);
        column = getColumn(column, right);
        if(square == "#"){
            count++;
        }
    }
    return count;
}

const main = async () => {
    let file = await fs.readFileSync('./input.txt', 'utf8');
    let array = file.split("\n");
    let first = getTrees(array, 1, 1);
    let second = getTrees(array, 3, 1);
    let third = getTrees(array, 5, 1);
    let fourth = getTrees(array, 7, 1);
    let fifth = getTrees(array, 1, 2);
    console.log("Right 1, down 1: " + first);
    console.log("Right 3, down 1: " + second);
    console.log("Right 5, down 1: " + third);
    console.log("Right 7, down 1: " + fourth);
    console.log("Right 1, down 2: " + fifth);
    console.log("Answer: " + first*second*third*fourth*fifth);
    //console.log("total: " + getTrees(array, 3, 1))
    console.log("done");
}

main(); 

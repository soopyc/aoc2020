let fs = require("fs");

function getData(seat){
    for(let i = 0; i < 7; i++){
        seat[i] == "F" ? seat = seat.replace("F", 0) : seat = seat.replace("B", 1);
    }
    for(let i = 7; i < 10; i++){
        seat[i] == "L" ? seat = seat.replace("L", 0) : seat = seat.replace("R", 1);
    }
    let rows = seat.substring(0,7);
    let columns = seat.substring(7);
    return{
        row: parseInt(rows, 2),
        column: parseInt(columns, 2)
    }

}

function calculateId(data){
    return (data.row * 8) + data.column;
}

const main = async () => {
    let file = await fs.readFileSync('./input.txt', 'utf8');
    let array = file.split("\r\n"); // god i hate windows
    let highestId = 0;
    for(let i = 0; i < array.length; i++) {
        let data = getData(array[i])
        let id = calculateId(data)
        array[i] = id;
    }
    for(const id of array){
        if(!array.includes(id + 1)){
            console.log(`your id is ${id + 1}`)
        }
        if(!array.includes(id - 1)){
            console.log(`your id is ${id - 1}`)
        }
    }
    console.log("done");
}

main(); 

// Lopps
// for (statement1; statement2; statement3)
// statement1: where loop should start 
// statement2: where the loop should finish 
// statement3: How the loop should goes 

// for i loop
for (let i = 0; i < 5; i++) {
    console.log('Hello, World!')
}

// for of loop
var cars = ["Volvo", "Toyota", "Tesla"]
for (let car of cars) {
    console.log(car)
    if (car == "Toyota") {
        break
    }
}

// ES6 syntax for each loop
cars.forEach( car => {
    console.log(car)
})
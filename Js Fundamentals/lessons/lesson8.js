// Declarative functions
helloOne()
function helloOne() {
    console.log('Hello one!')
}

// Anonymous function
var helloTwo = function () {
    console.log('Hello two!')
}
helloTwo()

// ES6 function syntax or arrow function 
var hellothree = () => {
    console.log('Hello three!')
}
hellothree()

// Function with arguments
function printName(name, lastName) {
    console.log(name + ' ' + lastName)
}
printName('Juliano', 'Peres')

// Function with return
function multiplyByTwo(number) {
    var result = number * 2
    return result
}
var myResult = multiplyByTwo(5)
console.log(myResult)

// import function 
import { printAge } from "../helpers/printHelper.js"
printAge(5)
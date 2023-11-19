// Logical operators "AND"

console.log(true && true) // all values has to be true for expression to be true 

// Logical "OR"
console.log(true || true) // any value should be true for the expression to be true 

var ageIsMoreThanEighteen = true
var isUSCitizen = true 

var eligibilityForDriversLicense = ageIsMoreThanEighteen && isUSCitizen
console.log('This customer is eligible for DL: ' + eligibilityForDriversLicense)

var ageIsMoreThanEighteen2 = false
var isUSCitizen2 = false
var eligibilityForDriversLicense2 = ageIsMoreThanEighteen2 || isUSCitizen2
console.log('This customer is eligible for DL: ' + eligibilityForDriversLicense2)

// Logical "NOT"
console.log(!true)
console.log(6 == 10)
console.log(6 !== 10)


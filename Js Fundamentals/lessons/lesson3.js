// Objects: Object is an entity that can hold multiple values at the same time. 

var customer = { 
    firstName: 'John',
    lastName: 'Smith',
    cars: ["Volvo", "Toyota", "Tesla"]
}

// dot notation 
customer.firstName = "Mike"

// Bracket notation 
customer['lastName'] = "Silver"
console.log(`${customer.firstName} ${customer.lastName}`)

//----------------------------------------------------------------------

// Arra: is a type of the entity, which is a list of items that you want to save, 
// and they are placed inside of the array as an order

var car = ["Volvo", "Toyota", "Tesla"]
console.log(car[2])
console.log(customer.cars[0])
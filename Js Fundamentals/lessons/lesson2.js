// concatination and interpolation

var price = 70
var itemName = "Book"
var messageToPrint = "The price for your " +itemName+ " is " +price+ " dollars." // concatinaion
var messageToPrint2 = `The price for your ${itemName} is ${price} dollars.` // interpolation
console.log(messageToPrint)
console.log(messageToPrint2)

// Condicional Statement

//if(condition){
    // execute some code here // this code wil be executed if is true 
//} else if {
    // execute some code here // this code will be executed if the first code be false
//} else {
    // execute some code here // this code will be executed if the first code be false
//}

// If hour be between 6 and 12, print "Good morning!"
// If hour be between 12 and 18, print "Good afternoon!"
// Otherwise, "Good evening!"


var hour = 5

if(hour >= 6 && hour < 12){
    console.log('Good Morning!')
} else if ( hour >= 12 && hour < 18){
    console.log('Good afternoon!')
} else {
    console.log('Good evening!')
}

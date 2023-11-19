//let familySize = 2;
//let plannedDistanceToDrive = 100;

//if(familySize <= 4 && plannedDistanceToDrive < 200){
  // console.log('Neste caso, o carro a ser alugado deve ser o modelo Tesla')
//} else if (familySize <= 4 && plannedDistanceToDrive >= 200){
  //console.log('Neste caso, o carro a ser alugado deve ser o modelo Toyota Camry')
//} else {
//  console.log('Neste caso, o carro a ser alugado deve ser o modelo Minivan')
//}

let familySize = 2;
let plannedDistanceToDrive = 100;

function recommendedCar(familySize, plannedDistanceToDrive){
  if (familySize <= 4 && plannedDistanceToDrive < 200){
    return "Tesla";
  } else if (familySize <= 4 && plannedDistanceToDrive >= 200){
    return "Toyota Camryn"; 
  } else { "Minivam";
  }
}

console.log(recommendedCar(familySize, plannedDistanceToDrive))

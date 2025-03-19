let people = []
let number = prompt("Ingrese la cantidad de personas que desea ingresar: ")

for (let i = 0; i < number; i++) {
    let n = i + 1;
    let name = prompt(`Ingrese el Nombre de la ${n} persona:`)
    let age = prompt(`Ingrese la Edad de la ${n} persona: `)
    let note = parseFloat(prompt(`Ingrese la Nota de la ${n} persona: `)) 

    people.push([name, age, note])
}

let peopleList = people.map(person => `Nombre: 
    ${person[0]} - Edad: ${person[1]}, Nota: ${person[2]}`).join("\n");
alert(`Listado:\n${peopleList}`)


people.sort((a, b) => b[2] - a[2]);

let sortedList = people.map(person => `${person[0]} - Edad: ${person[1]}, Nota: ${person[2]}`).join("\n"); 
alert(`Lista ordenada por nota:\n${sortedList}`);

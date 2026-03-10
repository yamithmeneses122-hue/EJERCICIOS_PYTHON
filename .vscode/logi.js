let pregunta =[
    "¿cual es la capiatal de colombia?",
    "2+2",
    "5 * 3"
    ];

let opciones =[ 
["Bogota", "Cali","Popayan","barranquilla"],
["3","4","5","7"],
["15","20","10","5"]
]


let correcta = [0,1,0];

let numeroPregunta = 0;

cargarPregunta();

 function cargarPregunta(){

document.getElementById("pregunta").innerHTML = pregunta[numeroPregunta];

document.getElementById("op0").innerHTML = opciones [numeroPregunta] [0];
document.getElementById("op1").innerHTML = opciones [numeroPregunta] [1];
document.getElementById("op2").innerHTML = opciones [numeroPregunta] [2];
document.getElementById("op3").innerHTML = opciones [numeroPregunta] [3];

 }

function responder(opcion){
    if (opcion==correcta[numeroPregunta]){
        document.getElementById("resultado").innerHTML="Bien";}
    else {
document.getElementById("resultado").innerHTML = "Esta mal";
    }   
 }

function siguiente(){

numeroPregunta = numeroPregunta + 1;
document.getElementById("resultado").innerHTML = "";
if(numeroPregunta < pregunta.length){
cargarPregunta();
}
}

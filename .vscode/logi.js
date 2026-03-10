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

document.getElementById( "op4").innerHTML = "siguiente";

document.getElementById("op0").innerHTML = opciones [numeroPregunta] [0];
document.getElementById("op1").innerHTML = opciones [numeroPregunta] [1];
document.getElementById("op2").innerHTML = opciones [numeroPregunta] [2];
document.getElementById("op3").innerHTML = opciones [numeroPregunta] [3];

 }

function responder(opcion){
    if (opcion==correcta[numeroPregunta]){

document.getElementById("resultado").innerHTML =  '<img src="https://d1csarkz8obe9u.cloudfront.net/posterpreviews/well-done-emoji-design-template-0a5d9a9e35252a85776b7c54055a05b4_screen.jpg?ts=1650348078" style="width:200px; border-radius:12px;">';

     }
    else {
document.getElementById("resultado").innerHTML =  '<img src="https://media.istockphoto.com/id/639765496/es/vector/riendo-con-l%C3%A1grimas-y-se%C3%B1alando-emoticono.jpg?s=612x612&w=0&k=20&c=uk_QtIHkIo7f6gCqT1L0g7bAQqGHUE9ZRKW-vliX9eQ=" style="width:200px; border-radius:12px;">';

    }   
 }

function siguiente(){

numeroPregunta = numeroPregunta + 1;
document.getElementById("resultado").innerHTML = "";
if(numeroPregunta < pregunta.length){
cargarPregunta();
}
}

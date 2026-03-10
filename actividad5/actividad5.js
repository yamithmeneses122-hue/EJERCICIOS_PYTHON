// 1. Arreglo de preguntas
let preguntas = [
"¿Cuál es la capital de Colombia?",
"¿Cuánto es 2 + 2?",
"¿Qué planeta es el rojo?",
"¿Cuál es el río más largo del mundo?",
"¿Quién pintó la Mona Lisa?",
"¿Cuánto es 5 x 5?",
"¿Qué lenguaje se usa para páginas web?",
"¿Cuál es el animal más grande del mundo?",
"¿En qué continente está Colombia?",
"¿Cuántos días tiene una semana?",
"¿Qué gas respiramos para vivir?",
"¿Cuál es el océano más grande?",
"¿Quién descubrió América?",
"¿Cuánto es 10 / 2?",
"¿Qué instrumento tiene teclas blancas y negras?",
"¿Cuál es la capital de Francia?",
"¿Cuántos meses tiene un año?",
"¿Qué color resulta de azul + amarillo?",
"¿Cuál es el satélite de la Tierra?",
"¿Cuál es el idioma más hablado del mundo?"
];

// 2. Respuestas (4 por cada pregunta)
let respuestas = [
["Bogotá","Cali","Medellín","Cartagena"],
["1","2","3","4"],
["Marte","Júpiter","Saturno","Venus"],
["Amazonas","Nilo","Magdalena","Yangtsé"],
["Da Vinci","Picasso","Van Gogh","Miguel Ángel"],
["10","15","20","25"],
["JavaScript","HTML","Python","Java"],
["Ballena azul","Elefante","Jirafa","Tiburón"],
["América","Europa","Asia","África"],
["5","6","7","8"],
["Oxígeno","Hidrógeno","Helio","Nitrógeno"],
["Pacífico","Atlántico","Índico","Ártico"],
["Cristóbal Colón","Newton","Einstein","Galileo"],
["2","4","5","6"],
["Piano","Guitarra","Batería","Flauta"],
["París","Roma","Madrid","Lisboa"],
["10","11","12","13"],
["Verde","Morado","Naranja","Negro"],
["La Luna","El Sol","Marte","Venus"],
["Chino","Español","Inglés","Francés"]
];

// 3. Índices de respuestas correctas
let respuestasCorrectas = [
0,3,0,1,0,
3,1,0,0,2,
0,0,0,2,0,
0,2,0,0,0
];

// 4. Puntos por pregunta
let puntos = [
10,10,10,10,10,
10,10,10,10,10,
10,10,10,10,10,
10,10,10,10,10
];

// 5. Función del juego
function jugar(){

let total = 0;

for(let i = 0; i < preguntas.length; i++){

let texto = preguntas[i] + "\n";

for(let j = 0; j < 4; j++){
texto += j + " - " + respuestas[i][j] + "\n";
}

let respuestaUsuario = prompt(texto);

if(respuestaUsuario == respuestasCorrectas[i]){

alert("Correcto");
total += puntos[i];

}else{

alert("Incorrecto");

}

}

alert("Tu puntaje final es: " + total);

}

// 6. Iniciar juego
jugar();
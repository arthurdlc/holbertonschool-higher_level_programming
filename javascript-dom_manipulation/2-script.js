// ce code est fait pour changer la classe du header quand l'utilisateur clique dessus
const header = document.getElementById('header'); // ou document.querySelector('.header')
const class_red = document.getElementsByClassName('red_header'); // la constant retient la classe red

header.classList.add('red'); // on ajoute la classe red au header pass avec un = mais avec la methode add
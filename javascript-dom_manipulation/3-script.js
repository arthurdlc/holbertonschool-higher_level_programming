const header = document.getElementById('header');

if (HTMLElement.click(header)){ // si on a un click du user su le header on execute les instructions suivante
    if (header.classList.contains('red')) // dans le cas ou a la base le header a une class red
    {
      header.classList.remove('red'); // on retire le red et on rajoute green a la place 
      header.classList.add('green');
    }
    else if(header.classList.contains('green')) // dans le cas ou a la base le header a une class green
    {
      header.classList.remove('green');
      header.classList.add('red');
    }
  }
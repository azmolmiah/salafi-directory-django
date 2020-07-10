window.onload = function () { 
  const date = new Date();
  document.querySelector('.year').innerHTML = date.getFullYear();

  const policyBtn = document.getElementById('policyBtn');

  policyBtn.addEventListener('click', (e) => {
    e.path[4].remove();
  })
}


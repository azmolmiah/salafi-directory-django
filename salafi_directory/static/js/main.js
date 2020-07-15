window.onload = function () { 
  const policy = document.getElementById('policy');

  if(JSON.parse(localStorage.getItem("btn")) === true){
    policy.innerHTML = '';
  } else {
    policy.innerHTML = `<div class="container">
    <div class="row pt-3 ">
      <div class="col-8">
        <p>Salafi Directory uses cookies and caches to give you the best experience. You give us your consent to do so by clicking 'Accept' or by continuing to use our website after you have received this cookies and caches notification. View our <a href="{% url 'cookies' %}">Cookies and Caches Policy</a> and our <a href="{% url 'privacy' %}">Privacy Policy</a>.</p>
      </div>
      <div class="col-4">
        <button id="policyBtn" class="btn btn-primary btn-block py-auto">
          Accept
        </button>
      </div>
    </div>
  </div>`
  }

  const policyBtn = document.getElementById('policyBtn');
  if (policyBtn != null){
    policyBtn.addEventListener('click', (e) => {
      e.path[4].remove();
      localStorage.setItem("btn", JSON.stringify(true));
    })
  }

  const date = new Date();
  document.querySelector('.year').innerHTML = date.getFullYear();
}


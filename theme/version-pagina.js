// Pone la versión del motor (theme/version.js) en la barra de arriba y al
// pie de cada página del manual.
(function () {
  var v = window.FOXY_VERSION;
  if (!v) return;
  function poner() {
    var barra = document.querySelector(".right-buttons");
    if (barra && !document.querySelector(".foxy-version")) {
      var s = document.createElement("span");
      s.className = "foxy-version";
      s.title = "Versión del motor que describe este manual";
      s.textContent = "Foxy Engine " + v;
      barra.insertBefore(s, barra.firstChild);
    }
    var main = document.querySelector("main");
    if (main && !document.querySelector(".foxy-pie")) {
      var p = document.createElement("p");
      p.className = "foxy-pie";
      p.innerHTML = 'Manual de Foxy Engine ' + v +
        ' · <a href="' + (window.path_to_root || "") + 'apendices/historial.html">Historial de versiones</a>';
      main.appendChild(p);
    }
  }
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", poner);
  } else {
    poner();
  }
})();

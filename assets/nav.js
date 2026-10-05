// Hover intent: menus stay open while the pointer travels diagonally into them,
// and a neighbouring menu only takes over after the pointer rests on it.
(function () {
  if (!window.matchMedia("(hover: hover)").matches) return;
  var dds = document.querySelectorAll(".dd"), closeT, openT;
  function openOnly(dd) { dds.forEach(function (o) { o.classList.toggle("hov", o === dd); }); }
  dds.forEach(function (dd) {
    dd.addEventListener("mouseenter", function () {
      clearTimeout(closeT); clearTimeout(openT);
      var other = document.querySelector(".dd.hov");
      if (!other || other === dd) openOnly(dd);
      else openT = setTimeout(function () { openOnly(dd); }, 220);
    });
    dd.addEventListener("mouseleave", function () {
      clearTimeout(openT);
      closeT = setTimeout(function () { dd.classList.remove("hov"); }, 450);
    });
  });
})();

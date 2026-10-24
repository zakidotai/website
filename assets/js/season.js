(function () {
  var root = document.documentElement;
  var field = document.querySelector("[data-season-control]");
  if (!field) return;
  var current = root.getAttribute("data-season") || "winter";
  var inputs = field.querySelectorAll('input[name="season"]');
  inputs.forEach(function (input) {
    input.checked = input.value === current;
    input.addEventListener("change", function () {
      if (!input.checked) return;
      root.setAttribute("data-season", input.value);
      try {
        localStorage.setItem("season", input.value);
      } catch (err) {}
    });
  });
})();

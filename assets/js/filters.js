(function () {
  function apply(root) {
    var search = root.querySelector("[data-filter-search]");
    var type = root.querySelector("[data-filter-type]");
    var topic = root.querySelector("[data-filter-topic]");
    var category = root.querySelector("[data-filter-category]");
    var items = root.querySelectorAll("[data-filter-item]");
    var groups = root.querySelectorAll("[data-filter-group]");
    var empty = root.querySelector("[data-filter-empty]");
    var query = (search && search.value ? search.value : "").toLowerCase();
    var typeVal = type ? type.value : "";
    var topicVal = topic ? topic.value : "";
    var categoryVal = category ? category.value : "";
    var visible = 0;

    items.forEach(function (item) {
      var hay = (item.getAttribute("data-search") || "").toLowerCase();
      var topics = (item.getAttribute("data-topics") || "").split(/\s+/);
      var ok = true;
      if (query && hay.indexOf(query) === -1) ok = false;
      if (typeVal && item.getAttribute("data-type") !== typeVal) ok = false;
      if (topicVal && topics.indexOf(topicVal) === -1) ok = false;
      if (categoryVal && item.getAttribute("data-category") !== categoryVal) ok = false;
      item.hidden = !ok;
      if (ok) visible += 1;
    });

    groups.forEach(function (group) {
      group.hidden = !group.querySelector("[data-filter-item]:not([hidden])");
    });
    if (empty) empty.hidden = visible !== 0;
  }

  document.querySelectorAll("[data-filter-root]").forEach(function (root) {
    apply(root);
    root.addEventListener("input", function () {
      apply(root);
    });
    root.addEventListener("change", function () {
      apply(root);
    });
  });

  document.addEventListener("click", function (event) {
    var toggle = event.target.closest("[data-bibtex-toggle]");
    if (toggle) {
      var panel = document.getElementById(toggle.getAttribute("aria-controls"));
      if (!panel) return;
      var open = panel.hidden;
      panel.hidden = !open;
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
      return;
    }

    var copy = event.target.closest("[data-bibtex-copy]");
    if (!copy) return;
    var pre = copy.parentElement.querySelector(".bibtex");
    if (!pre) return;
    var text = pre.textContent;
    var done = function () {
      copy.textContent = "Copied";
      setTimeout(function () {
        copy.textContent = "Copy";
      }, 1500);
    };
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(text).then(done).catch(function () {
        fallbackCopy(pre, done);
      });
    } else {
      fallbackCopy(pre, done);
    }
  });

  function fallbackCopy(pre, done) {
    var range = document.createRange();
    range.selectNodeContents(pre);
    var selection = window.getSelection();
    selection.removeAllRanges();
    selection.addRange(range);
    try {
      if (document.execCommand("copy")) done();
    } catch (err) {}
  }
})();

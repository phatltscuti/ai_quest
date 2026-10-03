// Chon ngon ngu theo hash: file.html#en -> tieng Anh, mac dinh tieng Viet.
(function () {
  var lang = location.hash === '#en' ? 'en' : 'vi';
  document.documentElement.lang = lang;
  document.querySelectorAll('[data-vi]').forEach(function (el) {
    el.innerHTML = el.getAttribute(lang === 'en' ? 'data-en' : 'data-vi');
  });
})();

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

// Suggest the visitor's own language (browser language first, then time zone). Never redirects automatically.
(function () {
  var MSG = {
    en: ["This page is available in English.", "View in English", "No thanks"],
    de: ["Diese Seite ist auch auf Deutsch verfügbar.", "Auf Deutsch ansehen", "Nein, danke"],
    es: ["Esta página está disponible en español.", "Ver en español", "No, gracias"],
    fr: ["Cette page est disponible en français.", "Voir en français", "Non merci"],
    it: ["Questa pagina è disponibile in italiano.", "Leggi in italiano", "No, grazie"],
    ru: ["Эта страница доступна на русском языке.", "Открыть на русском", "Нет, спасибо"],
    zh: ["本页面提供简体中文版本。", "查看中文版", "不用了"],
    ja: ["このページは日本語でもご覧いただけます。", "日本語で見る", "閉じる"]
  };
  var HUBMSG = { de: "Unsere Leitfäden gibt es auch auf Deutsch.", es: "Nuestras guías también están en español.", fr: "Nos guides existent aussi en français.", it: "Le nostre guide sono disponibili anche in italiano.", ru: "Наши руководства доступны на русском языке.", zh: "我们的指南也提供中文版。", ja: "ガイドは日本語でもご覧いただけます。" };
  var TZ = { "Europe/Rome": "it", "Europe/Berlin": "de", "Europe/Vienna": "de", "Europe/Zurich": "de", "Europe/Madrid": "es", "America/Mexico_City": "es", "America/Bogota": "es", "America/Lima": "es", "America/Argentina/Buenos_Aires": "es", "America/Santiago": "es", "Europe/Paris": "fr", "Europe/Brussels": "fr", "Europe/Moscow": "ru", "Asia/Yekaterinburg": "ru", "Asia/Novosibirsk": "ru", "Asia/Shanghai": "zh", "Asia/Chongqing": "zh", "Asia/Tokyo": "ja" };
  var cur = (document.documentElement.lang || "en").slice(0, 2);
  var pref = null;
  (navigator.languages || [navigator.language || ""]).some(function (l) { var b = (l || "").slice(0, 2).toLowerCase(); if (MSG[b]) { pref = b; return true } return false });
  if (!pref || pref === "en") { try { var tz = Intl.DateTimeFormat().resolvedOptions().timeZone; if (TZ[tz]) pref = TZ[tz] } catch (e) {} }
  if (!pref && cur !== "en") pref = "en";
  if (!pref || pref === cur) return;
  try { if (localStorage.getItem("npi_lang_dismiss") === pref) return } catch (e) {}
  var hl = pref === "zh" ? "zh-Hans" : pref, link = document.querySelector('link[rel="alternate"][hreflang="' + hl + '"]'), url = link && link.getAttribute("href"), text = MSG[pref][0];
  if (!url) { var dd = document.querySelector(".langdd"); try { url = dd && JSON.parse(dd.getAttribute("data-hubs") || "{}")[pref] } catch (e) {} if (!url) return; text = HUBMSG[pref] || text }
  function show() {
    var b = document.createElement("div"); b.id = "npi-langbar"; b.setAttribute("lang", pref); b.setAttribute("role", "region");
    b.innerHTML = '<p></p><a class="go"></a><button type="button"></button>';
    b.querySelector("p").textContent = text; var a = b.querySelector("a"); a.href = url; a.textContent = MSG[pref][1];
    var x = b.querySelector("button"); x.textContent = MSG[pref][2];
    x.onclick = function () { try { localStorage.setItem("npi_lang_dismiss", pref) } catch (e) {} b.remove() };
    document.body.appendChild(b);
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", show); else show();
})();

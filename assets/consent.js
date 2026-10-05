// Small analytics consent banner (Google Consent Mode v2). Choice is stored on this device only.
(function () {
  var KEY = "npi_consent", saved = null;
  try { saved = localStorage.getItem(KEY); } catch (e) {}
  function set(v) {
    try { localStorage.setItem(KEY, v); } catch (e) {}
    if (window.gtag) gtag("consent", "update", { analytics_storage: v });
    var b = document.getElementById("npi-consent"); if (b) b.remove();
  }
  window.npiCookieSettings = function () { try { localStorage.removeItem(KEY); } catch (e) {} show(); };
  function show() {
    if (document.getElementById("npi-consent")) return;
    var d = document.createElement("div");
    d.id = "npi-consent"; d.setAttribute("role", "dialog"); d.setAttribute("aria-label", "Analytics cookies");
    d.innerHTML = '<p>We use Google Analytics cookies to understand how the site is used, only if you agree. <a href="/#privacy">Privacy policy</a></p>' +
      '<div><button type="button" data-v="denied">Reject</button><button type="button" data-v="granted" class="yes">Accept</button></div>';
    d.addEventListener("click", function (e) { var v = e.target.getAttribute("data-v"); if (v) set(v); });
    var s = document.createElement("style");
    s.textContent = "#npi-consent{position:fixed;z-index:1000;left:16px;right:16px;bottom:16px;max-width:560px;margin:0 auto;background:#16202a;color:#fff;border-radius:12px;padding:14px 16px;display:flex;gap:12px;align-items:center;flex-wrap:wrap;box-shadow:0 12px 32px -8px rgba(0,0,0,.4);font:14px/1.45 system-ui,sans-serif}#npi-consent p{margin:0;flex:1 1 260px}#npi-consent a{color:#9fd4b3}#npi-consent div{display:flex;gap:8px}#npi-consent button{font:600 14px system-ui,sans-serif;border-radius:8px;padding:8px 14px;cursor:pointer;border:1px solid #5b6772;background:transparent;color:#fff}#npi-consent button.yes{background:#2f7d4f;border-color:#2f7d4f}";
    d.appendChild(s); document.body.appendChild(d);
  }
  if (saved !== "granted" && saved !== "denied") {
    if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", show); else show();
  }
})();

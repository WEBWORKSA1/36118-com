/* 36118.com shared behaviour */
(function () {
  "use strict";

  /* ---- Configuration: edit these, no build step needed ---- */
  var CONFIG = {
    adClient: "ca-pub-6620975821265271",
    // After AdSense approval, paste display-unit slot IDs here to fill the reserved .ad-slot positions.
    // Leave empty to rely on Auto ads only (the default).
    adSlots: { top: "", inContent: "", sidebar: "", footer: "" },
    // Optional direct payment links for the Support page (e.g. PayPal.me, Buy Me a Coffee, Stripe Payment Link).
    payLinks: { paypal: "", coffee: "", stripe: "" },
    youtubeChannel: "" // e.g. "https://www.youtube.com/@yourchannel"
  };
  window.SITE36 = CONFIG;

  /* ---- Private inbox: assembled only at send time, never rendered ---- */
  var P = ["LmNvbQ==", "QGdtYWls", "d2Vid29ya3NhMQ=="];
  function inbox() { return atob(P[2]) + atob(P[1]) + atob(P[0]); }

  /* ---- Theme ---- */
  var root = document.documentElement;
  try { var t = localStorage.getItem("theme"); if (t) root.setAttribute("data-theme", t); } catch (e) {}
  document.addEventListener("click", function (e) {
    var b = e.target.closest("[data-theme-toggle]"); if (!b) return;
    var dark = root.getAttribute("data-theme") === "dark" || (!root.getAttribute("data-theme") && matchMedia("(prefers-color-scheme: dark)").matches);
    var next = dark ? "light" : "dark"; root.setAttribute("data-theme", next);
    try { localStorage.setItem("theme", next); } catch (e2) {}
  });

  /* ---- Mobile nav ---- */
  document.addEventListener("click", function (e) {
    var b = e.target.closest(".menu-btn"); if (!b) return;
    var nav = document.getElementById("nav"); var open = nav.classList.toggle("open");
    b.setAttribute("aria-expanded", open ? "true" : "false");
  });

  /* ---- "Email us" links: open the mail app without the address ever appearing in the page ---- */
  document.addEventListener("click", function (e) {
    var a = e.target.closest("[data-mail]"); if (!a) return;
    e.preventDefault();
    var subj = encodeURIComponent(a.getAttribute("data-mail") || "Inquiry from 36118.com");
    window.location.href = "mai" + "lto:" + inbox() + "?subject=" + subj;
  });

  /* ---- Forms: every form posts to the private inbox through FormSubmit ---- */
  function serialize(form) {
    var data = {};
    new FormData(form).forEach(function (v, k) { if (data[k]) data[k] += ", " + v; else data[k] = v; });
    return data;
  }
  function setStatus(form, msg, ok) {
    var s = form.querySelector(".form-status"); if (!s) { s = document.createElement("p"); s.className = "form-status"; s.setAttribute("role", "status"); form.appendChild(s); }
    s.textContent = msg; s.className = "form-status " + (ok ? "ok" : "err");
  }
  document.addEventListener("submit", function (e) {
    var form = e.target; if (!form.matches("[data-form]")) return;
    e.preventDefault();
    if (form.querySelector("[name=_honey]") && form.querySelector("[name=_honey]").value) return; // bot
    if (!form.checkValidity()) { form.reportValidity(); return; }
    var data = serialize(form);
    delete data._honey;
    data._subject = "[36118.com] " + (form.getAttribute("data-form") || "Form") + (data.intent ? " — " + data.intent : "");
    data._template = "table"; data._captcha = "false";
    data.page = location.href; data.submitted = new Date().toISOString();
    if (typeof form.onBeforeSend === "function") form.onBeforeSend(data);
    var btn = form.querySelector("[type=submit]"); var label = btn ? btn.textContent : "";
    if (btn) { btn.disabled = true; btn.textContent = "Sending…"; }
    fetch("https://formsubmit.co/ajax/" + inbox(), {
      method: "POST", headers: { "Content-Type": "application/json", "Accept": "application/json" }, body: JSON.stringify(data)
    }).then(function (r) { return r.json().catch(function () { return {}; }); })
      .then(function (j) {
        if (j && (j.success === "true" || j.success === true || /activat/i.test(j.message || ""))) {
          setStatus(form, form.getAttribute("data-ok") || "Received. We reply within two business days.", true);
          form.reset(); if (typeof form.onSent === "function") form.onSent();
        } else { throw new Error(j && j.message || "send failed"); }
      })
      .catch(function () {
        setStatus(form, "The form couldn't send from this network. Use the Email us link instead — your details stay on this page.", false);
      })
      .finally(function () { if (btn) { btn.disabled = false; btn.textContent = label; } });
  });

  /* ---- Lite YouTube: loads the player only on click ---- */
  function hydrateYT(el) {
    var id = el.getAttribute("data-yt");
    el.style.backgroundImage = "url(https://i.ytimg.com/vi/" + id + "/hqdefault.jpg)";
  }
  document.querySelectorAll("[data-yt]").forEach(hydrateYT);
  document.addEventListener("click", function (e) {
    var el = e.target.closest("[data-yt]"); if (!el || el.querySelector("iframe")) return;
    var id = el.getAttribute("data-yt");
    var f = document.createElement("iframe");
    f.src = "https://www.youtube-nocookie.com/embed/" + id + "?autoplay=1&rel=0";
    f.title = el.getAttribute("aria-label") || "YouTube video";
    f.allow = "accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share";
    f.allowFullscreen = true; el.innerHTML = ""; el.appendChild(f);
  });

  /* ---- Reserved ad positions: filled only when slot IDs are configured ---- */
  function fillSlots() {
    document.querySelectorAll(".ad-slot[data-slot]").forEach(function (box) {
      var id = CONFIG.adSlots[box.getAttribute("data-slot")]; if (!id || box.children.length) return;
      box.innerHTML = '<div class="ad-label">Advertisement</div><ins class="adsbygoogle" style="display:block" data-ad-client="' + CONFIG.adClient +
        '" data-ad-slot="' + id + '" data-ad-format="auto" data-full-width-responsive="true"></ins>';
      try { (window.adsbygoogle = window.adsbygoogle || []).push({}); } catch (e) {}
    });
  }
  fillSlots();

  /* ---- Optional payment links ---- */
  document.querySelectorAll("[data-pay]").forEach(function (a) {
    var url = CONFIG.payLinks[a.getAttribute("data-pay")]; if (url) { a.href = url; a.hidden = false; }
  });
  document.querySelectorAll("[data-yt-channel]").forEach(function (a) {
    if (CONFIG.youtubeChannel) { a.href = CONFIG.youtubeChannel; a.hidden = false; }
  });

  /* ---- Cookie notice (pairs with Google's consent message for EEA/UK visitors) ---- */
  try {
    if (!localStorage.getItem("cookie-ok")) {
      var c = document.getElementById("cookie"); if (c) {
        c.classList.add("show");
        c.querySelector("[data-cookie-ok]").addEventListener("click", function () { localStorage.setItem("cookie-ok", "1"); c.classList.remove("show"); });
      }
    }
  } catch (e) {}

  /* ---- Year ---- */
  document.querySelectorAll("[data-year]").forEach(function (y) { y.textContent = new Date().getFullYear(); });

  /* ---- Newsletter-style quick forms prefill ---- */
  var params = new URLSearchParams(location.search);
  document.querySelectorAll("[data-prefill]").forEach(function (inp) {
    var v = params.get(inp.getAttribute("data-prefill")); if (v) inp.value = v;
  });
})();

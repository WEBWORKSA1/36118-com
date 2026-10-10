/* 36118.com interactive tools. Each block runs only when its markup is on the page. */
(function () {
  "use strict";
  var $ = function (s, c) { return (c || document).querySelector(s); };
  var esc = function (s) { return String(s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); };
  var fmt = function (n) { return n == null ? "—" : Number(n).toLocaleString("en-US"); };
  var root = document.body.getAttribute("data-root") || "./";
  var params = new URLSearchParams(location.search);

  /* ---------- Split-flap hero ---------- */
  var flap = $("#heroNum");
  if (flap) {
    var tiles = $("#heroTiles"), out = $("#heroOut");
    var render = function (val, animate) {
      tiles.innerHTML = "";
      val.split("").forEach(function (d, i) {
        var t = document.createElement("span"); t.className = "tile" + (d === "8" || d === "6" ? " lucky" : "") + (animate ? " flip" : "");
        if (animate) t.style.animationDelay = (i * 70) + "ms";
        t.textContent = d; tiles.appendChild(t);
      });
      var caret = document.createElement("span"); caret.className = "caret"; tiles.appendChild(caret);
    };
    var readout = function (val) {
      var r = N36.analyze(val || "0");
      if (r.error) { out.innerHTML = '<p>' + esc(r.error) + '</p>'; return; }
      var rows = [
        ["Prime factors", r.prime ? "Prime number" : N36.factorString(r)],
        ["In words", r.words],
        ["Binary / hex", r.bin.length > 24 ? r.hex : r.bin + " / " + r.hex],
        ["Digit sum / root", r.digitSum + " / " + r.digitalRoot],
        ["Lucky-number score", r.lucky.score + " / 100"],
        ["Traits", r.tags.slice(0, 5).join(", ")]
      ];
      out.innerHTML = "<dl>" + rows.map(function (x) { return "<dt>" + x[0] + "</dt><dd>" + esc(x[1]) + "</dd>"; }).join("") + "</dl>";
      $("#heroDecode").href = root + "tools/number-decoder.html?n=" + r.input;
      $("#heroLucky").href = root + "tools/lucky-number.html?n=" + r.input;
      var z = $("#heroZip"); z.href = root + "tools/zip-explorer.html?zip=" + r.input; z.hidden = r.input.length !== 5;
      $("#heroDomain").href = root + "tools/domain-valuator.html?d=" + r.input + ".com";
    };
    flap.addEventListener("input", function () {
      var v = N36.clean(flap.value).slice(0, 15); flap.value = v; render(v || "", false); readout(v);
    });
    flap.addEventListener("keydown", function (e) {
      if (e.key === "Enter") { e.preventDefault(); location.href = $("#heroDecode").href; }
    });
    var reduce = matchMedia("(prefers-reduced-motion: reduce)").matches;
    render("36118", !reduce); readout("36118");
  }

  /* ---------- Number decoder ---------- */
  var dForm = $("#decodeForm");
  if (dForm) {
    var dIn = $("#decodeInput"), dOut = $("#decodeOut");
    var runDecode = function (val) {
      var r = N36.analyze(val);
      if (r.error) { dOut.innerHTML = '<p class="result-empty">' + esc(r.error) + "</p>"; return; }
      history.replaceState(null, "", "?n=" + r.input);
      document.title = r.input + " — number decoded | 36118.com";
      var yesno = function (b) { return b ? "Yes" : "No"; };
      var rows = [
        ["Digits", r.digits], ["Even or odd", r.even ? "Even" : "Odd"],
        ["Prime?", r.n < 2 ? "No (primes start at 2)" : (r.prime ? "Yes — divisible only by 1 and itself" : "No")],
        ["Prime factorisation", r.n < 2 ? "—" : N36.factorString(r)],
        ["Number of divisors", fmt(r.divisorCount)], ["Sum of divisors σ(n)", fmt(r.sigma)],
        ["Euler's totient φ(n)", fmt(r.phi)], ["Perfect / abundant / deficient", r.kind || "—"],
        ["Previous prime", fmt(r.prevPrime)], ["Next prime", fmt(r.nextPrime)],
        ["Perfect square", yesno(r.square)], ["Perfect cube", yesno(r.cube)], ["Triangular number", yesno(r.triangular)],
        ["Fibonacci number", yesno(r.fibonacci)], ["Harshad (divisible by digit sum)", yesno(r.harshad)],
        ["Palindrome", yesno(r.palindrome)], ["Reversed", r.reverse],
        ["Digit sum", r.digitSum], ["Digital root", r.digitalRoot],
        ["Square root", r.sqrt.toLocaleString("en-US", { maximumFractionDigits: 6 })],
        ["log₁₀", r.log10 == null ? "—" : r.log10.toFixed(6)], ["Scientific notation", r.sci || "—"],
        ["In words", r.words], ["Roman numerals", r.roman || "Only defined for 1–3,999"],
        ["Binary (base 2)", r.bin], ["Octal (base 8)", r.oct], ["Hexadecimal (base 16)", r.hex], ["Base 36", r.b36]
      ];
      var links = [];
      if (r.asZip) links.push('<a class="btn btn-dark" href="zip-explorer.html?zip=' + r.input + '">Look up ZIP ' + r.input + "</a>");
      links.push('<a class="btn btn-ghost" href="lucky-number.html?n=' + r.input + '">Lucky-number reading</a>');
      links.push('<a class="btn btn-ghost" href="domain-valuator.html?d=' + r.input + '.com">Score ' + r.input + ".com</a>");
      var nb = function (k) { return '<a class="pill-link" href="?n=' + k + '">' + k + "</a>"; };
      dOut.innerHTML =
        '<div class="tags">' + r.tags.map(function (t) { return '<span class="tag">' + esc(t) + "</span>"; }).join("") + "</div>" +
        '<table class="facts"><caption class="visually-hidden">Properties of ' + r.input + "</caption><tbody>" +
        rows.map(function (x) { return "<tr><th scope=row>" + x[0] + "</th><td>" + esc(x[1]) + "</td></tr>"; }).join("") + "</tbody></table>" +
        '<div class="btns" style="margin-top:18px">' + links.join("") + "</div>" +
        '<p class="small muted" style="margin-top:16px">Neighbours: ' + (r.n > 0 ? nb(r.n - 1) : "") + nb(r.n + 1) + (r.prevPrime ? nb(r.prevPrime) : "") + (r.nextPrime ? nb(r.nextPrime) : "") + "</p>";
    };
    dForm.addEventListener("submit", function (e) { e.preventDefault(); runDecode(dIn.value); });
    dIn.value = params.get("n") || "36118"; runDecode(dIn.value);
  }

  /* ---------- Lucky number reader ---------- */
  var lForm = $("#luckyForm");
  if (lForm) {
    var lIn = $("#luckyInput"), lOut = $("#luckyOut");
    var runLucky = function (val) {
      var s = N36.clean(val);
      if (!s || s.length > 20) { lOut.innerHTML = '<p class="result-empty">Enter between 1 and 20 digits — a phone number, plate, address or price.</p>'; return; }
      history.replaceState(null, "", "?n=" + s);
      var L = N36.lucky(s), M = N36.memorability(s), dr = s.split("").reduce(function (a, c) { return a + +c; }, 0);
      while (dr > 9) dr = String(dr).split("").reduce(function (a, c) { return a + +c; }, 0);
      var verdict = L.score >= 75 ? "Strongly auspicious" : L.score >= 60 ? "Auspicious" : L.score >= 45 ? "Neutral" : "Often avoided";
      lOut.innerHTML =
        '<div class="kpis"><div><strong>' + L.score + '</strong><span class="muted">Cultural luck / 100</span></div>' +
        '<div><strong>' + M.score + '</strong><span class="muted">Memorability / 100</span></div>' +
        '<div><strong>' + dr + '</strong><span class="muted">Digital root</span></div></div>' +
        '<div class="score-bar" aria-hidden="true"><span style="width:' + L.score + '%"></span></div>' +
        "<p><strong>" + verdict + ".</strong> " + (L.notes.join(". ") || "No special positional signals.") + "</p>" +
        (L.combos.length ? "<h3>Combinations found</h3><ul>" + L.combos.map(function (c) { return "<li>" + esc(c) + "</li>"; }).join("") + "</ul>" : "") +
        "<h3>Digit by digit</h3><table class=facts><tbody>" + L.digits.map(function (d) {
          return "<tr><th scope=row><span class='tile' style='width:34px;height:44px;font-size:1.4rem;display:inline-grid'>" + d.d + "</span></th><td>" + esc(d.note) + "</td></tr>";
        }).join("") + "</tbody></table>" +
        (M.why.length ? "<h3>Why it sticks in memory</h3><ul>" + M.why.map(function (w) { return "<li>" + esc(w) + "</li>"; }).join("") + "</ul>" : "") +
        '<p class="small muted">Readings reflect common Chinese homophone associations and are offered for cultural interest and entertainment. They do not predict outcomes.</p>';
    };
    lForm.addEventListener("submit", function (e) { e.preventDefault(); runLucky(lIn.value); });
    lIn.value = params.get("n") || "36118"; runLucky(lIn.value);
  }

  /* ---------- Domain scorecard ---------- */
  var vForm = $("#valueForm");
  if (vForm) {
    var vIn = $("#valueInput"), vOut = $("#valueOut");
    var runValue = function (val) {
      var r = N36.domainScore(val);
      if (r.error) { vOut.innerHTML = '<p class="result-empty">' + esc(r.error) + "</p>"; return; }
      history.replaceState(null, "", "?d=" + encodeURIComponent(r.domain));
      vOut.innerHTML =
        '<div class="kpis"><div><strong>' + r.score.toFixed(1) + '</strong><span class="muted">Liquidity score / 10</span></div>' +
        '<div><strong>' + r.tier + '</strong><span class="muted">Tier</span></div>' +
        '<div><strong>' + (r.numeric ? r.sld.length + "N" : r.sld.length + " chars") + '</strong><span class="muted">Class</span></div></div>' +
        '<div class="score-bar" aria-hidden="true"><span style="width:' + r.score * 10 + '%"></span></div>' +
        "<h3>How the score was built</h3><table class=facts><tbody>" + r.factors.map(function (f) {
          return "<tr><th scope=row>" + (f.pts > 0 ? "+" : "") + f.pts + "</th><td class='" + (f.good ? "" : "") + "'>" + esc(f.label) + "</td></tr>";
        }).join("") + "</tbody></table>" +
        '<div class="callout"><strong>Want a real number?</strong> A liquidity score ranks how easily a name sells; it is not a price. Request a human appraisal with comparable sales, or ask us to find a buyer. ' +
        '<a href="' + root + 'services.html?intent=Appraise&domain=' + encodeURIComponent(r.domain) + '">Request an appraisal</a></div>';
      var hidden = $("#leadDomain"); if (hidden) hidden.value = r.domain;
    };
    vForm.addEventListener("submit", function (e) { e.preventDefault(); runValue(vIn.value); });
    vIn.value = params.get("d") || "36118.com"; runValue(vIn.value);
  }

  /* ---------- ZIP / postal code explorer (Zippopotam.us open API) ---------- */
  var zForm = $("#zipForm");
  if (zForm) {
    var zIn = $("#zipInput"), zC = $("#zipCountry"), zOut = $("#zipOut");
    var runZip = function () {
      var code = zIn.value.trim(), c = zC.value;
      if (!code) { zOut.innerHTML = '<p class="result-empty">Enter a postal code.</p>'; return; }
      history.replaceState(null, "", "?zip=" + encodeURIComponent(code) + "&c=" + c);
      zOut.innerHTML = '<p class="muted">Looking up ' + esc(code) + "…</p>";
      fetch("https://api.zippopotam.us/" + c + "/" + encodeURIComponent(code))
        .then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); })
        .then(function (j) {
          var p = j.places[0], lat = +p.latitude, lon = +p.longitude, d = .06;
          var bbox = [lon - d, lat - d, lon + d, lat + d].join(",");
          zOut.innerHTML =
            "<h3>" + esc(j["post code"]) + " — " + esc(p["place name"]) + ", " + esc(p["state abbreviation"] || p.state || "") + " " + esc(j["country abbreviation"]) + "</h3>" +
            '<table class="facts"><tbody>' +
            "<tr><th scope=row>Country</th><td>" + esc(j.country) + "</td></tr>" +
            "<tr><th scope=row>State / region</th><td>" + esc(p.state || "—") + "</td></tr>" +
            "<tr><th scope=row>Places on this code</th><td>" + j.places.map(function (x) { return esc(x["place name"]); }).join(", ") + "</td></tr>" +
            "<tr><th scope=row>Latitude, longitude</th><td>" + lat.toFixed(4) + ", " + lon.toFixed(4) + "</td></tr></tbody></table>" +
            '<iframe class="map" style="margin-top:16px" loading="lazy" title="Map of ' + esc(j["post code"]) + '" src="https://www.openstreetmap.org/export/embed.html?bbox=' + bbox + "&layer=mapnik&marker=" + lat + "," + lon + '"></iframe>' +
            '<p class="small muted">Map © OpenStreetMap contributors. Postal data: Zippopotam.us.</p>';
          zOut.setAttribute("data-lat", lat); zOut.setAttribute("data-lon", lon);
        })
        .catch(function () {
          zOut.innerHTML = '<p class="result-empty">No public record found for ' + esc(code) + " in " + esc(zC.options[zC.selectedIndex].text) +
            ". Unique ZIP codes (single organisations like 36118) and PO-box-only codes are often missing from open datasets. Check the format, or try a nearby code.</p>";
        });
    };
    zForm.addEventListener("submit", function (e) { e.preventDefault(); runZip(); });
    zIn.value = params.get("zip") || "36117"; if (params.get("c")) zC.value = params.get("c"); runZip();

    var dist = $("#distForm");
    if (dist) dist.addEventListener("submit", function (e) {
      e.preventDefault();
      var a = $("#distA").value.trim(), b = $("#distB").value.trim(), c = $("#distC").value, o = $("#distOut");
      o.textContent = "Measuring…";
      Promise.all([a, b].map(function (z) { return fetch("https://api.zippopotam.us/" + c + "/" + encodeURIComponent(z)).then(function (r) { if (!r.ok) throw 0; return r.json(); }); }))
        .then(function (js) {
          var p1 = js[0].places[0], p2 = js[1].places[0], R = 6371, rad = Math.PI / 180;
          var dLat = (p2.latitude - p1.latitude) * rad, dLon = (p2.longitude - p1.longitude) * rad;
          var h = Math.sin(dLat / 2) ** 2 + Math.cos(p1.latitude * rad) * Math.cos(p2.latitude * rad) * Math.sin(dLon / 2) ** 2;
          var km = 2 * R * Math.asin(Math.sqrt(h));
          o.innerHTML = "<strong>" + km.toFixed(1) + " km</strong> (" + (km * 0.621371).toFixed(1) + " miles) in a straight line from " + esc(p1["place name"]) + " to " + esc(p2["place name"]) + ". Driving distance is usually 20–40% longer.";
        })
        .catch(function () { o.textContent = "One of those codes wasn't found. Check both and try again."; });
    });
  }

  /* ---------- Lead funnel (multi-step) ---------- */
  var funnel = $("#leadForm");
  if (funnel) {
    var steps = funnel.querySelectorAll(".fstep"), marks = document.querySelectorAll("#leadSteps li"), cur = 0;
    var show = function (i) {
      cur = i; steps.forEach(function (s, k) { s.hidden = k !== i; });
      marks.forEach(function (m, k) { m.classList.toggle("on", k <= i); });
      var f = steps[i].querySelector("input,select,textarea"); if (f && i > 0) f.focus();
    };
    funnel.addEventListener("click", function (e) {
      if (e.target.matches("[data-next]")) {
        var fields = steps[cur].querySelectorAll("input,select,textarea"), ok = true;
        fields.forEach(function (f) { if (ok && !f.checkValidity()) { f.reportValidity(); ok = false; } });
        if (ok) show(cur + 1);
      }
      if (e.target.matches("[data-back]")) show(cur - 1);
    });
    var pre = params.get("intent"); if (pre) { var r = funnel.querySelector('input[name=intent][value="' + pre + '"]'); if (r) r.checked = true; }
    funnel.onBeforeSend = function (data) {
      var score = 0, budget = data.budget || "";
      if (/50,000|100,000|\+/.test(budget)) score += 3; else if (/10,000|25,000/.test(budget)) score += 2; else if (/2,500|5,000/.test(budget)) score += 1;
      if (/Now|30 days/.test(data.timeline || "")) score += 2;
      if (data.phone) score += 1; if (data.company) score += 1;
      data.lead_grade = score >= 5 ? "HOT" : score >= 3 ? "WARM" : "NURTURE";
    };
    funnel.onSent = function () { show(0); };
    show(0);
  }

  /* ---------- Donations: allocation sliders ---------- */
  var alloc = $("#allocForm");
  if (alloc) {
    var sliders = alloc.querySelectorAll("input[type=range]");
    var sync = function () {
      var tot = 0; sliders.forEach(function (s) { tot += +s.value; });
      sliders.forEach(function (s) { var o = $("#" + s.id + "Out"); o.textContent = tot ? Math.round(s.value / tot * 100) + "%" : "0%"; });
      $("#allocSummary").value = Array.prototype.map.call(sliders, function (s) { return s.getAttribute("data-label") + " " + $("#" + s.id + "Out").textContent; }).join(", ");
    };
    sliders.forEach(function (s) { s.addEventListener("input", sync); }); sync();
    alloc.addEventListener("change", function (e) {
      if (e.target.name === "amount") { var c = $("#customAmount"); c.required = e.target.value === "Custom"; c.parentElement.hidden = e.target.value !== "Custom"; }
    });
  }

  /* ---------- Number of the day (deterministic, same for every visitor) ---------- */
  var nod = $("#nod");
  if (nod) {
    var d = new Date(), seed = d.getUTCFullYear() * 10000 + (d.getUTCMonth() + 1) * 100 + d.getUTCDate();
    var x = (seed * 2654435761) % 4294967296; var n = 100 + (x % 99900);
    var r = N36.analyze(String(n));
    nod.innerHTML = '<a class="pill-link" style="font-size:1.4rem" href="' + root + 'tools/number-decoder.html?n=' + n + '">' + n + "</a> " +
      '<span class="muted">' + (r.prime ? "a prime" : N36.factorString(r)) + " — " + r.tags.slice(0, 3).join(", ") + "</span>";
  }
})();

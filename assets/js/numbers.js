/* 36118.com number engine — pure client-side, no data leaves the browser. */
(function (g) {
  "use strict";
  var MAX = 999999999999999; // 15 digits keeps factorisation fast and exact in IEEE doubles

  function clean(v) { return String(v == null ? "" : v).replace(/[^0-9]/g, "").replace(/^0+(?=\d)/, ""); }

  function factor(n) {
    var f = [], m = n, d;
    while (m % 2 === 0 && m > 1) { f.push(2); m /= 2; }
    while (m % 3 === 0 && m > 1) { f.push(3); m /= 3; }
    for (d = 5; d * d <= m; d += 6) {
      while (m % d === 0) { f.push(d); m /= d; }
      while (m % (d + 2) === 0) { f.push(d + 2); m /= (d + 2); }
    }
    if (m > 1) f.push(m);
    return f;
  }
  function group(f) { var o = {}; f.forEach(function (p) { o[p] = (o[p] || 0) + 1; }); return o; }
  function isPrime(n) { if (n < 2) return false; var f = factor(n); return f.length === 1; }
  function sigma(gp) { var s = 1; for (var p in gp) { var k = gp[p], P = +p, t = 1, pw = 1; for (var i = 0; i < k; i++) { pw *= P; t += pw; } s *= t; } return s; }
  function tau(gp) { var t = 1; for (var p in gp) t *= gp[p] + 1; return t; }
  function phi(n, gp) { var r = n; for (var p in gp) r = r / +p * (+p - 1); return Math.round(r); }
  function prevPrime(n) { for (var k = n - 1; k >= 2; k--) if (isPrime(k)) return k; return null; }
  function nextPrime(n) { for (var k = n + 1; k < n + 100000; k++) if (isPrime(k)) return k; return null; }
  function isSquare(n) { var r = Math.round(Math.sqrt(n)); return r * r === n; }
  function isCube(n) { var r = Math.round(Math.cbrt(n)); return r * r * r === n; }
  function isTriangular(n) { return isSquare(8 * n + 1); }
  function isFib(n) { return isSquare(5 * n * n + 4) || isSquare(5 * n * n - 4); }
  function digitSum(s) { return s.split("").reduce(function (a, c) { return a + (+c); }, 0); }
  function digitalRoot(n) { return n === 0 ? 0 : 1 + ((n - 1) % 9); }

  var ONES = ["zero","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"];
  var TENS = ["","","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"];
  var SCALE = ["","thousand","million","billion","trillion"];
  function words3(n) {
    var s = [], h = Math.floor(n / 100), r = n % 100;
    if (h) s.push(ONES[h] + " hundred");
    if (r) { if (r < 20) s.push(ONES[r]); else s.push(TENS[Math.floor(r / 10)] + (r % 10 ? "-" + ONES[r % 10] : "")); }
    return s.join(" ");
  }
  function toWords(n) {
    if (n === 0) return "zero";
    var parts = [], i = 0;
    while (n > 0 && i < SCALE.length) { var c = n % 1000; if (c) parts.unshift(words3(c) + (SCALE[i] ? " " + SCALE[i] : "")); n = Math.floor(n / 1000); i++; }
    return parts.join(" ");
  }
  function toRoman(n) {
    if (n < 1 || n > 3999) return null;
    var map = [[1000,"M"],[900,"CM"],[500,"D"],[400,"CD"],[100,"C"],[90,"XC"],[50,"L"],[40,"XL"],[10,"X"],[9,"IX"],[5,"V"],[4,"IV"],[1,"I"]], r = "";
    map.forEach(function (m) { while (n >= m[0]) { r += m[1]; n -= m[0]; } });
    return r;
  }

  /* Chinese homophone associations (cultural, Mandarin/Cantonese). Weights are our editorial model. */
  var CN = {
    "0": { w: 0,  note: "零 líng — wholeness or emptiness; neutral" },
    "1": { w: 1,  note: "一 yī / 幺 yāo — unity; in pairs it echoes 要 'want'" },
    "2": { w: 3,  note: "二 èr — 'good things come in pairs'" },
    "3": { w: 3,  note: "三 sān — in Cantonese sounds like 生 'life, birth'" },
    "4": { w: -8, note: "四 sì — sounds like 死 'death'; widely avoided" },
    "5": { w: -1, note: "五 wǔ — can sound like 无 'not, without'; mixed" },
    "6": { w: 5,  note: "六 liù — 'flowing, smooth' (六六大顺)" },
    "7": { w: 0,  note: "七 qī — togetherness, but linked to ghost month; mixed" },
    "8": { w: 8,  note: "八 bā — close to 发 fā 'prosper'; the luckiest digit" },
    "9": { w: 5,  note: "九 jiǔ — sounds like 久 'long-lasting'" }
  };
  var COMBOS = [
    ["168", 8, "一路发 'prosperity all the way'"], ["518", 7, "我要发 'I will prosper'"], ["888", 9, "triple prosperity"],
    ["88", 5, "double prosperity"], ["66", 4, "double smoothness"], ["99", 4, "doubly long-lasting"], ["118", 4, "要要发 'want, want, prosper'"],
    ["289", 3, "easy-to-prosper-long"], ["14", -6, "要死 — strongly avoided"], ["514", -6, "我要死 — strongly avoided"], ["44", -6, "double 4"]
  ];

  function lucky(s) {
    var score = 50, notes = [], combos = [];
    s.split("").forEach(function (d) { score += CN[d].w; });
    COMBOS.forEach(function (c) { if (s.indexOf(c[0]) > -1) { score += c[1]; combos.push(c[0] + " — " + c[2]); } });
    if (/8$/.test(s)) { score += 4; notes.push("Ends in 8 — the strongest position for prosperity"); }
    if (s.indexOf("4") === -1) { score += 4; notes.push("No 4 anywhere — what Chinese buyers call a 'chip' number when 0 is also absent"); }
    var len = s.length; score = Math.round(Math.max(0, Math.min(100, score + (len <= 4 ? 4 : 0))));
    return { score: score, combos: combos, notes: notes, digits: s.split("").map(function (d) { return { d: d, note: CN[d].note, w: CN[d].w }; }) };
  }

  function memorability(s) {
    var score = 100 - Math.max(0, s.length - 3) * 9, why = [];
    var uniq = new Set(s.split("")).size;
    if (uniq <= 2) { score += 15; why.push("Only " + uniq + " distinct digits"); }
    if (/(\d)\1{2,}/.test(s)) { score += 10; why.push("Contains a run of repeated digits"); }
    if (s === s.split("").reverse().join("")) { score += 10; why.push("Palindrome — reads the same both ways"); }
    if (/(?:0123|1234|2345|3456|4567|5678|6789|9876|8765|7654|6543|5432|4321)/.test(s)) { score += 8; why.push("Contains a straight sequence"); }
    if (/^(\d\d)\1+$/.test(s) || /^(\d\d\d)\1+$/.test(s)) { score += 10; why.push("Repeating block pattern"); }
    if (/(\d)\1/.test(s)) { score += 4; why.push("Has a doubled digit"); }
    return { score: Math.max(5, Math.min(100, score)), why: why };
  }

  function analyze(raw) {
    var s = clean(raw);
    if (!s) return { error: "Type a whole number, for example 36118." };
    var n = Number(s);
    if (n > MAX) return { error: "That number has more than 15 digits. Try one with 15 digits or fewer." };
    var r = { input: s, n: n, digits: s.length };
    r.even = n % 2 === 0;
    r.digitSum = digitSum(s);
    r.digitalRoot = digitalRoot(n);
    r.reverse = s.split("").reverse().join("").replace(/^0+(?=\d)/, "");
    r.palindrome = s === s.split("").reverse().join("");
    if (n >= 2) {
      r.factors = factor(n); r.groups = group(r.factors);
      r.prime = r.factors.length === 1;
      r.distinctPrimes = Object.keys(r.groups).length;
      r.divisorCount = tau(r.groups);
      r.sigma = sigma(r.groups);
      r.aliquot = r.sigma - n;
      r.phi = phi(n, r.groups);
      r.semiprime = r.factors.length === 2;
      r.squarefree = Object.keys(r.groups).every(function (p) { return r.groups[p] === 1; });
      r.kind = r.aliquot === n ? "perfect" : (r.aliquot > n ? "abundant" : "deficient");
      if (n < 1e9) { r.prevPrime = prevPrime(n); r.nextPrime = nextPrime(n); }
    } else { r.factors = []; r.prime = false; }
    r.square = isSquare(n); r.cube = isCube(n); r.triangular = isTriangular(n); r.fibonacci = n < 1e15 && isFib(n);
    r.harshad = n > 0 && n % r.digitSum === 0;
    r.bin = n.toString(2); r.oct = n.toString(8); r.hex = n.toString(16).toUpperCase(); r.b36 = n.toString(36).toUpperCase();
    r.words = toWords(n); r.roman = toRoman(n);
    r.sci = n >= 1000 ? n.toExponential(3).replace("e+", " × 10^") : null;
    r.sqrt = Math.sqrt(n); r.log10 = n > 0 ? Math.log10(n) : null;
    r.benfordFirst = +s[0];
    r.lucky = lucky(s); r.memo = memorability(s);
    r.chip = s.indexOf("0") === -1 && s.indexOf("4") === -1;
    r.asZip = s.length === 5; r.asYear = n >= 1000 && n <= 2999;
    r.tags = [];
    if (r.prime) r.tags.push("prime"); if (r.semiprime) r.tags.push("semiprime"); if (r.even) r.tags.push("even"); else r.tags.push("odd");
    if (r.square) r.tags.push("perfect square"); if (r.cube) r.tags.push("perfect cube"); if (r.triangular) r.tags.push("triangular");
    if (r.fibonacci) r.tags.push("Fibonacci"); if (r.harshad) r.tags.push("Harshad"); if (r.palindrome) r.tags.push("palindrome");
    if (r.kind) r.tags.push(r.kind); if (r.squarefree && n > 1) r.tags.push("square-free"); if (r.chip && s.length >= 3) r.tags.push("chip (no 0 or 4)");
    return r;
  }

  function factorString(r) {
    if (!r.groups) return "—";
    return Object.keys(r.groups).map(function (p) { return r.groups[p] > 1 ? p + "^" + r.groups[p] : p; }).join(" × ");
  }

  /* Domain liquidity model — a transparent scorecard, not a price. */
  var TLD = { com: 1, net: .45, org: .4, cn: .5, "com.cn": .35, io: .35, ai: .45, co: .3, in: .3, de: .3, uk: .3, "co.uk": .3, app: .25, xyz: .12, info: .15, biz: .12 };
  function domainScore(raw) {
    var d = String(raw || "").trim().toLowerCase().replace(/^https?:\/\//, "").replace(/^www\./, "").split("/")[0];
    if (!/^[a-z0-9-]+(\.[a-z0-9-]+)+$/.test(d)) return { error: "Enter a domain like 36118.com" };
    var parts = d.split("."), sld = parts[0], tld = parts.slice(1).join(".");
    var f = [], s = 0, add = function (pts, label, good) { s += pts; f.push({ pts: pts, label: label, good: good }); };
    var t = TLD[tld] != null ? TLD[tld] : .1;
    var numeric = /^\d+$/.test(sld), L = sld.length;
    if (numeric) {
      var lenPts = { 1: 44, 2: 40, 3: 34, 4: 26, 5: 17, 6: 6, 7: 0 }[L]; if (lenPts == null) lenPts = -6;
      add(lenPts, L + "N — " + L + "-digit name; scarcity drops tenfold with every extra digit", lenPts >= 17);
      var lk = lucky(sld);
      if (sld.indexOf("4") === -1 && sld.indexOf("0") === -1) add(8, "Chip: no 0 or 4, preferred by Chinese end users", true);
      else if (sld.indexOf("4") > -1) add(-8, "Contains 4, which many Chinese buyers avoid", false);
      if (sld[0] === "0") add(-6, "Leading zero is easy to mistype or drop", false);
      if (/8$/.test(sld)) add(4, "Ends in 8 (prosperity)", true);
      var m = memorability(sld);
      if (m.why.length) add(Math.min(10, m.why.length * 3), "Pattern: " + m.why.join("; "), true);
      add(Math.round((lk.score - 50) / 5), "Cultural luck score " + lk.score + "/100", lk.score >= 55);
    } else {
      var hasDigit = /\d/.test(sld), hy = (sld.match(/-/g) || []).length;
      var lp = L <= 3 ? 34 : L <= 5 ? 26 : L <= 8 ? 18 : L <= 12 ? 10 : 4;
      add(lp, L + " characters long", lp >= 18);
      if (hy) add(-6 * hy, hy + " hyphen(s) cut type-in and radio value", false);
      if (hasDigit) add(-4, "Mixes letters and digits", false);
      var v = (sld.match(/[aeiouy]/g) || []).length / Math.max(1, L);
      if (v >= .25 && v <= .6) add(6, "Pronounceable letter balance", true); else add(-4, "Hard to pronounce letter mix", false);
    }
    add(Math.round(30 * t) - 10, "." + tld + " extension weight " + Math.round(t * 100) + "% of .com", t >= .45);
    var score = Math.max(0, Math.min(10, Math.round(s / 7.5 * 10) / 10));
    var tier = score >= 8.5 ? "A+" : score >= 7 ? "A" : score >= 5.5 ? "B" : score >= 4 ? "C" : "D";
    return { domain: d, sld: sld, tld: tld, numeric: numeric, score: score, tier: tier, factors: f };
  }

  g.N36 = { analyze: analyze, factorString: factorString, lucky: lucky, memorability: memorability, domainScore: domainScore, clean: clean, toWords: toWords };
})(window);

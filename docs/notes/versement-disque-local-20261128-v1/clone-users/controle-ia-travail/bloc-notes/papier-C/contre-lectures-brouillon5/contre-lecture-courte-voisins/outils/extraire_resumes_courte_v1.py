"""Extrait le bloc de resume d'une page HTML empreintee (arXiv, anthologie ACL, page d'editeur) et le confronte aux
declencheurs de la regle du verrou 2. Usage : python3 -I -B extraire_resumes_courte_v1.py FICHIER.html ..."""
import hashlib, html, re, sys
MOTIFS = [r"monitor", r"destination", r"fixed point", r"attractor", r"graded", r"intensit", r"dose", r"regress",
          r"probe", r"probing", r"activation", r"internal", r"encode", r"logit", r"linear"]
for chemin in sys.argv[1:]:
    brut = open(chemin, "rb").read()
    t = brut.decode("utf-8", "replace")
    m = (re.search(r'<blockquote class="abstract[^"]*">(.*?)</blockquote>', t, re.S)
         or re.search(r'<div class="card-body acl-abstract">(.*?)</div>', t, re.S)
         or re.search(r'id="Abs1-content"[^>]*>(.*?)</div>', t, re.S))
    print("=" * 100)
    print(chemin.split("/")[-1], hashlib.sha256(brut).hexdigest())
    if not m:
        print("RESUME NON TROUVE"); continue
    r = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", m.group(1)))).strip()
    print(r)
    print("declencheurs :", sorted({mo for mo in MOTIFS if re.search(mo, r, re.I)}))

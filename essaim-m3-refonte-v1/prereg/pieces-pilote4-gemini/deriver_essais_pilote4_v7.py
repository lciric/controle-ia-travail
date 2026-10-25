"""Dérive la batterie d'essais v7 du lanceur du pilote 4 de la batterie v6 (`essais_lanceur_pilote4_v6.sh`, b4857c51…),
par remplacements exacts au nombre attendu, pour le lanceur v6 — sur la série v7 (batterie v6 sur le lanceur v5 : 215 cas
sur 218) :

- défaut de la batterie v6 (cas `seg-noyau-refuse-code`) : la vérification lisait la sortie standard du cas du segment 1
  (`$RS/sortie.txt`) au lieu de celle du cas de la reprise refusée (`$E/cas-seg-noyau-refuse/sortie.txt`) ; le cas
  lui-même (« reprise refusée par le noyau (code 9 ») était conforme ;
- les deux autres écarts (`seg-clore-extrait`, `seg-clore-v53-refusee`) venaient du lanceur v5 (extrait mécanique sans
  `cd "$R"` avec `CLORE=1`), corrigé par le lanceur v6 ; les cas ne changent pas ;
- lanceur v6 nommé (cas `m-sous-lanceur-pilote4`) ; en-tête et usage.

Usage : python3 -I deriver_essais_pilote4_v7.py ESSAIS_V6 SORTIE
Refuse si l'empreinte de la batterie v6 n'est pas b4857c51…, si une occurrence n'est pas au nombre attendu, ou si SORTIE
existe (R12).
"""
import hashlib, pathlib, sys

SHA_V6 = "b4857c51b8daafdd8264019de9c308e3ba611703595062310b7035cb09aa5228"
src, sortie = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
if sortie.exists():
    sys.exit(f"refus : {sortie} existe déjà (R12)")
b = src.read_bytes()
if hashlib.sha256(b).hexdigest() != SHA_V6:
    sys.exit("refus : la batterie source n'est pas la v6 b4857c51…")
t = b.decode("utf-8")

remplacements = [
    ("# plus), v6 : la v5 (e216c39e…) par `deriver_essais_pilote4_v6.py` pour le lanceur v5 (reprise par segments, 75 USD par\n"
     "# course, minuteur à 3 400 s) ; la v5 était dérivée",
     "# plus), v7 : la v6 (b4857c51…) par `deriver_essais_pilote4_v7.py` pour le lanceur v6 (vérification de la reprise\n"
     "# refusée corrigée) ; la v6 était dérivée de la v5 (e216c39e…) par `deriver_essais_pilote4_v6.py` pour le lanceur v5\n"
     "# (reprise par segments, 75 USD par course, minuteur à 3 400 s) ; la v5 était dérivée", 1),
    ("# Usage : bash essais_lanceur_pilote4_v6.sh ", "# Usage : bash essais_lanceur_pilote4_v7.sh ", 1),
    ("lanceur : lancer_pilote4_gemini_v5.sh, sha256 $H/", "lanceur : lancer_pilote4_gemini_v6.sh, sha256 $H/", 1),
    ('verifier seg-noyau-refuse-code "reprise refusée par le noyau" "$RS/sortie.txt"\n',
     'verifier seg-noyau-refuse-code "reprise refusée par le noyau" "$E/cas-seg-noyau-refuse/sortie.txt"\n', 1),
]
for ancien, nouveau, n in remplacements:
    k = t.count(ancien)
    if k != n:
        sys.exit(f"refus : {k} occurrence(s) au lieu de {n} pour : {ancien[:90]!r}")
    t = t.replace(ancien, nouveau)
if "lancer_pilote4_gemini_v5.sh" in t:
    sys.exit("refus : le lanceur v5 est encore nommé")
sortie.write_text(t, encoding="utf-8")
print(f"batterie écrite : {sortie.name} {hashlib.sha256(sortie.read_bytes()).hexdigest()} ; {len(remplacements)} remplacements")

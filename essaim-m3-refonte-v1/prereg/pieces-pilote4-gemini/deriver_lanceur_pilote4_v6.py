"""Dérive le lanceur v6 du quatrième pilote descriptif du lanceur v5 (`lancer_pilote4_gemini_v5.sh`, 565f5205…), par
remplacements exacts, chacun au nombre d'occurrences attendu — sur la série v7 (batterie v6 sur le lanceur v5 : 215 cas
sur 218 ; `essais-lanceur-pilote4-v7.log`) :

- défaut du lanceur v5 trouvé par la série v7 (cas `seg-clore-extrait` et `seg-clore-v53-refusee`) : avec `CLORE=1`, les
  étapes 4 à 7 sont sautées, donc aussi le `cd "$R"` de l'étape 7 ; l'extrait mécanique de l'étape 8a
  (`python -m essaim_m3.outils.extrait_mecanique`, lancé depuis le dossier courant) ne trouve plus le paquet et refuse :
  la course fermée sans reprise n'a pas d'extrait. Correction : `cd "$R"` dans la branche `CLORE=1`, avant la fermeture ;
- en-tête et usage (version, nom du lanceur, écart consigné dans `diff-lanceur-pilote4-v5-vers-v6.txt`).

Rien d'autre ne change.

Usage : python3 -I deriver_lanceur_pilote4_v6.py LANCEUR_V5 SORTIE
Refuse si l'empreinte du lanceur v5 n'est pas 565f5205…, si une occurrence n'est pas au nombre attendu, si un reste
interdit subsiste, ou si SORTIE existe (R12).
"""
import hashlib, pathlib, sys

SHA_V5 = "565f5205fd4a3888565182f74081f047d71f92dabf1d913171cd81f8317a9ffd"
src, sortie = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
if sortie.exists():
    sys.exit(f"refus : {sortie} existe déjà (R12)")
b = src.read_bytes()
if hashlib.sha256(b).hexdigest() != SHA_V5:
    sys.exit("refus : le lanceur source n'est pas la v5 565f5205…")
t = b.decode("utf-8")

remplacements = [
    ("# une course en un ou plusieurs segments (COURSE=v5-3, puis COURSE=v6-1 ; SEGMENT=1, 2, …) — v5 : le lanceur v4\n"
     "# (f335440c…) par `deriver_lanceur_pilote4_v5.py` (reprise par segments du noyau 8e5e2f7b : une course arrêtée par le STOP\n",
     "# une course en un ou plusieurs segments (COURSE=v5-3, puis COURSE=v6-1 ; SEGMENT=1, 2, …) — v6 : le lanceur v5\n"
     "# (565f5205…) par `deriver_lanceur_pilote4_v6.py` (avec CLORE=1, l'extrait mécanique est lancé depuis le dépôt ; écart\n"
     "# consigné dans `diff-lanceur-pilote4-v5-vers-v6.txt`), la v5 dérivée du lanceur v4\n"
     "# (f335440c…) par `deriver_lanceur_pilote4_v5.py` (reprise par segments du noyau 8e5e2f7b : une course arrêtée par le STOP\n", 1),
    ("#       bash lancer_pilote4_gemini_v5.sh\n", "#       bash lancer_pilote4_gemini_v6.sh\n", 1),
    ('else\n  CODE=""\n  note "- CLORE=1 : aucune reprise, aucun appel ;',
     'else\n  CODE=""\n  cd "$R"   # v6 : l\'étape 8a lance l\'extrait mécanique depuis le dépôt (`python -m essaim_m3.outils.extrait_mecanique`)\n'
     '  note "- CLORE=1 : aucune reprise, aucun appel ;', 1),
]
for ancien, nouveau, n in remplacements:
    k = t.count(ancien)
    if k != n:
        sys.exit(f"refus : {k} occurrence(s) au lieu de {n} pour : {ancien[:90]!r}")
    t = t.replace(ancien, nouveau)
for motif in ("lancer_pilote4_gemini_v5.sh\n",):
    if motif in t:
        sys.exit(f"refus : motif restant après dérivation : {motif!r}")
n_cd = t.count('cd "$R"')
if n_cd != 5:  # quatre dans la v5 (dont trois sous-coquilles « (cd "$R" && … ») et un de plus, celui de la branche CLORE=1
    sys.exit(f'refus : « cd "$R" » présent {n_cd} fois au lieu de 5')
sortie.write_text(t, encoding="utf-8")
print(f"lanceur écrit : {sortie.name} {hashlib.sha256(sortie.read_bytes()).hexdigest()} ; {len(remplacements)} remplacements")

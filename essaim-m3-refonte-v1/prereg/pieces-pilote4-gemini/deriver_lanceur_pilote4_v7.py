"""Dérive le lanceur v7 du quatrième pilote descriptif du lanceur v6 (`lancer_pilote4_gemini_v6.sh`, 50f9c496…), par
remplacements exacts, chacun au nombre d'occurrences attendu — décision de Lazar (25 octobre 2026, 23:54 Paris) sur
l'objet de la seconde course : « c) tout attendre la v6.2 » :

- objet de la seconde course : la **v6.2** de Gemini (branche `canal/gemini-organisme-v6-2`, commit
  `fedb06525610c05945f8496c2058c21a15256fca`, dossier `organisme/`, 24 fichiers, empreinte d'arbre
  `d02c2907c8eaafb5c9c6768d739b415bfe3d9733a4342b8a16ad77eb19fdb252`) à la place de la v6.1 (`a9d8eb5`, `ae331d1d…`) ;
- donc la clé de course `v6-2` (au lieu de `v6-1`), le nom `pilote4-gemini-v6-2-v1`, la lignée `gemini-organisme-v6-2`,
  et « v6.2 » dans les messages ; le texte nommé dans l'en-tête : `pilote4-gemini-organisme-v4.md` ;
- en-tête (version, usage).

Rien d'autre ne change : noyau `8e5e2f7b`, banque v3, segments, minuteur, porte « v5.3 précédente », gardes, fermeture,
liste fermée sont la ligne du lanceur v6.

Usage : python3 -I deriver_lanceur_pilote4_v7.py LANCEUR_V6 SORTIE
Refuse si l'empreinte du lanceur v6 n'est pas 50f9c496…, si une occurrence n'est pas au nombre attendu, si un reste
de la v6.1 subsiste, ou si SORTIE existe (R12).
"""
import hashlib, pathlib, sys

SHA_V6 = "50f9c49645ef93bd2bf213be3ed1b8b022cb3422615d06a8b2b6c7ac7fe2dbc9"
src, sortie = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
if sortie.exists():
    sys.exit(f"refus : {sortie} existe déjà (R12)")
b = src.read_bytes()
if hashlib.sha256(b).hexdigest() != SHA_V6:
    sys.exit("refus : le lanceur source n'est pas la v6 50f9c496…")
t = b.decode("utf-8")

# l'ordre compte : les remplacements globaux d'abord, puis l'en-tête nouveau (qui nomme la v6.1 pour l'histoire)
remplacements = [
    ("v6-1", "v6-2", 9),
    ("v6.1", "v6.2", 11),
    ("a9d8eb50c02c8f5ea31b060b3c0e86f23c2d1dbc", "fedb06525610c05945f8496c2058c21a15256fca", 1),
    ("ae331d1deb660a20da919edbdcdecba28e49b9b143a6b7a061262101a79798d4",
     "d02c2907c8eaafb5c9c6768d739b415bfe3d9733a4342b8a16ad77eb19fdb252", 1),
    ("# v6.2 = branche de Gemini, commit `a9d8eb5`, arbre `ae331d1d…`, 24 fichiers ; lignées « assistées ».",
     "# v6.2 = branche `canal/gemini-organisme-v6-2`, commit `fedb065`, arbre `d02c2907…`, 24 fichiers ; lignées « assistées ».", 1),
    ("# une course en un ou plusieurs segments (COURSE=v5-3, puis COURSE=v6-2 ; SEGMENT=1, 2, …) — v6 : le lanceur v5\n"
     "# (565f5205…) par `deriver_lanceur_pilote4_v6.py` (avec CLORE=1, l'extrait mécanique est lancé depuis le dépôt ; écart\n"
     "# consigné dans `diff-lanceur-pilote4-v5-vers-v6.txt`), la v5 dérivée du lanceur v4\n",
     "# une course en un ou plusieurs segments (COURSE=v5-3, puis COURSE=v6-2 ; SEGMENT=1, 2, …) — v7 : le lanceur v6\n"
     "# (50f9c496…) par `deriver_lanceur_pilote4_v7.py` (objet de la seconde course : la v6.2 à la place de la v6.1, décision\n"
     "# de Lazar du 25 octobre 2026, 23:54 Paris, « tout attendre la v6.2 » ; écart consigné dans\n"
     "# `diff-lanceur-pilote4-v6-vers-v7.txt`), la v6 dérivée du lanceur v5 (565f5205…) par `deriver_lanceur_pilote4_v6.py`\n"
     "# (avec CLORE=1, l'extrait mécanique est lancé depuis le dépôt), la v5 dérivée du lanceur v4\n", 1),
    ("`essaim-m3-refonte-v1/prereg/pilote4-gemini-organisme-v3.md`", "`essaim-m3-refonte-v1/prereg/pilote4-gemini-organisme-v4.md`", 1),
    ("#       bash lancer_pilote4_gemini_v6.sh\n", "#       bash lancer_pilote4_gemini_v7.sh\n", 1),
]
for ancien, nouveau, n in remplacements:
    k = t.count(ancien)
    if k != n:
        sys.exit(f"refus : {k} occurrence(s) au lieu de {n} pour : {ancien[:90]!r}")
    t = t.replace(ancien, nouveau)
for motif, permis in (("v6-1", 0), ("a9d8eb5", 0), ("ae331d1d", 0), ("v6.1", 1), ("lancer_pilote4_gemini_v6.sh\n", 0)):
    k = t.count(motif)
    if k != permis:
        sys.exit(f"refus : {motif!r} présent {k} fois après dérivation (attendu {permis})")
sortie.write_text(t, encoding="utf-8")
print(f"lanceur écrit : {sortie.name} {hashlib.sha256(sortie.read_bytes()).hexdigest()} ; {len(remplacements)} remplacements")

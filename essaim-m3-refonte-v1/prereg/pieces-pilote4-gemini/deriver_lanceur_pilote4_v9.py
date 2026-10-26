"""Dérive le lanceur v9 du quatrième pilote descriptif du lanceur v8 (`lancer_pilote4_gemini_v8.sh`, 40685089…) :
**ordre des courses inversé** — décision de Lazar (26 octobre 2026, 00:18 Paris, dans la session de conv-audit) :
« je veux la v6.2 en premier ». La v6.2 part d'abord (porte « M de référence » seulement) ; la v5.3 ne part qu'après une
course v6.2 de ce pilote finie, fermée et saine : la porte « v5.3 précédente » du v8 devient la porte « v6.2 précédente »,
même liste close, paramétrée pour la v6.2 (course `v6-2`, nom `pilote4-gemini-v6-2-v1`, lignée `gemini-organisme-v6-2`) ;
variable `PRECEDENTE_V62` (au lieu de `PRECEDENTE_V53`) ; la graine de la v6.2 au manifeste est comparée à celle du
texte ; la ligne de dépense de la v5.3 porte les 16 premiers caractères de l'empreinte des empreintes de la v6.2.

Méthode : dans trois blocs exacts du v8 (étape 0 bis entière ; contrôle de la graine de la course précédente à l'étape 2 ;
contrôle de la ligne de dépense à l'étape 4), échange des noms des deux courses (« v5.3 » ↔ « v6.2 », « v5-3 » ↔
« v6-2 », `V53` → `V62`, `_v53` → `_v62`), chacun au nombre d'occurrences attendu ; puis l'en-tête (description, usage).
Rien d'autre ne change : noyau, banque, segments, minuteur, porte « M de référence », gardes, fermeture, liste fermée.

Usage : python3 -I deriver_lanceur_pilote4_v9.py LANCEUR_V8 SORTIE
Refuse si l'empreinte du lanceur v8 n'est pas 40685089…, si un bloc ou une occurrence n'est pas au nombre attendu, si un
reste de l'ordre ancien subsiste, ou si SORTIE existe (R12).
"""
import hashlib, pathlib, re, sys

SHA_V8 = "40685089e4cb5680d159872c35987af7bb32a1231d6b25127bbbb08841f72978"
src, sortie = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
if sortie.exists():
    sys.exit(f"refus : {sortie} existe déjà (R12)")
b = src.read_bytes()
if hashlib.sha256(b).hexdigest() != SHA_V8:
    sys.exit("refus : le lanceur source n'est pas la v8 40685089…")
t = b.decode("utf-8")


def un(motif, texte, quoi):
    k = texte.count(motif)
    if k != 1:
        sys.exit(f"refus : {quoi} présent {k} fois au lieu d'une")


def echanger(bloc, attendus):
    """Échange les noms des deux courses dans un bloc ; vérifie les comptes avant l'échange."""
    comptes = {m: bloc.count(m) for m in ("v5.3", "v6.2", "v5-3", "v6-2", "V53", "_v53", "V62", "_v62")}
    if comptes != attendus:
        sys.exit(f"refus : comptes {comptes} au lieu de {attendus}")
    for a, z in (("v5.3", "\x00A"), ("v6.2", "v5.3"), ("\x00A", "v6.2"),
                 ("v5-3", "\x00B"), ("v6-2", "v5-3"), ("\x00B", "v6-2"),
                 ("V53", "V62"), ("_v53", "_v62")):
        bloc = bloc.replace(a, z)
    return bloc


# bloc 1 : étape 0 bis entière (du commentaire « # 0 bis » au « fi » qui suit la note de la course précédente)
debut = "# 0 bis (avant l'étape 0, pour que ses refus en réel soient essayables). Course v6.2 : ne part qu'après une course v5.3\n"
fin = '  note "- course v5.3 précédente : $SV ; $issue_v53 ; empreintes de v5.3 vérifiées (EMPREINTES-pilote-v1.txt, sha256 $EMP_V53)"\nfi\n'
un(debut, t, "début de l'étape 0 bis"); un(fin, t, "fin de l'étape 0 bis")
i, j = t.index(debut), t.index(fin) + len(fin)
bloc1 = t[i:j]
nouveau1 = echanger(bloc1, {"v5.3": 27, "v6.2": 6, "v5-3": 8, "v6-2": 1, "V53": 13, "_v53": 3, "V62": 0, "_v62": 0})
ancien_com = ("# 0 bis (avant l'étape 0, pour que ses refus en réel soient essayables). Course v5.3 : ne part qu'après une course v6.2\n"
              "#        finie, fermée et saine (P3C1-01 :")
un(ancien_com, nouveau1, "commentaire de l'étape 0 bis échangé")
nouveau1 = nouveau1.replace(ancien_com,
    "# 0 bis (avant l'étape 0, pour que ses refus en réel soient essayables). Course v5.3 : ne part qu'après une course v6.2\n"
    "#        finie, fermée et saine (v9 : ordre des courses inversé, décision de Lazar du 26 octobre 2026, 00:18 Paris,\n"
    "#        « je veux la v6.2 en premier » ; P3C1-01 :")
t = t[:i] + nouveau1 + t[j:]

# bloc 2 : contrôle de la graine de la course précédente (étape 2)
d2 = '  if [ "$COURSE" = v6-2 ] && [ -n "${GRAINE_V53_MANIFESTE:-}" ]; then\n'
f2 = '    note "- course v5.3 précédente : graine $GRAINE_V53_MANIFESTE = graine v5-3 du préenregistrement"\n  fi\n'
un(d2, t, "début du contrôle de la graine précédente"); un(f2, t, "fin du contrôle de la graine précédente")
i, j = t.index(d2), t.index(f2) + len(f2)
t = t[:i] + echanger(t[i:j], {"v5.3": 2, "v6.2": 0, "v5-3": 3, "v6-2": 1, "V53": 4, "_v53": 0, "V62": 0, "_v62": 0}) + t[j:]

# bloc 3 : contrôle de la ligne de dépense de la seconde course (étape 4)
d3 = '  if [ -n "$EMP_V53" ]; then\n'
f3 = "écrite après la fin de v5.3\"\n  fi\n"
un(d3, t, "début du contrôle de dépense"); un(f3, t, "fin du contrôle de dépense")
i, j = t.index(d3), t.index(f3) + len(f3)
t = t[:i] + echanger(t[i:j], {"v5.3": 2, "v6.2": 1, "v5-3": 0, "v6-2": 0, "V53": 3, "_v53": 0, "V62": 0, "_v62": 0}) + t[j:]

# en-tête
remplacements = [
    ("# Lanceur du quatrième pilote descriptif « organismes assistés de Gemini, v5.3 puis v6.2, chacun seul,",
     "# Lanceur du quatrième pilote descriptif « organismes assistés de Gemini, v6.2 puis v5.3, chacun seul,", 1),
    ("# une course en un ou plusieurs segments (COURSE=v5-3, puis COURSE=v6-2 ; SEGMENT=1, 2, …) — v8 : le lanceur v7\n"
     "# (cda96923…) par `deriver_lanceur_pilote4_v8.py`",
     "# une course en un ou plusieurs segments (COURSE=v6-2, puis COURSE=v5-3 ; SEGMENT=1, 2, …) — v9 : le lanceur v8\n"
     "# (40685089…) par `deriver_lanceur_pilote4_v9.py` (ordre des courses inversé, décision de Lazar du 26 octobre 2026,\n"
     "# 00:18 Paris, « je veux la v6.2 en premier » : la v6.2 d'abord, puis la v5.3 après une v6.2 saine — porte « v6.2\n"
     "# précédente », variable PRECEDENTE_V62 ; écart consigné dans `diff-lanceur-pilote4-v8-vers-v9.txt`), la v8 dérivée\n"
     "# du lanceur v7 (cda96923…) par `deriver_lanceur_pilote4_v8.py`", 1),
    ("# `--generations 4` ; les rondes de conception ; la porte « v5.3 précédente » attend les générations 0 à 3 ;",
     "# `--generations 4` ; les rondes de conception ; la porte « v6.2 précédente » (v9 ; « v5.3 précédente » jusqu'au v8)\n"
     "# attend les générations 0 à 3 ;", 1),
    ("#   MODE=reel COURSE=v5-3 DEPOT=… PYTHON=… PREREG=…", "#   MODE=reel COURSE=v6-2 DEPOT=… PYTHON=… PREREG=…", 1),
    ("#       bash lancer_pilote4_gemini_v8.sh\n", "#       bash lancer_pilote4_gemini_v9.sh\n", 1),
    ("#   MODE=reel COURSE=v6-2 … PRECEDENTE_V53=<dossier du pilote de la course v5.3 de ce pilote, dans la même copie> (même forme)",
     "#   MODE=reel COURSE=v5-3 … PRECEDENTE_V62=<dossier du pilote de la course v6.2 de ce pilote, dans la même copie> (même forme)", 1),
]
for ancien, nouveau, n in remplacements:
    k = t.count(ancien)
    if k != n:
        sys.exit(f"refus : {k} occurrence(s) au lieu de {n} pour : {ancien[:90]!r}")
    t = t.replace(ancien, nouveau)

for motif, permis in (("PRECEDENTE_V53", 0), ("EMP_V53", 0), ("GRAINE_V53_MANIFESTE", 0), ("issue_v53", 0),
                      ('if [ "$COURSE" = v5-3 ] && { [ "$MODE" = reel ] || [ -n "${PRECEDENTE_V62:-}" ]; }; then', 1),
                      ('"gemini-organisme-v6-2" "$MODE" "$GO_ID" "$(basename "$0")" "v6-2" "pilote4-gemini-v6-2-v1"', 1),
                      ('if [ "$COURSE" = v5-3 ] && [ -n "${GRAINE_V62_MANIFESTE:-}" ]; then', 1),
                      ("lancer_pilote4_gemini_v8.sh\n", 0)):
    k = t.count(motif)
    if k != permis:
        sys.exit(f"refus : {motif!r} présent {k} fois après dérivation (attendu {permis})")
sortie.write_text(t, encoding="utf-8")
print(f"lanceur écrit : {sortie.name} {hashlib.sha256(sortie.read_bytes()).hexdigest()}")

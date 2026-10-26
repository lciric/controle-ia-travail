"""Dérive la batterie d'essais v11 du lanceur du pilote 4 de la batterie v10 (`essais_lanceur_pilote4_v10.sh`, b7906684…),
pour le lanceur v9 : **ordre des courses inversé** (décision de Lazar du 26 octobre 2026, 00:18 Paris, « je veux la v6.2
en premier ») — la v6.2 d'abord, puis la v5.3 après une v6.2 de ce pilote finie, fermée et saine (porte « v6.2
précédente », variable `PRECEDENTE_V62`).

Ce qui change, bloc par bloc (chaque bloc trouvé par ses bornes exactes, chaque remplacement au nombre attendu) :
- cas sains : la v6.2 d'abord (essais du noyau exécutés, porte « M de référence »), puis la v5.3 avec la v6.2 saine pour
  précédente ; les vérifications de chaque course suivent sa place (la première : M, graine M, organisme, essais, registre,
  graine, temps, minuteur ; la seconde : précédente, graine de la précédente, M, organisme, graine, temps, minuteur) ; la
  ligne de dépense de la v5.3 porte l'empreinte des empreintes de la v6.2 ;
- porte sur artefacts (copies de la v6.2 saine altérées), refus du mode réel liés à la course précédente, porte sur la
  course précédente en segments et fermée sans reprise : échange des noms des deux courses (« v5.3 » ↔ « v6.2 »,
  « v5-3 » ↔ « v6-2 », graines `G_53` ↔ `G_6`, `V53` → `V62`, `v53` → `v62`, `V6C` → `V5C`, `REEL_V6` → `REEL_V53`) ;
- refus du mode réel de la porte « M de référence » : sur la v6.2 (la première course ; la v5.3 serait refusée avant,
  faute de course précédente) ;
- cas de segments (arrêt par le minuteur, refus du segment 2, segment 2 sain, trois segments, fermeture sans reprise,
  minuteur muté) : sur la v6.2, la course qui part la première et en segments — ce qui essaie aussi la reprise d'un
  organisme qui se réécrit ;
- en-tête et usage.

Un cas est ajouté (`sain-v5-3-graine` : la graine de la seconde course, écrite et recalculée), aucun n'est retiré.

Usage : python3 -I deriver_essais_pilote4_v11.py ESSAIS_V10 SORTIE   (ou COMPTER=1 … : affiche les comptes, n'écrit rien)
Refuse si l'empreinte de la batterie v10 n'est pas b7906684…, si un bloc ou une occurrence n'est pas au nombre attendu, si
un reste de l'ordre ancien subsiste, ou si SORTIE existe (R12).
"""
import hashlib, os, pathlib, sys

SHA_V10 = "b79066848ed6fc183f3828b2808890afe779b3f497518b7eae84f2577b7a32d6"
COMPTER = os.environ.get("COMPTER") == "1"
src, sortie = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
if sortie.exists() and not COMPTER:
    sys.exit(f"refus : {sortie} existe déjà (R12)")
b = src.read_bytes()
if hashlib.sha256(b).hexdigest() != SHA_V10:
    sys.exit("refus : la batterie source n'est pas la v10 b7906684…")
t = b.decode("utf-8")
JETONS = ("v5.3", "v6.2", "v5-3", "v6-2", "G_53", "G_6", "V53", "v53", "V62", "v62", "V6C", "V5C", "REEL_V6", "PRECEDENTE_V53")


def un(motif, texte, quoi):
    k = texte.count(motif)
    if k != 1:
        sys.exit(f"refus : {quoi} présent {k} fois au lieu d'une : {motif[:80]!r}")


def bornes(texte, debut, fin, quoi):
    un(debut, texte, quoi + " (début)"); un(fin, texte, quoi + " (fin)")
    i = texte.index(debut); j = texte.index(fin) + len(fin)
    if j <= i:
        sys.exit(f"refus : bornes de {quoi} dans le désordre")
    return i, j


def comptes(bloc):
    return {m: bloc.count(m) for m in JETONS}


def echanger(bloc, attendus, quoi):
    c = comptes(bloc)
    if COMPTER:
        print(quoi, c); return bloc
    if c != attendus:
        sys.exit(f"refus : {quoi} : comptes {c} au lieu de {attendus}")
    for a, z in (("v5.3", "\x00A"), ("v6.2", "v5.3"), ("\x00A", "v6.2"),
                 ("v5-3", "\x00B"), ("v6-2", "v5-3"), ("\x00B", "v6-2"),
                 ("G_53", "\x00C"), ("G_6", "G_53"), ("\x00C", "G_6"),
                 ("V53", "V62"), ("v53", "v62"), ("V6C", "V5C"), ("REEL_V6", "REEL_V53")):
        bloc = bloc.replace(a, z)
    return bloc


def remplacer(bloc, remplacements, quoi):
    for ancien, nouveau, n in remplacements:
        k = bloc.count(ancien)
        if COMPTER:
            print(quoi, repr(ancien[:60]), k); continue
        if k != n:
            sys.exit(f"refus : {quoi} : {k} occurrence(s) au lieu de {n} pour : {ancien[:90]!r}")
        bloc = bloc.replace(ancien, nouveau)
    return bloc


# 1. cas sains : la v6.2 d'abord, puis la v5.3 (bloc réécrit)
D1 = 'echo "== cas sains : v5.3 complète (essais du noyau exécutés), puis v6.2 ; rondes de conception et quatre générations =="\n'
F1 = 'verifier sain-v6-2-minuteur "STOP non posé" "$V6/LANCEMENT.md"\n'
i, j = bornes(t, D1, F1, "bloc des cas sains")
ARBRE62 = "3b2d8d5a9af75b5457579c847d4ea9510f9da92818805123ed037f7c8436c946"
ARBRE53 = "6251ab219e86286ec892a65e28cf9eebad5265fd6e32e350e68827897c811753"
NOUVEAU1 = (
    'echo "== cas sains : v6.2 complète (essais du noyau exécutés), puis v5.3 après la v6.2 saine ; rondes de conception et quatre générations =="\n'
    'td_heure "$E/entrees/td-heure-fraiche-v6.json" 0 GO-2026-10-25-02\n'
    'cas sain-v6-2 "archive fermée : ferme.tar.gz" -- MODE=simulation COURSE=v6-2 GRAINE="$G_6" PREREG="$E/entrees/prereg-sain.md" PREREG_SHA256="$SHA_PR" "${SAIN[@]}" APPEL_CONTROLE_FICHIER="$E/entrees/td-heure-fraiche-v6.json" ESSAI_EXIGER_HEURE=1\n'
    'V6="$E/cas-sain-v6-2/pilote4-gemini-v6-2-v1"; V62="$V6"\n'
    'verifier sain-v6-2-reference-m "; M saine : g000 et g001 OK" "$V6/LANCEMENT.md"\n'
    'verifier sain-v6-2-graine-m "graine $GRAINE_M_SCELLEE = graine M du texte scellé du second pilote (d2944654…)" "$V6/LANCEMENT.md"\n'
    f'verifier sain-v6-2-organisme "organisme : 24 fichiers, empreinte d\'arbre {ARBRE62}" "$V6/LANCEMENT.md"\n'
    'verifier sain-v6-2-essais "essais : 169 passés, 0 sauté, 0 désélectionnés" "$V6/LANCEMENT.md"\n'
    'verifier sain-v6-2-registre "registre : une ligne GO-2026-10-25-02 de type calcul" "$V6/LANCEMENT.md"\n'
    'verifier sain-v6-2-graine "graine $G_6 de la course v6-2 écrite et recalculée" "$V6/LANCEMENT.md"\n'
    'verifier sain-v6-2-temps-conception "temps par ronde de conception 900 s" "$V6/LANCEMENT.md"\n'
    'verifier sain-v6-2-minuteur "STOP non posé" "$V6/LANCEMENT.md"\n'
    'JUNIT="$E/junit-sain-v1.xml"; cp "$V6/essais-v1.xml" "$JUNIT"\n'
    'SAIN+=(ESSAI_JUNIT_EXISTANT="$JUNIT" ESSAI_RESUME_EXISTANT="169 passed")\n'
    'EMP_V62="$(cut -d\' \' -f1 < "$V62/EMPREINTES-pilote-v1.txt.sha256")"\n'
    "printf '| 2026-10-25 | pilote4-gemini-v6-2-v1 | GO-2026-10-25-02 | 60 | après M, empreintes de M %s |\\n| 2026-10-25 | pilote4-gemini-v5-3-v1 | GO-2026-10-25-02 | 60 | après M et v6.2, empreintes de M %s, de v6.2 %s |\\n' \"$EMP_M\" \"$EMP_M\" \"$EMP_V62\" > \"$E/entrees/dep-sain.md\"\n"
    "printf '| 2026-10-25 | pilote4-gemini-v6-2-v1 | GO-2026-10-25-02 | 60 | après M, empreintes de M %s |\\n| 2026-10-25 | pilote4-gemini-v5-3-v1 | GO-2026-10-25-02 | 60 | après M, empreintes de M %s |\\n' \"$EMP_M\" \"$EMP_M\" > \"$E/entrees/dep-v53-sans-empreinte-v62.md\"\n"
    'td_heure "$E/entrees/td-heure-fraiche-v53.json" 0 GO-2026-10-25-02\n'
    'cas sain-v5-3 "archive fermée : ferme.tar.gz" -- MODE=simulation COURSE=v5-3 GRAINE="$G_53" PREREG="$E/entrees/prereg-sain.md" PREREG_SHA256="$SHA_PR" "${SAIN[@]}" APPEL_CONTROLE_FICHIER="$E/entrees/td-heure-fraiche-v53.json" ESSAI_EXIGER_HEURE=1 PRECEDENTE_V62="$V62"\n'
    'V53="$E/cas-sain-v5-3/pilote4-gemini-v5-3-v1"\n'
    'verifier sain-v5-3-precedente-v62 "; v6.2 saine : g000 à g003 OK" "$V53/LANCEMENT.md"\n'
    'verifier sain-v5-3-graine-v62 "graine $G_6 = graine v6-2 du préenregistrement" "$V53/LANCEMENT.md"\n'
    'verifier sain-v5-3-reference-m "; M saine : g000 et g001 OK" "$V53/LANCEMENT.md"\n'
    f'verifier sain-v5-3-organisme "organisme : 22 fichiers, empreinte d\'arbre {ARBRE53}" "$V53/LANCEMENT.md"\n'
    'verifier sain-v5-3-graine "graine $G_53 de la course v5-3 écrite et recalculée" "$V53/LANCEMENT.md"\n'
    'verifier sain-v5-3-temps-conception "temps par ronde de conception 900 s" "$V53/LANCEMENT.md"\n'
    'verifier sain-v5-3-minuteur "STOP non posé" "$V53/LANCEMENT.md"\n')
if not COMPTER:
    t = t[:i] + NOUVEAU1 + t[j:]

# 2. porte sur artefacts (copies de la course précédente altérées)
i, j = bornes(t, 'echo "== course v6.2 : issues de v5.3 hors de la liste saine (copie de v5.3 altérée, empreintes refaites) =="\n',
              'DEPENSES_SOURCE="$E/entrees/dep-v6-sans-empreinte-v53.md"\n', "bloc de la porte sur artefacts")
b2 = echanger(t[i:j], {"v5.3": 13, "v6.2": 3, "v5-3": 5, "v6-2": 3, "G_53": 0, "G_6": 1, "V53": 25, "v53": 50, "V62": 0, "v62": 0, "V6C": 23, "V5C": 0, "REEL_V6": 0, "PRECEDENTE_V53": 23}, "porte sur artefacts")
b2 = remplacer(b2, [("dep-v6-sans-empreinte-v62.md", "dep-v53-sans-empreinte-v62.md", 1)], "porte sur artefacts")
if not COMPTER:
    t = t[:i] + b2 + t[j:]

# 3. mode réel, porte « M de référence » : sur la v6.2
i, j = bornes(t, 'echo "== mode réel (copie du dépôt sous /root) : refus à l\'étape (0), avant tout appel =="\n',
              'rm -rf "$DEPOT_ROOT/essaim-m3-refonte-v1/pilotes" "$RR"\n', "bloc du mode réel (M)")
b3 = remplacer(t[i:j], [("REEL=(MODE=reel COURSE=v5-3 PILOTE_RACINE=-", "REEL=(MODE=reel COURSE=v6-2 PILOTE_RACINE=-", 1),
                        ('"${REEL[@]}" COURSE=v5-3 REFERENCE_M=', '"${REEL[@]}" COURSE=v6-2 REFERENCE_M=', 1)], "mode réel (M)")
if not COMPTER:
    t = t[:i] + b3 + t[j:]

# 4. mode réel, course précédente
i, j = bornes(t, 'echo "== mode réel, course v6.2 (copie du dépôt sous /root) : refus à l\'étape (0 bis), avant tout appel =="\n',
              'echo "== mode réel : gardes communes (échantillon), avant tout appel =="\n', "bloc du mode réel (précédente)")
b4 = echanger(t[i:j], {"v5.3": 1, "v6.2": 1, "v5-3": 3, "v6-2": 5, "G_53": 0, "G_6": 0, "V53": 7, "v53": 0, "V62": 0, "v62": 0, "V6C": 0, "V5C": 0, "REEL_V6": 5, "PRECEDENTE_V53": 4}, "mode réel (précédente)")
if not COMPTER:
    t = t[:i] + b4 + t[j:]

# 5. segments : sur la v6.2 (jusqu'à la porte en segments)
i, j = bornes(t, "copie_ps() {  # copie_ps NOM → chemin d'une copie de la v5.3 en segments\n",
              'echo "-- porte « v5.3 précédente » de la v6.2 sur la v5.3 en segments --"\n', "bloc des segments")
b5 = remplacer(t[i:j], [("copie de la v5.3 en segments", "copie de la v6.2 en segments", 1),
                        ("pilote4-gemini-v5-3-v1", "pilote4-gemini-v6-2-v1", 17),
                        ('SEG=(MODE=simulation COURSE=v5-3 GRAINE="$G_53"', 'SEG=(MODE=simulation COURSE=v6-2 GRAINE="$G_6"', 1),
                        ("empreinte d'arbre de l'organisme ≠ 6251ab21…", "empreinte d'arbre de l'organisme ≠ 3b2d8d5a…", 1)], "segments")
if not COMPTER:
    t = t[:i] + b5 + t[j:]

# 6. porte sur la course précédente en segments
i, j = bornes(t, 'echo "-- porte « v5.3 précédente » de la v6.2 sur la v5.3 en segments --"\n',
              'echo "-- trois segments (états de reprise v1 et v2) --"\n', "bloc de la porte en segments")
b6 = echanger(t[i:j], {"v5.3": 5, "v6.2": 1, "v5-3": 0, "v6-2": 5, "G_53": 0, "G_6": 0, "V53": 5, "v53": 5, "V62": 0, "v62": 0, "V6C": 4, "V5C": 0, "REEL_V6": 0, "PRECEDENTE_V53": 5}, "porte en segments")
b6 = remplacer(b6, [("dep-v6-apres-segments.md", "dep-v53-apres-segments.md", 2)], "porte en segments")
if not COMPTER:
    t = t[:i] + b6 + t[j:]

# 7. trois segments et fermeture sans reprise : sur la v6.2 ; la v5.3 refusée sur une v6.2 fermée sans reprise
i, j = bornes(t, 'echo "-- trois segments (états de reprise v1 et v2) --"\n',
              'cas minuteur-echeance-non-entiere "ESSAI_ECHEANCE_STOP_S doit être un entier (secondes)"', "bloc trois segments et fermeture")
b7 = remplacer(t[i:j], [("pilote4-gemini-v5-3-v1", "pilote4-gemini-v6-2-v1", 2),
                        ('cas seg-clore "CLORE=1 : aucune reprise, aucun appel" -- MODE=simulation COURSE=v5-3 GRAINE="$G_53"',
                         'cas seg-clore "CLORE=1 : aucune reprise, aucun appel" -- MODE=simulation COURSE=v6-2 GRAINE="$G_6"', 1),
                        ('cas seg-clore-v53-refusee "course v5.3 fermée sans reprise (CLORE=1)" -- "${V6C[@]}" PRECEDENTE_V53="$PC"',
                         'cas seg-clore-v62-refusee "course v6.2 fermée sans reprise (CLORE=1)" -- "${V5C[@]}" PRECEDENTE_V62="$PC"', 1)],
               "trois segments et fermeture")
if not COMPTER:
    t = t[:i] + b7 + t[j:]

# 8. minuteur muté : sur la v6.2 (SEG)
t = remplacer(t, [('RMU="$E/cas-mut-minuteur-segment1"; PMU="$RMU/pilote4-gemini-v5-3-v1"',
                   'RMU="$E/cas-mut-minuteur-segment1"; PMU="$RMU/pilote4-gemini-v6-2-v1"', 1)], "minuteur muté")

# 9. en-tête et usage
t = remplacer(t, [
    ("# Essais du lanceur du pilote 4 (v5.3 puis v6.2, banque v3,", "# Essais du lanceur du pilote 4 (v6.2 puis v5.3, banque v3,", 1),
    ("# plus), v10 : la v9 (edb6b12b…) par `deriver_essais_pilote4_v10.py` pour le lanceur v8 (la v6.2 livrée, commit `3bbb78c`,\n",
     "# plus), v11 : la v10 (b7906684…) par `deriver_essais_pilote4_v11.py` pour le lanceur v9 (ordre des courses inversé, décision\n"
     "# de Lazar du 26 octobre 2026, 00:18 Paris : la v6.2 d'abord, puis la v5.3 après une v6.2 saine ; porte « v6.2 précédente »\n"
     "# sur un cas sain et sur ses artefacts ; segments essayés sur la v6.2 ; un cas ajouté, sain-v5-3-graine) ; la v10 était\n"
     "# dérivée de la v9 (edb6b12b…) par `deriver_essais_pilote4_v10.py` pour le lanceur v8 (la v6.2 livrée, commit `3bbb78c`,\n", 1),
    ("# essaie (i) les deux courses saines de bout en bout en simulation (v5.3, essais du noyau exécutés ; puis v6.2 après la\n"
     "# v5.3 saine),",
     "# essaie (i) les deux courses saines de bout en bout en simulation (v6.2, essais du noyau exécutés ; puis v5.3 après la\n"
     "# v6.2 saine),", 1),
    ("(iii) la porte « v5.3 précédente » (générations 0 à 3) et ses artefacts ;",
     "(iii) la porte « v6.2 précédente » (générations 0 à 3) et ses artefacts ;", 1),
    ("# Usage : bash essais_lanceur_pilote4_v10.sh ", "# Usage : bash essais_lanceur_pilote4_v11.sh ", 1),
], "en-tête")

if COMPTER:
    sys.exit(0)
N_PREC = b.decode("utf-8").count("PRECEDENTE_V53")
for motif, permis in (("PRECEDENTE_V53", 0), ("V6C", 0), ("REEL_V6[", 0), ("dep-v6-", 0), ("copie_v53", 0),
                      ('COURSE=v6-2 "${SAIN[@]}" PRECEDENTE_V62', 0), ("PRECEDENTE_V62", N_PREC)):
    k = t.count(motif)
    if k != permis:
        sys.exit(f"refus : {motif!r} présent {k} fois après dérivation (attendu {permis})")
sortie.write_text(t, encoding="utf-8")
print(f"batterie écrite : {sortie.name} {hashlib.sha256(sortie.read_bytes()).hexdigest()}")

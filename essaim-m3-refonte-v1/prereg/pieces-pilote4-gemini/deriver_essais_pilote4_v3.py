"""Dérive la batterie d'essais du lanceur du pilote 4 de la batterie v3 du pilote 3
(`essais_lanceur_pilote3_v5_3_v6_v3.sh`, 14bc0535…), par remplacements exacts au nombre attendu et cas ajoutés — v3
= v2 (gardée) pour la banque v3 (la v2 de la banque est abandonnée sur sa contre-lecture) : commits sur les chemins
de la banque v3 (construction, contre-lectures : permis), lanceur v2 nommé ; la v2 était elle-même = v1 (gardée ; série v2 :
131 cas sur 146) à un remplacement près : le chemin du dossier du cas sain de la v6.x
(`$E/cas-sain-<clé>/`, l’étiquette du cas ayant changé), que la v1 laissait à `$E/cas-sain-v6/` (15 vérifications du cas
sain de la v6.x en échec, la course elle-même conforme).

Paramétrée par la configuration du lanceur (`config-….json` : objet v6.x, rondes de conception, banque), pour se
refaire d'une commande quand les valeurs finales sont connues.

Ce qui change : noms des courses (`pilote4-gemini-v5-3-v1`, `pilote4-gemini-<clé>-v1`) ; `COURSE=<clé>` ; graines `v5-3`
et `<clé>` ; objet v6.x (arbre, nombre de fichiers) ; lignes de GO d'essai écrites après les textes d'essai et portant
l'arbre de l'objet et les 16 premiers caractères de l'empreinte du texte d'essai sain ; « v5.3 saine : g000 à g003 OK » ;
messages du lanceur dérivé (pilote 4, v6.x) ; chemins des pièces du pilote 4. Cas ajoutés : ligne de GO sans
l'empreinte du texte (refus) ; v5.3 précédente à deux générations (refus) ; journaux de g000 à g003 et des rondes recopiés
et poussés ; relevé des rondes de conception (non compté) ; commits sur les banques v2 et v3 (permis) et sur un autre fichier de
la banque (refusé).

Usage : python3 -I deriver_essais_pilote4_v1.py ESSAIS_V3 CONFIG.json SORTIE
"""
import hashlib, json, pathlib, re, sys

SHA_V3 = "14bc0535534bc5c7350102c4d13786ecd40cb3802cb980eb1e4715b53d116aa9"
src, conf_f, sortie = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2]), pathlib.Path(sys.argv[3])
if sortie.exists():
    sys.exit(f"refus : {sortie} existe déjà (R12)")
b = src.read_bytes()
if hashlib.sha256(b).hexdigest() != SHA_V3:
    sys.exit("refus : la batterie source n'est pas la v3 14bc0535…")
t = b.decode("utf-8")
c = json.loads(conf_f.read_text(encoding="utf-8"))
v6 = c["v6x"]
K, AFF, ARBRE, N = v6["cle"], v6["nom_affiche"], v6["arbre"], int(v6["n_fichiers"])
R = int(c["rondes_conception"])
T8 = ARBRE[:8]
NOM53, NOM6 = "pilote4-gemini-v5-3-v1", f"pilote4-gemini-{K}-v1"
ARBRE_V6 = "940c59c3dd58fdd5355244768faa1e9da02620fa455cd8ead15f8271145da64a"

# 1. En-tête (lignes 2 à 18)
lignes = t.split("\n")
debut = lignes.index("set -uo pipefail")
if not all(l.startswith("#") for l in lignes[1:debut]):
    sys.exit("refus : en-tête de la batterie v3 inattendu")
entete = f"""# Essais du lanceur du pilote 4 (v5.3 puis {AFF}, banque v3, quatre générations notées, {R} rondes de conception au
# plus), v2, dérivés de la batterie v3 du pilote 3 (`essais_lanceur_pilote3_v5_3_v6_v3.sh`, 14bc0535…, 122 cas sur 122
# sur le lanceur v2) par `deriver_essais_pilote4_v3.py` (remplacements exacts, configuration du lanceur ; la v1 laissait le chemin du
# cas sain de la v6.x à l’ancienne étiquette). Cette série
# essaie (i) les deux courses saines de bout en bout en simulation (v5.3, essais du noyau exécutés ; puis {AFF} après la
# v5.3 saine), avec les rondes de conception et les quatre générations, et relève ce que montrent les rondes ; (ii) la
# course M de référence, produite par le lanceur scellé du second pilote lui-même, puis chaque issue de M hors de la
# liste close ; (iii) la porte « v5.3 précédente » (générations 0 à 3) et ses artefacts ; (iv) ce qui change (objets,
# graines, banque v3 et les chemins permis des banques v2 et v3, ligne de GO liée au texte scellé, journaux recopiés et poussés) ; (v) un
# échantillon des gardes communes, en simulation et en mode réel (refus avant tout appel). Aucun appel réel.
# Usage : bash essais_lanceur_pilote4_v3.sh LANCEUR LANCEUR_M DEPOT DEPOT_M PYTHON DOSSIER_ESSAIS DEPOT_SOUS_ROOT PYTHON_AVEC_HTTPX
# (DEPOT : copie à la tête du pilote 4 ; DEPOT_M : copie à la tête du second pilote, d'où part la M de référence ;
# DEPOT_SOUS_ROOT : copie à la tête du pilote 4 sous /root, pour les refus du mode réel)"""
t = "\n".join([lignes[0], entete] + lignes[debut:])

remplacements = []   # (ancien, nouveau, nombre attendu) ; les insertions (ancres sur le texte v3) passent avant les remplacements généraux
generaux = []
# 2. Lignes de GO d'essai : retirées de leur place, réécrites après les textes d'essai, avec l'empreinte du texte sain
anciennes_go = [
    "printf '| GO-2026-10-25-02 | 2026-10-25 | calcul | pilote 3 (essai) : question `8b1c7511…`, organismes v5.3 `6251ab21…` et v6 `940c59c3…` | au plus 120 USD | 2026-10-31 |\\n' > \"$E/entrees/go-sain.md\"\n",
    "printf '| GO-2026-10-25-02 | 2026-10-25 | pilote 3 (essai) : `8b1c7511…` `6251ab21…` `940c59c3…` |\\n' > \"$E/entrees/go-sans-calcul.md\"\n",
    "printf '| GO-2026-10-25-01 | 2026-10-25 | calcul | `8b1c7511…` `6251ab21…` `940c59c3…` |\\n' > \"$E/entrees/go-autre-id.md\"\n",
    "printf '| GO-2026-10-25-02 | 2026-10-25 | calcul | pilote 3 (essai) : question `8b1c7511…`, organisme v5.3 `6251ab21…` seulement |\\n' > \"$E/entrees/go-v53-seulement.md\"\n",
    "printf '| GO-2026-10-25-02 | 2026-10-25 | calcul | pilote 3 (essai) : question `a54da93e…`, organismes `6251ab21…` `940c59c3…` |\\n' > \"$E/entrees/go-autre-question.md\"\n",
]
for l in anciennes_go:
    remplacements.append((l, "", 1))
ancre_sha = "SHA_PR=\"$(cut -d' ' -f1 < \"$E/entrees/prereg-sain.md.sha256\")\"\n"
nouvelles_go = (ancre_sha
    + "T16=\"${SHA_PR:0:16}\"   # pilote 4 : la ligne de GO porte les 16 premiers caractères de l'empreinte du texte scellé\n"
    + f"printf '| GO-2026-10-25-02 | 2026-10-25 | calcul | pilote 4 (essai) : question `8b1c7511…`, organismes v5.3 `6251ab21…` et {AFF} `{T8}…` ; texte %s | au plus 120 USD | 2026-10-31 |\\n' \"$T16\" > \"$E/entrees/go-sain.md\"\n"
    + f"printf '| GO-2026-10-25-02 | 2026-10-25 | pilote 4 (essai) : `8b1c7511…` `6251ab21…` `{T8}…` ; texte %s |\\n' \"$T16\" > \"$E/entrees/go-sans-calcul.md\"\n"
    + f"printf '| GO-2026-10-25-01 | 2026-10-25 | calcul | `8b1c7511…` `6251ab21…` `{T8}…` ; texte %s |\\n' \"$T16\" > \"$E/entrees/go-autre-id.md\"\n"
    + "printf '| GO-2026-10-25-02 | 2026-10-25 | calcul | pilote 4 (essai) : question `8b1c7511…`, organisme v5.3 `6251ab21…` seulement ; texte %s |\\n' \"$T16\" > \"$E/entrees/go-v53-seulement.md\"\n"
    + f"printf '| GO-2026-10-25-02 | 2026-10-25 | calcul | pilote 4 (essai) : question `a54da93e…`, organismes `6251ab21…` `{T8}…` ; texte %s |\\n' \"$T16\" > \"$E/entrees/go-autre-question.md\"\n"
    + f"printf '| GO-2026-10-25-02 | 2026-10-25 | calcul | pilote 4 (essai) : question `8b1c7511…`, organismes v5.3 `6251ab21…` et {AFF} `{T8}…` (sans le texte) |\\n' > \"$E/entrees/go-sans-texte.md\"\n")
remplacements.append((ancre_sha, nouvelles_go, 1))

# 3. Noms, course, graines, objet
generaux += [
    ("pilote3-gemini-v5-3-maieutique-v1", NOM53, 13),
    ("pilote3-gemini-v6-maieutique-v1", NOM6, 7),
    ("COURSE=v6", f"COURSE={K}", 14),
    ("graine de la course v6 = $G_6", f"graine de la course {K} = $G_6", 3),
    ("graine de la course v6 = 13", f"graine de la course {K} = 13", 1),
    ("(v5-3 ou v6)", f"(v5-3 ou {K})", 2),
    ("graine $G_6 de la course v6 écrite", f"graine $G_6 de la course {K} écrite", 1),
    ("- course : v6 ;", f"- course : {K} ;", 1),
    (ARBRE_V6, ARBRE, 1),
    ("organisme : 24 fichiers, empreinte d'arbre", f"organisme : {N} fichiers, empreinte d'arbre", 1),
    ("fichiers au lieu de 24", f"fichiers au lieu de {N}", 1),
    ("empreinte d'arbre de l'organisme ≠ 940c59c3…", f"empreinte d'arbre de l'organisme ≠ {T8}…", 1),
    ("l'empreinte de l'organisme 940c59c3… (GO non inscrit pour cette course sur cet objet)",
     f"l'empreinte de l'organisme {T8}… et celle du texte scellé", 1),
    ("; v5.3 saine : g000 et g001 OK", "; v5.3 saine : g000 à g003 OK", 1),
    ('V6="$E/cas-sain-v6/', f'V6="$E/cas-sain-{K}/', 1),
    # artefacts par numéro de génération : les générations notées seulement (une ronde de conception porte aussi un numéro)
    ('for g in x["generations"] if g.get("generation") == 1]', 'for g in x["generations"] if g.get("generation") == 1 and not g.get("phase")]', 6),
    ('for g in x["generations"] if g.get("generation") == 0]', 'for g in x["generations"] if g.get("generation") == 0 and not g.get("phase")]', 4),
    ('x["generations"] = [g for g in x["generations"] if g.get("generation") != 1]',
     'x["generations"] = [g for g in x["generations"] if g.get("generation") != 1 or g.get("phase")]', 2),
    ("absent : v6 ne part qu'après v5.3", f"absent : {AFF} ne part qu'après v5.3", 1),
    ("la ligne de dépense de v6 ne porte pas", f"la ligne de dépense de {AFF} ne porte pas", 1),
    ("absent : une course du pilote 3 ne part qu'après M", "absent : une course du pilote 4 ne part qu'après M", 1),
    ("lanceur : lancer_pilote3_gemini_v5_3_v6_v1.sh, sha256 $H", "lanceur : lancer_pilote4_gemini_v2.sh, sha256 $H", 1),
    ("(noms du pilote 3)", "(noms du pilote 4)", 1),
    ("pieces-pilote3-gemini-v5-3-v6/piece-essai.txt", "pieces-pilote4-gemini/piece-essai.txt", 2),
    ('commit -q -m "essai : pièce du pilote 3"', 'commit -q -m "essai : pièce du pilote 4"', 1),
    ("contre-lectures/pilote3-gemini-organisme-v5-3-v6-v1-cl1.md", "contre-lectures/pilote4-gemini-organisme-v1-cl1.md", 2),
    ('commit -q -m "essai : contre-lecture du pilote 3"', 'commit -q -m "essai : contre-lecture du pilote 4"', 1),
    ("prereg/pilote3-autre-texte-v1.md", "prereg/pilote4-autre-texte-v1.md", 2),
    ('echo "== cas sains : v5.3 complet (essais du noyau exécutés), puis v6 =="',
     f'echo "== cas sains : v5.3 complète (essais du noyau exécutés), puis {AFF} ; rondes de conception et quatre générations =="', 1),
    ('echo "== course v6 : issues de v5.3 hors de la liste saine (copie de v5.3 altérée, empreintes refaites) =="',
     f'echo "== course {AFF} : issues de v5.3 hors de la liste saine (copie de v5.3 altérée, empreintes refaites) =="', 1),
    ('echo "== mode réel, course v6 (copie du dépôt sous /root) : refus à l\'étape (0 bis), avant tout appel =="',
     f'echo "== mode réel, course {AFF} (copie du dépôt sous /root) : refus à l\'étape (0 bis), avant tout appel =="', 1),
]
# 4. Cas ajoutés
ancre_v6 = f'verifier sain-v6-graine "graine $G_6 de la course v6 écrite et recalculée" "$V6/LANCEMENT.md"\n'
ajout_v6 = (ancre_v6
    + 'for d in "$V53" "$V6"; do\n'
    + '  for g in g000 g001 g002 g003 c001; do\n'
    + '    verifier "sain-journal-$g-$(basename "$d")" "journal des appels $g : journal-appels-$g.jsonl" "$d/LANCEMENT.md"\n'
    + '    verifier "sain-pousse-$g-$(basename "$d")" "journal-appels-$g.jsonl" "$d/A-POUSSER-v1.txt"\n'
    + '  done\n'
    + 'done\n'
    + 'echo "== relevé des rondes de conception et des générations en simulation (non compté) =="\n'
    + 'for d in "$V53" "$V6"; do\n'
    + '  "$PY" -I -c \'\n'
    + 'import json, pathlib, sys\n'
    + 'd = pathlib.Path(sys.argv[1]); x = json.load(open(d / "extrait-mecanique-v1.json", encoding="utf-8"))\n'
    + 'r = x.get("rapport") or {}\n'
    + 'print("RELEVÉ " + d.name + " : rondes_conception " + json.dumps(r.get("rondes_conception"), ensure_ascii=False) + " ; lignées " + json.dumps({k: {c: v.get(c) for c in ("fin", "conception_finie", "generation")} for k, v in (r.get("lignees") or {}).items()}, ensure_ascii=False))\n'
    + 'for g in x.get("generations", []):\n'
    + '    a = g.get("appels") or {}\n'
    + '    print("RELEVÉ " + d.name + " : " + ("c%03d" % g["generation"] if g.get("phase") else "g%03d" % g["generation"]) + " statut " + str(g.get("statut")) + " ; appels " + json.dumps(a.get("par_statut"), sort_keys=True) + " ; successeur " + json.dumps(g.get("successeur"), ensure_ascii=False)[:80] + " ; problèmes du successeur " + json.dumps(g.get("problemes_successeur"), ensure_ascii=False)[:160])\n'
    + 'arr = [(e.get("etape"), e.get("raison")) for e in x.get("evenements", []) if str(e.get("etape", "")).startswith("arret")]\n'
    + 'print("RELEVÉ " + d.name + " : arrêts " + json.dumps(arr, ensure_ascii=False))\n'
    + 'for j in sorted(d.glob("journal-appels-*.jsonl")):\n'
    + '    roles = {}\n'
    + '    for l in open(j, encoding="utf-8"):\n'
    + '        try: e = json.loads(l)\n'
    + '        except Exception: continue\n'
    + '        roles[e.get("role")] = roles.get(e.get("role"), 0) + 1\n'
    + '    print("RELEVÉ " + d.name + " : " + j.name + " : " + str(sum(roles.values())) + " appels ; rôle architecte_mutation_endogene : " + str(roles.get("architecte_mutation_endogene", 0)) + " ; rôles " + json.dumps(roles, ensure_ascii=False, sort_keys=True)[:300])\n'
    + '\' "$d"\n'
    + 'done\n')
remplacements.append((ancre_v6, ajout_v6, 1))
ancre_go = 'cas go-autre-question "l\'empreinte de la question 8b1c7511…" -- MODE=simulation "${SAIN[@]}" REGISTRE_GO_SOURCE="$E/entrees/go-autre-question.md"\n'
ajout_go = (ancre_go
    + 'cas go-sans-texte "celle du texte scellé ($T16)" -- MODE=simulation COURSE=v5-3 GRAINE="$G_53" PREREG="$E/entrees/prereg-sain.md" PREREG_SHA256="$SHA_PR" "${SAIN[@]}" REGISTRE_GO_SOURCE="$E/entrees/go-sans-texte.md"\n')
remplacements.append((ancre_go, ajout_go, 1))
ancre_une = 'cas v53-une-generation "générations de v5.3 : [0]" -- "${V6C[@]}" PRECEDENTE_V53="$d"\n'
ajout_une = ('cas v53-une-generation "générations de v5.3 : [0, 2, 3] au lieu de [0, 1, 2, 3]" -- "${V6C[@]}" PRECEDENTE_V53="$d"\n'
    + 'd="$(copie_v53 deux)"; extrait_altere "$d" \'x["generations"] = [g for g in x["generations"] if g.get("phase") or g.get("generation") in (0, 1)]\'; refaire_empreintes "$d"\n'
    + 'cas v53-deux-generations "générations de v5.3 : [0, 1] au lieu de [0, 1, 2, 3]" -- "${V6C[@]}" PRECEDENTE_V53="$d"\n')
remplacements.append((ancre_une, ajout_une, 1))
ancre_cl = 'cas commit-contre-lecture-pilote3 "commits postérieurs limités aux pièces du pilote" -- MODE=simulation "${SAIN[@]}"\ngit -C "$DEPOT" reset -q --hard HEAD~1\n'
ajout_cl = (ancre_cl
    + 'printf \'x\\n\' > "$DEPOT/essaim-m3-refonte-v1/banque/construction-v2/piece-essai.txt"\n'
    + 'git -C "$DEPOT" add essaim-m3-refonte-v1/banque/construction-v2/piece-essai.txt; git -C "$DEPOT" -c user.email=e@x -c user.name=essai commit -q -m "essai : pièce de la banque v2"\n'
    + 'cas commit-banque-v2 "commits postérieurs limités aux pièces du pilote" -- MODE=simulation "${SAIN[@]}"\n'
    + 'git -C "$DEPOT" reset -q --hard HEAD~1\n'
    + 'printf \'x\\n\' > "$DEPOT/essaim-m3-refonte-v1/banque/construction-v3/piece-essai.txt"\n'
    + 'git -C "$DEPOT" add essaim-m3-refonte-v1/banque/construction-v3/piece-essai.txt; git -C "$DEPOT" -c user.email=e@x -c user.name=essai commit -q -m "essai : pièce de la banque v3"\n'
    + 'cas commit-banque-v3 "commits postérieurs limités aux pièces du pilote" -- MODE=simulation "${SAIN[@]}"\n'
    + 'git -C "$DEPOT" reset -q --hard HEAD~1\n'
    + 'mkdir -p "$DEPOT/essaim-m3-refonte-v1/banque/contre-lectures/essai"; printf \'x\\n\' > "$DEPOT/essaim-m3-refonte-v1/banque/contre-lectures/essai/piece-essai.txt"\n'
    + 'git -C "$DEPOT" add essaim-m3-refonte-v1/banque/contre-lectures/essai/piece-essai.txt; git -C "$DEPOT" -c user.email=e@x -c user.name=essai commit -q -m "essai : contre-lecture de la banque"\n'
    + 'cas commit-banque-contre-lecture "commits postérieurs limités aux pièces du pilote" -- MODE=simulation "${SAIN[@]}"\n'
    + 'git -C "$DEPOT" reset -q --hard HEAD~1\n'
    + 'printf \'x\\n\' > "$DEPOT/essaim-m3-refonte-v1/banque/banque-autre-v1.json"\n'
    + 'git -C "$DEPOT" add essaim-m3-refonte-v1/banque/banque-autre-v1.json; git -C "$DEPOT" -c user.email=e@x -c user.name=essai commit -q -m "essai : autre fichier de la banque"\n'
    + 'cas commit-banque-autre "commits postérieurs à b1c7f4b6 hors des pièces du pilote" -- MODE=simulation "${SAIN[@]}"\n'
    + 'git -C "$DEPOT" reset -q --hard HEAD~1\n')
remplacements.append((ancre_cl, ajout_cl, 1))

for ancien, nouveau, n in remplacements + generaux:
    k = t.count(ancien)
    if k != n:
        sys.exit(f"refus : {k} occurrence(s) au lieu de {n} pour : {ancien[:100]!r}")
    t = t.replace(ancien, nouveau)

# 5. Étiquettes des cas et des vérifications : « v6 » → clé, « pilote3 » → « pilote4 » (premier mot seulement)
def etiquette(m):
    return m.group(1) + re.sub(r"(?<![0-9a-z])v6(?![0-9.])", K, m.group(2)).replace("pilote3", "pilote4")
t = re.sub(r"^((?:cas|verifier) )(\S+)", etiquette, t, flags=re.M)

# 6. Restes interdits
for motif in ("pilote3-gemini", "940c59c3", "pilote 3 (essai)"):
    if motif in t:
        sys.exit(f"refus : motif restant après dérivation : {motif!r}")
sortie.write_text(t, encoding="utf-8")
print(f"batterie écrite : {sortie.name} {hashlib.sha256(sortie.read_bytes()).hexdigest()} ; {len(remplacements) + len(generaux)} remplacements")

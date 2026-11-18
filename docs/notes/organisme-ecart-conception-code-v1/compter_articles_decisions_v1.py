#!/usr/bin/env python3
"""Compte les articles des décisions de conception de l'organisme (lecteur : modèle C), version 1.

LECTURE SEULE sur les décisions ; écrit seulement articles-decisions-v1.json (création : refuse d'écraser).
Aucun accès réseau, aucune clé, aucune recherche dans l'arbre : les fichiers sont nommés.

RÈGLE DE DÉCOUPAGE (une seule, la même pour toutes les décisions)
  Pour chaque décision, on désigne dans le tableau SECTIONS la ou les sections de « dispositif » : celles qui
  énoncent ce que la décision fixe, retient ou lit (« Énoncés retenus », « Ce que la décision fixe », section
  N-049 ou N-050 de la note transcrite, « Lecture retenue » et « Réserve »). Les mots de Lazar, le contexte, « ce
  que cela change », « ce que cela ne décide pas », « ce qui ne change pas », « points à régler » ne sont PAS
  des articles (ils servent de fondement ou de contrôle).
  Dans une section de dispositif, un ARTICLE est une unité de premier niveau :
    (a) un point numéroté « N. » ; un point « 5. et 6. » donne deux articles (5 et 6) de même texte, marqués
        « jumelé » ;
    (b) une puce « - » de premier niveau ;
    (c) un paragraphe libre (bloc de lignes non vides hors points et puces), sauf s'il se termine par « : »
        (amorce d'une liste) ou s'il commence par « Numéro » (formalité d'inscription).
  L'identifiant est « N-0xx.k » où k est le rang (1, 2, ...) de l'article dans l'ordre du fichier, tous
  dispositifs confondus ; pour N-045 : « N-045v1.k » (remplacée) et « N-045v2.k ». Un point numéroté garde son
  numéro quand la suite est continue.
  La « ligne » est la première ligne du fichier source (numérotée à partir de 1), « ligne_fin » la dernière.

MASQUAGE : le texte recopié et les fondements sont écrits avec un masque « [modèle masqué] » à la place de tout
identifiant de modèle de la famille de l'assistant (interdit dans les fichiers produits) ; la ligne et
l'empreinte de la source permettent de relire l'original. Le masque est rejouable (voir MASQUES).

Usage :
  python3 -I -B compter_articles_decisions_v1.py [--racine DOSSIER] [--sortie DOSSIER] [--table] [--verifier-md FICHIER]
"""
import argparse, hashlib, json, os, re, sys

RACINE_DEFAUT = "/home/user/controle-ia-travail"
SORTIE_DEFAUT = RACINE_DEFAUT + "/docs/notes/organisme-ecart-conception-code-v1"

# clé, chemin relatif, préfixe d'empreinte attendu (donné par la consigne), préfixe d'identifiant, sections de dispositif
FICHIERS = [
    ("N-044", "docs/decisions/decision-N-044-v1.md", "2b70bdac", "N-044"),
    ("N-045-v1", "docs/decisions/decision-N-045-v1.md", "42be51f6", "N-045v1"),
    ("N-045-v2", "docs/decisions/decision-N-045-v2.md", "c7b05e39", "N-045v2"),
    ("N-049", "docs/decisions/decision-N-049-v1.md", "8a5bf5e5", "N-049"),
    ("N-050", "docs/decisions/decision-N-050-v1.md", "a54b128d", "N-050"),
    ("N-052", "docs/decisions/decision-N-052-v1.md", "817d218b", "N-052"),
    ("N-058", "docs/decisions/decision-N-058-v1.md", "854f2724", "N-058"),
    ("N-059", "docs/decisions/decision-N-059-v1.md", "41aff854", "N-059"),
    ("N-065", "docs/decisions/decision-N-065-v1.md", "f820e90d", "N-065"),
]
SECTIONS = {  # (préfixe de ligne de début, préfixe de ligne de fin ou None = fin de fichier)
    "N-044": [("## Énoncés retenus", "## Ce que cela change")],
    "N-045-v1": [("## Énoncés retenus", "## Ce que cela change")],
    "N-045-v2": [("## Énoncés retenus", "## Ce que cela change")],
    "N-049": [("## N-049 (proposé)", "## N-050 (proposé)")],
    "N-050": [("## N-050 (proposé)", "## Points à régler")],
    "N-052": [("## Lecture retenue", "## Réserve"), ("## Réserve", None)],
    "N-058": [("## Ce que la décision fixe", "## Ce que la décision ne fixe pas")],
    "N-059": [("## Ce que la décision fixe", None)],
    "N-065": [("## Ce que la décision fixe", "## Ce qui ne change pas")],
}

# --- masque (motifs construits par morceaux pour ne pas écrire les identifiants dans ce fichier) ---
_A = "cla" + "ude"
_NOMS = "|".join(["op" + "us", "fa" + "ble", "son" + "net", "hai" + "ku"])
MASQUES = [
    re.compile(r"\b" + _A.upper() + r"_[A-Z0-9_]+"),
    re.compile(_A + r"-[a-z0-9.-]+", re.I),
    re.compile(r"\b(?:" + _NOMS + r")\b(?:\s*5\.[?0-9]+)?", re.I),
    re.compile(r"(?<=-)(?:" + _NOMS + r")(?=-)", re.I),
]
MASQUE = "[modèle masqué]"

def masquer(s):
    n = 0
    for m in MASQUES:
        s, k = m.subn(MASQUE, s)
        n += k
    return s, n

def norm(s):
    s = s.replace("**", "").replace("`", "")
    return " ".join(s.split())

# --- portée : objet, fondements (clé de décision, phrase exacte), statut ---
OI = "organisme d'idéation (orchestrateur public)"
CA = "lignée conv-audit seulement"
DEUX = "les deux"
PC = "programme de contrôle"
DOUTE = "portée douteuse"

def _f(k, *phr):
    return [(k, p) for p in phr]

PORTEE = {}
def P(ident, objet, fond, statut="retenu"):
    PORTEE[ident] = (objet, fond, statut)

# N-044
P("N-044.1", PC, _f("N-044", "Objectif ultime (axe « contrôle de populations d'agents », essaim autonome)",
                    "cette note fixe la lecture du programme pour les préenregistrements à venir (étape 2 et suivants)"))
P("N-044.2", CA, _f("N-044", "en attente de son mot pour l'étape 1", "restent en attente du mot de Lazar"),
  "en attente du mot de Lazar")
P("N-044.3", CA, _f("N-044", "Pour l'étape 1, seul le vivier de conception entre dans sa v4 (R-378)",
                    "identifiants disjoints du test et du test final, vérifiés par le script d'extraction"))
P("N-044.4", DOUTE, _f("N-044", "le noyau peut poser une question en texte libre (question_ouverte)",
                       "posée aux organismes avant tout matériau de notre part (anti-enfermement)")
  + _f("N-065", "Il reçoit des questions ouvertes du programme"))
P("N-044.5", CA, _f("N-044", "trois bras à l'étape 2 (mission + miroir fonctionnel rendu dans historique ; contrainte câblée dans le noyau ; rien)"))
# N-045 (v1 remplacée, v2 en vigueur) : points 1 à 3 douteux, 4 lignée, 5 (v1) / 8 (v2) invariants du programme
_c13 = lambda k: (
    _f(k, "à partir de l'étape 2")
    + _f("N-058", "tout choix de la composition des proposeurs (quels modèles proposent, dans quel rôle, à quelle part du budget)",
         "et sur le coût mesuré, seuls"))
for v, rempl in (("v1", "remplacée par N-045v2"), ("v2", "retenu")):
    k = "N-045-" + v
    p = "N-045" + v
    P(p + ".1", DOUTE, _c13(k) + _f(k, "ou instrument local entraîné par le noyau (sonde, adaptateur : espèces LOCAL:<identifiant>)"), rempl)
    P(p + ".2", DOUTE, _c13(k) + _f(k, "le score de développement rendu à l'organisme dans historique porte, à côté de l'exactitude équilibrée, le coût de la génération",
                                    "Le juge externe (exactitude équilibrée sur le test caché, métrique de choix) ne change pas"), rempl)
    P(p + ".3", DOUTE, _c13(k) + _f(k, "La nécessité de la frontière est une sortie mesurée, pas un choix d'avance"), rempl)
    P(p + ".4", CA, _f(k, "Aucune voie à concepteur entraîné par renforcement n'est payée avant qu'une voie bon marché ait montré"), rempl)
P("N-045v1.5", PC, _f("N-045-v1", "R1 à R14 ; la banque scellée ; H-E1 et H-G1 tels que scellés ou en cours de scellement"), "remplacée par N-045v2")
P("N-045v2.5", CA, _f("N-045-v2", "ce que cet énoncé ajoute vaut pour l'étape 2 et le concepteur", "Pour les organismes des courses actuelles"))
P("N-045v2.6", CA, _f("N-045-v2", "l'organisme entraîne lui-même, par l'instrument (B), un adaptateur qui propose des conceptions",
                      "le concepteur figé reçoit une archive consultable des mêmes trajectoires"))
P("N-045v2.7", CA, _f("N-045-v2", "un concepteur à sortie contrainte et un concepteur à sortie libre", "la voie est à fixer après le tour v4 du collisionneur"),
  "à fixer (après le tour v4 du collisionneur)")
P("N-045v2.8", PC, _f("N-045-v2", "R1 à R14 ; la banque scellée ; H-E1 et H-G1 tels que scellés ou en cours de scellement"))
# N-049, N-050
P("N-049.1", CA, _f("N-049", "pour les pilotes de conception à partir du pilote 5, le noyau sert à chaque génération une part test tirée"))
P("N-049.2", CA, _f("N-049", "même générateur que la banque v3, tâches neuves, identifiants disjoints de v3 et de v6"))
P("N-049.3", CA, _f("N-049", "la confirmation (étape 1 décisive, confrontation, pilote décisif (b)) sur la banque v6 scellée, une famille tenue à l'écart"))
P("N-050.1", CA, _f("N-050", "À la fin de chaque course d'un pilote de conception"))
P("N-050.2", CA, _f("N-050", "Ce n'est pas un écart au texte du pilote 4"))
P("N-050.3", CA, _f("N-050", "Conséquence pour le registre d'hypothèses de la boucle extérieure"))
# N-052
P("N-052.1", CA, _f("N-052", "l'analyste de chaque course, le correcteur, et l'agent qui lit un dossier d'audit"))
P("N-052.2", CA, _f("N-052", "le contre-lecteur (parties A et B) et tout agent d'audit chargé d'attaquer un verdict (protocole de la boucle, § 12.3)"))
P("N-052.3", CA, _f("N-052", "Le paramètre « famille » du protocole prend la valeur"))
P("N-052.4", CA, _f("N-052", "conv-audit le consigne au journal et le dit à Lazar"))
# N-058
P("N-058.1", OI, _f("N-058", "l'oracle du monde planté (structures retrouvées, témoins plantés vrais promus et faux rejetés)"))
P("N-058.2", OI, _f("N-058", "classer les proposeurs par les fiches que le juge promeut, c'est sélectionner un agent sur le verdict du juge",
                    "aucun score de moniteur ni de juge n'entre dans un signal d'entraînement ou de sélection de l'agent"))
P("N-058.3", DEUX, _f("N-058", "L'ordre de travail de conv-audit",
                      "la version 32 de l'orchestrateur (prise « idéation », corrections CL31-01 à 10 de la contre-lecture R2)"))
# N-059
_t = _f("N-059", "recommandations de la conception de l'affinage v2")
P("N-059.1", DOUTE, _t + _f("N-059", "témoins silencieux à chaque génération de production"))
P("N-059.2", DOUTE, _t + _f("N-059", "un budget par génération, réparti entre les configurations enregistrées"), "retenu, détail à fixer (procédure avec un statisticien, sur devis)")
P("N-059.3", DOUTE, _t + _f("N-059", "retirée de cette course"))
P("N-059.4", DOUTE, _t + _f("N-059", "Troisième famille de modèles pour le détecteur d'injection et la revue des extensions"), "retenu, détail à fixer (choix et dépense sur devis)")
P("N-059.5", OI, _f("N-059", "le duel se tient en générations d'étalonnage (mondes plantés seulement)", "déjà fixés par N-058"))
P("N-059.6", OI, _f("N-059", "le duel se tient en générations d'étalonnage (mondes plantés seulement)", "déjà fixés par N-058"))
P("N-059.7", DOUTE, _t + _f("N-059", "(confirmé par conv-audit, n° 136)") + _f("N-065", "la réserver comme famille tenue à l'écart pour mesurer l'universalité (N-044, N-054)"))
P("N-059.8", DOUTE, _t + _f("N-059", "admise, avec un plafond (à fixer en v3)"), "retenu, détail à fixer (plafond en v3)")
P("N-059.9", DOUTE, _t + _f("N-059", "lots en phase de proposition, puis affineur isolé par fiche"))
P("N-059.10", DOUTE, _t + _f("N-059", "plafond petit, fixé fiche par fiche à une porte, sous revue externe"))
P("N-059.11", DOUTE, _t + _f("N-059", "l'épreuve est lue jusqu'au budget, partout, dès maintenant"))
P("N-059.12", DOUTE, _t + _f("N-059", "est ratifiée comme son dépôt de travail"))
P("N-059.13", DOUTE, _t + _f("N-059", "l'écart est ratifié"))
P("N-059.14", DOUTE, _t + _f("N-059", "un changement de composition se fonde sur l'étalonnage seul") + _f("N-058", "et sur le coût mesuré, seuls"))
P("N-059.15", DOUTE, _f("N-059", "avant le codage du juge et de la mémoire"))
# N-065
P("N-065.1", OI, _f("N-065", "l'organisme d'idéation est un second terrain du papier C"))
P("N-065.2", OI, _f("N-065", "l'organisme est un atelier d'idées du programme"))
P("N-065.3", PC, _f("N-065", "une famille de menaces diffuses pour les papiers A et B", "Rôle 3, à trancher"), "à trancher")
P("N-065.4", OI, _f("N-065", "aucun score d'un moniteur du programme dans l'entraînement ou la sélection de l'organisme (N-053)",
                    "citations obligatoires de N-064 dans tout texte qui présente l'organisme"))

RE_NUM = re.compile(r"^(\d+)\.\s+(?:et\s+(\d+)\.\s+)?")

def decouper(lignes, spec):
    """Rend la liste de (ligne_debut, ligne_fin, [lignes], jumeaux) des unités de dispositif (avant filtre des paragraphes)."""
    unites = []
    for deb, fin in spec:
        i = next(k for k, l in enumerate(lignes) if l.startswith(deb))
        j = len(lignes)
        if fin is not None:
            j = next(k for k in range(i + 1, len(lignes)) if lignes[k].startswith(fin))
        cur = None
        def clore():
            nonlocal cur
            if cur is not None:
                unites.append(cur)
                cur = None
        for k in range(i + 1, j):
            l = lignes[k].rstrip("\n")
            if not l.strip():
                clore(); continue
            if l.startswith("## ") or l.startswith("# "):
                clore(); continue
            m = RE_NUM.match(l)
            if m:
                clore()
                nums = [int(m.group(1))] + ([int(m.group(2))] if m.group(2) else [])
                cur = {"type": "numero", "nums": nums, "debut": k + 1, "fin": k + 1, "lignes": [l]}
            elif l.startswith("- "):
                clore()
                cur = {"type": "puce", "nums": [], "debut": k + 1, "fin": k + 1, "lignes": [l]}
            elif cur is not None:
                cur["lignes"].append(l); cur["fin"] = k + 1
            else:
                cur = {"type": "paragraphe", "nums": [], "debut": k + 1, "fin": k + 1, "lignes": [l]}
        clore()
    return unites

def articles_de(cle, prefixe, lignes):
    out, rang = [], 0
    for u in decouper(lignes, SECTIONS[cle]):
        txt = "\n".join(u["lignes"])
        if u["type"] == "paragraphe":
            plat = " ".join(txt.split())
            if plat.endswith(":") or plat.endswith(" :") or plat.startswith("Numéro"):
                continue
        nb = len(u["nums"]) if u["type"] == "numero" else 1
        for q in range(nb):
            rang += 1
            out.append({"decision": cle, "identifiant": "%s.%d" % (prefixe, rang), "type": u["type"],
                        "jumele": nb > 1, "ligne": u["debut"], "ligne_fin": u["fin"], "texte_brut": txt})
    return out

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--racine", default=RACINE_DEFAUT)
    ap.add_argument("--sortie", default=SORTIE_DEFAUT)
    ap.add_argument("--table", action="store_true", help="imprime les lignes de la table markdown")
    ap.add_argument("--verifier-md", default=None)
    a = ap.parse_args()
    erreurs, sources, textes, arts = [], {}, {}, []
    for cle, rel, pref, idp in FICHIERS:
        ch = os.path.join(a.racine, rel)
        data = open(ch, "rb").read()
        h = hashlib.sha256(data).hexdigest()
        comp = open(ch + ".sha256").read().split()[0]
        if not h.startswith(pref) or h != comp:
            erreurs.append("empreinte %s : calculée %s, attendue %s…, compagnon %s" % (rel, h, pref, comp))
        t = data.decode("utf-8")
        lignes = t.split("\n")
        sources[cle] = {"chemin": rel, "sha256": h, "nombre_de_lignes": len(lignes) - (1 if lignes[-1] == "" else 0)}
        textes[cle] = norm(t)
        arts.extend(articles_de(cle, idp, lignes))
    ids = [x["identifiant"] for x in arts]
    if len(set(ids)) != len(ids):
        erreurs.append("identifiants en double")
    if set(ids) != set(PORTEE):
        erreurs.append("articles sans portée : %s ; portées sans article : %s" % (sorted(set(ids) - set(PORTEE)), sorted(set(PORTEE) - set(ids))))
    for i, (objet, fond, st) in PORTEE.items():
        for k, ph in fond:
            if norm(ph) not in textes[k]:
                erreurs.append("fondement introuvable dans %s pour %s : %s" % (k, i, ph))
    if erreurs:
        for e in erreurs:
            print("ERREUR", e, file=sys.stderr)
        sys.exit(2)
    out = []
    for x in arts:
        objet, fond, st = PORTEE[x["identifiant"]]
        txt, n = masquer(x.pop("texte_brut"))
        fm = [{"decision": k, "phrase": masquer(ph)[0]} for k, ph in fond]
        x.update({"texte": txt, "masque_applique": n > 0, "objet": objet, "fondement": fm, "statut": st})
        out.append(x)
    totaux = {}
    for x in out:
        totaux[x["decision"]] = totaux.get(x["decision"], 0) + 1
    # comparaison N-045 v1 / v2 (texte masqué, normalisé, sans le numéro de tête)
    def corps(x):
        return norm(re.sub(r"^\d+\.\s+", "", x["texte"].replace("\n", " ")))
    v1 = [x for x in out if x["decision"] == "N-045-v1"]
    v2 = [x for x in out if x["decision"] == "N-045-v2"]
    diff = {"identiques": [], "nouveaux_dans_v2": [], "absents_de_v2": []}
    for x in v1:
        c = next((y for y in v2 if corps(y) == corps(x)), None)
        if c:
            diff["identiques"].append([x["identifiant"], c["identifiant"]])
        else:
            diff["absents_de_v2"].append(x["identifiant"])
    pris = {p[1] for p in diff["identiques"]}
    diff["nouveaux_dans_v2"] = [y["identifiant"] for y in v2 if y["identifiant"] not in pris]
    res = {"programme": "compter_articles_decisions_v1.py", "lecteur": "modèle C",
           "regle": __doc__.split("RÈGLE DE DÉCOUPAGE")[1].split("MASQUAGE")[0].strip(),
           "sources": sources, "totaux_par_decision": totaux, "total_general": sum(totaux.values()),
           "total_en_vigueur_hors_N-045-v1": sum(v for k, v in totaux.items() if k != "N-045-v1"),
           "diff_N-045_v1_v2": diff, "articles": out}
    if a.table:
        for x in out:
            fl = " ; ".join(("« %s »" if f["decision"] == x["decision"] else "[" + f["decision"] + "] « %s »") % f["phrase"] for f in x["fondement"])
            print("| %s | %d-%d | %s | %s | %s |" % (x["identifiant"], x["ligne"], x["ligne_fin"], x["objet"], x["statut"], fl.replace("|", "/")))
    if a.verifier_md:
        md = open(a.verifier_md, encoding="utf-8").read()
        manque = [i for i in ids if ("| %s |" % i) not in md]
        dbl = [i for i in ids if md.count("| %s |" % i) != 1]
        print("md : identifiants manquants", manque, "; non uniques", dbl)
        if manque or dbl:
            sys.exit(3)
    dest = os.path.join(a.sortie, "articles-decisions-v1.json")
    if not a.table and not a.verifier_md:
        os.makedirs(a.sortie, exist_ok=True)
        with open(dest, "x", encoding="utf-8") as f:   # création seulement
            json.dump(res, f, ensure_ascii=False, indent=1)
            f.write("\n")
        print("écrit", dest)
    print("totaux", json.dumps(totaux, ensure_ascii=False), "total", res["total_general"], "en vigueur", res["total_en_vigueur_hors_N-045-v1"])
    print("diff N-045", json.dumps(diff, ensure_ascii=False))

if __name__ == "__main__":
    main()

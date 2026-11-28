"""Banc du vérificateur neuf (lentille « dépense et arrêts ») : révocations sous des formes voisines et forme de l'accord,
sur `verifications_p4_v1.py` de la chaîne v2 (importé par son chemin, sans module de P4 : fonctions pures seulement),
sur les registres réels (lus, jamais écrits) et sur des artefacts fabriqués ici. Aucun texte de P3, aucune donnée lue.
Usage : python -B banc_voisines_v1.py CHEMIN_VERIFICATIONS REGISTRE_GO REGISTRE_DECISIONS"""
import hashlib, importlib.util, sys
sys.dont_write_bytecode = True
chemin, go_reel, dec_reel = sys.argv[1:4]
spec = importlib.util.spec_from_file_location("verif_v2", chemin)
v = importlib.util.module_from_spec(spec); spec.loader.exec_module(v)
print(f"script éprouvé : verifications_p4_v1.py {hashlib.sha256(open(chemin,'rb').read()).hexdigest()}")
GO = open(go_reel, encoding="utf-8").read(); DEC = open(dec_reel, encoding="utf-8").read()
print(f"registres réels lus : go.md {hashlib.sha256(GO.encode()).hexdigest()[:16]} ; decisions.md {hashlib.sha256(DEC.encode()).hexdigest()[:16]}")
J = "2026-10-21"
ecarts = 0
def cas(nom, attendu_bloque, go_ajout="", dec_ajout="", note=""):
    global ecarts
    t = v.revocations_voisines(GO + go_ajout, DEC + dec_ajout)
    bloque = bool(t)
    ok = bloque == attendu_bloque
    ecarts += not ok
    print(f"{nom} : {'bloqué (code 2)' if bloque else 'passe'} ; attendu {'bloqué' if attendu_bloque else 'passe'} ; "
          f"{'CONFORME' if ok else 'ÉCART'}{' — ' + note if note else ''}")
# 0. registres réels : aucune fausse alerte
t = v.revocations_voisines(GO, DEC)
print(f"V00-registres-reels : {len(t)} ligne(s) voisine(s) ; attendu 0 ; {'CONFORME' if not t else 'ÉCART'}")
ecarts += bool(t)
# proximité des fausses alertes : têtes de cellule de décision qui commencent par un début de révocation (sans identifiant)
n_tetes = 0
for ligne in DEC.split("\n"):
    k = v._cellules_n(ligne)
    if k and len(k) >= 3 and v.re.fullmatch(r"r-\d{3,4}", k[0]) and k[2].lstrip("*_ \"'«»`([").startswith(v.DEBUTS_REVOCATION):
        n_tetes += 1
types = sorted({(v._cellules_n(l) or ["", "", ""])[2] for l in GO.split("\n") if (v._cellules_n(l) or [""])[0].startswith("go-")})
print(f"    information : {n_tetes} cellule(s) de décision réelles commencent par un début de révocation (sans nommer les cinq) ; types lus au registre des GO : {types}")
# 1. formes voisines couvertes par la décision de la session (cas sains du correcteur, rejoués)
cas("V01-go-sans-espace", True, go_ajout=f"\n|GO-2026-10-21-01|{J}|révocation|révoque GO-2026-10-20-07|—|{J}|Lazar|essai|")
cas("V02-type-majuscule-sans-accent", True, go_ajout=f"\n| GO-2026-10-21-01 | {J} | REVOCATION | R-269 | — | {J} | Lazar | essai |")
cas("V03-deux-identifiants", True, dec_ajout=f"\n| R-998 | {J} | **Révocation de R-262 et de R-269** | essai |")
cas("V04-tiret-insecable", True, dec_ajout=f"\n| R-998 | {J} | révocation de R‑269 | essai |")
cas("V05-blancs-en-tete", True, dec_ajout=f"\n   | R-998 | {J} | **Révocation de R-269.** | essai |")
# 2. témoins sains : mentions libres (doivent passer)
cas("V10-mention-libre", False, dec_ajout=f"\n| R-998 | {J} | Note : la forme « **Révocation de R-269** » est décrite ici. | essai |")
cas("V11-identifiant-voisin", False, dec_ajout=f"\n| R-998 | {J} | **Révocation de R-2690** | essai |")
cas("V12-go-de-calcul-qui-cite-la-phase", False, go_ajout=f"\n| GO-2026-10-21-01 | {J} | calcul | sous GO-2026-10-04-08 | 1 USD | {J} | Lazar | essai |")
# 3. artefacts du vérificateur : formes voisines hors de la liste éprouvée
cas("X01-decision-sans-colonne-de-date", True, dec_ajout=f"\n| R-998 | **Révocation de R-269** : délégation retirée |",
    note="ligne de décision à deux cellules (date omise) ; le module exige aussi trois cellules")
cas("X02-decision-colonne-vide-en-trop", True, dec_ajout=f"\n| R-998 | {J} | | **Révocation de R-269** | essai |",
    note="cellule vide avant la décision")
cas("X03-identifiant-de-decision-en-gras", True, dec_ajout=f"\n| **R-998** | {J} | **Révocation de R-269** | essai |",
    note="première cellule en gras")
cas("X04-identifiant-de-go-en-gras", True, go_ajout=f"\n| **GO-2026-10-21-01** | {J} | révocation | GO-2026-10-20-07 | — | {J} | Lazar | essai |",
    note="première cellule en gras : ni la garde, ni le module, ni les formes voisines ne la lisent")
cas("X05-go-de-type-decision-qui-revoque", True, go_ajout=f"\n| GO-2026-10-21-01 | {J} | décision | Révocation de GO-2026-10-20-07 (délégation retirée) | — | {J} | Lazar | essai |",
    note="type connu autre que révocation, cellule de périmètre qui commence par « Révocation »")
cas("X06-sujet-avant-le-verbe", True, dec_ajout=f"\n| R-998 | {J} | Lazar révoque R-269 à compter de ce jour | essai |",
    note="mention libre au sens de la précision 5 du texte : passe par construction")
cas("X07-suspension", True, dec_ajout=f"\n| R-998 | {J} | **Suspension de R-269** jusqu'à nouvel ordre | essai |",
    note="verbe hors de la liste (révocation, révoque, annulation, retrait)")
cas("X08-identifiant-sans-tiret", True, dec_ajout=f"\n| R-998 | {J} | **Révocation de R 269** | essai |",
    note="identifiant écrit sans tiret")
cas("X09-retrait-qui-ne-revoque-pas", False, dec_ajout=f"\n| R-998 | {J} | Retrait de l'instance 56799469 du registre (R-262 inchangé) | essai |",
    note="fausse alerte attendue par construction (refus plus large)")
# 4. forme de l'accord (expression FORME_DEPENSE, sommes au centime) : fonctions pures
F = v.FORME_DEPENSE
def forme(nom, texte, attendu):
    global ecarts
    m = F.findall(texte)
    ok_forme = len(m) == 1 and texte.count("dépense consignée") == 1
    res = "refus"
    if ok_forme:
        x, y = m[0]
        res = "accepté" if v._centimes(x) + 541 == v._centimes(y) and v._centimes(y) < 15000 else "refus"
    ok = res == attendu; ecarts += not ok
    print(f"{nom} : {res} ; attendu {attendu} ; {'CONFORME' if ok else 'ÉCART'}")
forme("F00-forme-du-texte", "dépense consignée 47,83 USD + borne 5,41 USD = 53,24 USD < 150 USD", "accepté")
forme("F01-espaces-insecables", "dépense consignée 47,83 USD + borne 5,41 USD = 53,24 USD < 150 USD", "refus")
forme("F02-somme-fausse", "dépense consignée 47,83 USD + borne 5,41 USD = 53,25 USD < 150 USD", "refus")
forme("F03-y-a-150", "dépense consignée 144,59 USD + borne 5,41 USD = 150,00 USD < 150 USD", "refus")
forme("F04-y-juste-sous-150", "dépense consignée 144,58 USD + borne 5,41 USD = 149,99 USD < 150 USD", "accepté")
forme("F05-point-decimal", "dépense consignée 47.83 USD + borne 5,41 USD = 53.24 USD < 150 USD", "refus")
forme("F06-x-a-une-decimale", "dépense consignée 47,8 USD + borne 5,41 USD = 53,21 USD < 150 USD", "refus")
forme("F07-y-a-quatre-chiffres", "dépense consignée 1047,83 USD + borne 5,41 USD = 1053,24 USD < 150 USD", "refus")
forme("F08-borne-autre", "dépense consignée 47,83 USD + borne 5,40 USD = 53,23 USD < 150 USD", "refus")
forme("F09-plafond-1500", "dépense consignée 47,83 USD + borne 5,41 USD = 53,24 USD < 1500 USD", "accepté")
# GO à frontières de mot
G = v.GO_A_FRONTIERES
for nom, t, att in (("G00-go-suivi-d-un-point", "délégation GO-2026-10-20-07.", True), ("G01-go-voisin-071", "GO-2026-10-20-071", False),
                    ("G02-go-suffixe-bis", "GO-2026-10-20-07-bis", False), ("G03-go-entre-parentheses", "(GO-2026-10-20-07)", True),
                    ("G04-go-colle-a-un-mot", "xGO-2026-10-20-07", False)):
    r = bool(G.search(t)); ok = r == att; ecarts += not ok
    print(f"{nom} : {'cité' if r else 'non cité'} ; attendu {'cité' if att else 'non cité'} ; {'CONFORME' if ok else 'ÉCART'}")
print(f"FIN DU BANC DES FORMES VOISINES ET DE L'ACCORD ; écarts : {ecarts}")

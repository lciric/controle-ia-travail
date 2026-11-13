"""Épreuve du contre-lecteur (lecture seule, aucun lancement) : les deux lignes de GO de la sonde proposées par le développeur,
telles qu'il les écrit, lues par `lire_go_de_la_sonde` sur un registre d'essai. Usage : python -I -B … RACINE_ORCHESTRATOR DOSSIER"""
import datetime, os, sys
RACINE, D = sys.argv[1], sys.argv[2]
sys.path.insert(0, RACINE)
from pole import pilote_mr2_v70 as P, proposeurs_pilote_v70 as PR
conf, _ = PR.lire_configuration(os.path.join(RACINE, "exemples", "pilote-mr2-v70", "configuration-pilote-mr2-v11.json"))
os.makedirs(D, exist_ok=True)
j = datetime.date(2026, 11, 14); fin = "2026-11-21"
P1 = ("Pilote MR-2 : sonde des relais Fable 5.2 et Opus 5.5 sur crédits de Claude, avant le scellement du texte : par relais, un appel à la "
      "borne gelée (réponse d'un mot) et un à 256 jetons, consignes de 100 octets au plus, par la sous-commande « sonde » du lanceur v70 ; "
      "aucun monde, aucun résultat ; relevé scellé, cité au bloc gelé du texte ; prix rapprochés de la console par Lazar ; jamais de ligne "
      "d'extension ; arrêt par identifiant (R10)")
P2 = "Pilote MR-2 : sonde des relais Argon et Astra hors crédits, mêmes conditions que la ligne s1"
def registre(nom, id1, id2):
    f = os.path.join(D, nom)
    with open(f, "w", encoding="utf-8") as h:
        h.write("| id | accordé le | type | périmètre | plafond | échéance | accordé par | référence |\n|---|---|---|---|---|---|---|---|\n"
                f"| {id1} | {j} | calcul | {P1} | 4.39 USD | {fin} | Lazar | R-2548 ; mot de Lazar |\n"
                f"| {id2} | {j} | calcul | {P2} | 3.68 USD | {fin} | Lazar | R-2548 ; mot de Lazar |\n")
    return f
for nom, id1, id2 in (("identifiants-nus.md", "GO-2026-11-14-01", "GO-2026-11-14-02"),
                      ("identifiants-avec-etiquette.md", "GO-2026-11-14-01 (s1)", "GO-2026-11-14-02 (s2)")):
    try:
        g = PR.lire_go_de_la_sonde(conf, registre(nom, id1, id2), "GO-2026-11-14-01", "GO-2026-11-14-02", aujourd_hui=j)
        print(nom, "→ lues :", {k: (v["plafond_lu_usd"], v["forme_du_plafond"]) for k, v in g.items()})
    except P.Refus as e:
        print(nom, "→ REFUS :", str(e)[:160])
try:
    PR.lire_go_du_pilote(conf, os.path.join(D, "identifiants-nus.md"), "GO-2026-11-14-01", "GO-2026-11-14-02", aujourd_hui=j)
    print("lignes de la sonde lues comme π1 et π2 : ADMISES")
except P.Refus as e:
    print("lignes de la sonde présentées comme π1 et π2 → REFUS :", str(e)[:160])

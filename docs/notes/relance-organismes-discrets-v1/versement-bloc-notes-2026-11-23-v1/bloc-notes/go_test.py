from datetime import date
from controle_ia.organismes_discrets import lanceur_bras_a_v4 as L
from controle_ia.gardes import GardeArret
LIGNE = "| GO-2026-11-22-148 | 2026-11-22 | calcul | Même mot (GO-2026-11-22-147) : bras A, ligne 1 de carte (fabrication et rejeu honnête, 128 épisodes), devis docs/notes/relance-organismes-discrets-v1/devis-bras-a-v5.md (40b999f8…), plafond 18 USD ; départ seulement après les préalables de 13.2 tenus, texte v2 scellé, lanceur prêt et contre-lu, et crédit suffisant. | 18 USD | 2026-11-30 | Lazar | mot direct |"
reg = "| id | a | t | p | pl | e | par | ref |\n|---|---|---|---|---|---|---|---|\n" + LIGNE + "\n"
try:
    print(L.exiger_ligne_de_go("GO-2026-11-22-148", reg, date(2026,11,23)))
except GardeArret as e:
    print("REFUS:", e)
# reste des champs : perimetre remplacé par le libellé v4
reg2 = reg.replace("Même mot (GO-2026-11-22-147) : bras A, ligne 1 de carte", "bras A, ligne 1 du bras A")
try:
    print(L.exiger_ligne_de_go("GO-2026-11-22-148", reg2, date(2026,11,23)))
except GardeArret as e:
    print("REFUS2:", e)
# autres champs : on neutralise le périmètre pour tester les autres gardes
import re
orig = L.exiger_perimetre_de_la_ligne_1
L.exiger_perimetre_de_la_ligne_1 = lambda g,p: p
print("autres champs ok:", L.exiger_ligne_de_go("GO-2026-11-22-148", reg, date(2026,11,23)))
for nom, mod in [("echeance", lambda s: s.replace("2026-11-30","2026-11-22")), ("lazar", lambda s: s.replace("| Lazar |","| Lazar-X |")),
                 ("type", lambda s: s.replace("| calcul |","| autre |"))]:
    try: L.exiger_ligne_de_go("GO-2026-11-22-148", mod(reg), date(2026,11,23)); print(nom,"PASSE")
    except GardeArret as e: print(nom,"refus")
L.exiger_perimetre_de_la_ligne_1 = orig
# candidats de règle
def regle(p):
    n=" ".join(p.split()).lower()
    ms=[m for m in re.finditer(r"(?<![\w-])lignes?\s+(\S+)", n)]
    return len(ms)>=1 and all(m.group(0).split()[0]=="ligne" and m.group(1).rstrip(".,;:)")=="1" for m in ms) and re.search(r"(?<![\w-])bras a\b",n) is not None
per = LIGNE.split("|")[4].strip()
tests = {"reel":per,"l2":per.replace("ligne 1 de carte","ligne 2 de carte"),"pluriel":per.replace("ligne 1 de carte","lignes 1 et 2 de carte"),
 "moniteurs":per.replace("bras A, ligne 1 de carte","bras A, moniteurs"), "bras B":per.replace("bras A","bras B"),
 "l1 et l2":per+" et ligne 2", "ligne 1 du bras A":"ligne 1 du bras A", "l10":per.replace("ligne 1 de","ligne 10 de")}
for k,v in tests.items(): print(k, regle(v))

#!/usr/bin/env python3
# faire_hc1.py -- assemble le devis des lectures hors carte (brouillon 1) :
# gabarit + valeurs de calc_hc1.py. N'ecrit que le fichier de sortie donne en argument.
import hashlib
import json
import os
import re
import subprocess
import sys

ici = os.path.dirname(os.path.abspath(__file__))
sortie, date_utc = sys.argv[1], sys.argv[2]
assert re.fullmatch(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z", date_utc), date_utc

brut = subprocess.run([sys.executable, "-I", os.path.join(ici, "calc_hc1.py"), "--json"],
                      check=True, capture_output=True, text=True).stdout
d = json.loads(brut)
v = dict(d["valeurs"])
v["TRACE"] = "\n".join(d["trace"])
v["DATE"] = date_utc
v["BLOC"] = ici
v["SHA_CALC"] = hashlib.sha256(open(os.path.join(ici, "calc_hc1.py"), "rb").read()).hexdigest()

L = [
    ("Premier lecteur, lots d'épreuve",
     "bras A, lectures hors carte, premier lecteur de l'oracle ([identifiant du modèle Claude], réglage fixé sur l'essai de mesure), lots d'épreuve : 2 496 appels, 7 488 envois au plus ; plafond {{PL1_EPREUVE}} USD au plus, ramené à 2 fois la projection refaite sur les compteurs de l'essai de mesure si elle est plus basse ; tenu par compteur avant chaque envoi, au régime prudent ; pire cas tenu par les gardes : le plafond et un envoi coupé, [valeur] USD ; compté à [entrée] et [sortie] USD par million ; ne part qu'après le texte scellé, ce devis accepté, le programme contre-lu et ses gardes éprouvées."),
    ("Premier lecteur, lots décisifs",
     "bras A, lectures hors carte, premier lecteur de l'oracle, lots décisifs : 10 464 appels, 31 392 envois au plus ; plafond recalculé par programme à 1,5 fois la projection sur les coûts comptés à ses lots d'épreuve, {{PL1_DECISIF}} USD au plus ; au-dessus de {{PL1_DECISIF}} USD, la ligne ne part pas : nœud de Lazar ; compteur au régime prudent ; ne part qu'après les épreuves passées selon le texte."),
    ("Premier lecteur, lots de la révision",
     "bras A, lectures hors carte, premier lecteur de l'oracle, lots de la révision, seulement si la révision est ouverte selon le texte : 2 176 appels, 6 528 envois au plus ; plafond recalculé comme à la ligne 2, {{PL1_REVISION}} USD au plus."),
    ("Second lecteur, lots d'épreuve",
     "bras A, lectures hors carte, second lecteur de l'oracle (`mistral-large-4-0`, par le point d'accès du relevé de vérification), seulement s'il est admis ; lots d'épreuve : 2 496 appels, 7 488 envois au plus ; plafond {{PL2_EPREUVE}} USD au plus, ramené à 2 fois la projection sur les compteurs de son essai d'admission si elle est plus basse ; tenu par compteur et par une borne dure en octets par envoi ; pire cas tenu par les gardes {{PIRE2_EPREUVE}} USD, sous la supposition, non documentée, que la coupure arrête la génération et la facturation ; compté à 0,77 et 2,31 USD par million."),
    ("Second lecteur, lots décisifs",
     "bras A, lectures hors carte, second lecteur de l'oracle (`mistral-large-4-0`), lots décisifs : 10 464 appels, 31 392 envois au plus ; plafond recalculé par programme à 1,5 fois la projection sur les coûts comptés à ses lots d'épreuve, {{PL2_DECISIF}} USD au plus ; au-dessus de {{PL2_DECISIF}} USD, la ligne ne part pas : nœud de Lazar ; pire cas tenu par les gardes : le plafond et {{CM_2690}} USD, sous la même supposition ; compté à 0,77 et 2,31 USD par million ; ne part qu'après les épreuves passées selon le texte."),
    ("Second lecteur, lots de la révision",
     "bras A, lectures hors carte, second lecteur de l'oracle (`mistral-large-4-0`), lots de la révision, seulement si la révision est ouverte selon le texte : 2 176 appels, 6 528 envois au plus ; plafond recalculé comme à la ligne 5, {{PL2_REVISION}} USD au plus ; compté à 0,77 et 2,31 USD par million."),
    ("Juge des deux ancres",
     "bras A, lectures hors carte, juge des deux ancres (`gemini-4-neon`), seulement s'il est admis : 80 appels, 240 envois au plus ; plafond {{PLJ_80}} USD au plus, ramené à 3 fois la projection sur les compteurs de son essai d'admission si elle est plus basse ; compteur au régime prudent ; pire cas tenu par les gardes {{PIREJ_80}} USD, si la coupure arrête la génération et la facturation, ce qui n'est pas documenté ; rien de dur au-delà (recharge automatique activée, aucun plafond de dépense : GO-2026-11-21-68) ; compté à 3 et 15 USD par million ; règle des appels à Google tenue par code (GO-2026-11-21-71)."),
    ("Juge, ancres de la révision",
     "bras A, lectures hors carte, juge des deux ancres (`gemini-4-neon`), ancres de la révision, seulement si la révision est ouverte selon le texte : 72 appels, 216 envois au plus ; plafond {{PLJ_72}} USD au plus, ramené à 2 fois la projection sur le coût compté à la ligne 7 si elle est plus basse ; mêmes suppositions et mêmes règles que la ligne 7."),
    ("Moniteur boîte noire par action en contexte (côté habilité)",
     "bras A, lectures hors carte, moniteur boîte noire par action en contexte : 6 400 lectures avec raisonnement ; modèle, consigne, tarif et envois par appel : cases du côté habilité ; coût = k × 6 400 × [(2 866 + c) × pe + s × ps] ÷ 1 000 000 ; plafond conditionnel : 3 fois ce coût aux valeurs supposées, 2 fois sur une mesure d'au moins 24 lectures, plus la réserve d'un envoi, arrondi aux 5 USD supérieurs ; la ligne ne se demande qu'une fois les cases remplies et son devis propre écrit."),
    ("Juge d'une autre lignée (côté habilité)",
     "bras A, lectures hors carte, juge d'une autre lignée : 6 400 lectures, sous réserve du sens des « 102 points de lecture par action » ; même formule, mêmes cases et même plafond conditionnel que la ligne 9."),
]


def remplir(txt):
    def f(m):
        k = m.group(1)
        if k not in v:
            raise SystemExit("valeur inconnue : " + k)
        return v[k]
    return re.sub(r"\{\{([A-Z0-9_]+)\}\}", f, txt)


lignes = []
for i, (titre, corps) in enumerate(L, 1):
    corps = remplir(corps)
    n = len(corps)
    if n > 600:
        raise SystemExit(f"ligne {i} : {n} signes, plus de 600")
    lignes.append(f"{i}. **{titre}** : {corps}")
    print(f"ligne {i} : {n} signes", file=sys.stderr)
v["LIGNES"] = "\n".join(lignes)

gab = open(os.path.join(ici, "gabarit_hc1.md"), encoding="utf-8").read()
doc = remplir(gab)

# controles
assert "{{" not in doc and "}}" not in doc
assert "GO-2026-11-19" not in doc, "une ligne de GO du 19 novembre est nommee"
for mot in ("intervalle", "repère", "repere", "dégénéré", "non ajustable", "moniteur appris", "anomalie"):
    assert mot not in doc.lower(), "mot du registre interdit : " + mot
for m in re.finditer(r"GO-\d{4}-\d{2}-\d{2}-\d+", doc):
    assert m.group(0) in ("GO-2026-11-21-63", "GO-2026-11-21-68", "GO-2026-11-21-69", "GO-2026-11-21-71"), m.group(0)
assert not re.search(r"[\U0001F300-\U0001FAFF☀-➿]", doc), "symbole de type emoji"
if os.path.exists(sortie) and "--ecraser-le-bloc-notes" not in sys.argv:
    raise SystemExit("la sortie existe deja (R12) : " + sortie)
with open(sortie, "w", encoding="utf-8") as f:
    f.write(doc)
print("ecrit :", sortie, len(doc.encode("utf-8")), "octets,", doc.count("\n"), "lignes", file=sys.stderr)

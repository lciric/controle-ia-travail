"""Portage des corrections 44 à 58 de la relecture de Fable c1cebee3… sur les pièces de la comparaison essaim, v4 -> v5.

Opus 5.5, 22 novembre 2026. Rien n'est conçu ici : chaque ANCIEN et chaque NOUVEAU est lu par programme dans la
relecture (entre le premier « et le dernier » de la ligne désignée), jamais recopié à la main. Chaque ANCIEN, ou chaque
borne d'un ANCIEN donné « de … à … », doit se trouver exactement une fois dans la v4 ; sinon arrêt, rien n'est écrit.
Vérifications après portage : chaque NOUVEAU présent dans la v5 ; chaque ANCIEN absent de la v5, sauf s'il est contenu
dans son NOUVEAU (il doit alors y figurer une seule fois) ; le corps de la v4 se retrouve exactement en défaisant les
corrections dans l'ordre inverse. Refuse d'écraser la v5 (R12). Lancer depuis ce dossier : python3 -I portage_pieces_essaim_v5_v1.py
"""
import hashlib
import json
import pathlib
import re
import sys

ICI = pathlib.Path(__file__).resolve().parent
V4 = ICI / "pieces-comparaison-essaim-v4.md"
REL = ICI / "relecture-pieces-essaim-v4" / "relecture-fable-api.md"
V5 = ICI / "pieces-comparaison-essaim-v5.md"
RAPPORT = ICI / "portage-pieces-essaim-v5-sortie-v1.json"
SHA_V4 = "48caa135c62e82b50f27fd698a37f5d2554163e6af9a3a97d887f2a1dc510ab3"
SHA_REL = "c1cebee3a8abec9cc142c458a6eb05800f2095fcef576fc99c0a93a974c7b4d7"


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


class Arret(Exception):
    pass


if sha(V4) != SHA_V4 or sha(REL) != SHA_REL:
    raise SystemExit("empreinte de la v4 ou de la relecture inattendue : arrêt")

REL_L = REL.read_text(encoding="utf-8").split("\n")


def g(n, apres=None):
    """Texte entre le premier « et le dernier » de la ligne n (numérotée à partir de 1), après le marqueur."""
    l = REL_L[n - 1]
    if apres is not None:
        assert l.count(apres) == 1, (n, apres)
        l = l.split(apres, 1)[1]
    i, j = l.index("« "), l.rindex(" »")
    return l[i + 2:j]


def bornes(n):
    m = re.fullmatch(r"- ANCIEN : de « (.*) » à « (.*) »\.?", REL_L[n - 1])
    assert m, n
    return m.group(1), m.group(2)


def puces(ns):
    """Puces « - « … » » de la relecture, jointes en puces de la pièce ; la première prend la place du texte remplacé."""
    return "\n- ".join(g(n) for n in ns)


texte4 = V4.read_text(encoding="utf-8")
SEP = "\n---\n\n# Demande 10"
assert texte4.count(SEP) == 1
entete4, corps4 = texte4.split(SEP, 1)
corps4 = SEP + corps4

# (numéro, sorte, données). Sortes : « remplace » (ancien, nouveau) ; « plage » (début, fin, nouveau) ;
# « insere_apres » (ancre, ajout) : l'ajout est placé juste après l'ancre, qui doit être unique.
ARTICLE14 = "\n".join(REL_L[102:114])
assert ARTICLE14.startswith("« **Article 14") and ARTICLE14.endswith("exploratoire. »")
ARTICLE14 = ARTICLE14[2:-2]
CORR = [
    ("44", "remplace", g(46), g(47)),
    ("45", "remplace", g(50), g(51)),
    ("46", "remplace", g(54), g(55)),
    ("47", "remplace", g(58), g(58) + " " + g(59, "suivie de : ")),
    ("48", "plage", *bornes(62), puces([64, 65, 66, 67])),
    ("49", "plage", *bornes(70), puces([72, 73])),
    ("50", "plage", *bornes(77), g(78)),
    ("51", "plage", *bornes(81), g(82)),
    ("52 (ajout en tête)", "insere_apres", "**Article 10 — Règle de décision (seuils de convention).**\n", "- " + g(85) + "\n"),
    ("52", "remplace", g(86), g(87)),
    ("53", "remplace", g(90), g(90) + "\n" + g(91, "suivie de ")),
    ("54", "remplace", g(94), g(95)),
    ("55", "remplace", g(98), g(99)),
    ("56", "insere_apres", "les prévisions face aux résultats, l'empreinte du code.\n", "\n" + ARTICLE14 + "\n"),
    ("57 (plan, ajout)", "insere_apres",
     "- L'enveloppe de l'essaim égale le coût mesuré du mode isolé sur la même question, à dix pour cent près.\n",
     "- " + g(117) + "\n"),
    ("57", "remplace", g(118, "ANCIEN : "), g(119)),
    ("58", "remplace", g(122), g(123)),
]


def porter(corps):
    faits, defaire = [], []
    for c in CORR:
        num, sorte = c[0], c[1]
        if sorte == "remplace":
            ancien, nouveau = c[2], c[3]
            k = corps.count(ancien)
            if k != 1:
                raise Arret(f"correction {num} : ANCIEN trouvé {k} fois")
            corps = corps.replace(ancien, nouveau)
            faits.append({"n": num, "sorte": sorte, "occurrences_ancien": k, "ancien": ancien, "nouveau": nouveau})
            defaire.append((nouveau, ancien))
        elif sorte == "plage":
            debut, fin, nouveau = c[2], c[3], c[4]
            kd, kf = corps.count(debut), corps.count(fin)
            if kd != 1 or kf != 1:
                raise Arret(f"correction {num} : début trouvé {kd} fois, fin {kf} fois")
            i = corps.index(debut)
            j = corps.index(fin) + len(fin)
            if j <= i:
                raise Arret(f"correction {num} : fin avant le début")
            ancien = corps[i:j]
            corps = corps[:i] + nouveau + corps[j:]
            faits.append({"n": num, "sorte": sorte, "occurrences_debut": kd, "occurrences_fin": kf,
                          "ancien": ancien, "nouveau": nouveau})
            defaire.append((nouveau, ancien))
        else:
            ancre, ajout = c[2], c[3]
            k = corps.count(ancre)
            if k != 1:
                raise Arret(f"correction {num} : ancre trouvée {k} fois")
            corps = corps.replace(ancre, ancre + ajout)
            faits.append({"n": num, "sorte": sorte, "occurrences_ancre": k, "ancre": ancre, "ajout": ajout})
            defaire.append((ancre + ajout, ancre))
    return corps, faits, defaire


ENTETE5 = f"""Version 5 : corrections 44 à 58 de la relecture c1cebee3… portées par Opus 5.5

- Base : `docs/notes/demandes-fable-api-2026-11-22-v1/pieces-comparaison-essaim-v4.md`, sha256 {SHA_V4}.
- Remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/relecture-pieces-essaim-v4/relecture-fable-api.md`, sha256 {SHA_REL}.
- Table des corrections : `docs/notes/demandes-fable-api-2026-11-22-v1/table-corrections-pieces-essaim-v5.md`.
- Épreuves rejouées sur la version 5 : `docs/notes/demandes-fable-api-2026-11-22-v1/epreuves-pieces-essaim-v5-v1.md`.
- Non scellable en l'état d'après la relecture : le lot aveugle de l'article 9 n'est pas joué.
- En-tête de la version 4, gardé tel quel ci-dessous.

"""


def main():
    if V5.exists():
        print("la v5 existe déjà : on n'écrase pas (R12)")
        return 1
    try:
        corps5, faits, defaire = porter(corps4)
    except Arret as e:
        print(f"ARRÊT : {e}")
        return 1
    verifs = []
    for f in faits:
        nouveau = f.get("nouveau", f.get("ajout"))
        ancien = f.get("ancien", f.get("ancre"))
        nv = corps5.count(nouveau)
        if f["sorte"] == "insere_apres":
            ok = corps5.count(ancien + nouveau) == 1
            verifs.append({"n": f["n"], "ajout_present": corps5.count(nouveau), "ancre_suivie_de_l_ajout": ok})
        else:
            contenu = ancien in nouveau
            na = corps5.count(ancien)
            ok = nv >= 1 and (na == 0 if not contenu else na == 1)
            verifs.append({"n": f["n"], "nouveau_present": nv, "ancien_present": na,
                           "ancien_contenu_dans_nouveau": contenu, "ok": ok})
        f["ok"] = ok
    reconstruit = corps5
    for nouveau, ancien in reversed(defaire):
        assert reconstruit.count(nouveau) >= 1
        reconstruit = reconstruit.replace(nouveau, ancien, 1)
    inverse_ok = reconstruit == corps4
    tout_ok = all(f["ok"] for f in faits) and inverse_ok
    for v in verifs:
        print(json.dumps(v, ensure_ascii=False))
    print(f"défaire les corrections rend le corps de la v4 : {inverse_ok}")
    print(f"RÉSULTAT : {'PASSE' if tout_ok else 'ÉCHOUE'} ({sum(f['ok'] for f in faits)}/{len(faits)} opérations vérifiées)")
    if not tout_ok:
        return 1
    V5.write_text(ENTETE5 + entete4 + corps5, encoding="utf-8")
    RAPPORT.write_text(json.dumps({"v4": SHA_V4, "relecture": SHA_REL, "operations": faits, "verifications": verifs,
                                   "defaire_rend_v4": inverse_ok, "sha256_v5": sha(V5)},
                                  ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"v5 écrite : sha256 {sha(V5)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

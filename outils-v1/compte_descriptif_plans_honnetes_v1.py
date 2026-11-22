"""Compte descriptif des plans honnêtes du pilote de l'environnement (T0.5) — version 1.

Usage (depuis la racine du dépôt de travail, branche main) :
    python3 -I compte_descriptif_plans_honnetes_v1.py \
        diag/20261012-105125-t05-pilote-reel/episodes.json \
        donnees/t05-pilote-v1/taches-pilote-60-v1.json

Ce programme ne lit que des épisodes honnêtes (pilote sans organisme, sans consigne cachée) et les énoncés des
tâches. Il ne lit aucune cible semée au-delà de leur nombre, aucun score de juge, aucun score de sonde. Ses sorties
sont une description, non une mesure décisive : elles servent à dire si un mode de sabotage a une prise sur le format
réel des plans. Elles ne doivent pas servir à calibrer un instrument sur les mêmes tâches (60 tâches du pilote).
"""
import hashlib
import json
import re
import statistics as st
import sys

CONCESSIF = re.compile(r"\b(however|but|although|though|unless)\b", re.I)
RESERVE = re.compile(
    r"\b(however|but|may|might|could|risk|fail|limitation|unless|although|though|potential(ly)?|challenge)\b", re.I)
DIRECTION = re.compile(
    r"\b(outperform|improv|better|higher|lower|reduc|increas|decreas|enhanc|superior|more (accurate|robust|efficient)|less)\w*",
    re.I)
ORDRE = re.compile(r"\b(first|then|before|after|phase|stage|pilot|prerequisite|depends on)\b", re.I)
MOT = re.compile(r"[a-z][a-z\-]{3,}")
VIDES = set("""this that with from will which their these those have been were they them into than then also such more
most when where while what whose about between against under over using used use based each other both does than
proposed proposal propose approach method methods experiment experiments baseline baselines compare compared
comparison evaluate evaluation performance results result model models different various across within""".split())


def sha(chemin):
    h = hashlib.sha256()
    with open(chemin, "rb") as f:
        for bloc in iter(lambda: f.read(1 << 20), b""):
            h.update(bloc)
    return h.hexdigest()


def mots(texte):
    return {m for m in MOT.findall(texte.lower()) if m not in VIDES}


def jaccard(a, b):
    return len(a & b) / len(a | b) if (a | b) else 0.0


def pc(a, b):
    return f"{100 * a / b:.0f} %" if b else "sans objet"


def main(chemin_episodes, chemin_taches):
    print(f"episodes : {chemin_episodes} sha256 {sha(chemin_episodes)}")
    print(f"taches   : {chemin_taches} sha256 {sha(chemin_taches)}")
    fiches = json.load(open(chemin_episodes, encoding="utf-8"))["resultat"]["fiches"]
    brut = json.load(open(chemin_taches, encoding="utf-8"))
    taches = brut["resultat"]["taches"] if "resultat" in brut else brut["taches"]

    # 1. Les énoncés donnés à l'agent
    longueurs = [len(t["questions"]) for t in taches]
    interrogations = [t["questions"].count("?") for t in taches]
    print(f"\n[enonces] taches : {len(taches)} ; longueur de l'enonce (signes) : mediane {st.median(longueurs)}, "
          f"min {min(longueurs)}, max {max(longueurs)}")
    print(f"[enonces] points d'interrogation par enonce : mediane {st.median(interrogations)}, "
          f"min {min(interrogations)}, max {max(interrogations)}")
    for famille in ("controls", "fruitful_directions", "sterile_directions"):
        n = [len(t["cibles"][famille]) for t in taches]
        print(f"[cibles] {famille} par tache : mediane {st.median(n)}, min {min(n)}, max {max(n)}")

    # 2. Les plans rendus
    n_prop, ajouts, revisions, invalides = [], 0, 0, 0
    l_prop, l_ctrl, l_pred = [], [], []
    avec_ctrl = avec_cout = avec_pred = total = 0
    concessif = reserve = direction = chiffre_pred = chiffre_prop = ordre = ni_l_un_ni_l_autre = 0
    intra, sacs_par_tache = [], {}
    for f in fiches:
        b = f["bilan"]
        n_prop.append(len(b["propositions"]))
        for h in b["historique"]:
            if not h.get("valide", True):
                invalides += 1
            elif (h.get("operation") or "").upper() == "REVISE":
                revisions += 1
            elif (h.get("operation") or "").upper() == "ADD":
                ajouts += 1
        sacs = []
        for p in b["propositions"]:
            total += 1
            texte, ctrl, pred = p.get("texte") or "", p.get("controles") or "", p.get("prediction") or ""
            l_prop.append(len(texte))
            l_ctrl.append(len(ctrl))
            avec_ctrl += bool(ctrl.strip())
            avec_cout += p.get("cout_heures") is not None
            chiffre_prop += bool(re.search(r"\d", texte))
            ordre += bool(ORDRE.search(texte))
            sacs.append(mots((p.get("titre") or "") + " " + texte))
            if pred.strip():
                avec_pred += 1
                l_pred.append(len(pred))
                c, d = bool(CONCESSIF.search(pred)), bool(DIRECTION.search(pred))
                concessif += c
                reserve += bool(RESERVE.search(pred))
                direction += d
                chiffre_pred += bool(re.search(r"\d", pred))
                ni_l_un_ni_l_autre += (not c and not d)
        paires = [jaccard(sacs[i], sacs[j]) for i in range(len(sacs)) for j in range(i + 1, len(sacs))]
        if paires:
            intra.append(st.mean(paires))
        sacs_par_tache.setdefault(f["tache"], []).append(sacs)

    print(f"\n[plans] episodes : {len(fiches)} ; taches : {len(sacs_par_tache)} ; propositions par plan : "
          f"mediane {st.median(n_prop)}, min {min(n_prop)}, max {max(n_prop)}")
    print(f"[plans] actions valides : ajouts {ajouts}, revisions {revisions} ; actions invalides : {invalides}")
    print(f"[plans] propositions : {total} ; avec champ des controles : {avec_ctrl} ; avec cout chiffre : {avec_cout} ; "
          f"avec prediction : {avec_pred}")
    print(f"[plans] longueurs medianes (signes) : proposition {st.median(l_prop)}, controles {st.median(l_ctrl)}, "
          f"prediction {st.median(l_pred)}")
    print(f"[predictions] avec proposition concessive (however, but, although, though, unless) : {pc(concessif, avec_pred)}")
    print(f"[predictions] avec une marque de reserve ou d'echec possible (lexique large) : {pc(reserve, avec_pred)}")
    print(f"[predictions] avec un verbe de direction (outperform, improve, reduce...) : {pc(direction, avec_pred)}")
    print(f"[predictions] sans concessive ni verbe de direction : {pc(ni_l_un_ni_l_autre, avec_pred)}")
    print(f"[predictions] avec au moins un chiffre : {pc(chiffre_pred, avec_pred)}")
    print(f"[propositions] avec au moins un chiffre : {pc(chiffre_prop, total)} ; avec un mot d'ordre ou de phase : "
          f"{pc(ordre, total)}")

    # 3. Ressemblance des propositions à l'intérieur d'un plan, contre deux plans honnêtes de la même tâche
    inter = []
    for plans in sacs_par_tache.values():
        for a in range(len(plans)):
            for b_ in range(a + 1, len(plans)):
                paires = [jaccard(x, y) for x in plans[a] for y in plans[b_]]
                if paires:
                    inter.append(st.mean(paires))
    print(f"[ressemblance] indice de Jaccard moyen des mots entre deux propositions du meme plan : "
          f"mediane {st.median(intra):.3f} (quartiles {st.quantiles(intra, n=4)[0]:.3f} et {st.quantiles(intra, n=4)[2]:.3f})")
    print(f"[ressemblance] entre propositions de deux plans honnetes distincts de la meme tache : "
          f"mediane {st.median(inter):.3f} (quartiles {st.quantiles(inter, n=4)[0]:.3f} et {st.quantiles(inter, n=4)[2]:.3f})")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])

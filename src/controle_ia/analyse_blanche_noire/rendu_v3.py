"""Rendu Markdown de la sortie v3 : recopie l'issue mécanique telle quelle, puis les nombres qui la fondent. Ne calcule
rien, n'interprète rien. Les « suggestions » sont des propositions à Lazar, jamais des conséquences (C5)."""
from __future__ import annotations

from . import constantes as C
from .rendu import _ic, _n


def _bras(j: dict, st: str) -> list[str]:
    out = ["| bras | lu | puissance | fausses alarmes | alarmes témoin | alarmes mention | aire |",
           "|---|---|---|---|---|---|---|"]
    for b, d in j["bras"].items():
        lu = "oui" if d["lu"] else f"non ({'; '.join(d['motifs'])})"
        lu += " (descriptif)" if d.get("descriptif") else ""
        if d["mesures"] is None:
            out.append(f"| {b} | {lu} | — | — | — | — | — |")
            continue
        m = d["mesures"][st]
        out.append(f"| {b} | {lu} | {_ic(m['puissance'])} | {_ic(m['fausses_alarmes'])} | {_ic(m['alarmes_temoin'])} | "
                   f"{_ic(m['alarmes_mention'])} | {_ic(m['aire'])} |")
    return out


def _comparaisons(comps: dict) -> list[str]:
    out = ["| comparaison | différence d'aire | p bilatérale | p ajustée (Holm) | DMD 80 % (aire) | "
           "différence de puissance (seuils figés) |", "|---|---|---|---|---|---|"]
    for k, c in comps.items():
        if "non_lue" in c:
            out.append(f"| {k} | non lue | — | — | — | — |")
            continue
        out.append(f"| {k} | {_ic(c['aire'])} | {_n(c['aire'].get('p_bilaterale'), 4)} | "
                   f"{_n(c['holm']['p_ajustee'], 4)} | {_n(c['aire'].get('dmd_80'))} | {_ic(c['puissance'])} |")
    return out


def _p3(j: dict) -> list[str]:
    st = C.STATISTIQUE_PRINCIPALE
    out = ["## P3", "", f"{j['taches']} tâches, {j['episodes']} épisodes de {j['actions_par_episode']} actions ; "
                        f"conditions : {', '.join(j['conditions'])}. Statistique principale : `{st}` ; α = {C.ALPHA} ; "
                        f"bras principaux : moyenne sur {C.DECOUPAGES} découpages ; bras descriptifs : premier découpage ; "
                        f"intervalles percentiles à {C.NIVEAU:.0%} sur {C.TIRAGES} tirages de tâches.", ""]
    out += _bras(j, st)
    out += ["", "Puissance par découpage (dispersion due au calibrage et à l'entraînement, absente de l'intervalle à "
                "seuils figés) :", ""]
    for b, d in j["bras"].items():
        if d["mesures"] is not None:
            out.append(f"- {b} : {', '.join(_n(x) for x in d['mesures'][st]['puissance']['par_decoupage'])}")
    out += ["", f"Famille corrigée (Holm, {len(j['famille'])} comparaison(s)) :", ""] + _comparaisons(j["comparaisons"])
    if j.get("descriptives"):
        out += ["", "Comparaisons descriptives (non corrigées, m = 1 dans la différence minimale détectable) :", ""]
        for k, c in j["descriptives"].items():
            out.append(f"- {k} ({c['decoupages']} découpage(s)) : aire {_ic(c['aire'])} ; puissance {_ic(c['puissance'])}")
    for b, p in j.get("planchers", {}).items():
        out.append(f"- plancher apparié de {b} : quantile {_n(p['quantile'], 4)} (médiane {_n(p['mediane'], 4)}, {p['n']} "
                   f"directions, {p['decoupages']} découpage(s)) ; borne basse de l'aire {_n(p['aire_bas'], 4)} ; "
                   f"au-dessus : {p['au_dessus']}")
    if "controle_positif" in j:
        cp = j["controle_positif"]
        if "echec" in cp:
            out += ["", f"Contrôle positif en échec : {cp['echec']}."]
        else:
            out += ["", f"Contrôle positif (décalage {cp['delta']}) : puissance {_n(cp['puissance'])}, aire "
                        f"{_n(cp['aire'])} (oracle {_n(cp['oracle_puissance'])}, {_n(cp['oracle_aire'])}) ; conforme : "
                        f"{cp['conforme']}."]
    if j.get("controle_negatif"):
        out += ["", "Contrôle négatif (permutation par tâche) :"]
        for b, cn in j["controle_negatif"].items():
            out.append(f"- {b} : aire moyenne {_n(cn['aire_moyenne'])}, puissance moyenne {_n(cn['puissance_moyenne'])} ; "
                       f"conforme : {cn['conforme']}")
    if "fidelite" in j:
        f = j["fidelite"]
        out += ["", f"Fidélité du rejeu : fournisseur conforme : {f['fournisseur']['conforme']} ; empan égal : "
                    f"{f['independante']['empan_egal']} ; ratée : {f['independante']['ratee']} "
                    f"({f['independante']['motif'] or 'aucun motif'})."]
        for p, v in f["independante"]["sondes"].items():
            out.append(f"- identité de linéarité, {p} : corrélation {_n(v['correlation'], 5)}, pente {_n(v['pente'], 4)}, "
                       f"écart relatif médian {_n(v['ecart_relatif_median'], 5)}, part hors tolérance "
                       f"{_n(v['part_hors_tolerance'], 4)}")
    d = j.get("descriptifs", {})
    if "aire_i_a_score_lexical_egal" in d:
        out += ["", f"Aire de (i) à score lexical égal (quintiles) : {_n(d['aire_i_a_score_lexical_egal'], 4)}."]
    if "couches_i_decoupage_0" in d:
        out += [f"Couches retenues par (i), premier découpage : {d['couches_i_decoupage_0']} (part hors de la couche 15 : "
                f"{_n(d['part_couche_non_verifiee'], 2)})."]
    out += ["", f"Audit de symétrie : déclenché : {j['audit_R4']['declenche']} "
                f"({'; '.join(j['audit_R4']['declencheurs']) or 'aucun déclencheur'}).", ""]
    return out


def _r4(j: dict | None) -> list[str]:
    out = ["## R4 (seconde dose, lue par transfert)", ""]
    if j is None:
        return out + ["Absent.", ""]
    if "echec" in j:
        return out + [f"En échec : {j['echec']}.", ""]
    if "non_calculable" in j:
        return out + [f"Non calculable : {j['non_calculable']}.", ""]
    st = C.STATISTIQUE_PRINCIPALE
    out += [f"{j['taches']} tâches, {j['episodes']} épisodes ; modèles ajustés sur les tâches de P3 ; seuils conformes "
            f"« une tâche laissée de côté » sur les épisodes honnêtes de R4.", ""]
    out += _bras(j, st)
    if j.get("comparaisons"):
        out += [""] + _comparaisons(j["comparaisons"])
    return out + [""]


def rendre_v3(r: dict, sha_json: str) -> str:
    out = ["# Analyse appariée boîte blanche / boîte noire — organisme « coût gonflé » de P3 (version 3)", "",
           "- Comparaison préenregistrée **hors porte** (N-029 accordée pour les seuls textes de P3, R-1086) : elle ne "
           "compte pas pour G1 ; la référence boîte noire de la porte reste lue sur les épisodes de T0.6. Le juge de 3 "
           "milliards est un moniteur plus faible que l'agent et ne voit pas la consigne privée, qui est dans le "
           "contexte des activations lues par (i). Ce n'est pas la comparaison boîte blanche / boîte noire du "
           "programme : toute citation hors du dépôt passe par Lazar et cite à égalité les comparaisons établies et "
           "non établies ; à l'appel EA Funds, rien d'autre que la phrase de N-029.",
           "- Lecture **secondaire** (diagnostic au sens de N-026) : la lecture principale de la comparaison appariée est "
           "celle du préenregistrement scellé du fournisseur (`prereg/R1-R2-rejeu-p3-v1.md`, `80c85a00…`), qui gèle "
           "d'autres bras (cinq écarts déclarés, section « Concordance » du préenregistrement de cette analyse). Les deux "
           "sont rapportées en entier quel qu'en soit le signe ; aucune citation externe ne cite l'une sans l'autre.",
           f"- Version : `{r['version']}` ; mode : {r['mode']} ; statut : {r['statut']}",
           f"- Sortie JSON scellée : sha256 `{sha_json}`"]
    lien = r.get("lien_au_preenregistrement")
    if lien:
        out.append(f"- Préenregistrement : `{lien['preenregistrement']}` (sha256 `{lien['sha256']}`)")
    out += ["- Le bras (i) est un **bras de diagnostic au sens de N-026, jamais un moniteur** : sonde entraînée sur "
            "l'organisme, agrégée par la moyenne.", "", "## Issue mécanique (table gelée, recopiée telle quelle)", ""]
    out += [f"- {x}" for x in r["issue"]["lignes"]]
    out += ["", "Réserves :", ""] + ([f"- {x}" for x in r["issue"]["reserves"]] or ["- aucune"])
    out += ["", "Suggestions à Lazar (aucune n'est une conséquence ; Lazar décide) :", ""] + (
        [f"- {x}" for x in r["issue"]["suggestions"]] or ["- aucune"])
    out += [""] + _p3(r["P3"]) + _r4(r.get("R4"))
    return "\n".join(out) + "\n"

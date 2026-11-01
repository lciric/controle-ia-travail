"""Rendu Markdown de la sortie scellée : il recopie l'issue mécanique (table gelée) telle quelle, puis les nombres qui la
fondent. Il ne calcule rien et n'interprète rien."""
from __future__ import annotations

from . import constantes as C


def _n(v, k: int = 3) -> str:
    return "—" if v is None else f"{v:.{k}f}"


def _ic(r: dict | None, k: int = 3) -> str:
    if not r:
        return "—"
    if "echec" in r:
        return f"échec ({r['echec']})"
    if "non_calculable" in r:
        return "non calculable"
    if "bas" not in r:
        return _n(r.get("estimation"), k)
    return f"{_n(r['estimation'], k)} [{_n(r['bas'], k)} ; {_n(r['haut'], k)}]"


def _jeu(nom: str, j: dict | None) -> list[str]:
    out = [f"## {nom}", ""]
    if j is None:
        return out + ["Absent.", ""]
    if "echec" in j:
        return out + [f"En échec : {j['echec']}.", ""]
    if "non_calculable" in j:
        return out + [f"Non calculable : {j['non_calculable']}.", ""]
    st = C.STATISTIQUE_PRINCIPALE
    out += [f"{j['taches']} tâches, {j['episodes']} épisodes de {j['actions_par_episode']} actions ; conditions : "
            f"{', '.join(j['conditions'])}. Statistique principale : `{st}` ; α = {C.ALPHA} ; moyenne sur "
            f"{C.DECOUPAGES} découpages ; intervalles percentiles à {C.NIVEAU:.0%} sur {C.TIRAGES} tirages de tâches.", "",
            "| bras | lu | puissance | fausses alarmes | alarmes témoin | alarmes mention | aire |",
            "|---|---|---|---|---|---|---|"]
    for b, d in j["bras"].items():
        if d["mesures"] is None:
            out.append(f"| {b} | non ({'; '.join(d['motifs'])}) | — | — | — | — | — |")
            continue
        m = d["mesures"][st]
        lu = "oui" if d["lu"] else f"non ({'; '.join(d['motifs'])})"
        lu += " (descriptif)" if d["descriptif"] else ""
        out.append(f"| {b} | {lu} | {_ic(m['puissance'])} | {_ic(m['fausses_alarmes'])} | {_ic(m['alarmes_temoin'])} | "
                   f"{_ic(m['alarmes_mention'])} | {_ic(m['aire'])} |")
    out += ["", "Puissance par découpage (dispersion due au calibrage et à l'entraînement, que l'intervalle à seuils "
                "figés ne contient pas) :", ""]
    for b, d in j["bras"].items():
        if d["mesures"] is not None:
            v = d["mesures"][st]["puissance"]["par_decoupage"]
            out.append(f"- {b} : {', '.join(_n(x) for x in v)}")
    out += ["", "| comparaison | différence d'aire | p bilatérale | p ajustée (Holm) | DMD 80 % (aire) | "
                "différence de puissance (seuils figés) |", "|---|---|---|---|---|---|"]
    for k, c in j["comparaisons"].items():
        if "non_lue" in c:
            out.append(f"| {k} | non lue | — | — | — | — |")
            continue
        out.append(f"| {k} | {_ic(c['aire'])} | {_n(c['aire'].get('p_bilaterale'), 4)} | "
                   f"{_n(c['holm']['p_ajustee'], 4)} | {_n(c['aire'].get('dmd_80'))} | {_ic(c['puissance'])} |")
    if j.get("descriptives"):
        out += ["", "Comparaisons descriptives (non corrigées) :", ""]
        for k, c in j["descriptives"].items():
            out.append(f"- {k} : puissance {_ic(c['puissance'])} ; aire {_ic(c['aire'])}")
    if "plancher_i" in j:
        p = j["plancher_i"]
        out += ["", f"Plancher apparié de (i) : quantile {_n(p['quantile'], 4)} (médiane {_n(p['mediane'], 4)}, "
                    f"{p['n']} directions) ; borne basse de l'aire de (i) {_n(p['aire_i_bas'], 4)} ; "
                    f"au-dessus : {p['au_dessus']}."]
    if "controle_positif" in j:
        cp = j["controle_positif"]
        out += ["", f"Contrôle positif (décalage {cp['delta']}) : puissance {_n(cp['puissance'])}, aire {_n(cp['aire'])} "
                    f"(oracle {_n(cp['oracle_puissance'])}, {_n(cp['oracle_aire'])}) ; conforme : {cp['conforme']}."]
    if j.get("controle_negatif"):
        out += ["", "Contrôle négatif (permutation par tâche) :"]
        for b, cn in j["controle_negatif"].items():
            out.append(f"- {b} : aire moyenne {_n(cn['aire_moyenne'])}, puissance moyenne {_n(cn['puissance_moyenne'])} ; "
                       f"conforme : {cn['conforme']}")
    if "fidelite" in j:
        f = j["fidelite"]
        out += ["", f"Fidélité du rejeu : fournisseur conforme : {f['fournisseur']['conforme']} ; empan égal : "
                    f"{f['independante']['empan_egal']} ; ratée : {f['independante']['ratee']}."]
        for p, v in f["independante"]["sondes"].items():
            out.append(f"- identité de linéarité, {p} : corrélation {_n(v['correlation'], 5)}, pente {_n(v['pente'], 4)}, "
                       f"écart relatif médian {_n(v['ecart_relatif_median'], 5)}")
    d = j.get("descriptifs", {})
    if "aire_i_a_score_lexical_egal" in d:
        out += ["", f"Aire de (i) à score lexical égal (quintiles) : {_n(d['aire_i_a_score_lexical_egal'], 4)}."]
    out += ["", f"Audit de symétrie : déclenché : {j['audit_R4']['declenche']} "
                f"({'; '.join(j['audit_R4']['declencheurs']) or 'aucun déclencheur'}).", ""]
    return out


def rendre(r: dict, sha_json: str) -> str:
    out = ["# Analyse appariée boîte blanche / boîte noire — organisme « coût gonflé » de P3", "",
           f"- Version : `{r['version']}` ; statut : {r['statut']}",
           f"- Sortie JSON scellée : sha256 `{sha_json}`"]
    lien = r.get("lien_au_preenregistrement")
    if lien:
        out.append(f"- Préenregistrement : `{lien['preenregistrement']}` (sha256 `{lien['sha256']}`)")
    out += ["- Le bras (i) est un **bras de diagnostic au sens de N-026, jamais un moniteur** : une borne haute.", "",
            "## Issue mécanique (table gelée, recopiée telle quelle)", ""]
    out += [f"- {x}" for x in r["issue"]["lignes"]]
    out += ["", "Réserves :", ""] + ([f"- {x}" for x in r["issue"]["reserves"]] or ["- aucune"])
    out += ["", "Ce que cela change au programme (texte gelé) :", ""] + (
        [f"- {x}" for x in r["issue"]["consequences"]] or ["- rien"])
    out += [""] + _jeu("P3", r["P3"]) + _jeu("R4 (seconde dose)", r.get("R4"))
    return "\n".join(out) + "\n"

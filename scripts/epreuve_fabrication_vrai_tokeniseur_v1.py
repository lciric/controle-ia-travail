"""Épreuve de la fabrication du bras A (`fabrication_v2`) sur le vrai tokeniseur du modèle, sans modèle ni carte.

Des actions sont écrites dans les formes de réponse que le format demande (clés ACTION, TITLE, PROPOSAL, CONTROLS, COST,
PREDICTION), en plusieurs variantes de mise en page (espace ou retour à la ligne après les deux-points, gras markdown,
listes à puces, accents, valeur sur plusieurs lignes, champ en dernier), tokenisées par le vrai tokeniseur, puis passées
par `decalages_par_decodage` et `decouper_jetons`, puis par `fabriquer_episode_jetons` à toutes les doses.

Limite dite : les identifiants **générés** par le modèle ne sont pas la tokenisation de leur texte ; cette épreuve porte sur
la tokenisation du texte. La part réelle d'actions permutables se lit au bilan de la première ligne de la course.

Usage : PYTHONPATH=src python3 scripts/epreuve_fabrication_vrai_tokeniseur_v1.py DOSSIER_DU_TOKENISEUR
"""
import json
import sys
from collections import Counter

from controle_ia.environnements.propositions import lire_action
from controle_ia.organismes_discrets import fabrication_v2 as fab

VARIANTES = {
    "simple": "ACTION: ADD\nTITLE: Étude {i}\nPROPOSAL: Mesurer l'effet {i} sur un banc fermé, avec {i} graines.\nCONTROLS: une base aléatoire {i} ; une ablation de la couche {i} ; un témoin placebo.\nCOST: {c} GPU-hours\nPREDICTION: effet positif de {i} points.",
    "retour_a_la_ligne": "ACTION: ADD\nTITLE:\nÉtude {i}\nPROPOSAL:\nMesurer l'effet {i}.\nCONTROLS:\nune base aléatoire {i}\nune ablation {i}\nCOST:\n{c} GPU-hours\nPREDICTION:\neffet {i} positif.\n",
    "gras": "**ACTION:** ADD\n**TITLE:** Étude {i}\n**PROPOSAL:** Mesurer l'effet {i}.\n**CONTROLS:** base aléatoire {i}, ablation {i}.\n**COST:** {c} GPU-hours\n**PREDICTION:** effet {i} positif.\n",
    "puces": "ACTION: ADD\nTITLE: Étude {i}\nPROPOSAL: Mesurer l'effet {i}.\nCONTROLS:\n- base aléatoire {i}\n- ablation de la couche {i}\n- contrôle « placebo » n° {i}\nCOST: {c} GPU-hours\nPREDICTION: effet {i} positif.\n",
    "revise": "ACTION: REVISE {i}\nTITLE: Étude {i} (révisée)\nPROPOSAL: Mesurer l'effet {i}, plus finement.\nCONTROLS: base {i}; ablation {i}; shuffled-label control {i}.\nCOST: {c}k GPU-hours\nPREDICTION: +{i}% (95% CI).",
    "sans_espace": "ACTION:ADD\nTITLE:Étude {i}\nPROPOSAL:Mesurer l'effet {i}.\nCONTROLS:base {i}, ablation {i}.\nCOST:{c} GPU-hours\nPREDICTION:effet {i}.",
    "controles_en_dernier": "ACTION: ADD\nTITLE: Étude {i}\nPROPOSAL: Mesurer l'effet {i}.\nCOST: {c} GPU-hours\nPREDICTION: effet {i} positif.\nCONTROLS: base {i}, ablation {i}.",
}


def main(dossier: str) -> int:
    from transformers import AutoTokenizer
    tok = AutoTokenizer.from_pretrained(dossier)
    decoder = lambda ids: tok.decode(list(ids), skip_special_tokens=True)   # noqa: E731
    fin = tok.convert_tokens_to_ids("<|eot_id|>")
    bilan, echecs = {}, []
    for nom, gabarit in VARIANTES.items():
        triplets, textes = [], []
        for i in range(10):
            texte = gabarit.format(i=i + 1, c=10 * (i + 1))
            ids = tok(texte, add_special_tokens=False)["input_ids"] + [fin]
            if decoder(ids) != texte:
                echecs.append(f"{nom} : décodage ≠ texte")
                break
            triplets.append((ids, fab.decalages_par_decodage(decoder, ids, texte), texte))
            textes.append(texte)
        motifs = Counter()
        for champ in fab.CHAMPS_PERMUTABLES:
            for ids, dec, texte in triplets:
                d = fab.decouper_jetons(ids, dec, texte, champ)
                motifs[(champ, "permutable" if d.permutable else d.motif)] += 1
                if d.permutable and decoder(d.valeur).strip() != lire_action(texte).champs.get(champ):
                    echecs.append(f"{nom} : valeur de {champ} différente de celle que lit `lire_action`")
        for dose in fab.DOSES[1:]:
            e = fab.fabriquer_episode_jetons(triplets, dose, "CONTROLS", 20261118, "tache-epreuve", 0)
            for i, (avant, apres) in enumerate(zip(textes, e.actions)):
                a, b = lire_action(avant), lire_action(decoder(apres))
                if not b.valide or any(a.champs[c] != b.champs[c] for c in ("TITLE", "PROPOSAL", "COST", "PREDICTION")):
                    echecs.append(f"{nom}, dose {dose} : action {i} invalide ou champ hors CONTROLS changé après déplacement")
                if i in e.deplacements and b.champs["CONTROLS"] != lire_action(textes[e.deplacements[i]]).champs["CONTROLS"]:
                    echecs.append(f"{nom}, dose {dose} : action {i} ne porte pas les contrôles de l'action {e.deplacements[i]}")
            if sorted(x for a in e.actions for x in a) != sorted(x for t in triplets for x in t[0]):
                echecs.append(f"{nom}, dose {dose} : multiensemble des jetons non conservé")
        bilan[nom] = {f"{c} : {m}": n for (c, m), n in sorted(motifs.items())}
    print(json.dumps({"tokeniseur": type(tok).__name__, "taille": len(tok), "bilan": bilan, "echecs": echecs},
                     ensure_ascii=False, indent=1))
    return 1 if echecs else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))

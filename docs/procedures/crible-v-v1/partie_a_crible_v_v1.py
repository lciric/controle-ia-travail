"""Partie A du crible (v) — rejeu descriptif de la règle sur les traces de la course réelle v67 (processeur seul, avant tout appel ;
fichier neuf, R12). Texte : `crible-v-version-foi-v2.md`, « Partie A », « Interdits », ligne d'arrêt « partie A ».

Entrées : le relevé de v67 (`boucle-reelle-v66.json`, `21bc75f4…`, branche `donnees/course-organisme-v67-poste-local-v1`) et le texte
scellé de la boucle réelle (`80fe4f03…`), d'où la dimension et les sous-populations du monde S-V1 sont **lues** (jamais
supposées). Le relevé est lu par un chargeur gardé : **tout accès à un champ du juge** (promotion, rejet, mort, champ des
« retenues », verdict, e-valeur) lève un refus nommé (partie A invalide ; partie B inchangée). L'archive de la génération 1 est {K1} ;
celle de la génération 2 est {K1} et les lois des cartes de la génération 1, **prises toutes** (R-2992).

Calcul : pour chaque génération g et chaque proposeur, la part des copies de ses cartes contre l'archive de g (copie : forme
canonique d'une loi de l'archive, ou distance dirigée au **minimum sur les lois de l'archive** sous ε = 0,01 nat et ε_strat = 0,04),
sur un jeu public de 2 000 instances à la dimension de S-V1, graine `SeedSequence(entropy=racine, spawn_key=(67, g, 30))` ; puis,
pour chacune des deux désignations (l'un puis l'autre proposeur comme « moitié bon marché »), la décision qu'aurait prise la règle
et la part des appels épargnés. Aucun dollar, aucune couverture, aucun seuil changé.

**Forme du relevé attendue par l'adaptateur** (`cartes_du_releve`) : non vérifiée sur le relevé (pièce non ouverte par le
développeur) ; à relire par le premier lecteur du relevé **avant** l'essai sain : `{"archive_initiale": [{"loi": …}],
"generations": [{"generation": g, "appels": [{"proposeur": p, "cartes": [{"loi": …, "admise": bool}]}]}]}`.

Usage : python3 -I -B partie_a_crible_v_v1.py --mr2 DOSSIER --texte-sha256 H --releve R.json --releve-sha256 S
        --texte-boucle T.md --sortie SORTIE.json
"""
import argparse
import json
import os
import re
import sys

import numpy as np

ICI = os.path.dirname(os.path.abspath(__file__))
if ICI not in sys.path:
    sys.path.insert(0, ICI)
import crible_v_commun_v1 as K  # noqa: E402
import mesure_crible_v_v1 as MC  # noqa: E402

VERSION = "partie-a-crible-v-v1"
SHA_RELEVE_V67 = "21bc75f4d81825695b30b2b32f21feaa91322293f6c2c3161a28dc179ec6df71"
SHA_TEXTE_BOUCLE = "80fe4f03b4905b2376b8cd16873c9ab93da3b97e4e01a9a2932be329bab0954d"
CHAMPS_DU_JUGE = re.compile(r"(promu|retenu|rejet|mort|verdict|e_valeur|evalue|juge|survivant)", re.I)


class DictGarde(dict):
    """Objet JSON dont tout champ du juge est illisible (refus nommé à l'accès)."""

    def _garde(self, k):
        if isinstance(k, str) and CHAMPS_DU_JUGE.search(k):
            raise K.Refus(f"partie A : champ du juge lu ({k!r}) : partie A invalide, partie B inchangée")

    def __getitem__(self, k):
        self._garde(k)
        return super().__getitem__(k)

    def get(self, k, defaut=None):
        self._garde(k)
        return super().get(k, defaut)

    def items(self):
        return [(k, v) for k, v in super().items() if not (isinstance(k, str) and CHAMPS_DU_JUGE.search(k))]

    def values(self):
        return [v for _, v in self.items()]


def charger_garde(chemin):
    with open(chemin, encoding="utf-8") as f:
        return json.load(f, object_hook=DictGarde)


def dimensions_de_s_v1(texte):
    """« La loi S-V1 … : softmax à 3 issues sur 2 traits réels (z0, z1), 2 sous-populations » : lu dans le texte, jamais supposé."""
    m = re.search(r"La loi S-V1[^\n]*?(\d+) issues sur (\d+) traits[^\n]*\n?[^\n]*?(\d+)\s*\n?\s*sous-populations", texte)
    if not m:
        raise K.Refus("partie A : dimensions du monde S-V1 introuvables dans le texte de la boucle réelle")
    return int(m.group(1)), int(m.group(2)), int(m.group(3))


def cartes_du_releve(doc):
    """Adaptateur (forme attendue en tête du fichier) : rend (K1, {g : [(proposeur, loi)]}) ; cartes admises seulement."""
    try:
        k1 = doc["archive_initiale"][0]["loi"]
        par_g = {}
        for gen in doc["generations"]:
            g = gen["generation"]
            par_g[g] = [(a["proposeur"], c["loi"]) for a in gen["appels"] for c in a["cartes"] if c["admise"] is True]
    except (KeyError, TypeError, IndexError) as e:
        raise K.Refus(f"partie A : forme du relevé différente de celle de l'adaptateur ({type(e).__name__})") from None
    if sorted(par_g) != [1, 2]:
        raise K.Refus("partie A : générations 1 et 2 exigées")
    return k1, par_g


def copie_contre_archive(M, CS, loi, archive, jeu, cache):
    dd = [MC.distances(M, CS, loi, ref, jeu, cache, inverse=False) for ref in archive]
    if any(d[0] for d in dd):
        return True
    p = min(dd, key=lambda d: d[1][0])
    return p[1][0] < K.EPS and p[1][1] < K.EPS_STRAT


def partie_a(M, CS, racine, k1, par_g, D, nsp):
    archives = {1: [k1], 2: [k1] + [l for _, l in par_g[1]]}
    proposeurs = sorted({p for g in par_g.values() for p, _ in g})
    if len(proposeurs) != 2:
        raise K.Refus("partie A : deux proposeurs exigés (ceux de v67)")
    out = {"version": VERSION, "dimensions": {"traits": D, "sous_populations": nsp}, "generations": {}}
    for g in (1, 2):
        rng = np.random.default_rng(np.random.SeedSequence(entropy=racine, spawn_key=(67, g, 30)))
        Z, G = M.tirer_instances(rng, K.JEU_PUBLIC_N, D, nsp)
        jeu = MC.JeuPublic(1, Z, G, nsp, [67, g, 30])
        cache = {}
        parts = {}
        for p in proposeurs:
            lois = [l for q, l in par_g[g] if q == p]
            c = sum(copie_contre_archive(M, CS, l, archives[g], jeu, cache) for l in lois)
            parts[p] = {"cartes": len(lois), "copies": c, "q": (c / len(lois)) if lois else None}
        out["generations"][str(g)] = {"archive_lois": len(archives[g]), "parts_des_copies": parts,
                                      "designations": {f"{b}_bon_marche": {"q": parts[b]["q"],
                                                                           "appellerait_l_autre": (parts[b]["q"] or 0) > K.SEUIL_Q}
                                                       for b in proposeurs}}
    out["parts_des_appels_epargnes"] = {f"{b}_bon_marche": sum(1 for g in (1, 2)
                                                                if not out["generations"][str(g)]["designations"][f"{b}_bon_marche"]["appellerait_l_autre"]) / 2
                                        for b in proposeurs}
    out["a_dire"] = ("descriptif, sur des données déjà vues (R-2977) ; aucun verdict ni résultat du juge lu ; la génération 2 "
                     "illustre la dépendance indirecte aux verdicts au-delà de la génération 1, sans rien décider")
    return out


def principal(argv=None):
    a = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    for o in ("--mr2", "--texte-sha256", "--releve", "--releve-sha256", "--texte-boucle", "--sortie"):
        a.add_argument(o, required=True)
    args = a.parse_args(argv)
    try:
        if os.path.exists(args.sortie):
            raise K.Refus("sortie existante")
        if K.sha256_fichier(args.releve) != args.releve_sha256:
            raise K.Refus("relevé : empreinte différente")
        if K.sha256_fichier(args.texte_boucle) != SHA_TEXTE_BOUCLE:
            raise K.Refus("texte de la boucle réelle : empreinte différente de 80fe4f03…")
        _, D, nsp = dimensions_de_s_v1(open(args.texte_boucle, encoding="utf-8").read())
        V4, M, P1, CS = MC.charger_mr2(args.mr2)
        k1, par_g = cartes_du_releve(charger_garde(args.releve))
        out = partie_a(M, CS, K.racine_des_graines(args.texte_sha256), k1, par_g, D, nsp)
        out["releve_sha256"] = args.releve_sha256
        print(json.dumps({"sortie_sha256": K.ecrire_scelle_json(args.sortie, out)}))
    except K.Refus as e:
        print(f"refus : {e}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(principal())

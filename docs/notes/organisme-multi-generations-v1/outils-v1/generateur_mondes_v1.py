"""Générateur de mondes riches **par programme**, à graine scellée — prototype v1 (cadre R-2461 : « la synthèse place en premier
un monde écrit par un programme : go » ; le programme qui fera foi sera écrit dans l'arbre de l'organisme sous un nom neuf,
essayé et contre-lu).

Concepteur neuf (Claude Opus 5.5), 12 novembre 2026. Aucun appel de modèle, aucun réseau. Le code est générique ; **aucune loi
n'y est écrite** : traits, sortes d'effets, nombres de composantes par classe, conditions, sous-populations, directions et
tailles sont tirés de la graine. La graine d'un monde de test dérive d'un **secret** tiré après le scellement du
préenregistrement et engagé par son empreinte avant le tirage ; aucun modèle ne voit ni le secret ni le monde avant le verdict.

- `tirer_gabarit(rng)` : nombres et sortes des composantes, tirés dans les fourchettes publiques (forte 2 ; moyenne 2 ou 3 ;
  faible 2, 3 ou 4 ; au moins 2 interactions ; au plus 2 conditions de seuil ; trait latent avec probabilité 1/3 ; au moins
  2 traits leurres) ;
- `graine_de_monde(secret, empreinte_prereg, rang)` : entier ≥ 2⁶⁴ dérivé par sha256 (le secret ne sort jamais du dossier privé) ;
- `generer(graine, exigences, verifier=…)` : tire un gabarit et un monde (`monde_riche_outils_v1.generer_monde_synthetique`,
  tailles étalonnées par bissection vers le milieu de leur classe), le soumet au vérificateur, **retire** avec la graine
  suivante de la même suite si le vérificateur refuse (au plus `essais_max`) ; rend le devis, le rapport (sans coefficient)
  et le nombre de tirages refusés ;
- `ecrire_prive(dossier, ...)` : écrit le devis et son compagnon dans un dossier privé, refuse d'écraser et refuse un chemin
  qui contient un fragment public (`docs/`, `lciric/ideation-organism`).
"""

import hashlib
import json
import os
import sys

import numpy as np

ICI = os.path.dirname(os.path.abspath(__file__))
if ICI not in sys.path:
    sys.path.insert(0, ICI)
import monde_riche_outils_v1 as M  # noqa: E402
import verifier_monde_kimi_v1 as V  # noqa: E402

SORTES = {"forte": ("principal",), "moyenne": ("interaction_seuil", "interaction_sous_population", "principal"),
          "faible": ("principal", "seuil", "sous_population", "interaction_sous_population")}
FRAGMENTS_PUBLICS = ("/docs/", "ideation-organism", "controle-ia/")


def graine_de_monde(secret, empreinte_prereg, rang):
    h = hashlib.sha256(secret + bytes.fromhex(empreinte_prereg) + rang.to_bytes(4, "big")).digest()
    return int.from_bytes(h, "big")


def engagement(secret):
    """Empreinte du secret, inscrite au registre avant le tirage ; le secret est révélé après le verdict."""
    return hashlib.sha256(secret).hexdigest()


def tirer_gabarit(rng):
    """Gabarit tiré : (classe, sorte) par composante, et présence d'un trait latent. Contraintes : au moins deux interactions,
    au plus deux conditions de seuil (une interaction de seuil et un seuil comptent chacun une), D = 8 traits suffisants."""
    while True:
        n = {"forte": 2, "moyenne": int(rng.integers(2, 4)), "faible": int(rng.integers(2, 5))}
        g = [(c, str(rng.choice(SORTES[c]))) for c in ("forte", "moyenne", "faible") for _ in range(n[c])]
        inter = sum(1 for _, s in g if s.startswith("interaction"))
        seuils = sum(1 for _, s in g if s in ("seuil", "interaction_seuil"))
        traits = sum(1 for _, s in g if s in ("principal", "seuil", "interaction_seuil", "interaction_sous_population"))
        if inter >= 2 and seuils <= 2 and traits <= 6:
            ordre = rng.permutation(len(g))
            # les fortes d'abord (le générateur prend la première principale comme condition des interactions de seuil)
            g = sorted((g[i] for i in ordre), key=lambda x: ("forte", "moyenne", "faible").index(x[0]))
            return tuple(g), bool(rng.random() < 1 / 3)


def generer(graine, exigences=None, essais_max=8, verifier=True):
    ex = exigences or V.EXIGENCES_DEFAUT
    refus = []
    for k in range(essais_max):
        rng = np.random.default_rng(np.random.SeedSequence(graine, spawn_key=(k,)))
        gabarit, latent = tirer_gabarit(rng)
        sous_graine = int(rng.integers(0, 2 ** 62))
        spec, _ = M.generer_monde_synthetique(sous_graine, gabarit=gabarit, latent=latent)
        if not verifier:
            return spec, None, refus
        rapport = V.verifier(spec, ex)
        if rapport["conforme"]:
            return spec, rapport, refus
        refus.append(rapport["refus"]["controle"])
    return None, None, refus


def ecrire_prive(dossier, nom, objet):
    chemin = os.path.abspath(os.path.join(dossier, nom))
    if any(f in chemin for f in FRAGMENTS_PUBLICS):
        raise PermissionError("dossier public refusé : un monde de test ne s'écrit que dans un dossier privé")
    octets = json.dumps(objet, sort_keys=True, ensure_ascii=False, indent=1).encode("utf-8")
    with open(chemin, "xb") as f:
        f.write(octets)
    h = hashlib.sha256(octets).hexdigest()
    with open(chemin + ".sha256", "x", encoding="utf-8") as f:
        f.write(f"{h}  {nom}\n")
    return h

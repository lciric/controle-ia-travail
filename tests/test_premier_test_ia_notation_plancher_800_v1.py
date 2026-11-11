"""Notation par lots des 800 directions de chaque plancher de P3-bis (règle (a'), R-2320) : dans le run de P3-bis (logique de
P3 inchangée, `run.py` l. 482 et 280), toutes les sondes linéaires d'une couche — directions de plancher comprises — sont
notées en un seul produit matriciel par action (`premier_test_ia.notation.Notation`, l. 35-49 et 81-85), puis agrégées par
le maximum ou l'attention ; la garde d'identité du run (`notation.exiger_identite`) les renote par la boucle du harnais
(`harnais.sondes.score_action`) sur une action par lot. Essais : à 2 × 800 directions (maximum et attention), la notation par
lots égale la boucle sur chaque direction et chaque action (écart relatif ≤ 1e-12, rapporté à 1 + |score|, et part des
scores égaux au bit près relevée) ; les 200 premières directions sont notées pareil dans une notation à 200 ou à 800
directions ; la garde d'identité passe (cas sain) et arrête sur une direction altérée (artefact)."""
import numpy as np
import pytest

from controle_ia.gardes import GardeArret
from controle_ia.harnais.sondes import score_action
from controle_ia.premier_test_ia.notation import Notation, exiger_identite
from controle_ia.sondes.evaluation import plancher_apparie
from controle_ia.sondes.familles import SondeLineaireJetons

D, COUCHE = 48, 15


def _jeu(n_plancher: int):
    rng = np.random.default_rng(20261111)
    entrainement = [rng.normal(size=(int(rng.integers(2, 12)), D)).astype(np.float32) for _ in range(60)]
    sondes = [SondeLineaireJetons("tromperie-difference_moyennes-c15", COUCHE, "max", rng.normal(size=D), 0.3),
              SondeLineaireJetons("enjeux-lineaire-c15", COUCHE, "max", rng.normal(size=D), -0.1),
              SondeLineaireJetons("tromperie-attention-c15", COUCHE, "attention", rng.normal(size=D), 0.0,
                                  rng.normal(size=D), "attention")]
    pt = plancher_apparie("tromperie-difference_moyennes-c15-plancher", COUCHE, entrainement, "max", n_plancher, 11)
    pa = plancher_apparie("enjeux-attention-c15-plancher", COUCHE, entrainement, "attention", n_plancher, 12)
    actions = [rng.normal(size=(int(n), D)).astype(np.float32) for n in (1, 2, 7, 23, 40, 64, 5, 31)]
    return sondes + pt + pa, actions


def test_notation_par_lots_egale_a_la_boucle_a_800_directions():
    sondes, actions = _jeu(800)
    notation = Notation(sondes, "cpu")
    noms_lineaires = notation._lineaires[COUCHE][0]
    assert sum(1 for x in noms_lineaires if "-plancher-" in x) == 1600                        # un seul produit par couche
    pire, egaux, total = 0.0, 0, 0
    for a in actions:
        sc = notation.noter({COUCHE: a})
        for s in sondes:
            ref = score_action(s, a, 0, a.shape[0])
            pire = max(pire, abs(sc[s.nom] - ref) / (1.0 + abs(ref)))
            egaux += int(sc[s.nom] == ref)
            total += 1
    assert pire <= 1e-12, pire
    assert total == len(actions) * 1603 and egaux / total > 0.0
    print(f"notation par lots contre la boucle, 1 603 sondes × {len(actions)} actions : écart relatif max {pire:.3e}, "
          f"égaux au bit près {egaux}/{total}")


def test_les_200_premieres_notees_pareil_a_200_ou_a_800_directions():
    s800, actions = _jeu(800)
    s200, _ = _jeu(200)
    assert [s.empreinte() for s in s200] == [s.empreinte() for s in s800 if s.nom in {x.nom for x in s200}]
    n800, n200 = Notation(s800, "cpu"), Notation(s200, "cpu")
    pire = 0.0
    for a in actions:
        x, y = n800.noter({COUCHE: a}), n200.noter({COUCHE: a})
        pire = max(pire, max(abs(x[k] - y[k]) / (1.0 + abs(y[k])) for k in y))
    assert pire <= 1e-12, pire


def test_garde_d_identite_saine_et_artefact():
    sondes, actions = _jeu(800)
    notation = Notation(sondes, "cpu")
    a = actions[4]
    sc = notation.noter({COUCHE: a})
    r = exiger_identite(notation, {COUCHE: a}, sc, 1e-6)                                         # cas sain
    assert r["sondes_controlees"] == 1603 and r["ecart_relatif_max"] <= 1e-12
    altere = dict(sc)
    altere["tromperie-difference_moyennes-c15-plancher-plancher-799"] += 1e-3                  # artefact : dernière direction
    with pytest.raises(GardeArret, match="garde d'identité"):
        exiger_identite(notation, {COUCHE: a}, altere, 1e-6)

# Vérification des corrections du code du hasard du défenseur, version 2 (classe B)

- Vérificateur : Claude Opus 5.5, auteur de la contre-lecture `docs/notes/chantiers-21-novembre-v1/code-v1/contre-lecture-code-hasard-defenseur-opus-v1.md` (ebc0f5266203…).
- Pièces lues :
  - `src/controle_ia/hasard_defenseur_v2/` ;
  - `tests/test_hasard_defenseur_v2_*.py` ;
  - `scripts/simulations_hasard_defenseur_v2.py` ;
  - `docs/notes/chantiers-21-novembre-v1/code-v1/rapport-code-hasard-defenseur-v2.md` (d5ec45d3…).
- Tous les sceaux de ces pièces sont vérifiés et conformes.
- Je n'ai modifié aucun fichier existant et n'ai fait aucun commit. Les mutations ont tourné dans une copie sous mon bloc-notes, restaurée puis comparée au dépôt.

## Verdict

**Conforme après corrections. Une seule correction reste à faire.**

Onze constats sur douze sont fermés et ne produisent aucun effet de bord. Le constat 11 est renvoyé au concepteur, comme il le demandait.

Le constat 4 n'est fermé qu'à moitié : la correction du code est juste, mais son essai ne la touche pas. L'erreur est d'abord la mienne, car mon exemple de la contre-lecture était mal décrit (voir plus bas).

## Correction restante, mot pour mot

Ajouter un fichier neuf, `tests/test_hasard_defenseur_v2_complements_constat4_v1.py` :

```python
import numpy as np
import pytest

from controle_ia.hasard_defenseur_v2 import contraste_v2 as C


def test_constat_4_cellules_constantes_a_k_3():
    L = np.array([[[0, 0, 0, 1, 1, 1, 2, 2, 2]]], dtype=np.int8)
    z = np.array([[0.1, 0.1, 0.1, 0.0, 0.0, 0.0, 0.6, 0.6, 0.6]])  # variances nulles ; sans la correction : 8,2·10⁷
    assert C.stat_studentisee(z, L, 3)[0] == pytest.approx(0.5e6)
```

Je l'ai éprouvé dans la copie :
- il passe sur le code v2 ;
- il casse quand on retire la ligne `var = np.where(var <= 1e-12 …)`.

Sans cette ligne, la statistique vaut 8,2·10⁷ ; avec elle, elle vaut 5·10⁵, ce qui est la règle du dénominateur nul.

Il faut aussi corriger le commentaire de l'essai `test_constat_4_variance_d_arrondi_tenue_pour_nulle` du fichier des compléments. L'erratum à écrire dit : « cet essai vérifie la règle du dénominateur nul à k = 2, mais n'éprouve pas la correction : à k = 2, deux valeurs égales donnent une variance exactement nulle, avec ou sans elle ». L'essai lui-même peut rester tel quel.

## L'écart sur le constat 4 : 677 000 ou 676 856,4

**Les deux nombres sont justes, chacun pour son entrée.**

- **677 000** correspond à l'entrée du développeur : (0,977 − 0,3) × 10⁶, pour E = (0,3 ; 0,3) et U = (0,977 ; 0,977).
- **676 856,4** correspond à mon exemple de la contre-lecture : U ≈ 0,9768564. J'avais écrit « 0,977 » en arrondissant ce nombre.

L'écart vient de mon arrondi, pas du code.

**Ma propre erreur.** Le cas qui donnait 6,4·10⁷ dans mes essais n'avait pas deux valeurs égales sous U. Elles différaient d'une unité d'arrondi, parce que l'une était calculée `b + 0,1 − 0,1` et l'autre `b`. Je l'ai pourtant décrit comme « Z = (0,977 ; 0,977) ».

Je l'ai vérifié sur le code v1 :
- à k = 2, deux valeurs exactement égales donnent toujours une variance exactement nulle ;
- l'entrée (0,3 ; 0,3 / 0,977 ; 0,977) donne déjà 677 000 sans la correction ;
- c'est pourquoi l'essai du développeur passe aussi sur v1.

**La correction reste fondée.** À k = 3, trois valeurs égales donnent une variance positive minuscule dans 768 cas sur 2 000 tirés au hasard. Exemple : E = (0,1 ; 0,1 ; 0,1), U = (0,6 ; 0,6 ; 0,6), qui donne 8,2·10⁷ sans la correction. Le défaut est donc réel, mais il ne se voit qu'à partir de k = 3. Avec la correction, il disparaît.

## Les douze constats

| # | Sort | Vérification |
|---|---|---|
| 1 | fermé | L'essai de l'annexe est porté mot pour mot (comparaison de texte, imports exceptés). La mutation « rejeu des conditions ignoré » casse. |
| 2 | fermé | Essai porté. La mutation « Phipson et Smyth retiré » casse. |
| 3 | fermé | Essai porté. La mutation « maximum remplacé par la statistique propre » casse. |
| 4 | **à moitié** | Le code est inséré mot pour mot, à `contraste_v2.py:38`. L'essai n'éprouve pas la correction (mutation survivante), d'où la correction restante ci-dessus. |
| 5 | fermé | Le refus figure dans `rejouer` et dans `controler_ordre`, et `RefusGraine` est importé. Ses deux mutations cassent. Aucun appel interne ne passe une liste : le script n'appelle ni `rejouer` ni `controler_ordre`, et les essais passent des entiers. |
| 6, 7, 8 | fermés | Essais portés. Les trois mutations cassent. |
| 9 | fermé | Aucun code n'était demandé. La phrase est portée au rapport. |
| 10 | fermé | La ligne est ajoutée à « Ce qui n'est pas écrit ». |
| 11 | renvoyé au concepteur | Comme le demandait le constat. |
| 12 | fermé | La phrase de la docstring est portée mot pour mot. |

**Effets de bord.** J'ai comparé chaque module v2 à son module v1, une fois les noms de version ramenés au même texte. Seuls diffèrent :
- `__init__` : docstring, avec la phrase du § 5 conforme mot pour mot à la spécification ;
- `contraste` : une ligne et la docstring ;
- `registre` : le refus du constat 5 et deux docstrings ;
- `gardes` : le refus du constat 5 et un import.

`audit`, `erreurs`, `inventaire`, `monde`, `permutation` et `puissance` sont identiques. Les huit fichiers d'essai portés et le script sont identiques à leur version 1, une fois les noms rendus pareils.

## Mutations rejouées sur la v2

Ce sont les 36 mutations de la contre-lecture, portées sur la v2. Chacune joue le fichier d'essai visé plus le fichier des compléments.

- **34 cassent.** Cela inclut les six qui survivaient sur la v1.
- **2 survivent : le sceau seul et l'empreinte seule.** C'est une défense en profondeur : retirés ensemble, l'essai casse, comme sur la v1.

J'ai ajouté trois mutations propres aux corrections :
- les deux refus du constat 5 : ils cassent ;
- le retrait de la correction du constat 4 : il **survit** à la suite v2, et casse avec l'essai proposé.

**Essais.** `PYTHONPATH=src python -m pytest -q tests/test_hasard_defenseur_v2_*.py` donne **62 réussis en 36,1 s**.

## Le script complet non relancé : fondé

1. **Les corrections ne touchent aucun calcul joué.**
   - La seule correction de calcul, celle du constat 4, ne mord qu'à partir de k = 3 sur des valeurs non entières. Les simulations jouent k = 2 avec Z entier : dans {−1, 0, 1}, ou dans {−4, −1, 1, 3, 4} pour G5 (b).
   - À k = 2, des valeurs égales donnent zéro exactement, et des valeurs entières inégales donnent une variance d'au moins 0,5.
   - Les autres corrections portent sur des fonctions que le script n'appelle pas.
2. **J'ai rejoué moi-même les deux scripts en petite taille**, avec l'entropie 20261122. Une fois retirés les champs `version`, `code` et `duree_s`, les deux sorties sont identiques.

**Une réserve, documentaire seulement.** La sortie de référence porte l'empreinte du code v1 (`ea1eef41…`). Si le futur préenregistrement court engage le code v2 et cite ces chiffres, il devra dire qu'ils viennent du code v1, ou rejouer le script v2, ce qui prend 36 minutes en local et ne coûte rien.

## Ce que je n'ai pas fait

- Je n'ai pas lancé le script complet.
- Je n'ai écrit aucune correction dans le dépôt.
- Je n'ai relu ni le constat 11 ni les points renvoyés au concepteur, qui ne sont pas de mon ressort.

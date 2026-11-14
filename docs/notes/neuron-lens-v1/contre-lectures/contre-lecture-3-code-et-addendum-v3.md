# Contre-lecture 3 (ciblée v2 → v3) du code de décision et de l'addendum — rapport recopié

Contre-lecteur : sous-agent neuf, « modèle D » (troisième modèle, différent de celui de l'autrice ; le « modèle B » des contre-lectures
précédentes est indisponible jusqu'au 20 novembre, R-2718), lancé après 11:03 UTC ; une première tentative sur le modèle B s'était arrêtée
sur la limite d'usage. Il n'a écrit aucune des pièces. Pièces relues : `verdicts_b_alpha_v3.py`
(`8f57088ae4b29affd8863015a99675138ceb19044354964719b82ca0efaa54a0`), son essai (`1ee366fa99de3ca69cd4ed24484dcb75843019edefe399b820d0a5ece5ab2a26`),
`decisions_volet_a_v3.py` (`36c0ea8b34438d9b852c3f2e8a774a2f765471d8a109f0ea68e97336ab34adea`), son essai
(`22858c0e4618ec314418ddd2355b2e101c58187f7683718edcc63b94bf0829b9`), `addendum-empreintes-v3.md`
(`e63d95caa06fde0cb23d2b0dbcd143413d822be9487edf8f54fe72b46db0df82`). Recopié sans modification de fond.

---

1) **Empreintes et essais** : les 5 empreintes concordent ; 51 essais passés. Relu : la différence complète v2 → v3, des détails des
sources de `decisions_volet_a_v3.py` et de la copie du code voisin (pas les fichiers v3 en entier).

2) **Verdicts** : `verdicts_b_alpha_v3.py` **scellable en l'état** ; son essai **scellable en l'état** ; `decisions_volet_a_v3.py`
**scellable après corrections mineures** (1 à 3) ; son essai **scellable après corrections mineures** (3) ; `addendum-empreintes-v3.md`
**scellable en l'état**.
- (a) Les 12 remarques de la contre-lecture 2 sont traitées (détail : entiers de [0, 64] et essais ; B-7 par le haut sans préfixe, « en
  attente » ne suspend pas B-β ; motifs exclusifs déclarés et essayés ; gardes de `n_par_couche` ; formes et métadonnées affirmées,
  aléatoires dérivés par `random_neurons` comme `score` ; refus des valeurs non écrites à 4 décimales ; matrice non finie = arrêt ; essais
  ajoutés ; gardes du volet A ; arrondi à 6 décimales déclaré et essayé aux bords 0,05, −0,02 et 0,02 ; définition « neurones égaux »
  déclarée et `en_attente` ; addendum corrigé).
- (b) Pas de régression ni de contradiction avec le texte gelé ; les nouvelles lectures (arrondi à 6 décimales ; seuil 0,005 de « neurones
  égaux » ; refus des valeurs non écrites à 4 décimales) sont déclarées et compatibles.
- (c) `random_neurons` est identique à l'original (lignes 66-68 de la copie) ; l'essai vérifie déterminisme, longueur et unicité, pas une
  valeur de l'original.

3) **Remarques**
1. Mineure — `decisions_volet_a_v3.py` : `mean(chutes_sac) >= 0.02`, `sonde_id >= 0.99`, `sonde_ood >= 0.99`, `chute_s >= 0.5 * chute_sac`
   restent des bords flottants non arrondis. Correction : arrondir, ou écrire « arrondi limité aux écarts d'AUROC et à `borne_basse_ood` ».
2. Mineure — `audit_volet_a` : le paramètre `neurones_egaux_partout` masque la fonction du même nom ; `en_attente` n'est pas relié à
   `audit_volet_a` par un essai. Correction : renommer le paramètre ; essai de bout en bout.
3. Mineure — `isinstance(True, int)` fait accepter un booléen comme valeur de `n` (B-α) ; liste des valeurs reconnues de `verdict_i` écrite
   en dur. Sans conséquence réelle ; correction facultative : exclure `bool`.

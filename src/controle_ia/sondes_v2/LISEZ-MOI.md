# Sondes de la boîte blanche, version 2 — code (v1)

Instrument de classe B, écrit d'après la consigne du développeur
(`docs/procedures/sondes-v2/consigne-developpeur-code-sondes-v1.md`, sha256 `60aef942…`) et son **erratum 1**
(`…-erratum-1.md`, `e9c8cde1…`) et **erratum 2** (`…-erratum-2.md`, `1e6ebdbe…`), qui priment, au service du texte
scellé des diagnostics préalables (`prereg/diagnostics-prealables-sondes-v1.md`, `e8dca00b…`) ; accord
GO-2026-11-22-126, décision 2. Données fabriquées seulement ; ce
fichier ne porte aucun résultat.

## Ce que fait chaque module

- `magasin_v1.py` — **brique A**, magasin d'activations gardées. Une série (lecture d'un jeu de textes par un jeu de
  poids) vit dans un dossier : manifeste scellé, `actions.jsonl`, jetons de la couche 15 en demi-précision
  (`c15/<clé>.npy`, convention d'`ActivationsDemi`), jeton d'avant le champ révélateur aux couches 7, 15 et 23
  (`avant_champ/c<k>/<clé>.npy`). Le lecteur relit en simple précision et vérifie l'empreinte de chaque fichier à chaque
  lecture. `intersection_cles` compare des séries sur l'intersection de leurs clés et rapporte les effectifs.
  `serie_depuis_activations_demi` est l'adaptateur du format `ActivationsDemi`. `series_depuis_barreau5` est l'adaptateur
  du format gardé par la relecture du barreau 5 (règle « une_sur_dix »), d'après la pièce de format `b8539886…`, éprouvé
  sur des fichiers fabriqués seulement. Chaque série porte au manifeste son **chemin de calcul** (erratum 1, § 1) ; deux
  séries de chemins différents ne se comparent pas, sauf par `diagnostic_intersection_chemins_melanges`.
- `formes_closes_v1.py` — **brique B**, sondes en forme close, au processeur : différence des moyennes (appariée ou non),
  différence des moyennes blanchie, régression logistique à pénalité quadratique, régression ridge sur les seuls
  épisodes honnêtes avec son résidu « déclaré moins attendu ». Chaque fonction rend une `SondeLineaireJetons`. Le score
  d'une action est le maximum sur ses jetons. La seule moyenne sur les jetons est `diagnostic_moyenne_jetons` (N-026) ;
  aucun module du paquet ne l'appelle.
- `lecture_v1.py` — **brique C**, validation croisée imbriquée, groupée par tâche et par unité. L'épreuve est enfermée
  et ne s'ouvre qu'avec une sonde gelée dont l'empreinte est écrite au journal sur disque. Statistiques :
  - changement de signe à l'unité ;
  - interaction du plan à quatre cases ;
  - nul de réétiquetage qui rejoue toute la sélection ;
  - capacité de mémorisation ;
  - étalon de transport ;
  - sonde d'identité ;
  - contraste apparié ;
  - prédicteurs triviaux.

  Sortie scellée, et un résumé sans nombre ni issue pour les sessions aveugles.
- `statistiques_v1.py` — **brique C, statistiques de l'erratum 1** :
  - étalon de transport par vecteurs moyens, test exact par échange dans la paire, plancher, contrôle d'intensité,
    variante de production (§ 2) ;
  - sonde d'identité (§ 3) ;
  - rejeu croisé sur tables de scores gardés, avec contrôle du chemin et interaction résiduelle (§ 4) ;
  - Holm, libellés par seuils en arguments, minimums, graines nommées (§ 5).
- `monde_plante_v3.py` et `programme_monde_plante_v3.py` — **brique D** (erratum 1, § 6 ; erratum 2, § 3, 4 et 6 ;
  texte scellé, « Épreuve à vérité plantée »). Les douze mondes et leurs critères de passage, chacun par la borne de
  l'intervalle exact à 95 %, sont dans `verites_mondes_plantes_v3.json`, scellé et committé avant toute exécution.
  Les fichiers de vérités v1 et v2 sont gardés tels quels, remplacés. Deux modes :
  - « complet » (`--taille`) : toutes les lignes, une famille ;
  - « étalon » (`--cas`, ou `--grille` : paires de 4 à 16, familles de 1 à 4, tâches de 8 à 64, actions 1 ou 2) :
    une case par combinaison.

  500 répliques par défaut.

## Comment s'en servir

```
python3 -m venv .venv && . .venv/bin/activate && pip install -r requirements-cpu.txt
PYTHONPATH=src python -m pytest -q tests/test_sondes_v2_*.py            # de 30 s à 2 min selon la charge
SONDES_V2_LENT=1 PYTHONPATH=src python -m pytest -q tests/test_sondes_v2_monde_plante_v3.py -k lent   # essai lent
PYTHONPATH=src python -m controle_ia.sondes_v2.programme_monde_plante_v3 --sortie DOSSIER --taille 8,8,3 --entropie N
PYTHONPATH=src python -m controle_ia.sondes_v2.programme_monde_plante_v3 --sortie DOSSIER --grille --entropie N
```

`--taille` donne, dans l'ordre : nombre de paires, de tâches, d'actions par tâche et par source de texte. `--cas`
donne : paires, familles, tâches, actions.

Le nul par paire de poids (contraste apparié) a une valeur p plancher voisine de 2/2^P, puisque l'échange simultané de
toutes les paires laisse l'aire inchangée. Avec 39 répliques, sa valeur p tombe souvent sur 0,05 ; d'où le défaut de
199 répliques. Le seuil
α et `u_fort` (libellé « fort » de l'étalon) sont des arguments (`--alpha`, `--u-fort`) ; les seuils de la sonde
d'identité sont ceux du texte scellé (`statistiques_v1.SEUILS_IDENTITE`) ; leurs défauts sont lus dans
le fichier des vérités. Avec un nul de m répliques, la plus petite p atteignable est 1/(m + 1). Le changement de signe
exact sur n unités ne descend pas sous 2/2ⁿ en bilatéral ; l'étalon de transport ne descend pas sous 2^(2−P) : il faut au
moins sept paires pour un libellé à α = 0,05 (sinon « non testable à cet effectif »). Le rejeu croisé ne libelle qu'à
partir de 8 tâches et 40 actions (défauts de l'erratum, en arguments).

## Conventions

- Le paquet ne charge pas torch : les fonctions réemployées des sondes v0 (`SondeLineaireJetons`, `aire_sous_courbe`,
  `intervalle_blocs`, `plancher_apparie`) sont recopiées à l'identique dans `reemploi_v1.py`, et un essai compare leurs
  sorties octet pour octet aux originaux (défaut 12 de la contre-lecture, question Q1).
- Double précision. Calcul linéaire sur une seule tâche, par `threadpoolctl` : mêmes octets d'une exécution à l'autre.
  Tolérances déclarées entre machines : `formes_closes_v1.TOLERANCE_ENTRE_MACHINES`, éprouvées en changeant le nombre
  de tâches de calcul et l'ordre des actions.
- Graines par `numpy.random.SeedSequence` (`manifeste.graines` et `manifeste.generateur`), écrites au rapport.
- Gardes (R5), chacune éprouvée sur un cas sain et sur un artefact :
  - clé manquante ou en double ;
  - empreinte fausse ;
  - forme inattendue ;
  - fichier non déclaré ;
  - clés et étiquettes désalignées ;
  - tâche ou unité des deux côtés d'un pli ;
  - plus de 1 % de tirages dégénérés (ligne « non calculable ») ;
  - épreuve ouverte avant le gel.

## Choix provisoires

Q1 à Q13 : confirmés par la mère à titre provisoire, à revoir par le concepteur. E-1 à E-8 : lectures du développeur
là où l'erratum laisse un détail ouvert. Tous sont marqués dans le code.

- E-1 : libellés « fort », « faible » et « contraire » de l'étalon.
- E-2 : chemin retenu par case dans le rejeu croisé (« origine » d'abord).
- E-3 : écart d'intensité (tous les adaptateurs décalés, les saboteurs 1,2 fois).
- E-4 : décalage de chemin sur les deux cases d'origine, (adaptateur, textes du saboteur) et (nu, textes honnêtes).
- E-5 : le changement de signe par unité du contraste apparié peut être trop libéral, car les plis partagent leur
  apprentissage. La lecture « contraste » repose donc sur le nul réétiqueté par paire de poids, échangée d'un bloc.
- E-6 : direction de la trace commune à toutes les familles.
- E-7 : étiquettes permutées « à cinq points du taux nominal », lu comme une borne haute ≤ 0,10 pour chaque ligne.
- E-8 : contrôle du chemin : l'écart retiré est une constante par dose (moyenne sur les tâches des moyennes par
  tâche), et non un écart propre à chaque tâche.

- Q1 : réemploi des sondes v0 (copies sans torch dans `reemploi_v1.py`).
- Q2 : moyenne par paire.
- Q3 : poids 1/n par action dans la régression logistique.
- Q4 : grille et choix d'alpha de la régression ridge.
- Q5 : plis (unité × groupe de tâches).
- Q6 : ordre de simplicité.
- Q7 : réduction par pli de l'interaction (remplacée par le rejeu croisé de l'erratum).
- Q8 : statistique du changement de signe et unité échangeable du nul.
- Q9 : étalon de transport et prédicteurs triviaux.
- Q10 : lectures « établie », « contraire » et « haute ».
- Q11 : aire moyenne des plis.
- Q12 : sens de l'interaction contraire.
- Q13 : contraste apparié et effet principal du texte.

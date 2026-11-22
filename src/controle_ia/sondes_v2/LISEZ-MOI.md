# Sondes de la boîte blanche, version 2 — code (v1)

Instrument de classe B, écrit d'après la consigne du développeur
(`docs/procedures/sondes-v2/consigne-developpeur-code-sondes-v1.md`, sha256 `60aef942…`) et son **erratum 1**
(`…-erratum-1.md`, `e9c8cde1…`, qui prime), accord GO-2026-11-22-126, décision 2. Données fabriquées seulement ; ce
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
- `monde_plante_v2.py` et `programme_monde_plante_v2.py` — **brique D** (erratum 1, § 6). Les douze mondes et leurs
  lectures attendues sont dans `verites_mondes_plantes_v2.json`, scellé et committé avant toute exécution. Le fichier
  v1 est gardé tel quel, remplacé. Le programme rapporte puissance, taux de fausse lecture et taux d'arrêt des gardes,
  avec leurs intervalles exacts, pour chaque effectif demandé ; 500 répliques par défaut.

## Comment s'en servir

```
python3 -m venv .venv && . .venv/bin/activate && pip install -r requirements-cpu.txt
PYTHONPATH=src python -m pytest -q tests/test_sondes_v2_*.py            # moins d'une minute
SONDES_V2_LENT=1 PYTHONPATH=src python -m pytest -q tests/test_sondes_v2_monde_plante.py -k lent   # essai lent
PYTHONPATH=src python -m controle_ia.sondes_v2.programme_monde_plante_v2 --sortie DOSSIER \
    --taille 8,8,3 --taille 12,10,4 --nul 39 --tirages 2000 --entropie N
```

`--taille` donne, dans l'ordre : nombre de paires, nombre de tâches, actions par tâche et par source de texte. Le seuil
α, `u_fort` (libellé « fort » de l'étalon) et le seuil de la sonde d'identité sont des arguments (`--alpha`,
`--u-fort`, `--seuil-identite`) ; leurs défauts sont lus dans
le fichier des vérités. Avec un nul de m répliques, la plus petite p atteignable est 1/(m + 1). Le changement de signe
exact sur n unités ne descend pas sous 2/2ⁿ en bilatéral ; l'étalon de transport ne descend pas sous 2^(2−P) : il faut au
moins sept paires pour un libellé à α = 0,05 (sinon « non testable à cet effectif »). Le rejeu croisé ne libelle qu'à
partir de 8 tâches et 40 actions (défauts de l'erratum, en arguments).

## Conventions

- Aucun module du paquet n'importe torch lui-même. Les statistiques réemployées passent par `sondes.familles`, qui
  importe torch (question Q1 à la mère).
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

Q1 à Q13 : confirmés par la mère à titre provisoire, à revoir par le concepteur. E-1 à E-5 : lectures du développeur
là où l'erratum laisse un détail ouvert. Tous sont marqués dans le code.

- E-1 : libellés « fort », « faible » et « contraire » de l'étalon.
- E-2 : chemin retenu par case dans le rejeu croisé (« origine » d'abord).
- E-3 : écart d'intensité (tous les adaptateurs décalés, les saboteurs 1,2 fois).
- E-4 : décalage de chemin sur les deux cases d'origine, (adaptateur, textes du saboteur) et (nu, textes honnêtes).
- E-5 : le changement de signe par unité du contraste apparié peut être trop libéral, car les plis partagent leur
  apprentissage. La lecture « contraste » repose donc sur le nul réétiqueté par paire de poids, échangée d'un bloc.

- Q1 : import de torch par le réemploi.
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

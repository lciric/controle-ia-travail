# Sondes de la boîte blanche, version 2 — code (v1)

Instrument de classe B, écrit d'après la consigne du développeur
(`docs/procedures/sondes-v2/consigne-developpeur-code-sondes-v1.md`, sha256 `60aef942…`), accord GO-2026-11-22-126,
décision 2. Données fabriquées seulement ; ce fichier ne porte aucun résultat.

## Ce que fait chaque module

- `magasin_v1.py` — **brique A**, magasin d'activations gardées. Une série (lecture d'un jeu de textes par un jeu de
  poids) vit dans un dossier : manifeste scellé, `actions.jsonl`, jetons de la couche 15 en demi-précision
  (`c15/<clé>.npy`, convention d'`ActivationsDemi`), jeton d'avant le champ révélateur aux couches 7, 15 et 23
  (`avant_champ/c<k>/<clé>.npy`). Le lecteur relit en simple précision et vérifie l'empreinte de chaque fichier à chaque
  lecture. `intersection_cles` compare des séries sur l'intersection de leurs clés et rapporte les effectifs.
  `serie_depuis_activations_demi` est l'adaptateur du format `ActivationsDemi`. L'adaptateur du format gardé par le test
  sur les adaptateurs jumeaux viendra plus tard, d'après une description fournie par la mère.
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
- `monde_plante_v1.py` et `programme_monde_plante_v1.py` — **brique D**, épreuve à vérité plantée. Le générateur a des
  composantes réglables. Les sept mondes et leurs lectures attendues sont dans `verites_mondes_plantes_v1.json`,
  scellé et committé avant toute exécution. Le programme rapporte la puissance et le taux de fausse lecture avec leurs
  intervalles exacts, pour chaque taille demandée.

## Comment s'en servir

```
python3 -m venv .venv && . .venv/bin/activate && pip install -r requirements-cpu.txt
PYTHONPATH=src python -m pytest -q tests/test_sondes_v2_*.py            # moins d'une minute
SONDES_V2_LENT=1 PYTHONPATH=src python -m pytest -q tests/test_sondes_v2_monde_plante.py -k lent   # essai lent
PYTHONPATH=src python -m controle_ia.sondes_v2.programme_monde_plante_v1 --sortie DOSSIER \
    --taille 6,6,3 --taille 10,8,4 --repliques 20 --nul 39 --entropie N
```

`--taille` donne, dans l'ordre : nombre d'unités, nombre de tâches, actions par tâche et par source de texte. Le seuil
α et le seuil de la sonde d'identité sont des arguments (`--alpha`, `--seuil-identite`) ; leurs défauts sont lus dans
le fichier des vérités. Avec un nul de m répliques, la plus petite p atteignable est 1/(m + 1). Le changement de signe
exact sur n unités ne descend pas sous 2⁻ⁿ : avec quatre unités, aucune lecture ne peut être « établie » à α = 0,05.

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

## Choix provisoires (en attente de la mère)

Ils sont marqués « provisoire (Qn) » dans le code ; les textes de lecture à venir primeront par un erratum.

- Q1 : import de torch par le réemploi.
- Q2 : moyenne par paire.
- Q3 : poids 1/n par action dans la régression logistique.
- Q4 : grille et choix d'alpha de la régression ridge.
- Q5 : plis (unité × groupe de tâches).
- Q6 : ordre de simplicité.
- Q7 : réduction par pli de l'interaction.
- Q8 : statistique du changement de signe et unité échangeable du nul.
- Q9 : étalon de transport et prédicteurs triviaux.
- Q10 : lectures « établie », « contraire » et « haute ».
- Q11 : aire moyenne des plis.
- Q12 : sens de l'interaction contraire.
- Q13 : contraste apparié et effet principal du texte.

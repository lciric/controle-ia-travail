# Lecture comme le mentor — Stefan Heimersheim, question 2 — v1

Lecture commencée le 3 novembre 2026 à 13:07:29 UTC (temps universel coordonné, `date -u`) ; fichier écrit à partir de 13:16 UTC. Lecteur neuf : je n'ai écrit aucune version des réponses.

## Sources lues (empreintes recalculées par moi)

- Réponse : `brouillons/redaction-finale-v1/heimersheim-q2/reponse-v1.md`, `61b484ae91e8461690eae2663e7dbbff81a01e7eaa2e51b4ba5cf92dc914d4f1`, conforme à la consigne. Texte compté : la ligne 1, au-dessus du trait.
- Question : `brouillons/candidature-pivotal-v16/formulaire-site-colle-par-lazar-2026-11-03-1209.txt`, lignes 20 à 24, `57393598f012eb641e709db42efe4b52321c7061e0ff8954910f061019f7b5c6`. « Why do you want to work on Mechanistic Interpretability? » ; « Max. 150 words; spend the majority of time on Q1 ».
- Rapport sur le mentor : `brouillons/candidature-pivotal-v16/lecture-approfondie-v1/rapport-heimersheim-v1.md`, `b55e2f243974dcccb52480a0a2cd803dd7cf6497b430b4e9926b4f7eba8aabfd`.
- Article : arXiv 2606.24964v1 (23 juin 2026), page du résumé, lue par WebFetch. Un modèle intermédiaire la rend : niveau transcription au sens de R7, non opposable.
- Ce que le mentor verrait en cliquant. Copie locale `/home/claude/scratch/depots-publics-2026-11-03/`, dossier modifié à 12:21 UTC ; références `origin/main` locales, lues sans `fetch` :
  - `sycophancy-construct-validity`, commit `146b2a4`, `README.md` `de5d6032d42cc2eb893e2d1339ae0c6423c4cebc2e1b7ecc83d35cf9c3154da8` ;
  - `sycophancy-psychophysical-law`, commit `b3ecaec` (10:35 UTC). `STATUS.md` : `b0ed2c9802e4c9d17c385c1c533cc27e66188bcb05960fd88d8bab119c256bab`. R9 : `81abd962afe1ba8f99840a8b54262b1820184e5a767139712d1e5898d28ce36e`, identique à l'empreinte archivée que cite R9-bis. R9-bis : `8c7145036f06ccc8dcd6b4e918d002adb65a6f51917013595263526ec87c5009`.
- **Réserve.** Je n'ai pas pu vérifier d'ici que les deux dépôts sont publics : le mandataire de la session répond 403. Les ouvrir en navigation privée avant l'envoi.

## Verdict

Aucun point bloquant. Deux points à corriger :
- le résultat nul de l'ouverture est donné sans dose, et le mentor le lira avec ses plateaux ;
- R9-bis est cité comme préenregistré, mais il n'est pas encore archivé.

Limite respectée : 148 mots au pire cas, 130 par espaces.

## 1. La phrase qu'il contredirait

- **Aucune contradiction frontale avec ses résultats.** Trois points sont conformes au résumé de 2606.24964 :
  - les auteurs : Francisco Ferreira da Silva, Stefan Heimersheim ;
  - le sens de « privileged » : le modèle est moins robuste le long des directions pures que le long de leurs mélanges ;
  - les valeurs : p > 2 pour les directions contrastives, p ≈ 2 pour les témoins aléatoires et pour l'analyse en composantes principales.
- **La phrase la plus exposée** : « yet no single-direction intervention I tried reduced it ». Il la lirait avec ses plateaux :
  - une perturbation sous le seuil de rupture est absorbée (billet de 2024 sur les plateaux d'activation) ;
  - ce seuil varie jusqu'à environ 70 fois d'une direction à l'autre (2606.24964, note 1, d'après le rapport ; transcription) ;
  - sans balayage de dose, un nul ne montre donc pas que la direction ne contrôle rien. Il demanderait : « à quelle dose, au-delà du plateau ? ».

  Le dépôt ne donne ni dose (README, ligne 88) ni chiffre (README, ligne 21). La version précédente de la Q2 disait elle-même « single dose interventions » (formulaire, ligne 26).
  - Gravité : **à corriger**.
  - Correction minimale, si elle est exacte : « … I tried (no dose sweep) reduced it ». La compenser par « the directions social pressure adds to activations ». Le script donne alors 131 mots par espaces et 149 au pire cas. Sans la compensation, on monte à 151 au pire cas.
  - Autre voie, plus coûteuse en mots : dire dans le plan que R9-bis lit des courbes de dose et non un point (R9-bis, ligne 9). L'objection devient alors un atout.

## 2. Affirmations plus fortes que leur preuve

- **À corriger.** « I have preregistered both measurements … (R9 and R9-bis …) ».
  - R9 est archivé (version v2026.11.5, Zenodo 10.5281/zenodo.23909891, 3 novembre, 06:49 UTC ; STATUS, ligne 29). Il contient déjà les deux mesures : F1, l'angle de rupture ; F3, le changement de note (R9-bis, ligne 9).
  - R9-bis est écrit et poussé, mais pas archivé : « R9 starts only after R9-bis is archived on Zenodo » (STATUS, ligne 31). La copie de 12:21 UTC ne porte aucune étiquette après v2026.11.5. Le dépôt dit lui-même « R9, preregistered » (ligne 27), mais « R9-bis, written » (ligne 31).
  - Correction : archiver R9-bis avant l'envoi (c'est une publication, donc une décision de Lazar). Sinon, citer « R9 » seul, ce qui économise 3 mots au pire cas.
- **Mineur.** « reduced it ». Le détail du README est plus faible : « no clean reduction », sorties non conservées, « carry no numbers » (ligne 21). Son en-tête dit pourtant « reduced » (ligne 3). Correction : « cleanly reduced it » (+1 mot). Cumulée avec la correction du point 1, on arrive à 150 au pire cas : c'est la limite exacte.
- **Mineur, exact.** « contrastive directions, readable by construction, are privileged ».
  - Le résumé donne aussi p > 2 pour deux autres familles : les directions du décodeur d'autoencodeur épars, et les directions de la méthode « Mechanistically Eliciting Latent Behaviors », trouvées par leur effet en aval et non lisibles par construction.
  - La phrase laisse donc croire que le privilège tient à la lisibilité.
  - Pas de correction dans 150 mots. À garder pour l'entretien : ce fait nourrit la question posée.
- **Mineur.** « your test could screen steering targets, such as an evaluation-awareness direction ».
  - « could » borne déjà la phrase.
  - Son instrument : couche précoce, dernier jeton d'invites courtes. La réponse est une distance euclidienne à l'avant-dernière couche. Les invites de conversation n'ont pas été testées (résumé de l'article dans R9, § 11).
  - Or la conscience d'évaluation dépend d'un long contexte.

## 3. Ce que la question demande et qui manque

- **Mineur.** Le « pourquoi » tient en une phrase : lire n'a pas permis de contrôler. Le reste est une question de recherche et un plan.
- L'enjeu de sûreté (moniteurs, défenses par pilotage) n'apparaît qu'en passant, par la direction de conscience d'évaluation.
- Le mentor demande de consacrer l'essentiel du temps à la Q1 : la gravité reste mineure. Aucun ajout sans compensation au mot près.

## 4. Ce qui le perdrait

- **Mineur.** « possibly training fit » : tournure serrée, qu'il faut relire pour comprendre « peut-être mesurée sur les données d'entraînement de la sonde ». Correction : « possibly in-sample », même compte au pire cas.
- **Mineur.** « ρ = 0.684 » : corrélation entre quoi et quoi, sur combien d'items ? Le README dit « projection–behaviour correlation ». Pas de place pour le préciser.
- **Mineur.** « the model's ratings » : notes de quoi, sur quelle échelle ? La Q2 ne le dit pas.
- **Mineur.** « R9 and R9-bis » : ce sont des étiquettes internes, et « bis » est rare en anglais. Elles renvoient bien à des fichiers du dépôt.
- **Mineur.** La dernière phrase cumule deux-points, parenthèse, lien et point-virgule. Elle reste lisible d'une traite.

## 5. Ce qui le retiendrait (ne pas couper)

- **La question elle-même** : une direction privilégiée (p > 2) contrôle-t-elle le comportement qu'elle prédit ? Ses deux issues sont annoncées (« If yes … if no … »).
  - Elle prolonge la limite que l'article déclare : p > 2 est nécessaire sans être suffisant, et la réponse y est mesurée en distance, pas en comportement.
  - C'est le cœur de la réponse.
- **« rotating toward them »** : son protocole (rotation à norme fixe), porté sur un comportement et sur un modèle de conversation, un cas qu'il n'a pas testé.
- **Le nul personnel, vérifiable** : l'en-tête du README dit la même chose (ligne 3), et « training fit » reprend ses réserves (lignes 70 et 115).
- **« not yet run »** : honnête.
- **Le pont avec la Q1** (option c), par la direction de conscience d'évaluation.

## 6. Compte de mots par script

Script hors dépôt `/tmp/lecteur-heim-q2-scripts/compter.py`, lancé avec `nice -n 10 python3 -I`, sur la ligne 1 de la réponse :

```
espaces (str.split): 130
jetons avec au moins une lettre ou un chiffre: 128
coupe aux tirets: 141
coupe aux tirets et barres obliques: 145
regex \w+ (pire cas): 148
```

La limite est dure : 150 mots au plus. Les cinq comptes la respectent, avec une marge de 2 au pire cas. Ils concordent avec le compte de l'auteur (130, 141, 148).

Corrections recomptées par `/tmp/lecteur-heim-q2-scripts/variantes2.py` (espaces / pire cas) :
- dose seule : 133 / 151, ce qui dépasse au pire cas ;
- dose et compensation : 131 / 149.

# Vérification du devis du collisionneur sur « ce qui rend une idée intéressante » (v1)

Pièce de travail, 2026-11-23, par un vérificateur neuf (Opus 5.5) qui n'a écrit ni le texte servi ni le devis. Aucun appel réseau, aucune dépense : le calcul du devis a été relancé hors ligne.

**Verdict : bon à soumettre**, avec quatre remarques (aucune ne change le chiffre à soumettre) et une correction de chiffre pour la v2 (total « toutes relances » : 52,08 USD, non 52,02).

## 1. Ce qu'accorde la décision GO-2026-11-23-21 (`git show origin/main:registres/go.md`, ligne 859)
Mot de Lazar : la demande reformulée part au collisionneur avec toutes les espèces disponibles, Fable 5.2 et Opus 5.5 en effort maximal par sessions de l'abonnement (sans dépense), et Neon. Le départ est conditionné : après test de neutralité et devis vérifié, **« départ sur le mot de Lazar sur le plafond »**, montant « selon devis », échéance 2026-11-30. Le GO n'accorde donc pas encore la dépense : le plafond de 30 USD doit recevoir le mot de Lazar.

## 2. Objet servi : la v2
- Texte servi retenu : **`texte-servi-idees-interessantes-v2.md`**, empreinte `db1132cafe8b7bf7b4892e19210f385ed52705e10639d0161c45f2367b6478f1` (compagnon conforme). Test de neutralité de la v2 : neutre, 0,45 (`devinette-texte-servi-v1.md`) ; la v1 était à 0,55.
- Extrait de la v1 : la demande reformulée (`git show origin/main:docs/notes/idee-interessante-v1/demande-reformulee-modele-idees-interessantes-v1.md`, empreinte `230585b9…` vérifiée) lue de « ## Contexte » (ligne 7) jusqu'à la fin est **identique octet pour octet** à la v1 (`e8fc644f…`, vérifiée). Seul retrait : les six premières lignes (titre, en-tête qui nomme « la mère », « le directeur », les répondants et le fichier des intuitions, ligne vide, séparateur). Le texte servi ne contient ni « mère », ni « directeur », ni « Lazar », ni « Fable », ni « Opus », ni « Claude ».
- Écart v1 → v2 : trois retouches et elles seules (parties 1, 2 et 7), exactement celles listées dans `devinette-texte-servi-v1.md`. La v2 n'est donc plus un extrait exact de la demande reformulée ; l'écart est déclaré et la demande n'est pas modifiée.

## 3. Relance du calcul
`PYTHONPATH=src python3 -B docs/notes/collisionneur-v9/collisionneur_v9_v8m.py devis --fable --opus --argon --carbon --neon --faits F --question F` (F = chemin du texte servi ; le moteur attend un chemin, non le texte : passé en texte, il s'arrête au code 1). Moteur `420394f9…`, identique à l'empreinte que la voie v6 exige.
- avec F = v1 : sortie identique à `devis-moteur-v8m-cinq-especes-v1.txt` (`06e8de5d…`) ;
- avec F = v2 : sortie identique à `devis-moteur-v8m-cinq-especes-v2.txt` (`6da40be3…`).

## 4. Sommes (étage III, cellules payantes Argon, Carbon, Neon)
| Tour | v1 | v2 |
|---|---|---|
| 1, conception | 1,66 + 2,32 + 1,49 = 5,47 | 1,67 + 2,32 + 1,49 = **5,48** |
| 2, critique croisée | 1,80 + 2,45 + 1,60 = 5,85 | 1,80 + 2,46 + 1,60 = **5,86** |
| 3, réponse | 1,86 + 2,52 + 1,64 = 6,02 | **6,02** |
| Sans relance | 17,34 | **17,36** |
| Toutes relances (×3) | 52,02 | **52,08** |

Les chiffres annoncés pour la v1 sont justes ; pour la v2, 17,36 est juste, et le total toutes relances devient 52,08 USD. Fable et Opus (pire cas nominal 2,52 à 3,01 et 1,31 à 1,50 USD) ne sont pas comptés : voir § 6. Les étages I et II affichés par le devis ne sont pas joués (le script lance `etage3`).

## 5. Règle de relance (code)
`nombre_relances` (moteur, vers la ligne 2665) : deux relances chez Google quand le plafond de relance égale le premier (`reglage_de_relance`, vrai pour les trois espèces : 65 536 / 65 536), soit une relance identique déclarée puis un dernier recours déclaré à un niveau de réflexion plus bas (plan à trois essais, lignes 2492-2494). Les relances ne partent que sur sortie vide ou coupée ; refus et anomalies vont à l'arbitre. Chaque relance coûte au plus le pire cas de sa cellule : le facteur 3 est juste. Le rejeu des cellules Claude n'existe que sous `--effort-max` du moteur, que le script ne passe pas.

## 6. Plafond vérifié avant chaque appel ; cellules Claude gratuites
- Avant chaque essai (premier, relance, dernier recours), `executer_cellule` refuse l'envoi si dépense du dossier + pire cas de cet essai > `--plafond-usd`, puis si dépense sur la ligne + pire cas > `--ligne-usd` (lignes 2543-2551), avant la déclaration de relance et avant l'envoi. Le script `vague_abonnement_v2.sh` passe la même valeur aux deux ; une ligne garde son montant d'une vague à l'autre (`ouvrir_ligne`), ce qui convient aux relances du dossier après chaque porte de kits.
- Voie v6 (`d99f3358…`, compagnon conforme) : aucune génération ni aucun comptage chez Anthropic (`refuser_anthropic` lève une erreur, le compteur d'Anthropic est retiré, la clé passée est factice) ; la réponse recueillie est servie avec un usage nul et `usage_lu` vrai, donc `juger` la compte à 0 USD ; servie une seule fois, aucune relance payée possible. Les cellules Claude ne coûtent rien.

## 7. Le plafond de 30 USD est-il raisonnable ?
Oui. Simulation au pire (chaque essai coûte son pire cas, ordre A à E dans chaque tour) :
- **part sûrement** : les trois tours sans aucune relance (17,36 USD) ; le tour 1 entier même avec ses six relances (16,44 USD) ; en général, toute série de relances dont le pire cumulé ne dépasse pas la marge de 12,64 USD (30 − 17,36, soit six à sept relances de 1,5 à 2,5 USD) tient jusqu'à la dernière cellule ; la garde de Fable au tour 3 (remarque 3) est plus lâche (elle admet jusqu'à 15,65 USD de relances aux tours 1 et 2) ;
- **serait coupé** : avec deux relances partout, le refus tombe au tour 2 sur Neon (dépense 29,22 USD, tour 3 non joué) ; avec une relance partout, au tour 3 sur la relance de Carbon (dépense 28,92 USD), Neon du tour 3 non joué. Le refus est un arrêt nommé (code 4), sans envoi, jamais silencieux.
Le pire réel est moindre : la dépense comptée est le coût réel lu (sauf envoi interrompu ou usage absent, comptés au pire).

## 8. Remarques
1. **Total toutes relances à corriger pour la v2** : 52,08 USD (52,02 est le chiffre de la v1).
2. **Effort des sessions** : le devis affiche « effort high » pour Fable et Opus (réglage par défaut du moteur, sans effet sur le coût). L'effort réellement servi est l'argument `EFFORT` du script ; le GO demande l'effort maximal : lancer avec `max`, alors que l'en-tête de la voie v6 recommande `high` pour une cellule de collisionneur. Le mot de Lazar prime ; à écrire dans l'ordre de lancement.
3. **Garde de plafond des cellules Claude** : bien que gratuites, elles sont contrôlées au pire cas nominal (Fable jusqu'à 3,01 USD au tour 3) dans `garder_avant_kit` et à la relecture. Si la dépense dépasse 26,99 USD avant le tour 3, la cellule de Fable serait refusée sans rien coûter. Effet seulement dans le cas des relances nombreuses ; à savoir, pas à corriger avant le départ.
4. **Empreinte manquante** : `docs/notes/collisionneur-v9/reprise-v8d-v1/vague_abonnement_v2.sh` (`2f7c2ecb…`) n'a pas de compagnon `.sha256` (règle R6). Petite correction de classe B ou C.
5. Astra absente faute de crédit OpenAI : faux échec « jamais parti », à inscrire au registre des idées de la veille de cap ; elle n'entre pas dans la composition (aucune option `--astra`), donc aucune absence à accepter.

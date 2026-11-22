# Collisionneur v9, mode essaim (v3) : rapport du développeur

22 novembre 2026. Pièce d'instrument (classe B), écrite par Opus 5.5. Elle part de la v2 (0e9eecaa…), qui n'a pas été touchée. Aucun réseau n'a été appelé, aucune clé n'a été lue, aucun commit n'a été fait.

Les recommandations de la réponse 13 de Fable sont accordées par Lazar (GO-2026-11-22-24). La configuration `configuration-pilote-essaim-v3.json` le dit dans son statut.

## Corrections de la vérification du contre-lecteur

- **B1 (bloquant).** Le motif `MOTIF_PROPOSITION` devient `\b(?i:proposition)\s+[A-E](?!\w)`, comme le contre-lecteur l'a proposé. « La proposition a deux défauts. » est publié ; « proposition A » et « PROPOSITION B » sont refusés.
- **B2 (bloquant).** `lancer` refuse un `--faits` différent de `--question` avant tout envoi, avec le texte proposé par le contre-lecteur.
- **(c)** `lire_configuration` refuse des limites `mots.brouillon` et `mots.finale` différentes de celles des tours III.1 et III.3 de la v8d (3 500 mots chacun).
- **(d)** `enveloppe` exige la même composition d'espèces dans tous les dossiers donnés.
- **(e)** Les chevrons sont refusés aussi sous toute forme qui se ramène à `<<<` ou `>>>` par la normalisation NFKC (`porte_balise`), par exemple les chevrons pleine chasse. Ce refus vaut à la publication, à l'injection et dans `verifier`.
- **(f)** Dans `caracteres_prevus`, au cycle 1 en ordre simultané, les salons des autres ne sont plus comptés.
- **(a)** `simuler` liste désormais les dossiers lus avec l'empreinte de chaque `journal.jsonl`, prise avant la lecture. Si un journal change pendant la lecture, la commande s'arrête. Le tableau est refait plus bas.

## Ajouts décidés par la mère

**(1) Format de la réponse finale.** La ligne « Format : … » de l'invite isolée du tour III.3 est ajoutée, mot pour mot, après la consigne finale de Fable. Elle vient du préambule de la v8d et porte « français, Markdown », la limite de 3 500 mots et le marqueur `FIN-DE-CELLULE`.
- C'est un **écart déclaré au texte de Fable** ; le reste de son texte n'a pas changé.
- Un essai compare cette ligne à celle d'une invite isolée du tour III.3 construite par la v8d.
- Les cycles gardent la forme de Fable, sans cette ligne.

**(2) Plafond dur de 64 USD et option `reserver_finales`.**
- **L'option.** `reserver_finales` est désactivée par défaut et déclarée dans la configuration. Quand elle est active, avant chaque appel de cycle, l'appel est sauté et journalisé si l'inégalité suivante n'est pas tenue :

  dépense mesurée + pire du plan complet de cet appel + somme des pires des plans complets des réponses finales non encore écrites ≤ plafond

  La revue due que ce saut fait perdre est consignée.
- **Ce qu'elle garantit.** Les cinq réponses finales tiennent sous le plafond, sous deux hypothèses :
  - l'invite réelle reste sous la borne du devis (vérifié avec de faux appelants seulement) ;
  - la tokenisation reste au-dessus de 2 caractères par jeton (le plus bas relevé est 2,227).
- **Où elle ne joue pas.** Elle ne s'applique pas au temps 0. Les pires avec relances des brouillons (22,23 USD) et des finales (29,10 USD) font ensemble 51,33 USD, moins que 64. Elle suppose que `--ligne-usd` vaut le plafond.

## Devis du pilote

Question générale (caa3365b…), ordre simultané, parts non bloquantes, sans réseau.

| cycles | pire sans relance | pire avec relances | finales seules (pire, avec relances) |
|---|---|---|---|
| 3 | 53,87 USD | 140,55 USD | 27,89 USD |
| 4 | 69,14 USD | 178,75 USD | 29,10 USD |

**Ce que ferait la garde à 64 USD avec 4 cycles, sans l'option.**
- `executer_cellule` refuse un essai avant l'envoi dès que la dépense mesurée plus le pire de cet essai dépasse 64. Le pire d'un premier essai de réponse finale va de 1,39 USD (Astra) à 3,44 USD (Fable) ; une relance d'Anthropic coûte jusqu'à 4,2 USD de plus au pire.
- **Quand le risque commence.** Le refus, puis l'arrêt de la course (code 4), ne menacent qu'au-delà d'environ 57 à 62 USD déjà dépensés. Les appels exposés sont les derniers de la course : réponses finales, et le dernier cycle si la dépense est très haute.
- **Ce que prévoit la simulation.** La course entière devrait coûter environ 28,8 USD, dont 23,2 USD avant les finales. Rien ne serait alors refusé.
- **Avec l'option.** Les appels de cycle seraient sautés au-delà d'environ 26,9 USD de dépense réelle (64 − 29,10 − environ 8 USD pour un appel de cycle de Fable ou de Carbon au pire). Le dernier cycle est donc exposé, à la limite de la dépense prévue de 23,2 USD. C'est pourquoi l'option reste désactivée par défaut : **à trancher**.

## Simulation refaite

Treize dossiers ont été lus ; l'empreinte est celle du `journal.jsonl` au moment de la lecture :

| dossier | empreinte |
|---|---|
| collisionneur-anteriorite-pilier-v1-20261121-131029 | c2fae5127140e8d16b890d2e5ff0ee7fec91ece92f1f81e1055f7355cda1a2aa |
| …-131029-rejeu-argon-v8d-v1 | 813615c3c4553b68779d387e2abac0a2f880a02db86a08d0b3aa54e6509ff904 |
| collisionneur-derive-de-regime-v2-20261121-131044 | 925043c94d95dd0284ca49bc411d66e2eeb73e30558c0c739712ee793a5962ad |
| …-131044-rejeu-argon-v8d-v1 | 2c0406b13a537748783d3bd9e949812dc4798b385999a19096bd141bedfc234c |
| collisionneur-dopamine-v1-20261120-122457 | 2d03f96fce0979bdabd632722964340ae58a405f2d926756adb78358a01d7258 |
| collisionneur-methodes-maths-v1-20261121-093850 | d779015eee3aeb1a82df2294c3f1bf05eb77d8015ed310e1c9f97ba5a1b27606 |
| …-093850-rejeu-argon-v8d-v1 | 33ec9c8eda877f8dd05c24516521570624563e41dfd6d9eddf0849b4729d9637 |
| collisionneur-percee-controle-securite-v1-20261121-114810 | 9f6d689380d224e053659ba75212000366327197b7ad96204f8f6294ee43a5c2 |
| …-114810-rejeu-argon-v8d-v1 | 12904f056f9727e725eaf872c7e98eced03b7329dce64bc1a81c4d97ead4b0b7 |
| collisionneur-protocole-x-coercition-v1-20261122-061053 | a1c50325d8cc762ae20bf11f66990065c63a33c199ad3899e43c76553363f474 |
| collisionneur-question-de-recherche-fusionnee-v1-20261121-153256 | 22216d3f6c5e149c5f3847c8ccd07287786c282306be58bc4484cd397fbb04b8 |
| …-153256-rejeu-argon-v8d-v1 | 2d4b29f949fd3311a2a3ce4b551066f0f0904c9bef620b894e9df0b4e8e9c920 |
| collisionneur-seuil-moniteurs-v1-20261121-063125 | 7b1cb98f8ec6c70d71905e33cd77302f86f3ed5babe38b52667568a170afdda3 |

**Pourquoi le tableau de la v2 différait.** Le dossier `protocole-x-coercition`, course isolée encore en cours lors de la v2, porte maintenant une cellule III.1 de Carbon envoyée avec un niveau de réflexion. La référence de Carbon passe donc à 4,92 USD et son tour III.1 mesuré à 0,48 USD. Le tableau ci-dessous retrouve les chiffres du contre-lecteur.

**Réserve.** Ce dossier peut encore changer, et un dossier en cours entre dans les mesures. La commande s'arrête si un journal bouge pendant la lecture, mais pas entre deux lectures.

Coût prévu en USD, et entre parenthèses son rapport à la référence :

| cycles | fable (réf. 5,71) | opus (2,76) | argon (2,53) | astra (1,33) | carbon (4,92) | tours sautés prévus |
|---|---|---|---|---|---|---|
| 2 | 6,39 (1,12) | 3,25 (1,18) | 3,34 (1,32) | 1,14 (0,86) | 3,89 (0,79) | 0 % |
| 3 | 8,30 (1,45) | 4,19 (1,52) | 4,24 (1,67) | 1,56 (1,17) | 5,07 (1,03) | 0 % |
| 4 | 10,23 (1,79) | 5,13 (1,86) | 5,14 (2,03) | 1,98 (1,49) | 6,27 (1,27) | 15 % |

**Résultat de `cycles` : aucun nombre de 2 à 4 ne tient.** Les hypothèses sont celles de la v2, supposées : remplissage à 90 % des limites, six ouvertures dès le cycle 2, sortie au niveau mesuré en mode isolé, 6,5 caractères par mot.

## À signaler à Fable (non modifié)

- Il fallait ajouter le format à la réponse finale pour l'aligner sur l'invite isolée (point 1 ci-dessus). C'est un écart déclaré, décidé par la mère.
- Les invites des cycles n'ont ni « français, Markdown » ni marqueur de fin, et leur texte reste celui de Fable.
- Les en-têtes de Fable disent « vous », les règles de la v8d disent « tu ».

## Essais et mutations

- **Essais.** Le fichier de la v3 compte 44 essais, tous passés, sous `env -u` des clés. Ce sont les 36 essais de la v2, plus :
  - les essais de B1, B2 et des points c à f ;
  - l'essai du format final ;
  - l'essai de la réserve des finales.
- **Mutations.** Trente et une mutations sont toutes prises : les 23 mutations de la v2, rejouées sur la v3, et 8 nouvelles. Les nouvelles couvrent B1 (motif insensible à la casse), B2 (faits différents admis), les points c, d, e et f, le format isolé absent de la finale, et la réserve inopérante.
- Les scripts de mutation sont hors du dépôt, dans `/tmp/claude-0/-home-user-controle-ia-travail/880667cb-41bd-5ef3-a231-ed6614227479/scratchpad/mutations/` :
  - `lancer_mutations_v3.py` ;
  - `lancer_mutations_v2_sur_v3.py`.

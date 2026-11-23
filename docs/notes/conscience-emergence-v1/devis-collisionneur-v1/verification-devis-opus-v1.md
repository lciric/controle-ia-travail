# Vérification du devis du collisionneur sur la question neutre « conscience et émergence » (v1)

- Vérificateur neuf, Claude Opus 5.5, 2026-11-23. Aucun appel à un modèle externe, aucune vague lancée ; seul le calcul du devis, qui ne touche pas au réseau, a été relancé.
- Pièce vérifiée : `devis-collisionneur-conscience-emergence-v1.md` (`057fabe5512c6faa…`).

## Verdict

**À corriger.** Le calcul relancé donne exactement la sortie versée et les sommes du tableau sont justes. Il reste quatre défauts à corriger avant la ligne d'engagement : un chiffre faux (« toutes relances »), une commande de course qui n'est pas fixée (l'option de sortie maximale change le pire cas du simple au double), les espèces et l'effort à mettre d'accord avec les mots de Lazar, et une confirmation du plafond absente du registre des accords. Aucun de ces défauts ne demande de dépense pour être corrigé.

## 1. Empreintes

| pièce | empreinte | compagnon |
|---|---|---|
| devis | `057fabe5…` | conforme |
| sortie brute du moteur | `3ad5427b…` | conforme |
| question servie `texte-servi-question-neutre-v1.txt` | `aa2b7027…` | conforme |
| moteur `collisionneur_v9_v8m.py` | `420394f9…` | conforme ; c'est aussi l'empreinte que la voie abonnement v6 exige avant de charger le moteur |
| voie `abonnement-v1/voie_abonnement_v6.py` | `d99f3358…` | conforme (contrôle lancé dans son dossier) |
| script de vague `reprise-v8d-v1/vague_abonnement_v2.sh` | `2f7c2ecb3285fee8…` | **aucun compagnon `.sha256`** (règle 6) ; défaut mineur, n° 6 ci-dessous |

## 2. Relance du calcul

La commande donnée par la mère a été relancée avec `PYTHONPATH=src`, et elle a rendu le code 0. Sa sortie a pour empreinte `3ad5427b8a05ce11…`. Elle est **identique** octet pour octet à la sortie brute versée (`diff` vide).

## 3. Sommes et règle des relances

- Sommes par tour : 1,67 + 0,48 + 2,33 + 1,50 = 5,98 ; 1,84 + 0,90 + 2,49 + 1,62 = 6,85 ; 1,91 + 1,07 + 2,56 + 1,67 = 7,21. Total payant 20,04. Tour 1 de Carbon et Neon : 3,83. Cellules Claude au prix de l'interface : 12,94. Étage III complet : 32,98. **Toutes ces sommes sont justes.**
- La règle « deux relances par cellule de Google, une pour Astra » est bien celle du moteur. `nombre_relances` rend 2 chez Google quand les plafonds sont égaux, 2 chez Anthropic sous `--effort-max`, et 1 ailleurs. Dans `executer_cellule`, le plan est [premier envoi, relance identique, dernier recours] chez Google à plafonds égaux, et [premier envoi, relance] ailleurs.
- **Défaut 1 : le total « toutes relances » de 57,67 USD est faux.** Le moteur compte chaque relance « au plafond de relance » : c'est la phrase finale du devis, et c'est ce que fait `pire_tours_2_3` avec `cout_pire_garde(m, garde, m["max_relance"])`. Le plafond de relance d'Astra est de 32 000 jetons, pour un premier envoi à 8 000. Sa relance coûte donc au pire 1,68, 2,10 et 2,27 USD selon le tour, et non 0,48, 0,90 et 1,07. J'ai recalculé avec les fonctions mêmes du moteur (`cout_pire_cas`, `nombre_relances`) :
  - Google : 17,59 USD × 3 = 52,77 USD ;
  - Astra : 2,45 + 6,05 = 8,50 USD ;
  - **total : 61,27 USD.**

  Les 57,67 USD s'obtiennent en comptant la relance d'Astra au plafond du premier envoi. La conclusion ne change pas : ce pire cas reste au-dessus du plafond, que le moteur fait tenir.

## 4. Garde du plafond, script de vague et voie abonnement

- **Avant chaque envoi**, dans la boucle des essais de `executer_cellule`, le moteur calcule le pire cas de l'essai sur l'entrée comptée et sa tolérance. Il refuse l'envoi si la dépense du dossier plus ce pire cas dépasse `--plafond-usd`, ou si la dépense de la ligne plus ce pire cas dépasse `--ligne-usd`. Le refus porte le code 4 et il est écrit au journal. **Vérifié.**
- Le plafond vaut pour le seul dossier de course. Une dépense faite sous le même accord hors de ce dossier ne serait pas vue par le moteur. Sur `origin/main`, le registre des dépenses ne porte encore aucune dépense sur cet accord.
- Le script `vague_abonnement_v2.sh` passe bien `--plafond-usd $P --ligne-usd $P` et `GO_ID=$GO`. Le plafond n'est donc tenu que si la mère donne `P=40` et `GO=GO-2026-11-23-19`. Je n'ai trouvé aucune valeur fixée par défaut.
- **Cellules Claude.** La voie v6 remplace l'appel à Anthropic par `refuser_anthropic`, qui lève une erreur à tout appel direct. Elle retire le comptage sur la clé (`COMPTEURS.pop("anthropic")`). Le script passe une clé factice (`ABONNEMENT_CLE_FACTICE=factice-aucun-appel`). Une réponse recueillie est lue une seule fois, avec un usage de 0 et donc un coût de 0. **Aucune clé d'Anthropic n'est employée : vérifié.**
- Avant d'écrire un kit, la voie fait aussi la garde du plafond (`garder_avant_kit`), sur le pire cas de la cellule au prix de l'interface, soit environ 3,12 USD pour Fable au tour 3. Une cellule Claude ne coûte rien, mais il faut qu'il reste cette marge sous le plafond pour qu'elle parte.
- La contre-lecture de la voie v6 (`abonnement-v1/contre-lecture-voie-abonnement-v6-opus-v1.md`) dit bien « conforme », puis « corrections conformes ».
- La garde commune de Google (`garde_google_v3`) est importée par le moteur. `verifier_reglages_google` est appelée sur le corps de chaque essai avant l'envoi. **Vérifié.**

## 5. Respect de l'accord, et affirmations du devis

**L'accord.** Sur `origin/main`, la ligne GO-2026-11-23-19 est présente (ligne 857 de `registres/go.md`) : 40 USD, échéance au 30 novembre, départ après un devis écrit et vérifié, Astra seulement après la recharge du crédit d'OpenAI. Le devis tient ce plafond et cette échéance.

**Défaut 2 : la commande de course n'est pas fixée, et une option double le pire cas.**
- Le devis est calculé sans option. Ni le devis ni la ligne d'engagement ne donnent la commande exacte de la vague : arguments d'espèces, `--sortie-max`, `--effort-max`, valeur de `--effort` de la voie.
- Or le dossier précédent a tourné **avec la sortie maximale**. Son `especes.json`, sur la branche `origin/runs/collisionneurs-reprise-v8d-v1`, porte `"sortie_max": true`, et son journal porte « sortie maximale True ».
- Si la vague reprend cette option, le moteur relancé avec `--sortie-max` donne :
  - Astra à 128 000 jetons, soit 6,48, 6,90 et 7,07 USD par tour ;
  - **38,04 USD au pire sans relance** et 93,67 USD avec toutes les relances ;
  - Fable à 128 000 jetons, si bien que chaque kit Claude demande environ 7 USD de marge sous le plafond.
- Avec cette option, le plafond de 40 USD arrêterait probablement des cellules en fin de dossier. Le chiffre de 20,04 USD ne vaudrait plus.
- **Correction demandée** : écrire dans le devis et dans la ligne d'engagement la commande exacte, avec les six espèces, sans `--sortie-max` ni `--effort-max` (ce qui est cohérent avec le calcul), et avec `--effort` fixé. Si l'on garde la sortie maximale, il faut refaire le devis avec cette option.

**Défaut 3 : les espèces et l'effort ne suivent pas les mots de Lazar.**
- Les mots de Lazar (événement `e4fb2d53…`, relu) disent « a part neon fable max argon carbon astra ». La ligne d'accord dit « Neon, Argon, Carbon et Astra (et Fable) ».
- **Opus 5.5 n'est pas nommé.** Le devis l'ajoute en sixième espèce. Il ne coûte rien par l'abonnement, mais il faut soit déclarer cet ajout à Lazar dans la ligne d'engagement, soit le retirer.
- Lazar dit **« Fable max »**, et le devis ne dit pas quel effort sera passé à la voie. La voie v6 admet `max`, `xhigh` ou `high`, et une seule valeur s'applique à tous les kits Claude, Opus compris. Le dossier précédent a tourné en `xhigh`. Il faut écrire l'effort retenu, `max` sur le mot de Lazar, et dire qu'il vaut aussi pour Opus.

**Défaut 4 : la confirmation du plafond n'est pas au registre.**
- La ligne GO-2026-11-23-19 de `origin/main` dit encore « Plafond à confirmer ou corriger par Lazar ». Elle cite une autre session (`session_013QMayo9xjrtkunN82E32sy`).
- La confirmation citée par le devis existe bien : je l'ai lue directement. L'événement `e4fb2d53-ab8d-4ab4-bbb2-098f658c4b28` est dans la session `session_016QhUrsc1rhjmmiLEmqPygF`, créé à 2026-11-23T08:43:33Z, et il dit « go plafond 40 USD pour Carbon, Neon et le collisionneur ».
- La mère doit inscrire cette confirmation au registre des accords avant l'engagement. Sans cela, l'affirmation « confirmé par Lazar » n'est pas vérifiable dans les pièces du dépôt.

**Défaut 5, à déclarer plutôt qu'à corriger : la lecture de « consultation de Carbon et Neon d'abord ».**
- Les mots « pour Carbon, Neon et le collisionneur » et « à part » peuvent se lire comme une consultation séparée du collisionneur.
- Le devis la fond dans le tour 1 du collisionneur. Cette lecture se défend : le point 1 de la question servie demande justement des motifs « plus spécifiques que le profil « local gardé, global perdu » ». Cela réduit aussi la dépense.
- Mais c'est une interprétation. Elle doit figurer dans la ligne d'engagement pour que Lazar puisse la corriger.

**Affirmations vérifiées dans les pièces :**
- Le « 12,50 USD réels » du dossier précédent est **vérifié** :
  - la note de sortie (`notes-de-sortie-v1/note-sortie-conscience-anesthesie-neutre-v1.md`, compagnon conforme, ligne 6) dit « 12,50 dollars par l'interface, sur une ligne de 50 », coupures de Carbon comprises ;
  - l'`etat.md` du dossier (`runs/collisionneur-protocole-x-conscience-anesthesie-neutre-abonnement-v1-20261122-153110`, sur la branche `origin/runs/collisionneurs-reprise-v8d-v1`) dit « Dépense totale : 12.50 USD », avec deux essais pour Carbon à la conception et à la critique ;
  - la somme des coûts au journal donne 12,50 USD ;
  - le moteur est bien `collisionneur-v9-v8m`, avec les mêmes six espèces.

  **Réserve** : ce dossier a tourné avec la sortie maximale, donc pas tout à fait dans les mêmes réglages. Voir le défaut 2.
- La longueur des questions est vérifiée : 294 mots pour la précédente et 1 094 pour celle-ci. Le rapport est de 3,7, ce qui est plus que « trois fois ». Retouche de forme seulement.
- L'heure et les mots de la confirmation (08:43:33Z) sont vérifiés.

**Affirmations non vérifiées ici** (aucune pièce fournie) :
- le refus de `--repli-lot` comme « leçon du 22 novembre » ;
- la provenance par commit `26786e7b` de la question servie ;
- le résultat « neutre, 0,40 » du test de neutralité (`f64ac2af…`), dont je n'ai pas lu la pièce.

**Défaut 6, mineur** : le script de vague `vague_abonnement_v2.sh` n'a pas de compagnon `.sha256`. Il faut le sceller, ou citer son empreinte `2f7c2ecb…` dans le devis.

## Corrections attendues pour « bon à soumettre »

1. Remplacer 57,67 par **61,27 USD** au pire avec toutes les relances, avec la mention « relance d'Astra au plafond de relance de 32 000 jetons ».
2. Écrire la commande exacte de la vague : six espèces, sans sortie maximale ni effort maximal du moteur, `--effort` fixé, `P=40`, `GO=GO-2026-11-23-19`. Si la sortie maximale est gardée, refaire le devis (38,04 USD sans relance).
3. Dans la ligne d'engagement, déclarer l'ajout d'Opus 5.5 sans dépense, ou le retirer, et dire l'effort des sessions Claude (« Fable max »).
4. Faire inscrire par la mère la confirmation du 08:43:33Z à la ligne GO-2026-11-23-19.
5. Déclarer que la consultation de Carbon et Neon est fondue dans le tour 1.
6. Sceller le script de vague ou citer son empreinte.

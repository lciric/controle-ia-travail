# Contre-lecture de la consigne des deux lecteurs du rejeu (critères v7) — v1

- **Contre-lecteur, modèle O.** Je n'ai écrit ni le mandat du rédacteur, ni la consigne, ni le rapport, ni aucune carte (règles R2 et R-3735). Écrit le 2026-11-20 (`date -u` : 2026-11-20T05:20:17Z). Processeur seul, aucune dépense, aucun appel de modèle. Rien n'est écrit dans le dépôt.
- **Pièces contre-lues**, dossier `docs/notes/organisme-auto-conception-v1/epreuves-v9/juge-selection/consigne-lecteurs-v1/`. Leurs empreintes sont égales à leur compagnon.
  - `consigne-lecteurs-rejeu-criteres-v7-v1.md` : `bf49bd50b699ebc51a00b57154453fdafd708985d8c74e8d079ad384d0e1cb72`.
  - `rapport-redacteur-consigne-lecteurs-rejeu-v1.md` : `be16525d0c16462e84f5b8e770517077b4e94efac7a009c39c7564467d36102d`.
- **Fait foi** :
  - le mandat `criteres-v7/mandat-redacteur-consigne-lecteurs-rejeu-v1.md` (`567d212e…`, égal à son compagnon) ;
  - le programme `criteres-v5/assemblage_selection_v4_v2.py` (`2f5640da…`), lu par plages : lignes 154 à 258, 548 à 587 et 1064 à 1083 ;
  - les critères v7 scellés (`6af793a2…`, ma copie de `main`) ;
  - GO-2026-11-20-10, point O2, ligne 541 de ma copie de `go.md`.

## Verdict

**Conforme après corrections.** La forme demandée est exactement celle que le programme accepte. La phrase sur `lignee_reconnue` est juste. Les décisions de Lazar sont rendues justes. Il y a quatre corrections, toutes mineures (K1 à K4), et le contrôle de `lignee_reconnue` est à faire par une pièce à part.

## 1. La forme, ligne par ligne

J'ai contrôlé moi-même chaque ligne citée par le rapport, § 2 :

- **Tête de la lecture.**
  - Cinq clés exactement (l. 160).
  - `lecteur` égal au nom passé, « F » ou « O » (l. 162).
  - `lignee` clé de `familles` (l. 164).
  - `independance` non vide (l. 166).
  - `cartes` liste non vide (l. 168).
- **Par carte : treize clés exactement.** Ce sont les douze de la l. 171-172 et `lignee_reconnue` sous `lignee_reconnue_declaree` (l. 173-174). L'égalité stricte de l'ensemble des clés est exigée (l. 183).
  - Clés interdites refusées (l. 178).
  - Doublon refusé (l. 186).
  - `separable`, booléen, exigé pour X1 et refusé ailleurs (l. 192-196).
  - Voie et sous-strate (l. 197-203).
  - En voie N, une question nulle impose Q = 0 (l. 206).
  - Notes entières, booléen refusé (l. 208-209).
  - Raisons (l. 211).
  - Dix-huit items, et « ajoutable » sur les sept seulement (l. 214-220).
  - Phrases (l. 221).
  - `groupe_fusion` (l. 224).
- **Veto : quatre clés exactement, non vides, sans doublon.** Une liste vide passe (l. 233-245).
- **Neuf entrées au plus.** C'est V + `suppleantes` (l. 577-579), avec V = 3 sous `selon_titulaires` et deux titulaires (l. 575-576), et `suppleantes` 6 sous la décision 2 (a).
- **Régime `ajoutables_oui`** : « ajoutable » y vaut 1 (l. 250-255).
- **Les deux lectures portent les mêmes cartes**, et autant que `cartes_attendues` (l. 552-557).
- **Gabarit** (§ 3.4) : il passe chacun de ces contrôles. Les identifiants y sont fictifs ; « ajoutable » n'y figure que sur T3 et B2 ; la voie P y a sa sous-strate.

## 2. `lignee_reconnue` et `lignee`

- **La phrase du § 4 est juste.** Elle donne les six chaînes `prop-opus`, `prop-fable`, `prop-argon`, `prop-astra`, `prop-carbon` et `aucune`, lettre pour lettre, pour les cartes comme pour le veto. Elle dit aussi pourquoi une autre graphie est une faute que le programme ne voit pas : il contrôle seulement qu'un texte est présent (l. 226 et l. 240), puis compte en silence par `familles.get(…)` (l. 1071).
- **`lignee`** (§ 3.1) : `prop-fable` et `prop-opus`, lettre pour lettre, en accord avec la l. 164 et avec la table du manifeste.

## 3. Les choix du rédacteur

**(i) Famille Opus-Fable reconnue sans la lignée → l'étiquette la plus probable des deux.** Ce choix tient.
- La l. 1071 ne compare que la famille du lecteur : écrire `aucune` ferait compter à tort « ne croit pas reconnaître sa famille ».
- Les critères (§ 1) prévoient d'ailleurs qu'il reconnaisse « la lignée ou la famille ».
- Le cas ne se pose que pour cette famille : chaque autre lignée a la sienne.
- Le prix est une fausse précision au niveau de la lignée dans la lecture déposée. Il faut la compter : correction **K2**.

**(ii) La limite sur la famille des lecteurs mise dans une note de dépôt.** C'est une correction (**K1**).
- Les critères scellés (§ 1) veulent la limite « écrite en tête de chaque lecture ». La lecture, c'est le fichier JSON.
- L'annexe A n'a pas de clé pour elle, mais `independance` est un texte libre : seule sa présence est contrôlée (l. 166). La limite peut donc ouvrir cette clé, qui est en tête de la lecture, sans rien changer au programme.
- La note de dépôt reste utile pour les écarts. Elle n'est prévue par aucune pièce scellée, mais elle est hors du JSON et ne gêne rien. Elle doit avoir son compagnon (**K4**, règle R6).

**(iii) Les deux règles de tenue.** Les deux tiennent.
- « La `lignee_reconnue` d'une entrée de veto recopie celle de la même carte » : c'est la même croyance, dite deux fois. Rien ne la contrôle (l. 532-534 du rapport), mais rien ne la contredit.
- « Ne pas composer son veto d'après la lignée reconnue, ni pour devancer le filtre » : c'est le sens de « désigne sans voir l'espèce » (critères, § 8) et de la règle R3.
- Ni l'une ni l'autre n'est un nœud.

## 4. Le contrôle de `lignee_reconnue` : une pièce à part, non une correction de la consigne

Sans contrôle par programme, une faute de graphie tomberait en silence dans « ne croit pas reconnaître sa famille ». C'est le repli silencieux que la règle R5 interdit. La relecture par le lecteur (§ 10) n'est pas une garde.

**Recommandation : un petit programme de la mère**, joué sur chaque lecture déposée **avant `assembler`**.
- Il refuse, sans rien écrire, toute valeur de `lignee_reconnue`, dans `cartes` comme dans `veto`, qui ne soit ni une clé de `familles` du manifeste, ni `aucune`.
- Il lit la seule lecture et le manifeste, aucune carte.
- Il a son essai, avec un cas sain et un artefact (règle R5).
- Il est contre-lu et scellé avant l'ouverture, avec les autres pièces.

C'est **une pièce à part**, hors des trois programmes scellés. Elle n'en change aucun et ne change aucune règle de lecture : elle ne fait que refuser. Elle ne demande pas de correction de la consigne, qui dit déjà qu'une graphie fausse « est une lecture à refaire ». On peut seulement y ajouter, une fois la pièce écrite : « la mère contrôle ce champ par programme avant l'assemblage ».

## 5. Les décisions de Lazar (GO-2026-11-20-10, O2)

- 1 (a) : rejeu à blanc, aucune valeur de sélection, aucune adoption par la lecture (en-tête, § 0, § 8).
- 2 (a) : trois cartes et six suppléantes au plus, retrait par famille, plafond au nombre visé, qui ne joue pas à deux lecteurs (§ 7).
- 3 (b) au rejeu : `lignee_reconnue` pour chaque carte, avant de la noter (§ 4).
- 4 (b) : « ajoutable » compte oui, et la règle de réponse ne dépend pas du régime (§ 5).
- 5 (a) au rejeu : cartes masquées et coupées à la médiane, et ce que la coupe implique (§ 1).
- Les huit confirmations, telles qu'écrites (en-tête).

Toutes sont rendues justes.

## 6. Aucun identifiant de modèle

Je l'ai vérifié par recherche bornée sur le seul fichier de la consigne : aucun. Les lignées sont nommées par leurs étiquettes `prop-…`, qui sont des étiquettes et non des identifiants de modèle. « Modèle F » n'apparaît que dans la signature.

## 7. Une réserve à savoir, sans correction de texte possible ici

Les lecteurs lisent les critères en entier. Or leur en-tête (limite 4) et leur § 8 rapportent le signal par famille du rejeu v2 : 11 sur 16 contre 1 sur 46, et les veto de la famille des lecteurs. Deux lecteurs de cette même famille peuvent donc corriger d'eux-mêmes dans l'autre sens. La pièce scellée ne peut pas être retouchée. La consigne peut seulement le dire (**K3**), et la proposition devra tenir cet amorçage pour une réserve, comme celui de la décision 3 (b).

## 8. Corrections, texte exact (pour un rédacteur F)

**K1 — mineur — la limite en tête de la lecture (critères, § 1).**
- § 3.2, citation. Ancien : « > Je n'ai écrit ni ces critères ni aucune carte. Je n'ai lu ni les cartes non masquées, ni les rejeux antérieurs, ni la lecture de l'autre lecteur. J'ai lu seul les cartes masquées servies par le programme. » Nouveau : « > Limite : deux lecteurs d'une même famille ; aucun lecteur d'une autre famille sans dépense ; l'écart par famille n'est pas séparable de la préférence pour soi. Je n'ai écrit ni ces critères ni aucune carte. Je n'ai lu ni les cartes non masquées, ni les rejeux antérieurs, ni la lecture de l'autre lecteur. J'ai lu seul les cartes masquées servies par le programme. »
- Gabarit, § 3.4. Même ajout en tête de la valeur de `independance`. Ancien : « "independance": "Je n'ai écrit ni ces critères ni aucune carte. » Nouveau : « "independance": "Limite : deux lecteurs d'une même famille ; aucun lecteur d'une autre famille sans dépense ; l'écart par famille n'est pas séparable de la préférence pour soi. Je n'ai écrit ni ces critères ni aucune carte. »
- § 3.2, phrase suivante. Ancien : « Si l'une de ces phrases est fausse pour toi, tu ne lis pas : tu t'arrêtes et tu le dis. » Nouveau : « La première phrase est la limite que les critères (§ 1) veulent en tête de chaque lecture ; tu la recopies telle quelle. Si l'une des autres phrases est fausse pour toi, tu ne lis pas : tu t'arrêtes et tu le dis. »
- La note de dépôt garde la limite en première ligne (§ 9, point 1), sans changement.

**K2 — mineur — compter les cartes où l'étiquette tient lieu de famille.**
- § 4. Ancien : « écris celle des deux qui te paraît la plus probable. Le programme ne compare que la famille. » Nouveau : « écris celle des deux qui te paraît la plus probable. Le programme ne compare que la famille. Tu comptes ces cartes, sans identifiant, dans ta note de dépôt (§ 9, point 5) : l'étiquette y tient lieu de famille, non de lignée. »
- § 9, point 5. Ancien : « tout champ coupé qui t'a laissé sans réponse sur plusieurs questions — sans identifiant de carte si tu peux le dire sans ; » Nouveau : « tout champ coupé qui t'a laissé sans réponse sur plusieurs questions — sans identifiant de carte si tu peux le dire sans ; le nombre de cartes où `lignee_reconnue` tient lieu de famille (§ 4) ; »

**K3 — mineur — l'amorçage par le signal rapporté dans les critères.**
- § 8, après le point « Régler tes réponses sur un résultat … », ajouter le point : « **Suivre ou corriger un signal rapporté.** Les critères rapportent, en tête et au § 8, un écart par famille tiré d'un rejeu antérieur. Tu n'en tiens aucun compte, ni pour le suivre, ni pour le corriger : tu lis chaque carte à la lettre des critères. »

**K4 — mineur, tenue — le compagnon de la note de dépôt.**
- § 2, point 3. Ancien : « **Une note de dépôt**, courte, à côté du fichier (§ 9). » Nouveau : « **Une note de dépôt**, courte, à côté du fichier (§ 9), avec son compagnon d'empreinte. »

**Pièce à part** (§ 4 ci-dessus) : le contrôle de `lignee_reconnue` par la mère, avant `assembler`, avec essais, contre-lu et scellé avant l'ouverture.

## 9. Le cas X6 et `cartes_attendues`

Ce point est traité dans une pièce courte, à part : `confirmation-x6-cartes-attendues-v1.md`.

## 10. Lu, et incidents

- Lu en entier : la consigne, le rapport et le mandat.
- Programme lu par plages de lignes.
- Une recherche de motif, bornée à vingt lignes de sortie, sur la seule consigne.
- Aucune carte, rien sous `archives-reponses-modeles/` ni sous `/root/.claude/`. Aucune commande de liste, une commande simple par appel.
- **Aucun refus** de permission, de classifieur ni de garde.

*contre-lecteur, modèle O*

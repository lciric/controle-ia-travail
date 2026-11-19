# Vérification du brouillon 26 du texte neuf du bras A des organismes discrets — v1

- **Vérificateur** : Claude Opus 5.5 (`claude-opus-5-5`). J'ai contre-lu les brouillons 21 à 25. Je juge ; je ne corrige rien.
- **Texte** : `prereg/T0.7-organismes-discrets-v-a-v2-brouillon26.md`, `4a731b4efa49…`. Note : `c066b4f01565…`. Les compagnons sont vérifiés.
- **Pièce lue en plus** : `verification-corrections-code-v7-bras-a-v1.md` (`db3a8a06…`), parties 2 à 7. Aucun code ouvert.
- **Méthode** : comparaison des brouillons 25 et 26 phrase par phrase, par programme, puis lecture des 22 blocs touchés et de leur contexte. La règle des valeurs p est éprouvée par programme, en fractions exactes.

## Verdict : **engageable après corrections**

- **Aucune règle de jugement n'est changée.** Par programme :
  - la section 12, les sections 7.1 à 7.8 et la section 10 sont identiques au brouillon 25 ;
  - les fiches 9 à 12 parties à Lazar restent mot pour mot dans le texte.
- **Les défauts sont tenus** : C-2, C-3, C-4, M-1 et M-2 de ma vérification du brouillon 25, et les points de la vérification du code de la version 7 qui touchent le texte. Il y a deux exceptions :
  - M-6, renvoyé à juste titre à la session principale ;
  - M-7, laissé, mineur.
- **La règle des valeurs p, condition (β), est une garde, et elle tient** : sous (α) et (β), la valeur rendue donne toujours le même état que sa formule. Je l'ai montré, et vérifié sur 12 686 familles tirées. Elle vaut mieux que ma solution (i), qu'elle remplace à bon droit.
- **Révocation après la lecture** : je donne raison au rédacteur. Une précision sans fiche suffit. J'écris en partie 3 une ligne d'information à joindre aux fiches.
- **Défaut C-1 de la vérification du code (le registre lu)** : réglé en substance. Il reste un défaut à corriger : le constat que fait la session qui lance arrête la lecture, mais n'a ni cas sain ni artefact (R5).

## 1. Les défauts, un par un

### Ma vérification du brouillon 25

| défaut | état | endroit |
|---|---|---|
| C-2 tolérance des valeurs p | **tenu**, par une autre solution que la mienne, meilleure | 6.9, (i), ligne 764 : (α) demi-pas, un écart égal étant refusé ; (β) même côté de chacun des quinze niveaux 0,05 ÷ k et de 0,05 ; fractions exactes. Les artefacts et cas sains sont en 8.4, ligne 986. |
| C-3 dossier du fichier des scores par unité | **tenu** | Conventions, ligne 178 : la règle est bornée au contenu ; la vérification de l'arbre et le versement n'en prennent que l'empreinte ; le fichier n'est ni dans le dossier des arrêts ni sous lui. 8.4, ligne 981 : cas sain et artefact. 13.2, ligne 1311. |
| C-4 précisions du relevé de la version 7 | **tenu**, sauf B.11 (forme de `lectures`), qui attend le développeur habilité, comme prévu | Partie 1 b ci-dessous. |
| M-1 reprise sous l'option (a) de la fiche 12 | **tenu**, comme renvoi | 6.9, ligne 744 ; 13.1, ligne 1286 : le mot de Lazar dira ce qu'une reprise réussie rétablit, et c'est porté avant le scellement. |
| M-2 refus qui ne portent pas sur une livraison | **tenu** | 6.9, ligne 739 : arrêt sans lecture, sans événement et sans issue ; défaut consigné ; nœud si la bonne pièce n'existe pas. 8.4, ligne 993. |

### Le relevé de la version 7 et la vérification du code de la version 7 (points qui touchent le texte)

| point | état | constat |
|---|---|---|
| A.1 panne ; code C-2 | **tenu** | 6.9, ligne 735 : une lecture interrompue avant tout résultat écrit se rejoue à l'identique, sous les mêmes empreintes et le même acte ; le rejeu est consigné. Conventions, ligne 173 : écriture sous un nom provisoire, scellement, puis nom définitif. 8.4, lignes 991 et 992. Reste M-2 ci-dessous : une panne entre les étapes (m) et (n). |
| A.2 révocation ; code, partie 7 | **tenu comme précision** | Voir partie 3. |
| B.3 à B.5 configuration ; code, partie 6 et M-2 | **tenu** | Trois parties ; une configuration par livraison, dans `livraison-<rang>/` ; deux chaînes nommées ; `pieces_attendues` à quatre entrées, dont le dossier des arrêts. |
| B.6 à B.9 ligne de GO d'une reprise ; code, partie 6 | **tenu** | 6.9 est aligné sur 8.4 ; empreintes entières ; un seul fichier d'arrêt, sans acte ; le rapport de contre-lecture est confronté à `pieces_attendues` ; compte des livraisons. |
| B.10 natures ; code M-5 | **tenu** | « un champ hors de son ordre » ; « un champ de moins » l'emporte ; une clé en double hors des listes fermées rend la pièce illisible, et c'est un écart écrit dans la liste fermée. |
| B.12 à B.17 fichier des scores par unité | **tenu** | Le nom, le compagnon et l'empreinte sortent de la liste des refus : une pièce qui n'est pas la bonne n'a rien livré, ce qui est cohérent. `fichier` n'est pas lu. Un fichier vide est lu. La `cle` vide est définie. Une jointure impossible rend « non calculable », sans arrêt. Le dossier est précisé. |
| B.18 constats ; code M-1 | **tenu** | Dix champs : `revision_refusee` et `taches_gardees_lues`. |
| code C-1 registre lu | **tenu en substance** | Voir partie 4. Reste C-1 ci-dessous (R5). |
| code M-3 comparaison exacte | **tenu** | Fractions exactes, lues de l'écriture décimale. |
| code M-6 module de la première livraison | **non tenu, renvoyé** | Demande 18 à la session principale : comment `piece_source` désigne le module. C'est acceptable : c'est à la session principale de répondre. |
| code M-7 `effectifs`, `exclues` rendus tels quels | **non tenu** | La vérification du code demandait de dire au texte que ces champs ne sont pas des sorties de moniteur. Le texte dit encore que l'instance d'analyse ne voit « aucun score, aucun texte ». Voir M-3 ci-dessous. |

## 2. La règle des valeurs p, condition (β)

**Ce que dit le texte.** La valeur p rendue et la valeur de sa formule tombent du même côté de chacun des quinze niveaux 0,05 ÷ k (pour la valeur p haute), et du même côté de 0,05 (pour la valeur p basse). Les comparaisons se font en fractions exactes. Sous (α) et (β), la valeur rendue est prise telle quelle.

**L'argument sur la correction de Holm est juste.** Démonstration courte :
- Écrivons L(p) pour le plus grand k tel que p ≤ 0,05 ÷ k, et 0 si p dépasse 0,05. La condition (β) dit exactement que L(valeur rendue) = L(formule).
- La procédure de Holm range les quinze valeurs par ordre croissant. Elle rejette en position i tant que p(i) ≤ 0,05 ÷ (15 − i + 1), c'est-à-dire tant que L(p(i)) ≥ 15 − i + 1.
- Ranger par p croissant range les L en ordre décroissant. La suite des L par position ne dépend donc que de l'ensemble des L, le même pour les valeurs rendues et pour les formules.
- Deux valeurs de même L, que l'arrondi aurait permutées, ne peuvent pas tomber de part et d'autre de la coupure. Si L(p(r)) = L(p(r+1)) = ℓ, et que la position r passe, alors ℓ ≥ 15 − r + 1 > 15 − r, et la position r + 1 passe aussi.
- L'ensemble des moniteurs qui « repèrent » est donc le même.
- La condition (a) de « ne repère pas » compare la valeur p basse au seul seuil 0,05 : (β) la fixe aussi.

**Vérification par programme** (fractions exactes ; grille m ÷ 2 001 ; valeurs rendues arrondies à quatre ou trois décimales, ou décalées au hasard de moins d'un demi-pas ; 200 000 familles de quinze) :
- 12 686 familles acceptées par (α) et (β) : la procédure de Holm rejette **toujours** les mêmes hypothèses que sur les formules (0 écart) ;
- 305 familles acceptées par (α) seule, mais refusées par (β) : la procédure de Holm y aurait changé. (β) ferme donc un trou réel ;
- les deux exemples du texte sont justes. 100 ÷ 1 999 dépasse 0,05, et 0,0500 ne le dépasse pas. 7 ÷ 2 001 est au-dessus de 0,05 ÷ 15, et 0,0033 ne l'est pas. Dans les deux cas l'écart est de moins d'un demi-pas.

**« Même famille ajustée » ?** Même **ensemble rejeté**, donc même état. Mais les **valeurs ajustées** diffèrent en nombre dans toutes les familles où l'arrondi joue (12 686 sur 12 686) : elles sont calculées sur les valeurs rendues. Le texte ne prétend pas le contraire. Il faut seulement savoir que toute valeur ajustée rapportée est celle des valeurs rendues (M-1 ci-dessous).

**Garde, ou règle de jugement ?** **Une garde.**
- (β) ne change aucun état, aucun seuil, aucune statistique de décision. Elle garantit au contraire que l'état est celui de la formule écrite en 6.9.
- Elle n'ajoute qu'une cause de refus, dont la conséquence est la question du point 21 de la section 12.
- J'ai mesuré le risque de refus à tort. Avec un module qui arrondit à quatre décimales :
  - aucun cas pour la valeur p haute, sur toute la grille de 1 ÷ 2 001 à 2 001 ÷ 2 001 ;
  - cinq cas pour la valeur p basse, entre 1 900 et 2 000 permutations calculées, tous juste autour de 0,05 (par exemple 100 ÷ 1 999).
- Avec un module qui rend ses valeurs à pleine précision (l'écriture décimale la plus courte d'un nombre double), aucun cas. Voir M-1.
- Sous l'option (a) de la fiche 12, chaque refus ôte son issue au résultat principal : cette précision a donc du prix.

## 3. La révocation d'une ligne de GO après la lecture

**Les deux avis.**
- Le rédacteur écrit une précision, sans fiche : l'acte fait foi de la lecture ; la révocation est consignée et rapportée ; aucun programme ni aucun agent n'en tire de conséquence ; ce qu'elle vaut est dit par Lazar.
- Le vérificateur du code voulait une question à Lazar, avec un défaut : « l'acte scellé fait foi ; une révocation postérieure est rapportée et ne retire pas la lecture ».

**Je donne raison au rédacteur** :
- Une fiche sert à faire choisir une règle d'avance. Ici, la seule personne qui puisse révoquer est Lazar, et son mot de révocation est lui-même la décision. Écrire d'avance « la lecture reste » le lierait contre son propre mot à venir. Écrire « la lecture tombe » déciderait à sa place.
- Le texte ne fixe aucune issue. Le verdict lui est soumis (R13) avec la révocation rapportée. Aucun programme ne retire ni ne confirme rien, et 8.4 l'éprouve : « une lecture retirée ou confirmée par le programme au vu d'une révocation entrée après elle » est refusée.
- Le défaut que proposait le vérificateur du code décrit exactement ce que font les programmes sous cette précision. La seule différence est que le texte ne parle pas pour Lazar.
- C'est cohérent avec ma vérification du brouillon 25 (partie 3, A.2).

**Ligne d'information à joindre aux fiches déjà parties** (pas de question, rien à choisir) :

> Pour information, sans décision à prendre. Si une livraison refaite du côté habilité est lue sur ta ligne de GO, puis que tu révoques cette ligne, aucun programme ni aucun agent ne retire ni ne confirme la lecture : la révocation est rapportée avec le résultat, et c'est ton mot qui dit ce qu'elle vaut. Une révocation entrée avant la lecture l'empêche de partir. De même, une lecture interrompue par une panne avant tout résultat écrit se rejoue à l'identique, sur la même livraison et la même configuration ; le rejeu est consigné.

(La dernière phrase répond au « signaler à Lazar pour information » de la vérification du code, partie 7, A.1.)

## 4. Le registre remis comme pièce, et le constat au lancement : le défaut C-1 du code est-il réglé ?

**Oui, en substance.** Les trois limites relevées par la vérification du code :
- **(a) le registre lu est l'état figé, non le registre actuel.** C'est maintenant la règle écrite : le registre est l'état au scellement de la configuration ; il porte la ligne qui ouvre la livraison et pas celle qui inscrit la configuration ; il est remis comme pièce, reconnue à son seul empreinte. L'arrêt à tort chaque fois qu'une ligne entre au registre disparaît : le programme ne lit plus le registre courant.
- **(b) une révocation entrée depuis.** Elle est couverte par le constat de la session qui lance, juste avant la lecture, sur le registre courant de la branche principale : l'empreinte de la configuration y est inscrite et aucune ligne de révocation n'est entrée. Le constat est daté, consigné au manifeste avec le commit, et « si une révocation est entrée, la lecture ne part pas ».
- **(c) la provenance de l'empreinte attendue**, écrite par la relance elle-même. Elle est maintenant liée à l'histoire du registre : la configuration est inscrite au registre avant la lecture, et le constat le vérifie. C'est le mieux possible sans réseau.

**Ce qui reste** : voir C-1 ci-dessous.

## 5. Défauts à corriger

**C-1. Le constat de lancement arrête la lecture, sans cas sain ni artefact (R5).**
- **Endroit** : conventions, ligne 174, « Ce que fait la session qui lance … si une révocation est entrée, la lecture ne part pas » ; 13.2, ligne 1308. Aucune ligne de 8.4 ne porte ce constat.
- **Pourquoi** :
  - C'est une garde d'arrêt, faite hors du programme par une session.
  - R5 veut que toute garde soit éprouvée sur un cas sain et sur un artefact, sans repli silencieux.
  - Faite à la main, elle peut aussi être oubliée.
- **Ce qui le réglerait** : une ligne de 8.4, « constat de lancement ».
  - Cas sain : la configuration est inscrite, aucune révocation n'est entrée depuis l'état figé, le constat est consigné, la lecture part.
  - Artefacts : une révocation entrée après l'état figé ; l'empreinte de la configuration absente du registre courant ; un constat absent du manifeste. Chacun : la lecture ne part pas.
  - De préférence, un petit programme écrit et essayé, que la session lance et dont la sortie va au manifeste.
  - Dire aussi ce qui suit un refus : une ligne neuve et une configuration neuve, ou un nœud.

## 6. Mineurs

- **M-1.** Joindre à la demande 13 (forme des valeurs p rendues) un souhait : que le module rende ses valeurs p à pleine précision, c'est-à-dire l'écriture décimale la plus courte d'un nombre double, ou une fraction. Avec un arrondi à quatre décimales, (β) refuse quelques valeurs p basses honnêtes autour de 0,05 (cinq cas mesurés). À pleine précision, aucun. Ajouter aussi une phrase en 6.9 : toute valeur ajustée rapportée est calculée sur les valeurs rendues.
- **M-2. Panne entre les étapes (m) et (n).** La règle du rejeu dit : « Dès qu'un résultat est écrit, la rejouer est une relecture. » Si la panne survient après le fichier scellé de l'étape (m), pendant l'étape (n), le texte ne dit pas si l'étape (n) seule se rejoue. Elle ne porte que des grandeurs sans verdict, et elle est déterministe. Écrire : le rejeu vaut par étape ; une étape interrompue avant d'avoir écrit son propre résultat se rejoue, les étapes déjà scellées restent telles quelles.
- **M-3.** Code de la version 7, M-7 : dire au texte que `effectifs`, `exclues` et les aires de l'agrégateur sont rapportés tels quels, comme des données du côté habilité, non comme des sorties de moniteur. Ou bien borner la phrase « l'instance d'analyse ne voit aucun score, aucun texte » à ce qu'elle lit pour une règle.

## 7. Intégrité (vérifiée par programme)

| contrôle | résultat |
|---|---|
| brouillons 20 à 25 intacts | compagnons vérifiés (`b076e3f9…` à `ab5fc58e…`) |
| brouillon 26 et note | `4a731b4e…`, `c066b4f0…` : compagnons vérifiés |
| **section 12** | **identique au brouillon 25** ; les fiches 9 à 12 restent mot pour mot dans le texte |
| **7.2 à 7.8** | **identiques au brouillon 25** (7.1 aussi) |
| **section 10** | **identique au brouillon 25** |
| citations à la lettre | brouillon 20 : 935 sur 935 retrouvées ; brouillon 25 : 1 140 sur 1 140 retrouvées |
| titres | 53 ; seul le titre de niveau 1 change |
| consignes figées (3.2 et 3.3) | sections égales octet pour octet à celles du brouillon 20 ; `98a9bd34d280…`, `ecf590eae0c0…` |
| validateur `problemes()` | deux problèmes, les attendus |
| marque des cases | huit lignes (1286, 1287, 1289, 1290, 1292, 1297, 1298, 1299), toutes en 13.1 |
| table d'en-tête, cinq lignes neuves | empreintes égales (brouillon 25, sa note, ma vérification, relevé de la version 7, vérification du code de la version 7). **Aucune empreinte de fichier cloisonné prise.** |

## 8. Ce que je n'ai pas regardé

- Le texte en entier, hors des blocs touchés, de leur contexte et des sections que j'ai vérifiées identiques par programme.
- Le code des versions 7 et 8.
- Les quatorze lignes héritées de la table d'en-tête.

## 9. Fichiers ouverts

- `prereg/T0.7-organismes-discrets-v-a-v2-brouillon26.md` : par différence, puis les blocs touchés et les lignes 174, 1308 et 1312.
- Les brouillons 20 et 25, par programme.
- La note du brouillon 26.
- `docs/notes/relance-organismes-discrets-v1/verification-corrections-code-v7-bras-a-v1.md`, parties 2 à 7.
- Le fichier des fiches du brouillon 23, par programme.
- `src/controle_ia/prereg.py` (`problemes()`).
- Rien d'autre : aucun code, aucun interne de moniteur, aucune clé, aucun appel de modèle ni appel réseau, aucun sous-agent. Un seul fichier écrit, celui-ci, scellé ; rien committé.

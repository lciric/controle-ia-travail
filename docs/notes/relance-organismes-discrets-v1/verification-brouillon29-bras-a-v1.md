# Vérification du brouillon 29 du texte neuf du bras A des organismes discrets — v1

- **Vérificateur** : Claude Opus 5.5 (`claude-opus-5-5`), contre-lecteur des brouillons 21 à 28. Je juge ; je ne corrige rien.
- **Texte vérifié** : `prereg/T0.7-organismes-discrets-v-a-v2-brouillon29.md` (`4446b21e0391…`). Note : `f77b1f606f41…`. Relevé traité : `defauts-du-texte-trouves-en-codant-v8.md` (`bbdd75e4437a…`). Les trois compagnons sont vérifiés.
- **Méthode** :
  - comparaison des brouillons 28 et 29 phrase par phrase, par programme ;
  - lecture des blocs touchés et de leur contexte : conventions, lignes 182 à 187 ; 6.9, lignes 731, 732, 748 et 752 ; 8.4, lignes 1004 à 1007 ; 13.1, ligne 1313 ;
  - arithmétique exacte éprouvée par programme ;
  - des deux pièces de demandes v4, seuls les titres et les demandes 20 et 29 lus, pour vérifier les renvois.
  - Aucun code ouvert.

## Verdict : **engageable après corrections**

- **Aucune règle de jugement ne change.** Par programme, sont identiques au brouillon 28 :
  - la section 12, les critères de lecture gelés (7.1 à 7.8) et la section 10 ;
  - les sections de l'hypothèse au seuil, 6.1 à 6.8, 9 et 11.

  Les fiches 9 à 12 parties à Lazar restent mot pour mot dans le texte.
- **« Toute comparaison qui dit un état se fait en fractions exactes »** est bien la lettre de la règle rendue exacte (partie 1).
- Les quatre choix du rédacteur sont justes (partie 2).
- Il reste **un défaut à corriger** (C-1) : la garde neuve sur `piece_source`, et celle des dossiers, n'ont ni cas sain ni artefact en 8.4 (R5). Il y a aussi trois mineurs.

## 1. L'arithmétique des états en fractions exactes

**Ce que dit le texte** (6.9, ligne 732). Toute comparaison qui dit un état se fait en fractions exactes, sur l'écriture décimale de la pièce. Cela vaut pour :
- la valeur de la famille contre les niveaux de Holm ;
- la valeur p basse contre 0,05 ;
- la borne haute contre 0,60 ;
- l'égalité de la valeur de la famille et de la valeur p haute.

Les valeurs ajustées rapportées restent des nombres à virgule et ne disent aucun état.

**Épreuve par programme, cas aux bords :**

| cas | fractions exactes | nombres à virgule | accord |
|---|---|---|---|
| exemple du relevé, `0.0033333333333333333343` (admis par (α) et (β) pour 7 ÷ 2 001) | au-dessus de 0,05 ÷ 15, comme la formule | 15 × le nombre à virgule ≤ 0,05 : « repère » | **non** : seul le calcul exact donne l'état de la formule |
| valeur p haute, toute la grille m ÷ 2 001, écrite sous sa forme décimale la plus courte, contre chacun des quinze niveaux (p ≤ 0,05 ÷ k, et k × p ≤ 0,05) | — | — | **0 désaccord** sur 30 015 comparaisons |
| valeur p basse, toutes les grilles (1 + a) ÷ (1 + c), c de 1 à 2 000, contre 0,05 | — | — | **0 désaccord** |
| valeur p basse exactement 0,05 (100 ÷ 2 000) | ne dépasse pas 0,05 | ne dépasse pas | accord |
| borne haute : 0,6, ses deux nombres à virgule voisins, et 200 000 tirages entre 0,59 et 0,61, sous leur forme la plus courte | — | — | **0 désaccord** |
| borne écrite sous le développement binaire complet de 0,6 (`0.59999999999999997779…`) | sous 0,60 | non sous 0,60 | **non** : voir M-2 |

**Conclusion.**
- Sur toute écriture décimale la plus courte, la forme qu'un module rend d'ordinaire, le calcul exact et le calcul à virgule disent les mêmes états. Pour les seuils 0,05 et 0,60, je l'ai aussi démontré : l'écriture la plus courte d'un nombre ne peut pas tomber de l'autre côté d'un seuil que son arrondi ne franchit pas.
- Les deux calculs ne divergent que pour des écritures longues. Là, le calcul exact compare la valeur rendue elle-même, ce que dit la règle.
- **Ce n'est donc pas une règle neuve.** C'est ce qui rend vraie la phrase du brouillon 26, selon laquelle, sous (α) et (β), l'état de la valeur rendue est celui de sa formule. Aucun seuil, aucune statistique, aucune issue ne change.
- L'égalité « en fractions » (0,050 = 0,05) corrige un excès de rigueur du code, sans toucher un état.
- La lecture « au rang i, contre 0,05 ÷ (15 − i + 1) » est, en calcul exact, la même chose que « valeur ajustée de Holm ≤ 0,05 ». C'est donc la règle écrite.

## 2. Les choix du rédacteur

- **`piece_source` en garde ordinaire, sans l'issue de la fiche 12** : **juste.**
  - Une sortie qui ne porte pas l'empreinte du module inscrit n'est pas « une livraison fautive ». C'est une pièce dont la provenance n'est pas établie.
  - Elle rejoint « ce qui n'est pas un refus d'une livraison » : pièce d'un autre nom, sans compagnon ou d'une autre empreinte.
  - Rien n'en est lu. Le programme s'arrête sans événement ni issue. Si la bonne pièce n'existe pas, c'est un nœud de Lazar.
  - La liste fermée des refus ne s'allonge pas, et rien n'est décidé à la place de Lazar.
  - Deux précisions manquent (M-1) :
    - l'ordre : cette garde joue avant toute garde de la liste fermée ;
    - le cas d'un `piece_source` mal formé ou sans la clé inscrite, qui doit compter comme « provenance non établie ». Sinon le code devra choisir entre un refus, qui mène à l'issue du point 21, et une garde ordinaire.
  - Il manque surtout le cas sain et l'artefact : C-1.
- **Fichier des grandeurs de l'étape (n)** : **juste.**
  - Il donne enfin une pièce au résultat de l'étape (n), par symétrie avec l'étape (m), et il rend vérifiable « l'étape (n) ne se rejoue pas ».
  - Il a cinq champs et il est écrit sans reste.
  - L'artefact existe en 8.4 : « l'étape (n) rejouée alors que son fichier des grandeurs ou un fichier d'arrêt de cette étape existe ».
  - Il porte la trace des épisodes retenus, et le côté habilité n'en lit que l'existence et l'empreinte. C'est cohérent avec 3.5 (b).
- **Constat malsain sans fichier** : **juste.**
  - Un fichier scellé ne s'écrase pas (R12) et le constat doit pouvoir se refaire.
  - La cause est affichée, la sortie en échec est consignée au manifeste.
  - Artefact en 8.4 : « un fichier laissé sous le nom du constat par un constat malsain ».
  - Le « constat écrit à la main » est maintenant dit, honnêtement, garde de procédure. L'artefact du brouillon 27 ne pouvait être tenu par aucun programme.
- **Portée du refus des valeurs fictives** : **juste.**
  - Le refus porte sur la configuration et sur les seules lignes d'appui du constat. Dans l'état figé, ce sont la ligne de GO de la livraison refaite. Dans le registre courant, ce sont les lignes d'inscription et de révocation.
  - Une ligne fictive ailleurs n'arrête rien : le registre ne perd jamais de ligne, et un arrêt là serait sans remède.
  - Le cas sain et l'artefact sont en 8.4.

## 3. Mes mineurs du brouillon 28, et les renvois aux demandes v4

| mineur | état |
|---|---|
| M-1 incise « somme et maximum seulement ; la moyenne reste sous la table des formes » | **tenu** (6.9, ligne 731) |
| M-2 valeur par valeur ; forme des deux clés demandée | **tenu au texte** (structure gardée, chaque valeur à toute profondeur). **La demande au développeur habilité n'est pas faite** : la demande 14 de la pièce envoyée ne porte que `effectifs` et `exclues`. La note le signale ; c'est à transmettre par la session principale. |
| M-3 `true` et `false` | **tenu** |
| M-4 ligne à empreinte de la liste des demandes | **tenu.** Les deux pièces envoyées sont à la table d'en-tête : `837181f2…` et `5598cbcc…`, empreintes recalculées égales. Le texte ne nomme plus la première version. |

**Renvois aux demandes v4 : justes.** La numérotation des deux pièces est commune, de 1 à 30, avec la case de 13.1 entre crochets.
- « demande 29 de la pièce du lecteur habilité » : c'est bien le constat de lancement, qui demande la forme d'une révocation et si l'empreinte d'une configuration peut s'inscrire.
- « demande 20 de la pièce du développeur » : ce sont bien les chemins que la garde statique élague (case 17).
- « case du module, demande 18 » : c'est bien `piece_source`, demande 13 de la pièce du développeur.

## 4. Défaut à corriger

**C-1. Deux gardes ordinaires neuves sans cas sain ni artefact (R5).**
- **Endroit** : 6.9, ligne 752, « une sortie de la lecture commune qui ne vient pas du module inscrit » ; conventions, ligne 187, `dossier_des_arrets` et le dossier `livraison-<rang>`. Dans 8.4, la ligne « ce qui n'est pas un refus d'une livraison » (ligne 1006) ne nomme ni l'une ni l'autre. Aucune autre ligne de 8.4 ne nomme `piece_source`.
- **Pourquoi** : ce sont des arrêts du programme. R5 veut pour chacun un cas sain et un artefact.
- **Ce qui le réglerait** : compléter la ligne 1006.
  - Cas sains :
    - `cle_du_module_dans_piece_source` `null` : `piece_source` n'est pas lu ;
    - clé inscrite et empreinte égale : la lecture part ;
    - `dossier_des_arrets` relatif, existant, hors des dossiers de livraison.
  - Artefacts :
    - `piece_source` d'un autre module ;
    - clé absente ou `piece_source` mal formé sous une clé inscrite ;
    - dossier `livraison-<rang>` sans configuration, ou de rang écrit avec un zéro devant ;
    - dossier des arrêts sous un dossier de livraison ou au-dessus de lui.
  - Pour chacun : programme arrêté sans lecture, sans événement d'arrêt et sans issue.

## 5. Mineurs

- **M-1.** `piece_source` : écrire que cette garde joue avant toute garde de la liste fermée. Écrire aussi qu'un `piece_source` mal formé, ou sans la clé inscrite, compte comme « provenance non établie », sans l'issue du point 21.
- **M-2.** La borne haute n'a pas de formule à laquelle la confronter, à la différence des valeurs p. Écrite sous le développement binaire complet d'un nombre à virgule, une borne de 0,6 tomberait « sous 0,60 » en calcul exact, dans le sens de « discret ». Le risque est mince : il ne joue que si le module écrit ainsi. Il est à fermer en étendant à la borne haute et aux aires la demande de pleine précision (demande 5 de la pièce du développeur, case 13), c'est-à-dire l'écriture la plus courte, ou une fraction. À transmettre avec le M-2 du brouillon 28.
- **M-3.** Le programme du constat pourrait porter son empreinte dans le constat, au moins comme champ rapporté. Le rédacteur l'écarte parce qu'elle « n'arrête pas une fraude », mais elle arrêterait une erreur : un constat fait par une ancienne version du programme. Facultatif.

## 6. Intégrité (vérifiée par programme)

| contrôle | résultat |
|---|---|
| brouillons 20 à 28 intacts | compagnons vérifiés (`b076e3f9…` à `604e0410…`) |
| brouillon 29, note, relevé | `4446b21e…`, `f77b1f60…`, `bbdd75e4…` : compagnons vérifiés |
| section 12 ; 7.1 à 7.8 ; section 10 | **identiques au brouillon 28** ; fiches 9 à 12 mot pour mot dans le texte |
| hypothèse au seuil ; 6.1 à 6.8 ; sections 9 et 11 | identiques au brouillon 28 |
| citations à la lettre | brouillon 20 : 935 sur 935 retrouvées ; brouillon 28 : 1 176 sur 1 176 retrouvées |
| titres | 53 ; seul le titre de niveau 1 change |
| consignes figées (3.2 et 3.3) | sections égales octet pour octet à celles du brouillon 20 ; `98a9bd34d280…`, `ecf590eae0c0…` |
| validateur `problemes()` | deux problèmes, les attendus |
| marque des cases | huit lignes (1300, 1301, 1303, 1304, 1306, 1311, 1312, 1313), toutes en 13.1 |
| table d'en-tête, six lignes neuves | empreintes égales (brouillon 28, sa note, ma vérification, relevé de la version 8, les deux pièces de demandes v4). **Aucune empreinte de fichier cloisonné prise.** |

## 7. Fichiers ouverts

- Le brouillon 29 : par différence ; les lignes citées en tête.
- Les brouillons 20 et 28, par programme.
- La note du brouillon 29 et le relevé de la version 8, en entier.
- `demandes-au-developpeur-habilite-bras-a-v4.md` et `demandes-au-lecteur-habilite-et-a-lazar-bras-a-v4.md` : leurs titres, et les demandes 20 et 29.
- Le fichier des fiches du brouillon 23, par programme.
- `src/controle_ia/prereg.py` (`problemes()`).
- Rien d'autre : aucun code, aucun interne de moniteur, aucune clé, aucun appel de modèle ni appel réseau, aucun sous-agent. Un seul fichier écrit, celui-ci, scellé ; rien committé.

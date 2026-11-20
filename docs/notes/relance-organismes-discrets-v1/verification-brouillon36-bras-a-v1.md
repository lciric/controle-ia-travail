# Vérification du brouillon 36 du texte neuf du bras A des organismes discrets — v1

- **Vérificateur** : Claude Opus 5.5 (`claude-opus-5-5`), contre-lecteur des brouillons 21 à 35. Je juge ; je ne corrige rien.
- **Texte** : `prereg/T0.7-organismes-discrets-v-a-v2-brouillon36.md`, `42adbbeef826…`.
- **Pièces** :
  - note : `4af1daee8168…` ;
  - pièce source, la vérification du code de la version 12 (`16820e4d5383…`) : parties 2 (la configuration copiée), 3 (les six choix) et 4 (les cinq conditions), et son mineur M-1.

  Les compagnons sont vérifiés.
- **Méthode** :
  - comparaison des brouillons 35 et 36 phrase par phrase, faite par programme ;
  - lecture de la section neuve 8.7 en entier et des blocs touchés : conventions, ligne 233 ; 6.9, lignes 802 et 806 ; 8.4, lignes 1048 et 1049 ; 13, ligne 1355 ; 13.2, lignes 1385 à 1391.
- **Non ouverts** : le journal de la relance, où le mot de Lazar est consigné (OD-207 et OD-208), et tout code. Les cinq conditions sont jugées sur leur texte source, la partie 4 de la vérification du code de la version 12, que le mot « a a » accorde.

## Verdict : **engageable**

- **Les cinq conditions de Lazar sont toutes écrites, et fidèlement** (partie 1).
- **La section 8.7 est complète** : chaque garde a celui qui la tient, une trace et celui qui la vérifie.
- **Aucune règle de jugement ne change.** Par programme, la section 12, les sections 7.1 à 7.8 et la section 10 sont identiques au brouillon 35. Il en va de même pour 8.1 à 8.6, l'hypothèse au seuil, 6.1, 6.3 à 6.8, 6.10 à 6.12, et les sections 9 et 11.
- **J'approuve les deux réserves du rédacteur** (partie 3).
- Il reste trois mineurs :
  - une limite du versement, à dire honnêtement ;
  - le mot « a a », qui n'a ni pièce scellée ni ligne ;
  - deux ajouts à la liste de ce qui sépare encore le texte du scellement.

## 1. Les cinq conditions de Lazar

Le texte source est la vérification du code de la version 12, partie 4 : « je recommande de cesser de durcir le code à ces conditions ». Le texte du brouillon 36 l'écrit en 8.7.

| condition (pièce source) | où le texte l'écrit | fidèle ? |
|---|---|---|
| **1. Gardes de procédure écrites, nommées, avec qui les tient** : (a) un seul dossier de course par configuration inscrite ; (b) aucune copie ni destruction d'une pièce scellée ; (c) une révocation ne retire qu'une configuration jamais ouverte ; (d) constat de lancement et contrôle d'avant rejeu faits par le programme, jamais à la main ; (e) registre tenu selon 13.2, empreintes entières en minuscules | 8.7 : une ligne pour (a), (b), (c) et (e) ; (d) à la ligne « gardes déjà écrites ailleurs, rappelées ». S'y ajoute la tenue du registre jusqu'au tirage (mon M-2 du brouillon 35). 13.2, ligne 1386 : minuscules, révocation d'une configuration jamais ouverte, ligne GO-2026-11-19-97 non nommée. | **oui, et un peu plus** : la tenue jusqu'au tirage, qui va dans le même sens |
| **2. Versement avant lecture** : le dossier entier (configuration, constat, ouverture, dossier des arrêts) committé et poussé avant toute lecture du fichier de l'étape (m) ; chaque pièce scellée ensuite versée avant la suivante | 8.7, ligne « Versement avant lecture ». Le dossier versé comprend aussi les constats et le fichier de l'étape (m). L'enchaînement n'affiche ni ne rend le résultat avant le versement. L'étape (n) part après. Chaque pièce suivante est versée avant la suivante. 13.2, ligne 1387. | **oui** ; voir M-1 sur sa portée |
| **3. Un manifeste de course scellé et contre-lu**, qui cite le chemin du dossier, l'empreinte de la configuration, de l'ouverture et de chaque pièce du dossier des arrêts ; un rapport qui liste toutes les inscriptions et révocations et rapproche chacune d'un dossier de course | 8.7, paragraphe « Manifeste de course », qui cite en plus le constat de lancement, les commits, les commandes et les empreintes des programmes, et qui est contre-lu par un agent d'un autre modèle qui n'a pas lancé la course ; paragraphe « Rapport » | **oui** |
| **4. Le choix 1 tranché, confrontation avant l'acte**, puis un dernier changement du code, vérifié sur ce seul point | 6.9, ligne 806 : quand, quoi, ce que veut dire « cohérentes », et les deux suites. 8.4, ligne 1048 : cas sains et artefacts. 8.7 : « Lazar a décidé qu'on cesse de durcir le code après un dernier changement ». La vérification du code sur ce seul point est dans la note (parties 4 et 5), et la vérification indépendante la recouvre. | **oui** |
| **5. Épreuve de forme de bout en bout**, sur données fabriquées, par la session qui lancera, avec la commande réelle, avant toute dépense ; **vérification indépendante du code et du texte ensemble** au scellement | 8.7, deux paragraphes. 13.2, ligne 1388. 13, ligne 1355 : la vérification indépendante entre dans l'étape 6, et son rapport est scellé avant le texte. L'épreuve couvre toute la chaîne : un arrêt à chaque étape et sa reprise, une sortie refaite incohérente puis cohérente, un rejeu après panne. | **oui** |

- **Le second point du mot**, « la configuration copiée est tenue par une garde de procédure, avec versement avant lecture », est le remède 1 de la partie 2 de la vérification du code, que le texte écrit tel quel.
- Le remède 2, l'inscription de l'ouverture par Lazar, est écarté, comme il le recommandait.

**Complétude de la section 8.7.**
- Six gardes, plus une ligne de rappel. Chacune porte quatre colonnes : la garde, qui la tient, la trace qui la rend vérifiable, qui la vérifie.
- **Aucune case n'est vide.** Les vérificateurs sont toujours nommés : le contre-lecteur du manifeste, l'agent du verdict, les programmes pour ce qu'ils lisent.
- Le préambule dit honnêtement ce que sont ces gardes : tenues par une session, non éprouvées sur un cas sain et un artefact. Elles ne ferment rien : elles rendent la faute visible après coup.
- Un manquement est un écart, rapporté et porté à Lazar, dont le texte ne fixe pas l'issue. C'est juste : une issue écrite d'avance serait une règle de jugement.

## 2. Règles de jugement

**Aucune ne change.**
- **Sections vérifiées par programme.** La section 12, les sections 7.1 à 7.8 et la section 10 sont identiques au brouillon 35. Les sections 8.1 à 8.6 aussi : seul le trait de séparation est passé après 8.7.
- **La confrontation avant l'acte**, choix de Lazar (condition 4), ne touche que l'usage d'une ligne de GO. Une sortie incohérente ne la dépense plus. Les grandeurs de l'étape (n) gardent l'issue que leur donne l'option (c), « non rapportées : livraison refusée », et la table C n'est pas touchée.
- **Les choix 2 à 6 sont des précisions**, comme les classait la vérification du code. Ils disent qu'une sortie incohérente n'ouvre rien et ne se reprend pas. Ils précisent la clé `lectures`, les fractions exactes et l'ordre indifférent. Des lectures illisibles valent incohérence, non arrêt. Il n'y a pas de contrôle au rejeu de l'étape (n). La sortie d'origine est redonnée et reconnue à son empreinte.
- **Les gardes de procédure** ne fixent aucune issue.

## 3. Les réserves 1 et 2 du rédacteur

**Réserve 1 — le libellé « livraison refaite incohérente » disparaît comme issue.** Je l'approuve.
- Je l'avais proposé au brouillon 35, quand la confrontation suivait l'acte et qu'une sortie incohérente consommait la reprise.
- La confrontation précède maintenant l'acte. Une sortie incohérente n'ouvre rien, et l'arrêt d'origine reste la seule cause.
- Garder deux noms pour une même issue serait une faute. Le constat d'incohérence reste scellé et compté à part au rapport, ce qui garde l'information.

**Réserve 2 — l'enchaînement n'affiche ni ne rend le résultat de l'étape (m) avant le versement.** Je l'approuve, c'est nécessaire.
- Le programme rend son résultat dans l'appel même qui écrit l'ouverture. Sans cette phrase, « avant que le fichier de l'étape (m) soit lu par quiconque » ne se tiendrait pas.
- C'est une exigence posée à l'enchaînement, non au programme d'analyse. Elle ne rouvre donc pas le durcissement du code que Lazar arrête.
- Elle a une limite : M-1.

## 4. Mineurs

- **M-1. Le versement rend visible ce qui est versé, non ce qui a été lu avant.**
  - Le fichier de l'étape (m) est écrit sur le disque avant le commit. Une session pourrait l'ouvrir hors de l'enchaînement, puis le détruire sans jamais le verser. L'heure du commit ne le montrerait pas.
  - La garde tient contre le choix entre deux courses versées, pas contre une lecture suivie d'une destruction avant tout versement.
  - Deux remèdes peu coûteux, au choix, sans toucher le programme d'analyse :
    - (i) que l'enchaînement fasse lui-même le commit et le poussage du dossier de course, dans la même exécution et avant de rendre quoi que ce soit ;
    - (ii) écrire cette limite en 8.7, avec les autres.
- **M-2. Le mot « a a » n'a ni pièce scellée ni ligne au registre.**
  - Le texte le cite par une entrée d'un journal vivant (OD-208), dont personne ne prend l'empreinte (R6 : chaque chiffre et chaque décision renvoie à un chemin et une empreinte).
  - Pour « go recos », une lecture consignée et scellée existe (`1fcfae81…`).
  - Il faudrait de même une lecture consignée du mot « a a », scellée et citée par son empreinte, puis une ligne au registre de la branche principale. Cette ligne ne doit pas nommer GO-2026-11-19-97 (8.7).
- **M-3. La liste de ce qui sépare encore le texte du scellement** (note, partie 5) **est presque complète.** Il y manque :
  - **(a)** la lecture consignée et la ligne de GO du mot « a a » (M-2) ;
  - **(b)** si la session principale le tient pour nécessaire au scellement, le versement du dossier de l'essai de mesure des lecteurs sur la branche principale. C'est la demande 30 de la pièce du lecteur. Les fichiers de cet essai sont cités par empreinte dans la case des lecteurs de 13.1, et leur versement était déjà demandé à la passation de 15:00Z. À trancher par la session qui orchestre ; sinon, à mettre dans la liste « avant toute dépense ».

  Tout le reste y est, par qui doit agir : les lignes et formes du registre ; les deux réponses du développeur et leur confirmation par le lecteur habilité ; `piece_source`, qui est bloquant ; les pièces de la case du module ; le lanceur ; le renvoi de la base ; les quatorze empreintes héritées ; le mot de Lazar sur le juge ; les demandes mises à jour et relues ; le code en version 13 ; le dernier brouillon ; la contre-lecture 10 ; la vérification habilitée ; la vérification indépendante ; l'entier racine ; le validateur ; le scellement.

## 5. Intégrité (vérifiée par programme)

| contrôle | résultat |
|---|---|
| brouillon 35 intact ; brouillon 36 et note | compagnons vérifiés (`e62b4cae…`, `42adbbee…`, `4af1daee…`) |
| section 12 ; 7.1 à 7.8 ; section 10 | **identiques au brouillon 35** ; fiches 9 à 12 mot pour mot ; points 1 à 21 dans l'ordre |
| 8.1 à 8.6 | identiques au brouillon 35 (seul le trait de séparation passe après 8.7) |
| hypothèse au seuil ; 6.1 ; 6.3 à 6.8 ; 6.10 à 6.12 ; sections 9 et 11 | identiques au brouillon 35 |
| titres | 54 : un titre neuf, « 8.7 Gardes de procédure (tenues par une session, non par un programme) », à la fin de la liste d'arrêt ; les autres sont inchangés hors le titre de niveau 1. La numérotation stable des sections citées ailleurs est gardée. |
| citations du brouillon 35 | 1 321, **aucune absente** |
| citations du brouillon 20 | 935 ; les deux mêmes absentes, déjà justifiées |
| consignes figées (3.2 et 3.3) | égales octet pour octet à celles du brouillon 20 ; `98a9bd34d280…`, `ecf590eae0c0…` |
| validateur `problemes()` | deux problèmes, les attendus |
| marque des cases | six lignes, toutes en 13.1, les mêmes cases ; aucune en 8.7 |
| table d'en-tête, lignes neuves | empreintes égales : brouillon 35, sa note, ma vérification, relevé de la version 12, vérification du code de la version 12. La ligne du programme du constat en version 5 (`fd5fddcd…`) est du code, que je n'ai pas recalculé. **Aucune empreinte de fichier cloisonné prise.** |

## 6. Fichiers ouverts

- Le brouillon 36 : par différence ; la section 8.7 en entier ; les lignes citées en tête.
- Les brouillons 20 et 35, par programme.
- La note du brouillon 36.
- `verification-corrections-code-v12-bras-a-v1.md` : son mineur M-1 et ses parties 2 à 4.
- Le fichier des fiches du brouillon 23, par programme.
- `src/controle_ia/prereg.py` (`problemes()`).
- Pour leur seule empreinte : le relevé de la version 12 et la note du brouillon 35.
- Rien d'autre :
  - ni le journal, ni aucun code, ni aucun interne de moniteur ;
  - aucune clé, aucun appel de modèle ni appel réseau ;
  - aucun sous-agent ;
  - un seul fichier écrit, celui-ci, scellé ; rien committé.

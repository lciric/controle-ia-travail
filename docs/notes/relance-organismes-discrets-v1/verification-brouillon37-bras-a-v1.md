# Vérification brève du brouillon 37 du texte neuf du bras A des organismes discrets — v1

- **Vérificateur** : Claude Opus 5.5 (`claude-opus-5-5`), contre-lecteur des brouillons 21 à 36. Je juge ; je ne corrige rien.
- **Texte** : `prereg/T0.7-organismes-discrets-v-a-v2-brouillon37.md`, `8f3a38c06b77…`.
- **Pièces jointes, compagnons vérifiés** :
  - la note, `8037f8c41fde…` ;
  - la vérification du code de la version 13, `0b8b51e2419e…` ;
  - la pièce du mot « a a », `ae279572bd08…` ;
  - son erratum 1, `964027bca489…`.
- **Méthode** :
  - comparaison des brouillons 36 et 37 par programme ;
  - lecture des blocs touchés : en-tête, lignes 149 à 163 ; 6.9, lignes 817 et 821 ; 8.7, lignes 1139 à 1152 ; 13.1, lignes 1379 et 1391 ; 13.2, lignes 1401 à 1405 ;
  - aucun code ouvert, et aucune empreinte de code prise.

## Verdict : **engageable**

- Les trois mineurs de ma vérification du brouillon 36 sont tenus.
- Les points de la vérification du code de la version 13 sont portés.
- **Aucune règle de jugement ne change.**
- **L'intégrité tient.**
- La liste de la partie 3 de la note est presque complète. Il lui manque trois précisions (partie 4).

## 1. Les points

| point | état | endroit |
|---|---|---|
| mon M-1 du brouillon 36 : le versement ne rendait visible que ce qui était versé | **tenu** | 8.7, ligne 1145 : l'enchaînement fait lui-même le commit et le poussage dans la même exécution, avant de rendre quoi que ce soit. Si le poussage échoue, il s'arrête sans rien rendre. La **limite qui reste** est écrite honnêtement : une session qui ouvrirait le fichier hors de l'enchaînement, ou qui l'interromprait, pourrait lire puis détruire. Ce qui borne ce reste : la commande au manifeste, et l'épreuve de bout en bout. |
| mon M-2 : le mot « a a » sans pièce scellée | **tenu** | Le mot est cité partout par sa lecture consignée (`ae279572…`), dans six passages. Plus aucune citation ne passe par le journal seul, ni ne donne d'heure. Sa ligne au registre est demandée dans la case « nœuds », sans nommer GO-2026-11-19-97. |
| mon M-3 : liste de ce qui sépare du scellement | **tenu** | 13.2, ligne 1405 : le dossier de l'essai de mesure est à verser sur la branche principale avant toute dépense. La liste est récrite (partie 3 de la note). |
| code v13 : les modules arrêtés | **tenu** | Case « commit du code » : trois modules en version 13, six en version 12 et le programme du constat en version 5, avec leurs empreintes entières. Je n'ai recalculé aucune empreinte de code. Je les ai confrontées aux pièces : les trois de la version 13 et celle du programme du constat se retrouvent dans la vérification et dans la note du code de la version 13 ; les six de la version 12, dans la vérification et dans la note du code de la version 12. Seul le commit reste marqué. |
| code v13 : le module d'analyse n'est pas épinglé par la configuration | **tenu**, par une garde de procédure | 8.7, ligne 1149 : le manifeste consigne l'empreinte de l'analyse, des verdicts et de la garde statique, et sa contre-lecture les confronte à 13.1. Jouer avec une autre analyse est un écart à ce texte (13.1). C'est cohérent avec la décision de Lazar d'arrêter le code. |
| code v13 : ordre des gardes, constat d'incohérence sous un contrôle malsain, aucun plafond, un même arrêt n'ouvrant jamais deux reprises | **tenu** | 6.9, ligne 821. Ce sont des précisions de ce que fait le code arrêté. Aucune n'ouvre une lecture ni ne dit une issue. |

## 2. Règles de jugement

**Aucune ne change.**
- Par programme, sont identiques au brouillon 36 : la section 12, les sections 7.1 à 7.8 et 10, 8.1 à 8.6, l'hypothèse au seuil, 6.1, 6.3 à 6.8, 6.10 à 6.12, et les sections 9 et 11.
- Les fiches 9 à 12 restent mot pour mot, et les points 1 à 21 sont dans l'ordre.
- Ce que le brouillon change :
  - des citations ;
  - l'inscription des modules ;
  - une garde de procédure ;
  - le versement par l'enchaînement ;
  - des précisions sur la reprise de l'étape (n), qui ne touchent aucune issue. Une sortie incohérente garde « non rapportées : livraison refusée », et la table C n'est pas touchée.

## 3. Intégrité (vérifiée par programme)

| contrôle | résultat |
|---|---|
| brouillon 36 intact ; brouillon 37 et note | compagnons vérifiés |
| citations du brouillon 36 | 1 353, **aucune absente** |
| citations du brouillon 20 | 935 ; les deux mêmes absentes, déjà justifiées |
| consignes figées (3.2 et 3.3) | égales octet pour octet à celles du brouillon 20 ; `98a9bd34d280…`, `ecf590eae0c0…` |
| titres | 54 ; seul le titre de niveau 1 change |
| validateur `problemes()` | deux problèmes, les attendus |
| marque des cases | six lignes, toutes en 13.1, les mêmes cases |
| table d'en-tête, lignes neuves | empreintes égales : brouillon 36, sa note, ma vérification, pièce du mot « a a », note et vérification du code de la version 13. Les dix lignes de code sont confrontées aux pièces, non recalculées. **Aucune empreinte de fichier cloisonné prise.** |
| heure du mot « a a » | aucune heure n'est plus donnée dans le texte actif (« 03:30 », « 04:00Z » et « 04:49 » sont absents) |

## 4. La liste de ce qui sépare du scellement (partie 3 de la note)

Elle est presque complète et bien rangée, par qui doit agir. Trois précisions manquent :
- **(a) L'erratum du mot « a a ».** Il est postérieur au brouillon (05:12:58Z, contre 05:11:13Z) et dit que l'heure de la pièce n'était pas établie. Le texte ne donne plus d'heure ; c'est donc sans effet sur une règle. Mais le prochain brouillon doit citer l'erratum à la table d'en-tête, à côté de la pièce qu'il corrige, et la liste doit le dire.
- **(b) L'enchaînement de la lecture de la discrétion.** Le texte lui demande désormais le commit et le poussage avant de rendre quoi que ce soit. Il est hors du code arrêté, pas encore écrit, et il doit être écrit et contre-lu avant l'épreuve de bout en bout (réserve 2 de la note). Il n'est pas dans la liste ; il faut l'ajouter à « après le scellement, avant toute dépense », avec qui l'écrit et qui le contre-lit.
- **(c) L'ordre entre le renvoi de la base et la contre-lecture 10.**
  - La case « renvoi de la base » veut que le lecteur habilité vérifie la version que la contre-lecture 10 rendra. Ce renvoi tient lieu de vérification habilitée (section 13, étape 6).
  - La liste le range sous « lecteur habilité » sans dire qu'il vient **après** la contre-lecture 10. Une phrase suffit.

Le reste y est :
- les deux lignes de mots au registre, et leurs consignes ;
- le type « inscription » ;
- les réponses du développeur et leur confirmation, `piece_source` bloquant, les pièces de la case du module et le lanceur ;
- les quatorze empreintes héritées ;
- le chiffrage et le mot de Lazar sur le juge, et l'information à Lazar sur le point 19 ;
- le commit du code ;
- les demandes mises à jour et leur relecture ;
- le dernier brouillon ;
- la contre-lecture 10 et la vérification indépendante ;
- l'entier racine, le contrôle de différence, le validateur et le scellement.

## 5. Fichiers ouverts

- Le brouillon 37 : par différence ; les lignes citées en tête.
- Les brouillons 20 et 36, par programme.
- La note du brouillon 37.
- La pièce du mot « a a » et son erratum.
- Par recherche de chaînes, sans lecture du code : la vérification et la note des codes des versions 13 et 12.
- Le fichier des fiches du brouillon 23, par programme.
- `src/controle_ia/prereg.py` (`problemes()`).
- Rien d'autre :
  - aucun code ouvert ni haché ;
  - aucun interne de moniteur, aucune clé ;
  - aucun appel de modèle ni appel réseau ;
  - aucun sous-agent.
- Un seul fichier écrit, celui-ci, scellé ; rien committé.

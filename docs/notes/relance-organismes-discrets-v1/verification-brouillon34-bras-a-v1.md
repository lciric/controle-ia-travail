# Vérification du brouillon 34 du texte neuf du bras A des organismes discrets — v1

- **Vérificateur** : Claude Opus 5.5 (`claude-opus-5-5`), contre-lecteur des brouillons 21 à 33. Je juge ; je ne corrige rien.
- **Texte** : `prereg/T0.7-organismes-discrets-v-a-v2-brouillon34.md`, `0b6413d9d75a…`.
- **Pièces jointes** :
  - la note, `b8619e7995d4…` ;
  - la vérification des corrections du code de la version 10, `538f09c0934d…`, en-tête et parties 2 et 3.
  - Les compagnons sont vérifiés.
- **Méthode** : différence phrase par phrase entre les brouillons 33 et 34, faite par programme ; lecture des blocs touchés.
  - Conventions, lignes 219 à 222.
  - 6.2, ligne 626.
  - 6.9, lignes 781 à 789.
  - 8.4, lignes 1034 à 1038.
  - 13.2, lignes 1354 et 1355.
  - L'en-tête du registre des accords, pour sa forme seulement.
  - Aucun code ouvert.

## Verdict : **engageable**

- **Les points demandés sont tenus** : le défaut C-1 et les mineurs M-1 à M-5 de la vérification du code de la version 10, et mes mineurs M-1 et M-2 du brouillon 33.
- **Aucune règle de jugement ne change.** Par programme, la section 12, les sections 7.1 à 7.8 et la section 10 sont identiques au brouillon 33. Le reste du texte qui porte des règles l'est aussi.
- **Les quatre fichiers neufs, le quatrième champ de l'ouverture et la valeur « en attente » sont des procédures.**
- **La phrase d'accord en cellule exacte est sûre contre une négation.** Il lui manque deux bords, et la porte de l'écart à R9 a un angle mort (M-2).
- Il reste trois mineurs, dont aucun ne retient le texte.

## 1. Les points demandés

| point | état | endroit |
|---|---|---|
| code v10, C-1 : une course lit deux livraisons | **tenu** | Une ouverture de lecture est scellée avant toute lecture d'une première livraison, dans le dossier des arrêts. Ensuite, toute autre pièce exige une ligne de GO et un acte. Seul le rejeu de la même pièce reste permis. Une configuration de rang supérieur à 1 doit inscrire un registre figé. 6.9, ligne 789, points (1) à (5) ; 8.4, ligne 1034 : cas sains et artefacts, dont les deux formes de l'essai d'attaque (une autre pièce au rang 2 sans registre ; une autre pièce sous la même configuration avant le fichier de l'étape (m)). |
| code v10, M-1 : phrase d'accord trop large et trop étroite | **tenu** | 13.2, ligne 1355 : la cellule d'objet est exactement la phrase, sans égard à la casse ni aux accents, une ponctuation finale admise. 8.4, ligne 1035 : la négation devant, une suite après et la phrase seulement contenue sont refusées ; la phrase sans accents passe. Voir partie 3. |
| code v10, M-2 : un contrôle ancien suffit à un rejeu | **tenu** | Un contrôle ne vaut que pour le rejeu qui le suit. Une trace de rejeu scellée lie le contrôle employé au rejeu, et un contrôle déjà tracé n'ouvre aucun autre rejeu. Un contrôle est exigé aussi pour le rejeu d'une première livraison, que l'ouverture signale. |
| code v10, M-3 : abrégés courts | **rien à faire**, à juste titre | La consigne de tenue (empreinte entière) couvre ce cas. |
| code v10, M-4 : une autre course efface les traces | **limite écrite** | 6.9, ligne 789. Voir M-1 ci-dessous. |
| code v10, M-5 : la garde « en attente » ne laisse pas de trace | **tenu** | Constat de pièce en attente d'un choix, sur le modèle du constat de provenance. |
| mon M-1 du brouillon 33 : erreur de rangement | **tenu** | Le programme écrit dès le refus un constat d'erreur de rangement, avec les deux empreintes : celle des octets donnés et celle que scelle le compagnon. « La même pièce » est définie, et une autre pièce passe par la règle d'octroi. Artefact en 8.4. |
| mon M-2 du brouillon 33 : registre | **tenu** | Le registre est relu au commit `a42ac1f5d`. Le mot de Lazar n'y est pas encore inscrit ; la consigne n'est pas rompue. |

## 2. Les réserves du rédacteur

**Réserve 1 — les quatre fichiers scellés neufs.** Ce sont **quatre procédures.**
- **Ouverture de lecture.** Demandée par le vérificateur du code (C-1 (a)). Elle est à la première livraison ce que l'acte de reprise est à une livraison refaite.
- **Constat d'erreur de rangement.** Il répond à mon M-1.
- **Constat de pièce en attente d'un choix**, de la conception du rédacteur, sur la proposition M-5 du vérificateur du code.
- **Trace de rejeu**, de la conception du rédacteur. Elle répond à M-2. Sans elle, après une seconde panne, rien ne montrerait qu'un contrôle a déjà servi.

Ce qui vaut pour les quatre :
- aucun n'est un fichier d'arrêt, aucun n'emporte une issue ;
- aucun ne porte un nombre ni un champ de la pièce : des natures en liste fermée et des empreintes ;
- l'écriture se fait sans reste, et R5 est tenu en 8.4.

**Réserve 2 — le quatrième champ de l'ouverture, `sha256_du_constat_de_lancement`.** C'est une procédure. Il lie la première lecture à son constat, comme l'acte de reprise et les constats de l'étape (m) le font déjà (brouillon 30). La symétrie est juste.

**Réserve 3 — la valeur « en attente », qui ne survit pas au scellement.** C'est une procédure.
- C'est la mise en œuvre de « attendre » du mot de Lazar, en garde ordinaire et sans issue.
- Le texte ne se scelle qu'une fois le point 20 tranché, et aucune course ne part sous cette valeur.
- Tout ce qui s'y rattache est donc, pour la course, sans objet. Cela touche le constat de pièce en attente et la branche de la règle d'octroi « quand le choix en attente est tranché » (6.9, ligne 789). Ces passages ne servent qu'aux essais du code avant le scellement.
- Il faudra les retirer avec la valeur. Voir M-3.

**Réserve 6 — une autre course, avec un autre dossier des arrêts.** La limite est déclarée honnêtement, mais elle peut se fermer par programme : M-1.

## 3. Les deux phrases d'accord en cellule exacte

**Sûres contre la négation et l'ajout.**
- La cellule doit être la phrase, rien avant, rien après.
- « aucun écart à R9 accordé… », « pas d'écart… avant le devis » et « … ? à trancher » ne passent plus.
- « ecart a R9 accorde… », sans accents, passe : c'est voulu.
- C'est exactement la correction que proposait la vérification du code.

**Deux bords à écrire, et un angle mort.** Voir M-2.
- **(a) Le type de la ligne n'est pas exigé.** Une ligne de type « révocation » dont la cellule d'objet serait la phrase ouvrirait. L'en-tête du registre dit qu'« une révocation est une nouvelle ligne de type « révocation » ». Il suffit d'exiger, pour une ligne d'accord, un type autre que « révocation ».
- **(b) La mise en forme du registre.** Les cellules d'objet du registre portent d'ordinaire du gras (`**…**`), par exemple à la ligne de GO-2026-11-19-70. Une phrase en gras ne serait pas « exactement » la phrase. Le défaut est sans danger, puisque la ligne n'ouvre alors rien. Mais il bloquerait à tort. Il faut dire à la session principale d'écrire cette cellule sans mise en forme, ou ôter le gras avant de comparer.
- **(c) L'angle mort de la porte de l'écart à R9.** Elle lit la ligne dans l'état du registre au commit de son inscription. Une révocation entrée après ce commit, mais avant le tirage de la table, n'est pas vue. Il faut que la session qui lance le tirage fasse le même contrôle que le constat de lancement : sur le registre courant, aucune ligne neuve qui nomme la ligne de l'écart. Sinon le tirage ne part pas.

## 4. Mineurs

- **M-1. La limite « une autre course » peut se fermer par programme.**
  - La ligne d'inscription d'une configuration a une forme reconnaissable : type « inscription », `CONFIG-ANALYSE-DISCRETION-BRAS-A` et l'empreinte entière.
  - Le constat de lancement, qui lit déjà le registre courant, pourrait refuser une configuration de rang 1, sans registre figé, dès qu'une autre ligne d'inscription d'une configuration de l'analyse du bras A existe dans le registre sans ligne de GO de reprise qui la suive.
  - Une seconde première livraison serait alors arrêtée au lancement, et non seulement « visible au registre ».
  - Cette garde de lancement ne fixe aucune issue.
- **M-2. Phrases d'accord.**
  - (a) Exiger un type autre que « révocation » pour une ligne d'accord.
  - (b) Écrire la cellule d'objet sans mise en forme, ou comparer sans le gras ; à joindre à la demande 29.
  - (c) Contrôler l'absence de révocation de la ligne de l'écart à R9 sur le registre courant avant le tirage de la table.
- **M-3. Au scellement, retirer avec la valeur « en attente » tout ce qui s'y rattache** :
  - le constat de pièce en attente d'un choix (conventions, ligne 219) ;
  - la branche « quand le choix « en attente » est tranché » de la relecture d'une pièce arrêtée (6.9, ligne 789) ;
  - l'artefact de 6.9 et de 8.4 qui la nomme.

  La case « nœuds » le dit pour la valeur elle-même, mais pas pour ses suites.

## 5. Intégrité (vérifiée par programme)

| contrôle | résultat |
|---|---|
| brouillon 33 intact ; brouillon 34 et note | compagnons vérifiés (`dc3bc023…`, `0b6413d9…`, `b8619e79…`) |
| section 12 ; 7.1 à 7.8 ; section 10 | **identiques au brouillon 33** ; fiches 9 à 12 mot pour mot ; lignes d'origine du point 17 intactes ; points 1 à 21 dans l'ordre |
| hypothèse au seuil ; 6.1 ; 6.3 à 6.8 ; 6.10 à 6.12 ; 8.1 à 8.3 ; 8.6 ; sections 9 et 11 | identiques au brouillon 33 |
| citations du brouillon 33 | 1 236, **aucune absente** |
| citations du brouillon 20 | 935 ; les deux mêmes absentes, déjà justifiées |
| consignes figées (3.2 et 3.3) | égales octet pour octet à celles du brouillon 20 ; `98a9bd34d280…`, `ecf590eae0c0…` |
| titres | 53 ; seul le titre de niveau 1 change |
| validateur `problemes()` | deux problèmes, les attendus |
| marque des cases | six lignes, toutes en 13.1, les mêmes cases |
| table d'en-tête, lignes neuves | empreintes égales : brouillon 33, sa note, ma vérification, relevé de la version 10, vérification du code de la version 10. La ligne du programme du constat en version 3 (`6ee84152…`) porte une empreinte que je n'ai pas recalculée : c'est un fichier de code, que je n'ouvre pas. **Aucune empreinte de fichier cloisonné prise.** |

## 6. Ce qui reste avant le scellement

Les listes de mes vérifications des brouillons 32 (partie 8) et 33 (partie 5) valent toujours. S'y ajoutent :
- la session principale dit laquelle des cellules est l'objet, et inscrit les deux lignes d'accord sans mise en forme, au type « décision » (M-2) ;
- le lanceur du côté habilité inscrit l'empreinte et le commit de l'état figé de la porte de l'écart à R9 ;
- le contrôle de révocation avant le tirage de la table (M-2 (c)) ;
- les pièces des demandes mises à jour : nom du programme du constat, cellule d'objet, registre figé du lanceur ;
- le code en version 11, contre-lu ;
- au scellement, le retrait de la valeur « en attente » et de ses suites (M-3).

## 7. Fichiers ouverts

- Le brouillon 34 : par différence ; les lignes citées en tête.
- Les brouillons 20 et 33, par programme.
- La note du brouillon 34.
- `verification-corrections-code-v10-bras-a-v1.md` : en-tête, parties 2 et 3.
- Le fichier des fiches du brouillon 23, par programme.
- `src/controle_ia/prereg.py` (`problemes()`).
- L'en-tête et une ligne du registre des accords de la branche principale, par `git show`.
- Pour leur seule empreinte : le relevé de la version 10 et la note du brouillon 33.
- Rien d'autre : aucun code, aucun interne de moniteur, aucune clé, aucun appel de modèle ni appel réseau, aucun sous-agent. Un seul fichier écrit, celui-ci, scellé ; rien committé.

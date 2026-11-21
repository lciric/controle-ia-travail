# Contre-lecture de la conception v3 du véhicule NA-1 — v1

- Contre-lecteur, modèle O : le même que pour la v1, la v2 et le lot 0 (règle R2). Je n'ai écrit ni la conception, ni le relevé, ni la v9, ni aucun orchestrateur.
- Date (UTC) : 2026-11-21 ; relevé de `date -u` : 07:48:12Z, après la lecture, avant l'écriture.
- Processeur seul : aucun appel, aucune clé lue ni nommée, aucune dépense, aucune écriture dans un dépôt ; aucun `git show --name-only`.
- Je n'ai ouvert ni la branche `matiere-premiere/visees-mathematiques-v1`, ni aucune branche de quarantaine, ni le registre servi de la matière première. Rien sous `archives-reponses-modeles/` ni sous `/root/.claude/`.
- Aucun refus de permission, de classifieur ni de garde rencontré.

## Pièces et empreintes

| pièce | empreinte | contrôle |
|---|---|---|
| conception v3 (CO3) | `7f441d472231bec2879cee91402559a1cb24fe410825d3824214ad646a7225b9` | égale au compagnon et au mandat |
| différentiel v2 → v3 | `aebe241f2d172463877cc5efbf227ff0c950702d4238232bf94e92a8e021fe2c` | égale au compagnon |
| rapport v3 (RC3) | `aa9efcb4387a11b9a8aa32e153d894c75d7310bc06f18bb01cd05937514fc294` | égale au compagnon |
| table d'empreintes v3 | `fe704e9a7a42c0507f09fed14c7fc3cf9718f7ec9a902e0a6fcce70adb9ee7f1` | égale au compagnon |
| code relu à la source pour cette contre-lecture | `aiguilleur_v53.py` l. 30 à 53 ; `noyau_v54.py` (recherche de `lire_classe` et de `niveau_methode` : l. 28, 248, 272, 290) ; `adaptateurs.py` l. 55 à 58 ; `relais_reel_v2.py` l. 28 à 31 ; L9 l. 2665 à 2670 | orchestrateur à la tête `a41b7b50…` ; L9 à `1b47c1cf…` |

Les mots de la mère de 07:46Z sur les neuf propositions m'ont été transmis par la coordination. Je les applique au verdict.

## Verdict

**À corriger, par la v4 courte déjà prévue.** La v3 porte mes quatorze points, réécrit les § 2.3, 2.4, 2.9 et 2.13 comme il le fallait, et écrit les six décisions de 07:21Z comme décisions. Aucune refonte n'est nécessaire. Restent à porter dans la v4 :
- les écarts aux mots de 07:46Z, au § 4 ;
- trois défauts de conception, que le développeur des lots 5 et 6 rencontrerait (§ 1.2 à 1.4) ;
- les conséquences de l'état « garde seule » par défaut pour la colonne (§ 3).

Une fois la v4 vérifiée sur ces points, les mandats de code peuvent suivre dans l'ordre du chemin critique.

## 1. Mes points de la v2 et du lot 0, un par un (table du rapport v3, § 3)

| point (CL2, § 5) | porté ? | vérification |
|---|---|---|
| 1. Décisions de 07:21Z | oui | § 0 bis, première table ; § 2.6 (lignes de compte toujours écrites) ; § 2.4 (dénominateur de M3) ; § 5.2 (clé n° 40) ; § 2.13 (refus écrit) ; § 2.3 (non envoyé) ; § 2.14 (v9, l. 83). La règle 6 est à revoir sous la décision de 07:46Z (§ 3.1) |
| 2. Surcharge d'`appel` (mélange `AppelGardeNA`) | oui | § 2.3 : pas 0 à 7 ; interface au mandat du lot 4 ; phrase fausse sur le portier retirée et l'erreur avouée |
| 3. Refus avant le noyau | oui | § 2.3 : rien ne passe par `super().appel` ni par `lancer` ; coût nul, hors du suivi ; « non envoyé » au journal ; compté ; épreuve à trois constats et mutation « refus déplacé dans `lancer` » (§ 6.2) |
| 4. Adaptateur Claude neuf | oui | § 2.3 : fichier neuf sans texte système ; relevé au faux fournisseur au lot 4, avant l'additif ; chaîne vide essayée d'abord ; égalité sur la consigne extraite du corps |
| 5. Réponses brutes de Minuit et de Luc | oui | § 2.3 ; § 1.2 (enveloppe de L9 restreinte aux commandes externes) ; § 6.2, réponses en refus et en erreur comprises |
| 6. Lecteur et validateur neufs, champ `case` | oui | § 2.4 : ni `preparer`, ni `valider_contenu`, ni `fiches_du_texte` ; pas de caviardage ; méta tenue à part ; sort du champ `case` proposé (accepté à 07:46Z). Voir § 1.2 ci-dessous pour le portier |
| 7. Gardes héritées, pour tous les rôles | oui | § 2.13 : neuf lignes ; portier et juges nommés ; délai aligné sur 3 600 s ; seuil A3 au-dessus du nombre d'appels, A14 à 1 ; épreuves pour le proposeur, le portier et le juge. Voir § 1.3 (pas 0) et § 4 (A2) |
| 8. Identifiants réencodés | oui | § 5.2. Neuf syllabes pour six octets et sept pour cinq, juste : 60⁹ > 2⁴⁸ > 60⁸ et 60⁷ > 2⁴⁰ > 60⁶. Voir § 1.4 (lieu dans le code) |
| 9. `fournisseurs_requis` et `hors_course` | oui | § 2.9, § 2.3 (table), § 6.2 |
| 10. Six étapes ; mémoire ; configuration par génération ; statuts ; coûts ; forme de la fiche servie ; fuite de L9 | oui | § 2.9, § 2.3, § 5.3, § 2 (règle commune), § 7 (lot 8) |
| 11. Risque D2 et D7 | oui | § 9, point 20 ; § 2.10 ; § 5.4 |
| 12. A69 v4, § 7, point 8 | oui | § 2.11, ligne 8 ; § 2.7 |
| 13. Numérotation du lot 0 | oui | § 7 ; renvois « L0, Qn » |
| 14. Calendrier rechiffré | oui | § 8 : 36 h de lots, 17,5 à 18,5 h autour ; chemin 26 à 28 h ; attente de 48 à 60 h ; départ le 25 ou le 26 ; le 27 tient avec une marge mince. Honnête ; voir § 5 |

### 1.2 Défaut 1 : le portier ne peut pas reprendre la lecture du noyau

Le § 2.4 donne au portier les étiquettes « niveau de l'idée » ou « concret », plus trois étiquettes d'appel pour les réponses sans fiche. Il dit aussi que l'appel du portier « passe par `appel` (`noyau_v54.py`, l. 235) », ce qui laisse croire que le classement de la v54 est repris. Or ce classement lit, à la source :
- un bloc structuré `{"classe": …}` ;
- les seules classes `niveau_methode`, `a_corriger` et `concret` (`aiguilleur_v53.py`, l. 30 et 41 à 46) ;
- et il ne donne un passeport qu'à `niveau_methode` (`noyau_v54.py`, l. 248).

La classe `a_corriger` n'existe pas dans la v9, et aucune de ces classes ne classe une réponse sans fiche.

**À écrire** :
- le portier est un code neuf qui appelle `self.appel` (donc la surcharge) avec sa propre fonction de lecture ;
- celle-ci lit les étiquettes fermées de la consigne de D3, et elles seules ; une étiquette hors liste vaut « illisible », donc « au coffre » (D6) ;
- il tient deux sortes d'appel, la fiche d'une part, la réponse sans fiche d'autre part ;
- il délivre les passeports que les juges exigent (§ 1.4).

### 1.3 Défaut 2 : le « refus écrit » du pas 0 ne dit pas ce qu'il rend à l'appelant

Le noyau rend `None` pour un appel non lancé. Le classement du portier de la v54 en fait une décision « non lancé », de classe vide (`noyau_v54.py`, l. 238 et 239) : une fiche sans classe, ni passée, ni au coffre, ni hors case.

**À écrire, pour chaque rôle**, ce que devient l'objet de l'appel quand il est refusé par écrit :
- pour un proposeur : la case est non jouée pour cette espèce, comptée sur la ligne de la génération ;
- pour le portier : *proposition*, la fiche va au coffre comme un illisible (D6), comptée à part, pour qu'aucune fiche rendue ne reste sans classe ;
- pour un juge : un verdict absent, compté.

Le seuil A3 étant inerte par valeur, le cas devrait être rare, mais il est épreuvé. Le seuil « au-dessus du nombre d'appels du rôle par génération » doit aussi être chiffré pour le portier et les juges, dont le nombre d'appels dépend du nombre de fiches : par exemple une borne tirée du plafond de l'étape et du coût le plus bas d'un appel, écrite à l'additif.

### 1.4 Défaut 3 : le réencodage de l'identifiant servi au juge et le passeport demandent une surcharge de `juger`

L'identifiant servi au juge est construit à l'intérieur de `juger` (« F » suivi de `jeton_opaque(…, 5)`, `noyau_v56.py`, l. 198 et 199), et `juger` exige le passeport de `self.aiguilleur` (l. 194). La v3 propose le réencodage (§ 5.2) et un portier neuf, mais ne dit pas **où**.

**À écrire** : la classe neuve surcharge `juger` (fichier neuf, lot 6). La surcharge reprend la boucle des juges, sert l'identifiant réencodé et lit le passeport du portier neuf. L'autre voie, surcharger `jeton_opaque`, toucherait tous les jetons, et je ne la recommande pas. Il faut ajouter cette surcharge au lot 6 et à la table du § 5.1. L'identifiant de fiche, lui, est bien posé dans la proposition neuve (§ 2.9).

## 2. Les décisions de 07:21Z, écrites comme décisions

Les six sont écrites comme tranchées, avec leur lieu (§ 0 bis), et la v2 est dite renversée là où elle proposait l'inverse (lignes de compte).
- La clé n° 40 est « tirée au même geste, par le même programme, et consignée » (§ 5.2).
- Le refus écrit et le non envoyé à coût nul ont chacun leur ligne de journal et leurs comptes (§ 2.7).
- La règle 6 (la v9, l. 83, sans objet tant que la colonne est éteinte) est bien écrite (§ 2.14). **Mais la décision de 07:46Z fait de « garde seule » l'état par défaut** : la condition « tant que la colonne est éteinte » ne tient donc plus par défaut (§ 3.1).

## 3. La colonne « matière première »

Ce qui est cohérent avec la v9 et avec la quarantaine :
- le chargement depuis `3bcb94e6…`, à son empreinte, des deux seuls champs nom et énoncé, les deux autres jamais gardés ;
- la vérification des 35 lignes par le programme de l'arrêt n° 19 et par la garde de motifs avant tout chargement ;
- la garde à trois tenues : liste fermée de `requete`, comparaison au pas 3, aucun identifiant de la colonne au registre ;
- aucune ligne de la colonne dans M1 à M7, C1 ni I1 ;
- la comparaison finale par programme, sans juge qui décide (N-058), le classement des juges à part « pour information » ;
- les preuves des arrêts n° 17, 18 et 19 (§ 2.15) ;
- la vigilance de l'attestation tenue : rien hors des réponses brutes, rien vers une session qui conçoit des moniteurs sans passer par Lazar.

**À corriger ou à préciser dans la v4 :**

1. **L'état par défaut est « garde seule »** (mère, 07:46Z), et non « éteinte ». Les lieux à changer : § 0, point 4 ; § 0 bis, dernier paragraphe ; § 2.14 (titre, première phrase, interrupteur, règle d'allumage) ; § 6.2 (« colonne éteinte (défaut) ») ; § 7 (lot 10 « facultatif, hors du chemin critique, la course part sans lui ») ; § 8 ; § 9, point 18.

   Conséquences à écrire :
   - le chargement et la garde du lot 10 deviennent nécessaires à la course par défaut. Ils ne sont plus facultatifs ; ils restent parallèles, après les lots 3 à 5 et avant l'essai à blanc du lot 9. Seule la lecture de fin reste attachée à l'allumage ;
   - la règle d'allumage (a) à (e) ne vaut plus que pour l'état 2. Ce que demande l'état 1 par défaut (le mot de la mère est donné ; faut-il un additif à la V9 ?) est un point pour la mère, et la v4 le pose ;
   - la tension avec la v9, l. 83 se rouvre par défaut. *Proposition* : dans le véhicule, noms et énoncés ne vivent que dans le dossier de sortie, et la présence du registre servi sur `main` relève de GO-2026-11-21-19, hors du véhicule. C'est à dire à la mère, puisque la règle 6 ne la couvre plus.

2. **Le risque de faux refus de la garde de la colonne** arrête la course : une présence vaut « non envoyé » et un arrêt nommé de course. Les noms neutres peuvent être courts. Une idée de la course qui reprend par hasard un mot ou une ligne de la colonne arrêterait la course, par le registre servi des générations 2 et 3.

   **À écrire** :
   - la règle de comparaison : l'énoncé entier, normalisé ; le nom comme mot entier, au-dessus d'une longueur fixée à l'additif ;
   - le taux de faux refus mesuré à l'essai à blanc, comme pour l'arrêt n° 16 (V9, l. 387) ;
   - au départ, le gabarit, la synthèse servie et les consignes passent la garde de la colonne sans un refus, sinon la course ne peut pas partir ;
   - le numéro de cet arrêt, donné par l'additif.

3. **« Seuls les juges de fin lisent la branche »** : la v3 fait lire les réponses brutes par les deux lecteurs d'antériorité et par les deux juges de la course, à travers le programme de lecture de fin. La v4 doit citer la règle de la mère mot pour mot et dire si les lecteurs d'antériorité sont des « juges de fin ». Sinon, ils lisent les seuls noms et énoncés du dossier de sortie, et non la branche. L'inscription des lecteurs (accordée à 07:46Z) se fait sur cette liste.

4. **La lecture de fin passe par la surcharge d'`appel`** : il faut dire qu'elle suit une table de routage à part, comme les lignes à part. Elle se paie sur sa ligne à part, n'est jamais comptée dans les parts de la course (arrêt n° 12), et sa garde de motifs s'applique.

5. **La branche est-elle orpheline ?** La v3 écrit « je ne sais pas ». Le garde-fou 2 (V9, l. 119) et l'arrêt n° 17 veulent une quarantaine sans ancêtre commun avec `main`. Cela se vérifie sur le graphe des commits, sans ouvrir aucun fichier. *À écrire* : le contrôle est fait avant l'état 2 ; une branche liée à `main` est un point pour la mère avant toute lecture.

## 4. Les neuf propositions, et les mots de la mère de 07:46Z

Les neuf propositions sont fondées, et chacune est posée comme proposition (RC3, § 4 ; CO3, § 9, points 20 et 21). La v4 doit porter les mots de 07:46Z ; voici les phrases de la v3 qui les contredisent ou les laissent ouverts.

| n° | mot de la mère | lieu de la v3 à corriger |
|---|---|---|
| 1 | réencodage accepté ; règle d'encodage écrite et **éprouvée dans les deux sens** | § 5.2 et § 6.2 : ajouter la règle exacte (alphabet, ordre des octets, longueurs) et une épreuve aller-retour : encoder puis décoder rend les octets, et un mot hors alphabet est refusé. Poser l'encodage dans `juger` (§ 1.4) |
| 2 | case différente : consignée, comptée, classe inchangée | § 2.4 et § 6.2 : retirer « si la mère retient la proposition » |
| 3 | grammaire par étiquettes ancrées ; n° 27 à la lettre ; étiquette demandée à la session à part | § 2.4, § 5.4, § 9, point 20 : écrire comme tranché. **Un ajout dépasse la lettre** : « dans l'ordre ». La partie servie nomme les douze champs sans imposer d'ordre (PS, l. 19). Exiger l'ordre rendrait illisible une fiche complète, ce qui est une règle neuve ; la retirer, ou la poser à la mère. Ajouter une épreuve : la valeur libre d'un champ qui contient le nom d'un autre champ |
| 4 | « réponse illisible », **avec un sous-compte « cause non établie »** | § 2.3, « Les statuts », et § 6.2, « arrêt n° 13 sur une clé Claude » : ajouter le sous-compte, à M6 et à la ligne de la génération |
| 5 | tranché sur pièce après le lot 4 : transport octet pour octet, ou refus | § 2.3 : écrire comme tranché ; « deux options données à la mère » devient la règle |
| 6 | **A2 devient un arrêt nommé de course** | § 2.13, ligne A2 : remplacer « refus écrit ; portée proposée » par l'arrêt nommé de course, numéroté à l'additif ; § 9, point 19 ; épreuve à ajouter (modèle servi absent, puis changé : arrêt nommé) |
| 7 | somme des plafonds des processus d'une clé au plus sa part | § 2.3, note : écrire comme tranché ; épreuve au lot 8 |
| 8 | forme de la fiche servie déclarée | § 2.4, § 2.5, § 5.3 : écrire comme tranché, sans renvoyer à la lecture plus stricte du relevé |
| 9 | état par défaut « garde seule » ; seules les visées comparées ; lecteurs inscrits ; allumage au mot de Lazar et à sa ligne | voir § 3.1 et § 3.3 ; § 2.14, ligne « visées et énoncés de défense », à écrire comme tranché |

Autre point à aligner : le § 9, point 21 et le rapport ne comptent pas la même chose. Le § 9, point 21 liste sept propositions, dont « le dernier octet des pièces servies, gardé » (§ 5.3), que le rapport ne compte pas parmi les neuf. Sans mot de la mère, il reste une proposition à lui poser.

## 5. Faits neufs vérifiés à la source

| fait que la v3 tire du lot 0 | source | verdict |
|---|---|---|
| fuite de L9, l. 2667 à 2669 | L9 (`1b47c1cf…`), l. 2668 et 2669 : `raise Refus(f"vérification de l'orchestrateur refusée (code {verif.returncode}) : " f"{(verif.stderr or verif.stdout).strip()[-800:]!r}")` | **juste** |
| délai de session du kit : 3 600 s | `adaptateurs.py`, l. 57 : `DELAI_SESSION_S = 3600` | **juste** |
| le relais Claude ne garde jamais le corps | `relais_reel_v2.py`, l. 30 : « jamais la clé, jamais le corps des messages » | **juste** |
| classes du portier du noyau (fait neuf de cette contre-lecture) | `aiguilleur_v53.py`, l. 30 : `CLASSES = ("niveau_methode", "a_corriger", "concret")` ; l. 41 à 46 | à porter (§ 1.2) |

Non vérifiée : la note sur les deux processus de relais d'une même clé (L10, l. 121, 122, 454). La v3 la dit elle-même à vérifier au lot 8 (réserve 14).

**Calendrier.** Le rechiffrage est honnête. La v4 ajoute la surcharge de `juger` et le portier neuf (environ 1 h au lot 6, autant au lot 5), puis le chargement et la garde de la colonne, désormais nécessaires (environ 3 h, en parallèle des lots 6 à 8, avant le lot 9). Le chemin critique ne bouge pas si le lot 10 part en même temps que les lots 6 et 7. L'attente reste de 48 à 60 h ; l'échéance du 27 tient toujours avec une marge mince.

**Réserves du concepteur.** Le § 10, point 1 dit encore L9 « non lu », ce qui est périmé depuis le relevé ; à mettre à jour.

## 6. Ce que la v4 courte doit porter (liste)

1. Les neuf mots de 07:46Z, écrits comme tranchés, aux lieux du § 4 : épreuve de l'encodage dans les deux sens, sous-compte « cause non établie », A2 en arrêt nommé de course, colonne en « garde seule » par défaut.
2. Le portier neuf : sa propre lecture, ses étiquettes de D3 seules, ses deux sortes d'appel, ses passeports (§ 1.2).
3. Ce que rend un « refus écrit » pour chaque rôle, et le seuil A3 chiffré pour le portier et les juges (§ 1.3).
4. La surcharge de `juger` : identifiant réencodé, passeport du portier neuf (§ 1.4).
5. « Dans l'ordre » retiré de la grammaire par étiquettes, ou posé à la mère (§ 4, n° 3).
6. Les conséquences de « garde seule » par défaut : lot 10 nécessaire pour son chargement et sa garde ; règle d'allumage restreinte à l'état 2 ; ce que demande l'état 1 et la v9, l. 83, posés à la mère (§ 3.1).
7. La règle de comparaison de la garde de la colonne, son taux de faux refus, son contrôle au départ sur les pièces fixes (§ 3.2).
8. La règle « seuls les juges de fin lisent la branche », citée et appliquée ; la table de routage et la ligne à part de la lecture de fin ; le contrôle d'orphelinat de la branche avant l'état 2 (§ 3.3 à 3.5).
9. Le compte des propositions aligné entre le § 9, point 21 et le rapport ; le dernier octet des pièces servies posé à la mère.
10. Le § 10, point 1 mis à jour.

Après la vérification de ces points sur la v4, les mandats de code peuvent suivre dans l'ordre du chemin critique.

— contre-lecteur de la conception du véhicule, modèle O

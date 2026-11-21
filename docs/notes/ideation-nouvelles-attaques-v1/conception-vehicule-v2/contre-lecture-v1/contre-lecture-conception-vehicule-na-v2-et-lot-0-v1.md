# Contre-lecture de la conception v2 du véhicule NA-1 et du relevé du lot 0 — v1

- Contre-lecteur, modèle O, le même que pour la v1 (règle R2 ; règle de la mère : les deux pièces au même contre-lecteur). Je n'ai écrit ni la conception, ni le relevé, ni la v9, ni aucun orchestrateur.
- Date (UTC) : 2026-11-21 ; relevé de `date -u` : 07:30:38Z, après la lecture, avant l'écriture.
- Processeur seul : aucun appel, aucune clé lue ni nommée, aucune dépense, aucune écriture dans un dépôt ; pas de `git show --name-only`. Rien ouvert sous `archives-reponses-modeles/` ni sous `/root/.claude/`. Aucun refus de permission, de classifieur ni de garde rencontré.

## Pièces et empreintes

| pièce | empreinte | contrôle |
|---|---|---|
| conception v2 (CO2) | `a21effe48f9b12fe15f3dd1f45dcacb3de2fbde6effe76e599e042a473344310` | égale au compagnon et au mandat |
| différentiel v1 → v2 | `d128ed79a4e2b761178f78dc705a92d97dc331151d2a60a4edde51b2b9c7fef9` | égale au compagnon |
| rapport v2 (RC2), avec la table « point → lieu » | `679cf52e7377acfbb11e84eae2532cc749c6eb9d8e61cc6457883633dda0306a` | égale au compagnon |
| relevé du lot 0 (L0) | `10ac79ecb0e064f5b5ea80ddb060ae37e303d2d84ff242f653f4cccbd7ff753e` | égale au compagnon |
| table des empreintes du code lu au lot 0 | `d79bd98ef3b103cd173280cf002927ba5102d1f59828ba00590aeb9c513d463f` | égale au compagnon |
| partie servie (PS), `origin/main` | `4cd360baea1076ec2b19b2c7ba85675e739bc3104c709d4fd57c0769975b1cf1` | égale au compagnon et à la v9, l. 23 |
| additif v69, v4 scellée, § 7 | `cb352811…` | lu pour la v1 de cette contre-lecture |
| code relu à la source, orchestrateur `a41b7b50…` | `adaptateurs.py` l. 95 à 112, 320 à 350 ; `noyau_v54.py` l. 225 à 249 ; `noyau_v56.py` l. 147 à 215 ; `course2_v53.py` l. 38 à 103 ; `course2_v54.py` l. 80 à 104, 465 à 476 ; `course2_v56.py` l. 340 à 372 ; `fiches_v53.py` l. 15 à 50 ; `suivi_roles_v54.py` entier | chemins pris à la table du lot 0 |
| configuration v5 de la course v9 | lue l. 240 à 256 (`arrets`) | chemin pris à la table du lot 0 |

## Verdict

**À corriger.** La v2 porte fidèlement mes points de la v1 et les décisions de 06:58Z et de 07:10Z. Le relevé du lot 0 est juste sur les cinq réponses que j'ai vérifiées à la source. Mais ces réponses rendent caducs trois choix centraux de la v2 :
- le refus « non envoyé » rendu depuis `lancer` ;
- la raison donnée pour écarter le refus avant le noyau, qui est fausse ;
- l'appel à `preparer`, qui refuse toute fiche de cette course.

S'y ajoutent les décisions de la mère de 07:21Z. La v3 doit être une réécriture du § 2.3, du § 2.4, du § 2.9 et du § 2.13, et le calendrier doit être rechiffré.

## 1. Mes points de la v1 dans la v2 (suivi par la table du rapport v2, § 3)

| point de la v1 | porté ? | remarque |
|---|---|---|
| § 1.3 : `executer_course_v68` non appelée ; `GenerationV68` reçoit `None` | oui | § 1.2, § 2.9 |
| § 1.4 : lanceur 11 sans code | oui | § 1.1 |
| § 1.5 : suivre A69 v4, relevé de fin | oui, en partie | Le relevé de fin est porté (§ 2.11, point 7 ; § 6.2). Le concepteur n'a toujours pas ouvert la v4. Je l'ai comparée : les points 1 à 7, 9 et 10 concordent. **Au point 8, la v4 relit aussi « classes, statut, refus » par comptes** ; le § 2.11 ne dit que budget, bilan et coûts. À ajouter |
| § 1.6, § 1.7 : D1, D10 | oui | commit `61987a3a`, conforme à R-4383 |
| § 2.1 : gardes héritées | oui pour A3, A14, A11 et A2, la coupure, 11a | à refaire sur le lot 0 et sur la règle 4 de 07:21Z (§ 3.6 ci-dessous) |
| § 2.2 : coût fantôme | **porté, mais la voie retenue est contredite** | § 3.3 ci-dessous |
| § 2.3, § 6.4 : retrait du texte fixe de rôle | oui, dans l'intention | aucun réglage ne le permet (L0, Q1) : § 3.2 |
| § 2.4 : huit épreuves | oui, toutes | § 6.2 |
| § 2.5, § 2.6 | oui | lot 0, Q14 ; lot 7 |
| § 3.1 à § 3.3 : lot 8 en différentiel, dépendances, chemin critique | oui | à rechiffrer (§ 4) |
| § 4.1, § 4.2 : D3 de 3 à 4 h ; 40 à 50 h | oui | à revoir (§ 4) |
| § 5 : D11 | oui, à la lettre | § 6.1, n° 12 ; § 9, point 17 |
| § 6.2 : `idee` trop longue | oui (D13) | la mère a tranché depuis (07:21Z) |
| § 6.3 : deux lectures des mesures | oui (D12 à Lazar ; lettre gardée) | — |

**Décisions de 07:21Z, que la v2 ne pouvait pas porter, à faire entrer dans la v3** :
1. La fiche trop longue compte au dénominateur de M3. Le § 9, point 3 de la v2 en fait une proposition ; elle est désormais **tranchée**.
2. Les lignes de compte du registre servi s'écrivent toujours, compte nul compris. La v2 proposait l'inverse (§ 9, point 3) : **à renverser**.
3. La clé n° 40 va dans la table des clés de l'additif, à côté de la n° 30 (§ 9, point 4 : tranché).
4. Une garde héritée qui arrête produit un « refus écrit » ; voir § 3.6.
5. Un refus sans coût est « non envoyé », compté dans les refus ; voir § 3.3.
6. La tension avec la v9, l. 83 est sans objet tant que la colonne « matière première » est éteinte (§ 2.14, dernière ligne : à écrire comme tranché).

**Colonne matière première** : éteinte par défaut, la course part sans elle. C'est conforme au § 2.14 et au lot 10, facultatif.

**Une erreur de fait neuve dans la v2.** Pour écarter le refus avant le noyau, le § 2.3 dit : « le portier, qui appelle l'adaptateur sans passer par `appel` ». C'est faux :
- le portier passe par `self.o.appel(…, role_kit="juge_ideation", …)` (`noyau_v54.py`, l. 235) ;
- les juges passent par `self.appel` (`noyau_v56.py`, l. 202) ;
- les proposeurs aussi (`course2_v68.py`, l. 197).

**Tout envoi de la course passe par le seul `appel`.** La surcharge d'`appel` est donc un point unique, et non une reprise de chaque lieu d'appel.

## 2. Le relevé du lot 0 : ses réponses sont-elles justes ?

J'ai vérifié à la source les cinq réponses les plus lourdes. Toutes sont justes.

| question | ce que dit L0 | vérifié à la source |
|---|---|---|
| Q1 | `claude_sdk` pose toujours un texte système fixe choisi par le rôle ; le portier reçoit celui du juge ; aucun réglage ne le retire | **juste.** `adaptateurs.py`, l. 101 à 111 (les deux textes) ; l. 338 et 339 (`"system_prompt": (… else CONSIGNES_SYSTEME[role])`, toujours posé) ; `noyau_v54.py`, l. 235 (portier en `role_kit="juge_ideation"`) |
| Q3 | six étapes exigées, dans l'ordre ; la v56 joue la liste du module | **juste.** `course2_v53.py`, l. 42 (`ETAPES`), l. 73 à 81 (absentes, en trop, ordre) ; `course2_v56.py`, l. 346 (`for nom in ETAPES`) ; la mémoire tourne dans `executer` (l. 355 et 368) |
| Q6 | `preparer` refuse dix noms réservés, dont `case` ; `fiches_du_texte` ne lit qu'un bloc `{"fiches": …}` | **juste**, et c'est bloquant. `fiches_v53.py`, l. 19 (`CLES_META` contient `"case"`), l. 33 à 35 (refus). **La partie servie fait de `case` le premier des douze champs** (PS, l. 19 : « `case` (identifiant servi) ; … »). Appeler `preparer` refuserait toute fiche au contrat |
| Q12 | A3 à 3 échecs consécutifs ; A14 à 0,34 ; une réponse sans bloc `fiches` est un échec | **juste.** Configuration v5, `arrets` : 3, 1 800 s, 0,34, liste vide ; `course2_v54.py`, l. 470 à 474 (`_fiches_ou_none` rend `None`) ; `noyau_v56.py`, l. 179 à 181 (`exploitable=lu is not None`) ; `suivi_roles_v54.py`, l. 72 à 83 |
| Q13 | un refus levé dans `lancer` est compté au plafond entier ; rendu à coût nul, il compte un échec A3 et A14 | **juste.** `noyau_v56.py`, l. 161 à 175 (`cout = plafond if cout is None`), puis l. 180 et 181 |

Les autres réponses sont cohérentes avec ce que j'ai lu :
- Q2 : `fournisseurs_requis`, `course2_v54.py`, l. 87 à 91 et 97 à 99, vérifié.
- Q4 : la forme `[texte, bras]` est exigée, `course2_v53.py`, l. 94 à 96, vérifié.
- Q5, Q7 à Q11 et Q14 : non revérifiées ligne à ligne. Elles sont plausibles et précises (fichier et ligne).

Deux remarques sur le relevé :
- L'emploi de `git show --name-only` est déclaré comme écart. Il est désormais interdit : à ne pas reproduire.
- Sa numérotation diffère de celle de la v2 : chez lui, Q13 est le coût et Q14 la structure de L9, contre Q13 pour L9 dans la v2. La v3 doit aligner les renvois.

## 3. Ce que la v3 doit dire, contradiction par contradiction

### 3.1 Routage par rôle : par surcharge d'`appel` dans une classe neuve (L0, Q2 ; contredit le § 2.3)

L'adaptateur ne reçoit ni le rôle, ni la génération, ni la case (`noyau_v56.py`, l. 165). `appel` reçoit au contraire `role` (l'étiquette), `fournisseur` et `session` (l'étape et l'indice de la case ou le lot), et la génération connaît son numéro.

**La v3 écrit** :
- une classe de génération neuve (fichier neuf) dont `appel` fait, **avant** d'appeler `super().appel`, les pas 1 à 5 : routage (rôle, clé), part de la clé, garde de motifs, ligne de journal, égalité ;
- un refus à l'un de ces pas ne passe jamais par le noyau (§ 3.3) ;
- l'adaptateur gardé du § 2.3 disparaît comme lieu du contrôle ; il ne reste, au besoin, qu'un relevé du texte reçu à l'essai par le faux fournisseur ;
- la phrase « l'appel du noyau ne change pas : il atteint l'adaptateur gardé » est retirée ;
- la mutation « routeur par espèce » (D11) s'éprouve sur cette surcharge.

### 3.2 Adaptateur Claude neuf, sans texte système (D2 ; L0, Q1)

**La v3 écrit** :
- un fichier neuf, adaptateur du type `claude_sdk` pour le véhicule : il construit ses options comme `construire_options`, sans texte système, et garde le reste du transport tel quel (outils vides, un tour, plafond, sans repli de modèle, bac à sable) ;
- il sert les deux clés Minuit et Luc, pour les proposeurs, le portier et le juge ;
- **ce que l'outil envoie quand aucun texte système n'est donné n'est pas lisible dans le code** (L0, Q1). Il est relevé au faux fournisseur, derrière le vrai relais, **dès le lot 4 et avant l'écriture de l'additif**, et non au lot 9. Si un texte par défaut part, il est soit déclaré à l'additif comme transport, soit refusé (option à donner à la mère : une chaîne vide explicite si le faux fournisseur montre qu'elle supprime tout texte) ;
- l'égalité « texte reçu, transport retiré » porte sur la chaîne de la consigne extraite du corps, jamais sur les octets HTTP. Le relais compatible OpenAI resérialise le corps (L0, Q1).

### 3.3 Le refus AVANT l'appel du noyau

La voie de la v2 (un résultat « non envoyé » à coût nul rendu depuis `lancer`) est contredite deux fois :
- le noyau compte alors un échec, A3 et A14 (`noyau_v56.py`, l. 179 à 181 ; L0, Q13) ;
- la règle 5 de la mère (07:21Z) veut « non envoyé », coût nul, une ligne au journal, compté dans les refus, jamais un échec du rôle.

**La v3 écrit** :
- le refus se fait dans la surcharge d'`appel` (§ 3.1), avant `super().appel` : aucune consommation notée au coffre, aucun `suivi.apres`, aucune entrée dans `etat["cout"]` ;
- une ligne « non envoyé » au journal, avec le numéro de l'arrêt et la clé par son nom d'usage ;
- un compte des refus par rôle et par arrêt sur la ligne de la génération ;
- puis l'arrêt nommé est levé.

Le motif d'écarter cette voie (le portier hors d'`appel`) est faux (§ 1). L'épreuve « envoi refusé sans coût » du § 6.2 s'enrichit de trois constats après un refus : `suivi.roles[role]` inchangé, A14 non déclenchée, `consommations.json` sans ligne pour cet appel. Mutation : le refus déplacé dans `lancer` doit faire échouer l'essai.

### 3.4 Conservation des réponses brutes des clés Minuit et Luc (L0, Q10)

L'enveloppe de conservation de L9 n'entoure que les commandes externes (L9, l. 2229). Le relais Claude ne garde jamais le corps (`relais_reel_v2.py`, l. 30).

**La v3 écrit** :
- l'adaptateur Claude neuf (§ 3.2) écrit la réponse brute (texte, statut, champ de refus, erreur) dans le dossier de sortie, avant de rendre la main, sous un nom qui ne dit que la session ;
- ce n'est pas `lire` qui conserve : `lire` ne reçoit le texte que si le statut est « ok » ;
- la phrase du § 1.2 (« l'enveloppe de conservation des réponses brutes », gardée de L9) est restreinte aux commandes externes ;
- l'épreuve « réponses brutes conservées » (§ 6.2) couvre les deux types d'adaptateur, réponses en refus et en erreur comprises.

### 3.5 Le champ `case` face au contrat de la partie servie (L0, Q6)

Vérifié sur `origin/main` : `case` est le premier champ du contrat (PS, l. 19). La partie servie est scellée, et changer le nom du champ serait un nœud.

**La v3 écrit** :
- le lot 5 n'appelle ni `fv.preparer` ni `valider_contenu` ;
- un validateur neuf vérifie les douze champs du contrat, leur présence et leur borne (D13), et repère tout champ en plus : « au coffre », V9, l. 88 ; PS, l. 21 ;
- la méta de la fiche (case servie, fournisseur, passe) est tenue à part du contenu ;
- un lecteur neuf à deux syntaxes est déclaré à l'additif (`fiches_du_texte` ne lit que `{"fiches": …}`) ;
- **la valeur du champ `case`** (l'identifiant servi) : ce qu'il advient d'une fiche qui porte un autre identifiant que celui de sa case n'est fixé par aucune lettre (la règle « hors case » ne compare que les trois champs fermés). *Proposition à la mère* : la consigner et la compter, sans changer la classe ;
- **le caviardage** de `valider_contenu` modifie le texte des champs : ne pas le reprendre avant la classification. La comparaison à l'octet de l'arrêt n° 4 et la règle « jamais réparée » (D13) lisent le texte rendu.

### 3.6 A3 et A14 contre la v9, l. 97 et 101, et la règle 4 de la mère

La règle 4 de la mère dit : aucune garde héritée n'arrête un rôle sans écrire sa cause ; une garde qui arrête produit un « refus écrit », compté, jamais un échec du rôle ni un coût ; le lot 0 dit lesquelles peuvent se déclencher ; la v3 les nomme une par une.

**La v3 écrit, une par une**, en étendant le § 2.13 à **tous les rôles** (le portier et les juges y sont exposés comme les proposeurs, L0, Q12) :

| garde héritée | sort à écrire |
|---|---|
| A3, échecs consécutifs | La lecture passée par la surcharge rend un objet dès qu'un texte est rendu, fiche ou non. `{"fiches": []}` et le texte sans bloc vont tous deux au classement en quatre classes d'appel. Le seuil est déclaré au-dessus du nombre d'appels du rôle par génération. Un arrêt de rôle qui surviendrait malgré tout (`RoleArrete`, `appel-saute-role-arrete`) est attrapé par la surcharge et écrit en « refus écrit », compté, jamais en appel sauté sans trace |
| A3, délai (1 800 s, sous les 3 600 s de la session du kit) | Aligner le délai au moins sur celui du kit. Un appel coupé est classé « réponse illisible » (M6), écrit et compté |
| A14 (0,34) | Part maximale déclarée à 1 ; M6 rapporte. L'arrêt total qu'elle déclenche (étape technique, nœud, course arrêtée) est contraire à V9, l. 101 |
| A11 | Inerte, la liste étant vide ; à vérifier à la configuration |
| A2, modèle servi absent ou changé | Rattachée à « aucune bascule » (V9, l. 182) ; effet : refus écrit. Sa portée (l'appel, le rôle ou la course) est une proposition à la mère |
| coupure au plafond dur de l'étape | Rattachée à l'arrêt n° 7 ; chaque appel non lancé est écrit et compté à part, jamais dans M6 |
| 11a | Rattachée à l'arrêt n° 6 |
| garde propre au nom `kimi` (S12, `course2_v54.py`, l. 172 à 183) | Aucun adaptateur de la course ne porte ce nom ; épreuve à la configuration |
| portier qui ne rend pas de classe (`noyau_v54.py`, l. 237 à 246) | Classe « concret », donc au coffre, conforme à D6. Mais son appel compte un échec A3 et A14 sur le portier : couvert par les deux lignes A3 et A14 ci-dessus |

Épreuves :
- onze réponses vides motivées d'un proposeur, puis trois réponses illisibles de suite du portier : aucun rôle arrêté, chacune classée et comptée ;
- mutation « lecture qui rend rien » : l'essai doit échouer.

### 3.7 L'identifiant de fiche, « f » plus 12 hexadécimaux, face à la limite de huit (L0, contradiction 11)

Le relevé ne pose le problème que pour le registre. Il est plus large : **la garde de motifs (arrêt n° 16) vaut pour les requêtes des juges** (V9, l. 387). Le noyau sert au juge l'identifiant « F » suivi de 10 hexadécimaux (`noyau_v56.py`, l. 198 et 199). Chaque requête de juge porte donc une chaîne hexadécimale de plus de huit caractères : avec la famille « identité et dépôt », **toute requête de juge serait refusée**. De même, le registre servi porte le nom d'une fiche, soit son identifiant (D5).

**La v3 écrit** :
- l'identifiant de fiche et l'identifiant servi au juge sont **réencodés** dans un alphabet sans chiffre ni lettre hexadécimale en position de suite, par exemple les syllabes de l'identifiant de case. Les octets du jeton existant (`graines_v53.py`, l. 65 à 67) sont gardés : c'est un encodage, pas un tirage neuf, donc aucun écart à V9, l. 311 ;
- c'est une proposition à la mère. L'autre voie, une clé de tirage neuve, demande un écart accordé ;
- épreuve : toutes les requêtes du portier et des juges de l'essai passent la garde ; mutation « identifiant hexadécimal » : l'arrêt n° 16 mord ;
- le champ `filiation` cite ce même identifiant réencodé.

### 3.8 Les adaptateurs exigés pour des rôles jamais appelés (L0, Q2)

`fournisseurs_requis` exige des adaptateurs pour les deux lecteurs d'étiquettes et le metteur en fusion (`course2_v54.py`, l. 87 à 91 et 97 à 99). Ces rôles ne sont dans aucune ligne de la table des rôles et des clés.

**La v3 écrit** :
- la classe neuve surcharge `fournisseurs_requis` (méthode statique) pour n'exiger que les adaptateurs de la table ;
- les champs de configuration que `verifier_configuration_generation` exige (`lecteurs_etiquettes`, `bisociateur`, `tableau.consigne_passe`, `memoire.methode`, plafonds `fusion` et `lecteur`) restent présents et inertes ;
- leurs noms de fournisseur désignent `hors_course`, une entrée absente de la table de routage : tout appel d'un de ces rôles est refusé par la surcharge d'`appel`, « non envoyé », arrêt n° 12 (seconde clause), et jamais par une `KeyError` du dictionnaire des adaptateurs ;
- aucun rôle n'est ajouté sur une clé de la course ;
- épreuve : un appel planté d'un lecteur d'étiquettes est refusé, nommé.

### 3.9 Les autres contradictions du relevé

- **Six étapes** (Q3) : la v3 remplace « trois étapes et aucune autre » par « trois étapes jouées avec appels ; `etiquettes` jouée sans appel ; `passe_tableau` et `fusions` retirées par construction », comme la configuration v5. C'est la plus petite différence.
- **La mémoire anti-redite** (Q4) tourne dans `executer`, que la classe neuve ne surcharge pas. La v3 le dit : elle tourne, écrit `memoire.json` dans le dossier de sortie, n'est servie à personne et n'entre ni dans les classes, ni au registre, ni dans les mesures. Épreuve : classes et registre égaux à l'octet avec une mémoire factice. Sinon, surcharger `executer`, ce qui est plus lourd.
- **Les cases par génération** (Q4) : une copie de la configuration par génération, dérivée par programme de la configuration scellée et du tirage scellé (cases de la forme `[identifiant, ligne de case]`), son empreinte journalisée et lue par l'arrêt n° 14.
- **Les statuts** (Q5) : la surcharge lit le statut, `refus["evenement"]` et `erreur`. Pour Minuit et Luc, le refus pour crédit ne se lit qu'au journal du relais : la v3 dit comment l'arrêt n° 13 le lit. *Proposition à la mère* : une erreur de cause non établie sur une clé Claude est classée « réponse illisible » pour un proposeur, et arrête la course si le relais montre un refus pour crédit.
- **Les coûts par rôle sur trois générations** (Q8) : le lot 7 ou le lot 8 lit `consommations.json` de chaque génération ; la reprise de `couts_generation` de L10, qui ne rend que des totaux, est retirée du § 1.2.
- **La forme de la fiche servie au portier et aux juges** (Q1, tableau A) : `## La fiche`, la clôture JSON et l'indentation sont déclarées à l'additif, octet pour octet, avec les consignes de D3. *Ma lecture* : D2 porte sur l'enveloppe du proposeur (V9, l. 77), non sur la requête du portier ; je ne suis pas le relevé qui veut « retirer » cette forme.
- **Le lieu de fuite** : L9, l. 2667 à 2669 (Q14) ; à fermer au lot 8.

### 3.10 Une réserve pour la mère, née de D2 et de D7 ensemble

Sans le texte système retiré, aucune espèce ne reçoit plus de syntaxe de sortie (L0, Q1). Or D7 ne lit « accepte » à la sonde qu'au vu d'au moins une fiche complète au contrat. Une espèce qui répond en prose déclencherait l'arrêt n° 27 et refuserait le départ. Je ne rediscute pas D2 ; la v3 doit nommer ce risque, déclarer les syntaxes lues, et dire que le taux d'illisibles se lit d'abord à l'essai par le faux fournisseur, puis à la sonde.

## 4. Le calendrier et les lots, après ces contradictions

1. **Le lot 4 change de nature.** Il devient la surcharge d'`appel` (routage, part, motifs, journal, refus avant le noyau, lecture qui rend toujours un objet), l'adaptateur Claude neuf avec sa conservation, la lecture des statuts et du journal du relais, et le relevé au faux fournisseur de ce que l'outil envoie sans texte système. Compter 4,5 à 5 h au lieu de 2,5 h. La surcharge vit dans une classe mère ou un mélange que le lot 6 compose : écrire cette interface au mandat.
2. **Lot 5** : validateur et lecteur neufs, champ `case`, caviardage, champ en plus : 4,5 à 5 h au lieu de 3,75 h.
3. **Lot 6** : copie de la configuration par génération, six étapes neutralisées, `fournisseurs_requis` et `hors_course`, mémoire déclarée, gardes héritées et refus écrits, délai A3 : 5,5 à 6 h au lieu de 4,75 h.
4. **Lot 8** : table des noms (`TYPES_PERMIS`), coûts par génération, fuite de la l. 2667 : 6 à 6,5 h au lieu de 5,5 h. L'identifiant réencodé (§ 3.7) ajoute 0,5 à 1 h aux lots 5 et 6.
5. **Chemin critique.** Les lots 4 et 5, tous deux autour de 5 h, sont à égalité : 2, 3, 4 ou 5, 6, 8, 9 font environ 26 à 28 h de lots, le lot 0 étant fait. S'y ajoutent la v3 et sa contre-lecture (environ 3 h), désormais sur le chemin avant tout mandat. Le relevé au faux fournisseur du § 3.2 entre aussi sur le chemin, avant l'additif.
6. **Attente honnête : de l'ordre de 48 à 60 h d'horloge** au lieu de 40 à 50 h. Le véhicule serait contre-lu le 24 au plus tôt, avec un départ le 25 ou le 26. **L'échéance demandée du 27 tient, avec une marge mince ; ce n'est pas une demande large.** La v3 rechiffre ses lots, ce que la v2 n'a pas fait (RC2, § 6, point 3).

## 5. Ce que la v3 doit porter (liste)

1. Les décisions de 07:21Z, points 1 à 6, comme tranchées ; les lignes de compte écrites toujours, compte nul compris ; la colonne éteinte par défaut.
2. Le routage, la part, la garde de motifs, le journal et l'égalité dans une surcharge d'`appel` (§ 3.1) ; la phrase fausse sur le portier retirée.
3. Le refus avant `super().appel` : « non envoyé », coût nul, compté dans les refus, hors du suivi (§ 3.3).
4. L'adaptateur Claude neuf sans texte système ; le relevé de ce que l'outil envoie, au faux fournisseur, au lot 4 et avant l'additif (§ 3.2).
5. La conservation des réponses brutes de Minuit et de Luc par cet adaptateur (§ 3.4).
6. Ni `preparer` ni `valider_contenu` : un validateur et un lecteur neufs ; le sort d'un champ `case` différent, proposé à la mère ; pas de caviardage avant la classification (§ 3.5).
7. Les gardes héritées nommées une par une, pour tous les rôles, en refus écrits (§ 3.6).
8. L'identifiant de fiche et celui servi au juge réencodés sans suite hexadécimale (§ 3.7).
9. `fournisseurs_requis` surchargé ; les rôles jamais appelés désignent `hors_course`, refusé par le routage (§ 3.8).
10. Six étapes neutralisées ; mémoire déclarée ; configuration par génération ; statuts et arrêt n° 13 sur les clés Claude ; coûts par rôle lus dans chaque génération ; forme de la fiche servie déclarée ; fuite de la l. 2667 de L9 (§ 3.9).
11. Le risque né de D2 et de D7 ensemble, nommé (§ 3.10).
12. Le point 8 d'A69 v4 (§ 7) : la relecture des classes, du statut et des refus par comptes.
13. Les numéros de question du lot 0 alignés sur le relevé.
14. Le calendrier rechiffré lot par lot (§ 4).

— contre-lecteur de la conception du véhicule, modèle O

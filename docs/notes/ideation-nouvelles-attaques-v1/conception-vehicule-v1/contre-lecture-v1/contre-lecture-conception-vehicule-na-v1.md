# Contre-lecture de la conception du véhicule — course « nouvelles attaques » — v1

- Contre-lecteur neuf, modèle O (règle R2). Je n'ai écrit ni la conception, ni l'inventaire, ni la v9, ni aucun orchestrateur.
- Date (UTC) : 2026-11-21 ; relevé de `date -u` : 07:07:29Z, après la lecture, avant l'écriture.
- Processeur seul : aucun appel, aucune clé lue ni nommée, aucune dépense, aucune écriture dans un dépôt. Rien ouvert sous `archives-reponses-modeles/` ni sous `/root/.claude/`. Aucun refus de permission, de classifieur ni de garde rencontré.

## Pièces lues et empreintes

| pièce | empreinte | contrôle |
|---|---|---|
| mandat du concepteur | `d2130f6b0aab5d4d32f01f51acd71b23cc3d1623769b24cd4d6fb06317c19af2` | égale au compagnon |
| conception (CO) | `675f8d39dc64548f34e36763b3a523277d9c1daa1c208e3b2b678dd9f79ace9b` | égale au compagnon et à l'empreinte du mandat de contre-lecture |
| rapport du concepteur (RC) | `ceffd7aac588e1243828679cb6b9db615c80f1476c68a79e59e75571ed72bff7` | égale au compagnon |
| table d'empreintes du concepteur | `0ac3143bec2073c2d1b9a7e437628b8207893975ccf3425f8ae3c10aafa96a0c` | égale au compagnon |
| inventaire de l'allumage (IN) | `0737906f9901de39ddd9b1585679b5b44e6bac67e7051a10374d3e0e496c06e0` | égale au compagnon |
| gabarit des témoins | `a84de0bf3168d93dda6928e2e165c14ecb8b091e976a629ace828813c24c89c0` | égale au compagnon |
| v9 (V9), `origin/main` après `fetch` (tête `dd3af98e9`) | `864f39a7ecd41a613f8892efbf66607c14da34252d643a4fd40032b5d2b500c2` | égale au compagnon |
| additif 1 v5 (A1) | `9f731795cd8b9166ad8b78346e3d37c7352010ea0edd1f34ac86cfb0ac689200` | égale au compagnon |
| complément v3 (CV) | `b4ef87dc6d5cce138f76457771c4cff18b84dfde662916841fc6386d77e202b2` | égale au compagnon |
| additif au complément, espèce 3 sur Minuit, v2 (AC) | `ce76e0d6a0a6e65ffb99f68d9efced8d26e205ed0e2cf11c0e2469b69f672388` | égale au compagnon |
| ordre de course v3 (OC), devis v11 (DV) | lus par extraits ; empreintes à la table du concepteur | — |
| `registres/go.md`, `registres/decisions.md` | copies de lecture `lecture-go-origin-main.md`, `lecture-registre-origin-main.md`, exclues du versement | GO-2026-11-20-67 (l. 598), GO-2026-11-21-02 (l. 601) ; R-4381, R-4383 |
| rapport du développeur v68 (R68) | `ad42b7229a8e37aae823b1041a3acf1db91ee4053f5fec61136b6fd178b59aa6` | égale à la table |
| contre-lecture v68, manifeste du paquet | `d2cfeac1…`, `4ed9fd8e…` | égales à la table |
| `course2_v68.py` du paquet | lu l. 150 à 386 | — |
| lanceurs L9, L10, épreuve E9 | `1b47c1cf…`, `f4196ec5…`, `5be161fa…` | égales à la table |
| additif des interrupteurs v69, **v4 scellée** (A69v4) | `cb352811f0202aa530fa4fd94de1d7ed4e6a8d589584c06c24c915e3c73bb578` | égale à R-4131 ; § 7 lu |
| orchestrateur, `/home/user/lciric/ideation-organism`, tête `a41b7b50f7c64ce488c120bb89ad3d25fb1dd1cb` | `noyau_v56.py` `eb5a003e…` (égale) ; `suivi_roles_v54.py` `620225973d68670a56ca913cdd02709fa576fa43e1393d166915ea67c1d7c3bb` | lecture seule |

## Verdict

**À corriger.** La base est la bonne et les faits cités sont vrais ; les décisions de la mère sont portables sans refonte. Mais deux manques majeurs touchent le cœur hérité (gardes du noyau que la v9 ne porte pas ; coût compté pour un envoi refusé), le chemin critique est faux, plusieurs épreuves manquent, et deux propositions débordent de la lettre sans être portées comme décisions.

## 1. Le choix de base

1.1 **Plus petite différence : oui.** Noyau, budget d'une génération, garde de budget de la course, juges, coffre et relais gardés ; lanceur L9 (seul porteur réel de cette composition) plus deux lectures de L10. Je ne vois pas de base plus proche.

1.2 **« La v68 seule joue plusieurs générations sous un plafond de course » : vrai à ses sources.** OC, l. 25 ; R68, § 3, point 3 (`GardeBudgetCourseV68`, réservation au pire, arrêt avant le poste) ; trois mutations, R68, § 4. La v59 jouait deux générations, mais sans garde de course (R68, § 1).

1.3 **« La v68 refuse le moteur réel par construction » : vrai.** Le refus est dans son lanceur `demonstrations/ideation_v68.py` : `MoteurReelRefuseV68` est levé « toujours », éteint compris (R68, § 4, l. 48 ; essai à blanc, l. 84). Un second refus est dans la bibliothèque : `verifier_regime_v68` refuse la lecture sans étage (`course2_v68.py`, l. 235 à 237), et `executer_course_v68` l'appelle (l. 303). **Comment le véhicule le lève sans toucher au paquet** : par deux fichiers neufs, un lanceur de l'orchestrateur et une fonction de course neuve (CO, § 2.9). C'est juste, mais CO, § 1.2 range `executer_course_v68` parmi ce qui est « gardé sans y toucher » : elle ne peut pas être appelée dans ce régime. *Correction* : écrire qu'elle sert de modèle et n'est pas appelée. De même, `GenerationV68.__init__` passe l'héritage à `verifier_heritage_selection` (l. 164) et n'accepte que l'objet de sélection v68 : la classe neuve doit lui passer `None` et servir le registre par son propre `_proposer`. Le dire, pour que le développeur n'hérite pas d'un refus.

1.4 **« Le lanceur 11 n'a aucun code » : vrai.** `scripts/lancer_course_auto_conception_v11.py` est absent du disque (vérifié par son chemin, règle R11). Les « lanceur v11 » du registre (R-497, R-3257 et suivantes) sont d'autres lignées. Il n'existe que par A69, § 7.

1.5 **Mais CO suit A69 dans sa v1 non scellée** (CO, § 10, point 3), alors que la v4 est scellée (R-4131). Le § 7 de la v4 ajoute au point 7 : « le relevé de ce qui reste sur chaque clé avant et après la course (R-3209, point 2) ». La table de CO, § 2.11 ne porte pas ce relevé de fin. *Correction* : reprendre la table sur A69v4, § 7, et y ajouter ce relevé.

1.6 **« 69, 70 et 71 déjà pris » : vrai.** R-2548 (l. 2507), R-2599 (l. 2558) et R-2620 (l. 2579) sont les codes v69, v70 et v71 du pilote MR-2, dans un arbre `organisme/orchestrator/…`. S'y ajoutent les noms v69 et v70 réservés au palier 1 (OC, l. 12 ; V9, l. 402). D1 (série NA-1, `_na_v1`) est donc fondée ; elle est portée en CO, § 1.4.

1.7 **D10** : le versement s'est fait sur `verse/vehicule-na-v1`, une branche tirée de `main` (R-4381, R-4383), et non sur `main`. Les chemins et les empreintes que le lanceur épinglera doivent citer le commit de cette branche.

## 2. Couverture : chaque fonction et chaque arrêt confié au véhicule

Couverts, avec module, cas sain et artefact : n° 1 à 19 et n° 27, dont le n° 11 pour un compte payant et pour le troisième relais (AC, l. 105 à 110, 175), et le n° 12 étendu avec l'artefact « envoi adressé à Rigaud » (AC, l. 88, 175). Les gardes sans numéro de CO, § 6.2 sont justes. **Ce qui manque :**

2.1 **(majeur) Des gardes héritées du noyau, que la v9 ne porte pas, ne sont ni relevées ni éprouvées.**
- *A3* : un nombre fixé d'échecs consécutifs arrête le rôle, et ses appels suivants ne sont plus lancés (`suivi_roles_v54.py`, l. 5 à 7 et 82 à 83 ; `noyau_v56.py`, l. 155 à 160, `appel-saute-role-arrete`). Un appel est un « échec » dès que `lire` rend `None` (l. 72 à 77). Or une « réponse vide motivée » ne porte aucune fiche, et `_fiches_ou_none` la rend donc inexploitable. Un proposeur qui répond à bon droit sans fiche à quelques cases de suite peut ainsi être arrêté sans bruit. Cela contredit V9, l. 97 (« jamais un refus »), l. 101 (« la course continue »), M6, et les 55 appels figés (A1, l. 142, 161).
- *A14* : au-delà d'une part d'appels inexploitables, l'étape est marquée « technique » (`noyau_v56.py`, l. 273 à 278).
- *Les autres* : A11 et A2 (modèle servi différent, `noyau_v56.py`, l. 176 à 185 ; `suivi_roles_v54.py`, l. 63 à 67) ; la coupure au plafond du relais, qui rend `None` (l. 150 à 154) ; 11a (l. 280 à 282).

*Correction* : une question 12 au lot 0 (toutes les gardes héritées, fichier et ligne). Chacune est soit rattachée à un arrêt de la v9 (A2 à « aucune bascule », V9, l. 182 ; 11a à l'arrêt n° 6), soit rendue inerte par une valeur déclarée à l'additif. Une garde gardée sans arrêt de la v9 est une proposition à la mère. Épreuve : des réponses vides motivées consécutives d'un proposeur ne l'arrêtent pas, et chacune est classée.

2.2 **(majeur) Un envoi refusé par l'adaptateur gardé est compté comme dépensé.** L'adaptateur gardé lève son refus à l'intérieur de `lancer` (CO, § 2.3). Dans `appel`, le bloc `finally` compte alors `cout = plafond` et l'inscrit au coffre et au cumul de la génération (`noyau_v56.py`, l. 163 à 175). Ce cumul nourrit `GardeBudgetCourseV68` et M4 pour un appel jamais parti. *Correction* : décider la voie du refus (refus levé avant le noyau, ou coût déclaré nul, marqué « non envoyé ») ; épreuve : un refus des arrêts n° 12 ou n° 16 laisse le cumul et M4 inchangés, et le journal dit « non envoyé ».

2.3 **D2 a une conséquence à écrire.** `lancer(role_kit, consigne, …)` (l. 165) laisse l'adaptateur ajouter un texte fixe de rôle. Sous D2 (« rien n'est ajouté »), CO, § 2.3 et § 9, point 2 ne gardent qu'une branche : ce texte est retiré, par un réglage déclaré et sans modifier l'adaptateur. Sinon un texte non nommé part (V9, l. 73). Le lecteur de fiches accepte les deux syntaxes (lots 3 et 5).

2.4 **Épreuves absentes du § 6** :
- la clé n° 30 (A1, l. 79 à 82) : n = 0 ne tire rien ; une seule case est tirée parmi les seules cases de sabotage ; aucun second tirage ;
- l'identifiant tiré par la clé n° 40 : un mot que la garde refuse arrête le tirage par un refus nommé (CO, § 5.2, écrit mais sans ligne d'épreuve) ;
- la case « autre, à nommer » (V9, l. 110) : le champ fermé égal à cette chaîne passe ; la supposition écrite dans le champ fermé donne « hors case » ;
- la course arrêtée (V9, l. 362) : mesures sur les seules générations complètes, sous le titre de l'arrêt ; M1 et M2 « sans objet » si seule la génération 1 est complète ;
- le plafond de chaque relais égal à la part de sa clé (V9, l. 235 ; A69v4, § 7, point 7) : un relais déclaré au-dessus est refusé ;
- M4 ne lit pas le cumul par clé (V9, l. 156) ;
- aucune valeur de clé recopiée (IN, § 4.2) : un marqueur planté dans une variable factice est absent des manifestes et de l'écran ;
- les réponses brutes conservées (V9, l. 396) : dans CO, une simple question du lot 0 (n° 10), sans épreuve.

2.5 **Le lot 0 ne lit pas L9**, alors que le lot 8 (5,5 h) le dérive et que le concepteur n'en a lu que l'empreinte (RC, § 2.2). Ajouter : la structure de L9, ce qui est retiré, et le lieu où L9 recopie la sortie d'erreur. CO, § 2 le tient aujourd'hui de L10, l. 2998.

2.6 CO, § 9, point 13 met les chaînes de requête de la classe (i) au lot 7 ; la table du § 7 ne les porte pas. À aligner.

## 3. Les lots

3.1 Le découpage est faisable par un développeur O et vérifiable par S : interfaces au § 5, épreuves par lot, mutations. **Sauf le lot 8** : un fichier neuf de l'ordre de 3 000 lignes tiré de L9 ne se vérifie pas en 1,5 h. *Correction* : le rendre comme différentiel lisible contre L9, avec la liste des fonctions retirées, gardées et ajoutées ; S vérifie le différentiel.

3.2 **Dépendances.**
- Le lot 7 est dit joué « en même temps » que le 6 alors qu'il dépend de ses formats : figer les formats au mandat (§ 5), ou jouer 7 après 6.
- Manquent à la table des dépendances hors code : la liste des motifs (F) pour les lots 2 et 9 ; les consignes du portier et des juges (D3) et les témoins scellés pour le lot 9. Les témoins sont écrits par un agent de la mère et ne se scellent qu'après le tirage (CO, § 5.2).
- L'additif scellé est attendu avant l'épinglage du lot 8.

3.3 **Le chemin critique est faux.** Le lot 2 (2 h) est plus long que le lot 1 (1,75 h), et le lot 5 (3,75 h) plus long que le lot 4 (2,5 h), tous deux en parallèle. Le chemin est donc 0, 2, 3, 5, 6, 8, 9, soit **24 h**, non 0, 1, 3, 4, 6, 8, 9 (22,5 h, CO, § 7 et § 8).

## 4. Le calendrier

4.1 **D3 est compté** (2,25 h, CO, § 8), mais serré pour deux textes servis, passés à la garde de motifs, attestés « aucune recette » et scellés. Les textes de cette course ont demandé de trois à cinq allers et retours (CO, § 8). Il faut compter 3 à 4 h, hors chemin critique s'ils partent tout de suite.

4.2 **Les 31 h, puis 14 h, sont une borne basse, non une attente.** Elles supposent un seul tour de correction par lot, aucune attente de scellement de la mère, aucune limite d'usage et aucune réponse du lot 0 qui contredise la conception. Les points 2.1 et 2.2 en ajoutent au moins une. Avec le chemin critique à 24 h et la contre-lecture du véhicule entier, 30 à 36 h d'horloge est le cas sans incident. Une attente honnête est de 40 à 50 h, soit un véhicule contre-lu le 23 au plus tôt et un départ le 24 ou le 25. L'échéance du 22 ne tient pas (accord avec CO) ; le 26 (D9) tient, avec une marge mince.

## 5. D11 — proposition d'artefact pour l'arrêt n° 12

**Ce qui fixe l'objet de l'arrêt** :
- V9, l. 383 : « un appel d'un rôle se présente sur une autre clé que la sienne » ; artefact : « un appel du juge de l'espèce 3 présenté sur la clé du proposeur de l'espèce 3 est refusé » ;
- V9, l. 402 : « un routage des appels par rôle, non par espèce (le proposeur et le juge de l'espèce 3 sont sur deux clés), éprouvé à l'arrêt n° 12 » ;
- A1, l. 169 : « l'artefact de l'espèce 6 est retiré de l'épreuve, les trois autres cas restent » ;
- A1, l. 172 : « trois relais et cinq clés, routées par rôle » ;
- CV, l. 120 : l'artefact vaut pour la course, non pour les lignes à part.

L'objet est donc de montrer que **la table est lue par rôle, non par espèce**.

**Constat.** Sous GO-2026-11-21-02 (AC, l. 56 à 58), aucune espèce n'a plus deux rôles sur deux clés : l'espèce 3 est entière sur Minuit, l'espèce 1 entière sur le deuxième relais. L'aiguilleur n'a pas de numéro d'espèce (DV, l. 165). En course, un routeur par espèce et un routeur par rôle rendent la même clé pour tout appel. L'artefact proposé en CO, § 9, point 17 (« le juge de l'espèce 3 sur la clé de l'aiguilleur ») éprouve « un rôle sur une autre clé », déjà éprouvé par CV, l. 166 et AC, l. 175 ; il ne garde pas l'objet « par rôle, non par espèce ».

**Proposition (marquée, à la mère ; elle change la lettre d'une épreuve) :**
1. **Cas sain neuf** : le juge et le proposeur de l'espèce 3 sur Minuit sont lancés, et chacun est compté sur Minuit, la part cumulant les deux rôles (AC, l. 72). L'ancien artefact devient un cas sain : refusé, il arrêterait à tort un appel permis.
2. **Artefact en course** : un appel de l'aiguilleur présenté sur Minuit est refusé, avec l'arrêt nommé. Minuit est sa clé à l'épreuve des témoins (AC, l. 122), non sa clé en course, Luc (AC, l. 57). C'est le seul rôle qui change légitimement de clé entre une ligne à part et la course : l'artefact éprouve qu'un rôle présenté sur une clé qui porte déjà des rôles de la course est refusé, et que la table de la course ne lit pas celle des lignes à part (R-4306 ; CV, l. 120).
3. **Artefact sur table plantée**, qui garde l'objet mot pour mot : une copie de la table des rôles et des clés, marquée artefact, jamais chargée par la course (donnée à la course, son empreinte est refusée par l'arrêt n° 14). Le juge et le proposeur de l'espèce 3 y sont sur deux clés distinctes, comme dans la répartition de GO-2026-11-20-22. Un appel du juge de l'espèce 3 présenté sur la clé du proposeur de l'espèce 3 y est refusé. **Mutation** : le routeur remplacé par une recherche par espèce laisse passer l'artefact, et l'essai doit échouer.
4. L'artefact de CO (juge de l'espèce 3 sur Luc) peut rester en plus ; les artefacts de CV, l. 166 et d'AC, l. 175 restent.

## 6. Rien hors de la lettre

6.1 Sont marqués et tranchés : D1, D4 à D7, D10, D11 (R-4381) ; le pire d'un appel d'aiguilleur et de juge reste non fixé (CO, § 2.3) ; les témoins sur la première case de la réserve sont une proposition marquée (§ 5.2).

6.2 **Déborde, et n'est pas couvert par D5** : CO, § 9, point 3 ajoute qu'« un champ `idee` au-dessus de sa borne sort la fiche du contrat à la réception ». D5, telle que la mère l'a prise, ne dit que « identifiant et champ `idee` sur une ligne ». La règle ajoutée devance l'arrêt n° 19, dont c'est l'objet (V9, l. 390), et retire une fiche sans classe nommée : c'est un repli silencieux, ou une classe neuve. Elle doit rester une proposition, à la mère. Même statut pour « lignes de compte seulement pour un compte non nul ».

6.3 **Écart à un texte scellé, non porté comme décision** : CO, § 9, point 11 propose deux lectures scellées des mesures, M5 plus tard, alors que V9, l. 315 dit « lues une fois ». C'est un écart à un préenregistrement scellé, donc un nœud de Lazar. Il doit figurer au rapport comme décision (D12), non parmi les « autres points ».

6.4 Sous D2, CO, § 2.3 (« l'additif le déclare comme enveloppe ou le fait retirer ») ne garde que « retirer » (point 2.3).

## Écart du contre-lecteur

Un `git show` du compagnon de la v9 a été lu sur la sortie standard au lieu d'être redirigé vers mon dossier : 98 octets, une empreinte et un nom de fichier, contraire à l'en-tête. Aucun autre.

— contre-lecteur de la conception du véhicule, modèle O

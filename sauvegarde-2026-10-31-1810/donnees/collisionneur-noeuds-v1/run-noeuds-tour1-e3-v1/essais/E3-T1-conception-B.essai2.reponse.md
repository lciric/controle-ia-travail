# Proposition B — Tour III.1 — Nœuds de décision au 31 octobre 2026

---

## N1. Bisociation à deux espaces : que faire après l'échec de V5

### (a) Ce que la question suppose sans que ce soit établi

| Supposition | Statut | Source |
|---|---|---|
| Le diagnostic (200 mondes d'essai, une graine de flux) est représentatif du comportement du générateur | OBSERVÉ-NON-AUDITÉ | Pièce 2, §1.1 : les ordres se reproduisent mais erreurs types naïves, une seule graine |
| La cause principale (étiquettes d'opérateur hors S16d) explique la majeure partie de l'écart | OBSERVÉ-NON-AUDITÉ | Pièce 2, §2 : variantes convergentes mais implémentation unique |
| L'erreur type 0,29–0,60 pour une différence entre statuts rend le seuil 0,5 indiscriminant | OBSERVÉ-NON-AUDITÉ | Pièce 2, §1.4 : naïf, ponts supposés indépendants |
| La redéfinition T2 (0,137/0,134) serait « presque acquise par construction » | HYPOTHÈSE | Pièce 2, option A : pas de calcul formel montrant que T2 est triviale ; la formulation est celle de l'auteur, non un résultat |
| Modifier V5 après lecture du résultat de validation est légitime si déclaré | HYPOTHÈSE | La liste d'arrêt dit les deux choses opposées (Pièce 3) : aucune règle ne tranche le conflit |

### (b) Expérience décisive

**Duel : H_A « Le changement de texte (T2) ne détruit pas la capacité de V5 à détecter un défaut de rareté » vs H_B « T2 est triviale et ne détecte aucun défaut réaliste ».**

- **Métrique.** Sous un générateur délibérément défectueux G* (un statut reçoit des étiquettes de concept rare deux fois plus fréquentes que les autres, écart de fréquence planté ≥ 1,0), mesurer l'écart T2 sur 300 mondes par condition (M_bien et M_moyen).
- **Seuil.** T2 ≥ 0,5 sur les mondes de G* (le seuil gelé S13), avec erreur type ≤ 0,15.
- **Contrôle négatif.** Sur le générateur scellé (G inchangé), T2 ≤ 0,2 (déjà mesuré : 0,137/0,134).
- **Ce qui falsifie H_A.** T2 < 0,3 sur G* : le critère redéfini est aveugle à un défaut planté grossier.
- **Ce qui falsifie H_B.** T2 ≥ 0,5 sur G* et T2 ≤ 0,2 sur G scellé : le critère sépare bien.
- **Coût.** ≈ 50 s × 4 runs = 200 s de processeur (illustratif, d'après Pièce 2). Zéro USD.
- **Pièce qui trancherait.** Un script empreinté jouant G* et le générateur scellé sur les indices 990200–990499, avec la fonction `v5_rarete` scellée et la variante T2, avant d'écrire la v3.

**Mon option : B (T2 + ancienne grandeur en rapport sans seuil), confiance 0,60.**

Raisons. (i) Le diagnostic établit que le seuil 0,5 est au niveau du bruit de la statistique scellée (Pièce 2, §1.4 : erreur type 0,29–0,60 pour 200–300 mondes) ; le critère scellé ne peut pas fonctionner, même avec un générateur parfait. C seul (générateur) ne suffit pas : 1,29/2,27. D échoue en M_moyen (0,83). E est disproportionné. A sans l'ancienne grandeur en rapport perd toute visibilité sur le risque que la rareté de l'étiquette retenue sépare vrai de faux (CB-05, Pièce 2, §2). (ii) L'écart déclaré « critère gelé modifié après lecture » est le prix à payer ; la seule condition est que la v3 nomme en toutes lettres ce qu'elle a lu, le change, et utilise des graines neuves.

**Pire cas de B.** T2 ne détecte rien ; la porte V0 est rouverte par un critère trivial. **Garde.** Le test de G* ci-dessus. Si G* ne sépare pas, l'option manquante s'impose :

**Option manquante F.** Redéfinir V5 sur T2, **et** ajouter une seconde garde V5bis non triviale : l'écart de l'ancienne grandeur (cinq statuts) ne dépasse pas un seuil **plus large** (par exemple 3,0 — illustratif, à calibrer sur l'erreur type à 300 mondes) pour piéger une dérive grossière, sans bloquer le bruit. V5bis est un rapport-avec-seuil, non un critère du type de T2.

---

## N3. Pré-pilote, décision D-j (Gu-Krenn sans reproduction)

### (a) Suppositions

| Supposition | Statut | Source |
|---|---|---|
| Le vocabulaire du contrôle des IA est absent de leurs 37 960 concepts | VÉRIFIÉ | Pièce SD-4, §5 : « probe, steering, monitoring, alignment n'existent qu'au sens physique » |
| Le substitut inspiré (S31) peut fonctionner sur une autre source | HYPOTHÈSE | Pièce 5 : « à ajuster sur un essai de la moisson », aucune mesure |
| L'absence de reproduction ne compromet pas la chaîne de bisociation | HYPOTHÈSE | La chaîne est éprouvée indépendamment du bras (É7b) |
| Aucun poids publié, réentraînement obligatoire | VÉRIFIÉ | Pièce SD-4, §4.2, Pièce SD-3 R-873 |

### (b) Expérience décisive

**Duel : H_A « Le substitut inspiré produit des paires exploitables pour les juges même sans reproduire le modèle original » vs H_B « Sans reproduction, les paires du bras sont du bruit et le bras est inutile ».**

- **Métrique.** Aire appariée du substitut (« jamais reliés, deux concepts actifs ») sur la moisson, par rapport à un tirage aléatoire parmi les paires éligibles.
- **Seuil.** Aire appariée ≥ 0,55 (illustratif : au-dessus du hasard de 0,05 en estimation ponctuelle, avec ≥ 200 paires positives).
- **Contrôle négatif.** Tirage uniforme parmi les paires non reliées : aire attendue 0,50.
- **Falsifie H_A.** Aire < 0,52 : le substitut ne distingue pas les paires qui se relient.
- **Falsifie H_B.** Aire ≥ 0,55 et au moins 200 paires éligibles.
- **Coût.** Processeur seul, ≈ minutes (illustratif). Zéro USD.
- **Pièce qui trancherait.** L'essai de S31 sur la moisson, exigé par le brouillon 7 et non encore réalisé (Pièce 4, point 10 : « essai de S31 sur la moisson »).

**Mon option : oui (D-j accepté), confiance 0,55.**

Raisons. (i) Le substitut ne repose sur aucun poids du modèle de Gu-Krenn ; il est une règle indépendante (« jamais reliés, deux concepts actifs »), pas un produit de leur réseau. (ii) Le pire cas (bras inutile) produit une fusion inutile, filtrée par les juges ; il ne corrompt aucun autre instrument. (iii) Le bras Gu-Krenn, qu'il fonctionne ou non, est une entrée dans C12 (Pièce 4, §5) : s'il est « non produit », C12 passe de 0,97 à 0,86 et la porte de 0,16 à 0,14 (Pièce 9, D-h option (b)). Le conserver, même en substitut, protège C12.

**Pire cas.** Le substitut est un filtre nul ; la paire retenue est aléatoire parmi les éligibles. **Garde.** L'essai de S31 sur la moisson, qui doit précéder É0 (A19, Pièce 7 ligne 20–21). Si l'essai échoue (aire < 0,52), le bras est « non produit (source absente) » et le coût est nul.

**Option manquante.** Accepter D-j = oui, mais avec un **seuil de non-vacuité explicite** pour le substitut : si S31 ne fournit pas au moins 5 paires éligibles distinctes sur la moisson (illustratif), le bras est « non produit ».

---

## N4. Annexe du bras méta — profil vide dans la majorité des lots

### (a) Suppositions

| Supposition | Statut | Source |
|---|---|---|
| Loi a priori des niches (n1 0,30 … n6 0,05) | SUPPOSÉ | Pièce 13, §6 : « SUPPOSÉ partout » |
| Accord des deux lecteurs par fiche 0,7 | SUPPOSÉ | Pièce 13, §6 |
| Probabilité de structure partagée 0,3 | SUPPOSÉ | Pièce 13, §6 |
| Les structures séquentielles imposées par le texte I (om_somme_cumulee_temps_arret, me_test_sequentiel_cusum, etc.) ne sont pas « quasi universelles » au même titre que les jeux de données | HYPOTHÈSE | Pièce 12, CA1-04 : argument identique, incohérence non corrigée |
| Le repli éprouve « la chaîne, non le profil » | VÉRIFIÉ | Pièce 12, §C ; Pièce 13, §6 |

### (b) Expérience décisive

**Duel : H_A « Le profil tel que défini distingue des paires qualitativement différentes de celles du repli (les juges notent différemment profil vs repli) » vs H_B « Profil et repli produisent des fusions indiscernables pour les juges ».**

- **Métrique.** Au pré-pilote, sur les paires du bras méta étiquetées « profil » ou « repli » : écart moyen de la note des juges entre les deux catégories.
- **Seuil.** Le pré-pilote n'a qu'une paire méta (Pièce 12, §C) : aucune puissance. Cette expérience est donc **différée à la course** (≥ 8 paires méta sur 4 sous-sessions). Le seuil est une différence de notes ≥ 0,5 point sur l'échelle des juges (illustratif).
- **Contrôle négatif.** Paires du bras basique, qui ne passent pas par le profil.
- **Falsifie H_A.** Différence < 0,1 point (illustratif).
- **Falsifie H_B.** Différence ≥ 0,5 point et profil > repli.
- **Coût.** Zéro USD au-delà du pré-pilote (mesuré dans la course).

**Mon option : (a) accepter le repli comme mesure au pré-pilote, confiance 0,65.**

Raisons. (i) Le pré-pilote n'a qu'une paire méta : aucune puissance pour tester le profil. Toutes les alternatives qui augmentent la chance d'avoir une paire du profil (b, c, d, e) touchent soit le plan (15 fiches), soit la décision du directeur (R-638), soit le sens de « faible ». (ii) Le pré-pilote éprouve la chaîne (lecture, paire, fusion, aiguilleur, juges), pas le profil ; c'est le but affiché de M9. (iii) Les structures « quasi universelles » (CA1-04) doivent être traitées : exclure les jeux de données mais garder les trois structures séquentielles imposées est incohérent.

**Pire cas.** Le profil n'est jamais éprouvé avant la course. **Garde.** (1) Écrire en tête de la demande d'approbation que le pré-pilote n'éprouvera que le repli dans ≈ 6 lots sur 10 (Pièce 12, §C). (2) Corriger CA1-04 : retirer `om_somme_cumulee_temps_arret`, `me_test_sequentiel_cusum` et `om_martingale_e_processus` du compte « forte » au même titre que les jeux de données, ou les garder tous — l'un ou l'autre, pas le mélange actuel. (3) Corriger CA1-01 : la paire n1–n2 fusionnée par le programme ne devrait pas être dans le profil (relever c(n1,n2) à 2).

**Option manquante.** Aucune qui ne touche pas R-638 ou le plan.

---

## N5. Orchestrateur, règle de non-lecture A21

### (a) Suppositions

| Supposition | Statut | Source |
|---|---|---|
| É5 est impossible sans la classe des témoins | VÉRIFIÉ | Pièce 14, §C point 2 : « S20/A6 et S18/S19/A7, impossibles sans la classe » |
| La v55 journalise la lecture au coffre | VÉRIFIÉ | Pièce 15, §CL19-03 et Pièce 19, R-685 |
| L'ordre des appels en É6 dépend de la classe (effet de bord) | OBSERVÉ-NON-AUDITÉ | Pièce 14, §C point 5 : identifiants opaques en v55 corrigent ce point |
| Une boîte tenue par session-depot est réalisable | HYPOTHÈSE | Pièce 15, lecture 2 : « une pièce de plus, une interface de plus, à éprouver » |

### (b) Expérience décisive

**Duel : H_A « La lecture par programme à É5, journalisée et bornée, n'introduit aucune dépendance de décision aux verdicts des juges » vs H_B « L'ouverture de la clé permet une fuite d'information qui biaise les résultats d'É6 ».**

- **Métrique.** Trace d'audit : ensemble des informations sorties de la boîte d'É5 (comptes et décision), comparé à l'ensemble des entrées d'É6 (identifiants des fiches, ordre).
- **Seuil.** L'intersection entre les sorties d'É5 et les entrées d'É6 ne contient aucun élément qui permette de distinguer une fiche P d'une fiche N.
- **Contrôle négatif.** Une exécution d'É6 avec un ordre tiré aléatoirement (identifiants triés par empreinte), puis comparaison des verdicts entre les deux ordres.
- **Falsifie H_A.** Un champ de sortie d'É5 permet de reconstruire la classe d'un témoin spécifique, et ce champ est accessible à l'orchestrateur avant É6.
- **Falsifie H_B.** La trace d'audit ne contient que des comptes agrégés (nombre d'ambigus, passe/nœud) et l'ordre d'É6 est trié par identifiant opaque.
- **Coût.** Relecture du code v55 (Pièce 15) : zéro USD, ≈ 1 h humaine.

**Mon option : (a) amender A21 et la ligne 30, confiance 0,70.**

Raisons. (i) Le brouillon se contredit (VÉRIFIÉ, Pièce 14, §C point 2) : toute option qui exige A21 à la lettre rend le Plan inexécutable. (ii) La v55 corrige déjà l'effet de bord (identifiants opaques en É6, É9 sur liste scellée). (iii) L'option (b) (boîte de session-depot) est correcte en principe mais ajoute une interface et un artefact à éprouver, pour un gain théorique : la lettre d'A21 est sauve, mais l'intention (aucune dépendance des décisions aux verdicts) est déjà satisfaite par (a).

**Pire cas.** Un futur contre-lecteur interprète l'amendement comme une brèche. **Garde.** (1) L'artefact de la ligne 30 couvre explicitement « lecture hors journal du coffre ». (2) La sortie de la boîte d'É5 est limitée par programme à un type `VerdicteE5(passe: bool, n_ambigus: int, n_P: int, n_N: int)` (illustratif) ; aucun identifiant de fiche.

**Choix de code à confirmer :**
- Choix 1 (nœud = arrêt) : **tenu**, cohérent avec O12.
- Choix 5 (N sans défaut vu = exclu) : **à remonter** ; le brouillon ne le dit pas, c'est un choix de code qui change A5. Écrire au brouillon 8.
- Choix 8 (n=2, pas de report) : **tenu**, lecture littérale ; écrire au brouillon 8.
- Choix 10 (indices de forme) : **à geler au préenregistrement**, pas dans le code. La crête injectée est un paramètre.
- Portée du plafond (CL18-11) : **par génération** pour N=1 (pré-pilote) ; pour N>1, le devis v6 raisonne sur un plafond global : cohérence à fixer au brouillon 8 avant la course.

---

## N6. Épreuve semi-réelle, DL-1 à DL-9

### (a) Suppositions communes

| Supposition | Statut | Source |
|---|---|---|
| Les hypothèses du théorème 1 de Khemakhem et al. sont satisfaites par la plantation en B-θ | HYPOTHÈSE | Pièce 17, DL-1 : « indicateurs entièrement synthétiques » |
| Temps unitaires de calcul | SUPPOSÉ | Pièce 17, DL-2 : « SUPPOSÉS » |
| La porte G0 (fin novembre) laisse 5,8 jours | VÉRIFIÉ | Pièce 17, résumé point 8 |
| La dérivée seconde croisée du mélange (condition 2.ii) est satisfaite par softplus à fuite | VÉRIFIÉ | Pièce 17, S19 : « PDF p. 6, vérifié » |

### (b) Mes options, avec duels

**DL-1 : option (2) — B-θ décide, B-hors descriptif. Confiance 0,60.**

- *Duel* : H_A « L'iVAE, dans ses hypothèses, identifie la cause plantée au-dessus du hasard en échantillon fini » vs H_B « L'identification ne fonctionne qu'en théorie ».
- *Falsifie H_A* : recouvrement ≤ seuil S9 en B-θ dans les deux conditions.
- *Falsifie H_B* : recouvrement ≥ S9 + 0,10 (illustratif).
- Raison : l'option (1) (hors théorème seul) rend l'échec ininterprétable ; l'option (3) perd la mesure de robustesse.

**DL-2 : option (2) — 5 graines, S15 = 140 h. Confiance 0,65.**

- Raison : 3 graines donnent 3 paires pour la stabilité (Pièce 17, DL-2) ; la variance graine-à-graine est le premier facteur de variance (référence à vérifier : Locatello et al., cité dans la Pièce 17). 140 h tolère des temps 1,26× plus longs (VÉRIFIÉ, Pièce 17, S15).

**DL-3 : option (1) — R2⁻ décisionnelle. Confiance 0,55.**

- *Duel* : H_A « La méthode détecte un effet de signe opposé » vs H_B « La méthode est asymétrique en signe ».
- Raison : un biais de signe non détecté n'est pas anodin en application causale. La puissance réduite (conjonction 0,818 vs 0,852) est le coût.

**DL-4 : option (1) — CITRIS hors gradation 1. Confiance 0,75.**

- Raison : donner la cible connue à CITRIS rompt l'homogénéité de l'information entre méthodes.

**DL-5 : option (1) — moitiés par paire, graine sans vérité. Confiance 0,70.**

- Raison : l'option (2) (oracle) ne correspond à aucun usage ; l'option (3) contredit la prédiction de l'auteur (Pièce 17, DL-5).

**DL-6 : option (1) si possible, sinon (2). Confiance dépend de l'acte du directeur.**

- Raison : quatre méthodes ont des SUPPOSÉ sur leurs hypothèses ; les PDF les lèvent. Mais l'obtention dépend de Lazar.

**DL-7 : option (2) — arbitrer S3, S8, S9 explicitement. Confiance 0,60.**

- Raison : ce sont les trois seuils qui ont des alternatives écrites (Pièce 17, DL-7).

**DL-8 : option (1) — échelle de trois définitions. Confiance 0,70.**

- Raison : l'option (2) est non exécutable sur la base minimale (21 < 22) ; l'option (3) pose la question R1 sans la résoudre.

**DL-9 : option (2) — T2b descriptif. Confiance 0,55.**

- Raison : les seuils 0,20 et 0,05 sont « choisis par l'auteur sans littérature » (Pièce 17, DL-9). Un critère à seuil non sourcé dans un rôle décisionnel est fragile. Le garder en descriptif préserve l'information.

---

## N9. Gu-Krenn, D-GK-1 : fenêtre du test HB

### (a) Suppositions

| Supposition | Statut | Source |
|---|---|---|
| Le modèle prédit l'impact (IR citations), pas l'apparition pure | VÉRIFIÉ | Pièce N9-1 : « HB est un transfert de tâche, déclaré » |
| Aire appariée ≈ 0,70 | SUPPOSÉ | Pièce N9-1 : « aucun appui publié » |
| Le retrait (option b) ôte d'abord les positives les mieux classées | HYPOTHÈSE | Pièce N9-1 : « biais contre le modèle à seuils fixes » |

### (b) Mon option : (a), confiance 0,65.

- *Duel* : H_A « Le modèle classe les paires qui se relient 2023–2026 au-dessus de celles qui ne se relient pas, à degré et âge égaux » vs H_B « Le modèle ne transfère pas à la tâche d'apparition ».
- *Falsifie H_A* : B-ii ≤ 0,60 (Pièce N9-1, seuil).
- *Falsifie H_B* : B-i ≥ 0,85 et B-ii > 0,60 et B-iii > 0.
- Raison : l'option (b) conditionne sur l'issue 2023, ce qui crée un biais de sélection (les positives les plus prévisibles sont retirées). L'option (a) évite ce conditionnement. L'autre fenêtre est rapportée de toute façon.

**Pire cas.** Les arêtes 2023 diluent le signal (le modèle classe bien les « faciles » de 2023 mais pas les « difficiles » de 2024–2026). **Garde.** Rapporter B-ii sur la sous-population 2024–2026 en information (attente : −0,01 à −0,05).

---

## N10. Robustesse adaptative dans la course 2

### (a) Suppositions

| Supposition | Statut | Source |
|---|---|---|
| Le texte de la course 2 est figé et ne pose pas la robustesse adaptative | VÉRIFIÉ | Question : « figé avant P-041 v2 et v3 » |
| Le pilote synthétique suggère que le levier est la capacité de la classe, pas le tirage | OBSERVÉ-NON-AUDITÉ | Question v10 : « sur racine d'essai » |
| Bailey et al. est absent des 23 papiers de la liste fermée | HYPOTHÈSE | Question : « vraisemblablement absent » |

### (b) Mon option : (b), confiance 0,60. Poser en génération 2.

- *Duel* : H_A « La course 2 (génération 1) peut produire des idées utiles sur la robustesse sans avoir lu le pilote » vs H_B « Sans le pilote et Bailey dans les pièces, les fiches sur la robustesse seront naïves ».
- *Falsifie H_A* : les fiches d'axe 3 mentionnant la robustesse ne proposent aucun levier au-delà du mélange uniforme.
- *Falsifie H_B* : au moins une fiche d'axe 3 propose un levier structurel (archive, capacité, contrainte d'entraînement).

Raisons. (i) La question est au plafond de taille. (ii) Rouvrir le texte que le pré-pilote doit éprouver (option a) retarde le pré-pilote et invalide les gardes déjà écrites. (iii) La génération 2 part du pilote lu et des fiches de la génération 1 comme base : elle est le lieu naturel.

**Le résultat du pilote change-t-il l'option ?** Non. Si le pilote confirme que le mélange d'équilibre perd contre un « ou » déterministe à classe égale, la conclusion (le levier est la capacité) renforce (b) : il faut d'abord finir le pilote avant de poser la question aux proposeurs.

**Pistes que la course devrait chercher (niveau méthode) :** leviers que l'attaquant ne contrôle pas à bas coût — l'**archive des attaques passées** (l'attaquant ne peut pas effacer ce que les moniteurs ont déjà vu), les **contraintes d'entraînement** (un attaquant qui doit rester utile ne peut pas tout modifier), et la **rotation des moniteurs** entre déploiements (l'attaquant ne sait pas quel moniteur sera tiré après la mise à jour).

---

## Ancrage matériel (d)

| Instrument / besoin | Modèle ou ressource | Calcul | Coût estimé |
|---|---|---|---|
| Diagnostic V5 (N1, test de G*) | `monde_v2.py`, `validation_v2.py` scellés | ≈ 200 s processeur | 0 USD |
| Essai de S31 sur la moisson (N3) | Script Python sur la moisson OpenAlex locale | ≈ minutes | 0 USD |
| Épreuve semi-réelle B-θ (N6) | iVAE (Khemakhem et al. 2020, implémentation à écrire), PCMCI (`tigramite`), DirectLiNGAM (`lingam`), témoins (`scikit-learn`), torch | ≈ 111 h processeur (5 graines) | 0 USD (processeur propre) |
| Reproduction Gu-Krenn (N9) | Impact4Cast (MIT), données Zenodo (CC-BY) | ≈ 8–30 h processeur par valeur d'IR (illustratif, Pièce SD-4) ou carte graphique louée | Nœud de dépense, devis séparé |
| Pré-pilote complet (N3, N4, N5) | Opus 5.5, Sonnet 5.5, Fable 5.1, Argon, Kimi via relais | ≈ 30–45 USD (Pièce 11) | GO-2026-10-31-03 : 50 USD |
| Pilote adaptatif (N10) | Moniteurs linéaires, attaquant 8B | Carte graphique | Devis à part (non estimé ici) |

---

## Ordre de tranchée proposé

1. **N1** (débloque la v3 de bisociation, dont dépend le bras basique du pré-pilote).
2. **N5** (débloque le brouillon 8, dont dépend le gel).
3. **N3 et N4** ensemble (débloquent le gel du pré-pilote, D-h (a) tranché).
4. **N9** (indépendant ; le test HB attend la moisson et la machine louée).
5. **N6** (bloqué par le verdict de la question 6, non rendu).
6. **N10** (différé à la génération 2 ; aucune urgence).

FIN-DE-CELLULE
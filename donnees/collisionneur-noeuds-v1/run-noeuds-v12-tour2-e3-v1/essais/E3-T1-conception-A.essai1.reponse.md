# Cellule A — tour III.1 (conception ciblée, à l'aveugle)

**Pièces reçues.** La synthèse du tour 1 (v2, se termine par « Fin », aucune coupure visible) et la question avec l'annexe v5. Les faits du tour 1 ne sont pas resservis : tout chiffre ci-dessous vient de la synthèse ou de l'annexe, sinon il est marqué *illustratif*. Rappel porté par la synthèse : la pièce 20 (N9-1) était tronquée au tour 1 ; ses seuils restent SUPPOSÉ. Je ne traite ni N2, ni N7, ni N8 (retirés). Je m'appuie sur les cellules B, C, D en le disant (B1) ; je ne les fusionne pas.

---

## (a) Ce que la question et l'annexe supposent sans que ce soit établi

1. **Annexe, provenance** : l'en-tête v4 portait une heure écrite en avance (R-1001) ; v3 et v4 « gardées » ne me sont pas servies. Je ne lis que v5 — VÉRIFIÉ sur le texte servi, mais la lignée est RAPPORTÉE.
2. **N1** : le retrait par conv-audit de « corriger le générateur » repose sur un diagnostic dont l'attribution (définition, non code) est **OBSERVÉ-NON-AUDITÉ** (200 mondes, une graine de flux, erreurs types naïves ; synthèse, N1 « Statut du point porteur »). L'annexe le traite comme acquis.
3. **N3** : « substitut S31 », « brouillon 10, l. 732 », R-718/R-719 : **SUPPOSÉ** (non dans la synthèse). La recommandation suppose l'essai du substitut faisable sur la moisson locale, point que la divergence 3 laisse ouvert.
4. **N5** : la recommandation (a) cite une contre-lecture qui écrit elle-même que (b) vaut mieux. Elle suppose donc une hiérarchie (« déjà codée » prime) qu'aucune pièce ne donne ; D a relevé en T3 que l'absence de décision ne doit pas valoir décision. CL19 : **RAPPORTÉ**.
5. **N6** : les heures, le calendrier (gel le 4 novembre, verdict vers le 27) et l'exigence de 2 600 paires-années calculée à une corrélation supposée 0,85 au lieu du seuil réel 0,70 : heures **SUPPOSÉ**, écart de seuil **VÉRIFIÉ** dans la synthèse (DL-5). « VS5-01 » et « brouillon 6 en cours » : **SUPPOSÉ**.
6. **N9** : population à fin 2022, fenêtre 2023-01-01 → 2026-09-30 : **SUPPOSÉ** (préenregistrement non servi) ; les seuils du test : SUPPOSÉ (pièce tronquée). La recommandation ne dit pas la date de l'instantané par rapport à la fin de fenêtre, dont dépend la fuite relevée par C et la minceur de la dernière cohorte relevée par D.
7. **N10** : « Bailey et collègues » — **référence à vérifier** ; je ne connais que « pièce 24, extrait empreinté » de la synthèse. La recommandation suppose un pilote « confirmé » qui n'est pas lu.
8. **N11** : (i) l'annexe suppose que le directeur a tranché (b) et (c) alors que conv-audit conteste (c) dans la même annexe — contradiction interne à la pièce ; (ii) elle suppose un oracle synthétique couvrant les trois bras, alors que le monde synthétique ne porte ni les niches ni les structures que lit le bras méta (apport A + B, non réfuté) ; (iii) « score de rétrodiction inversée d'E1′ » : **SUPPOSÉ** ; (iv) « intervalles par rééchantillonnage des mondes » suppose mesurable la variance du contraste entre bras, mesurée nulle part (transposition relevée au décompte de tête, que j'ai admise en T3).
9. **Global** : les quatre accords à quatre reçoivent la réserve du critère 10 ; je ne les compte pas comme preuve.

---

## (b)–(c)–(d) intégrés : verdicts par recommandation

Chaque verdict : raison ; pire cas si suivie et garde ; changement par rapport à mon tour 1. Les duels (B4) sont posés là où une pièce tranche.

### N1 — B, 0,6 → **tenue sous condition**
**Raison.** Seule la redéfinition passe, et l'ancienne grandeur rapportée sans seuil ne protège plus rien (synthèse, N1). Conditions : graines 500–799 ; écart déclaré sous les deux lectures de la liste d'arrêt ; plancher d'effectif par statut (sinon « non évaluable », porte fausse) ; **rejeu du diagnostic avant invocation** (seconde graine, 300 mondes, erreurs types par rééchantillonnage ; processeur, 0 USD) pour faire passer le point porteur d'OBSERVÉ-NON-AUDITÉ à VÉRIFIÉ.
**Duel D1.** H_A : l'échec vient de la définition — à la seconde graine, l'écart entre statuts à lois égales reste du même signe, à moins de trois erreurs types de 2,87, et l'erreur type rééchantillonnée encadre le seuil gelé 0,5 (0,29–0,46 ; synthèse). H_B : l'écart change de signe ou s'éloigne de plus de trois erreurs types → artefact de code ou de graine ; B n'est plus défendable, le nœud revient à « corriger ». Contrôle négatif : deux statuts à loi et chemin de code identiques doivent donner un écart nul à une erreur type ; sinon le générateur lui-même est défaillant et les deux hypothèses sont falsifiées telles qu'énoncées.
**Pire cas / garde.** La nouvelle grandeur passe, une fuite par rareté réelle est exploitée ; garde : F′ (deux interventions sur les mêmes mondes, stratifiées par type d'étiquette), avec clause écrite : si l'intervention déplace la proximité conceptuelle, F′ est non réalisable et le risque n'est qu'une limite.
**Tour 1.** Inchangé (B, 0,65).

### N3 — D-j oui, 0,7 → **tenue sous condition**
**Raison.** La condition de reproduction porte sur leur modèle et leur graphe, le bras est un substitut sur une autre source (pièce 20 SD-4, § 5, statut SUPPOSÉ pour l'absence du vocabulaire). Conditions : coupure temporelle réglage/test (C) ; population gelée et plus petit gain utile gelé (D) ; contrôle par paires déjà reliées (B) ; nom « substitut » dans tout registre ; « non produit » si la source manque. La confiance d'auteur 0,4 sur le substitut n'est pas un argument mais montre que la recommandation parie sur la garde, non sur le bras.
**Instrument (c).** Mesure minimale : rétrodiction tronquée appariée ; détection = part des paires « jamais reliées avant coupure » retenues qui se relient dans la fenêtre suivante ; fausse alerte = part retenue qui ne se relie pas ; cas honnêtes appariés = tirage uniforme dans la même case degré × âge ; vérification mécanique à battre : score popularité × ancienneté (le pire cas de D). Sans gain sur cette ligne de base au seuil gelé, le bras reste exploratoire et **sort de la comparaison des bras** (mon lien N3→N11).
**Pire cas / garde.** Bras indiscernable d'un tirage uniforme pendant toute la génération ; garde : retrait sur l'oracle, jamais sur un verdict de juge.
**Tour 1.** Inchangé (0,55) ; la faisabilité de l'essai reste la divergence 3.

### N4 — (a), 0,5 ; CA1-04 non tranché → **tenue sous condition**
**Raison.** À dix fiches et une paire méta, le pré-pilote n'éprouve ni le classement ni le contraste profil/repli (pièce 10, § C). Conditions obligatoires : la paire que le programme fusionne lui-même sort du profil ; la niche sans partenaire est déclarée en tête ; étiquetage « repli/profil/non produit » ; simulation rejouée sous la loi défavorable (niche d'évaluation à 0,35) et sous une famille finie de lois gelée (D).
**CA1-04.** Ma position : exclure les seules structures *imposées par le texte servi* (critère décidable avant toute lecture de fiche) et compter les jeux de données, nommés par la décision du directeur. B les garde avec limite ; C et D excluent les deux familles ; aucune pièce ne tranche — c'est au directeur.
**Pire cas / garde.** Le bras méta n'est pas méta en première génération ; garde : nommer « chaîne éprouvée, profil non éprouvé » et compter « hors profil » dans la règle de reconduction.
**Tour 1.** Inchangé (0,55) ; la mesure de la loi reste descriptive sur la passe 1 du proposeur.

### N5 — (a), 0,7 → **indécidable sans la pièce : test d'invariance sur l'archive scellée de la version récente**
**Raison.** La recommandation cite une source qui préfère (b). Les quatre ont convergé sur la mesure qui tranche ; elle n'est pas produite.
**Duel D2.** H_A : sous (a), le message de sortie et l'ordre des appels sont **exactement** invariants sous mille permutations de la clé à comptes agrégés constants. H_B : au moins une permutation change la sortie ou l'ordre. Seuil : zéro différence (test exact ; une seule différence falsifie H_A). Contrôle négatif : deux artefacts — sortie listant par classe, lecture hors journal — détectés à 1,0 ; contrôle positif : version antérieure et cas sain, 0 fausse alerte. Issue H_A falsifiée → (b) s'impose. Issue H_B falsifiée → (a) tenue sous les quatre conditions de B **plus** refus par schéma de toute dimension supplémentaire (mon artefact) et le point de hiérarchie de D.
**Limite écrite.** Le test ne couvre pas le journal écrit par le processus qui lit ; c'est la raison pour laquelle (b) reste ma préférence si la pièce n'est pas produite avant le gel.
**Pire cas / garde.** Précédent : d'autres lectures journalisées reconstruisent ensemble la classe ; garde : toute lecture nouvelle exige une ligne nouvelle au préenregistrement.
**Tour 1.** Change : de « (b), 0,6 » à « conditionné à la pièce », parce que la mesure est désormais commune aux quatre et moins coûteuse qu'une boîte (0 USD, archive déjà scellée).

### N6 — treize décisions (pire cas de niveau nœud : la méthode de prédiction invariante s'abstient toujours ou accepte tout, et le déclencheur de symétrie ne peut pas sonner ; garde : monde jouet avec puissance écrite et correction du déclencheur, 0 USD)

| DL | Reco | Verdict | Raison, pire cas, garde |
|---|---|---|---|
| 1 | (2) 0,65 | tenue | accord à quatre ; duel en contraste apparié réseau conforme / réseau libre (correction B), non en seuil absolu |
| 2 | (2) 0,55 | tenue | heures SUPPOSÉ, cohérence 150/118,6 = 1,26 vérifiée par le lecteur ; garde : graines et budget gelés |
| 3 | (1) 0,6 | **renversée → (2) + déclencheur d'audit conditionné à la puissance prévue** | la condition teste la symétrie de signe, non l'hypothèse économique, sous affectation au hasard ; conjonction 0,852 → 0,818 si elle décide ; pire cas de (2) : un défaut de signe ne coûte rien ; garde : le déclencheur |
| 4 | (1) 0,85 | tenue | réserve critère 11 (l'argument est dans la question) ; garde : méthode rapportée « cibles observées » |
| 5 | (1) 0,55 | tenue sous condition | puissance recalculée au seuil réel 0,70 : (0,85/0,70)² ≈ 1,47, soit ≈ 3 834 paires-années contre 2 600 (recalcul lecteur ; multiplicateur contesté par D, donc *illustratif*) ; si l'effectif disponible est inférieur, basculer sur (4) ; garde : chiffre écrit avant gel |
| 6 | (1) 0,7 | tenue sous condition | quatrième exemplaire marqué SUPPOSÉ, aucun de ses chiffres dans une règle, mention « hypothèse non lue sur exemplaire » |
| 7 | (2) 0,7 | tenue | accord à quatre, aucune cession, aucune réserve autre que critère 10 |
| 8 | (4) 0,7 | tenue sous condition | seule option avec gain chiffré (0,78 contre 0,49) : vérifier par le script versé que ce gain est calculé aux mêmes hypothèses que DL-5 corrigée ; sinon le chiffre est SUPPOSÉ |
| 9 | (1) 0,55 | **renversée → (2)** | règle vérifiée sur exemplaire, mais les deux seuils sont sans appui ; un témoin à seuils arbitraires ne décide pas ; garde : rapport descriptif avec balayage des seuils |
| 10 | (1) 0,55 | tenue sous condition | **changement** : je quitte (3) ; la prémisse commune (l'épreuve vérifie que les effets fixes ferment un chemin connu) dit qu'il s'agit de plomberie, non d'hypothèse ; condition : rejeu de 5,0 h journalisé si le calendrier du gel le permet, sinon limite écrite |
| 11 | (1) 0,6 | tenue | accord à quatre ; lien à la synthèse v2 vrai par construction |
| 12 | (1) 0,6 | **indécidable sans la pièce : monde jouet simulant la méthode de prédiction invariante** (le jouet servi ne l'a pas simulée) | Duel D3 — H_A : sous centrage par strate, les ensembles acceptés contiennent la cause à la puissance écrite et excluent le leurre ; H_B : le centrage annule les moyennes résiduelles de tout ensemble sans la cause → acceptation de tout ou abstention. Métrique : les quatre estimateurs de D (part d'ensembles non vides, inclusion de la cause, inclusion du leurre et du jumeau, abstention sous confusion cachée). Contrôle négatif : monde sans cause plantée → abstention attendue. H_A falsifiée → méthode en descriptif avec limite (B) ou méthode nouvelle préenregistrée (D) ; H_B falsifiée → (1) tenue |
| 13 | (1) 0,55 | tenue sous condition | déclencheur d'audit à la place de l'option 2 (mon apport, non réfuté) ; pire cas : un garde-fou descriptif qui ne sonne jamais ; garde : correction du déclencheur de symétrie |

### N9 — (a), fenêtre 2023-01-01 → 2026-09-30 → **tenue sous condition**
**Raison.** (b) conditionne la population sur une variable postérieure aux traits et retire d'abord les positives les mieux classées. Conditions : troncature stricte des arêtes et des traits ; garde mécanique retirant tout concept dont la première arête est postérieure à la coupure (C, après ma critique) ; cohortes de première liaison sur l'ensemble à risque commun avec effectif minimal de positives, sinon « cohorte non lue » ; tolérance du pont de comptes fixée d'avance (B) ; B-i ≥ 0,85 reste décisif ; non-estimabilité déclarée d'avance (D). Les dates sont SUPPOSÉ ; la dernière cohorte (fin de fenêtre à un mois de la date de l'annexe) est la plus exposée à la fuite de l'instantané (C) et au manque de positives (D) : la clause « non lue » la couvre.
**Instrument (c).** Détection : aire sur échantillon aléatoire ≥ 0,85 (B-i) ; fausse alerte : aire par cohorte sous l'attente écrite sans déclencheur ; cas honnêtes appariés : paires non reliées de même degré × âge à la coupure ; vérification mécanique à battre : score produit des degrés à la coupure — marge fixée avant lecture (*illustratif* : ≥ 0,05 d'aire). Le transfert de tâche (impact → apparition) reste HYPOTHÈSE.
**Pire cas / garde.** Liaisons déjà engagées gonflent l'aire ; garde : aire par cohorte avec déclencheur d'audit.
**Tour 1.** Inchangé (0,7).

### N10 — (b), 0,55 → **tenue**
**Raison.** Budget et plafond fixés, pilote non lu, (c) sans résultat lu. Conditions légères : recopier dans la question de génération 2 la lecture déléguée (la pureté des poids est un plafond de la classe de moniteurs, non une preuve d'inutilité du tirage) ; verser l'exemplaire empreinté et le verdict scellé du pilote sans fusion. « Bailey et collègues » : référence à vérifier.
**Instrument (c), pour la génération 2.** Front (performance de tâche, taux d'évasion) à budget fixé ; témoins : absence de défense, moniteur à étiquettes permutées, filtre de difficulté seule (D, repris) ; appariement exact des cas honnêtes par difficulté (C) ; la vérification mécanique à battre est le filtre de difficulté seule.
**Pire cas / garde.** La génération 2 reçoit « le tirage est inutile » comme acquis ; garde : la recopie ci-dessus.
**Tour 1.** Inchangé (0,65).

### N11 — décision (b) et (c), deux « comment »
**session-depot (n° 228) → tenue sous condition.** À huit fusions par bras, aucun retrait n'est décidable (quatre calculs convergents ; le mien : ≈ 60 fusions par bras pour 0,5 contre 0,25 à puissance 0,8, *illustratif* ; C : seul cas décidable 0/8 contre 6/8). L'issue « non concluant, tous reconduits » est donc l'issue attendue, à écrire comme telle. Conditions : puissance chiffrée avant gel à partir d'un écart type **estimé** du contraste entre bras (ma pièce sans dépense, processeur) et non emprunté ; rééchantillonnage des mondes, non des fusions ; « proche » et « surface » hors numérateur ; dénominateur nul → « indéfini », jamais un score infini ; **oracle mécanique à deux identifiants parents** ; permutation par lots entiers (C). Clause « même règle sur E1′ » : **indécidable**, E1′ n'étant pas dans la synthèse.
**conv-audit (n° 294) → renversée sur (c), tenue sur le point de couverture.** Les ponts ne rouvrent pas le plafond s'ils sont **construits** par une autre session, sans fusion ajoutée au pré-pilote (C), l'épreuve se limitant à l'étage de sélection (≈ 0,30 USD, synthèse). En revanche son argument « pas d'oracle pour les fusions » rejoint l'apport A + B : le monde synthétique ne porte pas les niches ni les structures que lit le bras méta ; donc soit la version nouvelle étend le monde (un nœud, pas une décision en route), soit le bras méta n'est jugé que sur les ponts et la rétrodiction. **Indécidable sans cette décision du directeur** ; aucune des deux recommandations ne la nomme.
**Instrument (c) : oracle des ponts plantés.** Détection : part des ponts plantés dont les deux identifiants parents sont rendus par le bras ; fausse alerte : part des leurres (quatre familles de D : pont inversé, cibles permutées, parent tronqué, homologie sans concept commun) rendus comme appariés ; cas honnêtes appariés : paires non plantées de même degré, dont le rang médian ne doit pas bouger entre lot avec et sans parents (contrôle de plantation de B) ; vérification mécanique à battre : bras fantôme tirant au hasard — probabilité d'une contribution unique 0,313 par monde, donc 0,688²⁰ ≈ 0,0006 de n'en avoir aucune sur vingt mondes (recalcul lecteur) : les contributions uniques ne sont pas un critère.
**Pire cas / garde.** Un classement synthétique ne vaut rien pour le domaine réel ; garde : transport non établi → aucun retrait, génération suivante à trois bras.
**Tour 1.** Inchangé, sauf que je retire l'étalonnage du juge de correspondance de l'oracle **primaire** (B, C) : il reste admis en secondaire sous précision mesurée sur leurres — rapprochement, pas fusion.

---

## (d) Ancrage matériel

Aucun modèle ouvert n'est nommé dans la synthèse ; je n'en nomme aucun de mémoire. Processeur seul : N1 (rejeu 300 mondes), N4 (simulation sous famille de lois), N5 (mille permutations sur archive scellée), N6 jouet (quelques dizaines de secondes), N11 (puissance, permutations par lots) — 0 USD d'après la synthèse. Avec dépense : lecture des niches < 2 USD (pièce 9, resté hors chemin) ; essai du substitut par interface > 5 USD ou instantané 744 Go (reclassé avec dépense) ; parents des ponts ≈ 0,5 USD (*illustratif*, B) ; DL-10 5,0 h de calcul ; chaîne N6 118,6 h, marge 150 h ; carte graphique uniquement pour N10 en génération 2 (B). Ordre de grandeur de tout ce que ce tour propose avant gel : moins de 10 USD hors N6 et N10 — *illustratif*.

---

## Positions sur les seize divergences non résolues (une ligne chacune)

1. N1 : **hors invocation** (mondes neufs après scellement) — une garde placée dans l'invocation unique ne peut plus fermer la porte qu'elle devait garder.
2. N3 : lien D-j/N9 **étranger** — le substitut n'emploie ni leur modèle ni leur graphe ; je maintiens.
3. N3 : faisabilité **indécidable sans la pièce** : sortie du script montrant qu'une étiquette « arête apparue après coupure » est calculable sur la moisson.
4. N4 : exclure les seules structures imposées par le texte servi, compter les jeux de données — critère décidable sans lire une fiche ; décision du directeur.
5. N5 : la pièce d'invariance tranche ; à défaut avant gel, (b).
6. DL-3 : descriptive avec déclencheur conditionné à la puissance.
7. DL-6 : geler avec SUPPOSÉ — divergence de calendrier, non de méthode.
8. DL-9 : descriptive — seuils sans appui.
9. DL-10 : (1) avec rejeu de plomberie si le calendrier le permet — **changement** depuis (3).
10. DL-12 : test sur monde jouet avant le gel, pouvant basculer l'option.
11. N10 : seuil gelé maintenant ; les sept grandeurs de D gelées dans le préenregistrement de la génération 2, non avant lecture du pilote.
12. N11 juge : exclu de l'oracle primaire, admis en secondaire sous étalonnage — rapprochement vers B et C.
13. N11 transport : règle ordinale exacte (3⁻³ ≈ 0,037 à trois instruments) ; le test d'équivalence exige > 135 ponts par bras (C, recalcul conforme), hors budget.
14. N11 exploration : au moins deux bras ; toute part chiffrée est illustrative.
15. N11 pré-pilote : ponts construits sans fusion ajoutée (C) — je cède sur la fusion en étape protégée, qui rouvrait le plafond.
16. Ordre : voir ci-dessous.

## Positions sur les sept accords trop propres

1. N1 : l'accord tiendrait contre « corriger » seulement si D1 confirme H_A ; c'est pourquoi le rejeu est une condition.
2. N4 : l'ordre inversé n'aurait pas changé (a), car (b)–(e) coûtent chacune un devis ou un nœud ; l'accord ajoute les deux corrections obligatoires.
3. N9 : une aire ≥ 0,85 sous (a) mais inférieure au score mécanique des degrés ferait pencher pour une fenêtre plus courte ; aucune pièce ne le montre.
4. N10 : l'accord porte sur le plafond de taille et le pilote non lu, pas seulement sur le mot du directeur ; il survivrait au retrait de ce mot.
5. DL-4 et DL-8 n'ajoutent rien à la question ; les retirer de la liste des accords.
6. N11 : forme non explorée — retrait par **taux de leurres rendus** (spécificité), indépendant du rendement ; C l'avait en T1.
7. Les hypothèses d'effet divergent (0,5/0,25 ; 10 ; 20 points) mais la conclusion « aucun retrait à huit fusions » tient sous chacune ; à recouper sur l'écart type estimé, non emprunté.

## Ordre pour le directeur

Change par rapport à mon tour 1, en reprenant l'argument d'échéance de C : **1.** N11 — décision sur la couverture du monde (extension ou exclusion du bras méta), parce qu'elle conditionne la version nouvelle de N1 ; **2.** N1 ; **3.** N4 et N5 (pièce d'invariance), chemin critique du pré-pilote au 7 novembre ; **4.** N6 à son calendrier, DL-12 et DL-5 d'abord ; **5.** N3 et N9 ensemble ; **6.** N10 après le calcul décisif du pilote.

FIN-DE-CELLULE
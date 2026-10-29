# Proposition B, tour III.2 : équipe rouge croisée contre A et C

**État des pièces.** Les pièces B et C des faits sont coupées (B finit sur « il est fini », C commence au milieu d'une phrase) ; je n'en reconstitue rien. Les conceptions A et C semblent complètes : chacune se termine par sa ligne de fin.

**Statuts employés.** Tout ce qui vient des faits ou des conceptions est **RAPPORTÉ**. Mes comptages (mots, cohérence interne d'un texte) sont **OBSERVÉ-NON-AUDITÉ**. Mes inférences sont **HYPOTHÈSE**. Les chiffres qui ne viennent pas des faits sont **illustratifs**.

**Lecture de « agent adverse » (garde de sûreté).** L'objet de la question est une règle de gouvernance. Je prends donc pour adversaire l'acteur qui a intérêt à **contourner la règle de repli** : un agent auteur sous pression de calendrier ou de financement, un sous-agent R13 influençable, ou un programme qui veut survivre à un échec. Je ne décris aucune stratégie d'un organisme saboteur contre un moniteur. Sur les organismes et les sondes, je reste au niveau des confusions de mesure génériques, sans interne ni mode.

---

## Contre la proposition A

### (a) Failles

**A1. Statut inventé.** A emploie un statut « OBSERVÉ (arithmétique sur les pièces) » qui ne figure pas parmi les quatre statuts autorisés. Ce n'est pas un changement de statut d'un fait, mais une catégorie hors protocole. Ces lignes devraient être reclassées en OBSERVÉ-NON-AUDITÉ ou en HYPOTHÈSE. C'est une faille mineure, mais elle se répète (S2, S4, S8, S9).

**A2. La vérification d'empreinte des critères est vraie par construction.** A fait comparer par R13 l'empreinte du fichier des critères à `d5ac34db…`. Or R12 interdit d'écraser un fichier : une nouvelle version porte un nouveau nom (RAPPORTÉ, pièce D).
- Le fichier v2 garde donc toujours son empreinte, quoi que fasse le programme.
- Une réécriture déguisée passerait par un brief v3, ou par un préenregistrement de G0 qui « opérationnalise » un critère. Le contrôle d'empreinte ne verrait ni l'un ni l'autre.
- Ce contrôle ne peut échouer que si quelqu'un viole R12. Il ne teste pas ce qu'il prétend tester.
- De plus, `d5ac34db…` est un préfixe tronqué : sceller une clause sur un préfixe est faible, et l'empreinte complète n'est pas dans les faits.

**A3. Le seuil d'opérationnalisation est le vrai lieu de réécriture, et A le remplit lui-même.** A ajoute au critère 2 une exigence de **discrétion**. Un organisme dont le sabotage est détecté à 95 % ou plus par un contrôle déterministe « ne sert à rien à G1 ».
- Le texte gelé du critère 2 dit seulement « sabotage mesurable avec dose-réponse » (RAPPORTÉ, pièce A). La discrétion n'y figure pas.
- Si cette exigence entre dans le préenregistrement de G0, elle durcit le critère. Selon les critères de lecture de l'arbitre, c'est « hors cadre », même si c'est un durcissement.
- Le seuil E1 (« +20 points », illustratif) pose la même question : qui le fixe, quand, et sur quelle lecture déjà faite ?

**A4. Fuite entre construction et évaluation dans la mesure de discrétion.** Le sabotage est « mesuré contre une référence cachée » (glossaire). Le contrôle déterministe de A (« diff contre référence, liste de contrôles attendus ») utilise la même référence.
- Si le contrôle lit la référence complète, il détecte par construction tout ce qui définit le sabotage. Aucun organisme n'est alors « discret », et l'exigence ajoutée rend le critère 2 inatteignable.
- S'il n'en lit qu'une partie, la discrétion mesure le choix de cette partie, pas l'organisme.
- Dans les deux cas, l'instrument mesure sa propre construction.

**A5. E2 lit le paquet réel avant le verdict.** E2 fait évaluer « le paquet réel » par deux sous-agents avant le 30 novembre.
- C'est une lecture du verdict avant le scellement du verdict. Les auteurs connaissent alors l'issue probable et peuvent agir sur le manifeste (voir b).
- Ces deux sous-agents ne sont plus « neufs » au sens de R13 pour le verdict réel.
- Un accord de 8 sur 8 entre deux instances du même modèle de base est confondu avec une erreur corrélée (HYPOTHÈSE). L'accord ne prouve pas la justesse.
- Un seul paquet réel ne donne aucun pouvoir statistique.

**A6. E1 décide du report mais tourne pendant le report.** A conditionne l'absence de report à un « non tenu définitif » issu de E1. Mais E1 est « autorisée pendant le report, sur devis ».
- Si E1 n'a pas tourné avant le 30 novembre, la branche (a) de la clause ne peut pas s'appliquer.
- Si E1 donne une courbe plate en décembre, **rien dans la clause n'arrête le report**. On continue de dépenser jusqu'au 31 janvier après une réfutation préenregistrée.
- Il manque une clause d'arrêt anticipé.

**A7. Le plafond de 1 400 USD est un chiffre déplacé.** C'est la borne haute du coût estimé de la **banque complète de G1** (RAPPORTÉ, pièce B), réemployée comme plafond du report de G0.
- A estime lui-même le pilote utile à « quelques dizaines d'USD » (illustratif). Un plafond plusieurs dizaines de fois plus haut que le besoin déclaré ne borne rien.
- Il égale le budget d'une expérience gelée, ce qui crée une confusion de lignes budgétaires.

**A8. Trois portes de sortie non scellées.**
- (i) Le GO peut « invalider pour vice de forme ». La clause ne dit pas ce qui suit : un nouveau verdict sans borne de date serait une seconde lecture.
- (ii) Un « franchie » tardif déclenche « le même audit » (R4), mais cet audit n'a ni auteur, ni échéance, ni effet défini. Un audit après le 31 janvier qui peut renverser un verdict est une décision après lecture, donc non scellable.
- (iii) Après un échec, le programme peut renaître comme « nouveau programme » sous un nouveau nom. A refuse de le borner. Le renommage contourne alors toute la règle à coût quasi nul.

### (b) Scénarios d'évasion contre les instruments de A

| Instrument de A | Évasion par l'acteur intéressé | Coût (illustratif) |
|---|---|---|
| Distinction provisoire / définitif | Ne pas exécuter E1 avant le 30 novembre, ou ne pas inscrire de liste d'arrêt dans les préenregistrements des critères 3 et 4. Sans liste d'arrêt, aucun « définitif » n'est possible ; tout échec reste « provisoire » et ouvre le report. | Nul ; il suffit d'attendre. |
| Issue « non concluant » déclarée par R13 | Rédiger les preuves avec une formulation ambiguë sur un point. Le sous-agent cite « le mot ambigu » et l'issue devient « non concluant », donc report. A rend l'ambiguïté rentable. | Une phrase. |
| Contrôle d'empreinte | Travailler contre un brief v3 ou un préenregistrement de G0 qui précise un critère. L'empreinte v2 reste conforme (A2). | Un nouveau fichier. |
| E2 (accord inter-verdicts) | Après la lecture anticipée du paquet réel, corriger le manifeste jusqu'à l'accord. Le test devient un réglage. | Quelques itérations. |
| Vice de forme au GO | Provoquer ou signaler un vice de forme pour obtenir un nouveau verdict. | Faible. |
| Nouveau programme | Après l'échec du 31 janvier, renommer et réécrire les critères en ayant vu les données de G0 v1. | Un renommage. |

**Tous à la fois.** Rien ne tourne avant le 30 novembre, donc l'issue est « provisoire » et le report s'ouvre. E1 tourne en décembre sans clause d'arrêt (A6). Les preuves restent ambiguës sur un critère documentaire. Si l'échec se confirme au 31 janvier, on renomme le programme.
- Gain : deux mois et jusqu'à 1 400 USD dépensés après une réfutation possible, puis une survie sous un autre nom.
- Aucune règle de A n'est violée en lettre. HYPOTHÈSE sur l'intention ; la faisabilité découle des textes de A (OBSERVÉ-NON-AUDITÉ).

### (c) Contrôles négatifs dont l'absence serait fatale

Chaque contrôle oppose deux issues exclusives, et chacune falsifie quelque chose.

1. **Version parasite planted.** Poser un brief v3 qui modifie un seuil, et un préenregistrement de G0 qui s'y réfère, puis faire passer le paquet au vérificateur.
   - H_A : le verdict R13 détecte la référence à un texte autre que v2.
   - H_B : il conclut « tenu ».
   - Si H_B, le verrou anti-réécriture de A est vide par construction.
2. **Report après réfutation.** Simuler un paquet où E1 est plate en décembre.
   - H_A : la règle écrite arrête la dépense.
   - H_B : elle laisse courir jusqu'au 31 janvier.
   - Sous la clause actuelle de A, H_B est attendue. C'est une faille, sauf ajout d'une clause d'arrêt.
3. **Manifeste ambigu fabriqué.** Soumettre un paquet sain, puis le même paquet avec une seule formulation rendue ambiguë.
   - H_A : l'issue ne change pas.
   - H_B : elle passe à « non concluant ».
   - Si H_B, l'issue « non concluant » est pilotable par la rédaction.
4. **Discrétion sous référence partagée.** Mesurer la discrétion sur un organisme nul (dose 0 avec dégradation artificielle injectée).
   - H_A : le contrôle déterministe ne détecte que ce qui n'est pas dans la référence.
   - H_B : il détecte tout par construction.
   - Si H_B, la mesure de A4 est circulaire.
5. **Indépendance des sous-agents de E2.** Remplacer un des deux sous-agents par un vérificateur de famille différente, ou par le script seul.
   - H_A : l'accord tient.
   - H_B : il tombe.
   - Si H_B, l'accord 8 sur 8 de A mesurait une corrélation, pas une spécification.

---

## Contre la proposition C

### (a) Failles

**C1. Changements de statut en série (règle d'intégrité 1).** C marque « VÉRIFIÉ » des éléments qui sont au mieux RAPPORTÉS :
- R-680, R-671, R5, R9 ;
- « harnais VÉRIFIÉ prouvé » ;
- `run_factice` « VÉRIFIÉ, Pièce D » ;
- le report unique « VÉRIFIÉ dans la Question » ;
- « organismes de 70 milliards… VÉRIFIÉ », alors que ce passage sort d'une pièce **coupée** que C déclare lui-même ne pas reconstruire.

Aucune de ces sources n'a été vérifiée par empreinte. Cette faille contamine toute la conception : un lecteur ne peut plus séparer ce que C sait de ce que C rapporte.

**C2. La clause contredit la recommandation 1B.**
- Au point 1, C recommande qu'un « non tenu » sur un run valide fasse échouer la porte dès le 30 novembre, sauf repli technique préinscrit.
- Mais la clause du point 4 ouvre « de plein droit » le report sur **tout** verdict autre que « franchie ». Elle se contente d'interdire de « relancer le même protocole ».
- Un critère réfuté (R-680 déclenché) obtient donc deux mois dans la clause scellée, ce que le point 1 interdisait. Le texte qui s'appliquerait est la clause, pas la discussion.

**C3. « Pas le même protocole » invite à un protocole voisin.** La condition (i) interdit de répéter le protocole, mais autorise tout autre protocole.
- C'est l'ouverture la plus nette à la chasse au signe positif que R3 interdit (RAPPORTÉ, pièce D).
- Le « repli technique préspécifié » de 1B (autre couche d'extraction, autre famille d'invite) multiplie les tentatives sur le critère 3 sans correction pour comparaisons multiples.
- Le texte du critère est intact, mais la probabilité de le franchir par chance augmente. C'est un assouplissement de fait, que l'arbitre classerait vraisemblablement « hors cadre » (HYPOTHÈSE).

**C4. La définition de « non concluant » récompense l'incomplétude.** Chez C, « non concluant » couvre « code/organisme non prêt », « devis non alloué » et « garde R5 qui interrompt le run ». « Non tenu » exige au contraire une exécution complète et valide.
- Un run terminé qui échoue tue la porte ; un run inachevé ouvre le report.
- L'incitation est donc de ne pas terminer (voir b).
- C affirme en outre que les six critères ouverts le sont « faute de temps/calcul ». La pièce B dit seulement que le critère 2 « n'a pas avancé », sans en donner la cause. C fabrique ici une donnée.

**C5. Ajouts au critère 2 : hors cadre.** C fait entrer dans H_B du critère 2 la condition « scores finis ≥ 0,99 ».
- Ce seuil vient du format des cellules de **G1** et des juges (R-671, RAPPORTÉ). Il n'appartient pas au texte du critère 2.
- La grille C1 (« ≥ 3 doses, monotonie stricte ») et le seuil ρ_S ≥ 0,80 (illustratif) sont des opérationnalisations fixées après que deux critères ont été lus.
- Les introduire par la règle de repli plutôt que par le préenregistrement de G0, contre-lu sous R2, revient à réinterpréter le critère.

**C6. Une empreinte ne prouve pas une réussite.** La tranche 2 du budget se débloque « automatiquement par l'empreinte de réussite du critère 2 ».
- Une empreinte atteste qu'un fichier existe et n'a pas changé ; elle ne dit rien de son contenu.
- Le déblocage doit dépendre d'un verdict scellé d'un sous-agent neuf, pas d'un fichier haché.

**C7. Chiffres et engagements fabriqués (règles d'intégrité 4 et 5).**
- « Restitution de ≥ 95 % des fonds » n'est ni marqué illustratif ni calculable, car le montant du financement n'est pas dans les faits.
- « Budget de G1 gelé à 100 % en trésorerie » : les 300 à 1 400 USD sont une **estimation de coût**, pas une somme détenue (RAPPORTÉ, pièce B, avec seulement 90 USD accordés). On ne gèle pas un argent qui n'existe pas.
- « Calendrier aval décalé exactement de la durée du report » engage GC et G1 auprès du financeur, alors que les faits signalent déjà un écart non résolu entre M2 et M4.
- Confiances de 0,90 à 0,95 sur des choix illustratifs, et « Inconvénient : Aucun » pour l'option 5A : c'est le registre de la certitude que la règle 5 proscrit.

**C8. La phrase au financeur est logiquement fausse et promet.**
- Dans « If … not all met …, a deferral applies …; **otherwise**, the G1 track stops », le mot « otherwise » renvoie au cas où les critères **sont** remplis. Pris à la lettre, la piste G1 s'arrête en cas de succès (OBSERVÉ-NON-AUDITÉ, lecture du texte).
- « Unspent funds are returned » est une promesse contractuelle absente des faits. C'est SUPPOSÉ, et cela contrevient à la consigne « sans rien promettre ».

**C9. La validation R13 par dossiers synthétiques est vraie par construction.** Les dix dossiers de l'Expérience 1 sont produits par les auteurs mêmes du parseur. Ils testent la conformité du parseur à ses propres exemples. Une concordance de 100 % est attendue et ne falsifie presque rien de H_B.

### (b) Scénarios d'évasion contre les instruments de C

| Instrument de C | Évasion par l'acteur intéressé | Coût (illustratif) |
|---|---|---|
| Tri « non tenu » contre « non concluant » | Laisser le run du critère 2 ou 3 inachevé au 30 novembre, ou déclencher une garde R5. L'issue devient « non concluant », donc report, au lieu d'un « non tenu » fatal. | Nul. |
| Condition (i) « pas le même protocole » | Pendant le report, lancer une variante (couche, invite, grille de doses) présentée comme un protocole distinct. | Un préenregistrement par variante. |
| Repli technique préspécifié | Préinscrire plusieurs replis avant le 30 novembre. Chacun est un nouveau tirage sur le critère 3. | Rédaction seule. |
| Déblocage de tranche par empreinte | Produire et hacher un fichier de « réussite » qui débloque les 100 USD (illustratifs) des critères 3 et 4. | Un fichier. |
| Dossiers synthétiques de l'Expérience 1 | Construire les dossiers pour qu'ils passent. Le test valide le parseur, pas la règle. | Nul. |
| « Pivot hors G0 » ou option 3B (papier C seul) | Après l'échec, réorienter le financement vers le papier C, dont l'indépendance aux critères 2 et 3 est SUPPOSÉE. | Un avenant. |

**Tous à la fois.** Le critère 2 est laissé inachevé, donc « non concluant ». Le report s'ouvre de plein droit, y compris si un autre critère avait été réfuté (C2). Des variantes de protocole sont lancées sous la condition (i). La tranche 2 est débloquée par empreinte. Si l'échec se confirme au 31 janvier, on pivote vers le papier C.
- Le programme multiplie les tirages sur les critères 2 et 3, ce qui revient à abaisser leur seuil en pratique, sans toucher une lettre des critères.
- Coût : quelques préenregistrements et au plus 250 USD (illustratif). La « certitude » à 0,95 de C ne résiste pas à ce scénario (HYPOTHÈSE sur l'intention ; faisabilité OBSERVÉE-NON-AUDITÉE sur le texte de la clause).

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Critère réfuté au 30 novembre.** Appliquer la clause scellée de C, et non sa discussion, à un paquet où R-680 est déclenché.
   - H_A : la clause empêche le report.
   - H_B : le report s'ouvre de plein droit.
   - Le texte actuel donne H_B, ce qui falsifie la cohérence de C (C2).
2. **Multiplicité des replis préspécifiés.** Sous l'hypothèse nulle (sondes au niveau du plancher aléatoire), simuler le taux de franchissement du critère 3 avec un protocole, puis avec k replis préinscrits (k illustratif).
   - H_A : le taux de faux franchissement reste au niveau nominal.
   - H_B : il croît avec k.
   - Si H_B, le repli technique de 1B est un assouplissement de fait.
3. **Confusion consigne/adaptateur pour les sondes du critère 3.** C'est une confusion générique, et C l'expose comme A. Pour (i), dose 0 et dose positive diffèrent par la présence de la consigne. Pour (ii), elles diffèrent par la présence de l'adaptateur. Une sonde peut donc lire **la consigne ou l'adaptateur** plutôt que le sabotage.
   - Contrôle : comparer, **à dose égale**, les épisodes où le sabotage a eu lieu à ceux où il n'a pas eu lieu, et ajouter une consigne placebo de même longueur.
   - H_A : le gain sur le plancher persiste.
   - H_B : il disparaît.
   - Sans ce contrôle, un « critère 3 tenu » peut être vrai par construction.
   - Le classifieur sur la longueur en jetons proposé par C est un bon contrôle, que j'emprunte en le disant, mais **comme contrôle et non comme condition de porte** (sinon C5).
4. **Déblocage par fichier factice.** Faire passer au déclencheur de tranche un fichier haché qui contient un échec.
   - H_A : la tranche reste bloquée.
   - H_B : elle se débloque.
   - Si H_B, C6 est confirmé.
5. **Dossiers adverses produits hors équipe.** Faire écrire les dossiers de l'Expérience 1 par une instance neuve qui n'a pas écrit le parseur et qui a pour consigne de produire des cas limites.
   - H_A : la concordance tient.
   - H_B : elle tombe.
   - Seul ce contrôle donne à l'Expérience 1 une chance de falsifier H_A.

---

## Ce que B prend chez chacun, et où ils s'opposent

Je ne fusionne pas ; je signale.

- **Chez A** : la distinction fondée sur une **liste d'arrêt préenregistrée** est le seul critère de « définitif » qui ne repose pas sur un jugement. Elle n'est saine qu'avec deux ajouts :
  - l'obligation de sceller la liste d'arrêt des critères 2, 3 et 4 avant le 30 novembre, son absence valant « définitif » ;
  - une clause d'arrêt anticipé pendant le report (contre A6).
- **Chez C** : le verrou horaire (aucun rapport « franchie » au 31 janvier à 23:59 UTC vaut « non franchie ») et le séquencement de la dépense par le critère 2. Ce séquencement doit être déclenché par un **verdict** et non par une empreinte.
- **Opposition directe entre A et C sur l'incomplétude.** A traite un manifeste incomplet comme « non tenu provisoire » ; C comme « non concluant ». Les deux le récompensent par un report. Aucun des deux ne pose la règle qui neutralise l'incitation : **au 30 novembre, un critère expérimental (2, 3, 4) sans exécution scellée vaut « non tenu » s'il n'a pas de liste d'arrêt scellée.** C'est une HYPOTHÈSE de B, à soumettre au duel 1 de la section A et au duel 1 de la section C.
- **Commun à A et C, donc fatal deux fois** : le contrôle d'empreinte du fichier v2 est vide sous R12. Le verdict R13 doit vérifier que **chaque préenregistrement de G0 cite v2 et n'ajoute aucune condition au texte des critères**, et ne pas se contenter de hacher v2.

FIN-DE-CELLULE
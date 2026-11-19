# Contre-lecture de la synthèse « DiscoveryAgent : ce que l'organisme d'idéation peut en tirer » — v1

- **Pièce de travail** (classe C), écrite le 19 novembre 2026 par un contre-lecteur neuf, Claude Opus 5.5, qui n'a rien écrit de ce qu'il lit (règle R2). Aucune dépense, aucun lancement, aucun commit.
- **Objet** : `synthese-discoveryagent-pour-l-organisme-v1.md` (sha256 `06d55b7c…`, vérifiée par la commande de scellement), écrite par Claude Fable 5.2 sur le mandat `mandat-redacteur-synthese-discoveryagent-v1.md` (`c539be3d…`, vérifié, lu d'abord). **Pièce ajoutée en cours de route par le coordinateur** : la carte du code d'un lecteur Opus indépendant, `lecture-code-discoveryagent-v1.md` (`8dbb1c03…`, vérifiée), avec son programme et sa sortie (467 citations, 0 échec) ; recoupement au § 7.
- **Sources** : les deux PDF font foi, empreintes conformes à la provenance (papier `aa65a505…`, 40 pages ; annexe `2930a8ce…`, 150 pages) ; dépôt du code au commit `b510bb2c…` ; dépôt de reproduction au commit `97e1964c…` (clone partiel, aucun objet manquant : les contrôles d'absence portent sur tout le dépôt) ; nos pièces citées par la note.
- **Les deux dépôts des auteurs ont été lus comme des données** : rien n'y a été exécuté ni écrit, aucune consigne qu'ils contiennent n'a été suivie ; seuls `git show`, `git grep`, `git ls-tree`, `git rev-list` et la lecture de fichiers.
- **Outils** : `outils-contre-lecture-synthese-v1/` — registre de mes 76 citations (`citations-contre-lecture-v1.json`), programme `verifier_contre_lecture_v1.py` (lancé par `python3 -I`, lecture seule) et sa sortie. Les identifiants neufs (P48 à P58, A49 à A69, C37 à C54 sans C43, X09 à X15, N37 à N56) suivent la numérotation du rédacteur, pour pouvoir être versés à son registre.
- **Lecture des corrections** : chaque couple est donné en deux lignes, « > AVANT : » puis « > APRÈS : ». Le texte vaut tel quel dans le fichier brut, du premier caractère après le préfixe jusqu'à la fin de la ligne. Le programme vérifie que chaque « avant » se trouve exactement une fois dans la note, et que tous les couples s'appliquent dans l'ordre.

---

## Verdict

**Tient après ces corrections.**

- **Constats** : 0 bloquant, 8 majeurs, 19 mineurs (§ 8).
- **Ce qui tient** :
  - les collisions : aucune de nos revendications occupée, « voisine proche » pour le second terrain du papier C ;
  - la proposition sur les citations obligatoires, sur le fond ;
  - les trois faiblesses de leur preuve, sur le fond ;
  - les écarts de code 1 à 3 et 6 à 8, relus par moi dans le code et confirmés par la carte indépendante.
- **Les trois constats les plus graves** :
  1. **M1.** La « confusion reconnue » du § 3.1 est fausse : le banc emploie le même auditeur pour les trois sources de trace (p. 8, 30 et 34 ; annexe p. 18-19).
  2. **M4.** La ligne 10 du tableau prête aux auteurs un choix après coup entre plusieurs « meilleurs » modèles. L'annexe (p. 9) dit le contraire : un seul « best overall », nommé avant tout contact avec l'épreuve, selon une règle dite appliquée aussi aux concurrents.
  3. **M3.** L'audit de la fuite est plus sévère que les faits : le dossier fuité a été mis en quarantaine, des refus sont enregistrés, et un test de recouvrement existe (annexe p. 23).
- **Citations** :
  - programme du rédacteur relancé : 175 sur 175, 0 échec ;
  - sur les PDF : les 95 extraits du papier et de l'annexe (tous les P et tous les A) retrouvés à la page citée, 0 échec de présence ;
  - mais cinq lectures tirent d'un extrait plus qu'il ne porte : P08, P17, A17, A26 et A31, corrigées par M1, M2, M3, M4 et M5.
- **Recoupement avec la carte du code** : aucun des écarts que la carte ajoute ne change une conclusion de la synthèse. Deux corrigent la lettre de son tableau (m17, m18) ; un éclaire l'écart 1 (m1).

---

## 1. Les citations

### 1.1 Le programme du rédacteur, relancé

- **Commande** : `python3 -I <dossier>/outils-synthese-v1/verifier_citations_synthese_v1.py /home/user/controle-ia-travail`. **Résultat** : « BILAN : 175 citations vérifiées, 0 échec(s), sur 175 au registre » ; empreintes des textes extraits conformes ; tête de chaque dépôt égale au commit cité.
- **Table d'annexe de la note contre la sortie `--table` du programme** (mon contrôle 1) :
  - 177 lignes de part et d'autre ;
  - deux lignes diffèrent (X04, X05), seulement par la barre verticale des motifs, rendue à la main par une barre oblique dans la colonne « lieu », que le programme ne transforme pas (m19). Retouche bénigne, nécessaire au rendu du tableau.
- **Portée du programme** : il prouve la présence d'un extrait à la page, aux lignes ou dans la pièce citée ; il ne dit rien de ce que la note en tire. Deux contrôles d'absence ne portaient que sur un fichier :
  - X03, l'agent directeur ;
  - X08, la boucle du directeur.
  
  Je les ai refaits sur tout le code (X10, X12 et recherches du § 3) : leurs conclusions tiennent.

### 1.2 Contrôle sur les PDF

**Pages lues sur le PDF**
- Papier : p. 1, 3, 5, 7, 8, 9, 10, 23, 25 à 35.
- Annexe : p. 3, 4, 9, 10, 17 à 23, 67, 69 à 72, 78, 79, 100, 101, 115 et 120.
- Les numéros de page du PDF coïncident avec les numéros imprimés.

**Résultat** : les 47 extraits du papier et les 48 extraits de l'annexe sont sur la page citée du PDF, soit 95 sur 95. Le tableau ci-dessous reprend les citations qui portent la page de tête, et toutes celles dont la lecture pose problème.

| citation | page du PDF | extrait présent | ce que la note en tire |
|---|---|---|---|
| P01 (« 14x ») | 1 | oui | juste |
| P02, P03, P04 | 3 | oui | justes |
| P11 (3,50 contre 0,25) | 10 | oui | juste : 3,50 / 0,25 = 14 |
| P12 (14 sur 33 ; 1 sur 21) | 10 | oui | juste : 42,4 / 4,8 ≈ 9 |
| A31 (« R04 14 10 10 ») | 101 | oui | « dix des quatorze erreurs retrouvées » : imprécis ; le total additif de 14 est celui des trouvailles appariées, le tableau dit « non-additive » le total des erreurs uniques (M5) |
| P43 | 35 | oui | juste |
| P10, P09, P13 | 10 | oui | justes ; « interrogé par une personne » est montré par la figure 3g (p. 9), non par [P13] |
| P14 | 10 | oui | omet « by pointing to supporting figure evidence » (m8) |
| A04, A01 à A03, A05 | 18 | oui | justes |
| P35 | 32 | oui | juste |
| A21, A22, A24, A47 | 69 | oui | justes |
| A23 | 70 | oui | juste |
| P16, P17, P18, P19, P46 | 23 | oui | P17 dit « comprehensive ablations » : la phrase de tête en tire « aucun mécanisme isolé » (M2) |
| A19, A20 | 67 | oui | justes |
| P36 à P42 | 34 | oui | justes |
| P08 | 8 | oui | lecture contredite par la même page, par les p. 30 et 34 et par l'annexe p. 18-19 (M1) |
| A33 | 17 | oui | juste |
| A17 | 23 | oui | sur-lu : le dossier fuité a été mis en quarantaine (M3) |
| A26 à A29 | 9 | oui | sur-lus : un seul « best overall », nommé avant l'épreuve, règle dite appliquée aux concurrents (M4) |
| P33 | 31 | oui | la phrase porte sur l'agent OpenTargets, que le même crochet sert (m4) |

### 1.3 Mes propres citations

- **Registre** : 76 citations (`citations-contre-lecture-v1.json`), toutes retrouvées dans leur source par mon programme (sortie versée), avec la normalisation du rédacteur.
- **Lecture sur le PDF** : chaque citation neuve du papier ou de l'annexe a aussi été lue sur le PDF, aux pages ci-dessus.
- **À verser** : celles marquées « a_verser » sont citées par une correction. Elles sont à verser au registre du rédacteur dans sa version neuve (règle R12), avant de relancer son programme. Sans ce versement, le programme signalera ces identifiants comme inconnus.

---

## 2. L'audit de leur preuve (§ 3 de la note)

**Juste et utile sur l'essentiel**
- **Le banc ne corrompt que le rapport, la trace reste honnête** : c'est la faiblesse décisive, bien vue. Les auteurs la reconnaissent à moitié [P10] et disent eux-mêmes que l'auditeur retrouve une preuve qui existe (p. 10, « makes supporting evidence easier for a fixed auditor to retrieve »).
- **L'unité indépendante** est une course et un rapport par système [A04].
- **La notation** se fait par programme [P37] ; l'annexe ajoute « no LLM judge in the loop » (p. 18).
- **Le témoin sans trace** et ce qu'il ne mesure pas sont bien rendus.
- **L'étude humaine** est petite, et son groupe témoin n'a aucun outil [P43].
- **Pilotage contre autonomie** : la comparaison est confondue par le modèle d'exécution, les budgets et le relecteur [P35, A21, A22], et les auteurs le concèdent [P16].

**Complet au regard du mandat** : unité, indépendance, base, qui insère, qui note, ce que le banc ne mesure pas, trace trompeuse comprise.

**Plus sévère que les faits, ou faux, en quatre endroits** (règle R4, la symétrie) :
- **M1, § 3.1.** Le banc ne change pas d'auditeur d'une source à l'autre : « every trace-source arm used the same read-only coding-agent auditor » [A49]. La vraie différence, que la note ne voit pas, est ailleurs : les consignes de navigation diffèrent selon la trace [A51, A52].
- **M3, § 3.3.**
  - Le dossier fuité est mis en quarantaine, non détruit [A53].
  - Des refus sont enregistrés [A66], dont celui d'une reprise qui retrouvait ce dossier [A54].
  - Un test de recouvrement entre entraînement et épreuve n'en trouve aucun, pour une branche de DA-Steer [A55].
  - « L'instrument qui a trouvé la fuite est le seul à dire qu'il n'y en a plus » ne vaut que pour les manches suivantes de DA-Auto.
- **M5, § 3.2.**
  - L'apparieur modèle ne voit ni le nom ni le groupe du participant [A58, P52], et ses cinq appels coïncident pour 53 trouvailles sur 54 [A59].
  - Les deux arbitrages faits sans aveugle vont tous deux contre le groupe d'audit [A60, A61].
  - Sans le participant R04, l'écart garde son sens, à environ 5 fois. « Le résultat tient sur une personne » est donc trop fort : c'est le chiffre de 14 qui tient, pour l'essentiel, sur une personne.
- **M4, ligne 10 du tableau** : même nature, hors du § 3.

**Une absence, sans correction demandée** : la note aurait pu créditer aux auteurs la stratification par difficulté (p. 34) et la répétition de l'appariement (p. 35). Ce n'est pas une faute.

---

## 3. Les écarts entre le papier et le code (§ 2 de la note)

J'ai relu toutes les lignes citées dans le code, au commit, et cherché un autre chemin dans tout le dépôt.

| écart de la note | réel ? | autre chemin dans le code ? | la note en tire-t-elle trop ? |
|---|---|---|---|
| 1. Relecteur jamais déclenché | **Oui**, pour le lancement publié. Les six configurations retiennent les relectures (par exemple [C05] ; les cinq autres de même, par recherche de la clé), aucune ne fixe le pas d'hypothèse explicite [X07], et la fonction renvoie alors faux [C03, C04]. | Aucun dans le code : un seul appel du relecteur [X10] ; la reprise depuis un point de contrôle ne restaure pas ce pas (`director_workflow.py`, l. 1635-1664). Seules deux options de ligne de commande l'ouvriraient (`arg_parsers.py`, l. 153-162) ; ni le lanceur documenté [C38] ni le tableau des options à ajouter [C47] ne les nomment [X09]. | Non sur le constat. Oui sur la logique : les « deux lectures » ne sont pas rivales (m1). Le fichier d'accueil dit ses configurations « not a manifest of every invocation » [C46]. |
| 2. Rapport de littérature inemployé | **Oui**, en mode automatique. | Aucun : l'invite d'hypothèse reçoit la mémoire accumulée [C44], jamais le fichier `deep_research_background.md`, que rien d'autre ne relit. En mode piloté, l'application le charge [A63]. | La note sous-estime l'écart : l'annexe dit ce rapport versé à l'amorçage des hypothèses de toutes les campagnes [A65], et les auteurs expliquent par lui le faible usage de la recherche approfondie [P55] (m2). |
| 3. Plan d'analyse jamais produit | **Oui**, en mode automatique : les six configurations l'activent, les deux automatiques comprises [X11]. | Aucun ; l'application propose un plan en mode piloté [A64]. | Non ; préciser le mode (m2). |
| 4. Pause pour sélection jamais émise | Oui comme chemin mort : le statut n'est produit nulle part [X12]. | — | Oui : ce n'est pas un écart avec le texte, puisque la sélection passe par un fichier écrit à la main (m3). |
| 5. Tâche et directeur | Pas un écart avec le texte : la p. 25 [P22] ne promet pas la tâche au directeur. | — | La lettre du tableau est fausse : l'invite système du directeur annonce une tâche [C50]. Pour ProteinGym, la tâche est dans la description des données [C51] (m17). |
| 6. Crochet de protection des processus | **Oui** : il réécrit et autorise [C32]. Sa branche de refus emploie le format que le module voisin dit ignoré [C41, C33]. Rien n'y vise les commandes longues. | Il sert aussi l'agent OpenTargets [C40], que décrit la phrase de [P33] [P54] ; pour l'agent d'exécution, l'annexe dit seulement « screens » [A41]. | Non ; le contexte de [P33] est à rétablir (m4). |
| 7. « Vérification » de la mémoire | Oui comme absence de tout contrôle par programme : seule une consigne « Verify every important detail is preserved » (`results_memory.py`, l. 157). | — | Non : « écart de lettre » est le bon degré, puisque le texte prête la vérification au raffineur, qui est un modèle. La carte ajoute que la consigne demande aussi d'élaguer [C52]. |
| 8. Consigne d'épreuve | **Oui** : aucune invite employée par le lanceur n'interdit de télécharger ; l'invite de structure servie à l'agent d'exécution l'invite même à ajouter des « downloaded datasets » à `data/` [C42]. | — | Non. |
| 9. « 14x » contre « nine times » | Oui, deux mesures différentes. | — | Non. |

**Écarts que la note ne voit pas**, relevés par la carte et vérifiés par moi (détail au § 7) :
- **Mémoire procédurale** : la limite d'édition des deux sous-agents de documentation n'est qu'une consigne, donnée à l'un des deux seulement [C48, C49]. La note les dit « conformes » (m18).
- **Exploration** : les tours exploratoires des configurations diffèrent de la table 35 [X14, C53, A69].

---

## 4. Les collisions (§ 6 de la note)

| revendication | verdict de la note | tient ? | remarque |
|---|---|---|---|
| Juge au nul formé des lois connues (N-071, N-067 point 2) | sans rapport | **oui** | aucun juge statistique, aucun nul, aucune règle de promotion ; l'hypothèse va au directeur « without a judge » [A19] |
| Statistique calculée par l'orchestrateur, engagement scellé | sans rapport | oui | mais ce n'est plus une revendication : N-067 (point 1) dit ces composantes empruntées [N51] (m9) |
| Séparation de qui produit et de qui juge (O1) | voisine, principe | oui | déjà non revendiquée (N-067, point 5) |
| Scellement avant lecture (O17) | voisine, plus faible | oui | — |
| Attaque de Goodhart, forme resserrée (N-067, point 3) | voisine, n'occupe pas | **oui** | ni proposeur chargé de tromper, ni description du juge lue, ni bras avec et sans verdicts ; l'erreur est insérée une fois par un tiers [P36, P07] |
| Banc de tricheurs | voisine | oui | mais O11 n'a « plus aucune revendication d'idée » depuis N-067 [N50] (m9) |
| Second terrain du papier C (N-065, rôle 1) | **voisine proche** | **oui** | M1 le renforce plutôt : un même auditeur, une trace qui change, voilà la mesure d'un auditeur ; ce qui n'y est pas : l'attaque, l'adaptation, la trace trompeuse |
| Héritage et mémoire transmise (N-073, compléments 1 à 3) | voisine | **oui** | mémoire tenue dans une course, jamais héritée d'une autre ; aucun bras né vide ni sans mémoire ; la forme du complément 3 n'est pas touchée |
| « Le séquentiel doit battre le meilleur de N tirages » (N-073, § 2) | voisine, indice | **non** | les deux bras comparés sont séquentiels et aucun meilleur de N n'est mesuré (m10) |
| Boucle générer, classer, faire évoluer | voisine | oui | — |
| HC1, loi de déférence | sans rapport | oui | l'anecdote est un retrait devant une preuve montrée (m8) |
| HC2, HC2b | sans rapport | oui | la surface notée pour HC3 (l'agent audité écrit ce que l'auditeur lit d'abord [A33]) concerne aussi l'« agent auteur » de HC2 ; c'est une surface, non une revendication : pas de correction |
| HC3, usurpation | sans rapport sur la revendication ; surface voisine | oui | — |

**Règle R8 respectée.** Aucune zone n'est déclarée libre ; la phrase « ne rend libre aucune zone » est la bonne. Un seul endroit à resserrer : l'idée 1 présente « le bras que le papier n'a pas » sans dire qu'une limite de ce papier n'est pas un trou du champ (m13).

---

## 5. Les cinq idées (§ 5 de la note)

| idée | la prédiction signée a-t-elle un sens ? | test sur monde planté jouable sous N-058 ? | coût plausible ? | déjà ailleurs dans nos pièces ? |
|---|---|---|---|---|
| 1. Banc des affirmations fausses face au registre | Oui. La classe C « nulle face au témoin » demandera une marge d'équivalence au préenregistrement ; les tirages frais « positifs » servent de témoin de puissance. | Oui : le score se fait par identifiant, par programme, et le lecteur est mesuré sans rien trancher. | Oui, ancré sur le tarif des juges de la ligne 3 si chaque lecture est un appel unique, plus si c'est une session à outils (m11). | En partie : la classe C ressemble par sa construction au bras de diagnostic « entrées fausses plantées » du plan de l'héritage [N37]. Le rang 10 de l'ordre de passage (« la trace de lecture », [N56]) reste à ouvrir : ni le rédacteur ni moi n'avons lu ses cartes (m13). |
| 2. Fuite plantée et retour arrière | Oui sous consigne seule (prises non nulles). « Zéro sous isolement » est une garde à éprouver (règle R5), non une hypothèse. | Oui, mais le chemin de la détection est flou : qui prend l'appât, et comment l'oracle le voit. Et sous la forme imposée, l'expérimentateur n'a « rien à décider » [N47] (m12). | Inconnu tant que le coût d'un test de mort réel n'est pas mesuré [N53] (m11). | Pour l'isolement, déjà sondé au palier 0a, réseau refusé compris [N46]. |
| 3. Vue consolidée contre registre brut | Faiblement : « négatif ou nul » ne se réfute que par un écart positif, que « ce qui la tuerait » ne nomme pas (M6). | Oui : oracle de l'héritage. | Non chiffré ; ancrable sur les bornes de l'ordre de passage [N52] (M6). | **Oui, pour l'essentiel** : le plan v5 prévoit déjà un « registre paraphrasé » et un « historique brut … sans registre » parmi ses bras de diagnostic [N37, N38], et laisse au préenregistrement « ce qui est servi quand le registre dépasse la taille bornée » [N39]. Servir un texte libre écrit par un modèle déroge aux « champs typés et bornés » [N40] (M6). |
| 4. Critique servie contre texte témoin | Oui : le texte témoin de même longueur sépare le contenu de la présence d'un texte. | Oui, sous le nœud ouvert « note du juge montrée ou non » [N07], que la note signale. | Non chiffré ; de l'ordre de trois courses v9 par répétition [N42] ; la page de tête dit « deux bras », le § 5 « trois » (m11). | Non trouvé dans les pièces lues. |
| 5. Consigne de juge conçue par monde | Mal fondée : la consigne fixe est déjà commune aux deux juges, donc « même concepteur » ne distingue pas les deux bras ; le contraste utile est « même concepteur » contre « concepteurs distincts » (M7). | Oui sur les témoins plantés, mais **pas comme bras de la ligne 3** : son texte scellé (compagnon d'empreinte conforme) fige « même consigne figée » et un plafond de 25 USD que le cas haut de son devis approche (22,49 USD) [N44, N45] (M7). | Quelques dizaines de dollars par variante [N43], sur un devis neuf. | Sa place naturelle est la note de conception du juge que GO-2026-11-19-77 attend [N48]. |

**Remarque sans correction.** N-072 confie l'affinage de la matière première à l'organisme lui-même, dans une course préenregistrée [N55]. Les cinq idées, déjà mises en forme ici par une session, ne peuvent donc être versées que comme matière première : c'est ce que la note dit.

---

## 6. La proposition sur les citations obligatoires

**Sur le fond, elle tient.**
- **Proportionnée** : citation obligatoire seulement dans les textes qui présentent l'organisme comme second terrain du papier C, ou un banc d'auditeurs d'affirmations de recherche.
- **Juste sur la voisine la plus proche** : le banc mesure un auditeur génératif d'affirmations de recherche sur des fautes plantées, avec un témoin sans trace.
- **Conforme à la pratique** de N-064 et de N-067.
- **Respecte la règle R8.**

**Deux défauts de forme**
- **M8.** La page de tête nomme « (a) » et « (b) » les deux volets d'une même recommandation. Le § 6 nomme « (a) », « (b) » et « (c) » trois options rivales, dont l'option (b) est le contraire du volet (b). Lazar pourrait trancher sur un malentendu.
- **Défaut** : c'est un nœud ; il n'a donc pas de défaut sous 48 heures, et il faut l'écrire.

**La liste « Ne pas écrire » est à compléter (m14)** par les trois phrases que cette contre-lecture a trouvées fausses ou trop fortes :
- l'auditeur qui différerait selon la source ;
- le relecteur « jamais lancé » ;
- le meilleur modèle « choisi après coup ».

**À noter pour tout texte qui citera DiscoveryAgent** : décrire le banc avec la lettre corrigée — même auditeur pour les trois sources, rapport corrompu, trace honnête.

---

## 7. Recoupement avec la carte du code (pièce ajoutée par le coordinateur)

### 7.1 Accords

Les deux lectures, faites séparément, relèvent les mêmes faits :
- le relecteur jamais appelé avec les configurations publiées (carte : § 2.5 et contrôles R01 à R03) ;
- le rapport de littérature lu, jamais injecté (R04) ;
- le drapeau du plan jamais relu (R05) ;
- le statut de pause jamais produit (R06) ;
- la mémoire filtrée et « vérifiée » par consigne seulement ;
- le crochet de protection des processus qui réécrit au lieu de refuser ;
- l'absence de candidats, de révision, du banc et de l'étude humaine dans le dépôt ;
- l'absence de tout outil pour le retour en arrière après la fuite.

### 7.2 Divergences, et qui a raison

1. **La tâche et le directeur.**
   - **Synthèse** : « ce n'est pas un écart » (p. 25).
   - **Carte** : la tâche n'est jamais transmise, « alors que son invite système annonce une tâche » (`director_agent.py`, l. 70) [C50].
   - **Verdict** : les deux ont raison, chacune sur son terrain.
     - Face au texte, ce n'est pas un écart : la p. 25 [P22] énumère les entrées du directeur sans la tâche.
     - Dans le code, c'est un défaut interne : l'invite annonce ce qui n'arrive pas.
     - Pour les deux campagnes ProteinGym, la tâche est écrite dans la description des données [C51], que le directeur reçoit. Le défaut ne touche que les campagnes à fichier de tâche séparé (Dwarf, ACS, GW-CD4), toutes pilotées par un scientifique.
   - **Conclusion de la synthèse** : inchangée. Sa lettre est à corriger, car « ne mentionne jamais la description de la tâche » est faux pour l'invite système (m17).
2. **La mémoire procédurale.**
   - **Synthèse** : « conformes ».
   - **Carte** : écart, car la limite d'édition n'est qu'une consigne, donnée au seul DOCUMENTATION.md.
   - **Vérifié** : les deux sous-agents reçoivent l'outil d'édition sans restriction de fichier [C48], et la seule consigne de limite vise DOCUMENTATION.md [C49] ; l'annexe dit « can edit only their assigned document » [A35].
   - **Verdict** : la carte a raison (m18). Aucune conclusion ne change : la mémoire procédurale est « sans objet » pour l'organisme.
3. **Les entrées du directeur.**
   - **Synthèse** : « conforme ».
   - **Carte** : « partiel », car seul le rapport de la dernière requête est réinjecté à chaque tour de parole, les précédents restant dans la conversation.
   - **Verdict** : nuance de mécanique, pas un désaccord sur les faits ; aucune correction.

### 7.3 Écarts propres à la carte : changent-ils une conclusion ?

| écart relevé par la carte | vérifié par moi | change-t-il une conclusion de la synthèse ? |
|---|---|---|
| Modèle d'exécution de DA-Steer : la p. 31 dit « the ProteinGym configuration uses Sonnet 4.6 » [P58] ; la configuration de DA-Steer dit Opus 4.6 [C24], comme la p. 32 [P35] et la table 35 pour les manches 0 à 7 | oui (p. 31, 32 et 115 du PDF ; configuration) | **Non.** C'est une contradiction interne au papier : la p. 31 contre la p. 32 et la table 35. La configuration confirme la p. 32, sur laquelle la synthèse fonde sa troisième faiblesse [P35, C23, C24]. Cette faiblesse en sort renforcée : lue seule, la p. 31 cacherait le changement de modèle entre les deux bras. |
| Aucun agent d'audit à outils dans le dépôt : ni configuration en lecture seule, ni configuration avec exécution, ni harnais Codex | oui (p. 30 ; liste des fichiers ; aucune occurrence de « codex » dans le dépôt [X15]) | **Non** ; la synthèse le dit en substance (« absent du dépôt lu »). Une précision s'impose (m6) : l'auditeur du banc est la configuration en lecture seule sous le harnais Codex [P50], et non l'agent de l'application ; son code n'est dans aucun des deux dépôts lus. Les verdicts du banc ne se rejouent donc pas. |
| Tours exploratoires : la table 35 dit 1 pour les six campagnes [A69] ; les configurations disent 0 pour l'économie et la génomique [C53, C54], et rien pour DA-Steer [X14] | oui | **Non.** Cela appuie la lecture que corrige m1 : les configurations publiées ne sont pas celles des courses (« not a manifest of every invocation » [C46]). Trois des quatre campagnes qui ont des relectures sont justement celles dont la configuration s'écarte de la table 35 : c'est un indice, non une preuve. La retenue des relectures ne lit pas le mode du tour (carte, § 2.5) : l'écart 1 reste entier. |
| Crochets de l'agent OpenTargets : la protection d'écriture pose elle aussi sa décision au premier niveau ; rien ne vise les commandes longues | oui pour la protection des processus (lue en entier) ; la protection d'écriture n'a été lue que par la carte | **Non** : cela renforce l'écart 6 et le motif de l'idée 2 (configuré n'est pas tenu). |
| Le raffineur doit aussi « élaguer » (`results_memory.py`, l. 161) [C52] | oui | **Non** : cela appuie la prédiction de l'idée 3 (perte d'entrées). |
| Chaîne d'audit du dépôt : extracteurs désaccordés des fichiers écrits par le flux | non vérifié par moi | **Non** : l'audit du papier n'est pas dans ce dépôt de toute façon. |
| Invite du relecteur gardée à la racine, réécrite à chaque lancement ; liste de candidats jamais écrite par ce dépôt | non vérifié par moi | **Non.** |

**Conclusion du recoupement** : aucune des conclusions de la synthèse ne change, qu'il s'agisse des collisions, des idées, de la proposition sur les citations ou des trois faiblesses de leur preuve. La carte corrige deux lignes du tableau (m17, m18) et éclaire l'écart 1 (m1).

---

## 8. Constats et corrections

Ordre : majeurs, puis mineurs. Le programme applique les couples dans l'ordre de ce fichier.

### M1 — majeur — § 3.1 : l'auditeur ne change pas d'une source de trace à l'autre

**Constat.**
- **Ce que dit la note** : « l'auditeur de la trace de DiscoveryAgent est « the audit agent », celui des deux autres « a coding agent » [P08] », rangé parmi les « confusions reconnues ».
- **Ce que disent les auteurs** :
  - la même p. 8 : « we held … the auditor harness fixed across systems » [P48] ;
  - les méthodes : « varies the trace while holding the auditor fixed » [P49] ;
  - la p. 30 : la configuration en lecture seule est « used as the fixed auditor in the corrupted-claim benchmark » [P50] ;
  - l'annexe : « every trace-source arm used the same read-only coding-agent auditor » [A49].
- **Ce qui diffère vraiment** : les consignes de navigation, selon la trace [A51, A52].
- **Conséquence** : la note attribue aux auteurs une confusion qu'ils ne reconnaissent pas et que leurs méthodes excluent.

#### Correction M1-a
> AVANT : - **Confusions reconnues.** Les traces ne sont pas ramenées à une forme commune [A07] ; l'auditeur de la trace de DiscoveryAgent est « the audit agent », celui des deux autres « a coding agent » [P08].
> APRÈS : - **Confusions, reconnues ou non.** Les traces ne sont pas ramenées à une forme commune [A07], et les consignes de navigation données à l'auditeur diffèrent selon la trace [A51, A52]. L'auditeur, lui, est le même pour les trois sources : si la p. 8 nomme « the audit agent » d'un côté et « a coding agent » de l'autre [P08], la même page tient « the auditor harness fixed across systems » [P48], et les méthodes comme l'annexe disent un même auditeur en lecture seule pour les trois traces [P49, P50, A49].

### M2 — majeur — page de tête : « aucun de ses mécanismes n'est isolé par une ablation »

**Constat.**
- **Ce que disent les auteurs** : ne pas fournir d'ablations « comprehensive » [P17].
- **Ce qui est isolé** : le témoin sans trace retire l'accès de l'auditeur à la trace, « as the single manipulated variable » [A50]. La note elle-même en conclut au § 3.1 que « la trace sert ».
- **Ce qui est juste** : aucun mécanisme de la boucle de recherche (mémoire, relecteur, directeur) n'est isolé dans les pages lues.

#### Correction M2-a
> AVANT : sa preuve porte sur des erreurs glissées dans un rapport, face à une trace honnête, sur une seule course par système, et aucun de ses mécanismes n'est isolé par une ablation [P17].
> APRÈS : sa preuve porte sur des erreurs glissées dans un rapport, face à une trace honnête, sur une seule course par système ; aucun mécanisme de la boucle de recherche n'est isolé par une ablation (les auteurs disent ne pas fournir d'ablations « comprehensive » [P17]), et le seul retrait isolé trouvé dans les pages lues est celui de la trace donnée à l'auditeur, dans un témoin du banc [A50].

### M3 — majeur — § 3.3 et idée 2 : la fuite, plus sévère que les faits

**Constat.** L'annexe p. 23 rapporte ce que la note omet :
- **Quarantaine** : le dossier fuité a été placé hors de la liste de lecture, donc gardé [A53].
- **Refus enregistrés** : des refus des crochets de fichiers attestent le bac à sable [A66], dont celui d'une reprise qui retrouvait ce dossier [A54].
- **Test de recouvrement** : un test entre entraînement et épreuve ne trouve aucun recouvrement, pour une branche de DA-Steer [A55].

**Conséquences pour la note.**
- « La preuve de la fuite n'est plus dans l'enregistrement » et « l'instrument qui a trouvé la fuite est le seul à dire qu'il n'y en a plus » sont trop forts. Le second ne vaut que pour les manches suivantes de DA-Auto.
- L'élagage de l'historique Git est un geste de confinement ; il reste à comparer à notre règle « inventorier et verser avant d'effacer », sans inventaire scellé dans les pages lues.

#### Correction M3-a
> AVANT : - **Ce que la réparation prouve.** Peu : le bloqueur n'a jamais rien refusé [A15] ; le gardien d'après-outil ne voit pas ce qu'un processus du terminal écrit [A16] ; la vérification finale est faite par les agents d'audit eux-mêmes [A18]. L'instrument qui a trouvé la fuite est le seul à dire qu'il n'y en a plus.
> APRÈS : - **Ce que la réparation prouve.** Peu sur le réseau : le bloqueur d'adresses n'a jamais rien refusé [A15] ; le gardien d'après-outil ne voit pas ce qu'un processus du terminal écrit [A16] ; la vérification des manches suivantes est faite par les agents d'audit eux-mêmes [A18]. À décharge : des refus des crochets de fichiers sont enregistrés [A66], dont celui d'une reprise qui retrouvait le dossier mis en quarantaine [A54], et un test de recouvrement des variants entre entraînement et épreuve ne trouve aucun recouvrement, pour une branche de DA-Steer seulement [A55]. Pour les manches suivantes de DA-Auto, l'instrument qui a trouvé la fuite reste le seul à dire qu'il n'y en a plus.

#### Correction M3-b
> AVANT : - **Un geste contraire à notre règle.** L'historique a été élagué pour que les données téléchargées disparaissent [A17] : la preuve de la fuite n'est plus dans l'enregistrement. Chez nous, on inventorie et on verse avant d'effacer.
> APRÈS : - **Un geste à comparer à notre règle.** L'historique Git de l'espace de travail a été élagué pour que les objets devenus inaccessibles ne gardent pas les données téléchargées [A17] ; le dossier fuité, lui, a été mis en quarantaine hors de la liste de lecture [A53] : la preuve n'est donc pas détruite, mais rien, dans les pages lues, ne dit qu'elle ait été inventoriée ni scellée. Chez nous, on inventorie et on verse avant d'effacer.

#### Correction M3-c
> AVANT : Contrairement à eux [A17], rien n'est effacé : la prise est versée et scellée.
> APRÈS : À la différence de leur élagage [A17], qui garde le dossier fuité en quarantaine [A53] sans inventaire scellé dans les pages lues, rien n'est effacé ici : la prise est inventoriée, versée et scellée.

### M4 — majeur — tableau, ligne 10, et § 4 : le choix du modèle final

**Constat.**
- **Ce que dit la note** : « la trace nommait plusieurs « meilleurs » modèles ; les auteurs en ont choisi un ».
- **Ce que dit l'annexe p. 9** :
  - un seul modèle est nommé « best overall », dans le rapport de la requête 9 de la manche 2, « before the test set was touched » [A56] ;
  - les autres documents sont une recommandation de production plus simple et un troisième document [A26] ;
  - les auteurs retiennent le « best overall », « the selection rule applied to the comparators » [A57] ; les méthodes le redisent [P51].
- **Le sous-ensemble filtré de l'épreuve** est commun aux systèmes comparés [P57].
- **Ce qui reste juste** : l'évaluation a été écrite des mois plus tard, sur un modèle réentraîné ; aucune pièce lue ne montre la règle fixée avant l'évaluation.

#### Correction M4-a
> AVANT : La trace nommait plusieurs « meilleurs » modèles ; les auteurs en ont choisi un [A26] ; l'évaluation a été écrite des mois plus tard [A27], sur un modèle réentraîné après coup [A28] et un sous-ensemble filtré de l'épreuve [A29]. Règle non écrite d'avance dans les pièces lues.
> APRÈS : La trace nomme un modèle « best overall » à la manche 2, requête 9, avant tout contact avec l'épreuve [A56], à côté d'une recommandation de production plus simple et d'un troisième document [A26] ; les auteurs retiennent le « best overall », règle qu'ils disent appliquer aussi aux concurrents [A57, P51]. L'évaluation a été écrite des mois plus tard [A27], sur un modèle réentraîné après coup [A28] et sur un sous-ensemble filtré de l'épreuve, commun aux systèmes comparés [A29, P57]. La règle est écrite dans l'annexe et les méthodes ; rien, dans les pièces lues, ne montre qu'elle ait été fixée avant l'évaluation.

#### Correction M4-b
> AVANT : Choisir après coup entre plusieurs « meilleurs » candidats de la trace [A26].
> APRÈS : Choisir après coup entre des candidats de la trace [A26] selon une règle qui n'a pas été fixée d'avance.

### M5 — majeur — page de tête et § 3.2 : l'étude humaine, sans les faits à décharge

**Constat.**
- **« Le résultat tient sur une personne » est trop fort.**
  - Sans le participant R04, le groupe d'audit garde 4 erreurs uniques contre 1, soit 1,33 contre 0,25 en moyenne : environ 5 fois, toujours dans le même sens (calcul du contre-lecteur sur le tableau 11 [A31]).
  - C'est le chiffre de 14 qui tient, pour l'essentiel, sur une personne.
- **« Dix des quatorze erreurs retrouvées » est imprécis.** Le tableau dit « a non-additive total » pour les erreurs uniques [A62] ; le total additif de 14 est celui des trouvailles appariées.
- **Deux faits à décharge sont omis.**
  - L'apparieur modèle ne voit ni le nom ni le groupe du participant [A58, P52], et ses cinq appels coïncident pour 53 trouvailles sur 54 [A59].
  - Les deux arbitrages sans aveugle vont contre le groupe d'audit [A61, A60].

#### Correction M5-a
> AVANT : 2. **L'étude humaine tient sur huit personnes et un participant.** Le « 14 fois » du résumé [P01] est le rapport de 3,50 à 0,25 [P11] ; un seul participant porte dix des quatorze erreurs retrouvées [A31] ; le groupe témoin n'avait droit à aucun outil d'intelligence artificielle [P43].
> APRÈS : 2. **L'étude humaine tient sur huit personnes, et son « 14 fois », pour l'essentiel, sur un participant.** Le « 14 fois » du résumé [P01] est le rapport de 3,50 à 0,25 [P11] ; un seul participant porte dix des quatorze trouvailles appariées du groupe d'audit [A31] ; sans lui, l'écart garde son sens mais tombe à environ 5 fois (1,33 contre 0,25, calcul du contre-lecteur sur le tableau 11) ; le groupe témoin n'avait droit à aucun outil d'intelligence artificielle [P43].

#### Correction M5-b
> AVANT : - **Le résultat tient sur une personne** : un participant du groupe d'audit retrouve dix erreurs, les trois autres trois, zéro et une [A31].
> APRÈS : - **Le chiffre de tête tient, pour l'essentiel, sur une personne** : un participant du groupe d'audit retrouve dix erreurs, les trois autres trois, zéro et une [A31] ; sans lui, l'écart garde son sens mais tombe à environ 5 fois (calcul du contre-lecteur). Les comptes d'erreurs uniques ne s'additionnent pas d'un participant à l'autre [A62] ; le total additif de quatorze est celui des trouvailles appariées.

#### Correction M5-c
> AVANT : - **Qui note.** Un modèle apparie les trouvailles aux erreurs plantées [A42], puis un auteur tranche deux cas, sans aveugle [P44, A30].
> APRÈS : - **Qui note.** Un modèle apparie les trouvailles aux erreurs plantées [A42], sans voir ni le nom ni le groupe du participant [A58, P52], en cinq appels dont les ensembles d'appariement coïncident pour 53 trouvailles sur 54 [A59] ; puis un auteur tranche deux cas, sans aveugle [P44, A30], et les deux arbitrages vont contre le groupe d'audit : pas d'appariement pour R01 là où un appel sur cinq en voyait un, et, pour R04, une seconde erreur que les cinq appels appariaient est retirée [A61, A60].

### M6 — majeur — idée 3 : déjà dans le plan de l'héritage, prédiction mal bornée, coût absent

**Constat.**
- **Déjà dans le plan v5 de l'héritage.**
  - Ses bras de diagnostic comptent déjà un « registre paraphrasé » et un « historique brut de la source laissé en place, sans registre » [N37, N38].
  - Le préenregistrement doit déjà dire « ce qui est servi quand le registre dépasse la taille bornée » [N39].
  - Servir un texte libre écrit par un modèle déroge aux « champs typés et bornés » [N40] : l'idée ne peut vivre que comme bras de diagnostic.
- **Prédiction mal bornée.** La prédiction « négatif ou nul » ne se réfute que par un écart positif, et « ce qui la tuerait » ne le nomme pas.
- **Coût absent**, alors que le mandat demande un ordre de grandeur.

#### Correction M6-a
> AVANT : - **Énoncé.** À l'épreuve sur l'héritage, ajouter un bras de diagnostic où ce qui est servi au proposeur n'est pas le registre brut mais une vue bornée, réécrite par un modèle à la façon de leur mémoire à trois agents [P27], à coût de lecture égal [N17].
> APRÈS : - **Énoncé.** À l'épreuve sur l'héritage, donner au bras de diagnostic « registre paraphrasé », déjà prévu [N37], une variante où ce qui est servi au proposeur n'est pas le registre brut mais une vue bornée, réécrite par un modèle à la façon de leur mémoire à trois agents [P27], à coût de lecture égal [N17]. Comme tout bras de diagnostic, elle n'entre dans aucun verdict ; servir un texte libre écrit par un modèle déroge à la règle des champs typés et bornés [N40], ce qui la confine à ce bras.

#### Correction M6-b
> AVANT : - **Coût.** Un bras de plus à un palier payant de l'héritage, plus les appels de réécriture ; sur devis.
> APRÈS : - **Coût.** Sur processeur, 0 USD d'appels, avec des proposeurs scriptés et un réécrivain scripté qui perd une part fixée d'entrées, pour montrer que l'instrument voit la perte. À l'étage payant, de l'ordre du coût d'un bras de l'héritage plus les appels de réécriture : d'après les bornes de l'ordre de passage pour trois ou quatre bras [N52], quelques dizaines à quelques centaines de dollars par bras à composition réduite, davantage à composition pleine ; sur devis.

#### Correction M6-c
> AVANT : - **Ce qui la tuerait.** Un écart indiscernable du bruit au pilote, avec une perte d'entrées nulle : la question ne vaut pas un bras.
> APRÈS : - **Ce qui la tuerait.** Pour la prédiction : un écart positif net de la vue consolidée sur le registre brut, le registre tenant dans le budget de lecture. Pour son utilité : un écart indiscernable du bruit au pilote, avec une perte d'entrées nulle ; la question ne vaut alors pas une variante.

#### Correction M6-d
> AVANT : - **Ce qu'elle ne revendique pas.** Rien de neuf : la question de la forme de la mémoire est déjà au complément 3 de N-073, avec ses citations ; aucun bras de mémoire n'a d'effet établi chez un voisin déjà cité [N35]. Ce bras ne dit rien de l'héritage lui-même [N33, N34].
> APRÈS : - **Ce qu'elle ne revendique pas.** Rien de neuf : la question de la forme de la mémoire est déjà au complément 3 de N-073, avec ses citations ; aucun bras de mémoire n'a d'effet établi chez un voisin déjà cité [N35] ; le plan de l'héritage prévoit déjà un registre paraphrasé et un historique brut sans registre parmi ses bras de diagnostic [N37, N38], et laisse au préenregistrement « ce qui est servi quand le registre dépasse la taille bornée » [N39]. Ce bras ne dit rien de l'héritage lui-même [N33, N34].

#### Correction M6-e
> AVANT : | un bras de plus à un palier payant de l'héritage, sur devis |
> APRÈS : | une variante du bras de diagnostic « registre paraphrasé » déjà prévu ; 0 USD sur processeur ; à l'étage payant, quelques dizaines à quelques centaines de dollars par bras à composition réduite, sur devis |

### M7 — majeur — idée 5 : pas jouable comme bras de la ligne 3, prédiction confondue

**Constat.**
- **Pas un bras de la ligne 3.**
  - Le texte de la ligne 3 (version 4, compagnon d'empreinte conforme) fige « même consigne figée » pour les deux juges [N44].
  - Il pose un plafond d'arrêt dur de 25 USD, que le cas haut de son devis approche déjà, à 22,49 USD [N45].
  - Ajouter un bras « consigne conçue » serait un écart à un texte scellé (nœud de Lazar) et demanderait un devis neuf.
  - Sa place naturelle est la note de conception du juge qu'attend GO-2026-11-19-77 [N48].
- **Prédiction confondue.** La consigne fixe est déjà commune aux deux juges ; « quand le même concepteur écrit pour les deux » ne distingue donc pas les bras. Le contraste signé utile est « un même concepteur pour les deux juges » contre « un concepteur distinct pour chacun ».

#### Correction M7-a
> AVANT : - **Énoncé.** Dans la mesure des votes effectifs des juges croisés sur témoins plantés, ajouter un bras où la consigne de chaque juge est écrite par un modèle concepteur à partir de la description du monde, comme leur concepteur de relecture [P30], au lieu de la consigne fixe.
> APRÈS : - **Énoncé.** Sur les témoins plantés de la mesure des votes effectifs des juges croisés, comparer la consigne fixe à une consigne écrite pour chaque monde par un modèle concepteur, à partir de la description du monde, comme leur concepteur de relecture [P30] ; deux variantes : un même concepteur écrit pour les deux juges, ou un concepteur distinct pour chacun. La ligne 3 fige « même consigne figée » pour ses deux juges, sous un plafond de 25 USD que le cas haut de son devis approche déjà [N44, N45] : l'idée n'y entre pas comme bras ; elle relève d'une ligne neuve, ou de la note de conception du juge attendue [N48], sur son propre devis.

#### Correction M7-b
> AVANT : - **Prédiction signée.** Corrélation des erreurs des deux juges : consigne conçue moins consigne fixe, écart positif (moins de votes effectifs) quand le même concepteur écrit pour les deux ; taux de faux acceptés : écart nul.
> APRÈS : - **Prédiction signée.** Corrélation des erreurs des deux juges : consigne conçue par un même concepteur pour les deux juges moins consigne conçue par un concepteur distinct pour chacun, écart positif (moins de votes effectifs) ; consigne conçue moins consigne fixe : signe non prédit, puisque la consigne fixe est déjà commune aux deux juges ; taux de faux acceptés : écart nul.

#### Correction M7-c
> AVANT : - **Coût.** Un bras de l'étage payant de la ligne 3 ; sur devis.
> APRÈS : - **Coût.** De l'ordre de l'étage payant de la ligne 3 par variante, soit quelques dizaines de dollars [N43, N45], plus les appels du concepteur ; sur un devis neuf, hors du plafond de la ligne 3.

#### Correction M7-d
> AVANT : - **Ce qui la tuerait.** Une baisse nette des faux acceptés sans hausse de la corrélation.
> APRÈS : - **Ce qui la tuerait.** Une corrélation qui ne monte pas quand un même concepteur écrit pour les deux juges, face à des concepteurs distincts ; ou une baisse nette des faux acceptés sans hausse de la corrélation.

#### Correction M7-e
> AVANT : | les erreurs des deux juges vont davantage ensemble (moins de votes effectifs) | un bras de l'étage payant de la ligne 3, sur devis |
> APRÈS : | les erreurs des deux juges vont davantage ensemble quand un même concepteur écrit pour les deux (moins de votes effectifs) | quelques dizaines de dollars par variante, sur un devis neuf, hors de la ligne 3 scellée |

### M8 — majeur — proposition sur les citations : deux jeux de lettres pour deux choses différentes

**Constat.**
- **Collision de lettres.** La page de tête nomme « (a) » et « (b) » les deux volets d'une même recommandation. Le § 6 nomme « (a) », « (b) » et « (c) » trois options rivales, dont l'option (b) (« obligatoire dans tout texte qui présente l'organisme ») est l'inverse du volet (b) de la page de tête.
- **Confiances différentes** : 0,75 et 0,7 en tête, 0,75 seule au § 6.
- **Défaut non dit** : c'est un nœud ; il n'a pas de défaut sous 48 heures, et il faut l'écrire.

#### Correction M8-a
> AVANT : **Proposition sur les citations (nœud de Lazar ; je propose, je ne décide pas)** : (a) citation obligatoire dans tout texte qui présente l'organisme comme second terrain du papier C ou qui présente un banc d'auditeurs d'affirmations de recherche ; (b) « à citer quand le point est abordé » pour la mémoire et l'héritage, sans entrer dans les citations obligatoires de l'énoncé 5. Confiance : 0,75 pour (a), 0,7 pour (b).
> APRÈS : **Proposition sur les citations (nœud de Lazar, sans défaut ; je propose, je ne décide pas)** : l'option (a) du § 6, en deux volets — premier volet, citation obligatoire dans tout texte qui présente l'organisme comme second terrain du papier C ou qui présente un banc d'auditeurs d'affirmations de recherche ; second volet, « à citer quand le point est abordé » pour la mémoire, l'héritage et la séparation de qui produit et de qui audite, sans entrer dans les citations obligatoires de l'énoncé 5. Confiance : 0,75 pour le premier volet, 0,7 pour le second.

#### Correction M8-b
> AVANT : - *Recommandation* : (a), confiance 0,75.
> APRÈS : - *Recommandation* : (a), confiance 0,75 pour son premier volet, 0,7 pour le second ; nœud de Lazar, sans défaut.

### m1 — mineur — § 2, écart 1 : les « deux lectures » ne sont pas rivales

**Constat.**
- **Ce qui est certain.** Les configurations publiées ne déclenchent jamais le relecteur, et l'annexe compte des relectures dans quatre campagnes. Au moins ces quatre-là n'ont donc pas tourné avec ce code et ces seules configurations.
- **Ce qui est seulement possible.** Que le défaut explique aussi les deux campagnes sans relecture.
- **Ce que le dépôt dit lui-même.** Ses configurations sont « not a manifest of every invocation » [C46], et aucune option de relecture ne figure parmi les options à ajouter au lancement [C47, X09].
- **Relu par moi.** Le relecteur n'a qu'un appel dans le code [X10].

#### Correction m1-a
> AVANT : Deux lectures possibles, non départagées : les courses ont tourné sur un autre code ou d'autres options (le dépôt dit lui-même ne pas être un instantané [C21, C22]) ; ou le défaut explique les deux campagnes sans relecture [A22].
> APRÈS : Une conséquence est certaine : au moins les quatre campagnes qui ont des relectures n'ont pas tourné avec ce code et ces seules configurations. Le dépôt le laisse d'ailleurs entendre : ses configurations sont « not a manifest of every invocation » [C46], aucune option de relecture n'est nommée parmi les options à ajouter au lancement [C47, X09], et il dit ne pas être un instantané [C21, C22]. Le défaut peut, en plus, expliquer les deux campagnes sans relecture [A22] ; ce n'est pas une lecture concurrente de la première. Relu par le contre-lecteur : le relecteur n'a pas d'autre appel dans le code [X10].

### m2 — mineur — § 2, écarts 2 et 3 : la portée (mode automatique) et deux appuis qui manquent

**Constat.**
- **Rapport de littérature.**
  - L'annexe dit ce rapport versé à l'amorçage des hypothèses de toutes les campagnes [A65], et les auteurs expliquent par lui le faible usage de la recherche approfondie [P55]. L'écart est plus net que ne le dit la note.
  - L'invite d'hypothèse reçoit la mémoire accumulée, non ce rapport [C44].
  - En mode piloté, l'application charge le rapport [A63].
- **Plan d'analyse.** L'application propose aussi le plan en mode piloté [A64], et les six configurations activent le drapeau [X11].
- **Portée.** Les deux écarts valent pour le mode automatique.

#### Correction m2-a
> AVANT : 2. **Rapport de littérature chargé puis inemployé** dans le code lu [C27, X01], contre [P24].
> APRÈS : 2. **Rapport de littérature chargé puis inemployé** dans le code lu [C27, X01], contre [P24] et contre l'annexe, qui le dit versé à l'amorçage des hypothèses de toutes les campagnes [A65] ; les auteurs expliquent même par cet amorçage le faible usage de la recherche approfondie [P55]. L'invite d'hypothèse du code reçoit la mémoire accumulée, non ce rapport [C44]. L'écart vaut pour le mode automatique : en mode piloté, l'application, dépôt non pris, charge ce rapport [A63].

#### Correction m2-b
> AVANT : 3. **Plan d'analyse optionnel** annoncé [P26], non produit par l'invite publiée [C28, C29, X02].
> APRÈS : 3. **Plan d'analyse optionnel** annoncé pour le mode automatique [P26], non produit par l'invite publiée [C28, C29, X02], alors que les six configurations activent le drapeau [X11]. En mode piloté, c'est l'application, dépôt non pris, qui propose un plan [A64].

### m3 — mineur — tableau ligne 1 et § 2, écart 4 : un chemin mort, pas un écart avec le texte

**Constat.**
- **Statut de pause** : il n'est produit nulle part dans le code [X12] ; c'est un chemin mort.
- **Sélection** : elle passe par un fichier écrit à la main ou par l'application, ce que le texte permet.

#### Correction m3-a
> AVANT : 4. **Pause pour sélection** testée mais jamais émise [C30, C31, X08] ; la sélection passe par un fichier écrit à la main ou par l'application non lue [C20].
> APRÈS : 4. **Pause pour sélection** testée mais jamais émise [C30, C31, X08, X12] : c'est un chemin mort du code plutôt qu'un écart avec le texte, puisque la sélection passe par un fichier écrit à la main ou par l'application non lue [C20].

#### Correction m3-b
> AVANT : **Écart** : le statut de pause pour sélection est testé [C30] mais jamais produit par la boucle du directeur [C31, X08] ;
> APRÈS : **Chemin mort**, non un écart avec le texte : le statut de pause pour sélection est testé [C30] mais n'est produit nulle part [C31, X08, X12] ;

### m4 — mineur — § 2, écart 6 : le contexte de [P33] et ce que le crochet ne fait pas

**Constat.**
- **Contexte de [P33]** : la phrase « blocks long-running or destructive commands » décrit l'agent OpenTargets [P54], que le même crochet sert [C40]. Pour l'agent d'exécution, l'annexe dit seulement « screens » [A41].
- **Branche de refus** : elle emploie le même format de premier niveau [C41], que le module voisin dit ignoré [C33].
- **Commandes longues** : rien dans le crochet ne les vise (fichier lu en entier).

#### Correction m4-a
> AVANT : 6. **Crochet de protection des processus** : il réécrit et autorise au lieu de bloquer [C32], à rebours de [P33], et dans un format que [C33] dit sans effet.
> APRÈS : 6. **Crochet de protection des processus** : il réécrit et autorise au lieu de bloquer [C32], à rebours de [P33], phrase qui décrit l'agent OpenTargets [P54], branché sur le même crochet [C40] ; pour l'agent d'exécution, l'annexe dit seulement qu'il « screens » ces commandes [A41]. Sa branche de refus emploie le même format que [C33] dit sans effet [C41], et rien n'y vise les commandes longues que [P33] dit bloquées.

### m5 — mineur — tableau ligne 6 et idée 4 : ce que lit le relecteur

**Constat.**
- **Ce que reçoit le relecteur** : la description des données, la mémoire accumulée des manches précédentes et le rapport cumulé de la manche [C39, C07]. Avec l'option de recherche, active dans les six configurations, il peut aussi chercher sur le web.
- **Ce qui reste juste** : il ne lit jamais le code ni les fichiers.

#### Correction m5-a
> AVANT : Le relecteur ne lit que le rapport écrit par le directeur, jamais le code ni les fichiers [C07, C25].
> APRÈS : Le relecteur ne lit que des textes : la description des données, la mémoire accumulée des manches précédentes et le rapport cumulé de la manche [C39, C07, C25] ; jamais le code ni les fichiers.

#### Correction m5-b
> AVANT : Leur relecteur ne lit que le rapport de l'agent [C07] et n'a jamais été isolé [P17].
> APRÈS : Leur relecteur ne lit que des textes, mémoire accumulée comprise [C39, C07], et n'a jamais été isolé [P17].

### m6 — mineur — page de tête, « ce qui reste invérifié » : deux précisions

**Constat.**
- **Consignes par trace** : elles sont décrites, sans leur texte exact (annexe p. 19, note que le rédacteur dit avoir lue en entier) [A51, A52]. « Non trouvé » est donc inexact pour elles ; il reste juste pour la part d'affirmations corrompues.
- **Auditeur du banc** : ce n'est pas l'agent de l'application [A67]. C'est la configuration en lecture seule, « fixed auditor » du banc [P50] ; son code n'est dans aucun des deux dépôts lus.

#### Correction m6-a
> AVANT : - **Ce que l'auditeur du banc savait** (la part de moitié d'affirmations corrompues, ses consignes par trace) : non trouvé dans les pages lues.
> APRÈS : - **Ce que l'auditeur du banc savait** de la part d'affirmations corrompues : non trouvé dans les pages lues. Ses consignes de navigation par trace sont décrites, sans leur texte exact, et diffèrent d'une trace à l'autre [A51, A52].

#### Correction m6-b
> AVANT : - **L'agent d'audit lui-même n'est pas dans le code lu** : il vit dans l'application de pilotage, dépôt non pris [C19, C20].
> APRÈS : - **L'agent d'audit lui-même n'est pas dans le code lu** : celui de l'interface vit dans l'application de pilotage, dépôt non pris [A67, C19, C20] ; celui du banc est la configuration en lecture seule, « fixed auditor » du banc [P50], dont le code n'est dans aucun des deux dépôts lus.

### m7 — mineur — § 4, ligne 5 : la suppression par l'agent, sans ses atténuations

**Constat.** Le jugement « contraire à « récupérer ce qui est récupérable » » se défend, car rien n'est inventorié ni versé. Deux atténuations manquent :
- l'espace est commité après chaque requête, ce qui garde l'état antérieur dans l'historique [C08, C09] ;
- la même invite interdit de toucher aux fichiers de données [C45].

#### Correction m7-a
> AVANT : Un agent autorisé à supprimer ce qu'il juge contredit [C14] : contraire à « récupérer ce qui est récupérable ».
> APRÈS : Un agent autorisé à supprimer ce qu'il juge contredit [C14], sans inventaire ni versement : contraire à « récupérer ce qui est récupérable », même si, chez eux, le commit après chaque requête en garde l'état antérieur dans l'historique [C08, C09] et si les fichiers de données sont exclus de la suppression [C45].

### m8 — mineur — § 6, HC1 : l'anecdote omet la preuve montrée

**Constat.** Le participant conteste « by pointing to supporting figure evidence » [P53]. Le retrait peut donc être juste, et l'anecdote ne dit rien d'une déférence.

#### Correction m8-a
> AVANT : Une anecdote : un agent d'audit retire une accusation quand un participant la conteste [P14] ; elle ne mesure rien.
> APRÈS : Une anecdote : un agent d'audit retire une accusation quand un participant la conteste en montrant une figure à l'appui [P53, P14] ; rien ne dit si ce retrait est juste ou complaisant, et elle ne mesure rien.

### m9 — mineur — § 6 : deux lignes fondées sur N-064, que N-067 a remplacé sur ces points

**Constat.** N-067 remplace les points 2 à 4 de N-064 :
- la statistique calculée hors des agents et l'engagement scellé « ne sont plus revendiqués : elles sont empruntées et citées » [N51] ;
- O11 n'a « plus aucune revendication d'idée » [N50].

Les deux verdicts tiennent, mais les deux lignes présentent comme revendications ce qui n'en est plus.

#### Correction m9-a
> AVANT : | **Statistique calculée par l'orchestrateur, engagement scellé** (N-064 [N13]) | sans rapport |
> APRÈS : | **Statistique calculée par l'orchestrateur, engagement scellé** (N-064 [N13] ; composantes empruntées et plus revendiquées depuis N-067 [N51]) | sans rapport |

#### Correction m9-b
> AVANT : | **Banc de tricheurs** (forme, N-064) | voisine |
> APRÈS : | **Banc de tricheurs** (O11 : plus aucune revendication d'idée depuis N-067 [N50]) | voisine, sans enjeu de priorité |

### m10 — mineur — § 6 : « le séquentiel contre le meilleur de N » n'est pas ce que mesure [P20]

**Constat.** L'agent autonome et les boucles d'agent de code sont tous séquentiels, et aucun meilleur de N tirages n'est mesuré. [P20] est un indice sur une architecture élaborée face à une boucle simple, pas sur le protocole de N-073, § 2.

#### Correction m10-a
> AVANT : | voisine, indice | La course autonome ne se distingue pas d'une boucle simple [P20], budgets non égalisés : un indice de plus, de même sens que ceux déjà cités, à dire avec sa borne. |
> APRÈS : | sans rapport avec le protocole ; indice lointain | La course autonome ne se distingue pas d'une boucle d'agent de code [P20], budgets non égalisés ; mais les deux bras sont séquentiels et aucun meilleur de N tirages n'est mesuré : c'est un indice sur une architecture élaborée face à une boucle simple, pas sur le séquentiel face aux tirages indépendants, à dire avec sa borne si le point est abordé. |

### m11 — mineur — page de tête, § 5 et § 7 : coûts et nombre de bras

**Constat.**
- **Nombre de bras de l'idée 4** : la page de tête dit « deux bras », le § 5 « trois » (critique, rien, texte témoin).
- **Ordres de grandeur** : le mandat en demande un ; ils manquent ou ne sont pas ancrés. Nos pièces en donnent :
  - une course v9 coûte 72,50 USD par bras [N42] ;
  - l'étage payant de la ligne 3 coûte environ 25 USD [N43] ;
  - le coût d'un test de mort réel n'est pas encore mesuré [N53].

#### Correction m11-a
> AVANT : | deux bras à un étage réel, sur devis ; touche un nœud ouvert de Lazar |
> APRÈS : | trois bras à un étage réel (critique, rien, texte témoin), quelques centaines de dollars par répétition, sur devis ; touche un nœud ouvert de Lazar |

#### Correction m11-b
> AVANT : | surtout du code ; étage réel : dizaines de dollars, sur devis |
> APRÈS : | surtout du code ; étage réel : à chiffrer quand le coût d'un test de mort réel sera mesuré, sur devis |

#### Correction m11-c
> AVANT : - **Coût.** 0 USD d'appels à l'étage sur processeur ; quelques centaines d'appels de lecteur à l'étage réel, dizaines de dollars, sur devis.
> APRÈS : - **Coût.** 0 USD d'appels à l'étage sur processeur ; quelques centaines d'appels de lecteur à l'étage réel : quelques dizaines de dollars si chaque lecture est un appel unique au tarif des juges de la ligne 3 [N43], davantage si le lecteur est une session à outils qui retire des données ; sur devis.

#### Correction m11-d
> AVANT : - **Coût.** Du code et un étage sur processeur à 0 USD d'appels (expérimentateur scripté qui prend, qui ne prend pas) ; étage réel court, dizaines de dollars, sur devis.
> APRÈS : - **Coût.** Du code et un étage sur processeur à 0 USD d'appels (expérimentateur scripté qui prend, qui ne prend pas) ; étage réel court, à chiffrer quand le coût d'un test de mort réel sera mesuré [N53] ; sur devis.

#### Correction m11-e
> AVANT : - **Coût.** Trois bras à un étage réel ; sur devis.
> APRÈS : - **Coût.** Trois bras à un étage réel, chacun de l'ordre d'une course v9, soit 72,50 USD par bras d'après l'ordre de passage [N42], plus les appels du relecteur : quelques centaines de dollars par répétition ; sur devis.

#### Correction m11-f
> AVANT : Les coûts ne sont pas chiffrés.
> APRÈS : Les coûts sont des ordres de grandeur, non des devis.

### m12 — mineur — idée 2 et § 4, ligne 9 : la détection, la forme imposée, l'isolement déjà sondé

**Constat.**
- **Détection.** La note fait passer la détection par l'oracle (« un engagement qui l'emploie »), sans dire qui prend l'appât. La détection directe est la lecture du fichier dans le journal d'accès, par programme.
- **Forme imposée.** Sous la forme imposée du tour fermé, l'expérimentateur n'a « rien à décider » [N47], et les paliers payants imposent cette forme [N49] : l'étage réel doit se jouer sur une forme libre.
- **Isolement.** Il est déjà sondé au palier 0a, « connexion réseau refusée » comprise [N46].

#### Correction m12-a
> AVANT : - **Test sur monde planté, jugé par l'oracle.** La fausse clé rend la prise visible à l'oracle : un engagement qui l'emploie est apparié à une loi que le monde ne contient pas. Aucun modèle ne juge.
> APRÈS : - **Test sur monde planté, jugé par l'oracle.** La prise se compte par programme à deux endroits : la lecture du fichier appât dans le journal d'accès, et tout engagement ou résultat qui emploie la fausse clé, que l'oracle apparie à une loi que le monde ne contient pas. Aucun modèle ne juge. Il faut un expérimentateur qui ait de quoi décider : sous la forme imposée du tour fermé, il n'a « rien à décider » [N47], et les paliers payants de l'héritage imposent cette forme [N49] ; l'étage réel se joue donc sur une forme libre, à préciser.

#### Correction m12-b
> AVANT : Un appât pour mesurer que l'isolement tient, pas seulement qu'il est configuré (idée 2).
> APRÈS : Un appât pour mesurer ce que fait un agent sous la seule consigne (idée 2) ; que l'isolement tienne est déjà sondé au palier 0a, réseau refusé compris [N46].

### m13 — mineur — idée 1 : la phrase de la règle R8 et un voisin dans nos pièces

**Constat.**
- **Règle R8.** « Le bras que le papier n'a pas » est une limite de ce papier, pas un trou du champ ; l'idée doit le dire.
- **Voisin dans nos pièces.** Sa classe C ressemble, par sa construction, au bras de diagnostic « entrées fausses plantées » du plan de l'héritage [N37].

#### Correction m13-a
> AVANT : - **Ce qu'elle ne revendique pas.** Ni l'idée d'un banc d'erreurs plantées pour un auditeur (publiée ici même), ni celle d'un témoin sans trace [P09] ; rien sur la valeur d'un lecteur comme juge ; rien hors des mondes plantés.
> APRÈS : - **Ce qu'elle ne revendique pas.** Ni l'idée d'un banc d'erreurs plantées pour un auditeur (publiée ici même), ni celle d'un témoin sans trace [P09], ni qu'une trace cohérente avec le faux soit un angle neuf du champ : c'est une limite de ce papier, pas un trou du champ (R8), à chercher ailleurs avant toute phrase ; la classe C est proche, par sa construction, du bras de diagnostic « entrées fausses plantées » du plan de l'héritage [N37] ; rien sur la valeur d'un lecteur comme juge ; rien hors des mondes plantés.

### m14 — mineur — § 6 : la liste « Ne pas écrire » à compléter

**Constat.** Trois phrases que cette contre-lecture a trouvées fausses ou trop fortes doivent y entrer :
- l'auditeur du banc qui différerait selon la source ;
- le relecteur qui n'aurait jamais tourné ;
- le meilleur modèle choisi après coup.

#### Correction m14-a
> AVANT : « le pilotage améliore » sans la réserve des auteurs [P16].
> APRÈS : « le pilotage améliore » sans la réserve des auteurs [P16] ; « l'auditeur du banc différait selon la source de trace » (un même auditeur sert les trois [A49]) ; « le relecteur n'a jamais tourné » (le code publié ne le déclencherait pas, mais l'annexe compte des relectures dans quatre campagnes [A21]) ; « les auteurs ont choisi leur meilleur modèle après coup » (il est nommé avant tout contact avec l'épreuve [A56]).

### m15 — mineur — § 3.4 : la symétrie sur la classification d'étoiles variables

**Constat.**
- **Ce que dit la note** : la course autonome n'a pas montré d'avance sur ProteinGym. C'est juste, et borné à ce banc.
- **Ce qu'elle omet** : en classification d'étoiles variables, l'agent autonome a la meilleure exactitude sur l'épreuve parmi les systèmes comparés [P56, P57]. Le dire équilibre l'indice, sans en changer la borne.

#### Correction m15-a
> AVANT : - **Indice à garder.** La course autonome ne se distingue pas d'une simple boucle d'agent de code [P20].
> APRÈS : - **Indice à garder.** La course autonome ne se distingue pas d'une simple boucle d'agent de code [P20] ; en classification d'étoiles variables, l'agent autonome a en revanche la meilleure exactitude sur l'épreuve parmi les systèmes comparés [P56, P57], une course par système là aussi.

### m16 — mineur — § 5, statut commun : deux phrases inexactes

**Constat.**
- **« Le verdict d'un juge ou d'un lecteur modèle est ce qu'on mesure »** ne vaut que pour les idées 1 et 5. Dans les idées 2 à 4, la mesure est faite par programme ou par l'oracle.
- **Les coûts** reçoivent désormais un ordre de grandeur (m11).

#### Correction m16-a
> AVANT : Les coûts sont des ordres de grandeur non chiffrés.
> APRÈS : Les coûts sont des ordres de grandeur, ancrés quand c'est possible sur les montants de nos propres pièces, jamais des devis.

#### Correction m16-b
> AVANT : Dans toutes, le verdict d'un juge ou d'un lecteur modèle est ce qu'on mesure : il ne promeut, n'écarte ni ne sélectionne rien [N20, N01].
> APRÈS : Dans toutes, ce qui tranche est un programme ou l'oracle ; quand un juge ou un lecteur modèle intervient, son verdict est l'objet de la mesure (idées 1 et 5) ou la condition éprouvée (idée 4), et il ne promeut, n'écarte ni ne sélectionne rien [N20, N01].

### m17 — mineur — tableau ligne 2 et § 2, écart 5 : l'invite système du directeur annonce une tâche (recoupement avec la carte)

**Constat.**
- **La lettre du tableau est fausse.** « Ne mentionne jamais la description de la tâche » : l'invite système du directeur annonce « dataset description, task, and potentially a hypothesis » [C50]. Le contrôle X03 ne cherchait que le nom de variable.
- **La conclusion tient.** Il n'y a pas d'écart avec le texte (p. 25), mais un défaut interne au code.
- **ProteinGym.** La tâche est dans la description des données [C51].

#### Correction m17-a
> AVANT : Conforme sur ce point : l'invite du directeur porte la description des données [C34] et ne mentionne jamais la description de la tâche [X03] — ce que le texte ne promet pas non plus.
> APRÈS : Conforme au texte sur ce point : l'invite du directeur porte la description des données [C34], et le code ne lui passe jamais la tâche [X03], ce que le texte ne promet pas non plus ; mais son invite système annonce une tâche [C50] : défaut interne au code. Pour ProteinGym, la tâche est écrite dans la description des données [C51].

#### Correction m17-b
> AVANT : 5. **Description de la tâche et directeur** : ce n'est pas un écart. Le code ne la donne pas au directeur [X03, C34], et le texte ne la lui promet pas [P22].
> APRÈS : 5. **Description de la tâche et directeur** : ce n'est pas un écart avec le texte. Le code ne la donne pas au directeur [X03, C34], et le texte ne la lui promet pas [P22] ; l'invite système du directeur l'annonce pourtant [C50], défaut interne au code, que la carte du code relève aussi. Pour ProteinGym, la tâche est dans la description des données [C51] : le directeur la reçoit par là.

### m18 — mineur — tableau ligne 5 : la mémoire procédurale n'est pas « conforme » (recoupement avec la carte)

**Constat.**
- **Ce que dit l'annexe** : « can edit only their assigned document » [A35].
- **Ce que fait le code** :
  - les deux sous-agents reçoivent l'outil d'édition sans restriction de fichier [C48] ;
  - la seule consigne de limite vise DOCUMENTATION.md [C49].

#### Correction m18-a
> AVANT : Deux sous-agents de documentation, conformes.
> APRÈS : Deux sous-agents de documentation ; **écart** : la règle « chacun n'édite que son document » [A35] n'est qu'une consigne, donnée au seul agent de DOCUMENTATION.md, et les deux reçoivent l'outil d'édition sans restriction de fichier [C48, C49].

### m19 — mineur — annexe de la note : deux lignes de la table retouchées à la main

**Constat.**
- **Écart avec la sortie du programme.** La table est dite « produite par » le programme du rédacteur « puis collée ici ». Deux lignes (X04, X05) diffèrent pourtant de sa sortie : les barres verticales des motifs y sont rendues par des barres obliques, que le programme ne produit pas dans la colonne « lieu ».
- **Gravité.** Retouche bénigne, à dire.
- **Pour la version neuve** du programme : rendre ces barres lui-même.

#### Correction m19-a
> AVANT : à partir du registre `outils-synthese-v1/citations-synthese-v1.json`, puis collée ici.
> APRÈS : à partir du registre `outils-synthese-v1/citations-synthese-v1.json`, puis collée ici ; dans la colonne « lieu » de X04 et X05, les barres verticales des motifs sont rendues à la main par des barres obliques, que le programme ne produit pas.

---

## 9. Ce que j'ai ouvert, et ce que je n'ai pas ouvert

**Ouvert (lecture de fichier, `sed`, `grep`, `git show` ou `git grep`)**

*Le dossier de la note*
- `docs/notes/organisme-auto-conception-v1/lectures/discoveryagent-v1/` :
  - le mandat du rédacteur ;
  - la synthèse ;
  - les empreintes compagnons ;
  - `outils-synthese-v1/` : le programme, sa sortie, le registre (ses sources et une entrée par type).

*Les sources*
- `docs/sources/arxiv-2611.21950-v1/` :
  - `PROVENANCE-v1.md` ;
  - les deux PDF, aux pages du § 1.2 ;
  - les deux textes extraits, par recherche de mots seulement.

*Le dépôt du code (au commit)*
- configuration Git locale et liste des crochets ; liste des fichiers suivis ;
- `README.md` (l. 1-30, 120-290) ;
- `DiscoveryAgent/director_workflow.py` (l. 340-419, 560-604, 842-858, 955-975, 1120-1179, 1218-1236, 1268-1312, 1370-1395, 1556-1680) ;
- `DiscoveryAgent/hypothesis_brancher.py` (l. 128-207, 330-444, 578-667, 790-798, 805-840) ;
- `DiscoveryAgent/hyp_agents/hypothesis_gen_agent.py` (l. 50-145, 265-364) ;
- `DiscoveryAgent/hyp_agents/director_agent.py` (l. 68-71, 580-594) ;
- `DiscoveryAgent/utils/arg_parsers.py` (l. 1-40, 135-169) ;
- `DiscoveryAgent/tool_agents/security/kill_blocker.py` (en entier, avec l'outil de lecture) ;
- `DiscoveryAgent/tool_agents/security/sandbox_enforcement.py` (l. 1-20, 100-149) ;
- `DiscoveryAgent/tool_agents/security/url_blocker.py` (l. 15-24) ;
- `DiscoveryAgent/tool_agents/execution_agent_cc.py` (l. 995-1012, 1028-1052) ;
- `DiscoveryAgent/checkpoint_manager.py` (l. 885-910) ;
- `DiscoveryAgent/memory/results_memory.py` (l. 155-162, 340-368, 510-526) ;
- `DiscoveryAgent/prompts/hyp_generation.py` (l. 48-60, 105-160) ;
- `DiscoveryAgent/prompts/execution_agent.py` (l. 236-252) ;
- `DiscoveryAgent/prompts/review_agent.py` (l. 1-6) ;
- `DiscoveryAgent/prompts/cc_sub_agents.py` (l. 60-78) ;
- `DiscoveryAgent/prompts/claude_md_generator_command.py` (l. 171-174) ;
- `scripts/plan.py` (début) ;
- `scripts/utils/audit_run.py` (l. 1-10) ;
- `configs/paper/dms_steer.yaml` (en entier) ; `configs/paper/dms_auto.yaml` (l. 9-12) ; les six configurations par recherche de clés ;
- `inputs/dms_auto/README.txt` (l. 1-12) et `inputs/dms_steer/README.txt` (l. 6-8) ;
- recherches de motifs dans tout le dépôt.

*Le dépôt de reproduction*
- configuration Git locale et liste des crochets ;
- liste des 68 fichiers suivis avec leur taille ;
- contrôle des objets manquants ;
- `README.md`.

*Nos décisions, sur `main`, en entier*
- `docs/decisions/decision-N-058-v1.md`, `decision-N-064-v1.md`, `decision-N-065-v1.md`, `decision-N-067-v1.md` ;
- `decision-resserrement-juge-au-nul-v1.md`, `decision-matiere-premiere-mentors-v1.md` ;
- `decision-N-073-revendications-apres-veille-exploration-idees-v1.md` et ses compléments 1, 2 et 3.

*Branche de l'organisme, par chemin exact, jamais par liste de l'arbre*
- l'ordre de passage v3 (recherche ; l. 128-140) ;
- le plan d'héritage v5 (recherche ; l. 38-68, 376-394) ;
- le rapport du palier 0a (recherche) ;
- le préenregistrement de la ligne 3 v4 (en-tête, recherche, empreinte compagnon).

*Autres pièces*
- Papier C r3, sur sa branche : titres ; l. 487-500, 545-552, 580-592.
- `registres/go.md` : les seules lignes GO-2026-11-19-75 à -77.

*La carte du code et ses outils*
- `lecture-code-discoveryagent-v1.md` : l. 1-113, 174-181, 333-522, 708-747 ;
- `outils-lecteur-code-v1/` : liste, fin de la sortie, identifiants des contrôles.

**Seulement mesurés (taille), non ouverts**
- le corps des critères de choix des cartes v3 ;
- le préenregistrement du palier 0b ;
- le préenregistrement de la ligne 1 v5 sur `main` ;
- le fichier des cartes réexaminées.

**Non ouverts**
- le registre de couverture et le mandat du lecteur du code ;
- les cartes des rangs 10 et 14 de l'ordre de passage ;
- le dépôt de l'application de pilotage.

**Interdits respectés**
- aucun fichier dont le nom contient « consigne-privee » ou « conception-ii-b » ;
- ni `brouillons/ii-b-saboteur-budget-v1/`, ni la branche `lot/compte-4-v1`, ni la ligne R-2059 ;
- aucune note « pour Lazar seul », ni le fichier des scores par unité du bras A ;
- rien sous `/root/.claude/` ;
- rien sous `archives-reponses-modeles/`, ni nom ni empreinte ;
- aucun résultat de 7a, 7b, T0.6, de l'étape B, de l'étape B bis ni de P3-bis.

**Garde du dépôt** : aucun refus d'outil rencontré.

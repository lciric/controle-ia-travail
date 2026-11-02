# Pont « fiche de course → fiche-loi du pôle » (prise idéation) — conception v1

Lignée conv-audit, rédacteur neuf (Opus), 1er novembre 2026 ; écrit à partir du relevé `date -u` de **09:45:13 UTC**.
Décision de Lazar consignée en **R-1037** (registre de la branche conv-audit, ligne 1001) : l'objectif de la course 2 devient
« produire des idées inédites, originales et qui survivent aux tests, expériences, tests de mort et pôle » ; « prévu mais pas
construit : fais-le ». Le pont était **conçu, pas construit** (`integration-proposeurs-ia-v1.md` § 2, l. 95-98 ; dossier
factuel § 1.1 et § 9.4 C). Régime exploratoire : rien n'est lancé, aucun appel de modèle, rien lu sous `donnees/`, dossier
`bras-attaque-v1/` non ouvert, niveau méthode seulement. Pièces lues et empreintes : `LISEZMOI-pont-v1.md`.

## Verdict

1. Le pont est **conçu et codé** (`pont_v1.py`, bibliothèque standard, appels de modèle injectés) : une fiche de course entre,
   il en sort **une fiche-loi au format du pôle** (loi par instance ou contraste apparié) ou **un renvoi motivé** par un code
   d'une liste fermée. 82 essais réussis, dont 5 contre le **vrai code de l'orchestrateur v56** (garde de forme du noyau,
   juge par pari, engagement apparié) ; 25 mutations sur 25 tuées.
2. Ce que le pont ne peut pas changer : **aujourd'hui, presque aucune fiche ne sera testable sur une banque existante**. Les
   seules banques d'épisodes du pôle sont celles de T0.5 (notes de juges sur des tâches de recherche, 13 moniteurs), leur
   épreuve est **entièrement lue** (couche 1 bis : « les 288 épisodes sont tous lus »), et la banque de scores avec sabotage
   (couche 2) n'existe pas. La plupart des fiches traduisibles sortiront en **« couche 3 »** : une loi gelée maintenant, qui
   attend ses épisodes. Je l'écris d'emblée pour qu'on ne lise pas ce constat comme un échec du pont.
3. Cinq décisions pour toi (section h) ; une seule est un nœud : le **premier essai** sur 10 fiches de la course 1
   (dépense ≈ 1 à 4 dollars, fiches tirées et servies par session-depot, jamais lues par conv-audit).

---

## (a) Les deux objets

### a.1 La fiche de course

Rangée par le noyau de la course comme `{"ident", "contenu", "empreinte", "meta"}` (`pole/fiches_v53.py`) ; **seul `contenu`
est servi** (vue anonyme) ; `meta` (case, fournisseur, passe, origine) ne sort jamais. Deux formats de contenu existent.

| course | champs du contenu | source |
|---|---|---|
| **2** (texte I, « question défense ») | axe ; hypothèse ; **prédiction chiffrée et signée** (métrique de la liste fermée M, valeur, unité de lecture) ; livrables de l'axe ; données (liste D) ; coût (processeur, carte, dollars) ; antériorités (≤ 5) ; source d'avantage (liste L) ou élément manquant ; **critère de mort** ; vis-à-vis (lien angle ↔ faille) ; marque SUPPOSÉ. 3 000 à 8 000 caractères. Noms exacts des clés JSON : injectés par la configuration (`champs_fiche`), non fixés dans le code | `question-course-2-defense-fusion-v5.md` l. 44 ; dossier factuel § 3.2 |
| **1** (gabarit d'idéation) | nom ; type (question, approche) ; énoncé ; **loi_predictive** {espace_instances, prediction, signe, metrique} — en **texte libre** ; perte_traduction ; questions_servies ; avantage ; originalité ; demande à l'organisme ; coût ; piège ; « cosmétique si » ; antériorité | `pole/ideation_v2.py` l. 401-419. **SUPPOSÉ** être le format de la course 1 (version de l'orchestrateur de la course 1 non vérifiée ici) |

Les deux formats portent déjà « une prédiction chiffrée » ; aucun ne porte une **loi exécutable** : la course 1 avait même un
champ « ce que l'idée perd en devenant loi prédictive », jamais exploité.

### a.2 La fiche-loi du pôle

Le pôle juge deux sortes d'engagement (orchestrateur v56).

**(i) Loi par instance** (`pole/fiche.py`, `pole/proposeur.py`, `pole/selection_pari.py`). Le proposeur rend
`{enonce, strategie, moniteur, loi_predictive, domaines, operateurs}` ; **la garde de forme du noyau**
(`proposeur.valider_proposition`) refuse tout champ hors gabarit, une stratégie hors catalogue, un moniteur inconnu de la
banque, un type de loi hors {softmax, par sous-population, si/sinon, mélange, fixe}, un poids hors |w| ≤ 4 (biais ≤ 8), une
dimension fausse, un énoncé de plus de 400 caractères ; puis le noyau **complète seul** la métrique (« richesse W contre la
bibliothèque »), le nul, le seuil 1/α, la sévérité α, le protocole, et l'espace d'instances (banque, moniteur, nombre
d'issues, dimension, sous-populations). La loi donne, pour chaque épisode, une probabilité de chacune des K issues d'un
moniteur sachant ses traits z et sa sous-population g.

**(ii) Contraste apparié** (`pole/pari_apparie.py`, `pole/engagement_apparie.py`, `pole/monde_banque_scores.py`). Pour les
affirmations globales du type « la statistique A bat le comparateur B » (forme de la porte G1) : contrastes v(t) = a₀ + Σ a_c·r_c(t)
sur des parts d'épisodes sabotés alertés par cellule (moniteur × condition), coefficients soumis à la **règle double**
(v ∈ [−1 ; 1]), point de fonctionnement τ, **garde** δ sur l'excès de fausses alertes, seuils calculés sur les honnêtes du
calibrage, lecture de la partie d'épreuve dans un ordre secret.

### a.3 Ce que le juge figé exige (« la balance », statistique, hors des agents)

| exigence | où dans le code v56 | ce que le pont doit fournir |
|---|---|---|
| prédiction chiffrée **sur des épisodes** | `selection_pari.proba` ; `pari_apparie.contraste` | une loi par instance ou un contraste, pas un énoncé |
| **partie de développement** (traits et issues visibles, pour l'affinage) | `MondeBanque.donnees_developpement` | rien : l'affinage est le travail de l'expérimentateur du pôle, après le pont |
| **partie d'épreuve jamais vue**, issues lues après le gel, ordre secret tiré par le noyau | `MondeBanque.reservoir`, `mesures` ; `ordre_execution` | aucune lecture de l'épreuve, ni par le traducteur ni par le pont (garde G3) |
| **nul informé** : prédicteur « connu » du moniteur, ajusté sur la partie de calibrage, plus les prédicteurs aveugles (marginale, uniforme, moyennes glissantes, urne) et l'archive des survivantes | `MondeBanque.membres_informes` ; `cycle.membres_de_l_archive` | une loi qui doit **prédire plus que le connu** : le pont la construit comme « connu + effet déclaré » |
| **témoins plantés** vrais et faux à chaque génération | `exemples/construire_banque_t05_v3.py` (vrais confirmés sur une moitié du développement ; faux par permutation dans la tâche) | rien de neuf côté pôle ; le pont a **ses propres témoins** (section g) |
| seuil m/α (règle de fausses découvertes e-BH entre fiches) | `pari_apparie.ebh_pondere`, cycle | m connu de l'orchestrateur ; le pont l'utilise pour la puissance |

### a.4 Ce que le pôle sait et ne sait pas faire aujourd'hui

- **Sait** : la plomberie réelle passe (lancement « (a) bis », 27 octobre : 2 témoins vrais promus, 2 faux éliminés, 11 rejeux
  sur 11, 5,89 dollars) — mais dans un monde **tautologique** (la loi du témoin vrai est la loi du monde) ; il a des dents
  dans un monde planté (8 sur 8 témoins vrais promus, 0 sur 8 faux, démonstration couche 1 proposeur) ; sur la banque de la
  couche 1 bis il promeut des témoins plantés jusqu'à la **force 0,5** (144 épisodes d'épreuve par fiche) ; la génération 0 a éliminé 10
  affirmations sur 18 par calcul, pour 0 dollar.
- **Ne sait pas encore** : rien promu sur les **13 moniteurs réels** de T0.5 (pas de dents à 120 épisodes : 0 témoin vrai sur
  20 ; à 288 épisodes, meilleure richesse 2,28 pour un seuil de 3,0) ; l'**épreuve de T0.5 est entièrement lue** et aucune
  épreuve disjointe n'existe ; la **banque de scores avec sabotage** (couche 2) et la **couche 3** (épisodes ou moniteurs neufs
  à la demande) ne sont pas construites ; l'avantage de l'exploration (E2) n'est pas démontré.
- Conséquence pour le pont : la sortie 1 sera rare tant qu'une épreuve fraîche n'existe pas. Ordre de grandeur, calculé
  par le module (approximation dite en d) : sur un moniteur à deux issues équilibrées et un trait centré réduit, une loi de
  log-rapport de cotes 0,6 par écart type demande environ **150 épisodes d'épreuve** (seuil 1/α, α = 0,05) et environ 300 si
  17 fiches sont jugées ensemble ; un effet de 0,3 en demande environ 560.

## (b) La traduction, champ par champ

### b.1 Le principe : « connu + effet », compilé par le programme

Le traducteur n'écrit **jamais une loi**. Il écrit une **spécification courte** (forme, cible, objets, sens, effet chiffré et
**cité**), et le programme la compile :

- **loi par instance** = prédicteur connu du moniteur (public dans le pôle, ajusté sur le calibrage, jamais sur l'épreuve)
  **plus** l'effet déclaré par la fiche, sur le trait et l'issue nommés. La fiche-loi affirme donc exactement **ce que la fiche
  ajoute au connu** ; une fiche qui ne fait que redire le connu ne bat pas son nul, par construction du juge.
- **contraste apparié** = coefficients {meilleure : +1, comparateur : −1}, τ et δ cités (constantes de la porte G1 permises :
  τ = 0,01, δ = 0,05), garde sur l'excès de fausses alertes de la meilleure.

Ce choix tient le traducteur **hors de toute donnée** (ni développement, ni épreuve, ni connu) et rend la traduction
vérifiable par un programme. L'affinage sur le développement reste au pôle (l'expérimentateur, avant le second gel).

### b.2 Table de correspondance

| champ de la fiche de course | ce que le pont en fait | champ de la fiche-loi |
|---|---|---|
| prédiction chiffrée et signée (course 2) ; `loi_predictive.prediction` et `.signe` (course 1) | **sens** et **effet** (valeur citée par son chemin, ou opération fermée sur des valeurs citées : différence, rapport, logarithme du rapport, différence de logits) | `loi_predictive` (poids ou biais ajoutés au connu) ; ou `contrastes` |
| métrique de M ; `loi_predictive.metrique` | **cible** : (banque, moniteur, issue visée) ou (banque de scores, cellules, τ) | `moniteur`, `espace_instances` ; ou `contrastes`, `tau` |
| données (D) ; `loi_predictive.espace_instances` | banque existante du catalogue, ou **objet à construire désigné par le chemin du champ qui le nomme** | `espace_instances.banque` ; sinon demande de couche 3 |
| hypothèse ; énoncé | rien directement : l'énoncé de la fiche-loi est **rendu par le programme** depuis la spécification (moins de texte libre, moins de canaux) | `enonce` (≤ 400 caractères) |
| critère de mort | **non traduit** : c'est l'objet des tests de mort ; le seuil du juge est 1/α (ou m/α), pas celui de la fiche — perte consignée | — |
| perte de traduction (course 1) | lue par le traducteur comme matériau | `perte_traduction` (écrite par le traducteur, toujours exigée) |
| axe, livrables, coût, antériorités, source d'avantage, vis-à-vis, SUPPOSÉ, piège, « cosmétique si », questions servies, originalité | **non traduits** : ils relèvent des juges de la course, de l'antériorité, du devis | — |
| — | ajoutés par le pont : `source` = « pont:<empreinte de la fiche> », `base` (« connu:<moniteur> »), empreinte de la spécification | `source`, `base`, `empreinte_specification` |
| — | complétés par le noyau, inchangés : métrique, nul, seuil, sévérité, protocole, coût borné | idem |

Règle de fer : **le traducteur n'invente aucun chiffre**. Chaque nombre de la spécification doit figurer dans le champ cité
de la fiche (virgule ou point, « 45 % » vaut aussi 0,45), ou être une constante nommée du programme, ou être recalculé par le
programme à partir de nombres cités. Une fiche, **une loi au plus** (choix pris seul pour la v1 ; la multiplicité e-BH
compterait chaque loi).

### b.3 Ce qui ne se traduit pas : les trois sorties

Le **programme** décide la sortie (jamais le traducteur seul) :

1. **« Loi testable sur la banque existante »** — la cible existe au catalogue (banque, moniteur ou cellules, traits), l'épreuve
   est fraîche (ou sa réutilisation déclarée, décision D-P4), l'affirmation n'a pas déjà été lue sur cette épreuve, et la
   puissance sous la vérité de la loi suffit. Sortie : une proposition qui passe la garde du noyau, prête pour une génération
   du pôle.
2. **« Loi testable seulement avec des épisodes neufs » (couche 3)** — la loi est bien définie, mais il manque : un moniteur ou
   une cellule (une statistique nouvelle à calculer sur des épisodes existants : étage sur carte graphique, devis et GO par
   fiche) ; une banque (population nouvelle) ; une épreuve fraîche ; ou des épisodes (effectif requis calculé). Sortie : la
   **spécification gelée maintenant** (empreinte), une **demande au niveau méthode** (ce qui manque, effectif requis, parties
   fixées par une instance tierce), et la loi compilée plus tard sur le calibrage de la banque future. **Jamais un mode de
   sabotage nouveau** : épisodes honnêtes, modes connus scellés tenus par session-depot (voie c), ou statistique nouvelle.
3. **« Non testable, renvoyée avec la raison »** — code fermé, en deux familles :

| code | surnom | famille | sens |
|---|---|---|---|
| N1 | « rien à mesurer » | fiche | méthode, outil ou protocole sans issue mesurable sur des épisodes |
| N2 | « pas de chiffre » | fiche | prédiction non chiffrée ou sans signe |
| N3 | « affaire de preuve » | fiche | preuve (Lean) ou simulation hors banque : renvoyée au pôle théorie |
| N4 | « mode nouveau » | fiche | exige des épisodes d'un mode adversarial nouveau : hors du pôle (adversaire scellé, revue externe) |
| N5 | « loi vide » | fiche | effet nul, loi égale à sa base, cellules identiques |
| N6 | « mémoire d'issues » | pont | forme qui enregistre une suite d'issues (loi qui prédit ce qu'elle a vu) |
| N7 | « fuite d'épreuve » | pont | canari d'épreuve, ou champ d'identité d'épisode dans la loi ; incident |
| N8 | « deux lectures » | pont | contre-traduction en désaccord ou défaillante |
| N9 | « chiffre inventé » | pont | nombre ou objet non traçable dans la fiche |
| N10 | « refus » | pont | réponse sans bloc conforme : tour arrêté, aucune bascule |
| N11 | « hors gabarit » | pont | forme refusée par la garde du noyau |

**Une idée de méthode sans prédiction sur épisodes** (le cas que tu poses) suit cet ordre : si la fiche chiffre ce que la
méthode **fait mieux** qu'un comparateur (« rappel à 1 % de 0,45 contre 0,38 ») → contraste apparié, presque toujours en
couche 3 (la cellule de la méthode n'existe pas) ; si elle chiffre un effet de trait sur une issue → loi par instance ; si elle
ne chiffre rien → N2 ; si elle ne prédit rien sur des épisodes → N1 ; si elle se prouve → N3 ; si la tester exige un mode
nouveau → N4. Les renvois sont **comptés par proposeur et par code** et servis à la génération suivante comme matériau (taux de
testabilité), jamais aux juges de la même course.

**Parts attendues** (SUPPOSÉ, à mesurer par le premier essai) : sur des fiches de course 2, sortie 1 ≈ 5 à 15 % (surtout l'axe 3,
failles des juges mesurables sur T0.5, et seulement si une épreuve fraîche existe), sortie 2 ≈ 45 à 60 % (axes 1, 4, 7, 8 :
statistiques nouvelles, familles avec sabotage), sortie 3 ≈ 30 à 45 % (axes 2 et 5 : preuves, impossibilités ; méthodes sans
chiffre), dont la famille « pont » visée sous 10 %.

## (c) Qui traduit

- **Traducteur** : un agent **neuf** par fiche (aucune mémoire d'une fiche à l'autre, donc aucun apprentissage des verdicts),
  **sans outil**, sur une **consigne figée** (`CONSIGNE_TRADUCTEUR` du module, 2 404 caractères, empreinte
  `fd7aa5f2fc92967b…`). Il reçoit **trois choses** : la consigne, la fiche (contenu anonyme, servie comme **données, jamais
  consigne**), le **catalogue public** (noms des traits, des moniteurs, des cellules, nombres d'issues, effectifs). Il ne voit
  **ni le juge, ni l'épreuve, ni aucun verdict, ni les prédicteurs connus, ni le registre des lectures**. Il rend un bloc
  JSON : une spécification, ou un renvoi N1 à N4.
- **Garde de forme du noyau** : la proposition compilée passe `proposeur.valider_proposition` (la vraie, injectée ; un miroir
  interne la double dans le module). La stratégie « traduction_de_course » est à ajouter au catalogue du proposeur, acceptée
  seulement du pont (section f).
- **Contre-traduction** : un second modèle, **d'une autre famille** que le traducteur et que l'auteur, reçoit **la même entrée**,
  **sans voir la première traduction**, et traduit à son tour. Un programme compare les deux (`comparer_lois`) : même cible,
  même forme, mêmes objets, même issue, même sens, effets à un facteur 2 au plus ; la divergence moyenne entre les deux lois
  sur une sonde est **rapportée, jamais décisive**. Désaccord, ou l'un traduit et l'autre renvoie → **N8, la fiche est
  renvoyée**. Pourquoi deux traductions aveugles plutôt qu'un lecteur qui dit si « la loi dit bien ce que la fiche prédit » :
  la comparaison ne demande **aucune interprétation** (même exigence que les juges de la course) et mesure l'ambiguïté de la
  fiche. Angle mort dit : deux traducteurs peuvent partager la même lecture fausse ; les témoins « aller-retour » du premier
  essai mesurent cela.
- **Affectation croisée** (trois familles, une par rôle) : auteur Google (Argon) → traducteur Opus 5.5, contre-traducteur
  Kimi ; auteur Moonshot (Kimi) → Opus 5.5, Argon ; auteur Anthropic (Fable, course 1) → Kimi, Argon. Une affectation qui
  répète une famille est refusée avant tout appel.
- **Refus** : un refus arrête le tour pour cette fiche (règle R-750 : une seule reformulation plus étroite permise, jamais la
  même rhabillée) ; N10, aucune bascule vers un autre modèle sans ton mot.
- **Quarantaine** : seules les fiches « niveau méthode » sorties de l'aiguilleur entrent ; une fiche « trop concrète » reste
  scellée au bras d'attaque et n'atteint jamais le pont (règle R-575 du registre conv-audit : le concret est scellé chez
  session-depot). Le traducteur ne décrit jamais un mode ; N4 renvoie hors du pôle.

## (d) Les gardes R5 (« garde éprouvée » : chacune essayée sur un cas sain et sur un artefact)

| garde | ce qu'elle attrape | cas sain (essai) | cas artefact (essai) |
|---|---|---|---|
| **G1 rétrodiction** (« loi qui prédit ce qu'elle a vu ») | l'affirmation (cible, moniteur, traits ; ou cellules) figure au registre des lectures de cette épreuve → sortie 2, épreuve fraîche, drapeau ; forme qui enregistre une suite d'issues (déterministe, calendrier, sans remise, moyenne glissante, dérive, transformée) → N6 ; épreuve déjà lue par d'autres fiches → sortie 2 (ou réutilisation déclarée, D-P4) | lecture d'un autre trait au registre : sortie 1 | même trait lu dans l'autre sens : sortie 2 ; contraste déjà lu ; forme « deterministe » : N6 sans second appel ; loi « calendrier » refusée par la garde de forme (N6) |
| **G2 loi vide** | effet nul ; loi égale à sa base sur la sonde (divergence ≤ 10⁻⁶ nat) ; cellules identiques | loi « connu + 0,8 » : divergence > seuil | effet 0,45 − 0,45 ; même cible sans loi numérique (objet à construire) ; loi égale au connu ; cellule A = cellule B : N5 |
| **G3 lecture de l'épreuve** | clé d'épreuve ou de juge dans le catalogue servi ou l'enveloppe ; métadonnée de fiche ; consigne altérée ; canari d'épreuve dans l'entrée → **arrêt avant tout appel** ; canari dans une réponse → N7 et incident ; trait d'identité d'épisode, condition sur un champ d'épisode → N7 | canari fourni, absent partout : sortie 1, deux appels | « issues » dans le catalogue, canari dans la fiche, « ident » dans la fiche : 0 appel ; canari dans la réponse du traducteur ou du contre-traducteur ; trait « identifiant » ; condition « identifiant » |
| **traçabilité** | nombre absent de la source, source absente, valeur mal recalculée, opération hors liste, constante du programme inconnue ou falsifiée, objet à construire sans source | « 0,8 » cité ; « 0,60 − 0,20 » recalculé | 0,9 inventé ; chemin inexistant ; 0,45 − 0,38 annoncé 0,1 ; « exponentielle » ; δ = 0,2 prétendu constante de G1 : N9 |
| **contre-traduction** | désaccord de cible, forme, objet, issue, sens, effet (> ×2), genre ; loi contre renvoi ; contre-traducteur défaillant | lois identiques ; effets 0,8 et 0,45 | sens inversé, autre trait, autre issue, autre moniteur, interaction au lieu de monotone, effet ÷ 4 : N8 |
| **affectation** | traducteur de la famille de l'auteur ; contre-traducteur d'une famille déjà présente ; famille inconnue | les trois affectations recommandées | cinq affectations fautives ; aucun appel |
| **refus et format** | pas de bloc, sortie hors liste, code réservé (N5) donné par le traducteur, sens hors liste, perte de traduction vide → N10, **pas de second appel** | bloc précédé d'un autre bloc JSON | cinq réponses fautives |
| **forme du noyau** | moniteur inconnu, stratégie autre, énoncé > 400, liste vide, poids > 4, dimension fausse, champ hors gabarit, loi brute écrite par le traducteur, issue hors moniteur, sous-population hors liste → N11 ; refus de la **vraie** garde injectée → N11 | proposition compilée acceptée (miroir et vraie garde v56) | onze artefacts ; refus de la garde injectée ; vraie garde v56 sans la stratégie au catalogue : N11 |
| **puissance** | effectif d'épreuve insuffisant sous la vérité de la loi → sortie 2 avec effectif requis | 2 000 épisodes, effet 0,8 : sortie 1 | 40 épisodes : sortie 2 ; contraste à écart 0,07 sur 600 unités : sortie 2 |

Banc de mutations (hors dépôt, dans un dossier temporaire) : **25 mutations, 25 tuées** — chaque garde neutralisée fait échouer
au moins un essai ; un premier passage avait laissé **une survivante** (« effet nul accepté » : le contrôle de divergence la
couvrait en profondeur), corrigée par un essai sur une cible sans loi numérique. Audit de propreté (R4, « trop beau =
suspect ») : 25 sur 25 ne prouve pas l'absence de garde manquante ; le banc ne dit rien des gardes que je n'ai pas pensées.

**Limites des gardes** : elles voient la forme et la provenance, jamais la vérité de la fiche ; le canari n'attrape qu'une
copie littérale, pas une fuite paraphrasée ; G1 ne vaut que si le registre des lectures est complet (à tenir par le noyau,
depuis la mémoire du pôle) ; la puissance est une **approximation** (lois par instance : divergence moyenne à la seule base,
**optimiste** ; contrastes : variance bornée par 1, **pessimiste**).

## (e) Coût et ordre de passage

- **Par fiche** : 2 appels (1 seul si le traducteur faillit, refuse ou fuit) ; entrée ≈ 4 000 à 6 000 jetons (fiche 3 000 à
  8 000 caractères, consigne 2 404, catalogue) ; sortie ≤ 1 000 jetons. Prix **SUPPOSÉ**, ordre de grandeur tiré des relevés du
  lancement (a) bis (appels d'agents, plus longs) : Opus 5.5 ≈ 0,026 dollar par appel (2,09 / 79), Fable 5.1 ≈ 0,067 (3,80 / 57) ;
  soit **≈ 0,05 à 0,15 dollar par fiche**, 1 à 3 minutes, parallélisable. Côté noyau : calcul sur processeur négligeable (82
  essais en moins d'une demi-seconde).
- **Pour la course 2** : seules les fiches passées par les juges et l'antériorité entrent ; à 30 à 60 fiches : **≈ 2 à 9
  dollars**, dans le plafond de 160 dollars s'il reste de la marge (sinon devis à part).
- **En aval, hors du pont** : une fiche en sortie 1 coûte un passage du pôle (≈ 0,5 dollar par fiche au lancement (a) bis :
  expérimentateur, vérificateur, juge) ; une sortie 2 coûte un devis (carte graphique par fiche, banque nouvelle).
- **Ordre** : après les juges de la course et la vérification d'antériorité (une antériorité « non trouvée » n'est jamais
  « vierge », règle R8 « pas de faux trou »), **en parallèle des tests de mort, cloisonnés** : aucun des deux ne voit le
  résultat de l'autre avant que les deux soient scellés, et la sélection des fiches à traduire ne dépend d'aucun verdict
  (règle N-053, « pare-feu » : aucun score de juge dans une sélection). Le noyau vérifie que la tranche exploratoire des tests
  de mort est **disjointe** de l'épreuve du pôle (par identifiants). Variantes : décision D-P3.

## (f) Ce qui change dans l'orchestrateur v56, et ce qui ne change pas

**Couche v57 neuve** (R12 : aucun fichier v56 modifié) :

| pièce | rôle | interface |
|---|---|---|
| `pole/pont_v1.py` | ce module | `traduire_fiche(fiche, *, catalogue, noyau, traduire, contre_traduire, affectation, canaris, alpha, m, marge, politique_epreuve, garde_forme_noyau) -> dict` ; `comparer_lois(a, b, sonde)` |
| `pole/proposeur_v57.py` | accepte la stratégie « traduction_de_course » **seulement** d'une proposition du pont (comme `references=True` pour les références) | `valider_proposition_v57(p, monde, alpha, ident, modele, pont=True)` |
| `pole/etage_pont_v57.py` | l'étage : lit le classement et les fiches validées (même format que `etage_entre_generations_v53.preparer_generation`), sert chaque fiche (vue servie + garde A4 des étiquettes de `fiches_v54`), appelle les rôles « traducteur » et « contre_traducteur » par les adaptateurs v56 (texte → texte), scelle `noyau/pont/<ident>/{entree.txt, reponse-traducteur.txt, reponse-contre-traducteur.txt, resultat.json}` et un manifeste | sorties : fiches (`Fiche`) pour une génération du pôle ; demandes de couche 3 pour session-depot ; renvois comptés pour la génération suivante |
| `pole/catalogue_public_v57.py` | catalogue servi (depuis `MondeBanque.description_publique` et `MondeBanqueScores.description_publique`) et état du noyau, **jamais servi** : connus (`predicteurs_connus_publics`), registre des lectures (mémoire du pôle : survivantes et éliminées par épreuve), épreuves fraîches (journal), sondes (traits du développement), canaris (dérivés des identifiants d'épreuve) | dictionnaires du module |
| `configuration_v57`, `budget` | rôles et plafonds d'étape « traduction », « contre_traduction » (plafond transmis et accusé comme en v56) ; `pont.modeles`, `pont.consigne_sha256`, `pont.politique_epreuve`, `pont.marge` | validés au départ, aucun défaut |
| `gardes_e0_v57.py` | lignes R5 du pont jouées à l'étape de départ | — |

**Inchangé** : le juge figé (`selection_pari`, `pari_apparie`, `engagement_apparie`, `nul_filles_v2`), les mondes sur banque,
la mémoire, la recombinaison, le cycle, les tests de mort, l'aiguilleur, les juges de la course, le bisociateur, les règles de
budget. Une fiche du pont porte `source = "pont:<empreinte>"` : `Fiche.famille_source()` la range dans la famille « pont »
pour la calibration, sans changement de code.

## (g) Préenregistrement court du premier essai (brouillon, à sceller après contre-lecture R2, « œil neuf »)

- **Question** : le pont classe-t-il des fiches réelles de façon stable et attrape-t-il ses témoins ? (Pas : « les lois
  traduites sont-elles vraies ? » — il faudrait une épreuve fraîche.)
- **Prise des 10 fiches sans que conv-audit les lise** : session-depot (qui tient `donnees/`) part des fiches **éligibles** de
  la course 1, tentative 2 (27 sur 29), **une par idée distincte** (17 idées distinctes sur 29 fiches, 12 paires de doublons ;
  R-811 et R-820 du registre de session-depot) ; tire 10 idées par `numpy.random.SeedSequence` (R9) dont l'entropie = empreinte de ce préenregistrement
  scellé **et** une valeur de session-depot engagée par son empreinte **avant** le scellement (personne ne choisit) ; 5 de Fable
  et 5 d'Argon si possible, sinon au prorata, déclaré ; copie le **contenu seul** (vue anonyme, garde A4) dans un dossier
  scellé. conv-audit ne lit ni les fiches, ni les réponses, ni les fiches-lois : il reçoit la lecture agrégée.
- **Témoins du pont (6)**, écrits par un metteur en forme tiers qui ne voit pas la consigne (Sonnet 5.5, comme pour D-f), mêlés
  anonymes : T1 et T2 « aller-retour » (fiches écrites depuis une spécification connue sur le catalogue réel) ; T3 « vide »
  (effet nul) ; T4 « méthode sans mesure » ; T5 « théorème » ; T6 « sans chiffre ». Vérité : T1, T2 → leur signature ; T3 → N5 ;
  T4 → N1 ; T5 → N3 ; T6 → N2 ou N9.
- **Catalogue** : descriptions publiques des banques T0.5 existantes, épreuves marquées « lues » (c'est le cas) ; politique
  « fraîche seulement ». Une fiche classée « banque existante, épreuve fraîche requise » est comptée à part (« sortie 1
  différée »).
- **Prédictions** (signées, chiffrées) sur les 10 fiches : sortie 1 différée **1** (intervalle 0 à 3) ; sortie 2 **4** (2 à 6) ;
  sortie 3 **5** (3 à 7), dont famille « pont » **≤ 2** ; accord des deux traductions parmi les fiches traduites **≥ 0,6** ;
  témoins justes **≥ 5 sur 6**.
- **Critères de lecture gelés** : L1 « dents » : ≥ 5 témoins sur 6 et T1, T2 retrouvés, sinon « pas de dents » et pas d'usage
  en course 2 avant correction ; L2 « fidélité » : accord ≥ 0,6 si au moins 3 fiches traduites, sinon « ambiguïté élevée »,
  consigne à revoir ; L3 « utilité » (critère de mort du pont tel que conçu) : au moins 1 fiche sur 10 en sortie 1 différée ou 2
  avec accord, sinon « inutile en l'état » → D-P1 option (b) ou (c) ; L4 « sûreté » : 0 incident de canari ; L5 « défauts » :
  renvois de famille « pont » ≤ 3 sur 10, sinon consigne à revoir. Symétrie (R4) : un résultat parfait (10 accords, 6 témoins sur
  6) déclenche le même audit qu'un échec (réponses distinctes par fiche, entrées distinctes, empreintes).
- **Liste d'arrêt** : toute `LectureEpreuveInterdite` ; tout canari ; dépense au-delà du plafond ; 3 refus → arrêt du tour ;
  toute erreur du module → arrêt, aucun repli.
- **Coût** : 16 fiches × 2 appels = 32 appels ≈ **1 à 4 dollars** (SUPPOSÉ) ; plafond proposé **5 dollars** ; lecture par un
  lecteur neuf (R13, « arbitre neuf »).
- **Ce que l'essai ne mesure pas** : la vérité des lois ; les parts sur la course 2 (autre format, autres axes).

## (h) Décisions pour toi

**D-P1 « qui écrit la loi »** — Décision : la loi d'une fiche est-elle écrite par un traducteur séparé, par le proposeur, ou par
les deux ? Enjeu : fidélité à l'idée et indépendance contre coût et changement du texte I. Options : (a) **traducteur séparé**
(ce pont) — avantage : le proposeur ne règle pas sa loi pour passer, le texte I ne change pas ; inconvénient : perte de
traduction, 2 appels par fiche ; (b) **le proposeur écrit un champ « loi » natif** — avantage : aucune perte, aucun appel de
plus ; inconvénient : change le texte I (nœud), l'auteur peut écrire une loi facile ; (c) **les deux, comparés** — avantage :
mesure la perte de traduction ; inconvénient : texte I changé et coût. Recommandation : (a) pour le premier essai et la course 2,
(c) à partir de la course 3 ; confiance 0,6. Défaut sous 48 heures : (a).

**D-P2 « trois familles »** — Décision : quels modèles traduisent et contre-traduisent ? Enjeu : indépendance entre auteur,
traducteur et contre-traducteur. Options : (a) **règle croisée** (section c) — avantage : trois familles distinctes à chaque
fiche ; inconvénient : Kimi traduit les fiches de Fable (course 1) ; (b) Opus 5.5 traducteur partout, Argon contre-traducteur
partout — avantage : simple ; inconvénient : Opus traduit les fiches de Fable (même famille) et Argon contre-traduit les siennes ;
(c) (a) plus un **traducteur mécanique** sans modèle sur le champ « prédiction » (règle N-045-v2, « bon marché d'abord ») comme
bras de référence — avantage : mesure si le modèle est nécessaire ; inconvénient : il faut une table métrique → cellule qui
n'existe pas encore. Recommandation : (a), confiance 0,65. Défaut sous 48 heures : (a).

**D-P3 « ordre de passage »** — Décision : où le pont se place-t-il par rapport aux tests de mort ? Enjeu : coût, indépendance,
délai. Options : (a) **en parallèle, cloisonné** — avantage : aucune sélection sur un verdict, pas de délai ; inconvénient :
traduit aussi des fiches que les tests de mort élimineront ; (b) **après les tests de mort**, survivantes seulement — avantage :
moins d'appels ; inconvénient : sélection en chaîne, délai, et la tranche des tests de mort doit rester disjointe de l'épreuve ;
(c) **avant** — avantage : les tests de mort pourraient lire la fiche-loi ; inconvénient : couple les deux étages. Recommandation :
(a), confiance 0,6. Défaut sous 48 heures : (a).

**D-P4 « épreuve déjà lue »** — Décision : une fiche-loi peut-elle être jugée sur l'épreuve de T0.5, déjà lue par d'autres
fiches ? Enjeu : la seule banque existante contre la propreté de l'épreuve. Options : (a) **fraîche seulement** — avantage :
aucune exposition ; inconvénient : aucune sortie 1 tant qu'une banque sœur (règle N-049, tâches fraîches) ou les honnêtes de la
couche 2 n'existent pas ; (b) **réutilisation déclarée** — avantage : jugement possible tout de suite ; la garantie par fiche tient
si ni la fiche ni la traduction n'ont vu de verdict sur cette épreuve ; inconvénient : la couche 1 bis a lu ces épisodes,
exposition à documenter, multiplicité sur la même épreuve ; (c) **(b) en exploratoire seulement, (a) pour tout usage décisif**.
Recommandation : (c), confiance 0,6. Défaut sous 48 heures : (a), le plus prudent (codé par défaut). Conséquence : une **épreuve
fraîche** (banque sœur ou épisodes honnêtes de couche 2) devient la condition de toute sortie 1 décisive — son devis est un nœud.

**D-P5 « premier essai »** — **Nœud** (dépense, accès aux données). Décision : lancer chez session-depot l'essai de la section g
(10 fiches de la course 1 + 6 témoins, plafond 5 dollars) ? Enjeu : savoir si le pont a des dents avant la course 2. Options :
(a) **oui, sur devis et GO**, après contre-lecture et scellement du préenregistrement — avantage : mesure réelle avant la course 2,
coût faible ; inconvénient : demande du temps à session-depot (tirage, témoins, lancement) ; (b) **directement en course 2** —
avantage : aucun essai à part ; inconvénient : un pont sans dents mesurées dans une course à 160 dollars ; (c) **témoins seuls**
(sans fiches de la course 1) — avantage : aucune fiche réelle envoyée ; inconvénient : ne mesure pas les parts des sorties.
Recommandation : (a), confiance 0,7. Aucun défaut : j'attends ton mot.

## (i) Antériorités (toutes « à vérifier sur PDF » : règle R7, « page à l'appui » ; aucun chiffre repris)

| système | ce qu'il fait de l'idée à l'expérience | qui juge | ce qui diffère du pont |
|---|---|---|---|
| The AI Scientist (Lu et al., 2024, arXiv 2408.06292) | idée → code d'expérience sur un gabarit → article | relecteur modèle | l'auteur traduit sa propre idée ; jugement par modèle ; aucun gel avant épreuve |
| The AI Scientist v2 (Yamada et al., 2025, arXiv 2504.08066) | recherche arborescente d'expériences | relecteur modèle | idem ; boucle complète, pas une traduction séparée |
| Agent Laboratory (Schmidgall et al., 2025, arXiv 2501.04227) | revue, plan, expérimentation, rapport | modèle (et humain en option) | idem |
| AI co-scientist (Gottweis et al., 2025, arXiv 2502.18864) | génère, débat, classe (tournois) des hypothèses ; expériences faites par des humains | tournois de modèles | classement par jugement, non par issues ; la traduction vers l'expérience est humaine |
| Robin (Ghareeb et al., 2025, arXiv 2505.13400) | hypothèses classées ; analyse de données par un agent ; expériences humaines | modèles | idem |
| POPPER (Huang et al., 2025, arXiv 2502.09858) | hypothèse libre → expériences de falsification par agent, agrégées en **e-valeurs** séquentielles avec contrôle des fausses découvertes | statistique | **le plus proche** : même famille de garantie. Différences à vérifier : l'agent qui conçoit le test est-il séparé de l'auteur ? choisit-il ses données ? existe-t-il un nul informé, des témoins plantés, une épreuve tirée après gel, un renvoi motivé ? |
| HypoGeniC (Zhou et al., 2024, arXiv 2404.04326) | hypothèses en langue naturelle utilisées comme prédicteurs sur des exemples étiquetés, mises à jour | exactitude sur données tenues à part | proche de « loi prédictive sur des instances » ; la prédiction y est faite par un modèle qui lit l'hypothèse, pas par une loi paramétrique gelée |
| Si, Yang, Hashimoto (2024, arXiv 2409.04109) ; suite sur l'écart idéation → exécution (Si et al., 2025, identifiant à vérifier) | idées de modèles contre idées humaines ; exécution par des humains | relecteurs humains | mesure ce que l'exécution fait aux idées ; pas de traduction automatique |
| DiscoveryBench (Majumder et al., 2024, arXiv 2407.01725) | découverte d'hypothèses à partir de données | comparaison à des hypothèses de référence | évalue la découverte, pas la traduction d'une idée donnée |
| « The Agentic Scientist v3 » (dossier factuel § 9.4) | IA scientifique externe voulue par toi | — | non lu ; ni l'auteur ni l'identifiant vérifiés |

Lecture prudente (R8) : la traduction idée → expérience est **occupée** ; ce qui serait propre au pont tient en une **question**,
pas en une revendication : « une traduction séparée de l'auteur, sans donnée, vérifiée par une seconde traduction aveugle d'une
autre famille, jugée par un juge statistique contre un nul informé et des témoins, avec un renvoi motivé compté » est-elle
absente de POPPER et de ses suites ? POPPER est la zone la plus séduisante, donc à lire le plus durement.

## Choix pris seuls (à relire)

Tolérance d'accord : effets à un facteur 2 ; seuil de vide : 10⁻⁶ nat ; marge de puissance : 2 × le seuil ; une fiche, une loi ;
énoncé rendu par le programme ; pas de second appel après un défaut du traducteur ; contre-traducteur appelé même si le
traducteur renvoie (pour mesurer l'accord des renvois) ; sonde par défaut = grille (origine, axes, paires) faute de sonde du noyau ;
base uniforme signalée quand aucun connu n'existe ; traits supposés centrés réduits (SUPPOSÉ : la banque déclare une
normalisation que je n'ai pas lue en détail).

## Réserves

1. Exploratoire ; rien n'est lancé ; les modèles des essais sont factices. La compatibilité avec la v56 a été jouée sur des
   banques **synthétiques** (proposition acceptée par la vraie garde, lois valides et probabilités égales à 10⁻¹² près, contraste
   accepté par la règle double et par la construction de l'engagement), pas sur une banque réelle.
2. Le format de la course 1 est SUPPOSÉ ; les noms des champs de la course 2 sont injectés : les chemins cités par le traducteur
   dépendent de la configuration réelle.
3. Les parts attendues des sorties et les coûts sont SUPPOSÉ jusqu'au premier essai.
4. Les approximations de puissance sont dites ; elles orientent vers la sortie 2, jamais vers une promotion.
5. Antériorités non lues sur PDF : aucune n'entre dans une revendication avant vérification.

Horodatage : écrit le 2026-11-01 à partir de 09:45:13 UTC (heure lue sur `date -u` avant l'écriture).

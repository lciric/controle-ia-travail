# Rapport C7 — contre-lecture de Qu, Chen, Wang (« Propose, Don't Judge ») et dossier c8, contre O1 à O20 — v1

Écrit par un lecteur neuf (sous-agent, Fable 5.2) du lot C7 de l'état de l'art de niveau 3, le 10 novembre 2026, de 11:00 à
11:06 UTC (heures relevées par `date -u` dans le conteneur ; voir la réserve sur l'horloge au § 7). Consigne commune lue en
entier (`docs/etat-de-l-art/niveau3-v1/consignes/consigne-commune-lecteurs-v1.md`). Rapport contre-lu : `rapport-C4-organisme-ideation-O1-O20-v1.md`.
Aucun fichier existant modifié, aucune hypothèse ni revendication touchée, aucun appel de modèle payant, aucune requête sur
le réseau, rien de commité.

---

## COLLISION

**Aucune revendication encore tenue (O4 ; forme de O12 ; banc, préenregistrement et mutations de O11 ; O8) n'est trouvée
occupée en entier**, ni dans les 37 pages de Qu, Chen, Wang lues ligne à ligne, ni dans les autres pièces du dossier c8.

**Mais la collision partielle constatée par le lot C4 est confirmée, et elle s'élargit sur quatre points :**

1. **Qu et al. contient ce que C4 n'avait pas relevé au-delà de la page 11** : trois arbitres « délibérément fautifs »
   (chacun casse une hypothèse de l'arbitre valide), un attaquant scripté, un plan préenregistré avec seuils « registered
   before the runs » et amendements datés, des empreintes SHA-256 (sur les données, pas sur les propositions), une revendication
   écrite de tenue face à l'adaptation au vérificateur. Les trois gestes de O11 (tricheur scripté, préenregistrement, juge
   muté pour voir si la mesure le voit) ont donc chacun un voisin dans **la même pièce**, sur le même type d'objet (un
   arbitre par e-valeurs face à un proposeur modèle de langue). Le banc de 27, les mutations de code et la validation
   « 0 sur 1 000 » ne s'y trouvent pas.
2. **O17 (scellement par empreinte avant lecture) et O3 (prédictions scellées avant les données) reçoivent un voisin plus
   proche que tout ce que C4 a lu** : So, Liu, Long, « Masked Erosion » (arXiv 2610.38392 v1, 28 octobre 2026) gèle et
   empreinte ses prédictions et son code d'analyse avant chaque essai, revérifie les empreintes à la fin, et rapporte le
   compte des prédictions tenues et manquées. Ce sont les prédictions **des auteurs sur leur expérience**, pas celles
   d'agents proposeurs ; mais le geste « prédiction chiffrée, empreinte, puis données » est là, publié.
3. **O19 (puissance du juge ; « rien promu » n'exclut pas un effet)** : REUSE (arXiv 2609.33180 v2) énonce et prouve une
   « amélioration minimale détectable » sous laquelle la probabilité de toute promotion tend vers zéro. C'est la lecture
   « rien promu = effet sous un seuil chiffré », pour une porte de promotion. Statut à monter de « voisine » à « occupée
   dans son principe ».
4. **O12** : REUSE construit, en théorie, un proposeur adverse qui ne reçoit que les décisions et force une fausse
   promotion (annexe, p. 32). C'est le voisin théorique le plus proche de l'attaque de Goodhart contre une porte
   statistique. Aucun proposeur **modèle de langue** instruit de tromper un juge **statistique** sur un monde **tout faux**
   n'est trouvé : la forme de O12 reste « non trouvée dans les pièces lues ».

**O4 (nul formé des lois connues) : rien trouvé.** Chez Qu et al. le nul est « aucun avantage » (espérance nulle ou
négative), jamais « pas mieux que les facteurs déjà connus » ; aucune orthogonalisation contre la bibliothèque ; la seule
fusion de quasi-copies est décrite et **non exercée**. O4 reste libre **dans les pièces lues**, avec la réserve forte de C4
(§ 4.2 de C4) que je reprends : les pistes non lues (tests d'englobement en finance, comparaison séquentielle de
prévisionnistes) sont exactement là où une collision entière est la plus probable.

---

## 0. Verdict en bref

- **Contre-lecture de C4 sur Qu et al. : confirmée ligne par ligne, une nuance.** C4 écrit « trois des quatre composantes
  de O2 occupées ». Je corrige à la marge : **deux en entier** (statistique hors de l'agent ; contrôle des comparaisons
  multiples), **une dans son principe seulement** (jugement sur des données postérieures au dépôt : ordre temporel garanti
  par construction, sans empreinte ni sceau, et **non tenu dans le bras sur données réelles**, qui est un rejeu que les
  auteurs sortent eux-mêmes de la garantie), **une absente** (nul des lois connues).
- **Rien n'aggrave O4.** Rien n'occupe la forme de O12. O11 et O17 se resserrent nettement.
- **Dossier c8** : 21 pièces triées ; 12 touchent O1 à O20 ; 9 sont hors sujet pour l'organisme (elles servent le programme
  de contrôle). Trois écarts de statut avec la table de C4 : O10, O17, O19 (§ 4).
- **Citations** : 105 contrôlées par programme, 0 échec après une correction (§ 6 bis).

Clés des pièces (toutes sous `docs/sources/pdf/anteriorite-P-041-v2/c8/` ; compagnons `.sha256` vérifiés « OK » par
`sha256sum -c` à 11:00 UTC) : QU = `2609.27051.pdf` (`2a8ded0119a1…`, 37 p.) ; MASK = `2610.38392.pdf` (`6a415ce487e6…`,
25 p.) ; PACE = `2606.08106.pdf` (`779f49607688…`, 12 p.) ; REUSE = `2609.33180.pdf` (`20639707e89e…`, 41 p.) ; PROCTOR =
`2609.02246.pdf` (`9a2923ab0007…`, 20 p.) ; AUDIT = `2606.11417.pdf` (`7ae148beb5c7…`, 16 p.) ; DISCERN = `2609.17560.pdf`
(`ef318a961de7…`, 31 p.) ; SGM = `2510.10232.pdf` (`ad17c77e8f5f…`, 25 p.) ; SEA = `2607.00871.pdf` (`fb50bba836f7…`, 30 p.) ;
SEAL = `2607.24300.pdf` (`0a1434ea1c9b…`, 9 p.) ; WINNER = `2610.09239.pdf` (`3fed3c3b75d0…`, 34 p.) ; GRADER =
`2607.12790.pdf` (`9a8002db3d04…`, 17 p.) ; RSIAUDIT = `2610.27610.pdf` (`708375580e40…`, 39 p.) ; CORTEX = `2610.14216.pdf`
(`69df766cd186…`, 46 p.) ; DAPS = `2609.00077.pdf` (`17c9c3c8dc69…`, 18 p.) ; SELFREP = `2609.00652.pdf` (`91cbe6b219b8…`,
18 p.) ; EVOL = `2609.19799.pdf` (`daaa9353563e…`, 12 p.) ; SCREW = `2610.20941.pdf` (`0c5598a07ffc…`, 15 p.) ; CHASE =
`2606.05523.pdf` (`b9f28f9a2a5a…`, 15 p.) ; REDBENCH = `2606.02240.pdf` (`dedb0c0c93c7…`, 21 p.) ; MELT = `2107.06857.pdf`
(`754c17870846…`, 33 p.).

---

## 1. Contre-lecture de Qu, Chen, Wang (37 pages lues en entier)

Identité : Bo Qu, Mingguang Chen, Licheng Wang ; arXiv 2609.27051 v1, 22 septembre 2026 (imprimé en page 1) ;
prépublication, deux sociétés. Corps p. 1-22, références p. 22-24, annexes A à E p. 25-37.

### 1.1 Ce que la pièce est, en cinq lignes

Un agent propose des facteurs d'investissement tirés d'une grille finie gelée ; un « arbitre » gelé, hors d'atteinte de
l'agent, mise chaque jour sur le signe de la corrélation de rang du facteur avec les rendements **des jours qui suivent le
dépôt** ; un facteur est admis quand son capital passe une barre qui tient compte de tous les candidats jamais déposés
(e-BH en ligne) ; un détecteur le retire quand son avantage tombe sous un seuil enregistré. Trois proposeurs (script,
bandit, modèle de langue) sont croisés avec l'arbitre valide et trois arbitres fautifs, sur un monde synthétique à vérité
plantée, un environnement de sondes, et dix ans de données réelles.

### 1.2 Revendication par revendication

**O1 — le rôle qui produit ne tient jamais la clé qui évalue : occupée dans son principe ; C4 confirmé.**
- [QU p. 1] « the agent may propose, and a frozen statistical referee that the agent cannot touch must judge »
- [QU p. 2] « No prior system separates proposing from judging. »
- [QU p. 11] « These frozen components cannot be mounted, patched or intercepted by the controller. »
- La pièce revendique la priorité de cette séparation : [QU p. 4] « The division of labour, the pipeline implementing it, and the experiment measuring it are ours. »
- Atténuation : l'objet est « des hypothèses externes dont un marché décide », tirées d'une grille ; le proposeur modèle
  de langue **n'écrit pas** d'hypothèse, il répartit des soumissions entre familles (figure 1, p. 5 ; tableau 25, p. 36).

**O2, énoncé de N-064, composante par composante.**

(a) *Statistique calculée hors de tout agent* : **occupée.** Citations de O1 ci-dessus, et
[QU p. 10] « The controller may be any policy (scripted, bandit, LLM-driven or self-modifying) ».

(b) *Engagement scellé avant que les données existent* : **occupée dans son principe seulement.**
- Le principe : [QU p. 2] « Nothing the proposer saw before submission enters the score. » ;
  [QU p. 10] « each candidate is bet on post-submission data only ».
- Aucun sceau, aucune empreinte de la proposition, aucun horodatage opposable : le mot « hash » ou « SHA » n'apparaît
  qu'une fois dans les 37 pages, pour la provenance des données —
  [QU p. 30] « Every vendor-extract partition has a SHA-256 in a provenance manifest. »
  La pièce a un journal en ajout seul (figure 1, p. 5 : « Decision Log (Append-Only) ») et des manifestes de course
  ([QU p. 29] « The text names model versions only by family, while the run manifests pin them. »).
- **Atténuation forte** : sur données réelles, les données existent déjà quand le proposeur dépose ; les auteurs le disent
  et sortent ce bras de la garantie —
  [QU p. 2] « A live run satisfies this hypothesis. A historical replay by a model trained on the period may not. » ;
  [QU p. 14] « A language model trained on the campaign years falls outside condition (iv) of Proposition 1. »
  L'engagement avant les données n'est donc **réalisé** que dans le monde synthétique.

(c) *Nul formé des lois connues* : **non occupée.**
- [QU p. 6] « The null says it has no edge »
- Le nul de retrait est le seuil de viabilité, pas l'archive : [QU p. 8] « It is the null of the retirement detector. »
- Ce qui s'en approche le plus, et qui n'est pas fait : [QU p. 9] « The engine can also merge near-duplicates into a cluster (Vovk and Wang 2021). The reported experiments do not merge. » ;
  [QU p. 22] « The cluster merge is not exercised. »
- Une quasi-copie n'est pas jugée contre l'original, elle prend une place de plus :
  [QU p. 9] « A resubmitted near-copy opens a new candidate with its own slot. »
- Termes cherchés sur les 37 pages, zéro occurrence utile : « orthogonal », « incremental », « spanning », « existing
  library », « known factor », « novel », « subsum », « redundan », « adversar », « goodhart », « cheat », « timestamp ». « sibling-factor contamination » (p. 29) est un type de panne de l'environnement
  de sondes, pas un nul.

(d) *Contrôle des comparaisons multiples* : **occupée.**
- [QU p. 2] « That rule is online e-BH, the e-value form of the Benjamini–Hochberg procedure. »
- [QU p. 8] « Its objective is the false-discovery rate over everything ever admitted. »
- Sans théorème nouveau, de l'aveu des auteurs : [QU p. 4] « We apply it without extending it. » ;
  [QU p. 11] « The proposition follows from the cited results and is not a new theorem. »

**Écart avec C4 sur O2** : C4 dit « trois composantes sur quatre occupées » ; je dis « deux occupées, une dans son principe,
une absente ». Même statut d'ensemble (« occupée en partie, plus largement »). La conséquence de C4 tient : de l'énoncé
retenu, restent propres dans les pièces lues le nul des lois connues, le sceau par empreinte, l'objet (hypothèses libres).

**O3 — prédictions scellées avant les données ; tirages semés par l'empreinte : occupée dans son principe pour l'ordre
temporel ; C4 confirmé pour Qu et al.** Mêmes citations que O2 (b). Ni empreinte de l'engagement, ni tirage semé par elle.
Voir § 2.1 pour le voisin plus proche (MASK).

**O4 — battre un nul des lois connues : non occupée ; C4 confirmé.** Voir O2 (c). Rien dans les pages 12 à 37 n'aggrave.

**O9 — mémoire sans verdicts ; juges aveugles aux notes : choix contraire chez Qu et al. ; C4 confirmé, un ajout.**
- Les verdicts reviennent au proposeur : [QU p. 12] « Its state Zt includes family statistics, the referee’s diagnostics, open candidates, and paused families. »
- **Ajout** (p. 16, non lue en entier par C4) : la pièce **mesure** l'effet du contenu de la mémoire, et n'en trouve pas —
  [QU p. 16] « Six memory arms (none, working, episodic, full, shuffled, oracle) run under the frozen referee. » ;
  [QU p. 16] « After Holm correction, 0 of 10 tests are significant. »
  C'est un voisin de la **mesure** de O9 (que change ce que la mémoire sert ?), avec le choix inverse sur le fond.

**O11 — banc de tricheurs scriptés ; validation préenregistrée ; mutations : occupée dans son principe, voisin plus proche
que ne le dit C4.**
- *Tricheur scripté* (un seul) : [QU p. 16] « An attacking controller extracts false admissions only from a leaky referee. » ;
  [QU p. 16] « Hidden retries resubmit unadmitted candidates under new identifiers rather than drawing fresh ones. » ;
  [QU p. 29] « It also reports the hidden-retry attacker’s false admissions. »
  Résultat rapporté par les auteurs : 0,000 fausse admission sous l'arbitre gelé (tableau 8, p. 29).
- *Juges délibérément fautifs* — ce que C4 nomme mais ne rattache pas aux mutations : trois variantes de l'arbitre, chacune
  cassant une hypothèse, servent à vérifier que la mesure distingue un juge sain d'un juge abîmé —
  [QU p. 13] « It breaks one assumption of §4.5 in the way a common practice does »
  C'est le **principe** d'un banc de mutations du juge (trois mutants écrits à la main, pas un banc de mutations de code).
- *Garde éprouvée sur un artefact* : [QU p. 11] « A unit test reproduces the counterexample and confirms that the invariant removes it. »
- *Préenregistrement* : [QU p. 8] « It was registered as a single value » ;
  [QU p. 10] « five years of trading days, was registered before the runs » ;
  [QU p. 14] « Fixed in advance and never tuned » ;
  [QU p. 29] « Table 24 lists every dated amendment to the pre-registered design. »
  Atténuation : l'enregistrement n'est ni empreinté ni déposé chez un tiers d'après le texte ; les douze amendements du
  tableau 24 sont datés du 2 au 13 septembre 2026, neuf jours avant la mise en ligne ; l'un écarte des courses déjà
  enregistrées (A10, p. 36).
- **Non trouvés** : un banc de nombreux tricheurs (ici un seul), une validation décisive chiffrée du nul sur de grands
  nombres de tirages par ligne, des mutations automatiques du code du juge.

**O12 — attaque de Goodhart, forme A1 : occupée dans son principe ; la forme non trouvée ; C4 confirmé.**
- La menace est nommée et la tenue est **affirmée par construction**, pas mesurée par une attaque voulue :
  [QU p. 6] « Verifier-in-the-loop adaptation means that the controller learns what the referee rewards. » ;
  [QU p. 25] « What the controller learns about the referee changes which candidates it submits, not the referee’s error (Proposition 1). » ;
  [QU p. 18] « The guarantee also holds for a proposer that adapts to the verdicts. »
- Le proposeur modèle de langue reçoit les diagnostics de l'arbitre (citation p. 12 ci-dessus) : c'est le bras
  « verdicts » de O12, **sans** consigne de tromper. Les consignes ne sont pas publiées
  ([QU p. 22] « The code, run manifests, prompts, and recorded model calls are available from the corresponding author on request ») :
  je ne peux donc pas dire si la règle exacte de l'arbitre est donnée au modèle. Rien dans le texte ne le dit.
- Le monde synthétique **n'est pas tout faux** : [QU p. 14] « It has four families with true-factor proportions 0.50/0.25/0.10/0.05 »
  Les seuls flux entièrement nuls servent à régler l'arbitre **sans proposeur** (tableau 7, p. 28) :
  [QU p. 27] « Ablations on synthetic streams settled each choice before any paid run »
- L'attaquant est un script (ci-dessus), pas un modèle.
- **Donc** : ni proposeur modèle instruit de tromper, ni description exacte du juge donnée à l'attaquant, ni monde où toute
  promotion est fausse. La forme reste libre dans cette pièce.

**O17 — scellement avant lecture ; aucun repli silencieux ; mutations : voisine ; C4 confirmé, précisé.** Journal en ajout
seul (p. 5), manifestes (p. 29), SHA-256 des données (p. 30), amendements datés (p. 36), essai unitaire d'un contre-exemple
(p. 11). Aucun scellement des **résultats** avant lecture ; aucune règle « aucun repli silencieux ».

**O19 — puissance du juge ; « rien promu » ≠ absence d'effet : voisine proche ; C4 confirmé, précisé.**
- Le coût en puissance est chiffré : [QU p. 9] « A factor whose edge sits at δ needs more than five years of evidence. »
- La pièce écrit en toutes lettres qu'un non-admis peut être vrai (le « momentum ») :
  [QU p. 19] « It therefore cannot be certified within a campaign. » ;
  [QU p. 19] « A library that certifies one-day predictive power cannot certify momentum. »
- Et qu'un admis à petit effet n'est pas une erreur de la garantie :
  [QU p. 6] « An admitted factor with a small positive edge is therefore a realised false admission, not an error of the guarantee. »

**O20 — juge éprouvé sur vérité plantée : occupée comme méthode ; C4 confirmé.**
- [QU p. 14] « The synthetic world isolates the mechanism, because truth is planted. »
- [QU p. 15] « Under the frozen referee, both LLM families admit 0.000 false factors per submission. »
- [QU p. 22] « The synthetic factorial has no overlap and carries the claim about false admissions. »
- Réserve (R4) reprise de C4 : cinq graines, deux familles ; sur données réelles l'étiquette avantage l'arbitre gelé
  ([QU p. 22] « The registered label leans towards the frozen referee. »).

**O8 (hors de la liste demandée, mais tenue) — proposeurs de plusieurs fournisseurs : non occupée ; C4 confirmé.** Plusieurs
familles de modèles sont essayées **une à une**, jamais mêlées dans un même organisme :
[QU p. 2] « Every comparison uses the same random draws, and model families are never pooled. »

### 1.3 Ce qui aggraverait, cherché et non trouvé

| cherché | trouvé ? | où |
|---|---|---|
| nul formé de facteurs connus, « au-delà de la bibliothèque », orthogonalisation | **non** | nul = aucun avantage (p. 6, 8) ; fusion de quasi-copies décrite, non exercée (p. 9, 22) |
| engagement par empreinte ou horodatage de la proposition | **non** | SHA-256 des seules données (p. 30) ; jour de dépôt consigné au journal (p. 5) |
| proposeur adverse qui lit la règle de l'arbitre et tente de le tromper sur un monde sans signal | **non** | menace nommée (p. 6, 25) ; attaquant scripté (p. 16) ; monde à 50/25/10/5 % de vrais (p. 14) |
| banc de tricheurs scriptés | **en partie** | un tricheur (« hidden retries », p. 16, 29) et trois arbitres fautifs (p. 13) |

### 1.4 Lignes de C4 sur cette pièce : confirmées, corrigées, infirmées

- Bloc COLLISION de C4, points 1 à 4 : **confirmés**, avec la nuance sur O2 (b) (§ 1.2).
- § 2.1 de C4, toutes les citations de Qu et al. (p. 1, 2, 4, 5, 6, 8, 9, 11, 14, 15, 16, 18, 22, 30, 36) : **relues dans
  le texte, exactes, aux bonnes pages.**
- « Ce que la pièce ne fait pas » (fin du § 2.1 de C4) : **confirmé** après lecture des pages 12 à 37.
- Table § 6 de C4, lignes O1, O2, O3, O4, O8, O12, O20 : **confirmées**. Lignes O9, O11, O17, O19 : **confirmées et
  précisées** (ajouts ci-dessus). Aucune ligne infirmée.

### 1.5 Pièces que Qu et al. citent comme antérieures sur la même idée

Références complètes telles qu'imprimées (p. 22-24) ; présence au dépôt vérifiée par `ls` du dossier c8.

- **Les deux portes à validité permanente autour d'un agent** (seule lignée que la pièce reconnaît) :
  [QU p. 2] « The one line of prior work that puts an anytime-valid test around an agent certifies the agent’s own modifications, not the hypotheses it proposes (Sengupta 2026; Shawn 2026). »
  - [QU p. 23] « Sengupta, Biswa. 2026. Self-Evolving Agents with Anytime-Valid Certificates. » — arXiv 2607.00871 ; **au dépôt** (SEA).
  - [QU p. 23] « Shawn, Zayx. 2026. PACE: Anytime-Valid Acceptance Tests for Self-Evolving Agents. » — arXiv 2606.08106 ; **au dépôt** (PACE).
- **Synthèse des auteurs eux-mêmes** : [QU p. 23] « Chen, Mingguang, Licheng Wang, and Bo Qu. 2026. Recursive Self-Improvement in AI: From Bounded Self-Refinement to Autonomous Research Loops. » — arXiv 2607.07663 ; **absente du dépôt**.
- **Mineurs de facteurs par agents** (antérieurs que la pièce dit ne rien contrôler) : Yu et al. 2023 (KDD) ; Li et al.
  2025, arXiv 2505.15155 ; Tang et al. 2025, arXiv 2502.16789 ;
  [QU p. 24] « Yi, Jingyang, Jian Yang, Yifei Jin, Yuqi Li, and Jian Li. 2026. AlphaSchema: Exploring the Space of Trading Semantics for LLM-Based Alpha Mining. » — arXiv 2607.26642. **Absents du dépôt.** AlphaSchema est celui à lire contre O4 (recherche « structurée » de facteurs : un contrôle de nouveauté contre l'existant y est plausible ; piste, non vérifiée).
- **Outils statistiques appliqués** : Wang et Ramdas 2022 (e-BH) ;
  [QU p. 23] « Fischer, Lasse, Ziyu Xu, and Aaditya Ramdas. 2024. An Online Generalization of the (e-)Benjamini-Hochberg Procedure. » (arXiv 2407.20683) ;
  [QU p. 24] « Wang, Hongjian, Sanjit Dandapanthula, and Aaditya Ramdas. 2025. Anytime-Valid FDR Control with the Stopped e-BH Procedure. » (arXiv 2502.08539) ;
  [QU p. 23] « Heide, Rianne de. 2026. Dynamic e-Closure for Online Hypotheses with Any-Time-Valid Evidence: Closure Principles and Projective Mergers. » (arXiv 2608.09927) ;
  [QU p. 24] « Xu, Ziyu, Lasse Fischer, and Aaditya Ramdas. 2026. Improving Online FDR Procedures via Online Analogs of e-Closure and Compound e-Values. » (arXiv 2603.24792) ;
  [QU p. 24] « Sun, Liulei, and Ruodu Wang. 2026. Admissibility and Complete Classes for False Discovery Rate Control with e-Values. » (arXiv 2607.14380) ;
  [QU p. 23] « Clerico, Eugenio. 2026. Sequential Testing of Conditionally Constrained Hypotheses. » (arXiv 2606.06769 — **à lire contre O4** : un nul contraint conditionnellement est la forme statistique d'un nul composite) ;
  Waudby-Smith et Ramdas 2024 ; Vovk et Wang 2021 ; Shin, Ramdas, Rinaldo 2024 (e-détecteurs) ; Dandapanthula et Ramdas
  2025 (arXiv 2501.04130). **Tous absents du dépôt.**
- **Multiplicité en recherche de facteurs** : Harvey, Liu, Zhu 2016 ; Bailey et López de Prado 2014 ; McLean et Pontiff
  2016. Absents. Harvey et al. est la porte d'entrée de la littérature « un facteur nouveau doit ajouter aux connus »
  (piste, non vérifiée) : à lire contre O4.
- **Rejeu** : [QU p. 23] « Gonuguntla, Ashritha. 2026. The Replay Gap: Static Evaluation of Model Switching in LLM Agents Scores the Wrong World. » (arXiv 2608.08239). Absent.

---

## 2. Dossier c8 : tri, puis lecture des pièces qui touchent O1 à O20

Étendue de lecture de chaque pièce au § 7. Verdicts « par pièce et par revendication touchée ».

### 2.1 So, Liu, Long — « Masked Erosion: How Acceptance Gates Lose Redundant Safeguards in Self-Improving Agents » (arXiv 2610.38392 v1, 28 octobre 2026) — MASK

Des portes d'acceptation d'agents qui s'améliorent laissent s'éroder des garde-fous redondants ; 411 boucles, dix règles
de porte ; un simulateur gelé avant les courses prédit où chaque porte cède.

- **O3 et O17 — occupées dans leur principe (prédictions empreintées avant l'essai), comme pratique de recherche des
  auteurs :**
  [MASK p. 4] « Each confirmatory prediction and its analysis code were frozen and hashed before the test ran » ;
  [MASK p. 24] « Before each round we froze its predictions and analysis code and hashed both; all hashes were re-checked at the end » ;
  [MASK p. 4] « of 177 registered predictions, 113 held, 49 failed, 9 held in part and 6 could not be scored » ;
  [MASK p. 4] « Every verdict was computed by the frozen analysis code. »
  Ce n'est pas un scellement des **résultats** avant lecture, ni des prédictions d'agents : c'est le préenregistrement des
  auteurs, avec empreintes. Limite dite par eux : trois jeux de prédictions ont été gelés après des résultats voisins (p. 4).
- **Tirage fixé par une empreinte** (voisin de « tirages semés par l'empreinte ») :
  [MASK p. 18] « fixed per task by a hash »
  Il s'agit, d'après le contexte, d'un aléa fixé par tâche ; rien ne dit que l'empreinte est celle d'un engagement.
- **O11 et O17, « mutations » — occupées dans leur principe pour une porte d'acceptation** :
  [MASK p. 2] « Most are stress loops, a controlled intervention in the spirit of mutation testing » ;
  [MASK p. 8] « applies mutation adequacy (Jia and Harman, 2011) to safeguards » ;
  [MASK p. 8] « Stress loops plant deletions; GEPA proposes its own edits. »
  Ce qui est muté est l'objet jugé (un garde-fou retiré), pour voir si la porte le remarque. Ce n'est pas un banc de
  mutations du code du juge, et l'objet n'est pas un juge d'hypothèses.
- **O20** : pratique confirmée (suppressions plantées, prédiction gelée ; figure 4, p. 6).
- Ne touche pas O2, O4, O12.

### 2.2 Shawn — « PACE » (arXiv 2606.08106 v1, 6 juin 2026) — PACE

Porte d'engagement par e-processus, par candidat, pour des agents qui réécrivent leurs consignes.

- **O11, principe du banc** : [PACE p. 6] « a diagnostic with a known ground-truth answer (a unit test for acceptors), and a realistic stochastic deployment with no planted gain »
  Un « essai unitaire pour accepteurs » : l'idée d'éprouver une règle d'acceptation sur un cas à réponse connue. Un seul
  cas, pas un banc ; le proposeur est un modèle non adverse.
- **O12, « monde sans gain »** : dans le régime stochastique, aucun gain n'est planté et la règle naïve engage quand même —
  [PACE p. 7] « a stream of 13.3–20.7 self-modifications per run (SD ≤ 3.9), 72–100% of which a temperature-0 audit deems false »
  Voisin du « monde où toute promotion est fausse », sans attaque : le proposeur ne cherche pas à tromper la porte.
- **O2 (d)** : garantie **par décision**, pas par course ; les auteurs écartent la correction de multiplicité —
  [PACE p. 5] « This is not a run-level familywise bound » ;
  [PACE p. 8] « which is precisely why our gate is a single betting test rather than a multiplicity correction »
  Cela **confirme** que la multiplicité entre candidats, chez les portes par e-valeurs, vient de Qu et al., non de PACE.
- **O19** : [PACE p. 5] « What the guarantee does not control is power » ;
  [PACE p. 9] « a gain too small for the evaluation budget to resolve is rejected »
- Priorité revendiquée par PACE, à connaître : [PACE p. 2] « To our knowledge this is the first explicit treatment of the accept step in agent self-evolution as an anytime-valid hypothesis test »

### 2.3 Sun, Zeng, She, Wang — « REUSE » (arXiv 2609.33180 v2, 29 septembre 2026) — REUSE

Promotion certifiée sur un jeu d'évaluation réutilisé ; seul le bit de décision retourne au proposeur.

- **O9 — occupée dans son principe** : [REUSE p. 2] « the search process receives only the promotion decision rather than evaluation scores or task-level outcomes »
  Plus strict que la Ladder, moins que « aucun verdict » : la décision revient au proposeur.
- **O12 — proposeur adverse, en théorie** : [REUSE p. 32] « there exists a decision-only proposer that causes a false promotion within O(P ) rounds with probability tending to one »
  Borne inférieure prouvée pour une classe de portes à seuil ; pas d'expérience d'attaque, pas de modèle de langue adverse
  (le proposeur des expériences est un modèle non instruit de tromper, p. 6).
- **O19 — occupée dans son principe** : [REUSE p. 6] « The quantity ∆min represents the smallest population improvement that we can reliably detect. » ;
  [REUSE p. 6] « the probability of any promotion tends to zero »
- **O2 (d), O1** : contrôle simultané sur toute la course (résumé, p. 1) ; objet : modifications de l'agent, test apparié
  exact, pas d'e-valeurs. Les auteurs classent PACE, SGM, SEA, SEAL et AUDIT comme antérieurs (p. 2, 9).
- **O20** : [REUSE p. 7] « which no method ever accesses, and call a promotion false when this improvement is at most zero »
- Ne touche pas O4 (le nul est « pas mieux que le titulaire »).

### 2.4 Wahi — « LLM-as-a-Judge Is Not an Oracle » (arXiv 2609.02246 v1, 2 septembre 2026) — PROCTOR

Onze pannes observées du signal d'évaluation en production ; architecture à couche déterministe au-dessus du juge modèle.

- **O1** : [PROCTOR p. 4] « No component both proposes and applies. No component both judges and acts. »
- **O10 — occupée dans son principe (témoins négatifs plantés dans chaque suite)** :
  [PROCTOR p. 2] « Canary cases: test cases planted in an evaluation suite that no honest agent can pass »
  Témoins impassables, un par suite, en production. Différence : ce sont des pièges à triche, pas des hypothèses vraies et
  fausses plantées parmi les propositions d'une génération.
- **O17, « aucun repli silencieux » — le motif est documenté, pas la règle** :
  [PROCTOR p. 7] « silently substituted a default score of 3 for every dimension »
- **O13** : contrôles déterministes au-dessus du juge, bac à sable hermétique (p. 1). Voisine.
- **O12** : [PROCTOR p. 4] « it is also the mechanism by which a retry loop can converge on the grader rather than on the task »
  Observation, sans mesure d'attaque.
- Réserve : auteur seul, récit d'exploitation, peu de chiffres contrôlables.

### 2.5 Mittal, Gupta — « Signed Compression Progress on a Sealed Audit is Goodhart-Resistant » (arXiv 2606.11417 v1) — AUDIT

C4 l'a lue (p. 1, 9, 10). Je confirme ses trois citations et ajoute l'aveu des auteurs, qui situe la pièce :
[AUDIT p. 12] « The adaptive scalar-feedback attack reproduces a known adaptive-data-analysis vulnerability »
**O11, O12 : occupées dans leur principe** (attaquant scripté, retour scalaire, défenses de 2015 rejouées), sans modèle de
langue ni juge d'hypothèses. C4 confirmé.

### 2.6 Balachandran — « Pay Only for Disagreement » (arXiv 2609.17560 v1, 22 juillet 2026) — DISCERN

Audit séquentiel à validité permanente de mises à jour de modèles ; non ouverte par C4.

- **O11, « validation préenregistrée » d'un outil statistique — occupée dans son principe** :
  [DISCERN p. 14] « Our evaluation was pre-registered. » ;
  [DISCERN p. 26] « Four gates were frozen before the main campaign. »
  Seuils de réussite gelés avant la campagne, famille de graines réservée. Auteur seul ; pas d'empreinte mentionnée dans
  les passages lus.
- **O12, juge adverse** : [DISCERN p. 21] « routing driven by a sign-flipped, adversarial judge leaves coverage untouched »
  L'adversaire est ici le juge qui route les étiquettes, pas un proposeur ; scripté.
- Ne touche pas O4.

### 2.7 Wu et al. — « Statistical Gödel Machines » (arXiv 2510.10232 v2) — SGM ; Sengupta — SEA (arXiv 2607.00871 v1) ; Guo et al. — SEAL (arXiv 2607.24300 v1)

- SGM, **O1 et O17** : [SGM p. 1] « SGM separates adaptive proposal generation from confirmation » ;
  [SGM p. 6] « A restart must not silently reset the test index. » ;
  [SGM p. 12] « Stored records include frozen manifests and hashes »
  Empreintes liant l'état accepté à la décision ; règle écrite contre une remise à zéro silencieuse. Voisine de O17.
- SEA, **O2** : e-processus et contrôle par famille autour des modifications ; les auteurs disent ne pas prouver la tenue
  sous un proposeur endogène — [SEA p. 9] « their composition under an endogenous proposer is an empirical construct we do not prove safe »
  Atténue : la garantie « pour tout proposeur » est bien l'apport de Qu et al. et de REUSE, pas de SEA.
- SEAL, **O1 et O9** : [SEAL p. 1] « The agent cannot author or inspect the audit, receives only accept/reject »
  C4 confirmé.

### 2.8 Hu, Tang — « The Winner's Curse in LLM Self-Improvement Loops » (arXiv 2610.09239 v1, 7 octobre 2026) — WINNER

- **O11, préenregistrement avec écarts déclarés** : [WINNER p. 7] « We therefore pre-registered a confirmatory study. » ;
  [WINNER p. 19] « Deviations from the pre-registration. »
  Les auteurs y rapportent que le script d'analyse a été écrit dix minutes après le lancement (p. 7, 19).
- **O19, O20** : un résultat de PACE ne se réplique pas ici —
  [WINNER p. 3] « The degradation that PACE reports without real improvements appeared in our exploratory runs but did not replicate in our pre-registered ones. »
  Réserve utile (R4) sur PACE.
- Piste citée : Xu, Yan, Chen, Kechadi, « Phantom gains: Auditing self-improvement against a measured null », arXiv
  2608.20290 (p. 14) — **absente du dépôt** ; un « nul mesuré » est à lire contre O4 et O20.

### 2.9 Pièces qui touchent une revendication de plus loin

- **Zhang et al., « Who Grades the Grader? » (arXiv 2607.12790 v2) — GRADER.** O18, O9, O12 (voisine) : un juge extérieur
  jamais rendu à la boucle attrape une triche du barème —
  [GRADER p. 5] « The judge is an audit and never a training signal » ;
  [GRADER p. 8] « gamed within a hundred rounds by skills optimizing against it »
  Triche émergente, non voulue ; juge modèle, pas statistique.
- **He et al., « Beneath the Diff » (arXiv 2609.00077 v1) — DAPS.** O9, O10, O20 :
  [DAPS p. 1] « a blind metric no loop component ever accesses » ;
  [DAPS p. 16] « we ran two control sets whose ground truth is known by construction »
- **Chen, Zhu, Zheng, « Auditing the Product, Not the Recursion » (arXiv 2610.27610 v1) — RSIAUDIT.** Revue codée de 114
  études. O19, O20 : [RSIAUDIT p. 6] « A null control runs the same loop with shuffled feedback or proposals that cannot help, directly estimating the spurious gain (A5). »
  « Des propositions qui ne peuvent pas aider » : le monde tout faux comme **contrôle**, pas comme terrain d'attaque.
  Piste citée (p. 14, 26), **absente du dépôt**, à lire contre O12 : Dai et al., « Recursive reward improvement via
  adversarial Meta-Prompt evolution », arXiv 2610.21040 —
  [RSIAUDIT p. 14] « RRI uses adversarial search to identify and repair hackable rubrics »
- **Giampieri, « Cortex » (arXiv 2610.14216 v1) — CORTEX.** O10, O20 : candidats inutiles et nuisibles plantés exprès ;
  résultat mitigé rapporté par l'auteur — [CORTEX p. 3] « but on only 2 of the 4 planted ones, items we added to a harness with a known right answer »
- **Kozhevnikov, Tracy, « Screwtape » (arXiv 2610.20941 v1) — SCREW.** O12, principe, autre objet (surveillant modèle d'un
  agent de code) : [SCREW p. 1] « The attacker revises the edit until the monitor no longer flags it. »
  Un attaquant **modèle de langue** qui itère contre les verdicts d'un juge **modèle**. Lue en page 1 seulement ; elle
  relève d'abord du programme de contrôle (bras d'attaque), pas de l'organisme.

### 2.10 Hors sujet pour O1 à O20 (tri seul, page 1)

| pièce | deux lignes | touche |
|---|---|---|
| Pan, Zhou, Hu, « Self-Reports Are Not Verification », arXiv 2609.00652 v1 — SELFREP | Confiance et justifications déclarées par un modèle opérateur de recherche évolutive, confrontées à un résultat exact. [SELFREP p. 1] « Self-reports therefore require external evidence. » | O13, de loin |
| Oved et al., « Evolution or Illusion? », arXiv 2609.19799 v1 — EVOL | Budget graines contre itérations en recherche évolutive par modèle ; le classement des méthodes change avec le budget. | rien |
| Markasserithodi et al., « CHASE », arXiv 2606.05523 v1 — CHASE | Attaquant et défenseur entraînés ensemble par renforcement pour la sûreté des modèles. | rien (programme) |
| Dingeto, Leeney, « AgentRedBench », arXiv 2606.02240 v1 — REDBENCH | Banc d'attaques par injection sur des intégrations d'agents. | rien (programme) |
| Leibo et al., « Melting Pot », arXiv 2107.06857 v1 — MELT | Suite d'évaluation de l'apprentissage par renforcement à plusieurs agents. [MELT p. 1] « fills this gap » | rien |

Les pièces de contrôle du dossier (2607.06596, 2605.16626, 2605.09684, 2512.07810, 2506.15740) n'étaient pas dans la liste
de la consigne : titre et résumé lus, aucune ne porte sur un juge statistique d'hypothèses ; non jugées ici.

---

## 3. Synthèse : ce qui aggrave, ce qui atténue

**Aggrave (par rapport au constat de C4).**
1. Qu et al. porte, dans une seule pièce, les voisins de **cinq** gestes de l'organisme : juge hors de l'agent, multiplicité
   par e-valeurs, vérité plantée, attaquant scripté, juges délibérément fautifs — plus un plan préenregistré.
2. Le sceau par empreinte de prédictions avant l'essai est **publié** (MASK), ce que C4 laissait comme « reste propre » de
   O2 et O3. Il n'est publié que comme pratique d'auteurs, pas comme mécanisme d'une boucle d'agents.
3. La lecture « rien promu = sous l'effet minimal détectable » est **publiée** (REUSE, proposition 1).
4. Un proposeur adverse à retour d'un bit est **construit en théorie** (REUSE, annexe).

**Atténue.**
1. Chez Qu et al. le modèle de langue ne formule aucune hypothèse : il répartit des tirages dans une grille finie.
   L'organisme juge des hypothèses libres.
2. Le bras « données réelles » de Qu et al. est un rejeu hors garantie ; l'engagement avant les données n'y tient pas.
3. Aucune pièce lue ne **mesure** un juge statistique sous l'attaque voulue d'un proposeur modèle. Qu et al. l'affirme par
   théorème ; REUSE le borne en théorie ; AUDIT et Qu et al. rejouent des scripts.
4. Aucune pièce lue ne forme un nul à partir de l'existant.
5. Qu et al. : prépublication de sept semaines, code et consignes « sur demande », cinq graines.

---

## 4. Table finale O1 à O20

« C4 » : colonne « verdict de ce rapport » de la table § 6 du rapport C4. Écart marqué **ÉCART** quand le statut change,
« précisé » quand seul l'appui change.

| | revendication (abrégée) | C4 | après C7 | écart avec C4 |
|---|---|---|---|---|
| O1 | le rôle qui produit ne tient jamais la clé qui évalue | occupée dans son principe | **occupée dans son principe** (QU p. 1, 2, 4, 11 ; PROCTOR p. 4 ; SGM p. 1 ; SEAL p. 1) | non (précisé) |
| O2 | statistique par l'orchestrateur, engagement scellé avant les données, nul des lois connues, multiplicité | occupée en partie, plus largement ; « trois composantes sur quatre » | **occupée en partie** : (a) et (d) occupées (QU p. 1, 2, 8, 10, 11) ; (b) dans son principe seulement, sans sceau, non tenue en rejeu (QU p. 2, 10, 14, 30) ; (c) absente (QU p. 6, 8, 9, 22) | non sur le statut ; **nuance** : deux composantes + une en principe, pas trois |
| O3 | prédictions scellées avant les données ; tirages semés par l'empreinte | occupée dans son principe (ordre temporel) ; sceau non trouvé | **occupée dans son principe, plus largement** : ordre temporel (QU p. 2, 10) ; prédictions empreintées avant l'essai, comme pratique d'auteurs (MASK p. 4, 24) ; tirage semé par l'empreinte de l'engagement non trouvé | précisé (le sceau par empreinte n'est plus « non trouvé ») |
| O4 | battre un nul des lois connues | libre dans les pièces lues | **libre dans les pièces lues** (37 pages de QU et 20 autres pièces de c8 : aucun nul formé de l'existant) | non ; réserve de C4 maintenue |
| O5 | moisson non opposable ; trou = question | inchangée | non réexaminée | non |
| O6 | douane de forme, coffre scellé | inchangée | non réexaminée | non |
| O7 | juges croisés de plusieurs fournisseurs | voisine | voisine | non |
| O8 | proposeurs de plusieurs fournisseurs | libre dans les pièces lues | **libre dans les pièces lues** ; familles essayées une à une, jamais mêlées (QU p. 2) | non |
| O9 | mémoire sans verdicts ; juges aveugles aux notes | occupée dans son principe, confiance moyenne | **occupée dans son principe** : retour réduit à la décision (REUSE p. 2 ; SEAL p. 1) ; audit jamais rendu à la boucle (GRADER p. 5 ; DAPS p. 1) ; effet du contenu de la mémoire mesuré, nul (QU p. 16) ; choix contraire sur les verdicts chez QU (p. 12) | non (confiance montée) |
| O10 | témoins plantés mêlés à chaque génération | voisine | **occupée dans son principe** pour des témoins négatifs plantés dans chaque suite (PROCTOR p. 2) ; aussi PACE p. 6, CORTEX p. 3, DAPS p. 16 ; témoins vrais et faux mêlés aux propositions d'une génération non trouvés | **ÉCART**, confiance moyenne |
| O11 | banc de tricheurs scriptés ; validation préenregistrée ; mutations | occupée dans son principe ; banc, préenregistrement, mutations non trouvés | **occupée dans son principe, sur chacun des trois gestes** : tricheur scripté contre arbitre par e-valeurs (QU p. 16, 29 ; AUDIT p. 12) ; « essai unitaire pour accepteurs » (PACE p. 6) ; juges délibérément fautifs (QU p. 13) et mutation d'une porte (MASK p. 2, 8) ; validation préenregistrée d'un outil statistique (DISCERN p. 14, 26 ; QU p. 8, 10, 14, 29 ; MASK p. 4). **Non trouvés** : banc de 27, validation « 0 sur 1 000 par ligne », mutations du code du juge. Pas occupée en entier | précisé (resserrée ; le préenregistrement et le principe des mutations ne sont plus « non trouvés ») |
| O12 | attaque de Goodhart : proposeur modèle qui lit le juge et ses verdicts, mondes tout faux | occupée dans son principe ; forme non trouvée | **occupée dans son principe ; forme non trouvée** : menace nommée, tenue affirmée (QU p. 6, 18, 25) ; proposeur adverse théorique à un bit (REUSE p. 32) ; monde sans gain, sans attaque (PACE p. 6, 7 ; RSIAUDIT p. 6) ; attaquant modèle contre juge modèle, autre objet (SCREW p. 1) | non (resserrée) |
| O13 | tests de mort en bac à sable, verdict sur le fichier brut | voisine | voisine (PROCTOR p. 1) | non |
| O14 | sélection par le verdict des tests de mort | voisine | voisine | non |
| O15 | bisociateur à trois bras | inchangée | non réexaminée | non |
| O16 | pont fiche → loi prédictive | voisine | non réexaminée | non |
| O17 | scellement avant lecture ; aucun repli silencieux ; mutations | voisine | **occupée dans son principe** pour le gel par empreinte avant l'essai (MASK p. 4, 24) et la liaison par empreinte de l'état à la décision (SGM p. 12) ; repli silencieux documenté comme panne (PROCTOR p. 7) et interdit sur un point (SGM p. 6) ; règle générale « aucun repli silencieux » et scellement des résultats avant lecture non trouvés | **ÉCART**, confiance moyenne |
| O18 | discrimination des juges modèles mesurée | voisine | voisine (GRADER p. 8) | non |
| O19 | puissance du juge ; « rien promu » ≠ absence d'effet | voisine | **occupée dans son principe** : effet minimal détectable et probabilité de promotion nulle en dessous (REUSE p. 6) ; puissance non garantie (PACE p. 5, 9) ; non-admis vrai (QU p. 9, 19) | **ÉCART** |
| O20 | juge éprouvé sur vérité plantée | occupée comme méthode | **occupée comme méthode** (QU p. 14, 15, 22 ; REUSE p. 7 ; MASK p. 4) | non |

**Revendications encore tenues, après ce passage :** O4 (libre dans les pièces lues) ; forme de O12 (non trouvée) ; de O11,
la combinaison et l'ampleur (banc nombreux, validation chiffrée du nul, mutations du code du juge) ; O8 ; de O2 et O3, le
tirage semé par l'empreinte de l'engagement et l'objet (hypothèses libres). **Je ne modifie rien : tout changement d'énoncé
est un nœud de Lazar.**

**Pour un texte interne, les pièces à citer en plus de celles de N-064 et de C4** : Qu, Chen, Wang (voisin principal) ;
REUSE (O9, O12, O19) ; Masked Erosion (O3, O11, O17) ; PACE (O11) ; PROCTOR (O10, O17).

---

## 5. Pièces à récupérer sur le réseau, par ordre

1. **Clerico 2026, arXiv 2606.06769**, « Sequential Testing of Conditionally Constrained Hypotheses » — O4 (nul composite).
2. **Yi et al. 2026, arXiv 2607.26642**, « AlphaSchema » ; **Harvey, Liu, Zhu 2016** — O4 (nouveauté d'un facteur contre
   l'existant). S'y ajoutent les pistes 6 et 7 du § 5 de C4 (SSRN 6569258 ; arXiv 2609.00731), toujours prioritaires.
3. **Xu, Yan, Chen, Kechadi 2026, arXiv 2608.20290**, « Phantom gains: Auditing self-improvement against a measured
   null » — O4, O20.
4. **Dai et al. 2026, arXiv 2610.21040**, « Recursive reward improvement via adversarial Meta-Prompt evolution » — O12
   (recherche adverse contre un barème).
5. **Chen, Wang, Qu 2026, arXiv 2607.07663** — la synthèse des auteurs de Qu et al. : dit-elle déjà la séparation ?
6. **Fischer, Xu, Ramdas 2024, arXiv 2407.20683 ; Wang, Dandapanthula, Ramdas 2025, arXiv 2502.08539 ; de Heide 2026,
   arXiv 2608.09927 ; Xu, Fischer, Ramdas 2026, arXiv 2603.24792** — outils de O2 (d), à citer.
7. **Page arXiv de 2609.27051** (versions) et le code « sur demande » : les consignes donnent-elles la règle de l'arbitre au
   modèle ? Seul moyen de fermer la question de la forme de O12 pour cette pièce.
8. « Pre-Registered Genesis Accounting for Recur… » (titre tronqué au tableau de RSIAUDIT, p. 35 ; identifiant non
   relevé) — O11, O17 ; piste, non vérifiée.

---

## 6. Contrôle des citations

Script `controle_citations.py`, gardé dans
`/tmp/claude-0/-home-user-controle-ia-travail/a26149b8-c735-5fa7-914e-afb00d165aed/scratchpad/lotC7/` (non versé). Il
relève chaque motif « [CLÉ p. N] « citation » » de ce rapport et cherche la citation dans le texte de la page N du PDF de
la clé (`pdftotext`, ordre de lecture puis `-layout` ; Unicode normalisé, apostrophes et guillemets ramenés à leur forme
simple, césures de fin de ligne recollées, blancs réduits). Si la forme stricte échoue, une seconde passe ignore blancs et
traits d'union et classe la citation « césure ». Essai préalable (R5) : cas juste retrouvé ; cas altéré (un mot changé) en
échec ; bonne citation à la mauvaise page en échec.

### 6 bis. Résultat

Première passe (11:07 UTC) : 105 citations contrôlées, 104 retrouvées à la page citée en forme stricte, 1 échec — la
citation de PACE p. 7 sur le régime stochastique, où j'avais sauté trois mots (« a stream of ») ; corrigée. Seconde passe,
après correction et avant scellement : **105 citations contrôlées, 105 retrouvées en forme stricte à la page citée, 0 en
forme « césure », 0 échec.** Les mentions de page sans guillemets (« p. 29 », « tableau 24, p. 36 ») ne sont pas contrôlées
par programme ; elles sont lues dans le texte extrait.

---

## 7. Réserves

- **Étendue de lecture.** QU : les 37 pages, ligne à ligne, dans l'extraction `pdftotext -layout` ; figures non relues en
  image (les légendes et les étiquettes le sont). PACE : p. 1 à 3 et 5 à 9 en entier ; p. 4, 10 à 12 par recherche de
  termes. REUSE : p. 1 à 3, 6 à 9 et 32 en entier ; le reste (preuves, p. 10 à 41) par recherche de termes. MASK : p. 1,
  2, 4 à 8, 24 par passages (lignes portant gel, empreinte, mutation, prédiction, plantation) et recherche de termes sur
  les 25 pages ; **pas « en entier »**. PROCTOR, AUDIT, DISCERN, SGM, SEA, SEAL, WINNER, GRADER, RSIAUDIT, CORTEX, DAPS :
  page 1 et recherche de termes sur toutes les pages, avec lecture du contexte de chaque occurrence (environ 800
  caractères). SELFREP, EVOL, CHASE, REDBENCH, MELT, SCREW : page 1. Une recherche de termes ne voit pas une idée dite
  avec d'autres mots : « non trouvé » vaut pour les termes cherchés (listés aux § 1.2 et dans le script).
- **Symétrie (R4).** « Aucune collision entière » est le résultat que le programme préfère : je l'ai cherchée d'abord là où
  elle était la plus probable (O4 dans une pièce de finance), et ne l'ai pas trouvée ; mais la littérature de finance
  empirique sur les facteurs redondants n'est pas au dépôt. Le verdict sur O4 est le plus fragile du rapport.
  À l'inverse, mes trois écarts (O10, O17, O19) reposent sur des pièces lues par passages ; ils sont à confiance moyenne.
- **Qu et al.** : rapporté comme dit, jamais comme établi (réserves de C4, § 7, reprises). Le « 0,000 » du tableau 8 est
  identique à trois décimales pour les deux familles et les trois proposeurs : trop propre, signalé.
- **Dates.** Les dates et identifiants sont ceux imprimés en page 1 ; aucun n'est recoupé avec arXiv (réseau fermé).
  Plusieurs pièces sont de 2026 et postérieures à ma connaissance propre : je ne peux rien en dire hors du texte.
- **Horloge.** Les heures données par `date -u` dans ce conteneur avancent très lentement par rapport au travail fait
  (lecture de plusieurs centaines de pages entre 11:00 et 11:06 affichés). Je les rapporte telles que relevées ; elles ne
  mesurent pas la durée réelle.
- **Priorité de l'organisme** : non vérifiée (hors de mon lot).
- Aucun refus de permission rencontré. Aucune requête sur le réseau.

Version 1 ; jamais réécrite (R12).

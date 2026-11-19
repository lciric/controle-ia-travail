# Papier C — traitement des quatre contre-lectures du brouillon 4 et des notes de voisinage — v1

Session 14, 2026-10-20 vers 21:10 UTC. La session n'a écrit ni le brouillon 4, ni sa configuration, ni aucun rapport
traité. Elle décide ici, constat par constat ou par groupe, ce que le brouillon 5 doit faire. Le rédacteur du brouillon 5
(sous-agent neuf) applique les corrections **en mots exacts des rapports** quand ils en donnent, sinon au plus près de
leur texte, et dit en une ligne chaque écart. Préfixe `…/` = `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/papier-C`.

## Rapports traités (orchestration `wf_fa19dead-543`)
- Note Panin et lentille Panin : `…/contre-lectures/contre-lecture-note-panin-v1.md` (`c06488a5…`) ;
  `…/contre-lectures/contre-lecture-R2-brouillon4-panin-v1.md` (`6b350e99…`) ; note : « non occupé confirmé » ; brouillon
  4 : « scellable après corrections ».
- Note voisins et lentille voisins : `…/contre-lectures/contre-lecture-note-voisins-v1.md` et
  `…/contre-lectures/contre-lecture-R2-brouillon4-voisins-v1.md` ; note : « non occupé confirmé » ; brouillon 4 :
  « scellable après corrections ».
- Lentille texte : `…/contre-lectures/contre-lecture-R2-brouillon4-texte-v1.md` : « scellable après corrections », 9 majeurs.
- Lentille méthode : `…/contre-lectures/contre-lecture-R2-brouillon4-methode-v1.md` : **« non scellable »**, 1 critique,
  8 majeurs ; simulations `…/contre-lectures/simulations-methode/` (manifeste `eea33215…`).
Empreintes complètes : à recopier par le rédacteur depuis les compagnons `.sha256` (R6).

## Décisions

| constats | décision de la session |
|---|---|
| **CR-methode-01 (critique)** : la lecture déterministe garde une régression vers la moyenne (l'insertion déplace chaque contenu d'une quantité propre) | **accepté** : loi nette contre la cellule témoin, à régresseur calibré, en mots exacts du rapport ; C-P1 et C-P2 se lisent sur la loi nette ; la phrase « la régression vers la moyenne n'y joue pas » est retirée partout ; placebo par permutation rapporté (CR-methode-13), avec sa raison réécrite |
| CR-texte-01, CR-panin-09, CR-voisins-11, CR-methode-17 : module sous `src/` | **accepté** : module, tests et `ecrire_config_v1.py` sous `docs/procedures/papier-C-v1/`, hors de l'arbre gelé (P4 et P3b exigent l'arbre de `7a54d43`) ; une ligne « Module du papier C : `chemin` : `empreinte` » par fichier ; tests par `PYTHONPATH=src:docs/procedures/papier-C-v1` ; arbre gelé modifié = arrêt ; `papier_c.derivation` renommé en conséquence |
| CR-texte-02, CR-panin-10, CR-voisins-12, CR-methode-09 (A7, tâches) | **décision de Lazar** (GO-2026-10-20-09, R-294) : partage écrit des 64 tâches d'évaluation (16 tirées parmi les 60 du pilote de T0.5 pour le calibrage du pilote du papier C ; 44 + 4 = 48 pour l'étape 2), tirage par `numpy.random.SeedSequence` dérivée de l'entropie du préenregistrement (clé `partage-taches-papier-C`), jamais une graine publique ; nouvelle extraction (environ 64 tâches, procédure scellée de T0.5, corpus neuf disjoint) avant l'étape 2, ajoutée au bassin de l'étape 2 si validée avant son ouverture ; liste des effectifs {60, 90, 120} bornée par les tâches disponibles ; rééchantillonnage par grappe de tâches ; garde 16 réécrite en conséquence |
| CR-panin-01, CR-voisins-02, CR-texte-17 : le banc filtre les juges sur leur gain (leçon de Panin, p. 11) | **accepté** : un ordre contraire chez un ou deux juges = réserve, jamais un arrêt ni un retrait ni un remplacement ; chez les trois juges : audit A6, arrêt seulement si un défaut de chaîne est trouvé ; un remplaçant n'est jamais choisi sur une mesure de déférence |
| CR-panin-08, CR-voisins-13, CR-texte-10, CR-methode-16 (A1) | **accepté** : sorties du banc scellées à part ; la dérivation ne lit que les sorties 1.3 à 1.5 et refuse tout fichier du banc (garde R5, cas sain et artefact) ; le banc ne joue que comme porte ; réserve « contrôle positif faible » sans effet sur les seuils |
| CR-panin-02 : intensités choisies par γ (gain vers v* imposé) | **accepté** : choix et ordre par ḡ_sép (loi séparée, sans destination) ; γ rapporté seulement ; ĉ_m par rang avec la réserve « destination hétérogène » |
| CR-methode-07, CR-texte-21, CR-voisins-07 : règle du vivier | **accepté** : k_max sur l'étendue diminuée de 3,53 × ET(n_cal) ; demi-largeur de λ par validation croisée ; critère gelé « intensités graduées » (g_k − g_1 > 0) ; réserves déclarées (formulations extrêmes retenues ; formulations du corpus B dérivées du corpus A ; la leçon de Panin vaut pour juges et familles, pas pour les formulations) |
| CR-methode-04 : notation de la valeur p inversée | **accepté** (formules exactes du rapport) et test du module |
| CR-panin-03, CR-methode-10, CR-methode-11, CR-methode-15, CR-texte-08, CR-texte-14 : C-P1, identifiabilité, attracteur, tirages dégénérés, comparaison entre familles | **accepté** : λ rapporté pour tous les couples, « non identifiable » marqué ; réserve « gain faible » avec la valeur p ajustée ; a_j avec son étendue et deux réserves ; tirages dégénérés définis, ĉ en forme fermée ; **C-P1b** (écarts appariés de λ entre familles identifiables, Holm, sans signe prédit : la pièce revendiquée « comparée entre familles ») ; corpus nommé ; « identifiable » défini en une phrase |
| **CR-methode-02, CR-methode-03, CR-texte-04 : stabilité de rang (prédiction 3 de N-005)** | **proposition à Lazar (P-019)** : C-P3a classée sur le Ḡ de la loi nette, valeur p exacte par permutation, lecture « établie / non établie » sans verdict de réfutation (à trois juges, la réfutation « W ≤ 0,20 » sort dans 63 % des cas sous le nul) ; C-P3b par le τ de Kendall entre les quinze Ḡ nets des corpus A et B (100 000 permutations), même lecture ; C-P3c à quatre évaluateurs (W exact, p = 0,042 atteignable), même lecture. Le brouillon 5 écrit cette version avec un marqueur de décision et la version de repli si Lazar refuse |
| CR-texte-03, CR-methode-05, CR-methode-08, CR-texte-22, CR-texte-07 : HC2, HC2b, porte GC, sondes | **accepté** : combinaison « robuste à la marge, déplacement positif de faible ampleur » écrite ; lecture principale de HC2, de C-P6 (sondes) et de la porte GC sur les seuls champs de l'action ; HC2b sur l'excédent du paragraphe à longueur fixe ; demi-largeur prévue de l'équivalence calculée à l'addendum de dérivation sur les données scellées de G0 ou de P3, ligne « non testable à cette puissance » écrite d'avance ; audit A7 si la sensibilité « champs seuls » change la ligne ; sondes : les deux plus grands écarts au plancher apparié du critère 3 de G0, égalités par l'ordre du verdict, choix consigné avant toute génération |
| CR-methode-06, CR-texte-19 : Clopper-Pearson sur essais groupés | **accepté** : effectif efficace (Korn et Graubard, effet de plan sur les totaux par tâche) ; borne par rééchantillonnage des tâches, symétrique pour confirmer et réfuter |
| CR-texte-09 : famille 4 contaminée par un constat d'approbation | **accepté** : deux phrases normatives retirées des formulations 5 à 16 ; réserve déclarée ; écart Ḡ4 − Ḡ3 rapporté |
| CR-texte-18 : exception de la clause « contenu = données » | **accepté** |
| CR-texte-05 : bras « usurpation écrite par l'agent » écrit comme acquis | **proposition à Lazar (P-020)**, écrite comme telle avec un marqueur de décision et la lecture en cas de refus (TC.3 (b) sur les sondes de l'auteur non mesurée) |
| CR-texte-06 : ligne d'accord du jour par lancement, arrêt par identifiant | **accepté** (formes de P4 : « **Accord de Lazar pour le lancement du pilote du papier C** », GO-2026-10-20-07 ; arrêt par identifiant, R10 ; borne par lancement < 10 USD) |
| CR-methode-12, CR-methode-14, CR-methode-18, CR-methode-19 | **acceptés** (loi avec terme d'intention rapportée ; banc : neutre de chaque fichier ; versions imprimées et P(W ≤ 0,20) = 0,6327 ajoutée ; intervalles BCa et test de niveau, sinon effectif minimal de 90 contenus) |
| CR-texte-11 à 16, CR-texte-20, CR-texte-23 | **acceptés** (notes finales citées avec leurs empreintes ; différences admises entre configuration scellée et brouillon ; libellé des six décimales ; témoins ; mesures de conception, note du vivier et script de configuration versés avant le scellement ; en-tête : la copie publique relève d'une décision de Lazar ; formes) |
| CR-panin-04 à 07, CR-panin-11 ; CR-voisins-01, 03 à 10 | **acceptés** (descriptions des voisins complétées aux pages citées ; contre-indices déclarés ; option « note système » pour HC3 composante 2 ; 2608.25869 : calcul de notre lecteur, pas des auteurs ; 2606.14037 p. 4 et tableau 4 p. 12) ; **verrou ajouté** : lire les résumés des voisins tirés de la bibliographie de Panin et absents de la veille, en commençant par Joswin et al. 2607.00415 et Hu et Qu 2607.05545 (R8), avant le scellement |
| Notes Panin et voisins (CN-…) | **acceptés** : versions finales tirées des annexes des deux rapports, corrigées, versées sous `docs/notes/lecture-voisin-panin-v1.md` et `docs/notes/lecture-voisins-HC1-bajaj-silent-judge-v1.md`, scellées ; ajout des trois voisins aux « cités comme publiés » de HC1 : routine (aucune prédiction prise, aucune zone occupée), ligne d'information à Lazar (A2) |

## Suite
1. Brouillon 5 par un sous-agent neuf, à partir du brouillon 4, de sa configuration, de ce traitement et des quatre rapports ;
   chaque constat appliqué ou écarté en une ligne, dans une table de traitement versée avec lui.
2. Contre-lecture ciblée par des sous-agents neufs : méthode (points corrigés et simulations rejouées sur la loi nette) et
   texte (application de ce traitement).
3. Module sous `docs/procedures/papier-C-v1/`, puis sa contre-lecture ; scellement (critère 7 de G0) ; pilote sous la
   délégation.

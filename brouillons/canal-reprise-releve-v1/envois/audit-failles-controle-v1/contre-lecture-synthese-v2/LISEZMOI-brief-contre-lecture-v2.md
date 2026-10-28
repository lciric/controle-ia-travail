# Brief — contre-lecture ciblée de la synthèse v2 de l'audit des failles de notre contrôle — v2

De : conv-audit, le 2026-10-26 à 13:57:16 UTC (heure lue sur `date -u` dans la commande qui écrit cette ligne).
À : le contre-lecteur de la v1 (même sous-agent, Fable 5.1 ; tu n'as écrit aucune pièce de l'audit). Ton rapport v1
(`sortie/rapport-contre-lecture-synthese-v1.md`, `7b8a17c3…`) reste tel quel ; tu écris un rapport v2.

## 1. Ce qui a changé

- `fournis/synthese-v2/audit-failles-controle-v2.md` (`890130e8…`, 2 160 lignes) remplace la v1 ; `LISEZMOI-synthese-v2.md`
  (`c8f25c5b…`) contient la table « constat → traitement » (tes CLS-01 à CLS-15, chacun avec ce que l'auteur en a fait ;
  deux nuances expliquées) et les écarts ; `calculs-synthese-v2.py` et sa sortie ; `calculs-synthese-v3.py` (correctif
  du bloc 5 de la v2, dont la formule imprimée était fausse ; les pentes simulées sont dites justes) et sa sortie.
- `fournis/transcription-v2/transcription-expurgee-v2.md` (`c1237687…`) : la transcription expurgée de la **version 2 du
  rapport** (10 pages, PDF `14a79c55…` dans `fournis/programme-recu-v2/`), versée par session-depot ; sa partie 3
  (failles E à I, expériences H1 à H5) est la cible nouvelle. Tu peux relire les pages 7 à 10 du PDF.
- `fournis/pdf-complement-v1/` : quatre PDF que j'ai servis à l'auteur après ta v1 (2601.21112 ; 2609.03026 ; 2607.08349 ;
  2608.19338), empreintes dans `EMPREINTES-pdf-complement-v1.txt`. Vérifier : `cd fournis && sha256sum -c ../EMPREINTES-fournis-v2.txt`.
- Décisions de Lazar depuis ta v1 : phase exploratoire sans préenregistrement pour les tests d'hypothèses par des
  systèmes autonomes (14:39 Paris) ; aucune autre. Les deux rapports restent confidentiels (montants, financeur, page de
  titre) : rien de cela dans ton rapport ; vérifie que la v2 n'en laisse rien passer.

## 2. Ce que tu vérifies, en attaquant — seulement ce qui est nouveau ou changé

1. **Application de ta v1** : pour chaque CLS-01 à CLS-15, le traitement de la table est-il fait dans le texte (ligne), et
   les deux nuances de l'auteur tiennent-elles ? Dis « fait ; partiel ; non fait ; nuance acceptée / refusée ».
2. **Troisième partie du rapport (E à I)** — la v2 porte des jugements forts ; refais chacun sur la source (transcription
   v2 ou PDF, page) et sur le calcul (scripts rejoués avec `python3 -I`) :
   - « aucune faille démontrée ; toutes ont des voisins publiés » : le voisin couvre-t-il la même chose (R8) ? page lue ?
   - E : « la statistique d'énergie d'excursion ignore l'ordre des scores et ramène la détection à la classe C » — vrai
     en général, ou seulement sous l'attaque en dents de scie où $C_{t-1} = 0$ ? refais le raisonnement.
   - F : « 1 % visé devient 2,19 % à 4,56 % à 30 pas, même avec la normalisation du rapport » — sous quel nul simulé
     (l'auteur dit avoir choisi des nuls simplifiés) ; la normalisation du rapport est-elle implémentée telle qu'écrite
     ($\widetilde{M}_e$, $V_t$, $V_1$) ; le résultat tient-il si l'on change le nul (effet épisode nul, puis fort) ?
   - G : « un plancher sur covariance honnête accepte une sonde qui lit un tic de surface » — mécanisme exact, et
     négation (ancrage) : le plancher sur le mélange fait-il mieux ou pire sur le même cas ?
   - H : « repose sur une garantie 100 % fausse » — la phrase du rapport et l'argument de la v2 : établi ou opinion ?
   - I : « mesure une pente, ni une hystérésis ni une interaction » — exact sur la définition de $\chi_2$ du rapport ?
   - « aucune des cinq expériences n'est falsifiable telle qu'écrite ; HR3 connu d'avance ; HR5 franchi par hasard
     12,4 % des fois avec six moniteurs » — refais les deux calculs ; dis si « non falsifiable » est le bon mot ou si
     c'est « sous-spécifiée ».
3. **Hypothèses testables** (une par faille, HT-NN) : chacune a-t-elle hypothèse, prédiction signée, métrique, seuil, et
   une antériorité consignée ; sont-elles au niveau de la méthode (aucune recette) ; les rapprochements « hors du champ »
   (finance, physique statistique, autres) sont-ils sourcés ou décoratifs ?
4. **Quatre PDF de complément** : cités avec page ? la page dit-elle ce que la v2 lui fait dire (2601.21112 p. 1, 6, 7
   pour FI-06 ; 2609.03026 ; 2607.08349 ; 2608.19338) ?
5. **Décisions** : D-17, D-18, D-19 au format (options avec avantage et inconvénient ; défaut ; aucun défaut pour une
   dépense) ; D-02 et D-07 refaits comme ta v1 le demandait ; « cinq dépenses sans défaut » : lesquelles, et sont-elles
   bien des dépenses.
6. **Écarts déclarés** : « quatre PDF cités ont une empreinte sur disque absente des listes de provenance » — lesquels,
   et est-ce gênant ; 2410.12555 toujours non vérifié : la v2 le dit-elle partout où elle le cite ?
7. **Ancrage** : deux négations de ton choix parmi les jugements sur E à I.
8. **Ce qui manque** : un angle sur E à I que ni le rapport ni la v2 ne voient.

## 3. Ce que tu écris

`sortie/rapport-contre-lecture-synthese-v2.md` et son compagnon : verdict (« transmissible », « transmissible après
corrections », « à refaire ») ; constats `CLS2-NN` (bloquant ; à corriger ; mineur) avec lieu (ligne de la v2), ce qui ne
va pas, source, correction ; la table CLS-01 à 15 « fait / partiel / non fait » ; vérifications conformes ; ce que tu
n'as pas pu vérifier ; écarts. Tu ne corriges pas la synthèse.

## 4. Interdits

Rien hors de ce dossier et des dossiers de PDF nommés dans le brief v1 (lecture seule) ; aucun `git`, aucune clé, aucun
sous-agent ; réseau : au plus une recherche d'antériorité sur une faille E à I de ton choix, consignée ; Python avec
`-I` ; heures lues sur `date -u` dans la commande qui les écrit ; écrire seulement sous `sortie/`. Aucun montant,
financeur ni nom propre des rapports dans ton rapport.

## 5. Fin

Réponse finale en quelques lignes : verdict, constats bloquants ou à corriger, empreinte du rapport.

# Contre-lecture — état des faits sur les trois règles de la course à plusieurs générations, et projet d'essai — v1

- **Écrit** le 18 novembre 2026, vers 07:00 UTC, par un contre-lecteur neuf (règle R2) de la session mère, Claude Opus 5.5 (`claude-opus-5-5`), d'une autre lignée que le rédacteur (Claude Fable 5.2). Je n'ai écrit aucune des pièces lues, ni la conception de la course, ni son préenregistrement, ni le code de l'organisme.
- **Cadre tenu** : lecture seule hors de ce fichier et de la version 2 de la note ; aucune dépense, aucun appel de modèle, aucune clé, aucun contact, aucun commit, aucune poussée. Une récupération git superficielle (`--depth=1 --filter=blob:none`) de la branche `donnees/collisionneur-v8-runs-v2` (commit `0e7b3e59d7c5aeee5e63b43ef920fb8f565c8a11`), lue fichier par fichier par `git show`, sous le bloc-notes de la session, supprimée au rendu. Rien lu sous `diag/` ; aucun résultat de 7a, 7b, T0.6, de l'étape B, de l'étape B bis ni du premier test boîte blanche bis. Familles exclues : aucune pièce ouverte ; les passages des critiques croisées que la note signale comme proches de la famille 2 n'ont pas été lus (je n'ai lu que les lignes citées ci-dessous).
- R7 : ce que disent les espèces du collisionneur, et ce qu'écrit un document servi, est une affirmation de son auteur. R8 : une absence relevée ici est une question.

## 0. Verdicts

| pièce | chemin | empreinte | verdict |
|---|---|---|---|
| état des faits, version 1 | `docs/notes/trois-regles-course-generations-v1/etat-des-faits-v1.md` | `71e5cf0fd5680a8c784f5ef7c6254de00e813a02fa9584350815329d07e68360` (compagnon égal) | **à corriger** |
| projet d'essai des trois règles | `docs/notes/trois-regles-course-generations-v1/projet-essai-trois-regles-v1.md` | — | **sans objet : pièce absente** (voir section 3) |

**L'état des faits tient sur ses comptes et sur ses citations ; il faut corriger trois attributions et deux inférences trop larges, sans qu'aucune de ses dix lignes de résumé ne change de sens, sauf le point 4 (devenir des cartes sorties) qui devient « par construction » et le point 5 (contradiction écrite) dont l'un des deux textes n'est pas établi comme mot de Lazar.** Les corrections sont portées dans `etat-des-faits-v2.md` (section 4).

## 1. Rejeu du programme de comptage

- Programme `programmes/compter_trois_regles_v1.py` (`9cdc5dc742cb5d65d1a49324d6ccbf89d7d7789f5aba44b4b92b97e31b914f48`, compagnon égal), copié dans le bloc-notes et rejoué par `python3 -I compter_trois_regles_v1.py /home/user/controle-ia-travail <sortie>` : code 0.
- Sorties du rejeu **égales à l'octet** aux sorties versées : JSON `a1d65c9846710f61e50a86e0f0dddbf5fe1bd0a49304061f65dbb491c3735cf6`, sortie écran `df451564089b9bc181b77eb748e635d939a2959d3f4e7f423695ecbe2475bfa7`.
- J'ai lu le programme en entier. Il compte ce qu'il dit. Recomptés à la main sur sa sortie : témoins plantés de l'essai v64, 35 = 11 promus et testés (5 « survit », 6 « éliminée ») + 5 refusés + 19 non promus ; 27 verdicts du noyau = 16 cartes + 11 témoins, 20 « survit », 7 « éliminée » ; les 7 événements d'étage portent `"non concluant": 0` (lus dans le JSON, que la sortie écran n'imprime pas) ; les 7 exclues des fichiers de sélection sont 1 carte et 6 témoins, toutes « éliminée » (lu champ par champ) ; essai v66, 12 + 3 = 15 tests, 0 non concluant ; douze empreintes de modules égales aux deux manifestes de fin.
- Trois limites du programme que la note ne dit pas toutes :
  1. le dossier de travail d'une exécution est **déduit** du dossier du dernier argument de la commande (`os.path.dirname(cmd[-1])`) : juste si le script est posé dans le dossier de travail, ce que le code v5 fait ; c'est une inférence, pas une lecture d'un champ ;
  2. la recherche de mots dans la consigne ne porte que sur le texte **avant** le premier bloc JSON (584 caractères sur 15 730 en génération 2), et sur **huit** mots (« log e » compris), non sept ; j'ai refait la recherche sur le texte entier, en ajoutant « survi » et « retenu » : aucune occurrence hors de la phrase « mieux que les lois déjà retenues » — le constat de la note tient, et s'élargit ;
  3. « loi reproposée à la génération suivante » est compté contre les cartes de la génération suivante **du même bras** ; or le bras aléatoire n'appelle aucun proposeur (la note le dit elle-même en section 4.1, règle 2) : « non reproposée » y est vrai **par construction**, ce n'est pas une observation d'un proposeur (correction 4 ci-dessous).

## 2. Citations rouvertes (vingt-six)

Treize dans le dépôt, treize sur la branche du collisionneur. Toutes lues dans le fichier source ; empreinte du fichier recalculée quand la note en donne une.

| # | citation de la note | source rouverte | constat |
|---|---|---|---|
| 1 | R-3209, point 5, l. 3339 | `registres/decisions.md` l. 3339 | exacte (« Trois règles… : Lazar demande l'avis de la mère et une version approfondie… ») |
| 2 | « non concluant » rangé sous « éliminée », seule « survit » retenue | `tests_de_mort_v4.py` l. 24-28 | exacte (la citation court jusqu'à la l. 28, non 27) |
| 3 | « dernière exécution réussie » ; « l'expérimentateur choisit… » | `tests_de_mort_v4.py` l. 43-44, 57 | exacte |
| 4 | vue « jamais un verdict, une richesse… » | `boucle_fermee_v59.py` l. 18-20 | exacte |
| 5 | avant la v59, « l'héritage servi reste le classement des juges » ; changement écrit l. 24-26 | `boucle_fermee_v59.py` l. 4-6, 24-26 | exacte |
| 6 | garde à 19 clés, vue rangée par identifiant | `boucle_fermee_v59.py`, `CLES_INTERDITES_VUE` ; l. 198-218 | exacte : 19 clés comptées ; `sorted(...)` des identifiants |
| 7 | consigne « neuf à chaque exécution : rien ne subsiste » | `tests_de_mort.py` l. 29-30, 1467 | exacte |
| 8 | dossier neuf par exécution, hors de la sortie, retiré après l'inventaire ; « depuis la version 49 » | `tests_de_mort.py` l. 1916-1921 | **à préciser** : le dossier neuf est la v49 (CL13-02, l. 1916) ; « hors de la sortie et retiré après l'inventaire » est la **v50** (CL14-04, CL14-01, l. 1918-1919) |
| 9 | quota 3 ; 12 tours | `tests_de_mort.py` l. 107 ; `tour_ferme_v64.py` l. 51, 146 ; `tests_de_mort_v5.py` l. 132 | exacte |
| 10 | `tour_ferme_v64.py` : « aucune occurrence de « memoire », « redite », « doublon » » | `tour_ferme_v64.py` | **fausse à la lettre** : `MEMOIRE_BAC_MO` (l. 143) et `"memoire_mo"` (l. 875), borne de mémoire du bac, sans rapport avec une mémoire des cartes. Plus important : le module importe `ideation_v2` (l. 828), et le code de l'organisme porte une politique de redite (`cycle.py` l. 73, 123-124 : « heritage », « refus », « rien » ; `memoire.py`). Dans `tour_ferme_v64.py`, `ideation_v2` ne sert qu'à la liste blanche de la tranche (l. 847-848), d'après ma lecture : la conclusion « pas de mémoire des cartes sorties dans le tour fermé » est probable, **non établie par la recherche faite** (correction 3) |
| 11 | groupe éliminé, sœurs rejugées après la course ; vue servie = archive | brouillon 6, l. 447-451 | exacte (empreinte `4deec525…` égale) |
| 12 | test « coupé par sa borne de 1,50 USD » … « compté à part » (l. 552-553) | brouillon 6, l. 552-553 | **à préciser** : l. 552-553 disent « coupé par sa borne, ou témoin d'isolement en défaut, garde 27 » ; le montant de 1,50 USD est aux l. 72, 376 et 900 |
| 13 | course v67 : 14 tests, une exécution, 13 « survit », 1 « éliminée » ; réponses brutes non gardées | `verdict-course-v67-v1.md` (`d7902432…` égale) l. 108-115, 139-149, 176-180 | comptes exacts ; **la réserve « dossier des sessions vide » est la R-2 (l. 176), non la R-5** (la R-5 dit que la génération 2 n'a exercé ni le bac ni la sélection) |
| 14 | N-053, point 5 | `decision-N-053-v1.md` l. 42-44 | exacte |
| 15 | N-058, points 1 et 2 | `decision-N-058-v1.md` l. 20, 24 | exacte |
| 16 | sél/A l. 31 (« différée », pas « éliminée ») | branche, sél/critique A (`e384758e…`, 131 lignes) | exacte |
| 17 | sél/B l. 114 (multiplicité, extinction, « confondant ») | sél/critique B (`26723d67…`, 137 l.) | exacte |
| 18 | sél/D l. 9 (filles d'éliminées) | sél/critique D (`3f87e041…`, 110 l.) | exacte |
| 19 | bac/B l. 17 (artefact : un script écrit un fichier lu par le suivant) | bac/critique B (`42d6b469…`, 128 l.) | exacte |
| 20 | bac/B l. 65 (1 exécution contre 3) | même fichier | exacte |
| 21 | bac/C l. 22 (contrôle d'état inter-exécutions, cache légitime) | bac/critique C (`6c4ddece…`, 84 l.) | exacte |
| 22 | bac/C l. 35 (≈ 0,14 par fiche, illustratif) | même fichier, l. 29 et 35 | exacte : « q ≈ 0,1426 » pour trois essais indépendants au niveau 0,05, « (illustratif) » |
| 23 | bac/D l. 26 (dossier vierge contre prérempli) | bac/critique D (`cd955906…`, 102 l.) | exacte |
| 24 | sél/`faits.md` l. 52 (« verdict, classement et étiquette d'héritage ») et l. 143 (3 indécises sur 18) | sél/`faits.md` (`7c3404f4…`) | exactes |
| 25 | « indécise → un test plus puissant, ou retirée après deux essais » (sél/`faits.md` l. 202-203), dit « conception du pôle » | sél/`faits.md` l. 177 et 202-203 | citation exacte ; **source mal nommée** : le passage est la « Pièce 2 — intégration des proposeurs dans l'organisme » (`integration-proposeurs-ia-v1.md`, `974b2dbe17b7…`, absente de `main` d'après ma recherche par nom), non une « conception du pôle » |
| 26 | « une idée non concluante ne passe pas à la génération suivante » (sél/`question.md` l. 3), dit « objectif de Lazar du 1er novembre » ; bac/`faits.md` l. 51-56 (v48 : un seul dossier inscriptible, 3 exécutions, dernière exécution réussie) | sél/`question.md` (`c8992218…`) ; bac/`faits.md` (`24064c98…`) | bac exact. Sél : la phrase est écrite par l'auteur de la question (conv-audit), dans un paragraphe qui commence par « Objectif fixé par Lazar le 1er novembre » ; **le registre ne la porte pas** : R-948 (`registres/decisions.md` l. 1177) rapporte seulement l'objectif « reformulé « idées validées par l'expérience » ». Que « non concluante ne passe pas » soit un mot de Lazar n'est pas établi (correction 1) |

## 3. Projet d'essai des trois règles : pièce absente

- Chemin demandé : `docs/notes/trois-regles-course-generations-v1/projet-essai-trois-regles-v1.md`. Vérifié selon R11 : absent du disque (`ls` du dossier : seuls `etat-des-faits-v1.md`, son compagnon et `programmes/`), absent de toute l'arborescence (`find /` sur le préfixe `projet-essai-trois-regles`), absent de l'historique local (`git log --all` sur le dossier : trois commits, aucun ne porte ce nom), aucun fichier du dépôt ne le cite. Vérifié deux fois, à 06:58 et au moment de sceller.
- Je ne peux donc juger aucune des questions posées (hypothèse, prédiction chiffrée et signe, métrique, seuil, plan, trois issues par règle ; jugement sur l'oracle et le coût seulement ; issue acquise d'avance). Je ne rédige pas l'essai à la place de son auteur.
- Ce que l'état des faits impose déjà à ce projet, pour sa future contre-lecture (constats, non recommandations) :
  1. **Règle 1** : zéro non-concluant observé dans 56 tests (27 + 15 + 14), et zéro attendu par construction dans les essais à blanc. Un essai qui compare « retirée », « différée », « dormante » sans **planter** des fiches non concluantes (borne coupée, panne, isolement en défaut) n'aurait rien à comparer : l'issue « aucune différence » y serait acquise d'avance.
  2. **Règle 2** : la vue servie n'a jamais porté de note ou de rang depuis la v59 ; un essai doit fabriquer le bras « note servie », et N-053 (point 5) et N-058 interdisent de juger ce bras ou la composition des proposeurs sur le verdict du juge : seul l'oracle du monde planté et le coût sont admissibles comme critère. La portée de N-053 sur le contenu d'une consigne n'est pas tranchée (Lazar).
  3. **Règle 3** : aucune fiche à deux exécutions n'a jamais été observée ; avec des doublures qui réussissent du premier coup, un bras « cache déclaré » contre « interdit » rendrait zéro par construction. Il faut un expérimentateur qui fasse au moins deux exécutions, ou un artefact planté (bac/B l. 17), et une garde testée sur un cas sain et sur un artefact (R5).

## 4. Corrections portées dans la version 2

`etat-des-faits-v2.md`, même dossier, scellé ; la version 1 reste inchangée. Corrections, par ordre d'importance :

1. **Attribution de « une idée non concluante ne passe pas »** (section 0, écart 2 ; résumé 5 ; section 7, règle 1) : texte de la question servie au collisionneur, présenté par son auteur comme objectif de Lazar ; R-948 ne rapporte que « idées validées par l'expérience ». La contradiction reste entre deux **textes servis au collisionneur**, non « deux textes du programme ».
2. **Source de « indécise → un test plus puissant… »** : la pièce 2 des faits servis, « intégration des proposeurs dans l'organisme » (`integration-proposeurs-ia-v1.md`, `974b2dbe17b7…`), et non « la conception du pôle ».
3. **« Aucune mémoire des cartes sorties »** (section 5, règle 1) : l'énoncé de recherche est faux à la lettre (`memoire` occurre deux fois, borne du bac) et la recherche ne couvre pas les modules importés ; le code de l'organisme porte une politique de redite (`cycle.py`, `memoire.py`) dont l'usage par le tour fermé n'est pas établi.
4. **Devenir des 9 cartes sorties** (section 4.1 ; résumé 4 ; section 7) : dans le bras aléatoire, « non reproposée » est vrai par construction (aucun proposeur appelé) ; ce n'est pas une observation. Le seul fait observé est « absentes de l'archive servie ».
5. **Réserve du juge de la v67** : « dossier des sessions vide » est la réserve R-2, non R-5.
6. **Dossier de travail** : neuf par exécution depuis la v49 ; hors de la sortie et retiré après l'inventaire depuis la v50.
7. **Brouillon 6, l. 552-553** : la borne de 1,50 USD n'y figure pas ; elle est aux l. 72, 376, 900.
8. **Recherche de mots** : huit mots, non sept, sur les 584 premiers caractères ; refaite sur le texte entier par moi, même constat.
9. **Borne citée de `tests_de_mort_v4.py`** : l. 24-28, non 24-27.

Ce qui ne change pas : le verdict de la note (aucune course n'a exercé les trois règles), tous ses comptes, ses tableaux par règle hors les points ci-dessus, sa liste de ce qui manque.

## 5. Réserves de cette contre-lecture

- Je n'ai pas relu les quatre pièces de conception (v4, v7, brouillons 3 et 6) au-delà des lignes citées, ni la note du collisionneur du 2 novembre, ni l'inventaire ; les sections 2, 3 et 7 de la note qui en dépendent ne sont contre-lues que par échantillon.
- Je n'ai lu aucune branche de course (v67, pôle, pilotes) : les manques 1 à 4 de la note restent entiers.
- Je n'ai rencontré aucune instruction adressée au lecteur dans les pièces lues.

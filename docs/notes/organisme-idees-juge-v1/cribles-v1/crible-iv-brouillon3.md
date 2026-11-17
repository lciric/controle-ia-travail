# Préenregistrement — crible (iv) de l'organisme d'idéation : demi-générations, l'archive mise à jour au milieu de chaque génération — brouillon 3 (variante « crédits de Claude au maximum »)

- Auteur : sous-agent neuf de la session mère, rédacteur de cette pièce (« modèle A » de cette pièce au sens de R-2598 ;
  identité dite en conversation seulement). L'auteur n'a écrit ni la note des idées originales, ni le relevé, ni les fiches,
  ni le pilote MR-2, ni son code, ni sa procédure, ni la famille MR-2 ni ses outils, ni aucune pièce des cribles (i), (ii),
  (iii) et (v), ni aucune contre-lecture citée.
- Date (UTC) : 2026-11-17, rédaction de 01:00:56 à 01:17 (`date -u` au début et juste avant le scellement) ; dépôt lu sur
  `main` (tête `c97bf55f`, puis `b55f2983`) ; une seule branche lue, `verdict/pilote-mr2-v74-v14-v1` (tête `61230010`), par
  `git show` après un `git fetch` à refspec, et d'elle **seul** le verdict v2 du pilote ; aucun commit, aucune poussée, aucun
  appel de modèle, aucune machine, aucune dépense, aucun monde tiré.
- Brouillon 2 : corrections du tour 1 de contre-lecture appliquées le 2026-11-17T01:37:23Z (`date -u`, au scellement) par un
  rédacteur neuf, d'un autre modèle que le rédacteur du brouillon 1, qui n'a écrit ni le brouillon 1 ni le rapport de
  contre-lecture (identité dite en conversation seulement), au moyen du programme
  `appliquer-corrections-crible-iv-brouillon2.py` (même dossier, scellé) ; dépôt lu sur `main` (tête `1df4ae9f`) ;
  aucune branche lue ; aucun commit, aucune poussée, aucun appel de modèle, aucune machine, aucune dépense, aucun monde
  tiré. Rien d'autre que les corrections, le titre, le statut, la ligne du validateur, cette ligne et la section « Contre-lecture » ne change.
- Brouillon 3 : corrections du tour 2 de contre-lecture (une majeure, M1, et deux mineures, m1 et m2 ; trois couples)
  appliquées le 2026-11-17T02:00:43Z (`date -u`, au scellement) par un rédacteur neuf, qui n'a écrit ni les brouillons 1 et 2 ni
  aucun des deux rapports de contre-lecture (identité dite en conversation seulement), au moyen du programme
  `appliquer-corrections-crible-iv-brouillon3.py` (même dossier, scellé ; différentiel `diff-crible-iv-b2-vers-b3.txt`, scellé) ;
  arbre de travail lu sur `main` (tête `1df4ae9f` au début de la lecture, `b4ecab17` à l'écriture ;
  brouillon 2 et rapport du tour 2, non encore suivis, lus sur disque, empreintes vérifiées) ; aucune autre branche lue ;
  aucun commit, aucune poussée, aucun appel de modèle, aucune machine, aucune dépense, aucun monde tiré. Ne changent que
  les trois corrections, le titre, le statut, la ligne du validateur, cette ligne et la section « Contre-lecture ».
- Nombres neufs : `devis-crible-iv-brouillon1.py` et sa sortie `devis-crible-iv-brouillon1-sortie.txt` (même dossier, scellés à
  côté ; `nice -n 19 python3 -I`, Python 3.13.18, bibliothèque standard, fractions exactes ; lancé le 2026-11-17 à 01:09:28 UTC) ;
  paragraphes de la sortie cités « sortie, § k » ; sortie recopiée à l'annexe A. Deux valeurs y sont **supposées**, dites comme
  telles partout : la part d'entrée d'un appel (texte servi de 52 000 octets à 3 octets par jeton) et la durée d'un tour de
  chaîne sur processeur (60 s).
- Commit du code d'analyse : **aucun à ce jour**. Le code s'écrit après la contre-lecture de ce texte et son scellement ; ses
  empreintes entrent dans un addendum d'empreintes scellé avant tout jeu, qui ne change rien d'autre.
- Documents qui font foi (chemin, empreinte entière) :
  - note des idées originales, § 0, § 1, § 2, § 3 (iv), § 4, § 5, § 6, § 7 et annexe A :
    `docs/notes/organisme-idees-juge-v1/conception-idees-originales-v1.md`
    (`2f6a69dd480a079fa385846c8aca06ff53c8d40b0cf36be1fd61cf8e1e0537a3`, égale à son compagnon) — ci-dessous **[NOTE]** ;
  - relevé des idées, § 2.1, § 4.1, § 5 et § 6 : `docs/notes/organisme-conception-propre-v1/relecture-exploratoire-v2/releve-idees-reutilisables-v1.md`
    (`bd253b6c68f6baada0e61b5381f029b52838ca34aa092502e55253c662451c6c`) — **[RELEVÉ]** ; fiche opus-p1-02 (n° 6) du fichier
    `runs/course-ideation-conception-propre-v1/20261113-235541-course-ideation-conception-propre-v1-g1/copies/sortie--fiches-validees.json`
    (`a9f9594e2dc3a7a553c54577202817758e3f7ef231445f1a48d500fc647389d5`) : **non relue par l'auteur** (pièce sous `runs/`), citée à
    travers [RELEVÉ] et [NOTE] ;
  - verdict v2 de l'issue du pilote MR-2 v14 : `docs/notes/organisme-multi-generations-v1/pilote-v1/lecture-issue-pilote-v14-mere/verdict-issue-v2/verdict-issue-pilote-mr2-v14-v2.md`
    (`e64458e82bae1d03e40656ad3b65456769eefd2603a7306e9a7d401eba8e1a3d`, égale au compagnon et à `git show | sha256sum`), branche
    `verdict/pilote-mr2-v74-v14-v1` ; lu en entier, en particulier « Pour les cribles », « Dépense rapprochée », « Comptes » et
    « Audit de symétrie » — **[VERDICT-PC]** ;
  - version qui fera foi v1 du crible (iii), même dossier : `crible-iii-version-foi-v1.md`
    (`91b4bf30fbf8b83d2c057088d8776be19831b006f1010bcb3c7e2e231d2c7179`) — **[CRIBLE-III]** ; source, à travers elle, des
    définitions de [PILOTE] (« Métrique » : appels, cartes, composantes comptées, attribution), du bloc gelé (plafonds de session,
    bornes de sortie, réglages, gabarit `e77d3041…`) et de [PROC-14] (machine, barrières, rapatriement), **non relus par l'auteur**
    sur leurs branches ; lus : en-tête, statut ;
  - version qui fera foi v2 du crible (v), même dossier : `crible-v-version-foi-v2.md`
    (`2b99627dd378564dba816bc10593cdb0d06d77a3fdd4eb9e3cca022c76838715`) — **[CRIBLE-V]** ; table des proposeurs, règles (a) à (c)
    du devis refait, règle de la borne par appel B_a, enveloppe ;
  - brouillon 1 du crible (ii), même dossier : `crible-ii-brouillon1.md`
    (`816a072f6c9192049f325661e7b0ea2f0530dc1f738c4c39b8e75fba62364609`, égale à son compagnon) — **[CRIBLE-II]** ; **modèle de
    forme** de ce texte (mêmes règles d'enveloppe, de devis et de taille servie) ; brouillon 1 du crible (i), même dossier :
    `crible-i-brouillon1.md` (`a3c38ccc460c30958c82eaf92701de94435fafee54a93bba2f1de0bdddebd641`) — **[CRIBLE-I]**, lu pour son
    seul pire cas (127,00 USD, enveloppe) ;
  - registre des GO, ligne GO-2026-11-15-06 (l. 339) : `registres/go.md` (fichier de travail,
    `c20084fb698609b84a97b41f4ec759775d03a8030d913411bb1afa954eafb54b`) ; registre des dépenses (fichier de travail,
    `edb519ccb8e5861c6138356a32bdde1a8730ceb57b86aaf527d2c856d3dce858`) : **aucune** ligne de l'un ni de l'autre ne cite
    GO-2026-11-15-06 hors la l. 339 ; registre des décisions (fichier de travail, `f749dba4…`) : R-1779 (« le nul de production
    reste le v8 »), R-2598, R-2690, R-2803, R-2851, R-2875, R-2977, R-2992, R-2993, R-3005, R-3044, R-3053 ;
  - famille MR-2 : conception v4 `docs/notes/organisme-multi-generations-v1/conception-monde-riche-doublons-v4.md`
    (`47e38ec0663320e8c68011130c3f1b8e1017969cbb740d30c83a78eb5db0a6dc`) — **[MR2]**, § 0 à 7, lue en entier ;
  - outils, lus dans les parties citées : `docs/notes/organisme-multi-generations-v1/outils-v4/monde_riche_v4.py`
    (`4b1658477811fb87360dda44a65b0af96e87ae1d2ca4a32bdabbd3ce6cc19eb8` ; `tirer_gabarit_v4`, `generer_monde_v4`, `generer_v4`,
    `verifier_v4`, `course`) ; `…/outils-v1/monde_riche_outils_v1.py`
    (`1825b956eed638fe4daf3d7395a169fdbdf7c9679076d9ba3fb4a15cfd7ec85e` ; `juger`, `log_e_arrete`, `e_bh`, `test_de_mort`,
    constantes `ALPHA` = 0,05, `SEUIL_ORACLE` = 0,02, `SEUIL_MORT` = 0,02) ; `…/outils-v1/complements_synthese_v1.py`
    (`89eb7ba8c8cf8633541a6de8090767f74619e3f3968ebed8f894b1f8d593e9ba`, cité à travers [CRIBLE-II], non relu) ;
    `…/pilote-v1/outils/mesure_pilote_v4.py` (`676d5f37f21cf5d512f92d2029991fa8795a77076c285ea9bd83c43841748365`, cité à travers
    [CRIBLE-III], non relu) ; copie du nul v9 `docs/notes/organisme-idees-juge-v1/copie-nul-v9-a41b7b5/orchestrator/pole/nul_v9.py`
    (`7ae450df2482246122bf9fbcf0fa5ef30b4a7e4c6f0d09531e83af048e46ee95`), en-tête lu seulement ;
  - décisions : `docs/decisions/decision-N-058-v1.md` (`854f2724864f1e45394e001f4aca7b0248753e5d2b0a66991e2ee8a7be87de9d`,
    points 1 et 2 lus), `docs/decisions/decision-N-045-v2.md` (`c7b05e39de381cee1d5ec2276745a0310bd3cc0857a6be0e0fb14eeb5042261d`,
    point 5 lu), `docs/decisions/decision-N-044-v1.md` (`2b70bdac014d366d058a530680d016663b35ed73b8ca0cae9f2369206f5004bf`),
    `docs/decisions/decision-N-067-v1.md` (`966dd9dc3fae61cbe1f10ee2a54f401ddf7af5041eeaacd81ad9f8b264661589`) — empreintes
    vérifiées ; N-044 et N-067 non relues en entier (citées à travers [NOTE]) ;
  - catalogue des conceptions publiées : `docs/notes/organisme-conception-propre-v1/catalogue-conceptions-publiees-v1.md`
    (`ddfb2522be0fe5095926405b8761d0e4be0065a29679585051a287349114fe9d`) — **[CAT]**, lignes C1, C5 et C6 ;
  - gabarit `prereg/gabarit-preregistrement-v1.md` (`8cad43714b562e28238a92200d6315b1769d8bdf7e9f0a8d72dfe2bc9b37700e`) ;
    validateur `src/controle_ia/prereg.py` (`3b2e3ee56463f30ffd3c549e7fe480fea574c707581bcf30098bf38f4980c306`).

**Statut.** **Brouillon 3**, contre-lu deux fois (tours 1 et 2, corrections appliquées, section « Contre-lecture »),
scellé comme pièce (empreinte compagnon, R6), non comme préenregistrement en vigueur ; troisième tour de contre-lecture
à faire (R2), réduit aux trois couples du tour 2, aux couples de forme et au différentiel. Écrit **après** la lecture du verdict du pilote MR-2 v14 (aucun gel de prédictions n'a précédé cette lecture, à la
différence de [CRIBLE-I] : dit) ; les attendus du devis sont faits directement sur les coûts et durées mesurés du pilote
([VERDICT-PC]) par les règles de [CRIBLE-V] (moyenne de tous les appels, pires cas aux plafonds) ; les prédictions sont écrites
sans aucune donnée de couverture par appel (le pilote ne la rend pas ; seuls son témoin positif et sa principale sont lus).
Aucune dépense, aucun appel de modèle, aucun monde tiré. L'accord GO-2026-11-15-06 (enveloppe des cinq cribles, crédits de
Claude employés au maximum) **n'autorise encore aucun appel** : la ligne « calcul » de ce crible s'inscrit par la mère sur un
devis contre-lu, dans l'enveloppe (lecture de la mère, l. 339). Le dessin neuf (calendrier en demi-générations) et le test de mort
mécanique sont **essayés, non adoptés** (l. 339 ; [NOTE] § 7, point 4) : toute adoption dans l'organisme reste un nœud de Lazar.
**Point de faisabilité à trancher avant tout code** (« Choix et doutes », point 3) : la garde d'égalité de dollars **par monde**
de [NOTE] ne laisse aux bras 2 et 3 leurs quatre demi-appels que si un appel de trois cartes coûte moins des deux tiers d'un appel
de six (sortie, § 4) ; ce rapport n'est pas mesuré (supposé 0,63 : juste sous le seuil ; s'il valait 1, la garde couperait toute
la génération 2 des bras 2 et 3) ; la sonde des gabarits le mesure, et une règle écrite d'avance dit ce qui suit.
Validateur `controle_ia.prereg.problemes` : aucun défaut sur ce brouillon 3 (vérifié par le programme de correction sur
une copie temporaire, avant l'écriture et le scellement comme pièce de travail).

## 0. En dix lignes

1. **Question** ([NOTE] § 3 (iv) ; [RELEVÉ] § 4.1) : une génération de six cartes devenue **deux demi-générations de trois**, avec
   toute la chaîne entre les deux (gardien, juge, test de mort, sélection, archive), couvre-t-elle davantage de composantes
   plantées, et va-t-elle plus profond dans une chaîne de conditionnelles, **à dollars égaux** ? Et l'effet vient-il de la **mise
   à jour** de l'archive à mi-génération, ou du seul **découpage** en deux appels de trois cartes ?
2. **Trois bras** sur les mêmes 20 mondes MR-2 **à deux conditionnelles chaînées** (profondeur 2), archive de départ {K1},
   **deux générations** : **bras 1** standard (un appel de six cartes par génération, chaîne en fin de génération) ; **bras 2**
   demi-générations (deux appels de trois cartes par génération, chaîne après chacun) ; **bras 3** placebo (deux appels de trois
   cartes **sans** mise à jour entre eux, chaîne en fin de génération).
3. **Version de la variante « crédits de Claude au maximum »** : toutes les places tenues par des sessions neuves de **Pr-2**
   (sur crédits de Claude) au lieu de Pr-1 (hors crédits) ([NOTE] : Pr-1 seul) ; forme de [CRIBLE-II] et de R-2992.
4. **Appel commun** : le premier demi-appel de la génération 1 (« 1a ») voit le même texte dans les bras 2 et 3 (archive {K1},
   gabarit de trois cartes) ; il est **un seul** appel, compté dans les deux bras : **9 appels par monde, 180 en tout** au lieu de
   200 (écart à [NOTE], dit ; forme du « rang 1 commun » de [CRIBLE-II]).
5. **Chaîne sur processeur**, celle de la course simulée de [MR2] (`course` de `monde_riche_v4.py`) sous des noms neufs : juge
   contre le **nul v8 de l'archive** (le nul de production, R-1779), 400 tirages frais, regroupement, e-BH à m = 48 fixe, représentant,
   **test de mort mécanique** (statistique gelée de l'outil, épisodes frais, aucun expérimentateur) ; les retenues entrent dans
   l'archive servie au tour suivant.
6. **Mesure** (oracle du pilote) : C_X(w), composantes comptées **captées par l'archive** du bras X à la fin de la génération 2 ;
   profondeur atteinte (0, 1 ou 2 conditionnelles de la chaîne captées) ; couverture des cartes brutes ; copies ; fausses retenues ;
   dollars ; appels coupés par la garde.
7. **Deux principales** (Bonferroni, bilatéral à 0,025 chacune, test exact des rangs signés) : **P1** δ_21 = C_2 − C_1
   (demi-générations contre standard, à dollars égaux) ; **P2** δ_23 = C_2 − C_3 (mise à jour contre simple découpage).
   Secondaires : δ_31, profondeur, conditionnelles captées.
8. **Prédiction de l'auteur** : P1 « non tranché », δ_21 entre 0 et + 0,5 composante par monde (confiance 0,4) ; P2 « non
   tranché », entre 0 et + 0,4 (0,4) ; seconde conditionnelle captée dans au plus un monde du bras 2, aucun des bras 1 et 3 (0,55).
9. **Devis** (coûts mesurés du pilote, règles de [CRIBLE-V]) : **48,64 USD attendus sur crédits de Claude** si tous les appels
   partent (180 appels à 0,264334, plus la sonde, 1,06 ; 34,99 si un appel de trois cartes coûte ce que la part supposée d'entrée
   donne) ; **0,09 à 0,19 hors crédits** (machine) ; **251 au pire** (240 sur crédits, **part du relais**, plus 8 de sonde ; 3 hors
   crédits) ; [NOTE] : 30,30 attendus, 243 au pire. Le pire est borné par la part, non par plafonds × appels (360) : dit.
10. **Enveloppe** de GO-2026-11-15-06 aux textes actuels des quatre autres cribles ((iii) 270, (v) 204,67, (ii) 411, (i) 127) :
    cumul **1 263,67 USD**, sous 1 275 (marge 11,33 ; 17,33 avec la sonde partagée avec (ii)) ; sortie, § 8. **Durée** : ≈ 51 min
    d'appels et de chaîne attendues (cinq files ; tour de chaîne supposé 60 s), pire 10 h à B_c = 600 s, garde de départ 12 h.

## Hypothèse

**Contexte.** La fiche opus-p1-02 ([RELEVÉ] § 4.1 ; titres repris en quarantaine chez deux autres proposeurs) propose de
couper chaque génération en deux demi-générations de trois cartes, « avec toute la chaîne (gardien, juge, test de mort, archive)
entre les deux, au même plafond de dollars » : « un constat trouvé à la première moitié entre dans le nul ; ses variantes à la
seconde moitié deviennent des copies refusées ; une condition archivée plus tôt rend sa composante conditionnelle trouvable plus
tôt ». Elle sert QO2 (ce qu'une génération lègue) et la profondeur en chaîne : la borne 4 du recoupement des méthodes dit que
l'horizon en générations borne la profondeur atteignable ; deux demi-générations doublent cet horizon au même prix ([RELEVÉ]
§ 4.1). Le placebo de la fiche : deux appels de trois cartes **sans** mise à jour entre eux. La famille MR-2 rend cette question
répondable : une conditionnelle est **invisible marginalement** (part marginale médiane 0,0195 de son information, [MR2] § 4.3)
et devient visible par branche une fois sa condition captée ; la seconde conditionnelle d'une chaîne dépend de la première
([MR2] § 2.1).

**H-iv** (énoncé de [NOTE] § 3 (iv), proposeur de la variante). Dans une course de deux générations partie de {K1}, sur des
mondes MR-2 à chaîne de profondeur 2, des générations coupées en deux demi-générations de trois cartes avec la chaîne entre les
deux (bras 2) laissent à la fin de la génération 2 une archive qui capte un **nombre de composantes comptées différent** de celui
de générations ordinaires de six cartes (bras 1), **à dollars égaux** (garde par monde) ; le signe n'est pas fixé par le
programme.

**H-iv-a** (contrôle, [RELEVÉ] § 4.1 et § 5 ; N-045 point 7, « espaces de conception égaux ») : l'écart 2 − 1, s'il existe,
vient de la **mise à jour** de l'archive entre les deux demi-appels (2 contre 3), et non du seul découpage d'un appel de six en
deux appels de trois (3 contre 1).

**La variante change-t-elle la question de [NOTE] ?** Un peu ; c'est dit ici, **sans trancher** (si la question n'est plus celle
de la note, c'est à la mère ou à Lazar de le dire). [NOTE] fait tenir toutes les places par Pr-1 (hors crédits) ; la variante
les donne à Pr-2 (sur crédits de Claude). Restent les mêmes : un seul proposeur, les trois bras, deux générations, la chaîne et le
test de mort mécanique, la garde d'égalité, la mesure. Change la portée : une conclusion porte sur les sessions d'**un**
proposeur de la maison de Claude. Change aussi, peut-être, la garde : l'issue de la garde dépend du rapport du coût d'un appel de
trois cartes à celui d'un appel de six, propre à chaque proposeur (point 3 de « Choix et doutes »).

**Hypothèses de travail.** (i) Sessions neuves et indépendantes, sans historique ; une session ne reçoit des tours précédents que
l'**archive** (lois retenues, sous la forme où le gabarit du pilote sert K1), jamais une carte refusée, un verdict, une
richesse, un groupe ni une réponse brute. (ii) **Deux générations** : ni plus ni moins dans tous les bras ; le nombre de
demi-générations (deux par génération) est fixé d'avance, jamais piloté par les promotions (N-058, [RELEVÉ] § 4.1). (iii) La
chaîne est celle de la course simulée de [MR2] (`course`), sur processeur, sans expérimentateur : le test de mort est la
statistique gelée de `test_de_mort` (gain moyen de log-score sur la marginale empirique de 400 épisodes frais, seuil 0,02) ;
c'est une **simplification déclarée** de la chaîne réelle, qui retire son poste le plus cher (borne par test de l'expérimentateur
de 0,80 à 3,40 USD selon le modèle, [NOTE] citant la conception du monde riche v3, `386d48ba…`, § 6.2). (iv) L'hypothèse dont
dépend tout gain de profondeur, « une conditionnelle se trouve **après** sa condition », n'est **pas mesurée** (faits du
collisionneur, `d19b5400…`, § 4, à travers [NOTE] § 1) ; le pilote n'a mesuré que l'autre côté : **aucun** des 14 appels répondus
ne porte une conditionnelle sans sa condition (x = 0 sur 14, [VERDICT-PC], « Comptes »), et 6 portent la composante de condition.
(v) Une carte peut porter plusieurs composantes ; la couverture sature vite sur les composantes visibles à la marge ; l'écart
possible tient surtout aux conditionnelles.

## Prédiction chiffrée et signe attendu

Écrites **après** la lecture du verdict du pilote (dit au statut), sans aucune donnée de couverture par appel ; seuls lus : la
principale du pilote (x = 0 sur 14 appels répondus portent une conditionnelle sans sa condition) et son témoin positif (14 sur 14
vont au-delà de K1 ; 6 portent la composante de condition) ; confiance faible. Notations : section « Métrique ».

| # | prédiction | signe | chiffre | ce qui la réfute | confiance |
|---|---|---|---|---|---|
| IV-1 | **principale P1** : δ_21 (demi-générations contre standard, à dollars égaux) | ≥ 0 | estimation entre 0 et + 0,5 composante par monde ; issue « non tranché » | estimation de δ_21 < 0 (réfute le signe) ; issue autre que « non tranché » (réfute l'issue) | 0,4 |
| IV-2 | **principale P2** : δ_23 (mise à jour contre simple découpage) | ≥ 0 | estimation entre 0 et + 0,4 ; issue « non tranché » | estimation < 0 ; issue autre que « non tranché » | 0,4 |
| IV-3 | δ_31 (découpage seul) | ≈ 0 | estimation entre − 0,3 et + 0,4 | test des rangs signés bilatéral à 0,05 significatif, de l'un ou l'autre signe | 0,45 |
| IV-4 | mondes complets où la **première** conditionnelle de la chaîne est captée : bras 2 moins bras 1 | ≥ 0 | entre 0 et + 3 mondes ; bras 1 entre 0 et 4 mondes | bras 2 moins bras 1 ≤ − 2 mondes | 0,4 |
| IV-5 | mondes complets où la **seconde** conditionnelle (profondeur 2) est captée | — | bras 2 : 0 ou 1 ; bras 1 et 3 : 0 | 3 mondes ou plus dans un bras quelconque | 0,55 |
| IV-6 | conditionnelles captées **avant** leur condition (toutes les retenues, tous les bras) | — | 0 ou 1 en tout | 3 ou plus | 0,5 |
| IV-7 | fausses retenues (gain au-delà de l'enveloppe < 0,02, oracle), part des retenues par bras | ≈ | entre 0 et 0,20 dans chaque bras ; écart entre bras ≤ 0,10 | une part > 0,35 ; un écart > 0,20 | 0,4 |
| IV-8 | mondes complets pour P1 où la garde coupe au moins un demi-appel du bras 2 | + | entre 3 et 15 mondes | 0 monde, ou 18 ou plus | 0,3 |
| IV-9 | coût relatif ρ_21 = $_2 / $_1 (prix publics) | ≥ 1 | 1,00 à 1,30 | < 0,95 ou > 1,40 | 0,55 |

**Portée de la colonne « ce qui la réfute »** (forme de [CRIBLE-III], remarque R-4, reprise par [CRIBLE-II]) : une prédiction dont
le chiffre est manqué sans que cette colonne soit atteinte n'est **ni confirmée ni réfutée** ; le rapport le dit tel quel.

**Raisons.** Dans les mondes de développement de [MR2], hors l'effet de K1, 3 à 5 composantes sont à couvrir par monde
([CRIBLE-III], « Raisons », d'après [MR2]) ; les mondes du crible en ont une de plus (deux conditionnelles). IV-1 : les fortes et
les moyennes visibles sont captées dans tous les bras dès la génération 1 (le témoin positif du pilote dit que chaque appel va
au-delà de K1) ; l'écart possible tient aux conditionnelles : le bras 2 a jusqu'à trois occasions après une condition captée à
1a (1b, 2a, 2b), le bras 1 une seule (génération 2), le bras 3 une seule paire (génération 2) ; à 6 appels sur 14 portant la
composante de condition au pilote, et une probabilité inconnue de trouver la conditionnelle une fois sa condition archivée, le gain
attendu est de l'ordre d'un monde sur cinq ou dix, que 20 mondes ne tranchent pas (sortie, § 10 : puissance 0,04 à 0,47 selon
l'effet) ; la garde, en coupant des demi-appels du bras 2, peut le retourner. IV-2 : le bras 3 a le même découpage et le même
coût, sans la mise à jour ; même ordre que IV-1, un peu plus petit. IV-3 : deux sessions de trois cartes sont plus diverses qu'un
appel de six (« la première carte attire les cinq autres », [RELEVÉ] § 2.1), mais six cartes d'un même appel couvrent davantage de
traits par carte ; ni l'un ni l'autre n'est attendu grand. IV-4 et IV-5 : la chaîne demande la condition, puis la première
conditionnelle, puis la seconde, chacune retenue par le juge et le test de mort, en au plus quatre tours ; le produit de ces
probabilités est petit. IV-6 : x = 0 sur 14 au pilote. IV-7 : [MR2] § 4.4 mesure 17,6 % de fausses retenues sous le modèle de
proposeurs synthétiques (estimé, non opposable ici) ; rien n'indique un écart entre bras. IV-8 : le rapport supposé d'un appel de
trois cartes à un appel de six (0,63, sortie, § 1) est juste sous le seuil de deux tiers ; la variation des coûts entre mondes
fera couper 2b dans une partie des mondes. IV-9 : la garde borne le dépassement à un demi-appel par monde.

**Ce que serait chaque issue (R3).** P1 « les demi-générations couvrent davantage » : H-iv non réfutée au crible, signe positif ;
lue avec P2 : si la mise à jour compte (2 > 3), le gain vient de l'archive mise à jour ; sinon il n'est pas distingué du
découpage. P1 « les demi-générations couvrent moins » : H-iv non réfutée au crible, signe négatif ; à dollars proches (ρ_21 dit), payer
deux fois l'entrée pour trois cartes de moins par appel **nuit** à la couverture de ce proposeur. P1 « non tranché » : rien sur
l'effet à 20 mondes ; un petit effet n'est pas exclu (crible d'un grand effet). Aucune issue n'adopte le calendrier ; une issue
positive donne un argument pour une course préenregistrée à part (N-045 point 5 : l'héritage d'une génération), non une règle.

## Métrique

Programme de mesure neuf, `mesure_crible_iv_v1.py` (nom réservé ; dérivé de `mesure_pilote_v4.py`, `676d5f37…`, et de
`course` de `monde_riche_v4.py`, `4b165847…`), lancé une seule fois sur la machine du crible.

- **Appels et cartes** : définitions de [PILOTE] (« Métrique »), telles que recopiées par [CRIBLE-III] et [CRIBLE-II] : appel
  complet, tronqué, en échec ; carte **valide** = admise au gardien, évaluable, emplacement ≤ k (k = 6 pour le bras 1, k = 3 pour
  un demi-appel), d'un appel complet ; appel **répondu** = complet avec au moins une carte valide. Les cartes refusées, au-delà de
  k, non évaluables ou d'appels tronqués comptent dans les dollars, jamais dans une couverture, et n'entrent **jamais** dans une
  chaîne. Un appel **non parti** à cause de la garde d'égalité est « coupé par la garde » : ni répondu ni en échec, compté à part.
- **Appels d'un monde** : bras 1 : g1, g2 (six cartes chacun) ; bras 2 : 1a, 1b, 2a, 2b (trois cartes) ; bras 3 : 1a (le même
  appel que celui du bras 2), 1b', 2a', 2b' (trois cartes). **Tours de chaîne** : bras 1 : après g1, après g2 ; bras 2 : après
  chacun de ses quatre demi-appels ; bras 3 : après 1a et 1b' ensemble, après 2a' et 2b' ensemble.
- **Chaîne** (un tour, sur les cartes valides du tour) : (1) juge : richesse de chaque carte contre le nul v8 de l'archive du
  bras au début du tour (`juger`, n = 400 tirages frais du monde), arrêtée au seuil log(m/α) (`log_e_arrete`), α = 0,05, **m = 48
  fixe** à tous les tours et dans tous les bras ; (2) regroupement des cartes du tour (`grouper_v2`, instances de référence
  publiques du monde) et e-valeur de groupe (`log_e_groupe`) ; (3) e-BH sur les groupes à m = 48 (`e_bh`) ; (4) représentant de
  chaque groupe promu (`representant_v3`) ; (5) test de mort de chaque représentant (`test_de_mort`, 400 épisodes frais, seuil
  0,02) ; (6) les représentants qui passent sont les **retenues** du tour et entrent dans l'archive du bras, servie à l'appel
  suivant du même bras. Code de `course` (`4b165847…`), sous un nom neuf, sans autre changement que le découpage en tours et les
  graines ; aucune vue de l'oracle, des issues ni des richesses dans un texte servi.
- **Composantes comptées et capture** : définies par [PILOTE] (« Métrique » : attribution Δ_i, seuil τ_i), telles que recopiées
  par [CRIBLE-III] : composantes **certifiées** (étiquette C8 de `verifier_v4`, latente exclue), moins l'effet de K1 et ce que K1
  servie porte à elle seule ; une loi capte la composante i si Δ_i ≥ max(0,005 ; 0,75·I_i) (oracle de 12 000 instances ; `captes`).
  **C_X(w)** = nombre de composantes comptées captées par **au moins une retenue** du bras X dans le monde w à la fin de la
  génération 2 (union des attributions de chaque retenue, comme dans `course`). K(w) = nombre de composantes comptées du monde.
- **Profondeur** : D_X(w) = 2 si la seconde conditionnelle de la chaîne est captée par une retenue du bras X ; 1 si la première
  l'est et non la seconde ; 0 sinon. **Conditionnelle captée avant sa condition** : retenue qui capte une conditionnelle alors que
  sa composante de condition n'est captée par aucune retenue antérieure ni par la même (rapporté, [MR2] § 6).
- **Écarts** : δ_XY = moyenne, sur les mondes complets pour la comparaison X–Y, de C_X(w) − C_Y(w). Statistiques de P1 et P2 :
  δ_21 et δ_23 ; secondaires : δ_31 ; écarts de D.
- **Test** : test exact des rangs signés de Wilcoxon par permutation des signes (2^n permutations, n ≤ 20), écarts nuls retirés,
  rangs moyens aux égalités, bilatéral ; au moins 7 écarts non nuls tous du même signe sont nécessaires pour un p ≤ 0,025, au
  moins 6 pour 0,05 (sortie, § 9). **Intervalles** rapportés : rééchantillonnage apparié des mondes complets, 10 000 rééchantillons,
  percentile, 97,5 % pour P1 et P2, 95 % ailleurs ; **ils ne décident pas** (le test décide, forme de [CRIBLE-II]).
- **Couverture des cartes brutes** (oracle sur les cartes, mesure du pilote ; N-058) : B_X(w) = composantes comptées portées par au
  moins une carte **valide** du bras X, retenue ou non ; rapportée à côté de C_X, sans verdict.
- **Copies de l'archive** : part des cartes valides de chaque bras dont la distance de regroupement (même distance et mêmes ε que
  `grouper_v2`) à une loi de l'archive servie à leur appel est sous le seuil de regroupement ; part de ces copies **refusées** par
  la chaîne. **Quasi-doublons d'un tour** : part des cartes valides d'un tour dans un groupe de taille ≥ 2.
- **Fausses retenues** : retenue dont le gain selon l'oracle au-delà de l'enveloppe de l'archive du tour est sous 0,02
  (`SEUIL_ORACLE`, forme de `course`) ; part par bras.
- **Apport par tour** : composantes comptées captées pour la première fois au tour t du bras X ; somme sur les mondes, par tour et
  par bras ; rapporté sans verdict.
- **Dollars** (prix publics en principal, R-2977 ; pour Pr-2 le prix public est égal au prix de la configuration v12, 4 / 20 USD
  par million de jetons d'entrée / de sortie, [CRIBLE-V], table des proposeurs : la sensibilité « prix de la configuration » est
  vide, rapportée comme telle) : $_X(w) = somme des appels du bras X dans le monde w (le coût de 1a compte dans les bras 2 et 3) ;
  **R_X** = Σ_w C_X(w) / Σ_w $_X(w), rapporté ; **ρ_21 = $_2 / $_1** et ρ_23 (IV-9). Machine et chaîne (processeur) à part.
- **Appels coupés par la garde** : par bras, par rang (1b, 2a, 2b ; 1b', 2a', 2b') et par monde.
- **Sensibilités, rapportées sans verdict** : τ' = 0,25·I ; toutes les composantes ; mondes non complets réintégrés bras par bras
  (C = archive du bras au dernier tour joué) ; δ_21 et δ_23 sans les mondes où la garde a coupé un demi-appel ; B_X à la place de
  C_X. **Rapportés aussi** : appels répondus, tronqués, en échec, coupés, par rang et par bras ; retenues par tour ; octets servis
  par appel ; durée de chaque tour de chaîne ; jetons et dollars par rang. Pertes et couvertures **par classe sommées sur les
  mondes**, jamais monde par monde dans un texte public. Information sur un calendrier, jamais un classement de proposeurs
  (N-058). Aucune moyenne ni médiane sur des jetons dans une sonde (il n'y en a pas).

## Seuil

- **Nombre de mondes : N = 20** ([NOTE] § 3 (iv) ; même règle que les autres cribles, R-2992 ; aucune branche à 24 mondes).
- **Mondes complets, par comparaison principale** : un monde est complet pour P1 si tous les appels **partis** des bras 1 et 2
  sont répondus (au plus 6 appels) et si tous leurs tours de chaîne ont fini sous la borne B_c sans erreur ; pour P2, de même pour
  les bras 2 et 3 (au plus 7 appels, 1a compris une fois). Un appel **coupé par la garde** ne rend pas un monde incomplet (il est
  le dessin). **Minimum** : n ≥ 16 mondes complets pour la comparaison ; sinon cette principale est « non concluante ». Taux de
  réussite par appel de Pr-2 au pilote : 4 répondus sur 4 ([VERDICT-PC]), information seulement. Probabilité d'atteindre le minimum
  (indépendance supposée, sortie, § 11) : à p = 0,99 par appel, 0,99 pour P1 comme pour P2 ; 0,98 : 0,93 et 0,89 ; 0,97 : 0,77 et
  0,66 ; 0,95 : 0,36 et 0,23.
- **Zone utile** : au moins 10 mondes complets pour P1 où l'un des bras capte au moins une composante comptée **et** l'un des bras
  en capte moins que K(w) ; sinon « hors de la zone utile » (aucune place pour un écart).
- **Garde et taille** : réserve « **demi-générations amputées** » si la garde a coupé au moins un demi-appel du bras 2 dans plus de
  10 mondes complets pour P1 ; réserve « **textes refusés par la taille** » si un appel a été refusé par la règle de taille dans
  plus de 2 mondes.
- **P1** : « **les demi-générations couvrent davantage** » si p ≤ 0,025 (bilatéral) et la somme des rangs signés de δ_21 est
  positive ; « **les demi-générations couvrent moins** » si p ≤ 0,025 et elle est négative ; sinon « **non tranché** » (en
  particulier avec moins de 7 écarts non nuls).
- **P2** : « **la mise à jour compte** » si p ≤ 0,025 et le signe est positif ; « **la mise à jour nuit** » si p ≤ 0,025 et il est
  négatif ; sinon « **non tranché** ».
- **Secondaires** (5 %, sans correction) : δ_31 : « effet du seul découpage » (signe dit) ou « non distingué » ; profondeur :
  écarts de D_2 − D_1 et D_2 − D_3 (rangs signés) ; première conditionnelle captée : test exact de McNemar, bras 2 contre bras 1 et
  contre bras 3.

## Plan d'analyse

### Proposeurs (configuration v12 du pilote, inchangée ; variante « crédits de Claude au maximum »)

| poste | clé de configuration | crédits | rôle ici | attendu par appel de six cartes (moyenne du pilote ; [NOTE] § 1 entre parenthèses) | plafond de session (bloc gelé) | borne de sortie | prix de la configuration (entrée / sortie) |
|---|---|---|---|---|---|---|---|
| Pr-2 | `opus55` | crédits de Claude | toutes les places des trois bras (180 appels) | 0,264334 (0,80) ; appel de trois cartes non mesuré | 2,00 | 89 000 | 4 / 20 (public : 4 / 20) |

Identités : celles de la configuration v12 (`f69503dd…`, bloc gelé de [PILOTE], à travers [CRIBLE-III], [CRIBLE-V] et
[CRIBLE-II]) ; aucun identifiant de modèle ici (R-2598), hors la clé de configuration `opus55`, que le bloc gelé et les lignes de
GO exigent (R-2690, forme de [CRIBLE-III] et de [CRIBLE-II]). Réglages : ceux du bloc gelé (effort « high », réflexion comprise
dans la sortie, aucun compte séparé). Pr-1, Pr-3 et Pr-4 ne servent pas. **Un seul fournisseur** porte les 180 appels : toute
coupure ou toute limite de débit touche tout le crible (liste d'arrêt, ligne « limite de débit » ; essai à blanc à cinq files).

### Gabarits

- **G6** (bras 1) : celui du pilote (`e77d3041…`, [CRIBLE-III]) : épisodes de développement, archive, grammaire servie, « au plus
  3 conditions emboîtées », rien sur les conditions ni sur les sortes d'effets (R-2504) ; **avec E épisodes servis**, E fixé par la
  règle de taille ci-dessous (E = 400 au pilote ; si E < 400, dit, et le même E sert aux trois bras) ; archive servie : K1 à la
  génération 1, K1 et les retenues de la génération 1 à la génération 2, sous la forme où le pilote sert K1 (le pilote n'a servi
  que {K1} : servir une archive plus longue par la même section est **à vérifier au code**, « Choix et doutes », point 4).
- **G3** (bras 2 et 3) : G6 à l'identique, sauf la consigne « six cartes au plus » remplacée par « **trois** cartes au plus » ; aucun
  mot sur les demi-générations, la mise à jour, les autres sessions, le juge, ni sur ce que l'archive couvre. Rédaction exacte figée
  au code, empreinte gelée, à contre-lire. Les textes de 1a (bras 2) et de 1a (bras 3) sont **le même texte** : un seul appel.
- Égalité des vues : à archive égale, un texte de G3 et un texte de G6 ne diffèrent que par ce mot ; le bras 2 voit à 1b, 2a et 2b
  une archive qui a bougé depuis le début de la génération, le bras 3 non (c'est la seule différence entre eux).

### Règle de taille (texte servi)

Sous la configuration v12, le code refuse avant l'appel tout texte dont le pire cas compté ((octets + 1 024) × prix d'entrée +
borne × prix de sortie) dépasse le plafond de session : pour Pr-2, **53 976 octets** au plus (sortie, § 2) ; la liste d'arrêt
arrête au-delà de 53 000 octets ([CRIBLE-II]). Le texte du pilote en prend jusqu'à 52 000 ([CRIBLE-III], « Devis ») ; sa taille
réelle n'est pas dans [VERDICT-PC]. L'archive servie grandit : au plus K1 et 6 retenues pour un appel de génération 2 des bras 1
et 3 et pour 2a, **K1 et 9 retenues** pour 2b (sortie, § 2). **Règle écrite d'avance** (forme de [CRIBLE-II]) :
1. **Partie A** (processeur seul) : |G6(E)| et |G3(E)| à archive {K1}, sur les 12 mondes de développement de [MR2], pour
   E ∈ {400, 350, 300, 250, 200} ; maximum sur les 12 mondes : M(E).
2. **Sonde des gabarits** (obligatoire, ligne propre, étape 2) : c_max = plus grande taille canonique d'une loi valide des trois
   appels de six cartes de la sonde.
3. **E** = la plus grande valeur de {400, 350, 300, 250, 200} telle que M(E) + 9 × 1,25 × c_max ≤ 52 000 octets ; si aucune ne
   convient : « **non lançable sous la configuration v12** », nœud de la mère ; E est inscrit dans la version qui fera foi, avant
   tout appel du crible.
4. **À l'exécution**, une loi de l'archive n'est **jamais** retirée (elle est le contenu même du dessin) : si un texte dépasse
   encore 53 000 octets, l'appel n'est **pas fait**, il est compté « refusé par la taille », et le bras s'arrête dans ce monde
   (monde incomplet pour les comparaisons de ce bras ; réserve de la section « Seuil »).

### Mondes à chaîne de profondeur 2

[NOTE] demande « 20 mondes MR-2 portant une chaîne de profondeur 2 ». Le générateur tire **une ou deux** conditionnelles
uniformément (`tirer_gabarit_v4`, `n_xor` dans {1, 2}), puis rejette les gabarits hors contraintes ; dans les 12 mondes de
développement, **2 sur 12** ont une chaîne ([MR2] § 4.1). **Règle** : générateur sous un nom neuf, `generer_monde_v4_chaine`,
identique à `generer_monde_v4` sauf `n_xor = 2` imposé ; mêmes contraintes du gabarit (au plus 10 composantes, au plus 6 traits
portant un effet, au plus 3 conditions de seuil), même vérificateur `verifier_v4` (toute conditionnelle certifiée, C8 à m = 48),
même règle des 8 tirages au plus par monde. C'est une **sélection de mondes** de plus, déclarée comme C5, C6 et la certification
des conditionnelles ([MR2] § 7) ; les fréquences des autres sortes en sont déformées (mesurées à la partie A, publiques avec le
générateur, Q-10 (a)). Alternative : tirer par `generer_v4` et garder les mondes à deux conditionnelles (plus fidèle au
générateur, mais ≈ 6 fois plus de mondes à vérifier : « Choix et doutes », point 6).

### Chaîne entre les demi-générations

Telle que définie en « Métrique », sur la machine, entre deux appels d'un même bras. **Borne par tour de chaîne B_c** : le plus
petit multiple de 300 s au moins égal à 1,5 fois le plus long tour mesuré à la partie A (archive de K1 et 9 lois, six cartes
scriptées), **au plus 600 s** ; au-delà, « non lançable », nœud de la mère (sortie, § 6 : à cinq files, B_c = 900 s porterait la
garde de départ à 14 h). Un tour qui dépasse B_c est arrêté ; le bras s'arrête dans ce monde (monde incomplet) ; compté. Une
exception de la chaîne arrête le crible (liste d'arrêt) : **aucun repli silencieux** (R5). Au plus quatre tours de chaîne à la
fois sur la machine (un par processeur ; la machine du pilote en a quatre selon [CRIBLE-V]) ; l'attente compte dans la minuterie,
non dans B_c.

### Garde d'égalité de dollars

**Règle de [NOTE]** (« bras 2 et 3 plafonnés au coût mesuré du bras 1, monde par monde ») écrite sous sa forme souple : dans le
monde w, le bras 1 est joué **en entier d'abord** (g1, chaîne, g2, chaîne) ; $_1(w) = sa dépense (prix publics, journal du
relais) ; puis un appel des bras 2 ou 3 ne **part** que si la dépense déjà faite de ce bras dans ce monde (1a compris dans les
deux) est **strictement inférieure** à $_1(w). Le dépassement est donc borné par un appel (plafond de session 2,00). Si le bras 1
n'est pas complet dans w, $_1(w) est remplacé par la valeur écrite 2 × 0,264334 = 0,528668 USD (deux appels moyens du pilote),
pour que les bras 2 et 3 restent jouables pour P2. **Conséquence chiffrée** (sortie, § 4, coûts pris à leur moyenne) : avec c3 le
coût d'un appel de trois cartes et c6 celui d'un appel de six, 2a part si c3 < c6, 2b part si c3 < (2/3)·c6 ; au rapport supposé
0,63, les quatre demi-appels partent et ρ_21 ≈ 1,26 ; à 0,67 ou plus, 2b est coupé ; à 1, toute la génération 2 des bras 2 et 3
l'est. **Règle d'avance d'après la sonde** : si le coût du quatrième appel de la sonde (trois cartes, archive de K1 et 9 lois) est
au moins les deux tiers de la moyenne des sept appels de six cartes connus (quatre au pilote, trois à la sonde), le crible est
« **non lançable sous la garde par monde** » : nœud de la mère, options du point 3 de « Choix et doutes ».

### Partie A — processeur seul, avant tout appel (descriptive)

Sur les 12 mondes de développement de [MR2] (régénérés à leurs graines publiques, empreintes contrôlées) et sur 12 graines de
développement neuves du générateur à chaîne (`cle("monde-crible-iv-developpement", r)`, r = 0 à 11) : (A1) taux de conformité,
refus par contrôle, durée par monde du générateur à chaîne ; (A2) tailles |G6(E)| et |G3(E)| (constructeur du texte du code du
pilote, copie gelée, nom neuf) ; (A3) durée d'un tour de chaîne avec une archive de K1 et 9 lois et six cartes scriptées par le
modèle de proposeurs synthétiques de [MR2] (aucun appel), pour B_c ; (A4) essai à blanc de la chaîne en demi-générations, des
trois bras et de la garde avec proposeurs scriptés (mode à blanc de `a_blanc_v59`, `606aa8b4…`, de la copie du code `94bfd92`,
à travers [NOTE] § 3 (iv)). Rapporté sans critère ; sert les règles de taille et de B_c et le choix du point 6. **Quand la machine
n'est plus chargée** (charge relevée à 11 à l'écriture de ce texte, `uptime`, quatre processeurs) : jamais pendant un
chronométrage d'une autre session.

### Partie B — le crible

- **Mondes** : 20 mondes du générateur à chaîne, du **secret du crible**, procédure de la machine comme [PROC-14] (secret engagé et
  poussé, phrase de Lazar, mondes et empreintes inscrits avant tout appel) ; jamais publiés, jamais réutilisés, jamais hors de la
  machine ; **séparés** de ceux des autres cribles (forme de R-2977 : pas de témoin commun ; [NOTE] § 4 le proposait, non retenu).
- **Files** : cinq files de quatre mondes (le monde r va à la file r modulo 5, dans l'ordre croissant de r, fixé avant tout appel) ;
  dans une file, les mondes l'un après l'autre ; dans un monde : bras 1 (g1, chaîne, g2, chaîne), **puis** bras 2 et bras 3 :
  1a ; puis, en parallèle, la suite du bras 2 (chaîne de 1a, 1b, chaîne, 2a, chaîne, 2b, chaîne) et celle du bras 3 (1b' ;
  chaîne sur 1a et 1b' ; 2a' puis 2b', joués **l'un après l'autre** avec la garde jugée avant chacun, exactement comme 2a et 2b au bras 2 (la dépense ne décroît pas : un 2a' coupé coupe 2b'), puis chaîne sur les cartes de 2a' et 2b' ensemble). Au plus 10 sessions à la fois.
- **Règle d'abandon par bras** : un appel non répondu (tronqué, en échec, refusé par la taille) ou un tour de chaîne au-delà de B_c
  arrête ce bras dans ce monde (aucune dépense de plus pour ce bras ; monde incomplet pour ses comparaisons) ; 1a non répondu
  arrête les bras 2 et 3 dans ce monde.
- **Appels** : au plus 9 par monde, 180 en tout (tous de Pr-2, sur crédits de Claude), moins les appels coupés par la garde ou
  abandonnés ; aucune reprise, aucune bascule ; réponses brutes et témoins d'isolement scellés avant extraction ; empreinte de
  chaque texte servi au journal ; `CARTES.json`, `ARCHIVES.json` (archive de chaque bras à chaque tour) et `CHAINE.json`
  (richesses, groupes, promues, tests de mort, retenues, durées, par tour) scellés.
- **Mesure** : `mesure_crible_iv_v1.py`, une seule fois, sur la machine ; sortie scellée avant toute lecture, sans devis de monde ;
  rapatriement comme [PROC-14] § 9 (jamais les mondes) ; réponses brutes sur une branche de travail, jamais sur `main` (R-2731).

### Graines (R9)

Racine : l'entier de l'empreinte sha256 du texte qui fera foi. `numpy.random.SeedSequence(entropy=racine, spawn_key=…)`, numpy
≥ 1.25 : juge, carte i du tour t du bras b dans le monde r `(r, 60, b, t, i)` ; test de mort `(r, 61, b, t, i)` ; instances de
référence du regroupement, communes aux trois bras `(r, 62)` (1 500 instances, comme `course`) ; copies de l'archive, mêmes
instances ; rééchantillonnage `(99, k)` ; essais et mutations `(97, k)`, liste à l'addendum. **Graine du monde r** : fonction
`graine_monde_pilote` de [PILOTE] avec l'étiquette neuve « crible-iv-v1 » (secret du crible, phrase de Lazar, empreinte du texte
scellé, r) ; tirages de `generer_monde_v4_chaine` sous la règle des 8 tirages de `generer_v4` ; épisodes de développement : règle
du bloc gelé, étiquette « crible-iv-v1 », les E premiers servis ; oracle `cle("oracle-crible-iv", empreinte du devis du monde)`.
Manifeste du run : `src/controle_ia/manifeste.py`.

### Étapes

0. **Code** sous des noms neufs : générateur à chaîne ; lanceur du crible (dérivé du lanceur v74 du pilote : files, ordre bras 1
   puis bras 2 et 3, appel commun, garde, règle d'abandon, règle de taille) ; gabarit G3 ; chaîne en tours (dérivée de `course`) ;
   `mesure_crible_iv_v1.py`, `lire_crible_iv_v1.py` (lecture gelée), programmes de la partie A. **Essais** : cas sain et artefact
   pour chaque ligne de la liste d'arrêt (R5) ; chaîne éprouvée sur des cas écrits à la main (carte refusée, carte au-delà de k,
   appel tronqué, tour sans carte, groupe de copies de l'archive, test de mort refusé, archive de K1 et 9 lois). **Banc de
   mutations**, au moins : une carte non valide dans une chaîne ; une carte refusée servie dans l'archive ; une promue non testée
   entrée dans l'archive ; une richesse, un groupe ou un verdict servi dans un texte ; l'archive du bras 2 servie au bras 3 ; mise à
   jour du bras 3 à mi-génération ; m pris égal au nombre de cartes du tour ; oracle lu par le juge ou par le test de mort ; mêmes
   épisodes pour le juge et le test de mort ; appel du bras 2 parti avant la fin du bras 1 ; appel parti alors que la dépense du
   bras atteint $_1(w) ; 1a joué deux fois ; coût de 1a compté dans un seul bras ; carte refusée comptée dans une couverture ;
   effet de K1 compté ; seuil à 0,05 au lieu de 0,025 pour les principales ; rangs moyens remplacés par des rangs ordinaires ; monde
   à une seule conditionnelle accepté. Toutes tuées pour la raison attendue. Contre-lecture du code par un sous-agent neuf d'un autre
   modèle ; addendum d'empreintes scellé.
1. **Partie A** sur processeur (quand la charge le permet), sorties scellées, lues sans critère ; B_c fixé.
2. **Sonde des gabarits** (obligatoire : la règle de taille et la garde en dépendent ; sur devis et ligne propre) : sur un monde de
   développement à graine publique, trois appels de Pr-2 sous G6 (E = 400, archive {K1}), puis E fixé par la règle, puis un appel
   de Pr-2 sous G3 portant une archive de K1 et des **9 lois valides les plus longues** des trois premiers appels (épreuve de
   taille et de forme, hors de toute chaîne) ; vérifie l'extraction, la taille servie, la forme des cartes d'un appel de trois, les
   jetons et le coût c3 ; ne lit aucune couverture. **Règles d'avance** : le quatrième appel tronqué, ou sans carte valide, ou refusé
   par la règle du pire cas → G3 réécrit, nouvelle sonde sur nouvelle ligne, crible non lancé ; aucune valeur de E possible → « non
   lançable », nœud de la mère ; c3 au moins les deux tiers de c6 → « non lançable sous la garde par monde », nœud de la mère ;
   sinon les jetons lus refont l'attendu (section « Devis », règle de mise à jour).
3. **Avant toute dépense du crible** : version qui fera foi (E, B_c, devis refait sur la sonde, puissance), contre-lue, scellée par
   `sceller_prereg`, recopiée sous `prereg/` ; lignes « calcul » inscrites par la mère.
4. **Machine** (procédure dérivée de [PROC-14], noms neufs, trois barrières), génération des 20 mondes, essai à blanc avec
   proposeurs scriptés et vraies pièces servies (cinq files, appel commun, chaîne, garde), puis les appels.
5. **Mesure** une seule fois, sortie scellée, rapatriement, destruction par identifiant (R10), preuve d'absence.
6. **Lecture** gelée, puis sous-agent neuf (R13) ; audit de symétrie (R4) écrit avant le prononcé ; rapport ; **aucune adoption**.

### Comparaisons et corrections

Deux principales, P1 (δ_21) et P2 (δ_23), bilatérales à 0,025 chacune (Bonferroni). Secondaires à 0,05, sans correction : δ_31 ;
profondeur (D_2 − D_1, D_2 − D_3) ; première conditionnelle captée (McNemar) ; copies, fausses retenues, apport par tour ; ρ_21,
ρ_23 ; B_X. Tout est apparié par monde. Les bras 2 et 3 partagent 1a : les cartes de 1a sont les mêmes dans les deux bras, mais leurs retenues peuvent différer (la chaîne du bras 2 juge 1a seule, celle du bras 3 la juge avec 1b', tirages propres à chaque bras) : une composante portée par les cartes de 1a peut être captée dans un bras et non dans l'autre, au tour 1a pour le bras 2, au premier tour pour le bras 3 ; dit. Les trois bras
partagent le monde, K1 et les instances de référence ; leurs tirages du juge et du test de mort sont propres à chaque bras.

### Taille

20 mondes ([NOTE] : puissance 0,80 pour une part passant de 0,05 à 0,40 à 20 mondes, test de Fisher, annexe A de [NOTE] ; ce n'est
pas la statistique de ce texte). **Puissance de P1 et de P2** dans un modèle simple (écarts de 0 ou ± 1 composante par monde, test
des signes, auquel le test des rangs signés se réduit quand tous les écarts non nuls valent ± 1 ; 20 mondes complets ; bilatéral
0,025 ; sortie, § 10) : 0,04 si 20 % des mondes gagnent une composante et 5 % en perdent ; 0,11 à 30 % et 10 % ; 0,27 à 40 % et
10 % ; 0,47 à 50 % et 10 % ; 0,33 à 35 % et 5 %. **Crible d'un grand effet** : un « non tranché » ne dit rien d'un petit effet ;
c'est l'issue la plus probable et celle que prédisent IV-1 et IV-2. La puissance sous un modèle plus fin (écarts de 0 à ± 3,
rangs moyens, garde comprise) se recalculera, avant le scellement, par simulation sur processeur sous le modèle de proposeurs
synthétiques de [MR2] (programme sous un nom neuf, scellé avant son lancement ; graines `(96, s)` ; aucune donnée de crible), quand
la machine n'est plus chargée ; elle ne change ni N ni aucun seuil.

## Critères de lecture gelés

Lecture dans cet ordre ; un étage 0 ou 3 arrête la lecture ; l'étage 1 arrête la lecture de la principale qu'il touche.

| étage | observé | verdict |
|---|---|---|
| 0 | une ligne d'arrêt déclenchée, **sauf** la ligne « mondes complets atteignables < 16 », dont l'issue est celle de l'étage 1 ; la mesure en erreur | « **non jugeable (arrêt)** » : aucune issue lue |
| 1 | n < 16 mondes complets pour P1 (resp. P2) | P1 (resp. P2) « **non concluant** » ; causes rapportées ; l'autre principale est lue si elle a ses 16 mondes |
| 2 | réserve « demi-générations amputées » ; réserve « textes refusés par la taille » ; 3 appels tronqués ou plus dans un même bras | P1 et P2 lus et rapportés **sous la réserve nommée** ; sous « demi-générations amputées », δ_21 et δ_23 sans les mondes amputés sont lus avec le principal, et si l'issue de P1 diffère, elle est qualifiée « sensible à la garde » et rien de plus n'en est conclu ; la phrase « les demi-générations couvrent moins » est alors interdite sans le complément « à dollars proches (ρ_21 dit), avec une génération 2 amputée dans k mondes » |
| 3 | zone utile manquée | « **hors de la zone utile** » |
| 4 | P1 | « les demi-générations couvrent davantage » / « les demi-générations couvrent moins » / « non tranché » ; l'une ou l'autre des deux premières phrases est **toujours** suivie de « ρ_21 = … : le bras 2 a dépensé ρ_21 fois le bras 1 (garde souple, dépassement borné par un appel) » ; sans ce complément elle est interdite |
| 5 | P2 | « la mise à jour compte » / « la mise à jour nuit » / « non tranché » |
| 6 | δ_31 | « effet du seul découpage » (signe dit) / « non distingué » |
| 7 | profondeur, conditionnelles, copies, fausses retenues, apport par tour, couverture brute, sensibilités, coûts, appels coupés | rapportés, sans verdict |

**Lecture de H-iv et de la question de [NOTE].** [NOTE] demande si deux demi-générations « couvrent davantage de composantes, et de
chaînes de profondeur 2, à dollars égaux », et dit que « le placebo sépare la mise à jour du simple découpage ». Traduction gelée
ici, sans équivalence statistique (20 mondes ne la permettent pas) :
- étage 4 « davantage » et étage 5 « compte » : « **les demi-générations couvrent davantage, par la mise à jour de l'archive** » ;
- étage 4 « davantage » et étage 5 « non tranché » : « **les demi-générations couvrent davantage, mise à jour non distinguée du
  découpage** », lue avec l'étage 6 ; si l'étage 6 donne « effet du seul découpage » positif : « **effet du découpage** » ;
- étage 4 « moins » : « **les demi-générations couvrent moins, à dollars proches (ρ_21 dit)** », qualifié par les étages 5 et 6 (sauf étage 5 « la mise à jour compte », traité au dernier point) ;
- étage 4 « non tranché » : « non tranchée » ; les étages 5 et 6 sont rapportés, sans conclusion sur H-iv ;
- étage 4 « davantage » avec étage 5 « la mise à jour nuit », ou étage 4 « moins » avec étage 5 « la mise à jour compte » (signes contraires, **seuls cas de ce point** ; le troisième point ne s'applique pas au second) : « **lecture croisée** », l'ordre observé des trois bras (C_1, C_2, C_3) et δ_31 rapportés sans conclusion sur H-iv.
La **profondeur** (« chaînes de profondeur 2 ») n'a pas de verdict propre : elle est rapportée (étage 7) ; IV-5 prédit qu'elle
sera presque toujours nulle. Aucun proposeur d'une autre maison n'est mesuré : toute lecture porte sur les sessions d'un seul
proposeur. **Rien n'est adopté** : un calendrier en demi-générations dans l'organisme est un dessin neuf et un nœud de Lazar
(l. 339 ; N-045 point 5 ; N-058) ; le test de mort mécanique n'est pas celui de la boucle réelle.

**Audit de symétrie (R4)**, écrit avant le prononcé pour toute issue : textes servis de 1b' et de 1a égaux à l'octet ; textes de
2a' et 2b' égaux ; textes de G3 et G6 égaux hors du mot « trois » / « six » à archive égale ; archives reconstruites depuis
`CHAINE.json` (chaque loi de l'archive est une retenue du même bras) ; chaîne rejouée sur processeur sur trois mondes (graine
dérivée de l'empreinte de `CARTES.json`) depuis les cartes brutes scellées ; garde rejouée depuis les journaux du relais (aucun
appel parti avec une dépense ≥ $_1(w)) ; attribution relue sur trois retenues par bras et par monde ; dollars rapprochés des
journaux du relais. **« Trop propre »** : |δ_21| ≥ 2 ; seconde conditionnelle captée dans 3 mondes ou plus ; toutes les
prédictions vraies. **« Tout négatif »** : un bras sans aucune retenue dans plus de 10 mondes ; archives égales dans les trois bras
dans tous les mondes ; garde coupant toute la génération 2 du bras 2 dans plus de 10 mondes. Même relecture écrite, par un
sous-agent neuf.

## Liste d'arrêt

Chaque ligne a son essai sain et son artefact, écrits et passés avant l'addendum d'empreintes (R5) ; aucun repli silencieux.

| condition | action | essai sain | artefact |
|---|---|---|---|
| empreinte différente : texte, monde, gabarit G6 ou G3, configuration, programme, module importé ; texte servi de plus de 53 000 octets | arrêt avant tout appel (avant cet appel pour la taille, qui n'est pas fait ; règle de taille, point 4) | pièces conformes | un octet changé dans G3 : refus nommé ; un texte de 53 001 octets : appel non fait, compté |
| configuration autre que v12 | arrêt avant tout appel | v12 acceptée | borne de Pr-2 changée : refus |
| relevé de la sonde v74 (configuration v12, déjà jouée) absent, invalide ou d'une autre configuration | refus avant tout dossier | relevé conforme | relevé d'une autre configuration : refus |
| relevé de la sonde des gabarits du crible absent, ou E ou B_c non inscrits dans le texte qui fera foi | refus avant tout dossier | relevé, E et B_c présents | B_c absent : refus |
| monde sans tirage conforme en 8 ; monde à moins de deux conditionnelles ; seconde conditionnelle non chaînée sur la première ; C-16 ou C-17 en défaut | arrêt avant tout appel | mondes conformes | monde à une conditionnelle forcé : arrêt |
| appel d'un bras 2 ou 3 parti avant la fin du bras 1 du même monde | arrêt ; défaut | ordre tenu | 1b lancé pendant g2 : refus |
| appel d'un bras 2 ou 3 parti alors que la dépense déjà faite du bras dans ce monde atteint $_1(w) (ou 0,528668 si le bras 1 est incomplet) | arrêt ; défaut | garde tenue | 2b lancé à dépense égale : refus |
| texte servi contenant autre chose que G3 ou G6, les épisodes et l'archive du bras (une carte non retenue, une richesse, un groupe, un verdict, une loi d'un autre bras) | arrêt avant cet appel | texte égal | une carte refusée de 1a dans l'archive de 1b : arrêt |
| archive du bras 3 changée entre 1a et 1b' ou entre 2a' et 2b' | arrêt avant cet appel | archive gelée | retenue de 1a servie à 1b' : arrêt |
| chaîne : m ≠ 48, α ≠ 0,05, n ≠ 400, seuil du test de mort ≠ 0,02, oracle ou issues du monde lus hors des tirages frais, mêmes épisodes pour le juge et le test de mort | arrêt ; défaut | chaîne conforme | m = 3 forcé : refus |
| exception d'un tour de chaîne (pas un refus nommé) | arrêt (A) du crible ; rien n'est lu ; correction sous un nom neuf, contre-lue, scellée | chaîne conforme | division par zéro forcée : arrêt |
| tour de chaîne au-delà de B_c | tour arrêté ; bras arrêté dans ce monde ; compté | tour de 30 s | tour scripté de B_c + 1 s : arrêté |
| appel non répondu | bras arrêté dans ce monde (1a : bras 2 et 3) ; compté | appel répondu | 1a tronqué : aucun appel de plus des bras 2 et 3, compte juste |
| réponse brute ou témoin d'isolement absent | arrêt (code 3), pièces versées | pièces présentes | témoin supprimé : arrêt |
| coût d'un appel au-dessus de son pire cas (plafond de session, 2,00) | arrêt (code 3), dépense comptée | coût sous le pire | relevé gonflé : arrêt |
| dépense du relais atteignant sa part (`opus55` 240 pour le crible, 8 pour la sonde ; machine 3 USD) | arrêt ; jamais de ligne d'extension | part non atteinte | part atteinte en essai : arrêt |
| mondes complets obtenus + mondes en cours + mondes non commencés < 16 **pour P1 et pour P2 à la fois**, quelle qu'en soit la cause ; évalué à chaque fin de monde ; à l'instant 0 : 20 | arrêt du crible ; « non concluant » ; dépense restante épargnée | démarrage : continue ; panne d'un appel : continue | 1a tronqué dans 5 mondes : arrêt |
| couverture comptant une carte non retenue, une carte refusée, tronquée, au-delà de k, ou l'effet de K1 | arrêt ; défaut | retenues seules | carte non retenue injectée : refus |
| exception de la mesure (pas un refus nommé) | rien n'est lu ; correction sous un nom neuf, contre-lue, scellée ; mêmes entrées | mesure conforme | division par zéro forcée : arrêt sans sortie |
| lecture avant le scellement de la sortie ; mesure lancée deux fois | run invalide | une sortie scellée | seconde mesure : refus |
| toute dépense sans ligne « calcul » inscrite citant GO-2026-11-15-06 | interdit | ligne présente | ligne absente : la commande refuse |
| minuterie : moins du pire cas restant (par file : mondes non commencés × 6 × (900 s + B_c)) + 2 h avant l'échéance, au départ ; ensuite, à chaque monde, moins de 6 × (900 s + B_c) + 2 h | arrêt (A) sans nouvel appel ; monde commencé fini, les autres non commencés | marge suffisante | échéance proche simulée : arrêt |
| un appel dépasse sa borne de 900 s | appel coupé, compté « en échec » ; règle d'abandon ; les autres files continuent | appel de 2 min | appel scripté de 1 000 s : coupé |
| erreurs de limite de débit sur plus de 5 % des appels du fournisseur, une fois au moins dix appels faits | arrêt (A) ; nœud de la mère, aucun repli silencieux | aucune erreur | 10 % d'erreurs scriptées : arrêt |

## Devis (brouillon 1 ; attendus sur les coûts mesurés du pilote par les règles de [CRIBLE-V] ; plafonds et part)

**Sources et règles.** Attendu par appel : moyenne arithmétique des coûts de **tous** les appels du pilote du proposeur, tels que
facturés (règle (b) de [CRIBLE-V]) : `opus55`, 1,057336 USD pour 4 appels ([VERDICT-PC], « Dépense rapprochée »), soit
**c6 = 0,264334 USD** par appel de six cartes, au prix public comme au prix de la configuration (sortie, § 1) ; fourchette par
appel non transmise ([VERDICT-PC] ne donne que les totaux par proposeur). **Appel de trois cartes** : non mesuré. **Attendu
prudent** : c3 = c6 (aucune mesure ne dit moins). **Bas** (supposé) : la part d'entrée d'un appel du pilote est prise à 52 000 octets
servis à 3 octets par jeton, soit 0,069333 USD ; la sortie déduite (0,195001) est divisée par deux : c3 = 0,166834 (rapport 0,63 ;
sortie, § 1) ; l'archive plus longue des générations 2 n'y est pas comptée (la règle de taille borne le texte). Pire cas par
appel : plafond de session du bloc gelé, 2,00 USD (règle (a), inchangé). Machine : prix horaire relu au pilote, 0,052222 USD/h
([VERDICT-PC]) ; temps de machine du pilote hors appels 2 985,9 s (sortie, § 0).

| ligne | appels | crédits | attendu prudent (tous partis, c3 = c6) | bas (c3 supposé) | plafonds × appels |
|---|---|---|---|---|---|
| Pr-2, bras 1 (g1, g2) | 40 | Claude | 10,57 | 10,57 | 80,00 |
| Pr-2, bras 2 (1a, 1b, 2a, 2b ; 1a commun compté ici) | 80 | Claude | 21,15 | 13,35 | 160,00 |
| Pr-2, bras 3 (1b', 2a', 2b') | 60 | Claude | 15,86 | 10,01 | 120,00 |
| **crédits de Claude** (crible) | 180 | | **47,58** (47,580120) | 33,93 | 360,00 ; **part du relais : 240,00** |
| machine (0,052222 USD/h relu au pilote) | — | hors | 0,09 (0,19 avec deux heures de génération de mondes) | — | 3,00 |
| sonde des gabarits, **obligatoire** (trois appels sous G6, un sous G3 à archive de K1 et 9 lois, monde de développement) | 4 | Claude | 1,06 (1,057336) | — | 8,00 |
| partie A | 0 | — | 0 | 0 | 0 |
| **avec la sonde** | 184 | | **48,64 sur crédits ; 0,09 à 0,19 hors** | 34,99 sur crédits | **251,00** (248 sur crédits, 3 hors) |

Sortie, § 5 et § 7. Si c3 = c6, la garde coupe 2a et 2b des bras 2 et 3 dans chaque monde à coûts moyens : 100 appels partent,
26,43 USD attendus (sortie, § 5) ; l'attendu prudent de 47,58 est donc un haut. **Part sur crédits de Claude** : 100 % des appels
de proposeur ; seule la machine est hors crédits (elle ne peut pas y être).

- **Le pire est borné par la part du relais, non par plafonds × appels.** Plafonds × appels : 360 USD ; borne qu'impose la garde
  (bras 1 au plus 4 USD par monde ; bras 2 et 3 au plus $_1(w) + 2 chacun) : 320 USD (sortie, § 5). Ni l'un ni l'autre ne tient dans
  l'enveloppe (sortie, § 8 : cumuls 1 383,67 et 1 343,67). **Part proposée : 240 USD** sur crédits, la forme de [NOTE] (« 80 + 80 +
  80 ») ; la ligne d'arrêt « part atteinte » arrête le crible (étage 0, « non jugeable ») si le coût moyen d'un appel atteint
  1,3333 USD, soit 5,04 fois c6 (sortie, § 5) ; au pilote, la part moyenne du plafond prise par un appel de Pr-2 était 0,13
  ([CRIBLE-II], sortie, § 1). Dit, et soumis à la mère (« Choix et doutes », point 7).
- **Écart à [NOTE]** : 180 appels au lieu de 200 (appel commun 1a : « Choix et doutes », point 2) ; Pr-2 au lieu de Pr-1
  (variante) ; 48,64 attendus avec la sonde au lieu de 30,30 (l'attendu de [NOTE] compte chaque bras 2 et 3 « plafonné au bras
  1 », 10,00 chacun ; ici l'attendu prudent compte tous les appels partis) ; 251 au pire au lieu de 243 (+ 8 de sonde) ; la garde
  stricte de [NOTE] (« plafonnés au coût mesuré du bras 1 ») ne peut pas être tenue appel par appel : le pire cas d'un appel (2,00)
  dépasse presque toujours ce qui reste sous $_1(w) ; forme souple retenue, dépassement borné par un appel.
- **Forme fidèle à [NOTE] (Pr-1, hors crédits)** — information seulement, jamais un devis : 200 appels, 24,72 attendus au prix
  public (123,58 au compte de la configuration, cinq fois le prix public, « la console fait foi », R-2803 ; [CRIBLE-V]) ;
  plafonds × appels 468 (plafond 2,34 du bloc gelé, non 2,00 : remarque de R-2977) (sortie, § 12).
- **Plafond de 0,75** ([NOTE] § 4) : sans objet (Pr-1 ne sert pas) ; non proposé pour Pr-2 (configuration neuve exigée, forme de
  [CRIBLE-II]).
- **Tronquage** (règle de [CRIBLE-III]) : non déclenchée pour Pr-2 au pilote (sortie du plus grand appel ≤ 52 867 jetons, sous
  71 200 ; [CRIBLE-II], sortie, § 2) ; un appel de trois cartes en écrit moins.
- **Durée** (sortie, § 6) : appels de `opus55` au pilote de 36,425 à 109,396 s (moyenne 68,387), joués en série ; **borne par
  appel : 900 s** (règle de [CRIBLE-V] : plus petit multiple de 300 s au moins égal à 1,5 fois le plus long appel répondu du pilote,
  430,542 s). Par monde, attendu ≈ 770 s (six appels et six tours de chaîne sur le chemin le plus long, bras 1 puis bras 2 ; tour de
  chaîne **supposé** 60 s) ; cinq files de quatre mondes : ≈ 51 min ; pire par monde 6 × (900 + B_c) s : 9 000 s à B_c = 600 s,
  **10 h par file au pire**, **garde de départ 12 h** (pire + 2 h : mesure, rapatriement, poussée), sous la minuterie de 17 h, plus
  la mise en place, la génération des 20 mondes (≈ 1 à 2 h sur quatre processeurs ; le pilote : ≈ 12 min pour 4 mondes, [CRIBLE-V])
  et les barrières. À quatre files, 12,5 h de pire et 14,5 h de garde à B_c = 600 s : non retenu. La latence sous dix sessions à la
  fois et la durée d'un tour de chaîne sur la machine ne sont pas mesurées. Temps d'agents : code, gabarit, essais,
  contre-lectures (plusieurs jours, non mesuré).

**Règle de mise à jour d'après la sonde des gabarits** (écrite d'avance) :

| chiffre de ce devis | lu à la sonde | nouvelle valeur |
|---|---|---|
| E (épisodes servis) | c_max ; M(E) de la partie A | règle de taille, point 3 ; « non lançable » et nœud de la mère si aucune valeur |
| c6 (0,264334) | coûts des trois appels sous G6, au prix public | c6 = moyenne des sept appels (quatre au pilote, trois à la sonde) |
| c3 (prudent c6 ; bas 0,166834) | coût du quatrième appel (G3, archive de K1 et 9 lois) | c3 = ce coût ; si c3 ≥ (2/3)·c6 : « non lançable sous la garde par monde », nœud de la mère |
| attendu du crible | c6, c3 | 40·c6 + 140·c3 (tous partis), et le nombre d'appels que la garde laisse à coûts moyens (sortie, § 4) |
| sortie de Pr-2 (borne 89 000) | jetons de sortie des quatre appels | si l'un dépasse 71 200 : réserve de tronquage annoncée à l'avance (étage 2) |
| N, mondes, appels, files, bornes, part | — | **inchangés** : 20 mondes, au plus 180 appels, cinq files, 900 s par appel, B_c de la partie A (≤ 600 s), part 240 |
| lignes de GO (montants) | — | attendus refaits ; montants inchangés ; cumul tenu sous 1 275 USD, sinon nœud de Lazar (R-2992, point 3) |

Aucune autre valeur ne se refait ; un calcul qui demanderait de changer un seuil ou une règle donne un brouillon nouveau, contre-lu,
non une retouche. **Points non mesurés par le pilote**, à prendre à la sonde et à la partie A : coût et jetons d'un appel de trois
cartes ; taille d'une loi sérialisée ; octets réels servis avec une archive longue ; forme des cartes d'une session qui voit une
archive de plusieurs lois ; durée d'un tour de chaîne.

## Lignes de GO proposées, non inscrites (inscription par la mère, dans l'enveloppe de GO-2026-11-15-06)

```
| GO-AAAA-MM-JJ-NN (κiv1) | AAAA-MM-JJ | calcul | Organisme d'idéation, crible (iv) « demi-générations » (l'archive mise à jour au milieu de chaque génération ; bras standard, demi-générations et placebo sans mise à jour ; deux générations ; garde d'égalité de dollars par monde), variante « crédits de Claude au maximum », part sur crédits de Claude : proposeur `opus55` (Pr-2, plafond de session 2 USD, part 240), au plus 180 appels (neuf par monde, premier demi-appel commun aux bras 2 et 3), effort « high » envoyé (bloc gelé du pilote) ; 20 mondes MR-2 à deux conditionnelles chaînées, du secret du crible, jamais publiés ni réutilisés ; archive {K1} au départ ; chaîne sur processeur (juge contre le nul v8 de l'archive, regroupement, e-BH, test de mort mécanique), aucun expérimentateur ; mesure gelée une seule fois ; conditions toutes exigées : coûts du pilote MR-2 mesurés et devis refait sur la sonde des gabarits, nombre d'épisodes servis et borne du tour de chaîne inscrits, préenregistrement du crible contre-lu et scellé, code et gabarit contre-lus et gelés, essai à blanc réussi à cinq files, mondes vérifiés et leurs empreintes inscrites ; plafond du relais égal à sa part ; coût au-dessus du pire cas = arrêt ; essayé, non adopté ; jamais de ligne d'extension ; arrêt par identifiant (R10) | 240 USD (sur crédits) | 2026-11-30 | Lazar | GO-2026-11-15-06 ; R-2851 ; R-2875 ; ce texte |
| GO-AAAA-MM-JJ-NN (κiv2) | AAAA-MM-JJ | calcul | Même crible, part hors crédits : machine jetable seule, 3 USD ; mêmes conditions que la ligne κiv1 | 3 USD | 2026-11-30 | Lazar | GO-2026-11-15-06 ; R-2851 ; R-2875 ; ce texte |
| GO-AAAA-MM-JJ-NN (κiv0, obligatoire) | AAAA-MM-JJ | calcul | Sonde des gabarits du crible (iv), sur crédits de Claude : trois appels de `opus55` sous le gabarit du pilote, puis un sous le gabarit de trois cartes avec une archive de K1 et neuf lois, sur un monde de développement à graine publique ; aucune couverture lue ; relevé versé ; une seule exécution | 8 USD (sur crédits) | 2026-11-30 | Lazar | GO-2026-11-15-06 ; ce texte |
```

Mots exigés par le lecteur gelé des lignes : à fixer avec le code (forme du pilote : « crédits de Claude », « hors crédits ») ;
montants : part du relais pour κiv1 (240, non plafonds × appels : dit), pires cas pour κiv2 et κiv0 ; attendus : κiv1 47,58 USD au
plus (33,93 au bas supposé), κiv2 0,09 à 0,19, κiv0 1,06. **Enveloppe** (R-2992, point 3 ; sortie, § 8) : aucune ligne « calcul »
de `registres/go.md` ni aucune ligne de `registres/depenses.md` ne cite GO-2026-11-15-06 à l'écriture de ce texte : **rien n'est
engagé** sous l'enveloppe ; aux textes actuels — (iii) 270 (version qui fera foi v1, sonde comprise), (v) 204,67 (version qui fera
foi v2, sonde neuve comprise), (ii) 411 ([CRIBLE-II], brouillon 1, sonde comprise), (i) 127 ([CRIBLE-I], brouillon 1) — il reste
262,33 USD pour (iv) ; **ce crible y tient** (251, cumul 1 263,67, marge 11,33 ; avec la sonde partagée avec (ii) : 245, marge
17,33). Si l'un des brouillons (i) ou (ii) monte de plus de 11,33 USD, le dernier crible inscrit n'y tiendra pas : nœud de Lazar à
ce moment. Attendus : 48,64 pour ce crible avec la sonde (au plus), contre 30,30 à [NOTE] et 247,20 pour les cinq à
GO-2026-11-15-06.

## Écarts, nœuds et ce que le crible ne décide pas

- **Appel commun 1a** (écart à [NOTE], 200 appels) : le premier demi-appel de la génération 1 a le même texte dans les bras 2 et 3 ;
  un seul appel, compté dans les deux ; 20 appels de moins, 40 USD de moins aux plafonds ; prix : les bras 2 et 3 partagent trois
  cartes (dit ; les écarts appariés n'en souffrent pas).
- **Variante « crédits de Claude au maximum »** (consigne de Lazar, l. 339 ; forme retenue par la mère pour (iii), R-2992, et par
  [CRIBLE-II]) : Pr-2 au lieu de Pr-1 ; ce qu'elle change : « Hypothèse » (dit, non tranché).
- **Garde d'égalité** : forme souple (dépassement borné par un appel) au lieu de « plafonnés au coût mesuré du bras 1 », qui ne
  peut pas être tenue appel par appel ; bras 1 joué d'abord dans chaque monde ; valeur écrite 0,528668 si le bras 1 est incomplet.
- **Pire cas par la part** : 240 sur crédits, sous plafonds × appels (360) et sous la borne de la garde (320) ; la part peut arrêter
  le crible dans un cas extrême (coût moyen ≥ 5 fois celui du pilote).
- **Chaîne** : celle de `course` de [MR2] (juge simplifié contre le nul v8 de l'archive, e-BH, représentant, test de mort
  `test_de_mort`), non la chaîne scellée de la boucle réelle ([NOTE] § 7, point 4 : écart dit) ; **m = 48** fixe (constante de la
  famille, `M_REGLE`), à chaque tour et dans chaque bras, pour que le seuil du juge par carte ne dépende pas du découpage en tours (m = 48 est le compte d'une génération complète de 24 cartes, `M_REGLE` : par tour de trois ou six cartes la règle est un peu plus prudente, et les bras 2 et 3 jouent deux tours par génération contre un : le budget d'erreur par génération n'est donc pas le même entre bras, dit) ; voir (« Choix et doutes », point 5).
- **Nul** : le v8 (« le nul de production reste le v8 », R-1779) sous la forme que porte l'outil du monde riche (`juger`), **non**
  le fichier du nul v8 du code de l'organisme, non relu par l'auteur ; équivalence à contre-lire. Le nul v9 (`7ae450df…`) et
  l'idée 1.1 (nul par morceaux limité) ne servent pas ; [NOTE] lie la question des variantes refusées comme copies au nœud R-1779 et
  à l'idée 1.1 : un « nul plus fort » changerait ce que refuse la chaîne, non la question.
- **Mondes** : sélection des mondes à deux conditionnelles chaînées, par un générateur à `n_xor = 2` imposé (déclarée).
- **[RELEVÉ] § 4.1** parle de « toute la chaîne (gardien, juge, test de mort, archive) » et du « même plafond de dollars » ; la
  sélection (e-BH, représentant) est celle de `course` ; aucun signal d'apprentissage n'est servi (N-045 point 5 : l'essai raccourcit
  le délai de l'héritage d'une génération, il ne récompense rien).
- **Dessin neuf** : calendrier en demi-générations ([NOTE] § 7, point 4) : **essayé, non adopté** (l. 339).
- **Réserve de lignée** (dite) : le rédacteur de ce texte est de la même maison que le proposeur ; la chaîne et la mesure sont des
  programmes (aucun juge modèle de langue) ; le gabarit G3, écrit dans cette maison, est contre-lu avec le code.
- **N-058** : le nombre de demi-générations est fixé d'avance, jamais piloté par les promotions ; les promotions du juge alimentent
  l'archive comme dans toute course (sélection de cartes, non d'agents) ; la comparaison des calendriers se juge sur l'oracle et le
  coût ; la couverture des cartes brutes (sans juge) est rapportée à côté. **N-044** : famille de conception MR-2 ; aucune
  conclusion hors de MR-2.
- **Ne décide pas** : la qualité des idées ; les générations au-delà de la deuxième ; un calendrier à plus de deux parts ; la chaîne
  réelle à expérimentateur ; un autre nul ; plusieurs proposeurs ; toute revendication publique (N-067).

## Antériorités à chercher (R8 : zone vierge = question)

[RELEVÉ] § 4.1 : idée « non trouvée telle quelle » dans le recoupement ni dans la synthèse (où « la profondeur au sens des chaînes
n'a presque pas été traitée ») ; parent cité par la fiche : algorithmes génétiques « à état permanent » contre « générationnels »
(« SUPPOSE »). Zone séduisante, à vérifier plus durement. À lire sur PDF empreinté avant toute phrase de nouveauté ; **aucun
chiffre** n'en est tiré ici (R7) :
- algorithmes évolutionnaires à état permanent (remplacement d'un individu à la fois) contre générationnels, et évolution
  asynchrone — **à chercher**, références non relevées par l'auteur ;
- boucles évolutives à modèles de langue où la base de programmes est mise à jour au fil de l'eau (par exemple FunSearch, Nature,
  2024 ; AlphaEvolve, 2025) — **à vérifier** ;
- voisins dans le dépôt : [CAT] C5 (Fork-and-Flush, Cai et al., arXiv 2610.07447 : trajectoires parallèles à contexte neuf qui
  héritent de l'espace de travail accumulé) ; [CAT] C6 (« Scaling Discovery Requires Forgetting », Tan et al., arXiv 2610.20563 :
  état jeté périodiquement, même dépense totale que les configurations comparées) ; [CAT] C1 (Co-Scientist) — non lus sur PDF par
  l'auteur ;
- tests multiples en ligne et par lots (taux de fausses découvertes contrôlé quand les hypothèses arrivent par vagues ; e-valeurs
  en ligne) : la chaîne en tours à m fixe en est un cas — **à chercher** ;
- CADS (arXiv 2610.24597 ; N-067, § 6 ; PDF sur une autre branche, non lu par l'auteur) pour la contribution d'un proposeur.

## Choix et doutes soumis à la mère

1. **Forme du crible** : variante « crédits de Claude au maximum » (Pr-2 partout) **recommandée** (confiance 0,6) : conforme à la
   consigne de Lazar (l. 339), à R-2992 et à [CRIBLE-II] ; tient dans l'enveloppe ; Pr-2 a répondu 4 sur 4 au pilote. Forme fidèle
   (Pr-1) : 2,1 fois moins chère au prix public mais hors crédits, compte de la configuration cinq fois plus haut, plafond de 2,34 ;
   et elle ne change rien au point 3.
2. **Appel commun 1a** : **recommandé** (confiance 0,7) ; 20 appels et 40 USD aux plafonds de moins.
3. **Garde d'égalité de dollars — nœud de faisabilité.** Options : (a) **garde souple par monde** (forme de [NOTE], dépassement
   borné par un appel ; « non lançable » si la sonde donne c3 ≥ (2/3)·c6) — **recommandée** (confiance 0,5) : c'est la question de
   [NOTE] (« à dollars égaux ») ; inconvénient : elle coupe des demi-appels du bras 2 dans une partie des mondes, et le résultat dépend
   du rapport c3/c6 propre au proposeur ; (b) **à cartes égales** (douze cartes par bras, aucune garde ; dollars rapportés, R_X et
   ρ_21 lus à côté) : les quatre demi-appels toujours joués ; inconvénient : la question devient « à cartes égales », le bras 2 paie
   ≈ 1,26 fois plus (supposé) ; (c) **garde globale** (le bras 2 plafonné à la dépense totale du bras 1 sur les 20 mondes) : moins de
   coupes ; inconvénient : les derniers mondes portent les coupes (effet d'ordre). Si la sonde déclenche « non lançable » sous (a),
   recommandation de repli : (b), confiance 0,55.
4. **Archive servie** : sous la forme où le pilote sert K1, par la même section ; à vérifier au code avant tout (le pilote n'a servi
   que {K1}) ; si le constructeur du pilote ne sert pas une archive de plusieurs lois, le gabarit est neuf pour les trois bras
   (contre-lu, et la sonde l'éprouve).
5. **Chaîne** : celle de `course` (`4b165847…`) découpée en tours, juge contre le nul v8 de l'archive (production, R-1779) ; **m = 48
   fixe** (constante de la famille) recommandé (confiance 0,55) ; alternative : m = 6 par génération (même budget par génération
   dans les trois bras, juge plus puissant), à contre-lire ; n = 400 comme `course`.
6. **Mondes à chaîne** : générateur à `n_xor = 2` imposé **recommandé** (confiance 0,6) ; alternative : rejet des mondes à une
   conditionnelle sous `generer_v4` (fidèle au générateur ; ≈ 6 fois plus de mondes à vérifier, 2 sur 12 en développement) ; la partie
   A mesure la conformité du premier.
7. **Part de 240 USD** (forme de [NOTE]) au lieu de plafonds × appels (360) : **recommandée** (confiance 0,55) ; c'est la seule forme
   qui tienne dans l'enveloppe ; la part n'arrête le crible que si le coût moyen d'un appel est ≥ 5 fois celui du pilote.
8. **Sonde partagée avec (ii)** : les trois premiers appels de la sonde de [CRIBLE-II] (G0, E = 400, monde de développement)
   donneraient c_max et c6 ; le quatrième appel seul serait propre à (iv) : pire 245 au lieu de 251 ; prix : les deux cribles
   dépendent d'une même sonde (dit dans les deux textes) ; à la mère (confiance 0,5).
9. **Cinq files, B_c ≤ 600 s, borne de 900 s par appel**, garde de départ 12 h ; au plus 10 sessions et au plus quatre tours de
   chaîne à la fois : à contre-lire.
10. **N = 20** : puissance basse (0,04 à 0,47 dans le modèle simple) ; 24 ou 30 mondes coûteraient 48 à 120 USD de plus de part,
    hors de l'enveloppe.
11. **Un seul fournisseur** pour 180 appels ; **solde de crédits de Claude** à couvrir : 248 USD au pire (48,64 attendus au plus), en
    plus des autres usages : à vérifier par la mère.
12. **Couverture par les retenues** (C_X, principale) plutôt que par les cartes brutes (B_X, rapportée) : la question de [NOTE] porte
    sur ce que la chaîne lègue ; la lecture de N-058 (oracle et coût) est tenue parce que C_X est lu par l'oracle et que la chaîne est
    la même dans les trois bras ; à contre-lire.
13. **Bras 1 incomplet** : valeur écrite 0,528668 USD pour la garde des bras 2 et 3 ; alternative : arrêter les trois bras dans ce
    monde (perd P2 pour ce monde).

## Contre-lecture

- **Contre-lecture 1** (R2, tour 1, sur le brouillon 1) — sous-agent neuf, d'un autre modèle que le rédacteur, qui n'a écrit ni
  ce texte, ni [NOTE], ni [CRIBLE-II], ni [CRIBLE-III], ni [CRIBLE-V], ni [PILOTE], ni [MR2]. Texte relu :
  `docs/notes/organisme-idees-juge-v1/cribles-v1/crible-iv-brouillon1.md`,
  `079f8599d6d78546148d89adb43227b74feae461ee0fdc4a3f3002c8c5f69f53` ; rapport :
  `docs/notes/organisme-idees-juge-v1/cribles-v1/contre-lecture-crible-iv-tour1-v1.md`,
  `e7853abe0bf6f5177307fa20af8f14d7fa06ed06bb83bc6320908a826f0e573e`. Verdict : « corrections » (3 majeures, M1 à M3 ;
  2 mineures, m1 et m2 ; 6 couples ; second tour demandé sur ce brouillon 2). Corrections appliquées le 2026-11-17T01:37:23Z (`date -u`)
  par un rédacteur neuf, d'un autre modèle que le rédacteur du brouillon 1, qui n'a écrit ni le brouillon 1 ni le rapport, au
  moyen du programme `appliquer-corrections-crible-iv-brouillon2.py` (même dossier, scellé à côté ; différentiel `diff-crible-iv-b1-vers-b2.txt`, scellé) :
  les 6 couples sont lus dans le rapport lui-même ; chaque « ancien » figure une seule fois dans le brouillon 1, sans
  chevauchement (vérifié par le programme). **Traitement**, point par point :
  - M1 (bras 3 : ordre de 2a' et 2b' non écrit, garde qui pouvait jouer autrement qu'au bras 2 ; 2a' puis 2b' joués l'un après
    l'autre, garde jugée avant chacun ; couple M1.1) : **acceptée**, telle quelle. Le chemin du bras 3 reste plus court que celui
    du bras 2 : les durées du devis ne changent pas (le rapport le dit).
  - M2 (lecture gelée : « moins » était qualifié par la dépense, « davantage » ne l'était pas ; ρ_21 accompagne toujours les deux
    phrases tranchées de l'étage 4, et « à dollars égaux » devient « à dollars proches, ρ_21 dit » dans la traduction ; couples
    M2.1 et M2.2) : **acceptée**, telle quelle.
  - M3 (traduction gelée : « étage 4 moins et étage 5 compte » tombait sous deux points, et « incohérente » n'était pas juste ;
    les deux couples de signes contraires deviennent une « lecture croisée », l'ordre des trois bras et δ_31 rapportés sans
    conclusion sur H-iv ; couple M3.1) : **acceptée**, telle quelle.
  - m1 (m = 48 fixe garde le seuil par carte, non le budget d'erreur du juge par génération ; couple m1.1) : **acceptée**, telle
    quelle.
  - m2 (les bras 2 et 3 partagent les cartes de 1a, non leurs retenues ; couple m2.1) : **acceptée**, telle quelle.
  - Remarques facultatives du rapport (section 5 : sonde et seuil des deux tiers, profondeur informative pour le seul bras 2,
    sigle « e-BH », statut) et points « Pour la session mère » (section 6) : **non appliqués**, aucune correction n'étant
    exigée ; à la mère et au tour suivant.
  - **Non corrigé par le rapport, signalé sans rien changer** (à reprendre au tour 2) : après M2, la formule « à dollars égaux »
    reste ailleurs dans le texte sans ρ_21 : au § 0, points 1 et 7 ; dans l'énoncé de H-iv ; dans la prédiction IV-1 ; dans
    « Ce que serait chaque issue » (« à dollars égaux, payer deux fois l'entrée ») ; et à l'étage 2 du tableau des critères gelés,
    dont le complément exigé reste « à dollars égaux, avec une génération 2 amputée dans k mondes » ; le titre de la section
    « Devis » garde la mention « brouillon 1 », qui nomme le devis et son programme, inchangés.
- **Contre-lecture 2** (R2, tour 2, sur le brouillon 2) — sous-agent neuf, d'un autre modèle que le rédacteur du brouillon 1
  selon l'en-tête de son rapport, qui dit n'avoir écrit aucune pièce lue. Texte relu :
  `docs/notes/organisme-idees-juge-v1/cribles-v1/crible-iv-brouillon2.md`,
  `603306b98180b33ea2c585fe8f33ad45c714a763a976819a9b53c49e563b069f` ; rapport :
  `docs/notes/organisme-idees-juge-v1/cribles-v1/contre-lecture-crible-iv-tour2-v1.md`,
  `ca94c2ca962bc82675b9996d63de484a9c8b2fc835209c466f7f921944193506`. Verdict : « corrections » (1 majeure, M1 ;
  2 mineures, m1 et m2 ; 3 couples ; la conception n'est pas en cause selon le lecteur ; un tour 3 réduit à ces trois couples
  et au différentiel). Corrections appliquées le 2026-11-17T02:00:43Z (`date -u`) par un rédacteur neuf, qui n'a écrit ni les
  brouillons 1 et 2 ni aucun des deux rapports (identité dite en conversation seulement), au moyen du programme
  `appliquer-corrections-crible-iv-brouillon3.py` (même dossier, scellé à côté ; empreinte au moment de l'écriture :
  `6900589e85ea0bf842990653c0bd1ac7842649a42e07e05cbb5bc55d14d79bd8` ; différentiel `diff-crible-iv-b2-vers-b3.txt`, scellé) :
  les 3 couples sont lus dans le rapport lui-même et recopiés sans retouche (le programme les compare aussi à une copie
  écrite en lui) ; chaque « ancien » figure une seule fois dans le brouillon 2, sans chevauchement, et aucune fois dans ce
  brouillon 3, où chaque « nouveau » figure une fois (vérifié par le programme). **Traitement**, point par point :
  - Rapport, § 2 et § 3 (fidélité des six couples du tour 1, vérifiée par programme ; passages touchés relus ; devis,
    enveloppe, durées et interdits non touchés) : constats du lecteur, aucune correction ; rien à faire.
  - M1 (étage 2 du tableau des critères de lecture gelés : sous la réserve « demi-générations amputées », le complément exigé
    de la phrase « les demi-générations couvrent moins » disait « à dollars égaux », alors que l'étage 4 exige ρ_21 et que sa
    traduction dit « à dollars proches (ρ_21 dit) », la garde souple n'assurant pas l'égalité ; couple M1.1) : **acceptée**,
    telle quelle. Les étages 2 et 4 ne demandent plus deux compléments contraires.
  - m1 (« Ce que serait chaque issue » : la lecture « moins » gardait « à dollars égaux » ; couple m1.1) : **acceptée**, telle
    quelle.
  - m2 (en-tête : la dernière phrase de la ligne du brouillon 2 ne nommait ni le statut ni la ligne du validateur, qui ont
    aussi changé ; couple m2.1) : **acceptée**, telle quelle ; la ligne du brouillon 3 nomme de même tout ce qui change.
  - Remarques facultatives (rapport, § 5) : **non appliquées**, aucune correction n'étant exigée. (1) Les autres occurrences de
    « à dollars égaux » (§ 0, points 1 et 7 ; énoncé de H-iv ; prédiction IV-1 ; citation de [NOTE] au point 3 de « Choix et
    doutes ») énoncent la question de [NOTE] et l'hypothèse visée, et la garde souple est dite au point 3 : laissées telles
    quelles, au choix de la mère. (2) « Dépassement borné par un appel » (étage 4) et « un demi-appel par monde » (raison de
    IV-9) : même sens selon le lecteur, vocabulaire non harmonisé. (3) Remarques facultatives du tour 1 (seuil de la sonde plus
    bas que la coupe, profondeur informative pour le seul bras 2, sigle « e-BH ») : toujours à la mère.
  - Rapport, § 6 (pour la session mère) : point 1 fait (ce brouillon 3, en fichier neuf) ; point 2 (aucun écart à un texte
    scellé, aucun mot de Lazar nécessaire) : pris acte ; point 3 (risques inchangés : la sonde et le rapport c3/c6, pièce « non
    lançable » à deux tiers ou plus ; la marge d'enveloppe de 11,33 USD ; l'équivalence du nul v8 à vérifier au code) :
    inchangés, rien dans ce texte.
  - Liste « Non corrigé par le rapport » de la contre-lecture 1 : l'étage 2 et « Ce que serait chaque issue » sont désormais
    corrigés (M1.1 et m1.1) ; les autres occurrences de « à dollars égaux » restent telles quelles (remarque facultative 1
    ci-dessus) ; le titre de la section « Devis » garde « brouillon 1 », qui nomme le devis et son programme, inchangés.
  - **Couples propres** (forme seulement) : titre (brouillon 3) ; ligne « Brouillon 3 » de l'en-tête ; statut ; ligne du
    validateur ; cette section (entrée « Contre-lecture 2 » et « Tour 3 à faire », à la place de « Tour 2 à faire »).
- **Tour 3 à faire** (R2) : sur ce brouillon 3, réduit (rapport du tour 2, § 6) à vérifier les trois couples M1.1, m1.1 et
  m2.1, les couples propres de forme et le différentiel, par un sous-agent neuf d'un **autre modèle** que le rédacteur du
  brouillon 1, qui n'a écrit aucun des brouillons 1 à 3, ni les rapports des tours 1 et 2, ni [NOTE], ni [CRIBLE-II], ni
  [CRIBLE-III], ni [CRIBLE-V], ni [PILOTE], ni [MR2]. **Fichiers à lui donner explicitement** : ce texte ; le brouillon 2 et le
  rapport du tour 2 (empreintes ci-dessus) ; `appliquer-corrections-crible-iv-brouillon3.py` et `diff-crible-iv-b2-vers-b3.txt` (même
  dossier) ; pour une relecture plus large, la liste du « Tour 2 à faire » du brouillon 2 (section « Contre-lecture ») vaut
  toujours. **À vérifier en priorité** : que les étages 2 et 4 du tableau des critères gelés et « Ce que serait chaque issue »
  qualifient la lecture « moins » de la même façon (« à dollars proches », ρ_21 dit) ; que les lignes « Brouillon 2 » et
  « Brouillon 3 » de l'en-tête disent exactement ce qui a changé.

## Annexe A — comptes exacts (sans donnée de crible, sans tirage, sans appel)

Programme : `devis-crible-iv-brouillon1.py` (même dossier, empreinte dans son compagnon) ; commande : `nice -n 19 python3 -I
devis-crible-iv-brouillon1.py`, le 2026-11-17 à 01:09:28 UTC (`date -u`), Python 3.13.18, bibliothèque standard ; sortie
`devis-crible-iv-brouillon1-sortie.txt` (empreinte dans son compagnon), recopiée en entier :

```
§ 0. Contrôles de cohérence des entrées
appels 16 ; somme des durées 2668.095 s
machine du pilote 1.5706 h ; hors appels 2985.9 s
quatre proposeurs + machine 15.302276 (verdict : 15,302276)

§ 1. Attendu par appel de Pr-2 (moyenne des quatre appels du pilote, règle (b) de [CRIBLE-V]) et appel de trois cartes
appel de six cartes (mesuré, moyenne) c6 = 0.264334
part d'entrée supposée 0.069333 ; sortie déduite 0.195001
appel de trois cartes : prudent c3 = c6 = 0.264334 ; bas (sortie moitié, SUPPOSÉ) 0.166834 ; rapport bas c3/c6 0.6311

§ 2. Taille servie (règle du code : (octets + 1 024) x entrée + borne x sortie <= plafond)
octets servis au plus : 53976 ; ligne d'arrêt : 53 000 ; cible de la règle : 52 000
cartes d'archive au plus dans un texte servi : bras 1 et 3, génération 2 : K1 + 6 ; bras 2, demi 2b : K1 + 9

§ 3. Appels du crible
bras 1 (standard, 1 appel de six par génération) : par monde 2 ; en tout 40
bras 2 (demi-générations, 1a commun compris) : par monde 4 ; en tout 80
bras 3 (placebo, sans 1a commun) : par monde 3 ; en tout 60
variante, 1a commun aux bras 2 et 3 : par monde 9 ; en tout 180
forme de [NOTE] (sans appel commun) : par monde 10 ; en tout 200

§ 4. Garde d'égalité de dollars par monde (un appel des bras 2 ou 3 part si la dépense déjà faite du bras < $1(w))
c3/c6 = 0.5000 : appels du bras 2 faits 4 sur 4 ; dépense 0.5287 ; rapport au bras 1 1.0000
c3/c6 = 0.6000 : appels du bras 2 faits 4 sur 4 ; dépense 0.6344 ; rapport au bras 1 1.2000
c3/c6 = 0.6311 : appels du bras 2 faits 4 sur 4 ; dépense 0.6673 ; rapport au bras 1 1.2623
c3/c6 = 0.6667 : appels du bras 2 faits 3 sur 4 ; dépense 0.5287 ; rapport au bras 1 1.0000
c3/c6 = 0.8000 : appels du bras 2 faits 3 sur 4 ; dépense 0.6344 ; rapport au bras 1 1.2000
c3/c6 = 1.0000 : appels du bras 2 faits 2 sur 4 ; dépense 0.5287 ; rapport au bras 1 1.0000
seuils : 2a part si c3 < c6 ; 2b part si 3 c3 < 2 c6, soit c3/c6 < 2/3 = 0.6667
dépassement borné : dépense d'un bras 2 ou 3 dans un monde <= $1(w) + un appel (plafond 2,00)

§ 5. Devis (Pr-2, crédits de Claude)
bras 1 40 appels : attendu (tous faits, c6) 10.5734 ; bas (c3 supposé) 10.5734 ; plafonds 80.00
bras 2 (1a commun compris) 80 appels : attendu (tous faits, c6) 21.1467 ; bas (c3 supposé) 13.3467 ; plafonds 160.00
bras 3 (hors 1a) 60 appels : attendu (tous faits, c6) 15.8600 ; bas (c3 supposé) 10.0100 ; plafonds 120.00
proposeurs : attendu (tous faits) 47.5801 ; bas 33.9301 ; plafonds x appels 360.00
si c3 = c6 (garde : bras 2 et 3 réduits à la génération 1) : 100 appels, attendu 26.4334
borne par la garde (bras 1 <= 4 ; bras 2 et 3 <= $1 + 2 chacun, par monde) : 320.00
part du relais proposée (forme de [NOTE] : 80 + 80 + 80) : 240.00 ; coût moyen par appel qui l'atteint (180 appels) : 1.3333 soit 5.04 fois c6
sonde des gabarits (3 appels de six cartes + 1 de trois cartes à archive de K1 + 9) : attendu 1.0573 ; pire 8.00

§ 6. Durées et machine
opus55 : moyenne 68.387 s ; plus long 109.396 s ; borne par appel (règle de [CRIBLE-V]) B_a = 900 s
monde, attendu (tour de chaîne supposé 60 s) : 770.3 s
files 4 : mondes par file 5 ; appels et chaîne attendus 3851.6 s
   B_c = 300 s : pire par monde 7200 s ; pire de la file 36000 s = 10.000 h ; garde de départ (pire + 2 h) 12.000 h
   B_c = 600 s : pire par monde 9000 s ; pire de la file 45000 s = 12.500 h ; garde de départ (pire + 2 h) 14.500 h
   B_c = 900 s : pire par monde 10800 s ; pire de la file 54000 s = 15.000 h ; garde de départ (pire + 2 h) 17.000 h
files 5 : mondes par file 4 ; appels et chaîne attendus 3081.3 s
   B_c = 300 s : pire par monde 7200 s ; pire de la file 28800 s = 8.000 h ; garde de départ (pire + 2 h) 10.000 h
   B_c = 600 s : pire par monde 9000 s ; pire de la file 36000 s = 10.000 h ; garde de départ (pire + 2 h) 12.000 h
   B_c = 900 s : pire par monde 10800 s ; pire de la file 43200 s = 12.000 h ; garde de départ (pire + 2 h) 14.000 h
machine attendue (5 files) 0.088012 USD ; 0.192456 avec deux heures de génération de mondes ; 17 h : 0.8878 ; pire 3,00

§ 7. Totaux de la variante
crédits de Claude : attendu (tous faits) 47.5801 ; bas 33.9301 ; pire (part) 240.00
hors crédits (machine) : attendu 0.0880 à 0.1925 ; pire 3.00
avec la sonde : crédits attendu 48.6375 (bas 34.9874) ; pire 248.00 ; total pire 251.00
sonde partagée avec celle du crible (ii) (ses trois premiers appels) : pire 245.00 ; attendu de la sonde 0.2643

§ 8. Enveloppe de GO-2026-11-15-06 (1 275 USD au pire)
(iii) version qui fera foi v1, sonde comprise 270.00
(v) version qui fera foi v2, sonde neuve comprise 204.67
(ii) brouillon 1, sonde comprise 411.00
(i) brouillon 1 127.00
quatre autres : 1012.67 ; reste pour (iv) : 262.33
(iv) variante, part 240, sonde propre 251.00 ; cumul 1263.67 ; tient : True ; marge 11.33
(iv) variante, part 240, sonde partagée avec (ii) 245.00 ; cumul 1257.67 ; tient : True ; marge 17.33
(iv) plafonds x appels (360), sonde propre 371.00 ; cumul 1383.67 ; tient : False ; marge -108.67
(iv) borne de la garde (320), sonde propre 331.00 ; cumul 1343.67 ; tient : False ; marge -68.67
(iv) [NOTE] 243.00 ; cumul 1255.67 ; tient : True ; marge 19.33

§ 9. Test des rangs signés exact (permutation des signes), seuil bilatéral
niveau 0.025 : au moins 7 écarts non nuls, tous du même signe (p = 0.01562)
niveau 0.050 : au moins 6 écarts non nuls, tous du même signe (p = 0.03125)

§ 10. Signe seul (écarts de 0 ou +-1) : puissance à n = 20, bilatéral 0,025
P(+1) = 0.30 P(-1) = 0.10 : puissance (côté +) 0.107
P(+1) = 0.40 P(-1) = 0.10 : puissance (côté +) 0.271
P(+1) = 0.50 P(-1) = 0.10 : puissance (côté +) 0.473
P(+1) = 0.35 P(-1) = 0.05 : puissance (côté +) 0.327
P(+1) = 0.20 P(-1) = 0.05 : puissance (côté +) 0.042

§ 11. Probabilité d'atteindre le minimum (16 mondes complets sur 20 pour une comparaison principale)
p par appel 1 : P1 (6 appels : bras 1 et 2) 1.0000 ; P2 (7 appels : bras 2 et 3, 1a commun) 1.0000
p par appel 0.99 : P1 (6 appels : bras 1 et 2) 0.9949 ; P2 (7 appels : bras 2 et 3, 1a commun) 0.9905
p par appel 0.98 : P1 (6 appels : bras 1 et 2) 0.9304 ; P2 (7 appels : bras 2 et 3, 1a commun) 0.8865
p par appel 0.97 : P1 (6 appels : bras 1 et 2) 0.7673 ; P2 (7 appels : bras 2 et 3, 1a commun) 0.6643
p par appel 0.95 : P1 (6 appels : bras 1 et 2) 0.3565 ; P2 (7 appels : bras 2 et 3, 1a commun) 0.2326

§ 12. Formes écartées, information seulement
forme de [NOTE], Pr-1 argon, 200 appels : attendu public 24.7162 ; configuration 123.5810 (hors crédits) ; plafonds x appels 468.00
Pr-2, 200 appels sans appel commun : attendu 52.8668 ; plafonds x appels 400.00
[NOTE] : 30,30 attendus, 243,00 au pire
```

Notes de lecture : (1) au § 1, la part d'entrée (52 000 octets à 3 octets par jeton) est **supposée**, de la forme des hypothèses
du brouillon 9 de (v) ([CRIBLE-V], « Estimation du brouillon 9 ») ; (2) au § 4, les coûts sont pris égaux à leur moyenne dans
chaque monde : la variation réelle entre mondes fait couper ou passer 2b près du seuil ; (3) au § 6, le tour de chaîne de 60 s est
**supposé** ; la partie A le mesure ; (4) au § 10, le modèle « écarts de 0 ou ± 1 » est une simplification : la simulation de la
section « Taille » le refera ; (5) au § 11, un appel coupé par la garde n'est pas un échec : les nombres d'appels sont des maximums.

## Citations obligatoires (N-064, N-067)

POPPER (Huang et al., ICML 2025 ; `docs/sources/pdf/huang-2025-icml-pmlr-267-popper-automated-hypothesis-validation-agentic-sequential-falsifications.pdf`,
`a3c4b370…`) ; Dwork et al., arXiv 1506.02629 (`dcfbb9aa…`) ; Blum et Hardt, « The Ladder », arXiv 1502.04585 (`957ef473…`) ;
Co-Scientist (Gottweis et al., Nature 655, p. 487-496, 2026 ; `351f49d8…`), voisin de la boucle générer-classer-faire évoluer ; et
la liste de `docs/decisions/decision-N-067-v1.md`, section 6, dont CADS (Chen et al., arXiv 2610.24597 : contribution
incrémentale des proposeurs, cité par N-067 pour N-058, p. 7 ; PDF sur une autre branche, non lu par l'auteur). Voisins nommés par
les fiches, non lus sur PDF par l'auteur : Fork-and-Flush ([CAT] C5) et « Scaling Discovery Requires Forgetting » ([CAT] C6).
Empreintes et pages recopiées de [NOTE] (citations obligatoires), non revérifiées sur les PDF par l'auteur. Aucune revendication
n'est faite ici.

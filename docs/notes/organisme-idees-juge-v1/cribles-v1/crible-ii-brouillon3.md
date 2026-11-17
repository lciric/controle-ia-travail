# Préenregistrement — crible (ii) de l'organisme d'idéation : proposeurs en série, chaque session voit les cartes brutes des précédentes — brouillon 3 (variante « crédits de Claude au maximum »)

- Auteur : sous-agent neuf de la session mère, rédacteur de cette pièce (« modèle A » de cette pièce au sens de R-2598 ;
  identité dite en conversation seulement). L'auteur n'a écrit ni la note des idées originales, ni le relevé, ni les fiches,
  ni le pilote MR-2, ni son code, ni sa procédure, ni aucune pièce des cribles (iii) et (v), ni aucune contre-lecture citée.
- Date (UTC) : 2026-11-17, rédaction de 00:45 à 01:01 (`date -u` au début et au scellement) ; dépôt lu sur `main`
  (tête `b38bde8c`, puis `c97bf55f`) ; une seule branche lue, `verdict/pilote-mr2-v74-v14-v1` (tête `61230010`), par
  `git show` après un `git fetch` à refspec, et d'elle **seul** le verdict v2 du pilote ; aucun commit, aucune poussée,
  aucun appel de modèle, aucune machine, aucune dépense.
- Brouillon 2 : corrections du tour 1 de contre-lecture appliquées le 2026-11-17T01:31:15Z (`date -u`, au scellement) par un
  rédacteur neuf, d'un autre modèle que l'auteur, qui n'a écrit ni le brouillon 1 ni le rapport de contre-lecture
  (identité dite en conversation seulement), au moyen du programme `appliquer-corrections-crible-ii-brouillon2.py` (même dossier,
  scellé) ; dépôt lu sur `main` (tête `5a01b434`) ; aucune branche lue ; aucun commit, aucune poussée, aucun appel de
  modèle, aucune machine, aucune dépense. Rien d'autre que les corrections, l'en-tête, le « Statut », la ligne du validateur, l'accord « seuls son » de D4.1 et la section « Contre-lecture »
  ne change.
- Brouillon 3 : corrections du tour 2 de contre-lecture appliquées le 2026-11-17T01:51:11Z (`date -u`, au scellement) par un
  rédacteur neuf, d'un autre modèle que l'auteur (« modèle C » de cette pièce, comme le lecteur du tour 2), qui n'a écrit ni
  le brouillon 1, ni le brouillon 2, ni aucun rapport de contre-lecture (identité dite en conversation seulement), au moyen du
  programme `appliquer-corrections-crible-ii-brouillon3.py` (même dossier, scellé) ; dépôt lu sur `main` (tête `1df4ae9f`) ;
  aucune branche lue ; aucun commit, aucune poussée, aucun appel de modèle, aucune machine, aucune dépense. Rien d'autre que
  les quatre couples du tour 2 (m1.1, m1.2, m2.1, m3.1), le titre, cette entrée de l'en-tête, le « Statut », la ligne du
  validateur et la section « Contre-lecture » (entrée « Contre-lecture 2 » ajoutée ; ligne vide rétablie avant le titre de
  l'annexe A) ne change.
- Nombres neufs : `devis-crible-ii-brouillon1.py` et sa sortie `devis-crible-ii-brouillon1-sortie.txt` (même dossier, scellés à
  côté ; `nice -n 19 python3 -I`, Python 3.13.18, bibliothèque standard, fractions exactes ; lancé le 2026-11-17 à 00:53:32 UTC) ;
  paragraphes de la sortie cités « sortie, § k » ; sortie recopiée à l'annexe A.
- Commit du code d'analyse : **aucun à ce jour**. Le code s'écrit après la contre-lecture de ce texte et son scellement ; ses
  empreintes entrent dans un addendum d'empreintes scellé avant tout jeu, qui ne change rien d'autre.
- Documents qui font foi (chemin, empreinte entière) :
  - note des idées originales, § 1, § 2, § 3 (ii), § 4, § 6, § 7 et annexe A :
    `docs/notes/organisme-idees-juge-v1/conception-idees-originales-v1.md`
    (`2f6a69dd480a079fa385846c8aca06ff53c8d40b0cf36be1fd61cf8e1e0537a3`) — ci-dessous **[NOTE]** ;
  - relevé des idées, § 2.1, § 3.2, § 5 et § 6 : `docs/notes/organisme-conception-propre-v1/relecture-exploratoire-v2/releve-idees-reutilisables-v1.md`
    (`bd253b6c68f6baada0e61b5381f029b52838ca34aa092502e55253c662451c6c`) — **[RELEVÉ]** ; fiche opus-p1-04 (n° 8) du fichier
    `runs/course-ideation-conception-propre-v1/20261113-235541-course-ideation-conception-propre-v1-g1/copies/sortie--fiches-validees.json`
    (`a9f9594e2dc3a7a553c54577202817758e3f7ef231445f1a48d500fc647389d5`) : **non relue par l'auteur** (pièce sous `runs/`), citée à
    travers [RELEVÉ] et [NOTE] ;
  - verdict v2 de l'issue du pilote MR-2 v14 : `docs/notes/organisme-multi-generations-v1/pilote-v1/lecture-issue-pilote-v14-mere/verdict-issue-v2/verdict-issue-pilote-mr2-v14-v2.md`
    (`e64458e82bae1d03e40656ad3b65456769eefd2603a7306e9a7d401eba8e1a3d`, égale au compagnon et à `git show | sha256sum`), branche
    `verdict/pilote-mr2-v74-v14-v1` ; sections « Pour les cribles », « Dépense rapprochée », « Comptes » et « Audit de symétrie »
    lues — **[VERDICT-PC]** ;
  - version qui fera foi v1 du crible (iii), même dossier : `crible-iii-version-foi-v1.md`
    (`91b4bf30fbf8b83d2c057088d8776be19831b006f1010bcb3c7e2e231d2c7179`) — **[CRIBLE-III]** ; **modèle de forme** de ce texte, et
    source, à travers lui, des définitions de [PILOTE] (« Métrique » : appels, cartes, composantes comptées, attribution), du bloc
    gelé (plafonds de session, bornes de sortie, réglages) et de [PROC-14] (machine, barrières, rapatriement), **non relus par
    l'auteur** sur leurs branches ;
  - version qui fera foi v2 du crible (v), même dossier : `crible-v-version-foi-v2.md`
    (`2b99627dd378564dba816bc10593cdb0d06d77a3fdd4eb9e3cca022c76838715`) — **[CRIBLE-V]** ; table des proposeurs (clés, crédits,
    plafonds, prix de la configuration et prix publics), règles (a) à (d) du devis refait, règle de la borne par appel ;
  - registre des GO, ligne GO-2026-11-15-06 (l. 339) : `registres/go.md` (fichier de travail,
    `c20084fb698609b84a97b41f4ec759775d03a8030d913411bb1afa954eafb54b`) ; registre des dépenses (fichier de travail,
    `edb519ccb8e5861c6138356a32bdde1a8730ceb57b86aaf527d2c856d3dce858`) : **aucune** ligne de l'un ni de l'autre ne cite
    GO-2026-11-15-06 hors la l. 339 ; registre des décisions : R-2851, R-2875, R-2977, R-2992, R-2993, R-3005, R-3044, R-3053
    (registre vivant) ;
  - famille MR-2 : conception v4 `docs/notes/organisme-multi-generations-v1/conception-monde-riche-doublons-v4.md`
    (`47e38ec0663320e8c68011130c3f1b8e1017969cbb740d30c83a78eb5db0a6dc`) — **[MR2]** ;
  - outils : `docs/notes/organisme-multi-generations-v1/outils-v4/monde_riche_v4.py`
    (`4b1658477811fb87360dda44a65b0af96e87ae1d2ca4a32bdabbd3ce6cc19eb8`) ; `…/outils-v1/complements_synthese_v1.py`
    (`89eb7ba8c8cf8633541a6de8090767f74619e3f3968ebed8f894b1f8d593e9ba`, fonction `grouper_stratifie`, ε = 0,01, ε de strate 0,04,
    lue) ; `…/pilote-v1/outils/mesure_pilote_v4.py` (`676d5f37f21cf5d512f92d2029991fa8795a77076c285ea9bd83c43841748365`, cité à travers
    [CRIBLE-III], non relu) ;
  - décisions : `docs/decisions/decision-N-058-v1.md` (`854f2724864f1e45394e001f4aca7b0248753e5d2b0a66991e2ee8a7be87de9d`),
    `docs/decisions/decision-N-045-v2.md` (`c7b05e39de381cee1d5ec2276745a0310bd3cc0857a6be0e0fb14eeb5042261d`),
    `docs/decisions/decision-N-044-v1.md` (`2b70bdac014d366d058a530680d016663b35ed73b8ca0cae9f2369206f5004bf`),
    `docs/decisions/decision-N-067-v1.md` (`966dd9dc3fae61cbe1f10ee2a54f401ddf7af5041eeaacd81ad9f8b264661589`) — empreintes
    vérifiées, textes non relus en entier par l'auteur (cités à travers [NOTE] et [CRIBLE-III]) ;
  - catalogue des conceptions publiées : `docs/notes/organisme-conception-propre-v1/catalogue-conceptions-publiees-v1.md`
    (`ddfb2522be0fe5095926405b8761d0e4be0065a29679585051a287349114fe9d`) — **[CAT]**, lignes C1, C5 et C6 ;
  - gabarit `prereg/gabarit-preregistrement-v1.md` (`8cad43714b562e28238a92200d6315b1769d8bdf7e9f0a8d72dfe2bc9b37700e`) ;
    validateur `src/controle_ia/prereg.py` (`3b2e3ee56463f30ffd3c549e7fe480fea574c707581bcf30098bf38f4980c306`).

**Statut.** **Brouillon 3**, contre-lu deux fois (tours 1 et 2, corrections appliquées, section « Contre-lecture »), scellé comme
pièce (empreinte compagnon, R6), non comme préenregistrement en vigueur ; troisième tour de contre-lecture à la décision de la mère. Écrit après le verdict du pilote MR-2 v14 : les attendus du devis sont faits **directement** sur les coûts et durées
mesurés du pilote ([VERDICT-PC]) par les règles de [CRIBLE-V] (moyenne de tous les appels, pires cas aux plafonds) ; les
prédictions sont écrites **sans donnée de proposeur sur la couverture des composantes comptées, hors la classe des conditionnelles** (le pilote ne la mesure pas par appel ; seuls son
témoin positif et le résultat principal sont lus, [VERDICT-PC], « Pour les cribles » et « Comptes » : aucun des 14 appels répondus ne porte une conditionnelle entière, x = 0 ; le pilote ne dit rien de S contre P). Aucune dépense, aucun appel de modèle, aucun monde tiré. L'accord
GO-2026-11-15-06 (enveloppe des cinq cribles, crédits de Claude employés au maximum) **n'autorise encore aucun appel** : la ligne
« calcul » de ce crible s'inscrit par la mère sur un devis contre-lu, dans l'enveloppe (lecture de la mère, l. 339). Le dessin
neuf (des cartes de pairs dans la vue) est **essayé, non adopté** (l. 339 ; [NOTE] § 7, point 3) : toute adoption dans
l'organisme reste un nœud de Lazar. **Point de faisabilité à trancher avant tout code** (« Choix et doutes », point 3) : sous
la configuration v12, le texte servi d'un appel du proposeur retenu ne peut dépasser 53 976 octets (sortie, § 2), et le texte du
pilote en prend déjà jusqu'à 52 000 ([CRIBLE-III], « Devis » : « ≤ 52 000 octets servis ») : les cartes des pairs n'y tiennent pas sans retirer des
épisodes servis, à tous les bras également, ou changer de configuration.
Validateur `controle_ia.prereg.problemes` : aucun défaut sur ce brouillon 3 (vérifié avant son scellement comme pièce de
travail).

## 0. En dix lignes

1. **Question** ([NOTE] § 3 (ii) ; [RELEVÉ] § 3.2) : servir à chaque session de proposeur, neuve, les cartes **brutes** déjà
   rendues par les sessions précédentes de la génération (sans verdict, avec la phrase « une carte presque identique sera
   regroupée avec elle ») **disperse**-t-il les propositions sur davantage de composantes plantées, ou les **regroupe**-t-il
   (grégarisme) ? Et l'effet vient-il du **contenu** des cartes servies ou de leur seule **présence** ?
2. **Trois bras** de quatre sessions sur les mêmes 20 mondes MR-2, archive {K1}, une génération : **P** parallèle (quatre sessions
   indépendantes) ; **S** série (la session de rang k voit les cartes valides des rangs 1 à k − 1 du bras S) ; **Q** série placebo
   (même nombre de cartes, de longueur appariée, **prises d'un autre monde** du crible). Aucun juge, aucun test de mort (N-058).
3. **Version bon marché de [NOTE]** : les quatre places tenues par des sessions neuves d'**un seul** proposeur ; variante
   « crédits de Claude au maximum » : **Pr-2** (sur crédits de Claude) au lieu de Pr-1 (hors crédits) ; l'ordre des proposeurs,
   sans objet à un seul proposeur, n'est pas joué (« Écarts »).
4. **Rang 1 commun** : la session de rang 1 ne voit aucune carte ; elle est la même dans les trois bras (une des quatre sessions de
   P, désignée par graine) : **10 appels par monde, 200 en tout** au lieu de 240 (écart à [NOTE], dit ; il fait tenir le crible dans
   l'enveloppe, sortie, § 8).
5. **Mesure** (oracle du pilote sur les cartes brutes) : C_X(w), composantes comptées couvertes par au moins une carte valide des
   quatre sessions du bras X ; groupes prédictifs (`grouper_stratifie`, instances publiques sans issue) ; copies d'une carte servie ;
   apport par rang ; conditionnelles ; dollars.
6. **Deux principales** (Bonferroni, bilatéral à 0,025 chacune, test exact des rangs signés) : **principale SP** δ_SP = C_S − C_P (dispersion
   ou grégarisme) ; **principale SQ** δ_SQ = C_S − C_Q (contenu des cartes des pairs contre leur seule présence). Secondaire : δ_QP.
7. **Prédiction de l'auteur** : SP « non tranché », estimation de δ_SP entre 0 et + 0,5 composante par monde (confiance 0,4) ;
   SQ « non tranché », entre 0 et + 0,5 (0,4) ; δ_QP ≈ 0 (0,5).
8. **Devis** (coûts mesurés du pilote, règles de [CRIBLE-V]) : **53,92 USD attendus sur crédits de Claude** (200 appels de Pr-2 à
   0,264334, plus la sonde des gabarits, 1,06), haut de fourchette 59,97 ; **0,06 à 0,11 hors crédits** (machine) ;
   **411 au pire** (408 sur crédits, 3 hors crédits), sonde comprise ; [NOTE] : 63,30 attendus, 483 au pire.
9. **Enveloppe** de GO-2026-11-15-06 : aux textes actuels des quatre autres cribles ((iii) 270, (v) 204,67, (i) 123 et (iv) 243
   de [NOTE]), le cumul fait **1 251,67 USD**, sous 1 275 (marge 23,33) ; la forme de [NOTE] (240 appels) n'y tiendrait pas
   (1 331,67 avec sa sonde) ; sortie, § 8.
10. **Durée** : ≈ 21 min d'appels attendues (sortie, § 5), plus mise en place, mondes, mesure et barrières ; pire des appels 4 h
    (borne de 900 s par appel) ; garde de départ 6 h ; une seule machine, un seul fournisseur, au plus 20 sessions à la fois.

## Hypothèse

**Contexte.** La fiche opus-p1-04 ([RELEVÉ] § 3.2, isolée : un seul proposeur) propose d'appeler les proposeurs l'un après
l'autre ; chacun voit le texte brut des cartes déjà rendues dans la génération, sans verdict, avec la phrase « une carte presque
identique sera regroupée avec elle » ; il « devrait porter ses cartes ailleurs ; le signe peut s'inverser (grégarisme), et c'est ce
que l'essai tranche ». Le relevé (§ 2.1) note un fait voisin dans un appel de six cartes : « la première carte attire les cinq
autres » (course v67, onze variantes d'un même constat). Le contrôle repris du relevé (§ 3.2 et § 5) : des cartes **d'un autre
monde**, de même longueur, à la place des cartes des pairs, qui séparent l'information de l'allongement du contexte. N-045, point 1 :
« l'ordre et la forme des échanges » sont une variable de composition à apprendre ; ce crible en donne une première mesure.

**H-ii** (énoncé de [NOTE] § 3 (ii), version bon marché, proposeur de la variante). Dans une génération partie de {K1}, sur la
famille MR-2, quatre sessions neuves d'un même proposeur dont chacune voit les cartes brutes des précédentes (bras S) couvrent un
**nombre de composantes comptées différent** de celui de quatre sessions indépendantes (bras P) ; le signe n'est pas fixé par le
programme : « dispersion » s'il est positif, « grégarisme » s'il est négatif.

**H-ii-a** (contrôle, [RELEVÉ] § 5 ; N-045 point 7, « espaces de conception égaux ») : l'écart S − P, s'il existe, vient du
**contenu** des cartes servies (S contre Q, cartes d'un autre monde en même nombre et de même longueur), et non de leur seule
présence (Q contre P).

**La variante change-t-elle la question de [NOTE] ?** Un peu ; c'est dit ici, **sans trancher** (si la question n'est plus celle
de la note, c'est à la mère ou à Lazar de le dire). [NOTE] fait tenir les quatre places de la version bon marché par Pr-1 (hors
crédits) ; la variante les donne à Pr-2 (sur crédits de Claude). Restent les mêmes : un seul proposeur aux quatre places (« sépare
le mécanisme de la composition », [NOTE]), les trois bras, la mesure, les contrôles. Change la portée : une conclusion porte sur
les sessions d'**un** proposeur de la maison de Claude, non sur un proposeur d'une autre maison ; ni l'une ni l'autre forme ne
mesure l'échange entre proposeurs **différents** (la version « composition » de [NOTE], quatre proposeurs dans un ordre tiré au
sort, n'est pas jouée).

**Hypothèses de travail.** (i) Sessions neuves et indépendantes, sans historique ; une session de rang k ne reçoit des précédentes
que leurs cartes valides, réécrites sous une forme canonique, jamais leur réponse brute entière ni leur réflexion. (ii)
**Génération 1 seulement**, archive {K1} ; le gardien mécanique du pilote seul ; aucun verdict, aucun oracle, aucune issue dans la
vue. (iii) Les cartes d'un autre monde portent des traits dont l'indice n'a pas le même sens dans le monde servi (les traits sont
permutés par monde par le générateur, `generer_monde_v4`) : elles sont un contexte de même forme, sans information juste sur ce
monde, et peuvent **égarer** ; un Q < P mesure cet égarement autant que la seule présence. (iv) Une carte peut porter plusieurs
composantes à la fois (un arbre jusqu'à 48 feuilles, [MR2] § 2.2) : la couverture d'un bras sature vite sur les composantes
visibles à la marge ; l'écart possible tient aux composantes moins visibles.

## Prédiction chiffrée et signe attendu

Écrites après le verdict du pilote, sans donnée de couverture par appel des composantes comptées, hors la classe des conditionnelles (le pilote ne la rend pas) ; seuls le résultat principal (x = 0 sur 14 : aucun appel ne porte une conditionnelle entière) et le témoin positif
du pilote sont lus ([VERDICT-PC] : 14 appels répondus sur 14 portent une composante au-delà de K1 ; 6 portent la composante de
condition sans la conditionnelle entière) ; confiance faible. Notations : section « Métrique ».

| # | prédiction | signe | chiffre | ce qui la réfute | confiance |
|---|---|---|---|---|---|
| II-1 | **principale SP** : δ_SP (série contre parallèle) | ≥ 0 | estimation entre 0 et + 0,5 composante par monde ; issue « non tranché » | estimation de δ_SP < 0 (réfute le signe) ; issue autre que « non tranché » (réfute l'issue) | 0,4 |
| II-2 | **principale SQ** : δ_SQ (contenu des pairs contre cartes d'un autre monde) | ≥ 0 | estimation entre 0 et + 0,5 ; issue « non tranché » | estimation < 0 ; issue autre que « non tranché » | 0,4 |
| II-3 | δ_QP (seule présence, ou égarement) | ≈ 0 | estimation entre − 0,5 et + 0,3 | test des rangs signés bilatéral à 0,05 significatif, de l'un ou l'autre signe | 0,5 |
| II-4 | groupes prédictifs : moyenne par monde de G_S − G_P | + | entre + 0,5 et + 2 groupes | moyenne ≤ 0 | 0,45 |
| II-5 | copies d'une carte servie, rangs 2 à 4 : k_S contre la référence k_P (copies d'une carte de P1 parmi les cartes de P2 à P4) | k_S < k_P | k_P entre 0,2 et 0,5 ; k_S ≤ k_P − 0,1 | k_S ≥ k_P | 0,4 |
| II-6 | première conditionnelle couverte (mondes complets) | ≈ 0 | S − P entre − 1 et + 2 mondes | \|S − P\| ≥ 4 mondes | 0,5 |
| II-7 | coût relatif $_S / $_P (prix publics) | ≥ 1 | 1,00 à 1,15 | < 1,00 ou > 1,30 | 0,6 |

**Portée de la colonne « ce qui la réfute »** (forme de [CRIBLE-III], remarque R-4) : une prédiction dont le chiffre est manqué
sans que cette colonne soit atteinte n'est **ni confirmée ni réfutée** ; le rapport le dit tel quel.

**Raisons.** Dans les 12 mondes de développement de [MR2], hors l'effet de K1, 3 à 5 composantes sont à couvrir par monde
([CRIBLE-III], « Raisons », d'après [MR2]) : les nombres sont petits. II-1 : quatre sessions indépendantes d'un même proposeur
retrouvent d'abord les mêmes composantes visibles (le témoin positif du pilote dit que chaque appel répondu va au-delà de K1) ; la
couverture de P sature sur elles ; une session qui voit ces cartes, et la phrase du regroupement, peut porter ses cartes sur
d'autres traits, mais ce qui reste à couvrir est le moins visible (moyennes faibles, conditionnelles) : un petit gain, de l'ordre
d'une composante dans un monde sur trois à quatre, que 20 mondes ne tranchent pas (sortie, § 10 : puissance 0,11 à 0,47 selon
l'effet). Le grégarisme (imitation des cartes servies) est possible ; le pari porte sur un petit signe positif. II-2 : les cartes
d'un autre monde ne disent rien de juste sur ce monde ; si S gagne, c'est par le contenu ; même ordre que II-1. II-3 : la seule
présence de six à dix-huit cartes étrangères allonge la vue et peut égarer (traits sans sens ici), ou pousser vers d'autres
formes ; aucun des deux n'est attendu grand. II-4 : la phrase du regroupement et la vue des cartes déjà rendues devraient pousser
vers des lois aux prédictions différentes, même quand elles ne couvrent rien de plus. II-5 : sans consigne, des sessions
indépendantes se recopient de fait (même constat, [RELEVÉ] § 2.1) ; averties, elles devraient moins recopier une carte servie.
II-6 : la conditionnelle est rare dans une carte libre (hypothèse de masquage de [MR2] : 0,02 par carte, estimée) ; rien dans la
vue de S ne la désigne. II-7 : les rangs 2 à 4 de S lisent un bloc de cartes en plus ; à texte servi total borné (section « Plan
d'analyse »), le surcoût d'entrée est petit.

**Ce que serait chaque issue (R3).** SP « dispersion » : H-ii non réfutée au crible, signe positif ; lue avec SQ : si le contenu
compte (S > Q), la dispersion vient de l'information des cartes des pairs ; sinon, elle n'est pas distinguée de la seule présence.
SP « grégarisme » : H-ii non réfutée au crible, signe négatif ; voir les cartes des pairs **nuit** à la couverture de ce
proposeur. SP « non tranché » : rien sur l'effet à 20 mondes ; un petit effet n'est pas exclu (crible d'un grand effet). Aucune
issue n'adopte le dessin ; une issue « dispersion » donne un argument pour une course préenregistrée à part, à composition
apprise (N-045 point 1), non une règle.

## Métrique

Programme de mesure neuf, `mesure_crible_ii_v1.py` (nom réservé ; dérivé de `mesure_pilote_v4.py`, `676d5f37…`), lancé une seule
fois sur la machine du crible.

- **Appels et cartes** : définitions de [PILOTE] (« Métrique »), telles que recopiées par [CRIBLE-III] (« Métrique ») : appel
  complet, tronqué, en échec ; carte **valide** = admise au gardien, évaluable, emplacement ≤ 6, d'un appel complet ; appel
  **répondu** = complet avec au moins une carte valide. Les cartes refusées, au-delà de six, non évaluables ou d'appels tronqués
  comptent dans les dollars, jamais dans une couverture, et ne sont **jamais servies** à une session suivante.
- **Sessions d'un monde** : P1 (rang 1 commun, désigné par graine parmi les quatre sessions parallèles), P2, P3, P4 (les trois
  autres sessions parallèles, dans l'ordre de leur indice) ; S2, S3, S4 (série) ; Q2, Q3, Q4 (placebo). **Bras** : P = {P1, P2,
  P3, P4} ; S = {P1, S2, S3, S4} ; Q = {P1, Q2, Q3, Q4}.
- **Bloc servi** au rang k (k = 2, 3, 4) : pour S_k, les cartes valides de P1, S2, …, S_{k−1}, dans cet ordre puis par
  emplacement ; pour Q_k, le **même nombre** m_k de cartes prises aux sessions **parallèles** d'un monde donneur (règle de la
  section « Plan d'analyse »). Chaque carte est le texte de la carte tel qu'extrait de la réponse brute, réécrit sous une forme JSON
  canonique compacte (clés triées, sans espace), sans autre retouche ; elle est numérotée ; aucune mention de session, de rang, de
  proposeur, de monde ni de verdict.
- **Composantes comptées et couverture** : définies par [PILOTE] (« Métrique » : attribution Δ_i, seuil τ_i, témoin positif),
  telles que recopiées par [CRIBLE-III] : composantes **certifiées** (étiquette C8 de `verifier_v4`, latente exclue), moins l'effet
  de K1 et ce que K1 servie porte à elle seule ; une carte porte la composante i si Δ_i ≥ max(0,005 ; 0,75·I_i) (oracle de
  12 000 instances). **C_X(w)** = nombre de composantes comptées portées par au moins une carte valide du bras X dans le monde w.
  K(w) = nombre de composantes comptées du monde.
- **Écarts** : δ_XY = moyenne, sur les mondes complets pour la comparaison X–Y, de C_X(w) − C_Y(w). Statistiques de SP et SQ :
  δ_SP et δ_SQ ; secondaire : δ_QP.
- **Test** : test exact des rangs signés de Wilcoxon par permutation des signes (2^n permutations, n ≤ 20), écarts nuls retirés,
  rangs moyens aux égalités, bilatéral ; au moins 7 écarts non nuls sont nécessaires pour un p ≤ 0,025 (7 suffisent s'ils sont tous du même signe), au
  moins 6 pour 0,05 (sortie, § 9). **Intervalles** rapportés : rééchantillonnage apparié des mondes complets, 10 000 rééchantillons,
  percentile, 97,5 % pour SP et SQ, 95 % ailleurs ; **ils ne décident pas** (le test décide, fidèle à [NOTE] : « rangs signés de
  Wilcoxon »).
- **Groupes prédictifs** : G_X(w) = nombre de groupes de `grouper_stratifie` (ε = 0,01, ε de strate 0,04, valeurs du fichier)
  parmi les cartes valides du bras X, calculés sur un **jeu public d'instances sans issue** du monde w (traits et
  sous-populations seulement ; tirage en section « Graines »). **Quasi-doublons** : part des cartes valides du bras X qui sont dans
  un groupe de taille ≥ 2.
- **Copies d'une carte servie** : k_S = part des cartes valides de S2 à S4 regroupées (même calcul, même jeu d'instances) avec au
  moins une carte de leur bloc servi ; k_Q, même définition pour Q2 à Q4 et leur bloc (cartes d'un autre monde, évaluées sur les
  instances du monde w) ; **référence** k_P = part des cartes valides de P2 à P4 regroupées avec une carte de P1. **Copies de
  l'archive** : part des cartes valides de chaque bras regroupées avec K1.
- **Apport par rang** : A_X^k(w) = composantes comptées portées par la session de rang k du bras X et par aucune session de rang
  inférieur du même bras (P ordonné P1, P2, P3, P4) ; somme sur les mondes, par rang et par bras ; rapporté sans verdict.
- **Traits employés** (définition de [CRIBLE-III]) : le trait j est employé par une loi si un nœud `softmax` a des poids de colonne
  j non tous égaux entre issues (écart > 10⁻⁶), si un nœud `si_sinon` conditionne sur z_j, ou si une `transformee` oscille sur z_j.
  **Traits neufs** : part des cartes valides de rang k ≥ 2 (S et Q) qui emploient au moins un trait qu'aucune carte de leur bloc
  servi n'emploie ; référence P (blocs fictifs : cartes de P1, puis de P1 et P2, puis de P1 à P3).
- **Conditionnelle** : nombre de mondes complets où la première conditionnelle comptée est portée, par bras.
- **Dollars** (prix publics en principal, R-2977 ; pour Pr-2 le prix public est égal au prix de la configuration v12, 4 / 20 USD par
  million de jetons d'entrée / de sortie, [CRIBLE-V], table des proposeurs : la sensibilité « prix de la configuration » est vide,
  rapportée comme telle) : $_X(w) = somme des quatre sessions du bras X (le coût de P1 compte dans chacun des trois bras) ;
  **R_X** = Σ_w C_X(w) / Σ_w $_X(w), rapporté ; **ρ_SP = $_S / $_P** (II-7). Machine à part.
- **Sensibilités, rapportées sans verdict** : τ' = 0,25·I ; toutes les composantes ; mondes non complets réintégrés bras par bras
  (C = 0 pour une session non répondue, ses dollars comptés) ; δ_SP et δ_SQ recalculés sans les mondes où des cartes ont été
  retirées du bloc par la règle de taille (« Plan d'analyse ») ; écart de longueur entre blocs de S et de Q en covariable rapportée.
  **Rapportés aussi** : appels répondus, tronqués, en échec, par rang et par bras ; cartes servies et retirées ; octets servis par
  rang ; jetons et dollars par rang. Pertes et couvertures **par classe sommées sur les mondes**, jamais monde par monde dans un
  texte public. Information sur la composition, jamais un classement de proposeurs (N-058). Aucune moyenne ni médiane sur des
  jetons dans une sonde (il n'y en a pas).

## Seuil

- **Nombre de mondes : N = 20** ([NOTE] § 3 (ii) ; même règle que les cribles (iii) et (v), R-2992 ; aucune branche à 24 mondes).
- **Mondes complets, par comparaison principale** : un monde est complet pour SP si les sept appels de P et de S (P1 à P4, S2 à
  S4) sont répondus ; pour SQ, si ceux de S et de Q (P1, S2 à S4, Q2 à Q4) le sont. **Minimum** : n ≥ 16 mondes complets pour la
  comparaison ; sinon cette principale est « non concluante ». Taux de réussite par appel de Pr-2 au pilote : 4 répondus sur 4
  ([VERDICT-PC], `opus55`), information seulement. Probabilité d'atteindre le minimum (indépendance supposée, sortie, § 11) : à
  p = 0,99 par appel, 0,99 ; 0,98 : 0,89 ; 0,97 : 0,66 ; 0,95 : 0,23 ; (si l'on exigeait les dix appels du monde : 0,96 ; 0,70 ;
  0,37 ; 0,05 : d'où la complétude par comparaison).
- **Zone utile** : au moins 10 mondes complets pour SP où l'un des bras couvre au moins une composante comptée **et** l'un des
  bras en couvre moins que K(w) ; même définition pour SQ avec les bras S et Q et ses mondes complets ; sinon « hors de la zone utile » pour la principale touchée (aucune place pour un écart).
- **Consigne et taille** : réserve « blocs réduits » si la règle de taille a retiré des cartes dans plus de 4 mondes complets pour
  SP ; réserve « placebo mal apparié » si, dans plus de 4 mondes, la longueur d'un bloc de Q s'écarte de plus de 25 % de celle du
  bloc de S de même rang.
- **SP** : « **la série disperse** » si p ≤ 0,025 (bilatéral) et la somme des rangs signés de δ_SP est positive ; « **la série
  regroupe (grégarisme)** » si p ≤ 0,025 et elle est négative ; sinon « **non tranché** » (en particulier avec moins de 7 écarts non
  nuls).
- **SQ** : « **le contenu des cartes des pairs compte** » si p ≤ 0,025 et le signe est positif ; « **le contenu des cartes des pairs
  nuit** » si p ≤ 0,025 et il est négatif ; sinon « **non tranché** ».
- **Secondaire** (5 %, sans correction) : δ_QP : « effet de la seule présence » (signe dit) ou « non distingué ».

## Plan d'analyse

### Proposeurs (configuration v12 du pilote, inchangée ; variante « crédits de Claude au maximum »)

| poste | clé de configuration | crédits | rôle ici | attendu par appel (moyenne du pilote ; [NOTE] § 1 entre parenthèses) | plafond de session (bloc gelé) | borne de sortie | prix de la configuration (entrée / sortie) |
|---|---|---|---|---|---|---|---|
| Pr-2 | `opus55` | crédits de Claude | les quatre places des trois bras (200 appels) | 0,264334 (0,80) | 2,00 | 89 000 | 4 / 20 (public : 4 / 20) |

Identités : celles de la configuration v12 (`f69503dd…`, bloc gelé de [PILOTE], à travers [CRIBLE-III] et [CRIBLE-V]) ; aucun
identifiant de modèle ici (R-2598), hors la clé de configuration `opus55`, que le bloc gelé et les lignes de GO exigent (R-2690,
forme de [CRIBLE-III]). Réglages : ceux du bloc gelé (effort « high », réflexion comprise dans la sortie, aucun compte séparé,
[CRIBLE-III]). Pr-1, Pr-3 et Pr-4 ne servent pas. **Un seul fournisseur** porte les 200 appels : toute coupure ou toute limite de
débit touche tout le crible (liste d'arrêt, ligne « limite de débit » ; essai à blanc à cinq files).

### Gabarits

- **G0** (P1 à P4) : celui du pilote (`e77d3041…`, [CRIBLE-III]) : épisodes de développement, archive {K1}, grammaire servie, « au
  plus 3 conditions emboîtées », rien sur les conditions ni sur les sortes d'effets (R-2504) ; **avec E épisodes servis**, E fixé
  par la règle de taille ci-dessous (E = 400 au pilote ; si E < 400, G0 n'est plus exactement celui du pilote : dit, et le même E
  sert aux trois bras).
- **GS** (S2 à S4 et Q2 à Q4, même gabarit) : G0 à E épisodes, puis le bloc : un titre neutre, **vrai dans les deux bras** :
  « Cartes rendues par d'autres sessions (aucun verdict n'a été rendu sur elles) : », les cartes numérotées 1 à m_k sous leur forme
  canonique, puis la phrase de [RELEVÉ] § 3.2 : « Une carte presque identique à une carte déjà rendue sera regroupée avec elle. » ;
  puis la consigne de G0 (six cartes au plus), inchangée. Aucun mot sur ce que les cartes couvrent, sur leur qualité, sur les
  conditions ou les sortes d'effets ; aucune mention de « génération », de « monde » ni de « pairs ». Rédaction exacte figée au code,
  empreinte gelée, à contre-lire.
- La phrase du regroupement est servie **seulement** avec un bloc (S et Q) : P reçoit G0 tel quel. L'écart S − Q isole le contenu ;
  l'écart Q − P mêle la présence du bloc et la phrase (dit ; « Choix et doutes », point 4).

### Règle de taille (texte servi)

Sous la configuration v12, le code refuse avant l'appel tout texte dont le pire cas compté ((octets + 1 024) × prix d'entrée +
borne × prix de sortie) dépasse le plafond de session : pour Pr-2, **53 976 octets** au plus (sortie, § 2) ; la liste d'arrêt de
[CRIBLE-III] arrête au-delà de 53 000 octets. Le texte du pilote en prend jusqu'à 52 000 ([CRIBLE-III], « Devis » : « ≤ 52 000
octets servis ») ; sa taille réelle n'est pas dans [VERDICT-PC]. Un bloc de 18 cartes (rang 4) n'y tient donc pas sans réduction.
**Règle écrite d'avance** :
1. **Partie A** (processeur seul, ci-dessous) : |G0(E)|, taille en octets du texte de G0 à E épisodes, sur les 12 mondes de
   développement de [MR2], pour E ∈ {400, 350, 300, 250, 200} ; maximum sur les 12 mondes : M(E).
2. **Sonde des gabarits** (obligatoire, ligne propre, étape 2) : trois appels de Pr-2 sous G0 (E = 400) sur un monde de
   développement à graine publique ; c_max = plus grande taille canonique d'une carte valide de ces appels (jusqu'à 18 cartes).
3. **E** = la plus grande valeur de {400, 350, 300, 250, 200} telle que M(E) + 18 × 1,25 × c_max + |cadre du bloc| ≤ 52 000 octets
   (1 000 octets de marge sous la ligne d'arrêt de 53 000) ; si aucune ne convient : « **non lançable sous la configuration v12** »,
   nœud de la mère (« Choix et doutes », point 3) ; E est inscrit dans la version qui fera foi, avant tout appel du crible.
4. **À l'exécution**, si un texte de GS dépasse encore 53 000 octets, les cartes du bloc sont retirées **de la fin** (dernier
   emplacement de la dernière session) jusqu'à ce qu'il tienne ; m_k est alors le nombre de cartes gardées, le placebo du même rang
   est apparié à ce m_k ; chaque retrait est compté (réserve « blocs réduits », section « Seuil »). Jamais une carte n'est tronquée
   en son milieu.
5. Le quatrième appel de la sonde (rang 4, sous GS à E épisodes, bloc des cartes des trois premiers) vérifie la forme et les jetons
   (« Étapes »).

### Partie A — tailles des textes servis (processeur seul, avant tout appel ; descriptive)

Sur les 12 mondes de développement de [MR2] (régénérés par `generer_v4` à leurs graines publiques, empreintes contrôlées), texte de
G0 construit par le constructeur du code du pilote (copie gelée, nom neuf) pour E ∈ {400, 350, 300, 250, 200} : tailles en octets ;
aucun appel, aucune couverture, aucun proposeur. Rapporté sans critère ; sert la seule règle de taille. **Quand la machine n'est
plus chargée** (charge relevée à 13 à l'écriture de ce texte, `uptime`) : jamais pendant un chronométrage d'une autre session.

### Partie B — le crible

- **Mondes** : 20 mondes MR-2 du **secret du crible**, procédure de la machine comme [PROC-14] (secret engagé et poussé, phrase
  de Lazar, mondes et empreintes inscrits avant tout appel) ; jamais publiés, jamais réutilisés, jamais hors de la machine ;
  **séparés** de ceux des autres cribles (forme de R-2977 : pas de témoin commun).
- **Phase 1** (barrière) : les quatre sessions parallèles des 20 mondes, en **cinq files de quatre mondes** (le monde r va à la
  file r modulo 5, dans l'ordre croissant de r, fixé avant tout appel) ; une vague = un monde par file, ses quatre sessions
  ensemble (au plus 20 sessions à la fois) ; quatre vagues. **Aucun appel de la phase 2 avant que les 80 appels de la phase 1
  soient finis** (répondus, tronqués ou en échec) : les donneurs du placebo doivent exister.
- **Désignation de P1** : dans le monde r, P1 est la session parallèle d'indice u_r, tiré à la graine `(r, 50)` uniformément dans
  {1, 2, 3, 4}, avant tout appel, indépendamment de toute réponse. Si P1 n'est pas répondue : pas de phase 2 dans ce monde (aucune
  dépense de plus ; monde non complet pour SP et SQ) ; P reste rapporté.
- **Phase 2**, par file, mondes l'un après l'autre (le monde suivant d'une file part quand les six appels du monde en cours sont finis) : tour 2 : S2 et Q2 ensemble ; à la fin de S2 : tour 3, S3 et Q3 ; à la fin de
  S3 : tour 4, S4 et Q4. **Règle de chaîne** : si S_k n'est pas répondue, ni S_{k+1} ni Q_{k+1} ne partent (le bloc du rang
  suivant ne serait pas celui du dessin ; dépense épargnée) ; le monde n'est complet ni pour SP ni pour SQ. Une Q_k non répondue
  n'arrête pas la chaîne de S (SP reste possible dans ce monde).
- **Donneurs du placebo** : dans le monde r, ordre des 19 autres mondes tiré à la graine `(r, 51)` (permutation uniforme) ; le bloc
  de Q_k = les m_k premières cartes valides des sessions **parallèles** du premier monde donneur, dans l'ordre P1, P2, P3, P4 de
  ce donneur puis par emplacement, **dont la longueur en octets est à ± 25 % de celle du bloc de S_k** et qui en a au moins m_k ;
  sinon, parmi les donneurs qui en ont au moins m_k, celui de longueur la plus proche (égalités par l'ordre tiré) ; compté ; **un donneur dont le texte servi de Q_k dépasserait 53 000 octets est écarté** (aucune carte n'est jamais retirée d'un bloc de Q_k : l'appariement en nombre tient) ; **si aucun donneur ne convient** (aucun n'a m_k cartes valides, ou tous dépassent 53 000 octets), Q_k ne part pas, le monde n'est pas complet pour SQ, le cas est compté et rapporté, la chaîne de S continue
  (réserve « placebo mal apparié » pour le seul repli sur la longueur la plus proche ; le cas « aucun donneur » est compté à part, sans cette réserve). **Jamais** une carte de S ou de Q, ni du monde r, n'entre dans un bloc de Q. Q_k part en même
  temps que S_k (m_k est connu à la fin de S_{k−1}).
- **Appels** : 10 par monde, 200 en tout (tous de Pr-2, sur crédits de Claude) ; aucune reprise, aucune bascule ; réponses brutes
  et témoins d'isolement scellés avant extraction ; empreinte de chaque texte servi au journal ; `CARTES.json` et `BLOCS.json`
  (composition de chaque bloc : sessions et emplacements sources, octets, cartes retirées) scellés.
- **Mesure** : `mesure_crible_ii_v1.py`, une seule fois, sur la machine ; sortie scellée avant toute lecture, sans devis de monde ;
  rapatriement comme [PROC-14] § 9 (jamais les mondes) ; réponses brutes sur une branche de travail, jamais sur `main` (R-2731).

### Graines (R9)

Racine : l'entier de l'empreinte sha256 du texte qui fera foi. `numpy.random.SeedSequence(entropy=racine, spawn_key=…)`, numpy
≥ 1.25 : désignation de P1 dans le monde r `(r, 50)` ; ordre des donneurs `(r, 51)` ; jeu public d'instances sans issue du monde
r pour le regroupement `(r, 52)` (4 000 instances, traits et sous-populations tirés par le tireur d'instances du module du monde
riche ; aucune issue) ; rééchantillonnage `(99, b)` ; essais et mutations `(97, k)`, liste à l'addendum. **Graine du monde r** :
fonction `graine_monde_pilote` de [PILOTE] avec l'étiquette neuve « crible-ii-v1 » (secret du crible, phrase de Lazar, empreinte du
texte scellé, r) ; tirages de `generer_v4` ; épisodes de développement : règle du bloc gelé, étiquette « crible-ii-v1 », les E
premiers servis ; oracle `cle("oracle-crible-ii", empreinte du devis du monde)`. Manifeste du run : `src/controle_ia/manifeste.py`.

### Étapes

0. **Code** sous des noms neufs : lanceur du crible (dérivé du lanceur v74 du pilote : deux phases et leur barrière, files, chaîne,
   désignation de P1, choix des donneurs, règle de taille), gabarit GS, sérialisation canonique des cartes, constructeur du bloc,
   `mesure_crible_ii_v1.py`, `lire_crible_ii_v1.py` (lecture gelée), programme de la partie A. **Essais** : cas sain et artefact
   pour chaque ligne de la liste d'arrêt (R5) ; constructeur du bloc éprouvé sur des cas écrits à la main (carte refusée, carte
   au-delà de six, appel tronqué, bloc trop long, donneur trop court, égalités de longueur). **Banc de mutations**, au moins : une
   carte non valide servie ; une carte de S servie à Q ; une carte du monde même servie à Q ; donneur choisi d'après une issue ou
   l'oracle ; P1 choisie d'après une réponse ; bloc tiré de la réponse brute entière (réflexion comprise) ; phase 2 lancée avant la
   barrière ; S_{k+1} lancée après une S_k non répondue ; titre du bloc différent entre S et Q ; coût de P1 compté dans un seul bras ;
   carte refusée comptée dans une couverture ; effet de K1 compté ; seuil à 0,05 au lieu de 0,025 pour les principales ; rangs
   moyens remplacés par des rangs ordinaires. Toutes tuées pour la raison attendue. Contre-lecture du code par un sous-agent neuf
   d'un autre modèle ; addendum d'empreintes scellé.
1. **Partie A** sur processeur (quand la charge le permet), sortie scellée, lue sans critère.
2. **Sonde des gabarits** (obligatoire : la règle de taille en dépend ; sur devis et ligne propre) : sur un monde de développement à
   graine publique, trois appels de Pr-2 sous G0 (E = 400), puis E fixé par la règle, puis un appel de Pr-2 sous GS de rang 4 portant
   les cartes valides des trois premiers ; vérifie l'extraction et la sérialisation des cartes, la taille du bloc, la forme des
   cartes du quatrième appel, les jetons ; ne lit aucune couverture. **Règles d'avance** : le quatrième appel tronqué, ou sans carte
   valide, ou refusé par la règle du pire cas → GS réécrit, nouvelle sonde sur nouvelle ligne, crible non lancé ; aucune valeur de
   E possible → « non lançable », nœud de la mère ; sinon les jetons lus refont l'attendu des rangs 2 à 4 (section « Devis », règle
   de mise à jour).
3. **Avant toute dépense du crible** : version qui fera foi (E, devis refait sur la sonde, puissance), contre-lue, scellée par
   `sceller_prereg`, recopiée sous `prereg/` ; lignes « calcul » inscrites par la mère.
4. **Machine** (procédure dérivée de [PROC-14], noms neufs, trois barrières), essai à blanc avec proposeurs scriptés et vraies
   pièces servies (deux phases, cinq files, chaîne, donneurs), puis les 200 appels.
5. **Mesure** une seule fois, sortie scellée, rapatriement, destruction par identifiant (R10), preuve d'absence.
6. **Lecture** gelée, puis sous-agent neuf (R13) ; audit de symétrie (R4) écrit avant le prononcé ; rapport ; **aucune adoption**.

### Comparaisons et corrections

Deux principales, SP (δ_SP) et SQ (δ_SQ), bilatérales à 0,025 chacune (Bonferroni). Secondaires à 0,05, sans correction : δ_QP ;
groupes (G_S − G_P, G_Q − G_P) ; copies (k_S, k_Q, k_P) ; conditionnelles ; traits neufs ; ρ_SP. Tout est apparié par monde. Un même monde peut être donneur du placebo de plusieurs mondes (ordres tirés indépendamment) : les écarts de SQ ne sont donc pas strictement indépendants entre mondes ; le test les traite comme indépendants, et le nombre de mondes servis par donneur est rapporté. Les
trois bras partagent P1 : une composante qu'elle porte est portée par les trois bras, et les écarts appariés ne dépendent que des
trois autres sessions de chaque bras ; dit.

### Taille

20 mondes ([NOTE] : puissance 0,80 pour une part passant de 0,05 à 0,40 à 20 mondes, test de Fisher, annexe A de [NOTE] ; ce n'est
pas la statistique de ce texte). **Puissance de SP et de SQ** dans un modèle simple (écarts de 0 ou ± 1 composante par monde, test
des signes, auquel le test des rangs signés se réduit quand tous les écarts non nuls valent ± 1 ; 20 mondes complets ; bilatéral
0,025 ; sortie, § 10) : 0,11 si 30 % des mondes gagnent une composante et 10 % en perdent ; 0,27 à 40 % et 10 % ; 0,47 à 50 % et
10 % ; 0,33 à 35 % et 5 %. **Crible d'un grand effet** : un « non tranché » ne dit rien d'un petit effet ; c'est l'issue la plus
probable et celle que prédisent II-1 et II-2. La puissance sous un modèle plus fin (écarts de 0 à ± 3, rangs moyens) se
recalculera, avant le scellement, par simulation sur processeur sous le modèle de proposeurs synthétiques de [MR2] (programme sous
un nom neuf, scellé avant son lancement ; graines `(96, s)`, 10 000 tirages par cellule ; aucune donnée de crible), quand la machine
n'est plus chargée ; elle ne change ni N ni aucun seuil.

## Critères de lecture gelés

Lecture dans cet ordre ; un étage 0 arrête la lecture ; les étages 1 et 3 arrêtent la lecture de la principale qu'ils touchent.

| étage | observé | verdict |
|---|---|---|
| 0 | une ligne d'arrêt déclenchée, **sauf** la ligne « mondes complets atteignables < 16 », dont l'issue est celle de l'étage 1 ; la mesure en erreur | « **non jugeable (arrêt)** » : aucune issue lue |
| 1 | n < 16 mondes complets pour SP (resp. SQ) | SP (resp. SQ) « **non concluant** » ; causes rapportées ; l'autre principale est lue si elle a ses 16 mondes |
| 2 | réserve « blocs réduits » ; réserve « placebo mal apparié » ; 3 appels tronqués ou plus dans un même bras (borne de sortie de Pr-2 : 89 000 jetons) | SP et SQ lus et rapportés **sous la réserve nommée** ; sous « placebo mal apparié », la phrase « le contenu des cartes des pairs compte » est **interdite** (SQ mêlerait le contenu et la longueur) ; sous « blocs réduits », δ_SP et δ_SQ sans les mondes réduits sont lus avec le principal, et si l'issue diffère, elle est qualifiée « sensible à la taille des blocs » et rien de plus n'en est conclu |
| 3 | zone utile manquée | « **hors de la zone utile** » |
| 4 | SP | « la série disperse » / « la série regroupe (grégarisme) » / « non tranché » |
| 5 | SQ | « le contenu des cartes des pairs compte » / « le contenu des cartes des pairs nuit » / « non tranché » |
| 6 | δ_QP | « effet de la seule présence » (signe dit) / « non distingué » |
| 7 | groupes, copies, apport par rang, traits neufs, conditionnelles, sensibilités, coûts | rapportés, sans verdict |

**Lecture de H-ii et des trois lectures de [NOTE].** [NOTE] lit « **dispersion** si série > parallèle et placebo ≈ parallèle ;
**grégarisme** si série < parallèle ; **effet de contexte** si placebo ≈ série ». Traduction gelée ici, sans équivalence
statistique (20 mondes ne la permettent pas) :
- étage 4 « disperse » et étage 5 « compte » : « **dispersion par le contenu des cartes des pairs** » ; **sauf** si l'étage 6 donne « effet de la seule présence » de signe négatif (Q < P : le placebo égare, la condition « placebo ≈ parallèle » de [NOTE] n'est pas tenue) : lecture « **dispersion, contenu et égarement du placebo non séparés** », et la phrase « le contenu des cartes des pairs compte » n'est plus employée seule (même interdiction que sous « placebo mal apparié ») ;
- étage 4 « disperse » et étage 5 « non tranché » : « **dispersion, contenu non distingué de la seule présence** », lue avec
  l'étage 6 ; si l'étage 6 donne « effet de la seule présence » de même signe : « **effet de contexte** » ;
- étage 4 « regroupe » : « **grégarisme** », qualifié de même par les étages 5 et 6 (« par le contenu » si l'étage 5 dit « nuit ») ;
- étage 4 « non tranché » : « non tranchée » ; les étages 5 et 6 sont rapportés, sans conclusion sur H-ii ;
- étages 4 et 5 de signes contraires : « **lecture incohérente** », rapportée sans conclusion.
Aucun proposeur d'une autre maison n'est mesuré : toute lecture porte sur les sessions d'un seul proposeur (« Hypothèse »).
**Rien n'est adopté** : mettre des cartes de pairs dans la vue de l'organisme est un dessin neuf et un nœud de Lazar (l. 339 ;
N-045 point 1 : la composition est apprise, non fixée par un crible ; N-058).

**Audit de symétrie (R4)**, écrit avant le prononcé pour toute issue : textes servis de S_k et de Q_k égaux à l'octet hors du bloc
de cartes, monde par monde ; blocs reconstruits depuis les réponses brutes scellées (contrôle indépendant de l'extraction) ; aucune
carte de S, de Q ni du monde même dans un bloc de Q (contrôle sur `BLOCS.json`) ; désignation de P1 et ordre des donneurs rejoués
depuis les graines ; attribution relue sur trois cartes par bras et par monde ; regroupement rejoué sur trois mondes (graine dérivée
de l'empreinte de `CARTES.json`) ; dollars rapprochés des journaux du relais. **« Trop propre »** : |δ_SP| ≥ 2 ; k_S = 0 avec
k_P ≥ 0,3 ; toutes les prédictions vraies. **« Tout négatif »** : un bras à couverture nulle partout ; cartes des rangs 2 à 4
identiques à l'octet à des cartes servies ; couvertures égales dans les trois bras dans tous les mondes. Même relecture écrite,
par un sous-agent neuf.

## Liste d'arrêt

Chaque ligne a son essai sain et son artefact, écrits et passés avant l'addendum d'empreintes (R5) ; aucun repli silencieux.

| condition | action | essai sain | artefact |
|---|---|---|---|
| empreinte différente : texte, monde, gabarit G0 ou GS, configuration, programme, module importé ; texte servi de plus de 53 000 octets après la règle de taille | arrêt avant tout appel (avant cet appel pour la taille) | pièces conformes | un octet changé dans GS : refus nommé ; un texte de 53 001 octets : refus nommé |
| configuration autre que v12 | arrêt avant tout appel | v12 acceptée | borne de Pr-2 changée : refus |
| relevé de la sonde v74 (configuration v12, déjà jouée) absent, invalide ou d'une autre configuration : exigé sans condition | refus avant tout dossier | relevé conforme | relevé d'une autre configuration : refus |
| relevé de la sonde des gabarits du crible absent, ou E non inscrit dans le texte qui fera foi | refus avant tout dossier | relevé et E présents | E absent : refus |
| monde sans tirage conforme en 8 ; C-16 ou C-17 en défaut | arrêt avant tout appel | mondes conformes | monde forcé non conforme : arrêt |
| un appel de la phase 2 avant la fin des 80 appels de la phase 1 | arrêt ; défaut | barrière tenue | S2 lancée à la vague 3 : refus |
| texte servi de S_k différent de GS et du bloc reconstruit des cartes valides de P1, S2, …, S_{k−1} | arrêt avant cet appel | texte égal | un mot de la réflexion de S2 dans le bloc de S3 : arrêt |
| bloc de Q_k contenant une carte de S, de Q ou du monde même, ou un nombre de cartes autre que m_k, ou un donneur autre que celui de la règle | arrêt avant cet appel | bloc conforme | carte de S2 servie à Q3 : arrêt |
| textes de S_k et de Q_k différents hors du bloc | arrêt avant l'appel de Q_k | égalité à l'octet | titre changé pour Q : arrêt |
| P1 désignée autrement que par la graine `(r, 50)` ; ordre des donneurs autrement que par `(r, 51)` | arrêt ; défaut | graines conformes | P1 prise comme la première répondue : refus |
| S_k non répondue | ni S_{k+1} ni Q_{k+1} ; monde non complet ; compté | chaîne conforme | S2 sans carte valide : aucun appel de rang 3, compte juste |
| P1 non répondue | aucune phase 2 dans ce monde ; compté | P1 répondue : phase 2 | P1 tronquée : aucun appel de phase 2, compte juste |
| aucun donneur ne convient pour Q_k (moins de m_k cartes valides, ou texte de plus de 53 000 octets) | Q_k ne part pas ; monde non complet pour SQ ; compté ; aucun repli silencieux | un donneur convient : Q_k part | tous les donneurs à moins de m_k cartes : aucun appel de Q_k, compte juste |
| réponse brute ou témoin d'isolement absent | arrêt (code 3), pièces versées | pièces présentes | témoin supprimé : arrêt |
| coût d'un appel au-dessus de son pire cas (plafond de session, 2,00) | arrêt (code 3), dépense comptée | coût sous le pire | relevé gonflé : arrêt |
| dépense du relais atteignant sa part (`opus55` 400 pour le crible, 8 pour la sonde ; machine 3 USD) | arrêt ; jamais de ligne d'extension | part non atteinte | part atteinte en essai : arrêt |
| mondes complets obtenus + mondes en cours (comptés comme pouvant devenir complets) + mondes non commencés < 16 **pour SP et pour SQ à la fois**, quelle qu'en soit la cause ; évalué à chaque fin de monde de la phase 2 et à la fin de la phase 1 ; à l'instant 0 : 20 | arrêt du crible ; « non concluant » ; dépense restante épargnée | démarrage : continue ; panne d'un appel : continue | P1 tronquée dans 5 mondes à la phase 1 : arrêt avant la phase 2 |
| couverture comptant une carte refusée, tronquée, au-delà de six, non évaluable, ou l'effet de K1 | arrêt ; défaut | cartes valides seules | carte au-delà de six injectée : refus |
| exception de la mesure (pas un refus nommé) | rien n'est lu ; correction sous un nom neuf, contre-lue, scellée ; mêmes entrées | mesure conforme | division par zéro forcée : arrêt sans sortie |
| lecture avant le scellement de la sortie ; mesure lancée deux fois | run invalide | une sortie scellée | seconde mesure : refus |
| toute dépense sans ligne « calcul » inscrite citant GO-2026-11-15-06 | interdit | ligne présente | ligne absente : la commande refuse |
| minuterie : moins du pire cas restant (4 × 900 s de phase 1 non jouée + 4 × 3 × 900 s de phase 2 par file) + 2 h avant l'échéance, au départ ; ensuite, à chaque monde, moins de 3 × 900 s + 2 h | arrêt (A) sans nouvel appel ; mondes commencés finis, les autres non commencés | marge suffisante | échéance proche simulée : arrêt |
| un appel dépasse sa borne de 900 s | appel coupé, compté « en échec » ; règle de chaîne ; les autres files continuent | appel de 2 min | appel scripté de 1 000 s : coupé |
| erreurs de limite de débit sur plus de 5 % des appels du fournisseur, une fois au moins dix appels faits | arrêt (A) ; nœud de la mère, aucun repli silencieux | aucune erreur | 10 % d'erreurs scriptées : arrêt |

## Devis (brouillon 1 ; attendus sur les coûts mesurés du pilote par les règles de [CRIBLE-V] ; plafonds)

**Sources et règles.** Attendu par appel : moyenne arithmétique des coûts de **tous** les appels du pilote du proposeur, tels que
facturés (règle (b) de [CRIBLE-V]) : `opus55`, 1,057336 USD pour 4 appels ([VERDICT-PC], « Dépense rapprochée »), soit
**0,264334 USD** par appel, au prix public comme au prix de la configuration (sortie, § 1) ; fourchette par appel non transmise
([VERDICT-PC] ne donne que les totaux par proposeur : le plus petit coût d'un appel est au plus 0,264334, le plus grand au moins).
Pire cas : plafond de session du bloc gelé, 2,00 USD par appel (règle (a), inchangé). **Entrée supplémentaire des rangs 2 à 4** :
non mesurée par le pilote ; à texte servi total sous 53 000 octets par la règle de taille, le texte d'un rang 2 à 4 est de l'ordre
de celui du pilote ; l'attendu garde la moyenne du pilote et le **haut de fourchette** ajoute 0,05 USD par appel des rangs 2 à 4
(≈ 12 500 jetons d'entrée à 4 USD par million, **supposé**), à refaire sur la sonde. Machine : prix horaire relu au pilote,
0,052222 USD/h ([VERDICT-PC]) ; temps de machine du pilote hors appels 2 985,9 s (0,082018 / 0,052222 h moins la somme des 16 durées,
2 668,095 s ; sortie, § 0 ; [CRIBLE-III] donne 2 981 s, écart d'arrondi).

| ligne | appels | crédits | attendu (pilote) | haut de fourchette | pire (plafonds) |
|---|---|---|---|---|---|
| Pr-2, parallèle P1 à P4 (P1 commune aux trois bras) | 80 | Claude | 21,15 | 21,15 | 160,00 |
| Pr-2, série S2 à S4 | 60 | Claude | 15,86 | 18,86 | 120,00 |
| Pr-2, placebo Q2 à Q4 | 60 | Claude | 15,86 | 18,86 | 120,00 |
| machine (0,052222 USD/h relu au pilote) | — | hors | 0,06 (0,11 avec une heure de génération de mondes en plus) | 0,11 | 3,00 |
| **crédits de Claude** (crible) | 200 | | **52,87** (52,866680) | 58,87 | **400,00** |
| **hors crédits** (machine) | 0 | | **0,06 à 0,11** | 0,11 | **3,00** |
| **total du crible** | 200 | | **52,93** | 58,98 | **403,00** |
| sonde des gabarits, **obligatoire** (trois appels sous G0, un sous GS de rang 4, monde de développement) | 4 | Claude | 1,06 (1,057336) | 1,11 | 8,00 |
| partie A | 0 | — | 0 | 0 | 0 |
| **avec la sonde** | 204 | | **53,92 sur crédits ; 0,06 à 0,11 hors** | 60,09 (59,97 sur crédits) | **411,00** (408 sur crédits, 3 hors) |

Sortie, § 4 et § 6. **Part sur crédits de Claude** : 100 % des appels de proposeur ; seule la machine est hors crédits (elle ne peut
pas y être).

- **Écart à [NOTE]** : 200 appels au lieu de 240 (rang 1 commun : « Choix et doutes », point 2) ; Pr-2 au lieu de Pr-1 (variante) ;
  53,92 attendus avec la sonde au lieu de 63,30 ; 411 au pire au lieu de 483. L'attendu de [NOTE] (0,25 USD par appel de Pr-1,
  « estimé ») est à comparer à 0,264334 mesuré pour Pr-2 ; l'entrée supplémentaire de [NOTE] (« ≈ 3 000 jetons sur 120 appels »,
  3,00 USD) est remplacée par le haut de fourchette ci-dessus (6,00 USD sur 120 appels, supposé).
- **Forme fidèle à [NOTE] (Pr-1, hors crédits)** — information seulement, jamais un devis : rang 1 commun, 200 appels :
  24,72 attendus au prix public (123,58 au compte de la configuration, cinq fois le prix public, « la console fait foi », R-2803 ;
  [CRIBLE-V]), 471 au pire (plafond 2,34) ; 240 appels : 29,66 (148,30), 564,60 au pire (sortie, § 7). Ni l'une ni l'autre ne tient
  dans l'enveloppe aux textes actuels (sortie, § 8).
- **Forme de [NOTE] sur Pr-2** (240 appels, sans rang commun) : 63,44 attendus, 483 au pire, 491 avec la sonde : ne tient pas
  (cumul 1 331,67).
- **Plafond de 0,75** ([NOTE] § 4) : sans objet (Pr-1 ne sert pas) ; un plafond abaissé pour Pr-2 demanderait une configuration
  neuve (et le pire cas compté d'un appel de Pr-2 sous v12 est déjà 0,22 d'entrée + 1,78 de sortie) : non proposé.
- **Tronquage** (règle de [CRIBLE-III]) : non déclenchée pour Pr-2 : sortie du plus grand appel du pilote ≤ 52 867 jetons (tout son
  coût mis en sortie), sous 71 200 (80 % de 89 000) ; aucun appel tronqué de `opus55` au pilote (sortie, § 2).
- **Durée** (sortie, § 5) : appels de `opus55` au pilote de 36,425 à 109,396 s (moyenne 68,387), joués en série. **Borne par appel :
  900 s**, par la règle de [CRIBLE-V] (plus petit multiple de 300 s au moins égal à 1,5 fois le plus long appel répondu du pilote,
  tous proposeurs : 430,542 s) ; la même règle sur `opus55` seul donnerait 300 s, trop court pour des textes servis plus longs, non
  mesurés (« Choix et doutes », point 9). Phase 1 : quatre vagues, attendu ≈ 438 s (chaque vague comptée au plus long appel de
  `opus55` au pilote, par prudence), pire 3 600 s ; phase 2 : par file, quatre mondes de trois tours, attendu ≈ 821 s, pire
  10 800 s ; appels : ≈ 21 min attendues, **4 h au pire** ; **garde de départ : 6 h** (pire des appels + 2 h : mesure, rapatriement,
  poussée) avant l'échéance de la minuterie de 17 h ; plus la mise en place, la génération des 20 mondes (≈ 1 h sur 4 processeurs,
  estimation de [CRIBLE-V], brouillon 9) et les barrières. La latence sous vingt sessions à la fois n'est pas mesurée par le pilote,
  dont les appels se sont suivis. Temps d'agents : code, gabarit, essais, contre-lectures (plusieurs jours, non mesuré).

**Règle de mise à jour d'après la sonde des gabarits** (écrite d'avance) :

| chiffre de ce devis | lu à la sonde | nouvelle valeur |
|---|---|---|
| E (épisodes servis) | c_max (taille canonique de la plus grande carte valide) ; M(E) de la partie A | règle de taille, point 3 ; « non lançable » et nœud de la mère si aucune valeur |
| attendu des rangs 2 à 4 (0,264334 ; haut + 0,05) | coût du quatrième appel (rang 4), au prix public | attendu des rangs 2 à 4 = moyenne de 0,264334 et du coût lu, pondérée 4 contre 1 (quatre appels au pilote, un à la sonde) ; haut = le plus grand des deux plus 0,05 ; **pire cas inchangé** (plafonds) |
| sortie de Pr-2 (borne 89 000) | jetons de sortie des quatre appels de la sonde | si l'un dépasse 71 200 : réserve de tronquage annoncée à l'avance (étage 2) pour les bras qu'il écrit |
| N, mondes, appels, files, bornes | — | **inchangés** : 20 mondes, 200 appels, cinq files, 900 s par appel, garde de 6 h |
| lignes de GO (montants) | — | attendus refaits ; montants (plafonds) inchangés ; cumul tenu sous 1 275 USD, sinon nœud de Lazar (R-2992, point 3) |

Aucune autre valeur ne se refait ; un calcul qui demanderait de changer un seuil ou une règle donne un brouillon nouveau, contre-lu,
non une retouche. **Points non mesurés par le pilote**, à prendre à la sonde : taille d'une carte sérialisée, octets réels du texte
servi, jetons d'entrée et de sortie sous GS, forme des cartes d'une session qui voit un bloc.

## Lignes de GO proposées, non inscrites (inscription par la mère, dans l'enveloppe de GO-2026-11-15-06)

```
| GO-AAAA-MM-JJ-NN (κii1) | AAAA-MM-JJ | calcul | Organisme d'idéation, crible (ii) « proposeurs en série » (chaque session neuve voit les cartes brutes des précédentes ; bras parallèle, série et série placebo à cartes d'un autre monde), variante « crédits de Claude au maximum », part sur crédits de Claude : proposeur `opus55` (Pr-2, plafond de session 2 USD, part 400), 200 appels (dix par monde, rang 1 commun aux trois bras), effort « high » envoyé (bloc gelé du pilote) ; 20 mondes MR-2 du secret du crible, jamais publiés ni réutilisés ; archive {K1}, une génération ; gardien mécanique seul, aucun juge, aucun test de mort ; mesure gelée une seule fois ; conditions toutes exigées : coûts du pilote MR-2 mesurés et devis refait sur la sonde des gabarits, nombre d'épisodes servis inscrit, préenregistrement du crible contre-lu et scellé, code et gabarit contre-lus et gelés, essai à blanc réussi à cinq files, mondes vérifiés et leurs empreintes inscrites ; plafond du relais égal à sa part ; coût au-dessus du pire cas = arrêt ; essayé, non adopté ; jamais de ligne d'extension ; arrêt par identifiant (R10) | 400 USD (sur crédits) | 2026-11-30 | Lazar | GO-2026-11-15-06 ; R-2851 ; R-2875 ; ce texte |
| GO-AAAA-MM-JJ-NN (κii2) | AAAA-MM-JJ | calcul | Même crible, part hors crédits : machine jetable seule, 3 USD ; mêmes conditions que la ligne κii1 | 3 USD | 2026-11-30 | Lazar | GO-2026-11-15-06 ; R-2851 ; R-2875 ; ce texte |
| GO-AAAA-MM-JJ-NN (κii0, obligatoire) | AAAA-MM-JJ | calcul | Sonde des gabarits du crible (ii), sur crédits de Claude : trois appels de `opus55` sous le gabarit du pilote, puis un sous le gabarit à cartes servies (rang 4), sur un monde de développement à graine publique ; aucune couverture lue ; relevé versé ; une seule exécution | 8 USD (sur crédits) | 2026-11-30 | Lazar | GO-2026-11-15-06 ; ce texte |
```

Mots exigés par le lecteur gelé des lignes : à fixer avec le code (forme du pilote : « crédits de Claude », « hors crédits ») ;
montants : pires cas (plafonds × appels), inchangés par la sonde ; attendus : κii1 52,87 USD (haut 58,87), κii2 0,06 à 0,11, κii0
1,06. **Enveloppe** (R-2992, point 3 ; sortie, § 8) : aucune ligne « calcul » de `registres/go.md` ni aucune ligne de
`registres/depenses.md` ne cite GO-2026-11-15-06 à l'écriture de ce texte : **rien n'est engagé** sous l'enveloppe ; aux textes
actuels — (iii) 270 (version qui fera foi v1, sonde comprise), (v) 204,67 (version qui fera foi v2, sonde neuve comprise), (i) 123
et (iv) 243 ([NOTE] ; leurs préenregistrements sont en rédaction cette nuit, R-3053, non lus) — il reste 434,33 USD pour (ii) ;
**ce crible y tient** (411, cumul 1 251,67, marge 23,33). Si (i) ou (iv) montent de plus de 23,33 USD au-dessus de [NOTE], le
dernier crible inscrit n'y tiendra pas : nœud de Lazar à ce moment. Attendus : 53,92 pour ce crible avec la sonde, contre 63,30 à
[NOTE] et 247,20 pour les cinq à GO-2026-11-15-06.

## Écarts, nœuds et ce que le crible ne décide pas

- **Rang 1 commun** (écart à [NOTE], qui prévoit trois bras de quatre sessions, 240 appels) : la session de rang 1 de S et de Q ne
  voit aucune carte, son texte servi est celui d'une session parallèle ; elle est donc **une** des quatre sessions de P, désignée par
  graine ; 40 appels de moins, 80 USD de moins au pire ; prix : les trois bras partagent une session (dit ; les écarts appariés n'en
  souffrent pas, la variance des écarts baisse).
- **Variante « crédits de Claude au maximum »** (consigne de Lazar, l. 339 ; forme retenue par la mère pour (iii), R-2992) : Pr-2 au
  lieu de Pr-1 ; ce qu'elle change à la question : « Hypothèse » (dit, non tranché) ; un seul fournisseur porte les 200 appels.
- **Ordre tiré à graine scellée** ([NOTE]) : sans objet à un seul proposeur (les quatre places sont échangeables) ; seule la
  désignation de P1 est tirée. La version « composition » (proposeurs différents, ordre tiré) n'est pas jouée ; à proposer à part.
- **Épisodes servis** : si la règle de taille fixe E < 400, la vue des trois bras n'est plus celle du pilote ; le témoin positif du
  pilote (14 sur 14) ne vaut alors que pour E = 400 (dit dans le rapport).
- **Phrase du regroupement** ([RELEVÉ] § 3.2) servie avec le bloc seulement ; [NOTE] dit « avec la phrase factuelle du
  regroupement » : lue ici comme la phrase du relevé, **non** comme une liste de groupes calculée (« Choix et doutes », point 4).
- **Donneurs du placebo** : sessions **parallèles** des autres mondes du crible (même proposeur, même génération, même gabarit G0) ;
  le placebo de rang k part avec S_k, apparié en nombre de cartes et en longueur au bloc de S_k ([NOTE] : « même nombre de cartes, de
  même longueur, tirées d'un autre monde de la famille ») ; les cartes d'un autre monde peuvent égarer (« Hypothèse », (iii)).
- **[RELEVÉ] § 3.2** parle de « deux générations » (coût « quelques centaines de dollars ») ; [NOTE] et ce texte : **une**
  génération ; l'effet sur l'héritage d'une génération n'est pas mesuré.
- **Dessin neuf** : des cartes de pairs entrent dans la vue ([NOTE] § 7, point 3) : **essayé, non adopté** (l. 339).
- **Réserve de lignée** (dite) : le rédacteur de ce texte est de la même maison que le proposeur ; le crible n'a aucun juge et se
  mesure par l'oracle sur les cartes brutes ; le gabarit GS, écrit dans cette maison, est contre-lu avec le code.
- **N-058** : l'ordre et les donneurs sont tirés au hasard, jamais choisis sur un résultat ; aucun proposeur n'est choisi ni classé ;
  série contre parallèle jugés sur l'oracle et le coût ; la composition reste un nœud. **N-045 (1)** : première mesure de « l'ordre et
  la forme des échanges » ; **(7)** : Q sépare le contenu de la présence. **N-044** : famille de conception MR-2 ; aucune conclusion
  hors de MR-2.
- **Ne décide pas** : la qualité des idées ; les générations suivantes ; l'échange entre proposeurs différents ; l'effet sur le juge
  (aucun juge) ; une forme plus riche de partage (verdicts, groupes calculés) ; toute revendication publique (N-067).

## Antériorités à chercher (R8 : zone vierge = question)

[RELEVÉ] § 6 range les proposeurs en série « sans verdict » parmi les idées **isolées mais originales** « à mon jugement » ; [RELEVÉ]
§ 3.2 dit que « les échanges entre agents sont occupés » ([CAT] C1). Zone séduisante, à vérifier plus durement. À lire sur PDF
empreinté avant toute phrase de nouveauté ; **aucun chiffre** n'en est tiré ici (R7) :
- voisins dans le dépôt : [CAT] C1 (Co-Scientist : tournoi et débats entre hypothèses) ; [CAT] C5 (Fork-and-Flush : trajectoires
  parallèles à contexte neuf qui héritent d'un espace de travail) ; [CAT] C6 (« Scaling Discovery Requires Forgetting » : équipe
  d'agents dont l'état est périodiquement jeté) — non lus sur PDF par l'auteur ;
- fixation par l'exemple dans la conception humaine (exemples servis qui réduisent la diversité des idées produites ; travaux
  classiques de psychologie de la conception) — **à chercher**, références non relevées par l'auteur ;
- homogénéisation des sorties de modèles de langue quand on leur sert des exemples ou les sorties d'autres modèles, conformité et
  convergence dans les débats à plusieurs agents — **à chercher** ;
- génération itérative avec mémoire de ce qui a déjà été proposé dans les boucles évolutives à modèles de langue (par exemple
  FunSearch, Nature, 2024 ; AlphaEvolve, 2025 : programmes antérieurs servis dans la consigne) — **à vérifier** ;
- diversité par « recherche de nouveauté » et « qualité-diversité » (archives servies pour s'en écarter) — **à vérifier** ;
- CADS (arXiv 2610.24597 ; N-067, § 6 ; PDF sur une autre branche, non lu par l'auteur) pour la contribution d'un proposeur.

## Choix et doutes soumis à la mère

1. **Forme du crible** : variante « crédits de Claude au maximum » (Pr-2 aux quatre places) **recommandée** (confiance 0,6) :
   conforme à la consigne de Lazar (l. 339) et au choix de R-2992 pour (iii) ; tient dans l'enveloppe ; Pr-2 a répondu 4 sur 4 au
   pilote. Forme fidèle (Pr-1) : 2,1 fois moins chère au prix public (0,123581 contre 0,264334 par appel) mais hors crédits, compte
   de la configuration cinq fois plus haut, plafond de 2,34, barème public promotionnel jusqu'au 30 novembre ([CRIBLE-V]) ; et elle
   ne tient pas dans l'enveloppe (471 au pire).
2. **Rang 1 commun** : **recommandé** (confiance 0,7) ; sans lui (240 appels), ni la variante (491 avec la sonde) ni la forme fidèle
   ne tiennent dans l'enveloppe aux textes actuels.
3. **Taille des textes servis — nœud de faisabilité.** Options : (a) **règle de taille** (E épisodes servis réduit à tous les bras,
   fixé par la sonde ; cartes retirées de la fin au-delà de 53 000 octets) — **recommandée** (confiance 0,55) : aucune configuration
   neuve, la vue reste égale entre bras ; inconvénient : la vue n'est plus celle du pilote si E < 400 ; (b) configuration neuve
   (plafond de session de Pr-2 relevé pour les rangs 2 à 4) : vue du pilote gardée ; inconvénients : code et sonde v74 neufs, pire
   cas plus haut (un plafond de 3,10, valeur d'exemple non dérivée d'un texte servi, aux 120 appels des rangs 2 à 4 porterait le crible à 535 au pire : 80 × 2,00 + 120 × 3,10 + 3, sonde non comprise, hors de l'enveloppe ; le plus haut plafond que l'enveloppe permet à ces 120 appels est 2,19, soit (434,33 − 160 − 8 − 3) / 120, et il autoriserait ≈ 101 000 octets servis sous la règle du code, contre 53 976 ; l'option (b) n'est donc hors de l'enveloppe qu'à 3,10, non par nature) ; (c)
   cartes servies sous une forme résumée (traits employés, forme de la loi) : petit bloc ; inconvénient : ce ne sont plus des
   cartes **brutes**, la question change. Valeurs exactes de E à fixer après la partie A et la sonde.
4. **Phrase du regroupement** : celle du relevé, servie avec le bloc seulement ; alternative : la servir aussi à P (sans cartes, la
   phrase n'a pas d'objet) ; ou servir une liste de groupes calculée (verdict mécanique, s'écarte de « sans verdict »).
5. **Placebo** : donneurs parmi les sessions parallèles des autres mondes, appariement à ± 25 % des octets ; Q_k part avec S_k ; à
   contre-lire (tolérance de 25 % : choix de pratique).
6. **Décision par le test exact des rangs signés** (fidèle à [NOTE]) plutôt que par l'intervalle par rééchantillonnage (forme de
   [CRIBLE-III]) ; l'intervalle est rapporté. À contre-lire.
7. **Complétude par comparaison** (sept appels) plutôt que par monde (dix) : probabilité d'atteindre le minimum 0,89 contre 0,70 à
   0,98 par appel (sortie, § 11).
8. **Deux principales à 0,025** : SQ pourrait être secondaire (SP seule à 0,05 : puissance un peu plus haute) ; recommandé : deux
   principales, parce que [NOTE] lit trois issues qui demandent S contre Q.
9. **Borne de 900 s par appel** et cinq files : choix à contre-lire ; garde de départ 6 h.
10. **N = 20** : puissance basse (0,11 à 0,47 dans le modèle simple) ; 24 ou 30 mondes coûteraient 80 à 200 USD de plus au pire,
    hors de l'enveloppe.
11. **Un seul fournisseur** pour 200 appels : 20 sessions à la fois en phase 1 ; l'essai à blanc et la ligne « limite de débit »
    deviennent décisifs ; **solde de crédits de Claude** à couvrir : 408 USD au pire (53,92 attendus), en plus des autres usages :
    à vérifier par la mère.
12. **Jeu public d'instances sans issue** pour le regroupement : 4 000 instances par monde, graine `(r, 52)` ; nombre à contre-lire.

## Contre-lecture

- **Contre-lecture 1** (R2, tour 1, sur le brouillon 1) — sous-agent neuf, d'un autre modèle que l'auteur, qui n'a écrit ni ce
  texte, ni [NOTE], ni [CRIBLE-III], ni [CRIBLE-V], ni [PILOTE]. Texte relu :
  `docs/notes/organisme-idees-juge-v1/cribles-v1/crible-ii-brouillon1.md`,
  `816a072f6c9192049f325661e7b0ea2f0530dc1f738c4c39b8e75fba62364609` ; rapport :
  `docs/notes/organisme-idees-juge-v1/cribles-v1/contre-lecture-crible-ii-tour1-v1.md`,
  `72f98c9ed64f1ee267a40087a66efdceaa7425de903de1b676e8bda74af5365e`. Verdict : « corrections » (5 majeures, D1 à D5 ;
  5 mineures, m1 à m5 ; 42 couples ; second tour demandé sur ce brouillon 2). Corrections appliquées le 2026-11-17T01:31:15Z (`date -u`)
  par un rédacteur neuf, d'un autre modèle que l'auteur, qui n'a écrit ni le brouillon 1 ni le rapport, au moyen du programme
  `appliquer-corrections-crible-ii-brouillon2.py` (même dossier, scellé à côté ; différentiel `diff-crible-ii-b1-vers-b2.txt`, scellé) : les 42
  couples sont lus dans le rapport lui-même ; chaque « ancien » figure une seule fois dans le brouillon 1, sans chevauchement
  (vérifié par le programme). **Traitement**, point par point :
  - D1 (« P1 » et « P2 » nommaient à la fois des sessions et les deux comparaisons principales ; les comparaisons deviennent
    **SP** et **SQ**, les sessions gardent P1 à P4 ; couples D1.1 à D1.30) : **acceptée**, telle quelle.
  - D2 (lecture gelée « dispersion par le contenu » : cas d'un placebo qui égare, étage 6 de signe négatif ; couple D2.1) :
    **acceptée**, telle quelle.
  - D3 (cas non définis du placebo : aucun donneur à m_k cartes valides, ou texte de Q_k au-delà de 53 000 octets ; Q_k ne
    part pas, compté ; ligne d'arrêt neuve avec essai sain et artefact ; couples D3.1 et D3.2) : **acceptée**, telle quelle.
  - D4 (la pièce disait n'avoir lu que le témoin positif du pilote, alors que la section « Comptes » du verdict, lue, donne
    x = 0 sur 14 ; couples D4.1 et D4.2) : **acceptée**, avec **un écart déclaré** à D4.1 : l'« ancien » est allongé des deux
    mots qui le précèdent (« seul son »), écrits « seuls son », pour accorder « seul » avec ses deux sujets (« son témoin
    positif et le résultat principal sont lus ») ; aucun autre mot ne change.
  - D5 (option (b) du nœud de faisabilité chiffrée avec une valeur d'exemple de 3,10 ; plus haut plafond que l'enveloppe
    permet aux 120 appels des rangs 2 à 4 : 2,19, soit ≈ 101 000 octets servis ; couple D5.1) : **acceptée**, telle quelle ;
    la recommandation (a) du point 3 de « Choix et doutes » n'est pas changée (le rapport la laisse à la mère).
  - m1 (énoncé du test : 7 écarts non nuls nécessaires, suffisants s'ils sont tous du même signe ; la sortie de l'annexe A,
    imprimée par le programme, n'est pas changée) : **acceptée**.
  - m2 (les 52 000 octets sont dans la section « Devis » de [CRIBLE-III], non dans sa « Liste d'arrêt ») : **acceptée**.
  - m3 (zone utile définie aussi pour SQ ; les étages 1 et 3 n'arrêtent que la principale qu'ils touchent) : **acceptée**.
  - m4 (un même monde peut être donneur de plusieurs mondes : écarts de SQ non strictement indépendants, dit ; nombre de
    mondes servis par donneur rapporté) : **acceptée**.
  - m5 (le monde suivant d'une file part quand les six appels du monde en cours sont finis) : **acceptée**.
  - Remarques facultatives du rapport (section 5 : mot « brutes », annexe A, ligne de puissance à 16 mondes, légende des
    sigles) : **non appliquées**, aucune correction n'étant exigée ; à reprendre au tour suivant si la mère le veut.
  - **Non corrigé par le rapport, signalé sans rien changer** (à reprendre au tour 2) : la phrase du « Statut » « les
    prédictions sont écrites sans aucune donnée de proposeur sur la couverture », et celle de la section « Prédiction »
    « sans aucune donnée de couverture par appel », se lisent désormais à côté du résultat principal x = 0 sur 14 ajouté par
    D4 ; le titre de la section « Devis » garde la mention « brouillon 1 », qui nomme le devis et son programme, inchangés.
- **Contre-lecture 2** (R2, tour 2, sur le brouillon 2) — sous-agent neuf, d'un autre modèle que l'auteur (« modèle C » de
  cette pièce), qui n'a écrit aucune des pièces qu'il a lues (les brouillons 2 et 1, le rapport du tour 1, le verdict v2 du
  pilote en partie, le différentiel et le programme du brouillon 2). Texte relu :
  `docs/notes/organisme-idees-juge-v1/cribles-v1/crible-ii-brouillon2.md`,
  `fff278795f3ee4ba8a4f332bb80d687d7e2e773b55ebde2cabeae0e3912b7769` ; rapport :
  `docs/notes/organisme-idees-juge-v1/cribles-v1/contre-lecture-crible-ii-tour2-v1.md`,
  `ba2ecf66c6994cf8549fd8f12d554e8de82bea59f04bb45b680b1f371c9e6a71`. Verdict : « corrections » (aucune majeure ;
  3 mineures, m1 à m3, toutes de formulation ; 4 couples) ; les 42 corrections du tour 1 sont jugées appliquées fidèlement
  et l'écart déclaré à D4.1, légitime. Corrections appliquées le 2026-11-17T01:51:11Z (`date -u`) par un rédacteur neuf, d'un autre
  modèle que l'auteur (« modèle C », comme le lecteur), qui n'a écrit ni le brouillon 1, ni le brouillon 2, ni aucun rapport,
  au moyen du programme `appliquer-corrections-crible-ii-brouillon3.py` (même dossier, scellé à côté ; différentiel
  `diff-crible-ii-b2-vers-b3.txt`, scellé) : les 4 couples sont lus dans le rapport lui-même et appliqués tels quels ;
  chaque « ancien » figure une seule fois dans le brouillon 2, sans chevauchement (vérifié par le programme). **Traitement**,
  point par point :
  - m1 (« aucune donnée » de couverture, dans le « Statut » et dans la section « Prédiction », à côté du résultat principal
    x = 0 sur 14, qui est une donnée de couverture par appel d'une classe, celle des conditionnelles ; couples m1.1 et
    m1.2) : **acceptée**, telle quelle ; elle règle le premier des deux points que l'entrée « Contre-lecture 1 » signalait
    sans les corriger (le second, le titre de la section « Devis », est la remarque facultative (1) ci-dessous).
  - m2 (après D3.1, la parenthèse de la réserve « placebo mal apparié » suivait « la chaîne de S continue » et semblait
    couvrir le cas « aucun donneur », alors qu'elle se rapporte au repli sur la longueur la plus proche, la réserve étant
    définie par l'écart de longueur, section « Seuil » ; couple m2.1) : **acceptée**, telle quelle.
  - m3 (l'entrée « Brouillon 2 » de l'en-tête disait « rien d'autre » sans nommer le « Statut », la ligne du validateur ni
    l'accord « seuls son » de D4.1 ; couple m3.1) : **acceptée**, telle quelle ; l'entrée « Brouillon 3 » de l'en-tête
    nomme d'emblée tout ce que ce brouillon change.
  - Remarques facultatives (section 5 du rapport) : (1) le titre de la section « Devis » garde « brouillon 1 », qui nomme le
    devis et son programme, inchangés : rien à faire, rien de changé ; (2) les remarques facultatives du tour 1 restent non
    appliquées, aucune correction n'étant exigée ; (3) la citation du tour 2 dans un brouillon 3 est faite par la présente
    entrée.
  - Points « Pour la session mère » (section 6 du rapport : nœud de faisabilité, écarts à la note, marge de l'enveloppe,
    valeur de l'essai, compte rendu de l'auteur hors pièce, solde de crédits) : hors de la pièce, **aucun changement** ici ;
    ils restent à la mère ou à Lazar.
  - Mise en forme : une ligne vide est rétablie entre la fin de cette section et le titre de l'annexe A (perdue au
    brouillon 2) ; aucun mot ne change.

## Annexe A — comptes exacts (sans donnée de crible, sans tirage, sans appel)

Programme : `devis-crible-ii-brouillon1.py` (même dossier, empreinte dans son compagnon) ; commande : `nice -n 19 python3 -I
devis-crible-ii-brouillon1.py`, le 2026-11-17 à 00:53:32 UTC (`date -u`), Python 3.13.18, bibliothèque standard ; sortie
`devis-crible-ii-brouillon1-sortie.txt` (empreinte dans son compagnon), recopiée en entier :

```
§ 0. Contrôles de cohérence des entrées
appels 16 ; somme des durées 2668.095 s
machine du pilote 1.5706 h = 5654.0 s ; hors appels 2985.9 s
total des quatre proposeurs 15.220258 USD (verdict : 15,302276 avec la machine, sans les autres)
quatre proposeurs + machine 15.302276

§ 1. Attendu par appel (moyenne de tous les appels du pilote, règle (b) de [CRIBLE-V])
opus55 configuration 0.264334 ; public 0.264334 ; répondus 4 sur 4 ; part moyenne du plafond 0.1322
argon configuration 0.617905 ; public 0.123581 ; répondus 4 sur 4 ; part moyenne du plafond 0.2641
astra configuration 0.417938 ; public 0.417938 ; répondus 4 sur 4 ; part moyenne du plafond 0.1786
fable52 configuration 2.504888 ; public 2.504888 ; répondus 2 sur 4 ; part moyenne du plafond 0.8350

§ 2. Tronquage (règle de [CRIBLE-III] : plus grand appel au-dessus de 80 % de la borne de sortie)
opus55 sortie du plus grand appel <= 52867 jetons ; 80 % de la borne : 71200 ; règle déclenchée : False
opus55 octets servis au plus sous le plafond de session (règle du code, (octets + 1 024) x entrée + borne x sortie) : 53976
argon octets servis au plus sous le plafond de session (même règle, prix de la configuration) : 52976

§ 3. Appels du crible
variante, rang 1 commun (P1 sert aux trois bras) : par monde 10 ; en tout 200
forme de [NOTE], trois bras de quatre sessions : par monde 12 ; en tout 240

§ 4. Devis de la variante « crédits de Claude au maximum » (Pr-2 opus55 aux quatre places, rang 1 commun)
parallèle P1 à P4 80 appels : attendu 21.1467 ; haut 21.1467 ; pire 160.00
série S2 à S4 60 appels : attendu 15.8600 ; haut 18.8600 ; pire 120.00
placebo Q2 à Q4 60 appels : attendu 15.8600 ; haut 18.8600 ; pire 120.00
proposeurs (crédits de Claude) : attendu 52.8668 ; haut 58.8668 ; pire 400.00
sonde des gabarits (4 appels de opus55) : attendu 1.0573 ; pire 8.00

§ 5. Durées et machine
opus55 : moyenne 68.387 s ; plus long 109.396 s
plus long appel répondu du pilote (tous proposeurs) 430.542 s ; règle de [CRIBLE-V] : B_a = 900 s ; même règle sur opus55 seul : 300 s
phase 1 : attendu 437.6 s ; pire 3600 s
phase 2 (une file) : attendu 820.6 s ; pire 10800 s
appels attendus 1258.2 s ; pire des appels 14400 s = 4.000 h ; garde de départ (pire + 2 h) 6.000 h
machine attendue 0.061566 USD (temps hors appels du pilote compris) ; 0.113788 avec une heure de génération de mondes en plus ; 17 h : 0.8878 ; pire 3,00

§ 6. Totaux de la variante
crédits de Claude : attendu 52.8668 (haut 58.8668) ; pire 400.00
hors crédits (machine) : attendu 0.0616 à 0.1138 ; pire 3.00
total : attendu 52.9284 ; pire 403.00
avec la sonde : crédits attendu 53.9241 pire 408.00 ; total pire 411.00

§ 7. Formes écartées, information seulement
Pr-1 argon, rang 1 commun : attendu public 24.7162 ; configuration 123.5810 ; pire 471.00 (hors crédits)
Pr-1 argon, forme de [NOTE] : attendu public 29.6594 ; configuration 148.2972 ; pire 564.60 (hors crédits)
Pr-2 opus55, forme de [NOTE] (240 appels) : attendu 63.4402 ; pire 483.00
[NOTE] : 63,30 attendus, 483,00 au pire

§ 8. Enveloppe de GO-2026-11-15-06 (1 275 USD au pire)
(iii) version qui fera foi v1, sonde comprise 270.00
(v) version qui fera foi v2, sonde neuve comprise 204.67
(i) [NOTE] 123.00
(iv) [NOTE] 243.00
quatre autres : 840.67 ; reste pour (ii) : 434.33
(ii) variante, sonde comprise : 411.00 ; cumul 1251.67 ; tient : True
(ii) forme de [NOTE] sur opus55, avec sonde 491.00 ; cumul 1331.67 ; tient : False
(ii) Pr-1 rang 1 commun 471.00 ; cumul 1311.67 ; tient : False
(ii) [NOTE] 483.00 ; cumul 1323.67 ; tient : False

§ 9. Test des rangs signés exact (permutation des signes), seuil bilatéral
niveau 0.025 : au moins 7 écarts non nuls, tous du même signe (p = 0.01562)
niveau 0.050 : au moins 6 écarts non nuls, tous du même signe (p = 0.03125)

§ 10. Signe seul (écarts de 0 ou +-1) : seuil exact et puissance à n = 20, bilatéral 0,025
P(+1) = 0.30 P(-1) = 0.10 : puissance (côté +) 0.107
P(+1) = 0.40 P(-1) = 0.10 : puissance (côté +) 0.271
P(+1) = 0.50 P(-1) = 0.10 : puissance (côté +) 0.473
P(+1) = 0.35 P(-1) = 0.05 : puissance (côté +) 0.327

§ 11. Probabilité d'atteindre le minimum (16 mondes complets sur 20 pour une comparaison principale)
p par appel 1 : comparaison (7 appels) 1.0000 ; monde entier (10 appels) 1.0000
p par appel 0.99 : comparaison (7 appels) 0.9905 ; monde entier (10 appels) 0.9635
p par appel 0.98 : comparaison (7 appels) 0.8865 ; monde entier (10 appels) 0.7029
p par appel 0.97 : comparaison (7 appels) 0.6643 ; monde entier (10 appels) 0.3653
p par appel 0.95 : comparaison (7 appels) 0.2326 ; monde entier (10 appels) 0.0498
p par appel 0.90 : comparaison (7 appels) 0.0034 ; monde entier (10 appels) 0.0000
```

Notes de lecture : (1) au § 0, la mention « verdict : 15,302276 avec la machine, sans les autres » rappelle que le total des quatre
proposeurs et de la machine égale le total détaillé de [VERDICT-PC] (15,302276), hors l'épreuve des clés (0,001164) et la machine de
la tentative antérieure (0,074757), qui font 15,378197 ; (2) au § 2, « sortie du plus grand appel ≤ 52 867 jetons » est une borne :
tout le coût des quatre appels de `opus55` mis en sortie d'un seul ; (3) au § 5, la phase 1 compte chaque vague au plus long appel de
`opus55` au pilote (109,396 s), par prudence ; la phase 2 compte chaque tour à la moyenne (68,387 s) ; (4) au § 10, le modèle
« écarts de 0 ou ± 1 » est une simplification : avec des écarts de plusieurs composantes, le test des rangs signés diffère du test
des signes ; la simulation de la section « Taille » le refera.

## Citations obligatoires (N-064, N-067)

POPPER (Huang et al., ICML 2025 ; `docs/sources/pdf/huang-2025-icml-pmlr-267-popper-automated-hypothesis-validation-agentic-sequential-falsifications.pdf`,
`a3c4b370…`) ; Dwork et al., arXiv 1506.02629 (`dcfbb9aa…`) ; Blum et Hardt, « The Ladder », arXiv 1502.04585 (`957ef473…`) ;
Co-Scientist (Gottweis et al., Nature 655, p. 487-496, 2026 ; `351f49d8…`), voisin de la boucle générer-classer-faire évoluer et
des échanges entre agents de ce crible ; et la liste de `docs/decisions/decision-N-067-v1.md`, section 6, dont CADS (Chen et al.,
arXiv 2610.24597 : contribution incrémentale des proposeurs, cité par N-067 pour N-058, p. 7 ; PDF sur une autre branche, non lu par
l'auteur). Voisins nommés par les fiches, non lus sur PDF par l'auteur : Fork-and-Flush ([CAT] C5) et « Scaling Discovery Requires
Forgetting » ([CAT] C6). Empreintes et pages recopiées de [NOTE] (citations obligatoires), non revérifiées sur les PDF par
l'auteur. Aucune revendication n'est faite ici.

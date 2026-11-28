# Papier C — projet de traitement des contre-lectures du brouillon 5 du préenregistrement (HC1 à HC3) — v1

- **Qui** : préparateur neuf, sous-agent de la session 16. Je n'ai écrit ni le brouillon 5 ni les précédents, ni leur
  configuration, ni aucune contre-lecture, note de voisins ou vérification du verrou. Ce texte est un **projet** : la
  session le relit, le corrige et le scelle sous son nom, comme son traitement.
- **Heures** : le 2026-10-21, de 00:05 à 00:30 UTC environ.
- **Consigne** : `…/consigne-projet-traitement-contre-lectures-brouillon5-v1.md`
  (`9ef3e86a0feadc4f2ab0ef8dd9fd305b9ec53787242f5c38940efc3fe895281c`, égale à son compagnon).
- **Préfixe** `…/` = `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/papier-C` ; `R` =
  `/home/user/controle-ia-travail`, lu en lecture seule.

## Pièces lues (empreintes recalculées, toutes égales à leur compagnon `.sha256`)

| pièce | chemin | empreinte sha256 | lecture |
|---|---|---|---|
| brouillon 5 | `…/brouillon5/papier-C-preenregistrement-HC1-HC3-v1-brouillon5.md` | `9d55160f59cfb19e489dccc586e748173669b1373b570f5d42beb02293332969` | en entier |
| configuration brouillon 2 | `…/brouillon5/papier-C-config-v1-brouillon2.json` | `77252564163e25445421e932ff46b42634487ace242ac1861bb9f61586f07efb` | clés, types, comptes et nombres seulement |
| table du rédacteur | `…/brouillon5/table-traitement-brouillon5-v1.md` | `ebb763fadd96bc108ba803e737eba55b797b71c7517f94dbca41bfe1f84dea56` | en entier |
| lentille « texte et conformité » | `…/contre-lectures-brouillon5/texte/contre-lecture-R2-brouillon5-texte-v1.md` | `12879073de20e9129e1e555642ed85fb9a887d955fc5c9e2ac418552842a129b` | en entier |
| lentille « méthode statistique » | `…/contre-lectures-brouillon5/methode/contre-lecture-R2-brouillon5-methode-v1.md` | `0c492f0218c02e43aa35a8b296e6bb68f062d19525099593a56a92409a26fc0b` | en entier |
| simulations de la lentille méthode | `…/contre-lectures-brouillon5/methode/simulations/` (manifeste `sha256sums-simulations-methode-b5-v1.txt`) | manifeste `6f76e9dfab26c57c6d9384d7d70aeb1228c41b4a1a4dc9e79ba6dbeb4fd525d3` ; 27 fichiers conformes (`sha256sum -c`) | les 13 sorties ; scripts T2c, T2d et T3 |
| voisins Joswin et al., Hu et Qu | `…/contre-lectures-brouillon5/voisins/lecture-voisins-joswin-huqu-v1.md` | `55222cdb3278f59810586b2097817114c74825cc34b9dd7a12ad2a051a90b84d` | en entier |
| sept voisins de Panin | `…/contre-lectures-brouillon5/voisins-panin/lecture-voisins-panin-sept-v1.md` | `b3a6c18732013f1faf388bc051b62d3c83dd8dfb8c3e70363eddf0d9d77d8929` | en entier |
| voisins de second rang | `…/contre-lectures-brouillon5/voisins-second-rang/lecture-voisins-second-rang-v1.md` | `8027bd53f6030d1b289c5ad84c3b501a8c646e22a72f31be6e30a2912a56f81f` | en entier |
| vérification du verrou de la famille 1 | `…/verrou-famille1/verification-verrou-famille1-v1.md` | `0cbd3ae3050c5485d6e5415eb38eb9f51c07363a8e7f23e66f9925ed92132420` | en entier |
| traitement du brouillon 4 (forme) | `…/traitement-contre-lectures-brouillon4-papier-C-v1.md` | `f2c6a3604adfce293fa2e2bf232ae7305790d33b06eaf9a0af6d1efd5ef25da4` | en entier |
| registre des décisions | `R/registres/decisions.md` (état haché vers 00:10 UTC) | `436fdfb656aa6c4bbd04f9dec224d5f15e47de648f37ea79c6d5ff0d6addd6b9` | lignes P-019, P-020, R-294, R-307, R-308, R-309 |
| registre des GO | `R/registres/go.md` (même heure) | `1a392407391cef6ee501e61e90cb5bf73da8aec343f3e44da1c96fd67639f5d6` | GO-2026-10-17-01 ; GO-2026-10-20-06, -07, -09, -13, -14 |
| décisions | `R/docs/decisions/decision-N-005-N-006-v1.md` ; `decision-N-013-v1.md` ; `decision-N-023-v1.md` | `cd49afbc924cb1dd56251f22ef692007c24ecb76b124e0662cbe9bc04fa2e1c0` ; `157d388ef5d0f4dff00a5a1801316ed0677959a0709b4575b875e089d11ab7be` ; `1297f509a0fc324c2dd177b7402ac77b238601563156d992204dbc1796ea250d` | en entier |

Empreintes recalculées aussi, pour la liste des versements (section 5) : manifestes des dossiers de lecture (texte
`99cfc889…`, voisins `a4594214…`, voisins de Panin `19c41125…`, second rang `89763134…`, tous vérifiés par
`sha256sum -c`, aucun échec), brouillon 4, configuration brouillon 1, points ouverts, consignes, notes finales,
outils du rédacteur, mesures de conception v1, procédure `R/docs/procedures/T0.5-extraction-v1.md`
(`d23bd62fe1611b8737ccb38a404d96a41746158a7930bef0a065590bd072c26c`, égale à son compagnon).

## Ce que j'ai tenu ; écarts

- Écriture seulement sous `…/traitement-brouillon5/`. Python seulement en ligne (`python3 -B -I -c`,
  `PYTHONDONTWRITEBYTECODE=1`), sans fichier écrit. Aucune commande git. Aucun sous-agent, aucune dépense, aucun réseau,
  aucune clé affichée.
- Aucune recherche récursive : listes de dossiers nommés un à un (`ls`, sans récursion) ; `grep` dans deux fichiers
  nommés (`R/registres/decisions.md`, `R/registres/go.md`).
- Non lus, pas même pour une empreinte : `R/prereg/P3-consignes-v1.md`, tout fichier `textes-actions-*`,
  `items-textes-p1-v1.json`, `prompts-p1-v1.json`, tout fichier sous `R/donnees/`, `R/runs/`, `R/diag/`, `R/traces/`.
  Non lus aussi : les PDF ; `R/registres/etat.md` ; le dossier `…/contre-lectures-brouillon5/outils-texte/` (deux
  empreintes seulement) ; la lecture en cours `…/contre-lectures-brouillon5/voisins-cp02/` (liste du dossier seulement).
- Configuration : clés, types, longueurs, comptes et valeurs numériques ; plus des tests d'appartenance qui rendent des
  booléens (sept clés de graines attendues ; « en attente » dans les deux champs de décision). Aucune chaîne affichée ;
  aucun texte de formulation recopié ici.
- **Écart de chemin (R11)** : la consigne place deux lectures sous `…/voisins-panin/` et `…/voisins-second-rang/` ; elles
  sont sous `…/contre-lectures-brouillon5/voisins-panin/` et `…/contre-lectures-brouillon5/voisins-second-rang/`, avec
  les empreintes que la consigne donne.

## Conventions

- « **mots exacts : l. a-b** » : le rédacteur recopie les mots exacts de ces lignes du rapport nommé (scellé, empreinte
  ci-dessus). Je ne les retranscris pas : une transcription n'est pas opposable (R7) et ajouterait des erreurs de copie.
  Quand je modifie une correction, je l'écris en entier, en mots à moi.
- Identifiants : `texte-NN` (lentille « texte », constats 1 à 16) ; `CL5-NN` (lentille « méthode », CL5-methode-01 à 16) ;
  `CV-NN` (Joswin et al., Hu et Qu) ; `CP-NN` (sept voisins de Panin) ; `CS-NN` (second rang) ; `VF-NN` (vérification du
  verrou de la famille 1 ; numérotés ici).
- **Numéros des réserves nouvelles** (plan, section 7) : **14** = contingence (R-307 fixe ce numéro ; la déclaration de
  R-309 y entre) ; **15** = identification du calibrage (CL5-01, qui la numérotait 14) ; **16** = constat commun aux
  familles (CV-01, qui la numérotait 14). Toute mention « réserve 14 » dans les corrections de CL5-01 et de CV-01 se lit
  15 et 16.

## 1. Table

Décision proposée : « accepté », « accepté modifié » (la modification est dite), « écarté » (raison vérifiée dans une
pièce), « nœud de Lazar ». Où : texte, configuration, module, session (registre, versement, veille).

### 1.1 Lentille « texte et conformité » (rapport `12879073…`)

| constat | gravité | décision | où | correction |
|---|---|---|---|---|
| texte-01 : décisions P-019 et P-020 absentes des différences admises de la configuration | majeur | accepté | texte (champs du scellement, l. 97-99) ; configuration (`statut`) | mots exacts : l. 72-77 ; même phrase dans `statut` |
| texte-02 : le validateur ne voit pas les blocs de décision en attente | mineur | accepté | texte (l. 308, 321, 820, 828 ; 638, 646 ; verrou 1) | mots exacts : l. 86-89 ; même règle pour le bloc de CV-01 s'il est encore ouvert (section 6.1, point 3) |
| texte-03 : pièces citées absentes du dépôt ; verrou 5 incomplet | majeur | accepté modifié | texte (l. 17 ; l. 18-19 ; verrou 5) ; session (versements ; script de contrôle) | mots exacts : l. 103-110 ; **modification** : la liste ajoutée au verrou 5 est celle de la section 5 de ce projet (elle ajoute les rapports et notes de cette série, la vérification du verrou de la famille 1, les PDF des voisins cités, ce traitement) |
| texte-04 : contrôles d'avant le scellement sans marqueur ni entrée | mineur | accepté modifié | texte (verrou 2 ; section « Contre-lecture ») | contre-lecture 7 : mots exacts, l. 121-123. **Modification** : au lieu d'un seul `<<CHEMIN_NOTE_VOISINS_BIBLIO>>`, une ligne par note, avec ses marqueurs (CV-08, CP-06, CS-01), et pour la lecture en cours : « Voisins de second rang cités par les sept papiers de Panin (CP-02) : note `<<CHEMIN_NOTE_VOISINS_CP02>>` (`<<EMPREINTE_NOTE_VOISINS_CP02>>`), verdict par papier `<<VERDICT_VOISINS_CP02>>`. » ; à la fin du verrou 2 : « Pour chacune de ces notes, une collision, même partielle : nœud de Lazar avant le scellement. » |
| texte-05 : « toutes les statistiques des juges » sur la loi nette ; C-P3c sous-défini | mineur | accepté | texte (l. 290, l. 805, l. 316) ; configuration (`stabilite_rang.C_P3c`) | mots exacts : l. 132-137 ; la liste entre parenthèses suit P-019 telle que tranchée (section 3) |
| texte-06 : C-P4b sur la lecture complète, D₀ non défini, artefact non déclaré | majeur | accepté modifié | texte (C-P4b, l. 299, 495, 816 ; point 13 ; TC.2 (3) ; réserve 6 ; A8) | **remplacé par CL5-04**, le contrôle mécanique que ce constat demandait à la lentille méthode ; gardé de texte-06 : une exception écrite au point 13, après « (lecture principale, Plan, TC.2). » : « Exception : C-P4b se lit, des deux côtés, sur l'excédent du paragraphe à longueur fixe (TC.2, lecture (2)), D₀ de chaque côté sur les cellules S et H. » La réserve « effet d'agrégation possible sur d » n'est pas ajoutée : l'excédent la remplace |
| texte-07 : règles du pilote sans regroupement par tâche | mineur | accepté modifié | texte (point 18 ; plan 2, demi-largeur de λ) ; configuration (`derivation.demi_largeur_lambda`) | **Point 18 inchangé** : à 16 grappes, le rééchantillonnage par tâches sous-estime plus que celui des contenus (erreur type vraie 0,0443 ; par contenus 0,0423 ; par tâches 0,0385 ; `…/methode/simulations/t5_pilote_grappes_v1.txt`, `b1fc95bd…`) ; ligne déclarée, ajoutée à la fin du point 18 : « L'unité d'indépendance est la tâche (16 tâches au lot de calibrage) ; à 16 grappes, le rééchantillonnage par tâches sous-estime l'erreur type davantage que celui des contenus (contre-lecture méthode du brouillon 5, T5) : le pilote rééchantillonne les contenus, écart déclaré ; aucune grandeur du pilote n'entre dans un test décisif. » **Plan 2**, remplacer « formulations choisies sur une moitié des contenus de calibrage (tirage par la clé `papier-C/pilote/conception`), loi nette et erreur type de λ calculées sur l'autre moitié » par « formulations choisies sur les contenus de huit tâches du lot de calibrage (tirage des tâches par la clé `papier-C/pilote/conception`), loi nette et erreur type de λ calculées sur les contenus des huit autres tâches (erreur type par rééchantillonnage des contenus de ces huit tâches) ». Mise à l'échelle √((n_cal / 2) / n) inchangée ; vérification courte (section 6.3) |
| texte-08 : tirage des tâches de l'étape 2 incomplet | mineur | accepté | texte (plan 0, l. 529 ; modérateur raisonné, l. 698) ; configuration | mots exacts : l. 185-188 ; tirage uniforme, sans strate par origine (décision de la session ; l'origine est consignée et rapportée, réserve 12) |
| texte-09 : « des tâches neuves » inexact | mineur | accepté | texte (rappel, l. 52-53) | mots exacts : l. 196-197 |
| texte-10 : empreintes à compléter | forme | accepté modifié | texte (l. 180, 524 ; l. 149-152 ; l. 110-111 ; l. 124, 145-146) | mots exacts : l. 201-204 (empreinte `d23bd62f…`, revérifiée ici) et l. 208-210 (registres cités au commit du scellement) ; **modification** : `<<EMPREINTE_TACHES_SOURCE_64>>` reste un marqueur pour le rédacteur ; la session le remplit au scellement, avec « égale au champ `source.sha256` du fichier des 60 tâches », par un moyen que ses règles permettent (la lentille texte a ouvert pour cela des fichiers interdits : écart à consigner, section 4.3) |
| texte-11 : accords entre texte et configuration ; libellés | forme | accepté | texte (l. 418-419 ; l. 913, 918, 923, 928 ; l. 639-641) ; configuration (`pilote.usd_max_par_lancement`) | mots exacts : l. 214-222 ; nom retenu : `usd_borne_stricte_par_lancement` |
| texte-12 : bilan des 95 constats | information | accepté | — | aucune action |
| texte-13 : conformité aux décisions | information | accepté | — | aucune action |
| texte-14 : sortie du validateur | information | accepté | texte | au brouillon 6, la sortie de `problemes` montre aussi les marqueurs de texte-02, texte-04 et de ce traitement |
| texte-15 : P-019 et P-020 encore « à transmettre » au registre | information | accepté | session (registre) | heure de transmission écrite au registre ; P-019 remplacée par P-019 corrigée (section 3) |
| texte-16 : pages vérifiées | information | accepté | — | aucune action |

### 1.2 Lentille « méthode statistique » (rapport `0c492f02…` ; simulations, manifeste `6f76e9df…`)

| constat | gravité | décision | où | correction |
|---|---|---|---|---|
| CL5-01 : calibrage de λ, hypothèse d'identification non déclarée | majeur | accepté | texte (point 8 bis ; Seuil, C-P1 ; réserve 15) ; configuration (`etape2.loi_nette`) ; module (test) | mots exacts : l. 129-151, la réserve « 14 » numérotée 15 ; extension aux statistiques de rang : section 3 |
| CL5-02 : C-P3a, témoins partagés, niveau du W exact dépassé | majeur | nœud de Lazar | texte (bloc P-019) ; configuration (`stabilite_rang.C_P3a`) | P-019 corrigée (section 3) ; si l'option (A) est retenue : mots exacts, l. 172-182 |
| CL5-03 : C-P3b mesure le profil des familles | majeur | nœud de Lazar | texte (bloc P-019 ; Seuil, l. 491) ; configuration (`stabilite_rang.C_P3b`) | P-019 corrigée (section 3) ; si (A) : mots exacts, l. 203-209 ; si (B) ou (C) : C-P3b rapportée sans verdict |
| CL5-04 : C-P4b reste sur la lecture complète | majeur | accepté | texte (C-P4b ; A8 ; réserve 6) | mots exacts : l. 224-230 ; avec l'exception du point 13 (texte-06) |
| CL5-05 : C-P5 non défini si toutes les alarmes sortent | majeur | accepté | texte (points 15 et 11) ; configuration (`etape2.effectif_efficace`) ; module (garde R5) | mots exacts : l. 242-246 |
| CL5-06 : lectures restées sur la loi brute | majeur | accepté modifié | texte (point 10 ; Combinaisons ; A1, A2, A5, A7 ; point 16) | mots exacts : l. 265-278 ; **ajout** (même logique que la correction de A2) : Combinaisons, ligne « C-P1 confirmée mais … » (l. 835-836), écrire « intervalle de ĉ_témoin qui recoupe l'intervalle de ĉ brut (point 8) » au lieu de « intervalle de ĉ_témoin qui recoupe l'intervalle de ĉ » ; vérification courte (section 6.3) |
| CL5-07 : décompte et BCa sans préséance | mineur | accepté | texte (point 12) ; configuration (`etape2.valeurs_p`) | mots exacts : l. 292-296 |
| CL5-08 : tests du module sous-spécifiés | mineur | accepté | texte (points 8 bis et 11) ; module ; versement (script S2) | mots exacts : l. 306-315 ; plus le test de la règle conjointe (CL5-01, point 4) |
| CL5-09 : réserve d'intention sans loi nulle | mineur | accepté | texte (point 8 bis ; Combinaisons) ; configuration | mots exacts : l. 324-325 |
| CL5-10 : configuration muette sur des règles de décision | mineur | accepté | configuration (`etape2`, `etape2.loi_nette`) | mots exacts : l. 333-337 ; liste complète des champs : section 6.2 |
| CL5-11 : ordre de l'appariement des témoins non fixé | forme | accepté | texte (plan 2, témoins) ; configuration (`regle_temoins`) | mots exacts : l. 344-345 |
| CL5-12 : borne haute uni- ou bilatérale | forme | accepté | texte (l. 296, 811 ; 301, 818) | mots exacts : l. 350 |
| CL5-13 : estimabilité et puissance | information | accepté | session (devis de la piste C ; enjeu de P-020) | aucune correction du texte ; le devis prévoit n = 120 avec « puissance faible » (`t9_effectif_pilote_v1.txt`, `2788fcac…`) et l'extraction neuve |
| CL5-14 : pilote, rééchantillonnage des contenus ; k_max prudent | information | accepté modifié | texte (point 18) | la ligne déclarée de texte-07 ; l'option « erreur type des écarts à la moyenne de la famille » n'est pas retenue : elle change la règle du vivier sans simulation à l'appui ; la règle prudente (k souvent égal à 3) reste |
| CL5-15 : mesures v2 en attente ; lois exactes du W vérifiées | information | accepté | versement | mesures v2 à écrire puis verser (verrou 5) ; citer T2b (`99aee96a…`), jamais la table (a) de T2 (défaut d'arrondi pour trois évaluateurs, déclaré par le rapport) |
| CL5-16 : empreintes des registres changées | information | accepté | texte (l. 124, 145-146) | comme texte-10 |

### 1.3 Voisins : Joswin et al., Hu et Qu (note `55222cdb…`)

| constat | gravité | décision | où | correction |
|---|---|---|---|---|
| CV-01 : constat commun aux rangs hauts des familles 1 à 4, sans condition de référence | majeur | nœud de Lazar (option (b)) ; option (a) appliquée dans tous les cas | texte (réserve 9 ; réserve 16 ; contre-indices) ; si (b) : Métrique, point 5 ; Plan, TC.1 ; configuration ; module | (a) mots exacts : l. 229-244, « réserve 14 » écrit « réserve 16 » ; (b) mots exacts : l. 246-254, selon la décision (section 4.2) |
| CV-02 : verrou 2 incomplet | majeur | accepté modifié | texte (verrou 2) | remplacé par les phrases qui rendent compte des lectures faites : CP-06 (note des sept, l. 196, branche « sinon ») et CS-01 (note de second rang, l. 337-343) ; marqueurs de CV-08 gardés |
| CV-03 : les deux papiers cités au verrou seulement | mineur | accepté | texte (HC1, ajouts ; Familles) | mots exacts : l. 285-309 |
| CV-04 : précédent du témoin d'ajout neutre | mineur | accepté | texte (point 10) | mots exacts : l. 315-317 ; suivi de CS-04 |
| CV-05 : contre-indice côté lecteur | mineur | accepté | texte (contre-indices, sondes lectrices) | mots exacts : l. 324-328 |
| CV-06 : contre-indices de la famille 2 | mineur | accepté modifié | texte (contre-indices) | mots exacts : l. 334-339, la parenthèse « (argument de Joswin et al. … non opposable) » remplacée par celle de CS-02 (a) (note de second rang, l. 355-357) |
| CV-07 : second appui de la forme en bascule | mineur | accepté | texte (contre-indices ; A7) | mots exacts : l. 344-347 |
| CV-08 : ni la note ni son verdict au texte | forme | accepté modifié | texte (section « Contre-lecture » ; champs, l. 121-122) | mots exacts : l. 354-360 ; la liste entre parenthèses s'allonge de « ; Hussain et Nielbo ; Kumaran et al. ; Barkett ; Zeng » (CP-06) et des voisins de second rang cités (Wang Q. et al. ; Choi et al. ; Chen et al. ; Vennemeyer et al. ; Germani et Spitale) |
| CV-09 : fiabilité de Joswin et al. | information | accepté | — | citer en qualitatif (déjà la règle de N-023, section 1) |
| CV-10 : Hu et Qu et nos trois juges | information | accepté | — | aucune action |
| CV-11 : vocabulaire voisin de HC4 | information | accepté | session (veille) | ligne de veille HC4 |

### 1.4 Sept voisins de Panin (note `b3a6c187…`)

| constat | gravité | décision | où | correction |
|---|---|---|---|---|
| CP-01 : version publiée de Kumaran et al. non lue | majeur | accepté modifié (décision de la session, section 4.3) | session (contrôle avant le scellement) ; texte (verrou 2) | mots exacts : l. 169 ; **ajout** : même contrôle du résumé pour la version publiée de Pan et al. (Findings of the ACL 2026), citée par Panin ; même écart, « de moindre risque », relevé par la note (CP-01, l. 167 ; tableau, l. 17) |
| CP-02 : voisins de second rang des sept | majeur | accepté modifié | texte (verrou 2) | la lecture des cinq est en cours (`…/contre-lectures-brouillon5/voisins-cp02/`) : la phrase de CP-02 (l. 174) est remplacée par la ligne de texte-04 (marqueurs `<<CHEMIN_NOTE_VOISINS_CP02>>`, `<<EMPREINTE_NOTE_VOISINS_CP02>>`, `<<VERDICT_VOISINS_CP02>>`) ; verdict non préjugé ; sa dernière phrase (Zhu et al. et Weng et al., études fondatrices selon Hussain et Nielbo) est gardée |
| CP-03 : trois précédents de HC1 non cités | mineur | accepté | texte (HC1, ajouts ; Familles) | mots exacts : l. 180-181 |
| CP-04 : précédent partiel de HC3, composante 2 | mineur | accepté | texte (HC3) | mots exacts : l. 186 |
| CP-05 : trois contre-indices non déclarés | mineur | accepté | texte (contre-indices) | mots exacts : l. 191 (la correction seule ; elle ne recopie aucune formulation) |
| CP-06 : la note n'a pas de place au texte | forme | accepté | texte (verrou 2 ; section « Contre-lecture » ; champs) | mots exacts : l. 196 ; branche « sinon » (CV-02 est remplacé, pas appliqué) |
| CP-07 : nos juges dans ces papiers | information | accepté | — | aucune action |
| CP-08 : fiabilité | information | accepté | — | citer en qualitatif |
| CP-09 : mot « deference » | information | accepté | rédaction anglaise du papier | aucune action au préenregistrement |
| CP-10 : voisins de HC5 et HC4 | information | accepté | session (veille) | lignes de veille |

### 1.5 Voisins de second rang (note `8027bd53…`)

| constat | gravité | décision | où | correction |
|---|---|---|---|---|
| CS-01 : les neuf contrôlés ; verrou à écrire | mineur | accepté | texte (verrou 2) | mots exacts : l. 337-343 |
| CS-02 : contre-indices des familles 2 et 3 | mineur | accepté | texte (contre-indices) | mots exacts : (a) l. 353-357 ; (b) l. 358-369 |
| CS-03 : précédent d'instrument et mise en garde de style pour HC2b | mineur | accepté modifié | texte (Hypothèse, HC2b) | mots exacts : l. 377-385, placés en sous-puce « Précédents cités (aucun énoncé changé) : » sous la puce HC2b, et non à la fin de la phrase de l'énoncé (énoncés repris mot pour mot du brouillon 3) ; la remarque pour la méthode (l. 386-387) va à la vérification courte |
| CS-04 : second précédent du témoin neutre | information | accepté | texte (point 10) | mots exacts : l. 393-395 |
| CS-05 : style sans ordre (Wang Q. et al.) | information | accepté modifié | texte (HC3, composante 2) | citation facultative retenue, mots à moi, après la phrase de CP-04 : « Plus loin encore : une phrase qui imite la réflexion, sans ordre, insérée entre deux options, déplace des juges de raisonnement vers l'option qui la suit ; style du raisonnement, pas de l'instructeur ; choix binaire, une intensité, aucun moniteur ni sonde de l'auteur (Wang Q. et al., 2504.09946v2, `1d231bbe…`, p. 6). » |
| CS-06 : Zhong et al. et les intensités graduées | information | écarté | — | citation facultative non retenue : Zhong et al. ne portent pas sur des juges (agents de décision, direction imposée) ; la note le dit (l. 410-411) ; rien de HC1 n'y est pris |
| CS-07 : appui faible à CV-01 (Choi et al.) | information | accepté | dossier du nœud CV-01 | versé à l'enjeu de CV-01 (section 4.2) |
| CS-08 : fiabilité | information | accepté | — | citer en qualitatif |
| CS-09 : HC4 | information | accepté | session (veille) | ligne de veille HC4 |
| CS-10 : registre de veille | forme | accepté | session (veille) | l. 446-448 ; une ligne par papier, aussi pour Joswin et al., Hu et Qu et les sept de Panin (CV-11, CP-10) |

### 1.6 Vérification du verrou de la famille 1 (`0cbd3ae3…`)

| constat | gravité | décision | où | correction |
|---|---|---|---|---|
| VF-01 : verrou faux (famille 1 : 9, 12, 14, 15, 16 ; limites 6 et 11) | verdict | accepté | texte (réserve 14 ; verrous) | tranché par Lazar (R-309, GO-2026-10-20-14) : déclaration au lieu du verrou (section 2) |
| VF-02 : autres familles (ordres en bande 13 à 16 ; limites : ordres en bande 12, revendication d'autorité 15 ; deux familles et les témoins sans contingence) | information | accepté | texte (réserve 14) | repris dans la déclaration (section 2.2) |
| VF-03 : le plaidoyer écrit par l'agent est hors du champ du verrou | information | écarté | — | hors du champ de R-307 et de R-309, qui visent le vivier ; la consigne du plaidoyer ne porte aucune contingence (vérification, l. 23) ; aucun critère ne lit une contingence ; rien à ajouter |

### 1.7 Place prévue

| pièce | état | où | règle |
|---|---|---|---|
| lecture des cinq voisins de CP-02 (`…/contre-lectures-brouillon5/voisins-cp02/`) | en cours, non lue ici | texte (verrou 2 ; section « Contre-lecture ») | ligne de texte-04 et de CP-02 ; verdict non préjugé ; une collision, même partielle : nœud de Lazar avant le scellement ; ses constats seront traités par la session comme ceux de cette série |

## Bilan

**66 constats : 47 acceptés, 14 acceptés modifiés, 2 écartés, 3 nœuds de Lazar.**

| pièce | constats | accepté | accepté modifié | écarté | nœud |
|---|---|---|---|---|---|
| texte | 16 | 11 | 5 | 0 | 0 |
| méthode | 16 | 12 | 2 | 0 | 2 (CL5-02, CL5-03 : P-019 corrigée) |
| Joswin et al., Hu et Qu | 11 | 7 | 3 | 0 | 1 (CV-01) |
| sept de Panin | 10 | 8 | 2 | 0 | 0 |
| second rang | 10 | 7 | 2 | 1 | 0 |
| verrou de la famille 1 | 3 | 2 | 0 | 1 | 0 |

Nœuds à soumettre : P-019 corrigée (CL5-02, CL5-03), CV-01, et P-020 (sans constat neuf, enjeu chiffré mis à jour).
Aucun constat ne change un énoncé, le vivier, une famille ou une constante ; aucune zone revendiquée n'est trouvée
occupée (18 papiers lus ou contrôlés, « pas de collision » pour chacun).

## 2. Décisions de Lazar déjà prises, à intégrer au brouillon 6

Sources : `R/registres/decisions.md`, R-307, R-308, R-309 ; `R/registres/go.md`, GO-2026-10-20-13 et GO-2026-10-20-14.
L'ajout 1 de R-307 (verrou « famille 1 sans conséquence conditionnée au verdict ») est **remplacé** par la déclaration de
R-309 : le brouillon 6 n'écrit aucun verrou de ce type.

### 2.1 R-307, ajout 2 — clause d'ouverture

Place : Plan d'analyse, section 3, après « Familles et échafaudage ». Texte proposé :

> **Clause d'ouverture** (décision de Lazar R-307 ; GO-2026-10-20-13). Un facteur interne à une famille (par exemple la
> contingence de la famille « flatterie et supplication », réserve 14 ; PA-5) ferait l'objet d'un préenregistrement
> complémentaire, scellé et contre-lu avant l'étape 2, lu sur les mêmes contenus de TC.1, hors des corrections de Holm de
> C-P1 et de C-P2, sans changer le choix des formulations. Sans ce complément scellé avant l'ouverture de l'étape 2, aucun
> facteur interne n'est lu. Son ouverture relève de Lazar (R-307).

Plan d'analyse, section 5 (comparaisons multiples), ajouter à la fin :

> Un facteur interne à une famille ne relève que du préenregistrement complémentaire de la clause d'ouverture (Plan,
> section 3) : il n'entre dans aucune des corrections ci-dessus et ne les change pas.

### 2.2 R-307, ajout 3, et R-309 — réserve 14

Place : Plan d'analyse, section 7, après la réserve 13. Texte proposé :

> 14. **Contingence dans les familles** (décisions de Lazar R-307 et R-309 ; GO-2026-10-20-13 et GO-2026-10-20-14). Les
>     formulations 9, 12, 14, 15 et 16 de la famille « flatterie et supplication » (configuration,
>     `vivier.flatterie_supplication`) et 13 à 16 de la famille « ordres en bande » (`vivier.ordres_en_bande`) portent une
>     conséquence conditionnée au verdict (vérification par indices seulement, par un sous-agent neuf :
>     `docs/notes/contre-lectures-papier-C-v1/verification-verrou-famille1-v1.md`,
>     `0cbd3ae3050c5485d6e5415eb38eb9f51c07363a8e7f23e66f9925ed92132420` ; R-308). Ces indices sont gelés ici comme
>     **étiquette descriptive**, jamais comme facteur ni comme critère : aucune analyse, aucun contraste, aucune strate,
>     aucun audit et aucune règle de l'addendum ne les lit ; aucune ligne de C-P1 à C-P6 n'en dépend ; le choix des
>     formulations ne les lit pas. L'étiquette est seulement écrite, au rapport de l'étape 2, à côté de chaque formulation
>     retenue qui la porte. Cas limites, déclarés comme tels et non étiquetés : « flatterie et supplication », indices 6 et
>     11 ; « ordres en bande », indice 12 ; « revendication d'autorité », indice 15. Les familles « approbations forgées » et
>     « usurpation stylistique » et les seize témoins n'en portent aucune. La contingence occupe le haut de l'échelle de la
>     famille 1 (indices 14 à 16, les plus longs de la famille). Vivier, configuration, constantes et longueurs inchangés.
>     L'effet de la contingence est réservé au préenregistrement complémentaire de la clause d'ouverture (Plan, section 3)
>     et n'entre dans aucun critère de C-P1 à C-P6.

### 2.3 Ailleurs dans le brouillon 6

- **Verrous** : ajouter « Déclaration de la réserve 14 (R-309) : si la contre-lecture du brouillon 6 établit qu'elle ne
  suffit pas, repli (b) de R-309 : réécriture des formulations 9, 12, 14, 15 et 16 de la famille « flatterie et
  supplication », configuration de brouillon suivant, vérification par indices refaite par un sous-agent neuf. » Le repli
  n'entre pas au texte scellé.
- **Configuration** : rien pour R-309 (« configuration inchangée » ; l'étiquette vit au texte seul, ce qui garantit
  qu'aucun module ne la lit).
- **GO** : ajouter GO-2026-10-20-13 et GO-2026-10-20-14 (type « décision », aucune dépense).
- **Documents qui font foi** : lignes R-307, R-308 et R-309 du registre des décisions.
- **Champs du scellement**, ligne « Décisions » : ajouter « R-307 (GO-2026-10-20-13) et R-309 (GO-2026-10-20-14) :
  intégrées (Plan, sections 3, 5 et 7, réserve 14) ».
- **« Ce que change le brouillon 6 »** : une puce « Contingence : déclarée comme étiquette descriptive (R-309), clause
  d'ouverture et réserve 14 (R-307) ; PA-5 n'entre pas dans ce texte. »

## 3. P-019 corrigée (stabilité de rang, prédiction 3 de N-005)

**Décision.** Remplacer la version de P-019 transmise le 20 octobre (C-P3a, C-P3b, C-P3c, valeurs p exactes ou par
permutation, « établie / non établie ») par une version corrigée, ou rapporter tout ou partie de la prédiction 3 sans
verdict.

**Enjeu.** La version du 20 octobre prend son défaut le 2026-10-22 vers 21:15 UTC ; si elle le prend, le papier C scelle
deux règles fausses. C-P3a sort « établie » sans aucun écart entre juges dans 0,075 à 0,111 des essais au lieu de 0,05,
parce que les familles partagent des témoins (avec des témoins indépendants : 0,033 à 0,049) ; C-P3c tient son niveau
(0,036 à 0,055) (T2, `…/contre-lectures-brouillon5/methode/simulations/t2_rang_temoins_partages_v1.txt`,
`852adb68c4eb96f367b841d3e66410a07e12a04ba1091a1dc54c10d0c1cfbe56`). C-P3b sort « établie » dans 0,945 à 0,965 des essais
quand seules les familles se classent de la même façon dans les deux corpus, et dans 0,318 à 0,445 quand les juges
s'inversent d'un corpus à l'autre (T2d, `…/methode/simulations/t2d_C_P3b_variantes_v1.txt`,
`294ec49a3f6257da090c10cc564b70b8fda669852ed773dfe0c1b4bc419a31a4`). Un argument de plus (CL5-01, non simulé ; modèle
« D » du script T3, `…/methode/simulations/t3_compression_temoins_v1.py`,
`0c5238b0a8b14fc97d9b9e59f82cf3a6ffec01775c895b21d71d208a35f96626`) : si la lecture sans insertion est exacte et que toute
insertion comprime la lecture, le Ḡ calibré d'un juge est gonflé de 1/(1 − κ_j) dans toutes ses familles ; si l'erreur
d'insertion touche aussi v₀ (modèle « S »), c'est le Ḡ sans calibrage qui est réduit de ρ_j. Dans les deux cas un facteur
propre au juge ordonne les juges partout : la lecture qui n'est pas la bonne peut rendre une stabilité de rang qui n'existe
pas. Aucun énoncé ne change ; seule la lecture de la prédiction 3 change.

**Options.**
- **(A) Version corrigée, lecture « établie / non établie », sans réfutation.**
  - C-P3a « établie » si p exact ≤ 0,05 (W ≥ 0,64 ; 7 776 affectations) **et** p par rééchantillonnage centré ≤ 0,05
    (dans chaque tirage par tâches du point 11, W* sur les rangs des écarts Ḡ*_{j,f} − Ḡ_{j,f} ;
    p = (1 + #{W* ≥ W}) / (B + 1)) ; mots exacts de CL5-02, l. 172-182.
  - C-P3b « établie » si le τ de Kendall entre les quinze écarts intra-famille nets du corpus A (Ḡ_{j,f} moins la moyenne
    des trois juges de la famille f) et les quinze du corpus B a un p unilatéral ≤ 0,05 par rééchantillonnage centré des
    deux corpus (tirages indépendants par tâches et par items) ; le τ des quinze valeurs (100 000 permutations) est
    rapporté sans verdict, comme concordance des profils ; mots exacts de CL5-03, l. 203-209.
  - C-P3c inchangée (W exact ; quatre évaluateurs, ou trois sans P-020, « établie » alors seulement si W = 1), avec la
    précision de texte-05 (gains d'écart **bruts** des juges, consigne A, mode direct).
  - **Les trois aux deux lectures** de la loi nette (calibrée, et sans calibrage, ρ = 1, mêmes tirages) pour leurs
    composantes en Ḡ : « établie » seulement si les deux lectures concluent (extension, par moi, de la règle conjointe
    que CL5-01 écrit pour C-P1).
  - **Clause de repli mécanique** : si la vérification courte d'avant le scellement (sous-agent neuf, section 6.3) trouve,
    pour l'une de ces règles, un niveau réel sous le nul au-dessus de 0,05 plus deux erreurs de Monte-Carlo, dans le
    modèle de la contre-lecture méthode rejoué avec un vrai rééchantillonnage, cette statistique est rapportée sans
    verdict, écrit tel quel, sans nouveau nœud.
  - Avantage : la prédiction 3 de N-005 garde un verdict pour ses trois parties, au niveau annoncé dans le modèle :
    rééchantillonnage centré de C-P3a à 0,028 pour k = 5 (T2c, `…/methode/simulations/t2c_W_reechantillonnage_centre_v1.txt`,
    `30605e2e7a8e7eb38e658fbb1f77b41df5f941ad5c269a3d9e5aaa81cbb8a205`) ; C-P3b corrigée à 0,038 à 0,055, et 0,000 à 0,012
    quand les juges s'inversent (T2d) ; C-P3c à 0,036 à 0,055 (T2).
  - Inconvénient : puissance faible, donc « non établie » fréquente (C-P3b : 0,283 à 0,492 si l'ordre des juges est
    vraiment le même à un écart type ; C-P3a corrigée, centré seul : 0,448 pour k = 3 et 0,657 pour k = 5 à un écart de
    gain de 0,03 entre juges, T2c) ; niveau pas encore établi partout : rééchantillonnage centré seul à 0,062 pour k = 3
    (400 essais, 45 tâches : T2c et son script, `e05aae2a…`), niveau de la conjonction non calculé ; C-P3b corrigée
    validée par une loi nulle tirée de la vraie loi des erreurs, pas par un rééchantillonnage des données (script T2d,
    `49b03ccc…`) ; extension aux deux lectures non simulée ; module et tests plus lourds.
- **(B) C-P3a et C-P3c comme en (A) ; C-P3b rapportée sans verdict** (τ des écarts intra-famille et τ des quinze valeurs,
  avec leurs valeurs p ; c'est le repli que CL5-03 juge acceptable). Avantage : retire la règle la moins puissante et la
  moins vérifiée. Inconvénient : l'invariance au corpus (prédiction 3 de N-005) n'a plus de verdict : écart à N-005
  déclaré, partiel.
- **(C) Repli d'origine de P-019** : les trois statistiques et leurs valeurs p rapportées sans verdict. Avantage : aucun
  faux « établie » possible ; module plus simple. Inconvénient : la prédiction 3 n'a aucun verdict : écart à N-005 déclaré,
  entier.
- La version du 20 octobre n'est plus une option (faux « établie » : 0,075 à 0,111 pour C-P3a ; 0,945 à 0,965 pour C-P3b).

**Recommandation.** (A), avec sa clause de repli ; confiance ≈ 60 %. La clause fait passer d'elle-même une statistique de
(A) à « rapportée sans verdict » si la vérification courte ne tient pas son niveau : (A) ne peut pas finir moins sûre que
(B) ou (C), et garde un verdict quand il est valide.

**Défaut sous 48 heures.** (A) avec sa clause, 48 heures après la transmission de cette version corrigée (heure écrite au
registre). La version du 20 octobre ne prend jamais son défaut : la session l'écrit au registre avant le 2026-10-22 vers
21:15 UTC, par une ligne nouvelle qui renvoie à P-019 (R12 : l'ancienne ligne n'est pas réécrite).

## 4. Autres nœuds de Lazar ; décisions de la session

### 4.1 P-020 — bras « usurpation écrite par l'agent » (telle qu'au registre ; enjeu chiffré mis à jour)

**Décision.** Ajouter ou non le bras « usurpation écrite par l'agent » à l'étape 2 du papier C (plan 2 × 3 au lieu de
2 × 2).

**Enjeu.** Sans lui, TC.3 (b) n'est pas mesuré sur les sondes de l'auteur : le versant sondes de C-P6 (composante 2 de
HC3) est « non mesuré » ; C-P3c n'a que trois évaluateurs et n'est « établie » que si W = 1 (p = 0,0278 ; T2b,
`…/methode/simulations/t2b_lois_exactes_W_v1.txt`, `99aee96aa97fc407891ae60a050d85a14769e4ace78dda245dbb79564989aef1`).
Coût : + 50 % d'épisodes à l'étape 2. Avec l'effectif probable (la règle de l'addendum rend n = 120 dans 100 % des essais
à gains modestes et 56 % à gains forts : T9, `…/methode/simulations/t9_effectif_pilote_v1.txt`,
`2788fcac56ac7de8072425dc9618965d74b664fe9fc65b8eebae7409461fcd05`) : 360 épisodes au lieu de 240 ; avec les 48 tâches du
partage seules (n ≤ 90) : 270 au lieu de 180. Coût au devis de la piste C (GO séparé, après G0). Aucune pièce de cette
série ne demande de changer P-020 ; texte-01 règle seulement l'écriture de la décision dans la configuration scellée.

**Options.**
- (a) Inclure. Avantage : composante 2 de HC3 mesurée des deux côtés (juges, sondes de l'auteur) ; C-P3c à quatre
  évaluateurs (W ≥ 0,8125, p = 0,0417 atteignable). Inconvénient : + 50 % d'épisodes ; le texte écrit par l'agent n'est
  contrôlé que par la garde lexicale descriptive (marques d'ordre ; réserve au-delà de 20 %).
- (b) Ne pas inclure. Avantage : coût de l'étape 2 inchangé. Inconvénient : versant sondes de C-P6 « non mesuré » ; C-P3c
  à trois évaluateurs.

**Recommandation.** (a), confiance ≈ 65 % (inchangée).

**Défaut sous 48 heures.** (a), 48 heures après la transmission (registre : 2026-10-22 vers 21:15 UTC si elle a eu lieu le
20 vers 21:15 ; la colonne « à transmettre » est à mettre à jour, texte-15).

### 4.2 CV-01 — condition de référence « constat nu »

**Décision.** Ajouter ou non à TC.1 une condition de référence « constat nu », rapportée sans verdict.

**Enjeu.** Les rangs hauts des familles 1 à 4 affirment tous le même constat sur le contenu ; les témoins n'en portent
aucun ; la loi nette mesure donc ensemble l'enveloppe (locuteur, autorité, style) et le constat (note `55222cdb…`, CV-01 ;
indices par la sortie `outils/indices_constat_vivier_v1.sortie.txt`, `4d00b9b9…`). Sans référence, C-P6 (juges) ne peut
pas attribuer un Ḡ_4 positif au style, alors que la composante 2 de HC3 revendique le versant stylistique ; « destination
commune non rejetée » (C-P1b) et « intensités graduées » peuvent venir du constat commun. Leçon publiée : sur des réponses
à des questions, la réponse affirmée sans locuteur porte l'essentiel du déplacement (Hu et Qu, 2607.05545v1, p. 1, p. 2,
p. 6 et p. 8). Appui faible et mêlé : sans position nette, l'autorité n'entraîne rien (Choi et al., 2601.04790v1, p. 1 et
p. 5 ; CS-07). Aucun énoncé, aucune pièce revendiquée, aucun seuil ne change.

**Options.**
- (a) Déclaration seule (réserve 16 ; réserve 9 réécrite ; contre-indice de Hu et Qu ; mots exacts, note l. 229-244).
  Avantage : aucun coût, configuration inchangée sur ce point. Inconvénient : C-P6 (juges) se lit « usurpation stylistique
  portant un constat », sans attribution au style.
- (b) (a) plus la condition « constat nu » en TC.1 (insertion du constat seul, sans locuteur, ni style, ni ordre, à la même
  place, avec son témoin de longueur ; g et ĉ nets à un seul rang, par juge × corpus ; Ḡ_f − g_constat et
  g_{k_f} − g_constat par famille ; Ḡ_4 − g_constat = contraste « style contre contenu » de la réserve 9 ; tout rapporté
  sans verdict ; mots exacts, note l. 246-254). Avantage : sépare le style du constat pour C-P6 et la réserve 9 ; coût
  faible (deux lectures de plus par contenu, par juge et par corpus ; aucun épisode de plus). Inconvénient : champ neuf dans
  la configuration et le module, à contre-lire ; garde lexicale à rejouer sur l'insertion neuve ; insertion non lue au
  pilote (variante à trancher par la session : la lire au point 1.4, hors du choix des formulations, pour la lisibilité
  seulement).
- (c) (a) maintenant, et la condition « constat nu » renvoyée au préenregistrement complémentaire de la clause
  d'ouverture (R-307), lu sur les mêmes contenus de TC.1. Avantage : aucun changement du dessin de ce texte. Inconvénient :
  ce complément n'existe que si Lazar ouvre PA-5 (R-307), et sa clause vise un facteur interne à une famille, pas une
  référence commune : il faudrait l'élargir.

**Recommandation.** (b), confiance ≈ 65 % (celle de la note des voisins) : la configuration brouillon 3 est réécrite de
toute façon (CL5-01, CL5-05, CL5-10, CL5-11, texte-01, texte-11), et (b) est la seule option qui permette à C-P6 de parler
du style.

**Défaut sous 48 heures.** (b).

### 4.3 Décisions de la session, proposées (routine ; pas des nœuds)

1. **CP-01** : contrôle, avant le scellement, du résumé des versions publiées de Kumaran et al. (Nature Machine
   Intelligence, 2026) et de Pan et al. (Findings of the ACL 2026), par un sous-agent neuf ; règle de passage au texte
   entier : celle du verrou 2 ; texte entier payant : demande à Lazar, aucun achat. Je ne retiens pas « la préimpression
   suffit » : Kumaran et al. est le voisin le plus proche des sept (intensités graduées régressées, lecture par les
   logits) et le titre a changé à la publication ; c'est une zone séduisante (R8).
2. **Weng et al. 2501.13381 et Zhu et al. (ACL 2025)**, exigés par le verrou 2 du brouillon 5 (deux voisins cités par
   Bajaj et Tiganj ; « études fondatrices » selon Hussain et Nielbo) : aucune pièce de cette série ne les a lus. Contrôle
   à faire avant le scellement, même règle.
3. **Contre-lecture courte des notes de voisins** (Joswin et Hu et Qu ; sept de Panin ; second rang ; puis celle des cinq
   de CP-02) par un sous-agent neuf : verdicts de collision et pages, comme les notes du brouillon 4 l'ont été. Motifs :
   R8 (zones séduisantes vérifiées plus durement) et R4 (18 « pas de collision » de suite : même audit qu'un résultat
   trop propre).
4. **Registre** : P-019 corrigée, CV-01 (proposition, défaut sous 48 heures) et l'heure de transmission de P-020, en
   lignes nouvelles ; l'ancienne version de P-019 marquée remplacée sans réécriture.
5. **Réserves** numérotées 14 (R-307, R-309), 15 (CL5-01), 16 (CV-01).
6. **R-309** : déclaration au texte seul, aucun champ dans la configuration.
7. **texte-08** : tirage uniforme des tâches de l'étape 2, sans strate par origine.
8. **texte-10** : l'empreinte de la source des 64 tâches est remplie par la session au scellement, jamais par un
   rédacteur.
9. **Écart de la lentille texte** (son script a ouvert en binaire, pour une empreinte, `R/prereg/P3-consignes-v1.md`,
   `items-textes-p1-v1.json`, `prompts-p1-v1.json` et le fichier source des 64 tâches ; rapport, l. 35-39) : consigné au
   registre des décisions ; les consignes suivantes gardent « pas même pour une empreinte ».
10. **`…/contre-lectures-brouillon5/outils-texte/`** : auteur à établir (la lentille texte dit ne pas le connaître) ; les
    deux annexes extraites que les lecteurs de voisins ont utilisées (`2cf7b134…`, `e0f53012…`, sans compagnon) sont
    versées avec un compagnon et une ligne de provenance ; le reste du dossier n'est pas versé tant que son auteur n'est pas
    établi.
11. **Voisins ajoutés aux « cités comme publiés »** (Joswin et al. ; Hu et Qu ; Hussain et Nielbo ; Kumaran et al. ;
    Barkett ; Zeng ; et les voisins de second rang cités) : routine, comme au brouillon 4 (aucune revendication changée,
    aucune zone occupée, aucune prédiction prise) ; une ligne d'information à Lazar ; lignes de veille (CV-11, CP-10,
    CS-09, CS-10).
12. **texte-06 contre CL5-04** : la correction de CL5-04 l'emporte (texte-06 demandait cet avis à la lentille méthode).

## 5. Pièces à verser au dépôt avant le scellement

Chemins de source relatifs au préfixe `…/` ; destinations relatives à `R`. Chaque fichier garde ou reçoit son compagnon
`.sha256` (R6). Les dossiers de lecture sont versés entiers, pour que leurs manifestes restent vérifiables. Les textes
extraits de PDF (`pdf-texte/`, `texte/`) restent dans la zone privée : la session vérifie que la copie publique les exclut.

| # | pièce | source (bloc-notes) | empreinte | destination |
|---|---|---|---|---|
| 1 | brouillon 4 du texte | `papier-C-preenregistrement-HC1-HC3-v1-brouillon4.md` (+ compagnon) | `40bf1d4f…` | `brouillons/` |
| 2 | configuration brouillon 1 | `papier-C-config-v1-brouillon1.json` (+ compagnon) | `348379fb…` | `brouillons/` |
| 3 | traitement de la session du brouillon 4 | `traitement-contre-lectures-brouillon4-papier-C-v1.md` (+ compagnon) | `f2c6a360…` | `docs/notes/contre-lectures-papier-C-v1/` |
| 4 | table de traitement du brouillon 5 | `brouillon5/table-traitement-brouillon5-v1.md` (+ compagnon) | `ebb763fa…` | `docs/notes/contre-lectures-papier-C-v1/` |
| 5 | sortie du validateur du brouillon 5 | `brouillon5/problemes-brouillon5-v1.txt` (+ compagnon) | `a2f78166…` | `docs/notes/contre-lectures-papier-C-v1/` |
| 6 | points ouverts du brouillon 4 | `points-ouverts-brouillon4-v1.md` (+ compagnon) | `babe4b4d…` | `docs/notes/contre-lectures-papier-C-v1/` |
| 7 | six rapports du brouillon 4 et des notes | `contre-lectures/contre-lecture-*.md` (+ compagnons) | `0f1cf812…`, `08618f6b…`, `6b350e99…`, `09f14364…`, `c06488a5…`, `2c720d22…` | `docs/notes/contre-lectures-papier-C-v1/` |
| 8 | simulations de la lentille méthode du brouillon 4 | `contre-lectures/simulations-methode/` (26 fichiers dont le manifeste ; `s2_regression_moyenne_v1.py` cité par CL5-08) | manifeste `eea33215…` ; S2 `60219b56…` | `docs/notes/contre-lectures-papier-C-v1/simulations-methode/` |
| 9 | mesure de conception de la lentille Panin | `contre-lectures/outils-panin/` (dont `empreintes-outils-panin-v1.sha256`) | `498d4cde…`, sortie `0ddda72b…` | `docs/notes/contre-lectures-papier-C-v1/outils-panin/` |
| 10 | notes finales des voisins du brouillon 4 | `brouillon5/notes/lecture-voisin-panin-v1.md` ; `brouillon5/notes/lecture-voisins-HC1-bajaj-silent-judge-v1.md` (+ compagnons) | `8781d6a7…` ; `a98ddc75…` | `docs/notes/` |
| 11 | scripts de configuration | `outils/ecrire_config_v1.py` ; `brouillon5/outils/ecrire_config_brouillon2_v1.py` et son journal (+ compagnons) | `634c3e8f…` ; `1726dcdf…` ; `4cdda1a2…` | `docs/procedures/papier-C-v1/` |
| 12 | mesures de conception v1 ; vérification exacte du W | `mesures/mesures-conception-papier-C-v1.txt`, `mesures/mesures_conception_papier_c_v1.py` ; `brouillon5/outils/verifier_kendall_C_P3_v1.py` et `.txt` (+ compagnons) | `bbad099d…`, `1a1db18e…` ; `383a66d6…`, `18961a7c…` | `docs/notes/papier-C-mesures-v1/` |
| 13 | mesures de conception v2 (CR-methode-18) | **à écrire** (absentes du bloc-notes) | `<<EMPREINTE_MESURES_V2>>` | `docs/notes/papier-C-mesures-v1/mesures-conception-papier-C-v2.txt` |
| 14 | note du vivier | **source à désigner par la session** (dépôt privé, décision de Lazar ; absente des dossiers listés ici) | `dbad9e66…` | `docs/sources/` (`<<CHEMIN_NOTE_VIVIER>>`) |
| 15 | lentille texte du brouillon 5 | `contre-lectures-brouillon5/texte/` entier (rapport, outils, sorties, `pdf-texte/`, manifeste) | rapport `12879073…` ; manifeste `99cfc889…` | `docs/notes/contre-lectures-papier-C-v1/brouillon5/texte/` |
| 16 | lentille méthode du brouillon 5 | `contre-lectures-brouillon5/methode/` entier (rapport, `simulations/`) | rapport `0c492f02…` ; manifeste `6f76e9df…` | `docs/notes/contre-lectures-papier-C-v1/brouillon5/methode/` |
| 17 | note Joswin et al., Hu et Qu | `contre-lectures-brouillon5/voisins/` entier | note `55222cdb…` ; manifeste `a4594214…` | `docs/notes/contre-lectures-papier-C-v1/brouillon5/voisins/` |
| 18 | note des sept voisins de Panin | `contre-lectures-brouillon5/voisins-panin/` entier | note `b3a6c187…` ; manifeste `19c41125…` | `docs/notes/contre-lectures-papier-C-v1/brouillon5/voisins-panin/` |
| 19 | note de second rang | `contre-lectures-brouillon5/voisins-second-rang/` entier | note `8027bd53…` ; manifeste `89763134…` | `docs/notes/contre-lectures-papier-C-v1/brouillon5/voisins-second-rang/` |
| 20 | note des cinq voisins de CP-02 | `contre-lectures-brouillon5/voisins-cp02/` entier, une fois finie | à venir | `docs/notes/contre-lectures-papier-C-v1/brouillon5/voisins-cp02/` |
| 21 | PDF cités au brouillon 6 (11) | `contre-lectures-brouillon5/voisins/pdf/` : 2607.00415v1, 2607.05545v1 ; `…/voisins-panin/pdf/` : 2608.11247v1, 2507.03120v1, 2601.17577v1, 2510.01228v2 ; `…/voisins-second-rang/pdf/<id>/` : 2504.09946v2, 2601.04790v1, 2507.21509v3, 2509.21305v4, 2505.13488v1 (+ compagnons) | celles des compagnons et des notes | `docs/sources/pdf/<id>.pdf`, avec une note de provenance écrite par la session (`docs/sources/pdf/provenance-voisins-papier-C-brouillon5-v1.md` : hôtes, heures, versions, empreintes, tirés des notes) |
| 22 | vérification du verrou de la famille 1 | `verrou-famille1/verification-verrou-famille1-v1.md` (+ compagnon) | `0cbd3ae3…` | `docs/notes/contre-lectures-papier-C-v1/` |
| 23 | consignes de cette série | `consignes-contre-lectures-brouillon5-v1.md` (**sans compagnon : le créer**) ; `consigne-redacteur-brouillon5-v1.md` ; `consigne-voisins-cp02-v1.md` ; `consigne-projet-traitement-contre-lectures-brouillon5-v1.md` | `14829997…` ; `5da5939a…` ; `7de50f46…` ; `9ef3e86a…` | `docs/notes/contre-lectures-papier-C-v1/consignes/` |
| 24 | annexes extraites utilisées par les lecteurs de voisins | `contre-lectures-brouillon5/outils-texte/annexe-note-panin-extraite.md` ; `…/annexe-note-voisins-extraite.md` (**sans compagnon** ; auteur à établir) | `2cf7b134…` ; `e0f53012…` | `docs/notes/contre-lectures-papier-C-v1/brouillon5/outils-texte/`, avec une ligne de provenance |
| 25 | traitement de la session du brouillon 5 (ce projet, une fois scellé par la session) | `traitement-brouillon5/` | à venir | `docs/notes/contre-lectures-papier-C-v1/traitement-contre-lectures-brouillon5-papier-C-v1.md` |

Observation (R6, R11) : dans `R/brouillons/`, les brouillons 1 à 3 du texte n'ont pas de compagnon `.sha256` à côté
d'eux (liste du dossier) ; la session vérifie s'ils sont empreintés ailleurs. Le script de contrôle demandé par texte-03
(chaque chemin cité avec une empreinte existe et lui est égal) le dira.

## 6. Brouillon 6

### 6.1 Ce que fait le rédacteur (sous-agent neuf), dans cet ordre

1. Partir du brouillon 5 (`9d55160f…`) et de la configuration brouillon 2 (`77252564…`). Écrire sous des noms neufs
   (R12) : brouillon 6 ; configuration brouillon 3, par un script neuf `ecrire_config_brouillon3_v1.py` (gardes lexicales
   et longueurs rejouées, journal) ; table de traitement du brouillon 6, une ligne par ligne de la table de ce
   traitement tel que la session l'a scellé (appliqué, où, écart).
2. Intégrer R-307 (ajouts 2 et 3) et R-309 avec les textes et aux places de la section 2. N'écrire aucun verrou
   « famille 1 sans contingence ».
3. Écrire les blocs de décision selon la réponse de Lazar ou le défaut échu au moment de la rédaction : P-019 corrigée
   (section 3), P-020, CV-01 (section 4). Pour un nœud encore ouvert : les deux versions, chacune sous son en-tête, avec
   `<<TRANCHER_P019>>`, `<<TRANCHER_P020>>` (texte-02) et, par analogie, `<<TRANCHER_CV01>>` ; aux champs du scellement :
   `<<DECISION_STABILITE_RANG>>`, `<<DECISION_BRAS_USURPATION>>`, `<<DECISION_CONSTAT_NU>>`.
4. Appliquer les constats acceptés, dans cet ordre : texte-01 ; texte-05 ; CL5-01 (réserve 15) ; CL5-04 avec
   l'exception du point 13 (texte-06) ; CL5-05 ; CL5-06 et son ajout ; CL5-07 ; CL5-08 ; CL5-09 ; CL5-11 ; CL5-12 ;
   texte-07 et la ligne de CL5-14 ; texte-08 ; texte-09 ; texte-10 ; texte-11 ; CV-01 (a) (réserve 16) ; CV-03 ;
   CV-04 puis CS-04 ; CV-05 ; CV-06 avec CS-02 (a) ; CS-02 (b) ; CV-07 ; CP-03 ; CP-04 puis CS-05 ; CP-05 ; CS-03
   (sous-puce). Chaque correction en mots exacts des lignes citées ; chaque écart en une ligne.
5. Récrire le verrou 2 dans cet ordre : (i) notes finales Panin et Bajaj et Tiganj (inchangé) ; (ii) Joswin et al. et
   Hu et Qu, puis les sept de Panin (CP-06, branche « sinon ») ; (iii) versions publiées de Kumaran et al. (CP-01, mots
   exacts, l. 169) et de Pan et al. (même forme) ; (iv) second rang de Joswin et Hu et Qu (CS-01) ; (v) second rang des
   sept (ligne de texte-04, lecture en cours) ; (vi) Weng et al. 2501.13381 et Zhu et al. (ACL 2025) : phrase du
   brouillon 5 gardée, contrôle encore à faire ; (vii) « Pour chacune de ces notes, une collision, même partielle : nœud
   de Lazar avant le scellement. »
6. Mettre à jour : « Ce que change le brouillon 6 » ; historique (brouillon 5 sous `brouillons/`, `9d55160f…` ; traitement
   et table aux chemins de texte-03) ; GO (GO-2026-10-20-13, -14) ; documents qui font foi (R-307, R-308, R-309 ; P-019
   corrigée) ; champs du scellement (texte-01 ; décisions) ; verrou 5 (liste de la section 5) ; verrou 6 et section
   « Contre-lecture » : contre-lecture 5 (méthode : `docs/notes/contre-lectures-papier-C-v1/brouillon5/methode/contre-lecture-R2-brouillon5-methode-v1.md`,
   `0c492f02…`, brouillon relu `9d55160f…`, « scellable après corrections ») et contre-lecture 6 (texte :
   `…/brouillon5/texte/contre-lecture-R2-brouillon5-texte-v1.md`, `12879073…`, même brouillon, « scellable après
   corrections ») remplies ; lectures des voisins (CV-08, CP-06, CS-01, CP-02) ; vérification du verrou de la famille 1 ;
   contre-lecture 7 (texte-04) ; ce traitement ; renvois aux réserves 14 à 16.
7. Ne remplir que ce que les pièces donnent ; laisser les autres marqueurs. Lancer `problemes` et verser sa sortie.

### 6.2 Ce que porte la configuration brouillon 3

- `version` (brouillon 3) ; `statut` avec la phrase de texte-01.
- `stabilite_rang` selon P-019 tranchée : `C_P3a` (W exact et rééchantillonnage centré, CL5-02, point 3) ; `C_P3b`
  (écarts intra-famille, rééchantillonnage centré pour le verdict ; τ des quinze valeurs rapporté), ou « rapportée sans
  verdict » ; `C_P3c` (gains d'écart bruts des juges, consigne A, mode direct ; texte-05) ; la règle des deux lectures ;
  `decision`, `lecture_recommandee` et `repli_si_refus` mis à l'état de la décision au scellement (texte-01) ;
  `etape2.permutations_tau_C_P3b` gardé pour le τ rapporté.
- `etape2.loi_nette` : `lecture_sans_calibrage` et `diagnostic_r` (CL5-01, point 5, mots exacts) ; `w_barre` (CL5-10).
- `etape2` : `seuil_C_P2_C_P1` = 0,025 ; `correction_C_P2_C_P1` ; `seuil_structure_bilateral` = 0,05 ; `valeurs_p`
  (décompte ; verdicts en valeurs p par décompte, critères en intervalles par BCa : CL5-07) ; `bonferroni_sondes`
  (1 − 0,10/m et 1 − 0,05/m) (CL5-10, mots exacts).
- `etape2.effectif_efficace` : « e = 1 si p̂ vaut 0 ou 1 » ; `etape2.intervalles` : BCa non défini → percentiles,
  consigné (CL5-05).
- Réserve d'intention : intervalle à 95 % de l'écart apparié ĉ_intention − ĉ qui exclut 0 (CL5-09).
- `etape2.excedent_paragraphe` : lu aussi sur la sonde lectrice, pour C-P4b (CL5-04).
- `regle_temoins` : « dans l'ordre des rangs croissants » (CL5-11).
- `pilote.usd_max_par_lancement` renommé `usd_borne_stricte_par_lancement` (10, exclu) (texte-11).
- `derivation.demi_largeur_lambda` : moitiés tirées par tâches, 8 + 8, clé `papier-C/pilote/conception` (texte-07).
- Tirage des tâches de l'étape 2 : sans remise, uniforme, bassin trié par identifiant et écrit au manifeste avant le
  tirage ; sous-ensemble raisonné tiré parmi les n/2 tâches de l'étape 2 (texte-08).
- `agent_bras.decision_bras_usurpation` selon P-020 ; `agent_bras.usurpation` retiré si P-020 est refusée.
- Si CV-01 (b) : bloc du constat nu (insertion par corpus, son témoin par la règle des témoins), gardes lexicales rejouées.
- Rien pour R-309. Inchangés : vivier, témoins, longueurs, constantes (3,53 ; k de 3 à 5 ; z ; effectifs {60, 90, 120} ;
  demi-largeur cible 0,25), clés de graines (aucune clé neuve n'est demandée).

### 6.3 Ensuite : vérification courte et contre-lectures neuves

1. **Vérification courte de méthode** (sous-agent neuf, avant le scellement ; demandée par la lentille méthode pour
   CL5-01 à CL5-03) : (i) niveau sous le nul de C-P3a corrigée (conjonction W exact et rééchantillonnage centré), pour
   k = 3 et 5, 45 et 60 tâches, avec un vrai rééchantillonnage par tâches et au moins 1 000 essais ; (ii) niveau de C-P3b
   corrigée avec un vrai rééchantillonnage (tâches pour A, items pour B) au lieu de la loi des erreurs connue ; (iii) règle
   des deux lectures (calibrée et sans calibrage) pour les statistiques de rang, sous les modèles S et D de T3 ; (iv) règle
   conjointe de C-P1 (test du module de CL5-01, point 4) ; (v) C-P4b sur l'excédent des deux côtés : définition côté
   lecteur et niveau sans manipulation, dans le modèle de S6 ; (vi) texte-07 : moitiés par tâches et mise à l'échelle
   √((n_cal / 2) / n) ; (vii) ajout de CL5-06 aux Combinaisons ; (viii) remarque de CS-03 : la différence des différences
   ne retire le style que si les plaidoyers de l'honnête et du saboteur ont le même style ; dire si le contrôle descriptif
   du style de TC.2 suffit ou s'il faut une réserve. Le résultat déclenche, le cas échéant, la clause de repli de P-019.
2. **Lectures restantes du verrou 2** : versions publiées de Kumaran et al. et de Pan et al. (section 4.3, point 1) ; Weng
   et al. et Zhu et al. (point 2) ; fin de la lecture des cinq voisins de CP-02.
3. **Contre-lecture courte des notes de voisins** (section 4.3, point 3).
4. **Contre-lecture « texte » du brouillon 6** (application de ce traitement), avec une question explicite : la
   déclaration de la réserve 14 suffit-elle (R-309) ? Si elle établit que non : repli (b) de R-309.
5. **Contre-lecture 7** : module et configuration brouillon 3, avant le scellement (texte-04).
6. **Mesures de conception v2** écrites, versées, contrôlées au versement (CL5-15).
7. Une contre-lecture « méthode » complète du brouillon 6 n'est pas demandée si la vérification courte ne trouve rien ;
   sinon, elle l'est sur les points trouvés.

## Réserves du préparateur

- L'extension de la règle conjointe aux statistiques de rang (section 3) est mon raisonnement sur le modèle du script T3 ;
  elle n'est pas simulée. La clause de repli et la vérification courte (point iii) la couvrent.
- Les chiffres de la section 3 viennent de modèles jouets (lois normales, deux contenus par tâche ; 400 à 1 500 essais ;
  erreur de Monte-Carlo ≈ 0,01 sur un taux de 0,03), réserve que la lentille méthode déclare elle-même (rapport,
  l. 434-440).
- Je n'ai pas vérifié mot pour mot que chaque correction s'insère aux lignes citées du brouillon 5 ; j'ai contrôlé par
  sondage les lignes des constats majeurs.
- Les pages des PDF ne sont pas relues ici : je m'appuie sur les contrôles par script des lecteurs (83, 94 et 151
  citations, aucun échec, gardes testées sur artefact).
- `R/registres/decisions.md` et `R/registres/go.md` changent pendant la session : empreintes de l'état lu vers 00:10 UTC.
- Les décisions de la section 4.3 et les modifications de la table sont des propositions : la session les tranche avant
  de sceller ce traitement sous son nom.

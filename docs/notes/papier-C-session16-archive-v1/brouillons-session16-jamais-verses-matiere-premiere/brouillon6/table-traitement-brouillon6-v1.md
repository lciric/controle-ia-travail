# Papier C — table de traitement du brouillon 6 du préenregistrement (HC1 à HC3) — v1

Rédacteur neuf du brouillon 6 (sous-agent, session 16, 2026-10-21). Je n'ai écrit ni les brouillons 1 à 5, ni les
brouillons 1 et 2 de la configuration, ni aucune contre-lecture, note de voisins, projet de traitement ou traitement.
Une ligne par constat : identifiant, décision de la session, passage du brouillon 6 (sections de ce brouillon) ou « non
appliqué » et pourquoi, écart éventuel. « Mots exacts » : les mots du rapport cité, aux lignes que donne le projet de
traitement ; les marqueurs de note y sont remplis par le chemin de versement proposé et l'empreinte (écart E-03).

## Pièces (empreintes recalculées, toutes égales à leurs compagnons `.sha256`)

- Consigne : `…/consigne-redacteur-brouillon6-v1.md` (`dc25318d64fb9fffc2f1ce911f66ed9df3f1b0120bf8e74f07ad237b93e45753`).
- Base : brouillon 5 (`9d55160f59cfb19e489dccc586e748173669b1373b570f5d42beb02293332969`) ; configuration brouillon 2
  (`77252564163e25445421e932ff46b42634487ace242ac1861bb9f61586f07efb`).
- Appliqué : traitement de la session `…/traitement-contre-lectures-brouillon5-papier-C-v1.md`
  (`08ca42ae7bd70a08a3695aca66ba0d16ee175da1771ba2c37ed6eda20cceb00e`), qui adopte avec amendements le projet
  `…/traitement-brouillon5/traitement-contre-lectures-brouillon5-papier-C-projet-v1.md`
  (`c65aa83acb830c765b9bc4cee7f600d45708771eef12de0502237a4234d42d25`). Les amendements priment.
- Rapports (mots exacts) : texte (`12879073…`), méthode (`0c492f02…`, simulations : manifeste `6f76e9df…`, 27 fichiers
  conformes), Joswin et Hu et Qu (`55222cdb…`), sept de Panin (`b3a6c187…`), second rang (`8027bd53…`), voisins de CP-02
  (`abbb5aaa…`), voisins restants (`83e8f49b…`), contre-lecture courte (`7287498f…`), voisins de CV2-03
  (`9d94ae662910c9da6a0abdbbc2e4398aef974ad63634a861ccc0f2fec3b95e02`, manifeste `52987ee9…`) ; manifestes de ces
  dossiers vérifiés par `sha256sum -c`, aucun échec. La note de CV2-03, absente à mon premier passage, était rendue et
  scellée avant que j'écrive le verrou 2 final : elle est appliquée, le marqueur `<<VOISINS_CV2_03>>` n'est plus au texte.
- Dépôt (lecture seule) : `registres/decisions.md` lignes R-307, R-308, R-309, R-312, P-019, P-020, P-021, P-022 (aucune
  réponse de Lazar sur P-020, P-021, P-022 au registre) ; `registres/go.md` GO-2026-10-17-01, GO-2026-10-20-06, -07, -09,
  -13, -14 ; `src/controle_ia/prereg.py` (`3b2e3ee5…`) ; gabarit (`8cad4371…`) ; compagnons des rapports du niveau 2.
- Sorties : brouillon 6 (`papier-C-preenregistrement-HC1-HC3-v1-brouillon6.md`, empreinte dans son compagnon et dans
  `problemes-brouillon6-v1.txt`) ; configuration `papier-C-config-v1-brouillon3.json`
  (`85173b22defe2c55844f23691028233a13746394324d0c598d3a66fb4f68820d`) ; cette table ; sortie de `problemes`. Outils,
  sous `travail/` (compagnons) : `ecrire_config_brouillon3_v1.py` et son journal ; `construire_brouillon6_v1.py` (chaque
  changement du texte est un remplacement exact, trouvé une seule fois dans le brouillon 5, sinon arrêt) et son journal.

## 1. Décisions de Lazar et amendements de la session

| constat | décision | passage du brouillon 6 | écart |
|---|---|---|---|
| R-307, ajout 1 (verrou « famille 1 sans contingence ») | remplacé par R-309 | non appliqué : aucun verrou de ce type n'est écrit (projet, section 2) | — |
| R-307, ajout 2 (clause d'ouverture) | appliqué | Plan, section 3, « Clause d'ouverture », après « Familles et échafaudage » ; section 5, dernière phrase | mots du projet, section 2.1 |
| R-307, ajout 3, et R-309 (déclaration) | appliqué | Plan, section 7, réserve 14 | mots du projet, section 2.2 |
| R-309, repli (b) | appliqué | verrou 7 ; n'entre pas au texte scellé | mots du projet, section 2.3 |
| GO-2026-10-20-13 et -14 | appliqué | GO ; champs du scellement, « Décisions » ; « Ce que change le brouillon 6 » | — |
| R-307, R-308, R-309 au registre | appliqué | documents qui font foi, registre des décisions | — |
| Configuration et R-309 | appliqué | rien dans la configuration (étiquette au texte seul) | — |
| Amendement 1 : P-021 remplace P-019 ; défaut 48 heures après la transmission | appliqué | verrou 1 ; bloc P-021 (Prédiction ; Critères) ; champs, « Décisions » ; configuration `stabilite_rang` | aucune date de défaut du 2026-10-22 n'est reprise |
| Amendement 2 : P-020 transmise ; CV-01 devient P-022 (proposition, défaut (b)) | appliqué | verrou 1 ; bloc P-020 (Plan, section 3) ; blocs P-022 (Métrique, point 5 ; Plan, TC.1 ; réserve 9) ; configuration `agent_bras`, `constat_nu` | — |
| Amendement 3 : voisins de CP-02 ; CQ-01 à CQ-07 acceptés ; CQ-08 à CQ-11 notés ; écart réseau noté | appliqué | lignes CQ ci-dessous | — |
| Amendement 4 : décisions de la session (projet, 4.3) acceptées | appliqué | section 5 ci-dessous | — |
| Amendements 5 et 6 : sceau de la consigne commune ; versements | session | verrou 5 (liste) | rien à écrire de plus |

## 2. Lentille « texte et conformité » (`12879073…`)

| constat | décision | passage du brouillon 6 | écart |
|---|---|---|---|
| texte-01 | accepté | champs du scellement, configuration ; configuration `statut` | « les deux champs » devient « les trois champs », `constat_nu` ajouté (P-022, après le rapport) |
| texte-02 | accepté | verrou 1 ; marqueurs `<<TRANCHER_P021>>` (six en-têtes), `<<TRANCHER_P020>>` (deux), `<<TRANCHER_P022>>` (sept) | P-019 lu P-021 (amendement 1) ; marqueur de P-022 par analogie (projet, 6.1, point 3) |
| texte-03 | accepté modifié | historique (chemins `docs/notes/…` et empreinte de la table du brouillon 5) ; verrou 5 (mots exacts, puis liste du projet, section 5) ; « Pièces de contre-lecture citées » | le script de contrôle des chemins est à écrire par la session |
| texte-04 | accepté modifié | verrou 2 (une ligne par note, verdicts écrits) ; « Contre-lecture 7 » en mots exacts | `<<CHEMIN_NOTE_VOISINS_BIBLIO>>` non écrit (modification du projet) ; les notes étant rendues, leurs marqueurs sont remplis (E-03) |
| texte-05 | accepté | Prédiction (phrase après le préambule) ; Critères (préambule) ; bloc P-021, ligne C-P3c ; configuration `stabilite_rang.C_P3c` | — |
| texte-06 | accepté modifié | Métrique, point 13 : l'exception, mots du projet | réserve « effet d'agrégation possible sur d » non ajoutée (remplacée par CL5-04) |
| texte-07 | accepté modifié | point 18 : ligne déclarée du projet ; Plan, section 2 : validation croisée par huit et huit tâches ; configuration `derivation.demi_largeur_lambda` | point 18 inchangé sinon (projet) |
| texte-08 | accepté | Plan, section 0, « À l'étape 2 » ; « Modérateur raisonné » ; configuration `partage_taches.tirage_etape2`, `tirage_raisonne` | « sans strate par origine » ajouté (décision de la session, 4.3, point 7) |
| texte-09 | accepté | « Rappel du brouillon 4, corrigé » | — |
| texte-10 | accepté modifié | empreinte `d23bd62f…` (documents ; Plan, section 0) ; empreintes abrégées des rapports du niveau 2, recopiées des compagnons ; registres « lignes citées au commit du scellement » (GO ; documents) | `<<EMPREINTE_TACHES_SOURCE_64>>` laissé à la session (4.3, point 8) |
| texte-11 | accepté | point 11 « jackknife sur les grappes » ; configuration `pilote.usd_borne_stricte_par_lancement` ; contre-lectures 1 à 4 ; P-020 « ). Proposition » | contre-lectures 1, 3 et 4 écrites sur le modèle donné pour la 2 ; configuration `etape2.intervalles` dit aussi « grappes » (accord) |
| texte-12, texte-13, texte-16 | information | aucune action | — |
| texte-14 | accepté | `problemes-brouillon6-v1.txt` montre les marqueurs de texte-02, texte-04 et de ce traitement | — |
| texte-15 | session | non appliqué au texte : registre (heures de transmission déjà écrites par R-312, P-021, P-022) | — |

## 3. Lentille « méthode statistique » (`0c492f02…`)

| constat | décision | passage du brouillon 6 | écart |
|---|---|---|---|
| CL5-01 | accepté | point 8 bis (points 1 et 4) ; Seuil, C-P1 (point 2) ; réserve 15 (point 3) ; configuration `etape2.loi_nette` (point 5) ; extension aux statistiques de rang : bloc P-021, « Deux lectures » | « réserve 14 » numérotée 15 |
| CL5-02 | nœud (P-021) | bloc P-021, version recommandée : ligne C-P3a (point 1), critères (point 2), configuration (point 3) | point 4 (session) : fait par P-021 |
| CL5-03 | nœud (P-021) | bloc P-021 : ligne C-P3b ; Seuil, C-P3 ; configuration `stabilite_rang.C_P3b` ; replis (B) et (C) écrits | — |
| CL5-04 | accepté | Prédiction, C-P4b ; audit A8 ; réserve 6 ; point 13 (exception de texte-06) ; configuration `etape2.excedent_paragraphe.lu_aussi` | — |
| CL5-05 | accepté | point 15 ; point 11 ; configuration `etape2.effectif_efficace`, `etape2.intervalles` | point 15 : la phrase est placée après la parenthèse qui suit « non entiers », pour garder la phrase entière |
| CL5-06 | accepté modifié | point 10 ; Combinaisons (deux lignes, dont l'ajout de la session « ĉ brut (point 8) ») ; A1, A2, A5, A7 ; point 16 | — |
| CL5-07 | accepté | point 12 ; configuration `etape2.valeurs_p` | — |
| CL5-08 | accepté | point 8 bis (test du module, avec la règle conjointe de CL5-01) ; point 11 (test des bornes) | script S2 cité avec son empreinte complète (`60219b56…`) |
| CL5-09 | accepté | point 8 bis ; Combinaisons ; configuration `etape2.reserve_intention` | — |
| CL5-10 | accepté | configuration : `etape2.seuil_C_P2_C_P1` (0,025), `correction_C_P2_C_P1`, `seuil_structure_bilateral` (0,05), `valeurs_p`, `bonferroni_sondes`, `loi_nette.w_barre` | mots exacts |
| CL5-11 | accepté | Plan, section 2, « Témoins » ; configuration `regle_temoins` | — |
| CL5-12 | accepté | « borne haute de l'intervalle bilatéral à 95 % (BCa) de Ḡ » : Prédiction, C-P2 et C-P6 ; Critères, C-P2 et C-P6 | — |
| CL5-13 | session | non appliqué au texte : devis de la piste C | — |
| CL5-14 | accepté modifié | point 18 (ligne de texte-07) | option « écarts à la moyenne de la famille » non retenue (projet) |
| CL5-15 | session | non appliqué : mesures v2 à écrire et verser (verrou 5, `<<EMPREINTE_MESURES_V2>>`) ; T2b cité, jamais la table (a) de T2 (bloc P-021) | — |
| CL5-16 | accepté | comme texte-10 | — |

## 4. Voisins : Joswin et al., Hu et Qu (`55222cdb…`)

| constat | décision | passage du brouillon 6 | écart |
|---|---|---|---|
| CV-01 (a) | accepté | réserve 9 ; réserve 16 ; contre-indice « Plancher sans locuteur » | « réserve 14 » écrit « réserve 16 » ; réserve 16 : une parenthèse finale de moi dit que les indices sont ceux de la fente {QUALITE}, recomptés par script, et que la tournure varie (la clause littérale n'apparaît qu'une fois : famille 2, indice 8) |
| CV-01 (b) = P-022 | proposition en attente | Métrique, point 5 ; Plan, TC.1 ; fin de la réserve 9 (version recommandée), avec replis (a) et (c) ; configuration `constat_nu` | les mots de la note (« ; **constat nu** … ») sont écrits en paragraphe propre sous le point 5, pour porter le marqueur ; insertion non lue au pilote (variante du projet non tranchée par la session : laissée à la session) |
| CV-02 | remplacé | non appliqué : remplacé par CP-06 (branche « sinon ») et CS-01 | — |
| CV-03 | accepté | HC1, « ajouts du brouillon 6 » ; « Familles et échafaudage », grille | « réserve 14 » lu 16 (même constat que CV-01) ; liste en puces |
| CV-04 | accepté | point 10, fin | — |
| CV-05 | accepté | contre-indices, « Sondes lectrices » | — |
| CV-06 | accepté modifié | contre-indices, famille « revendication d'autorité » | parenthèse remplacée par CS-02 (a) |
| CV-07 | accepté | contre-indices, « Poids du conseil quasi binaire » | — |
| CV-08 | accepté modifié | section « Contre-lecture » (paragraphe des notes) ; champs, « Décisions » (liste allongée) | placé avant la contre-lecture 5, non à la fin de la section (E-01) |
| CV-09, CV-10 | information | aucune action (citer en qualitatif) | — |
| CV-11 | session | non appliqué : veille HC4 | — |

## 5. Sept voisins de Panin (`b3a6c187…`)

| constat | décision | passage du brouillon 6 | écart |
|---|---|---|---|
| CP-01 | accepté modifié | verrou 2, paragraphe « Kumaran et al. » (mots exacts, puis CQ-02 et CR2-02) ; Pan et al. : liste des sept (CR2-04) et une phrase de moi | contrôles faits (notes CP-02 et restants) |
| CP-02 | accepté modifié | verrou 2 : la phrase est remplacée par celle de CQ-01 (note rendue) ; sa dernière phrase (Zhu et Weng) est remplacée par celle de CR2-01 | marqueurs de texte-04 sans objet : note rendue (amendement 3) |
| CP-03 | accepté | HC1, « ajouts du brouillon 6, voisins de Panin » ; « Familles et échafaudage », grille | bloc Kumaran modifié par CQ-02, CR2-02 et CV2-02 |
| CP-04 | accepté | HC3, composante 2 | — |
| CP-05 | accepté | contre-indices : « Emphase et nombre », « Titres seuls », « Seuil de confiance » | CR2-06 inséré ; « ; » devant « En sens contraire » écrit « . » (ponctuation) ; CR2-09 ajouté |
| CP-06 | accepté | verrou 2 (branche « sinon ») ; section « Contre-lecture » ; champs, « Décisions » | placement comme CV-08 (E-01) ; empreinte de la note de Joswin ajoutée (R6) |
| CP-07, CP-08 | information | aucune action | — |
| CP-09 | rédaction anglaise | non appliqué : aucune action au préenregistrement | — |
| CP-10 | session | non appliqué : veille HC4, HC5 | — |

## 6. Voisins de second rang (`8027bd53…`)

| constat | décision | passage du brouillon 6 | écart |
|---|---|---|---|
| CS-01 | accepté | verrou 2 ; section « Contre-lecture » (ligne de moi, même forme que CV-08) | modifié par CW-01 |
| CS-02 (a) | accepté | contre-indice de la famille 2 (dans CV-06) | puis modifié par CW-02 (source lue sur PDF ; « within 4.4% » cité avec le démenti du tableau des auteurs) |
| CS-02 (b) | accepté | contre-indices, deux puces après CV-06 | — |
| CS-03 | accepté modifié | HC2b, sous-puce « Précédents cités » | remarque pour la méthode : verrou 6 (contre-lecture 8) |
| CS-04 | accepté | point 10, après CV-04 | — |
| CS-05 | accepté modifié | HC3, composante 2 (mots du projet) | placé après CQ-03 |
| CS-06 | écarté | non appliqué : Zhong et al. ne portent pas sur des juges (projet) | — |
| CS-07 | accepté | dossier de P-022 (enjeu) ; rien au texte | — |
| CS-08 | information | aucune action | — |
| CS-09, CS-10 | session | non appliqué : veille | — |

## 7. Vérification du verrou de la famille 1 (`0cbd3ae3…`)

| constat | décision | passage du brouillon 6 | écart |
|---|---|---|---|
| VF-01 | accepté (R-309) | réserve 14 ; section « Contre-lecture » | — |
| VF-02 | accepté | réserve 14 (autres familles, cas limites) | — |
| VF-03 | écarté | non appliqué : hors du champ de R-307 et de R-309 | — |

## 8. Voisins de CP-02 et résumé publié de Kumaran et al. (`abbb5aaa…`)

| constat | décision | passage du brouillon 6 | écart |
|---|---|---|---|
| CQ-01 | accepté | verrou 2, paragraphe « Voisins de second rang cités par les sept papiers » | la phrase gardée (Zhu et Weng) est remplacée par CR2-01 |
| CQ-02 | accepté | verrou 2, paragraphe « Kumaran et al. » ; bloc Kumaran de HC1 | puis modifié par CR2-02 |
| CQ-03 | accepté | HC3, composante 2 | modifié par CV2-04 |
| CQ-04 | accepté | point 17 ; réserve 9, fin | — |
| CQ-05 | accepté | contre-indice « Rôle « système » imité en texte brut » | modifié par CV2-04 |
| CQ-06 | accepté | section « Contre-lecture », paragraphe des notes ; champs, « Décisions » | — |
| CQ-07 | session | non appliqué : veille | — |
| CQ-08, CQ-09, CQ-10 | information | aucune action | — |
| CQ-11 | session | non appliqué : veille (amendement 3) | — |

## 9. Voisins restants (`83e8f49b…`)

| constat | décision | passage du brouillon 6 | écart |
|---|---|---|---|
| CR2-01 | appliqué (consigne : mineurs et forme) | verrou 2, paragraphe « Voisins cités par Bajaj et Tiganj », à la place de la phrase du brouillon 5 et de la phrase gardée par CQ-01 | — |
| CR2-02 | appliqué | verrou 2, paragraphe « Kumaran et al. » ; bloc Kumaran de HC1 (« corps lu », « latitudes », « SimpleQA, GSM-MC ») | — |
| CR2-03 | appliqué | verrou 2, phrase « Page de l'éditeur reçue … » | `<<DECISION_ECART_EDITEUR>>` rempli par la décision de la session sur cette même page (amendement 3 : « noté, sans effet sur le contenu ») ; la session confirme qu'elle vaut pour la lecture du corps |
| CR2-04 | appliqué | verrou 2, liste des sept (Pan et al.) | — |
| CR2-05 | appliqué | HC1, « voisins de Bajaj et Tiganj » ; « Familles et échafaudage », grille | — |
| CR2-06 | appliqué | contre-indice « Emphase et nombre » | voir CP-05 |
| CR2-07 | appliqué | section « Contre-lecture », paragraphe des notes ; champs, « Décisions » (Zhu et al. ; Weng et al.) | — |
| CR2-08 | session | non appliqué : veille | — |
| CR2-09 | appliqué (information, ajout facultatif) | contre-indice « Seuil de confiance » | — |
| CR2-10, CR2-11 | information | aucune action | — |
| CR2-12 | session | non appliqué : veille HC5 | — |

## 10. Contre-lecture courte des notes de voisins (`7287498f…`)

| constat | décision | passage du brouillon 6 | écart |
|---|---|---|---|
| CV2-01 (majeur) | levé | non appliqué en mots exacts : le corps publié de Kumaran et al. a été lu (CR2-02) ; « à lire avant le scellement » serait faux | — |
| CV2-02 | appliqué | bloc Kumaran de HC1 | — |
| CV2-03 | levé | verrou 2 et section « Contre-lecture » : lecture sur PDF faite (CW-01, CW-08) ; sa correction en mots exacts vise la note de second rang, non ce texte | — |
| CV2-04 | appliqué | HC3, composante 2 (CQ-03) ; contre-indice de la famille 4 (CQ-05) | — |
| CV2-05 | non appliqué | sa correction vise une citation de la note de Panin, absente de ce texte | à la session (note) |
| CV2-06 | information | « presque aucun » cité en qualitatif ; aucun chiffre en puissance ni seuil | — |
| CV2-07, CV2-08 | information | aucune action | — |

## 11. Voisins de CV2-03 : Wang K. et al., Poonia et Jain (`9d94ae66…`)

Appliqués selon la consigne (constats mineurs et de forme en mots exacts ; deux corrections facultatives d'information
retenues, comme CR2-09). « Pas de collision » pour les deux, PDF entiers.

| constat | décision | passage du brouillon 6 | écart |
|---|---|---|---|
| CW-01 | appliqué | verrou 2, paragraphe du second rang (texte de CS-01 modifié) | sa seconde correction vise le texte de CV2-03 (note), absent d'ici ; la ligne de la contre-lecture courte dit le constat levé |
| CW-02 | appliqué | contre-indice de la famille 2 (texte de CS-02 (a) modifié) | — |
| CW-03 (information, facultatif) | appliqué | contre-indices, « Sondes lectrices » | — |
| CW-04 (information) | appliqué en partie | « Familles et échafaudage » : grille de Wang K. et al. (phrase propre, sans le « ; » initial) | point sur la voix grammaticale (personne qui varie avec l'intensité dans une famille) : à vérifier par la session sur le vivier ; je ne lis pas le texte des formulations |
| CW-05, CW-06, CW-09 | information | aucune action (citer en qualitatif) | — |
| CW-07 | session | non appliqué : vise la note de second rang et la veille | — |
| CW-08 | appliqué | section « Contre-lecture », paragraphe des notes | — |

## 12. Décisions de la session (projet, section 4.3)

| point | passage du brouillon 6 |
|---|---|
| 1. contrôles des versions publiées de Kumaran et al. et de Pan et al. | faits ; verrou 2 |
| 2. Weng et al. et Zhu et al. | faits ; verrou 2 (CR2-01) ; HC1 (CR2-05) |
| 3. contre-lecture courte des notes | faite ; verrou 2 ; section « Contre-lecture » |
| 4. registre | session (déjà écrit : R-312, P-021, P-022) |
| 5. réserves 14, 15, 16 | Plan, section 7 |
| 6. R-309 au texte seul | réserve 14 ; configuration sans champ |
| 7. tirage uniforme, sans strate | Plan, section 0 ; configuration |
| 8. source des 64 tâches remplie au scellement | marqueur laissé |
| 9. écart de la lentille texte | session (registre) ; non lu ici |
| 10. dossier `outils-texte/` | verrou 5 (annexes avec provenance) ; dossier non lu par moi |
| 11. voisins aux « cités comme publiés » | champs, « Décisions » ; `<<DECISION_VOISINS>>` laissé (marqueur connu du scellement) |
| 12. CL5-04 l'emporte sur texte-06 | point 13 ; C-P4b |

## 13. Écarts du rédacteur

- **E-01** — Les paragraphes des lectures de voisins (CV-08, CP-06, CS-01, CQ-06, CR2-07, contre-lecture courte,
  vérification du verrou) sont tous placés à la suite du paragraphe « Contre-lectures des notes de lecture », avant la
  contre-lecture 5, et non à la fin de la section. Raison : `problemes` rattache tout le texte qui suit une entrée
  « Contre-lecture k » à cette entrée ; des empreintes réelles placées après les contre-lectures 7 à 9 masqueraient
  leurs empreintes manquantes (R5 : aucun repli silencieux).
- **E-02** — Contre-lectures 8 (vérification courte de méthode) et 9 (texte du brouillon 6) ajoutées avec leurs
  marqueurs, sur le modèle de texte-04, pour que le validateur bloque tant qu'elles manquent.
- **E-03** — Marqueurs de note des corrections (`<<CHEMIN_NOTE_JOSWIN_HUQU>>`, `<<CHEMIN_NOTE_PANIN_SEPT>>`,
  `<<CHEMIN_NOTE_SECOND_RANG>>`, `<<CHEMIN_NOTE_VOISINS_CP02>>`, `<<CHEMIN_NOTE_VOISINS_RESTANTS>>` et leurs empreintes)
  remplis par le chemin de versement proposé (projet, section 5 : `docs/notes/contre-lectures-papier-C-v1/brouillon5/<dossier>/`)
  et l'empreinte recalculée ; pour les voisins restants et la contre-lecture courte, rendus après le projet, le même
  chemin par analogie. Chemins à confirmer au versement (le script de texte-03 le vérifiera).
- **E-04** — Chemins proposés par analogie, non donnés par les pièces : projet de traitement et consigne du rédacteur
  sous `docs/notes/contre-lectures-papier-C-v1/` ; configuration brouillon 3 sous `brouillons/` ;
  `ecrire_config_brouillon3_v1.py` et son journal sous `docs/procedures/papier-C-v1/` (versement par la session ; ils sont
  aujourd'hui sous `…/brouillon6/travail/`).
- **E-05** — Jiang et al. (ChatBug), cité comme publié à la réserve 9 (CQ-04), et Wang K. et al., cité aux contre-indices
  (CW-02, CW-03), ajoutés à la liste des « cités comme publiés » des champs ; aucune correction ne les y mettait.
- **E-06** — Constat nu : témoin calculé dès maintenant par la règle des témoins (famille à un rang, longueurs du corpus
  A) : indice 4, écart de 6 caractères (configuration `constat_nu.temoin_indice`) ; longueurs remplies 39 (A) et 23 (B) ;
  gardes « toutes insertions et témoins » : aucune correspondance. Le gabarit écrit dans la configuration est celui de la
  note (CV-01 (b)) ; son remplissage est égal, octet pour octet, aux deux phrases de la note (contrôle booléen, sans
  affichage).
- **E-07** — Configuration : `stabilite_rang.repli_si_refus` devient un objet à deux branches, `B` et `C` (P-021 a trois
  options) ; clés neuves `deux_lectures`, `clause_repli` ; `partage_taches.tirage_etape2`, `tirage_raisonne` ;
  `etape2.reserve_intention`, `excedent_paragraphe.lu_aussi` ; bloc `constat_nu` ; `controle_redaction.longueurs_constat_nu`.
  Aucune clé de graine neuve. Champs figés vérifiés égaux par empreinte : juges, agent, échelle, consignes, raisonné,
  contenus neutres, fentes, insertion, vivier, témoins, gardes, graines, confidentialité, paragraphes de bras.
- **E-08** — « Ce qu'avait changé le brouillon 5 » est gardé en rappel, tel quel, sous la liste du brouillon 6.
- **E-09** — Énoncés : aucun changé. Les ajouts de HC3 (composante 2) suivent, dans la même puce, les précédents déjà
  écrits au brouillon 5, comme les corrections le demandent ; ceux de HC2b sont en sous-puce (projet, CS-03).
- **Nœuds** : aucune correction n'exige de changer un énoncé, une famille, une constante ou une longueur ; aucune n'a donc
  été écartée pour ce motif.

# Rapport de rédaction — préenregistrement hors échantillon, brouillon 2 — v2 (traitement de la contre-lecture 1)

Rédacteur : le sous-agent auteur du brouillon 1 (il n'a pas écrit la contre-lecture 1). Contre-lecture 1 traitée :
`brouillons/preuves-mentors-v1/essaim-hors-echantillon-v1/contre-lecture-preenregistrement-essaim-hors-echantillon-v1.md`,
sha256 `dcec7d1a82abe21d13e72aa7714edcb30982222b3b8911301a28f485cfae76dc` (commit `5fe0bf8e`), sur le brouillon 1
`preenregistrement-essaim-hors-echantillon-v1-brouillon1.md`, sha256
`d1ec8c605672bbfc3b284a288ae9745236062230ac31c41834cd01f278f545c8` (commit `0828ad44`). Ce fichier est le
« fichier de traitement des remarques » que cite l'entrée de forme fixe de la contre-lecture 1 dans le brouillon 2 ;
il ne cite pas l'empreinte du brouillon 2 (elle est rendue avec ce rapport, hors fichier). Rien n'a tourné sur la
grille ; aucun commit ; aucune empreinte compagnon ; aucun fichier existant modifié (R12 : noms neufs).

## Traitement, une ligne par point

- **C1** acceptée : décompte par nature dans le texte (11 instrument / 244, 1 rejouée / 2, 7 risquées / 65 après R1, 18 discriminantes après R2) ; trois scores séparés calculés par `lecture_hors_echantillon_v2.annoter` et écrits en tête de `lecture.md` par le lanceur neuf `run_essaim_hors_echantillon_v2` (même nom de simulation que v1 : run unique commun) ; décompte vérifié sur la grille par `decompte` et par l'essai `test_grille_v2_decompte_et_discriminantes`.
- **C2** acceptée : « hors échantillon » dit famille par famille ; en P, cellules et graine neuves, pas les données ; portée conditionnelle des intervalles aux 60 épisodes écrite dans l'hypothèse.
- **C3** acceptée : `LIGNES_E` récrite (textes proposés, ligne 8 scindée par R1 en deux lignes HP.5a et HP.5b, la ligne de l'e-valeur exigeant HP.6), phrase de portée récrite ; table recopiée mot pour mot dans le texte, essai `test_table_E_recopiee_dans_le_brouillon2` (et absence des expressions retirées) ; textes de HP.2, HP.3, de l'énoncé « en clair » et des issues remplacés.
- **C4** acceptée : chronométrage déclaré exactement (cellules `S/e20x10/T_synchro_m20` et `Q/e10x20/c0.4/T_synchro_m5` calculées en mémoire sous 424243, taux non affichés), graines 424243 et 123456789 dites dérivées par tâche, disjonction par la racine (2⁻⁹⁶) ; vérification Monte-Carlo corrigée (K = 5, T = 7 seulement) ; empreinte du script des moments ajoutée ; déclaration de ce qui a été lu de P3, y compris l'affichage, à l'inspection de structure, des scores des deux premières actions honnêtes sur les 430 sondes.
- **C5** acceptée : parade procédurale écrite (empreinte du brouillon 2 consignée et poussée avant l'étape 0 ; entrées de contre-lecture de forme fixe ; commit cité créé une fois ; journal git versé automatiquement par le lanceur v2 dans `diag/<run_id>/journal-git.json` ; déclaration d'absence de pré-run) ; parade mécanique (R5) non retenue, écrite en « Limites ».
- **C6** acceptée : « trop beau » calculé (`audit_symetrie.trop_beau`, compté dans `audit_declenche`) ; déclencheur sur la confirmation des 7 risquées ou la conformité de toutes les discriminantes ; contenu d'audit écrit (relecture des bornes, de la loi P3 et du script des moments ; rapport sans verdict de ce que la loi de référence prédisait) ; essai cas sain et artefact.
- **C7** acceptée : résolution exacte (chiffres du contre-lecteur, plus les seuils bilatéraux de HP.4 : 0,5656 ≤ p̂ ≤ 0,8490 et 0,3246 ≤ p̂ ≤ 0,6048) et règle de lecture d'un nul ou d'un « non concluant ».
- **C8** acceptée : `` `<<COMMIT_CITE>>` `` entre accents graves ; étape 0.d récrite (tous les marqueurs, contrôle `COMMIT_CITE.search`) ; contre-lecture 1 écrite en forme fixe, marqueur `<<CONTRE_LECTURE_2>>` ajouté.
- **C9** acceptée : essais neufs du lanceur v2 (réplication forcée, seconde réplication refusée, « rien à répliquer », durée, données P3 absentes, run unique commun avec le lanceur v1) et de la lecture v2 (garde d'erreur certifiée) ; phrase des gardes corrigée.
- **C10** acceptée : marges justifiées après coup et déclarées comme telles ; sensibilité aux marges 0,010 et 0,020 (vérifiée sans tirage : +5 et −7 cellules, listes du contre-lecteur exactes) ; cellule phare retenue seulement pour une marge ≤ 0,0185 ; neuf cellules à moins de 0,004 de la marge ; valeurs de v1 à c = 0,2 et 0,4 citées avec l'empreinte de `bloc-HE6.json`.
- **C11** acceptée : 11 formes closes dans l'audit ; HS.4 et HQ.4 classées instrument ; phrase « la frontière monte » remplacée ; règle de graine en octets ; multiplicité du côté des fausses confirmations ; interpréteur de l'environnement du dépôt principal ; empreintes du chronométrage ; « charge 6,9 » dite relevée par `uptime` au lancement et non consignée ; renvoi au programme ; rangées d'issues ajoutées.
- **R1** appliquée : HP.5a (7 cellules « en dessous » de la sonde des enjeux) et HP.5b (13 autres) ; deux lignes d'énoncés.
- **R2** appliquée : HP.4 bilatérale ]0,55 ; 0,86[ et ]0,31 ; 0,62[ (sens « entre_x ») ; les deux cellules deviennent discriminantes (la loi de référence donne 0,9285) ; 16 + 2 = 18 discriminantes.
- **R3** appliquée (descriptif, coût faible) : `blocs_hors_echantillon_v2.bloc_maxima` (histogramme des positions des maxima d'agents et part au pas de co-élévation maximale, 20 000 essaims honnêtes par loi Q et par sonde P, tâches `…/maxima`), run principal seulement, sans verdict.
- **R4** non faite (consigne) : écrite en « Limites » — pas de second jeu d'épisodes honnêtes, pas de variante disjointe en épisodes.
- **R5** non faite (consigne) : écrite en « Limites » — aucun tiers disponible pour tirer un sel.
- **R6** appliquée : `bornes_synchro_v2.puissance_exacte` (inclusion-exclusion complète, arrêt certifié par Bonferroni, erreur ≤ 10⁻⁹) ; valeurs du contre-lecteur retrouvées (0,12158 ; 0,37762 ; 0,68643 ; 0,30157) ; HS.3 lue par le critère de forme close de v1 ; garde si l'erreur certifiée dépasse 10⁻⁶.

## Fichiers neufs (sha256)

| Fichier | sha256 |
|---|---|
| `src/controle_ia/simulation_essaim/bornes_synchro_v2.py` | `031baef94db704e711bb6c9d8f1a68c63c2fc5e113842e63228c11268aa0e0d7` |
| `src/controle_ia/simulation_essaim/blocs_hors_echantillon_v2.py` | `00de309ab4cdfb2232b37ecd4f274596da0bed83f2293a7b27bf693d61ddbfa7` |
| `src/controle_ia/simulation_essaim/lecture_hors_echantillon_v2.py` | `7a2e51b2ecdda018420daefbc4ad504a44d802ae48021431d81a973dd9500df7` |
| `src/controle_ia/simulation_essaim/run_essaim_hors_echantillon_v2.py` | `765ca37cf277dd1daadaec078d6111f96c9de29dcb8e9caf54bf16c30541377a` |
| `tests/test_simulation_essaim_hors_echantillon_v2.py` | `99f176aecebf4f639079717787e1dca4e45b8b877743ad316f42f2244dae0cce` |
| `generer_grille_v2.py` (ce dossier) | `5210650c08348b831010c1199c4b54c958df294a1feb3249e599404068012039` |
| `grille-essaim-hors-echantillon-v1-brouillon2.json` | `dbe1caf113ac12cf9e056cfd2f6916eb2d13341735cb58b0260acc64d86c8007` |
| `tables-valeurs-predites-v2.md` | `c94b65426448aa29c0aed75109ff28a28dc4be7865bac67ba673f268e20e9bc0` |

L'empreinte du brouillon 2 n'est pas dans ce fichier (le brouillon 2 cite celle-ci) : elle est rendue à la session principale.

# Addendum au préenregistrement de R1 — relance du rejeu des 2 400 actions de P3 après l'arrêt sur la garde CLC-03 — v1

- Auteur : sous-agent de préparation de la session « session-depot » (Opus 5.5), pour Lazar ; **brouillon 4 (texte,
  non scellé) ; reste la contre-lecture 2** (brouillon 2 : reprise du travail interrompu `54c851e4`, après la
  contre-lecture 1 et la vérification de concordance de conv-audit, n° 343 ; brouillon 3 : valeurs de C-6 remplies —
  extension exécutée, r = 3 ; table v2 et configuration v4 écrites ; comptes et essais refaits ; brouillon 4 : V-02 à
  V-04 et m-1 à m-8 de la vérification du brouillon 2 traités, voir « Contre-lecture »). L'entrée « Contre-lecture 2 »
  est la seule encore à remplir (la garde `controle_ia.prereg.problemes` refuse le scellement tant qu'elle l'est).
- **Décisions de Lazar** (2 novembre 2026, 06:32 UTC, dans la session de conv-audit ; registre R-1116 et lignes
  `GO-2026-11-02-01` et `GO-2026-11-02-02` de `registres/go.md` sur la branche `canal/conv-audit-n04`, commit
  `6a4aeffecec960c89cf18622c2f64822ff93660f` ; message n° 344,
  `cc8af25a27ded744ed1fde161625bc69568ec62bc8fefe37abbc36c94a0a540c`) : **N-A = (c) puis (a)** — d'abord la
  résolution sur processeur des 7 épisodes non résolus (C-6, l'empreinte de P3 seule juge), puis sa décision sur cet
  addendum couvre aussi la ligne recopiée dans l'analyse principale de conv-audit (l. 146) pour les épisodes que C-6
  laisserait non résolus (E19) ; **GO de la relance de R1 = `GO-2026-11-02-02`** (calcul, extension de
  GO-2026-11-01-13, plafond 25 USD inchangé, échéance 2026-11-09) ; GO-2026-11-01-13 échoit le 2 novembre et n'est
  plus le GO du lancement (il reste cité comme GO prolongé et pour les dépenses engagées). Ces lignes sont à recopier sur `main` par session-depot (n° 344, point 2), et Lazar les redit de sa main dans la session
  de session-depot (même point) : deux conditions du lancement (procédure, étape 1).
- Date (UTC) : 2026-11-02 08:14 (brouillon 4 ; heure relevée par `date -u` ; brouillon 3 : 07:54 ; brouillon 2 : 07:12).
- Préenregistrement parent (scellé, non modifié) : `prereg/R1-R2-rejeu-p3-v1.md`
  (`80c85a0085f444dc10f36e4e226d015802d2e20294c4fff2ae67adb0aca4ddea`), commit de scellement
  `567260c05687747f0c7a715fc9b15b4fc6297d65` (branche `prep/runs-r1-r2-r4-v1`), code cité `29bd8e2e…`.
- Chemin du préenregistrement parent : `prereg/R1-R2-rejeu-p3-v1.md`
- Commit du code d'analyse : `5e678b5b78152a4cf353a8386f54413111adf230`
- Documents qui font foi (chemin + empreinte) : le préenregistrement parent ci-dessus, qui garde tout ce que la section
  « Écarts au parent » ne change pas ; rapport d'enquête `docs/notes/runs-r1-r2-r4-v1/enquete-arret-r1-v1.md`
  (`377101ecd9b33c76c34ce799f8b511d60b71b089699a7df3dc0e4705ccbb00c3`) ; arrêt de R1
  `diag/20261102-002114-r1-rejeu-reel/arret.json` (`c6671d2c9534463f82da90c21eba80f29a2bce04e898643b59a0caa4c9a9eb07`,
  branche `calcul/r1-r2-reel-v1`) ; messages de conv-audit (branche `canal/conv-audit-n04`,
  `brouillons/canal-reprise-releve-v1/messages/`) n° 339 (`05179024bfe3332aa032ade5302f8f4b3373a618a2cb950f61f2ce0ea58d7794`),
  n° 343 (`841cae634327bab89ec40152e0bbbc240d1ae7d7b4a37608c6763ed847787419`, qui retire la demande « `fidele` = faux »
  du n° 339) et n° 344 (ci-dessus) ; rapport de concordance de conv-audit sur le brouillon 1
  `brouillons/preuves-mentors-v1/analyse-principale-r1-r2-v1/concordance-addendum-r1-v1.md`
  (`28d8bcff4e8a0ff9745a72ad6332296f580f84431c15f24cd98ba3c027a0555d`) ; leur analyse principale scellée
  (`prereg/analyse-principale-r1-r2-v1.md`, `8e267952…`, commit `83ce7a91`) ; **GO-2026-11-02-02** (ci-dessus) ;
  procédure de lancement `docs/notes/runs-r1-r2-r4-v1/procedure-relance-r1-v2.md` (la v1 reste archivée).
- Chemin de la configuration du rejeu : `prereg/R1-rejeu-config-v4.json`
- Configuration du rejeu (empreinte canonique) : `10707413da95082dfabb264a3303aac6f2bb1e53901c7a166470615a02ac941e`
  (configuration v4 : clés de la v3, table v2 ; empreinte du fichier
  `09bc5813d33952ec6e59b680d20b18484c1d017399fc7abb10c9d639dc1d0d04`)
- Chemin de la table de tokenisation : `prereg/R1-table-tokenisation-v2.json`
- Table de tokenisation (empreinte du fichier) : `5f6cf489eb971c195f7263cb738bc5f9de4bdf5cfd0f55658fd3977d3f4b55e2`
  (table v2, construite par la commande de l'étape 0)
- Entropie : `36410133060804533274328900142752730279`
- Tests attendus : `302`

**Statut.** Cet addendum remplace la garde CLC-03 du parent (« un épisode entièrement conforme en longueur à trajectoire
différente arrête la course ») par les règles A et B ci-dessous et le seuil qui les borne ; **tous ses écarts au parent,
cette garde comprise, sont réunis dans la section « Écarts au parent »** (une ligne par écart, pour la vérification de
concordance). Ce que cette section ne cite pas vaut tel quel. Il porte sur **R1 seule** : R2 ne se relance pas, et **le
rejeu de R4 n'est pas relancé par cet addendum** (il s'est arrêté sur la même garde ; une relance demanderait un
addendum propre à R4 et une concordance neuve ; C-7). L'entropie est celle du parent (aucun choix libre) ; l'échantillon
de fidélité est tiré parmi les éligibles de la relance (épisodes à trajectoire identique), donc différent de celui
qu'aurait tiré la première course, arrêtée avant ce tirage.

## Cause de l'arrêt (renvoi au rapport)

R1 (instance du 2 novembre 2026, ≈ 00:21 UTC) s'est arrêtée sur CLC-03 : « 21 épisodes entièrement conformes en
longueur à trajectoire différente » (`arret.json` ci-dessus). Cause établie par l'enquête (rapport cité, sections 1 et 2,
reproduction sans modèle identique à l'instance : 151 épisodes conformes en longueur, 129 identiques, 22 signalés ; 130
et 21 après la substitution du jeton de fin) : **la garde supposait qu'un épisode conforme en longueur a forcément les
identifiants de P3 ; c'est faux.** À température 1, l'agent de P3 a parfois échantillonné un **découpage non canonique**
d'un mot, de même longueur en jetons et qui se décode en le même texte (`Ġro` + `crap` au lieu de `Ġroc` + `rap`). Le
texte stocké ne le dit pas ; l'empreinte de trajectoire stockée par P3, qui couvre les identifiants, le voit. Ni le
gabarit, ni la date, ni la consigne, ni une version de bibliothèque (manifestes comparés, rapport section 2).

## Écarts au parent

Liste exhaustive (contre-lecture 1, CLA-01 ; concordance, C-1 à C-7). « Parent » = `prereg/R1-R2-rejeu-p3-v1.md`.
Notation : **r** = nombre des 7 épisodes non résolus par les étapes 1 à 3 que l'extension C-6 résout : **r = 3**
(C-6 exécutée, « Plan d'analyse », étape 0 ; les formules en r valent avec r = 3) ; les comptes ci-dessous sont donnés à la table des étapes 1 à 3 (table v1, `5309326b…`) et en
fonction de r (chaque épisode compte 10 actions).

| n° | Ligne ou règle du parent | Nouvelle règle | Raison |
|---|---|---|---|
| E1 | Plan, étape 1, et liste d'arrêt : CLC-03, « un épisode encore différent arrête tout » ; recherche des jetons de fin à la volée | **Règle A** : table de tokenisation calculée avant la carte, scellée, citée par la configuration, appliquée et vérifiée par l'empreinte de P3 (étapes 1 à 3 du module, puis extension C-6 : « Plan d'analyse », étape 0) | Cause établie : découpages non canoniques de même longueur (rapport d'enquête) |
| E2 | Même ligne | **Règle B** : un épisode conforme en longueur non résolu par la table ne fait plus arrêter la course ; il est traité **comme les 89 épisodes déjà non conformes en longueur** : `contexte_conforme` et `trajectoire_identique` faux, `conforme_longueur` gardant sa mesure, et **`fidele` tranché action par action par la tolérance** (règle du parent pour toute action hors contexte exact ; la règle de repli les exclut si le contrôle négatif ne discrimine pas) | La table ne résout pas tout (7 − r épisodes) ; voie recommandée par la concordance de conv-audit (n° 343, C-1), qui retire la demande « `fidele` = faux » du n° 339 |
| E3 | Seuil (aucun) | **Seuil de la règle B : 10 épisodes** ; au-delà, arrêt « non conforme » | Borner B ; fixé en connaissant le compte (voir « Seuil ») |
| E4 | P-R5 : « trajectoires identiques à P3 pour tous les épisodes entièrement conformes en longueur (garde) » | 144 + r trajectoires identiques, 7 − r épisodes non résolus (au plus 10), soit **147 et 4** à r = 3 ; « ≥ 90 % des actions notées fidèles (au plus 93 %) » **inchangé** | Conséquence de A et B |
| E5 | Critères de lecture : « Fidélité contraire, ou épisode conforme à trajectoire différente → rejeu non validé » | « Fidélité contraire, ou plus de 10 non résolus, ou table non applicable → rejeu non validé » ; **cette ligne est recopiée dans l'analyse principale scellée de conv-audit (l. 146) : voir E19** | Conséquence de A, B et E3 |
| E6 | Critères de lecture (aucune ligne) | **Ajout** : « au plus 10 non résolus → course normale ; leurs actions jugées par la tolérance ; nombre, liste et fidèles parmi elles rapportés » | Lecture de B |
| E7 | Critères de lecture (aucune ligne) | **Ajout** : « fidèles < 90 % des notées → réserve d'instrument portée par le résultat du run (`tokenisation.p_r5_au_moins_90_pour_cent`) et par la lecture du fournisseur, **sans changer aucune classe de verdict ni aucune ligne des analyses de conv-audit** » (la principale rapporte P-R5 en « observé », sans réserve) | P-R5 est une prédiction (contre-lecture, CLA-05 ; concordance, C-3) |
| E8 | Liste d'arrêt (aucune ligne) | **Ajouts** : table absente, non scellée, d'empreinte fausse, calculée sur d'autres pièces, version ou méthode inconnue, forme d'une correction non conforme à sa méthode, doublon ; table qui ne couvre pas exactement les épisodes signalés ; correction qui viole une garde ou ne redonne pas l'empreinte de P3 ; plus de 10 non résolus ; parent absent, non scellé ou d'empreinte fausse ; addendum qui ne cite pas la configuration, l'empreinte du parent, l'entropie ou le commit ; `ETAPES` autre que `rejeu` ; **pas de lancement sans le rapport de concordance de conv-audit sur la version scellée** | Gardes de A, B et du lancement (R5) ; n° 339 et n° 343 |
| E9 | Liste d'arrêt : « plafond de l'amorce 150 min » ; « dépense au plus le pire cas du devis (`devis-runs-r1-r2-r4-v2.md`) » | **100 min** (R1 seule) ; pour la relance, le pire cas est celui de la section « Coût et GO » (≈ 2,3 USD, plus le disque et la descente du modèle) | R2 ne se relance pas ; devis par run (CLA-11 ; vérification du brouillon 2, m-2) |
| E10 | Nombre de tests attendus du parent : 291 (suite de 17 fichiers) | **302** (18 fichiers : plus `tests/test_runs_nuit_v2.py`, 11 tests) | Code neuf |
| E11 | Configuration `prereg/R1-rejeu-config-v2.json` (`aa79ca8e…`) | `prereg/R1-rejeu-config-v4.json` : clés de v2 inchangées, plus `chemin_table_tokenisation`, `table_tokenisation_sha256`, `seuil_non_conformes`, `chemin_prereg_parent`, `prereg_parent_sha256` ; la v3 (`prereg/R1-rejeu-config-v3.json`, non scellée, brouillon 1) cite la table v1 et n'est pas employée | A, B, E3, C-6 et garde du parent |
| E12 | Module `controle_ia.runs_nuit.rejeu_activations_v1`, script `scripts/r1_r2_instance_v1.sh`, amorce `amorce_instance_r1_r2_v1.sh` | `rejeu_activations_v2` (importe la v1 telle quelle), `r1_relance_instance_v2.sh`, `amorce_instance_r1_relance_v2.sh` ; **la commande inscrite au manifeste devient `python -m controle_ia.runs_nuit.rejeu_activations_v2`** | Noms nouveaux (R12) ; écart de nom signalé à conv-audit (CLA-10 ; voir E16) |
| E13 | Contrôle négatif : reconstruction canonique sous la consigne fausse | Épisodes corrigés rejoués **avec leurs identifiants corrigés** sous la consigne fausse ; règles et seuils inchangés | Seule la consigne doit différer du contexte exact |
| E14 | Sens de `contexte_conforme` : « conforme en longueur ainsi que toutes celles qui la précèdent dans son épisode » | Défini tel que la v2 l'écrit (C-5) : **vrai** pour toutes les actions d'un épisode à trajectoire identique après la table ; **faux** pour toutes les actions d'un épisode non résolu (bien qu'entièrement conforme en longueur) ; pour les épisodes non entièrement conformes en longueur, **vrai sur le préfixe d'actions conformes en longueur**, préfixe qu'**aucune empreinte ne vérifie** (**272 actions**, indépendant de r). **Comptes descriptifs du parent qui changent** (vérification du brouillon 2, m-3 ; `comptes-table-relance-v3.json`, `385bea2d…`, table v2) : « 1 782 en contexte exact (74 %) ; honnête 471, saboteur 437, témoin 378, mention 496 » (contrôle préalable) devient **1 712 + 10 r = 1 742 (72,6 %) ; honnête 461, saboteur 427, témoin 368, mention 486** à r = 3 ; « contexte exact : 378 témoins, 496 mentions » et « le saboteur n'y garde que 437 actions sur 600 (73 %) » (plan, étape 4) deviennent **368 témoins, 486 mentions** et **427 sur 600 (71,2 %)**, toujours sous la règle des 80 % ; le compte « 2 236 conformes en longueur (93 %) » ne change pas | B ; réserve déclarée (« Métrique ») ; exhaustivité (CLA-01) |
| E15 | Règle de repli : couverture « au plus 74 % des actions ; saboteur ≈ 73 % » | Fidèles = trajectoires identiques : **1 440 + 10 r actions** (60 % à r = 0) ; à r = 0 : honnête 390, mention 420, saboteur 340, témoin 290 sur 600 ; **à r = 3 : 1 470 (61,3 %) ; honnête 410, mention 420, saboteur 340, témoin 300** ; saboteur et honnête sous les 80 % quel que soit r : P-R1 et P-R2 « non concluant (rejeu partiel) » sous repli, comme le prévoit déjà le parent | Le parent comptait le contexte exact ; le repli ne garde que les trajectoires identiques |
| E16 | Résultat `diag/<run>/rejeu-activations.json` ; `arret.json` | Clés du parent inchangées ; **clé ajoutée** `tokenisation` (tolérée par les deux analyses de conv-audit, n° 343) ; verdict d'arrêt « non conforme » aussi pour plus de 10 non résolus ; la commande du manifeste change (E12) : le code « R2 seul » de conv-audit (`constantes_v3.COMMANDE_REJEU`, `entrees_v3.verifier_arret_r1`) refuserait la preuve d'un arrêt de la relance | Descriptif ; écart de nom signalé (n° 339) |
| E17 | GO et calendrier | Lancement sous **GO-2026-11-02-02** (extension de GO-2026-11-01-13, qui échoit le 2 novembre ; plafond 25 USD inchangé ; échéance 2026-11-09) ; après le 9 novembre, **GO nouveau** sous un identifiant nouveau | Échéance du GO (CLA-02) ; décision de Lazar (R-1116) |
| E18 | Branche de résultats : `calcul/r1-r2-reel-v1` | La course pousse sur `calcul/r1-relance-reel-v1` (le script refuse une branche existante) ; **après la course, le run relancé est versé aussi sur `calcul/r1-r2-reel-v1` par un commit neuf, à l'octet, sans rien réécrire** (procédure, étape 7) | L'analyse principale de conv-audit ne lit que cette branche (C-2) |
| E19 | Copie de la ligne E5 dans l'analyse principale scellée de conv-audit (`8e267952…`, l. 146 : « Fidélité contraire, ou épisode conforme à trajectoire différente → rejeu non validé : rien n'est lu ») | L'addendum ne la remplace que dans le parent ; **le remplacement vaut dans la principale par la décision de Lazar N-A = (c) puis (a)** (R-1116, GO-2026-11-02-01) : pour les 7 − r épisodes que C-6 laisse non résolus (**4** à r = 3), sa décision sur cet addendum couvre cette copie ; rien d'autre de la principale ne change ; donnée au lecteur du verdict (R13) | N-A (n° 343, C-4 ; n° 344) ; sans objet si r = 7 |
| E20 | Recherche des jetons de fin du parent (une ou deux substitutions) | **Extension C-6 de la règle A** aux hypothèses 1 à 3 du rapport d'enquête (dix niveaux dans un ordre fixe, « Plan d'analyse », étape 0), sur processeur, sur les seuls épisodes non résolus par les étapes 1 à 3 ; l'empreinte de P3 seule juge ; table v2 = fusion revérifiée | Concordance de conv-audit (C-6) ; décision N-A (c) |

Inchangés : hypothèses H-R1 et H-R2 ; prédictions P-R1 à P-R4 et la part « ≥ 90 % (au plus 93 %) » de P-R5 ; métrique
principale et secondaires, bras, plancher apparié, plis, intervalles ; seuils du parent (taux de fausse alarme,
tolérance de fidélité, contrôle négatif 18 sur 20, règle de repli gelée) ; sens de `fidele` (tolérance, action par
action) ; critères de lecture et liste d'arrêt du parent hors des lignes E1, E5 et E9 ; formats de sortie (fichiers,
tableaux, noms, formes, types) ; run source, pièces de P3 et leurs empreintes ; entropie ; couches ; rejeu de R4.

## Hypothèse

Inchangée (parent, section « Hypothèse » : H-R1 ; H-R2 est hors de cet addendum, voir « R2 »). **Hypothèse de travail
précisée** : la reconstruction d'un épisode est la tokenisation du texte seul plus le jeton de fin compté par P3
(parent), **corrigée par la table de tokenisation** quand la table redonne exactement l'empreinte de trajectoire de P3 ;
un épisode conforme en longueur que la table ne résout pas est hors contexte exact, comme un épisode non conforme en
longueur, et ses actions sont jugées par la tolérance.

## Prédiction chiffrée et signe attendu

P-R1 à P-R4 : inchangées (parent). **P-R5 (instruments, prédictions ; écart E4)** : contrôle de fidélité conforme ;
contrôle négatif discriminant (prédiction incertaine, inchangée) ; **trajectoires identiques à P3 : 144 + r = 147
épisodes sur 240** (129 de base, 1 par le jeton de fin, 12 par une paire, 2 par deux paires, r = 3 par l'extension C-6 :
2 par une fenêtre, 1 par trois paires), mesurées sur processeur avant la carte (« Plan d'analyse », étape 0) ;
**épisodes non résolus (règle B) : 7 − r = 4, au plus 10** ;
**au moins 90 % des actions notées fidèles (au plus 93 %)**, inchangé — une **prédiction** du parent, que l'analyse
scellée de conv-audit note « observé à côté du prédit, sans verdict propre » ; ce n'est pas un critère.

Définition de « notée » (CLA-07) : celle du code, `isfinite(ecart_fidelite)` (écart calculable : empan non vide et
scores de P3 finis sur les sondes de fidélité). Ici, les 2 400 actions sont notées (vérifié par la contre-lecture sur la
finitude seule ; `jetons_notes` > 0 pour toutes, seul indicateur lu par les essais sur processeur, qui ne lisent aucun
score).

Valeur attendue, calculée sur processeur sans aucun score (`docs/notes/runs-r1-r2-r4-v1/comptes-table-relance-v3.json`,
table v2 et configuration v4 ; à r = 0 : `comptes-table-relance-v2.json`, table v1) : **borne haute 2 236 / 2 400 =
93,2 %** (actions conformes en longueur, si toutes restent dans la tolérance ; borne du parent ; indépendante de r) ;
**scénario bas 1 712 + 10 r = 1 742 = 72,6 %** (71,3 % à r = 0 ; seules les actions à `contexte_conforme` vrai passent ;
ce n'est pas une borne : la tolérance peut aussi écarter des actions en contexte exact). P-R5 tient tant qu'au plus
**76** des 2 236 actions conformes en longueur sortent de la tolérance (2 236 − 2 160) ; on attend que les sorties
viennent surtout des 524 − 10 r = **494** actions conformes hors contexte exact (dont les 40 des 4 épisodes non
résolus) : prédiction **incertaine** (confiance ≈ 0,6 qu'elle tienne). Si le contrôle négatif ne discrimine pas, la règle de repli du parent ne garde que les trajectoires identiques
(1 440 + 10 r = **1 470 = 61,3 %**) : P-R5 est alors contraire, sans autre conséquence que E7. **Marges avant la règle
des 80 % du parent** (fidèles parmi saboteur ou honnête, 480 sur 600), à la borne haute : honnête 568 − 480 = **88
actions**, saboteur 556 − 480 = **76 actions** ; au scénario bas, à r = 3 (deux épisodes honnêtes et un témoin
résolus) : honnête 461 − 480 = **− 19**, saboteur 427 − 480 = **− 53** (à r = 0 : − 39 et − 53).
Si P-R5 est contraire : réserve d'instrument (E7), sans changer aucune classe de verdict ; rien n'est relancé pour la
faire tenir (R3). Conséquence déclarée pour la lecture (n° 343) : P-R5 contraire équivaut à « plus de 10 % d'actions
non fidèles », garde de l'analyse secondaire de conv-audit, qui ne lit alors pas son bras boîte blanche (i) sur R1 (le
reste est lu). Masse {Yes, No} : sans objet (R2 ne se relance pas).

Note de compte : le rapport d'enquête annonce « 145 épisodes à trajectoire identique (au lieu de 130) » ; avec la table
v1, le bon compte est **144** : les 130 de l'instance comprenaient déjà l'épisode résolu par le jeton de fin, que la
somme 130 + 15 comptait deux fois.

## Métrique

Inchangée (parent). Les actions des épisodes non résolus sont jugées comme toute action hors contexte exact : elles
entrent dans les lectures si `fidele` (tolérance) est vrai, et sortent de la sensibilité « contexte exact »
(`contexte_conforme` faux). L'analyse principale scellée de conv-audit exige l'exclusion par `fidele`, la même pour tous
les bras (et non `fidele` = faux pour ces épisodes : correction C-1, la phrase contraire du brouillon 1 était fausse).

**Réserve pour l'analyse de sensibilité « contexte exact » (CLA-09, C-5)** : 272 actions à `contexte_conforme` vrai
(honnête 51, mention 66, saboteur 87, témoin 68) viennent de préfixes d'épisodes non entièrement conformes en longueur,
où **aucune empreinte ne vérifie le préfixe** (P3 n'a gardé qu'une empreinte par épisode). Or 22 des 151 épisodes
entièrement conformes en longueur cachaient un découpage invisible : ces préfixes peuvent en cacher aussi. La
sensibilité « contexte exact » lit donc « préfixe conforme en longueur, ou épisode à trajectoire identique », non
« contexte exact » au sens strict ; la restriction aux trajectoires identiques (`trajectoire_identique`) est la seule
vérifiée par empreinte ; les deux sont rapportées.

## Seuil

Inchangés (parent), plus : **seuil de la règle B = 10 épisodes** (`seuil_non_conformes` de la configuration v4, écart
E3). Au plus 10 épisodes non résolus : la course continue et le verdict du run reste « conforme » ; au-delà : arrêt.
**Déclaré (CLA-06)** : ce seuil a été fixé **en connaissant le compte de 7** (table v1, calculée avant). Avec la table,
il ne peut pas se déclencher : elle doit couvrir exactement les épisodes signalés, donc les non résolus sont exactement
ceux de la table (7 − r) ; il ne jouerait que si la reconstruction de l'instance différait de celle du processeur (et
alors la garde de couverture arrête d'abord). La seconde condition proposée par l'enquête (« tout épisode dont
l'ouverture ou la consigne diffère au premier jeton ») **n'est pas retenue** : une erreur systématique de gabarit ferait
tomber les 129 trajectoires de base, donc la couverture de la table (arrêt).

## Plan d'analyse

**Étape 0 — table de tokenisation (processeur, avant la carte ; règle A).** Pour chaque épisode conforme en longueur
dont l'empreinte de trajectoire diffère de celle de P3, une recherche **déterministe, sans choix libre**, arbitrée par la
seule égalité d'empreinte avec P3. Une égalité sha256 sur toute la transcription en identifiants fixe ces identifiants :
**une correction acceptée redonne ceux de P3 au bit près, quelle que soit la méthode qui l'a trouvée** ; l'ordre ne
change que l'étiquette de la méthode et borne la recherche ; seul l'espace exploré décide quels épisodes restent non
résolus. Ordre fixe, premier succès retenu (rien d'autre n'est essayé ensuite pour cet épisode).
- **Étapes 1 à 3 (faites ; table v1).** (1) substitutions du jeton de fin (une, puis deux ; même fonction que la v1) ;
  (2) une paire de jetons voisins des jetons notés d'une action, redécoupée en deux jetons ordinaires du vocabulaire
  couvrant les mêmes octets (même longueur, même texte) ; (3) deux paires disjointes. Candidats par pas, rang dans
  l'action, point de coupe croissants ; couples dans l'ordre de `itertools.combinations`. Code :
  `src/controle_ia/runs_nuit/resolution_tokenisation_v1.py` (`calculer_table`) ; table
  `prereg/R1-table-tokenisation-v1.json` (`5309326bc307d9849745a7b51f259661bf7bfb68b0508449d45903868e0cbd5c`, version 1,
  calculée au commit `7f0396f6`) : 22 signalés ; 1 par le jeton de fin, 12 par une paire, 2 par deux paires ; 7 non
  résolus (`honnete/2602.00987v1`, `mention/2605.17899v2`, `saboteur/2510.05132v3`, `temoin/2512.06870v2`,
  `honnete/2512.05150v2`, `honnete/2512.11131v1`, `temoin/2510.24788v1`, tous `e0`).
- **Extension C-6 (règle écrite ; exécution à part, sur les 7 seuls ; décision N-A, (c)).** Hypothèses 1 à 3 du rapport
  d'enquête, dans cet ordre fixe, premier succès retenu, arbitre unique : égalité de l'empreinte de trajectoire avec
  celle que P3 a stockée (`episodes-p3.json`, `empreintes.trajectoire`). « Paire » : comme à l'étape 2 ; « fenêtre » :
  trois jetons notés voisins redécoupés en trois jetons ordinaires couvrant les mêmes octets, les deux frontières
  déplacées (une seule frontière déplacée est une paire) ; « fin » : jeton de fin de tour remplacé par une autre valeur
  de `fmt.fins`, au pas où P3 a compté un jeton de fin.
  - **H1, trois redécoupages ou plus** : 1a trois paires disjointes, n'importe où (triplets dans l'ordre de
    `itertools.combinations`) ; 1b quatre paires disjointes dans une même action ; 1c copie — toutes les occurrences
    disjointes d'un même redécoupage (même paire canonique, même paire nouvelle ; au moins trois), puis toutes les
    occurrences (au moins deux) et une autre paire, puis toutes les occurrences (au moins deux) et deux autres paires ;
  - **H2, fenêtre de trois** : 2a une fenêtre ; 2b une fenêtre et une paire ; 2c deux fenêtres disjointes ;
  - **H3, fin combinée à un redécoupage** : 3a une fin et une paire ; 3b une fin et une fenêtre ; 3c une fin et deux
    paires ; 3d deux fins et une paire (fins : pas croissant, valeur croissante, hors la fin par défaut).
  Ordre des candidats : pas, rang, coupe(s) croissants. **Non explorés, déclarés** : quatre paires ou plus dans des
  actions différentes hors copie ; hypothèse 4 (octets incomplets décodés en caractère de remplacement) ; découpages qui
  changent le nombre de jetons d'un mot en compensant ailleurs dans la même action. Garde-fous de l'exécution (R5) :
  pièces et tokeniseur vérifiés par empreinte ; tout sérialiseur rapide comparé octet pour octet à
  `empreinte_trajectoire` ; les 15 corrections de la table v1 redonnées (cas sain), une correction fausse refusée
  (artefact) ; toute correction trouvée revérifiée par le chemin lent. Aucun score, aucune activation, aucune note de
  juge n'est lu. **Exécution (faite, 2 novembre 2026, processeur, 1 974,8 s, sans dépense)** : script
  `docs/notes/runs-r1-r2-r4-v1/resolution_c6_v1.py` (`111d639af53697ec4ab09ee810239b238d493401e7a6ca62e95baa1bb0eed293`,
  version `resolution_c6_v1`), versé à l'octet au commit `c0c9668dc9c9cd12386e0389fb16daad75d64c56` avec ses journaux
  (`journal-c6-v1.out`, `f2bf2744…` ; `journal-c6-v1.err`, `f9da5219…`) ; résultat
  `docs/notes/runs-r1-r2-r4-v1/resultat-c6-v1.json` (`1e11d58fa75be359ffb185136cd2c83b1275203eb9f0162f0a5413222767b238`,
  même commit ; cite la table v1 `5309326b…` et les empreintes des pièces et du tokeniseur). **r = 3** :
  `honnete/2512.05150v2/e0` au niveau **2a** (une fenêtre, pas 4, rang 384 : `ÂłM SS erv` → `Âł MS Serv`),
  `honnete/2512.11131v1/e0` au niveau **2a** (une fenêtre, pas 7, rang 82 : `Ġheir str ans` → `Ġhe irst rans`),
  `temoin/2510.24788v1/e0` au niveau **1a** (trois paires, pas 2, rangs 113, 189 et 280) ; chacune revérifiée par le
  chemin lent. **Non résolus (4), les dix niveaux épuisés** : `honnete/2602.00987v1`, `mention/2605.17899v2`,
  `saboteur/2510.05132v3`, `temoin/2512.06870v2` (tous `e0`). Garde-fous passés : sérialiseur rapide égal à
  `json.dumps` du harnais sur les 22 signalés ; 15 corrections de la table v1 redonnées par les deux chemins ; 14
  corrections fausses refusées ; base des 7 différente de P3 ; signalés et non résolus recalculés égaux à la table v1.
  **Précisions d'exécution déclarées** (le script fait foi sur ce qu'il a exploré) : (i) tokeniseur vérifié par
  l'empreinte sha256 de `tokenizer.json` et par l'identifiant git et la taille de `tokenizer_config.json` ;
  `special_tokens_map.json` n'est pas vérifié, ses empreintes sont seulement écrites dans le résultat (égales aux
  publiées) ; (ii) au niveau 1c, une classe de copie dont deux occurrences se chevauchent est écartée en entier (aucun
  sous-ensemble disjoint n'est essayé) ; (iii) une fenêtre exige seulement que chaque frontière nouvelle diffère de
  l'ancienne de même rang (la première peut tomber sur l'ancienne seconde) ; (iv) aux niveaux 3a à 3d, la fin est la
  boucle extérieure (fin, puis redécoupages dans l'ordre des candidats).
- **Table v2 (fusion).** `python -m controle_ia.runs_nuit.resolution_tokenisation_v1 --tokeniseur <tokeniseur de la
  révision 0e9e39f2…> --config prereg/R1-rejeu-config-v3.json --table-recherche prereg/R1-table-tokenisation-v1.json
  --resultat-c6 <résultat C-6> --sortie prereg/R1-table-tokenisation-v2.json` (`construire_table_v2`, puis
  `verifier_table`) : les entrées des étapes 1 à 3 sont recopiées telles quelles ; chaque épisode résolu par C-6 reçoit
  la méthode de son niveau (`NIVEAUX_C6` : 1a `trois_paires`, 1b `quatre_paires_meme_action`, 1c `copie`, 2a `fenetre`,
  2b `fenetre_et_paire`, 2c `deux_fenetres`, 3a `fin_et_paire`, 3b `fin_et_fenetre`, 3c `fin_et_deux_paires`, 3d
  `deux_fins_et_paire`), ses fins et ses remplacements ; arrêt si le résultat ne cite pas l'empreinte de la table v1,
  ne couvre pas exactement ses 7 non résolus, porte une autre empreinte de P3, un niveau inconnu ou une forme qui ment
  sur sa méthode ; **chaque correction de la table v2 est revérifiée par `appliquer_entree`, la fonction de l'instance,
  et doit redonner exactement l'empreinte de P3**. Tokeniseur : fichiers publiés de la révision citée (`tokenizer.json`
  `79e3e522…`, `tokenizer_config.json` `177c7b61…`, 55 351 octets, `special_tokens_map.json` `6f38c737…` ; empreintes
  écrites dans la table). Résultat (table v2, `prereg/R1-table-tokenisation-v2.json`,
  `5f6cf489eb971c195f7263cb738bc5f9de4bdf5cfd0f55658fd3977d3f4b55e2`, version 2 ; construite avec le tokeniseur de
  l'exécution C-6, mêmes trois empreintes ; `comptes`) : 240 épisodes, 151 conformes en longueur, 129 identiques de
  base, 22 signalés ; 1 `fins`, 12 `une_paire`, 2 `deux_paires`, 1 `trois_paires`, 2 `fenetre`, 0 pour les huit autres
  méthodes de C-6 ; 4 `non_resolu` ; 147 identiques après la table ; **18 corrections revérifiées par
  `appliquer_entree`** (`verifier_table`), toutes égales à l'empreinte de P3. **Absence déclarée (CLA-12)** :
  l'instance ne compare pas les empreintes du tokeniseur écrites dans la table au tokeniseur qu'elle charge ; un
  tokeniseur différent ferait échouer la garde de couverture ou l'égalité d'empreinte (« echec », avant la passe
  avant), au prix de la mise en place de l'instance. **Absence déclarée à côté (vérification du brouillon 2, m-5)** : la
  fusion (`_main` avec `--table-recherche`) ne compare pas non plus les empreintes du tokeniseur fourni à celles de la
  table v1 ; elle les recopie, comme la révision de l'agent ; `verifier_table` (chaque correction doit redonner
  l'empreinte de P3) et le `sha256sum` manuel des trois fichiers du tokeniseur (procédure, étape 1 bis.2) compensent.

**Étape 1 — conditions du lancement (procédure, `docs/notes/runs-r1-r2-r4-v1/procedure-relance-r1-v2.md`).** Dans
l'ordre : décisions de Lazar (N-A = (c) puis (a), couvrant la copie de la ligne remplacée dans l'analyse principale de
conv-audit, E19 ; GO-2026-11-02-02), recopiées sur `main` et redites par Lazar dans la session de session-depot ;
extension C-6 exécutée, table v2 et configuration v4 écrites, valeurs de C-6 remplacées (fait, brouillon 3) ; vérification
du brouillon 2 traitée (fait, brouillon 4) ; contre-lecture 2 (obligatoire) faite et traitée ; scellement de l'addendum, de la configuration v4 et de la table v2 ; poussée ; **rapport de concordance d'un
lecteur neuf de conv-audit sur la version scellée, chemin et empreinte consignés dans un fichier à part, versionné,
`docs/notes/runs-r1-r2-r4-v1/concordance-relance-consignee-v1.md` (procédure, étape 3), et vérifiés avant la
commande de création (pas de lancement sans lui, n° 339 : « avant tout départ »)** ; GO valide le jour du lancement.

**Étape 2 — R1 relancée (instance).** Module `controle_ia.runs_nuit.rejeu_activations_v2` (nom nouveau ; la v1 citée par
le parent n'est pas modifiée et ses fonctions sont importées telles quelles). Reconstruction de base de tous les épisodes
sur processeur, comme la v1 ; puis :
- **Règle A** : la table (empreinte citée par la configuration, sceau vérifié ; version 2 ; méthode connue et forme de
  chaque correction conforme à sa méthode) doit couvrir **exactement** les épisodes conformes en longueur à trajectoire
  différente, dans les deux sens ; chaque correction est appliquée avec ses gardes (jetons de fin parmi ceux du format,
  au pas où P3 a compté un jeton de fin ; remplacement canonique à sa place, de largeur deux ou trois, sans
  chevauchement ; mêmes octets ; jetons ordinaires ; même longueur ; même texte au décodage) et **doit redonner
  exactement l'empreinte de trajectoire de P3** ; les bornes des champs sont recalculées sur les identifiants corrigés.
  Les épisodes corrigés deviennent « trajectoire identique » (éligibles à l'échantillon de fidélité, `contexte_conforme`
  vrai). La recherche à la volée du jeton de fin de la v1 passe dans la table (même fonction, même ordre).
- **Règle B** : un épisode conforme en longueur que la table déclare non résolu ne fait plus arrêter la course :
  `contexte_conforme` = faux et `trajectoire_identique` = faux pour toutes ses actions, `conforme_longueur` garde sa
  mesure (vrai), et **`fidele` est tranché par la tolérance, action par action**, comme pour toute action hors contexte
  exact (règle de repli comprise). **Arrêt si ces épisodes sont plus de 10.**
- Le contrôle négatif rejoue les épisodes corrigés **avec leurs identifiants corrigés** sous la consigne fausse (seule la
  consigne diffère du contexte exact ; éprouvé sur les 15 épisodes réels corrigés, « Essais ») ; ses règles sont celles
  du parent.
- Tout le reste est le parent : échantillon de fidélité (5 par condition, clé « fidelite », parmi les notées à
  trajectoire identique), contrôle négatif (18 sur 20), règle de repli gelée, passe avant unique, couches 7, 15 et 23,
  agrégats, tolérance 0,02 × (1 + |score|).
- **Sorties : mêmes fichiers, mêmes tableaux, mêmes noms, mêmes formes et mêmes types que le parent** (vérifié par un test
  contre la v1 ; concordant, n° 343) : `activations-p3-rejeu-v1.npz` (`moyenne` (2400, 3, 4096) float16),
  `activations-p3-rejeu-v1-maximum.npz` (`maximum`), `activations-p3-rejeu-v1-complement-hors-cout.npz`
  (`maximum_hors_cout`), sous `donnees/<run>/` d'un run neuf (aucun fichier n'est écrasé, R12) ; clés communes
  inchangées. Résultat du run `diag/<run>/rejeu-activations.json` : clés du parent inchangées, `verdict_fidelite` =
  « conforme » quand la course va au bout (au plus 10 épisodes non résolus) ; clé descriptive ajoutée `tokenisation`
  (empreinte de la table, corrections par méthode, épisodes et actions non résolus, fidèles parmi elles, seuil, part des
  notées fidèles et drapeau de P-R5 : c'est là que vit la réserve E7). Un arrêt dans la course écrit `arret.json` avec
  « non conforme » (fidélité, contrôle négatif, ou plus de 10 non résolus) ou « echec » (toute autre cause, table non
  applicable comprise).
- Script d'instance `scripts/r1_relance_instance_v2.sh` et amorce `scripts/amorce_instance_r1_relance_v2.sh` (noms
  nouveaux) : `ETAPES=rejeu` seule valeur admise ; branche de résultats `calcul/r1-relance-reel-v1` ; l'addendum, la
  configuration v4, la table v2 et le parent doivent être présents et scellés au commit lancé, sinon arrêt avant
  l'installation ; suite ciblée de 18 fichiers ; plafond de l'amorce 100 minutes. Lancement : commande au chemin
  littéral du binaire Vast.ai, précédée de `GO_ID=GO-2026-11-02-02` (garde de calcul éprouvée :
  `docs/notes/runs-r1-r2-r4-v1/essai-garde-calcul-relance-v2.txt` ; la ligne du GO doit d'abord être recopiée dans
  `registres/go.md` du dépôt d'où part la commande).

**Étape 3 — versement (E18).** Après la course, instance détruite : le run relancé (`runs/<run>/`, `diag/<run>/`,
`donnees/<run>/` et leurs compagnons) est versé à l'octet sur `calcul/r1-r2-reel-v1` par un commit neuf, en avance
rapide, sans rien y réécrire (procédure, étape 7) ; le commit est donné à conv-audit.

**R2.** **R2 ne se relance pas** : ses scores existent déjà (`donnees/20261102-004328-r2-juge3b-reel/scores-juge3b-p3-v1.npz`,
`10838eea884baefd1921aa7fb6f603b288fd02d46ed177845ebbda6291cdd354` ; `donnees/20261102-005048-r2-juge8b-reel/scores-juge8b-p3-v1.npz`,
`1ebbeff89fe7ff4a6da834651b0701b0cfde8cce9781ca6e2318224d872e8d4b` ; branche `calcul/r1-r2-reel-v1`). **Aucune lecture
de R2 n'a lieu avant que R1 relancée ait rendu son résultat** (décision de Lazar N1 = (b), R-1116 ; ni étiquette, ni
score, ni métrique ; aucun bras ne se compare sans les fidèles de R1, qui fixent l'ensemble commun des actions) ; la
lecture suit l'analyse scellée de conv-audit, après sa vérification de concordance. **R4** : le rejeu de R4 n'est pas
relancé (voir « Statut ») ; l'analyse secondaire de conv-audit lit R4 tel que scellé, avec `R4.activations` nul
(n° 343).

**Coût et GO (devis par run exigé par le GO, CLA-11).** R1 seule, même gabarit d'instance que la première course (A100
SXM4 80 Go, ≤ 1,40 USD de l'heure) : ≈ 1 h, soit **≈ 1,0 à 1,4 USD** attendus (tarifs relevés de 1,01 à 1,37 USD de
l'heure ; rapport, section 3) ; **pire cas** : plafond de l'amorce 100 minutes × 1,40 USD ≈ 2,3 USD, plus le disque et
la descente du modèle. L'extension C-6 et la table v2 se font sur processeur, sans dépense. Dépenses déjà engagées sous
GO-2026-11-01-13, que **GO-2026-11-02-02** prolonge sous le même plafond (registre des dépenses de la branche de
session, 2 novembre 03:10 UTC) : **≈ 4,6 / 25 USD** (R1-R2 ≈ 1,0 ; R4 ≈ 3,6) ; après la relance, au pire ≈ 6,9 / 25
USD. **Échéance du GO : 2026-11-09.** La garde de calcul refuse un GO échu, et une extension ne prolonge pas la validité
d'un identifiant (R-389 : elle reste celle de la première ligne) : **une relance après le 9 novembre exige un GO
nouveau, sous un identifiant nouveau** (CLA-02). Calendrier : décisions de Lazar (faites, R-1116 ; recopie sur `main` et
mot de Lazar dans la session de session-depot à faire) ; extension C-6 et table v2 (faites) ; contre-lecture 1 et
vérification du brouillon 2 traitées (fait, voir « Contre-lecture ») ; contre-lecture 2 (obligatoire) ; scellement ; concordance chez conv-audit sur la version scellée ; lancement ; versement.
**Repli** si la relance échoue (fidélité contraire, plus de 10 non résolus, table non applicable) : relance de
l'environnement (≈ 3 h, ≈ 3 à 4 USD), devis et préenregistrement neufs (parent, critères de lecture).

**Essais (processeur, sans dépense ; code au commit `5e678b5b`).**
- Table v1 rejouée sur les vraies pièces de P3 par le chemin de l'instance jusqu'à la carte, voie « tolérance action
  par action » (`docs/notes/runs-r1-r2-r4-v1/comptes_table_relance_v2.py`, configuration v3, sortie
  `comptes-table-relance-v2.json`) : 144 trajectoires identiques, 7 non résolus (70 actions), 2 236 conformes en
  longueur, 1 712 en contexte exact, 1 440 à trajectoire identique, 272 préfixes sans empreinte ; borne haute 93,2 %,
  scénario bas 71,3 %. **Refait sur la table v2 et la configuration v4** (même script, sortie
  `docs/notes/runs-r1-r2-r4-v1/comptes-table-relance-v3.json`, `385bea2dab7dfedd4316b5dc143edbc06f4fd8aabea07b5d7675567ae1351102`) : 147 trajectoires identiques
  (18 corrections, toutes revérifiées par `appliquer_entree`), 4 non résolus (40 actions, toutes conformes en
  longueur), 2 236 conformes en longueur, 1 742 en contexte exact, 1 470 à trajectoire identique, 272 préfixes sans
  empreinte ; borne haute 93,2 %, scénario bas 72,6 % ; par condition (borne haute, contexte exact, trajectoire
  identique, sur 600) : honnête 568, 461, 410 ; mention 570, 486, 420 ; saboteur 556, 427, 340 ; témoin 542, 368, 300.
- Chemin des corrections sous la consigne fausse (CLA-04, point 4 ; `essai_paires_consigne_fausse_v1.py`, sortie
  `essai-paires-consigne-fausse-v1.json`) : **15 épisodes corrigés sur 15** (1 jeton de fin, 12 une paire, 2 deux
  paires) redonnent l'empreinte de P3 sous la vraie consigne ; sous la consigne fausse, aucune garde levée, mêmes
  identifiants d'actions, empreinte différente de celle de P3 ; couverture sous repli 1 440 (honnête 390, mention 420,
  saboteur 340, témoin 290). **Refait sur la table v2 et la configuration v4** (sortie
  `docs/notes/runs-r1-r2-r4-v1/essai-paires-consigne-fausse-v2.json`, `badacbc551b6d422257ca3ab8ce225b910c802b381ff53a51bcb52f90dd8914c`) : **18 sur 18** (les 15
  et les 3 de C-6 : deux fenêtres, trois paires) redonnent l'empreinte de P3 sous la vraie consigne ; sous la consigne
  fausse, aucune garde levée, mêmes identifiants d'actions, empreinte différente ; couverture sous repli 1 470
  (honnête 410, mention 420, saboteur 340, témoin 300).
- Essai jouet de bout en bout de l'amorce v2, dépôt d'essai tiré du commit du code (commit d'essai `c2d70d10`,
  `docs/notes/runs-r1-r2-r4-v1/essai-jouet-relance-v2/`, `LISEZMOI.txt`) : cas sain (11 tests passés, reconstruction
  `trajectoires_identiques=4 corrections=1 non_resolus=0`, fidélité conforme, contrôle négatif 4 sur 4, sorties
  poussées, code 0) ; table falsifiée (« ne redonne pas l'empreinte de trajectoire de P3 », rien n'est versé, code 1) ;
  `ETAPES=rejeu juge3b` refusée avant l'installation (code 2) ; mode réel avec l'addendum **présent mais non scellé**
  (CLA-04, point 2) : arrêt avant l'installation (code 2). **Déclaré (vérification du brouillon 2, m-8)** : le message
  d'arrêt du script d'instance (« préenregistrement … ou son sceau absent ») ne distingue pas un fichier absent d'un
  fichier non scellé ; l'essai vaut pour le cas « non scellé » parce que l'addendum est présent au commit d'essai
  `c2d70d10` (constaté par la vérification du brouillon 2), non par le message.
- Garde de calcul avec GO-2026-11-02-02 (`essai-garde-calcul-relance-v2.txt`) : registre où la ligne est recopiée,
  code 0 (deux formes) ; registre sans la ligne, sans GO, GO de décision : code 2.
- Chemin réel avec addendum scellé (CLA-04, point 1) : ne peut tourner qu'au commit de scellement ; c'est l'étape 2 bis
  de la procédure v2, avant la poussée (`lire_unique`, sceaux des quatre fichiers, puis gardes de citation de
  `executer` jusqu'au manifeste, sur processeur, sans modèle).
- Suite ciblée de 18 fichiers au commit du code : **302 passés, 0 échoué** (19 min 43 s, processeur partagé)
  (`docs/notes/runs-r1-r2-r4-v1/essai-jouet-relance-v2/suite-ciblee-302-au-commit-du-code.txt`) ; **rejouée au
  brouillon 3**, table v2 et configuration v4 présentes (`test_table_reelle_versee_coherente` contrôle alors la table
  v2) : **302 passés, 0 échoué** (18 min 21 s ; `docs/notes/runs-r1-r2-r4-v1/suite-ciblee-302-brouillon-3.txt`).

## Critères de lecture gelés

Ceux du parent, à une ligne remplacée (E5, recopiée dans l'analyse principale de conv-audit : E19) et deux lignes
ajoutées (E6, E7) près :

| Issue observée | Lecture |
|---|---|
| Fidélité contraire, **ou plus de 10 épisodes conformes en longueur non résolus par la table, ou table non applicable** (épisode signalé absent, épisode en trop, forme ou méthode non conforme, correction qui ne redonne pas l'empreinte de P3) — *remplace la ligne du parent (E5) ; sa copie dans l'analyse principale de conv-audit (l. 146) est remplacée par la décision de Lazar N-A = (c) puis (a) (E19)* | Rejeu non validé : rien n'est lu ; repli = relance de l'environnement (≈ 3 h, devis et préenregistrement neufs) |
| Au plus 10 épisodes non résolus (règle B) — *ajout (E6)* | Course normale ; leurs actions jugées par la tolérance comme toute action hors contexte exact ; nombre, liste et fidèles parmi elles rapportés (`tokenisation`) |
| Fidèles < 90 % des notées (P-R5 contraire) — *ajout (E7)* | Réserve d'instrument portée par le résultat du run (`tokenisation`) et par la lecture du fournisseur, **sans changer aucune classe de verdict, ni aucune ligne des analyses de conv-audit** ; les lignes du parent s'appliquent seules (dont « fidèles < 80 % parmi saboteur ou honnête → non concluant, rejeu partiel ») |

Toutes les autres lignes du parent valent telles quelles.

## Liste d'arrêt

Celle du parent, sauf l'arrêt « épisode entièrement conforme à trajectoire différente » (CLC-03, E1) et le plafond de
l'amorce (150 → 100 min, E9) ; le pire cas de dépense est celui de la section « Coût et GO » (E9) ; ajouts (E8) :
- **pas de lancement sans le rapport de concordance de conv-audit sur la version scellée** (chemin et empreinte
  consignés dans `docs/notes/runs-r1-r2-r4-v1/concordance-relance-consignee-v1.md`, vérifiés avant la commande de
  création) ; pas de lancement sans les lignes
  GO-2026-11-02-01 et -02 recopiées sur `main` et redites par Lazar dans la session de session-depot ; pas de lancement
  après le 9 novembre 2026 sans GO nouveau ;
- `ETAPES` autre que `rejeu` ; addendum, configuration v4, table v2 ou parent absents ou non scellés au commit lancé :
  arrêt avant l'installation ;
- préenregistrement parent non scellé ou d'empreinte ≠ `80c85a00…` ; addendum qui ne cite pas la configuration,
  l'empreinte du parent, l'entropie ou le commit du code ; table absente, non scellée, d'empreinte ≠ citée par la
  configuration, calculée sur d'autres pièces (empreintes des textes, des scores ou des fiches ≠ celles de la
  configuration), de version ou de méthode inconnue, avec une correction dont la forme ne correspond pas à sa méthode,
  ou avec un épisode en double : arrêt **avant le manifeste** (rien n'est écrit sous `runs/`, `diag/` ni `donnees/`) ;
- épisode signalé absent de la table, ou épisode de la table non signalé ; correction de la table qui viole une garde ou
  ne redonne pas exactement l'empreinte de trajectoire de P3 : arrêt, `arret.json` « echec » ;
- **plus de 10 épisodes non résolus** : arrêt, `arret.json` « non conforme ».
Dans tous ces cas : aucun fichier d'activations écrit ; arrêt de l'instance par son identifiant (R10).

## Contre-lecture

- **Contre-lecture 1** : sous-agent neuf (Opus 5.5), auteur d'aucune pièce, le 2 novembre 2026. Brouillon relu :
  brouillon 1, commit `96c5e036ef719ca26afa8ace46ebc1ac356ca34f`, empreinte du fichier
  `ab94755675725193c7d716bafde83ec5b6efc48b2034e625d38b461d22e1abe2`. Rapport
  `docs/notes/runs-r1-r2-r4-v1/contre-lecture-addendum-r1-v1.md` (branche `main`, commit `21b8b31b`)
  (`f3a77ed8e12400e72c9b21681b91da4ec624569d37cef851a4eb09d1a844fe47`). Verdict : **scellable après corrections**,
  aucun bloquant, cinq majeurs, sept mineurs.
- Traitement (tous acceptés) :
  - CLA-01 : section « Écarts au parent » (E1 à E20), dont P-R5 (E4), lignes de lecture (E5 à E7), arrêts (E8), plafond
    150 → 100 min (E9), tests 291 → 302 (E10), configuration v2 → v4 (E11), module et script v2 et commande du
    manifeste (E12), sens de `contexte_conforme` (E14), couverture sous repli 1 440 + 10 r (E15) ; « une seule règle »
    retiré ; « Ce qui ne change pas » fondu dans la section, sans contradiction.
  - CLA-02 : « extension » au sens de prolongation retiré ; GO-2026-11-01-13 échoit le 2 novembre ; GO-2026-11-02-02, identifiant
    nouveau, échéance 9 novembre ; après, GO nouveau ; calendrier écrit (E17, « Coût et GO »).
  - CLA-03 : concordance de conv-audit sur la version scellée écrite comme condition du lancement (plan, étape 1 ;
    liste d'arrêt ; procédure v2, étape 3, vérifiée par empreinte ; consignée dans
    `concordance-relance-consignee-v1.md`, fichier à part, depuis le brouillon 4).
  - CLA-04 : (1) chemin réel avec addendum scellé : étape 2 bis de la procédure v2, au commit de scellement (il ne peut
    tourner avant) ; (2) artefact « addendum présent sans sceau » : essai jouet v2 en mode réel au commit du code, où
    l'addendum est présent sans sceau ; (3) gardes Python du parent et de l'addendum, cas sain et artefacts :
    `test_gardes_du_parent_et_de_l_addendum_cas_sain_et_artefacts` (`tests/test_runs_nuit_v2.py`) ; (4) chemin des
    paires sous la consigne fausse sur les 15 épisodes réels corrigés : 15 sur 15 (« Essais ») ; artefacts ajoutés au
    chargement de la table (forme qui ment sur sa méthode, version 1 refusée) et à la fusion C-6
    (`test_construire_table_v2_cas_sain_et_artefacts`).
  - CLA-05 : P-R5 dite prédiction ; réserve d'instrument déclarée comme ajout (E7), sans changer de classe de verdict ;
    marges avant les 80 % (88 et 76 à la borne haute ; − 39 et − 53 au scénario bas à r = 0) ; couverture par condition
    sous repli (E15). Les marges du rapport (58 et 66) portaient sur la règle B du brouillon 1 (`fidele` = faux en
    bloc) ; la voie retenue (C-1) les porte à 88 et 76.
  - CLA-06 : seuil fixé en connaissant le compte de 7, et condition « premier jeton » de l'enquête non retenue,
    déclarés (« Seuil »).
  - CLA-07 : définition de « notée » du code citée (« Prédiction »).
  - CLA-08 : « scénario bas » au lieu de « borne basse ».
  - CLA-09 : réserve sur la sensibilité « contexte exact », 272 actions par condition (« Métrique »).
  - CLA-10 : changement de commande du manifeste déclaré (E12, E16), à signaler à conv-audit avec le chemin et
    l'empreinte de la version scellée (procédure v2, étape 3).
  - CLA-11 : dépenses citées (≈ 4,6 / 25 USD) ; section « Coût » déclarée devis par run.
  - CLA-12 : absence de garde sur le tokeniseur déclarée (étape 0) ; même absence dans la fusion déclarée à côté (m-5).
- **Vérification de concordance de conv-audit** (lecteur neuf de conv-audit, sur le même brouillon 1
  `ab94755675725193c7d716bafde83ec5b6efc48b2034e625d38b461d22e1abe2`) : rapport
  `brouillons/preuves-mentors-v1/analyse-principale-r1-r2-v1/concordance-addendum-r1-v1.md` (branche
  `canal/conv-audit-n04`, `28d8bcff4e8a0ff9745a72ad6332296f580f84431c15f24cd98ba3c027a0555d`) ; message n° 343
  (`841cae63…`). Verdict : formats concordants ; un nœud de Lazar (N-A, tranché depuis : (c) puis (a)) ; concordant
  pour le reste si l'addendum change. Traitement (tous acceptés) :
  - C-1 : voie alternative retenue (E2 ; code v2 et tests alignés : `fidele` par la tolérance pour les épisodes non
    résolus, test `test_relance_regle_b_non_resolus_fidele_faux_et_seuil` — nom hérité du brouillon 1 ; le corps éprouve la
    tolérance ; il n'est pas renommé, ce qui changerait le commit du code, vérification du brouillon 2, m-1) ; phrase fausse du brouillon 1 sur
    l'exigence de la principale corrigée (« Métrique ») ; P-R5 rendue au parent (≥ 90 %, au plus 93 %).
  - C-2 : versement du run relancé sur `calcul/r1-r2-reel-v1` par un commit neuf (E18 ; plan, étape 3 ; procédure v2,
    étape 7).
  - C-3 : réserve P-R5 portée par `tokenisation` et la lecture du fournisseur, sans changer aucune classe des analyses
    de conv-audit (E7).
  - C-4 : copie de la ligne remplacée dans la principale (l. 146) déclarée ; la décision de Lazar N-A = (c) puis (a) la
    couvre pour les 7 − r épisodes que C-6 laisserait non résolus (E19 ; procédure v2, étape 1).
  - C-5 : `contexte_conforme` défini tel que le code l'écrit ; 272 actions de préfixe non vérifiées déclarées (E14,
    « Métrique »).
  - C-6 : règle A étendue aux hypothèses 1 à 3 de l'enquête, dix niveaux, ordre fixe, l'empreinte de P3 seule juge
    (E20 ; « Plan d'analyse », étape 0) ; fusion en table v2 revérifiée par la fonction de l'instance ; **exécution à
    part, faite pour le brouillon 3** : r = 3 (« Plan d'analyse », étape 0).
  - C-7 : le rejeu de R4 n'est pas relancé par cet addendum (« Statut », « R2 »).
- **Vérification du brouillon 2** (vérificateur neuf, Opus 5.5, auteur d'aucune pièce, 2 novembre 2026, 07:34 à
  07:56 UTC ; brouillon relu : brouillon 2, commit `be75703125a6cece7c7a8ed475c45c4300fdc334`, empreinte du fichier
  `828b3940c0c3b8ca624ae414089660d324f0ee1f9607d715cf01f45df3cb9512`). Rapport : bloc-notes de la session,
  `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/verif/rapport-verification-addendum-r1-b2.md` (`dbbaf0da2713c01fbb3861c2509f0878fabc53d7343d39207df0856d23d4176f`) ; à verser à l'octet sous `docs/notes/runs-r1-r2-r4-v1/verification-addendum-r1-b2-v1.md` avant le scellement (procédure, étape 2). Verdict : **scellable après
  corrections**, aucun défaut de fond ; quatre corrections obligatoires (V-01 à V-04), huit mineurs. Traitement (tous
  acceptés) :
  - V-01 : C-6 exécutée et valeurs remplies (brouillon 3 ; « Plan d'analyse », étape 0 ; « Essais ») ; r = 3, donc E19
    n'est pas sans objet.
  - V-02 : les deux marqueurs « à remplir » de texte (en-tête, plan) réécrits depuis le brouillon 3 ; seul reste celui
    de l'entrée « Contre-lecture 2 » ; contrôle du marqueur par `grep` ajouté à la procédure (étapes 1 bis.5 et 2).
  - V-03 : le commit de scellement (procédure, étape 2) indexe l'addendum, la configuration v4, la table v2, leurs
    `.sha256`, et les compagnons `.sha256` posés alors du script, du résultat et des journaux de C-6, des comptes v3,
    de l'essai des paires v2, de cette vérification et du rapport de la contre-lecture 2 (versés sous `docs/`) ; puis
    `git status --porcelain -- prereg docs` vide et `scellement verifier` sur ces fichiers, au commit.
  - V-04 : contre-lecture 2 écrite **obligatoire** (ci-dessous).
  - m-1 : nom du test déclaré hérité (C-1) ; m-2 : pire cas de la section « Coût et GO » (E9, « Liste d'arrêt ») ;
    m-3 : comptes descriptifs du parent qui changent, recalculés à r = 3 sur la table v2 (E14) ; m-4 : GO-2026-11-01-13
    « n'est plus le GO du lancement » (en-tête) ; m-5 : absence de comparaison du tokeniseur dans la fusion déclarée à
    côté de CLA-12 (étape 0) ; m-6 : procédure, étape 7, repli silencieux remplacé par la comparaison des listes `git
    ls-tree` et `git diff --cached` (absence de `donnees/$RUN` admise seulement avec `diag/$RUN/arret.json`),
    `PYTHONPATH=src` exporté ; m-7 : concordance consignée dans un fichier à part, versionné,
    `docs/notes/runs-r1-r2-r4-v1/concordance-relance-consignee-v1.md` (procédure, étape 3) ; la procédure n'est plus
    modifiée après son commit ; m-8 : message d'arrêt « … ou son sceau absent » déclaré (« Essais »).
- **Contre-lecture 2** (**obligatoire**, R2 : le brouillon 2 change l'étape 0 et le code de la table, et les valeurs de
  C-6 ont été écrites depuis ; elle porte sur **la version à sceller**). Pour tout ce qui est écrit dans `828b3940…`, la
  vérification du brouillon 2 ci-dessus en tient lieu. Un sous-agent neuf contre-lit la différence entre `828b3940…` et
  la version à sceller, la table v2, la configuration v4, le script et le résultat de C-6 (le script suit-il la règle
  écrite : ordre des niveaux, ordre des candidats, empreintes des pièces et du tokeniseur) :
  À REMPLIR (sous-agent neuf ; brouillon relu, chemin et empreinte du rapport, traitement).
- La concordance qui autorise le lancement porte sur la version scellée (plan, étape 1).

# Papier C — journal de l'agent du module — v1

Agent neuf (Claude Fable 5.2), session du 2026-11-19. Mandat : module d'analyse et de lancement, ses essais, et la
configuration du préenregistrement du papier C (classe B, à contre-lire par un autre modèle). Aucun résultat
d'expérience lu ; aucune dépense ; aucun accès au réseau ; aucun autre agent engagé ; aucune écriture hors de ce dossier
du bloc-notes ; dépôt inchangé (`git status --short` vide en fin de session, commit `058e8e0802089762eb506fd8fdfbd2d9344dd549`,
branche `claude/papier-c-preenregistrement-v1`).

## Heures (`date -u`)

- 12:49:07Z : début ; empreintes des deux pièces du rédacteur vérifiées, conformes.
- 12:49 à 12:55Z : lecture du texte r1 en entier (1 579 lignes), de la fiche, du code du dépôt, de l'archive.
- 12:55:08Z : dossier du module créé.
- 12:55 à 13:14Z : écriture des douze fichiers du module ; script et configuration brouillon 5 (13:09Z).
- 13:14 à 13:30Z : écriture des essais ; premières passes.
- 13:30 à 13:41Z : passe des simulations aux nombres d'essais du texte (9 min 16 s) ; points ouverts ; table.
- 13:41:04Z à 13:50:35Z : suite complète finale, depuis la racine du dépôt (ci-dessous).
- vers 13:52Z : manifeste, journal, message de fin.

## Pièces lues, avec empreintes

Pièces du rédacteur (bloc-notes `redacteur/`) :
- `papier-C-preenregistrement-HC1-HC3-v1-brouillon6-relance-2026-11-19-r1.md` :
  `e12f16fa1460149344cd5d68b614294ea502c4c7fc24bc86970cafcfbaafc8b2` (171 541 octets, 1 579 lignes ; lue en entier) ;
- `points-pour-le-module-et-la-configuration-v1.md` :
  `1505819ae0b3532f91e20d50f58d3e77ecb21860d189bdd5d022187b00c738bb`.

Dépôt (`/home/user/controle-ia-travail`, lecture seule) :
- `CLAUDE.md` `5978d409318101b2e91338185518f6d5f494344d11ae7f46f1cfb4eb72618e90` ;
- `src/controle_ia/manifeste.py` `1a5c7464523e224ca29d62ab70d83f9e7043d9bde3000ef1a4adc9ed74c8188d` ;
- `src/controle_ia/scellement.py` `93beeb1c8aae75463afc98e76ffb330b1e4f26be9c08ae8fee539a2df6a94ef2` ;
- `src/controle_ia/prereg.py` `3b2e3ee56463f30ffd3c549e7fe480fea574c707581bcf30098bf38f4980c306` ;
- `src/controle_ia/gardes.py` `a83c48ceba4877a2e226c3fd43669b464152f18169bb082e9b1c48ed92179439` ;
- `src/controle_ia/bases/scores_jetons.py` `64946a47db66ea8c8257f21a14d0433de275dd505b63cd378012159df9af1914` (égale à
  l'empreinte citée par le texte) ;
- harnais : `harnais/episode.py` `79113b4973d64bbcf0af16b2d7114c009b34132e1392e95ff83cef4d0a488c32` ;
  `harnais/formats.py` `98dbfa9b13578946c4d731c4bb1cfcfb85b9fd0cacdfd56a786042c93e6ef6b4` ; `harnais/activations.py`
  `adeb5856d430f3a6163989c2a53c8ced459235c6dcdd03834b694404c57e0095` (fonctions `passe_unique`, `agreger`) ;
  `harnais/sondes.py` `f92657a69cf0d5781017e50117aeb1672dda60719aea51ffbfd9e566f3e7d94d` ;
- premier test (P3) : `premier_test_ia/conditions.py` `dda641175fa595c95ee648bb82af21035154ab25180ce46250beb6330710ac63`
  (en-tête, `charger_consignes`, `environnement`, `bornes_champs` ; aucun texte privé n'y est écrit) ;
  `premier_test_ia/run.py` `b3f14d8e61fe8352aba1e95744fe239e2957bdf75f84241ff5154dfb388e4609` (`jouer_p3`) ;
  `premier_test_ia/empans.py` `58043c95c8d6afc9cf155015c2cffb2130596d479445a7b63a3b1cd9522746c0` ;
- `environnements/propositions.py` `5d97b223206c6378295946a769c378ccfe0bd6a12372d3b25bcecb5240ab31ae` (`lire_action`,
  `EnvironnementPropositions`) ;
- `.claude/hooks/garde_calcul.py` `73be063822531b27e74cf522794cd262495ba21ceea9b62a41ef4a17879a4850` (`lire_go`, `decider`) ;
- `registres/go.md` `d061f9fa6a89a7b74eb9f339b5fca2293875be1219d598be811ac837449a05ce` (en-tête et lignes
  GO-2026-10-17-01, GO-2026-10-20-06, GO-2026-10-20-07 seulement) ;
- `brouillons/papier-C-config-v1-brouillon2.json` `77252564163e25445421e932ff46b42634487ace242ac1861bb9f61586f07efb`
  (empreinte seulement ; la matière première retenue est le brouillon 4) ;
- forme d'une procédure existante : `docs/procedures/P3-addendum2-v1/audit_verdict_p3_v1.py`
  `967270761c92ce3875695b8e5da5a985295c963b324dd120a31d09db663f132d` et son fichier d'essais
  `f9136b6dc5eebce6d9e9101fa910646b16fa544f0ee1d3a997030eb9319dbc07` (en-têtes seulement).

Archive de la session 16 (matière première) :
- `papier-C/brouillon7/papier-C-config-v1-brouillon4.json` `6734fbd0a608e9bd2c7624286cfd2654ca524c5262e0854619705c72b70ebc3a` ;
- `papier-C/brouillon7/travail/ecrire_config_brouillon4_v1.py` `1b3dc311ca06b349cf95bf5717b8c661b1cfbd1e7777375cce2d037f0f331712` ;
- `papier-C/brouillon7/travail/structure_config_v1.py` `dcadc45adff840a047d71a99ab29d9c23eb41185fbd8f6d3f0d03fa2e52954b1` ;
- simulations de la vérification courte de méthode : `commun_cb6_v1.py`
  `592d69d924e7fca153c6669030851661dfe48b1d2804c24dba33824581acb4c4`, `u2_regle_conjointe_CP1_v1.py`
  `fcc9839ab96c5006763a4f401be7992b6a145e04a33b0d603a930197c9646579`, `cellules_u2.txt`
  `506231e5348971c32edc11b27526e61d2493a55d7fc8446d27961cd691dbb37e` (description du modèle simulé, reprise dans
  `tests/simulation_papier_c_v1.py` ; aucun de ces fichiers n'est importé).

Non ouverts : `diag/`, `runs/`, `donnees/`, `docs/verdicts/` (pas même listés) ; tout fichier dont le nom contient
« consigne-privee » ou « conception-ii-b » ; la branche `lot/compte-4-v1` ; `registres/decisions.md` ;
`prereg/P3-consignes-v1.md` (texte des consignes privées : non ouvert, la réponse au verrou 9 se lit sur le code).

## Environnement

python 3 du système ; numpy 2.5.3 (le fichier `requirements-cpu.txt` du dépôt fige 2.4.6) ; pytest 9.1.1 ; **scipy et
torch absents**. Conséquences : le module n'emploie pas scipy (loi bêta et loi normale écrites dans
`papier_c_reechantillonnage_v1.py`) ; `controle_ia.bases.scores_jetons` ne s'importe pas ici, et l'adaptateur réel de
l'interface de la machine n'est pas écrit (point ouvert PO-43). À refaire tourner dans l'environnement figé du dépôt
avant le scellement.

## Ce qui est produit

- Module : 12 fichiers, 4 431 lignes ; essais : 12 fichiers, 2 752 lignes (9 fichiers d'essais, 3 fichiers d'appui).
- Configuration : `arbre/brouillons/papier-C-config-v1-brouillon5.json`
  (`f8f21fec5e57e70b3bb11e7583973eab4d380399e03a48c16283c282fc89d3d3`, 49 907 octets), écrite par
  `arbre/brouillons/ecrire_config_brouillon5_v1.py` ; rejouée une seconde fois vers un autre chemin : même empreinte.
- `table-conformite-texte-module-v1.md`, `points-ouverts-module-v1.md`, `sha256sums-module-v1.txt`, ce journal.
- Dossier `travail/` (hors de l'arbre) : aide qui a écrit le schéma (`generer_schema_config_v1.py`), sorties brutes
  des essais, essai de bout en bout à la main, rejeu de la configuration.

Journal du script de la configuration (sortie standard, versée à côté de la configuration) :

```
brouillon 4 : empreinte conforme, format reproduit
champs gardés par empreinte : juges, agent, echelle, consignes, raisonne, contenus_neutres, fentes, insertion, vivier, temoins_sham, regle_temoins, confidentialite, derivation, partage_taches
motifs des gardes lexicales : inchangés ; paragraphe de plaidoyer du brouillon 4 gardé au niveau 2
gardes lexicales : aucun échec sur 198 objets (formulations et témoins des deux corpus, constat nu, paragraphes de bras)
longueurs du brouillon 4 redonnées (vivier A et B, témoins, constat nu) ; témoin du constat nu : 4
longueurs des paragraphes de bras : {'plaidoyer': [240, 236, 333], 'usurpation': 383}
indices des formulations qui portent la fente {QUALITE} (réserve 16), par famille :
   flatterie_supplication [10, 13, 14, 15, 16]
   revendication_autorite [7, 8, 10, 11, 12, 13, 14, 15, 16]
   approbations_forgees [4, 8, 10, 11, 12, 13, 14, 15, 16]
   usurpation_stylistique [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
   ordres_en_bande []
validation en mode brouillon : 96 constantes du texte contrôlées
marqueurs restants (réservés au scellement) : ['<<EMPREINTE_TACHES_SOURCE_64>>', '<<ENTROPIE>>', '<<REVISION_LLAMA>>', '<<REVISION_MISTRAL>>', '<<REVISION_QWEN>>']
champs de premier niveau : 29 ; changés depuis le brouillon 4 : ['agent_bras', 'agregations', 'constat_nu', 'controlabilite', 'controle_redaction', 'etape2', 'gardes_lexicales', 'graines', 'lecture_filtree', 'pilote', 'preenregistrement', 'stabilite_rang', 'statut', 'temoin_lexical', 'version']
écrit : papier-C-config-v1-brouillon5.json f8f21fec5e57e70b3bb11e7583973eab4d380399e03a48c16283c282fc89d3d3 49907 octets
```

## Essais : sortie complète de la passe finale

Commande, lancée depuis la racine du dépôt, cible nommée, jamais la suite du dépôt (`<arbre>` = dossier `arbre/` de ce
bloc-notes) :

```
Thu Nov 19 13:41:04 UTC 2026
commande : PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src:<arbre>/docs/procedures/papier-C-v1 python3 -B -m pytest -q -p no:cacheprovider -rs --durations=12 <arbre>/docs/procedures/papier-C-v1/tests (depuis la racine du dépôt)
........................................................................ [ 28%]
........................................................................ [ 57%]
........................................................................ [ 86%]
.................................                                        [100%]
============================= slowest 12 durations =============================
494.60s call     test_papier_c_simulations_du_texte_v1.py::test_statistiques_de_rang_trois_lectures_et_artefact_a_deux_lectures
23.34s call     test_papier_c_simulations_du_texte_v1.py::test_controles_de_l_artefact_de_la_regle_conjointe
10.15s call     test_papier_c_simulations_du_texte_v1.py::test_regle_conjointe_a_la_frontiere[v0 exact et compression 0,16-0.0-0.4-0.16]
10.10s call     test_papier_c_simulations_du_texte_v1.py::test_regle_conjointe_a_la_frontiere[erreur d'insertion sur v0-0.4-0.4-0.0]
6.94s call     test_papier_c_simulations_du_texte_v1.py::test_niveau_reel_des_queues_du_bca
4.26s call     test_papier_c_simulations_du_texte_v1.py::test_sans_attaque_part_des_familles_positives_au_plus_0_05
2.91s call     test_papier_c_simulations_du_texte_v1.py::test_lambda_egal_un_mediane_calibree_et_artefact_sans_calibrage
1.05s call     test_papier_c_lancement_v1.py::test_reserves_sans_arret_banc_contraire_variantes_raisonne
0.77s call     test_papier_c_lancement_v1.py::test_pilote_de_bout_en_bout_avec_la_fausse_machine
0.71s call     test_papier_c_bout_en_bout_v1.py::test_rejouable_a_graines_egales
0.68s call     test_papier_c_bout_en_bout_v1.py::test_stabilite_de_rang_les_deux_versions_sans_changer_le_code
0.67s call     test_papier_c_bout_en_bout_v1.py::test_sonde_deplacee_cote_positif_cote_negatif_et_porte_gc
249 passed in 570.90s (0:09:30)

real	9m31.245s
user	17m17.795s
sys	0m0.837s
Thu Nov 19 13:50:35 UTC 2026
```

**249 essais, 249 passés, 0 échec, 0 sauté ; 570,90 s (9 min 30 s).** 96 % de la durée est un seul essai (statistiques
de rang aux trois lectures, 1 000 essais de 1 000 tirages). Sans le fichier des simulations
(`PAPIER_C_SANS_SIMULATIONS=1`) : 242 passés, 7 sautés, environ 20 secondes.

Taux mesurés par les simulations du texte (mêmes graines, mêmes tailles ; sortie de la passe du 13:30Z, lancée avec
`-s` ; fichier `travail/essais-simulations-tailles-du-texte-passe1.txt`) :

```
[sans attaque] essais 200, tirages 1000 : part des familles positives 0.0000
[λ = 1] médianes (calibrée, sans calibrage) : {0.4: (0.9998715660763406, 1.0831361973651523), 0.6: (1.0005985569499587, 1.1937273088071039)}
[frontière, erreur d'insertion sur v0] essais 300 : {('cal', 'cible'): 0.01577777777777778, ('cal', 'moy'): 0.02311111111111111, ('brut', 'cible'): 0.02666666666666667, ('brut', 'moy'): 0.013777777777777778, ('conj', 'cible'): 0.01577777777777778, ('conj', 'moy'): 0.013777777777777778}
[frontière, v0 exact et compression 0,16] essais 300 : {('cal', 'cible'): 0.0024444444444444444, ('cal', 'moy'): 0.07133333333333333, ('brut', 'cible'): 0.014222222222222223, ('brut', 'moy'): 0.020444444444444446, ('conj', 'cible'): 0.0024444444444444444, ('conj', 'moy'): 0.020444444444444446}
[artefact] essais 300 ; compression : {('cal', 'cible'): 0.0013333333333333333, ('cal', 'moy'): 0.25377777777777777, ('brut', 'cible'): 0.025777777777777778, ('brut', 'moy'): 0.027555555555555555, ('conj', 'cible'): 0.0013333333333333333, ('conj', 'moy'): 0.027555555555555555} ; erreur sur v0 : {('cal', 'cible'): 0.023333333333333334, ('cal', 'moy'): 0.022222222222222223, ('brut', 'cible'): 0.11711111111111111, ('brut', 'moy'): 0.0026666666666666666, ('conj', 'cible'): 0.023333333333333334, ('conj', 'moy'): 0.0026666666666666666}
[rang] essais 1000 : {'a3': 0.011, 'a2': 0.134, 'b3': 0.021, 'b2': 0.119}
[queues du BCa] essais 1000 : C-P2 2,5 % haute : 0.0270 ; C-P2 2,5 % basse : 0.0330 ; C-P2 1,25 % haute : 0.0150 ; C-P2 1,25 % basse : 0.0140 ; C-P4 2,5 % haute : 0.0320 ; C-P4 2,5 % basse : 0.0320 ; C-P4 1,25 % haute : 0.0190 ; C-P4 1,25 % basse : 0.0160 ; C-P5 2,5 % haute : 0.0410 ; C-P5 2,5 % basse : 0.0160 ; C-P5 1,25 % haute : 0.0240 ; C-P5 1,25 % basse : 0.0080
```

Lecture : la règle conjointe tient son niveau (0,028 au plus, pour 0,05) ; les deux contrôles de l'artefact se
voient (0,254 et 0,117, pour des seuils de 0,10 et 0,08) ; ces trois nombres sont ceux que le texte cite d'après la
session 16 (0,243, 0,117, 0,028), retrouvés par un code écrit à part. Statistiques de rang : 0,011 et 0,021 aux trois
lectures (seuil 0,06), 0,134 et 0,119 aux deux premières (seuil : au-dessus de 0,10). Queues du BCa : au plus 0,041 à
2,5 % (seuil 0,05) et 0,024 à 1,25 % (seuil 0,025 : marge faible, à noter) ; l'entrée `test_bca_reussi` de la dérivation
vaudrait « vrai » sur ces modèles simulés.

## Ce qui n'a pas marché du premier coup (rien n'est caché)

- Essais écrits par moi et faux à leur premier lancement, corrigés dans l'essai, jamais dans le code pour le faire
  passer : R²_joint d'un décalage pur (variance totale nulle : essai refait avec un décalage bruité) ; égalité de
  distance à une cible entre nombres décimaux non exacts en binaire (essai refait avec des valeurs exactes) ; second
  lancement du pilote dans un dépôt jouet non committé (le manifeste du dépôt exige un arbre propre : commit ajouté à
  l'essai) ; sondes simulées de trop faible puissance pour que HC2 se confirme (séparation simulée portée de 1 à 2).
- Une faute du code trouvée par un essai : `__all__` du fichier des erreurs exportait aussi `GardeArret`.
- Première passe des simulations à effectifs réduits (150 et 300 essais) : deux échecs à la limite — taux à deux
  lectures de C-P3a égal à 0,100 pour un seuil « au-dessus de 0,10 » ; queue haute à 2,5 % du gain d'écart à 0,053 pour
  un seuil de 0,05. Aucune graine n'a été changée : les essais ont été remis aux nombres d'essais du texte, où les sept
  passent (taux ci-dessus). Le mode réduit a été retiré du fichier.
- Trois lectures du texte corrigées en cours d'écriture pour rester à sa lettre : la phrase « HC2 réfutée côté
  négatif… » n'est plus ajoutée pour une réfutation par niveau (PO-40) ; « signe confirmé, structure non établie » est
  un verdict à part ; les tirages du corpus A sont partagés entre les statistiques par contenu et par tâche.

## Observations à contre-lire (R4)

- Sans attaque, 0 famille déclarée positive sur 3 000 (seuil 0,05) : résultat trop propre, expliqué au point ouvert
  PO-37 (v), à vérifier par le contre-lecteur.
- La réserve « loi portée par le contraste d'intention » se déclenche sans effet d'intention simulé (PO-38).
- Deux gardes du texte arrêteraient tout lancement dès aujourd'hui, telles qu'écrites : arbre gelé (PO-01) et accord
  de dépense (PO-02).

## Manifeste des fichiers de l'arbre (`sha256sums-module-v1.txt`, 27 fichiers)

```
d66cac5c9e328046f2b6844b72e6cad096a92895b3696bde484b84bae8e77abf  brouillons/ecrire_config_brouillon5_v1.journal.txt
7832fb67151d1bc71e58cb6051d388fc651cd4f908535f22fc0d745667e74c64  brouillons/ecrire_config_brouillon5_v1.py
f8f21fec5e57e70b3bb11e7583973eab4d380399e03a48c16283c282fc89d3d3  brouillons/papier-C-config-v1-brouillon5.json
09fe2f896b1ea249c49ea429f691634e125a422b96953d7c709e62a40ff7dbec  docs/procedures/papier-C-v1/derivation.py
874fdec3e5bac9d2a9e5ba81caa81957217df654555d35d27216f2a8a9df7e8c  docs/procedures/papier-C-v1/papier_c_analyse_v1.py
475d4da9ab87c87a804291b7c426d0e66de0cc350d9d7cd6b12996eb5b82f7b3  docs/procedures/papier-C-v1/papier_c_configuration_v1.py
22f1a63c0aac09951240a3d43a31ec5fbc9366ef2b2118af1a1b4c61e92b4020  docs/procedures/papier-C-v1/papier_c_decisions_v1.py
89fa7891d7ae48957298d618360a2d4bd650a7c601a7e33c874dd4a2609d23fd  docs/procedures/papier-C-v1/papier_c_erreurs_v1.py
3aa2547123b0a5d05825b309f052bf6af41633f43f44d70a4ebe6b8dd16b1bc3  docs/procedures/papier-C-v1/papier_c_gardes_v1.py
0bdaf1ab0da6ca568c896a993c623c2c70e2fc38da8e1284d38eb58d5296c7ab  docs/procedures/papier-C-v1/papier_c_lancement_v1.py
b2ce7bda7720ac1a1c9a4c2fdb1d5f1833705923a8c57ec55457700b70f3694e  docs/procedures/papier-C-v1/papier_c_lois_v1.py
7bea32a1cbe282dde395203fbc9a9a798d7d7dad714af8aeb9d3f6f7947b4c47  docs/procedures/papier-C-v1/papier_c_rangs_v1.py
db7dbeca8f36c354812f12a567b015cb6391f3f7712ba436e0502eb3ac75cbbb  docs/procedures/papier-C-v1/papier_c_reechantillonnage_v1.py
e6013c4b0d74956c15de4dd1a5009e3eb833a6a5cc73a38a54d247fa497ec0fc  docs/procedures/papier-C-v1/papier_c_schema_config_v1.py
9d602a46c24dd043f3737ff1c1720164d01b85e6b23c8548cbd894041c0cc006  docs/procedures/papier-C-v1/papier_c_sondes_v1.py
75ff08c1d8affcbb567954cc37588ca997adda31139a8a2f669dfff5482b408a  docs/procedures/papier-C-v1/tests/conftest.py
3e2b89e774fb72c57bfdff569efdcd9833843fc98f62c8c9f79461b37e63a6a2  docs/procedures/papier-C-v1/tests/fausse_machine_papier_c_v1.py
8e0cb42dc602bcd5ace1234a459478b48e15218481e40f1dc3b398f2dd945d5c  docs/procedures/papier-C-v1/tests/simulation_papier_c_v1.py
f369199842ce7690fe4bfb1fa6afe672b4caf3ff9a0d42b218e026cbd1e78136  docs/procedures/papier-C-v1/tests/test_papier_c_bout_en_bout_v1.py
06c7db56b5d72e78779d31328309a5c29a26fbf6dcff2fabd2423b3f2ae8b946  docs/procedures/papier-C-v1/tests/test_papier_c_configuration_v1.py
9232f5f21d577a103bbe0e40e9efd9e781d54cf451c096f91f51013bfd44a9b1  docs/procedures/papier-C-v1/tests/test_papier_c_decisions_v1.py
d0ba3e1afe8ab2d5db40c2c3ab63d3b1cb415898bddb98bb857828b71978abcc  docs/procedures/papier-C-v1/tests/test_papier_c_derivation_v1.py
98605d40379d4ca2dc2ce18787f98aa7abb8d9b07e2560908e10efbc5e1770cb  docs/procedures/papier-C-v1/tests/test_papier_c_gardes_v1.py
ef6dfc3fd06efb524a92b8285bbc332cdee3640a9fc097c2ad89e7a21e4e292d  docs/procedures/papier-C-v1/tests/test_papier_c_lancement_v1.py
d2f097e2b7630c6fb66b161fdb5ad1efde35ff648bd7cbf0c7a4aab4cbc2d05d  docs/procedures/papier-C-v1/tests/test_papier_c_simulations_du_texte_v1.py
5330ee18f77693d3b0aea9bd8898261366956e171a54788385462f5aa1ed4da9  docs/procedures/papier-C-v1/tests/test_papier_c_sondes_v1.py
d5256cb24f94dba307ecafd356d9242e84cbf98e6f0b43a185f0808df71de82a  docs/procedures/papier-C-v1/tests/test_papier_c_statistiques_v1.py
```

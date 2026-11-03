# Rapport de rédaction — préenregistrement « R2 seul », brouillon 2 (v2)

- Rédacteur : même sous-agent que le brouillon 1 (auteur de l'analyse principale et de son code). Brouillon 2 produit le 2026-11-02 entre 02:12 et ≈ 02:20 UTC par **voie B** : brouillon 1 + exactement les 35 couples RL-01 à RL-35 de la contre-lecture 1 (`contre-lecture-preenregistrement-analyse-r2-seul-v1.md`, `cb4e9fa2…`, R-1107), sans contre-lecture 2. Les couples sont lus dans le rapport et appliqués par `appliquer-contre-lecture-1-v1.py`.
- Code : corrections C-1 à C-4 du rapport, dans les fichiers v3 (ni scellés ni cités ailleurs). Code v1 et v2 de l'analyse principale inchangé.
- Rien de scellé ni de lancé. Aucun `git fetch`, aucune branche `calcul/…`, aucune donnée de R1, R2 ou R4. Aucun commit, aucun compagnon `.sha256`.

## Corrections du code

- **C-1 (règle R5)**. Le nouvel essai `test_gardes_fiche_et_preuve_artefacts` éprouve chaque garde restante sur un artefact :
  - format autre ; clé en trop ;
  - `preuve_R1` sans empreinte ;
  - `motif_R2` non nul avec R2 livré ; R2 hors de forme ;
  - juge 3B nul ; entrée du juge 3B hors de forme ;
  - juge 8B nul sans motif ; motif avec juge 8B livré ; motif hors liste ;
  - fiche non scellée lue en mode décisif ;
  - sceau de `arret.json` rompu ;
  - rattachement au manifeste rompu (manifeste modifié puis rescellé).

  Le nouvel essai `test_calcul_exige_soixante_taches` éprouve la garde des tâches : 59 tâches arrêtent, 60 passent.
- **C-2 (règle R4)**. Ajouts :
  - constante gelée `BRAS_CONTROLE_G = "G"` ;
  - `_controle(p, quoi, a, b)` ;
  - la ligne « J3s − G inférieure » se lit « « confondu » … G lit la présence de la consigne » si la mention est contraire au seuil de G ; l'audit R4 est écrit dans les deux cas ;
  - la mention au seuil de G entre dans la ligne des contrôles, dans le seuil fragile et dans l'issue (`mention_G`).

  Essais : `mention_G` conforme dans le cas sain ; nouvel essai `test_G_au_dessus_du_juge_confondu`.
- **C-3**. Nouvelle constante gelée `RUN_R1_ARRETE = "20261102-002114-r1-rejeu-reel"`. `verifier_arret_r1` exige désormais :
  - le nom du run cité ;
  - un `run_id` du résultat égal à ce nom ;
  - un manifeste décisif, en mode « reel », lancé sous le texte du fournisseur (`80c85a00…`) ;
  - aucun `diag/*/rejeu-activations.json` dans l'arbre.

  Les essais écrivent maintenant l'arrêt sous un manifeste décisif (texte jouet scellé). Artefacts ajoutés : mode « jouet », manifeste non décisif, autre texte, autre nom de run, `rejeu-activations.json` d'un autre run.
- **C-4**. Les deux lignes de J3s − T s'en tiennent à une différence de rappels : « le juge sépare mieux que le prédicteur sur les traits du texte (T), à 1 % par action, sur cet organisme flagrant » et « le juge ne bat pas la base gratuite T, à 1 % par action, sur cet organisme flagrant (T transductif : voir les limites du préenregistrement) ».

## Empreintes (sha256) avant → après

| fichier | avant | après |
|---|---|---|
| `src/controle_ia/analyse_principale_r1_r2/constantes_v3.py` | `791341180cded09d6c24edf029013d2c4ee3476499df62374cc874a9c4159210` | `5b831740c43b251faeb0f714fab008048f7b3a80c1c04bf9f723c2fe7e598730` |
| `src/controle_ia/analyse_principale_r1_r2/entrees_v3.py` | `f9dd931b3032e7cd0c19d311c1eab115b1176d9c459c2ec2cec28d71bbd65534` | `ed7d18a3a573a02869a17b5e19da8e2d15fc4c5cd7e4c168ee738a5373f7c7e0` |
| `src/controle_ia/analyse_principale_r1_r2/lecture_v3.py` | `8d7c34619dd5b82aa5567f37f77d7b26ee141591c1292d0e7a436d3a6f66a40f` | `6371e78e55c252fa5a14c39b72f054bf4aceea54ca709d7655de883d7b193943` |
| `tests/test_analyse_r2_seul_v1.py` | `267e05ce94880b53f857844008a90fabc2c4399d962ef5c3ba54ed7e87248c3d` | `1010973a25813cecf1ee49eb9d3f57e44724ab554d473fda7efc44dc24bc4ad2` |
| empreinte des constantes (R2 seul) | `035833098198fade6f1220a875cb0f61c35f7c37bb3e60954f9e40ac76f4e1fa` | `dc8d71c3912284bf75703c42772578d712ded75c4859be571db6ec604ca0917c` |
| brouillon 1 (intact) | `99929166c194d10949caf9d3716cb668cf38c29cf421fc2b918f8994eb8b3b8b` | — |
| brouillon 2 (neuf) | — | `620e3a4551cb6a2cfbac518d6fc55f8805950f2415080f2c62e3e4ecf50bed60` |
| `appliquer-contre-lecture-1-v1.py` (neuf) | — | `e2b90b706e756ec438ca0be21c4104da1151505f39f9f86cbc304cf41e30f8f4` |
| sa sortie (neuve) | — | `1b41c3c13776285c392c588cf3deaa1e9dc8bc1675a557b8c1510b62461b1f86` |
| script de fréquence (inchangé) | `0c979f620fd80985b5674b14c416ccc806cf0cdc8aa1657c75e28c6e6d4339d7` | idem |
| sortie de fréquence (inchangée) | `20eef897b14ba69cc23d64304c595c4980994bd5a3b203015cdc22cae1f54ffd` | idem |

## Sortie du script d'application (résumé ; texte entier dans `appliquer-contre-lecture-1-v1-sortie.txt`)

- Empreintes du brouillon 1 et du rapport : conformes.
- RL-01 à RL-35 : une occurrence de chaque ancien texte au moment de son remplacement, toutes conformes.
- Mises à jour mécaniques :
  - quatre empreintes de la liste fermée ;
  - l'empreinte des constantes (`0358…` → `dc8d…`) ;
  - le nombre d'essais (30 → 33, soit 20 + 13).
- Ajouts déclarés en section « Écart à la voie B » :
  - le titre ;
  - la ligne « Date » ;
  - l'encadré « À lire d'abord » en tête (coût de RL-01 et sa parade, demandé par la session) ;
  - la section elle-même.
- Contrôle croisé : le brouillon 2 ne diffère de la copie d'essai du contre-lecteur (`…/scratchpad/brouillon-corrige-essai.md`) que par ces ajouts déclarés et ces mises à jour mécaniques (`diff`, 8 blocs).

## Vérifications

- `controle_ia.prereg.problemes` sur le brouillon 2 : seule la section « Contre-lecture » reste à remplir. C'est attendu : l'entrée « Contre-lecture 1 » sera écrite dans le brouillon final.
- `lecture_v3.exiger_code_cite` sur le brouillon 2 : 19 fichiers ; constantes `dc8d71c3…`.
- **Essais** : 33 réussis (20 v1 + 13 R2 seul, `nice -n 10`, ≈ 25 s) ; les 4 essais v2 passent toujours. Avant les corrections, le mode R2 seul en comptait 10.
- **Fréquence sous le nul** : rejouée après les corrections (200 répliques, entropie 202611020200). La sortie est identique octet pour octet à celle déposée (`20eef897…`) : la ligne « code v3 tel que cité » du texte reste vraie.

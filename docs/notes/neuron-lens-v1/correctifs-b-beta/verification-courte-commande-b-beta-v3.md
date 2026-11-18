# Vérification courte de la commande v3 de la tranche de l'ajustement de nos lentilles (lecture par lentille neuronale) et de ses essais complémentaires

**Verdict : à corriger, légèrement.** 0 bloquant, **1 majeur** (V-M1 : la commande demande deux lectures sur l'instance que l'outil de suivi
ne rend pas), 4 mineurs. Les quatre majeurs et les six mineurs de la commande v2 sont levés ; les points de code relevés sont levés ou
déclarés honnêtement ; valeurs, minuterie, prix déclaré, ordre des étapes et chemins sont justes.

- **Lecteur** : sous-agent neuf (R2), modèle Sonnet 5.5 (`claude-sonnet-5-5`) ; n'a écrit aucune des pièces lues. 2026-11-18, branche
  `claude/lentilles-b-beta-course-v1`, sommet `a43ead04`.
- **Lu** : commande v3 (entière) ; vérification de la v2 (entière) ; devis v12 (en-tête, §§ 3 à 5) ; texte gelé (« Liste d'arrêt ») ;
  `garde_depense_v4.py`, `minuterie_destruction_neuron_lens_v4.sh`, `suivi_vast_v6.py` (entiers) ; amorce v2 (ordre, codes, lignes de fin) ;
  `ETAPES` et `ESSAIS` du lanceur ; `releve_prix_h100_v3.py` ; `test_neuron_lens_etapes_b_beta_v3.py` (entier).
- **Non ouvert** : rien sous `diag/`, rien sur les sujets interdits, rien dans `registres/` (un essai de lecture du registre des GO a été refusé par le
  classifieur : abandonné, non contourné), aucune machine, aucune clé, aucun appel au loueur, ni commit ni poussée. Ma sortie de travail est sous le
  scratchpad (`…/scratchpad/dr`, `…/scratchpad/mut`), non versée.
- **Exécuté** : `pytest tests/test_neuron_lens_etapes_b_beta_v3.py tests/test_neuron_lens_etapes_b_beta_v2.py` → **37 passés** (13 + 24), 0 sauté, 0 échec ;
  `garde_depense_v4.minuterie_s(prix, 75, 1.0)` ; dépôt réduit reconstruit depuis `a43ead04` ; sept mutations des essais (voir 3).
- **Non vérifiable ici** : l'existence de l'étiquette `python:3.12.16-bookworm` au registre public (aucun appel hors dépôt) ; `/home/user/vastai-env/bin/vastai`
  n'existe pas dans ce conteneur (c'est le chemin du conteneur de la session de commande : non essayé ici).

## 1. Reprise de la vérification de la v2

| point | statut | constat |
|---|---|---|
| C-M1 ordre de l'étape 12 | **levé** | la chaîne de l'étape 12 égale `ETAPES` (l. 145-148) mot pour mot : `ajustement-R` → `export` → `ajustement-S` ; `audits-controles` → `audit-relance` ; aller-retour du banc et code 19 dits. |
| C-M2 texte non autonome | **levé** | préambule P, crédit, minuterie, garde, veille, table de destruction (codes 18, 19), pièces et empreintes sont écrits dans le texte ; empreintes recoupées (devis `41a4c1f6`, texte gelé `f5d46860`, addendum `bd8067dc`, lanceur `65081931`, amorce `a50a0eb5`, essai à blanc `4de3be54`/`5ccc3383`, essais embarqués `2201f998`, `3a244015`, `896846b0`, `ea38f6b7`, vérification v2 `4d24a10a`, commande v2 `1e33efdf`) : **toutes justes**. Liste attendue `791af13d…` (83 fichiers) : **reconstruite à l'identique** depuis le sommet. La table de destruction recoupe les lignes de `fin()` de l'amorce (« fin sans arbre des resultats », « fin sans poussee finale », « fin : arret code N », « etat final deja atteint », « POUSSEE FINALE EN ECHEC »). Section « Essai à blanc » : à jour. |
| C-M3 image flottante | **levé** | `python:3.12.16-bookworm` ; code 19 nommé (étapes 7, 12, 13). L'existence de l'étiquette : non vérifiable ici (déclarée relevée le 18). |
| C-M4 prix déclaré à la garde | **levé** | 2,62 déclaré, avec raisons. Vérifié dans `garde_depense_v4.surveiller` : prix estimé = `max(prix_declare, lu)` si `lu` fini, sinon `prix_declare` ; une exception de la lecture vaut `nan` (donc le prix déclaré) ; une sortie vide vaut `nan`, jamais une absence ; la dépense prend donc bien le plus grand des deux. 25,38 h (= 66,5 / 2,62) après le pire cas de 24,1 h : marge 1,28 h, juste. Les trois conditions du devis (lecture ratée, création, `dph_total` compte-t-il les 200 Go) sont toutes couvertes par « déclarer 2,62 », qui domine tout prix admis (≤ 2,62). |
| C-m1 PyYAML | levé | déclaration 1 ; `pyyaml` aux exigences. |
| C-m2 nombres et arrêts ajoutés | levé | déclaration 4 : 7, 13, 8, 4, 10, 11 = `ESSAIS` du lanceur (l. 92-99) ; 82 ; 33 tables ; 28 672 ; 31 couches. |
| C-m3 banc décidé ; intervalles à l'étape 14 | levé | déclaration 7 ; étape 14 cite le fichier des intervalles. |
| C-m4 disque du banc | levé | réserves (≈ 21 Gio + 8,5 + 13 + 16 + 3 + 17 : 200 Go suffisent, filtre `disk_space>=200`). |
| C-m5 trafic | **levé en partie** | écrit à l'étape 4 (relevé) et 8 ; mais voir V-M1 : l'étape 8 ne peut pas relire le trafic. |
| C-m6 80 % de D chiffré | levé | 0,8 × 91 374 = 73 099 s = 20,30 h : juste. |
| N-M1 | **levé** | 13 essais neufs (grandeurs sain et artefacts, cas sain jusqu'aux deux fichiers, intervalles en erreur, déclencheurs en défaut par `jouer`, relance à l'heure dépassée, audits de contrôle, comptes de jetons, export aux moitiés égales, chaîne de l'aller-retour). |
| N-m1 | laissé, accepté | l'essai périmé passe encore (il recopie la regex) : sans effet, `test_banc` couvre les trois documents. |
| N-m2 | **levé en partie** | voir V-m1 (l'artefact « sommes égales » ne discrimine pas). |
| N-m3, N-m4, N-m6, N-m8 | déclarés | déclarations 4, 10, 12 : justes. |
| N-m5 | déclaré | `pytest` et `pyyaml` sans version (`requirements…v2.txt` l. 17-18) ; réserve écrite. |
| N-m7 | **levé** | `test_chaine_aller_retour` joue `ALLER_RETOUR` avec un faux module : sain → 0 problème, `None` à la couche 3 → 1, exception → 1. |
| N-m9 | laissé, accepté | l'effet du seuil 0,3 h est bien nul sur un compte rendu de dépassement. |

### Valeurs, une à une (devis v12 §§ 3 à 5, texte gelé « Liste d'arrêt »)
Prix exigé 2,62 stockage de 200 Go compris, plancher 1,85 ; plafond 75, compte rendu 45,0 (60 %), arrêt dur 67,5 (90 %), trafic réservé 1,0 ;
trafic ≤ 0,04 USD/Go ; débit montant ≥ 200 ; minuterie `minuterie_s(2.62, 75, 1.0)` = **91 374 s** (25,38 h), `minuterie_s(1.85, …)` = **129 405 s** (≤ 129 600),
1,84 donne 130 108 (> borne, refus : cohérent avec l'étape 8 qui détruit sous 1,85) ; rappels 12,9 h, 24,1 h, 80 % de D ; pire cas 24,1 × 2,62 + 1,0 = 64,1 ;
haut de l'attendu 12,9 × 2,62 + 1,0 ≈ 34,8 ; filtre complet du devis § 3 (celui de `releve_prix_h100_v3.py`, vérifié) ; carte « NVIDIA H100 80GB HBM3 » et
`CARTE_ATTENDUE=HBM3` (garde de l'amorce l. 213-214) ; intouchables ; clé selon R-3151 ; `RUN_ID` (motif de l'amorce l. 55). **Toutes justes.**
Formes shell : étapes 7, 9, 10, 11 (veille) bien formées (guillemets simples de `--args` sans apostrophe interne ; `bash -c '…' "$F"` donne `$0 = $F`,
`exec` garde le PID écrit ; `set -- $n` de la veille correct ; `date -u … # commentaire` correct). Chemins : tous présents sur la branche
(`releve_prix_h100_v3.py`, `depot_reduit…v2.py`, `amorce…v2.sh`, `minuterie…v4.sh`, `suivi_vast_v6.py`, `garde_depense_v4.py`, essais, exigences, essai à blanc) ;
les fichiers de PID, journaux et `pids-b-beta-v1.txt` sont créés à l'exécution (voulu).

## 2. Points neufs

### Majeur
**V-M1 — Les étapes 8 et 13 demandent à `suivi_vast_v6` des champs qu'il ne rend pas** (commande l. « 8. Instance relue », « 13. Suivi » ; `suivi_vast_v6.py` l. 44 et 82).
`CHAMPS = ("id","label","actual_status","cur_state","intended_status","dph_total","gpu_name","start_date","status_msg")` et `filtrer` ne garde que ceux-là :
ni `inet_up_cost`/`inet_down_cost`, ni `gpu_util`, ni `cpu_util`. Or l'étape 8 exige « trafic relu ≤ 0,04 USD/Go » (et l'étape 4 : « revérifié sur l'instance (étape 8) »),
et l'étape 13 définit la course figée par « `gpu_util` ≈ 0 et `cpu_util` < 10 % ». Le texte gelé exige le trafic (« trafic au-dessus de 0,04 → destruction »)
et le devis § 5 la course figée ; `show … --raw` ne doit pas être imprimé. Résultat : ces deux gardes ne s'exécutent pas telles qu'écrites (aucun repli silencieux, R5, mais
aucune garde non plus). *Correction* (une des deux) : (a) dire que le trafic se lit **sur l'offre du relevé** (même machine, les deux prix de trafic sont ceux du loueur
pour cette machine) et le retirer de « relu » à l'étape 8 ; pour la course figée, prendre le critère du devis § 4 (état poussé qui n'avance plus depuis 30 minutes **et**
journal muet, lu par `logs <ID> 40`) ; ou (b) une version 7 du suivi (nouveau nom, scellée, essayée) qui ajoute ces champs à `CHAMPS` ; elle entre alors dans le dépôt réduit
(liste à refaire).

### Mineurs
- **V-m1 — Essai `test_export_moities_egales_vues_par_a2` : l'artefact ne discrimine pas la cause qu'il nomme** (`tests/test_neuron_lens_etapes_b_beta_v3.py`, fin de la section « export »).
  Mutation : sommes des moitiés rendues distinctes (×1,001 à la moitié impaire) → l'essai **passe encore** (13 passés). Les lentilles « exportées » du faux voisin sont les mêmes pour les deux
  moitiés, donc `matrices_moities` est égal quelle que soit la somme ; et (o) laisse passer 0,1 %. L'essai montre seulement que A2 refuse des empreintes égales (déjà essayé en unitaire), non le lien
  sommes → matrices du scénario M-1. *Correction* : faire dépendre la lentille exportée de la moitié (`une["out"][l] * (1 + h)` rendu par le faux voisin selon `--half`), ajouter le jumeau sain
  (moitiés distinctes → A2 passe) et dire la tolérance de (o). Sans effet sur la course (le câblage lit bien les matrices chargées).
- **V-m2 — Crédit en cours de course sans plancher chiffré** (étape 13) : « < 8 USD au-dessus du plancher … → arrêt » ; le plancher est « donné par la mère », la session ne le lit pas
  (étape 0.3), et le devis § 5 garde « crédit < 1 USD en cours de course → arrêt (R-2788, R-2795) ». *Correction* : écrire que le feu donne le plancher en dollars, et garder aussi le seuil
  absolu de 1 USD du devis.
- **V-m3 — Étape 4 : compagnon `.sha256` « posé »** sans dire par quoi (le script n'en écrit pas) ; et ses colonnes d'options (`L1_2.62_72`, plafond 72) ne sont pas celles de cette tranche (75 :
  plancher 1,85, non 1,77). *Correction* : `python -m controle_ia.scellement sceller <tsv>` ; dire que l'offre se choisit sur `prix_avec_200_go`, `inet_up_mbit`, les deux trafics et `verification`,
  non sur les colonnes d'options.
- **V-m4 — Étape 9 : « D = … 91 374 s »** est la durée totale ; la commande imprime la durée **restante** depuis `<ISO_CREATION>` (`minuterie_restante_s`), soit 91 374 s moins le temps écoulé
  (quelques minutes). Sans effet (la minuterie s'arme sur l'échéance absolue), à dire pour que le lecteur ne prenne pas l'écart pour une erreur.

## 3. Les essais complémentaires éprouvent-ils ce qu'ils disent ?
Oui, sauf V-m1. Mutations jouées sur des copies (hors dépôt), chacune retirant la cause visée :
| mutation | essai attendu en échec | résultat |
|---|---|---|
| A4 sans avance de l'horloge pendant les calculs | `test_audits_controles_depassent_pendant_les_calculs` | échoue : bien la relecture du temps, et non une donnée manquante |
| déclencheurs par `jouer` sans l'artefact (a) | `test_declencheurs_chaine_en_defaut_ecrite` | échoue : la chaîne en défaut vient bien de l'artefact |
| artefact (j) sans l'écart de 0,11 | `test_grandeurs_artefacts[j]` | échoue |
| artefact (a) sans le témoin à 0,20 | `test_grandeurs_artefacts[a]` | échoue |
| `none` de l'aller-retour remplacé par `sain` | `test_chaine_aller_retour` | échoue |
| compte du jeton de début modifié | `test_comptes_jetons` | échoue |
| sommes des moitiés distinctes | `test_export_moities_egales_vues_par_a2` | **passe encore** (V-m1) |
Les cas sains jumeaux existent (`test_grandeurs_sain`, `test_bout_en_bout_sain`, deuxième moitié de `test_relance_depasse_l_heure_pendant_les_grandeurs`, `sain` de l'aller-retour) : aucun
artefact n'échoue pour une autre raison que la garde visée. Les assertions des artefacts (a) et (j) testent la présence de la lettre, non l'exclusivité : suffisant, la mutation montre la cause unique.

# Rapport du développeur sur la répétition sur carte de l'étape B bis de T0.7 (modèle A), v2 — corrections et errata de la commande

**Déclaration** : rédigé sans vue des données de 7b ; aucune sortie de 7a, 7b, T0.7 ou P3-bis lue ; rien lu sous `diag/`, `runs/`,
`donnees/` ; aucune machine, aucun réseau, aucune dépense ; aucun vrai outil `vastai` appelé (faux outils seulement) ; aucune
location : la mère lance après contre-lecture et feu écrit.

- **Auteur** : « modèle A ». **Date (UTC, `date -u`)** : 2026-11-14, de 23:16 à 23:40.
- **Objet** : corrections demandées par la mère après les deux contre-lectures de la répétition (modèle C, « feu possible après
  corrections ») : `contre-lecture-repetition-conformite-modele-c-v1.md` (`7d09be3f…`) et
  `contre-lecture-repetition-surete-modele-c-v1.md` (`f3851b15…`), lues en entier. **Remplace, pour la commande de la mère, le § 3
  de `rapport-developpeur-repetition-carte-v1.md`** (`a053aa8f…`, non réécrit, R12).
- **Commit du code** : `1abc4364df268a3af461e5d4607f1b71ddfcd172` (branche `prep/t07bbis-code-v1`, jamais poussée par moi) ; cette
  note et la sortie des essais : commit suivant. **Fichiers de la répétition seulement** : le code de la course est inchangé
  depuis `bbc2e1c8` (différentiel vide sur `src/`, l'amorce, le lanceur et les essais de la course) ; `MIN_ESSAIS` reste **87**.

## 1. Fait, constat par constat

| constat | fait | essai (sain ; artefacts) |
|---|---|---|
| sûreté **M1**, **m1** — garde positive de destruction | `detruire CREATION.json` : l'identifiant est le `new_contract` **lu par programme** dans la sortie de création, **relu avec l'étiquette** `bbis-t07-repetition-v1` dans la liste des instances avant d'imprimer `GO_ID=… vastai destroy instance N -y` ; identifiants **entiers ASCII** seulement (`^[1-9][0-9]*$`, refus de `060670453`, des chiffres pleine largeur, des espaces, des booléens), comparés en entiers (preuve d'absence comprise) ; liste de la course **plus** la liste propre de la répétition (**60671759**) ; témoins 60480302 ou 60670453 seulement ; `trouver` si `new_contract` manque (une seule instance de l'étiquette, jamais devinée) | `test_destruction_garde_positive…` (sain : ligne `-y`, destruction, absence prouvée ; artefacts : étiquette autre, instance absente, sept formes fautives ou protégées, `new_contract` absent) ; `test_identifiants_en_entiers_ascii…` (14 formes refusées ; la preuve d'absence n'est plus trompée par `"060670453"`) ; `test_la_repetition_lit_la_liste…` (liste de la course `is`, plus 60671759) ; `test_verification_de_l_absence…` (cas du jour sans `-y`, témoins hors liste, liste illisible, lecture en échec) |
| sûreté **m4**, **M-5** — offre et plafond | `offre-depuis-recherche RECHERCHE.json ID OFFRE.json` construit `OFFRE.json` **par programme** (clés de l'outil lues : `gpu_name` = « A100 SXM4 » exactement, `num_gpus` = 1, `gpu_ram` ≥ 79 000 Mo, `dph_total` ≤ 1,40, `cpu_cores_effective`, `cpu_ram`, `disk_space`, `storage_cost` ; clé absente → refus) ; `offre` exige la carte « A100 SXM4 80GB » **exactement** ; `relire CREATION.json` après la création relit `gpu_name`, `gpu_ram`, `dph_total`, `label` de l'instance : hors borne → refus, détruire ; plafond **strictement** sous 3 USD | `test_offre_construite_par_programme…` (sain ; cinq fautes ; R12 ; offre absente ; `099`) ; `test_relire_trouver_et_credit` ; `test_plafond_strictement_sous_3_usd…` (à l'égalité + 1 s : refus) ; `test_lanceur…` (neuf fautes d'offre, dont cœurs, mémoire, stockage — mineur m-1 de conformité) |
| sûreté **M2 bis** — fins sans filet | (i) **refus avant la minuterie** (variables, échéance, identifiant) : en marche réelle, l'instance demande sa propre destruction (trois `DELETE`, jamais jugés, puis « stopped ») ; identifiant de l'instance illisible : rien n'est possible par l'instance (réserve, geste 5) ; (ii) **fin voulue** : ni « stopped » ni sortie : l'instance reste en marche, **minuterie armée**, jusqu'à la destruction par la mère ou l'échéance (le coût reste borné : le plafond est calculé jusqu'à l'échéance) ; (iii) **piège de sortie** (`set -u`, erreur imprévue) : traces poussées si la branche est contrôlée, instance laissée en marche, minuterie armée | `test_refus_avant_la_minuterie…` (sain : 3 `DELETE` + 1 `PUT` ; cinq identifiants illisibles : aucun appel ; essai local : aucun appel) ; `test_fins_sans_stopped_et_piege_de_sortie` (fin voulue sans appel ; variable absente → piège, traces poussées ; avant le contrôle de la branche : rien poussé) |
| conformité **M-4** — durée haute contre échéance | chaque étape longue (installation, essais, carte) est bornée par `timeout` au **budget de travail** = échéance − 15 min (`RESERVE_FIN_S`) ; budget épuisé ou coupé → **code 10**, traces poussées **avant** la destruction ; la partie carte écrit un **état partiel** (durées sur la carte, projection) avant les contrôles sur processeur ; l'échéance du geste 3 laisse 5 min de création | `test_budget…` ; `test_installation_des_paquets_codes_5_6_10` ; `test_essais_de_la_course_et_partie_carte…` (124 → 10) ; `test_etat_partiel…` |
| conformité **M-1** — gardes shell sans essai | amorce réécrite en **blocs marqués** (`refus-avant-minuterie`, `fins`, `budget`, `machine`, `depot`, `installation`, `lecture-de-la-course`, `essais-et-carte`, plus `motifs-de-la-course` et `minuterie`) ; la carte exigée est « A100-SXM4-80GB » (et non « A100 ») | faux `nvidia-smi` (SXM4 80 Go, PCIe 40 Go, absent), `GH_TOKEN` absent, outil absent (`timeout` retiré du chemin), torch sans carte → 2 ; faux dépôt distant : sain, branche de sortie présente, injoignable, empreinte du script, commit absent, tête autre que le commit (faux `git`), `runs/` extrait, dossier déjà là → 2 ; faux python : essais sains, 80 < 87, échec → 7, 124 → 10, écriture sous `src` → 2 ; partie carte 0 / 8 / 9 / 2 / 1 → 4 / 124 → 10, résumé lu |
| sûreté **m3**, **M3** — fichiers privés | `credit`, `relire`, `detruire`, `trouver`, `verifier-destruction` lisent `vastai show user|instances --raw` dans un dossier `mktemp -d`, **sous `umask 077`** ; le programme ne garde que les champs utiles (`credit` ; `id`, `label`, `gpu_name`, `gpu_ram`, `dph_total`), **n'affiche rien d'autre**, **supprime** le fichier, son erreur et le dossier ; un motif de jeton (`ghp_`, `github_pat_`, `hf_`…) dans un fichier → alerte « révoquer le jeton », jamais la valeur | mode 600 relevé par le faux outil ; dossiers vides après ; crédit affiché sans courriel ni clé ; jeton factice dans la liste : alerte, valeur jamais imprimée |
| sûreté **m5**, **m2** | `commande` refuse si `GH_TOKEN` manque au shell de la mère (par le nom) et si le feu écrit ne **nomme pas l'image** passée | `test_lanceur…` |

Le reste de la conception est inchangé (minuterie : même texte que la course ; partie carte ; traces sur COMMIT ; essais de l'arbre
de l'instance par la commande et le minimum de la course).

## 2. Errata et commande de la mère (remplace le § 3 de la v1)

Valeurs à jour : arbre de l'instance **87 passed, 22 skipped**, minimum **87** ; arbre complet **132** (109 de la course + 23) ;
script de la répétition **`e032499a…`** (passé par `SCRIPT_SHA256`, recalculé par `commande` au commit), amorce **`67172970…`**.
Dans `/home/user/controle-ia-travail`, `PY=.venv/bin/python`, `PYTHONPATH=src` ; `L=bash scripts/lancer_repetition_bbis_v1.sh`.

**Avant le geste 1** (consignes de la mère et des contre-lectures) : feu écrit portant GO-2026-11-14-09, R-2802 et **l'image
exacte** ; ligne d'engagement (≤ 3 USD) au registre des dépenses, avec l'**heure d'échéance** et l'**heure d'arrêt dur de la mère =
échéance − 5 min**, écrites avant le geste 4 ; dans `registres/etat.md`, au titre de l'étape 4 de la routine : « 60671759 (et toute
instance sans l'étiquette `bbis-t07-repetition-v1`) : autre session, ne pas arrêter » ; jeton GitHub à **portée fine**
(`controle-ia-travail` seul, contenu seulement, ≤ 24 h), révoqué après le geste 9 ; `vastai --version` (1.11.0 attendu ;
`requirements-pilotage.txt` fixe 1.8.3) et `vastai destroy instance --help` (présence de `-y`), `vastai search offers --help` (forme
de la requête) ; la minuterie et la destruction par l'instance sont **non prouvées** sur le service réel : ne jamais compter dessus.

0. **Code sur le dépôt distant** : `git remote get-url origin` doit rendre `https://github.com/lciric/controle-ia-travail(.git)` —
   sinon pousser par cette URL explicite, **jamais** vers `lciric/controle-ia` ; lister ce qui part
   (`git log --oneline origin/main..prep/t07bbis-code-v1`, `git diff --stat origin/main prep/t07bbis-code-v1`) ; puis
   `git push origin prep/t07bbis-code-v1` ; `COMMIT=$(git rev-parse prep/t07bbis-code-v1)` ; `git ls-remote origin
   refs/heads/prep/t07bbis-code-v1` = `$COMMIT` ; `git ls-remote --exit-code origin refs/heads/calcul/t07bbis-repetition-v1; echo
   $?` = **2**.
1. **Crédit** : `$L credit` → « CREDIT x USD : suffisant » (au moins 4 USD ; fichier privé, champ `credit` seul, supprimé).
2. **Offre** : `( umask 077; vastai search offers 'gpu_name=A100_SXM4 num_gpus=1 cpu_cores_effective>=16 cpu_ram>=128 disk_space>=60 reliability>0.98' -o 'dph_total' --raw > /tmp/repetition-recherche.json )` ;
   choisir l'identifiant (de préférence **≤ 1,15 USD/h** : budget de travail ≥ 100 min, la durée haute) ;
   `$L offre-depuis-recherche /tmp/repetition-recherche.json ID OFFRE.json` ;
   `P=$($PY -c 'import json; print(json.load(open("OFFRE.json"))["prix_usd_h"])')` ; `$L offre OFFRE.json ID "$P"` → « OFFRE
   ACCEPTEE ». Jamais retaper ni l'identifiant ni le prix.
3. **Échéance** : `DMAX=$($PY -c "import importlib.util as u; s = u.spec_from_file_location('r', 'scripts/repetition_carte_bbis_v1.py'); m = u.module_from_spec(s); s.loader.exec_module(m); print(int(m.duree_max_h($P) * 3600) - 300)")` ;
   `ECH=$(( $(date +%s) + DMAX ))` (5 min de création). Échéance et budget de travail (échéance − 15 min) : 1,09 USD/h → 123 et
   108 min ; 1,12 → 119 et 104 ; 1,15 → 116 et 101 ; 1,30 → 100 et 85 ; 1,40 → 91 et 76. Au-delà de 1,15 USD/h, la durée haute
   (≈ 100 min) ne tient pas : l'amorce coupe alors au budget (code 10) et pousse des traces partielles.
4. **Création** : `$L commande . OFFRE.json ID "$COMMIT" prep/t07bbis-code-v1 "$ECH" "$P" "<feu écrit>" <image> > /tmp/repetition-commande.txt`
   (refus : offre, feu sans GO, sans R-2802 ou sans l'image, `GH_TOKEN` absent, échéance au plafond ou au-delà, commit absent,
   amorce ou script autres) ; jouer la **dernière ligne** sous `umask 077`, sortie dans un fichier :
   `( umask 077; <dernière ligne> > CREATION.json )` ; `$PY scripts/repetition_carte_bbis_v1.py creation CREATION.json` →
   « INSTANCE N », écrit **dans la minute** au registre des dépenses. Sans `new_contract` lisible : `$L trouver CREATION.json`
   (une seule instance de l'étiquette), jamais deviner.
5. **Relecture** : `$L relire CREATION.json` → « INSTANCE CONFORME N » (A100 SXM4, prix ≤ 1,40, étiquette) ; sinon geste 9
   aussitôt. **Minuterie** : `vastai logs N | grep 'BBIS REPETITION'` : « minuterie lancée (PID …, échéance …), avant toute passe ».
   Une ligne « REFUS » (refus avant la minuterie : l'instance a demandé sa propre destruction) ou rien 15 min après « running » :
   geste 9.
6. **Dépense**, toutes les 15 minutes : `$L depense CUMUL "$P"` avec le cumul **de la répétition seule**, stockage compris ; refus →
   geste 9 aussitôt. **Arrêt dur de la mère à l'échéance − 5 min** : geste 9 quoi qu'il en soit.
7. **Suivi** (`vastai logs N`) : carte A100-SXM4-80GB ; dépôt au commit, motifs de la course, aucune entrée de 7b, script à
   l'empreinte attendue ; installation « code 0, N s (délai …) » ; essais « code 0, ligne de compte : 87 passed, 22 skipped … ;
   minimum de la course : 87 » ; « carte : code 0 » et son résumé (état reussie ; jetons ≈ 143 000 ; déterministe {linéaire :
   True, attention : True} ; médiane ; projeté ; écarts ≤ 10⁻⁴) ; « FIN : répétition menée au bout » ; « traces poussées … » ;
   « fin, code 0 ; instance laissée en marche, minuterie armée … ».
8. **Dans les 15 minutes qui suivent « fin, code N »** : lire `vastai logs N` **avant** toute destruction (traces non poussées :
   le journal n'existe que là) ; `git fetch origin calcul/t07bbis-repetition-v1` ; `git rev-parse FETCH_HEAD^` = `$COMMIT` ;
   `traces/bbis-t07-repetition-v1/` seulement ; lire `repetition-carte.json`.
9. **Destruction** : `$L detruire CREATION.json` (garde positive : `new_contract`, étiquette relue) ; jouer la ligne
   `GO_ID=GO-2026-11-14-09 vastai destroy instance N -y` ; puis `$L verifier-destruction CREATION.json 60480302` (ou 60670453) →
   « DESTRUCTION PROUVEE » ; sinon refaire destruction et vérification, compte rendu. **Aucune seconde création avant l'absence
   prouvée de la première.** Jamais 58936096, 58936099, 58936100, 60480302, 60599797, 60670453, 60671759.
10. **Consigner** : `$L credit` (après), dépense, arrêt (`registres/arrets.md`), résultats ; révoquer le jeton ; supprimer
    `CREATION.json`, `OFFRE.json` et la recherche une fois consignés (aucun ne porte de valeur privée : l'identifiant et le prix
    sont au registre).

**Codes réellement émis par l'amorce** (journal « ARRET : … », puis « fin, code N ») :

| code | sens |
|---|---|
| 0 | réussie |
| 2 | garde : carte autre qu'une A100 SXM4 80 Go, `GH_TOKEN` absent, outil absent, clonage, branche de sortie présente ou dépôt injoignable, MOTIFS de la course illisibles, entrée de 7b dans l'arbre, commit introuvable, tête ≠ COMMIT, empreinte du script, torch sans carte, compte ou minimum de la course illisibles, essais écrivant sous `src`/`tests`, garde de la partie carte |
| 4 | autre (code inattendu de la partie carte, poussée des traces impossible en fin) |
| 5 | installation au-delà de 60 min |
| 6 | installation en échec, environnement virtuel |
| 7 | essais en échec, ou moins de 87 passés |
| 8 | erreur d'apprentissage sur la carte (torch compris) |
| 9 | contrôle carte-processeur au-delà de 10⁻⁴, ou apprentissage non déterministe ; aussi une sonde en échec pendant le contrôle (mineur m-4) |
| 10 | échéance proche : travail coupé au budget (échéance − 15 min), traces poussées |
| — | **le code 3 n'est jamais émis** (mineur m-2) ; un **refus d'arguments avant la minuterie** écrit « BBIS REPETITION REFUS : … » dans les journaux de l'instance seulement (rien n'est poussé) et sort en 2 après avoir demandé la destruction de l'instance (mineur m-3) |

## 3. Ce qui reste en réserve

- **Minuterie et destruction par l'instance jamais jouées sur le service réel** (`DELETE` avec la clé de conteneur) : la butée
  du plafond repose sur l'arrêt dur de la mère à l'échéance − 5 min et sur la garde de dépense ; ne jamais compter sur elles.
- **Fin voulue sans « stopped »** : l'instance reste facturée (carte comprise) jusqu'au geste 9 ou à l'échéance ; borné par le
  plafond (calculé jusqu'à l'échéance), d'où la consigne des gestes 8 et 9 dans les 15 minutes.
- **Identifiant de l'instance illisible avant la minuterie**, ou mort brutale du processus principal (signal d'arrêt forcé,
  mémoire) : ni destruction par l'instance ni piège ; le conteneur s'arrête, l'instance reste listée (stockage) jusqu'au geste 9 :
  consigne du geste 5.
- **Formes des sorties de l'outil supposées** (`new_contract` ; clés `label`, `gpu_name`, `gpu_ram`, `dph_total` de `show
  instances` ; clés de la recherche ; `credit` de `show user`) : toute forme autre rend un **refus** (jamais un faux « prouvé » ni
  une offre devinée), donc au pire une répétition arrêtée avant ou un geste refait à la main. Le `dph_total` de la recherche
  peut ne pas compter le disque de 60 Go : la relecture du geste 5 lit celui de l'instance créée.
- **Jeton** (M3) : portée et révocation sont des consignes ; la liste des instances peut porter l'environnement : elle n'est jamais
  affichée, elle est scannée (alerte) et supprimée.
- **Poussée depuis un clone partiel** jamais jouée sur le service réel (m6) : lire `vastai logs` avant toute destruction.
- **Projection de la garde de débit** : formule de la course recopiée (constantes importées), médiane sur six apprentissages :
  un ordre de grandeur (M-3) ; le clone partiel rapatrie les commits et arbres de l'historique de la branche (noms de chemins),
  jamais ouverts (remarque 3a).
- **Pour la course** (décisions, aucun changement fait) : la liste `registre_bbis_v1.INSTANCES_D_AUTRES_SESSIONS` ne porte pas
  60671759 (l'ajouter change `MIN_ESSAIS`) ; la même garde d'identifiant en entiers ASCII serait à porter dans `registre_bbis_v1`
  (m1) ; l'image ne peut pas être épinglée par empreinte (`@` refusé par le filtre d'image, m2) ; `scripts/depot_expurge.py` doit
  ignorer la branche `calcul/t07bbis-repetition-v1` (non vérifié ici).

## 4. Empreintes (SHA-256, commit `1abc4364`) et décomptes

| fichier | empreinte |
|---|---|
| `scripts/repetition_carte_bbis_v1.py` | `e032499acd7b87e1a4f0bb94f21de1f7c18c05c426da82b69afd4be1ed0d729c` |
| `scripts/amorce_repetition_bbis_v1.sh` | `67172970fefdb66f5e14e8202b21aa099ab890226b1d264cc1cb427a99e38c1b` |
| `scripts/lancer_repetition_bbis_v1.sh` | `d61a11202f9c3ef4c57dc46795b8d57ce150a8272ef3a7574f19ef1a54403b1a` |
| `tests/test_repetition_bbis_v1.py` | `aaea8301462e3b98d29ad340f717d5ddc33e4e1258808dec305ead300c1bd67d` |

Essais : **132 passés** (109 de la course + 23 de la répétition, 13 de plus qu'en v4) ;
`brouillons/T0.7-etape-B-bis-v1/code/essais-sortie-repetition-carte-v2.txt`. La commande de création a été imprimée sur le vrai
commit `1abc4364` (essai, rien créé). Aucun refus de la garde d'isolement dans ce tour.

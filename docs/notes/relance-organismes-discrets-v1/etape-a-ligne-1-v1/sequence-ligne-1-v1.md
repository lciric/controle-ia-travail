# Ligne 1 de carte du bras A : séquence de la session, version 1

- **Date (UTC)** : 2026-11-23. Rédacteur : Claude Opus 5.5, agent délégué par la session du bras A. Écrite sur processeur seul : aucune dépense, aucune instance, aucune clé lue, aucun réseau hors git.
- **Objet** : la séquence que la session suit pour jouer la ligne 1 de carte du bras A : les 128 épisodes honnêtes du modèle de base sur les 16 tâches de fabrication (texte scellé, 6.3 (b)). La ligne est conduite **sous GO-2026-11-22-148**, avec un plafond de 18 USD (devis de la carte, version 5, ligne 1). Rien de cette note n'a été exécuté hors du processeur.
- **Pièces** (empreintes recalculées à l'écriture) :

| pièce | chemin | sha256 |
|---|---|---|
| texte scellé | `prereg/T0.7-organismes-discrets-v-a-v2.md` | `b4fbfb4e6cddfdc4775119a3e42a61045460ce8cee18a341834155ef1367a0cd` |
| lanceur (en contre-lecture finale) | `src/controle_ia/organismes_discrets/lanceur_bras_a_v7.py` | `82672d3aebbbf6ef1f56cea9c22384463e528a19bb39c59d03780132befdfb27` |
| configuration du lanceur, scellée | `prereg/T0.7-organismes-discrets-v-a-v2-config-lanceur-ligne-1-v1.json` | `aff9b5d8ddc29dd32e33c221057aa671b18ff1969641d2600be480269b3d35aa` |
| plan des tâches de l'étape (a), scellé | `docs/notes/relance-organismes-discrets-v1/etape-a-ligne-1-v1/plan-des-taches-v1.json` | `bfb0752bd19c0f8ed2430023821f3388d4baea0009f036c15e6a28ee1563b19b` |
| programme de la course sur l'instance | `scripts/course_ligne_1_bras_a_v1.py` | compagnon `.sha256` |
| programme de la liste blanche | `scripts/liste_blanche_ligne_1_bras_a_v1.py` | compagnon `.sha256` |
| essais des deux programmes | `tests/test_course_ligne_1_bras_a_v1.py` | compagnon `.sha256` |
| devis de la carte, version 5 (lu par `git show 06416a69a:…`, branche `origin/relance-bras-a/devis-carte-v3`) | `docs/notes/relance-organismes-discrets-v1/devis-bras-a-v5.md` | `40b999f825361ba94a45464921022ce74175733bd29b4fd98671269f7bb745f5` |

**Si le lanceur change** (une version 8 après la contre-lecture finale) : la configuration est réécrite sous un nom neuf (`…-config-lanceur-ligne-1-v2.json`), avec le chemin et l'empreinte de la v8, puis scellée. Le plan des tâches est refait et scellé sous un nom neuf : il cite l'empreinte de la configuration. Le programme de la course ne change pas : il reçoit le lanceur par `--lanceur-chemin` et `--lanceur-sha256`. La liste blanche est recalculée par son programme.

## 0. Ce qui est fait à l'étape (a) par cette livraison

1. **Configuration du lanceur** : les sept clés de `CLES_DE_LA_CONFIGURATION`. Le lanceur est désigné par son chemin et son empreinte (v7). Le texte est désigné par son chemin et `b4fbfb4e…`. La configuration de référence est `b7a5c1ba…`. L'entropie vaut **89450145880220938582573338461458398609** : c'est l'entier de 13.1, case « entropie » (vérifié dans le texte scellé). `entropie_fictive` vaut `false`. Les réglages de l'instrument sont les options retenues, écrites en toutes lettres, et la ligne 1 porte 18 USD et 2 USD. Elle passe `lire_la_configuration(chemin, ".")` au départ réel (`essai=False`), et elle est scellée.
2. **Coupes des tâches et contrôle de séparation sur l'entropie réelle** (6.3 (a)) : `plan_des_taches` puis `graines_de_la_course`. Résultat : 16 tâches de fabrication (8 ouvertes, 8 gardées) et 16 de vérification. Le contrôle de séparation contre les 64 tâches d'évaluation est passé. Les 269 clés de graines sont écrites (sans leurs valeurs), avec l'empreinte de l'objet des graines. Le tout est dans le plan scellé. Tout tourne sur processeur ; `torch` est chargé seulement à l'import du module des tâches (`environnements.pilote_a`), et rien n'est joué.
3. **Programme de la course** et ses essais : voir la section 3.

## 1. Relevé du tarif du jour (session ; clé lue par son nom, jamais affichée)

La carte est celle du devis : **A100 SXM4 80 Go**, une seule. La configuration de référence fixe les bornes de l'offre : mémoire de la carte ≥ 80 000 Mo, mémoire vive ≥ 128 000 Mo, au moins 16 cœurs effectifs, disque ≥ 150 Go. Elle borne aussi les prix : carte ≤ 1,30 USD par heure, stockage ≤ 0,08 USD par heure, téléchargement ≤ 0,05 USD par Go. La roue de torch 2.14.1 vise CUDA 13.0 (`requirements-gpu.txt`), il faut donc une offre dont la version CUDA maximale est d'au moins 13.0.

Commande, **non exécutée ici** :

```
curl -sS -G "https://console.vast.ai/api/v0/bundles/" \
  -H "Authorization: Bearer ${VAST_API_KEY}" \
  --data-urlencode 'q={"gpu_name":{"eq":"A100 SXM4"},"num_gpus":{"eq":1},"gpu_ram":{"gte":80000},
     "cpu_ram":{"gte":128000},"cpu_cores_effective":{"gte":16},"disk_space":{"gte":150},
     "cuda_max_good":{"gte":13.0},"rentable":{"eq":true},"verified":{"eq":true},"rented":{"eq":false},
     "type":"on-demand","order":[["dph_total","asc"]],"limit":20}' \
  > releve-offres-$(date -u +%Y%m%dT%H%M%SZ).json
```

Ce qu'on retient de l'offre choisie, à consigner dans le registre des dépenses avec l'heure du relevé (`date -u +%Y-%m-%dT%H:%M:%SZ`) :
- `carte_usd_h` = `dph_base` (prix de la carte seule) ;
- `stockage_usd_h` = `storage_cost` × 150 Go ÷ 720 (`storage_cost` est en USD par Go et par mois) ;
- `telechargement_usd_go` = `inet_down_cost` ;
- le pilote de l'hôte (`driver_version`) et `cuda_max_good`, plus l'identifiant de l'offre.

Si l'un des trois prix dépasse sa borne, **on ne part pas** (8.1 ; le constat le refuse).

## 2. Constat de départ (session, avant la création, le même jour UTC que le relevé)

```
PYTHONPATH=src .venv/bin/python -m controle_ia.organismes_discrets.lanceur_bras_a_v7 \
  --configuration prereg/T0.7-organismes-discrets-v-a-v2-config-lanceur-ligne-1-v1.json \
  --go GO-2026-11-22-148 --registre-go registres/go.md --credit-lu-usd <crédit lu> \
  --tarif-carte-usd-h <dph_base> --tarif-stockage-usd-h <stockage> --tarif-telechargement-usd-go <inet_down_cost> \
  --date-du-releve-utc <AAAA-MM-JJTHH:MM:SSZ du relevé> > constat-ligne-1.json
```

- Le crédit est celui du compte Vast.ai, lu par la session (`vastai show user`). Il doit atteindre au moins **20 USD** (18 + 2), sinon le constat refuse.
- Le relevé doit dater du même jour UTC que le constat, et lui être antérieur. Si le relevé est fait avant minuit et le constat après, il faut refaire le relevé.
- Le constat ne doit être ni réécrit ni retouché : son empreinte est recontrôlée sur l'instance (M-2).
- Le constat est versé avec les sorties (section 6).

## 3. Programme de la course et essais (ce qui a tourné ici)

`scripts/course_ligne_1_bras_a_v1.py` (docstring complète dans le fichier) suit cet ordre :
1. il vérifie le lanceur (chemin, empreinte, fichier importé) ;
2. il lit la configuration (départ réel), puis le constat ;
3. il construit le compteur du plafond, puis recontrôle le constat avec ce compteur **avant de charger le modèle** ;
4. il refait le plan et le confronte au plan scellé ;
5. il charge les graines, le guide et le modèle réel ;
6. il appelle `jouer_ligne_1` vers `<dossier>/episodes/`, puis écrit `<dossier>/manifeste-de-la-ligne-1.json` et `<dossier>/journal-course-ligne-1.txt`.

Le compteur du plafond se règle ainsi :
- plafond : 18 USD (celui du constat) ;
- taux : carte + stockage relevés ;
- départ : l'heure de création de l'instance ;
- frais fixes : téléchargement relevé × 40 Go (configuration de référence, `telechargement_go_prevu`), soit 2 USD au plus.

Une heure de création antérieure au constat, ou postérieure à l'horloge, est refusée.

Codes de sortie :
- **0** : la ligne est jouée ;
- **2** : refus avant tout jeu ;
- **3** : arrêt pendant le jeu (plafond, coupe A14, autre garde ou exception). Ce qui est joué reste écrit, et le manifeste porte l'arrêt.

Le programme ne supprime rien et n'écrase rien : il refuse un dossier qui existe déjà.

**Garde du mode.** Le mode `reel` n'admet que le texte `b4fbfb4e…`. Le mode `jouet` le refuse. Une sortie du modèle jouet ne peut donc jamais être produite sous la vraie configuration.

**Essais** (`tests/test_course_ligne_1_bras_a_v1.py`, sur processeur). Le dossier temporaire est rempli **par la liste blanche seule**. Le programme y tourne dans un processus à part, dont le chemin d'import ne voit que ce dossier : cela éprouve que la liste blanche suffit. Comme dans les essais de la v7, la configuration est déclarée réelle, sur un texte fictif à entropie fictive.
- Course entière sur le modèle jouet : 128 épisodes, manifeste, versement scellé, puis destruction simulée (après le manifeste). Elle n'est jouée que sous `COURSE_LIGNE_1_ESSAI_LONG=1`. **Jouée le 2026-11-23 de 00:52 à 01:14Z : passée** (code 0 ; 128 épisodes en 1 304 s ; 9 actions coupées sur 1 280 ; manifeste écrit ; versement scellé ; destruction simulée après lui ; 21 min 51 s en tout, dont une partie sous charge d'un autre essai).
- Toujours joués (26 passent, environ 7 min 40 s : chaque essai à part importe torch) :
  - arrêt au plafond après au plus un lot, de bout en bout (code 3, arrêt au manifeste, versement scellé) ;
  - sept refus avant jeu : empreinte du lanceur, autre lanceur, commit, création antérieure au constat, création postérieure à l'horloge, heure illisible, mode réel sur un texte non scellé ;
  - constat altéré ;
  - plan différent du plan scellé ;
  - dossier existant ;
  - mode jouet sous le texte réel ;
  - guide explicite ;
  - compteur nourri du constat ;
  - liste blanche de la vraie configuration ;
  - neuf chemins cloisonnés reconnus, et une liste qui en contient un refusée ;
  - imports placés dans des fonctions, et imports relatifs.

## 4. Création de l'instance (session, sous la garde de calcul)

La garde (`.claude/hooks/garde_calcul.py`, `4fae077c…`, égale à `origin/main`) ne laisse passer une commande de lancement (`vastai create|launch|start`) que si elle cite un identifiant de GO valide au registre. Cet identifiant doit être de type « calcul », accordé par Lazar, en cours de validité et non révoqué ; le rang peut avoir deux ou trois chiffres. **Une création par `curl` sur l'interface de programmation n'est pas vue par la garde : elle est donc exclue.** On utilise la ligne de commande :

```
GO_ID=GO-2026-11-22-148 vastai create instance <identifiant de l'offre> \
  --image pytorch/pytorch:<version CUDA ≥ 13.0, à relever> --disk 150 --ssh --direct \
  --label bras-a-ligne-1
```

Remarques sur cette commande :
- Elle ne porte **aucune clé**. La clé du hub des modèles (`HF_TOKEN`) n'est posée qu'au moment du téléchargement (section 5), par une variable d'environnement de la commande distante, sans jamais être écrite ni affichée.
- L'heure de création UTC est relevée aussitôt (`vastai show instance <id> --raw`, champ `start_date`, ou `date -u` à la création) : elle part dans `--creation-instance-utc`.
- L'identifiant d'instance (chiffres seuls) est consigné tout de suite, au registre des dépenses et dans l'état.

## 5. Mise en place sur l'instance, par liste blanche de fichiers nommés

**Jamais `git clone` du dépôt entier, ni `cp -r` de `src/`.** Le dépôt contient des chemins cloisonnés.

1. Les fichiers posés doivent être ceux d'un commit poussé : `git diff --quiet HEAD -- <liste>`, et `COMMIT=$(git rev-parse HEAD)`.
2. Calculer la liste par programme et la confronter au cloisonnement :
   ```
   PYTHONPATH=src .venv/bin/python scripts/liste_blanche_ligne_1_bras_a_v1.py \
     --configuration prereg/T0.7-organismes-discrets-v-a-v2-config-lanceur-ligne-1-v1.json \
     --lanceur-chemin src/controle_ia/organismes_discrets/lanceur_bras_a_v7.py \
     --plan-scelle docs/notes/relance-organismes-discrets-v1/etape-a-ligne-1-v1/plan-des-taches-v1.json \
     --guide <aucun|H1-classification> > liste-blanche.json
   ```
   Le programme lit l'arbre syntaxique de chaque module du paquet, imports placés dans les fonctions compris. Le lanceur importé par son nom y est ajouté par son chemin. Chaque chemin est confronté à `cloisonnement_bras_a_v14.est_cloisonne` et aux chemins cloisonnés de la session ; un seul chemin cloisonné arrête.
3. Ajouter à la main `requirements-gpu.txt`, `requirements-cpu.txt` et `requirements-donnees.txt` (installation), ainsi que `constat-ligne-1.json`.
4. Écrire les empreintes : `sha256sum $(fichiers) > empreintes-posees.txt`.
5. Faire l'archive par liste explicite : `tar -cf ligne-1.tar -T fichiers.txt empreintes-posees.txt` (fichiers seuls, aucun dossier).
6. L'envoyer par `scp -P <port> ligne-1.tar root@<hôte>:/root/ligne-1/`.
7. Sur l'instance : `tar -xf`, puis `sha256sum -c empreintes-posees.txt`, qui doit être entièrement conforme.
8. Installer : `python3 -m venv .venv && . .venv/bin/activate && pip install -r requirements-gpu.txt`. Le manifeste consigne les versions.
9. Vérifier la carte : `python -c "import torch; print(torch.cuda.is_available(), torch.version.cuda)"`.
10. Télécharger le modèle de la configuration de référence (`meta-llama/Llama-3.1-8B-Instruct`, révision `0e9e39f249a16976918f6564b8830bc894c89659`, environ 16 Go en safetensors) par `harnais.modeles.precharger_modele`. On le fait sous `HF_TOKEN` passé dans la seule commande distante, et lu par son nom.

**Liste blanche calculée ici** (guide « aucun » ; 48 fichiers, plus les trois fichiers de dépendances et le constat) :

- programme : `scripts/course_ligne_1_bras_a_v1.py` ;
- modules (35) : `src/controle_ia/__init__.py`, `gardes.py`, `manifeste.py`, `prereg.py`, `scellement.py` ;
  - `environnements/` : `__init__.py`, `invites.py`, `juges.py`, `pilote_a.py`, `propositions.py`, `rubrique.py` ;
  - `harnais/` : `__init__.py`, `activations.py`, `episode.py`, `formats.py`, `modeles.py` ;
  - `organismes/` : `__init__.py`, `distillation.py`, `lora.py` ;
  - `organismes_discrets/` : `__init__.py`, `epreuves_couverture_bras_a_v4.py`, `fabrication_v3.py`, `graines_bras_a_v4.py`, `instrument_appariement_v4.py`, `lanceur_bras_a_v2.py`, `lanceur_bras_a_v7.py`, `lots_bras_a_v6.py`, `reponses_lecteurs_v5.py` ;
  - `premier_test_ia/` : `__init__.py`, `conditions.py` ;
  - `t06/` : `__init__.py`, `distillation_transcription.py`, `identite.py` ;
  - `verite_dommage/` : `__init__.py`, `artefacts_v1.py` ;
- données (chacune avec son compagnon `.sha256`) : la configuration du lanceur, le texte scellé, `prereg/T0.6-organismes-config-7b-v1.json`, `donnees/20261007-082440-t05-extraction/taches-entrainement.json` et `…/taches-evaluation.json`, et le plan scellé.

Aucun de ces chemins n'est cloisonné. Aucun module de sondes, de bases, de lecture, ni du côté habilité.

**Guide de classification : à trancher avant le départ (règle non écrite).** Les 32 tâches de réserve portent toutes une classification. L'environnement honnête y ajoute le guide de classification si on le lui passe (`EnvironnementPropositions(…, guide_classification)`). Les lanceurs de T0.6 et le pilote passaient `charger_invite("H1-classification")`. Les essais du lanceur v7 passent `None`. Le texte scellé n'en dit rien, et ce choix change le contexte de chaque épisode, donc les épisodes. Le contexte reconstruit à l'étape (c) devra reprendre **le même** guide.

Le programme exige `--guide` et porte son empreinte au manifeste. Si `H1-classification` est retenu, les fichiers du guide (`docs/sources/invites-2606.08892-v1/index.json`, l'invite et leurs compagnons) doivent rejoindre la liste blanche. Ce chemin est cloisonné pour moi : je ne l'ai ni ouvert ni listé, et le programme de la liste blanche le déclare manquant. **Recommandation : `H1-classification`**, confiance moyenne : c'est la continuité avec l'organisme précédent, dont viennent la configuration de référence et les débits du devis. C'est à décider par la session, et à soumettre à Lazar si elle y voit une lecture du texte.

## 6. Lancement, surveillance, rapatriement

**Lancement sur l'instance**, en tâche détachée, sortie dans un fichier :

```
cd /root/ligne-1 && . .venv/bin/activate && PYTHONPATH=src nohup python scripts/course_ligne_1_bras_a_v1.py \
  --configuration prereg/T0.7-organismes-discrets-v-a-v2-config-lanceur-ligne-1-v1.json \
  --lanceur-chemin src/controle_ia/organismes_discrets/lanceur_bras_a_v7.py \
  --lanceur-sha256 82672d3aebbbf6ef1f56cea9c22384463e528a19bb39c59d03780132befdfb27 \
  --constat constat-ligne-1.json \
  --plan-scelle docs/notes/relance-organismes-discrets-v1/etape-a-ligne-1-v1/plan-des-taches-v1.json \
  --creation-instance-utc <heure de création> --dossier /root/sorties-ligne-1 --commit "$COMMIT" \
  --guide <choix> --mode reel --hors-ligne > /root/course.out 2>&1 &
```

- **Surveillance par la session** : le journal se lit par `ssh … tail`. Le compteur arrête la ligne entre deux lots dès que le cumul dépasse 18 USD. La session tient en plus une **échéance** : création + 6 h, soit environ deux fois le haut de l'attendu. Passé ce délai sans ligne « FIN », elle rapatrie ce qui existe, puis détruit l'instance (8.5).
- **Rapatriement** :
  - nom du dossier local : `la.nom_du_dossier_de_versement("ligne-1", "fini" | "arret", <heure UTC>)`, soit `diag/organismes-discrets-v-a-v2/ligne-1-<état>-<AAAAMMJJTHHMMSSZ>/` ;
  - `scp -r -P <port> root@<hôte>:/root/sorties-ligne-1/. <dossier local>` ;
  - on y ajoute `course.out`, `constat-ligne-1.json` et `empreintes-posees.txt` ;
  - on compare les tailles et empreintes du côté instance (`sha256sum` distant) à celles du côté local.

## 7. Versement scellé, destruction, consignation

```
PYTHONPATH=src .venv/bin/python - <<'FIN'
import json, subprocess
from pathlib import Path
from controle_ia.organismes_discrets import lanceur_bras_a_v7 as la
d = Path("diag/organismes-discrets-v-a-v2/ligne-1-<état>-<date>")
m = json.loads((d / "manifeste-de-la-ligne-1.json").read_text(encoding="utf-8"))
print(la.sceller_le_versement(d, m, manquants=[]))        # ce qui manque : {"nom": …, "pourquoi": …}
print(la.detruire_l_instance("<identifiant>", d,
      lambda i: subprocess.run(["vastai", "destroy", "instance", i], capture_output=True, text=True).stdout))
FIN
```

- Si l'instance est perdue, ou si le manifeste de la ligne manque, on scelle avec la liste `manquants` qui dit quoi et pourquoi. La destruction n'est jamais faite avant le manifeste du versement scellé (garde de 8.4, ligne 1195).
- Après la destruction, `vastai show instances` doit montrer que l'instance n'y est plus. On consigne ensuite :
  - `registres/arrets.md` : identifiant, heure, motif « fin de ligne » ou l'arrêt ;
  - `registres/depenses.md` : durée et coût lus au compte ;
  - `registres/etat.md`, puis commit et poussée du versement.
- **Récupérer n'est pas lire** : les épisodes versés ne sont ouverts que par l'étape (c), fabrication par programme.

## 8. Durée et coût estimés (devis v5, section 4 ; rien de neuf)

| poste | estimation |
|---|---|
| 128 épisodes × 40,2 à 42,8 s | 1,43 à 1,52 h |
| mise en route (installation, téléchargement d'environ 16 Go, chargement) | 1,0 h (supposée au devis) |
| **total** | **2,43 à 2,52 h** |
| attendu | ≈ 3,9 à 5,3 USD (calcul 2,87 à 3,28 USD, téléchargement 1 à 2 USD) |
| pire cas (débit deux fois plus lent, une relance complète) | 17,92 USD ; plafond 18 USD |
| compteur sur l'instance | au tarif plafond de 1,38 USD par heure et 2 USD de frais fixes, il arrête après environ 11,6 h d'instance |

Quant au débit du jouet : sur ce processeur, un lot de huit épisodes du modèle jouet prend environ 50 s. Cela ne dit rien du débit sur la carte.

## 9. Ce qui manque ou bloque avant le départ

1. **Contre-lecture finale du lanceur v7.** Si elle demande une v8 : configuration et plan neufs (voir en tête).
2. **Guide de classification** : choix à faire (section 5). S'il est retenu, ses fichiers doivent rejoindre la liste blanche, par une session qui peut ouvrir `docs/sources/`.
3. **Autres cases de 13.2 « avant toute dépense »**, hors de ce travail : selon la lecture du devis (section 8), la ligne de GO de la ligne 1 et les pièces que le devis liste. Je n'ai pas vérifié leur état : le registre est hors de mon cloisonnement.
4. **Inscription de la configuration** au registre (`CONFIG-BRAS-A-V2`, 6.3 (a)) : elle relève de la session.
5. **Image de l'instance** (version CUDA ≥ 13.0) et **clé du hub des modèles** : elles relèvent de la session.
6. **Durée des essais** : les essais toujours joués ajoutent environ 7 à 8 minutes à la suite, car chaque processus à part importe torch.

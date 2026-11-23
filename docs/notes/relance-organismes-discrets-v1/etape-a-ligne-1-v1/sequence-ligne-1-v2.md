# Ligne 1 de carte du bras A : séquence de la session, version 2

- **Date (UTC)** : 2026-11-23. Rédacteur : Claude Opus 5.5, agent délégué par la session du bras A. Écrite sur processeur seul : aucune dépense, aucune instance, aucune clé lue, aucun réseau hors git. Rien de cette note n'a été exécuté hors du processeur.
- **Objet** : la séquence que la session suit pour jouer la ligne 1 de carte du bras A : les 128 épisodes honnêtes du modèle de base sur les 16 tâches de fabrication (texte scellé, 6.3 (b)), sous la ligne de GO de la ligne 1 (GO-2026-11-22-148), plafond 18 USD (devis de la carte, version 5, ligne 1).
- **Ce qui change depuis la version 1** (`sequence-ligne-1-v1.md`, qui reste telle quelle) :
  1. **le guide d'invite de l'agent dans les épisodes honnêtes est « H1-classification »** : décision de la chaîne de décision (session mère, étage 3) ; le texte scellé est muet ; le choix est consigné et rapporté. Il est porté par la configuration (clé `guide`), d'où un **lanceur v8**, une **configuration v2**, un **plan des tâches v2**, un **programme de la course v2** (plus d'argument `--guide`) et une **liste blanche v2** (qui ajoute les fichiers du guide à leurs empreintes données) ;
  2. les corrections de la contre-lecture de la préparation v1 (`contre-lecture-preparation-ligne-1-v1.md`, `83ec85866c0ee785abae8190088aa04bbdecf0ee53444725d615be1079921ccd`) : D1, D2, m1 à m5, et les précisions sur 8.5 (sections 3, 4, 6 et 7 ci-dessous) ;
  3. la règle écrite pour la ligne 2 (section 10).

## Pièces

| pièce | chemin | sha256 |
|---|---|---|
| texte scellé | `prereg/T0.7-organismes-discrets-v-a-v2.md` | `b4fbfb4e6cddfdc4775119a3e42a61045460ce8cee18a341834155ef1367a0cd` |
| lanceur, version 8 | `src/controle_ia/organismes_discrets/lanceur_bras_a_v8.py` | `2663d32d39133ab1a96cb7a694baf7908c005c37e835d9f17cff2d578bc6344b` |
| différence du lanceur v7 à v8 | `docs/notes/relance-organismes-discrets-v1/difference-lanceur-v7-v8-v1.diff` | compagnon `.sha256` |
| configuration du lanceur, version 2, scellée | `prereg/T0.7-organismes-discrets-v-a-v2-config-lanceur-ligne-1-v2.json` | `2a17e067fabd590d9d8469f6fa85c72860410ef6fc65c787fcf3f06a3831baff` |
| plan des tâches de l'étape (a), version 2, scellé | `docs/notes/relance-organismes-discrets-v1/etape-a-ligne-1-v1/plan-des-taches-v2.json` | `7cc3d4a4354e61dfd72de0f1e62b4301c7bff7d4be640b889a26205fc5c4625e` |
| guide « H1-classification », invite (empreinte donnée, non lue ici) | `docs/sources/invites-2606.08892-v1/invites/H1-classification.txt` | `69d50fb972f3255c94430205ab09c4f21054185d7def25b061c7255d71cc5540` |
| guide, index des invites (empreinte donnée, non lue ici) | `docs/sources/invites-2606.08892-v1/index.json` | `adb4b8bca7788baf2c4714df96dcdcc2c5043e8f1943542d0fbe1863491ae2d9` |
| programme de la course sur l'instance, version 2 | `scripts/course_ligne_1_bras_a_v2.py` | compagnon `.sha256` |
| programme de la liste blanche, version 2 | `scripts/liste_blanche_ligne_1_bras_a_v2.py` | compagnon `.sha256` |
| essais du lanceur v8 | `tests/test_lanceur_bras_a_v8.py` | compagnon `.sha256` |
| essais des deux programmes v2 | `tests/test_course_ligne_1_bras_a_v2.py` | compagnon `.sha256` |
| devis de la carte, version 5 (lu par `git show 06416a69a:…`) | `docs/notes/relance-organismes-discrets-v1/devis-bras-a-v5.md` | `40b999f825361ba94a45464921022ce74175733bd29b4fd98671269f7bb745f5` |

Le lanceur v8 ne diffère de la v7 (`82672d3a…`, contre-lu « bon pour le départ ») que par : la clé `guide` dans `CLES_DE_LA_CONFIGURATION` (clés fermées `identifiant`, `fichier`, `sha256`, `index`, `index_sha256` ; identifiant exigé égal à « H1-classification » ; chemins et empreintes exigés égaux aux constantes du module), contrôlée à la lecture de la configuration **sans toucher aux fichiers** ; la fonction à part `verifier_les_octets_du_guide` (empreinte sur disque des deux fichiers), appelée par le programme de l'instance avant de charger le guide ; `CHEMIN_DU_LANCEUR` ; l'en-tête. La différence entière est scellée dans le fichier `.diff` ci-dessus. **Le lanceur v8 demande une contre-lecture avant le départ**, comme la v7 (section 9).

## 0. Ce qui est fait à l'étape (a) par cette livraison

1. **Configuration v2** : la v1 (`aff9b5d8…`) plus le lanceur v8 (chemin et empreinte) et la clé `guide`. Elle passe `lanceur_bras_a_v8.lire_la_configuration(chemin, ".")` au départ réel (`essai=False`), et elle est scellée.
2. **Plan des tâches v2** : refait sous la configuration v2 (le programme de la course exige que le plan scellé cite l'empreinte de la configuration jouée). Il est **identique** au plan v1 (`bfb0752b…`) pour les 16 tâches de fabrication, les 16 de vérification, les 8 ouvertes, les 8 gardées, les 269 clés de graines et l'empreinte des graines (`c378316e…`, forme : `json.dumps(graines, sort_keys=True)` en UTF-8, puis sha256 — la forme que la contre-lecture n'avait pas pu refaire). Il cite le plan v1 et son empreinte.

## 1. Relevé du tarif du jour (session ; clé lue par son nom, jamais affichée)

Inchangé (version 1, section 1) : une A100 SXM4 80 Go ; bornes de l'offre et des prix de la configuration de référence ; CUDA maximale ≥ 13.0 ; `carte_usd_h` = `dph_base`, `stockage_usd_h` = `storage_cost` × 150 ÷ 720, `telechargement_usd_go` = `inet_down_cost` ; le pilote de l'hôte (`driver_version`), `cuda_max_good` et l'identifiant de l'offre sont consignés. Un prix au-dessus de sa borne : on ne part pas.

## 2. Constat de départ (session, avant la création, le même jour UTC que le relevé)

```
PYTHONPATH=src .venv/bin/python -m controle_ia.organismes_discrets.lanceur_bras_a_v8 \
  --configuration prereg/T0.7-organismes-discrets-v-a-v2-config-lanceur-ligne-1-v2.json \
  --go <identifiant du GO de la ligne 1> --registre-go registres/go.md --credit-lu-usd <crédit lu> \
  --tarif-carte-usd-h <dph_base> --tarif-stockage-usd-h <stockage> --tarif-telechargement-usd-go <inet_down_cost> \
  --date-du-releve-utc <AAAA-MM-JJTHH:MM:SSZ du relevé> > constat-ligne-1.json
```

Crédit ≥ 20 USD ; relevé du même jour UTC que le constat et antérieur à lui ; constat jamais retouché (son empreinte est recontrôlée sur l'instance) ; versé avec les sorties.

## 3. Programme de la course v2 et essais (ce qui a tourné ici)

`scripts/course_ligne_1_bras_a_v2.py` suit cet ordre :
1. il vérifie le lanceur (chemin, empreinte, fichier importé) ;
2. il lit la configuration (départ réel ; la clé `guide` y est contrôlée sans toucher aux fichiers), puis le constat ;
3. il construit le compteur du plafond, puis recontrôle le constat avec ce compteur ;
4. il refait le plan et le confronte au plan scellé ; il refait les graines ;
5. **guide** : il vérifie les octets des deux fichiers du guide à leurs empreintes (`verifier_les_octets_du_guide`) ; tout écart, fichier absent ou lien symbolique est un refus avant tout jeu (code 2) ; puis il charge le guide par la fonction du dépôt (`environnements.invites.charger_invite`, sous le dossier de l'index, qui revérifie les compagnons et l'entrée de l'index), confronte l'entrée de l'index (fichier et empreinte) et l'empreinte chargée à la configuration ; toute erreur de lecture devient un refus dit ;
6. **déterminisme (D2)** : `harnais.modeles.regler_determinisme(fils, "cuda")` (un fil, selon la configuration de référence) avant tout chargement : algorithmes déterministes, TF32 coupé, espace de travail cuBLAS fixé, cuDNN déterministe ; son retour (carte `torch.cuda.get_device_name`, capacité, CUDA, cuDNN, pilote, réglages relus) est écrit au journal et versé au manifeste (`resume.determinisme`) ;
7. **compteur relevé et gardé avant et après le chargement du modèle (m3)** ; un plafond franchi là est un refus avant jeu ;
8. il charge le modèle réel, appelle `jouer_ligne_1` avec le texte du guide vers `<dossier>/episodes/`, puis écrit le manifeste de la ligne (le guide entier, avec l'empreinte chargée, y figure) et le journal.

**D1** : toute exception, et non la seule garde, est dite au journal avec sa trace et une ligne « FIN » ; le code est 2 avant tout jeu, 3 pendant le jeu, jamais 1. Codes : **0** ligne jouée ; **2** refus avant tout jeu ; **3** arrêt pendant le jeu (plafond, coupe à 20 %, autre garde ou exception), ce qui est joué restant écrit et le manifeste portant l'arrêt.

**Essais** (sur processeur ; rien n'est lu sous `docs/sources/`) :
- `tests/test_lanceur_bras_a_v8.py` : les essais de la v7 portés (configuration augmentée du guide), plus le guide : constantes ; configuration avec le guide lue sans toucher aux fichiers ; configuration réelle v2 ; douze artefacts de la clé (identifiant « aucun » ou autre, chemin de l'invite, chemin de l'index, chacune des deux empreintes, empreinte en majuscules ou tronquée, clé en trop, clé manquante, guide qui n'est pas un objet) ; configuration sans guide ; clé en trop à la racine ; et la vérification des octets **sur des fichiers de guide fictifs en dossier temporaire** : sain, invite altérée, index altéré, fichier absent (deux cas), lien symbolique, guide autre que les constantes, vrai guide absent ; enfin, la lecture de la configuration n'appelle pas la vérification des octets. Résultat : **194 passent** (2 min 40 s).
- `tests/test_course_ligne_1_bras_a_v2.py` : dossier rempli par la liste blanche seule, plus un **guide fictif, déclaré tel** (son texte le dit), dont les chemins et empreintes fictifs sont **injectés par l'essai** à la place des constantes du lanceur (en processus par remplacement ; dans un processus à part par un petit programme d'amorce hors du dossier posé, qui remplace les constantes en mémoire puis joue la course ; le fichier du lanceur, donc son empreinte, ne change pas). Toujours joués : arrêt au plafond de bout en bout (guide et déterminisme au manifeste) ; sept refus avant jeu, chacun avec « FIN » ; vrai guide absent du dossier (refus par les octets, avant le déterminisme et le modèle) ; guide fictif sans injection (refusé par le lanceur) ; dossier existant ; `--guide` refusé par la course et par la liste ; chargement du guide sain, octets altérés, index altéré, compagnon absent, index qui nomme un autre fichier, lien symbolique ; **D1** avant le jeu (`OSError` au chargement : code 2, trace, « FIN ») et pendant le jeu (`RuntimeError` : code 3, manifeste partiel) ; **m4** coupe à 20 % côté course (`ArretCoupe` au quatrième lot, code 3, quatre lots écrits, le guide passé est bien le guide fictif) ; **m3** plafond franchi au relevé d'avant le chargement (refus, modèle non chargé) ; **D2** refus du réglage sur carte absente ; liste blanche (voir section 5). Résultat : **38 passent, 1 sauté** (le rejeu long), 3 min 02 s.
- **Rejeu de bout en bout sur le modèle jouet avec le guide fictif** (`COURSE_LIGNE_1_ESSAI_LONG=1`), joué une fois : **passé**, le 2026-11-23 de 01:43:00 à 02:35:17Z : code 0 ; 128 épisodes en 3 128 s (≈ 196 s par lot de huit, un seul fil sur ce processeur à quatre cœurs, sous le réglage du déterminisme ; la v1, sans ce réglage, jouait ≈ 50 s par lot) ; 9 actions coupées sur 1 280 (0,70 %) ; journal : guide fictif chargé après vérification des octets (`af1a8a40…`, index `fc796d50…`, empreintes fictives de l'essai), « déterminisme réglé (cpu, 1 fil) » ; manifeste écrit (guide et déterminisme au résumé) ; versement scellé ; destruction simulée après lui ; 3 136 s en tout. Une première tentative, lancée à 01:30Z, a été arrêtée par moi par ses PID après trois lots : au rythme d'un fil, elle aurait dépassé le délai de 50 min que l'essai donnait au processus à part ; le délai de l'essai long a été porté à 2 h, puis l'essai rejoué en entier (rien de la première tentative n'est gardé ni lu).

## 4. Création de l'instance (session, sous la garde de calcul)

Inchangé quant à la commande (version 1, section 4 : ligne de commande `vastai` sous `GO_ID=` l'identifiant de la ligne 1 ; jamais `curl` pour créer ; aucune clé dans la commande). **Piège de la garde** : elle prend pour un lancement toute commande qui cite à la fois un identifiant de GO et une création d'instance ; ne jamais écrire de note, de journal ni de registre par une commande qui cite les deux (écrire ces textes avec l'outil d'écriture de fichiers).

Ajouts :
- **m1, même jour UTC** : la création doit tomber le **même jour UTC** que le constat (donc que le relevé du tarif). Si minuit UTC passe entre le constat et la création, on ne crée pas : nouveau relevé, nouveau constat.
- **Heure de création** : l'identifiant (chiffres seuls) est consigné aussitôt ; `vastai show instance <identifiant> --raw` donne `start_date` en secondes depuis 1970 ; conversion écrite, arrondie vers le bas (le compteur compte alors un peu plus, jamais moins) :
  ```
  python3 -c "import datetime,sys; print(datetime.datetime.fromtimestamp(int(float(sys.argv[1])), datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'))" <start_date>
  ```
  La valeur part dans `--creation-instance-utc`. Si `start_date` est absent ou nul, on prend `date -u +%Y-%m-%dT%H:%M:%SZ` relevé **juste avant** la commande de création (antérieur à la création, donc prudent).
- **m2, prix réel** : dans la même lecture `--raw`, relire `dph_total` (prix horaire réel de l'instance créée, carte et stockage) et le comparer au taux du constat (`carte_usd_h` + `stockage_usd_h`). **Si `dph_total` dépasse ce taux** (le compteur sous-compterait), **destruction immédiate par l'identifiant** (`vastai destroy instance <identifiant>`, R10), avant toute pose de fichier : aucune sortie n'existe encore, il n'y a rien à verser ; on relit `vastai show instances` pour voir l'instance partie ; on consigne au registre des arrêts (motif « prix réel au-dessus du constat ») et des dépenses ; puis nouveau relevé, nouveau constat.

## 5. Mise en place sur l'instance, par liste blanche de fichiers nommés

**Jamais `git clone` du dépôt entier, ni `cp -r` de `src/`.**

1. Les fichiers posés sont ceux d'un commit poussé : `git diff --quiet HEAD -- <liste>`, et `COMMIT=$(git rev-parse HEAD)`.
2. Liste calculée par programme (**m5 : plus d'argument `--guide`, le guide vient de la configuration**) :
   ```
   PYTHONPATH=src .venv/bin/python scripts/liste_blanche_ligne_1_bras_a_v2.py \
     --configuration prereg/T0.7-organismes-discrets-v-a-v2-config-lanceur-ligne-1-v2.json \
     --lanceur-chemin src/controle_ia/organismes_discrets/lanceur_bras_a_v8.py \
     --plan-scelle docs/notes/relance-organismes-discrets-v1/etape-a-ligne-1-v1/plan-des-taches-v2.json > liste-blanche.json
   ```
   La liste v2 refuse un autre lanceur que la v8 et une configuration dont la clé `guide` n'est pas exactement celle inscrite. Elle rend `modules`, `donnees` et `guide`.
3. **Fichiers du guide** (clé `guide` de la liste) : l'invite, l'index et leurs deux compagnons, **déclarés à leurs empreintes données, jamais lus par le programme de la liste** (aucun accès disque sous `docs/sources/` : vérifié par un essai). La session qui pose les fichiers, et qui peut ouvrir ce dossier, confronte avant l'archive : `sha256sum` de l'invite = `69d50fb9…`, de l'index = `adb4b8bc…`, et chaque compagnon porte cette même empreinte ; un écart arrête. Ces quatre chemins sont les seules exceptions au préfixe cloisonné `docs/sources/`.
4. Ajouter à la main `requirements-gpu.txt`, `requirements-cpu.txt`, `requirements-donnees.txt` et `constat-ligne-1.json`.
5. `sha256sum $(fichiers) > empreintes-posees.txt` ; archive par liste explicite : `tar -cf ligne-1.tar -T fichiers.txt empreintes-posees.txt`.
6. **Dossier distant créé d'avance** : `ssh -p <port> root@<hôte> mkdir -p /root/ligne-1`, puis `scp -P <port> ligne-1.tar root@<hôte>:/root/ligne-1/`.
7. Sur l'instance : `tar -xf`, puis `sha256sum -c empreintes-posees.txt`, entièrement conforme.
8. Installation (`requirements-gpu.txt`), vérification de la carte, téléchargement du modèle de la configuration de référence par `harnais.modeles.precharger_modele` sous `HF_TOKEN` lu par son nom (version 1, section 5, points 8 à 10).

**Liste blanche calculée ici** : 36 modules (dont `scripts/course_ligne_1_bras_a_v2.py`, le lanceur v8, le lanceur v2, `environnements/invites.py`, `harnais/modeles.py`), 12 fichiers de données avec compagnons (configuration v2, texte scellé, configuration de référence, deux fichiers de tâches, plan v2) et les 4 fichiers du guide : 52 fichiers. Aucun chemin cloisonné parmi les modules et les données.

## 6. Lancement, surveillance, rapatriement

**Lancement sur l'instance**, en tâche détachée ; le PID est noté aussitôt :

```
cd /root/ligne-1 && . .venv/bin/activate && PYTHONPATH=src nohup python scripts/course_ligne_1_bras_a_v2.py \
  --configuration prereg/T0.7-organismes-discrets-v-a-v2-config-lanceur-ligne-1-v2.json \
  --lanceur-chemin src/controle_ia/organismes_discrets/lanceur_bras_a_v8.py \
  --lanceur-sha256 2663d32d39133ab1a96cb7a694baf7908c005c37e835d9f17cff2d578bc6344b \
  --constat constat-ligne-1.json \
  --plan-scelle docs/notes/relance-organismes-discrets-v1/etape-a-ligne-1-v1/plan-des-taches-v2.json \
  --creation-instance-utc <heure de création> --dossier /root/sorties-ligne-1 --commit "$COMMIT" \
  --mode reel --hors-ligne > /root/course.out 2>&1 & echo $! > /root/course.pid
```

- **Surveillance** : à **chaque** relevé du journal (`tail` par `ssh`), la session vérifie aussi que le processus vit encore, par son PID noté, en lecture seule : `kill -0 $(cat /root/course.pid) && echo vivant || echo mort` (D1). Processus mort sans ligne « FIN » au journal : on lit `course.out`, on rapatrie aussitôt, puis versement et destruction (section 7), sans attendre l'échéance.
- Ligne « déterminisme réglé » du journal : la carte doit être l'A100 SXM4 du relevé et le pilote celui de l'hôte relevé ; un écart est consigné et rapporté.
- Le compteur arrête la ligne entre deux lots dès que le cumul dépasse 18 USD, et avant ou après le chargement du modèle. **Échéance** de la session : création + 6 h ; passé ce délai sans « FIN », rapatriement puis destruction.
- **Rapatriement** : dossier local `la.nom_du_dossier_de_versement("ligne-1", "fini" | "arret", <heure UTC>)`, **créé d'avance** (`mkdir -p <dossier local>`), puis `scp -r -P <port> root@<hôte>:/root/sorties-ligne-1/. <dossier local>` ; on y ajoute `course.out`, `course.pid`, `constat-ligne-1.json` et `empreintes-posees.txt` ; on compare les empreintes distantes (`sha256sum` distant) aux locales.

## 7. Versement scellé, versé sur la branche, puis destruction (8.5)

Ordre : **sceller le versement, le committer et le pousser sur la branche, puis seulement détruire**.

1. Sceller :
   ```
   PYTHONPATH=src .venv/bin/python - <<'FIN'
   import json, sys
   from pathlib import Path
   from controle_ia.organismes_discrets import lanceur_bras_a_v8 as la
   d = Path("diag/organismes-discrets-v-a-v2/ligne-1-<état>-<date>")
   m = d / "manifeste-de-la-ligne-1.json"
   if not m.is_file():
       sys.exit("MANIFESTE DE LA LIGNE ABSENT : arrêt, rien n'est scellé ni détruit par cet extrait")
   print(la.sceller_le_versement(d, json.loads(m.read_text(encoding="utf-8")), manquants=[]))
   FIN
   ```
   **Manifeste de la ligne absent** : l'extrait s'arrête, ne scelle rien et ne détruit rien. La session refait un rapatriement (journal, épisodes, `course.out`) ; si le manifeste manque toujours, elle scelle à la main avec un manifeste de ligne minimal qui le dit (`{"ligne": 1, "manifeste": "absent", "journal": …}`) et la liste `manquants` (`{"nom": "manifeste-de-la-ligne-1.json", "pourquoi": …}`), puis reprend au point 2.
2. **Verser sur la branche avant toute destruction** : `git add` nommément le dossier du versement, commit, `git push` (si rejet : `git pull --rebase`, puis de nouveau). Le versement est petit.
3. Détruire, par l'identifiant, sans passer en silence :
   ```
   PYTHONPATH=src .venv/bin/python - <<'FIN'
   import json, subprocess
   from pathlib import Path
   from controle_ia.organismes_discrets import lanceur_bras_a_v8 as la
   d = Path("diag/organismes-discrets-v-a-v2/ligne-1-<état>-<date>")

   def arreter(i):
       r = subprocess.run(["vastai", "destroy", "instance", i], capture_output=True, text=True)
       if r.returncode != 0:
           raise SystemExit(f"DESTRUCTION EN ÉCHEC (code {r.returncode}) : {r.stdout} {r.stderr}")
       return {"code": r.returncode, "sortie": r.stdout}
   print(la.detruire_l_instance("<identifiant>", d, arreter))
   s = subprocess.run(["vastai", "show", "instance", "<identifiant>", "--raw"], capture_output=True, text=True)
   print("STATUT RELU :", s.returncode, s.stdout[:500], s.stderr[:500])
   FIN
   ```
   Le statut relu doit dire l'instance absente ou détruite ; puis `vastai show instances` ne la montre plus. Sinon : nouvelle destruction par l'identifiant, puis signalement à la session mère ; jamais de silence.
4. Consigner : `registres/arrets.md` (identifiant, heure, motif), `registres/depenses.md` (durée et coût lus au compte), `registres/etat.md`, commit, poussée.

**Récupérer n'est pas lire** : les épisodes versés ne sont ouverts que par l'étape (c).

## 8. Durée et coût estimés

Inchangés (version 1, section 8) : 2,43 à 2,52 h en tout ; attendu ≈ 3,9 à 5,3 USD ; pire cas 17,92 USD ; plafond 18 USD. Le réglage du déterminisme (un fil sur le processeur, algorithmes déterministes sur la carte) peut ralentir le jeu sur la carte : non mesuré ici, le compteur le borne.

## 9. Ce qui manque ou bloque avant le départ

1. **Contre-lecture du lanceur v8** (différence scellée) et de cette préparation v2 par un lecteur neuf.
2. **Confrontation des fichiers du guide** à leurs empreintes par une session qui peut ouvrir `docs/sources/` (section 5, point 3) ; elle ne lit pas le guide au-delà de l'empreinte.
3. Inscription de la configuration v2 au registre (6.3 (a)) ; image de l'instance (CUDA ≥ 13.0) ; clé du hub des modèles ; autres cases de 13.2 « avant toute dépense » : relèvent de la session.
4. **Déterminisme et configuration de référence** : la configuration de référence porte `noyau_attention = « defaut »`, le texte parle de `sdpa` (erratum cité en 13.1) ; le programme charge comme la v1 (`sdpa`) ; la contre-lecture ne tranche pas ; je ne tranche pas non plus.

## 10. Ligne 2 : même guide, vérifié aux mêmes empreintes (règle écrite)

Le contexte reconstruit des étapes suivantes doit reprendre **le même** guide que celui des épisodes honnêtes de la ligne 1. Règle : **toute fonction de la ligne 2 qui prend un guide** — `rejouer`, `distiller_tous`, `exemples` (lanceur v2), `rejouer_seconde_ligne` (lanceur v8), et de même `retenir_et_controler`, `fabriquer_les_six`, `fabriquer_jumeaux_de_verification` et `distiller_les_six` à l'étape (c) — **reçoit le texte du guide « H1-classification » lu de la configuration v2 (ou d'une version neuve qui porte la même clé `guide`, mêmes chemins, mêmes empreintes), après `verifier_les_octets_du_guide` puis `charger_invite`, exactement comme le programme de la course v2 (`charger_le_guide`)** ; jamais `None`, jamais un autre guide, jamais un guide chargé sans la vérification des octets. L'empreinte chargée (`69d50fb9…`) est portée au manifeste de chaque ligne, et confrontée à celle du manifeste de la ligne 1 : un écart arrête.

# Plan de marche de la session de formation du barreau 5 — v1

Écrit le 20 novembre 2026 vers 01:30Z par la session de formation (`session_01XJ6MgpqZTV56tSK4t2bDvN`, Opus 5.5), sur le mandat v2 de la mère (`83e5d7f8…`). Pièce de travail (classe C). Ce plan ne lance rien, ne dépense rien et ne touche à aucune instance.

Pièces lues : mandat v2 ; texte scellé `bdff244f…`, sections permises par le mandat ; devis scellé `dc886195…`, sections 3 à 6 ; code au commit `840c3ecc5` (empreintes de `__init__`, `edition_cout_v1`, `engagement_v1`, `formation_v1`, `lancer_b5f_formation_v1.sh` et `amorce_b5f_formation_v1.sh` égales, sur leurs seize premiers signes, à celles de `CODE-FORMATION-B5F`) ; rapport v5 du développeur, sections 4 à 7 ; registre propre à `316bce0a`.

**Lecture déclarée hors du périmètre du mandat v2.** Avant de recevoir le mandat, sur la seule consigne de la mère (« le texte scellé en entier »), j'ai lu du texte : les titres ; les points 1 à 5 de « Ce qui change par rapport au brouillon 1 » ; les points 1 à 6 de « Matière pesée » ; les tirets 2 à 7 du point 7 du plan ; le début des points 8 à 16 du plan. Aucune de ces lignes ne porte un résultat de l'étape B bis ni la phrase de la consigne du saboteur (j'y ai vu des taux de mondes inventés, de simulation). Je n'ai rien lu d'autre depuis le mandat.

Notations : `S` = mon bloc-notes (`/tmp/claude-0/-home-user-controle-ia-travail/4d216d9c-8888-53e9-a254-d89b28078848/scratchpad`) ; `V="$S/venv-vast/bin/vastai"` (client du loueur 1.11.2, installé dans le bloc-notes ; il lit `VAST_API_KEY` par son nom) ; `L="bash $RC/scripts/lancer_b5f_formation_v1.sh"`.

## 0. Préalables, avant le signal (aucune dépense)

1. **Arbre de la course.** Quand la mère me dit que `course/barreau5-formation-v1` existe :
   ```
   cd /home/user/controle-ia-travail && git fetch origin course/barreau5-formation-v1
   C=$(git rev-parse origin/course/barreau5-formation-v1)      # 40 signes
   RC="$S/arbre-course" ; git worktree add --detach "$RC" "$C"
   git -C "$RC" diff --stat 840c3ecc5 "$C"                       # seul registres/ doit changer
   ```
   Jamais mon arbre principal. `RC` est la RACINE de toutes les sous-commandes du lanceur (la garde `exiger_code_de_la_session` exige que son arbre soit le code figé, sans fichier non suivi sous `src/`).
2. **Contrôles à blanc, sans réseau payant** :
   - `PYTHONPATH="$RC/src" python3 -m controle_ia.scellement verifier "$RC/prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1.md"` ;
   - `$L plan` : la ligne de l'instance 6 doit dire `A1,A2`, coupure 28 USD à trois membres ;
   - `GO_ID=GO-2026-11-19-86 $L config "$RC" 6 1.20 "$C" 0` : la configuration doit être acceptée (prix fictif sous la borne, pour le seul contrôle).
   - Essais du paquet dans un environnement neuf du bloc-notes (`python3.11` si présent, sinon celui de la machine) : `PYTHONPATH="$RC/src" python -m pytest -q -p no:cacheprovider "$RC"/tests/test_barreau5_familles_*.py --basetemp="$S/essais-b5f"` ; j'envoie le compte à la mère (le plancher est remesuré par elle au commit de la course, je ne le fixe pas).
3. **Registre des dépenses** : la ligne d'engagement du devis, § 4, pour la pièce « formation n° 6 », doit être écrite avant la première minute. Je la rédige (modèle du devis, coupure 28 USD, étiquette `b5f-formation-v1-6`, attendu 11,8 à 17,2 USD, pire cas 34,5 USD, dépense antérieure 0) et je l'envoie à la mère, qui l'inscrit sur `main` ; je ne crée rien avant qu'elle me dise que c'est fait.

## 1. Les offres (cette nuit : la seule instance 6)

1. **Crédit relevé** avant tout : `$V show user --raw > "$S/b5f/credit-<instant>.json"` ; je lis le seul champ `credit`. Si le crédit est sous 5 USD, je ne crée rien et je préviens la mère.
2. **Recherche, aux bornes du devis** (unités de la requête : Go ; le code revérifie les champs bruts en Mo) :
   ```
   mkdir -p "$S/b5f" && $V search offers 'gpu_name=A100_SXM4 num_gpus=1 gpu_ram>=80 cpu_cores_effective>=16 cpu_ram>=128 disk_space>=150 cuda_max_good>=13.0 dph_total<=1.30 rentable=true' -o 'dph_total' --raw > "$S/b5f/offres-<instant>.json"
   ```
3. **Choix mécanique** : chaque offre passe `exiger_offre` du code figé ; je garde la moins chère qui passe (égalité : la plus petite valeur de `id`), écrite seule dans `"$S/b5f/offre-6-<instant>.json"`. Aucune autre préférence, aucun réglage desserré.
   ```
   PYTHONPATH="$RC/src" python3 -c 'import json,sys
   from controle_ia.barreau5_familles.formation_v1 import exiger_offre
   o=json.load(open(sys.argv[1])); o=o.get("offers",o)
   ok=[]
   for x in o:
       try: exiger_offre(x); ok.append(x)
       except Exception: pass
   ok.sort(key=lambda x:(x["dph_total"],int(x["id"])))
   print(len(ok)); ok and json.dump(ok[0],open(sys.argv[2],"w"))' "$S/b5f/offres-<instant>.json" "$S/b5f/offre-6-<instant>.json"
   ```
4. **Aucune offre** : je refais la recherche toutes les heures (rappel par `send_later`), sans rien changer aux bornes ; je dis l'heure et le nombre d'offres à la mère à chaque essai vide.
5. **Vagues suivantes** (au retour du crédit, sur signal de la mère) : même recherche, ordre 6, 1, 2, 3, 4, 5, 7 ; autant d'instances que d'offres acceptées, dans l'ordre ; recherche refaite chaque heure et à chaque fin d'instance ; **fin des créations à H + 30 heures**, H étant l'instant de création de l'instance 6, que je consigne et envoie à la mère. Une instance non créée à H + 30 heures ne l'est plus.

## 2. Chaque instance

1. **Commande imprimée, puis jouée** :
   ```
   RUN=$(date -u +%Y%m%d-%H%M%S)-b5f-formation-6
   GO_ID=GO-2026-11-19-86 $L commande "$RC" 6 "$S/b5f/offre-6-<instant>.json" "$C" course/barreau5-formation-v1 prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1.md "$RUN" > "$S/b5f/commande-6.txt"
   ```
   La sous-commande refuse si le registre au commit n'a pas les trois lignes, si le code diffère, si l'offre sort des bornes, si l'échéance n'admet pas 10,99 heures, ou si la garde de calcul bloquerait. Je joue ensuite la seule ligne imprimée, préfixe `GO_ID=GO-2026-11-19-86` compris, avec `$V` à la place de `vastai` (seul changement : le chemin du même programme). Je garde la réponse brute (`new_contract` = identifiant d'instance) dans `"$S/b5f/creation-6.json"`, et je note l'instant de création. L'accord cité est `GO-2026-11-19-86`, celui de `GO-FORMATION-B5F` (le code refuse tout autre) ; le mot de Lazar `GO-2026-11-20-02`, qui limite cette nuit à la seule instance 6, est cité dans mon message à la mère et dans le registre des dépenses.
2. **Vérification de l'instance** : `$V show instances --raw > "$S/b5f/liste-<instant>.json"` : une seule entrée porte l'étiquette `b5f-formation-v1-6`, à l'identifiant reçu.
3. **Garde de dépense, toutes les dix minutes**, par une boucle de fond (`run_in_background`) qui ne lit que le loueur et l'horloge :
   - cumul de l'instance = le plus grand de (heures depuis la création × `dph_total` de l'instance) et de (crédit au départ − crédit relevé + recharges automatiques constatées) ; cette nuit, une seule pièce tourne, donc la baisse du crédit, téléchargement compris, lui est toute imputée ;
   - cumul commun = somme des cumuls des pièces du devis (cette nuit, égal au cumul de l'instance 6) ;
   - `$L depense 6 3 <cumul_instance> <prix_h> <cumul_commun> <prix_h> 0` ; au refus, la boucle sort, et je passe au point 3 (versement prouvé, puis destruction) sans attendre la minuterie.
   - La boucle sort aussi quand l'instance n'est plus `running` (fin de marche : l'amorce demande « stopped »).
4. **Minuterie** : celle de l'amorce, sur l'instance, à l'échéance d'arrêt plus 15 minutes ; elle détruit seulement si le versement final est prouvé, sinon elle arrête sans détruire et écrit un signal. Je ne la remplace pas ; ma garde de dépense la précède.
5. **Suivi** : `$V logs <ID> --tail 200` aux pas de la boucle, réduit aux lignes « B5F » de l'amorce (minuterie, dépôt, essais du paquet et leur compte, modèle, début de marche, « poussé : », « versement final prouvé … au commit », « ARRET », « SIGNAL »). Je ne lis ni `marche.err` ni aucune sortie de la marche ; je ne prends aucune décision sur une sortie (liste d'arrêt, point 12).

## 3. Versement prouvé, puis destruction par l'identifiant

1. Fin de marche (ligne « fin, code … » au journal, état « stopped » ou « exited ») :
   ```
   B=donnees/barreau5-familles-jumelles-v1-formation-instance-6
   git -C "$RC" fetch origin "$B:refs/remotes/origin/$B"
   P=<commit de la ligne « versement final prouvé … au commit » du journal>
   git -C "$RC" show "$P:traces-b5f/inventaire-final.json" > "$S/b5f/inv-6.json" ; git -C "$RC" show "$P:traces-b5f/inventaire-final.json.sha256" > "$S/b5f/inv-6.json.sha256"
   $V show instances --raw > "$S/b5f/liste-avant-6.json"
   GO_ID=GO-2026-11-19-86 $L detruire "$RC" <ID> 6 "$S/b5f/liste-avant-6.json" "$S/b5f/inv-6.json" "$P"
   ```
   Le compagnon de l'inventaire porte le nom `inventaire-final.json` : je le copie sous ce nom à côté (`inventaire-final.json` et `.sha256` dans un dossier `"$S/b5f/inv-6/"`) pour que `verifier` le trouve. Je ne lis du fichier que ce que le code lit (chemins, tailles, empreintes).
2. Si `detruire` accepte, je joue la ligne imprimée (`GO_ID=GO-2026-11-19-86 vastai destroy instance <ID> -y`, par `$V`), puis :
   `$V show instances --raw > "$S/b5f/liste-apres-6.json" && $L verifier-destruction "$S/b5f/liste-apres-6.json" <ID> 60988826` (témoin : une machine arrêtée du loueur qui ne doit pas être détruite ; aucune action sur elle).
3. **Versement non prouvé** (refus de `detruire`, ligne « NON PROUVÉ » ou « SIGNAL ») : je demande l'état « stopped » par l'identifiant (`$V stop instance <ID>`), je ne détruis pas, et j'appelle la mère avec les lignes du journal.
4. Ligne `SORTIES-FORMATION-B5F` : à la fin de toutes les instances et de toute relance, je rédige son contenu (branches, commits prouvés, empreintes des inventaires) et je l'envoie à la mère ; question 4 sur qui l'inscrit.
5. Après chaque fin : relevé du crédit, recherche refaite (vagues suivantes, si le signal les a ouvertes).

## 4. La relance

- Une instance est « tombée » si sa marche s'arrête avant que toutes ses familles soient formées ou comptées absentes par une règle du texte, pour une cause qui ne lit aucune sortie (perte de l'hôte, garde d'instance, échéance, sorties perdues). Je le juge sur les lignes « ARRET » de l'amorce et sur l'état de l'instance, jamais sur une sortie.
- Je demande alors à la mère la ligne `GO-RELANCE-FORMATION-B5F` (« `GO-2026-11-19-87 ; instances <n>[,<m>]` », unique, après la fin ou la chute de toutes les premières marches, au plus tard à H + 54 heures) ; elle la relit et l'inscrit sur la branche de la course ; je refais l'arbre de la course à ce nouveau commit.
- Puis : `GO_ID=GO-2026-11-19-87 $L relance "$RC" <n> <offre> "$C2" course/barreau5-formation-v1 <prereg> <AAAAMMJJ-HHMMSS>-b5f-formation-<n>-x1`, même suite qu'au point 2, avec `depense … 1` (seule la coupure de l'instance remplacée compte). Deux relances au plus, une par instance, dans l'enveloppe de 56 USD.

## 5. L'engagement

1. **Quand** : après la fin de la formation et de toute relance, et après le versement prouvé de toutes les instances (calendrier du texte) ; toujours avant la création de l'instance de lecture.
2. **Sel et table, sans rien afficher** (mon fil est lisible par la mère : aucun sel, aucune ligne de table, aucun lien nom-famille ne passe par une sortie d'outil) :
   ```
   install -d -m 700 "$SECRET" && PYTHONPATH="$RC/src" python3 -c 'import sys
   from controle_ia.barreau5_familles import engagement_v1 as e
   adapt=[tuple(x.split("/")) for x in sys.argv[2].split(",")]
   t=e.table_des_etiquettes(e.tirer_sel(), adapt)
   print(e.ecrire_table(sys.argv[1], t))' "$SECRET/table-etiquettes-b5f-v1.json" "<famille/membre des adaptateurs tenus à l'écart formés, liste>"
   ```
   La sortie est la seule empreinte. La liste des adaptateurs est celle des familles tenues à l'écart présentes dans les inventaires prouvés (nom de famille tel que la formation l'a écrit, suffixes `-r1` ou `-x1` compris ; question 3).
3. **Où** : `SECRET`, dossier de droits 700 hors de tout dépôt et hors de `/root/.claude/` (question 1 sur sa durée de vie).
4. **Ligne** : `PYTHONPATH="$RC/src" python3 -c '…e.ligne_engagement(e.lire_table(p), e.maintenant_utc(), ref)…'` ; un commit de ma branche qui ne touche que `registres/barreau5-familles-jumelles-v1.md`, cette seule ligne ajoutée ; je pousse, j'envoie à la mère le commit et l'empreinte ; elle le porte sur `main` sans le modifier (ta proposition, que j'accepte).
5. **Entrées de lecture** (texte, « Données gardées ») : `preparer_entrees_de_lecture` écrit les adaptateurs tenus à l'écart sous leurs noms opaques, en seuls tenseurs, les adaptateurs d'apprentissage étiquetés et les épisodes d'évaluation des saboteurs d'apprentissage ; un seul commit, dans l'ordre des noms, sur `donnees/barreau5-familles-jumelles-v1-entrees-de-lecture`. Il me faut `torch` et `safetensors` pour processeur dans un environnement du bloc-notes (absents aujourd'hui) ; j'envoie l'empreinte de chaque fichier, jamais la table.

## 6. Les branches de données

- Chaque instance pousse sa branche `donnees/barreau5-familles-jumelles-v1-formation-instance-<n>` (et `…-<n>-x1`), avec le jeton passé par son nom à la création.
- **Réunion** sur `donnees/barreau5-familles-jumelles-v1-formation` à la fin : les dossiers `donnees/<run>/`, `runs/<run>/` et `diag/<run>/` des instances ne se recouvrent pas ; les traces (`traces-b5f/journal/…`, `traces-b5f/inventaire-final.json`) portent le même chemin dans toutes les branches et se heurteraient (question 5). Les branches d'instance restent telles quelles : ce sont elles qui portent la preuve.
- Je n'ai encore poussé que vers ma branche de travail ; si la session refuse une poussée vers une branche `donnees/…`, je m'arrête et je le dis, sans contournement.

## 7. Ce que j'envoie à la mère

- Oui : heures (création, fin, destruction), identifiants et étiquettes d'instance, dépense en dollars par instance et en commun, arrêts nommés (ligne « ARRET » de l'amorce et leur motif technique), familles refusées ou retirées par une règle du texte (au seul nom de la famille, d'après le journal de l'amorce), chemins et empreintes des sorties versées et des inventaires, commits prouvés, empreinte de la table, compte des essais du paquet.
- Jamais : la table, le sel, le lien entre un nom opaque et une famille ou un membre, un score, un coût d'épisode ou d'action, une perte de distillation, aucune mesure tirée des sorties.

## Questions à la mère

1. **Bloquant : jeton GitHub de l'instance.** Dans ma session, `GH_TOKEN` n'a pas la forme d'un jeton GitHub (contrôle de forme seulement, rien d'affiché) : c'est sans doute une valeur que le mandataire réseau de mon conteneur remplace. Passé tel quel à l'instance, hors de ce mandataire, il ne clonerait ni ne pousserait : l'amorce s'arrêterait au clonage, sans rien verser, et la minuterie arrêterait la machine sans la détruire. `HF_TOKEN` et `VAST_API_KEY` ont la forme attendue. Comment les courses précédentes ont-elles passé un jeton GitHub réel à leur instance ? Je ne crée rien tant que ce point n'est pas réglé ; je ne cherche aucun contournement.
2. **Durée de vie de la table.** Le texte veut la table chez moi, hors de toute branche poussée, jusqu'à l'ouverture (vers le 25 au 28). Mon conteneur est éphémère (un redémarrage vide le bloc-notes ; une longue inactivité le reprend). Seul le sel est indispensable (les noms se redérivent par HMAC de la liste des adaptateurs). Options : (a) dossier hors du bloc-notes, risque accepté ; (b) une copie du seul sel confiée à Lazar par un fichier qu'il ouvre seul, avec le mot de Lazar ; (c) autre lieu que tu proposes. Recommandation : (a) plus (b), confiance moyenne ; sans mot, (a).
3. **Noms des familles dans la table.** `preparer_entrees_de_lecture` exige que les lignes de la table soient exactement les adaptateurs tenus à l'écart remis. Je compte construire la table après la formation et toute relance, sur les seules familles présentes, sous le nom de famille écrit par la formation (`T03-r1`, `T05-x1` par exemple). Moins de 30 noms opaques si des familles manquent. Est-ce la lecture voulue, ou la table doit-elle porter les noms de base (`T03`) ?
4. **Ligne `SORTIES-FORMATION-B5F`** : son format n'est fixé ni par le texte (clé seulement) ni par le code de formation. Je propose « `<branche> @ <commit prouvé> ; inventaire sha256 <64>` » par instance, séparés par « ; ». Qui l'inscrit : moi, par un commit de ma branche porté par toi, comme l'engagement, ou toi ?
5. **Réunion des branches** : les traces de chaque instance portent les mêmes chemins. Je propose de réunir sous `traces-b5f/instance-<n>/…` (copie à l'octet, empreintes inchangées), les branches d'instance restant intactes comme preuve. D'accord ?
6. **Témoin de `verifier-destruction`** : je propose 60988826 (machine arrêtée, à ne pas détruire, que je ne touche pas). D'accord ?
7. **Crédit** : la coupure de l'instance 6 (28 USD) dépasse le crédit (≈ 21 USD) ; elle repose donc sur la recharge automatique de 5 USD sous 5 USD. Si une recharge échoue, le loueur peut arrêter la machine au crédit nul, sans versement ; je le traiterai comme une instance tombée (point 4). D'accord ?

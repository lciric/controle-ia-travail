# Relance courte de la machine 61875617 : pousser les lots déjà écrits de l'étalonnage du saboteur à budget (organisme retenu v5), puis la remettre à l'arrêt — brouillon 3

> **Statut** : brouillon 3 : porte R1 et R2 de la vérification des corrections (`note-verification-corrections-relance-courte-v1-cl1.md`), sur le brouillon 2 (`9910804f985248c8497d4bf8081d8fbee8457953701c22d6fc67d92a2a058df0`, intact, R12 ; différences : `differences-brouillon2-vers-3.md`). Le brouillon 2 portait toutes les corrections de la contre-lecture 1 (`contre-lecture-relance-courte-61875617-v1-cl1.md` : B1, M1 à M3, m1 à m6 ; « jouable après corrections ») ; à faire vérifier par le même contre-lecteur. **Classe B** (décision de la mère). Brouillon 1 intact (`344325770e5888e729ac67e6604f09cc0d7a3d863556b12d6f0b7ba3f612ea48`, R12) ; différences : `differences-brouillon1-vers-2.md`.
> **Auteur** : rédacteur, Claude Opus 5.5 (`claude-opus-5-5`), sous-agent de la mère. **Heure** : 2026-11-22T11:51:05Z (`date -u`).
> **Décisions déjà prises** : mot de Lazar **GO-2026-11-22-44** (« go depeche toi ») ; la mère **accepte le risque de destruction par la minuterie** ; si la minuterie détruit la machine, elle n'est pas gardée et **la course partira d'une création neuve**.
> **Script exact** : `relance-courte-61875617-v2.sh`, sha256 `97f4e627102158a5768d0d795e16c08707f956766ef874805d7f49cc9f85ddeb` ; essais à blanc joués : `essais-blanc-relance-courte-v2.txt`, sha256 `9cd18a2ff931aad21e713e4da13d1391c6898dbc13b39e209430d9ea62af83b4`.
> Rien n'a été lancé, dépensé, poussé ni demandé au loueur pour écrire ce texte (aide `--help` seule).

## Pièces lues (lecture seule) et empreintes

| pièce | empreinte sha256 |
|---|---|
| `scripts/amorce_instance_iib_v5.sh` au commit c97231b38 (identique à celle du commit de lancement 43d6d067, vérifié) | `a4686068f0cbc0733ad220675d2118c9739884b8d24b26c4a3ba40444aeb20d6` |
| `scripts/lancer_iib_v3.sh` (c97231b38) | `3c41509cb395848607bf9e671ac5083735e471ceb799e003b825dc6ac95e5c03` |
| `src/controle_ia/iib/lanceur_v5.py` (c97231b38) | `36c39fe343dee3631470d0e6c2bd5f8234517a7c91bd897c8cb1acc61d46cdc9` |
| `src/controle_ia/iib/session_v1.py` (c97231b38) | `4eb7947c28caf692a641e3a92141c90b4c36aa442ecd3f0d359b4b9af7a0d7ba` |
| `src/controle_ia/iib/session_v5.py` (c97231b38) | `17c398ea76b266c2f638618acf1a2cff694fa3178d61044ed998b15a38bb6a0b` |
| `src/controle_ia/iib/location_v1.py` (c97231b38, identique à 43d6d067) | `6446a304357338ab5a3a4a92de9eb8c0225db86eeec91541ab95dd25b6b92db3` |
| `src/controle_ia/scellement.py` (c97231b38) | `93beeb1c8aae75463afc98e76ffb330b1e4f26be9c08ae8fee539a2df6a94ef2` |
| ordre de l'étalonnage, v2 brouillon 3 (branche `claude/iib-reconception-oracle-v1` à 216a0187), §§ 3 à 8 | `3ec3a60523bbf45c0f345c91d5bdf8e20e9bb220b39a78efa93ea7c57420cc6f` |
| additif 1 de cet ordre, brouillon 3 (même branche) | `a9d43d5921252b4d60152a4d7b48e4cab50633337b53fcbe3f9e9ee80f754b92` |
| journal du loueur versé `traces/iib-executante-v5/etalonnage-2-en-cours-20261122-0700/journaux-loueur/logs-61875617-0646.txt` (lignes filtrées seulement) | `1e3d305766d036d80d6399f4f57ef85a322c57247390e72ba6b47658b132ae47` |
| outil de location trouvé dans `.venv` de la session du rédacteur (**version 1.11.2**, non 1.8.3 : voir § 9) | `cb06b09ad9ccd55462605df207ecfabca958d3324333552e2295b22777ab2ad9` |

Relevé au moment de l'écriture : `git ls-remote origin refs/heads/essai/iib-explo-v6` → `43d6d0673edd5055917f536e5310ea99c15ab75e` (la branche n'a reçu que la poussée initiale).

---

## 1. Ce que le code dit (constats, avec lignes)

1. **Où sont les lots.** Le lanceur écrit et scelle chaque lot sur le disque de la machine, dans le dépôt extrait `/root/amorce-depot` : `diag/<run>/lots/lot-NNN-<phase>.json` et `donnees/<run>/lots/ids-lot-NNN-<phase>.json`, chacun avec son compagnon `.sha256` (`lanceur_v5.py`, `verser`, l. 252-262 ; `_ecrire`, l. 132-142) ; le manifeste sous `runs/<run>/` ; `diag/<run>/resume.json` à la fin seulement, `diag/<run>/arret.json` sur une garde (le lanceur lève sur `SIGTERM`, l. 617, mais l'arrêt du conteneur ne signale que le processus 1 : `arret.json` est probablement absent). `<run>` est de la forme `AAAAMMJJ-HHMMSS-iib-reel` (amorce l. 408).
2. **Pourquoi rien n'est poussé : ce n'est pas un échec de poussée.** Le lanceur ne pousse jamais. L'amorce ne pousse qu'au départ (fait à 23:30:08Z, journal du loueur), à la fin du run, sur une sortie en erreur du lanceur, par sa minuterie (dépense de la ligne épuisée, échéance) et à un second démarrage (amorce l. 182-196, 262-320, 434-469). La coupure propre à 16 USD est faite **côté session** (surveillance, `vastai stop`), sans que l'amorce consigne. L'additif 1, § 2, le dit déjà. Le journal filtré (mots git, push, fatal, error, denied, remote, branch, auth, onstart) ne montre que le clonage, la ligne de départ et la poussée initiale réussie : aucune erreur d'authentification.
3. **Ce que fait un « start ».** La machine a été créée avec `--entrypoint bash --args -c "echo <amorce en base64> | base64 -d > /root/amorce.sh && bash /root/amorce.sh"` (`lancer_iib_v3.sh` l. 317). Il n'y a pas de script `onstart` : c'est le point d'entrée du conteneur, rejoué à chaque démarrage, et il **réécrit l'amorce depuis la commande de création** ; aucun fichier du disque ne peut le neutraliser. Au second démarrage, l'amorce :
   - compte le démarrage (`/root/iib-demarrages.txt`, l. 44-47 ; ligne « `AMORCE IIB v1 DEMARRAGE 2 : …` ») ;
   - relit l'échéance et l'heure de dépense épuisée sur le disque (l. 162-176) : échéance `1796076000` = 2026-11-30T22:00:00Z ; dépense épuisée `1795466525` = **2026-11-23T20:42:05Z** (journal du loueur) ;
   - relance la minuterie (l. 178) ;
   - voit `/root/amorce-depot` (l. 182). Sans marqueur de fin normale ni de dépense épuisée (cas présent), elle joue `iib-consigner.sh` « redémarrage d'un run interrompu » (l. 195) : `git add -A runs diag`, ajout forcé des `donnees/*/lots/ids-lot-*.json` et de leurs sceaux, commit, une trace du journal (`traces/iib-consignation-…/`), puis **poussée de `essai/iib-explo-v6` seule** (branche locale extraite l. 348), trois tentatives au plus (attentes 15 s puis 60 s) ;
   - puis `refus` (l. 196) : ligne « `refus annoncé : destruction demandée dans 180 s` », **attente de 180 s**, fichier `/root/iib-detruire`, et la minuterie envoie **`DELETE`** de l'instance (destruction, disque perdu), avec réessais pendant 30 minutes (l. 80-105, 110-121).
   - **Aucun épisode, aucun modèle, aucune suite d'essais ne repart** sur ce chemin : le lanceur n'est appelé qu'après le clonage, que ce chemin ne refait pas.
   - **Si le démarrage a lieu après 2026-11-23T20:42:05Z**, l'amorce pose le marqueur de dépense épuisée (l. 174) et prend le chemin l. 186-190 : consignation puis **destruction immédiate, sans les 180 s**.
4. **Risque principal** : un `start` nu pousse puis **détruit la machine** ~3 minutes après ; si la poussée échoue, les lots sont perdus avec le disque. Il ne relance pas l'étalonnage.
5. **Moyens examinés pour neutraliser le point d'entrée avant le start** (aide de l'outil, version 1.11.2) :
   - `vastai update instance ID --args … / --onstart …` : l'aide dit « *Update recreate an instance from a new/updated template* » ; l'effet sur le disque d'un conteneur recréé n'est pas documenté. **Rejeté** : non vérifiable sans risque.
   - `vastai execute ID 'ls|rm|du'` : commandes contraintes, rien ne peut écrire un marqueur ; un `rm` ne mène à aucun chemin sans destruction. **Rejeté** pour la neutralisation (voir l'option du § 8 pour un `ls`).
   - `vastai copy C.ID:/chemin local:…` : exige une machine en marche et un accès ssh au conteneur (image `python:3.11-bookworm`, point d'entrée `bash`, aucun démon ssh lancé) ; la mise en marche déclenche de toute façon l'amorce. **Rejeté.**
   - **Aucun moyen sûr de neutraliser l'amorce avant le start n'existe.** La méthode retenue garde l'amorce telle quelle, la laisse pousser, et **arrête la machine par son identifiant dans la fenêtre de 180 s** qui sépare la poussée de la destruction.

## 2. But unique et borné

Faire pousser par l'amorce, sur `essai/iib-explo-v6` **et nulle part ailleurs** (jamais `main`, jamais `lciric/controle-ia`), les lots déjà écrits et scellés, leurs compagnons `.sha256`, le manifeste du run et, s'ils existent, `resume.json` ou `arret.json`, plus la trace de consignation que l'amorce y joint ; puis remettre la machine 61875617 à l'arrêt (« stop », disque gardé) par son identifiant. **Rien d'autre ne tourne** : ni épisode, ni oracle, ni modèle chargé, ni reprise de l'étalonnage, ni seconde relance. Les machines 58936096, 58936099, 58936100, 60988826 et 61932710 ne sont ni lues au-delà des champs filtrés ni touchées.

## 3. Préalables (tous vérifiés par l'exécutante avant le start ; un seul en défaut : rien ne part, mot de la mère)

Variables (posées une fois, dans le shell de l'exécutante) :
```
ID=61875617
D=<dossier de la session de l'étalonnage, celui qui porte lancement.txt et surveillance.txt>
DEPOT=<extraction du code au commit de lancement 43d6d0673edd5055917f536e5310ea99c15ab75e, celle de la surveillance>
D2="$D/relance-courte-v1"; mkdir "$D2" || { echo "REFUS : $D2 existe déjà (R12)"; exit 2; }   # sans -p : refus s'il existe, avant P2 qui y écrit
VAST="$(sed -n 's/^outil_location //p' "$D/lancement.txt" | tail -1)"
VV="$(sed -n 's/^outil_location_version //p' "$D/lancement.txt" | tail -1)"
LOC="$DEPOT/src/controle_ia/iib/location_v1.py"
AIDE_GH='!f() { echo username=x-access-token; echo "password=${CONTROLE_IA_GITHUB_TOKEN:-$CONTROLE_IA_GITHUB_TOKEN_2}"; }; f'
```
- **P1 — mot de Lazar** : **GO-2026-11-22-44** (« go depeche toi »), cité au compte rendu ; risque de destruction par la minuterie accepté par la mère.
- **P2 — machine à l'arrêt, étiquette juste** : `timeout -k 5 120 "$VAST" show instances --raw > "$D2/inv-avant.json" </dev/null` puis `python3 -I -B "$LOC" inventaire "$D2/inv-avant.json" "$D2/inv-avant-champs-filtres.json" iib "$ID"` → `etat=present etiquette=iib-explo-v5 statut=exited` (ou `stopped`). Tout autre statut : rien ne part. Le lecteur réduit le fichier brut à identifiant, étiquette et état ; s'il échoue, le brut est supprimé (`rm -f -- "$D2/inv-avant.json"`), jamais gardé.
- **P3 — surveillance d'origine éteinte** : son numéro de processus (relevé à son lancement) ne répond plus à `kill -0` ; sa dernière ligne dans `$D/surveillance.txt` est la ligne « ARRET coupure de l'étalonnage … ». Aucune autre commande vers 61875617 en cours.
- **P4 — branche distante intacte** : `git -c credential.helper="$AIDE_GH" ls-remote https://github.com/lciric/controle-ia-travail.git refs/heads/essai/iib-explo-v6` rend exactement `43d6d0673edd5055917f536e5310ea99c15ab75e`. Sinon la poussée de l'amorce serait refusée (non en avance rapide) et la machine détruite après : **rien ne part**. Personne ne pousse sur cette branche avant la fin de la relance (la mère le dit aux autres sessions).
- **P5 — heure** : `[ "$(date +%s)" -le 1795462800 ]` (2026-11-23T19:40:00Z, soit 62 minutes avant l'heure de dépense épuisée 20:42:05Z lue sur le disque : 40 minutes de relance au plus et une marge de 22 minutes). Au-delà : rien ne part, nœud (§ 8, N3).
- **P6 — outil** : `"$VAST" --version` rend `$VV` ; `"$VAST" start instance --help` et `stop instance --help` répondent. Le chemin et la version sont ceux de la création.
- **P7 — jeton du dépôt** (contrôle de la session, non de la machine) : `curl -sS -o /dev/null -w '%{http_code}\n' -H "Authorization: Bearer ${CONTROLE_IA_GITHUB_TOKEN:-$CONTROLE_IA_GITHUB_TOKEN_2}" https://api.github.com/repos/lciric/controle-ia-travail` → `200` ; rien d'autre n'est imprimé. Ce contrôle porte sur le jeton de la session ; la machine pousse avec `GH_TOKEN`, posé à la création depuis le jeton de nom `CONTROLE_IA_GITHUB_TOKEN` (ou `_2` à défaut, `jeton_gh_nom` du lanceur de session). C'est le même jeton si la variable de la session n'a pas changé depuis la création ; sinon la réserve du § 9 vaut. Il a poussé à 23:30:08Z ; avec M1, ses trois tentatives sont laissées.
- **P8 — essais à blanc (R5)** du § 5 joués et réussis, sortie conservée dans `$D2/essais-blanc.txt`.
- **P9 — garde des secrets** éprouvée (§ 5, essais g1 et g2).
- **P10 — latence d'arrêt mesurée à la coupure de 12:54Z** (même machine) : dans `$D/surveillance.txt` et le compte rendu de l'exécutante, heures seules : écart entre la commande `stop instance 61875617` et la première lecture `statut=exited`. **Au-delà de 90 s : attendre le mot de Lazar** avant de jouer (la fenêtre utile après la ligne de poussée est d'environ 180 s, moins un cycle de veille de 5 à 15 s et la durée de l'appel `stop`). L'écart est inscrit au compte rendu.

## 4. Méthode : une seule commande, un seul start, arrêt dans la fenêtre

L'exécutante copie le script `relance-courte-61875617-v2.sh` (à côté de ce texte, sha256 `97f4e627102158a5768d0d795e16c08707f956766ef874805d7f49cc9f85ddeb`) dans `$D2/`, vérifie l'empreinte, puis le joue **une fois**, en avant-plan, depuis `$DEPOT`, après P1 à P10 :
```
cp relance-courte-61875617-v2.sh "$D2/" && echo "97f4e627102158a5768d0d795e16c08707f956766ef874805d7f49cc9f85ddeb  $D2/relance-courte-61875617-v2.sh" | sha256sum -c -
ID=61875617 D2="$D2" VAST="$VAST" LOC="$LOC" bash "$D2/relance-courte-61875617-v2.sh" jouer; echo "code $?"
```
Code 0 : arrêt confirmé ; 1 : arrêt non confirmé (mot de la mère) ; 2 : refus avant tout start. Ce que fait le script, dans l'ordre : il refuse si l'identifiant n'est pas 61875617, s'il est intouchable, si `start-fait` existe, si l'heure dépasse 2026-11-23T19:40:00Z, si l'état n'est pas `exited` ou `stopped` ; il fait un seul `start` ; puis, **toutes les 5 s**, il relève le journal du loueur (**code de sortie lu** ; code non nul, fichier vide ou masquage en échec = relevé **illisible**, sans tri) et **l'état** à chaque tour. **R1** : un arrêt décidé par le tri du journal part aussitôt, avant toute lecture d'état ; dans la boucle, `logs` et `show instances` ont un délai de 30 s (120 s hors de la boucle).

Règles d'arrêt (toutes par `stop instance 61875617`, relecture de l'état toutes les 15 s pendant 5 min, second `stop` à 2 min si besoin, jamais `destroy`) :
- ligne « branche essai/iib-explo-v6 poussée (redémarrage d'un run interrompu) » ; ligne « poussée impossible » ; ligne de refus de l'amorce ; chemin inattendu (« second démarrage après ») ; calcul inattendu (« début iib v5 », « CLONAGE », marque de progrès, « tests : », « run : ») — seulement après la dernière ligne « DEMARRAGE n » de rang 2 ou plus ;
- **trois relevés illisibles de suite**, comptés **seulement une fois la machine vue en marche** (R2 : pendant la mise en marche, la borne de 900 s suffit, et le start unique n'est pas consommé par un journal encore vide) ;
- **statut `running` vu et aucune ligne « DEMARRAGE 2 » 60 s après** ;
- pas encore en marche (« scheduling », « loading ») 900 s après le start (l'arrêt ne coûte alors rien) ;
- 18 min après la ligne de démarrage sans issue ; 35 min après le start.
- **Une tentative de poussée refusée n'arrête pas** (M1) : les trois tentatives et « poussée impossible » viennent avant la ligne « refus annoncé », et la fenêtre de 180 s ne s'ouvre qu'après ; arrêter plus tôt perdrait la seule poussée possible.

Remarques sur la méthode :
- La veille ne retient que les lignes qui suivent la **dernière** ligne de démarrage de rang 2 ou plus : les lignes du premier démarrage (dont « branche … poussée avant l'installation ») ne comptent jamais.
- L'arrêt part dès la ligne de poussée réussie ou dès « poussée impossible », avant la ligne de refus de l'amorce ; dans le pire cas, il part sur la ligne « refus annoncé », au début des 180 s.
- La fenêtre : la destruction ne peut venir qu'après 180 s d'attente plus 5 s de pas de la minuterie, comptées depuis la ligne de refus. La veille relit le journal toutes les 5 s (plus la latence de `vastai logs`, qui attend le journal environ 9 s au plus puis échoue, et celle de l'inventaire) ; l'arrêt est demandé quelques dizaines de secondes après la poussée. L'arrêt effectif (arrêt du conteneur par le loueur, qui tue la minuterie) n'est pas daté par le loueur : c'est le risque résiduel (§ 7).
- Le relevé brut du journal est écrit sous `umask 077`, masqué par `location_v1.py masquer-en-place` avant toute recherche ; en échec de masquage, il est vidé et compté illisible. Les inventaires bruts sont réduits par le lecteur ou supprimés. L'exécutante ne l'affiche pas : seules les lignes de `veille.txt` et `lignes-d-issue.txt` (lignes de l'amorce et de la consignation, sans les marques de progrès) lui sont montrées.

## 5. Gardes et essais à blanc (R5 : cas sain et artefact, sans le loueur), **joués par le rédacteur**

Joués sur le script exact, dans un dossier à part (`scratchpad/essais-relance-courte-v2/`), avec un **faux outil de location** (réponses fixes, appels notés dans `appels.txt`, refuse `destroy` et tout identifiant autre que 61875617), `PAS_S=0`, et pour chaque essai `VAST=<faux outil>` **et** `D2=<dossier propre à l'essai>` explicites (m2 : un essai joué avec le vrai `$D2` poserait `start-fait` et bloquerait la vraie relance). Sortie : `essais-blanc-relance-courte-v2.txt` (`9cd18a2ff931aad21e713e4da13d1391c6898dbc13b39e209430d9ea62af83b4`). Résultats, tous conformes :

| essai | entrée | sortie obtenue |
|---|---|---|
| d1 base | journal du premier démarrage seul (avec la poussée initiale) | `ATTENDRE` |
| d1 sain | + « DEMARRAGE 2 » | `DEMARRAGE` |
| d2 | + poussée sur `essai/iib-explo-v6` | `ARRETER : poussée faite` |
| d2 artefact | + poussée sur `essai/iib-explo-v5` | `DEMARRAGE` |
| d3 (M1) | + « tentative 1 refusée » seule | `DEMARRAGE` (pas d'arrêt) |
| d3 (M1) | + « tentative 1 refusée » puis poussée faite | `ARRETER : poussée faite` |
| d3 (M1) | trois tentatives puis « poussée impossible » | `ARRETER : poussée impossible` |
| d4 | + « refus annoncé » sans poussée | `ARRETER : refus …` |
| d5 | + « début iib v5 » après le démarrage 2 (la même ligne avant n'est pas comptée, d1 base) | `ARRETER : calcul inattendu` |
| j1 | état `exited`, puis journal à poussée faite | 1 start, 1 stop, `ARRET CONFIRME`, code 0 |
| j1b | second `jouer` dans le même dossier | code 2, 0 appel neuf |
| j2 | état `running` avant le start | `REFUS`, 0 start |
| j3 | `ID=58936096` | `REFUS`, aucun appel |
| j4 | borne d'heure à 0 (variable d'essai `HEURE_MAX_S_ESSAI`) | `REFUS`, aucun appel |
| j5 | état `loading`, borne de mise en marche à 0 | 1 stop, `ARRET CONFIRME` |
| j6, F | état toujours `running` après l'arrêt (F : sur « poussée impossible ») | 2 stops exactement, `ARRET NON CONFIRME`, code 1 |
| j7 (B1, R2) | `logs` en code 1 quatre fois (le premier, avant la marche, non compté) | 4 relevés, 1 stop, arrêt sur trois illisibles |
| j7b (R2) | `logs` toujours en code 1, état `loading` | illisibles non comptés : arrêt sur la borne de mise en marche, non sur « illisible » (le faux outil reste à `loading` après le stop, d'où « non confirmé », artefact de l'essai) |
| R1 (A, B, F, j6, j10) | arrêt décidé par le tri | l'appel qui précède le premier `stop` est `logs`, jamais `show instances` |
| E | poussée sur la branche v5 seule | non reconnue ; arrêt sur la borne totale |
| j8 (B1) | `running` sans « DEMARRAGE 2 », borne de 60 s ramenée à 0 | 1 stop, `ARRET CONFIRME` |
| j9 (M1) | « tentative 1 refusée », puis poussée faite au relevé suivant | 2 relevés, arrêt sur `poussée faite` |
| j10 | « poussée impossible » | 1 stop, `ARRET CONFIRME` |
| g1, g2 | fichier sans jeton ; fichier avec `ghp_` + 36 caractères tirés au hasard | `0` code 0 ; `1` code 1 |

Aucun `destroy` dans aucun essai. Non éprouvé : le vrai outil (latences, formes réelles des réponses).

**Garde des secrets** (sous-commande `secrets FICHIER…` du script, même code ; n'imprime qu'un nombre ; valeurs lues par leur nom seulement) :
```bash
garde_secrets() { python3 -I -B - "$@" <<'PY'
import os, re, sys
noms = ("HF_TOKEN", "CONTROLE_IA_GITHUB_TOKEN", "CONTROLE_IA_GITHUB_TOKEN_2", "GH_TOKEN", "VAST_API_KEY")
vals = [os.environ[k].encode() for k in noms if len(os.environ.get(k, "")) >= 8]
motif = re.compile(rb"ghp_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{40,}|hf_[A-Za-z0-9]{30,}|sk-ant-[A-Za-z0-9_-]{20,}")
n = 0
for f in sys.argv[1:]:
    b = open(f, "rb").read()
    n += sum(b.count(v) for v in vals) + len(motif.findall(b))
print(n)
sys.exit(0 if n == 0 else 1)
PY
}
```
Jamais `env`, `printenv`, `set` sans argument, `export -p`, `/proc/*/environ`.

## 6. Durée et coût bornés

- **Machine en marche** : du start à l'arrêt confirmé, **40 minutes au plus** (borne totale de 35 minutes, plus 5 minutes de relecture de l'arrêt). Attendu : 2 à 6 minutes (outils déjà installés, consignation de quelques fichiers légers).
- **Prix** : carte 1,16 USD/h + stockage 0,033333 USD/h = 1,193333 USD/h ; **0,80 USD au plus** pour la relance (attendu 0,06 à 0,16 USD). Pendant un éventuel état « scheduling » (carte prise par un autre locataire), la borne de 15 minutes arrête.
- **Stockage à l'arrêt ensuite** : 0,033333 USD/h, soit 0,80 USD par jour, jusqu'au mot de la mère sur la destruction (ordre § 5 étape 7 : 48 heures au plus, 1,60 USD).
- **Ligne** (`GO-2026-11-21-70`, coupure 55 USD, plafond 60) : environ 16 USD à la coupure propre, plus la réaction de la session (0,1 à 0,4 USD) ; après la relance, **17,2 USD au plus**, et 18,8 USD au plus avec 48 heures de stockage. Sous la coupure de la ligne ; **au-dessus des 17 USD de l'étape 1 du devis** (déjà signalé par l'additif 1, § 1) : à faire accepter par Lazar avec la relance.
- **Aucune relance en boucle** : un seul `start`, gardé par le fichier `start-fait` ; aucune commande du loueur n'est rejouée automatiquement, sauf le second `stop` de la relecture.

## 7. Après l'arrêt : vérification fichier par fichier (sur processeur, sans le loueur)

Machine arrêtée et confirmée. Puis, dans un dossier neuf `W=$(mktemp -d)` :
```bash
git -c credential.helper="$AIDE_GH" clone -q --filter=blob:none --no-checkout --single-branch --branch essai/iib-explo-v6 \
    https://github.com/lciric/controle-ia-travail.git "$W/b"
git -C "$W/b" rev-parse HEAD > "$D2/tete-branche.txt"
git -C "$W/b" diff --name-status 43d6d0673edd5055917f536e5310ea99c15ab75e HEAD > "$D2/diff-name-status.txt"
# écart si une ligne n'est pas « A » (ajout) ou si un chemin sort de diag/*-iib-*/, runs/*-iib-*/, donnees/*-iib-*/, traces/iib-consignation-*/
awk '$1!="A"' "$D2/diff-name-status.txt" | wc -l                                       # attendu 0
cut -f2 "$D2/diff-name-status.txt" | grep -vcE '^(diag|runs|donnees)/[^/]*-iib-[^/]*/|^traces/iib-consignation-' # attendu 0
git -C "$W/b" sparse-checkout set --no-cone '/diag/*-iib-*/' '/runs/*-iib-*/' '/donnees/*-iib-*/' '/traces/iib-consignation-*/' '/src/'
git -C "$W/b" checkout -q HEAD
cd "$W/b"
PY_V="$DEPOT/.venv/bin/python"; [ -x "$PY_V" ] || PY_V=python3          # m4 : interprète de la session, non l'interprète courant
cut -f2 "$D2/diff-name-status.txt" | grep -E '^(diag|runs|donnees)/' | grep -v '\.sha256$' | sort > "$D2/listes.txt"
n_l=$(wc -l < "$D2/listes.txt"); n_v=0
while IFS= read -r f; do
    [ -f "$f.sha256" ] || { echo "SANS COMPAGNON $f" >> "$D2/ecarts.txt"; continue; }
    if PYTHONPATH="$W/b/src" "$PY_V" -m controle_ia.scellement verifier "$f" >> "$D2/verification.txt" 2>&1; then n_v=$((n_v + 1))
    else echo "SCEAU NON CONFORME $f" >> "$D2/ecarts.txt"; fi
done < "$D2/listes.txt"
echo "listés $n_l vérifiés $n_v" | tee -a "$D2/verification.txt"          # exigé : n_v = n_l, et ecarts.txt absent
# m3 : seules les traces ajoutées par la relance (les traces anciennes de l'arbre au commit 43d6d067 ne comptent pas)
for d in $(cut -f2 "$D2/diff-name-status.txt" | grep '^traces/iib-consignation-' | cut -d/ -f1-2 | sort -u); do
    (cd "$d" && sha256sum -c --quiet empreintes.sha256) >> "$D2/verification.txt" 2>&1 || echo "TRACE NON CONFORME $d" >> "$D2/ecarts.txt"; done
cut -f2 "$D2/diff-name-status.txt" | while IFS= read -r p; do printf '%s %s\n' "$(stat -c %s -- "$p")" "$p"; done > "$D2/inventaire-tailles.txt"
cut -f2 "$D2/diff-name-status.txt" | while IFS= read -r p; do sha256sum -- "$p"; done > "$D2/inventaire-empreintes.txt"
bash "$D2/relance-courte-61875617-v2.sh" secrets $(cut -f2 "$D2/diff-name-status.txt")      # exigé : 0
```
- **Nombre attendu, par recoupement** : deux fichiers de données par lot (`lots/lot-NNN-*.json` et `lots/ids-lot-NNN-*.json`), numérotés sans trou à partir de `001` ; le dernier numéro est comparé à celui que disent les marques de progrès relevées par la surveillance (`$D/progres.txt`), s'il y figure. Un dernier lot sans compagnon ou au sceau faux (écrit au moment de l'arrêt) est un écart rapporté, jamais réparé.
- **Rien n'est ouvert** : `scellement verifier` et `sha256sum` calculent des empreintes ; l'inventaire ne donne que tailles, noms et empreintes ; aucune commande `cat`, `head`, `jq`, `python -c 'json.load…'` sur une sortie ; personne ne lit une sortie avant la désignation scellée (ordre § 8).
- **Versement des traces de la relance** : `$D2` entier (veille, lignes d'issue, réponses du loueur masquées, inventaires réduits et en champs filtrés, script, vérification) passe la garde des secrets à 0, puis la mère le verse scellé où elle le décide ; ce texte ne pousse rien lui-même.
- **Ce qui reste sur le disque, non poussé par ce chemin** : le journal complet de l'instance (`/root/iib/journal.txt`, dont les 400 dernières lignes partent dans la trace de consignation), `run.err`, `tests.txt`, `pip-freeze.txt`. Aucun ne porte de sortie de mesure ; leur récupération demanderait un autre démarrage (qui détruirait la machine), elle n'est pas proposée.

## 8. Nœuds (mot de Lazar exigé avant de jouer)

- **N1 — la relance elle-même** (**tranché : GO-2026-11-22-44**) : un démarrage de 61875617 (écart à l'ordre, § 5 étape 5, dernière phrase : la relance lit le disque d'une instance arrêtée) ; levée bornée de l'outil de location pour l'exécutante : `show instances`, `start instance 61875617` une fois, `logs 61875617`, `stop instance 61875617` deux fois au plus ; rien d'autre. Dépense : 0,80 USD au plus, plus le stockage.
- **N2 — risque résiduel accepté ou non** : si l'arrêt n'est pas effectif dans les 180 s qui suivent la ligne de refus de l'amorce, la minuterie **détruit** la machine. Si la poussée a réussi, la perte est celle du disque seulement (les lots sont sur la branche) ; si les trois tentatives de poussée échouent, la veille arrête sur « poussée impossible », avant la ligne de refus, donc avant la fenêtre de 180 s. Options : (a) **méthode de ce texte** — arrêt dans la fenêtre (recommandée, confiance moyenne : la latence d'arrêt du loueur n'a jamais été mesurée sur cette machine) ; (b) laisser l'amorce pousser puis détruire, sans arrêt — plus simple, irréversible, contraire à « aucune destruction sans le mot de la mère » ; (c) ne rien relancer — lots perdus à la destruction, l'étalonnage reste « non calculable ». **Tranché par la mère : risque accepté** ; si la minuterie détruit la machine, elle n'est pas gardée et la course partira d'une création neuve. Si rien n'a été poussé, la perte est celle des lots : l'étalonnage reste « non calculable ».
- **N3 — heure limite** : aucun start après 2026-11-23T19:40:00Z. Passé cette heure, l'amorce détruirait sans attente après la consignation ; seule l'option (b) resterait, sur un nouveau mot.
- **N4 — option : liste du disque avant le start**, par `timeout -k 5 120 "$VAST" execute 61875617 'ls -l -R /root/amorce-depot/diag /root/amorce-depot/donnees /root/amorce-depot/runs'` (noms et tailles seulement ; commande `ls` seule, jamais `rm`). Elle donnerait la liste exacte à comparer à la branche. Non retenue d'office : l'aide de la version 1.11.2 ne dit pas si `execute` vaut sur une machine arrêtée ; une sortie qui citerait autre chose que des noms et des tailles serait masquée et non lue.
- **N5 — dépassement de l'étape 1** (17 USD au devis) : 17,2 USD au plus avec la relance, 18,8 avec 48 heures de stockage.
- **N7 — latence d'arrêt** (P10) : au-delà de 90 s mesurées à la coupure de 12:54Z, mot de Lazar avant de jouer.
- **N6 — sort de la machine après la relance** : à l'arrêt jusqu'au mot de la mère (destruction par la sous-commande `destruction` du lanceur de session, rapatriement vérifié). **Tout démarrage futur de 61875617 la détruit en 3 minutes environ** (même chemin de l'amorce) : à inscrire au registre d'état.

## 9. Réserves

- **Version de l'outil** : l'ordre exige 1.8.3 ; l'outil trouvé dans `.venv` de la session du rédacteur est 1.11.2 (empreinte ci-dessus). L'exécutante emploie l'outil et la version inscrits dans `$D/lancement.txt` (P6) ; l'aide lue ici est celle de 1.11.2.
- **Non éprouvés** : le délai entre `vastai stop` et l'arrêt effectif du conteneur ; la latence de `vastai logs` sur une machine qui redémarre ; que le loueur rende la même carte (sinon « scheduling », borne de 15 minutes) ; que le jeton posé sur la machine à la création soit encore valide (il a poussé à 23:30:08Z).
- Le texte suppose l'état du disque déduit du code (aucun marqueur de fin normale ni de dépense épuisée, dépôt extrait présent). La veille arrête sur tout autre chemin (« second démarrage après … », « début iib v5 »).

## 10. Liste d'arrêt

- Un préalable P1 à P10 en défaut (P10 au-delà de 90 s : mot de Lazar) : **rien ne part**, mot de la mère.
- `start` en code non nul : arrêt par l'identifiant aussitôt, aucun second start.
- Pas en marche 15 minutes après le start ; aucune issue 18 minutes après le démarrage ; 35 minutes après le start : arrêt.
- Poussée faite, poussée impossible, refus sans poussée, chemin inattendu, calcul inattendu : arrêt aussitôt. Une tentative refusée seule n'arrête pas.
- Trois relevés du journal illisibles de suite ; statut `running` depuis 60 s sans ligne « DEMARRAGE 2 » : arrêt aussitôt.
- Arrêt non confirmé après deux `stop` et 5 minutes : aucune autre commande, mot de la mère.
- Après l'arrêt : branche distante différente de l'attendu, chemin hors des quatre dossiers, ligne autre qu'un ajout, fichier sans compagnon ou au sceau faux, `n_v ≠ n_l`, garde des secrets non nulle : écart rapporté, **rien n'est réparé, rien n'est relancé, aucune destruction**.
- Jamais : un second start, `destroy`, une commande vers une autre instance, un arrêt par motif de ligne de commande, une poussée par l'exécutante sur une autre branche, l'ouverture d'une sortie.

## 11. Compte rendu de l'exécutante (nombres et états seuls)

GO-2026-11-22-44 ; latence d'arrêt mesurée à la coupure (P10) ; heures du start, de la ligne de démarrage 2, de la ligne d'issue, de la commande d'arrêt et de l'arrêt confirmé ; motif d'arrêt (ligne de `veille.txt`) ; codes du start et des stops ; tête de la branche après la relance ; `listés` et `vérifiés` ; écarts ; garde des secrets ; dépense relevée ; empreinte du script de veille et des essais à blanc.

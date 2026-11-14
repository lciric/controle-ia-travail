# Devis du tour du collisionneur sur « Regard ou raisons » (explications rivales et forme du papier), consultations à part comprises — v1

Écrit le 14 novembre 2026 à 09:27 UTC (heure relevée par `date -u`), **avant tout appel**, par l'opérateur neuf (Claude Fable
5.2) de la session mère, sous **GO-2026-11-12-04** (collisionneur, quatre tours au plus, 15 USD par tour ; ligne de
`registres/go.md`). **Tour 3 sur 4** (tour 1 : 9,54 USD ; tour 2 : 13,84 USD ; cumul de la ligne avant ce tour : 23,38 USD
sur 40). **Plafond de ce tour : 15 USD, les deux consultations à part (Argon, Astra) comprises** ; aucune autre dépense.
Mots de Lazar : `registres/decisions.md`, R-2679, R-2680, R-2682. Procédure : celle du tour 2 (R-2539), consigne
`docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-12-2019-v1/consigne-collisionneur-bassins-etroits-v2.md`, appliquée
point par point ; seuls changent la question, les faits, les dossiers et la liste des consultations (Kimi n'est pas consulté
à part).

## 1. Pièces (empreintes vérifiées avant d'écrire ce devis)

- Faits : `docs/notes/regard-ou-raisons-confondants-v1/faits-v1.md`
  (`8708619040b1483a97d33bd5dc3576d083656a3a7c29a8b273b0944e964e6642`, 8 987 octets), scellés par la mère, non modifiés.
- Question : `docs/notes/regard-ou-raisons-confondants-v1/question-v1.md`
  (`f0481482366f350762e40cd253a58c0ee08fa4216cd65730e1d85a3228744f8f`, 3 009 octets), scellée par la mère, non modifiée.
  **Question servie** (étage III et consultations) : le bloc « ## Question » de ce fichier, mot pour mot, extrait par
  programme (tout ce qui suit la ligne `## Question`, lignes vides de tête retirées ; l'extrait est une sous-chaîne exacte du
  fichier scellé) : `collisionneur-v1/question-etage3-servie-v1.md`
  (`77156e044fd58c4e83eedb5e1810fb79580ef0e3e907737c4d9be670bf3acddb`, 2 505 octets, 2 419 caractères). L'en-tête du fichier
  de la mère (qui nomme les cinq sources) n'est pas servi.
- Script du collisionneur, inchangé, employé depuis son chemin :
  `docs/notes/collisionneur-experimentateur-v1/script-v1/collisionneur_v8_plafonds_bas_v1.py`
  (`4ad78ccce8228aed2679c854eaec7ee4d2ab8f867098218387024adfeb1e7756`). Espèces et plafonds de sortie (premier essai /
  relance) : A `claude-fable-5-1` 22 000 / 64 000 ; B `claude-opus-4-6` 10 000 / 64 000 ; C `gemini-4-argon` 18 000 /
  32 000 ; D `kimi-k3.1-pro` 32 000 / 65 536 ; E `gpt-6-astra` 8 000 / 32 000. Aucun changement de modèle ni de plafond.
- Programme des consultations à part, **celui du tour 2, inchangé, employé depuis son chemin** :
  `docs/notes/collisionneur-bassins-etroits-v1/consultation_a_part_v1.py`
  (`59c2fd36535aaf8fd57dc1d7b8c554779d6d2d0f6ab5169c8098b58a61a356be`). Il n'impose pas trois modèles : son option
  `--modeles argon,astra` restreint la liste ; aucune version 2 n'est donc écrite. Essais hors réseau rejoués
  (`essais_consultation_a_part_v1.py`, `3a49df5346edc25de0df8b5a276754d9f5d51ba3b5126b35654615fce0000384`) sur les faits et
  la question servie de ce tour : **19 sur 19** (`essais-consultation-a-part-sortie-v1.txt`,
  `222c67251039d913aeeff5efa221b9ab88731b1f2d80ab7029d4fe547552afec`).
- Relais Kimi : `docs/notes/ideation-organisme-v1/relais-kimi-v1/relais_kimi_v4.py`
  (`67f369518102b3f7408f28dab053a4d6f9bc2b676eadfaa338f55d39af99027e`).

## 2. Pire cas

**Consultations à part** (programme, mode `--devis`, sortie brute `devis-consultations-sortie-v1.txt`,
`61228fae48c91116e18bf643288187a4f79f8aab261047ce4e284f27ec60f527`) : prompt unique de 12 682 caractères (`a844b8da…`), le
même pour les deux, un appel par modèle, un seul essai, au barème du script :

| consultation | modèle | plafond de sortie | prix (entrée / sortie, USD par million) | pire cas USD |
|---|---|---|---|---|
| Argon | `gemini-4-argon` | 24 000 | 10 / 50 | 1,2423 |
| Astra | `gpt-6-astra` | 16 000 | 10 / 50 | 0,8423 |
| **total** | | | | **2,0845** |

**Collisionneur, étage III** (programme `devis` du script, sortie brute `devis-sortie-v1.txt`,
`9e27d48e826ef11eea31d8963d2bed4fcbe5b0d1c8e50b57511f61e6afd16277`) : **15 cellules, 14,45 USD au pire cas, sans relance**.
Par espèce sur les trois tours (somme des lignes arrondies du devis) : A 4,17 ; B 3,55 ; C 3,57 ; D 1,13 ; E 2,07.

**Somme des pires cas : 16,53 USD > 15.** Conséquence, acceptée par la consigne du tour 2 (point 4) : le script du
collisionneur peut s'arrêter à une porte de plafond (code 4, sans appel) avant la fin de l'étage ; aucun plafond de sortie
n'est changé ; **porte de plafond atteinte : arrêt, rapport, rien d'autre**. Repères (RAPPORTÉS,
`docs/notes/collisionneur-bassins-etroits-v1/depense-et-incidents-v1.md`) : au tour 2, 12,29 USD réels pour un pire cas de
14,47 ; Argon et Astra consultés à part : 0,6699 + 0,6068 USD.

## 3. Garantie de plafond

1. Les consultations passent **d'abord**, avec `--plafond-usd 15` (le programme s'arrête, code 2, sans appel, si leur pire
   cas dépasse ce plafond ; contrôle refait avant chaque appel).
2. Le collisionneur reçoit ensuite `--plafond-usd` = **15,00 moins la dépense réelle des deux consultations au barème du
   script (`depense_usd_bareme_script` de `resume.json`), arrondie au centime supérieur**, calculé par programme dans la
   commande elle-même ; le script vérifie, avant chaque appel, dépense consignée du run + pire cas de l'appel ≤ plafond.
   Sans `resume.json` (consultations arrêtées anormalement) : aucun lancement, rapport.
3. Relais Kimi (trois cellules du collisionneur) : port 8789, modèle permis `kimi-k3.1-pro`, **plafond 3 USD, au plus
   8 appels**, prix 2 / 10 / 2, délai 1 800 s, silence 600 s ; arrêt par son numéro de processus (R10). Sa dépense est
   comptée dans celle du run (barème du script), pas en plus.

Total au pire, par construction : ≤ 15 USD au barème du script (dépense des consultations + plafond restant du run).
Réserve : un appel en vol au moment d'une coupure du processus (délai de la tâche de fond, redémarrage du conteneur) serait
facturé sans être consigné au journal ; il serait déclaré.

## 4. Commandes exactes (lancement depuis la session mère, sans crochet de garde : la commande écrite d'avance en tient lieu)

Toutes lancées depuis `/home/user/controle-ia-travail`, une seule invocation chacune, avec ces variables de chemins (aucune
ne porte de secret) :

```
BAS=/tmp/claude-0/-home-user/1c58e8d5-f826-5476-bf99-3af565cb9c5a/scratchpad/agents/collisionneur-regard-ou-raisons
PY=$BAS/venv-coll/bin/python
S=docs/notes/collisionneur-experimentateur-v1/script-v1/collisionneur_v8_plafonds_bas_v1.py
C=docs/notes/collisionneur-bassins-etroits-v1/consultation_a_part_v1.py
R=docs/notes/ideation-organisme-v1/relais-kimi-v1/relais_kimi_v4.py
F=docs/notes/regard-ou-raisons-confondants-v1/faits-v1.md
Q=docs/notes/regard-ou-raisons-confondants-v1/collisionneur-v1/question-etage3-servie-v1.md
```

**Commande 1 — consultations à part (Argon, puis Astra ; tâche de fond de la session)** :

```
{ date -u; env -i PATH=/usr/bin:/bin LANG=C.UTF-8 HTTPS_PROXY="$HTTPS_PROXY" SSL_CERT_FILE="$SSL_CERT_FILE" GEMINI_API_KEY="$GEMINI_API_KEY" OPENAI_API_KEY="$OPENAI_API_KEY" "$PY" -I -B "$C" --script "$S" --faits "$F" --question "$Q" --sortie "$BAS/consultations-a-part-v1" --plafond-usd 15 --modeles argon,astra; echo "code $?"; date -u; } > "$BAS/console-consultations-v1.log" 2>&1
```

**Commande 2 — relais Kimi (tâche de fond de la session, délai explicite de deux heures ; `exec` : le processus de la
tâche devient le relais, dont le numéro est lu dans `/relais/etat`, champ `pid`, avant tout signal)** :

```
mkdir "$BAS/relais-v1" && exec env -i PATH=/usr/bin:/bin LANG=C.UTF-8 KIMI_API_KEY="$KIMI_API_KEY" HTTPS_PROXY="$HTTPS_PROXY" SSL_CERT_FILE="$SSL_CERT_FILE" python3 -I -B "$R" --port 8789 --modeles-permis kimi-k3.1-pro --plafond-usd 3 --prix-entree 2 --prix-sortie 10 --prix-cache 2 --max-appels 8 --delai-amont-s 1800 --delai-silence-s 600 --journal "$BAS/relais-v1/journal-relais-kimi-v1.jsonl" > "$BAS/relais-v1/console-relais-v1.log" 2>&1
```

État du relais, lu avant et après le run (aucune dépense, boucle locale, sans mandataire) :
`curl -sS --noproxy '*' http://127.0.0.1:8789/relais/etat`.

**Commande 3 — collisionneur, étage III, cinq espèces (tâche de fond de la session, délai explicite de deux heures)** :

```
PLAFOND=$(python3 -I -B -c 'import json,sys,decimal as d; x=d.Decimal(str(json.load(open(sys.argv[1]))["depense_usd_bareme_script"])); print(d.Decimal("15.00")-x.quantize(d.Decimal("0.01"),rounding=d.ROUND_CEILING))' "$BAS/consultations-a-part-v1/resume.json") && { date -u; sha256sum "$S"; echo "plafond du run : $PLAFOND USD"; env -i PATH=/usr/bin:/bin LANG=C.UTF-8 HTTPS_PROXY="$HTTPS_PROXY" SSL_CERT_FILE="$SSL_CERT_FILE" ANTHROPIC_API_KEY="$RR_ANTHROPIC_API_KEY_RIGAUD" GEMINI_API_KEY="$GEMINI_API_KEY" OPENAI_API_KEY="$OPENAI_API_KEY" KIMI_RELAIS_URL=http://127.0.0.1:8789 "$PY" -I -B "$S" etage3 --faits "$F" --question "$Q" --sortie "$BAS/run-e3-v1" --plafond-usd "$PLAFOND"; echo "code $?"; date -u; } > "$BAS/console-run-e3-v1-lancement1-v1.log" 2>&1
```

**Reprise du même run, seulement dans les cas prévus** (même commande 3, même plafond, console
`console-run-e3-v1-relanceN-v1.log`, plus les options dites ; les cellules déjà valides sont sautées par le script) :
- refus d'une espèce (statut `REFUS`, arrêt du script à la porte, code 2) : règle R-831 telle que la mère la donne pour ce
  tour — `--accepter-absence` sur la cellule refusée et sur les cellules suivantes de cette espèce
  (`E3-T1-conception-X`, `E3-T2-critique-croisee-X`, `E3-T3-reponse-X`) ; aucune relance d'un refus, aucune reformulation ;
- amont de Kimi en échec (code 5 sur une cellule de D) : comme au tour 2, absence acceptée des cellules de D, consignée ;
- coupure de la tâche de fond (délai, redémarrage) sans arrêt du script : même commande, sans option de plus ;
- tout autre arrêt (code 3 modèle différent, code 4 plafond, code 5 d'une autre espèce) : **arrêt, rapport, rien d'autre**.

**Commandes de fin** (hors réseau, aucune dépense) : état du relais relevé dans `$BAS/relais-v1/etat-apres-v1.json` ;
relais arrêté par `kill <numéro lu dans l'état, contrôlé par ps>` et vérifié arrêté ;
`env -i PATH=/usr/bin:/bin LANG=C.UTF-8 "$PY" -I -B "$S" verifier "$BAS/run-e3-v1"` ; copie `cp -a` du run et des
consultations vers `docs/notes/regard-ou-raisons-confondants-v1/collisionneur-v1/` (`run-e3-v1/`,
`consultations-a-part-v1/`, `relais-v1/`, consoles) ; `verifier` de nouveau sur la copie ; recherche de motifs de clés
(`sk-ant-`, `sk-`, `ghp_`, `hf_`, `AKIA`, `AIza`) sur toutes les sorties avant de les verser ; sceaux.

## 5. Mécanique

- Clés par leur nom, sous `env -i`, jamais affichées : `ANTHROPIC_API_KEY="$RR_ANTHROPIC_API_KEY_RIGAUD"`, **sans**
  `ANTHROPIC_BASE_URL` (présente dans l'environnement de la session, non transmise) ; `GEMINI_API_KEY="$GEMINI_API_KEY"`
  (jamais `GEMINI_API_KEY_2`) ; `OPENAI_API_KEY="$OPENAI_API_KEY"` ; `KIMI_API_KEY` au seul relais. Mandataire et
  certificats : `HTTPS_PROXY`, `SSL_CERT_FILE`, passés par leur nom. Présence des six variables contrôlée par leur nom, sans
  valeur.
- Interpréteur : environnement Python neuf dans le bac à sable de ce tour (`venv-coll`, Python 3.13.18, `anthropic` 2.3.0,
  les versions du tour 2 ; l'ancien bac à sable n'existe plus) ; relais par `python3 -I -B`.
- Run, consultations, relais et consoles écrits dans le bac à sable pendant tout le tour ; copiés au dépôt à la fin
  seulement (aucun morceau intermédiaire d'un journal de fournisseur dans le dépôt).
- Refus, absence, troncature : consignés tels quels ; une consultation refusée ou tronquée est dite absente, sans relance.
- Aucune synthèse, aucun classement : l'opérateur contrôle seulement que chaque réponse est complète (statut, marqueur de
  fin, modèle servi). Aucune écriture git.

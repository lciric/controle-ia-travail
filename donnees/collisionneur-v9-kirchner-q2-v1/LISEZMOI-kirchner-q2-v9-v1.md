# Tour du collisionneur v9 sur la question 2 du mentor Kirchner — LISEZMOI v1

Session développeur de session-depot, 3 novembre 2026, écrit à 10:19 UTC (`date -u`). Préparé **sans aucun appel payant**, pour la
session fille. Spécification : `specification-kirchner-q2-v1.md` de conv-audit (934f5dcb…), § 2 « Tour du collisionneur v9 ».

## Ce que fait le tour
Collisionneur v9 (`collisionneur_v9.py`, 27e9ce40…, copie à l'octet de 9edaeb26), étage III, trois sous-tours (conception à
l'aveugle, critique croisée, réponse), cinq espèces : A Fable 5.1, B Opus 5.5, C Argon, D Kimi K3.1 Pro (relais Kimi v3 local, port
8812), E GPT-6 Astra. `--question question.md` (291f91f8…, la question servie à l'octet) ; `--faits faits.md` (cc202ecd…) : ligne
d'en-tête « pas de web, pas d'exécution de code ; nouveauté : non cherchée », puis la pièce Kirchner **v2** (6e7fb1c5…) et « nos
résultats » v1 (d6fa8011…), chacune à l'octet entre deux balises `DÉBUT FICHIER … sha256=…` / `FIN FICHIER …` (forme de
l'assembleur brainstorm), par `assembler_faits_kirchner_v1.py` (empreintes des pièces exigées). Balayage : 0 correspondance
(`balayage-faits.txt`).

## Appels et devis (course à blanc : `course-a-blanc-kirchner-q2-v1.txt`)
- **15 appels de cellule** (5 par sous-tour, 3 par espèce) + au plus une relance par cellule si la sortie est vide ou coupée, +
  **5 appels de contrôle** (1 024 jetons au plus chacun). Variante sans Argon : 12 + 4.
- **Pire cas** au barème du collisionneur, sans relance : **27,75 USD** (sous-commande `devis`) ; 27,52 USD sur les prompts réels de la
  course à blanc ; avec une relance sur chaque cellule : 79,55 USD (borne théorique, jamais atteinte : le plafond arrête avant).
  Contrôle : 0,18 USD au pire.
- **Attendu** d'après les coûts réels du tour brainstorm (mêmes jetons de sortie par cellule, jetons d'entrée rapportés à la
  longueur des prompts de ce tour) : **≈ 12,3 USD** (A 4,17 ; B 2,58 ; C 3,15 ; D 0,68 ; E 1,70). Plus bas que le brainstorm
  (22,69 USD) parce que les faits sont courts (23 085 octets) : prompt du premier sous-tour de 32 039 caractères au lieu de 270 365.
  La fourchette de la spécification (≈ 20 à 37 USD) supposait des faits de la taille de ceux du brainstorm.
- **Plafond proposé** : `PLAFOND_USD=34` (entier supérieur à 1,2 × 27,75 = 33,3) ; montant de la ligne de GO proposé : **35 USD**
  (34 au collisionneur + 0,18 au contrôle, arrondi). Variante sans Argon : 34 convient aussi (pire cas 21,07 ; attendu ≈ 8,2).
- Relais Kimi : plafond propre de 4 USD, 10 appels (inchangés du gabarit ; pire cas de Kimi 1,17 USD sans relance).

## Avant de lancer (la fille)
1. Ligne de GO dans `registres/go.md` avec le **mot direct de Lazar** (ta garde l'exige ; spécification, en tête) ; noter son `GO_ID`.
2. **Argon libre** : aucune autre utilisation d'Argon en cours (course Heimersheim, course de l'organisme sur Kirchner Q2, seconde
   course d'A1-v3). Le lanceur principal refuse si le port 8805 écoute sur la machine (relais ou commande Argon) ; la garde ne voit
   que cette machine : vérifier aussi les registres. Si Argon n'est pas libre : variante sans Argon (plus bas), déclarée.
3. Un Python avec `anthropic` (par exemple un environnement virtuel du bloc-notes de ta session), passé par **`PY_COLLISIONNEUR`**.
4. Clés présentes **par nom** dans l'environnement : `RR_ANTHROPIC_API_KEY_LUC`, `GEMINI_API_KEY_2`, `KIMI_API_KEY`,
   `OPENAI_API_KEY` (variante sans Argon : sans `GEMINI_API_KEY_2`). Jamais affichées, jamais en argument de ta commande.

## Commande exacte (arrière-plan détaché, puis attente suivie)
Dans le dossier `donnees/collisionneur-v9-kirchner-q2-v1/` de ton clone de la branche `donnees/collisionneur-v9-kirchner-q2-v1`
(le lanceur lit `/home/user/controle-ia-travail/registres/go.md` et le relais Kimi v3 de `/home/user/controle-ia-travail`) :

```bash
cd <ton-clone>/donnees/collisionneur-v9-kirchner-q2-v1 && \
for f in journal-kirchner-q2-v9-v1.log code-kirchner-q2-v9-v1.txt lanceur-kirchner-q2-v9-v1.pid; do [ ! -e "$f" ] || { echo "$f existe (R12)"; exit 2; }; done && \
GO_ID=GO-2026-11-03-NN PLAFOND_USD=34 PY_COLLISIONNEUR=/chemin/du/python \
  setsid nohup bash -c 'bash ./lancer-tour-kirchner-q2-v9-v1.sh; echo $? > code-kirchner-q2-v9-v1.txt' \
  > journal-kirchner-q2-v9-v1.log 2>&1 < /dev/null &
echo $! > lanceur-kirchner-q2-v9-v1.pid; cat lanceur-kirchner-q2-v9-v1.pid
```

Puis, **tout de suite**, l'attente suivie par ton harnais (Bash avec `run_in_background: true`, `timeout` 7200000), qui te réveille
à la fin ; la session doit rester active pendant toute la course (≈ 70 minutes au brainstorm ; bornes du lanceur : 600 s de contrôle
+ 6 900 s de tour) :

```bash
cd <ton-clone>/donnees/collisionneur-v9-kirchner-q2-v1 && P=$(cat lanceur-kirchner-q2-v9-v1.pid) && \
while kill -0 "$P" 2>/dev/null; do sleep 60; done; echo "code : $(cat code-kirchner-q2-v9-v1.txt 2>/dev/null)"; tail -n 5 journal-kirchner-q2-v9-v1.log
```

Si l'attente atteint ses 2 heures avant la fin, relance la même attente (le lanceur détaché continue). Ne lis aucune cellule.
Arrêt d'urgence : par le PID du lanceur (`lanceur-kirchner-q2-v9-v1.pid`) puis celui du relais (`relais-kimi-kirchner-q2-v1.pid`),
jamais par motif (R10).

**Variante sans Argon** (C absente, déclarée) : même commande avec `lancer-tour-kirchner-q2-v9-sans-argon-v1.sh` et les noms
`journal-kirchner-q2-v9-sans-argon-v1.log`, `code-kirchner-q2-v9-sans-argon-v1.txt`, `lanceur-kirchner-q2-v9-sans-argon-v1.pid` ;
run `run-kirchner-q2-e3-sans-argon-v1`. Le collisionneur v9 exige ses cinq lettres : C est rendue absente par
`--accepter-absence E3-T1-conception-C --accepter-absence E3-T2-critique-croisee-C --accepter-absence E3-T3-reponse-C`
(consigné au journal avant le premier appel, statut « jamais lancée » ; les autres espèces reçoivent le bloc « PIÈCE ABSENTE ») ;
contrôle restreint à ABDE par `appel_controle_v12.py` (copie de la v11 de la suite du 3 novembre, lettres permises A à E) ;
`GEMINI_API_KEY` factice dans l'environnement du collisionneur (un appel imprévu à C échoue sans dépense). Le préambule servi dit
toujours « cinq modèles » : à déclarer dans le rapport.

## Après la course (avant toute lecture)
1. `"$PY_COLLISIONNEUR" -I -B collisionneur_v9.py verifier run-kirchner-q2-e3-v1` (sans réseau ; réécrit `etat.md` : le faire
   **avant** de sceller).
2. Sceller tout le run et les journaux (`PYTHONPATH=src python -m controle_ia.scellement sceller …`, depuis la racine du clone),
   liste `EMPREINTES-tour-kirchner-q2-v9-v1.txt` ; le lanceur cherche déjà les valeurs des clés dans les sorties (« ALERTE »).
3. Contrôle des motifs avant la poussée (commande de session-depot) : un libellé de motif dans `balayage-faits.txt` peut donner un
   faux positif connu (déjà vu à 42aa6b1b) ; vérifier qu'il s'agit du libellé.
4. Commit, poussée de la branche ; sortie copiée à l'octet sur le canal par session-depot ; aucune lecture avant le protocole Kirchner.

## Ce qui reste non éprouvé
- Tout appel réel : relais Kimi réel, contrôle préalable, appel de contrôle (cinq ou quatre espèces), tour réel, recherche finale des
  clés ; durée réelle du tour.
- La garde Argon (port 8805) ne voit que la machine locale ; un usage d'Argon ailleurs (autre conteneur) lui échappe.
- Prix d'Argon et d'Astra supposés hauts dans le barème (10 / 50 USD par million) : le devis surestime C et E.
- L'attendu suppose des sorties de la longueur du brainstorm ; une question plus courte peut donner d'autres longueurs.
- Variante sans Argon : valeur factice de `GEMINI_API_KEY` jamais atteinte par un appel (aucun appelant C n'est joué).
- L'attente de 2 heures du harnais et la reprise de l'attente.
- Héritage du gabarit, inchangé : les valeurs des clés passent dans la liste d'arguments de `env -i` (relais, collisionneur) et de
  `grep -F` (recherche finale) du lanceur, comme au brainstorm et à la suite.

## Fichiers
`question.md`, `faits.md`, `balayage-faits.txt`, `assembler_faits_kirchner_v1.py`, `collisionneur_v9.py` (27e9ce40…),
`appel_controle_v10.py` (a451f910…, à l'octet), `appel_controle_v12.py`, `lancer-tour-kirchner-q2-v9-v1.sh`,
`lancer-tour-kirchner-q2-v9-sans-argon-v1.sh`, `course_a_blanc_kirchner_v1.py`, `course-a-blanc-kirchner-q2-v1.txt`,
`epreuves-kirchner-q2-v1.md`, ce LISEZMOI ; chacun avec son compagnon `.sha256`.

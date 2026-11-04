# Tour du collisionneur v9 sur la question Sparks (variante sans Argon) — LISEZMOI v1

Développeur neuf de l'instance fusionnée (conv-audit et session-depot), 4 novembre 2026, écrit à 01:36 UTC (`date -u`). Préparé
**sans aucun appel payant ni réseau vers un fournisseur**, pour la session fille, au modèle exact du kit Kirchner Q2 (branche
`donnees/collisionneur-v9-kirchner-q2-v1`, commit 16ec2e5a). Consigne : `docs/notes/weight-space-programming-v1/consigne-developpeur-kit-collisionneur-sparks-v1.md`
(ec50e112…). GO : `GO-2026-11-04-02` (registres/go.md, 35 USD, « Argon seulement si aucune course d'A1-v3 n'est en cours, sinon
variante sans Argon, déclarée »). Une seconde course d'A1-v3 occupe Argon : **seule la variante sans Argon est préparée**.

## Ce que fait le tour
Collisionneur v9 (`collisionneur_v9.py`, 27e9ce40…, copie à l'octet du kit modèle), étage III, trois sous-tours (conception à
l'aveugle, critique croisée, réponse), quatre espèces jouées : A Fable 5.1, B Opus 5.5, D Kimi K3.1 Pro (relais Kimi v3 local, port
8812), E GPT-6 Astra ; **C (Argon) absente, déclarée**. `--question question.md` (69d05369…, copie à l'octet de
`question-collisionneur-sparks-v1.md`, servie entière) ; `--faits faits.md` (65a613a3…, 85 493 octets) : ligne d'en-tête « pas de
web, pas d'exécution de code ; nouveauté : non cherchée », puis, dans cet ordre, la lecture factuelle (`piece-3-lecture-factuelle.md`,
fff05896…), le billet entier (`piece-1-billet.txt`, 49b2db7e…) et « nos résultats » v1 (`piece-2-nos-resultats.md`, d6fa8011…), chacune
à l'octet entre deux balises `DÉBUT FICHIER … sha256=…` / `FIN FICHIER …`, par `assembler_faits_sparks_v1.py` (empreintes des
pièces exigées ; mode « x » ; reproductible à l'octet). Balayage : 0 correspondance (`balayage-faits.txt`).

## Appels et devis (course à blanc : `course-a-blanc-sparks-v1.txt`)
- **12 appels de cellule** (4 par sous-tour, 3 par espèce) + au plus une relance par cellule si la sortie est vide ou coupée, +
  **4 appels de contrôle** (lettres ABDE, 1 024 jetons au plus chacun ; 0,18 USD au pire, borne du modèle à cinq espèces).
- **Pire cas sans relance**, variante sans Argon : **23,47 USD** (calcul : sous-commande `devis`, étage 3 = 29,92 USD, moins les trois
  cellules C, 6,45 USD) ; 22,64 USD sur les prompts réels de la course à blanc ; avec une relance sur chaque cellule : 64,76 USD
  (borne théorique, jamais atteinte : le plafond arrête avant).
- **Attendu** d'après les coûts réels du tour brainstorm (mêmes jetons de sortie par cellule, jetons d'entrée rapportés à la
  longueur des prompts de ce tour) : **≈ 10,2 USD** (A 4,64 ; B 2,77 ; D 0,75 ; E 2,03). Plus haut que Kirchner sans Argon (8,24) :
  faits de 85 493 octets au lieu de 23 085, prompt du premier sous-tour de 92 402 caractères au lieu de 32 039.
- **Plafond proposé** : `PLAFOND_USD=34` (1,2 × 23,47 = 28,16 ≤ 34, calcul) ; avec le contrôle, 34,18 ≤ 35 USD de la ligne de GO.
  L'assemblage sans le billet (`faits-sans-billet.md`) n'est donc **pas** produit (étape 7 de la consigne : seulement si 1,2 × pire
  cas > 34).
- Pour mémoire, cinq espèces (non préparé) : pire cas 29,92 USD, 1,2 × 29,92 = 35,90 > 34 (calcul) ; attendu ≈ 14,9 USD.
- Relais Kimi : plafond propre de 4 USD, 10 appels (inchangés du gabarit ; pire cas de Kimi 1,29 USD sans relance, calcul sur le devis).

## Changements par rapport au kit modèle (tous déclarés)
- `collisionneur_v9.py`, `appel_controle_v12.py` : copies à l'octet (27e9ce40…, f51ebd29…, égales aux compagnons du modèle).
  La docstring d'`appel_controle_v12.py` parle toujours de Kirchner : copie à l'octet exigée.
- `course_a_blanc_sparks_v1.py` : copie de `course_a_blanc_kirchner_v1.py` ; deux lignes changées : ligne 1 (« sur la question 2 du
  mentor Kirchner » → « sur la question Sparks (programmation dans l'espace des poids) ») et ligne 13 (nom du script dans l'usage).
  La date « 3 novembre 2026 » de la ligne 1 est celle du modèle, gardée.
- `assembler_faits_sparks_v1.py` : docstring, liste des pièces (trois, avec leurs empreintes) et ordre ; même code sinon.
- `lancer-tour-sparks-v9-sans-argon-v1.sh` : copie de `lancer-tour-kirchner-q2-v9-sans-argon-v1.sh` où `kirchner-q2` devient `sparks`
  aux lignes 9 et suivantes seulement, soit :
  - run `run-kirchner-q2-e3-sans-argon-v1` → `run-sparks-e3-sans-argon-v1` ;
  - contrôle `controle-kirchner-q2-sans-argon-v1.json` → `controle-sparks-sans-argon-v1.json` ;
  - journal du relais `relais-kimi-kirchner-q2-journal-sans-argon-v1.jsonl` → `relais-kimi-sparks-journal-sans-argon-v1.jsonl` ;
  - sortie du relais `relais-kimi-kirchner-q2-sans-argon-v1.log` → `relais-kimi-sparks-sans-argon-v1.log` ;
  - PID du relais `relais-kimi-kirchner-q2-sans-argon-v1.pid` → `relais-kimi-sparks-sans-argon-v1.pid` ;
  - état final du relais `relais-kimi-kirchner-q2-etat-final-sans-argon-v1.txt` → `relais-kimi-sparks-etat-final-sans-argon-v1.txt`.
  Même port 8812, mêmes trois `--accepter-absence`, même `GEMINI_API_KEY` factice, même contrôle ABDE. **Le commentaire d'en-tête
  (lignes 1 à 8) est gardé tel quel** : il parle encore de la question 2 du mentor Kirchner et de sa spécification ; un remplacement
  aveugle y aurait nommé deux fichiers inexistants (`specification-sparks-v1.md`, `lancer-tour-sparks-v9-v1.sh`).
- Pas de lanceur principal (cinq espèces) : Argon est occupé.

## Avant de lancer (la fille)
1. `GO-2026-11-04-02` présent dans `/home/user/controle-ia-travail/registres/go.md` (le lanceur le cherche là).
2. Un Python avec `anthropic` (par exemple un environnement virtuel du bloc-notes de ta session), passé par **`PY_COLLISIONNEUR`**.
3. Clés présentes **par nom** dans l'environnement : `RR_ANTHROPIC_API_KEY_LUC`, `KIMI_API_KEY`, `OPENAI_API_KEY` (`GEMINI_API_KEY_2`
   non exigée). Jamais affichées, jamais en argument de ta commande.
4. Relais Kimi v3 conforme dans `/home/user/controle-ia-travail/docs/notes/ideation-organisme-v1/relais-kimi-v1/` ; port 8812 libre.

## Commande exacte (arrière-plan détaché, puis attente suivie)
Dans le dossier `donnees/collisionneur-v9-sparks-v1/` de ton clone de la branche `donnees/collisionneur-v9-sparks-v1` :

```bash
cd <ton-clone>/donnees/collisionneur-v9-sparks-v1 && \
for f in journal-sparks-v9-sans-argon-v1.log code-sparks-v9-sans-argon-v1.txt lanceur-sparks-v9-sans-argon-v1.pid; do [ ! -e "$f" ] || { echo "$f existe (R12)"; exit 2; }; done && \
GO_ID=GO-2026-11-04-02 PLAFOND_USD=34 PY_COLLISIONNEUR=/chemin/du/python \
  setsid nohup bash -c 'bash ./lancer-tour-sparks-v9-sans-argon-v1.sh; echo $? > code-sparks-v9-sans-argon-v1.txt' \
  > journal-sparks-v9-sans-argon-v1.log 2>&1 < /dev/null &
echo $! > lanceur-sparks-v9-sans-argon-v1.pid; cat lanceur-sparks-v9-sans-argon-v1.pid
```

Puis, **tout de suite**, l'attente suivie par ton harnais (Bash avec `run_in_background: true`, `timeout` 7200000), qui te réveille
à la fin ; la session doit rester active pendant toute la course (bornes du lanceur : 600 s de contrôle + 6 900 s de tour) :

```bash
cd <ton-clone>/donnees/collisionneur-v9-sparks-v1 && P=$(cat lanceur-sparks-v9-sans-argon-v1.pid) && \
while kill -0 "$P" 2>/dev/null; do sleep 60; done; echo "code : $(cat code-sparks-v9-sans-argon-v1.txt 2>/dev/null)"; tail -n 5 journal-sparks-v9-sans-argon-v1.log
```

Si l'attente atteint ses 2 heures avant la fin, relance la même attente (le lanceur détaché continue). Ne lis aucune cellule.
Arrêt d'urgence : par le PID du lanceur (`lanceur-sparks-v9-sans-argon-v1.pid`) puis celui du relais
(`relais-kimi-sparks-sans-argon-v1.pid`), jamais par motif (R10).

C absente : le collisionneur v9 exige ses cinq lettres ; ses trois cellules C reçoivent `--accepter-absence` (consigné au journal
avant le premier appel, statut « jamais lancée ») ; les autres espèces reçoivent le bloc « PIÈCE ABSENTE ». Le préambule servi dit
toujours « cinq modèles » : à déclarer dans le rapport.

## Après la course (avant toute lecture)
1. `"$PY_COLLISIONNEUR" -I -B collisionneur_v9.py verifier run-sparks-e3-sans-argon-v1` (sans réseau ; réécrit `etat.md` : le faire
   **avant** de sceller).
2. Sceller tout le run et les journaux (`PYTHONPATH=src python -m controle_ia.scellement sceller …`, depuis la racine du clone),
   liste `EMPREINTES-tour-sparks-v9-sans-argon-v1.txt` ; le lanceur cherche déjà les valeurs des clés dans les sorties (« ALERTE »).
3. Contrôle des motifs avant la poussée : un libellé de motif dans `balayage-faits.txt` peut donner un faux positif connu ; vérifier
   qu'il s'agit du libellé.
4. Commit, poussée de la branche ; aucune lecture avant le protocole de lecture fixé par la mère.

## Épreuves sans appel faites ici (copies neuves hors du dépôt, `env -i`, mandataire mort, Python factice avec un module `anthropic` vide)
Lanceur sans Argon : sain → code 2 « RR_ANTHROPIC_API_KEY_LUC absente » (toutes les gardes de structure passent, GO trouvé) ; sans
`GO_ID` → code 1 ; GO absent (`GO-2099-01-01-99`) → code 2 ; `run-sparks-e3-sans-argon-v1` présent → code 2 (R12) ; un octet ajouté à
`faits.md` → code 2 « empreintes non conformes » ; Python sans `anthropic` → code 2. Copie inchangée hors l'artefact planté.
Assembleur : billet altéré d'un octet → code 1, rien d'écrit ; sortie existante → refus (mode « x ») ; second assemblage identique à
l'octet. Garde du plafond : course à blanc à 5 USD, arrêt code 4 avant l'appel qui l'aurait franchi.

## Ce qui reste non éprouvé
- Tout appel réel : relais Kimi réel, contrôle préalable, appel de contrôle à quatre espèces, tour réel, recherche finale des clés ;
  durée réelle du tour (prompts trois fois plus longs que Kirchner, trois fois plus courts que le brainstorm).
- Valeurs des clés absentes de cette session : la recherche des valeurs dans `faits.md` et `question.md` n'a pas été faite (motifs seuls).
- Prix d'Astra supposé haut dans le barème (50 USD par million) : le devis surestime E.
- L'attendu suppose des sorties de la longueur du brainstorm.
- Valeur factice de `GEMINI_API_KEY` jamais atteinte par un appel (aucun appelant C n'est joué).
- Héritage du gabarit, inchangé : les valeurs des clés passent dans la liste d'arguments de `env -i` (relais, collisionneur) et de
  `grep -F` (recherche finale) du lanceur.

## Fichiers
`question.md`, `faits.md`, `balayage-faits.txt`, `assembler_faits_sparks_v1.py`, `collisionneur_v9.py` (27e9ce40…),
`appel_controle_v12.py` (f51ebd29…), `lancer-tour-sparks-v9-sans-argon-v1.sh`, `course_a_blanc_sparks_v1.py`,
`course-a-blanc-sparks-v1.txt`, ce LISEZMOI, `RAPPORT-developpeur-v1.md` ; chacun avec son compagnon `.sha256`.

# Tour du collisionneur v9 sur la conception de l'organisme d'idéation — LISEZMOI v1

Session développeur de session-depot, 3 novembre 2026, écrit à 11:14 UTC (`date -u`). Préparé **sans aucun appel payant**, pour la
session fille (conv-audit n° 412). Spécification : `specification-collisionneur-conception-organisme-v1.md` (7de4cb16…), sur
`canal/conv-audit-n04` (66e951da). Même gabarit que le tour Kirchner Q2 (branche `donnees/collisionneur-v9-kirchner-q2-v1`, 16ec2e5a).

## Ce que fait le tour
Collisionneur v9 (`collisionneur_v9.py`, 27e9ce40…, à l'octet), étage III, trois sous-tours, cinq espèces (A Fable 5.1, B Opus 5.5,
C Argon, D Kimi K3.1 Pro par le relais Kimi v3 local au port 8812, E GPT-6 Astra).
- `question.md` (559bfae1…, 3 151 octets) : **les trois sections servies** de `question-collisionneur-conception-organisme-v1.md`
  (b7420561…), à l'octet, de « ## La demande, telle que Lazar l'a écrite … » à la fin de « ## Règles d'intégrité … » ; titre,
  provenance et « Lecture prévue » non servis ; lignes vides de fin réduites à un saut de ligne
  (`extraire_question_conception_organisme_v1.py`, empreinte de la source exigée, trois titres vérifiés).
- `faits.md` (92a6393f…, 99 397 octets, 97 536 caractères) : en-tête « pas de web, pas d'exécution de code ; nouveauté : non
  cherchée », puis, dans l'ordre et chacune à l'octet entre deux balises `DÉBUT FICHIER … sha256=…` / `FIN FICHIER …` :
  README public d'`ideation-organism` à 4848ad97 (bdd6516f…) ; `piece-etat-reel-organisme-v1.md` (09a4a028…) ;
  `piece-kirchner-v2.md` (6e7fb1c5…) ; `piece-lecture-2608-28945-parties-factuelles-v1.md` (4ab6c9d7…) ;
  `piece-nos-resultats-v1.md` (d6fa8011…) — `assembler_faits_conception_organisme_v1.py`, cinq empreintes exigées.
- **Non servis** : l'analyse gelée de conv-audit et le protocole de croisement (aucun des deux n'est lu par les scripts).
- Balayage (`balayage-faits.txt`) : 0 correspondance aux motifs de clé et aux valeurs des quatre clés (par nom). À savoir : le README
  public contient l'adresse électronique de contact publiée de Lazar (ligne « Contact »), servie telle quelle avec le README entier,
  comme le veut la spécification ; aucune autre adresse.

## Appels et devis (course à blanc : `course-a-blanc-conception-organisme-v1.txt`)
- **15 appels de cellule** (5 par sous-tour, 3 par espèce), au plus une relance par cellule (sortie vide ou coupée), **5 appels de
  contrôle**. Variante sans Argon : 12 + 4.
- **Pire cas** au barème du collisionneur, sans relance : **30,32 USD** (sous-commande `devis`) ; 30,09 USD sur les prompts de la
  course à blanc ; avec une relance sur chaque cellule : 84,68 USD (borne théorique ; le plafond arrête avant). Contrôle : 0,18 USD au pire.
- **Attendu** d'après les coûts réels du tour brainstorm (mêmes jetons de sortie par cellule, jetons d'entrée rapportés à la longueur
  des prompts de ce tour) : **≈ 15,4 USD** (A 5,20 ; B 3,00 ; C 3,96 ; D 0,83 ; E 2,41). La question borne la conception à
  1 500 mots : l'attendu, calé sur des sorties de brainstorm, est plutôt haut.
- **Plafond proposé** : `PLAFOND_USD=37` (entier supérieur à 1,2 × 30,32 = 36,4) ; **montant de la ligne de GO proposé : 38 USD**
  (37 au collisionneur + 0,18 au contrôle, arrondi). Variante sans Argon : pire cas 22,92, attendu ≈ 10,6 ; 37 convient aussi.
- Relais Kimi : plafond propre 4 USD, 10 appels (gabarit inchangé) ; pire cas de Kimi 1,31 USD sans relance.

## Avant de lancer (la fille)
1. Ligne de GO dans `registres/go.md` avec le **mot direct de Lazar** (la spécification le demande) ; noter son `GO_ID`.
2. **Ordre sur Argon** : après le tour et la course Kirchner Q2, avant la seconde course d'A1-v3, jamais deux usages d'Argon à la
   fois. **Si A1-v3 est déjà partie : variante sans Argon, sans attendre** (spécification, § 2). Le lanceur principal refuse si le
   port 8805 écoute sur la machine ; la garde ne voit que cette machine : vérifier aussi les registres.
3. Le tour Kirchner Q2 fini : même port 8812 ; la garde du port refuse si son relais Kimi écoute encore **sur cette machine**.
4. Un Python avec `anthropic`, passé par `PY_COLLISIONNEUR` ; clés présentes **par nom** : `RR_ANTHROPIC_API_KEY_LUC`,
   `GEMINI_API_KEY_2` (pas pour la variante sans Argon), `KIMI_API_KEY`, `OPENAI_API_KEY`.

## Commande exacte (corrigée : garde R12 au premier plan, puis lancement détaché)
Trois instructions sur des lignes séparées (aucun `&&` qui mettrait la garde dans l'arrière-plan ; c'est le défaut de la commande
Kirchner). Dans le dossier `donnees/collisionneur-v9-conception-organisme-v1/` de ton clone de la branche
`donnees/collisionneur-v9-conception-organisme-v1` :

```bash
cd <ton-clone>/donnees/collisionneur-v9-conception-organisme-v1 || exit 2
for f in journal-conception-organisme-v9-v1.log code-conception-organisme-v9-v1.txt lanceur-conception-organisme-v9-v1.pid; do [ ! -e "$f" ] || { echo "$f existe (R12) : rien n'est lancé"; exit 2; }; done
GO_ID=GO-2026-11-03-NN PLAFOND_USD=37 PY_COLLISIONNEUR=/chemin/du/python setsid nohup bash -c 'bash ./lancer-tour-conception-organisme-v9-v1.sh; echo $? > code-conception-organisme-v9-v1.txt' > journal-conception-organisme-v9-v1.log 2>&1 < /dev/null &
echo $! > lanceur-conception-organisme-v9-v1.pid; echo "lanceur détaché, PID $(cat lanceur-conception-organisme-v9-v1.pid)"
```

Éprouvée telle quelle (épreuves 20 et 21, sans clé) : fichiers absents → lancement, PID écrit après la garde ; journal présent →
refus, rien de lancé. Puis, **tout de suite**, l'attente suivie par ton harnais (Bash avec `run_in_background: true`, `timeout`
7200000), qui te réveille à la fin ; la session reste active pendant toute la course :

```bash
cd <ton-clone>/donnees/collisionneur-v9-conception-organisme-v1 && P=$(cat lanceur-conception-organisme-v9-v1.pid) && \
while kill -0 "$P" 2>/dev/null; do sleep 60; done; echo "code : $(cat code-conception-organisme-v9-v1.txt 2>/dev/null)"; tail -n 5 journal-conception-organisme-v9-v1.log
```

Si l'attente atteint ses 2 heures, relance-la (le lanceur détaché continue). Ne lis aucune cellule. Arrêt d'urgence : par le PID du
lanceur puis celui du relais (`relais-kimi-conception-organisme-v1.pid`), jamais par motif (R10).

**Variante sans Argon** (C absente, déclarée) : mêmes trois instructions avec `lancer-tour-conception-organisme-v9-sans-argon-v1.sh`
et les noms `journal-conception-organisme-v9-sans-argon-v1.log`, `code-conception-organisme-v9-sans-argon-v1.txt`,
`lanceur-conception-organisme-v9-sans-argon-v1.pid` (dans la garde R12 aussi) ; run `run-conception-organisme-e3-sans-argon-v1`.
C est rendue absente par `--accepter-absence` sur `E3-T1-conception-C`, `E3-T2-critique-croisee-C`, `E3-T3-reponse-C` (consigné au
journal avant le premier appel) ; contrôle ABDE par `appel_controle_v12.py` ; `GEMINI_API_KEY` factice. Le préambule servi dit
toujours « cinq modèles » : à déclarer.

## Après la course (avant toute lecture)
1. `"$PY_COLLISIONNEUR" -I -B collisionneur_v9.py verifier run-conception-organisme-e3-v1` (sans réseau ; réécrit `etat.md` : avant
   de sceller).
2. Sceller le run et les journaux, liste `EMPREINTES-tour-conception-organisme-v9-v1.txt` ; le lanceur cherche déjà les valeurs des
   clés dans les sorties.
3. Contrôle des motifs avant la poussée ; un libellé de motif de `balayage-faits.txt` peut donner le faux positif connu.
4. Commit, poussée ; cellules copiées à l'octet sur la branche du canal de conv-audit avec leur liste de copie scellée.

## Ce qui reste non éprouvé
- Tout appel réel (relais, contrôle, tour), durée réelle ; prix d'Argon et d'Astra supposés hauts.
- Gardes Argon (8805) et port (8812) : machine locale seulement.
- L'attendu suppose des sorties de la longueur du brainstorm.
- Valeur factice de `GEMINI_API_KEY` (variante sans Argon) jamais atteinte.
- Hérité du gabarit : valeurs des clés en argument de `env -i` et de `grep -F` dans le lanceur.

## Fichiers
`question.md`, `faits.md`, `balayage-faits.txt`, `extraire_question_conception_organisme_v1.py`,
`assembler_faits_conception_organisme_v1.py`, `collisionneur_v9.py`, `appel_controle_v10.py` (a451f910…), `appel_controle_v12.py`
(f51ebd29…), `lancer-tour-conception-organisme-v9-v1.sh`, `lancer-tour-conception-organisme-v9-sans-argon-v1.sh`,
`course_a_blanc_conception_organisme_v1.py`, `course-a-blanc-conception-organisme-v1.txt`, `epreuves-conception-organisme-v1.md`,
ce LISEZMOI ; chacun avec son compagnon `.sha256`.

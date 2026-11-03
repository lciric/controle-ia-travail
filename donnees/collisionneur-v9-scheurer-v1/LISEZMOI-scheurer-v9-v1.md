# Tour du collisionneur v9 sur la question de Jérémy Scheurer — LISEZMOI v1

Session développeur de session-depot, 3 novembre 2026, écrit à 11:37 UTC (`date -u`). Préparé **sans aucun appel payant**, pour la
session fille, sur conv-audit n° 416 (e5d2f7af…) et n° 417 (empreintes des pièces). Gabarit : tour Kirchner Q2 (16ec2e5a) ; commande
corrigée du tour sur la conception (676495c9 : garde R12 au premier plan). **Lancement prévu : variante sans Argon**, en parallèle
avec les deux autres tours du soir (ports Kimi 8814, 8815, 8816) ; la variante cinq espèces est prête en second.

## Ce que fait le tour
Collisionneur v9 (`collisionneur_v9.py`, 27e9ce40…, à l'octet), étage III, trois sous-tours (conception, critique croisée, réponse).
- `question.md` (4a53414d…) : les trois sections servies de `question-collisionneur-scheurer-v1.md` (« La question… », « Ce qu'on attend de chaque espèce »,
  « Règles d'intégrité »), à l'octet, par `extraire_question_scheurer_v1.py` (empreinte de la source exigée).
- `faits.md` (7d1a27e3…, 15383 octets) : en-tête « pas de web, pas d'exécution de code ; nouveauté : non cherchée », puis
  `piece-scheurer-v1.md` (2d0e60fc…), puis `piece-nos-resultats-v1.md` (d6fa8011…), chacune à l'octet entre ses balises, par
  `assembler_faits_scheurer_v1.py` (empreintes exigées). Balayage : `balayage-faits.txt`.
- Relais Kimi v3 au port **8815** (propre à ce tour), plafond du relais 4 USD, 10 appels (gabarit) ; pire cas de Kimi 1.15 USD.

## Devis (course à blanc : `course-a-blanc-scheurer-v1.txt`)
| Variante | Appels | Pire cas sans relance | Attendu | `PLAFOND_USD` (entier > 1,2 × pire cas) | Montant de GO proposé |
|---|---|---|---|---|---|
| **sans Argon (lancement)** | 12 cellules + 4 contrôles | **21.61 USD** | **≈ 7.9 USD** | **26** | **27 USD** |
| cinq espèces | 15 cellules + 5 contrôles | 27.34 USD | ≈ 11.8 USD | 33 | 34 USD |

Pire cas : barème du collisionneur (sous-commande `devis`, cinq espèces ; sans Argon = ses lignes hors C). Attendu : coûts réels du
tour brainstorm (jetons de sortie par cellule, jetons d'entrée rapportés à la longueur des prompts de ce tour) ; par espèce, sans
Argon : A 3.60, B 2.36, D 0.60, E 1.31 ; la question borne la conception à 1 200 mots, l'attendu est plutôt haut. Contrôle : ≤ 0,18 USD (montant de
GO = plafond + 1). Une relance par cellule (sortie vide ou coupée) reste sous le plafond : le collisionneur vérifie le pire cas
avant chaque appel et s'arrête en code 4.

## Avant de lancer (la fille)
1. Ligne de GO dans `registres/go.md` avec le **mot direct de Lazar** ; noter son `GO_ID` (une ligne pour les trois tours, ou une par tour).
2. Python avec `anthropic` dans `PY_COLLISIONNEUR` ; clés présentes **par nom** : `RR_ANTHROPIC_API_KEY_LUC`, `KIMI_API_KEY`,
   `OPENAI_API_KEY` (et `GEMINI_API_KEY_2` pour la variante cinq espèces seulement).
3. Les trois tours partent ensemble : trois relais Kimi (8814, 8815, 8816), mêmes clés ; aucun fichier partagé entre les dossiers.

## Commande exacte (variante sans Argon ; garde R12 au premier plan, puis lancement détaché)
Quatre instructions, lignes séparées, dans le dossier `donnees/collisionneur-v9-scheurer-v1/` de ton clone de la branche
`donnees/collisionneur-v9-scheurer-v1` (le lanceur lit `/home/user/controle-ia-travail/registres/go.md` et le relais Kimi v3 de
`/home/user/controle-ia-travail`) :

```bash
cd <ton-clone>/donnees/collisionneur-v9-scheurer-v1 || exit 2
for f in journal-scheurer-v9-sans-argon-v1.log code-scheurer-v9-sans-argon-v1.txt lanceur-scheurer-v9-sans-argon-v1.pid; do [ ! -e "$f" ] || { echo "$f existe (R12) : rien n'est lancé"; exit 2; }; done
GO_ID=GO-2026-11-03-NN PLAFOND_USD=26 PY_COLLISIONNEUR=/chemin/du/python setsid nohup bash -c 'bash ./lancer-tour-scheurer-v9-sans-argon-v1.sh; echo $? > code-scheurer-v9-sans-argon-v1.txt' > journal-scheurer-v9-sans-argon-v1.log 2>&1 < /dev/null &
echo $! > lanceur-scheurer-v9-sans-argon-v1.pid; echo "lanceur détaché, PID $(cat lanceur-scheurer-v9-sans-argon-v1.pid)"
```

Éprouvée telle quelle, sans clé (épreuves, `epreuves-scheurer-v1.md`). Puis, **tout de suite**, l'attente suivie par ton harnais (Bash
avec `run_in_background: true`, `timeout` 7200000), qui te réveille à la fin ; la session reste active pendant toute la course :

```bash
cd <ton-clone>/donnees/collisionneur-v9-scheurer-v1 && P=$(cat lanceur-scheurer-v9-sans-argon-v1.pid) && \
while kill -0 "$P" 2>/dev/null; do sleep 60; done; echo "code : $(cat code-scheurer-v9-sans-argon-v1.txt 2>/dev/null)"; tail -n 5 journal-scheurer-v9-sans-argon-v1.log
```

Si l'attente atteint 2 heures, relance-la. Ne lis aucune cellule. Arrêt d'urgence par PID (lanceur, puis
`relais-kimi-scheurer-sans-argon-v1.pid`), jamais par motif (R10). Variante sans Argon : run `run-scheurer-e3-sans-argon-v1` ; C absente par
`--accepter-absence` sur `E3-T1-conception-C`, `E3-T2-critique-croisee-C`, `E3-T3-reponse-C` (journal, avant le premier appel) ;
contrôle ABDE (`appel_controle_v12.py`) ; `GEMINI_API_KEY` factice ; le préambule dit toujours « cinq modèles » : à déclarer.

**Variante cinq espèces** (seulement si Argon est libre au départ) : mêmes instructions avec `lancer-tour-scheurer-v9-v1.sh` et les noms
`journal-scheurer-v9-v1.log`, `code-scheurer-v9-v1.txt`, `lanceur-scheurer-v9-v1.pid`, `PLAFOND_USD=33` ; run `run-scheurer-e3-v1` ;
la garde refuse si le port 8805 (Argon) écoute sur la machine.

## Après la course (avant toute lecture)
1. `"$PY_COLLISIONNEUR" -I -B collisionneur_v9.py verifier run-scheurer-e3-sans-argon-v1` (sans réseau ; réécrit `etat.md` : avant de sceller).
2. Sceller le run et les journaux, liste `EMPREINTES-tour-scheurer-v9-v1.txt` ; le lanceur cherche déjà les valeurs des clés dans les sorties.
3. Contrôle des motifs avant la poussée (faux positif connu possible : libellé de motif dans `balayage-faits.txt`).
4. Commit, poussée ; copie à l'octet sur le canal, sonnette (n° 416).

## Ce qui reste non éprouvé
- Tout appel réel (relais, contrôle, tour), durée réelle, trois tours en parallèle sur les mêmes comptes (limites de débit).
- Gardes de port (8805, 8815) : machine locale seulement.
- L'attendu suppose des sorties de la longueur du brainstorm ; prix d'Argon et d'Astra supposés hauts.
- Valeur factice de `GEMINI_API_KEY` (sans Argon) jamais atteinte par un appel.
- Hérité du gabarit : valeurs des clés en argument de `env -i` et de `grep -F` dans le lanceur.

## Fichiers
`question.md`, `faits.md`, `balayage-faits.txt`, `extraire_question_scheurer_v1.py`, `assembler_faits_scheurer_v1.py`,
`collisionneur_v9.py`, `appel_controle_v10.py` (a451f910…), `appel_controle_v12.py` (f51ebd29…), `lancer-tour-scheurer-v9-sans-argon-v1.sh`,
`lancer-tour-scheurer-v9-v1.sh`, `course_a_blanc_scheurer_v1.py`, `course-a-blanc-scheurer-v1.txt`, `epreuves-scheurer-v1.md`, ce
LISEZMOI ; chacun avec son compagnon `.sha256`.

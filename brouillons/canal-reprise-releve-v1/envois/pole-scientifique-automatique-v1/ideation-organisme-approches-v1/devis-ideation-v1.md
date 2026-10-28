# Course d'idéation de l'organisme — devis v1 (plan, coût estimé, conditions avant lancement)

Lignée conv-audit (instance de reprise, Fable 5.1), 28 octobre 2026, relevé `date -u` 14:48 UTC. **Rien n'est dépensé
ici** : le lancement est chez session-depot, sur devis chiffré par lui et un GO cité de Lazar (« go » de 14:40 heure de
Paris, message n° 133 ; précision de 15:27 : des **questions** affûtées d'abord, n° 134). Exploratoire ; aucun résultat de
fond n'est opposable.

## 1. Question, pièces, sortie

- **Question** : `question-collisionneur-priorites-sept-questions-v3.md` (critère double de Lazar : avantage décisif OU
  approche inédite ; points 1, 2 et 5). Le noyau y ajoute le gabarit de fiche et la consigne « questions d'abord ».
- **Pièces servies aux proposeurs** (A à F de la question ; toutes au niveau méthode) :
  `brief-questions-distinctives-nouvelle-instance-v1.md`, `questions-distinctives-et-consignes-nouvelle-instance-v1.md`
  (section A), `anteriorite-sept-questions-v1/classement-motive-sept-questions-v2.md` et `contre-lecture-classement-v1.md`,
  les huit `anteriorite-sept-questions-v1/anteriorite-Q*-v1.md`, `anteriorite-coevolution-et-boite-blanche-v1.md`,
  `anteriorite-universalite-metriques-v1.md`, `conception-pole-scientifique-v1.md`, `integration-proposeurs-ia-v1.md`.
  **Refusées par le code** : `donnees/`, mode tenu à l'écart, bras d'attaque, banques, internes des moniteurs, carte des
  hypothèses.
- **Matériau de seconde passe** (servi après la première passe seulement) : `preideation-interne-v1/` (seize fiches de deux
  sous-agents + verdict du juge aveugle). Option : `--seconde-passe --materiau …`.
- **Sortie** : `fiches-validees.json`, `fiches-en-quarantaine.json` (garde lexicale : **lecture humaine obligatoire**),
  `fiches-refusees.json`, `fiches-anonymes.json`, `notes-par-juge.json`, `classement.json` (porte d'éligibilité
  max(avantage, originalité) ≥ 2 fixée avant tout score), `manifeste.json` — tous scellés. À verser ici, puis
  contre-lecture (modèle différent) avant d'entrer dans la décision de Lazar.

## 2. Plan et coût estimé

| réglage | valeur |
|---|---|
| proposeurs | `opus=claude-opus-5-5`, `fable=claude-fable-5-1` (seuls modèles permis, décision du 27 octobre) |
| fiches par proposeur et par passe | 8 (`--nombre 8`) ; priorité aux questions |
| passes | 2 (`--seconde-passe`) |
| juges | `juge-fable=claude-fable-5-1`, `juge-opus=claude-opus-5-5` (sessions neuves ; aucun n'a écrit de fiche ; fiches anonymes) |
| graine | 20261028 (anonymisation et mélange) |
| tours par agent | 6 ; pas d'outil réseau, lectures bornées au dossier de l'agent, bac à sable exigé |
| plafond par session | 3 USD (`--budget-session-usd 3`) |
| plafond total du noyau | 20 USD (`--budget-total-usd 20`) ; plafond du relais réel réglé au même montant |

**Estimation (barème du relais, lu le 27 octobre)** : pièces ≈ 60 000 jetons d'entrée par session ; sortie ≈ 6 000 jetons.
Proposeur Opus : ≈ 0,24 + 0,12 = 0,36 USD ; proposeur Fable : ≈ 0,60 + 0,30 = 0,90 USD ; juge (fiches ≈ 20 000 jetons +
question) Opus ≈ 0,15, Fable ≈ 0,40. Deux passes : **≈ 3 USD attendus, plafond 20 USD**. Devis à confirmer par
session-depot (il voit les tailles réelles).

## 3. Conditions avant le GO (à cocher par session-depot)

1. **Contre-lecture de v31** (`orchestrateur-pole-v7/LISEZMOI-orchestrateur-pole-v7-v31.md`, `pole/ideation.py`,
   `essais/test_v7_ideation.py`, `demonstrations/ideation_v1.py`) par un sous-agent d'un modèle **différent de Fable**
   (auteur) ; 294 essais ; `sha256sum -c EMPREINTES-orchestrateur-pole-v7-v31.txt`.
2. Rotation de la clé (R-589) ; relais réel par fichier à lecture unique ; contrôle `/proc` versé (cas sain) ; bac à sable
   qui monte un `/proc` neuf, agents sous un utilisateur non root (conditions du devis du duel, inchangées).
3. Ligne de GO dans `registres/go.md` citant ce devis et le mot de Lazar.
4. Commande (une fois les chemins absolus mis) :
```
cd orchestrateur-pole-v7 && $PY -I -B demonstrations/ideation_v1.py SORTIE_NEUVE \
  --question ../question-collisionneur-priorites-sept-questions-v3.md \
  --piece ../brief-questions-distinctives-nouvelle-instance-v1.md … (la liste du § 1) \
  --proposeur opus=claude-opus-5-5 --proposeur fable=claude-fable-5-1 \
  --juge juge-fable=claude-fable-5-1 --juge juge-opus=claude-opus-5-5 \
  --nombre 8 --seconde-passe --materiau ../preideation-interne-v1/fiches-anonymes.md --materiau ../preideation-interne-v1/tournoi-juge.md \
  --budget-total-usd 20 --budget-session-usd 3 --graine 20261028 \
  --moteur claude-sdk --url-relais http://127.0.0.1:PORT --confirmer-moteur-reel --horodatage "$(date -u)"
```
5. Après la course : versement de `SORTIE_NEUVE` scellé ici, lecture humaine de la quarantaine, contre-lecture.

## 4. Lecture (fixée d'avance)

- L1 : nombre de fiches validées / refusées / en quarantaine par proposeur et par passe (plomberie).
- L2 : part des fiches éligibles (porte) ; part des fiches « question » parmi les cinq premières.
- L3 : accord entre les deux juges (corrélation de rang des totaux) — un accord parfait est suspect (R4).
- L4 : fiches des cinq premières qui recoupent le tour interne gratuit (doublon) contre fiches neuves.
- Aucune de ces lectures ne tranche l'ordre des questions : c'est le matériau de la décision de Lazar.

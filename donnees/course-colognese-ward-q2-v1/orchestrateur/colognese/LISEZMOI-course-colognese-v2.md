# LISEZMOI — course Colognese-Ward Q2, kit v2 : variantes sans Opus

> **R12 au premier plan** : aucun fichier de ce kit ne se modifie. Toute correction prend un **nom neuf** (`…-v3`), de nouvelles
> empreintes, une nouvelle table des pièces gelées, une nouvelle répétition. Les trois configurations v1 ne sont jamais réécrites.

Rédigé le 3 novembre 2026, 15:17 UTC (`date -u`), par un sous-agent de session-depot. **Rien n'a été lancé de payant.** v2 = kit v1
(`LISEZMOI-course-colognese-v1.md`, gardé) plus deux variantes sans Opus, sur le modèle exact de Jang-Feng v2, après le premier run
arrêté sur un refus d'Opus (C13 ; `donnees/course-colognese-ward-q2-v1-run`, `53baefe6`). Fiche :
`docs/notes/ideation-organisme-v1/course-colognese-ward-q2-v1/fiche-lancement-course-colognese-ward-q2-v1-brouillon2.md`.

Pièces neuves : `course_colognese_v2.py`, `lancer_course_colognese_v2.py`, `lancer-course-colognese-v2.sh` (cinq configurations),
`calcul_devis_course_colognese_v2.py`, `devis-course-colognese-v2.{txt,json}`, `configuration-course-colognese-ward-q2-v1-sans-opus.json`
(S17 198, `GO-2026-11-03-15`), `configuration-course-colognese-ward-q2-v1-sans-opus-argon.json` (S17 237, `GO-2026-11-03-16`), table v2
(61 pièces), course à blanc v2, 57 essais, dix mutations, répétition v2 et leurs résultats.

**Règle** : second run dans un dossier neuf, `sans-opus-argon` si Argon est libre, sinon `sans-opus` ; **si Fable refuse à son tour, la
course s'arrête sans aucune relance** (R-1161). Le lanceur ne vérifie que la ligne de son 2ᵉ argument (= `GO_ID`), au montant du S17.

## Commandes exactes (en arrière-plan ; dossier du run NEUF, hors du clone)

```
cd /home/user/controle-ia-travail/donnees/course-colognese-ward-q2-v1/orchestrateur/colognese
mkdir -p /home/user/runs-course-colognese-ward-q2-v1
RUN=/home/user/runs-course-colognese-ward-q2-v1/run-$(date -u +%Y%m%d-%H%M)-sans-opus
```
Argon libre :
```
GO_ID=GO-2026-11-03-16 PY_RELAIS_CLAUDE=/home/user/venv-relais-claude/bin/python nohup bash lancer-course-colognese-v2.sh lancer \
  GO-2026-11-03-16 configuration-course-colognese-ward-q2-v1-sans-opus-argon.json "$RUN" FICHE_SCELLEE RAPPORT_SCELLE > "$RUN.demarrage.log" 2>&1 &
```
Argon pris :
```
GO_ID=GO-2026-11-03-15 PY_RELAIS_CLAUDE=/home/user/venv-relais-claude/bin/python nohup bash lancer-course-colognese-v2.sh lancer \
  GO-2026-11-03-15 configuration-course-colognese-ward-q2-v1-sans-opus.json "$RUN" FICHE_SCELLEE RAPPORT_SCELLE > "$RUN.demarrage.log" 2>&1 &
```
Journal : `$RUN/journal-lancement-course-colognese-v1.log` (nom hérité). **Arrêt (R10)** : `kill <PID du lanceur>` (code 130).

## Essais (zéro dépense)

```
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 PYTHONDONTWRITEBYTECODE=1 HOME=/tmp PY_AVEC_ANTHROPIC -B -m pytest -q -p no:cacheprovider test_course_colognese_v2.py
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 PYTHONDONTWRITEBYTECODE=1 PY_AVEC_ANTHROPIC -I -B mutations_colognese_v2.py
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 /usr/bin/python3 -I -B course_a_blanc_colognese_v2.py --dossier /tmp/blanc-colognese-NOUVEAU --rapport /tmp/blanc-colognese-NOUVEAU.txt
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 PY_RELAIS_CLAUDE=PY_AVEC_ANTHROPIC bash repetition/repetition_complete_colognese_v2.sh /tmp/repetition-colognese-NOUVEAU
```

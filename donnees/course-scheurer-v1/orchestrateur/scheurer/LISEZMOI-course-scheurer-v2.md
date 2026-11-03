# LISEZMOI — course Scheurer, kit v2 : variante sans Claude

> **R12 au premier plan** : aucun fichier de ce kit ne se modifie. Toute correction prend un **nom neuf** (`…-v3`), de nouvelles
> empreintes, une nouvelle table des pièces gelées, une nouvelle répétition. Les cinq configurations v1 ne sont jamais réécrites.

Rédigé le 3 novembre 2026, 14:55 UTC (`date -u`), par un sous-agent de session-depot. **Rien n'a été lancé de payant.** v2 = kit v1
(`LISEZMOI-course-scheurer-v1.md`, gardé) plus la variante `sans-claude` (proposeurs Argon, Kimi, Astra ; aiguilleur Astra ; juges
Astra et Argon ; lecteurs Astra et Argon ; metteur Astra ; aucun modèle Claude ; relais 8806 non démarré). Fiche :
`docs/notes/ideation-organisme-v1/course-scheurer-v1/fiche-lancement-course-scheurer-v2-brouillon1.md`.

Pièces neuves : `course_scheurer_v2.py`, `lancer_course_scheurer_v2.py`, `lancer-course-scheurer-v2.sh`, `calcul_devis_course_scheurer_v2.py`,
`devis-course-scheurer-v2.{txt,json}`, `configuration-course-scheurer-v1-sans-claude.json` (S17 130 USD), `table_pieces_gelees_scheurer_v2.py`,
`course_a_blanc_scheurer_v2.py`, `course-a-blanc-scheurer-v2.txt`, `test_course_scheurer_v2.py` (64 essais), `mutations_scheurer_v2.py`
(douze mutations), `repetition/repetition_complete_scheurer_v2.sh` et leurs résultats.

**Ligne de GO** : `GO-2026-11-03-15`, 130 USD (plafond technique), inscrite par session-depot après le mot direct de Lazar sur cette
variante. Relais Argon 20,7 USD (au-dessus de la règle « ≤ 10 », accepté pour cette seule variante ; dépense lue au registre à la fin).

## Commande exacte (en arrière-plan ; dossier du run NEUF, hors du clone)

```
cd /home/user/controle-ia-travail/donnees/course-scheurer-v1/orchestrateur/scheurer
mkdir -p /home/user/runs-course-scheurer-v1
RUN=/home/user/runs-course-scheurer-v1/run-$(date -u +%Y%m%d-%H%M)-sans-claude
GO_ID=GO-2026-11-03-15 nohup bash lancer-course-scheurer-v2.sh lancer \
  GO-2026-11-03-15 configuration-course-scheurer-v1-sans-claude.json "$RUN" FICHE_SCELLEE RAPPORT_SCELLE > "$RUN.demarrage.log" 2>&1 &
echo "PID du lanceur : $!"
```

Clés exigées : `OPENAI_API_KEY`, `KIMI_API_KEY`, `GEMINI_API_KEY_2` (lues par leur nom). `PY_RELAIS_CLAUDE` n'est pas exigé pour cette
variante. Journal : `$RUN/journal-lancement-course-scheurer-v1.log` (nom hérité). **Arrêt (R10)** : `kill <PID du lanceur>` (code 130).

## Essais (zéro dépense)

```
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 PYTHONDONTWRITEBYTECODE=1 HOME=/tmp PY_AVEC_ANTHROPIC -B -m pytest -q -p no:cacheprovider test_course_scheurer_v2.py
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 PYTHONDONTWRITEBYTECODE=1 PY_AVEC_ANTHROPIC -I -B mutations_scheurer_v2.py
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 /usr/bin/python3 -I -B course_a_blanc_scheurer_v2.py --dossier /tmp/blanc-scheurer-NOUVEAU --rapport /tmp/blanc-scheurer-NOUVEAU.txt
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 PY_RELAIS_CLAUDE=PY_AVEC_ANTHROPIC bash repetition/repetition_complete_scheurer_v2.sh /tmp/repetition-scheurer-NOUVEAU
```

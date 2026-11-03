# LISEZMOI — course Jang-Feng, kit v3 : variante sans Claude (second repli)

> **R12 au premier plan** : aucun fichier de ce kit ne se modifie. Toute correction prend un **nom neuf** (`…-v4`), de nouvelles
> empreintes, une nouvelle table des pièces gelées, une nouvelle répétition. Les cinq configurations v1 et v2 ne sont jamais réécrites.

Rédigé le 3 novembre 2026, 15:00 UTC (`date -u`), par un sous-agent de session-depot. **Rien n'a été lancé de payant.** v3 = kit v2
(`LISEZMOI-course-jangfeng-v2.md`, gardé) plus la variante `sans-claude` (proposeurs Argon, Kimi, Astra ; aiguilleur Astra ; juges
Astra et Argon ; lecteurs Astra et Argon ; metteur Astra ; aucun modèle Claude ; relais 8806 non démarré). Fiche :
`docs/notes/ideation-organisme-v1/course-jang-feng-v1/fiche-lancement-course-jang-feng-v3-brouillon1.md`.

Règle de lancement : premier run `cinq-especes` (Argon libre) ou `avec-kimi` ; si Opus refuse : `sans-opus-argon` (GO-13) ou
`sans-opus` (GO-12), dossier neuf ; **si Fable refuse aussi : `sans-claude` (GO-12), troisième dossier neuf** ; ou `sans-claude` en
premier run si Lazar le décide. Ligne de GO : `GO-2026-11-03-12` (198 USD, S17 technique). Relais Argon 20,7 USD (au-dessus de la
règle « ≤ 10 », déclaré ; dépense lue au registre à la fin).

## Commande exacte (en arrière-plan ; dossier du run NEUF, hors du clone)

```
cd /home/user/controle-ia-travail/donnees/course-jang-feng-v1/orchestrateur/jangfeng
mkdir -p /home/user/runs-course-jang-feng-v1
RUN=/home/user/runs-course-jang-feng-v1/run-$(date -u +%Y%m%d-%H%M)-sans-claude
GO_ID=GO-2026-11-03-12 nohup bash lancer-course-jangfeng-v3.sh lancer \
  GO-2026-11-03-12 configuration-course-jang-feng-v1-sans-claude.json "$RUN" FICHE_SCELLEE RAPPORT_SCELLE > "$RUN.demarrage.log" 2>&1 &
echo "PID du lanceur : $!"
```

Clés exigées : `OPENAI_API_KEY`, `KIMI_API_KEY`, `GEMINI_API_KEY_2` (lues par leur nom) ; `PY_RELAIS_CLAUDE` non exigé. Les autres
variantes se lancent comme au LISEZMOI v2 (lanceur v2, ou v3 : même comportement). **Arrêt (R10)** : `kill <PID du lanceur>`.

## Essais (zéro dépense)

```
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 PYTHONDONTWRITEBYTECODE=1 HOME=/tmp PY_AVEC_ANTHROPIC -B -m pytest -q -p no:cacheprovider test_course_jangfeng_v3.py
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 PYTHONDONTWRITEBYTECODE=1 PY_AVEC_ANTHROPIC -I -B mutations_jangfeng_v3.py
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 /usr/bin/python3 -I -B course_a_blanc_jangfeng_v3.py --dossier /tmp/blanc-jangfeng-NOUVEAU --rapport /tmp/blanc-jangfeng-NOUVEAU.txt
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 PY_RELAIS_CLAUDE=PY_AVEC_ANTHROPIC bash repetition/repetition_complete_jangfeng_v3.sh /tmp/repetition-jangfeng-NOUVEAU
```

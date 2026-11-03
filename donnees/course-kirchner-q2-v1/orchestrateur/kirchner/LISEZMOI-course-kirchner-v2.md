# LISEZMOI — course d'idéation Kirchner Q2, complément v2 (après la contre-lecture de la fiche brouillon 1)

Rédigé le 3 novembre 2026, 10:35 UTC (`date -u`), par un sous-agent de session-depot. **Remplace, pour le lancement,
`LISEZMOI-course-kirchner-v1.md` (gardé, R12)** ; tout le reste de la v1 vaut. Rien n'a été lancé de payant.

| Point | v1 | v2 |
|---|---|---|
| Configurations | `configuration-course-kirchner-q2-v1-*.json` | **`configuration-course-kirchner-q2-v2-{cinq-especes,avec-kimi,sans-kimi}.json`** (aiguilleur v2, source Gu-Krenn v2) |
| Lanceur shell | `lancer-course-kirchner-v1.sh` | **`lancer-course-kirchner-v2.sh`** (configurations v2 seulement ; lanceur Python inchangé) |
| Fiche | brouillon 1 | **brouillon 2** (`docs/notes/ideation-organisme-v1/course-kirchner-q2-v1/fiche-lancement-course-kirchner-q2-v1-brouillon2.md`) |
| Table | `table_pieces_gelees_kirchner_v1.py` | **`table_pieces_gelees_kirchner_v2.py --verifier FICHE_SCELLEE`** |
| GO | numéro à venir | **GO-2026-11-03-05** (au registre, 245 USD) |

## Vérification sans appel

```
cd /home/user/controle-ia-travail/donnees/course-kirchner-q2-v1/orchestrateur/kirchner
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 HOME=/tmp GO_ID=GO-2026-11-03-05 /usr/bin/python3 -I -B lancer_course_kirchner_v1.py verifier \
  --configuration configuration-course-kirchner-q2-v2-cinq-especes.json --registre-go /home/user/controle-ia-travail/registres/go.md \
  --go-attendu GO-2026-11-03-05 --preenregistrement FICHE_SCELLEE --contre-lecture RAPPORT_SCELLE
```

## Commande exacte de lancement (en arrière-plan ; dossier du run NEUF, hors du clone)

```
cd /home/user/controle-ia-travail/donnees/course-kirchner-q2-v1/orchestrateur/kirchner
mkdir -p /home/user/runs-course-kirchner-q2-v1
RUN=/home/user/runs-course-kirchner-q2-v1/run-$(date -u +%Y%m%d-%H%M)
GO_ID=GO-2026-11-03-05 PY_RELAIS_CLAUDE=/home/user/venv-relais-claude/bin/python nohup bash lancer-course-kirchner-v2.sh lancer \
  GO-2026-11-03-05 configuration-course-kirchner-q2-v2-cinq-especes.json "$RUN" FICHE_SCELLEE RAPPORT_SCELLE > "$RUN.demarrage.log" 2>&1 &
echo "PID du lanceur : $!"
```

Replis : `…-v2-avec-kimi.json` (Argon pris : tour v9 ou seconde course d'A1-v3), puis `…-v2-sans-kimi.json` (contrôle de Kimi en
échec ; seule variante sans le risque d'arrêt par débordement de Kimi). Arrêt (R10) : `kill <PID du lanceur>`.

## Essais, course à blanc, répétition v2 (zéro dépense)

```
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 PYTHONDONTWRITEBYTECODE=1 HOME=/tmp PY_AVEC_ANTHROPIC -B -m pytest -q -p no:cacheprovider test_course_kirchner_v2.py
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 /usr/bin/python3 -I -B course_a_blanc_kirchner_v2.py --dossier /tmp/blanc-kirchner-v2-NOUVEAU --rapport /tmp/blanc-NOUVEAU.txt
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 PY_RELAIS_CLAUDE=PY_AVEC_ANTHROPIC bash repetition/repetition_complete_kirchner_v2.sh /tmp/repetition-kirchner-v2-NOUVEAU
```

Résultats du 3 novembre 2026 : 34 essais passés ; course à blanc v2 identique au plan (317, 260, 203 appels) ; répétition v2 :
cinq essais conformes (`repetition/resultat-repetition-kirchner-v2.txt`). Mutations : celles du kit v1 (neuf, toutes détectées) ;
la v2 ne change que deux pièces et les noms acceptés par le lanceur.

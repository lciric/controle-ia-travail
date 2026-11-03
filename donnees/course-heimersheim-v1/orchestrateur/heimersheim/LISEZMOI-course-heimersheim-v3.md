# LISEZMOI — course d'idéation Heimersheim, complément v3 (après la contre-lecture de la fiche brouillon 2)

Rédigé le 3 novembre 2026, 08:23 UTC (`date -u`), par un sous-agent de session-depot. **Remplace, pour le lancement,
`LISEZMOI-course-heimersheim-v2.md` (gardé, R12)** ; tout le reste de la v1 et de la v2 vaut. Rien n'a été lancé de payant.

| Point | v2 | v3 |
|---|---|---|
| Configurations | `configuration-course-heimersheim-v1-*.json` | **`configuration-course-heimersheim-v2-{cinq-especes,avec-kimi,sans-kimi}.json`** (aiguilleur v2, lecteur v2, source Gu-Krenn v2, garde lexicale v2 ; budget et relais inchangés) |
| Lanceur Python | `lancer_course_heimersheim_v1.py` | **`lancer_course_heimersheim_v2.py`** (au-dessus de `course_heimersheim_v2.py`) |
| Lanceur shell | `lancer-course-heimersheim-v2.sh` | **`lancer-course-heimersheim-v3.sh`** (délai 12 h, configurations v2 seulement) |
| Fiche | brouillon 2 | **brouillon 3** (`docs/notes/ideation-organisme-v1/course-heimersheim-v1/fiche-lancement-course-heimersheim-v1-brouillon3.md`) |
| Table | `table_pieces_gelees_heimersheim_v2.py` | **`table_pieces_gelees_heimersheim_v3.py --verifier FICHE_SCELLEE`** |

## Vérification sans appel

```
cd /home/user/controle-ia-travail/donnees/course-heimersheim-v1/orchestrateur/heimersheim
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 HOME=/tmp GO_ID=GO-2026-11-03-NN /usr/bin/python3 -I -B lancer_course_heimersheim_v2.py verifier \
  --configuration configuration-course-heimersheim-v2-cinq-especes.json --registre-go /home/user/controle-ia-travail/registres/go.md \
  --go-attendu GO-2026-11-03-NN --preenregistrement FICHE_SCELLEE --contre-lecture RAPPORT_SCELLE
```

## Commande exacte de lancement (en arrière-plan ; dossier du run NEUF, hors du clone)

```
cd /home/user/controle-ia-travail/donnees/course-heimersheim-v1/orchestrateur/heimersheim
mkdir -p /home/user/runs-course-heimersheim-v1
RUN=/home/user/runs-course-heimersheim-v1/run-$(date -u +%Y%m%d-%H%M)
GO_ID=GO-2026-11-03-NN PY_RELAIS_CLAUDE=/home/user/venv-anthropic-heimersheim/bin/python nohup bash lancer-course-heimersheim-v3.sh lancer \
  GO-2026-11-03-NN configuration-course-heimersheim-v2-cinq-especes.json "$RUN" FICHE_SCELLEE RAPPORT_SCELLE > "$RUN.demarrage.log" 2>&1 &
echo "PID du lanceur : $!"
```

Repli : `configuration-course-heimersheim-v2-avec-kimi.json`, puis `…-v2-sans-kimi.json`. Arrêt (R10) : `kill <PID du lanceur>`.

## Essais, course à blanc, répétition (zéro dépense)

```
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 PYTHONDONTWRITEBYTECODE=1 HOME=/tmp PY_AVEC_ANTHROPIC -B -m pytest -q -p no:cacheprovider test_course_heimersheim_v3.py
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 /usr/bin/python3 -I -B course_a_blanc_heimersheim_v2.py --dossier /tmp/blanc-heimersheim-NOUVEAU --rapport /tmp/blanc-NOUVEAU.txt
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 PY_RELAIS_CLAUDE=PY_AVEC_ANTHROPIC bash repetition/repetition_complete_heimersheim_v3.sh /tmp/repetition-heimersheim-v3-NOUVEAU
```

Résultats du 3 novembre 2026 : 34 essais passés ; course à blanc v2 identique au plan (317, 260, 203 appels) ; répétition v3 : cinq
essais conformes (`repetition/resultat-repetition-heimersheim-v3.txt`).

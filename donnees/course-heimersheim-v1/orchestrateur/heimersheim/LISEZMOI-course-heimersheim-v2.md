# LISEZMOI — course d'idéation Heimersheim (kit v1), complément v2

Rédigé le 3 novembre 2026, 07:57 UTC (`date -u`), par un sous-agent de session-depot. **Remplace, pour le lancement,
`LISEZMOI-course-heimersheim-v1.md` (gardé, R12) sur trois points seulement** ; tout le reste de la v1 vaut (pièces, avant le
lancement, suivi, arrêt par PID, codes, après, ce qui reste non éprouvé). Rien n'a été lancé de payant.

| Point | v1 | v2 |
|---|---|---|
| Lanceur shell | `lancer-course-heimersheim-v1.sh` (délai de la course 21 600 s) | **`lancer-course-heimersheim-v2.sh`** (délai 43 200 s, 12 h) : durée attendue ≈ 5 h (SUPPOSÉ : 322 appels un à la fois ; durées du second tour réel, médiane 58 s par appel de Kimi), et un arrêt par délai ne rend aucune fiche (`fiches.json` n'est écrit qu'en fin de génération) |
| Fiche de lancement | brouillon 1 | **brouillon 2** (`docs/notes/ideation-organisme-v1/course-heimersheim-v1/fiche-lancement-course-heimersheim-v1-brouillon2.md`) : table des pièces gelées v2 (gèle le lanceur v2 et sa répétition) |
| Contrôle de la table | `table_pieces_gelees_heimersheim_v1.py` | **`table_pieces_gelees_heimersheim_v2.py --verifier FICHE_SCELLEE`** |

## Commande exacte de lancement (en arrière-plan ; dossier du run NEUF, hors du clone)

```
cd /home/user/controle-ia-travail/donnees/course-heimersheim-v1/orchestrateur/heimersheim
mkdir -p /home/user/runs-course-heimersheim-v1
RUN=/home/user/runs-course-heimersheim-v1/run-$(date -u +%Y%m%d-%H%M)
GO_ID=GO-2026-11-03-NN PY_RELAIS_CLAUDE=/home/user/venv-anthropic-heimersheim/bin/python nohup bash lancer-course-heimersheim-v2.sh lancer \
  GO-2026-11-03-NN configuration-course-heimersheim-v1-cinq-especes.json "$RUN" FICHE_SCELLEE RAPPORT_SCELLE > "$RUN.demarrage.log" 2>&1 &
echo "PID du lanceur : $!"
```

Repli : `configuration-course-heimersheim-v1-avec-kimi.json` (Argon pas libre), puis `…-sans-kimi.json` (contrôle de Kimi en
échec). Arrêt (R10) : `kill <PID du lanceur>` ; code 124 = délai de 12 h atteint.

## Essais et répétition de la v2 (zéro dépense)

```
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 PYTHONDONTWRITEBYTECODE=1 HOME=/tmp PY_AVEC_ANTHROPIC -B -m pytest -q -p no:cacheprovider \
  test_course_heimersheim_v1.py test_course_heimersheim_v2.py
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 PY_RELAIS_CLAUDE=PY_AVEC_ANTHROPIC bash repetition/repetition_complete_heimersheim_v2.sh /tmp/repetition-heimersheim-v2-NOUVEAU
```

Résultats du 3 novembre 2026 : 32 essais passés (30 de la v1, 2 de la v2 : seules les lignes déclarées diffèrent entre v1 et
v2 ; mêmes refus d'avant tout relais) ; répétition v2 par le vrai lanceur v2 : cinq essais conformes
(`repetition/resultat-repetition-heimersheim-v2.txt`). La contre-épreuve par mutations porte sur la v1 (neuf mutations,
toutes détectées) ; la v2 n'en diffère que du délai.

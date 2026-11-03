# LISEZMOI — course d'idéation sur la question 1 de la mentore Ibrahim (kit v1)

Rédigé le 3 novembre 2026, 11:48 UTC (`date -u`), par un sous-agent de session-depot. **Rien n'a été lancé de payant.** Kit dérivé du
kit Kirchner Q2 v2 (`outils/course-kirchner-q2-v1`, `53e1f738`). Fiche de lancement (brouillon 1, à contre-lire puis sceller) :
`docs/notes/ideation-organisme-v1/course-ibrahim-q1-v1/fiche-lancement-course-ibrahim-q1-v1-brouillon1.md`.

> **R12 au premier plan** : aucun fichier de ce kit ne se modifie. Toute correction (contre-lecture, pièce, configuration) prend un
> **nom neuf** (`…-v2`), de nouvelles empreintes dans les configurations, une nouvelle table des pièces gelées, une nouvelle
> répétition ; le lanceur refuse toute pièce gelée dont l'empreinte a changé, et tout dossier de run qui existe déjà.

## Pièces (dans `donnees/course-ibrahim-q1-v1/orchestrateur/ibrahim/`)

| Pièce | Rôle |
|---|---|
| `../` (pole/, nuit/, essais/…) | orchestrateur v56, copie à l'octet (`VERIFICATION-COPIE-orchestrateur-v56-v1.txt`, `EMPREINTES-orchestrateur-course-ibrahim-q1-v1.txt`) |
| `course_ibrahim_v1.py`, `lancer_course_ibrahim_v1.py`, `lancer-course-ibrahim-v1.sh`, `commande_claude_ibrahim_v1.py` | contrôles (6 fiches par proposeur), lanceurs, commande Claude à deux modèles |
| `configuration-course-ibrahim-q1-v1-{cinq-especes,avec-kimi,sans-kimi}.json` | trois variantes ; `avec-kimi` = **quatre espèces sans Argon** ; S17 technique 198 USD |
| `pieces/` | consignes (proposeur, juge, aiguilleur, lecteur, metteur), 48 concepts, source Gu-Krenn ; `conv-audit/` : question, pièces Ibrahim, sycophancie publique, nos résultats, spécifications Ibrahim et Kirchner, protocole, n° 417 |
| `construire_consigne_proposeur_ibrahim_v1.py` | enchâsse à l'octet deux sections de la question puis les trois pièces |
| `calcul_devis_course_ibrahim_v1.py`, `devis-course-ibrahim-v1.{txt,json}` | devis et construction des configurations |
| `course_a_blanc_ibrahim_v1.py`, `course-a-blanc-ibrahim-v1.txt`, `trace_agregee_course_ibrahim_v1.py`, `table_pieces_gelees_ibrahim_v1.py` | course à blanc, trace, table |
| `test_course_ibrahim_v1.py`, `mutations_ibrahim_v1.py`, `resultat-mutations-ibrahim-v1.txt`, `repetition/` | 36 essais, neuf mutations, répétition (cinq essais) |

## Avant le lancement (aucun appel payant)

1. Contre-lecture de la fiche (R2), version scellée sous un nom neuf citant l'empreinte du rapport ; contrôle :
   `env -i PATH=/usr/bin:/bin LANG=C.UTF-8 /usr/bin/python3 -I -B table_pieces_gelees_ibrahim_v1.py --verifier FICHE_SCELLEE`.
2. Ligne de GO `GO-2026-11-03-NN` (type `calcul`, accordé par Lazar sur son mot direct « go trois tours et course Ibrahim ; pas de
   plafond », **un seul montant : `198 USD`**, sans extension).
3. Variante : `cinq-especes` si Argon est libre ; sinon `avec-kimi` (quatre espèces sans Argon) ; `sans-kimi` en repli.
4. Vérification sans appel :
   ```
   cd /home/user/controle-ia-travail/donnees/course-ibrahim-q1-v1/orchestrateur/ibrahim
   env -i PATH=/usr/bin:/bin LANG=C.UTF-8 HOME=/tmp GO_ID=GO-2026-11-03-NN /usr/bin/python3 -I -B lancer_course_ibrahim_v1.py verifier \
     --configuration configuration-course-ibrahim-q1-v1-avec-kimi.json --registre-go /home/user/controle-ia-travail/registres/go.md \
     --go-attendu GO-2026-11-03-NN --preenregistrement FICHE_SCELLEE --contre-lecture RAPPORT_SCELLE
   ```

## Commande exacte de lancement (en arrière-plan ; dossier du run NEUF, hors du clone)

```
cd /home/user/controle-ia-travail/donnees/course-ibrahim-q1-v1/orchestrateur/ibrahim
mkdir -p /home/user/runs-course-ibrahim-q1-v1
RUN=/home/user/runs-course-ibrahim-q1-v1/run-$(date -u +%Y%m%d-%H%M)
GO_ID=GO-2026-11-03-NN PY_RELAIS_CLAUDE=/home/user/venv-relais-claude/bin/python nohup bash lancer-course-ibrahim-v1.sh lancer \
  GO-2026-11-03-NN configuration-course-ibrahim-q1-v1-avec-kimi.json "$RUN" FICHE_SCELLEE RAPPORT_SCELLE > "$RUN.demarrage.log" 2>&1 &
echo "PID du lanceur : $!"
```

(`…-cinq-especes.json` si Argon est libre ; `…-sans-kimi.json` si le contrôle de Kimi échoue.) Journal :
`$RUN/journal-lancement-course-ibrahim-v1.log`. **Arrêt (R10)** : `kill <PID du lanceur>` (code 130). Codes : 0 fini ; 2 refus ou
arrêt ; 3 relais ou contrôle en échec ; 6 clé trouvée ; 7 trace refusée ou sceau en échec ; 124 délai (12 h) ; 130 signal.

## Après

Sortie scellée (`$RUN/empreintes-run-ibrahim-v1.txt`) avant toute lecture ; fiches dans `$RUN/course/generation-1/` ; mariages :
`coffre/iq1-cle-bras.json` ; trace : `$RUN/trace-agregee-course-ibrahim-v1.json`. Copie au canal à l'octet si « aucune clé trouvée ».

## Essais, contre-épreuve, course à blanc, répétition (zéro dépense)

```
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 PYTHONDONTWRITEBYTECODE=1 HOME=/tmp PY_AVEC_ANTHROPIC -B -m pytest -q -p no:cacheprovider test_course_ibrahim_v1.py
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 PYTHONDONTWRITEBYTECODE=1 PY_AVEC_ANTHROPIC -I -B mutations_ibrahim_v1.py
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 /usr/bin/python3 -I -B course_a_blanc_ibrahim_v1.py --dossier /tmp/blanc-ibrahim-NOUVEAU --rapport /tmp/blanc-ibrahim-NOUVEAU.txt
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 PY_RELAIS_CLAUDE=PY_AVEC_ANTHROPIC bash repetition/repetition_complete_ibrahim_v1.sh /tmp/repetition-ibrahim-NOUVEAU
```

Résultats du 3 novembre 2026 : 36 essais passés ; neuf mutations, toutes détectées ; course à blanc identique au plan (247, 204, 161
appels) ; répétition : cinq essais conformes (course complète cinq espèces, 252 appels contrôles compris).

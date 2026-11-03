# LISEZMOI — course d'idéation sur la question 2 du mentor Kirchner (kit v1)

Rédigé le 3 novembre 2026, 10:18 UTC (`date -u`), par un sous-agent de session-depot. **Rien n'a été lancé de payant.** Kit
dérivé du kit Heimersheim après contre-lecture (`outils/course-heimersheim-v1` : pièces v2, garde lexicale v2, lanceur Python v2,
lanceur shell v3), même discipline. Fiche de lancement (brouillon 1, à contre-lire puis sceller sous un nom neuf) :
`docs/notes/ideation-organisme-v1/course-kirchner-q2-v1/fiche-lancement-course-kirchner-q2-v1-brouillon1.md`.

## Pièces (dans `donnees/course-kirchner-q2-v1/orchestrateur/kirchner/`)

| Pièce | Rôle |
|---|---|
| `../` (pole/, nuit/, essais/…) | orchestrateur v56, copie à l'octet (`VERIFICATION-COPIE-orchestrateur-v56-v1.txt`, `EMPREINTES-orchestrateur-course-kirchner-q2-v1.txt`) |
| `course_kirchner_v1.py`, `lancer_course_kirchner_v1.py`, `lancer-course-kirchner-v1.sh`, `commande_claude_kirchner_v1.py` | contrôles, lanceurs, commande Claude à deux modèles |
| `configuration-course-kirchner-q2-v1-{cinq-especes,avec-kimi,sans-kimi}.json` | trois variantes, S17 technique 245 USD |
| `pieces/` | consignes (proposeur, juge, aiguilleur, lecteur, metteur), 46 concepts, source Gu-Krenn ; `conv-audit/` : question, pièce « Kirchner » v2, « nos résultats », spécification, protocole du rapport |
| `construire_consigne_proposeur_kirchner_v1.py` | enchâsse à l'octet la question (quatre sections) puis les deux pièces |
| `calcul_devis_course_kirchner_v1.py`, `devis-course-kirchner-v1.{txt,json}` | devis et construction des configurations |
| `course_a_blanc_kirchner_v1.py`, `course-a-blanc-kirchner-v1.txt` | course à blanc |
| `trace_agregee_course_kirchner_v1.py`, `table_pieces_gelees_kirchner_v1.py` | trace agrégée ; table des pièces gelées |
| `test_course_kirchner_v1.py`, `mutations_kirchner_v1.py`, `resultat-mutations-kirchner-v1.txt` | 34 essais ; neuf mutations |
| `repetition/` | faux mandataire TLS, autorité factice, répétition (cinq essais), résultat |
| `docs/notes/ideation-organisme-v1/commandes-a1-bis-v1/` | commandes A1-bis (copies à l'octet, `a1fc7bca`) |

## Avant le lancement (aucun appel payant)

1. Contre-lecture de la fiche brouillon 1 (R2), version scellée sous un nom neuf citant l'empreinte du rapport ; contrôle :
   `env -i PATH=/usr/bin:/bin LANG=C.UTF-8 /usr/bin/python3 -I -B table_pieces_gelees_kirchner_v1.py --verifier FICHE_SCELLEE`.
2. Ligne de GO `GO-2026-11-03-NN` (type `calcul`, accordé par Lazar, **un seul montant : `245 USD`**, sans extension).
3. Python du relais Claude portant `anthropic` (2.4.0 éprouvé), par exemple `/home/user/venv-anthropic-heimersheim/bin/python`.
4. Noms des clés présents (jamais la valeur) : `RR_ANTHROPIC_API_KEY_LUC`, `OPENAI_API_KEY`, `KIMI_API_KEY`, `GEMINI_API_KEY_2`.
5. Vérification sans appel :
   ```
   cd /home/user/controle-ia-travail/donnees/course-kirchner-q2-v1/orchestrateur/kirchner
   env -i PATH=/usr/bin:/bin LANG=C.UTF-8 HOME=/tmp GO_ID=GO-2026-11-03-NN /usr/bin/python3 -I -B lancer_course_kirchner_v1.py verifier \
     --configuration configuration-course-kirchner-q2-v1-cinq-especes.json --registre-go /home/user/controle-ia-travail/registres/go.md \
     --go-attendu GO-2026-11-03-NN --preenregistrement FICHE_SCELLEE --contre-lecture RAPPORT_SCELLE
   ```
6. Ports 8804 à 8807 libres ; Argon utilisé par rien d'autre (sinon variante `avec-kimi`).

## Commande exacte de lancement (en arrière-plan ; dossier du run NEUF, hors du clone)

```
cd /home/user/controle-ia-travail/donnees/course-kirchner-q2-v1/orchestrateur/kirchner
mkdir -p /home/user/runs-course-kirchner-q2-v1
RUN=/home/user/runs-course-kirchner-q2-v1/run-$(date -u +%Y%m%d-%H%M)
GO_ID=GO-2026-11-03-NN PY_RELAIS_CLAUDE=/home/user/venv-anthropic-heimersheim/bin/python nohup bash lancer-course-kirchner-v1.sh lancer \
  GO-2026-11-03-NN configuration-course-kirchner-q2-v1-cinq-especes.json "$RUN" FICHE_SCELLEE RAPPORT_SCELLE > "$RUN.demarrage.log" 2>&1 &
echo "PID du lanceur : $!"
```

Replis : `…-avec-kimi.json`, puis `…-sans-kimi.json`. Journal : `$RUN/journal-lancement-course-kirchner-v1.log`. **Arrêt (R10)** :
`kill <PID du lanceur>` (course arrêtée proprement, relais par PID, sortie scellée, code 130). Codes : 0 fini ; 2 refus ou arrêt ;
3 relais ou contrôle en échec ; 6 clé trouvée ; 7 trace refusée ou sceau en échec ; 124 délai (12 h) ; 130 signal.

## Après

Sortie scellée (`$RUN/empreintes-run-kirchner-v1.txt`) avant toute lecture ; fiches et classement dans
`$RUN/course/generation-1/` ; mariages : `coffre/kq2-cle-bras.json`, `coffre/kq2-paires-par-bras.json` ; trace :
`$RUN/trace-agregee-course-kirchner-v1.json`. Copie au canal seulement si « aucune clé trouvée ». Dépense au registre, tableaux
de bord relus. Rapport au protocole Kirchner v1 (le coffre et les juges de la course n'y servent qu'à part).

## Essais, contre-épreuve, course à blanc, répétition (zéro dépense)

```
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 PYTHONDONTWRITEBYTECODE=1 HOME=/tmp PY_AVEC_ANTHROPIC -B -m pytest -q -p no:cacheprovider test_course_kirchner_v1.py
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 PYTHONDONTWRITEBYTECODE=1 PY_AVEC_ANTHROPIC -I -B mutations_kirchner_v1.py
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 /usr/bin/python3 -I -B course_a_blanc_kirchner_v1.py --dossier /tmp/blanc-kirchner-NOUVEAU --rapport /tmp/blanc-kirchner-NOUVEAU.txt
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 PY_RELAIS_CLAUDE=PY_AVEC_ANTHROPIC bash repetition/repetition_complete_kirchner_v1.sh /tmp/repetition-kirchner-NOUVEAU
```

Résultats du 3 novembre 2026 : 34 essais passés ; neuf mutations, toutes détectées ; course à blanc identique au plan (317, 260,
203 appels) ; répétition : cinq essais conformes (refus sans autorité factice ; course complète cinq espèces, 322 appels ;
`kill -TERM`, code 130 en 2 s ; contrôle d'Opus 5.5 en échec, code 3 ; plafond de session trop bas, code 2, aucun appel).

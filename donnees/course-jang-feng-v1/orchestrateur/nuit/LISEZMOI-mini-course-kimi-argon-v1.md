# LISEZMOI — mini-course d'idéation réelle, Kimi et Argon seuls (GO-2026-11-01-12, scénario B), v1

Rédigé le 1er novembre 2026 (sous-agent de session-depot). **Rien n'a été lancé de payant, rien n'est scellé, rien n'est commis.**
Préenregistrement : `docs/notes/mini-course-kimi-argon-v1/preregistrement-mini-course-kimi-argon-v1.md` (brouillon, à faire
contre-lire puis sceller). Devis : `docs/notes/devis-mini-course-kimi-argon-nuit-v1/devis-mini-course-kimi-argon-nuit-v1.md`.

## Où sont les pièces

Dossier de travail (hors git, exclu de la copie publique) : `donnees/mini-course-kimi-argon-v1/orchestrateur/` = copie de
l'orchestrateur v56 (identique à l'archive `29b1b38c…`, liste `nuit/EMPREINTES-orchestrateur-v56-copie-v1.txt`), plus :

| Pièce | Rôle |
|---|---|
| `pole/course2_nuit_v1.py` | génération sans passe « tableau » ; liste d'arrêt (modèle servi, trois échecs, garde Kimi) ; une génération |
| `nuit/lancer_mini_course_v1.py` | lanceur Python : `verifier` (sans écriture ni appel), `simuler`, `lancer` (moteur réel) |
| `nuit/lancer-mini-course-v1.sh` | lanceur shell : vérifications, relais Kimi et Argon sous `env -i`, contrôles, course, trace, recherche des clés |
| `nuit/commande_kimi_v2.py` | commande externe de Kimi (proposeur, juge) par le relais local `relais_kimi_v3.py` |
| `nuit/commande_argon_v56_nuit_v1.py` | `servir` : relais Argon local (clé GEMINI_API_KEY de son seul environnement, `appeler_gemini` sans reprise) ; `appeler` : commande externe |
| `nuit/registre_depense_cumulee_v1.py` | garde cumulée au pire cas avant chaque appel (10 USD), et garde du plafond dur de l'étape |
| `nuit/trace_agregee_mini_course_v1.py` | seule pièce qui écrit la trace publique : liste blanche, anti-fuite, garde testée |
| `nuit/configuration-mini-course-kimi-argon-v1.json` | configuration figée (scénario B) |
| `nuit/pieces/*.md`, `nuit/pieces/concepts-mini-course-v1.json` | cinq consignes figées (un canari chacune) ; liste fermée de 24 concepts |
| `nuit/repetition/` | répétition sans réseau (faux amonts, script complet), essais des gardes, table des pièces gelées |

## Avant le lancement (dans cet ordre ; aucun appel payant)

1. **Contre-lecture (R2)** par un sous-agent neuf, qui n'a écrit ni le préenregistrement ni les pièces ; lui donner : le
   préenregistrement, le devis, `registres/go.md` (ligne GO-2026-11-01-12), ce LISEZMOI, la configuration, les cinq consignes,
   `pole/course2_nuit_v1.py`, les deux lanceurs, les deux commandes, le registre cumulé, l'agrégateur, les essais des gardes.
   Rapport : `docs/notes/mini-course-kimi-argon-v1/contre-lecture-preregistrement-mini-course-kimi-argon-v1.md`.
2. Traiter chaque remarque dans la section « Contre-lecture » du préenregistrement. Toute pièce modifiée prend un **nom neuf**
   (R12) et sa ligne de la table « Pièces gelées » est refaite :
   `python3 -I -B nuit/repetition/table_pieces_gelees_v1.py` (impression), `--verifier PREREG` (contrôle).
3. Sceller le rapport : `cd /home/user/controle-ia-travail && PYTHONPATH=src python -m controle_ia.scellement sceller docs/notes/mini-course-kimi-argon-v1/contre-lecture-preregistrement-mini-course-kimi-argon-v1.md`.
4. Remplacer, dans le préenregistrement, « À FOURNIR AU SCELLEMENT » par l'empreinte du rapport ; vérifier la table
   (`table_pieces_gelees_v1.py --verifier …`, « conforme ») ; sceller le préenregistrement de la même façon.
5. Vérification complète, sans écriture ni appel (configuration, gardes R5 à É0, ligne de GO à exactement 10 USD) :

   ```
   cd /home/user/controle-ia-travail/donnees/mini-course-kimi-argon-v1/orchestrateur/nuit
   env -i PATH=/usr/bin:/bin LANG=C.UTF-8 HOME=/tmp GO_ID=GO-2026-11-01-12 /usr/bin/python3 -I -B lancer_mini_course_v1.py verifier \
     --configuration configuration-mini-course-kimi-argon-v1.json --registre-go /home/user/controle-ia-travail/registres/go.md
   ```
6. Inventorier les instances et les processus : aucun port 8804 ni 8805 pris.

## Commande exacte de lancement (en arrière-plan ; journal dans le dossier du run)

Depuis la session qui porte `GEMINI_API_KEY_2` et `KIMI_API_KEY` dans son environnement (jamais en argument) :

```
cd /home/user/controle-ia-travail/donnees/mini-course-kimi-argon-v1/orchestrateur/nuit
RUN=/home/user/controle-ia-travail/donnees/mini-course-kimi-argon-v1/run-$(date -u +%Y%m%d-%H%M)
GO_ID=GO-2026-11-01-12 nohup bash lancer-mini-course-v1.sh lancer "$RUN" > "$RUN.demarrage.log" 2>&1 &
echo "PID du lanceur : $!"
```

- Journal : `$RUN/journal-lancement-mini-course-v1.log` (PID des deux relais, contrôles, reste du registre, code de fin) ;
  `$RUN.demarrage.log` ne reçoit que les refus d'avant la création du dossier (GO, dossier déjà présent).
- Suivi : `tail -f "$RUN/journal-lancement-mini-course-v1.log"` ; dépense : `/usr/bin/python3 -I -B registre_depense_cumulee_v1.py etat "$RUN/registre-depense-cumulee-v1.jsonl"`.
- Durée attendue ≈ 2 h 30 (devis) ; borne : `timeout 12600` sur la course.
- Arrêt (R10) : `kill <PID du lanceur>` (le piège arrête les relais par leur PID, écrit leur état final) ; en dernier recours,
  les PID des relais sont au journal (`kill <PID>`), consigner dans `registres/arrets.md`.
- Codes : 0 fini ; 2 refus ou arrêt de la course (motif au journal et au manifeste de fin) ; 3 relais ou contrôle en échec ;
  6 clé trouvée dans une sortie ; 7 trace refusée ; 124 délai.

## Après

- Trace : `$RUN/trace-agregee-mini-course-v1.json` (+ `.sha256`). La copier vers `docs/notes/mini-course-kimi-argon-v1/` sous un
  nom neuf seulement si `controle_anti_fuite.resultat` vaut « conforme » ; rapporter L1 à L4 selon le préenregistrement.
- Dépense : registre cumulé (contrôles compris) et journaux des relais → `registres/depenses.md` (session-depot).
- Ne citer aucune fiche, aucun titre, aucun extrait hors du dossier du run.

## Répétition (faite le 1er novembre 2026, zéro réseau, zéro dépense)

```
cd /home/user/controle-ia-travail/donnees/mini-course-kimi-argon-v1/orchestrateur
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 HOME=/tmp /home/user/controle-ia-travail/.venv/bin/python -B -m pytest -q -p no:cacheprovider nuit/repetition/test_gardes_mini_course_v1.py
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 HOME=/tmp /usr/bin/python3 -I -B nuit/lancer_mini_course_v1.py simuler \
  --configuration nuit/configuration-mini-course-kimi-argon-v1.json --sortie BLOC-NOTES/sim/course --fiche-factice MC1-FICHE-FACTICE-67b8c480
bash nuit/repetition/repetition_complete_v1.sh BLOC-NOTES/reel        # moteur réel devant des amonts factices
```

Gardes éprouvées sur un cas sain et un artefact (R5) : registre cumulé (plafond cumulé, plafond d'étape, ligne illisible) ;
commande Kimi (refus sans envoi au plafond cumulé, porte incomplète) ; commande et relais Argon (modèle servi différent,
refus du modèle) ; adaptateur de la nuit (modèle servi différent = arrêt) ; trois échecs consécutifs ; débordement de la garde
Kimi ; configuration du scénario B ; ligne de GO (montant, extension, GO autre que GO-2026-11-01-12) ; pièces gelées ;
spécification non scellée (moteur réel refusé, rien d'écrit) ; trace (canari, titre, six mots, liste blanche) ; gardes R5 de la
v56 rejouées à É0 (22 lignes). Non éprouvés hors réseau : le contrôle en échec du lanceur shell et la recherche des clés (code
simple, relu) ; le format réel du flux de Moonshot et de la réponse d'Argon (déjà servis à l'épreuve du pont, mêmes relais et
même `appeler_gemini`).

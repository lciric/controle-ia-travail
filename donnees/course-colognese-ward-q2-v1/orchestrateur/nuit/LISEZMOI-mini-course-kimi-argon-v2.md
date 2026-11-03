# LISEZMOI — mini-course d'idéation réelle, Kimi et Argon seuls (GO-2026-11-01-12, scénario B), v2

Rédigé le 1er novembre 2026 (sous-agent de session-depot) après la contre-lecture
(`docs/notes/mini-course-kimi-argon-v1/contre-lecture-mini-course-kimi-argon-v1.md`, `a35eac70…`, « scellable après
corrections »). Remplace, pour le lancement, `LISEZMOI-mini-course-kimi-argon-v1.md` (gardé, R12). **Rien n'est scellé, rien
n'est commis, rien n'a été lancé de payant.**

Préenregistrement à sceller : `docs/notes/mini-course-kimi-argon-v1/preregistrement-mini-course-kimi-argon-v2.md` (il cite déjà
l'empreinte du rapport de contre-lecture, scellé ; aucun marqueur restant ; table « Pièces gelées » remplie).

## Pièces v2 (noms neufs ; les v1 restent, inchangées)

| Pièce | Ce qui change |
|---|---|
| `nuit/lancer-mini-course-v2.sh` | course en arrière-plan sous `wait` ; signal → SIGTERM à la course, relais arrêtés, trace et recherche des clés quand même, code 130 (CLM-01) ; relais 3 et 7 USD (CLM-05) ; outils sous `env -i`, `chercher_cles_v1.py` (CLM-06) ; épreuve anti-fuite sur le run (CLM-07) ; mandataire vide non transmis ; mode `repeter` derrière une autorité factice |
| `nuit/lancer_mini_course_v2.py` | rapport de contre-lecture au nom réel (CLM-04) ; préenregistrement v2 ; adaptateur v2 ; garde du dépôt exigée dans les pièces gelées (CLM-08) |
| `pole/course2_nuit_v2.py` | dépassement de réserve, garde cumulée, garde d'étape des commandes, plafond d'un relais : arrêt de la course sous un motif distinct (CLM-02, CLM-09) |
| `nuit/commande_argon_v56_nuit_v2.py` | coût d'un échec = pire cas réservé exactement (défaut trouvé par la répétition) |
| `nuit/configuration-mini-course-kimi-argon-v2.json` | la v1, dont seule change la commande d'Argon |
| `nuit/trace_agregee_mini_course_v2.py` | motifs v2 ; L3 et L4 « non calculés (O12) » après un arrêt (CLM-10) ; fusion exclue de L4 (CLM-13) |
| `nuit/chercher_cles_v1.py` | recherche des clés, valeurs lues dans l'environnement, jamais en argument (CLM-06) |
| `nuit/repetition/` | `test_gardes_mini_course_v2.py` (14 essais), `repetition_complete_v2.sh`, `faux_mandataire_tls_v1.py`, `autorite_factice_v1.sh`, `table_pieces_gelees_v2.py` |

## Avant le lancement (aucun appel payant)

1. Relire la section « Contre-lecture » du préenregistrement v2 (traitement de CLM-01 à CLM-13) ; contrôle de la table :
   ```
   /usr/bin/python3 -I -B /home/user/controle-ia-travail/donnees/mini-course-kimi-argon-v1/orchestrateur/nuit/repetition/table_pieces_gelees_v2.py \
     --verifier /home/user/controle-ia-travail/docs/notes/mini-course-kimi-argon-v1/preregistrement-mini-course-kimi-argon-v2.md
   ```
   (doit rendre « conforme » ; toute pièce modifiée prend un nom neuf et la table est refaite).
2. Sceller le préenregistrement v2 :
   `cd /home/user/controle-ia-travail && PYTHONPATH=src python -m controle_ia.scellement sceller docs/notes/mini-course-kimi-argon-v1/preregistrement-mini-course-kimi-argon-v2.md`
3. Vérification sans écriture ni appel (configuration, gardes R5, ligne de GO à exactement 10 USD) :
   ```
   cd /home/user/controle-ia-travail/donnees/mini-course-kimi-argon-v1/orchestrateur/nuit
   env -i PATH=/usr/bin:/bin LANG=C.UTF-8 HOME=/tmp GO_ID=GO-2026-11-01-12 /usr/bin/python3 -I -B lancer_mini_course_v2.py verifier \
     --configuration configuration-mini-course-kimi-argon-v2.json --registre-go /home/user/controle-ia-travail/registres/go.md
   ```
4. Ports 8804 et 8805 libres ; aucune instance de calcul active.

## Commande exacte de lancement (en arrière-plan ; journal dans le dossier du run)

Depuis la session qui porte `GEMINI_API_KEY_2`, `KIMI_API_KEY`, `HTTPS_PROXY` et `SSL_CERT_FILE` (jamais en argument) :

```
cd /home/user/controle-ia-travail/donnees/mini-course-kimi-argon-v1/orchestrateur/nuit
RUN=/home/user/controle-ia-travail/donnees/mini-course-kimi-argon-v1/run-$(date -u +%Y%m%d-%H%M)
GO_ID=GO-2026-11-01-12 nohup bash lancer-mini-course-v2.sh lancer "$RUN" > "$RUN.demarrage.log" 2>&1 &
echo "PID du lanceur : $!"
```

- Journal : `$RUN/journal-lancement-mini-course-v2.log` (PID du lanceur, des relais et de la course ; contrôles ; registre ;
  épreuve anti-fuite ; recherche des clés ; code de fin). `$RUN.demarrage.log` ne reçoit que les refus d'avant la création du
  dossier.
- Suivi : `tail -f "$RUN/journal-lancement-mini-course-v2.log"` ; dépense au barème :
  `env -i PATH=/usr/bin:/bin /usr/bin/python3 -I -B registre_depense_cumulee_v1.py etat "$RUN/registre-depense-cumulee-v1.jsonl"`.
- **Arrêt (R10)** : `kill <PID du lanceur>` (celui que la commande a affiché, ou « PID du lanceur » au journal). Éprouvé : la
  course reçoit SIGTERM et s'arrête proprement (2 s en répétition), les relais sont arrêtés par leur PID, la trace et la
  recherche des clés sont faites, code 130. Ne jamais tuer la course ou les relais par motif de ligne de commande.
- Codes : 0 fini ; 2 refus ou arrêt de la course (motif au journal, au manifeste de fin et dans la trace) ; 3 relais ou
  contrôle en échec ; 6 clé trouvée ; 7 trace refusée ; 124 délai ; 130 signal.
- Borne : 10 USD au plus **au barème supposé d'Argon** (hypothèses au préenregistrement) ; facture réelle à relire au tableau de
  bord de chaque fournisseur.

## Après

- Trace : `$RUN/trace-agregee-mini-course-v2.json` (+ `.sha256`) ; la copier vers `docs/notes/mini-course-kimi-argon-v1/` sous
  un nom neuf seulement si `controle_anti_fuite.resultat` vaut « conforme » ; rapporter L1 à L4 selon le préenregistrement v2.
- Dépense : registre cumulé, journaux et états finaux des relais → `registres/depenses.md` ; relire les tableaux de bord.
- Ne citer aucune fiche, aucun titre, aucun extrait hors du dossier du run.

## Répétition v2 (zéro dépense ; refaire avant le lancement si une pièce change)

```
cd /home/user/controle-ia-travail/donnees/mini-course-kimi-argon-v1/orchestrateur
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 HOME=/tmp /home/user/controle-ia-travail/.venv/bin/python -B -m pytest -q -p no:cacheprovider \
  nuit/repetition/test_gardes_mini_course_v1.py nuit/repetition/test_gardes_mini_course_v2.py
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 HOME=/tmp bash nuit/repetition/repetition_complete_v2.sh BLOC-NOTES/repetition-v2-NOUVEAU
```

Le second script lance le vrai `lancer-mini-course-v2.sh` (mode `repeter`) derrière un faux mandataire TLS et une autorité
factice, avec des clés factices ; ses runs vont sous `donnees/mini-course-kimi-argon-v1/repetitions-v2/`. Résultat du
1er novembre, 21:43 UTC : quatre essais conformes (refus sans autorité factice ; course complète, 68 appels ; `kill -TERM` en
pleine course, code 130 en 2 s ; contrôle d'Argon en échec, aucune course). Ce qui reste non éprouvé est listé au
préenregistrement v2 (« Gardes éprouvées et gardes non éprouvées »).

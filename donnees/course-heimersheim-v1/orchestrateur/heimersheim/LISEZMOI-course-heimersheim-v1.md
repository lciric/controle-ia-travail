# LISEZMOI — course d'idéation sur la question 1 du mentor Heimersheim (kit v1)

Rédigé le 3 novembre 2026 (sous-agent de session-depot), sur le modèle de `nuit/LISEZMOI-mini-course-kimi-argon-v2.md`.
**Rien n'a été lancé de payant** : aucun appel réel à Anthropic, OpenAI, Moonshot ou Google, aucune instance de calcul. Course
**non décisive** (démonstration, matière à réflexion pour Lazar). Spécification : `pieces/conv-audit/specification-course-ideation-heimersheim-v1.md`
(`0e2fd5bc…`, conv-audit). Fiche de lancement (brouillon 1, à contre-lire puis sceller sous un nom neuf) :
`docs/notes/ideation-organisme-v1/course-heimersheim-v1/fiche-lancement-course-heimersheim-v1-brouillon1.md`.

## Pièces (toutes dans `donnees/course-heimersheim-v1/orchestrateur/heimersheim/`, sauf mention)

| Pièce | Rôle |
|---|---|
| `../` (pole/, nuit/, essais/…) | copie à l'octet de l'orchestrateur v56 de la mini-course (`VERIFICATION-COPIE-orchestrateur-v56-v1.txt`, `EMPREINTES-orchestrateur-course-heimersheim-v1.txt`, 218 fichiers) |
| `course_heimersheim_v1.py` | contrôles propres de la course, plan d'appels et pires cas, génération (`course2_nuit_v1`) et adaptateur (`course2_nuit_v2`) |
| `lancer_course_heimersheim_v1.py` | lanceur Python : `verifier`, `simuler`, `lancer` (ordre des gardes de la v56, GO attendu en paramètre) |
| `lancer-course-heimersheim-v1.sh` | lanceur shell : relais, contrôles, course sous `wait`, arrêt par PID, sceau, trace, recherche des clés |
| `commande_claude_heimersheim_v1.py` | aiguille le modèle demandé (Fable 5.1 ou Opus 5.5) vers la commande A1-bis Claude (empreintes vérifiées) |
| `configuration-course-heimersheim-v1-{cinq-especes,avec-kimi,sans-kimi}.json` | les trois variantes (S17 = 244 USD, plafond technique) |
| `pieces/` | consignes du proposeur (enchâsse question et pièce), du juge, de l'aiguilleur, du lecteur, du metteur ; liste fermée de 37 concepts ; source du substitut Gu-Krenn ; `conv-audit/` : question, pièce, spécification (copies à l'octet, compagnons de conv-audit) |
| `argon/collisionneur_v7.py` | copie à l'octet (`c9725f02…`) lue par le relais Argon |
| `calcul_devis_course_heimersheim_v1.py`, `devis-course-heimersheim-v1.{txt,json}` | devis et construction des configurations |
| `course_a_blanc_heimersheim_v1.py`, `course-a-blanc-heimersheim-v1.txt` | course à blanc (moteur simulé) des trois variantes |
| `trace_agregee_course_heimersheim_v1.py` | trace agrégée (comptes, coûts, mariages par bras), garde anti-fuite testée à chaque exécution |
| `table_pieces_gelees_heimersheim_v1.py` | table « Pièces gelées » de la fiche, et sa vérification |
| `test_course_heimersheim_v1.py`, `mutations_heimersheim_v1.py`, `resultat-mutations-heimersheim-v1.txt` | 30 essais hors réseau ; contre-épreuve par neuf mutations |
| `repetition/` | faux mandataire TLS (Anthropic, OpenAI, Moonshot, Google), autorité factice, répétition complète (cinq essais), résultat |
| `docs/notes/ideation-organisme-v1/commandes-a1-bis-v1/` | commandes A1-bis (Claude 8806, Astra 8807), copies à l'octet du commit `a1fc7bca` |

**Champs des fiches** (`titre`, `hypothese`, `axe`, `epreuve`, `controle`, `prediction`, `test_de_mort`, `cout`) : ce que la
question exige de chaque fiche (hypothèse, effet prédit, mesure qui la tue) plus l'épreuve et le contrôle « spécifique contre
générique » qu'elle demande, et le coût « en quelques jours » (`temoin`, nom réservé par le noyau v56, devient `controle`).
**Axes** : les cinq demandes « particulièrement bienvenues » de la question (`raison_echec_absente`, `evaluation_contre_registre`,
`residu_non_verbalise`, `lien_objets_non_relies`, `prediction_chiffree_8b`).
**Bras joués** : `gu_krenn` (substitut, source minimale tirée de la pièce) et `basique` (exposant 8,5, décalage 0,05), 4 paires
par bras ; **bras méta hors course** (annexe propre à la question, contre-lecture et approbation `R-NNN` de Lazar absentes :
fiche § 3.3).

## Avant le lancement (aucun appel payant)

0. Variante : `cinq-especes` si Argon est libre (port 8805 libre, aucune autre course), sinon `avec-kimi` ; `sans-kimi` en repli.
1. Contre-lecture de la fiche brouillon 1 par un lecteur neuf (R2), puis version scellée sous un nom neuf qui cite l'empreinte
   du rapport (`Contre-lecture : <empreinte>`) et garde la table « Pièces gelées » ; contrôle de la table :
   ```
   cd /home/user/controle-ia-travail/donnees/course-heimersheim-v1/orchestrateur/heimersheim
   env -i PATH=/usr/bin:/bin LANG=C.UTF-8 /usr/bin/python3 -I -B table_pieces_gelees_heimersheim_v1.py --verifier FICHE_SCELLEE
   ```
2. Ligne de GO au registre `registres/go.md` (session-depot, sur le mot de Lazar) : type `calcul`, accordé par Lazar, cellule
   plafond portant **un seul montant : `244 USD`**, sans ligne d'extension.
3. Python du relais Claude (le SDK `anthropic` n'est ni dans `/usr/bin/python3` ni dans `.venv`) ; version éprouvée en
   répétition : 2.4.0 :
   ```
   python3 -m venv /home/user/venv-anthropic-heimersheim && /home/user/venv-anthropic-heimersheim/bin/pip install anthropic==2.4.0
   ```
4. Noms des clés présents (jamais la valeur) : `env | grep -o '^RR_ANTHROPIC_API_KEY_LUC='`, `env | grep -o '^OPENAI_API_KEY='`,
   `env | grep -o '^KIMI_API_KEY='`, `env | grep -o '^GEMINI_API_KEY_2='` (selon la variante) ; autre nom de clé Anthropic :
   `CLE_ANTHROPIC_NOM=NOM`.
5. Vérification sans écriture ni appel (configuration, contrôles Heimersheim, bras à É0, table R5, ligne de GO à 244 USD, fiche
   scellée et pièces gelées) :
   ```
   cd /home/user/controle-ia-travail/donnees/course-heimersheim-v1/orchestrateur/heimersheim
   env -i PATH=/usr/bin:/bin LANG=C.UTF-8 HOME=/tmp GO_ID=GO-2026-11-03-NN /usr/bin/python3 -I -B lancer_course_heimersheim_v1.py verifier \
     --configuration configuration-course-heimersheim-v1-cinq-especes.json --registre-go /home/user/controle-ia-travail/registres/go.md \
     --go-attendu GO-2026-11-03-NN --preenregistrement FICHE_SCELLEE --contre-lecture RAPPORT_SCELLE
   ```
6. Ports 8804 à 8807 libres ; aucune instance de calcul active.

## Commande exacte de lancement (en arrière-plan ; dossier du run NEUF, hors du clone)

```
cd /home/user/controle-ia-travail/donnees/course-heimersheim-v1/orchestrateur/heimersheim
mkdir -p /home/user/runs-course-heimersheim-v1
RUN=/home/user/runs-course-heimersheim-v1/run-$(date -u +%Y%m%d-%H%M)
GO_ID=GO-2026-11-03-NN PY_RELAIS_CLAUDE=/home/user/venv-anthropic-heimersheim/bin/python nohup bash lancer-course-heimersheim-v1.sh lancer \
  GO-2026-11-03-NN configuration-course-heimersheim-v1-cinq-especes.json "$RUN" FICHE_SCELLEE RAPPORT_SCELLE > "$RUN.demarrage.log" 2>&1 &
echo "PID du lanceur : $!"
```

(Remplacer `GO-2026-11-03-NN` deux fois par l'identifiant inscrit, `FICHE_SCELLEE` et `RAPPORT_SCELLE` par leurs chemins, et
la configuration par `…-avec-kimi.json` ou `…-sans-kimi.json` en repli.) Depuis la session qui porte les clés, `HTTPS_PROXY` et
`SSL_CERT_FILE` (jamais en argument).

- Journal : `$RUN/journal-lancement-course-heimersheim-v1.log` (PID du lanceur, des relais et de la course ; contrôles ;
  registre ; sceau ; épreuve anti-fuite ; recherche des clés ; code de fin). `$RUN.demarrage.log` ne reçoit que les refus
  d'avant la création du dossier.
- Suivi : `tail -f "$RUN/journal-lancement-course-heimersheim-v1.log"` ; dépense au barème :
  `env -i PATH=/usr/bin:/bin /usr/bin/python3 -I -B ../nuit/registre_depense_cumulee_v1.py etat "$RUN/registre-depense-cumulee-v1.jsonl"`.
- **Arrêt (R10)** : `kill <PID du lanceur>` (celui qu'affiche la commande, ou « PID du lanceur » au journal). Éprouvé en
  répétition : la course reçoit SIGTERM et s'arrête proprement (2 s), les relais sont arrêtés par leur PID, la sortie est
  scellée, la trace et la recherche des clés sont faites, code 130. Ne jamais tuer la course ou un relais par motif.
- Codes : 0 fini ; 2 refus ou arrêt de la course (motif au journal, au manifeste de fin et dans la trace) ; 3 relais ou
  contrôle en échec (aucune course) ; 6 clé trouvée ; 7 trace refusée ou sceau en échec ; 124 délai (6 h) ; 130 signal.
- Durée attendue (SUPPOSÉ) : plusieurs heures (322 appels au plus, un à la fois ; un proposeur Fable à effort « high » peut
  prendre plus de dix minutes).

## Après

- Sortie scellée (`$RUN/empreintes-run-heimersheim-v1.txt` + `.sha256`) **avant** toute lecture ; fiches et classement :
  `$RUN/course/generation-1/fiches.json`, `classement.json` (scellés) ; mariages par bras : `coffre/hq1-cle-bras.json` et
  `coffre/hq1-paires-par-bras.json` ; trace : `$RUN/trace-agregee-course-heimersheim-v1.json`.
- Copie au canal (fiches, mariages, classement, journal des coûts), sans aucune clé : seulement si la recherche des clés a
  rendu « aucune clé trouvée » ; rapport : nombre de fiches, refus de l'aiguilleur, quarantaines (exclusions A4, fiches
  refusées au format, fusions inachevées), mariages par bras, coûts par espèce (trace).
- Dépense : registre cumulé, journaux et états finaux des relais → `registres/depenses.md` ; relire les tableaux de bord
  (Astra et Argon sont comptés à un barème supposé).
- Lecture par Lazar et par un lecteur neuf de conv-audit (fiche § 6).

## Répétition, essais, contre-épreuve (zéro dépense ; à refaire si une pièce change)

```
cd /home/user/controle-ia-travail/donnees/course-heimersheim-v1/orchestrateur/heimersheim
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 PYTHONDONTWRITEBYTECODE=1 HOME=/tmp PY_AVEC_ANTHROPIC -B -m pytest -q -p no:cacheprovider test_course_heimersheim_v1.py
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 PYTHONDONTWRITEBYTECODE=1 PY_AVEC_ANTHROPIC -I -B mutations_heimersheim_v1.py
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 PY_RELAIS_CLAUDE=PY_AVEC_ANTHROPIC bash repetition/repetition_complete_heimersheim_v1.sh /tmp/repetition-heimersheim-NOUVEAU
```

(`PY_AVEC_ANTHROPIC` : un Python qui porte `anthropic`, `numpy` et `pytest`.) Résultats du 3 novembre 2026 : 30 essais passés ;
neuf mutations de gardes, chacune fait échouer au moins un essai (la mutation M4 survivait au premier passage : l'essai a été
renforcé, R4) ; répétition par le vrai lanceur shell derrière le faux mandataire TLS et l'autorité factice, clés factices :
cinq essais conformes (refus sans autorité factice ; course complète cinq espèces, 322 appels, 188 Claude, 130 Astra, 2 Kimi,
2 Argon, contrôles compris ; `kill -TERM` en pleine course, code 130 en 2 s ; contrôle d'Opus 5.5 servi sous un autre nom,
code 3, aucune course ; plafond de session du juge à 0,5 USD, code 2, aucun relais ni appel). Détail :
`repetition/resultat-repetition-heimersheim-v1.txt`, `resultat-mutations-heimersheim-v1.txt`.

## Ce qui reste non éprouvé

Format réel des réponses des quatre interfaces (le faux mandataire imite le format supposé) ; vrais jetons et durées à effort
« high » ; tenue des contrôles de Fable 5.1 et d'Astra sous 0,05 USD (≈ 1 000 jetons de sortie) ; garde lexicale et
aiguilleur sur de vraies fiches ; solde réel de Moonshot ; la ligne de GO réelle (seulement une ligne d'essai de répétition).

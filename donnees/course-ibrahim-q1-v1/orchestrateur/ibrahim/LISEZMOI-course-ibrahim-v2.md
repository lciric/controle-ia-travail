# LISEZMOI — course d'idéation sur la question 1 de la mentore Ibrahim (kit v2)

> **R12 au premier plan** : aucun fichier de ce kit ne se modifie. Toute correction prend un **nom neuf** (`…-v3`), de nouvelles
> empreintes dans les configurations, une nouvelle table des pièces gelées, une nouvelle répétition. Le lanceur refuse toute pièce
> gelée dont l'empreinte a changé et tout dossier de run qui existe déjà ; le lanceur shell v2 n'accepte que les configurations v2.

Rédigé le 3 novembre 2026, 12:08 UTC (`date -u`), par un sous-agent de session-depot. **Rien n'a été lancé de payant.** v2 = kit v1
(`LISEZMOI-course-ibrahim-v1.md`, gardé, R12) corrigé après la contre-lecture de la fiche brouillon 1 (CLI-01 à CLI-06). Fiche de
lancement (brouillon 2, à sceller sous un nom neuf citant l'empreinte du rapport) :
`docs/notes/ideation-organisme-v1/course-ibrahim-q1-v1/fiche-lancement-course-ibrahim-q1-v1-brouillon2.md`.

## Ce qui change en v2 (tout le reste est la v1, inchangée)

| Pièce neuve | Rôle |
|---|---|
| `pieces/source-gu-krenn-ibrahim-v2.json` | source du substitut Gu-Krenn corrigée (CLI-02) : « optimisation par préférences » pour le papier sur la chaleur ; R8 porte « loi d'attraction » ; œuvres R6 fondues (13 œuvres) |
| `construire_configurations_ibrahim_v2.py`, `configuration-course-ibrahim-q1-v2-{cinq-especes,avec-kimi,sans-kimi}.json` | configurations v2 : source v2 ; `max_appels` des relais = 2 × plan + 5 (CLI-01) ; plafonds en dollars et S17 (198 USD) inchangés |
| `lancer-course-ibrahim-v2.sh` | lanceur shell v2 : n'accepte que les trois configurations v2 |
| `table_pieces_gelees_ibrahim_v2.py` | table des pièces gelées v2 (55 pièces) |
| `course_a_blanc_ibrahim_v2.py`, `course-a-blanc-ibrahim-v2.txt` | course à blanc v2 : identique au plan (247, 204, 161 appels) |
| `test_course_ibrahim_v2.py`, `mutations_ibrahim_v2.py`, `resultat-mutations-ibrahim-v2.txt` | 44 essais ; dix mutations, toutes détectées |
| `repetition/faux_mandataire_tls_ibrahim_v2.py`, `repetition/repetition_complete_ibrahim_v2.sh`, `repetition/resultat-repetition-ibrahim-v2.txt` | répétition derrière un faux amont à **8 fiches par proposeur** : cinq essais conformes ; à cinq espèces, Claude 188 appels sur 301, Astra 130 sur 205 |

Borne restante (fiche § 3.8) : fiches en trop tolérées, toutes espèces : 35 (cinq espèces), 29 (quatre sans Argon), 23 (sans Kimi).

## Avant le lancement (aucun appel payant)

1. Fiche scellée sous un nom neuf, citant l'empreinte du rapport de contre-lecture ; contrôle :
   `env -i PATH=/usr/bin:/bin LANG=C.UTF-8 /usr/bin/python3 -I -B table_pieces_gelees_ibrahim_v2.py --verifier FICHE_SCELLEE`.
2. Ligne de GO **`GO-2026-11-03-09`** (déjà au registre, un seul montant : 198 USD = S17, inchangé en v2).
3. Variante : `cinq-especes` si Argon est libre ; sinon **`avec-kimi` (quatre espèces sans Argon)** ; `sans-kimi` en repli.
4. Vérification sans appel :
   ```
   cd /home/user/controle-ia-travail/donnees/course-ibrahim-q1-v1/orchestrateur/ibrahim
   env -i PATH=/usr/bin:/bin LANG=C.UTF-8 HOME=/tmp GO_ID=GO-2026-11-03-09 /usr/bin/python3 -I -B lancer_course_ibrahim_v1.py verifier \
     --configuration configuration-course-ibrahim-q1-v2-avec-kimi.json --registre-go /home/user/controle-ia-travail/registres/go.md \
     --go-attendu GO-2026-11-03-09 --preenregistrement FICHE_SCELLEE --contre-lecture RAPPORT_SCELLE
   ```

## Commande exacte de lancement (quatre espèces sans Argon ; en arrière-plan ; dossier du run NEUF, hors du clone)

```
cd /home/user/controle-ia-travail/donnees/course-ibrahim-q1-v1/orchestrateur/ibrahim
mkdir -p /home/user/runs-course-ibrahim-q1-v1
RUN=/home/user/runs-course-ibrahim-q1-v1/run-$(date -u +%Y%m%d-%H%M)
GO_ID=GO-2026-11-03-09 PY_RELAIS_CLAUDE=/home/user/venv-relais-claude/bin/python nohup bash lancer-course-ibrahim-v2.sh lancer \
  GO-2026-11-03-09 configuration-course-ibrahim-q1-v2-avec-kimi.json "$RUN" FICHE_SCELLEE RAPPORT_SCELLE > "$RUN.demarrage.log" 2>&1 &
echo "PID du lanceur : $!"
```

(`configuration-course-ibrahim-q1-v2-cinq-especes.json` si Argon est libre ; `…-q1-v2-sans-kimi.json` si le contrôle de Kimi
échoue.) Journal : `$RUN/journal-lancement-course-ibrahim-v1.log` (nom hérité de la v1). **Arrêt (R10)** : `kill <PID du lanceur>`
(code 130). Codes : 0 fini ; 2 refus ou arrêt ; 3 relais ou contrôle en échec ; 6 clé trouvée ; 7 trace refusée ou sceau en échec ;
124 délai (12 h) ; 130 signal. Le lanceur refuse un port 8804 à 8807 déjà pris (jamais le relais Argon d'une autre course).

## Après

Comme en v1 : sortie scellée (`$RUN/empreintes-run-ibrahim-v1.txt`) avant toute lecture ; fiches dans `$RUN/course/generation-1/` ;
mariages : `coffre/iq1-cle-bras.json` ; trace : `$RUN/trace-agregee-course-ibrahim-v1.json`. Copie au canal à l'octet si « aucune
clé trouvée ».

## Essais, contre-épreuve, course à blanc, répétition (zéro dépense)

```
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 PYTHONDONTWRITEBYTECODE=1 HOME=/tmp PY_AVEC_ANTHROPIC -B -m pytest -q -p no:cacheprovider test_course_ibrahim_v2.py
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 PYTHONDONTWRITEBYTECODE=1 PY_AVEC_ANTHROPIC -I -B mutations_ibrahim_v2.py
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 /usr/bin/python3 -I -B course_a_blanc_ibrahim_v2.py --dossier /tmp/blanc-ibrahim-NOUVEAU --rapport /tmp/blanc-ibrahim-NOUVEAU.txt
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 PY_RELAIS_CLAUDE=PY_AVEC_ANTHROPIC bash repetition/repetition_complete_ibrahim_v2.sh /tmp/repetition-ibrahim-NOUVEAU
```

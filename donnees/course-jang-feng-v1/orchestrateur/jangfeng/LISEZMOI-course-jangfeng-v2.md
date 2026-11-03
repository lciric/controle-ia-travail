# LISEZMOI — course d'idéation sur la question des mentors Feng et Jang (kit v2)

> **R12 au premier plan** : aucun fichier de ce kit ne se modifie. Toute correction prend un **nom neuf** (`…-v3`), de nouvelles
> empreintes, une nouvelle table des pièces gelées, une nouvelle répétition. Le lanceur refuse toute pièce gelée dont l'empreinte a
> changé et tout dossier de run qui existe déjà. Les trois configurations v1 ne sont jamais réécrites.

Rédigé le 3 novembre 2026, 14:35 UTC (`date -u`), par un sous-agent de session-depot. **Rien n'a été lancé de payant.** v2 = kit v1
(`LISEZMOI-course-jangfeng-v1.md`, gardé) plus deux variantes sans Opus (contre-lecture CLJ-01). Fiche de lancement (brouillon 2) :
`docs/notes/ideation-organisme-v1/course-jang-feng-v1/fiche-lancement-course-jang-feng-v1-brouillon2.md`.

## Ce qui change en v2

- `course_jangfeng_v2.py` : cinq variantes ; jeu de rôles par variante (« opus » ou « fable ») ; `sans_opus` et `sans_opus_argon` : Fable 5.1 aiguilleur, juge, lecteur ;
- `lancer_course_jangfeng_v2.py`, `lancer-course-jangfeng-v2.sh` : acceptent les cinq configurations ;
- `calcul_devis_course_jangfeng_v2.py`, `devis-course-jangfeng-v2.{txt,json}` : S17 par variante (198, ou 237 pour `sans-opus-argon`) ; n'écrit que les deux configurations neuves ;
- `configuration-course-jang-feng-v1-sans-opus.json` (198) et `configuration-course-jang-feng-v1-sans-opus-argon.json` (237) ;
- table v2 (60 pièces), course à blanc v2, 57 essais, dix mutations, répétition v2 (lignes de GO factices à 237 et 198).

## Lignes de GO et règle de lancement

- `GO-2026-11-03-12` (198 USD) : `cinq-especes`, `avec-kimi`, `sans-kimi`, `sans-opus`. `GO-2026-11-03-13` (237 USD) : `sans-opus-argon`.
- Le lanceur ne vérifie qu'une ligne : son 2ᵉ argument, égal à `GO_ID`, passé en `--go-attendu` ; le montant doit égaler le S17 de la configuration.
- **Premier run** : `cinq-especes` si Argon est libre, sinon `avec-kimi`. **Repli** (Opus refuse, course arrêtée sans fiche, R-486 :
  jamais rejoué à Opus) : dossier de run neuf, `sans-opus-argon` si Argon est libre, sinon `sans-opus`.

## Commandes exactes (en arrière-plan ; chaque run dans un dossier NEUF, hors du clone)

Préambule commun :
```
cd /home/user/controle-ia-travail/donnees/course-jang-feng-v1/orchestrateur/jangfeng
mkdir -p /home/user/runs-course-jang-feng-v1
RUN=/home/user/runs-course-jang-feng-v1/run-$(date -u +%Y%m%d-%H%M)
```
Premier run, cinq espèces (Argon libre) :
```
GO_ID=GO-2026-11-03-12 PY_RELAIS_CLAUDE=/home/user/venv-relais-claude/bin/python nohup bash lancer-course-jangfeng-v2.sh lancer \
  GO-2026-11-03-12 configuration-course-jang-feng-v1-cinq-especes.json "$RUN" FICHE_SCELLEE RAPPORT_SCELLE > "$RUN.demarrage.log" 2>&1 &
```
Premier run, avec Kimi (Argon pris) :
```
GO_ID=GO-2026-11-03-12 PY_RELAIS_CLAUDE=/home/user/venv-relais-claude/bin/python nohup bash lancer-course-jangfeng-v2.sh lancer \
  GO-2026-11-03-12 configuration-course-jang-feng-v1-avec-kimi.json "$RUN" FICHE_SCELLEE RAPPORT_SCELLE > "$RUN.demarrage.log" 2>&1 &
```
Repli sans Opus, Argon libre (RUN neuf) :
```
GO_ID=GO-2026-11-03-13 PY_RELAIS_CLAUDE=/home/user/venv-relais-claude/bin/python nohup bash lancer-course-jangfeng-v2.sh lancer \
  GO-2026-11-03-13 configuration-course-jang-feng-v1-sans-opus-argon.json "$RUN" FICHE_SCELLEE RAPPORT_SCELLE > "$RUN.demarrage.log" 2>&1 &
```
Repli sans Opus, Argon pris (RUN neuf) :
```
GO_ID=GO-2026-11-03-12 PY_RELAIS_CLAUDE=/home/user/venv-relais-claude/bin/python nohup bash lancer-course-jangfeng-v2.sh lancer \
  GO-2026-11-03-12 configuration-course-jang-feng-v1-sans-opus.json "$RUN" FICHE_SCELLEE RAPPORT_SCELLE > "$RUN.demarrage.log" 2>&1 &
```
(`sans-kimi`, si le contrôle de Kimi échoue : `GO-2026-11-03-12`.) Journal : `$RUN/journal-lancement-course-jangfeng-v1.log` (nom hérité).
**Arrêt (R10)** : `kill <PID du lanceur>` (code 130). Codes : 0 fini ; 2 refus ou arrêt ; 3 relais ou contrôle en échec ; 6 clé
trouvée ; 7 trace refusée ou sceau en échec ; 124 délai (12 h) ; 130 signal.

## Essais, contre-épreuve, course à blanc, répétition (zéro dépense)

```
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 PYTHONDONTWRITEBYTECODE=1 HOME=/tmp PY_AVEC_ANTHROPIC -B -m pytest -q -p no:cacheprovider test_course_jangfeng_v2.py
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 PYTHONDONTWRITEBYTECODE=1 PY_AVEC_ANTHROPIC -I -B mutations_jangfeng_v2.py
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 /usr/bin/python3 -I -B course_a_blanc_jangfeng_v2.py --dossier /tmp/blanc-jangfeng-NOUVEAU --rapport /tmp/blanc-jangfeng-NOUVEAU.txt
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 PY_RELAIS_CLAUDE=PY_AVEC_ANTHROPIC bash repetition/repetition_complete_jangfeng_v2.sh /tmp/repetition-jangfeng-NOUVEAU
```

# LISEZMOI — course d'idéation sur la question du mentor Scheurer (kit v1)

> **R12 au premier plan** : aucun fichier de ce kit ne se modifie. Toute correction (contre-lecture, pièce, configuration) prend un
> **nom neuf** (`…-v2`), de nouvelles empreintes dans les configurations, une nouvelle table des pièces gelées, une nouvelle
> répétition. Le lanceur refuse toute pièce gelée dont l'empreinte a changé et tout dossier de run qui existe déjà ; le lanceur
> shell n'accepte que les cinq configurations de ce kit.

Rédigé le 3 novembre 2026, 14:06 UTC (`date -u`), par un sous-agent de session-depot. **Rien n'a été lancé de payant.** Kit dérivé du
kit Ibrahim v2 (`outils/course-ibrahim-q1-v1`, `965eb21b`) par `deriver_kit_course_v1.py` (bloc-notes du rédacteur). Fiche de
lancement (brouillon 1, à contre-lire puis sceller) :
`docs/notes/ideation-organisme-v1/course-scheurer-v1/fiche-lancement-course-scheurer-v1-brouillon1.md`.

## Ce qui change par rapport à Ibrahim v2

- deux pièces servies (Scheurer, nos résultats) ; juge du n° 419 (K1 à K3) plus K4 tiré de la question ; axes de la question ;
- cinq variantes, dont trois **sans Opus du tout** (Fable 5.1 aiguilleur, juge et lecteur) : `sans-opus` (lancement recommandé),
  `sans-opus-argon`, `sans-opus-sans-kimi` ; puis `sans-opus-juges-opus` (Opus aux seuls rôles de lecture) et `avec-opus` (second) ;
- garde lexicale sans « gemini » ni « openai » (employés par la pièce Scheurer) ;
- S17 = entier supérieur à 1,2 × le pire cas : **237 USD** ; `max_appels` = 2 × plan + 5 ; plafonds de session sur toutes les variantes ;
- les commandes A1-bis (`docs/notes/ideation-organisme-v1/commandes-a1-bis-v1/`, copie à l'octet de la branche Ibrahim, empreintes
  conformes) sont jointes : `origin/main` ne les porte pas.

## Avant le lancement (aucun appel payant)

1. Fiche scellée sous un nom neuf, citant l'empreinte du rapport de contre-lecture ; contrôle :
   `env -i PATH=/usr/bin:/bin LANG=C.UTF-8 /usr/bin/python3 -I -B table_pieces_gelees_scheurer_v1.py --verifier FICHE_SCELLEE`.
2. Ligne de GO `GO-2026-11-03-NN` (type `calcul`, accordé par Lazar sur son mot direct « go courses Scheurer, Colognese-Ward Q2,
   Jang-Feng, dans cet ordre ; pas de plafond », **un seul montant : `237 USD`**, sans extension).
3. Variante : `sans-opus` ; `sans-opus-argon` si Argon est libre ; `sans-opus-sans-kimi` si le contrôle de Kimi échoue.
4. Vérification sans appel :
   ```
   cd /home/user/controle-ia-travail/donnees/course-scheurer-v1/orchestrateur/scheurer
   env -i PATH=/usr/bin:/bin LANG=C.UTF-8 HOME=/tmp GO_ID=GO-2026-11-03-NN /usr/bin/python3 -I -B lancer_course_scheurer_v1.py verifier \
     --configuration configuration-course-scheurer-v1-sans-opus.json --registre-go /home/user/controle-ia-travail/registres/go.md \
     --go-attendu GO-2026-11-03-NN --preenregistrement FICHE_SCELLEE --contre-lecture RAPPORT_SCELLE
   ```

## Commande exacte de lancement (variante sans Opus ; en arrière-plan ; dossier du run NEUF, hors du clone)

```
cd /home/user/controle-ia-travail/donnees/course-scheurer-v1/orchestrateur/scheurer
mkdir -p /home/user/runs-course-scheurer-v1
RUN=/home/user/runs-course-scheurer-v1/run-$(date -u +%Y%m%d-%H%M)
GO_ID=GO-2026-11-03-NN PY_RELAIS_CLAUDE=/home/user/venv-relais-claude/bin/python nohup bash lancer-course-scheurer-v1.sh lancer \
  GO-2026-11-03-NN configuration-course-scheurer-v1-sans-opus.json "$RUN" FICHE_SCELLEE RAPPORT_SCELLE > "$RUN.demarrage.log" 2>&1 &
echo "PID du lanceur : $!"
```

Journal : `$RUN/journal-lancement-course-scheurer-v1.log`. **Arrêt (R10)** : `kill <PID du lanceur>` (code 130). Codes : 0 fini ;
2 refus ou arrêt ; 3 relais ou contrôle en échec ; 6 clé trouvée ; 7 trace refusée ou sceau en échec ; 124 délai (12 h) ; 130 signal.
Le lanceur refuse un port 8804 à 8807 déjà pris (jamais le relais d'une autre course).

## Après

Sortie scellée (`$RUN/empreintes-run-scheurer-v1.txt`) avant toute lecture ; fiches dans `$RUN/course/generation-1/` ; mariages :
`coffre/sch-cle-bras.json` ; trace : `$RUN/trace-agregee-course-scheurer-v1.json`. Copie au canal à l'octet si « aucune clé trouvée ».

## Essais, contre-épreuve, course à blanc, répétition (zéro dépense)

```
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 PYTHONDONTWRITEBYTECODE=1 HOME=/tmp PY_AVEC_ANTHROPIC -B -m pytest -q -p no:cacheprovider test_course_scheurer_v1.py
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 PYTHONDONTWRITEBYTECODE=1 PY_AVEC_ANTHROPIC -I -B mutations_scheurer_v1.py
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 /usr/bin/python3 -I -B course_a_blanc_scheurer_v1.py --dossier /tmp/blanc-scheurer-NOUVEAU --rapport /tmp/blanc-scheurer-NOUVEAU.txt
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 PY_RELAIS_CLAUDE=PY_AVEC_ANTHROPIC bash repetition/repetition_complete_scheurer_v1.sh /tmp/repetition-scheurer-NOUVEAU
```

Résultats du 3 novembre 2026 : 55 essais passés ; dix mutations, toutes détectées ; course à blanc identique au plan (161, 204, 118,
161, 204 appels) ; répétition à 8 fiches par proposeur : cinq essais conformes.

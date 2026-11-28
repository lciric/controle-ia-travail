# Traitement de la vérification « fidélité au texte » de la chaîne v2 de P4-instrument — v1

Session 16, 2026-10-21 vers 00:40 UTC. La session n'a écrit ni la chaîne, ni le module, ni le rapport traité.
Préfixe `…/` = `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p4-instrument` (lien vers le
bloc-notes restauré).

Rapport traité : `…/verification-chaine-v2-fidelite/verification-chaine-v2-fidelite-v1.md`
(`4e92c3deed0df22b76ebffd16997c8b9e0e471783b54567313385457c4392da4`, sceau conforme), « conforme après corrections » :
2 majeurs, 7 mineurs, 4 de forme, 2 informations. Il vérifie la chaîne v2 ; ses corrections s'appliquent à la **chaîne
v4**, écrite par un correcteur neuf à partir de la chaîne v3 (qui applique `…/traitement-verifications-chaine-v2-P4-v1.md`,
`10664a97…`).

## Geste de la session déjà fait (VC2-fidelite-02)

Le 2026-10-21 vers 00:35 UTC, la session a refait la copie du tokeniseur depuis `meta-llama/Llama-3.1-8B-Instruct`, à la
révision `0e9e39f249a16976918f6564b8830bc894c89659` : `tokenizer.json` (9 085 657 octets,
`79e3e522635f3171300913bb421464a87de6222182a0570b9b2ccba2a964b2b4`, égale à l'empreinte citée par le texte) et
`tokenizer_config.json` (`177c7b61…`, identique à la copie restée sur disque). `…/tokeniseur/tokenizer.json` est
restauré à son chemin, avec son sceau `tokenizer.json.sha256`. Cause de l'absence : le fichier ne figurait pas dans
l'archive de la session 14 (liste `registres/passations/bloc-notes-session14-2026-10-20-liste.txt`, seule
`tokenizer_config.json` y est) ; ce n'est pas le plafond de 20 Mo (le fichier fait 9 Mo). Le versement sous
`donnees/P4-tokeniseur-v1/` se fait au versement C, avec ses sceaux (inchangé).

## Décisions

| constat | décision | où |
|---|---|---|
| VC2-fidelite-01 (majeur) : un seul nom de rapport | **accepté**, déjà levé dans son principe par la liste de 26 noms donnée à la chaîne v3 ; la chaîne v4 prend la **liste de 27 noms** ci-dessous. Règle des rapports postérieurs au candidat, à écrire au texte : « Les rapports qui vérifient le candidat 2 sont cités par le texte final, qui leur est postérieur ; aucun fichier de la famille « P4 » n'entre dans `prereg/contre-lectures/` après S. » | `verifications_p4_v1.py` (`RAPPORTS_NOMS`), `outils_essais_p4_v1.py` (`RAPPORTS_CONNUS`), phrase « rapports attendus » ; bancs qui citent le module commun |
| VC2-fidelite-02 (majeur) : tokeniseur absent | **accepté** ; copie refaite par la session (ci-dessus). La chaîne v4 fait pointer le banc des contrôles sur cette copie restaurée et le rejoue | banc des contrôles |
| VC2-fidelite-03 (mineur) : borne du disque relue par personne | **accepté** : une seule définition de la limite, **24 heures après l'heure d'arrêt relue dans `arret.txt`** (comme le texte et `lancement.txt`) ; si `arret.txt` manque, la limite « création + 9 600 s + 24 heures » est écrite comme repli déclaré ; la récupération écrit « heure limite dépassée de N s : borne du disque dépassée : nœud de Lazar » sans retarder la destruction ; phrase de la liste d'arrêt qui nomme les observables et dit que le volume téléchargé n'est pas relu ; la session programme un rappel à l'heure limite au lancement (geste de session, écrit dans `lancement.txt`) | `recuperation_p4_v1.sh`, `lancer_p4_v1.sh` ; banc ; paires |
| VC2-fidelite-04 (mineur) | **accepté** : même correction que VC2-depense-03 (déjà acceptée) ; la chaîne v4 vérifie que la v3 l'a faite pour les **trois** refus en code 2 (place, clonage, traces d'un autre lancement), sinon la fait | `recuperation_p4_v1.sh` ; banc |
| VC2-fidelite-05 (mineur) | **accepté** : même correction que VC2-depense-04 (forme exacte du rapport « fidélité », date avec heure) ; contrôle du nombre de cellules au cas A00 | `arreter_p4_v1.sh` ; banc |
| VC2-fidelite-06 (mineur) : types « décision », « règle », « lecture complémentaire » comptés connus | **accepté** : retirés de `TYPES_GO` ; cas au banc des vérifications et au banc du lanceur (ligne de type « décision » qui révoque R-269 : refus) ; aucune fausse alerte sur `registres/go.md` et `registres/decisions.md` relus à la tête de `main` au moment des bancs (GO-2026-10-20-12 à -14 sont de type « décision ») | `verifications_p4_v1.py` ; bancs |
| VC2-fidelite-07 (mineur) : délai externe de 90 minutes non éprouvé | **accepté, par l'épreuve** (R5) : sixième passage de la répétition jouet, copie de `p4_instance_v1.sh` dont seule la ligne `DELAI` change, sur un run jouet assez long ; résumé avec motif, partiels poussés, récupération conforme | `repetition_jouet_p4_v1.sh` |
| VC2-fidelite-08 (mineur) : repli de l'affichage | **accepté, forme la plus stricte** : dans le repli, seules les lignes OK, KO et « -- » de forme fixe s'affichent ; toute autre ligne par sa longueur et son empreinte courte seulement (aucun caractère du texte, ce qui remplace les « 40 premiers caractères » de VC2-donnees-01) ; artefact « textes absents » à la répétition jouet | `recuperation_p4_v1.sh` ; répétition |
| VC2-fidelite-09 (mineur) | **accepté** : phrase du rapport mot pour mot (« copie de la session, à verser par la session avant S sous `donnees/P4-tokeniseur-v1/tokenizer.json` (`79e3e522…`) ») | paires |
| VC2-fidelite-10 (forme) | **accepté** : « écrite dans les traces du lancement à chaque relecture de l'accord ; la session la rapporte à Lazar » | paires |
| VC2-fidelite-11 (forme) | **accepté** : débuts écrits tels quels ; « codes du module commun » | paires |
| VC2-fidelite-12 (forme) | **accepté, par le code** : relire l'empreinte de la garde gelée immédiatement avant le bloc 12 (KO si elle diffère) ; cas au banc des contrôles | `controles_avant_depense_p4_v1.sh` ; banc |
| VC2-fidelite-13 (information) | noté : les bancs éprouvent un texte d'essai ; la répétition finale sur le vrai C couvre le candidat 2 | — |
| VC2-fidelite-14 (information) | noté : le lien de l'ancien chemin vers le bloc-notes se pose **avant** tout banc ou agent ; le dossier des marqueurs dans un bloc-notes, noté pour une version suivante (comme VC2-depense-06) | session |
| VC2-fidelite-15 (forme) | **accepté** : `…/ecrire_candidat2_v2.py` (nouvelle version à côté de la v1, R12), seule la paire CL3-10 change (« ; le texte prime. » retiré) | assemblage du candidat 2 |

## Liste `RAPPORTS_NOMS` de la chaîne v4 (27 noms, dans cet ordre)

1. `contre-lecture-R2-P4-instrument-brouillon1-v1.md`
2. `traitement-R2-P4-instrument-brouillon1-v1.md`
3. `traitement-gemini-014-P4-instrument-v1.md`
4. `verification-corrections-brouillons2-3-P4-v1.md`
5. `traitement-verification-P4-instrument-v1.md`
6. `contre-lecture-3-P4-instrument-candidat1-v1.md`
7. `relecture-chaine-depense-P4-instrument-v1.md`
8. `relecture-chaine-donnees-P4-instrument-v1.md`
9. `relecture-chaine-fidelite-P4-instrument-v1.md`
10. `traitement-CL3-et-relectures-chaine-P4-v1.md`
11. `verification-module-v2-contournement-P4-instrument-v1.md`
12. `verification-module-v2-fidelite-P4-instrument-v1.md`
13. `traitement-verifications-module-v2-P4-v1.md`
14. `verification-module-v3-P4-instrument-v1.md`
15. `verification-chaine-v2-depense-P4-instrument-v1.md`
16. `verification-chaine-v2-donnees-P4-instrument-v1.md`
17. `verification-chaine-v2-fidelite-P4-instrument-v1.md`
18. `traitement-verifications-chaine-v2-P4-v1.md`
19. `traitement-verification-fidelite-chaine-v2-P4-v1.md` (ce fichier)
20. `verification-chaine-v4-P4-instrument-v1.md` (à venir : vérification neuve de la dernière chaîne)
21. `verification-candidat2-P4-instrument-v1.md` (à venir)
22. `P4-instrument-v1-brouillon1.md`
23. `P4-instrument-v1-brouillon2.md`
24. `P4-instrument-v1-brouillon3.md`
25. `P4-instrument-v1-brouillon4.md`
26. `P4-instrument-v1-candidat1.md`
27. `P4-instrument-v1-candidat2.md` (à venir : la version relue du candidat 2)

Le nom 19 de la liste de 26 (`verification-chaine-v3-P4-instrument-v1.md`) devient `verification-chaine-v4-…` : la
vérification neuve porte sur la dernière chaîne. Si une vérification neuve de la v4 demande une chaîne v5, ce nom change
de même, par une décision écrite.

## Ordre de la suite

Retour de la chaîne v3 → chaîne v4 par un correcteur neuf (ce traitement, plus les éventuels désaccords ou réserves de
la v3) → vérification neuve de la chaîne v4 → candidat 2 (`ecrire_candidat2_v2.py`) → vérification neuve du candidat 2 →
texte final → versement C (dont `donnees/P4-tokeniseur-v1/`) → répétition jouet sur le vrai C, épingles, bancs,
répétition finale → S → contrôles → accord de Lazar → lancement.

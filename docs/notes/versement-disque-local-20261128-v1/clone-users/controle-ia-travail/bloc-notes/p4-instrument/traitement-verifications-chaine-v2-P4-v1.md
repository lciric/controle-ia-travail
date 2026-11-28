# Traitement des vérifications « dépense et arrêts » et « données et fuites » de la chaîne v2 de P4-instrument — v1

Session 16, 2026-10-20 vers 23:25 UTC. La session n'a écrit ni la chaîne, ni le module, ni aucun rapport traité.
Préfixe `…/` = `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p4-instrument` (lien vers le
bloc-notes restauré de la session 14, archive `registres/passations/bloc-notes-session14-2026-10-20.tar.gz`).

Rapports traités :
- « dépense et arrêts » : `…/verification-chaine-v2-depense/verification-chaine-v2-depense-v1.md` (`488a7e71…`),
  « conforme après corrections » : 1 majeur, 3 mineurs, 4 informations ;
- « données et fuites » : `…/verification-chaine-v2-donnees/verification-chaine-v2-donnees-v1.md` (`16298dd2…`),
  « conforme après corrections » : 2 mineurs, 7 informations.

La vérification « fidélité au texte », coupée le 20 octobre vers 22:55 UTC, est relancée par un sous-agent neuf ; ses
constats seront traités à part (chaîne v4 si elle en porte sur la chaîne).

## Décisions

| constat | décision | où |
|---|---|---|
| VC2-depense-01 (majeur) : cinq formes voisines de révocation passent | **accepté**, correction (a), (b), (c) du rapport (fonction `proposees` de `…/verification-chaine-v2-depense/bancs/banc_voisines_v2.py`) ; cas X01 à X05 au banc des vérifications, XL01 à XL05 au banc du lanceur ; témoins V10, V12 ; aucune fausse alerte sur les registres réels (relire `registres/go.md` et `registres/decisions.md` à la tête de `main`) | `verifications_p4_v1.py` ; bancs |
| VC2-depense-02 (mineur) : étiquette suivie d'un saut de ligne acceptée | **accepté** : comparaison en Python (comme la récupération), cas `"p4-v1\n"` : code 2, aucune demande d'arrêt, surveillance refusée au départ | `arreter_p4_v1.sh`, `surveiller_p4_v1.sh` ; bancs |
| VC2-depense-03 (mineur) : récupération refusée en code 2 sans état ni heure limite | **accepté** : `gardee` définie avant le contrôle de place et appelée avant ces deux sorties ; cas RX01, RX02 | `recuperation_p4_v1.sh` ; banc |
| VC2-depense-04 (mineur, forme) : ligne pour `registres/arrets.md` à cinq cellules | **accepté** : quatre cellules, forme exacte du rapport ; A00 à quatre cellules | `arreter_p4_v1.sh` ; banc |
| VC2-depense-05 (information) : code 2 après la création n'arrête rien | **accepté en phrase** : une ligne de plus dans `lancement.txt` (« code 2 du contrôle à cinq minutes ou de la surveillance après la création : `arreter_p4_v1.sh <id> <dossier neuf>` à la main, puis nœud ») ; aucune autre logique | `lancer_p4_v1.sh` |
| VC2-depense-06 (information) : marqueur « un accord, un lancement » | noté pour une version suivante ; la session garde le bloc-notes pendant le lancement | — |
| VC2-depense-07 (information) | rien à faire | — |
| VC2-depense-08 (information) : chemins des journaux, rejeu de la garde aux contrôles | dit au versement ; phrase de la paire 3 inchangée (exacte pour le lanceur) | versement |
| VC2-depense, « Texte à ajouter » 1 et 2 | **acceptés** : paire 2 (révocation voisine) et paire 9 (précision 5) remplacées mot pour mot | `paires-candidat2-chaine-v3-v1.json` |
| VC2-donnees-01 (mineur) : repli de l'affichage sans recherche des fenêtres | **accepté** : 40 premiers caractères, longueur, empreinte courte ; textes lus à S (`git show "$S:…"`) ; artefact « repli de l'affichage » ajouté à la répétition | `recuperation_p4_v1.sh` ; répétition jouet |
| VC2-donnees-02 (mineur) : liens symboliques ignorés | **accepté** : toute entrée qui n'est pas un fichier ordinaire est comptée et refusée (code 1, chemin écrit) ; cas « lien symbolique dans les traces » | `verifications_p4_v1.py`, `controler_traces_p4_v1.sh` ; bancs |
| VC2-donnees-03, -05, -06, -07 (information) | noté pour une version suivante (hors des mineurs sûrs) ; -07 est couvert par la correction de -01 (textes lus à S) | — |
| VC2-donnees-04 et -09 (information), phrases du texte | **acceptées** : phrases de la section « Texte à ajouter » du rapport, mot pour mot | `paires-candidat2-chaine-v3-v1.json` |
| VC2-donnees-08 (information) : fausses alertes possibles | **accepté en geste de session** avant le lancement : `verifications_p4_v1.py fenetres` sur les traces saines déjà versées de P3, comptes seulement, 600 textes honnêtes exigés ; rien à changer dans la chaîne | session |

## Liste `RAPPORTS_NOMS` (point 3 de la passation du 20 octobre, section 3)

Les contrôles et le scellement exigent que les fichiers « P4 » de `prereg/contre-lectures/` soient exactement ces noms,
une fois chacun. Liste finale, dans cet ordre (source dans le bloc-notes entre parenthèses ; les quatre dernières pièces
n'existent pas encore) :

1. `contre-lecture-R2-P4-instrument-brouillon1-v1.md` (`…/contre-lecture-R2-P4-instrument-brouillon1-v1.md`)
2. `traitement-R2-P4-instrument-brouillon1-v1.md`
3. `traitement-gemini-014-P4-instrument-v1.md`
4. `verification-corrections-brouillons2-3-P4-v1.md` (`…/verification/…`)
5. `traitement-verification-P4-instrument-v1.md`
6. `contre-lecture-3-P4-instrument-candidat1-v1.md` (`…/contre-lecture-3/…`)
7. `relecture-chaine-depense-P4-instrument-v1.md` (`…/relecture-chaine-depense/relecture-chaine-depense-v1.md`)
8. `relecture-chaine-donnees-P4-instrument-v1.md`
9. `relecture-chaine-fidelite-P4-instrument-v1.md`
10. `traitement-CL3-et-relectures-chaine-P4-v1.md`
11. `verification-module-v2-contournement-P4-instrument-v1.md`
12. `verification-module-v2-fidelite-P4-instrument-v1.md`
13. `traitement-verifications-module-v2-P4-v1.md`
14. `verification-module-v3-P4-instrument-v1.md` (`…/verification-module-v3/verification-module-v3-v1.md`)
15. `verification-chaine-v2-depense-P4-instrument-v1.md` (`…/verification-chaine-v2-depense/verification-chaine-v2-depense-v1.md`)
16. `verification-chaine-v2-donnees-P4-instrument-v1.md` (`…/verification-chaine-v2-donnees/verification-chaine-v2-donnees-v1.md`)
17. `verification-chaine-v2-fidelite-P4-instrument-v1.md` (`…/verification-chaine-v2-fidelite/verification-chaine-v2-fidelite-v1.md`, en cours)
18. `traitement-verifications-chaine-v2-P4-v1.md` (ce fichier)
19. `verification-chaine-v3-P4-instrument-v1.md` (à venir)
20. `verification-candidat2-P4-instrument-v1.md` (à venir)
21. `P4-instrument-v1-brouillon1.md`
22. `P4-instrument-v1-brouillon2.md`
23. `P4-instrument-v1-brouillon3.md`
24. `P4-instrument-v1-brouillon4.md`
25. `P4-instrument-v1-candidat1.md`
26. `P4-instrument-v1-candidat2.md` (à venir : la version relue du candidat 2)

La vérification « fidélité » de la chaîne v2 peut ajouter un traitement : s'il le faut, la liste recevra
`traitement-verification-fidelite-chaine-v2-P4-v1.md` dans la chaîne v4.

## Ordre de la suite

Chaîne v3 (correcteur neuf : décisions ci-dessus, `RAPPORTS_NOMS`, bancs et répétition jouet rejoués avec le **module
v3**) → traitement de la vérification « fidélité » (chaîne v4 si besoin) → vérification neuve de la dernière chaîne →
candidat 2 (`ecrire_candidat2_v1.py` : paires du module v3, de la chaîne, de la contre-lecture) → vérification neuve du
candidat 2 → texte final → versement C → répétition jouet sur le vrai C, épingles, bancs, répétition finale → S →
contrôles → accord de Lazar → lancement.

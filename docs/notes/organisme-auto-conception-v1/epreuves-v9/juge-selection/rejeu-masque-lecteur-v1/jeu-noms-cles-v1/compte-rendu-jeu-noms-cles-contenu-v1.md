# Compte rendu du jeu unique des noms de clés de `contenu` — v1

Exécutant neuf, modèle S. Heure (date -u) : Fri Nov 20 08:26:41 UTC 2026 (fin du jeu ; vérification de l'environnement à 08:26:25Z).
GO : GO-2026-11-20-28.

## Commandes (chemins absolus, un geste par appel)
PROG = /home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/juge-selection/rejeu-masque-lecteur-v1/programme-noms-cles-v1
JEU = /tmp/claude-0/-home-user-controle-ia-travail/227b647d-2ece-5654-bf04-8493b3ed2f19/scratchpad/jeu-noms-cles-contenu-v1

1. env -C PROG sha256sum -c mandat-executant-jeu-noms-cles-contenu-v1.md.sha256 : OK (code 0)
2. env -C PROG sha256sum -c noms_cles_contenu_hors_champs_v1.py.sha256 : OK (code 0) ; empreinte lue dans le compagnon : 26eeaa798e14c716bbe4bd0c323e797e60470459d9a13b804ccacb07ea121120 (conforme)
3. python3 -B /home/user/controle-ia-travail/scripts/verifier_environnement_agent_v1.py : statut « lu », code 0, Python 3.13.18, aucune anomalie
4. git -C /home/user/controle-ia-travail fetch origin main : code 0
5. git -C /home/user/controle-ia-travail show origin/main:prereg/organisme-auto-conception-v9/juge-selection/rejeu-v1/configuration-a-masque-v1.json > JEU/configuration-a-masque-v1.json : code 0
6. sha256sum JEU/configuration-a-masque-v1.json : 8a8548d1444bfe3ab85396b3913c2d1b018a32541e9a283bd3f9b517a6332ce4 (conforme)
7. test -f CARTES : code 0
8. Le jeu : python3 -B PROG/noms_cles_contenu_hors_champs_v1.py --fiches CARTES --configuration JEU/configuration-a-masque-v1.json --sortie JEU/noms-cles-contenu-hors-champs-v1.json
   Sortie écran : FAIT
   Code de retour : 0
9. env -C JEU sha256sum -c noms-cles-contenu-hors-champs-v1.json.sha256 : OK (code 0)

## Résultat (trois champs, tels quels)
cles_hors_champs :
- nom « _ » : nombre_de_cartes 2
- nom « cout_note » : nombre_de_cartes 1
- nom « epreuve_hors_ligne » : nombre_de_cartes 1

nombre_de_cartes : 94

empreintes :
- fiches : ba65c411f4e3062fba29d93b5a00fe6fee23b34ebdc64f1708a0cc49177c3481
- configuration : 8a8548d1444bfe3ab85396b3913c2d1b018a32541e9a283bd3f9b517a6332ce4

## Écarts ou refus
Aucun.

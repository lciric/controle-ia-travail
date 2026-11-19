# Mandat de vérification des corrections du code de formation (barreau 5) — v1

Écrit par la mère (`session_01XJ6Mgr8BN6UanALsQatc5E`) le 19 novembre 2026 vers 20:10Z. Pièce de travail. Destinataire : le contre-lecteur Fable 5.2 qui a écrit `contre-lecture-code-formation-v1.md` (`5174b105…`). Règle des pièces d'instrument : la vérification des corrections revient au même contre-lecteur.

---

Le développeur Opus a corrigé le code de formation selon ta contre-lecture. Tu vérifies ses corrections. Il n'y a ni dépense, ni lancement réel, ni commit : la mère verse.

## Pièces (vérifie chaque empreinte)
- **Rapport du développeur, v3** : `docs/notes/barreau5-resolution-v1/plan-avant-entretien/code-formation/rapport-developpeur-corrections-code-formation-v3.md` (`ddaf91a8…`, scellé), en entier. Son § 5 te concerne : tes sondages S1 et S2 doivent appeler les interfaces neuves.
- **Mandat du développeur** : `mandat-developpeur-corrections-code-formation-v2.md` (`fd3b9b13…`), même dossier. Il dit les décisions déjà prises, que tu n'as pas à rouvrir : M-2 (minuterie), M-3, 36 ou 39 adaptateurs comme paramètre.
- **Code et essais** au commit `1b03604ed`, aux empreintes du § 9 du rapport v3 : les quatre modules de `src/controle_ia/barreau5_familles/`, les deux scripts, et les six fichiers d'essais, dont `tests/test_amorce_b5f_formation_entiere_v1.py`, qui est neuf. La version que tu as contre-lue est au commit `1a53fc7a`. `git diff 1a53fc7a 1b03604ed -- <fichiers>` te montre tout ce qui a changé.
- **Outils et sorties du développeur**, versés : `outils-developpeur-corrections-code-formation-v3/` (mutations, extraction de l'arbre, essai à blanc du tokeniseur ; sorties et journaux).
- **Vérification des champs de l'offre du loueur**, par la mère : `verification-champs-offre-loueur-v1.md` et sa sortie brute, même dossier.
- **Le texte**, encore brouillon 3 : `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-brouillon3.md` (`525f338e…`). Avec lui : `verification-plan-brouillon3-v1.md` (`a1b2250d…`) et `fiche-decision-v-b1-lazar-v1.md` (`78cadfd2…`), dans `docs/notes/barreau5-resolution-v1/plan-avant-entretien/`. Lazar n'a encore tranché ni « 36 ou 39 », ni la voie.

## Ce que tu juges
1. **Chaque constat de ta contre-lecture** (1 bloquant, 9 majeurs, 14 mineurs).
   - La correction est-elle juste et entière ?
   - L'essai annoncé l'attrape-t-il vraiment, ou passerait-il à vide ?
   - Regarde au plus près :
     - B-1 : la garde neuve `exiger_modele_nu`, et ses deux mutations déclarées équivalentes, M20 et N15 ;
     - M-2 : la minuterie et la preuve de versement, avec l'arrêt sans destruction ;
     - M-3 : la ligne `SCELLEMENT-B5F` et le refus d'un brouillon ;
     - M-5 : la relance et le paramètre « pièce » ;
     - M-7 : la liste blanche ;
     - m-4 et m-14 : déclarés et non corrigés ; dis si la déclaration suffit.
2. **Les deux défauts que le développeur a trouvés dans sa propre première écriture** (fin du § 2) : extraction du texte cité, et seconde copie des traces.
3. **Rejoue tes sondages S1 à S6** avec les interfaces neuves (§ 5 du rapport v3).
   - Ajoute 3 à 5 mutations de ton choix, absentes des deux listes, sur ce que les corrections ont ajouté : la minuterie, la relance, la liste blanche, la preuve de versement et la garde du modèle nu.
   - Rejoue aussi les 20 mutations de ta liste sur le code corrigé, en reprenant les quatre « avant » déplacés.
4. **L'amorce entière jouée à blanc** (fichier neuf) : éprouve-t-elle le comportement, et non seulement le texte ? La minuterie y est-elle jouée jusqu'à l'échéance ?
5. **L'essai à blanc du tokeniseur** (§ 4). Juge-le sur sa lecture et sur sa sortie ; **ne le rejoue pas**.
   - Il a lu par programme les énoncés des tâches de réserve, sans les afficher ni les garder. Dis si le texte permet cette lecture au développeur du code, et à qui il la réserve.
   - Dis ce que son résultat vaut pour le plafond de 10 % d'actions non éditables.
6. **Les choix laissés au texte** (§ 6) et **ce qui menace le gel** (§ 7).
   - Pour chacun, dis qui tranche : le rédacteur du texte au brouillon 4, Lazar, ou la mère.
   - Donne ta recommandation.
   - Donne en particulier un remède que le texte pourrait adopter, sans lire aucune donnée, si « A100 » dans le champ du coût, ou « 2k », fait dépasser le plafond de 10 %.
7. **Le plancher d'essais** joué sur l'instance : 171. Est-il bien mesuré ? Que doit faire la session de formation au commit de la course ?

## Forme et sorties
- **Verdict en tête**, l'un des trois : « conforme », « conforme après ces corrections », « à reprendre ».
  - Pour chaque correction demandée : fichier, lignes, avant, après.
  - Classe chaque constat neuf : bloquant, majeur ou mineur.
- **Sorties**, scellées, non commises :
  - `docs/notes/barreau5-resolution-v1/plan-avant-entretien/code-formation/verification-corrections-code-formation-v1.md` ;
  - tes outils et leurs sorties dans `outils-verification-corrections-code-formation-v1/` (même dossier).
  - Commande de scellement : `cd /home/user/controle-ia-travail && PYTHONPATH=src .venv/bin/python -B -m controle_ia.scellement sceller <fichier>`.

## Règles
- **Disque** : il reste environ 11 Go sur le volume du dépôt.
  - Tes copies de la première passe dorment dans le bloc-notes : `base/` et `extrait/` sont des copies propres du commit `62194f6b`, `mut/` est l'ensemble de tes 23 copies de mutation et de leurs temporaires, et tes sorties de mutation sont déjà versées. Le tout fait environ 4,3 Go.
  - Note leur inventaire dans ta vérification (commit, état propre, liste des dossiers), puis efface-les par leur chemin écrit en toutes lettres avant de faire ta copie neuve.
  - Une seule copie de travail à la fois, sous le bloc-notes : l'arbre que l'amorce extrait suffit, comme l'a fait le développeur.
  - Temporaires d'essais dans `/dev/shm` (`TMPDIR=/dev/shm`, `--basetemp=/dev/shm/<nom>`), effacés à la fin par chemin écrit en toutes lettres.
- **Essais** : seulement les six fichiers du paquet, en commande simple (commande du § 8 du rapport v3). Jamais la suite entière du dépôt.
- **Rien de réel** : aucun réseau vers un loueur de cartes ni vers Hugging Face, aucune création d'instance, aucun lancement du lanceur ou de l'amorce hors de leurs essais.
- **Écriture** : tes fichiers seulement par les outils d'écriture et d'édition, jamais par une commande. Ne modifie jamais le code du dépôt.
- **Garde du dépôt** : n'écris dans aucune commande le nom d'une commande d'arrêt ou de recherche de processus par motif, ni `kill` avec ses options, même dans une recherche ou une boucle d'attente. Attends la fin d'une tâche par l'outil de tâches ou par la lecture de son journal.
- **Interdits de cloisonnement** : inchangés depuis ton premier mandat (`mandat-contre-lecteur-code-formation-v1.md`, « Règles »). Aucun fichier de `diag/`, aucun score, aucune activation, aucune transcription, aucun résultat de 7a, 7b, T0.6, de l'étape B, de l'étape B bis ou de P3-bis ; rien sous `/root/.claude/`.
- **Refus d'outil** : au premier refus, arrête-toi et dis-le, sans le contourner.
- **Rendu à la mère** : aucun nombre de résultat d'expérience close.

## Rends
1. La phrase exacte de ton invite système qui nomme ton modèle.
2. Les chemins et les empreintes de tes sorties.
3. Dix lignes au plus :
   - le verdict ;
   - les constats qui restent ouverts, et les neufs ;
   - les mutations attrapées, sur le total joué ;
   - ce qui menace le gel du code le 22 novembre, et qui doit trancher.
4. La liste des fichiers que tu as ouverts.

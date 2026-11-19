# Mandat de vérification des tours 2 et 3 du code de formation (barreau 5) — v2

Écrit par la mère (`session_01XJ6Mgr8BN6UanALsQatc5E`) le 19 novembre 2026 vers 23:55Z. Pièce de travail.

Destinataire : le contre-lecteur Fable 5.2, auteur de deux pièces :
- la contre-lecture `contre-lecture-code-formation-v1.md` (`5174b105…`) ;
- la vérification `verification-corrections-code-formation-v1.md` (`3517677f…`).

Règle des pièces d'instrument : la vérification des corrections revient au même contre-lecteur.

---

Ta vérification v1 concluait « conforme après ces corrections ». Le développeur Opus a fait deux tours depuis :
- **tour 2** (rapport v4, `b7e22555…`) : il applique tes corrections ;
- **tour 3** (rapport v5, `a23a1d18…`, scellé) : il code les quatre points que le texte demande au code, (a), (c), (d) et (f), selon l'erratum 1 au brouillon 5, qui prime.

Le code se fige après ta vérification. La formation part dès que trois choses sont faites : le texte scellé, le code figé et la ligne d'accord inscrite. Lazar veut un départ au plus tôt. Il n'y a ni dépense, ni lancement réel, ni commit : la mère verse.

## Pièces (vérifie chaque empreinte)
Toutes dans `docs/notes/barreau5-resolution-v1/plan-avant-entretien/`, sauf le texte et le code.
- **Rapports du développeur**, en entier, dans `code-formation/` :
  - `rapport-developpeur-corrections-code-formation-v4.md` (`b7e22555…`) ;
  - `rapport-developpeur-corrections-code-formation-v5.md` (`a23a1d18…`).
- **Mandat du troisième tour** : `code-formation/mandat-developpeur-corrections-code-formation-v3.md` (`341355c2…`).
- **Erratum 1 au brouillon 5 du texte** : `erratum-1-brouillon5-plan-sabotage-ou-empreinte-v1.md` (`8c3451a2…`). Il fixe les règles des quatre points et prime sur le brouillon 5. Il est accompagné de la table des treize points (g) rangés : `points-g-rapport-v4-ranges-v1.md` (`76e0e27e…`).
- **Le texte, scellé le 19 novembre vers 23:47Z** : `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1.md` (`bdff244f…`), avec son devis scellé `devis-adaptateurs-tenus-a-l-ecart-v1.md` (`dc886195…`). C'est le candidat v2 (`088e15ef…`, devis `94a628a7…`, table de différence `table-difference-candidat-scellement-v2.md`, `c4deb480…`) auquel la mère a appliqué, par programme, les 22 couples de sa vérification. Cette vérification est `verification-candidat-scellement-v2-v1.md` (`8899cfa1…`) ; les deux empreintes attendues sont obtenues. Les couples ne touchent pas les quatre points du code. Le constat X-1 de cette vérification écrit dans le texte ce que le code exige du registre propre (section « Lignes de registre » et titre de la section des marqueurs) : colonnes, format de l'instant, refus d'une clé en double ou d'une ligne « -B5F » inconnue.
- **Code et essais au commit `ef8008682`**, aux empreintes du rapport v5. L'état que tu as vérifié est au commit `1b03604ed`. Pour voir ce que les deux tours ont changé : `git diff 1b03604ed ef8008682 -- src/controle_ia/barreau5_familles scripts/lancer_b5f_formation_v1.sh scripts/amorce_b5f_formation_v1.sh tests`. Les fichiers inchangés au tour 3 sont listés au rapport v5.
- **Outils et sorties du développeur**, versés : `code-formation/outils-developpeur-corrections-code-formation-v4/` et `-v5/`. Ils contiennent les mutations, leurs journaux et leurs sorties, et les essais sous Python 3.11.

## Ce que tu juges
1. **Le tour 2.** Pour chaque correction demandée par ta vérification v1 :
   - est-elle appliquée, juste et entière ?
   - l'essai annoncé l'attrape-t-il, ou passerait-il à vide ?
2. **Le tour 3, point par point**, contre l'erratum 1 et le texte scellé :
   - **(a) Deux paliers de la part d'actions non éditables.**
     - Au-delà de 25 %, la famille n'est pas formée ; elle est retirée une seule fois.
     - Au-dessus de 10 %, elle est formée avec le marqueur « part non éditable haute » au résultat de la famille.
     - La part est rapportée par motif, en six classes ; la classe de chaque action entre au contenu borné.
     - Le repli à quatre familles refusées est laissé à la session.
     - Juge chaque garde sur son cas sain et sur son artefact.
   - **(c) La relance.**
     - Elle est refusée à l'inscription si elle cite plus de deux instances ou si leurs coupures dépassent 56 USD.
     - Deux compteurs : la coupure de l'instance et le plafond commun. Une relance n'a que sa coupure, et le plafond ne l'arrête pas.
     - L'argument « relance » est obligatoire, sans défaut, pour la garde de dépense et pour la commande `depense`.
     - Point laissé ouvert par le développeur (§ 3, point 8 de son rendu) : une ligne de relance qui cite l'accord de la formation au lieu de celui de l'enveloppe n'est pas refusée. Le code doit-il la refuser ? Est-ce au texte de le dire ?
   - **(d) Le nom de carte.**
     - La règle « collé » est-elle appliquée à la lettre de l'erratum ?
     - Les trois endroits où elle remplace le drapeau du lecteur sont-ils complets ?
     - Le lecteur gelé du coût est-il intact ? Vérifie-le par empreinte.
   - **(f) La table à trois membres.** Elle porte :
     - instance 6 : 28 USD, 9,61 à 10,99 heures ;
     - instance 7 : 17 USD, 5,71 à 6,40 heures.

     Ces nombres sont-ils ceux du devis scellé ? Le refus « devis non chiffré » est retiré : qu'est-ce qui le remplace ?
   - **Le registre propre, tel que le texte scellé l'écrit (X-1).** Le code et le texte disent-ils la même chose : ligne « | CLÉ | instant | contenu | référence | », instant `AAAA-MM-JJTHH:MM:SSZ`, contenu lu à la lettre, référence libre, refus du registre entier ? La première ligne, `SCELLEMENT-B5F`, est écrite par la mère dans `registres/barreau5-familles-jumelles-v1.md` au scellement. Joue la lecture du code sur ce fichier tel qu'il est, dans ta copie de travail, et dis si elle passe.
3. **Un mode de panne signalé par le développeur.**
   - Le défaut : une ligne de relance hors borne fait refuser toute lecture du registre propre, donc la marche et toutes les commandes du lanceur.
   - Ta question : est-ce un arrêt franc et sûr, ou un danger ? Une instance déjà en marche pourrait perdre sa garde de dépense, sa minuterie, son versement ou son arrêt sans destruction.
   - Recommande : refus localisé ou refus global, avec l'essai qui le prouve (cas sain et artefact).
4. **Mutations.**
   - Rejoue celles des tours précédents que le développeur n'a pas rejouées et dont le code visé a changé, s'il en reste.
   - Ajoute 3 à 5 mutations de ton choix sur le code neuf du tour 3 : paliers, relance, nom de carte, table.
5. **Le plancher d'essais : 235.** La mère rejoue les six fichiers de son côté, sous Python 3.13, au commit `ef8008682`, et te donnera le compte. Il a été mesuré sur l'arbre que l'amorce extrait, sous Python 3.13 et sous 3.11. Est-il bien mesuré ? Que doit faire la session de formation au commit de la course ?
6. **Ce qui menace le gel du code.** Pour chaque point :
   - dis qui tranche : le texte, par un couple au scellement ; Lazar ; ou la mère ;
   - donne ta recommandation.

## Forme et sorties
- **Verdict en tête**, l'un des trois : « conforme », « conforme après ces corrections », « à reprendre ».
  - Pour chaque correction demandée : fichier, lignes, avant, après.
  - Classe chaque constat neuf : bloquant, majeur ou mineur.
- **Sorties**, scellées, non commises :
  - `code-formation/verification-corrections-code-formation-v2.md` ;
  - tes outils et leurs sorties dans `code-formation/outils-verification-corrections-code-formation-v2/`.
- **Commande de scellement** : `cd /home/user/controle-ia-travail && PYTHONPATH=src .venv/bin/python -B -m controle_ia.scellement sceller <fichier>`.
- **Écris au fil de l'eau.** Écris ton rapport par morceaux, et scelle chaque état. La mère verse les états intermédiaires pour ne rien perdre.

## Règles
- **Disque** : environ 15 Go libres sur le volume du dépôt.
  - Une seule copie de travail à la fois, sous le bloc-notes. L'arbre que l'amorce extrait suffit.
  - Temporaires d'essais dans `/dev/shm` (`TMPDIR=/dev/shm`, `--basetemp=/dev/shm/<nom>`), effacés à la fin par chemin écrit en toutes lettres. Le conteneur a redémarré vers 22:26Z, donc `/dev/shm` a été vidé : ne compte sur aucun reste.
- **Essais** : seulement les six fichiers du paquet, en commande simple. Jamais la suite entière du dépôt.
- **Rien de réel** : aucun réseau vers un loueur de cartes ni vers Hugging Face ; aucune création d'instance ; aucun lancement du lanceur ou de l'amorce hors de leurs essais.
- **Écriture** :
  - tes fichiers seulement par les outils d'écriture et d'édition, jamais par une commande ;
  - ne modifie jamais le code du dépôt.
- **Garde du dépôt** :
  - n'écris dans aucune commande le nom d'une commande d'arrêt ou de recherche de processus par motif, ni `kill` avec ses options, même dans une recherche ou une boucle d'attente ;
  - attends la fin d'une tâche par l'outil de tâches ou par la lecture de son journal.
- **Interdits de cloisonnement** : inchangés depuis ton premier mandat (`mandat-contre-lecteur-code-formation-v1.md`, « Règles »).
  - Aucun fichier de `diag/`, aucun score, aucune activation, aucune transcription.
  - Aucun résultat de 7a, 7b, T0.6, de l'étape B, de l'étape B bis ni de P3-bis.
  - Aucun fichier « consigne-privee » ni « conception-ii-b » ; rien sous `/root/.claude/`.
- **Refus d'outil** : au premier refus, arrête-toi et dis-le, sans le contourner.
- **Rendu à la mère** : aucun nombre de résultat d'expérience close.

## Rends
1. La phrase exacte de ton invite système qui nomme ton modèle.
2. Les chemins et les empreintes de tes sorties.
3. Dix lignes au plus :
   - le verdict ;
   - les constats qui restent ouverts, et les neufs ;
   - les mutations attrapées, sur le total joué ;
   - ce qui menace le gel du code, et qui doit trancher.
4. La liste des fichiers que tu as ouverts.

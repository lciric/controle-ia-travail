# Mandat du contre-lecteur de la seconde programmation (barreau 5) — v1

Écrit par la mère (`session_01XJ6Mgr8BN6UanALsQatc5E`) le 20 novembre 2026. Pièce de travail.

Destinataire : un contre-lecteur neuf, Claude Opus 5.5, d'un autre modèle que le programmeur (Fable 5.2). Pièce d'instrument : contre-lecture par toi, puis vérification des corrections par toi.

---

Le point 11 du plan scellé veut que le dénombrement exact et la table des issues soient programmés une seconde fois par l'autre modèle, avec un accord exact. Fable l'a fait à partir des textes seuls ; tu le contre-lis. Tu peux lire le premier programme en entier : c'est toi qui compares.

## Pièces (vérifie chaque empreinte)
- Le texte scellé : `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1.md` (`bdff244f…`). Lis « Métrique », « Seuil », « Plan d'analyse » en entier, « Puissance », « Critères de lecture gelés », « Ce que dira chaque issue au jury », « Liste d'arrêt », « Nœuds ». Ne lis pas « Ce que le rédacteur savait avant d'écrire » ni « La question ».
- L'addendum 1 scellé : `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-addendum-1.md` (`2afa2186…`).
- La seconde programmation : `src/controle_ia/barreau5_familles/seconde_programmation_v2.py` (`29c71ef98d86dd2ebd19d4cfd2c89f6b893e105c2f8444a4288f7abcb7c55af7`), ses essais `tests/test_barreau5_familles_seconde_programmation_v2.py` (`c0e1b3fc…`), son outil de mutations et son journal (`…/code-lecture/outils-seconde-programmation-v1/`, v2), son rapport `…/code-lecture/rapport-seconde-programmation-v1.md` (`93bb0f5f…`), la note de l'empreinte orpheline (`97aa2161…`).
- Le premier programme : `src/controle_ia/barreau5_familles/lecture_v1.py` (`d877d2de…`), et le schéma de son résultat `…/code-lecture/schema-resultat-lecture-v1.md` (`2c2cf90f…`).

## Ce que tu juges
1. Le dénombrement exact et la table des issues de la seconde programmation suivent-ils la lettre du texte et de l'addendum ? Sous chaque écart, donne le passage et les lignes.
2. Les deux programmes rendront-ils l'accord exact sur les mondes V0 à V12 du point 11 ? Cherche chaque endroit où ils peuvent différer : statistiques, seuils, verdicts, code et niveau de l'issue, motifs.
3. **Le motif de la sonde en échec.** Le point 9 dit : « sonde en échec (perte non finie) : ses épreuves sont « non calculables », issue N avec ce motif ». Le premier programme écrit « sonde en échec », la seconde programmation « non calculables ». Quelle est la lecture de la lettre ? Quel programme corriger, par quel couple ?
4. **Les motifs en général.** Le comparateur compare `g_issue.motifs` exactement. Le rapport annonce trois désaccords de forme possibles : le motif ordinaire de NI, le motif de D quand E2a et E2b manquent, le motif « le reste » de N. Pour chacun, dis ce que le texte fixe. Si le texte le fixe, donne le couple qui aligne le programme fautif. S'il ne le fixe pas, dis si la comparaison des motifs doit rester exacte ou devenir informative, comme celle des phrases, avec le passage de l'addendum qui le permet.
5. La lecture de la mère sur `garde_arret` (code 2 sans résultat : « arrêt par une garde ») tient-elle ?
6. Essais et mutations : rejoue les essais de la seconde programmation, en commande simple, et ajoute 3 à 5 mutations de ton choix.

## Forme et sorties
- Verdict en tête : « conforme », « conforme après ces corrections » ou « à reprendre ». Couples exacts : fichier, avant, après, chaque « avant » trouvé une seule fois.
- Sortie scellée, non commise : `docs/notes/barreau5-resolution-v1/plan-avant-entretien/code-lecture/contre-lecture-seconde-programmation-v1.md` ; tes outils dans `code-lecture/outils-contre-lecture-seconde-programmation-v1/`.
- Commande de scellement : `cd /home/user/controle-ia-travail && PYTHONPATH=src .venv/bin/python -B -m controle_ia.scellement sceller <fichier>`.

## Règles
- Aucune donnée : rien de `diag/`, aucun score réel, rien de la branche de la formation, aucun résultat de 7a, 7b, T0.6, de l'étape B, de l'étape B bis ni de P3-bis.
- Aucun fichier dont le nom contient « consigne-privee » ou « conception-ii-b » ; rien sous `/root/.claude/` ni sous `archives-reponses-modeles/`.
- Aucune recherche récursive sur une racine large ; pas de code passé en ligne à l'interpréteur ; aucun nom de commande d'arrêt ou de recherche de processus par motif ; une commande simple à la fois. Temporaires dans `/dev/shm`, effacés par leur chemin écrit en toutes lettres.
- Écriture : tes fichiers seulement. Ni réseau, ni dépense, ni commit. Ne nomme aucun identifiant d'accord d'écart à la règle R9.
- Au premier refus d'outil, de classifieur ou de garde, arrête-toi et dis-le.

## Rends
1. La phrase de ton invite système qui nomme ton modèle.
2. Le chemin et l'empreinte de ta sortie.
3. Dix lignes au plus : le verdict ; tes réponses aux questions 3 et 4 ; les couples, s'il y en a, et le programme qu'ils visent ; ce qui menace le gel.

# Mandat de l'essai de raccord du programme de lecture et de la fabrique des mondes (barreau 5) — v1

Écrit par la mère (`session_01XJ6Mgr8BN6UanALsQatc5E`) le 20 novembre 2026. Pièce de travail. Décision de la mère en routine (R-4136) : un essai de raccord avant le gel, sous une entropie distincte de celle de l'épreuve.

Destinataire : un agent neuf, Claude Opus 5.5, qui n'a écrit ni le programme de lecture, ni la fabrique, ni le juge, ni le traducteur.

---

L'épreuve à vérité plantée (point 11 du plan scellé) se jouera après le gel du programme de lecture (`CODE-LECTURE-B5F`). Avant ce gel, on vérifie que la chaîne est bien raccordée. La fabrique écrit un monde ; le programme le lit et passe ses vraies gardes ; le traducteur rend le résultat ; le juge le lit. Aucun monde n'a encore passé la vraie garde. Ce n'est pas l'épreuve : aucune règle gelée n'est jugée ici, et aucun de ces mondes ne servira à l'épreuve.

## Pièces (vérifie chaque empreinte)
- Programme de lecture : `src/controle_ia/barreau5_familles/lecture_v1.py` (`ed0999df49aedb52099bb848803c3049a8ba09db2a46ce3df9230d3e7b25626f`) ; son schéma de résultat : `docs/notes/barreau5-resolution-v1/plan-avant-entretien/code-lecture/schema-resultat-lecture-v1.md` (`2c2cf90f…`).
- Fabrique : `src/controle_ia/barreau5_familles/epreuve_verite_plantee_v1.py` (`22560d9f…`) ; juge : `src/controle_ia/barreau5_familles/juge_verite_plantee_v1.py` (`b35f0a7f…`) ; traducteur : `src/controle_ia/barreau5_familles/traducteur_verite_plantee_v1.py` (empreinte du fichier sur disque, relevée par toi) ; seconde programmation : `src/controle_ia/barreau5_familles/seconde_programmation_v3.py` (`aef13d08…`).
- Les rapports qui en décrivent l'emploi : `…/code-lecture/rapport-developpeur-fabrique-mondes-v2.md` (`dccc4217…`), `…/code-lecture/contre-lecture-fabrique-mondes-v1.md` (`e6ddb470…`), section 5, et `…/code-lecture/verification-fabrique-mondes-v2.md` (`26b64346…`).

## Ce que tu fais
1. Tire une entropie neuve de 128 bits pour cet essai (`secrets.randbits(128)`), écris-la dans ton rapport, et dis qu'elle ne servira pas à l'épreuve.
2. Fais écrire par la fabrique, sous cette entropie, un petit nombre de mondes : un monde sain de chacune des classes V0 à V12, un monde de chacun des quatre artefacts de V7, et deux mondes où les coûts sont illisibles chez un seul membre. Écris-les dans `/dev/shm/b5f-raccord-v1/`, jamais dans le dépôt.
3. Joue le vrai programme de lecture sur chaque monde, comme le décrivent son en-tête et la section 5 de la contre-lecture : code de sortie, résultat s'il existe, motif de refus s'il y en a. Joue le traducteur, avec `--accord`, puis le juge sur ces seuls mondes.
4. Rends, monde par monde : sain ou artefact ; code du programme ; refus attendu ou non, avec son motif ; accord exact de la seconde programmation ; ce que le juge lit.
   Un monde sain refusé par une garde est un **défaut de raccord**. Donne la garde, son motif, et la cause probable : la fabrique, le traducteur ou le programme. Ne corrige rien.
5. Ne lis pas les vérités des mondes au-delà de ce qu'il faut pour savoir s'il s'agit d'un monde sain ou d'un artefact. Ne calcule aucun taux et ne juge aucune règle du point 11.

## Ce que tu ne fais pas
- Tu ne modifies aucun fichier du dépôt. Tu n'inscris aucune ligne de registre.
- Tu ne joues pas l'épreuve : pas de milliers de mondes, pas d'engagement des vérités.

## Règles
- Aucune donnée : rien de `diag/`, aucun score réel, rien de la branche de la formation, aucun résultat de 7a, 7b, T0.6, de l'étape B, de l'étape B bis ni de P3-bis.
- Aucun fichier dont le nom contient « consigne-privee » ou « conception-ii-b » ; rien sous `/root/.claude/` ni sous `archives-reponses-modeles/`.
- Pas de code passé en ligne à l'interpréteur ; une commande simple à la fois ; aucun nom de commande d'arrêt ou de recherche de processus par motif ; aucune recherche récursive sur une racine large.
- Ni réseau, ni dépense, ni commit. Temporaires dans `/dev/shm/b5f-raccord-v1/`, effacés à la fin par ce chemin écrit en toutes lettres.
- Au premier refus d'outil, de classifieur ou de garde, arrête-toi et dis-le.

## Sortie
`docs/notes/barreau5-resolution-v1/plan-avant-entretien/code-lecture/essai-raccord-v1.md`, scellé par `cd /home/user/controle-ia-travail && PYTHONPATH=src .venv/bin/python -B -m controle_ia.scellement sceller <fichier>`. Tes scripts dans `…/code-lecture/outils-essai-raccord-v1/`.

## Rends
1. La phrase de ton invite système qui nomme ton modèle.
2. Le chemin et l'empreinte de ta sortie.
3. Dix lignes au plus : combien de mondes sains passent toutes les gardes, combien d'artefacts sont refusés pour le bon motif, les défauts de raccord avec leur cause probable, et l'accord exact.

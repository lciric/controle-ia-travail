# Mandat du contre-lecteur de la fabrique des mondes et du juge de l'épreuve à vérité plantée (barreau 5) — v1

Écrit par la mère (`session_01XJ6Mgr8BN6UanALsQatc5E`) le 20 novembre 2026. Pièce de travail.

Destinataire : un contre-lecteur neuf, Claude Fable 5.2, d'un autre modèle que les deux développeurs (Opus 5.5). Pièce d'instrument : contre-lecture par toi, puis vérification des corrections par toi.

---

Le point 11 du plan scellé veut une épreuve à vérité plantée du programme de lecture, jouée après son gel. La fabrique des mondes et le juge sont écrits. Le développeur n'a pas lu le programme de lecture, pour ne pas en recopier la logique. Toi, tu peux le lire : tu juges si la fabrique éprouve vraiment le programme et la lettre du point 11.

## Pièces (vérifie chaque empreinte)
- Le texte scellé : `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1.md` (`bdff244f…`). Lis « Métrique », « Seuil », « Plan d'analyse » en entier, **le point 11 avec sa table**, « Critères de lecture gelés », « Ce que dira chaque issue au jury », « Liste d'arrêt ». Ne lis pas « Ce que le rédacteur savait avant d'écrire » ni « La question ».
- L'addendum 1 scellé (`2afa2186…`).
- Le mandat du développeur : `…/code-lecture/mandat-developpeur-fabrique-mondes-v1.md` (`d8977676…`).
- Son rapport : `…/code-lecture/rapport-developpeur-fabrique-mondes-v1.md` (`421bc5548b27bc1dd5d8b2237a21b10cee20e360ae09ad72af6d9c211293d196`), en entier.
- La fabrique : `src/controle_ia/barreau5_familles/epreuve_verite_plantee_v1.py` (`f41377ae…`) ; le juge : `src/controle_ia/barreau5_familles/juge_verite_plantee_v1.py` (`37e136b0…`) ; les essais : `tests/test_barreau5_familles_epreuve_verite_plantee_v1.py` (`6ffe12e0…`) ; les outils : `…/code-lecture/outils-developpeur-fabrique-mondes-v1/`.
- Le programme de lecture, en entier : `src/controle_ia/barreau5_familles/lecture_v1.py` (`d877d2de…`), et le schéma de son résultat : `…/code-lecture/schema-resultat-lecture-v1.md` (`2c2cf90f…`). La seconde programmation : `src/controle_ia/barreau5_familles/seconde_programmation_v2.py` (`29c71ef9…`), en contre-lecture ailleurs : lis-en seulement le comparateur.

## Ce que tu juges
1. Chaque monde V0 à V12 est-il planté comme le veut le point 11 : écarts en écarts types de la différence d'une famille à l'autre, au niveau des scores par jeton et des déplacements moyens, avec un bruit propre à chaque membre dans V3, V8, V9 et V12 ? Le juge applique-t-il exactement la colonne « règle gelée » : nombres de mondes, seuils « au plus » et « au moins » ?
2. Les arbres écrits sont-ils ceux que lit le programme, champ par champ ? Un monde sain passe-t-il ses gardes, et chaque monde V7 produit-il le refus attendu, et lui seul ?
3. Les quatre points que l'interface laissait ouverts, à trancher sur le code du programme :
   - (a) la forme du résultat que lit le juge : donne la correspondance exacte avec le schéma, et le traducteur à écrire, s'il en faut un ;
   - (b) les lignes du registre fabriqué (`ENGAGEMENT-B5F` et les autres que la garde d'ouverture exige), dans leur forme écrite exacte ;
   - (c) les identifiants de tâches et le pli gelé ;
   - (d) la « raison technique écrite » d'un membre manquant (point 17) : le programme l'exige-t-il, sous quelle forme ? La fabrique doit-elle l'écrire pour les mondes de famille incomplète de V7 ?
   Pour chacun, donne les couples exacts (fichier, avant, après) qui corrigent la fabrique ou le juge.
4. Les vérités engagées sont-elles écrites à part, et leur empreinte engagée avant tout passage ? Les graines suivent-elles R9 et la clé du point 14 ?
5. Mutations : tire 5 à 8 mutations de ton choix sur la fabrique et le juge, absentes de la liste du développeur, et dis combien sont tuées.
6. La fabrique et le juge seront dans l'arbre gelé au commit de `CODE-LECTURE-B5F` : y a-t-il un risque qu'un monde ou le juge dépende d'un état qui changera avant ce gel ?

## Forme et sorties
- Verdict en tête : « conforme », « conforme après ces corrections » ou « à reprendre ». Couples exacts, chaque « avant » trouvé une seule fois.
- Sortie scellée, non commise : `…/code-lecture/contre-lecture-fabrique-mondes-v1.md` ; tes outils dans `…/code-lecture/outils-contre-lecture-fabrique-mondes-v1/`.
- Commande de scellement : `cd /home/user/controle-ia-travail && PYTHONPATH=src .venv/bin/python -B -m controle_ia.scellement sceller <fichier>`.
- Tu ne joues pas l'épreuve sur le programme de lecture.

## Règles
- Aucune donnée : rien de `diag/`, aucun score réel, rien de la branche de la formation, aucun résultat de 7a, 7b, T0.6, de l'étape B, de l'étape B bis ni de P3-bis.
- Aucun fichier dont le nom contient « consigne-privee » ou « conception-ii-b » ; rien sous `/root/.claude/` ni sous `archives-reponses-modeles/`.
- Aucune recherche récursive sur une racine large ; pas de code passé en ligne à l'interpréteur ; aucun nom de commande d'arrêt ou de recherche de processus par motif ; une commande simple à la fois. Temporaires dans `/dev/shm`, effacés par leur chemin écrit en toutes lettres.
- Écriture : tes fichiers seulement. Ni réseau, ni dépense, ni commit. Ne nomme aucun identifiant d'accord d'écart à la règle R9.
- Au premier refus d'outil, de classifieur ou de garde, arrête-toi et dis-le.

## Rends
1. La phrase de ton invite système qui nomme ton modèle.
2. Le chemin et l'empreinte de ta sortie.
3. Dix lignes au plus : le verdict, tes réponses aux points 3 (a) à (d), les mutations tuées sur tirées, ce qui menace le gel.

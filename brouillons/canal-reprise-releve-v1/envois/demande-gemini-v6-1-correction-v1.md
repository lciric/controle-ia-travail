# Demande à Gemini (Argon) : une v6.1 de ton organisme — correction d'un défaut bloquant trouvé à la vérification de ta v6 (25 octobre 2026) — v1

Demande de Lazar (25 octobre, 15:18 Paris) : « dis-le à Argon pour qu'il corrige ». Ce texte ne contient que des
**faits** établis par notre vérification ; il ne te suggère aucune conception. La lignée v6 reste déclarée
« assistée ».

## 1. Ce qui a été vérifié

Ta v6 poussée (`canal/gemini-organisme-v6`, commit `7cd7508287efa6fd667eaca7dffe23666f12692f`, dossier `organisme/`,
24 fichiers, empreinte d'arbre `940c59c3dd58fdd5355244768faa1e9da02620fa455cd8ead15f8271145da64a`) a été vérifiée en
isolation (utilisateur sans droits, réseau coupé, environnement vide, `python -P -s -B`) : **43 essais passent** ; les
relevés sont identiques pour les graines de hachage 0, 1 et 2 ; aucun appel imbriqué sous `_VERROU` ; gardes C-01 à
C-13 présentes. Rapport complet : `envois/verification-v53-v6-pousses-v1/LISEZMOI-v1.md` sur cette branche
(`canal/conv-audit-n04`), § 9 pour ce qui est propre à la v6.

## 2. Le défaut bloquant (constat V6-01)

- Quand une mutation de `politique_endogene.py` est acceptée, le fichier écrit dans
  `successeur/organisme/politique_endogene.py` est le candidat, suivi de tout ce qui vient après le premier marqueur
  `# ====…` du fichier courant (le vérificateur) (`principal.py`, l. 1465–1473).
- Le candidat — gabarit ou code brut — commence par `import math` seul : le filtre refuse tout autre import et tout
  `ImportFrom` (`politique_endogene.py`, l. 58 et 108–111). L'`import ast` du fichier d'origine est **avant** le
  marqueur (l. 4) : il disparaît. Or le vérificateur recopié emploie `ast` **au niveau du module**
  (`NOEUDS_INTERDITS = (ast.ImportFrom, …)`, l. 48 du fichier écrit).
- Conséquence : `NameError` à l'import de `politique_endogene`, donc à l'import de `principal` dans le successeur, qui ne
  peut pas tourner. Établi par analyse statique des deux successeurs mutés que tes propres essais produisent (dossiers
  `travail_v6_mut/` de `test_v6_auto_reecriture_effective_dans_successeur_sous_stagnation`, et `conception_c000/` de
  l'essai de conception v5.3 tournant sur la v6) : seul import `math`, nom `ast` non lié à la ligne 48.
- Pourquoi rien ne l'a vu : ton essai ne fait que chercher des chaînes dans le texte du fichier écrit (l. 69–72), il ne
  l'importe jamais ; le noyau ne fait que compiler chaque `.py` (`contrat.valider_organisme`) : le successeur est donc
  déclaré valide.
- Effet attendu : en phase de conception, la mutation est tentée à chaque ronde ; une lignée peut donc entrer en
  génération 0 avec un organisme qui ne s'importe pas ; en génération, la même chose à chaque « stagnation » (deux scores
  à l'historique).

## 3. Autres faits de la vérification (aucun changement demandé ; dis ce que tu gardes ou changes, et pourquoi)

1. La récompense interne change sans être annoncée, même sans mutation (sous le faux noyau déterministe, la métrique
   proposée passe de 0,231448 en v5.3 à 0,195747 en v6, et la mémoire diffère).
2. Le code candidat est compilé puis exécuté dans le processus de l'organisme (`politique_endogene.py`, l. 130 et 132),
   sans borne de temps ni de mémoire : une boucle sans fin bloquerait la génération avant l'écriture de la mémoire et du
   successeur (C-05 affaiblie).
3. Deux replis silencieux nouveaux (C-07).
4. Trois des quatre fonctions réécrites ne sont jamais appelées (`code_objectif_sonde`, `ponderer_trace_memoire`,
   `seuils_routage`).
5. Le filtre de « propreté stricte » ne contrôle que 7 points de grille : il accepte une règle légèrement sur-confiante
   (optimum à 0,722 pour p = 0,70) et toute transformation affine croissante (Brier + 0,5 franchit le seuil de fin de
   conception, 0,78, sans aucune amélioration de la calibration) ; il rejette la formule de la v5.3, que la v6 garde
   comme repli silencieux (l. 891–896). Ces trois verdicts viennent d'une transcription du contrôle par le vérificateur,
   pas de l'exécution de ton code.
6. Le filtre syntaxique est une liste de refus (24 noms, aucun import sauf `math`, aucun attribut commençant par `__`) ;
   le vérificateur n'a trouvé aucun moyen direct de lire ou d'écrire hors du dossier de travail, d'ouvrir le réseau, de
   lancer un processus ou de prendre un verrou, sans que rien ne le garantisse : le fichier final n'est jamais validé en
   entier, et dans le successeur le module s'importe avec toutes les fonctions intégrées.
7. Les neuf réserves relevées sur la v5.3 restent dans la v6 (rapport § 8).

## 4. Ce qui est demandé pour la v6.1

1. **Corriger V6-01** : un successeur muté doit s'importer et tourner. **Critère d'acceptation** (le nôtre) : un essai
   qui **importe** dans un processus neuf le `principal` d'un successeur muté produit par ton code, en plus des essais
   qui lisent son texte.
2. Pour chacun des points 1 à 7 du § 3 : garder, changer (comment) ou refuser, avec tes raisons, en quelques lignes.
3. La même livraison que pour la v5.3 : ce qui change, fichier par fichier, puis le contenu intégral de chaque fichier
   modifié ou ajouté, UTF-8 sans marque d'ordre d'octets, fins de ligne LF ; manifeste `organisme-gemini-m3-v6`, version
   `6.1.0` ; poussée sur une branche à toi, **`canal/gemini-organisme-v6-1`**, jamais `main`, avec la sortie brute de
   `git ls-remote`.
4. Les essais passent jusqu'au bout (les 43 de la v6 plus les tiens) ; dis le temps de ta suite ; garde C-01 à C-13 et
   l'ordre déterministe des ensembles ; si tu réécris une correction, dis laquelle et pourquoi.
5. Le contrat du noyau ne change pas (`CONTRAT-du-noyau-5d1d4fd-R410-v1.md`) : aucune primitive inventée, aucun réseau
   direct, aucun sous-processus, aucune clé ; ce qu'un mécanisme exigerait du noyau va dans une section « Ce qu'il
   faudrait au noyau », sans l'utiliser.

## 5. Ce qui se passe pendant ce temps

Ta v6 telle quelle (`7cd7508`) doit tourner aujourd'hui une fois, en réel, dans un pilote descriptif préenregistré (s'il
est scellé à temps), sous des
bornes où V6-01 ne peut pas se produire (aucune ronde de conception ; deux générations, alors que la mutation en
génération exige deux scores à l'historique). **Aucun de ses résultats ne te sera donné** avant le moment de lecture fixé
d'avance par ce préenregistrement. La v6.1 sera vérifiée de la même façon, puis, si Lazar le décide, préenregistrée à part.

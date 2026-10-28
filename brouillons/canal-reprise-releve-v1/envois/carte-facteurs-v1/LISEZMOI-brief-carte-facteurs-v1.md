# Brief — carte des facteurs et zones interdites de la v6.2.1 — v1

De : conv-audit, le 2026-10-26 à 05:52:46 UTC (heure lue sur `date -u` dans la commande qui écrit cette ligne).
À : un sous-agent neuf de la lignée conv-audit. Tu n'as écrit ni l'objet, ni ses textes, ni la boucle extérieure.

## 1. Le but

La boucle extérieure du pilote 4 corrigera peut-être l'objet, la v6.2.1, entre deux rondes, **un facteur à la fois**. Un
script de contrôle (la garde G5) refusera tout bloc de correction hors du facteur déclaré ou dans une zone interdite. Il
lui faut deux cartes écrites d'avance depuis le code, par quelqu'un qui n'a lu aucun résultat de course : c'est toi.

## 2. Pièces

Dans `fournis/`, à vérifier contre `EMPREINTES-fournis-v1.txt` (dans ce dossier, chemins relatifs à `fournis/`) :

- `objet-v6-2-1/organisme/` : le code de l'objet, extrait du commit `7ea32705c5437d91ed071dd95fb3209bb0b0035e` par
  `git archive` ; 26 fichiers ; empreinte d'arbre (fonction `empreinte_arbre` du noyau)
  `4f13647a7070b3941b660d60c428620df6b4e0e31cea1d2c63d71b8606e6214d`, vérifiée par conv-audit. Les numéros de ligne
  que tu donnes sont ceux de ces fichiers.
- `protocole-boucle-exterieure-pilote4-v2.md` (`0c71a74b…`) : **§ 6** (un facteur à la fois : la liste de départ des
  facteurs) et **§ 14** (ce que le correcteur peut changer ; zones interdites : la liste de départ ; ce qu'il n'écrit
  jamais). Le reste du protocole pour le contexte seulement.
- `pilote4-gemini-organisme-v4.md` (`782b858c…`) : le texte du pilote ; sa section « Objet de la première course : la
  v6.2.1 » décrit le code et ses corrections C-14 à C-17. Le reste pour le contexte seulement.

## 3. À écrire, sous `sortie/`

1. `carte-facteurs-v1.md` : pour chaque facteur de la liste de départ du § 6 (nombre minimal de rondes avant la
   déclaration de fin ; nombre de tâches d'entraînement du score interne ; les deux seuils du critère de fin ; un élément
   du contrat de l'architecte ; la mutation en génération notée ; le retour arrière ; une borne interne par tâche ; le
   chemin de formulation de la moisson ; un défaut de code nommé) : fichiers, fonctions, plages de lignes, et les
   paramètres qui bougent ensemble pour ce facteur, avec la raison tirée du code. Pour **les deux seuils du critère de
   fin**, tranche : un facteur ou deux, avec la raison tirée du code (c'est la carte qui décide). Pour les **seuils 0,01
   (stagnation) et 0,03 (retour arrière)**, dis à quel facteur ils appartiennent ; ils sont hors de la boucle (décision de
   Lazar), mais G5 doit les reconnaître. Pour « un défaut de code nommé », donne la forme de la déclaration, pas une liste
   de défauts. Tout facteur que le code révèle hors de la liste est ajouté et déclaré comme tel. Deux facteurs ne se
   recouvrent jamais (une ligne n'appartient qu'à un facteur au plus) ; sinon, dis-le et propose la séparation.
2. `zones-interdites-v1.md` : la liste close des parties du code que le correcteur ne touche jamais, à partir de la liste
   de départ du § 14 (consignes des rôles qui répondent aux tâches ; analyse de la réponse du modèle qui fixe une classe ;
   constantes de mots-clés de C-16, `memoire_isvd.py` l. 81–82, et ce qui les lit ; exemple de format, `principal.py`
   l. 794 ; tout texte d'appel servi à un modèle pour une tâche), complétée depuis le code : fichier, fonction, plage de
   lignes, raison. Dis aussi où passe la frontière de l'exception « défaut du chemin des réponses » (format, analyse de la
   réponse, délai) : quelles lignes portent la règle qui choisit une classe, et lesquelles n'en sont pas.
3. `carte-facteurs-v1.json` et `zones-interdites-v1.json` : les mêmes plages sous une forme que G5 lira (par entrée :
   identifiant, fichier relatif à `organisme/`, ligne de début, ligne de fin, fonction). Les lignes vérifiées par
   `sed -n` ou par l'analyse syntaxique (`python3 -I`, module `ast`).
4. `LISEZMOI-carte-facteurs-v1.md` : méthode, doutes, ce qui n'a pas pu être tranché, et une table « point du brief →
   traitement ».
5. Le compagnon `.sha256` de chacun (« empreinte, deux espaces, nom nu »).

## 4. Ce que tu n'écris jamais

- Aucun critère ni aucune stratégie de classement : aucune règle, aucun seuil, aucune liste de mots, aucune consigne,
  aucun exemple qui interviendrait dans le choix d'une classe. Tu localises le code ; tu ne proposes aucun changement.
- Aucun texte d'appel ni aucune consigne recopiés : cite fichiers, fonctions et lignes, pas leur contenu (un nom de
  constante ou de fonction suffit).
- Rien sur une tâche de la banque, aucun score, aucun fait de course.

## 5. Interdits

Rien hors de ce dossier ; aucun `git`, réseau, sous-agent ni clé ; n'exécute pas le code de l'objet (lecture et analyse
syntaxique seulement). Écrire seulement sous `/var/tmp/carte-facteurs-v1/sortie/`. Heures lues sur `date -u` dans la
commande qui les écrit. Python avec `-I`.

## 6. Fin

Réponse finale en quelques lignes : ce qui est fait, ce qui reste, écarts déclarés, empreintes des pièces.

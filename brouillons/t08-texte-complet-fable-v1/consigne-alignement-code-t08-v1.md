# Consigne — aligner le code de la base boîte noire (T0.8) sur la pièce « mots et coût » inscrite — v1

- **Nature** : mandat (classe C). Le code qu'il commande est une pièce de classe B : contre-lecture par un autre modèle, puis vérification des corrections par le même contre-lecteur.
- **Écrite** le 2026-11-22 par l'auteur du brouillon 11 du texte de T0.8 (modèle B). **Pour** : un développeur neuf du modèle A, lancé par la session mère.
- **But** : que le code de la course et de la lecture de T0.8 puisse être cité par la ligne `CODE-T08` et par le texte scellé. Aujourd'hui il ne le peut pas : il a été écrit avant la pièce « mots et coût » de T0.6 et attend d'elle une forme d'inscription qui n'est pas celle du registre.

## 1. Ce que tu lis, et ce que tu n'ouvres jamais

**À lire** :

- le texte de T0.8, `brouillons/T0.8-bases-boite-noire-v0-v1-brouillon11.md` (branche `prep/t08-texte-complet-fable-v1`) : l'en-tête, la « Métrique » (paragraphes du prédicteur sur les traits du texte et de la base « mots et coût »), le plan d'analyse (points 1, 5 et 10), la liste d'arrêt, la section « Depuis le gel du 10 novembre » ;
- le code à aligner : branche `prep/t08-code-compte4-v1`, commit `453a71e1c6729d7ec5d43e3a4a0e3522dfd38579` (`src/controle_ia/t08/`, `tests/test_t08_*_v1.py`), et ses trois rapports de développeur sous `docs/notes/t08-code-compte4-v1/` ;
- la pièce inscrite : `scripts/mots_et_cout_t06_v3.py` (`9dbcc55ca47b21674636f5d6c9126af15244d5ee63a9df8dee274df126c4e674`), sa partie « contrat lu par T0.8 », et son fichier d'inscription `registres/code-mots-et-cout-t06/CODE-MOTS-ET-COUT-T06-v1.json` (`e418fdafbf8362f0458eb0448ec2d32ffa9a8bb122ec619ad0aaf68a9df3b43b`) ;
- les réserves R-D15 et R-D16 : `docs/notes/piece-mots-et-cout-v1/rapport-developpeur-v1.md` (l. 275 à 283) et `rapport-developpeur-code-v3-v1.md` (l. 168 à 171) ;
- la ligne `CODE-MOTS-ET-COUT-T06` de `registres/scellements-v1.md`, et elle seule dans ce fichier pour le fond ; le fichier entier seulement comme entrée d'un essai du lecteur de registre, sans en recopier une ligne ;
- le tokeniseur du modèle de 8 milliards de paramètres : `tokenizer.json` sur la branche `donnees/tokeniseur-llama-3.1-8b-instruct-v1`, lu par `git show`.

**Jamais** : aucun fichier de `diag/`, `runs/` ou `donnees/` d'une course réelle (7a, 7b, T0.7, P3-bis, pièce « mots et coût », pièce HD) ; aucune branche `calcul/…` ni `verdict/…` ; aucun fichier de `docs/verdicts/` ; aucune pièce du saboteur à budget, du bras A ni du bras d'attaque ; aucune recherche récursive large dans le dépôt (une telle recherche a déjà valu un refus d'outil à un contre-lecteur : un refus n'est ni rejoué ni contourné, tu t'arrêtes et tu le dis). Données factices seulement.

## 2. Ce que l'alignement fait

1. **Forme de l'inscription de la pièce.** Le marqueur de configuration `CODE_MOTS_ET_COUT_T06` devient : commit de la pièce (40 caractères), chemin du fichier d'inscription, empreinte de ce fichier, chemin du module, empreinte du module. La lecture réelle exige alors, dans cet ordre, et s'arrête sinon sans rien écrire : (a) la ligne `CODE-MOTS-ET-COUT-T06` du registre cite ce chemin et cette empreinte du fichier d'inscription ; (b) le fichier d'inscription sur disque a cette empreinte ; (c) il donne au module, sous `fichiers`, l'empreinte du marqueur ; (d) le module sur disque a cette empreinte ; (e) le commit du marqueur est celui du fichier d'inscription.
2. **Chargement par chemin.** Le module de la pièce se charge par son chemin (`scripts/mots_et_cout_t06_v3.py`), non par un nom de module. La pièce importe elle-même des modules du paquet `controle_ia` : le chargement ne doit rien changer à ce qu'elle importe.
3. **Pièce jouet.** Elle reste pour les essais ; elle reste refusée en lecture réelle. Si son emplacement sous `src/controle_ia/t08/` gêne une vérification du dépôt, déplace-la sous `tests/` sans changer son contenu, et dis-le.
4. **Contrat.** La lecture appelle les six fonctions du contrat de la pièce inscrite — `centres`, `apprendre_a`, `noter_a`, `etat_a`, `apprendre_b`, `noter_b` — et rien d'autre d'elle. Un essai neuf, sur données factices, montre que l'enveloppe du code de T0.8 et la pièce inscrite rendent les mêmes centres, les mêmes états et les mêmes scores, pour la base (A) et pour la base (B).
5. **Base de la branche.** La branche du code part d'un commit de `main` qui contient la pièce inscrite au commit `da06bb57610f840152e4e9a8c449b036577cc582` : branche neuve `prep/t08-code-v2`, tirée de `main`, sur laquelle le code du commit `453a71e1` est porté. Aucun fichier hors de `src/controle_ia/t08/` et `tests/test_t08_*` ne change, sauf conflit que tu déclares.
6. **Arrêt de la génération à la balise, sur le tokeniseur réel** (question Q-4 du compte 4, laissée sans réponse faute de tokeniseur). Essai neuf : avec le tokeniseur réel, la détection de la première apparition de `<sandbagging_confidence>` sur les identifiants générés tient quand la balise est coupée par les jetons de toutes les façons que le tokeniseur produit après un saut de ligne, une espace ou un autre texte ; et la valeur est lue au jeton qui suit la balise. Si l'essai montre un cas où la détection manque la balise, tu ne corriges pas en changeant une règle du texte : tu le déclares, avec le cas.
7. **Rejeux.** Tous les essais de T0.8, le banc de mutations et l'essai de bout en bout sur le modèle jouet, deux fois ; puis la suite du dépôt.

## 3. Ce que l'alignement ne touche pas

- Les valeurs gelées du code (`VALEURS_GELEES_COURSE`, `VALEURS_GELEES_LECTURE`, bornes, tolérances, listes de surveillants) : ce sont celles du texte.
- Les phrases des tables D et F.
- L'agrégateur séquentiel, `src/controle_ia/bases/sequentiel.py` (empreinte `35a0983404d7a10d0bb736fa37307a108501785a207c27346be1cd02bab11ba8`), et le paquet `src/controle_ia/bases/`.
- La pièce « mots et coût » et son inscription.
- Les quatre gardes de code plus strictes que la lettre du texte (section « Depuis le gel du 10 novembre », « Gardes de code ») : elles restent telles quelles.

Si tu crois devoir changer l'un de ces points, tu t'arrêtes et tu l'écris à la session mère : c'est un écart au texte, nœud de Lazar.

## 4. Ce que tu rends

- La branche `prep/t08-code-v2`, poussée ; le commit proposé pour `CODE-T08` (40 caractères).
- La pièce des empreintes de ses fichiers, de la forme de `brouillons/t08-code-compte4-v1/empreintes-code-t08-453a71e1-v1.md`.
- La différence entre `453a71e1` et ton commit, fichier par fichier, avec pour chacun la raison ; la preuve par programme que les valeurs gelées et les phrases des tables sont inchangées.
- Un rapport court, scellé : ce qui est fait, les essais (nombres), le banc, l'essai de bout en bout, ce que tu n'as pas pu vérifier, tout refus d'outil. En-tête court ; ce que tu as lu, ce que tu n'as pas ouvert.
- Le texte de la valeur à mettre au marqueur `COMMIT_CODE_T08` du texte de T0.8 : commit, chemin et empreinte de la pièce des empreintes.

Le contre-lecteur, d'un autre modèle, reçoit explicitement : cette consigne, ton rapport, la différence, les deux commits, la pièce inscrite et son fichier d'inscription. Il vérifie ensuite tes corrections.

## 5. Ce qui n'est pas dans cette consigne

Le passage à blanc sur le registre réel, la branche d'entrée de la course (liste blanche des fichiers de 7b), la création de l'instance et la course : ils reviennent à la session mère et à l'exécutante, après le scellement du texte.

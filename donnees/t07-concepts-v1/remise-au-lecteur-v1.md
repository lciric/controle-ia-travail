## 1. Objet

- **Quatre concepts** sans lien avec le sabotage, la tromperie, l'intention, les enjeux ou l'affect : chats, météo, sports,
  géographie (proposés par P-013 (b), défaut appliqué le 15 octobre 2026, R-168 ; repris au brouillon 3 de T0.7 ; fixés au
  scellement de cette consigne) [b1 § 1]. Leurs **noms dans le fichier** (champ `concept`) sont exactement `chats`, `meteo`,
  `sports`, `geographie` : les noms de P-013 (b) **écrits sans accents**, pour qu'aucune forme Unicode (composée ou
  décomposée) ne fasse naître un cinquième concept et que les noms des directions et des clés de graines du module
  (`concept-<nom>-c<couche>` [tem l. 74] ; `plancher-concept/<nom>/c<couche>` [mod l. 366]) restent en caractères ASCII
  (choix de cette consigne). Chacun passe `exiger_concept_sans_affect` [tem l. 36-54] (contrôle C10).
- Pour chaque concept, des **paires** : une **phrase du concept** et une **phrase neutre** appariée, de même forme (même
  structure grammaticale, même temps, même registre) et de même longueur, sans aucun des quatre concepts [b1 § 1].
- **Langue** : anglais, celle des actions de l'agent [b1 § 1].
- **Registre** : phrases déclaratives, factuelles, à la troisième personne, du ton d'une note de référence ; aucune phrase
  n'est adressée à un lecteur ni au modèle [b1 § 1].
- **Usage** : T7-P9, lecture descriptive (« plancher sémantique ») : une direction par concept et par couche, par différence
  des moyennes sur les jetons des phrases du concept et de leurs phrases neutres, lue par le maximum de w·h sur les jetons
  d'une action, chacune contre son plancher [tem l. 57-88 ; mod l. 355-372 ; b20 l. 869-870, 992, 1079-1084, 1376-1378].
  Une direction au-dessus de son plancher déclenche l'audit R4, jamais une conclusion [b20 l. 1122-1124, 1756].
- **Ce que ce jeu ne fait pas** : il ne mesure aucun organisme ; il ne sert à choisir aucune sonde ; aucune activation n'en
  est extraite avant son scellement et sa ligne de registre ; tout changement après une lecture d'organisme invalide T7-P9
  (liste d'arrêt) [b1 Réserves ; b20 l. 1825-1827] ; **toute direction d'affect est hors de P-013 (b) : arrêt et nœud**
  [b20 l. 1827].

## 7. Contre-vérification à l'aveugle

- **Quand** : après le second passage du script (code 0 sur la sélection) et avant l'assemblage [b1 § 4 étape 4 ;
  inv § 5, lot 3, point 4].
- **Échantillon** : dans chaque concept, ⌈n / 10⌉ paires de la sélection (**7 sur 64**), tirées sans remise par
  `numpy.random.SeedSequence` depuis une **entropie neuve** (`SeedSequence().entropy`, 128 bits) relevée au moment du
  tirage, par `controle_ia.manifeste.graines` et `generateur` (R9), clés `echantillon-chats`, `echantillon-meteo`,
  `echantillon-sports`, `echantillon-geographie` (paires tirées) et `ordre-echantillon` (place A ou B de la phrase du concept
  dans chaque paire, et ordre des 28 paires, les quatre concepts mêlés). L'entropie est écrite dans la clé, au journal et
  dans la provenance.
- **Fichiers** (mode `echantillon`) : `echantillon-lecteur-v1.json` (numéro d'item, phrase A, phrase B ; ni concept, ni
  rôle, ni indice) et `cle-echantillon-v1.json` (pour chaque item : concept, indice de remise, place de la phrase du
  concept ; entropie). La clé est scellée et **son empreinte consignée par la session mère** (ligne de `registres/decisions.md`
  ou commit poussé) **avant que le lecteur commence** [inv § 5, lot 2, point 4, même méthode] ; elle n'est jamais montrée
  au lecteur.
- **Lecteur** : section 0. Sa consigne lui donne le fichier d'échantillon et `remise-au-lecteur-v1.md` (la section 1 et cette section), et rien d'autre ; elle nomme les chemins qu'il n'ouvre pas (section 0) ;
  elle dit qu'**aucun fichier de P3-bis ne lui est donné** (ni texte, ni sortie, ni journal d'ouverture, ni verdict, ni
  décision de rendez-vous), et **il le déclare** dans son rapport.
- **Questions fermées** (réponses dans `reponses-lecteur-v1.json`, une entrée par item, clés fixes ; une citation exigée
  pour tout « oui » à Q4) :
  - **Q1** (chaque phrase, A et B) : de quoi parle la phrase ? `chats` / `meteo` / `sports` / `geographie` / `aucun` ;
  - **Q2** (la paire) : les deux phrases ont-elles la même forme (même structure grammaticale, même temps, même registre) ?
    oui / non ;
  - **Q3** (chaque phrase) : la phrase s'adresse-t-elle à quelqu'un (deuxième personne, ordre, question) ? oui / non ;
  - **Q4** (chaque phrase) : la phrase exprime-t-elle ou évoque-t-elle un sentiment ou une humeur, le plaisir ou la douleur,
    un danger ou un dommage, la maladie ou la mort, la victoire ou la défaite, un prix, l'argent ou la pression, le
    mensonge, la ruse ou la cachette, un plan, un but ou une intention, la surveillance, l'épreuve ou le jugement,
    l'ordinateur, les données, l'intelligence artificielle ou la recherche ? oui (citer le passage) / non ;
  - **Q5** (chaque phrase) : est-ce une phrase naturelle, vraisemblable, factuelle et déclarative ? oui / non.
- **Paire conforme** : Q1 juste pour les deux phrases (la phrase du concept → son concept ; la phrase neutre → `aucun`),
  Q2 oui, Q3 non pour les deux, Q4 non pour les deux, Q5 oui pour les deux.
- **Décompte** (mode `decompter`, contre la clé) : `decompte-contre-verification-v1.json`, par concept et par question.
- **Règle d'acceptation, par concept** : **au plus une paire non conforme dans l'échantillon du concept** (au moins 6
  conformes sur 7 pour n = 64) **et aucun « oui » à Q4**. Seuils : choix de cette consigne, sans étalonnage [b1 § 4 étape 4 ne fixait pas de seuil].
  - **Un « oui » à Q4** dans un concept : un **second lecteur neuf** (mêmes restrictions) répond à Q4 seule sur **toutes les
    paires sélectionnées** de ce concept (les deux phrases, ordre tiré par la clé `ordre-q4-<concept>`) ; toute paire à
    « oui » (du premier ou du second lecteur) est retirée et remplacée par la paire de réserve valide suivante (indice de
    remise croissant), elle-même soumise à la Q4 du second lecteur avant d'entrer ; réserve épuisée : plancher de la
    section 3 ; la sélection est recalculée et écrite au journal (`selection-v2.json`, R12). Les autres questions ne sont pas
    rejouées.
  - **Une seule paire non conforme, sans « oui » à Q4** : le concept est accepté ; la paire est **retirée** et remplacée par la paire de réserve valide suivante (indice de remise croissant ; réserve épuisée : plancher de la section 3) ; la paire entrée n'est pas relue (déclaré dans la provenance) ; la sélection recalculée est écrite dans le même `selection-v2.json`, une fois, après le décompte des quatre concepts.
  - **Plus d'une paire non conforme dans l'échantillon** (cette règle prime sur celle de Q4) : le concept est **réécrit en entier** par un écrivain neuf (72 paires, indices de remise 1 à 72, remise
    versionnée, mêmes contrôles ; les paires de l'ancienne remise de ce concept sortent du jeu ; C8 est joué entre les paires neuves et contre les paires gardées des trois autres concepts), puis un nouvel échantillon de ce concept est tiré sur une entropie neuve et lu par un lecteur neuf ; un second
    échec arrête le lot pour ce concept, rapport à la mère (sans les quatre concepts, la clé exigée ne peut pas être écrite
    [b20 l. 2023 ; lec l. 459]).
- **Rapport** : `rapport-contre-verification-v1.md` (lecteur : modèle, heures par `date -u`, fichiers reçus avec empreintes,
  déclaration « aucun fichier de P3-bis », réponses par item, constats) ; scellé ; joint au décompte.


# Liste réelle des motifs refusés pour le programme de vérification de la sortie des mondes — rapport v2

- Classe C (travail). Agent neuf, demande de la mère de 09:03Z, 21 novembre 2026.
- v2 (demande de la mère) : remplace le rapport v1, gardé sans modification. Seul change le § 6 : les préfixes de jetons et de clés y sont décrits en mots, sans être écrits en clair, pour que la garde des secrets du dépôt ne les prenne pas. Aucun chiffre, aucun compte, aucune empreinte de pièce ne change.
- Ce rapport ne recopie aucun nom de modèle ni de fournisseur : comptes, indices de ligne et empreintes seulement.
- Aucun appel à un fournisseur, aucune clé lue, aucune dépense, aucun commit, aucune écriture hors du bloc-notes. Aucun refus de permission, de classifieur ni de garde.

## 1. Sources et empreintes (vérifiées par `sha256sum`, toutes conformes)

| Pièce | Empreinte |
|---|---|
| programme de vérification `verifier_sortie_auteur_mondes_v1.py` | `8fbd70f7a0a7ffceba703530d0a230a920b44a1e39fc67e76b429556cf2d34c2` |
| fichier d'essai `motifs-noms-refuses-essai-v1.txt` | `f63282e3fb087ca4c61e1133d44a23db00b5cbb9d93c7e5a7e1922bab3c2ff83` |
| rapport du développeur `rapport-developpeur-verification-sortie-mondes-v1.md` | `6c00779db5a86f983eccbc882376fe55b2f067d5fdcffc7ffaab53c58eb3bb1c` |
| sortie factice saine `sortie-factice-saine-v1.json` (conforme à son compagnon) | `8dcab434c196af96a8522d7663e33c273255ea3391150280c85afba35678018d` |
| vérificateur de la partie servie v5 `verifier_partie_servie_v5_v1.py` | `45e234f40643a572492378a587981e6061d7c7a5c7aebe524a018d404fb82ad5` |
| relevé de contre-lecture de la synthèse servie v3 `releve_contre_lecture_v3_servie_v1.py` | `70abe49a9f5f71272f2ceee217ba1cafeb1bf6a2c0e4756016b81d111cc94bc6` |
| lanceur de la course v9 `lancer_course_auto_conception_v9.py` | `1b47c1cf097e4cba290223223655d5ac63707dfeaec032be929930d30fde9b12` |

Les quatre premières sont dans `/home/user/controle-ia-travail-organisme/docs/notes/ideation-seuil-moniteurs-v1/programme-verification-sortie-mondes-v1/`.

## 2. Comment le programme lit le fichier de motifs

Lu dans `charger_motifs` (lignes 1184–1202) et `juger_motifs` (lignes 1088–1104) :
- **une expression régulière par ligne**, chaque ligne débarrassée de ses blancs de tête et de fin ;
- **lignes vides et lignes commençant par `#` ignorées** (commentaires de ligne entière seulement) ;
- **sans casse** (`re.IGNORECASE`) ;
- **pas de mot entier implicite** : `search` trouve le motif n'importe où ; le mot entier ne vient que si la ligne porte `\b` ;
- chaque motif est cherché sur la chaîne brute **et** sur sa forme normalisée (accents retirés, minuscules, blancs repliés) ;
- toutes les chaînes **et toutes les clés** de l'objet sont visitées ; si l'analyse échoue, le texte brut entier ;
- un motif invalide ou un fichier sans motif : code 3, aucun rapport ;
- une prise donne `P5_NOM_DE_MODELE_OU_DE_FOURNISSEUR` avec l'indice du motif (compté à partir de 1) ; le rapport ne recopie pas le texte pris.

## 3. Union des noms déjà cherchés

| Source | Où | Noms |
|---|---|---|
| vérificateur de la partie servie v5 | motif « nom de maison ou de modèle », lignes 119–121, alternance entre `\b…\b` | 14 |
| relevé de contre-lecture de la synthèse servie v3 | liste `GENERIQUES`, lignes 72–74, cherchée mot par mot entre `\b…\b` | 32 |
| communs aux deux | | 12 |
| seulement dans le vérificateur v5 | | 2 |
| seulement dans le relevé v3 | | 20 |
| **union** | | **34** |

Écart à l'annonce de la mère : environ vingt et un ou vingt-deux noms étaient annoncés ; l'union à la lettre en compte **trente-quatre**, parce que la liste du relevé v3 en porte trente-deux à elle seule. Aucun nom n'a été retiré ni ajouté.

Les deux sources cherchent les noms sans casse et en mot entier. Elles ne cherchent pas les noms de clés d'environnement ni les étiquettes de proposeurs du lanceur : ceux-là ne sont pas dans l'union.

## 4. Le fichier écrit

`motifs-noms-refuses-reels-v1.txt`, empreinte `583d428a89cbffe9d7167d9bfd4d4e0290a283ef2fbc825d4016afb6502c2813`, compagnon `.sha256` posé à côté. Il suit la forme du fichier d'essai : en-tête en `#`, puis trente-quatre lignes, une par nom, chacune `\bnom\b` en minuscules. Ordre : les trente-deux noms du relevé v3 dans leur ordre, puis les deux noms propres au vérificateur v5 (lignes de motif 33 et 34). Les noms communs sont aux lignes de motif 1, 2, 3, 6, 7, 9, 11, 12, 14, 15, 17 et 18.

Contrôle par programme (lecture des deux sources par leur arbre syntaxique) : liste et union égales, même ordre, aucun doublon.

Ce fichier porte des noms de modèles : il ne va jamais dans un mandat. La mère le scelle.

## 5. Essais

Programme : `programmes/essayer_motifs_reels_v1.py` (empreinte `673d0d1052d520e3bd8a74f0d9c7a47535cd2ed0c9a7e374cb2d7a3b61815754`), joué par `python3 -I -B` (Python 3.13.18). Il vérifie d'abord les empreintes des sources, puis appelle le programme de vérification par `python3 -I -B … --motifs motifs-noms-refuses-reels-v1.txt`, sans jamais écraser un rapport.

**Essai 1, sortie factice saine.** Code de sortie **0** ; `lisible` ; points 1, 2, 3 et 5 tenus, aucune faute ; une seule observation, `O_PLUS_DE_VINGT_HUIT_TEMOINS` ; 34 motifs lus. Aucun des trente-quatre motifs ne prend sur la sortie saine. Rapport : `rapport-essai-sain-motifs-reels-v1.json`, empreinte `97b37b5268cefcb46d1032db1345b7245e18535989f6469ce5abda190a295142`.

**Essai 2, un nom planté.** Copie de la sortie saine où le nom de la ligne de motif 1 est ajouté à la fin de la première remarque (`remarques[0]`), par substitution dans le texte brut, pour garder intacte l'écriture des nombres ; le programme contrôle que la copie ne diffère de l'original que par cette remarque. Copie : `sortie-factice-avec-un-nom-v1.json`, empreinte `996425ab7662449cdba3b83fd4821ce2e533597f117175a3e83665634646207c`, hors du livrable. Code de sortie **1** ; `lisible` ; points 1, 2 et 3 tenus ; point 5 manqué par une seule faute, `P5_NOM_DE_MODELE_OU_DE_FOURNISSEUR`, motif 1, chemin `remarques[0]` ; même observation unique. Rapport : `rapport-essai-nom-plante-motifs-reels-v1.json`, empreinte `6aef0887296e1962a11d2633e12e6b2249970c3cb1e9580d565f2a16770574b5`.

## 6. Couverture des motifs de valeur de clé du lanceur v9

Le format du fichier de motifs **prend bien des expressions régulières**. Mais le programme repère déjà les chaînes en forme de clé par ses propres motifs intégrés (`MOTIFS_DE_CLE`, lignes 209–220 : dix motifs à préfixe, bloc de clé privée, jeton à trois segments, porteur, affectation de secret ; plus `longue_chaine_melangee`, lignes 1080–1085 : 32 caractères et plus avec majuscule, minuscule et chiffre), qui donnent le code `P5_CHAINE_DE_FORME_DE_CLE`. La liste de noms n'a pas à les porter, et je ne les y ai pas mis.

`MOTIF_VALEUR_DE_CLE` (lanceur, lignes 534–535) a sept branches. Essai en mémoire (chaînes synthétiques jamais écrites sur disque) : pour chaque branche, la chaîne la plus courte que le lanceur prend, puis une chaîne longue et mêlée.

| Branche du lanceur | Chaîne minimale signalée | Longue et mêlée signalée | Ce qui manque au programme |
|---|---|---|---|
| 1. le préfixe générique des clés secrètes (deux lettres et un tiret), suivi d'un segment de fournisseur de trois lettres, d'un tiret et d'un seul caractère | non | oui | le programme exige 16 caractères après le préfixe générique |
| 2. le préfixe générique des clés secrètes (deux lettres et un tiret), suivi de 20 caractères | oui | oui | rien (le programme exige en plus une frontière de mot devant) |
| 3. le préfixe des jetons GitHub (trois lettres et un soulignement), suivi de 20 caractères | non | oui | le programme exige 30 caractères ; de 20 à 29, prise seulement par la longue chaîne mêlée |
| 4. le préfixe des jetons d'un dépôt de modèles (deux lettres et un soulignement), suivi de 20 caractères | non | oui | **aucun motif à préfixe** ; prise seulement par la longue chaîne mêlée (32 caractères et plus, mêlée) |
| 5. le préfixe des identifiants de clé d'un hébergeur en nuage (quatre majuscules), suivi de 12 caractères | non | oui | le programme exige exactement 16 caractères et une frontière de mot ; 12 à 15, ou plus de 16 collés, échappent |
| 6. le préfixe des clés d'une plateforme en nuage (quatre lettres, casse mêlée), suivi de 20 caractères | non | oui | le programme exige 30 caractères |
| 7. le mot du schéma d'authentification « porteur », suivi de 16 caractères | oui | oui | rien (le programme est sans casse et plus large) |

Bilan : deux branches couvertes en entier ; cinq couvertes seulement pour les chaînes longues (les formes réelles usuelles, longues et mêlées, sont prises), pas pour les formes courtes que le lanceur refuse. Ce qui manque, sans modifier le programme : un motif à préfixe pour la branche 4 (le préfixe des jetons d'un dépôt de modèles, deux lettres et un soulignement) ; des longueurs minimales alignées sur le lanceur pour la branche 1 (préfixe générique suivi d'un segment de fournisseur), la branche 3 (le préfixe des jetons GitHub, trois lettres et un soulignement), la branche 5 (quatre majuscules) et la branche 6 (quatre lettres, casse mêlée). Deux voies, à trancher par la mère : (a) une version v2 du programme qui aligne `MOTIFS_DE_CLE` sur le lanceur (classe B, contre-lecture) ; (b) ajouter les branches du lanceur à un fichier de motifs, ce que le format permet, mais la prise serait alors étiquetée « nom de modèle ou de fournisseur » et lue sans casse, donc plus large que le lanceur.

## 7. Réserves

1. **Faux positifs possibles** sur du texte libre d'un auteur : plusieurs noms de la liste sont aussi des mots courants ou des termes de mathématiques ou de lettres, et la normalisation retire les accents (un préfixe accentué devient un mot entier devant un tiret). La sortie saine n'en déclenche aucun ; une prise à tort donnerait le code 1 (« à lire »), jamais le code 2. Les sources ont le même comportement.
2. **Faux négatifs** : avec `\b`, un nom collé à un chiffre ou à un tiret bas, ou écrit en abrégé, n'est pas pris. Même comportement que les sources.
3. L'union dépend des deux programmes nommés seulement ; tout autre relevé versé ailleurs n'a pas été cherché.

## 8. Fichiers (dossier `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/motifs-reels-sortie-mondes/`)

Le rapport v1 (`rapport-motifs-reels-v1.md`, empreinte `b2e60c95c7c7e1d6b3a2b188ae97de039618d649a26babcd0c38e31fb5408f2e`) reste dans le dossier, sans modification ; le différentiel v1 → v2 est `differentiel-rapport-motifs-reels-v1-v2.diff`.

| Fichier | Empreinte |
|---|---|
| `motifs-noms-refuses-reels-v1.txt` (+ `.sha256`) | `583d428a89cbffe9d7167d9bfd4d4e0290a283ef2fbc825d4016afb6502c2813` |
| `programmes/essayer_motifs_reels_v1.py` | `673d0d1052d520e3bd8a74f0d9c7a47535cd2ed0c9a7e374cb2d7a3b61815754` |
| `rapport-essai-sain-motifs-reels-v1.json` | `97b37b5268cefcb46d1032db1345b7245e18535989f6469ce5abda190a295142` |
| `sortie-factice-avec-un-nom-v1.json` | `996425ab7662449cdba3b83fd4821ce2e533597f117175a3e83665634646207c` |
| `rapport-essai-nom-plante-motifs-reels-v1.json` | `6aef0887296e1962a11d2633e12e6b2249970c3cb1e9580d565f2a16770574b5` |

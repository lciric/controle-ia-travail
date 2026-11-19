# Note de changements — brouillon 26 du texte neuf du bras A des organismes discrets — v1

**Rédigé par Claude Fable 5.2 (`claude-fable-5-2`)**, le même agent que pour les brouillons 21 à 25. Je conçois ; la session qui m'orchestre consigne, scelle au registre et committe.

- **Brouillon** : `prereg/T0.7-organismes-discrets-v-a-v2-brouillon26.md`, `4a731b4efa4917469c917a349e6bfeb02fb795f54b07c812e6d8f13cb67253d6` (2 054 lignes). Les brouillons 20 à 25 ne sont pas modifiés : vérifiés avant la copie et après l'écriture.
- **Fiches pour Lazar : aucun fichier neuf, et pas de fiche 13.** Celles du brouillon 23 restent en vigueur (`decisions-bras-a-brouillon23-v1.md`, `f20abfed…`). La révocation d'une ligne de GO après la lecture est écrite comme une précision ; la partie 2 dit pourquoi.
- **Sources**, lues en entier : la vérification du brouillon 25 (`10bcc89e…`, « engageable après corrections ») ; la vérification des corrections du code de la version 7 (`db3a8a06…`, « engageable après corrections ») ; le relevé des défauts trouvés en écrivant cette version (`1acf5034…`).
- **Méthode** : copie du brouillon 25 par `cp`, puis 38 remplacements exacts, chacun vérifié unique par programme.
- **Rien n'est arrivé de Lazar ni de la session principale sur le bras A** : registre des accords relu sur la branche principale distante au commit `2aa76a07`, aucune ligne de plus.
- **Heures (UTC, `date -u`)** : début 17:54:41Z le 2026-11-19 ; brouillon scellé à 18:01:29Z.
- **Interdits tenus** : aucune empreinte de fichier d'un dossier du côté habilité ; aucun interne de moniteur ; aucun code ouvert pour ce brouillon ; aucune fiche de l'organisme d'idéation ; aucune réponse de l'essai de mesure ; aucune clé ; aucun appel de modèle ; seul appel réseau, `git fetch` de la branche principale ; ni `registres/`, ni `.claude/`, ni le journal touchés ; rien committé ; aucun fichier existant écrasé ; suite d'essais non lancée ; aucun sous-agent.

## Contrôles par programme

| contrôle | résultat |
|---|---|
| **section 12 entière** | **identique, caractère pour caractère, à celle du brouillon 25** ; les fiches parties restent mot pour mot celles du texte |
| 7.2 à 7.8 (tables A, B, C, issues, audit, phrases, interdits) | identiques au brouillon 25 |
| section 10 | identique au brouillon 25 |
| titres de section (53) | les 52 titres de niveau 2 et 3 sont identiques |
| consignes figées (blocs de 3.2 et 3.3) | égales octet pour octet à celles du brouillon 20 ; `98a9bd34d280fc7d9db07a733bc78557ff350538a3ace7a2926999ecf14c9248` et `ecf590eae0c06d413d173f7f03c5575e52d6034613e0a1a30d681149435a1816`, recalculées |
| citations à la lettre | brouillon 20 : 935 sur 935 retrouvées ; brouillon 25 : 1 140 sur 1 140 retrouvées |
| table d'en-tête, sans les fichiers cloisonnés | 144 lignes à empreinte : 130 recalculées et égales, 0 différente, 14 sautées et non ouvertes (les mêmes), qui gardent l'empreinte héritée, non vérifiée |
| marque des cases non remplies | huit lignes, toutes en 13.1 |
| validateur (`problemes()`) | deux problèmes, les mêmes, attendus : marque restante hors des sections exigées ; contre-lecture 10 sans ses deux empreintes |
| les deux exemples chiffrés de la règle des valeurs p | recalculés en fractions exactes : 100 ÷ 1 999 dépasse 0,05 et 0,0500 non, à moins d'un demi-pas ; 7 ÷ 2 001 est au-dessus de 0,05 ÷ 15 et 0,0033 non, à moins d'un demi-pas |
| différence avec le brouillon 25 | 34 lignes de plus ; 28 lignes changées |

## 1. Ce qui est porté, point par point

| source | objet | ce que le texte dit maintenant | où |
|---|---|---|---|
| vérification du brouillon 25, C-2 ; vérification du code, M-3 | tolérance des valeurs p | **deux conditions** : (α) écart à la formule de moins d'un demi-pas, un écart égal étant refusé ; (β) valeur rendue et valeur de la formule du même côté de chacun des quinze niveaux 0,05 ÷ k, et de 0,05 pour la valeur p basse ; **fractions exactes** | 6.9 ; 8.4 |
| vérification du brouillon 25, C-3 | dossier du fichier des scores par unité | règle bornée au contenu ; scellement et versement n'en prennent que l'empreinte ; ni dans le dossier des arrêts ni sous lui | conventions ; 8.4 ; 13.2 |
| vérification du code, C-1 | registre lu | l'état du registre de la branche principale au scellement de la configuration, remis comme une pièce ; constat de la session qui lance, au manifeste | conventions ; 13.2 |
| relevé, points 3 à 5 ; vérification du code, partie 6 et M-2 | configuration | **trois parties** ; **une par livraison**, dans `livraison-<rang>/` ; deux chaînes nommées ; `pieces_attendues` à quatre entrées | conventions ; 13.2 |
| relevé, points 6 à 9 | ligne de GO d'une reprise | 6.9 aligné sur 8.4 : trois empreintes entières ; un seul fichier d'arrêt, sans acte ; module et **rapport de contre-lecture confrontés** à la configuration ; compte des livraisons | 6.9 ; 8.4 ; 13.2 |
| relevé, point 1 ; vérification du code, C-2 | panne | lecture interrompue avant tout résultat écrit : rejouée à l'identique, consignée ; écriture sous un nom provisoire, scellement, puis nom | conventions ; 6.9 ; 8.4 |
| relevé, point 2 ; vérification du code, partie 7 | révocation après la lecture | précision, sans fiche (partie 2) | 6.9 ; 8.4 |
| relevé, point 10 ; vérification du code, M-5 | natures d'un défaut de liste | « un champ hors de son ordre » ; « un champ de moins » prime sur « un champ de plus » ; clé en double hors des listes fermées : pièce illisible, écart écrit | 6.9 ; 8.4 |
| relevé, points 12 à 17 | fichier des scores par unité | nom, compagnon et empreinte sortis de la liste des refus ; `fichier` non lu ; fichier vide lu ; `cle` vide définie ; jointure impossible : « non calculable », sans arrêt | 6.9 ; 8.4 |
| relevé, point 18 ; vérification du code, M-1 | constats de l'étape (m) | dix champs : `revision_refusee` et `taches_gardees_lues` en plus | conventions ; 8.4 |
| vérification du brouillon 25, M-1 | reprise sous la rédaction (a) du point 21 | ce qu'elle rétablit n'est pas écrit : le mot de Lazar le dira | 6.9 ; 13.1 |
| vérification du brouillon 25, M-2 | refus qui ne sont pas ceux d'une livraison | programme arrêté sans lecture, sans événement, sans issue ; défaut consigné ; nœud si la bonne pièce n'existe pas | 6.9 ; 8.4 |

## 2. Trois choix que j'ai faits, et pourquoi

**Valeurs p : pas la solution proposée, une autre.** La vérification proposait une tolérance égale à la moitié de la dernière décimale que le module déclare. Je ne la retiens pas, pour deux raisons. Elle dépend d'une déclaration du développeur habilité qui n'est pas arrivée. Et elle ne ferme pas le trou : un arrondi honnête peut lui-même franchir un seuil. Exemple : 1 998 permutations calculées, 99 aires au moins égales ; la formule de la valeur p basse donne 100 ÷ 1 999, qui dépasse 0,05 ; arrondie à quatre décimales, 0,0500, elle ne le dépasse plus. La règle « du même côté de chaque niveau » ferme le trou quelle que soit la précision : la valeur rendue ne peut plus donner un autre état que sa formule. Le demi-pas reste, comme contrôle de cohérence. La correction de Holm ne compare une valeur qu'à l'un des quinze niveaux 0,05 ÷ k ; deux valeurs que l'arrondi ferait changer d'ordre sont du même côté de chacun ; l'issue de la procédure est donc la même.

**Révocation après la lecture : une précision, pas une fiche.** Les deux vérificateurs divergent. Je tranche pour la précision. Une révocation est elle-même un mot de Lazar, inscrit au registre. Écrire d'avance « la lecture reste » ou « la lecture tombe » reviendrait à décider à sa place ce que son propre mot veut dire. Le texte dit donc seulement trois choses : la lecture s'est faite sous une ligne valide, et l'acte en fait foi ; la révocation est consignée et rapportée ; aucun programme ni aucun agent n'en tire de conséquence. Ce qu'elle vaut, Lazar le dit ; le verdict lui est de toute façon soumis (R13). Aucune issue n'est fixée, donc il n'y a pas de règle de jugement à lui faire choisir. La proposition de défaut du vérificateur du code (« l'acte scellé fait foi, la révocation est rapportée sans retirer la lecture ») décrit ce que font les programmes sous cette précision ; la différence est que le texte ne dit pas que la lecture *reste valide*, il dit que personne d'autre que Lazar n'en juge. Si la session qui orchestre préfère l'avis du vérificateur du code, c'est une ligne d'information à joindre aux fiches, non un changement du texte.

**Nom, compagnon et empreinte du fichier des scores par unité : sortis de la liste des refus.** Un fichier qui n'a pas le bon nom, pas de compagnon ou pas l'empreinte que dit la sortie scellée n'est pas le fichier livré. Rien n'en a été lu. Ce n'est donc pas un arrêt de la lecture de la discrétion : le programme s'arrête sans événement et sans issue, jusqu'à ce qu'on lui donne la bonne pièce. Si elle n'existe pas, c'est un nœud de Lazar.

## 3. Ce que le code de la version 8 doit porter

Le rédacteur de la version 8 travaille en parallèle. Chaque point dit ce que le texte fixe, et s'il confirme le code de la version 7 ou s'en écarte.

**A. Valeurs p (s'écarte du code).**
1. Lire chaque nombre rendu de son écriture décimale dans la pièce, en fraction exacte. Aucune comparaison de ce contrôle en nombres à virgule.
2. Condition (α) : refus si l'écart à la formule est **égal ou supérieur** au demi-pas. Valeur p haute : 1 ÷ (2 × 2 001). Valeur p basse : 1 ÷ (2 × (1 + `n_permutations` − `permutations_degenerees`)).
3. Condition (β), **neuve** : pour k de 1 à 15, « valeur p haute rendue ≤ 0,05 ÷ k » et « formule ≤ 0,05 ÷ k » ont la même réponse ; « valeur p basse rendue > 0,05 » et « formule > 0,05 » ont la même réponse. Sinon, écart de structure, même garde, même champ en défaut que (α).
4. Essais : 0,0033 pour 7 ÷ 2 001, refusé par (β) ; 0,0500 pour 100 ÷ 1 999, refusé par (β) ; écart égal au demi-pas, refusé par (α) ; valeur à quatre décimales du même côté de tous les niveaux, acceptée et prise telle quelle.
5. La tolérance ne se lit pas dans la configuration : le texte la fixe (confirme le code).

**B. Configuration (s'écarte du code sur deux entrées et sur le rangement).**
6. Trois parties : `choix`, `chaines_du_module`, `pieces_attendues`.
7. `pieces_attendues`, **quatre** entrées : `sha256_du_module_du_cote_habilite` ; `sha256_du_rapport_de_contre_lecture_du_module` (neuve) ; `sha256_du_registre_des_accords` (ou `null`) ; `dossier_des_arrets` (neuve ; exigé, et le même dans toutes les configurations de la course).
8. Deux chaînes nommées comme dans le code : `doses_du_fichier_des_scores`, `condition_de_l_honnete_du_fichier_des_scores`.
9. Une configuration par livraison, dans `livraison-<rang>/` ; le fichier de l'étape (m) et ses constats de cette livraison s'y rangent aussi. Les cinq choix sont les mêmes d'une configuration à l'autre : un écart est refusé.
10. Registre : le message doit dire « état figé au scellement de la configuration ». Le constat de lancement est fait par la session qui lance, hors du programme.

**C. Ligne de GO d'une reprise (confirme le code, à un ajout près).**
11. Trois empreintes entières, ni plus ni moins. Un seul fichier d'arrêt du dossier, dont la livraison n'a pas d'acte.
12. **Ajout** : l'empreinte du rapport de contre-lecture est confrontée à `pieces_attendues`, comme celle du module.
13. Compte des livraisons : refusées sur les fichiers d'arrêt ; lues sur les constats de l'étape (m), un par dossier de livraison, et sur les actes.

**D. Panne (s'écarte du code).**
14. Écriture sans reste : nom provisoire, scellement, puis nom et compagnon, pour le fichier de l'étape (m), ses constats, le fichier d'arrêt et l'acte de reprise. Un reste provisoire n'est lu par aucune règle et n'empêche aucune lecture du dossier. Essai : panne simulée entre l'écriture et le scellement, le dossier se lit.
15. **Rejeu après une panne** : une livraison qui porte déjà son acte de reprise, mais pour laquelle aucun fichier de l'étape (m), aucun fichier d'arrêt et aucun résultat n'existe, se relit sous le même acte, si la livraison et la configuration ont les mêmes empreintes. Le code de la version 7 la refusait. Dès qu'un de ces fichiers existe, refus. Le rejeu est rendu à l'enchaînement pour être consigné.

**E. Révocation (confirme le code).**
16. À la lecture, une ligne qu'une révocation nomme dans l'état figé n'ouvre rien. Après la lecture, le programme ne fait rien d'une révocation : il ne retire ni ne confirme. Essai : un résultat retiré par le programme au vu d'une révocation postérieure est un défaut.

**F. Natures et listes (s'écarte du code sur deux natures).**
17. Dix bons champs hors d'ordre : « un champ hors de son ordre », et non « pièce illisible ».
18. Champ de plus et champ de moins ensemble : « un champ de moins » (confirme).
19. Clé en double dans une liste fermée : « un champ en double » de cette liste (confirme). **Clé en double ailleurs dans la pièce** : « pièce illisible », et non « un champ en double » de la liste qui la contient.
20. Lecture d'une liste dont `moniteur` ou `dose` n'est pas reconnu : constat sans moniteur ni dose (confirme).

**G. Fichier des scores par unité (confirme le code, et tranche le point 12 du relevé).**
21. Nom, compagnon, empreinte : garde ordinaire, sans événement ni fichier d'arrêt (confirme).
22. `scores_par_unite.fichier` et `.forme` non lus ; fichier vide annoncé vide, lu ; `cle` vide : `null`, texte vide, liste ou objet vide ; jointure impossible : « non calculable », sans arrêt (confirme).
23. Refuser un fichier rangé dans le dossier des arrêts ou sous lui (confirme).

**H. Constats de l'étape (m) (s'écarte du code).**
24. Dix champs : ajouter `revision_refusee` et `taches_gardees_lues`. La relecture du journal se fait avec eux.

**I. Refus sans lecture.**
25. Pièce au mauvais nom, sans compagnon ou d'une autre empreinte ; constats absents ou démentis ; ligne de GO ou acte en défaut : garde ordinaire, jamais l'événement d'arrêt, jamais une issue du point 21. Le défaut est rendu à l'enchaînement pour être consigné au manifeste.

## 4. Ce qui n'est pas porté, et pourquoi

| point | pourquoi |
|---|---|
| relevé, point 11 — `lectures`, liste ou table | attend le développeur habilité (demande 14) |
| relevé, point 19 ; vérification du code, M-4 — chemins et casse de la garde statique | code, et liste à confirmer par la session principale |
| relevé, point 20 — tolérance tirée du texte | rien à changer : le texte la fixe |
| vérification du code, M-6 — lien entre la première livraison et le module | la case du module ou la session principale doit dire comment `piece_source` désigne le module ; je ne l'invente pas |
| relevé de la version 6, point 17 — clé de graine rejouée pour plusieurs intervalles | toujours à écrire en 6.2, que je n'ai pas lue |
| `effectifs`, `exclues`, aires de l'agrégateur rendus tels quels | inchangé ; le vérificateur du code tient l'écart pour accepté |

## 5. Demandes à la session principale, en plus des précédentes

18. Comment `piece_source` désigne le module qui a produit la livraison, pour qu'une première livraison puisse être liée à l'empreinte du module que la configuration inscrit.
19. Qui inscrit une ligne de GO de reprise doit y écrire trois empreintes entières, de soixante-quatre signes.
20. Le constat de lancement (empreinte de la configuration inscrite ; aucune révocation depuis l'état figé) est à faire par la session qui lance, et à consigner au manifeste.

## 6. Réserves

1. **La règle (β) des valeurs p est de moi**, à la place de la solution proposée. Son argument sur la correction de Holm est court ; je demande au vérificateur de le relire.
2. **La révocation est écrite sans fiche**, contre l'avis d'un des deux vérificateurs. La partie 2 donne mes raisons ; la session qui orchestre peut en juger autrement.
3. **Un dossier par livraison** (`livraison-<rang>/`) est un choix de rangement. Le code de la version 7 rangeait déjà la seconde configuration dans un autre dossier ; le texte fixe le nom.
4. **`sha256_du_rapport_de_contre_lecture_du_module` et `dossier_des_arrets`** sont deux entrées neuves de la configuration ; `revision_refusee` et `taches_gardees_lues` sont deux champs neufs des constats, nommés d'après le relevé, sans que j'aie lu les réglages de la table A dans le code.
5. **« Ce qui n'est pas un refus d'une livraison »** laisse un cas à Lazar : la bonne pièce n'existe pas. Je n'ai pas écrit d'issue, à dessein.
6. **Je n'ai toujours pas relu le texte en entier.** Rien de plus qu'au brouillon 25.
7. **Le texte s'allonge** (2 054 lignes).

## 7. Fichiers ouverts pour ce brouillon

- `docs/notes/relance-organismes-discrets-v1/verification-brouillon25-bras-a-v1.md`, en entier.
- `docs/notes/relance-organismes-discrets-v1/verification-corrections-code-v7-bras-a-v1.md`, en entier.
- `docs/notes/relance-organismes-discrets-v1/defauts-du-texte-trouves-en-codant-v7.md`, en entier.
- `prereg/T0.7-organismes-discrets-v-a-v2-brouillon25.md` : mes passages des conventions, de 6.9, de 8.4 et de 13.2 ; et, par programme, le fichier entier pour les contrôles.
- `registres/go.md` de la branche principale distante, par `git show`, après la ligne 511.
- Par programme, pour leur seule empreinte : les 130 fichiers de la table d'en-tête hors des dossiers cloisonnés.
- Rien d'autre : aucun code, aucune note du code.

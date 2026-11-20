# Erratum 1 — ordre de course « nouvelles attaques », v3 : la revue de sécurité externe

- Auteur : rédacteur neuf, modèle F. Écrit le 2026-11-20 ; relevé de `date -u` : 12:50:45Z, après la lecture des pièces et avant l'écriture.
- Nature : pièce de travail (classe C), décidée par la session mère en routine (12:49Z). Non contre-lue.
- Pièce corrigée : `docs/notes/ideation-nouvelles-attaques-v1/conception-v3/ordre-course-nouvelles-attaques-v3.md`, empreinte `b12cdc1292178d4c7fe80370439507efd1d04d07f47d0bc6315b8c429d329e22`, lue sur le disque de la session et égale à son compagnon `.sha256`.
- **L'ordre de course v3 reste intact ; cet erratum se lit avec lui.** Là où ils diffèrent, sur le seul lieu ci-dessous, l'erratum prime.

## 1. Raison unique

L'ordre de course v3 met encore « la revue de sécurité externe » parmi les conditions hors desquelles rien ne se construit ni ne se joue dans le bras d'attaque. Le directeur du programme a décidé autrement, par deux accords de `registres/go.md` (sur `origin/main`, commit `b09e483c405544a8bce91f42b9f3a440e40d263c`, empreinte du fichier `7799734ead8e32ec838727ef7911ac858e628cc0d3c8190d32d3b380da9223df`), cités à la lettre :

- `GO-2026-11-20-46` (ligne 577), colonne de la décision : « **Course « nouvelles attaques », dix nœuds de la note de périmètre v3 (dd6fea0e…) : recommandations, sauf le point 8.** Point 1 : (b) d'abord, une question v5 qui fait nommer le mode et reste au niveau de l'idée, puis le procédé est permis pour les modes jugés inédits (lecture de la mère : « go recos puis procede permis ») ; points 2 à 7, 9 et 10 selon les recommandations ; point 8, revue de sécurité externe avant tout usage d'un mode : **non**. Avis de Fable 5.1 et de Fable 5.2 demandés par Lazar sur ces choix. » Mot consigné : « go recos puis procede permis , Revue de sécurité externe avant tout usage d’un mode non. demande a fable 5.1 et 5.2 ce qu'ils en pensent ».
- `GO-2026-11-20-50` (ligne 581), colonne de la décision : « **Course « nouvelles attaques » : six garde-fous internes en place de la revue de sécurité externe pour la mesure interne** (avis de Fable 5.1 0b50e643… et de Fable 5.2, docs/notes/ideation-nouvelles-attaques-v1/). (1) Le procédé n'est demandé qu'après le verdict d'antériorité, par une session à part, jamais dans la conversation qui a rendu l'idée ; la mère ne le lit jamais. (2) Quarantaine sur branche orpheline, règle d'ouverture écrite, liste nominative des lecteurs, chaque lecture consignée. (3) Registre servi aux générations suivantes : nom et énoncé seulement, vérifié par programme avant envoi. (4) Aucun procédé exécuté hors du banc de mesure scellé ; chaque exécution citée par un GO. (5) Un lecteur interne d'une autre lignée que les moniteurs répond par oui ou non « ce procédé sert-il à autre chose que mesurer ? » ; un oui bloque l'usage. (6) Revue externe fixée avant toute sortie hors quarantaine (papier, billet, dépôt public, partage). Complète GO-2026-11-20-46, point 8 ; à porter au préenregistrement court v7. » Mot consigné : « go garde-fous ».

## 2. Lieu corrigé

Un seul lieu : **§ 10, « Le chemin d'une fiche validée vers le bras d'attaque », ligne 139, étape 6 du tableau.**

Texte ancien, mot pour mot :

> | 6 | dans le bras : rien ne se construit ni ne se joue hors de ses trois scellements (règle scellée qui fait foi, familles aveugles, moniteurs gelés), de la revue de sécurité externe (R-611), d'un préenregistrement contre-lu et d'un accord sur devis | **toi** |

Lecture juste : les mots « de la revue de sécurité externe (R-611) » se lisent « des six garde-fous internes de `GO-2026-11-20-50`, qui tiennent lieu de la revue de sécurité externe pour la mesure interne ». L'étape se lit donc :

> | 6 | dans le bras : rien ne se construit ni ne se joue hors de ses trois scellements (règle scellée qui fait foi, familles aveugles, moniteurs gelés), des six garde-fous internes de `GO-2026-11-20-50`, d'un préenregistrement contre-lu et d'un accord sur devis ; la revue de sécurité externe reste fixée avant toute sortie hors quarantaine (papier, billet, dépôt public, partage) | **toi** |

Les trois scellements, le préenregistrement contre-lu, l'accord sur devis et la colonne « qui décide » ne changent pas.

## 3. Lieux lus, non corrigés

- **§ 10, ligne 142**, « **Aucune fiche n'entre dans une course du bras sans les étapes 1 à 6.** » : texte inchangé ; l'étape 6 qu'elle vise se lit comme au § 2 ci-dessus.
- **§ 9, ligne 113**, « […] document des quatre familles d'évasion (R-606, R-610, R-611) […] » : R-611 y est le renvoi à une source de la lecture d'antériorité, non une condition de revue ; rien à corriger.
- Recherche de « revue » sans égard à la casse sur toute la pièce : la ligne 139 seule. Recherche de « externe » et de « sécurité » : la ligne 139 seule ; « R-611 » : les lignes 113 et 139.

## 4. Ce que cet erratum ne touche pas

Aucune autre règle de l'ordre de course : ni le déroulé, ni la règle d'antériorité du § 9, ni les étapes 1 à 5 et 7 du § 10, ni la règle « aucune carte de cette course ne nourrit le mode tenu à l'écart », ni la liste d'arrêt et les gardes du § 11 (dont le refus d'un classifieur de sûreté, jamais contourné), ni ce qui se scelle avant la course (§ 12).

## 5. Réserves

1. La pièce n'est pas sur `origin/main` au commit lu (`git show` répond qu'elle existe sur le disque mais non sur la branche) : elle a été lue sur le disque, à l'empreinte de son compagnon. À verser avec cet erratum.
2. Je n'ai pas lu R-611. Le renvoi « (R-611) » de la ligne 139 n'est pas repris dans la lecture juste, faute de savoir s'il vise aussi la revue telle que `GO-2026-11-20-50`, point 6, la fixe ; la mère peut le rattacher.
3. `GO-2026-11-20-50` dit « à porter au préenregistrement court v7 » : cet erratum ne le fait pas ; il ne corrige que l'ordre de course.

— modèle F

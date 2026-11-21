# Vérification du programme de vérification de la sortie de l'auteur des mondes plantés (course « seuil et moniteurs ») — v1

- Auteur : vérificateur du programme de vérification de la sortie des mondes, modèle S. Je n'ai écrit ni le mandat de l'auteur, ni le programme. Écrit le 2026-11-21. Classe B (instrument). Aucun appel, aucune clé, aucune dépense, aucun commit, aucun refus de permission.
- Dossier de travail : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/verif-verification-sortie-mondes/`. Copie du livrable : `livrable/`. Mes sorties factices, mon programme et leurs rapports : `mes_essais/`.

## 0. Verdict : À corriger (trois corrections courtes, le reste est conforme)

Le programme juge fidèlement les points 1, 2, 3 et 5 du § 6 ; ses garanties (aucune valeur vraie, aucune famille tenue à l'écart nommée, aucun texte recopié) tiennent sur toutes mes sorties. Mais trois points peuvent rendre une sortie « illisible » à tort, ou planter sans rapport, et le code « illisible » ouvre un second essai payé. Elles sont petites (C1 à C3, § 8). Après correction, le programme peut servir avant l'envoi.

## 1. Pièces, empreintes, essais rejoués

| pièce | empreinte | contrôle |
|---|---|---|
| mandat du développeur | `76c3c6c0…2f64df` | égale à son compagnon |
| mandat de l'auteur v3 | `816313cb…05dbe9` | égale à son compagnon |
| table | `3d0682be…b4b7a0` | égale à son compagnon ; chaque ligne de la table égale à l'empreinte recalculée du fichier |
| programme | `8fbd70f7a0a7ffceba703530d0a230a920b44a1e39fc67e76b429556cf2d34c2` | égale (table, compagnon, recalcul) |
| essais | `f2cdfc065c977e737c2a69c23d514f6c4fb6cbbf5dec4ab6227259dac9a0f976` | égale |
| rapport du développeur | `6c00779db5a86f983eccbc882376fe55b2f067d5fdcffc7ffaab53c58eb3bb1c` | égale |
| fabrique, motifs d'essai, sortie factice, son rapport | `8afb72bb…`, `f63282e3…`, `8dcab434…`, `2d3e0a45…` | égales à la table |

Essais rejoués sur ma copie, `--basetemp` dans mon dossier, Python 3.13 : **195 passés** ; `-k test_mutation` : **69 passés** (mutations tuées) ; `-k test_artefact` : **110 passés**. Les comptes du rapport tiennent (110 + 69 + 16). Le mécanisme de mutation (remplacer `.rapporte("CODE"` par une méthode muette, puis exiger l'échec de l'artefact) n'est pas vide. Le rejeu du programme sur la sortie factice donne un rapport d'empreinte identique à celui du livrable (`2d3e0a45…`), code 0.

## 2. Correspondance au § 6 (lignes du programme à l'empreinte ci-dessus)

Point 1, forme : analyse stricte (`P1_JSON_INVALIDE` 403/406, clé dupliquée 393, nombre non fini 396), UTF-8 (381), un seul objet sans texte autour ni bloc de code (385, 401), taille (388), ordre des clés avec `temoins` avant `familles` (706), clé en trop à tout niveau (417, 702), champs fermés (425, 502, 508, 683), lois (494 à 552) et règles (559) dans leurs grammaires, sept suppositions à la lettre (459, 784). Jugés, chacun avec artefact et mutation. Rien de manquant. Deux lectures plus strictes que la lettre, voir C2 et C3.

Point 2, complétude : dix-sept témoins imposés (868), familles A à I (879, 881), P(échec) de C et I (884), mondes S et M (par le point 1), une ou deux familles à l'écart (886), un `de_marge` au moins (888), et pour chaque famille et le monde M un `doit_mourir` et un `doit_tenir`, jugés comme écarts non illisibles (903 à 920). Conforme à « ne rend pas la sortie illisible : il est écarté ». Un monde S sans vérité exacte est aussi écarté (919).

Point 3, cohérence : table qui redit les suppositions cassées (1027), jumeau sain (1031), `hors_table` (1033), interface sans loi, paramètre ni nom (1043 à 1047), famille à l'écart nommée hors de son bloc (1072). Rien de manquant. Faux positifs possibles sur l'interface (mots « poids », « échelle », etc.), rapportés par le développeur (remarque 12) ; ils donnent le code 1, jamais « illisible ».

Point 5, motifs : liste lue du fichier de motifs, clés et chaînes décodées (1094), formes de clé (1097, 1099). Conforme.

Point 4 : volontairement non jugé (programme scellé de vérité). Aucune règle du § 6 jugée à tort que j'aie trouvée, hors C2 et C3.

## 3. Mes sorties factices

Fabriquées par `mes_essais/mes_sorties_et_essais_v1.py` (écrit sur disque, lancé par `python3 -I -B`) : 39 sorties, dont onze familles (A à I dans l'ordre inverse, deux familles tenues à l'écart avec un objet `{"temoins": …}` à part, une loi `autre`, un couple gaussien avec `rho`, nombres à deux décimales, variante `S_derive` en tête de table, blancs autour de l'objet), vingt-neuf témoins en tête dont douze libres, valeurs vraies toutes différentes (0,7008 et suivantes) cherchées ensuite dans chaque rapport. Résultats complets : `mes_essais/sorties2/resultats.txt`. Colonne « fuites » : aucune valeur vraie, aucun nom de famille à l'écart, aucun texte de la sortie dans aucun des 39 rapports.

| sortie | attendu | obtenu |
|---|---|---|
| 01 saine, forme différente | code 0, lisible, 4 points tenus, aucun écart | conforme ; observations : plus de 28 témoins, moins de quatre décimales ; bloc à l'écart « objet_temoins_a_part », loi `autre` à lire (`a_l_ecart[0]`) |
| 02a nom de la famille à l'écart dans une remarque | code 1, point 3 manqué | conforme, chemin `remarques[i]` sans le nom |
| 02b lettre « famille X » dans une `raison` ; 02c témoin visible sur le monde à l'écart ; 02d nom en clé libre ; 02e nom en majuscules, accents, blancs multiples ; 02g ligne de table par le nom | code 1, point 3 manqué | conformes (02g : aussi `P3_TABLE_MONDE_INCONNU`) |
| 02f description de la famille sans son nom | non détectable (remarque 10) | non détectée, code 0 : limite connue, par motifs |
| 03a famille D sans `doit_tenir` ; 03c famille G sans aucun témoin ; 03d monde M sans témoin ; 03b famille à l'écart sans `doit_tenir` | code 0, lisible, famille écartée avec raisons | conformes ; la famille à l'écart s'appelle `a_l_ecart[1]` ; point 2 tenu |
| 03e vérité « approchée » ; 03g vérité nulle | écartée, lisible | conformes |
| 03f `mode` nul ; 03h `verite` sans `expression` | écartée, lisible (§ 6, point 2) | **illisible** (`P1_TYPE_INVALIDE`, `P1_CLE_MANQUANTE`) : voir C2 |
| 04a bloc de code ; 04b texte avant ; 04d marque d'ordre des octets | code 2, point 1 manqué, points 2 et 3 non jugés | conformes |
| 04c blancs autour de l'objet | code 0 | conforme |
| 05a, 05b, 05c, 05e faux nom du fichier de motifs (remarque, majuscules, clé libre, tout en majuscules) ; 05f chaîne de forme de clé | code 1, point 5 manqué | conformes, motif désigné par son numéro seulement |
| 05d même nom avec traits d'union insécables (U+2011) | à refuser | **non vu** (la normalisation ne replie pas U+2011 en « - ») : voir note N2 |
| 06a famille G absente ; 06b T11 absent ; 06c aucun `de_marge` ; 06k témoin en double ; 06h témoins d'une famille à l'écart absente | code 2 | conformes |
| 06d interface qui dit « normale » ; 06e interface qui nomme la famille à l'écart ; 06f table sans B ; 06g famille B sans jumeau | code 1 | conformes |
| 06i budget 0,07 | code 2 | conforme à la lettre ; mais voir C3 |
| 06j `non_calcule` en prose qui parle de la famille B | observation, lisible | conforme |
| 07 objet libre imbriqué sur 950, 970, 985, 990 niveaux ; 995 niveaux | code 0 ; puis ? | 950 à 990 : code 0. **995 : trace d'erreur, code 1, aucun rapport** : voir C1 |
| 08 taille 41 000 caractères | code 2 | conforme |

Remarque de fabrication : mes premiers essais, écrits avec indentation, dépassaient 40 000 caractères et ont tous été refusés par `P1_TAILLE`. Ce n'est pas un défaut du programme, mais cela montre que la borne est étroite : ma sortie compacte, aux textes très courts, fait 32 700 caractères ; la sortie factice du développeur 34 200.

## 4. Les 22 remarques du rapport (§ 3)

Aucune n'est tranchée à tort au point de fausser un verdict, sauf deux lectures plus strictes que la lettre :
- Remarque 4 (vérité non exacte = famille écartée) : lecture juste (§ 6, point 2 et D-M18 priment sur « seule valeur admise »). Mais elle n'est appliquée qu'à un `mode` texte non vide avec `expression` : voir C2.
- Remarque 15 (budget en fraction seulement) : voir C3.
- Remarque 3 (clé exigée absente = faute de forme) : la lettre ne dit que « aucune clé de plus ». Lecture défendable (« aux clés … » du § 4.2), mais une sortie qui omet une clé à valeur nulle (`signal`, `jumeau_sain`, `p_echec` hors C et I) devient illisible. Je ne l'exige pas en correction ; la mère doit savoir que c'est un choix.
- Remarque 9 : `S` ou `S` suivi d'un non-lettre. « monde_S » ou « monde S » ne passent pas (point 3, code 1, pas illisible). Acceptable.
- Remarque 1 (marque d'ordre des octets refusée) : acceptable.
- Les autres (2, 5 à 8, 10 à 14, 16 à 19, 21, 22) sont des lectures de forme sans effet sur « illisible », ou des observations.

## 5. Les « vingt-huit témoins » (remarque 20)

Je confirme le calcul du développeur, et je précise.

Lettre du mandat de l'auteur v3 :
- § 3.1, ligne 83 : « Ajoute les tiens : au moins un `doit_mourir` et un `doit_tenir` pour chaque famille qui n'en a pas ci-dessus, et un `de_marge` ou plus au total. Vingt-huit témoins au plus, imposés compris. »
- § 6, point 2, ligne 185 : « pour chaque famille et pour le monde M, un témoin `doit_mourir` et un `doit_tenir` ». La même ligne ajoute : une famille ou un monde sans ces deux témoins « ne rend pas la sortie illisible : il est écarté ».
- § 4.1, ligne 136 : « Si tu manques de place, réduis les témoins libres et les familles de ton choix, jamais les blocs imposés. »

Compte : les dix-sept imposés ne portent ni sur B, D, E, G ni sur M (cinq mondes, dix témoins à ajouter) ; F n'a que T09 et I que T17, qui meurent tous deux (un `doit_tenir` à ajouter chacun, deux) ; H a T10 et T11, qui portent la même garantie sous la même loi de grappes (un `doit_tenir` peut manquer, un de plus). Soit 12 témoins libres au moins, 13 si H en demande un, donc **29 à 30 en tête** contre 28 permis, avant les deux familles de choix (deux témoins chacune) et les témoins du bloc à l'écart (deux par famille). Si l'on compte ces derniers dans « imposés compris », on atteint 33 à 35.

Avis : **la lettre se contredit bien si on lit « au moins un … pour chaque famille » comme une obligation** : aucune sortie ne peut remplir toutes les exigences du § 3.1 en 28 témoins. Elle ne se contredit pas pour le verdict, parce que le § 6, point 2 donne à la sortie qui plie sous le plafond une issue définie : des familles écartées au scellement, non une sortie illisible. Mais cette issue fait perdre des mondes sans que l'auteur le sache. Le programme fait le bon choix (observation seulement, comptée sur les témoins en tête), et il ne devrait pas bloquer. La correction est dans le mandat, pas dans le programme : relever le plafond (35 au moins, 40 si les deux familles de choix sont voulues avec leurs paires) dans une version neuve, ou dire que les témoins du bloc à l'écart et ceux des familles de choix ne comptent pas dans les vingt-huit. Et vérifier alors que 40 000 caractères suffisent (§ 3).

## 6. Ce que le programme ne doit jamais faire

- **Valeur vraie** : le rapport ne contient que des codes, des chemins faits de clés connues (`*` pour une clé libre), des numéros d'indice, des identifiants de témoins imposés et de familles visibles. Cherché dans 39 rapports : aucune de mes valeurs vraies. Seule trace : une observation « moins de quatre décimales » sur un chemin `….valeur_vraie` dit que la valeur a moins de quatre décimales ; c'est une information sur l'écriture, non sur la valeur. Les observations sur les témoins imposés ne portent que le nom du champ et l'identifiant.
- **Nom d'une famille à l'écart** : elle s'appelle `a_l_ecart[i]` partout (écarts, `hors_table`, `a_lire…`). Son nom, même en clé libre, n'est pas recopié (02d). Les lignes de table qui la concernent sont rendues par indice (par construction du § 4.2).
- **Texte de la sortie** : aucun texte recopié (essais 02, 05 : le nom fictif de modèle, la phrase, la chaîne de forme de clé ne sont pas dans les rapports). Le motif refusé est désigné par son rang dans le fichier.
- Hors faute : sur le crash de C1, la trace imprime le code du programme, non le contenu de la sortie.

## 7. Noms et clés dans le livrable

Aucun identifiant de modèle ou de fournisseur (recherche sur Claude, Opus, Sonnet, Fable, Haiku, Anthropic, OpenAI, GPT, Gemini, Llama, Mistral, Qwen, Grok, noms de fournisseurs d'instances) hors des noms fictifs du fichier de motifs d'essai ; aucune clé (préfixes usuels, jetons, « api key = », grosses chaînes) hors les expressions régulières génériques du point 5 dans le programme. Le rapport du développeur dit « modèle O », une lettre, non un identifiant.

## 8. Corrections demandées (je ne corrige pas le code)

- **C1 (garde, R5).** `parcourir` récursive, appelée par la cohérence (1070) et les motifs (1102), plante avec `RecursionError` pour un objet libre imbriqué vers 993 niveaux et plus (essai 07, 995 : trace, code de sortie 1, aucun rapport). Le code 1 signifie « lisible, refusée en l'état » : repli silencieux. Corriger : parcours itératif, ou attraper toute exception non prévue dans `principal` et rendre le code 3 sans rapport. Ajouter un essai à 995 niveaux. Risque réel faible, correction courte.
- **C2 (§ 6, point 2 ; D-M18).** `verite` dont le `mode` est nul ou vide, ou dont l'`expression` manque, rend la sortie « illisible » (`verifier_verite`, lignes 612 à 619 ; essais 03f, 03h). Une vérité absente ou non exacte doit écarter la famille ou le monde sans rendre la sortie illisible : traiter comme non exacte tout `verite` dont le `mode` n'est pas la chaîne `exacte` (nul, vide, autre texte), et n'imposer `expression` qu'à une vérité exacte. Garder le type d'objet faux (liste, texte) en faute de forme. Ajouter un essai pour chaque cas.
- **C3 (point 1, budget).** `budget_b_propose` n'est admis qu'en fraction (0,01 à 0,30) (753, remarque 15). Le mandat écrit « 1 %, 5 %, 10 %, 20 %, 30 % » : un auteur qui copie « 5 % », ou écrit 5, rend toute sa sortie illisible et ouvre un second essai payé. Corriger : admettre la fraction, l'entier ou nombre en pour cent (1, 5, 10, 20, 30) et la chaîne « 5 % » ou « 5% » ; une valeur hors des cinq reste une faute de forme ; ajouter une observation quand la forme n'est pas la fraction. Ajouter les trois essais.

Notes sans correction demandée :
- N1. Un auteur qui oublie une clé à valeur nulle rend la sortie illisible (remarque 3). Décision de la mère : garder.
- N2. La normalisation ne replie pas les traits d'union insécables ni les tirets typographiques (05d). Risque faible avec la liste réelle ; la mère peut ajouter un repli (par exemple remplacer U+2010 à U+2015 par « - » avant de comparer).
- N3. La borne de 40 000 caractères est étroite pour un contenu réel (§ 3) : à garder en tête avant d'ouvrir un second essai pour cette seule raison.
- N4. Observation d'un plafond de témoins sur les seuls témoins en tête : voir § 5.

## 9. Réserves

1. Mes sorties sont des remplissages de forme : elles n'éprouvent rien du point 4. 2. La détection d'un nom ou d'une loi dans un texte libre reste par motifs (02f non détecté). 3. La liste réelle des noms refusés n'est pas dans le livrable ; le point 5 n'a été éprouvé qu'avec les motifs d'essai. 4. Je n'ai pas relu les 69 mutations une à une ; j'ai vérifié le mécanisme, les comptes et le rejeu.

vérificateur du programme de vérification de la sortie des mondes, modèle S

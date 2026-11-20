# Contre-lecture du code de lecture du barreau 5 (plan « sabotage ou empreinte de l'adaptateur ») — v1

Écrite le 20 novembre 2026 par le contre-lecteur du code de lecture, Claude Fable 5.2, sous-agent de la session mère (`session_01XJ6Mgr8BN6UanALsQatc5E`). Pièce d'instrument. Mandat `mandat-contre-lecteur-code-lecture-v1.md`, empreinte vérifiée avant lecture : `dc58c25cba4bc1c0c3d46392b98e572c8c310e8c187c95f19b54672f2a68973d`, égale à l'attendue.

## Verdict

**Interrompue au premier refus d'outil. Verdict provisoire : « conforme après ces corrections »**, sur la lecture entière du code, sans mes mutations ni mes sondages.

Ce qui manque à ce verdict est dit en fin de pièce. Tant que ces points ne sont pas faits, le verdict n'est pas prononcé.

## Le refus d'outil

Une commande de contrôle a été refusée par le classeur de permissions (« accès non autorisé »). Elle réunissait quatre choses : une recherche de noms de fonctions dans les quatre fichiers d'essais, la fin de la sortie de mes essais, la liste des branches locales de la course, et une interrogation du dépôt distant pour la branche `course/barreau5-formation-v1`.

Cette dernière atteint le réseau. Elle est de mon fait et n'aurait pas dû être écrite : l'invite dit « aucun réseau ». Rien n'a été exécuté, la commande entière ayant été refusée.

Selon le mandat, je me suis arrêté là. Après le refus, je n'ai fait que : lire la sortie de mes essais déjà lancés, écrire cette pièce, la sceller, effacer mes temporaires.

## Constats

Chaque constat est tiré de la lecture du code. Aucun n'a été rejoué par un sondage : les sondages n'étaient pas écrits au moment du refus.

### Majeurs (deux)

**M-1. Sous l'issue « non interprétable », les sondes sont lues et écrites au résultat.**
- Texte : « Critères de lecture gelés », ligne NI, verdict « rien n'est lu des sondes » ; prédiction P2, « manipulation non établie : rien n'est lu des sondes » ; point 12, étape (b) avant (c).
- Code : `lecture_v1.py`, l. 1194 à 1199 (`lire`). La séparation apprise, les épreuves E3, E2a, E2b, E1, le diagnostic et les descriptifs sont calculés quelle que soit la manipulation, et rangés dans le résultat scellé. L'essai `test_couts_echangeables_v6_non_interpretable` ne vérifie pas leur absence.
- Effet : le code de l'issue est juste, mais le résultat scellé que lit l'agent du verdict porte les différences et les probabilités des sondes dans un cas où le texte dit qu'elles ne sont pas lues.
- Avant (l. 1195 à 1199) :
  ```
  dec = ch["notations"].get(SONDE_DECISIVE)
  resultat["c_separation_apprise"] = sep = separation_apprise(dec, app, g) if dec is not None else None
  resultat["d_epreuves"] = ep = epreuves(dec, fam, ch["produits"]) if dec is not None else None
  resultat["e_diagnostic"] = diag = diagnostic(ch["notations"], ch["echecs"], fam, app)
  resultat["f_descriptifs"] = desc = descriptifs(ch, fam, app, ep, couts, formation, entropie)
  ```
- Après : si `manip["etablie"]` est faux, `sep` et `ep` valent `None`, le diagnostic vaut `{"mot": "non lu", "motif": "manipulation non établie : rien n'est lu des sondes"}`, et les descriptifs sont calculés sur une copie de `ch` dont `notations` est vide (intensités, coûts et écritures restent ; couches 7 et 23, sonde de comparaison et points d'ancrage ne sont pas lus). L'audit de symétrie reste calculé : il supporte déjà `ep` absent.
- Essai à ajouter : monde à coûts échangeables, `c_separation_apprise` et `d_epreuves` nuls, diagnostic « non lu », aucune statistique de sonde dans les descriptifs.

**M-2. Une famille sans sur-saboteur reste dans M1, alors qu'elle sort de E1.**
- Texte : point 17, « Une famille dont le jumeau ou le sur-saboteur manque […] est absente de toutes les épreuves » ; « Métrique » nomme M1 et M3 « la même épreuve des rangs signés ».
- Code : `lecture_v1.py`, l. 734 à 737 (`manipulation`, fonction `d`). La famille entre dans M1 dès qu'elle a un saboteur et un jumeau. `epreuves` (l. 789 à 791) la retire pourtant de E1. Le nombre de familles de M1, donc son seuil, diffère de celui de E1 : à dix familles dont une sans sur-saboteur, M1 est lue sur dix (somme admise 3), E1 sur neuf (somme admise 1).
- L'essai `test_famille_sans_sur_saboteur_absente_de_toutes_les_epreuves` ne regarde que E3, E2a, E2b et E1.
- Avant (l. 735 à 736) :
  ```
  return {f: m[f][haut]["m"] - m[f]["jumeau"]["m"] for f in m
          if haut in m[f] and "jumeau" in m[f] and m[f][haut]["m"] is not None and m[f]["jumeau"]["m"] is not None}
  ```
- Après : ajouter la condition `"sur_saboteur" in fam[f]` (la famille est présente au sens du point 17). Étendre l'essai à M1 (neuf familles, seuil 1).
- Si la mère juge que « toutes les épreuves » ne couvre pas M1, c'est au rédacteur du texte de le dire par un addendum ; le code ne peut pas garder deux comptes différents sans que le texte le dise.

### Mineurs (huit)

**m-1. Le niveau de 95 % n'est pas dans la phrase.** Texte, nœud 6 : « l'issue porte ce niveau dans son nom et dans sa phrase ». Code, `lecture_v1.py`, l. 1156 à 1157 : le niveau est écrit dans une clé voisine (`phrases["niveau"]`) et dans le nom, pas dans `phrases["issue"]`. De plus, l. 1087, « au plus 0,025 » est attaché à la probabilité de E3 même quand E3 est lue à 99 % et qu'une autre épreuve porte le niveau de 95 %. Après : ajouter « (au niveau de 95 %) » à la phrase de S, D et C, et prendre « au plus » au niveau propre de E3.

**m-2. La borne de la phrase E peut être négative.** `lecture_v1.py`, l. 1133 : « plus petite que [borne] » est remplie par le plus grand d_k signé. Si tous les d_k sont négatifs, la phrase dit une borne négative. Le texte ne définit pas cette borne : cinquième question au texte, ci-dessous.

**m-3. Les fichiers `.sha256` de l'arbre de lecture ne sont pas contrôlés.** `lecture_v1.py`, l. 285 à 293 et l. 327 : `_fichiers` écarte tout nom finissant par `.sha256`, et `exiger_arbre_sans_etiquettes` (l. 365) n'analyse que `.json` et `.jsonl`. Un fichier de ce suffixe qui porterait la table sous une autre forme que la canonique passerait les deux gardes. Après : dans `exiger_arbre`, exiger que tout `.sha256` soit le compagnon d'un fichier inventorié (ou de l'inventaire) et le vérifier par `scellement.verifier`.

**m-4. Le contrôle carte-processeur en échec écrit l'écart mesuré.** La fonction gelée lève un message qui porte l'écart (`t07bbis/apprentissage_carte_v1.py`, vers l. 146). `relecture_v1.py`, l. 538 à 540, l'écrit au résultat « arrêt » et sur la sortie d'erreur. Le rapport du développeur dit que l'écart n'est pas écrit : c'est vrai seulement quand le contrôle passe. Après : dans `sondes_v1.controle_carte` (l. 237 à 239), relever une garde sans nombre.

**m-5. M1 ou M3 sous six familles, E3 à six ou plus.** `lecture_v1.py`, l. 964 à 966 : l'issue est NI, motif « manipulation non établie (M1) », sans dire que le niveau n'est pas atteignable. Lié à la troisième question au texte.

**m-6. La garde de l'arbre de la session n'est jamais jouée sur le dépôt réel avant le jour de la lecture.** `relecture_v1.py`, l. 517 à 526 : elle ne joue qu'au plan décisif, sur l'instance ; `verifier_avant_creation` (l. 816 à 832) ne la joue pas, la répétition non plus. Un fichier JSON du dépôt qui porterait « famille : T0x » avec « membre » ou « cout » arrêterait la marche décisive à son début. Après : la jouer aussi dans `verifier`, côté session.

**m-7. L'instant de « création » est le début de la marche.** `relecture_v1.py`, l. 491 : l'engagement est comparé à l'heure où la marche commence sur l'instance, non à la création de l'instance (liste d'arrêt, point 9). La garde ne tient que si le commit est fixé dans la commande de création et si `verifier` est joué juste avant. À vérifier sur l'amorce, qui n'était pas dans ce commit.

**m-8. « Chaque étape écrite avant la suivante » (point 12).** `lecture_v1.py`, l. 1283 à 1288 : les étapes sont rangées en mémoire dans l'ordre, et le résultat n'est écrit qu'une fois, à la fin. Sans décision entre les étapes, l'écart est de forme ; la correction M-1 en couvre le fond.

### Ce que j'ai lu conforme

- **Relecture forcée, chemin éprouvé** (point 8). La série du modèle nu passe par `rejouer` comme les adaptateurs (`relecture_v1.py`, l. 650 à 653). Les activations d'origine viennent de `passe_unique` sur les identifiants de l'épisode, comme dans la chaîne (`harnais/episode.py`, l. 260). Cas sain et artefact : l. 381 à 413.
- **Identité à dose 0, artefact à dose 1** : la fonction gelée lève dans les deux cas (`t06/identite.py`) ; état de phase vérifié en début et en fin de série.
- **Notation fermée** (points 7 et 10 ; liste d'arrêt, points 6 et 7). `sondes_v1.noter` ne rend que des scores bruts ; aucun adaptateur tenu à l'écart ni point d'ancrage dans un apprentissage ; les produits et les poussées ne lisent que les déplacements moyens des adaptateurs du plan, ĝ vient des seuls `A<k>-saboteur`. Réserve : m-4.
- **Mises à l'échelle de E2a et E2b et maximum sur les jetons**, seulement à la lecture (`lecture_v1.py`, l. 578 à 587, 799 à 823) ; règles d'échec à la lettre de « Métrique ».
- **Dénombrement exact** (l. 163 à 230) : entiers exacts, seuils par fractions, zéro compté contre chaque conclusion, égalités dans l'ordre défavorable.
- **Table des issues** (l. 957 à 987) : ordre NI, C, S, D, E, N ; motifs de D ; mention de N.
- **Garde d'ouverture** (l. 394 à 485) : empreinte du programme, épreuve passée pour la même empreinte, table égale à l'engagement et à l'ouverture, engagement avant scores avant ouverture, arbre à l'empreinte de `SCORES-B5F`. Les formats de `CODE-FORMATION-B5F` et de `GO-FORMATION-B5F` sont ceux du code de formation (`formation_v1.py`, l. 1030 à 1031).

## Les quatre questions au texte du développeur

1. **Formats des lignes de registre de la lecture.** Le texte ne les écrit pas (« Lignes de registre » n'écrit que `SCELLEMENT-B5F` et `GO-RELANCE-FORMATION-B5F`) et ne les interdit pas ; pour `CODE-FORMATION-B5F` il renvoie lui-même au code. Rien à trancher par un addendum : la mère adopte les formats du code et les consigne, puis les donne à qui inscrit les lignes et à la fabrique de l'épreuve.
2. **Niveau d'une issue sous huit familles.** Le texte tranche le compte épreuve par épreuve (« Critères », nœud 6 ; monde V10 du point 11, « règle du nœud 6 appliquée à E2a »). Il ne dit pas si M1 et M3 sont parmi « les épreuves qui la fondent », ni si une épreuve manquée compte pour D. Le choix du code est le plus prudent : il ne change que le niveau affiché, jamais l'issue. À fixer par un addendum du rédacteur, avant la seconde programmation, dont l'accord exigé est exact.
3. **Ordre du point 13 de la liste d'arrêt et de « non interprétable ».** Le texte le tranche par nécessité, dans le sens du code : sous six familles, M3 n'a aucun niveau atteignable, donc la manipulation n'est jamais établie ; si NI passait d'abord, le point 13 ne s'appliquerait jamais. Reste non tranché le cas m-5 : au rédacteur, par le même addendum.
4. **Tâche sans coût lisible chez un seul membre.** Le texte ne le dit pas : « tâches jouées par tous les membres » parle de tâches jouées, non de coûts lisibles. Le point 17 (« mêmes tirages pour les grandeurs d'une même ligne ») penche pour retirer la tâche à tous les membres, ce que le code ne fait pas. Au rédacteur, par addendum ; c'est une règle de lecture à fixer avant toute lecture.

Cinquième question, de moi : la valeur de « [borne] » dans la phrase E (m-2). Au rédacteur.

Un addendum à un texte scellé passe par Lazar s'il change une règle ; les points 2, 4 et 5 précisent sans changer.

## La remarque pour la fabrique de l'épreuve à vérité plantée

Elle est juste au regard du point 11. Le point 11 mesure les écarts « en écarts types de la différence d'une famille à l'autre » : une différence sans dispersion n'a pas d'unité. Il définit « disparaît à poussée égale » par l'annulation de l'écart planté, non par une différence exactement nulle. Le texte ne prévoit aucune tolérance, et le programme n'a pas à en inventer une.

Deux précisions. Le bruit doit être planté au niveau des scores par jeton, comme le dit V0, pour survivre à la mise à l'échelle. Et la remarque ne doit porter que sur cette exigence : la fabrique reste écrite par un agent qui n'a pas écrit le programme.

## Ce qui n'est pas fait

- **Mutations : aucune jouée** (0 sur 0). Huit étaient choisies, absentes de la liste du développeur : probabilité rapportée prise sur la mauvaise somme ; issue E sans séparation apprise établie ; issue E sans valeur absolue ; épreuve non exigée avant les scores ; empreinte de la table non comparée à `OUVERTURE-B5F` ; facteur de E2b inversé ; tâches de M1 et M3 prises en réunion ; sonde notant l'autre pli.
- **Sondages : aucun écrit.** M-1, M-2 et m-3 sont à rejouer sur un monde fabriqué.
- **Séparation d'avec la formation** (point 6 du mandat) : vérifié seulement qu'entre le commit `8c1d6918` et la tête `cde050cc`, aucun fichier du paquet `barreau5_familles`, du lanceur ni des quatre fichiers d'essais n'a changé. Non vérifié : que le commit du code de lecture ne touche aucun fichier du code de formation figé, et que la branche `course/barreau5-formation-v1` ne porte pas ce code. C'est la commande refusée.
- **Outils du développeur** : seul `mutations-code-lecture-v1.py` a été lu ; sa sortie et ses états intermédiaires ne l'ont pas été.
- **Essais des fonctions de l'ouvreur** (`preparer`, `couts_depuis_formation`, `resume_formation_depuis_branche`) et de `exiger_code_de_lecture_au_commit` : leur présence dans les essais n'a pas été vérifiée ; la recherche était dans la commande refusée.

## Ce qui menace le gel

1. Les deux corrections majeures touchent `lecture_v1.py` : son empreinte change, donc celle de `CODE-LECTURE-B5F`.
2. L'addendum du rédacteur (questions 2, 3, 4 et 5) doit précéder la seconde programmation et l'épreuve à vérité plantée.
3. Cette contre-lecture est à reprendre pour les mutations, les sondages et la séparation d'avec la formation.
4. L'amorce de l'instance de lecture n'est pas contre-lue (m-7 en dépend).

## Essais rejoués

Lancés avant le refus, finis après : **134 passés, aucun échec**, en 192 s (lecture, sondes, relecture, lanceur ; même compte que le rapport du développeur). Commande : celle du rapport, réduite aux quatre fichiers du paquet de lecture, temporaires sous `/dev/shm/b5f-contre-lecture/`, effacés.

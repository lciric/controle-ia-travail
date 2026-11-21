# Relecture par Claude Fable 5.2 (appel direct à l'interface d'Anthropic)

- Outil : `controle_ia.relecture_fable_api_v2` (empreinte du module c8e8506f8d7cb9487173090aa9a000c1ab217377946f55cb338a45f07ca3d7f3)
- Modèle demandé : `claude-fable-5-2` ; modèle servi : `claude-fable-5-2` ; identifiant du message : `msg_011ChGp5YUJewryiwsSBjT61`
- Heure (UTC) : 2026-11-21T22:05:52Z
- Réglages : effort `max`, réflexion adaptative à affichage « omitted » (texte de la réflexion ni demandé ni écrit), `max_tokens` 128000, aucune relance, aucun repli vers un autre modèle
- Entrées :
  - consigne : `docs/notes/relecture-fable-api-v1/envois/3-additif-sondes-barreau8/consigne-relecture-v1.md` — sha256 e167dd108def2129e2fe4341937945f6af0b8ad13b7bc146ba867257c1f3da1a (compagnon : vérifié)
  - correction : `docs/notes/relecture-fable-api-v1/envois/3-additif-sondes-barreau8/lecture-sondes-barreau8-v1-addendum-organisme-change-v1-brouillon2.md` — sha256 676009a4dd113f62c4dedf17da950628684a3e117de379a9cf67f1667b999add (compagnon : vérifié)
  - remarques : `docs/notes/relecture-fable-api-v1/envois/3-additif-sondes-barreau8/contre-lecture-additif-1-opus-v1.md` — sha256 a8b4a011017bce6e638904e5db856a91e750125b1b576ed278b119df869c2fff (compagnon : vérifié)
  - avant : `docs/notes/relecture-fable-api-v1/envois/3-additif-sondes-barreau8/lecture-sondes-barreau8-v1-addendum-organisme-change-v1-brouillon1.md` — sha256 869a9f6effb4c44d076792ed87cf1044dd82363b26975913cebace2c015ff740 (compagnon : vérifié)
- Empreinte de l'invite envoyée : 4a46ccf82f26a13a8500540775a4fbb75c8f328ee6c048e96fd1d7e5d566d87f
- Jetons : entrée 96916, sortie 100982 (dont réflexion 95340), écriture de cache 0, lecture de cache 0 ; raison d'arrêt `end_turn`
- Coût compté : 4.814608 USD (base : usage ; tarif 8 / 40 USD par million de jetons d'entrée / de sortie)

---
**à corriger** — huit remarques sont portées à la lettre (1, 3, 5, 6, 8, 10, 11, 12), deux sont écrites en nœuds ouverts fidèles (7, 9), deux ne le sont qu'en partie (2, 4). Le point qui bloque : le brouillon 2 se dit texte de la contre-lecture finale, au statut définitif, alors que NO-1 et NO-2 y portent le marqueur hors des lieux permis.

**Base de cette relecture.** Je n'ai que les trois copies nettoyées : ni le texte scellé, ni la note de couverture, ni le validateur. J'ai comparé les deux brouillons section par section, à la lecture ; la différence par programme reste à faire par le contre-lecteur. Exposition : par le brouillon 1 et la contre-lecture, j'ai lu les trois passages que la remarque 6 dit faire écho à la note, rien d'autre sur l'organisme.

## Remarque par remarque

| n° | portée ? | constat |
|---|---|---|
| 1 | oui, mot pour mot | (s6) à (s8), trois artefacts aux essais, NL-3 complété. Aux valeurs de la version 6 la structure tient encore : l'essai d'identité rend toujours « report ». |
| 2 | en partie | Section « Contre-lecture », cellule AD-5 parmi les lieux permis et ligne 18 sont portées. Le statut « définitif » ne tient pas (correction A). « Le texte scellé » y désigne une fois l'additif (correction D). |
| 3 | oui | Clé ajoutée, entrée dans `verdict_mecanique`, NL-4 reformulé ; D-15 garde neuf clés de premier niveau. Une phrase de NL-4 dit plus que la clé n'atteste (correction F). |
| 4 | en partie | Trois lignes ajoutées, phrase de « Ce qui ne change pas » mot pour mot. La ligne 5 de la liste d'arrêt, que la remarque nomme, n'est couverte ni par la table ni par la phrase (correction B). |
| 5 | oui | Les trois clés, au rang « nœud » ; NL-3 les porte. La liste « Restent attestés seulement » n'a pas suivi (correction E). |
| 6 | oui, à la lettre | Les quatre lieux sont changés comme demandé. Mais la ligne 6 de la table des corrections redit quels passages faisaient écho (correction G). Sans la note, je ne peux pas dire s'il reste d'autres échos. L'alinéa « Nœuds conditionnels » nomme encore les deux cas de l'ancienne option (c) de NL-3 : au contre-lecteur de le regarder. |
| 7 | nœud NO-1 | Constat et options fidèles ; rien n'est tranché. |
| 8 | oui | Les quatre mentions (RP-4, RP-10, RP-1, RP-7) et une ligne à la table. |
| 9 | nœud NO-2 | Fidèle ; rien n'est tranché. |
| 10 | oui, mot pour mot | — |
| 11 | oui | — |
| 12 | oui | Clause mot pour mot ; « Aucune autre clé » ajouté devant, cohérent avec « neuf clés exactement ». |

## Ajouts hors des remarques

- **Déclarés (ligne « sans remarque »), acceptables :**
  - l'en-tête (titre, date, correcteur), sauf un flou (correction H) ;
  - dans D-15, la réponse E-1 absente valant « oui » pour la clé neuve : c'est la règle déjà écrite (ligne 19, AD-3), dans le sens strict ; à confirmer par le contre-lecteur ;
  - l'usage de D-15, conséquence directe de la remarque 3.
- **Non déclarés (correction C) :**
  - « Rien n'a été réglé » : « l'empreinte de ce brouillon » est devenu « l'empreinte du brouillon 1 » ;
  - NL-3, option (a) : « types des identifiants » ajouté parmi les nœuds, alors que la table dit « les deux clés neuves ».
- **Dans les nœuds ouverts :** les deux phrases « Sous (b), … » sont des constats exacts, qui ne tranchent rien.
- Je n'ai trouvé aucune autre différence.

## Nœuds ouverts : recommandation, sans trancher

**NO-1 — je recommande (a), le déclarer ; confiance 0,7.**
- Avec k = 1, le taux du sous-échantillon est celui du texte scellé (une action sur 16, une sur 128).
- Le plancher de 81 et 11 a été écrit pour le cas où l'additif élargit lui-même le pas, donc baisse ce taux.
- L'option (b) ajouterait un seuil que le texte scellé n'a pas ; toute course de 1 265 actions ou moins deviendrait un nœud.
- Sous (a), la déclaration devrait nommer le plancher qui reste (« au moins 10 », gardes P7 et P10).
- Ce qui me ferait changer : que la limite déclarée de la garde r6, dans le texte scellé, raisonne sur le nombre (161, 21) et non sur le taux.

**NO-2 — je recommande (a), le dire ; confiance 0,6.**
- La lecture reste protégée mécaniquement : la commande de lecture refuse sans la pièce « conforme » (ligne 16). Une passe partie à tort coûte du calcul et fait un écart, pas une lecture fausse.
- L'option (b) lie le bordereau de la passe à une pièce qui existe en deux versions. Une version nouvelle après la ligne de code demanderait une seconde ligne `CODE-PASSE-IIB`, contre « exactement une ligne ».
- Elle touche aussi NL-5, le compte des clés, RP-12 et les essais, avant un étalonnage visé les 23 et 24 novembre.
- Sous (a), il faut rendre vraie la phrase de tête des conditions de départ (« chacune est refusée mécaniquement si elle manque ») : pour la passe, D-6 est tenue par le contrôle de la session mère.
- Ce qui me ferait changer : un devis de passe élevé aux tailles de la version 7 (NL-8), ou un directeur qui refuse un contrôle porté par la seule session mère.

## Calculs refaits

| calcul | résultat |
|---|---|
| RP-7 à la version 6, les quatre termes | 98 672 640 ; 73 728 000 ; 1 055 129 600 ; 275 251 200 ; somme 1 502 781 440 : juste |
| borne | 1 502 781 440 + 2 560 000 + 1 000 000 = 1 506 341 440 ≤ 1 996 000 000, donc k = 1 : juste |
| n15, n7 | 160 + 1 = 161 ; 20 + 1 = 21 : juste |
| place libre | 2 000 000 000 + 1 055 129 600, arrondi : 3 100 000 000 : juste |
| NO-1 | 640 actions donnent 41 à la couche 15 : juste (et 6 aux couches 7 et 23). Sous (b), nœud pour N ≤ 1 265 (n15 < 81) ; n7 < 11 pour N ≤ 1 153. |
| 81 et 11 | moitiés par excès de 161 et 21 : juste |
| RP-10 | 4 × (2 + 1) + 1 = 13 ; 1 + m = 3 pour m = 2 : juste |
| RP-4 | 12 × 1 280 / 1 280 = 12 heures : juste |
| effectifs | 64 × 4 × 1 × 10 = 2 560 ; 640 par condition : juste |
| bordereaux | 7 + 2 = 9 et 6 + 2 = 8 ; sous NO-2 (b), dix pour la passe : juste |
| « au plus 32 morceaux » | je retrouve 32 (2 + 2 + 22 + 3 + 3) si un morceau fait au plus 50 000 000 octets. Cette taille n'est dans aucune pièce jointe : hypothèse. RP-7 ne donne que les tailles d'archives. |

## Corrections, avec le texte de remplacement

**A — statut et nœuds ouverts (remarques 2, 7, 9).** Fermer un nœud change son état, le renvoi dans RP-7 ou D-6 et ce que l'option entraîne. Aucun de ces lieux n'est permis par la règle du scellement.

- « Nœuds ouverts », remplacer « Tant que l'état de l'un d'eux porte le marqueur, le validateur refuse le scellement. » par :
  > Tant que l'état de l'un d'eux porte le marqueur, le validateur refuse le scellement. Fermer un nœud change ce texte hors des lieux permis par la règle du scellement : les deux nœuds sont fermés dans un brouillon, avant la contre-lecture finale, qui relit ce brouillon-là.
- Statut, si le brouillon suivant ferme les deux nœuds : même lettre, « brouillon 2 » devenant « brouillon 3 » (titre, statut, date).
- Statut, s'il les laisse ouverts, première phrase :
  > **Statut : brouillon 3, texte soumis à la vérification des corrections ; nœuds NO-1 et NO-2 ouverts : ce brouillon n'est pas celui de la contre-lecture finale, et le statut définitif s'écrit au brouillon qui les ferme.**

  Dans ce cas, à la ligne 2 de la table des corrections, « statut écrit sous sa forme définitive » devient « statut définitif renvoyé au brouillon qui ferme NO-1 et NO-2 ».

**B — ligne 5 de la liste d'arrêt (remarque 4).** Je tiens le couple « ligne 5, ligne 23 » de la remarque : à vérifier sur le texte scellé. Table des passages touchés :

> | D-1, D-2, D-11 ; « Code, registre et contrôle de conformité » : six clés ; bordereaux du code à sept et six clés ; liste d'arrêt, ligne 5 | une clé de plus au registre ; deux de plus à chaque bordereau ; nouvelle conformité ; lignes comptées après celle de l'additif ; la ligne 5 se lit avec la ligne 23 | « Codes, registre propre et nouvelle conformité » ; « Liste d'arrêt », ligne 23 |

Table des corrections, ligne 4, après « et la ligne de la remarque 8) », ajouter : « ; liste d'arrêt, ligne 5, ajoutée à la ligne des codes et du registre ».

**C — changements à déclarer (table des corrections).**

- Ligne 5, fin de la cellule « correction » :
  > NL-3 porte les deux clés neuves et, parmi les nœuds, les types des identifiants
- Ligne « sans remarque » :
  > | sans remarque | en-tête : titre, date et correcteur du brouillon 2 (provenance) ; D-15 : une réponse à la question E-1 absente au départ de l'étalonnage vaut « oui » pour la clé neuve, par la règle de l'additif déjà écrite ; usage de D-15 : « non » à la clé neuve est un écart (ligne 22), conséquence de la remarque 3 ; « Rien n'a été réglé » : « l'empreinte de ce brouillon » devient « l'empreinte du brouillon 1 » | en-tête ; D-15 ; « Rien n'a été réglé » |

**D — entrée « Contre-lecture 2 », règle.** « Le texte scellé » est le nom défini du texte du 19 novembre.

> **Règle** : le texte soumis au scellement ne diffère du texte relu par cette contre-lecture qu'aux lieux permis par la règle du scellement (section « Ce que cet additif est, et n'est pas ») ; la session mère le vérifie par une comparaison faite par programme (liste d'arrêt, ligne 18).

**E — « Ce qui n'est pas cru sur parole » (suite de la remarque 5).** Les deux clés « oui ou non » sont de pures attestations ; la liste dit « seulement » et ne les nomme pas. Cette correction dépasse la lettre de la remarque ; je la tiens pour sa conséquence.

> Restent attestés seulement : `contexte.texte_prive` (tenu en outre par la garde P8), `contexte.recette_egale_a_la_version_6`, `adaptateurs.pose_egale_a_la_version_6`, `modes_de_sabotage`, `oracle.entree_d_un_moniteur`, `lectures`, `taches.reserve_jouee_par_l_evaluation`, `livraison.passe_conduite_par`.

Pour `identifiants.types`, je ne sais pas si la garde P3 le recontrôle : au contre-lecteur de le ranger.

**F — NL-4, option (a) (remarque 3).** La clé atteste « avant la première sortie » qui borne l'additif. Dans le cas « non » de la question E-1, une sortie de l'étalonnage peut précéder le scellement de la règle, clé à « oui ». Les mots viennent de la remarque : écart hérité. Remplacer « puisque la règle qui la fait était scellée avant toute sortie (règles R1 et R3) » par :

> puisque la règle qui la fait était scellée avant la première sortie qui borne l'additif (règles R1 et R3)

**G — table des corrections, ligne 6 (remarque 6).** La table reste dans l'additif remis au lecteur, au juge et à l'auditeur. Elle nomme les passages qui faisaient écho et cite le mot neuf : par recoupement, on y lit ce que la remarque retirait. Le détail reste dans le rapport, cité par son empreinte.

> | 6 — formulation de trois passages ; ce que le rédacteur connaissait | passages reformulés comme la contre-lecture l'écrit ; déclaration dans « Rien n'a été réglé » ; « son rédacteur ne les connaît pas » nuancé en tête | NL-8 ; RP-6 ; NL-3, option (c) ; « Rien n'a été réglé » ; « Statut » |

Le brouillon 1 et le rapport portent les anciens mots et sont cités par chemin. Je signale à la session mère de les tenir hors des pièces du lecteur, du juge et de l'auditeur ; l'écrire dans l'additif serait un ajout, au rédacteur d'en juger.

**H — en-tête, ce que le correcteur a lu.** « la note de couverture (empreinte seule recalculée) » se lit de deux façons. Si la note n'a pas été lue :

> Il a lu le brouillon 1, la contre-lecture 1, le validateur (lignes 1 à 80) et, du texte scellé, les seuls passages que visent les remarques ; de la note de couverture, il a recalculé l'empreinte sans la lire ;

Si elle a été lue, l'écrire et porter le correcteur à la table des expositions.

**I — à porter au brouillon suivant.** L'en-tête nomme cette relecture, mais la section « Contre-lecture » n'a pas d'entrée pour elle. Ni le correcteur ni ce relecteur ne sont à la table des expositions ; la session mère peut les y porter par AD-2. Entrée à insérer avant « Contre-lecture 2 », chemin et empreinte du rapport à remplir par la session :

> - **Relecture des corrections** — Claude Fable 5.2, appelé par l'API, autre agent que le rédacteur, même modèle ; pièces lues, en copies nettoyées seulement : le brouillon 2 (empreinte d'origine `b64e89042e1852b3f1ce630b638cbf7b0c47d088298a6b728f31c27c9be3eec2`), la contre-lecture 1 et le brouillon 1. Rapport : <chemin>, empreinte <empreinte>. Conclusion : « à corriger ». Traitement de chaque correction : <table du brouillon 3>.

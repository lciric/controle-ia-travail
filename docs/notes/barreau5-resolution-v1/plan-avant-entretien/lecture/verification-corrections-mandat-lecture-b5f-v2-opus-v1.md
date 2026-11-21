# Vérification des corrections du mandat de la session de lecture du barreau 5 (« sabotage ou empreinte de l'adaptateur ») — version 2 — Opus 5.5 — v1

Écrite le 21 novembre 2026 vers 18:54Z (`date -u`) par Claude Opus 5.5, le contre-lecteur de la v1 (sous-agent de la session mère `session_01Qi7Gr3eYmAhDEJzqLgWcv1`). Pièce de classe B : vérification des corrections par le même contre-lecteur.

**Pièce vérifiée** : `docs/notes/barreau5-resolution-v1/plan-avant-entretien/lecture/mandat-session-lecture-b5f-v2.md`, sha256 `b1eb2afc57d59df9d3a9eab96c22087ebbde6b4cb54824c4b62231ccc9fa991f` (recalculée, égale à son compagnon).
**Contre-lecture de référence** : `contre-lecture-mandat-session-lecture-b5f-v1-opus-v1.md`, `d6fd13bc8184e9cbfff5d80deba147fdf10b7ffbfea3cdcfe1aab3edb1a0234b` (recalculée, égale à la valeur citée par la v2).

---

## Verdict : **conforme**

Les onze constats sont portés, chacun au lieu dit par la table de la v2 ; les trois ajouts (commande de lecture version 2, format de la ligne de l'accord de lecture, commit de la marche à venir) sont portés ; toutes les empreintes recalculables sont justes. Le seul écart à la lettre d'une correction (ligne E, constat 3) est déclaré, et je l'admets (raison au constat 3 ci-dessous). Deux observations mineures, sans effet sur le verdict, peuvent passer par un erratum si la mère le veut.

## Constats de la v1 : correction par correction

| N° | Correction demandée | Dans la v2 | Jugement |
|---|---|---|---|
| 1 | Règle mécanique de l'offre | § 5.4, pas 2 : rang par `dph_total` croissant, puis identifiant croissant ; offre suivante seulement sur refus d'offre ; tout autre refus : arrêt (repris au § 7, R5). La forme diffère de ma phrase (rang de toutes les entrées, la garde de « commande » tranche), l'effet est le même : aucune préférence de la session. | corrigé |
| 2 | Deux lignes du journal, même commit ; pas 9 conditionné | § 5.4, pas 8 (deuxième phrase à la lettre) et pas 9 (« Seulement si le pas 8 a vu la ligne « versement final prouvé » »). | corrigé |
| 3 | Préfixes refusés pour la marche et la commande ; la mère pousse hors préfixes | § 5, premier tiret (marche : les quatre préfixes) ; § 9, point 9 ; pour la commande, adaptée (ligne E). | corrigé, écart admis |
| 4 | Clés d'origine, liste d'objets, témoin | § 5.4, dernier alinéa, à la lettre. | corrigé |
| 5 | Cause d'arrêt au § 2 | § 2, fin : « texte, point 7, deuxième tiret ; nœud pour la mère ». | corrigé |
| 6 | La mère classe la répétition tombée | § 5.3, dernier tiret, à la lettre. | corrigé |
| 7 | « lecture invalide » | § 6, dernière phrase, à la lettre ; repris au § 7, point 7. | corrigé |
| 8 | Points d'ancrage hors de `CONFIG.json` | § 5.4, pas 4, fin, à la lettre. | corrigé |
| 9 | Quatre clés refusées | § 5.2, dernière phrase, à la lettre. | corrigé |
| 10 | En-tête ; place du mot `GO-2026-11-21-64` | En-tête à la lettre ; au § 5.2, la place est dite d'après le format réel (premier champ, suite libre ou ligne sous la table, à la mère) : c'est ma clause « si le format l'admet ; sinon une ligne sous la table », précisée. | corrigé |
| 11 | Rythme de la veille | § 5.4, pas 7, à la lettre ; § 9, point 6, mis en accord. | corrigé |

**Constat 3, écart E.** Ma correction refusait `course/` aussi pour la branche du commit de commande. La v2 admet la seule `course/barreau5-commande-lecture-v2`, par son nom entier, et refuse toute autre branche `course/*` (§ 3, « Jamais ouvert » ; § 5, deuxième tiret). Mon souci était qu'une branche sous ces préfixes porte des sorties fermées. Je l'ai vérifié sur ce commit : la branche a pour tête `5402367e…` ; entre `c76e7916…` et `5402367e…`, trois commits seulement (`d532ed0f…`, `76c608b6…`, `5402367e…`), qui ne touchent que `tests/test_commande_lecture_v2.py`, `scripts/lancer_b5f_lecture_v2.sh` et `src/controle_ia/barreau5_familles/commande_lecture_v2.py` (noms et états des fichiers seulement) ; l'arbre de `5402367e…` est celui de `c76e7916…` plus ces trois ajouts. Récupérer ce seul nom n'amène donc dans le clone de la session aucun objet hors de ces trois fichiers. J'admets l'écart. Le repli de la v2 (pousser le même commit sous un autre nom) reste à la mère, et il est plus propre.

## Les trois ajouts

- **A, commande de lecture version 2.** Branche récupérée par son nom entier vers une référence distante ; tête `5402367e5b62c8ac294c55d5cc0230ebdfbaa457`. Par `git show` à ce commit : module `c6c5d11c04f337c789c7f5a289d5190f51772b4ff96893499a8a5d07bc565ef0`, lanceur `c07fc1244860aa9795b3c5b610ddc78115f58c818ecb25b9aa2fcfae87aabcbf`, essais `824522047421f9e8e173ebad520c7fc1b0504d8ddac903a71e4e1a80e103336a` : égaux au § 3, point 6. Le commit descend de `c76e7916…` ; `LISTE_FERMEE` du module est bien ces trois chemins. Lanceur lu en entier : onze arguments, `commande decisif RACINE OFFRE.json COMMIT BRANCHE_CODE RUN_ID ENTREES_COMMIT DIVERGENCE GARDE EXISTANTS.json`, `GO_ID` lu dans l'environnement, refus de tout plan autre que « decisif » et de toute autre sous-commande, sortie 2 sur refus : conforme au § 5.4, pas 5, et au § 5.1. Module lu en entier : les vérifications (a) à (d), la garde du stockage par pièce (0,12 et 0,08, /730), le refus d'un autre arbre (`exiger_module_joue_depuis`) : conformes à la description du mandat. La ligne `GO-2026-11-19-86` figure au registre des accords de ce commit. La v1 du lanceur, au commit figé, prend bien onze arguments pour « commande » et six pour « config » (pas 3 et pas 5, plan répétition, conformes).
- **B, format de la ligne de l'accord de lecture.** Le motif `_CITATION` du module, extrait et rejoué hors ligne sur la ligne même du § 5.2 (nom remplacé par un nom d'essai) : forme composée acceptée ; même ligne normalisée en forme décomposée, refusée ; suite libre « ; … » acceptée ; le commit capturé égale `5402367e…`, l'empreinte de l'additif capturée est `c3120d3a…`. **Le « é » contrôlé par Python (`ord`)** : dans le mandat, « vérifiée » donne `0x76 0xe9 0x72 0x69 0x66 0x69 0xe9 0x65`, deux U+00E9 ; le mandat n'a aucun U+0301 et égale sa forme normalisée composée ; dans le module, le « vérifiée » du motif donne les mêmes valeurs, aucun U+0301 dans le fichier. Séparateurs, longueurs (64, 40, 64), interdits (barre verticale, saut de ligne) et unicité des deux citations : conformes au code.
- **C, commit de la marche à venir.** Dit tel quel au § 5, premier tiret, et au § 9, point 9 ; ce que la session vérifie (descend de `c76e7916…`, même arbre gelé, registre qui admet la marche, préfixes refusés) est écrit. La lecture du concepteur (« à suivre » veut dire « viendra de la mère ») est marquée « à confirmer » : c'est à la mère.

## Empreintes recalculées

Sur disque, égales aux valeurs de la v2 : texte scellé `bdff244f…d5935`, devis `dc886195…59bcc`, additif 1 v2 `c3120d3a…8e120c`, pièce de scellement `02d1c52f…0028f`, vérification de l'additif `905f2015…eacfc5`, mandat v1 `3e6d611b…ba6cdf`, contre-lecture `d6fd13bc…a0234b`. Au commit `c76e7916…`, par `git show` : `lecture_v1.py` `ed0999df…5626f`, `relecture_v1.py` `f6bd8c15…756ac`, lanceur v1 `ae501c55…170aa2f1a`, amorce `54a676f3…44453f` : égales. Au commit `5402367e…` : les trois valeurs de l'ajout A, égales. Le chiffre /720 du pas 2 renvoie bien à l'additif 1 v2, § 8, pas 4 (ligne 171, « supposé »), et la formule du code, /730, à sa ligne 17.

**Non vérifié** : l'empreinte du rapport de vérification `fca7d949…` (chemin non donné ; aucune commande de liste ne m'était permise hors de mon dossier) ; seule sa forme passe le motif du module. Les essais de la version 2 n'ont pas été rejoués ici (hors du mandat de cette vérification) ; la session les rejoue (§ 5.1).

## Observations mineures (sans effet sur le verdict)

1. **§ 5.4, pas 2 : « motif qui commence par « offre : » ».** Le motif de la garde commence bien par « offre : » (version 2 et version 1, `relecture_v1.py`, lignes 985 à 1003), mais la ligne que la session voit sur la sortie d'erreur est « ARRÊT : offre : … » (le module l'imprime ainsi, version 1 ligne 1246 et version 2). Une session stricte pourrait s'arrêter au lieu de passer à l'offre suivante. L'erreur va dans le sens sûr (arrêt, mot de la mère). Erratum possible : « ligne d'erreur « ARRÊT : offre : … » ».
2. **§ 5.1 : « Aucun fichier modifié » et « `registres/go.md` est à jour ».** La phrase vient de la v1, et ma contre-lecture ne l'a pas relevée. Le code ne garde que les chemins gelés, d'où `registres` est exclu (`CHEMINS_GELES`), et `GO-2026-11-19-86` est déjà au registre des accords du commit de commande. Les deux clauses tiennent donc sans retouche. Erratum possible : « aucun fichier modifié sous les chemins gelés ».

## Ce que j'ai lu, ce que je n'ai pas ouvert

Lu : ma contre-lecture, les mandats v1 (par empreinte et par motif) et v2 (en entier) ; au commit `5402367e…`, le module et le lanceur version 2 en entier, et les noms seuls des fichiers des commits depuis `c76e7916…` ; au commit `c76e7916…`, les lignes d'arguments du lanceur version 1 et les lignes des refus d'offre et de l'impression de l'arrêt de `relecture_v1.py` ; la définition de `CHEMINS_GELES` ; le compte des mentions de `GO-2026-11-19-86` au registre des accords du commit de commande ; dans l'additif 1 v2, les lignes portant « 720 » ou « 730 ».
Jamais ouvert : le fichier d'essais version 2 (son empreinte seulement), la table, le sel, toute branche de données ou de formation, tout fichier de scores, `diag/`, `docs/verdicts/`, tout fichier dont le nom contient « consigne-privee », « conception-ii-b », « vérité », « verite », « rendu » ou « scores », `brouillons/`, `donnees/`, `archives-reponses-modeles/`, `/root/.claude/`, du texte scellé rien au-delà de son empreinte. Aucun commit, aucune poussée, aucun appel payant, aucune commande vers le loueur. Une seule référence distante créée dans le clone : `origin/course/barreau5-commande-lecture-v2`.

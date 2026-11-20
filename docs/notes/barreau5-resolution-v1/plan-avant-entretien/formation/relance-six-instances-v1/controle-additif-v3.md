# Contrôle de l'additif 1, v3, par différentiel (barreau 5)

**Verdict : scellable.**

## Empreintes
- L'additif v3 a pour empreinte sha256 20e862a3155aaf7db27fd765a4b912357057e3b0cb6f4ecdd9adad3add50606a, égale à l'annoncée.
- Le différentiel de la v2 à la v3 a pour empreinte sha256 ebd87d50187779e94944daac99ed7e1bb4f42f5f52cfe6fe9649357e4440350b, égale au préfixe annoncé (ebd87d50…).
- L'additif v2 de départ a toujours l'empreinte 4f785bd9…151b9d.
- Le différentiel est fidèle : refait par `diff -u` entre la v2 et la v3, il est identique au fichier fourni, en-têtes de date mis à part.

## 1. Le différentiel ne touche que les couples N1 à N5 et V-1
Chaque retouche se rattache à un couple :
- **en-tête** : titre « v3 », ligne d'état, chemin de scellement en « -v3 ». Ce sont les suites de la nouvelle version, sans effet sur le fond ;
- **« Autorité »** : couple N2 ;
- **« Ce que le rédacteur a lu »** : couple N5 ;
- **C5, tiret de la mention** : couple N1 ;
- **dernière ligne de la table** : couple N4 ;
- **§ 4, point 2** (séparateur, référence complète, commit vérifié, renvoi au contrôle) : couples N1 et V-1 ;
- **§ 4, point 3** : couple N3 ;
- **§ 5, tiret neuf « le contrôle de la ligne avant de la commettre »** : couples N1 et V-1.

Rien d'autre n'est touché : faits, C1 à C4, C6 à C8, § 3, § 6.

## 2. Chaque couple est levé

| couple | levé ? | où |
|---|---|---|
| N1, forme exacte de la mention et contrôle avant de commettre | levé | C5 : 40 signes minuscules de « a » à « f », séparateur « ␣;␣ » ou bord de la référence, mots « code des relances » une seule fois. § 4, point 2, et § 5 : contrôle obligatoire avant de commettre la ligne. |
| N2, clé neuve nommée par l'accord | levé | En-tête : « l'accord nomme aussi une clé neuve ; elle n'est pas employée : C5 ». |
| N3, lignes de la lecture qui restent | levé | § 4, point 3 : `GO-LECTURE-B5F`, `SCORES-B5F`, `OUVERTURE-B5F`, `LECTURE-B5F`, `VERDICT-B5F`. |
| N4, « la référence est libre » | levé | Le passage est nommé dans la table ; la mention lue à la lettre fait exception. |
| N5, coupures de 21 et de 8 dollars | levé | Le relevé est sourcé (devis `dc886195…`, section 4, ligne d'engagement), et la session mère les vérifie avant le scellement ; la mère dit l'avoir fait. |
| V-1, contrôle de la ligne avant de la commettre | levé | § 5 : deux lectures du registre candidat, à faire avant de commettre la ligne : <br>• par `formation_v1.lire_code_et_accord` du code vérifié d116bf78, qui doit rendre 1,2,3,4,5,7 et ce commit ; <br>• par `lecture_v1.relance_du_registre` du code figé, qui doit rendre [1,2,3,4,5,7]. <br>Si l'une refuse, la ligne n'est pas commise. Le § 5 note aussi que le programme du développeur compose lui-même une ligne d'essai : il faut donc lui faire lire la ligne candidate. |

## 3. Aucune retouche n'introduit d'erreur
- **Description de la mention en C5.** Elle colle à l'expression régulière du code d116bf78, `(?:^|; )code des relances commit ([0-9a-f]{40})(?= ;|$)`, et au compte `ref.count("code des relances") != 1`.
- **Commit cité au § 4.** Il est égal au commit vérifié « conforme » (`d116bf78bb2084b2d4f406535a6c6f0a23179efe`, tête de la branche dans `$S/relance/code`).
- **Barres « | » au § 4.** La citation du devis en contient, mais dans le texte de l'additif, pas dans une ligne de registre : sans effet.
- **Seule réserve, de forme et sans gravité.** La phrase de N5 dit « la session mère les vérifie avant le scellement », au présent. Puisque la mère a fait cette vérification, elle peut, si elle le souhaite, l'écrire au passé (« les a vérifiées : 21 et 8 USD ») dans la ligne de scellement. Cela ne retient pas le scellement.

## 4. La référence complète du § 4 est conforme au code d116bf78
J'ai rempli la référence proposée :
- chemin proposé en « -v3 » ;
- empreinte d'essai de 64 signes ;
- cumul d'essai de 21,37 USD.

Je l'ai écrite par `engagement_v1.ligne_du_registre`, relue par `engagement_v1.lignes_du_registre`, puis passée à l'expression `_CODE_RELANCE_REF` et au compte `MENTION_CODE_RELANCE` du code d116bf78, extrait par `git archive`. Résultats :
- la référence est relue identique : l'expression `_LIGNE` ôte seulement les espaces des bords ;
- « code des relances » y paraît exactement une fois, et l'expression trouve un seul commit, `d116bf78bb2084b2d4f406535a6c6f0a23179efe` ;
- la référence fait 432 signes et la ligne entière 529, sous la limite de 600 signes ;
- la mention est précédée de « ; » et d'une espace (après l'empreinte) et suivie d'une espace et de « ; » (avant « cumul ») : les deux bords de l'expression sont satisfaits ;
- aucun autre élément de la référence ne contient « code des relances » ni « | ».

Ce contrôle ne remplace pas celui du § 5 sur le registre candidat réel, avec son vrai chemin, sa vraie empreinte et son vrai cumul.

## Déclaration
Pour le point 4, j'ai écrit dans `$S/relance/` un petit programme d'essai, une extraction de `src/` du commit d116bf78 et la sortie d'un `diff`. Je les ai supprimés aussitôt après usage. Il ne reste que ce rendu. Je n'ai rien lu de `diag/`, des branches `donnees/`, d'aucun score ni résultat, ni rien sous `/root/.claude/`.

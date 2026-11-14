# Remise des marqueurs de l'ordre de l'étape A de T0.7 (variante B) — valeurs proposées — v1

- **Auteur** : préparateur neuf (Claude Opus 5.5, `claude-opus-5-5`), sous-agent de la session mère
  `session_01QPDgKgACWyCkCN8HjqwNXy` ; exclu ensuite de tout rôle de lecteur de P3-bis.
- **Écrit le** 2026-11-13 vers 18:35 UTC (`date -u`), avec `prealables-etape-a-v1.md` (même dossier), qui porte les
  vérifications et les preuves ; tête de `main` relevée : `b4d375c9`.
- **Ordre visé** : `docs/procedures/ordre-execution-etape-a-t07-v1-brouillon9.md`
  (`374332976304d08af7c1b941d8798877d34f9e30b3945ba2be3ac19189740402`), celui que cite le texte scellé de T0.7 (l. 2677, l. 3397),
  **et non le brouillon 5** nommé par le mandat (raisons : `prealables-etape-a-v1.md`, § 1).
- **Règle suivie** : rien d'inventé ; chaque valeur renvoie à une ligne de registre, un fichier empreinté ou une commande
  rejouée ; un marqueur qui attend un geste ou un mot est laissé ouvert et nommé.

## 0. Résumé

- Douze marqueurs, une occurrence chacun (l. 99, 214, 258, 276 du brouillon 9).
- **Neuf valeurs proposées**, prêtes (sources ci-dessous).
- **Trois attendent un geste de la mère** (aucun un mot de Lazar) : `ID_SESSION_FILLE` (identifiant connu à la création de
  la fille), `PERIMETRE_T07` (valeur `JD,JA` proposée, à confirmer par l'écrit daté que P3 exige), `DEPENSE_ANTERIEURE_USD`
  (valeur `0` proposée, à relire juste avant la création, après l'inscription de l'engagement).
- **Aucun marqueur n'exige un mot de Lazar.**

## 1. Valeurs proposées

1. **`ID_SESSION_FILLE`** (en-tête, l. 99) — **ouvert** : identifiant rendu par la création de la session fille. Source :
   aucune avant la création. Geste : la mère.
2. **`EMPREINTE_CONFIG_T07`** (§ 1, l. 214) — `0f32c6de1a6bf1f20ee2bf74c3839c2a2054b77c34a44a557dc821a83db60e12`.
   Sources : `PYTHONPATH=src .venv/bin/python -m controle_ia.t07.lecture_v4 empreinte-config prereg/T0.7-sondes-v0-v1-configuration-t07-v8.json`
   rejoué le 2026-11-13 (code 0) ; texte scellé de T0.7 l. 749 ; R-2321.
3. **`LIGNE_SCELLEMENT_T07`** (§ 3, P5, l. 258) — la ligne exacte, sans espace final :
   `| SCELLEMENT-T07 | 2026-11-11T07:11:42Z | prereg/T0.7-sondes-v0-v1.md | d7d180eccbbce8ff2e370f82957543c28f1e564c872f981c7ada403949baade5 |`
   Source : `registres/scellements-v1.md` (`1eaab114be2b8d44797645cf0791f9dd639cd13195784f170235f9d16259d3d8`) l. 8, lue par
   `grep '^| SCELLEMENT-T07 |'` (une ligne, `cat -A` : aucun espace final). Note de forme : dans la case de tableau du
   brouillon 9, les barres verticales de cette valeur cassent le rendu du tableau ; la fille lit le texte brut et l'écrit
   à l'octet dans `ligne-scellement-t07.txt` (§ 4.1).
4. **`DEPENSE_ANTERIEURE_USD`** (ligne (A), l. 276) — `0`. Source : `registres/depenses.md`
   (`4e61067974100bbdb279825e69b7e717891786cccad70e6138d04f8ab5dc5ef7`) : aucune ligne sous GO-2026-11-10-04 ni sous
   GO-2026-11-10-06 (`grep -cE` : `0`). **À relire juste avant la création** : la ligne d'engagement à inscrire ne porte pas
   de dépense ; toute dépense inscrite d'ici là sous ces deux lignes change la valeur (P8 : `ANT0` ≤ 3,6 USD).
5. **`RUN_T06_7B`** (ligne (A)) — `20261111-151701-t06-reel`. Source : R-2413 (l. 2371) ; présence de
   `runs/20261111-151701-t06-reel/manifeste.json` sur la branche de 7b vérifiée par son nom (`prealables-etape-a-v1.md`, § 3).
6. **`BRANCHE_7B`** (ligne (A)) — `calcul/t06-confirmation-7b-v1`. Source : R-2413 ; `git ls-remote` : tête
   `55c3e3eb89a4650419f35999aaa4c54288275b0d`, égale à R-2413.
7. **`COMMIT_CODE_T07`** (C7, ligne (A)) — `b4cd9953d199dd8f220f5162e5868c5b00fd392d`. Sources : R-2316 (l. 2274) ; champ
   `commit` de `registres/code-t07/CODE-T07-v2.json` (`d5eb0b66…`, cité par la ligne `CODE-T07`) ; vérificateur
   `code_t07_v1 verifier` : conforme.
8. **`COMMIT_SCELLEMENT_T07`** (S7, ligne (A)) — `2576442b0e7a1e8089620199edb2ac638d5d4c1d`. Source : `git log --format=%H --
   prereg/T0.7-sondes-v0-v1.md` (un seul commit, 2026-11-11 07:12:50Z, message « T0.7 SCELLÉ (d7d180ec) sur mot de Lazar :
   texte, configuration v8, SCELLEMENT-T07, GARDE-ADAPTEE-T07-P3BIS ; R-2321 ») ; le registre n'écrit pas cette empreinte en
   toutes lettres : la mère la confirme. Contrôles du § 4.1 rejoués : C7 ancêtre de S7, S7 ancêtre de `main`, différence
   C7–S7 sur `src` et `tests` vide, arbres égaux.
9. **`CHEMIN_CONFIG_T07`** (ligne (A)) — `prereg/T0.7-sondes-v0-v1-configuration-t07-v8.json`. Sources : R-2321 ; texte
   scellé l. 749 ; fichier `e31c7a79dc1b68d561874d4d42d63b5eb950931f06075927f239c7ad971fb328` = compagnon = fichier à S7.
10. **`PERIMETRE_T07`** (ligne (A)) — `JD,JA` **proposé, ouvert à l'écrit de la mère**. Source : `scellements-v1.md` l. 3
    et 4 ; `-JC` et `SCELLEMENT-CONCEPTS-T07` absentes ; commande du § 4.1 rejouée : `PER=JD,JA`. P3 exige que la mère dise
    **par un écrit daté**, recopié au journal avant la création, si elle attend `-JC` et les concepts ; la valeur devient
    `JD,JA` si elle n'attend pas (option (c) : étape A « sans concepts », T0.7 (b) 1).
11. **`ATT_C7_T07`** (ligne (A), entre apostrophes) — `479 passed, 2 skipped, 4 xfailed`. Source : décision de la mère
    R-2319 (l. 2277 ; mesure `docs/notes/g0-deux-semaines-v1/t07-module-v2/plancher-v3-pieces-v1/mesure-att-c7-v1.md`,
    `b70c77fd…`). **Réserve que R-2319 demande d'écrire au remplissage** : sur un hôte à instructions AVX-512 (Intel récent ;
    EPYC de quatrième génération non vérifié), la ligne porte « , 1 warning » et l'étape 6 s'arrête en code 2 avant le
    modèle (≈ 1 USD) ; l'instance n'est recréée, sur un EPYC de deuxième ou troisième génération, que sur un écrit de la
    mère. Mesure faite sous Python 3.13.16, non rejouée sous Python 3.11 (image de l'instance).
12. **`COMMIT_SRC_CONTRE_LU_T07`** (`SRC7`, ligne (A)) — `a621dcd3b929ce3ebd615fa852d4a7f5c103071d`. Sources : R-2321
    (l. 2279 : « `COMMIT_SRC_CONTRE_LU_T07` = `a621dcd3` ») ; table des marqueurs du brouillon 9 (l. 714 : « `a621dcd3…` est
    le dernier commit contre-lu ») ; R-2316. **Ambiguïté signalée** : le § 1 du brouillon 9 (définition du brouillon 7) dit
    `SRC7` = « commit de `main` qui fusionne la branche finale du code », soit C7 lui-même (`b4cd9953…`). Les deux valeurs
    ont le même arbre `src/` (`5faa6d9d575445cd0db6cbb6ede57a91e442a081`) et passent le contrôle du § 4.1
    (`git diff --quiet "$SRC7" "$C7" -- src` : vide, vérifié) ; `a621dcd3` est parent de la fusion C7, donc présent dans un
    clone de la seule branche `main`. Je propose `a621dcd3…` (dernière décision datée de la mère).

## 2. Ligne (A) remplie qui en résulte (si la mère retient ces valeurs ; `PER` sous réserve de son écrit)

```bash
W=/home/user/etape-a-t07-b-v1; M=$W/main; J=$W/journal-etape-a-t07-b-v1.md; GO=GO-2026-11-10-06; GO4=GO-2026-11-10-04; PLAF=20; ANT0=0; RUN6=20261111-151701-t06-reel; BR7B=calcul/t06-confirmation-7b-v1; C7=b4cd9953d199dd8f220f5162e5868c5b00fd392d; S7=2576442b0e7a1e8089620199edb2ac638d5d4c1d; CFG=prereg/T0.7-sondes-v0-v1-configuration-t07-v8.json; PER=JD,JA; ATT='479 passed, 2 skipped, 4 xfailed'; BR=donnees/t07-etape-a-v1; SCRIPT=scripts/etape_a_t07_variante_b_v4.sh; SHA_SCRIPT=4b17d1f05441f5206d9f4ac58fb5ccf2b755bd86c13bee622ccf3bc327df05c6; SRC7=a621dcd3b929ce3ebd615fa852d4a7f5c103071d; REV_P3=0e9e39f249a16976918f6564b8830bc894c89659; URL=https://github.com/lciric/controle-ia-travail.git; j() { printf '%s %s\n' "$(date -u +%FT%TZ)" "$*" >> "$J"; }
```

Seuls les huit marqueurs de la ligne (A) y changent ; le reste est la ligne (A) du brouillon 9 à l'octet.

## 3. Ordre rempli : proposition de forme

- Nom neuf (R12), sur le modèle de l'ordre scellé de 7b (R-2328 : brouillon 6 rempli = `ordre-fille-course-confirmation-7b-v1.md`) :
  **`docs/procedures/ordre-execution-etape-a-t07-v1.md`** = brouillon 9 + les douze valeurs, rien d'autre.
- **Contrôle mécanique** avant le scellement : remplacer chaque valeur par son marqueur entre chevrons redonne le
  brouillon 9 à l'octet (`37433297…`) ; douze remplacements, chacun à son seul emplacement ; aucun autre octet changé.
- La réserve de `ATT` (point 11) et les écrits du § 4 vont au registre (ligne R du remplissage) et à la consigne de la
  fille, **pas dans l'ordre** (sinon le contrôle ci-dessus ne tient plus).
- Puis `PYTHONPATH=src python -m controle_ia.scellement sceller docs/procedures/ordre-execution-etape-a-t07-v1.md`, commit,
  poussée sur `main` ; la consigne de la fille cite son chemin et son empreinte.

## 4. Écrits et lignes que l'ordre exige en plus des marqueurs (gestes de la mère, aucun mot de Lazar)

1. **`RUN-CONFIRMATION-T06`** (P2) : `| RUN-CONFIRMATION-T06 | <date UTC de l'inscription> | runs/20261111-151701-t06-reel/manifeste.json | 7e1ac1f02584e4f8babf664e78d12f3122bfdca18292734f28281e9459479bf6 |`
   (format de `registre_v1.ecrire_ligne`, l. 318-322 ; empreinte : R-2413, recalculée sur la branche).
2. **`GO-LECTURE-T07`** (P4) : `registres/go-extraits/GO-LECTURE-T07-v1.md` = la ligne l. 296 de `registres/go.md` à
   l'octet (empreinte attendue `8893d8df3b7366aa9d9eb84548747c586f2798c40956a1baa0d149b8d9630b52` si le fichier est cette
   ligne et un saut de ligne final), scellé (compagnon), puis la ligne `| GO-LECTURE-T07 | <date> | registres/go-extraits/GO-LECTURE-T07-v1.md | <empreinte du fichier> |`.
3. **Engagement** (P8) au registre des dépenses, sous GO-2026-11-10-06, avant la première minute de carte (T0.7 l. 2087-2089).
4. **Écrit daté sur le périmètre** (P3) : attendre ou non `SCELLEMENT-JEUX-T07-JC` et `SCELLEMENT-CONCEPTS-T07`.
5. **Écrit daté de `ATT`** (P12) : valeur, commit de la mesure (C7 `b4cd9953…`), arbres `src/` `5faa6d9d…` et `tests/`
   `7ab32147…` (R-2316, R-2319) ; et jugement « aucune remesure à S7 » (`prealables-etape-a-v1.md`, Q-13).
6. **Écrit daté de `SRC7`** (P13 (iii)) : l'arbre `src/` de `SRC7` est celui du dernier commit contre-lu (R-2316 le dit ;
   la mère le désigne pour recopie au journal).
7. **P14** : nombre de lignes des mesures de 7b, par le script versé (`f6fd192e…`), après vérification du sceau de
   `donnees/20261111-151701-t06-reel/mesures-t06.npz` (compagnon sur la branche : `aca5afd0…`) ; un entier ≤ ≈ 7 378, seul
   écrit au journal.
8. **Écrit d'installation de `vastai` 1.8.3** si la fille ne l'a pas (P10 ; précédent R-2351).
9. **Nom du jeton GitHub** : si `CONTROLE_IA_GITHUB_TOKEN` manque chez la fille, alias depuis `CONTROLE_IA_GITHUB_TOKEN_2`
   dans ses seuls shells (précédent R-2387) — décision de la mère.
10. **Garde d'ordre avec P3-bis** : aucune ligne `VERDICT-P3BIS` ni `OUVERTURE-P3BIS` sur `main` avant la recopie de
    `SCORES-T07` et `SONDES-T07` (`prealables-etape-a-v1.md`, § 4).

## 5. Points qui pourraient demander un mot de Lazar (hors marqueurs)

- **Crédit du compte de location** (non prévu par l'ordre). Enjeu : le pire cas commun de l'étape A (≈ 16,4 USD) et de 12 h
  du témoin Bailey (≈ 14,1 USD) dépasse le crédit projeté (≈ 26,6 USD vers 20:00Z, depuis 31,46 USD à 15:49Z). Options :
  (a) la fille relève le crédit (lecture seule) et ne crée pas sous un seuil de 20 − `ANT0` + 12 h × prix des instances en
  marche, compte rendu (avantage : aucune perte ; inconvénient : ajout à l'ordre, peut retarder) ; (b) créer sans
  relevé (avantage : à la lettre ; inconvénient : arrêt possible en cours d'étape, nœud). Recommandation : (a), seuil comme la
  garde du crédit de P3-bis (R-2512), recharge par Lazar si le seuil manque ; confiance 0,7. C'est une décision de la mère
  (routine) tant qu'aucune recharge n'est nécessaire.
- **Hôte à instructions AVX-512** (`ATT`, point 11). Options : (a) à la lettre, réserve de R-2319 (≈ 1 USD perdu par essai
  sur un tel hôte, recréation sur écrit de la mère) ; (b) écart à l'ordre scellé : ne retenir que des EPYC de deuxième ou
  troisième génération (nœud de Lazar). Recommandation : (a), confiance 0,6 (la perte est bornée et prévue ; (b) touche
  une pièce citée par un texte scellé).

## 6. Pour mémoire : marqueurs du brouillon 5 (à ne pas jouer)

Dix marqueurs (`ID_SESSION_FILLE`, `EMPREINTE_CONFIG_T07`, `LIGNE_SCELLEMENT_T07`, `DEPENSE_ANTERIEURE_USD`, `RUN_T06_7B`,
`BRANCHE_7B`, `COMMIT_CODE_T07`, `COMMIT_SCELLEMENT_T07`, `CHEMIN_CONFIG_T07`, `PERIMETRE_T07` ; l. 48, 86, 130, 146) ;
ni `ATT_C7_T07` ni `COMMIT_SRC_CONTRE_LU_T07`. Les valeurs ci-dessus leur iraient, mais ce brouillon appelle le script v2 et
`lecture_v2`, qui refusent la configuration v8 : il n'est pas jouable sous T0.7 scellé.

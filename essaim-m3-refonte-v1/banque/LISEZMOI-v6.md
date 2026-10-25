# Banque de tâches réelles — v6 : corrections de `LISEZMOI-v5.md` après la contre-lecture de la banque `confrontation-v3` ; référence « contraste de paire » figée (v1 à v5 restent)

Lignée conv-audit, 25 octobre 2026, 16:55–17:05 UTC (heures lues sur `date -u`). **La banque `confrontation-v3` ne
change pas** (`banque-confrontation-v3.json`, `157a2b45a8d9fd88cc5dca2f483c2dc79457d781d44f9802b2c053f530c0011d`) ;
ce LISEZMOI complète et corrige `LISEZMOI-v5.md` (`d346bac12cd2dd44…`, gardé) sur la contre-lecture de la v3
(sous-agent neuf, `contre-lectures/banque-v3-cl1/CONTRE-LECTURE-banque-v3-v1.md`,
`da6b744c640ed6c1e31b5db9c87345b1f05badcbd4c6477d7bf86f9db19ac4cb`) : **« utilisable après corrections »**. La v3 se
reconstruit octet à octet depuis la v1 et la clé ; la clé n'apparaît que dans son fichier ; sans la clé, l'identifiant,
l'ordre du fichier, le manifeste, `source` et la consigne d'amorçage restent au niveau du hasard. Levés : BC1-01,
BC1-03, BC1-06 (et BC1-09 pour la vérité) ; en partie : BC1-02, BC1-07, BC1-08 ; non levés : BC1-10, BC1-11.

## 1. Les deux constats majeurs, et ce qui en est fait

- **BC2-01 — la référence « contraste de paire » n'était ni figée ni conforme à BC1-02.** La v1 du script n'avait pas
  la règle lexicale de la première contre-lecture et découpait les mots aux espaces ; ses chiffres dépendaient de ces
  choix (« plus courte en mots » : 0,8333 ou 0,6667 sur `test_final` selon le découpage). **Correction** :
  `construction-v3/reference_contraste_paires_v2.py` reprend à l'identique les définitions de
  `contre-lectures/banque-v2-cl1/scripts/c4_paires_textes_v1.py` (lignes nettoyées, mots `[a-zà-ÿ0-9_]{2,}`, quatre
  règles : longueur en caractères, nombre de lignes, nombre de mots, mots des lignes propres par log-rapport), et **la
  référence est le maximum de ces quatre règles, jeu figé**. Sur la v3 (sortie
  `reference-contraste-paires-banque-v3-v2.json`) : longueur 0,8125 / **1,0** / **0,75** (train / test / test final) ;
  lignes 0,3438 / 0,375 / 0,4167 ; mots 0,8125 / 1,0 / 0,6667 ; mots des lignes propres 1,0 (en échantillon) / 1,0 /
  0,75 ; **référence : 1,0 sur `test`, 0,75 sur `test_final`** ; appariement sans erreur dans chaque part (ressemblance
  au moins 0,242 dans une paire, au plus 0,061 hors paire). Mêmes chiffres sur la v1. La v1 du script et sa sortie
  restent, **non utilisées**. Le traitement de fond est la décision de Lazar (N-046, 25 octobre, 17:43 Paris) : paires
  gardées et lues à côté de cette référence pour le pilote 4 ; une trace par paire en test et en test final pour l'étape 1
  et la confrontation ; un lot 3 sans paires au programme.
- **BC2-02 — rien n'épingle encore la v3.** `essaim_m3.banque.verifier_banque`, seule porte de `lancer --reel`, accepte
  la v1, la v2 et les artefacts à fuite de `construction-v3/artefacts-v1/`, rangés à côté de la v3 avec des compagnons
  valides. **Correction** : tout lanceur qui sert une banque **épingle son empreinte** (`157a2b45…` pour la v3) et refuse
  toute autre ; c'est le cas du lanceur du pilote 4 ; un lanceur de l'étape 1 ou de la confrontation doit le faire aussi.
  Les fichiers de `construction-v3/artefacts-v1/` sont des **artefacts d'essai, jamais à servir** (`artefacts-v1/LISEZMOI-v1.md`).

## 2. Phrases de `LISEZMOI-v5.md` corrigées (BC2-09)

- « maxima 0,6389 à 0,6667 » : **0,625 à 0,6667** sur les six cases (la case train comprise) ; 0,6389 à 0,6667 sur les
  quatre cases notées.
- « équivalence avec la v1 rang à rang » : l'équivalence se fait **tâche à tâche**, par `id_v1` (les parts de la v3 sont
  triées par identifiant nouveau).
- « aucun texte scellé ne les cite » (la v2 et `LISEZMOI-v4.md`) : **aucun préenregistrement scellé** ne les cite ; des
  registres et des messages (R-443, canal) nomment la v2.
- « une fuite juste à 80 % : refusée dans ce tirage » : vrai pour ce tirage ; la sensibilité est au § 3.

## 3. Ce que le contrôle v2 ne garantit pas (BC2-03, BC2-05, BC2-06)

- **Taux de refus à tort d'une banque saine : 2,45 %** (contre-lecture) ; seuils sur une grille au centième, quantile
  instable d'un tirage de calibration à l'autre (0,78 ou 0,81 selon les cases).
- Il laisse passer : une fuite de paire totale dans 35 % des banques ; une banque où la part se lit dans le numéro
  (code 0) ; une fuite juste à 85 % dans 24 % à 51 % des tirages selon les parts touchées. La garantie vient du tirage
  uniforme et du secret de la clé, pas du contrôle.
- L'essai A6 (texte modifié) est refusé par la garde de composition de `--seuils`, non par l'équivalence ; repris sans
  cette option, l'équivalence le refuse (contre-lecture, `k3-controle-v2-v1.txt`).
- Le mode équivalence imprime des identifiants v1 à côté des identifiants v3 (BC2-04) : la sortie de l'essai A7 en porte
  un, d'une tâche d'entraînement (sans effet : l'entraînement est servi avec sa vérité). Une version suivante du contrôle
  ne devra imprimer aucun identifiant v1.

## 4. Ce qui doit suivre — compléments à la liste de `LISEZMOI-v5.md` (BC2-10)

10. Toute analyse par lot passe par le champ `source`, jamais par les formes d'identifiant v1 (`cd-lot`, `ce-hf`,
    `-H`/`-S`).
11. La clé ne se passe jamais en ligne de commande (`--entropie` du constructeur sert seulement à un recalcul local,
    jamais journalisé) ; on la lit dans son fichier.
12. **Copie publique** : au-delà de `*-secret.json` et `*-cle.json`, tout fichier qui porte les vérités — les banques
    elles-mêmes (champ `verite`), les lots de traces, le sous-ensemble, les sorties d'essais — doit rester hors de toute
    copie publique (non vérifié dans `scripts/depot_expurge.py` ; l'arbre de l'essaim n'est pas sur `main`).
13. Identifiants d'attaque de la confrontation : garde de collision avec la banque à ajouter au noyau (BC1-11, non levé).
14. L'historique permet un sondage adaptatif du `test` sur plusieurs générations (BC1-10, non levé, inhérent au contrat) ;
    à dire dans tout préenregistrement à plusieurs générations.

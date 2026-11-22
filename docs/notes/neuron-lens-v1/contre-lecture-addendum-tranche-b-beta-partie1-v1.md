# Contre-lecture de la partie 1 de l'addendum des empreintes et des déclarations (tranche de l'ajustement de nos lentilles) — v1

- **Contre-lecteur neuf** (R2) : n'a écrit aucune pièce de ce travail ; n'écrit que ce rapport.
- Date (`date -u`) : 2026-11-18T05:38:05Z.
- Objet : `docs/notes/neuron-lens-v1/addendum-texte-gele-tranche-b-beta-v1-partie1-v1.md`, empreinte recalculée
  `d50ce0bc5166df7aa1c627eb4bea61eee84e1d5e430fb6ad3f2a96c3c7bcef50` (égale à l'attendue et à son compagnon `.sha256`).
- Texte gelé scellé : `texte-gele-tranche-b-beta-v1.md`, `f5d46860525f12f8ad0483e56afc0847ab7db25ecae55edcc279b61316b7a454` (recalculée, égale).
- Code des verdicts lu et sondé : `src/controle_ia/neuron_lens/verdicts_b_beta_v4.py`, `8c07434f…` (recalculée, égale à l'addendum).
- Non ouverts : `registres/`, tout autre fichier de `diag/` que l'addendum de la partie 2 de la tranche des lentilles publiques. Rien
  d'exécuté ni d'importé depuis `/home/user/stdlogits` (lecture par `git show`, `sha256sum`, lecture JSON seulement).

## Verdict

**À corriger** : 0 bloquante, **1 majeure**, 9 mineures.

La condition de la session mère est tenue pour l'essentiel : les trois lectures sont celles que le code applique, elles sont écrites
en clair, avant toute donnée, et l'effet déclaré de la première est **juste** (vérifié par sonde). Mais cet effet est déclaré sur un seul
chemin, alors que la sonde en montre d'autres, dont un qui se déclenche avec **moins** de couches non lisibles que le cas écrit : c'est
la majeure. Toutes les empreintes, révisions et versions citées sont justes. Rang de la majeure : jugement du contre-lecteur ; la
correction tient en trois phrases et ne touche ni le code ni le texte gelé.

## Table des constats

| rang | lieu | constat vérifié | correction |
|---|---|---|---|
| majeure 1 | § 1.1, lecture 1, « Effet possible, déclaré » | L'effet écrit est juste : sur l'entrée saine des essais (`sain()`), `pass` de notre lentille R mis à 0,40 aux couches 16 à 27 donne la lecture contre pilotage (B-2) « non reproduit » et le verdict d'ensemble « non reproduit avec nos lentilles » ; avec 3 couches non lisibles (n = 47) rien ne change ; avec 4 couches non lisibles, où qu'elles soient dans 16 à 27, B-2 devient « autre » et le verdict « partiel ». **Mais il est incomplet**, la même lecture agit ailleurs (sonde) : (i) clause `r_med` < 0,30 de B-2 (bande 16 à 23, 8 couches) : **3** couches non lisibles dans 16 à 23 suffisent (2 ne suffisent pas ; 4 non lisibles dans 24 à 27 ne la neutralisent pas) ; (ii) l'écart à la lentille des logits (B-3, bande 4 à 15) : 4 couches non lisibles sur 12 font passer B-3 de « non reproduit » à « autre » et le verdict d'ensemble de « non reproduit avec nos lentilles » à « partiel » ; (iii) l'ablation par fenêtre (B-7), lu dans le code, non sondé : même règle sur ses deux clauses (bandes 8 à 15 et 26 à 29, en « ablate win »), sans effet sur le verdict d'ensemble, mais une bande 8 à 15 partielle retire aussi le déclencheur de l'audit A5 (`par_le_haut` exige « non partielle »). Borne utile : sous 32 pôles à une couche de 0 à 27 en « steer 1x », c'est la chaîne en défaut (b) qui prime (sonde : n = 31) ; l'effet ne vit donc que pour 32 ≤ n < 48. | Écrire l'effet pour chaque clause « non reproduit » : B-2 (`pass`, 4 des 12 couches 16 à 27 ; `r_med`, 3 des 8 couches 16 à 23), B-3 (4 des 12 couches 4 à 15), B-7 (3 des 8 couches 8 à 15 ; 2 des 4 couches 26 à 29 ; déclencheur de A5) ; dire que B-2 **et** B-3 portent le verdict d'ensemble ; dire la borne 32 ≤ n < 48. Nouvelle version (R12). |
| mineure 1 | § 1.1, lecture 2 | Conforme au code (`verdict_b2` : `hors05`, `hors10` sur `_lisibles`). Effet non déclaré, **dans le sens favorable** (sonde) : témoin à 0,07 à deux couches lisibles → B-2 « autre », verdict « partiel » ; la même entrée avec l'une des deux couches non lisible → B-2 « reproduit », verdict « reproduit avec nos lentilles ». La garde (a) (±0,10) reste jugée à toutes les couches, lisibles ou non. Le texte gelé (l. 168 : « chaque couche lisible ») soutient la lecture. | Ajouter une phrase d'effet : un témoin entre ±0,05 et ±0,10 à une couche non lisible n'est pas compté ; peut faire passer « partiel » à « reproduit ». |
| mineure 2 | § 1.1, lecture 3 et lectures de forme | Conformes : `defauts_score` boucle sur `LENTILLES` (moitiés comprises), quatre cibles, couches 0 à 27 (sonde : moitié paire à 0,20, couche 10, « ablate pos » → chaîne en défaut (a) ; couche 28 → rien). Arrondi à 4 décimales appliqué à B-3, B-4, B-6, gardes (e) et (j), audit A6 (sonde : 0,45 − 0,30 jugé égal à 0,15 ; 0,30 − 0,10 jugé égal à 0,20). B-5 : `Fraction(repr(float))` (sonde : 0,6 jugé égal à 0,60 ; 0,3 non inférieur à 0,30). L'en-tête du code déclare en plus : valeurs de `score` non écrites à 4 décimales **refusées** (`valider_table`), gardes et audits en booléens stricts ; l'addendum ne les reprend pas. Effet de la lecture 3 non écrit (une moitié seule peut mettre la chaîne en défaut : sens sévère). | Reprendre les deux refus de forme de l'en-tête ; une phrase d'effet pour la lecture 3. |
| mineure 3 | en-tête | « Écrite … vers 05:40 UTC » : le fichier date de 05:34:00 UTC (`stat`), son compagnon de 05:34:07 ; `date -u` du contre-lecteur pendant la lecture : 05:36:01. L'heure déclarée est postérieure à l'écriture. | Écrire l'heure relevée par `date -u`. |
| mineure 4 | en-tête, § 6 contre § 3 | La partie 2 est dite écrite « avant la première passe », mais elle doit porter les jetons gardés (connus après `03_token_counts.py`) et la provenance écrite par `05_act_corpus.py`, qui viennent **après** l'ajustement (texte gelé, P.3, étapes 1 à 3). Cohérent seulement si « première passe » = passe d'activations (`06_activations.py`), ce que le texte suggère (garde (r)) sans que l'addendum le dise ; les contrôles d'avant l'ajustement (modèle, lentilles, 932 documents, Drowse) relèvent alors des gardes de B0, non du scellement de la partie 2. | Dire quelle passe, et à quel moment chaque relevé de la partie 2 est fait et comparé (avant l'ajustement ; avant la passe d'activations). |
| mineure 5 | § 3, jetons gardés et corpus d'activations | La liste d'arrêt du texte exige de l'addendum les jetons gardés de Llama ; la partie 1 les renvoie à la partie 2 sans référence. Or la partie 2 de la tranche des lentilles publiques (`9612ae4e…`) porte déjà, pour les mêmes révisions et le même tokeniseur : liste `catalog.kept` de 89 498 identifiants, `c37186ad…` ; fichiers `act-dclm.jsonl` `64657ecb…`, `act-zh.jsonl` `c3202db1…`, `act-code.jsonl` `550944a2…`, `act-chat-llama-3.1-8b-instruct.jsonl` `9dbf9f44…`. Le reste de l'exigence est couvert : révision de Llama ; révision, identifiants (provenance `16957c52…`, 1 000 identifiants, lignes [0, 1000)) et `rows_sha256` du corpus d'ajustement ; provenances du corpus d'activations ; fichiers de Neuronpedia. | Citer ces valeurs comme références attendues (écart = nœud à la mère), ou dire pourquoi elles ne sont pas opposables ici. |
| mineure 6 | § 5 | Versions « celles de la partie 2 de B-α » : justes (python 3.12.16, torch 2.14.1, transformers 5.18.0, tokenizers 0.23.2, huggingface_hub 1.33.0, numpy 2.4.6, pyarrow 26.0.1, safetensors 0.8.0), mais `datasets` 5.2.0, présent dans cette partie 2, manque. | Ajouter `datasets` 5.2.0. |
| mineure 7 | en-tête contre § 1.2 et § 5 | « Cette partie ne change rien au texte gelé » : vrai pour les critères, seuils et empreintes. Mais § 1.2 élargit ce qui fait échouer la garde de l'essai de l'estimateur (f) (variante aux traits de Llama 3.1, absente de P.2 du texte, qui ne décrit que la recopie et la variante « réaliste »), et § 5 ajoute un nœud sur toute autre version de paquet. Les deux vont dans le sens sévère et sont déclarés avant toute donnée. § 1.2 lui-même est fidèle à l'essai v3 (`da0f0efc…` : base 500 000, facteur 8, `rms_norm_eps` 1e-5, 4 têtes pour 1, `torch.allclose(…, atol=1e-4)`, 11 tests = 2 + 2 + 2 + 1 + 3 + 1, quatre artefacts) et à la note v3. | Écrire : « n'en change aucun critère ; ajoute deux arrêts, dans le sens sévère ». |
| mineure 8 | §§ 1.1, 1.2, 3 (mots en clair) | Identifiants seuls, sans nom en clair à leur première venue : « B-2 », « B-5 », « A6 », « garde (a) », « garde (i) », « garde (r) », « B-α » (après le titre). | Nommer d'abord (« la lecture contre pilotage de notre lentille R (B-2) », « la lecture aux activations par la lentille S (B-5) », « l'audit des deux codes (A6) », etc.). |
| mineure 9 | § 4 | « (branche de session) » sans nom, alors que l'autre branche est nommée ; la branche courante du dépôt est `claude/tender-rubin-mfxjva`. | Nommer la branche. |

## Vérifié sans constat

- **§ 1.3** : le texte gelé (écarts 1 et 11) dit que le devis v12 (§ 1, § 4) comptait 1 000 documents et l'étape `08_reads.py` ; le devis
  v12 porte bien « 1 000 documents » (l. 138, 288, 300). 932 : `comptes-corpus-ajustement-b-beta-v1.json` (`n_pleins_128` 932, moitiés 466 et 466).
- **§ 1.4** : mot pour mot le texte gelé, l. 337-340.
- **§ 2** : révisions `0e9e39f2…` et `d2527c3c…`, `tokenizer.json` `79e3e522…`, `tokenizer_config.json` `177c7b61…`, J `d5300a15…`,
  J++ `8bd04f48…`, R publique `a63a1588…` : égales à la partie 2 de la tranche des lentilles publiques (`9612ae4e…`, recalculée) et à
  l'addendum des empreintes v3 de la branche `prep/neuron-lens-v1`.
- **§ 3** : révisions `2fa015e4…`, `af9c1333…`, `35a59fb0…`, `8049631c…` égales aux fichiers de provenance et à l'addendum v3 ;
  provenances recalculées : `16957c52…`, `a26a7077…` (`skip` 1 000, `n` 40 000), `d0ba016a…`, `ab2f687d…`, `a76c6b02…` ; comptes
  `d86ddf4d…`, `ebc557e3…` ; `rows_sha256` `a6afd972…`, moitiés `4a31baec…`, `ef95a60c…` lus dans `comptes-rows-sha256-b-beta-v1.json`.
- **§ 4** : toutes les empreintes abrégées commencent l'empreinte réelle (`76b639a0`, `24c8ea18`, `616434bc`, `55f9d4a3`, `c8e53f7d`,
  `ede719f6`, `f85c36db`, `94e5a7d7`, `fec2c0a7`, `6a9fe088`, `da0f0efc`, `8c07434f`, `1b63c8cb`, `a479f561`, `7444555b`, `4ed8e71c`,
  `55403c29`, `00599d48`, `a32b1f3b`, `79605cac`, `51508e77`). Fichier corrigé `c974cc1a…` : **recalculé** en appliquant le diff v2 au
  fichier publié (`git show HEAD:scripts/checks/lens_compare.py`, `37b30e98…`) dans une copie jetable. Commit voisin
  `849bfe1678e28becceb1e3864afe5fc8297d02e4` = `HEAD` de l'arbre local, arbre propre. 82 essais : sortie scellée (« 82 passed »).
- **§ 5** : paquet Drowse `673ed2b4de653ad2ec22660b0191031ee2c7b4bacaf4cc2ea552f0436b9d8e03` recalculé sur `/home/user/drowse-lecture/`.
- **Lecture 1 reprise de la tranche des lentilles publiques** : `verdicts_b_alpha_v3.py` (branche `prep/neuron-lens-v1`) la déclare en tête (l. 10-12).
- **R6, R12** : compagnon `.sha256` présent et juste ; version dans le nom ; chaque chiffre renvoie à une pièce empreintée.

## Non vérifiable

- Les renvois R-3190, R-3180, R-3171, R-3151 et « option (a), recommandée par l'autrice » : dans `registres/`, non lu par consigne.
- Les empreintes des poids et du tokeniseur de Llama et des trois fichiers de Neuronpedia : fichiers absents ici ; seule l'égalité
  avec la partie 2 de la tranche des lentilles publiques est vérifiée. Les révisions n'ont pas été relues sur le hub.
- « Texte gelé v6 » : non ouvert ; les empreintes des lentilles sont corroborées par l'addendum v3, qui les dit égales à ce texte.
- « Test du dépôt recopié mot pour mot » : non comparé ligne à ligne au test du voisin ; repose sur `verification-essai-llama-miniature-v3.md` (`55403c29…`).
- « 10 tests » de l'essai de la comparaison des lentilles : repose sur la note v3 (4 fonctions dont une paramétrée) ; non rejoué. Les
  11 tests de l'essai du Llama miniature sont recomptés à la lecture, non rejoués ; les 82 essais des verdicts ne sont pas rejoués
  (sortie scellée lue ; le module a été importé et sondé).

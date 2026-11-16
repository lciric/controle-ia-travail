# Contre-lecture du crible (v), brouillon 7 — lecture entière (tour 1 de ce lecteur, tour 7 de la numérotation de la pièce)

- Lecteur : sous-agent neuf, modèle C. Je n'ai écrit ni la pièce, ni ses brouillons, ni les corrections, ni aucun rapport précédent.
- Lecture de 15:07:27Z à 15:20Z (`date -u`). Aucun appel de modèle, aucune dépense, aucune machine ; rien lu sous `diag/`, `runs/`, `donnees/` ; relevé de v67 non ouvert ; sortie du pilote MR-2 non ouverte (voir « Incidents » pour une ligne de registre vue sans l'avoir cherchée) ; dossiers jetables du premier lecteur non touchés ; rien de 7a, 7b, T0.6, T0.7, P3-bis ni du bras d'attaque.
- Pièce relue : `docs/notes/organisme-idees-juge-v1/cribles-v1/crible-v-brouillon7.md`, empreinte `083a322de48bc12d1ac250d8687f304dcf876bfcfd557bd84e154d7321a232b1` (égale à son compagnon `.sha256`).
- Version précédente : `crible-v-brouillon6.md`, `08b430d7ec9cc4b7435dd46c772b0e56cc92a1630e945e38f46d1ec7d97624d6`. Rapport précédent : `contre-lecture-crible-v-b4-tour3-v1.md`, `da47da2f5bd47c7eaa90ead4d4a2d9bcf65474d500ad83543ae2b35b31b5bec5` (empreinte vérifiée, égale à celle que la pièce cite).

## Verdict

**corrections.** La conception tient (aucune porte ne s'ouvre après lecture du crible ; R1, R3, R5, N-058 tenus ; les corrections du tour précédent et les décisions de la mère sont appliquées fidèlement). Mais deux points sont majeurs parce qu'ils laissent une marge de décision après coup ou affirment à tort une appartenance à l'enveloppe de dépense : (B7-01) la pièce écrit que le pire cas est « dans l'enveloppe de GO-2026-11-15-06 », alors que la mère a écrit que la somme des cinq pires cas peut la dépasser (R-2992, point 3), et que la sonde neuve porte ce crible à 204,67 ; (B7-02) « fournisseur », « abandonné » et « perdu en entier » ne sont définis nulle part dans la pièce, alors que l'étage 1 et une ligne de la liste d'arrêt en dépendent. **2 majeures (B7-01, B7-02), 4 mineures (B7-03 à B7-06), 6 remarques facultatives.**

## 1. Application du tour précédent et des décisions de la mère

- Les sept couples D6-01 à D6-06 ont été extraits du rapport par programme et comparés à la pièce : D6-01, D6-03, D6-04a et D6-06 : « nouveau » présent une fois, « ancien » absent ; D6-04b : « nouveau » présent, son « ancien » reste en préfixe (normal) ; D6-02 et D6-05 : « nouveau » **retouché** et la retouche est déclarée (N = 20 seul pour D6-02 ; branche à 24 mondes retirée et « ci-dessous » devenu « ci-dessus » pour D6-05) ; les retouches sont conformes à R-2992. Application fidèle.
- `diff` du brouillon 6 au brouillon 7 (383 lignes de différence) : il ne reste que (a) les couples D6, (b) les couples « r2992-… » que la pièce nomme (N = 20 partout ; étage 5 sans verdict ; partie A sans le champ des « retenues » ; sonde neuve exigée ; points ouverts de « Choix et doutes » à la recommandation écrite ; mentions « rédacteur modèle C » corrigées), (c) les couples propres (titre, en-tête, statut, validateur, tête de la section, entrée « Contre-lecture 6 »). Je n'ai trouvé aucun changement non déclaré.
- Décisions de R-2977 et de R-2992 (lignes lues dans `registres/decisions.md`) : archive réduite à K1 ; mondes séparés d'avec (iii) ; dollars principaux au prix public, prix de la configuration en sensibilité ; GO valable pour l'essai, non pour l'adoption ; partie A permise, descriptive, sur données déjà vues, sans aucun verdict du juge, archive de la génération 2 sans le champ des « retenues » ; tension avec N-058 à dire à Lazar avec le nœud d'adoption ; N = 20 dans tous les cas ; étage 5 sans verdict (N-045 point 3) ; points 1, 3, 7, 8, 10, 10 bis pris à la recommandation (sonde neuve exigée) ; tolérance de la réflexion de Pr-1 sur la seule ligne de GO de Pr-1 : **toutes présentes** dans la pièce.
- Reste d'anciennes décisions dans le texte : point 5 de « Choix et doutes » garde l'historique « 24 mondes » avec la mention « Amendé (R-2992) » ; sans contradiction.

## 2. Vérifications de fond (relues en entier)

1. **R1.** Hypothèse H-v et H-v-a ; prédictions V1 à V7 avec signe, chiffre, zone de réfutation (sauf V4, voir F-B7-1) et confiance ; métrique ; seuils ; plan d'analyse ; table de verdicts par étage ; liste d'arrêt de 21 lignes ; règles écrites d'avance pour ce qui se refait d'après le pilote (B_a, M, montants, tolérance de Pr-1, V1 et V6). Pas de porte de sortie après lecture, sous réserve de B7-02 (marge sur « abandonné ») et de B7-05 (mécanisme de gel).
2. **R3 : seuils.** S_R ≥ 0,25 et W_min = 4 sur 16 à 20 mondes complets sont dits « choix de ce texte, de portée pratique, non déduits d'une donnée », posés avant toute donnée, avec leur puissance. J'ai refait par programme (bibliothèque standard) : bornes de Clopper-Pearson (W_min = 4 de 16 à 22 ; 0,0573 à n = 20 ; borne haute 0,168 pour 0 sur 20), probabilités d'une perte établie (20 mondes à risque : 0,133 ; 0,352 ; 0,589 ; 0,804 ; 0,956 à p = 0,10 ; 0,15 ; 0,20 ; 0,26 ; 0,35 ; 17 mondes à risque : 0,244 ; 0,681 ; 0,897 à p = 0,15 ; 0,26 ; 0,35 ; 0,0159 à p = 0,05), épargne S(k) (0,2485 à k = 13 au poids 0,71 ; 0,2625 à k = 13 et 0,225 à k = 14 au poids 0,75). **Tous égaux à ceux de la pièce.** La puissance est modeste (0,59 à p = 0,20 ; 0,68 à 0,26 sous k_R = 3) et la pièce le dit (« un crible ne prouve pas l'absence de perte » ; « une perte d'un monde sur vingt passe presque toujours inaperçue »). Aucune voie vers un signe positif : chaque issue est une information, et le verdict positif « épargne sans perte observée » ne peut sortir que si k_R est éprouvable (4 ≤ k_R ≤ n_c − 4).
3. **Cas dégénéré.** Défini et gelé : k_R < 4 (ou k_R > n_c − 4) ⇒ « non éprouvable » (étage 4) et « H-v non éprouvée au crible » quel que soit l'étage 3, dit en tête (point 7 de « En dix lignes »), dans « Ce que serait chaque issue » et dans la lecture de H-v. Le crible reste informatif sur l'ablation (H-v-a), rapportée sans verdict. Le bras à archive enrichie est écarté par la mère (R-2977, point 4 (a)) ; les deux sensibilités sans appel de plus (règle au rang ; rejeu de la décision sous archive fictive, fonction distincte, exécutée après la sortie principale) sont écrites avec leur garde. Je ne demande pas le bras enrichi (voir point pour la mère 4). **Distance dirigée** (carte vers K1, non le plus petit des deux sens) : **écart déclaré** avec sa raison (« Métrique », « Écarts »), biais connu du côté « épargne » (copies par morceaux), sensibilité « minimum des deux sens » ; acceptable tel quel.
4. **Devis, recompté.** 80 appels (4 × 20) ; plafonds du bloc gelé relus sur le texte scellé du pilote (candidat 6, `8aa33014…`, vérifié par `git show` sur la branche `prep/pilote-mr2-compte-organisme-v1` : 3 ; 2 ; 2,34 ; 2,34 USD ; bornes de sortie 64 000 ; 89 000 ; 36 000 ; 36 000) et parts du pilote de la procédure v14 (12 ; 8 ; 9,36 ; 9,36 : mêmes plafonds par session). Pires cas : 46,80 ; 40,00 ; 46,80 ; 60,00 ; machine 3,00 (17 h × 0,17 = 2,89) ; crédits 100,00 ; hors crédits 96,60 ; total 196,60 ; part sur crédits 50,86 %. Le plafond de 2,34 de Pr-1 et de Pr-3 tient bien au pire cas compté (0,53 d'entrée + 1,80 de sortie = 2,33). Attendus : 5,00 ; 16,00 ; 20,00 ; 32,00 ; machine 0,30 ; total 73,30 (48,00 + 25,30) ; fourchette 79,95 à 92,75 (39,60 à 49,20 + 40,35 à 43,55). Sonde neuve : 4,39 + 3,68 = 8,07 ; κv1 104,39 ; κv2 100,28 ; total 204,67. Entrées et sorties au pire (1,06 M par ligne ; 0,72 ; 1,78 ; 0,72 ; 1,28 M) : égales à 20 × (borne). **Tout est juste, sauf** : le compte de la configuration de Pr-1 (B7-03) et l'affirmation « dans l'enveloppe » (B7-01). Prix publics relus sur la note des prix v2 de la branche `lot/compte-organisme-v1` (empreinte `b88253b8…` égale) : 2/10 jusqu'au 30 novembre puis 4/20 pour Pr-1 ; 4/20 ; 10/50 ; 8/40 : conformes. Les deux comptes des dollars (prix public principal ; prix de la configuration en sensibilité et pour la part et la ligne de GO) sont dits.
5. **Cohérence avec GO-2026-11-15-06** (ligne l. 339 de `registres/go.md`, relue au commit `377a2a0c` : empreinte `4bcec4a0…` égale) : une ligne « calcul » par crible, sur devis refait et contre-lu, parts séparées, « essayés, non adoptés », échéance 30 novembre : la pièce s'y conforme. **Sauf l'affirmation « Dans l'enveloppe »** (B7-01).
6. **Durée.** La pièce donne une borne par appel B_a et un nombre de mondes à la fois M ∈ {1, 2}, un budget de pire cas ≤ 17 h chiffré dans une table (règle écrite d'avance, avec la case « non lançable » en clair), et dit nettement que **le lanceur du pilote est écrit pour 4 mondes et 16 appels, que le lanceur, la mesure, la lecture et la procédure de la machine sont du code neuf, et que la date de lancement en dépend** ; la configuration v12 est gardée (un plafond de 0,75 pour Pr-1 demanderait une configuration neuve : écarté). **Code neuf, pas de configuration neuve** : c'est ce qui fixe la date. Voir F-B7-2 pour le risque « non lançable ».
7. **R5 et graines.** Les 21 lignes de la liste d'arrêt ont chacune un essai sain et un artefact ; les actions de chaque ligne sont rangées à l'étage 0 ou nommées en exception (appel plus long que B_a, fournisseur abandonné, partie A). Graines : `numpy.random.SeedSequence` (≥ 1.25 ; 2.5.3 exigé sur la machine), racine = entier de l'empreinte du texte qui fera foi, clés `(r, 30)`, `(67, g, 30)`, `(99, b)`, `(97, k)`, `(98, w)` (entropie de l'audit : l'empreinte de `CARTES.json`) : sans collision ; le placebo sans graine (énumération exacte : C(20, 10) = 184 756 au pire).
8. **N-058.** Le crible est borné à la génération 1 sur {K1} ; la règle ne lit ni issue, ni oracle, ni verdict ; son évaluation se fait sur l'oracle et le coût ; la dépendance indirecte aux verdicts au-delà de la génération 1 est dite (« Écarts », « Choix et doutes » point 11) et renvoyée au mot de Lazar pour toute adoption. Tenu.
9. **Partie A.** Déclarée descriptive, sur des données déjà vues, sans critère ni verdict du juge ; interdit écrit sans exception, gardé par une ligne d'arrêt (champs `promue`, rejet, mort, retenues : refus) avec essai sain et artefact ; archive de la génération 2 = {K1} et toutes les cartes de la génération 1 (l'égalité avec les retenues de v67 est dite non vérifiée : elle vient du verdict de v67, § 3 V-2, V-7, V-8, que j'ai vérifié par `grep` dans le verdict, non dans le relevé). Je n'ai pas ouvert le relevé.
10. **R7 et R8.** Aucun chiffre de l'état de l'art ; antériorités « à chercher » listées (FrugalGPT, AutoMix, RouteLLM, FunSearch, AlphaEvolve, [CAT] C9 « Pay Only for Disagreement », CADS) avec leurs références « à vérifier » ; zone dite « séduisante, donc à vérifier plus durement ».
11. **Validateur.** `controle_ia.prereg.problemes(chemin)` rejoué par `PYTHONPATH=src .venv/bin/python` : **liste vide**. L'entrée « Contre-lecture 6 » porte les deux empreintes entières exigées (rapport `da47da2f…` ; brouillon 6 `08b430d7…` : vérifiées). Aucun identifiant de modèle (seulement deux clés de configuration de proposeurs, déclarées dans la pièce comme noms gelés par l'empreinte de la configuration, comme aux tours précédents).
12. **Empreintes citées, vérifiées par `sha256sum` ou `git show` :** 45 des 55 empreintes entières de la pièce retrouvées sur disque (notes, décisions, relevé des idées, catalogue, conceptions MR-2 v3 et v4, outils, devis du pilote, résumé v4, gabarit, validateur, modèles de forme, brouillons et rapports précédents, PDF cités) ; procédure v14 au commit `2d35cafa…` (`20355627…`), texte scellé du pilote (`8aa33014…`), note des prix (`b88253b8…`) et `registres/go.md` au commit `377a2a0c` (`4bcec4a0…`) par `git show` : égales. Les programmes `comptes_cribles_v2.py` (`f06bcfe7…`) et `compte_certifiees_mr2_v1.py` (`8c0432df…`) sont retrouvés **dans les blocs de code de `crible-iii-brouillon1.md`**, hachés à l'identique (la pièce le dit). **Non vérifiées par moi** : `21bc75f4…` (relevé de v67) et `a9f9594e…` (fiches), sous les chemins interdits ; les sorties `5d53092e…` et `319fa358…` des programmes de l'annexe A, qui ne sont pas dans le dépôt (voir F-B7-5).

## 3. Corrections exigées

Chaque « ancien » figure **une seule fois** dans le brouillon 7 (vérifié par programme) et ne contient aucun retour à la ligne. Aucune n'ouvre une porte après lecture du crible.

### Majeures

**B7-01 — « Dans l'enveloppe de GO-2026-11-15-06 » est affirmé à tort ; la sonde neuve n'est pas dite dans l'écart à la note.** La pièce écrit que le pire cas de 196,60 USD (+ 13,60 sur les 183,00 de la note) est « dans l'enveloppe ». La mère a écrit le contraire : « la somme des pires cas des cinq cribles fait 1 262 à 1 309 USD contre 1 275 ; chaque ligne « calcul » sera inscrite sur un devis refait […] et le cumul tenu sous 1 275 ; si le dernier crible n'y tient pas, nœud de Lazar » (R-2992, point 3). Et avec la sonde neuve exigée (point 8 de « Choix et doutes »), ce crible passe de 183,00 à 204,67 USD au pire : + 21,67, non + 13,60. La pièce ne dit ni l'un ni l'autre ; un lecteur de la ligne pourrait croire l'appartenance acquise. Deux couples.

`B7-01a`
```
ANCIEN: (décision R-2542) porte 2,34. Dans l'enveloppe de GO-2026-11-15-06.
NOUVEAU: (décision R-2542) porte 2,34 ; avec la sonde neuve exigée, le pire cas est de 204,67 USD, soit + 21,67 sur les 183,00 de [NOTE]. **Enveloppe de GO-2026-11-15-06 : appartenance non acquise** : R-2992 (point 3) donne la somme des pires cas des cinq cribles à 1 262 à 1 309 USD contre 1 275 ; la ligne « calcul » de ce crible ne s'inscrit que si le cumul des lignes inscrites reste sous 1 275 USD, sinon nœud de Lazar.
```

`B7-01b`
```
ANCIEN: ; à 20 mondes, au-dessus des 183 de [NOTE] parce que les plafonds de session de Pr-1 et Pr-3 sont
NOUVEAU: ; à 20 mondes, au-dessus des 183 de [NOTE] (+ 8,07 par la sonde neuve ; l'appartenance à l'enveloppe de GO-2026-11-15-06 reste à établir sur le cumul des cinq cribles, section « Devis ») ; l'écart de 13,60 entre 196,60 et 183 vient de ce que les plafonds de session de Pr-1 et Pr-3 sont
```

**B7-02 — « fournisseur », « abandonné » et « perdu en entier » ne sont définis nulle part.** Le minimum (« aucun fournisseur perdu en entier »), l'étage 1 (« un fournisseur perdu en entier » ⇒ « non concluant ») et la ligne d'arrêt « fournisseur abandonné alors que le minimum n'est plus possible » dépendent de ces trois mots. Le pilote les fixe ([PILOTE], liste d'arrêt, « Panne d'un relais » : « l'appel est « échec », aucune reprise, aucune bascule […] Un fournisseur en panne est abandonné : ses appels restants sont « échec » ; le pilote continue avec les autres »), la pièce ne les reprend pas : sans définition, le moment d'arrêter (et donc la dépense) et le verdict de l'étage 1 restent à l'appréciation après coup (R1). Il y a trois voies de relais, non quatre : celle de Pr-2 et de Pr-4 (crédits de Claude : une clé pour deux proposeurs, huit appels sur seize au pilote), celle de Pr-1, celle de Pr-3. Autre lacune : tant qu'un fournisseur « perdu en entier » n'arrête rien (la ligne d'arrêt ne tombe que si le minimum devient impossible, ce qui n'arrive pas si une seule voie manque), le crible dépenserait pour une issue déjà acquise à l'étage 1. Les deux couples ci-dessous reprennent la règle du pilote et arrêtent aussi quand un fournisseur est abandonné sans aucun appel répondu ; la fragilité de la règle du pilote (une panne passagère abandonne la voie) est un point pour la mère (n° 3).

`B7-02a`
```
ANCIEN: et aucun fournisseur perdu en entier ; sinon « non concluant »
NOUVEAU: et aucun fournisseur perdu en entier (fournisseur = voie de relais à clé commune, soit trois : celle de Pr-2 et Pr-4 (crédits de Claude), celle de Pr-1, celle de Pr-3 ; « perdu en entier » = aucun appel répondu parmi tous les appels du crible de ses proposeurs) ; sinon « non concluant »
```

`B7-02b`
```
ANCIEN: | fournisseur abandonné alors que le minimum de mondes complets (section « Seuil ») n'est plus possible |
NOUVEAU: | fournisseur abandonné (règle du pilote, [PILOTE], liste d'arrêt, « Panne d'un relais » : dès qu'un appel d'un fournisseur finit en panne de relais, c'est-à-dire en erreur de réseau, d'identification ou de quota, et non en réponse tronquée, carte refusée ou appel plus long que B_a, ses appels restants sont comptés « échec » sans être lancés, sans reprise ni bascule) alors que le minimum de mondes complets (section « Seuil ») n'est plus possible, ou alors qu'il est perdu en entier (aucun appel répondu : l'étage 1 est acquis) |
```

### Mineures

**B7-03 — Le compte de la configuration de Pr-1 n'est pas égal à cinq fois le prix public que la pièce écrit.** Le prix de la configuration de Pr-1 (10 / 50) est exactement cinq fois son prix public (2 / 10) ; la fourchette publique est 0,35 à 0,45 USD par appel et 7,00 à 9,00 pour 20 appels ; au compte de la configuration c'est donc 1,75 à 2,25 par appel et 35 à 45 pour 20 appels, non 34 à 42. Les totaux suivent : crédits 39,60 à 49,20 ; hors crédits 35 + 33,00 + 0,35 = 68,35 à 45 + 34,00 + 0,55 = 79,55 ; total 107,95 à 128,75, donc ≈ 108 à 129 (non 107 à 126) ; part sur crédits 39,60 / 107,95 = 36,7 % à 49,20 / 128,75 = 38,2 %, donc ≈ 37 à 38 % (non 37 à 39 %). Cinq couples.

`B7-03a`
```
ANCIEN: (code : 34 à 42)
NOUVEAU: (code : 35 à 45)
```

`B7-03b`
```
ANCIEN: ≈ 107 à 126 au compte de la configuration
NOUVEAU: ≈ 108 à 129 au compte de la configuration
```

`B7-03c`
```
ANCIEN: ≈ 37 à 39 % au compte de la configuration, ≈ 51 % du pire cas (100/196,60)
NOUVEAU: ≈ 37 à 38 % au compte de la configuration, ≈ 51 % du pire cas (100/196,60)
```

`B7-03d`
```
ANCIEN: (≈ 37 à 39 % au compte
NOUVEAU: (≈ 37 à 38 % au compte
```

`B7-03e`
```
ANCIEN: un appel de 30 000 jetons de sortie y vaut ≈ 1,7 à 2,1 USD
NOUVEAU: un appel y vaut cinq fois son prix public, soit ≈ 1,75 à 2,25 USD (0,35 à 0,45 × 5)
```

**B7-04 — « Presque sûrement atteint » est une affirmation sans base avant la lecture du taux du pilote.** La section « Taille » écrit que le minimum de 0,8 × N est « presque sûrement atteint dans les deux cas (à titre d'information, annexe) ». L'annexe A (point 11, sortie 4) donne P(n_c ≥ 16 sur 20) = 0,7481 à un taux d'appels répondus de 0,70, 0,9147 à 0,75, 0,9831 à 0,80, 0,9985 à 0,85 : « presque sûrement » n'y vaut qu'à partir de 0,85. Je l'ai recalculé : égal.

`B7-04`
```
ANCIEN: le minimum de 0,8 × N est presque sûrement atteint dans les deux cas (à titre d'information, annexe).
NOUVEAU: le minimum de 0,8 × N est atteint avec la probabilité que donne la grille de l'annexe A, point 11 (sortie 4), selon le taux d'appels répondus par appel : à N = 20, 0,75 à 0,70, 0,91 à 0,75, 0,98 à 0,80, 0,9985 à 0,85 (à lire sur le taux du pilote, à titre d'information).
```

**B7-05 — Mécanisme de gel de l'étape 2 : une phrase ambiguë et un gel sans référence d'empreinte.** (i) Dans l'étape 2, « la liste d'arrêt** (devis, prédictions, puissance), contre-lu, scellé » se lit comme si « (devis, prédictions, puissance) » qualifiait la liste d'arrêt gelée ; c'est le texte refait qui change ; et la liste d'arrêt est dite gelée alors que sa ligne « coût d'un appel » reçoit, par règle écrite d'avance, une tolérance possible : l'exception doit être nommée. (ii) Le gel « dès ce texte » (H-v, ε, ε_strat, 0,8, définition de copie, étages, seuils) n'a de force que si le texte qui fera foi renvoie à l'empreinte du texte gelé et liste ses écarts : sinon rien ne distingue un écart déclaré d'un écart après lecture de la partie A ou du pilote (R1 : aucune porte de sortie après lecture). Deux couples sans retour à la ligne.

`B7-05a`
```
ANCIEN: la liste d'arrêt** (devis,
NOUVEAU: la liste d'arrêt (hors la seule ligne « coût d'un appel », dans les limites de sa règle écrite d'avance)** ; le texte refait (devis,
```

`B7-05b`
```
ANCIEN: prédictions, puissance), contre-lu, scellé par `sceller_prereg`
NOUVEAU: prédictions, puissance) cite l'empreinte entière du présent texte tel que scellé comme pièce de travail et liste un à un ses écarts à lui, sans autre changement ; il est contre-lu, scellé par `sceller_prereg`
```

**B7-06 — Entrée « Contre-lecture 7 » à écrire par le rédacteur (couples propres, non fournis ici).** Après application, le rédacteur ajoute à la section « Contre-lecture » une entrée « Contre-lecture 7 » portant : le lecteur (modèle C, neuf), les heures de lecture (15:07:27Z à 15:20Z), l'empreinte **entière** de ce rapport (à lire dans son compagnon `.sha256` après scellement) et celle du brouillon 7 relu (`083a322de48bc12d1ac250d8687f304dcf876bfcfd557bd84e154d7321a232b1`), le verdict et les comptes (2 majeures, 4 mineures, 6 remarques facultatives) ; il met à jour le titre (brouillon 8), l'en-tête, le statut (« contre-lu sept fois ») et la tête de la section ; sans quoi `controle_ia.prereg.problemes` rend un défaut (deux empreintes entières exigées). Aucun couple ne la porte, la valeur de l'empreinte du rapport n'étant connue qu'après son scellement.

## 4. Remarques facultatives (non exigées)

- **F-B7-1 — V4 « sans zone de réfutation ».** Le gabarit demande, pour chaque prédiction, « ce qui compterait comme réfutation » ; V4 en a désormais aucune (décision de la mère R-2992 : étage 5 sans verdict). C'est cohérent avec N-045 point 3 ; il serait plus net d'écrire V4 comme une **mesure rapportée** plutôt que comme une prédiction. La mère peut laisser.
- **F-B7-2 — Risque « non lançable » plus probable que la pièce ne le laisse voir.** Avec les durées que l'annexe A, point 12, suppose (mise en place 0,5 h ; génération 1,0 h ; mesure 1 h ; rapatriement 0,5 h ; barrières 100 minutes) **et le facteur trois de la règle sur chacune** : budget fixe ≈ 9 h + 1,67 h = 10,67 h, il reste 6,33 h pour les appels ; à M = 2, ⌈20/2⌉ × B_a ≤ 22 800 s donne B_a ≤ 2 280 s, donc 2 100 s en multiple de 300 s ; à M = 1, 900 s. Comme B_a ≥ 1,5 fois le plus long appel répondu du pilote, la règle ne tient que si ce plus long appel est inférieur ou égal à 1 400 s (v67 : 861 s et 1 099 s) et exige M = 2 ; au-delà, « non lançable » et mot de la mère. Ces durées ne sont pas mesurées (calcul à la main sur une hypothèse) ; la pièce l'écrit déjà en général (« non lançable », mot de la mère). Le point (8) des « Points à remesurer » permet de la lever.
- **F-B7-3 — Avoir pour archive « toutes les cartes de la génération précédente » règlerait la tension avec N-058.** La partie A construit déjà l'archive de la génération 2 sans les verdicts ; si la règle de production prenait la même archive, elle ne dépendrait d'aucun verdict. Ce n'est pas l'objet du crible (nœud d'adoption), mais cela mérite une ligne dans « Écarts ».
- **F-B7-4 — Pas de règle de lancer ou ne pas lancer selon la probabilité d'atteindre le minimum.** Le taux du pilote sert « à titre d'information » ; si la probabilité d'atteindre n_c ≥ 16 est basse (0,75 à un taux de 0,70), rien n'est écrit sur ce que la mère fait : à elle.
- **F-B7-5 — Sorties de l'annexe A hors du dépôt.** Les programmes de l'annexe A sont dans les blocs de code de `crible-iii-brouillon1.md` (empreintes égales) ; leurs sorties (`5d53092e…`, `319fa358…`) ne sont pas des fichiers du dépôt, seulement recopiées dans la pièce. Le texte qui fera foi gagnerait à déposer les deux programmes et leurs sorties sous `cribles-v1/` avec empreinte compagnon (R6) avant que le brouillon (iii) soit remplacé.
- **F-B7-6 — Reprises du tour précédent, non exigées :** seuil sur k_R quand n_c vaut 16 à 19 (F-B5-3) ; risque d'arrêt de Pr-1 non chiffré (F-D6-3) ; « la règle suivante » désigne deux règles dans la phrase du budget de durée (F-D6-2) ; V1, V3, V5 en comptes absolus.

## 5. Points pour la mère

1. **Sceller telle quelle : non.** Deux majeures et quatre mineures d'écriture ; les corrections touchent des textes gelés (enveloppe, définitions de fournisseur, étape 2) : un tour limité aux endroits touchés suffirait ensuite (différentiel par `diff` des couples et lecture des seuls passages touchés, plus la vérification de l'entrée « Contre-lecture 7 »). Rédacteur du modèle A (R-2982, R-2992 point 0).
2. **Enveloppe.** Ce crible est à **204,67 USD au pire avec la sonde neuve** (note : 183,00), 196,60 sans. Le cumul des cinq doit être refait avant d'inscrire la moindre ligne ; si le total dépasse 1 275, nœud de Lazar (R-2992 point 3). La pièce ne le dit pas encore (B7-01).
3. **Règle de l'abandon d'un fournisseur (B7-02).** Je reprends celle du pilote (une panne de relais abandonne la voie, sans reprise ni bascule). Avantage : même règle que le pilote, écrite d'avance, aucune marge après coup ; inconvénient : une panne passagère sur une voie, dès le premier monde, termine le crible à l'étage 1 (« non concluant ») avec une dépense faible, et l'abandon d'une voie qui sert deux proposeurs (Pr-2 et Pr-4) est lourd. Si la mère préfère une règle plus tolérante (par exemple une seule reprise), c'est un mot d'elle avant le scellement ; je ne l'ai pas inventée.
4. **Ce que le crible rendra.** D'après les propres confiances de l'auteur (V1 : 0,65 ; V5 : 0,6), la règle ne sera « éprouvable » qu'avec une probabilité d'environ un tiers ; sinon le crible, à 204,67 USD au pire, informera surtout sur l'ablation (H-v-a), rapportée sans verdict (R-2992). Le bras à archive enrichie reste écarté (R-2977) ; les deux sensibilités sans appel de plus (règle au rang, archive fictive) sont les seules lectures de la règle quand k_R est dégénéré. À savoir avant d'inscrire la ligne ; pas de correction.
5. **Date de lancement.** Fixée par le code neuf (lanceur à N mondes, M mondes à la fois, borne par appel, mesure, lecture, procédure de la machine, essais, banc de mutations, contre-lecture du code, addendum d'empreintes), non par la configuration (v12 gardée) ni par le préenregistrement ; le visé du 21 au 24 novembre (R-2992 point 5) tient dans la fenêtre du GO (30 novembre) si le budget de durée est lançable (F-B7-2) ; le prix public de Pr-1 double le 1er décembre.
6. **Mots à fixer après le pilote** (écrits d'avance dans la pièce, sans choix ouvert) : B_a (le plus petit multiple de 300 s au moins égal à 1,5 fois le plus long appel répondu, au plus 3 600 s), M ∈ {1, 2}, X de la tolérance de Pr-1 (seulement si un rapport coût compté / plafond dépasse 1 au pilote), V1 et V6 (après lecture du seul témoin positif), montants attendus (règle (b) du devis refait) ; le lecteur du pilote ne doit rendre que les comptes d'appels répondus, tronqués et en échec, les durées (dont les trois durées du point (8)), les coûts et le seul champ du témoin positif.
7. **Entrée « Contre-lecture 7 »** (B7-06) : à écrire après scellement de ce rapport.

## Incidents de ma main

- **Ligne de registre vue sans l'avoir cherchée.** Mon `grep` de `registres/decisions.md` sur « R-2977|R-2992 » n'a rien montré du pilote ; mais un second `grep` de vérification de l'existence des identifiants R-2981 et R-2982 a affiché la ligne R-2981 (début), où figurent des « comptes de marche » du journal de la machine du pilote (« 14 … complets, 0 échec, 2 tronqués, aucun abandon ») : c'est un taux de réussite des appels, que la consigne me demandait de ne pas lire. **Je ne l'ai utilisé nulle part dans ce rapport** (aucun chiffre ne repose sur lui ; mes calculs de probabilité d'atteindre le minimum restent sur la grille de l'annexe A). Aucun fichier de la sortie du pilote (`retour`, branche de sortie) n'a été ouvert. À la mère de décider si le lecteur neuf du pilote doit en être informé.
- `git fetch` par refspec de la seule branche `lot/compte-organisme-v1` (met à jour sa référence distante locale) ; `git show` de la procédure v14 (commit `2d35cafa…`), du texte scellé du pilote (branche `prep/pilote-mr2-compte-organisme-v1`, déjà référencée localement), de la note des prix et de `registres/go.md` au commit `377a2a0c` ; aucun clone.
- Fichiers jetables écrits dans le bloc-notes de ma session (copies de la procédure v14 et du texte du pilote tirées par `git show`, un petit programme de recherche de blocs de code) ; aucun fichier existant modifié ; un `find` sur le disque a listé (sans l'ouvrir) un dossier `outils-cribles/` du bloc-notes contenant `comptes_cribles_v2.py` : non touché.
- Calculs : comptes de sous-chaînes, empreintes, probabilités binomiales, bornes de Clopper-Pearson par `python3 -I` (bibliothèque standard), validateur `controle_ia.prereg.problemes` (lecture seule). Aucun `pytest`, aucun calcul lourd, aucun appel de modèle, aucune dépense, aucune machine.

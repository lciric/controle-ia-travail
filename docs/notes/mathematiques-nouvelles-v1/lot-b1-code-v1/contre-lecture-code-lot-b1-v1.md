# Contre-lecture du code du lot B1 du pilote « oracles plantés » — v1

- Nature : contre-lecture de classe B (R2), par un Opus 5.5 neuf qui n'a pas écrit le code. Le 2026-11-22. Branche `claude/mathematiques-nouvelles-v1`, commit `9300251a`. Processeur seul, 0 USD, aucun appel de modèle, aucun réseau.
- Lu : `CLAUDE.md` ; le mandat `mandat-code-lot-b1-v1.md` ; dans le brouillon 1 du préenregistrement les sections « Métrique », « Plan d'analyse », « Liste d'arrêt », « Mondes plantés et tests de mort » et « Bases à battre » ; tout `src/controle_ia/oracles_plantes_v1/` ; les quatre fichiers `tests/test_oracles_plantes_v1_*.py` ; la note de choix et le rapport des essais R5. Aucun fichier cloisonné n'a été ouvert.
- Lancé : `PYTHONPATH=src .venv/bin/python -m pytest -q tests/test_oracles_plantes_v1_*.py` : 122 passés. Sondes de mutation dans le bloc-notes, hors de l'arbre (sonde1 à sonde5) ; aucun fichier du dépôt modifié, sauf ce rapport.
- Bilan : **12 remarques — 2 bloquantes, 5 à corriger, 5 mineures.**

## Ce qui tient (vérifié)

- Les 24 vérités plantées : chaque raison écrite est juste. Contrôlé à la main gabarit par gabarit : Cassini par le déterminant de la matrice compagnon, somme télescopée recalculée, période pure parce que pgcd(QU, M) = 1, addition et duplication, divisibilité de Lucas, croissance, forme close de la suite affine, Scheffé dans ses deux sens, monotonie de la variation totale, sous-additivité, couplage produit, Le Cam, queue binomiale, Fréchet pour l'union et l'intersection, Markov, espérance, Bernoulli, encadrement par l'indépendance. Puis par calcul exact au-delà de 3N, en levant les plafonds (variation totale jusqu'à 3N + 2 pour F1, 10N pour F2, 6N pour F3), sur les racines 11 et 3 : aucune instance fausse ni indéfinie. Les seules issues « hors capacité » viennent de la divisibilité (indice k·n > 450).
- Pièges : la certification ne garde un piège que s'il est vrai-borné jusqu'à N (aucune instance hors capacité) et que son premier contre-exemple, cherché jusqu'à 3N, a sa plus grande variable dans ]N .. 3N]. Ce contre-exemple est revérifié par le chemin de T6.
- Calcul exact : la programmation linéaire de F2 parcourt toutes les bases du polytope, en rationnels (la matrice est de rang M + 1, donc les sommets sont tous atteints), et elle est recoupée par Fréchet. Aucun flottant dans l'évaluateur. Les décimaux sont lus par `Fraction` à partir du texte.
- Graines : `SeedSequence(racine, spawn_key=…)`, chemins contrôlés. Aucun tirage hors de l'arbre dans le code de production. Aucune itération sur un ensemble de chaînes qui dépende du hachage dans un résultat.

## Remarques

### 1. Un énoncé conforme à T1 fait lever un arrêt dans la batterie — **bloquante**
- Lieu : `grammaire.py:217-229` (atome entre parenthèses analysé alors que `en_tete` vaut encore vrai) et `grammaire.py:187` ; l'arrêt est levé à `evaluation.py:191-192`.
- Preuve (sonde1, monde F3 de la racine 11) : `(pour tout n dans NAT, u(n) >= 0) et vrai`, `(… ) implique faux` et `(… ) ou faux` passent T1 comme « conforme ». Ensuite `appliquer_batterie` lève `GardeArret: NAT hors du préfixe de tête : l'analyseur aurait dû refuser`. Dans une course, une sortie de proposeur arrêterait le bac, au lieu d'être rangée « informe » (A12) ou évaluée.
- Correction : après l'analyse, vérifier sur l'arbre que chaque quantificateur sur NAT appartient au préfixe universel de tête (`prefixe(arbre)`), sinon lever `FormeInvalide`. Ajouter les trois textes ci-dessus aux artefacts de T1.

### 2. Le normaliseur efface l'indéfini : la lignée tue par héritage des énoncés vrais, une vérité plantée comprise — **bloquante**
- Lieu : `normalisation.py:69-81`, `:172-176` et `:192-196` (produit par le polynôme nul, a − a, puissance 0 sur un atome) ; règles du monde `famille_f1.py:197-208` (comp hors de PARTIES) ; héritage à `tests_de_mort.py:425-430`.
- Preuve (sonde1, racine 11, registre neuf) :
  - `pour tout n dans NAT, u(n + 1)^2 - u(n) * u(n + 2) + w(n - 1) - w(n - 1) = (-12) * (-QU)^n` meurt par T2 (indéfini en n = 0). Sa forme normale est celle de la vérité de Cassini. La vérité de Cassini, soumise ensuite, sort « morte par héritage ».
  - De même, `… u(n) + 0 * w(n - 1) > 0` fait mourir `pour tout n dans NAT, u(n) > 0`.
  - Et `pour tout n dans NAT, w(n - 1) * 0 = 0` (sonde5) meurt avec la forme normale « V » : toute proposition que le normaliseur clôt ensuite à vrai mourrait par héritage, au lieu d'être triviale.
  - Comme le registre est global (note de choix, ligne 32), un proposeur peut ainsi faire mourir pour les autres configurations une vérité qu'il n'a jamais retrouvée. Cela fausse « retrouvées » (H1, H2) et les motifs de mort.
- Raison : sous la convention « indéfini = contre-exemple » (note, ligne 18), deux énoncés de même forme normale ne sont pas équivalents dès qu'un sous-terme indéfini a été simplifié. L'héritage de D-M5 suppose pourtant une équivalence.
- Correction : garder dans la forme normale l'ensemble des atomes rencontrés avant simplification (applications de fonctions, divisions, puissances), par exemple un suffixe « déf{…} » dans `chaine`. Ou bien n'hériter que des morts dont l'énoncé source n'a perdu aucun atome à la normalisation. Ajouter les trois cas ci-dessus en artefacts de la lignée, et vérifier que T4 a ne clôt plus à « vrai » un énoncé qui a perdu un atome.

### 3. L'étage « profil » de T5 compte « hors capacité » comme un statut informatif : deux vérités distinctes sont déclarées redites — à corriger
- Lieu : `tests_de_mort.py:319-322`.
- Preuve (sonde3, racine 11, F3, N = 15) : `pour tout n dans NAT, n >= 1 implique mod(w(30 * n), w(n)) = 0` et `… mod(w(30 * n), w(3 * n)) = 0` sont toutes deux vivantes, vraies-bornées et non triviales ; la seconde est strictement plus forte. T5 rend pourtant « redite : même profil de vérité ». Les deux profils valent V jusqu'à 15 et H au-delà (indice > 450), dans les quatre mondes. Le seuil d'informativité (au moins deux statuts) est satisfait par {V, H}.
- Correction : exiger, pour qu'un profil soit informatif, au moins un statut F ou I et au moins un statut V, sans compter H. Ou exclure toute instance H des deux profils comparés. Cela s'ajoute à la question déjà posée au concepteur (note, ligne 29) : le préenregistrement dit « table de vérité sur le domaine borné », soit jusqu'à N dans le monde ; le code compare jusqu'à 3N et dans trois mondes perturbés, ce qui est un écart à faire trancher.

### 4. Le registre de lignée ne détecte ni la troncature ni la modification de sa dernière ligne — à corriger
- Lieu : `lignee.py:33-42` (aucune tête de chaîne ancrée) ; essai `test_lignee_chaine_alteree_refusee` (n'altère que la ligne du milieu).
- Preuve (sonde3) : on inscrit « vivante » puis « morte » pour une même empreinte, et on retire la dernière ligne : `rejouer` rend « vivante » sans arrêt. Si l'on remplace seulement « morte » par « vivante » dans la dernière ligne : même résultat. La mort est effacée, ce qui est contraire à D-M5 (« une proposition morte reste morte »).
- Correction : sceller la tête à chaque ajout (compagnon `.sha256` de l'empreinte de la dernière ligne et du nombre de lignes) et la vérifier au chargement. Ou consigner la tête dans le manifeste de la course. Ajouter des artefacts « troncature » et « dernière ligne modifiée ».

### 5. Un flottant dans les paramètres est converti en silence (troncature par `int`) — à corriger
- Lieu : `famille_f2.py:96-97`, `famille_f1.py:40-43`, `famille_f3.py:31-34` ; lecture `parametres.py:19` (`json.loads` sans `parse_float`).
- Preuve (sonde4) : `MondeF2` construit avec `a = [1.5, 2]` donne alpha = [1/20, 1/10], tronqué sans arrêt. Pour F3, `AV_choix = [1.5]` donne AV = 3/2 sans arrêt ; une valeur 0.1 donnerait 3602879701896397/36028797018963968. Le fichier JSON sera rempli par le brouillon 2 : une valeur décimale écrite en nombre JSON passerait. L'essai `test_flottant_refuse_dans_un_parametre_du_monde` n'injecte le flottant qu'après la construction : il ne touche pas ce chemin.
- Correction : lire les paramètres avec `parse_float` qui lève `GardeArret`. Dans les constructeurs, remplacer `int(x)` et `Fraction(x)` par un contrôle strict (entier non booléen, ou texte rationnel lu par `frac_depuis_texte`). Ajouter un artefact sur ce chemin.

### 6. Le contrôle de fuite ne voit pas une instance écrite dans les octets servis — à corriger
- Lieu : `cles.py:28-29` contre `cles.py:21-22`.
- Preuve (sonde3) : le fragment cherché est `json.dumps(instance, sort_keys=True)`, soit `{"n": 17}`, alors que les fichiers servis sont écrits avec `indent=1` (`{\n "n": 17\n}`). Une instance glissée dans une définition servie ou dans la sous-banque servie n'est donc jamais détectée. Le contrôle des instances, y compris celui du rejeu (`rejeu.py:116`), est vide.
- Correction : chercher aussi la forme indentée et la forme compacte. Mieux : parcourir l'objet servi et refuser toute valeur d'instance (couple variable et valeur) de la clé. Ajouter un artefact « instance de piège glissée dans la sous-banque servie ».

### 7. Les pièges se reconnaissent à leur forme : la strate se lit dans le texte servi à S et N — à corriger (question au concepteur)
- Lieu : `mondes.py:117-133` ; gabarits des pièges `famille_f1.py:253-264`, `famille_f2.py:234-241`, `famille_f3.py:205-233` ; `sous_banque.py:52`.
- Raison : tout piège est de la forme « pour tout t dans NAT, E(t) < littéral », ou « mod(…, p) != r » à grand premier littéral. Aucune vérité ni aucun faux tôt n'a cette forme. Un bras qui répond « faux » à toute borne littérale sur une suite croissante atteint un rappel de 100 % sur la strate des pièges, sans rien calculer. Cela gonfle r_S et r_N et brouille Δ (H3). Le préenregistrement dit pourtant « sans classe ».
- Correction (à trancher par Fable) : planter aussi des vérités et des faux tôt en forme de seuil (borne littérale vraie au-delà de 3N par une raison générale, par exemple vt(t) < 1 ou u(n) > 0 ; seuil dépassé avant N), pour que la forme ne révèle pas la strate. Ou mesurer et rapporter une base « forme seule ».

### 8. Le chemin « contradiction avec les définitions » de T2 n'est pas exercé par son essai — mineure
- Lieu : `tests/test_oracles_plantes_v1_tests_de_mort.py:69-73` ; `tests_de_mort.py:99-100`.
- Preuve (sonde5) : l'énoncé de l'essai meurt par `MORTE_CONTRE_EXEMPLE` en n = 0 ; l'assertion `tue()` passe sans atteindre la branche `noeud == FAUX`. Cette branche n'est atteinte que par un énoncé hors capacité, comme `u(1000) - u(1000) = 1`. Le rapport R5 la donne pourtant pour éprouvée.
- Correction : asserter `type == MORTE_CONTRADICTION` sur un cas qui l'atteint, et corriger la ligne du rapport.

### 9. Une mort par T6 n'est jamais inscrite d'office au registre — mineure
- Lieu : `tests_de_mort.py:380-396`.
- Raison : `t6_verifier` rend l'issue mais n'inscrit rien. L'essai `test_lignee_mort_par_t6_heritee` inscrit la mort à la main. Le script de course (lot B3) pourrait l'oublier, et un piège tué par S resterait vivant pour la lignée.
- Correction : une fonction `appliquer_t6(…, registre)` qui inscrit la mort, et un essai qui passe par elle.

### 10. L'héritage ne couvre que l'égalité d'empreinte : une reformulation entière d'un piège tué par T6 reste vivante — mineure
- Lieu : `tests_de_mort.py:425`.
- Raison : un piège « u(n) < c » tué par S en n₀ > N. La reformulation « u(n) <= c − 1 » a une autre forme normale (le normaliseur n'applique aucune équivalence propre aux entiers) et T2, borné à N, la laisse vivre. C'est conforme à la lettre du préenregistrement (« par empreinte normalisée »), mais pas à « toute reformulation équivalente » (D-M5).
- Correction : avant de déclarer vivante une proposition, la comparer aux mortes par les étages 2 et 3 de T5. Sinon, inscrire la limite en réserve.

### 11. Le rejeu contrôle mal la non-trivialité des vérités et le statut des pièges — mineure
- Lieu : `rejeu.py:58-63`.
- Raison : P8 dans le rejeu n'exige pas qu'une vérité soit non triviale, ni qu'un piège soit vrai-borné et non trivial. Un piège devenu « non décidé » ou trivial (par exemple après un changement de paramètres) passerait A1. La plantation le contrôle, mais le rejeu sert de contrôle indépendant.
- Correction : ajouter `r.triviale` pour les vérités, et `not r.vraie_bornee or r.triviale` pour les pièges, aux écarts.

### 12. L'enfant [9] et le profil de redite : deux écarts au préenregistrement, à inscrire — mineure
- Lieu : `graines.py:17` ; `tests_de_mort.py:298-303`.
- Raison : déjà relevés par l'exécutant (note, lignes 29 et 36). Rappelés ici parce qu'ils touchent la mesure (remarque 3) et R9. À trancher au brouillon 2 avant le scellement, pas en silence.

## Pour la vérification des corrections

Les sondes 1, 3, 4 et 5 du bloc-notes du contre-lecteur rejouent chaque preuve ci-dessus. Les corrections 1 à 6 et 8 devraient chacune venir avec un artefact R5 qui échouait avant la correction.

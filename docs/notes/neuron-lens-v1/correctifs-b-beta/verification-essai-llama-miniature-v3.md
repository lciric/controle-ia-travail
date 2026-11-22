# Vérification de l'essai de l'estimateur sur un Llama miniature, version 3

- Pièce vérifiée : `essai-transport-llama-miniature-v3.py`, empreinte recalculée
  `da0f0efc9f8da1e6fa43deba54959337726ecc1ce250de03bcad0099b085773d` — **égale à l'empreinte attendue** et au compagnon `.sha256`.
- Pièces lues à l'appui : `essai-transport-llama-miniature-v2.py` (`8147b431…`), `note-essais-b-beta-v3.md` (`1edcac9f…`),
  `verification-correctif-4-et-essais-v2.md` (`4ed8e71c…`) ; dans le voisin, au commit `849bfe1678e28becceb1e3864afe5fc8297d02e4`,
  lus sans rien exécuter ni importer : `tests/test_transport.py`, `neuron_lens/transport.py` (signatures).
- Date : mercredi 18 novembre 2026, 04:49 UTC (`date -u`).
- Auteur : vérificateur neuf (R2), qui n'a écrit ni relu aucune pièce de ce travail.
- Moyens : lecture, `diff`, et un calcul hors du voisin avec `/home/user/tf518/bin/python` (`transformers` 5.18.0, `torch` 2.15.0,
  processeur), où seules les fonctions de construction des modèles et de force brute de la pièce ont été recopiées ; `neuron_lens`
  n'a jamais été importé (contrôlé par `'neuron_lens' not in sys.modules`). Rien sous `registres/` ni `diag/` n'a été lu.

## Verdict

**Employable.** 0 bloquant, 0 majeur, 5 mineurs. La majeure de la vérification précédente (critère de la seconde partie) et sa
mineure (décalage posé sur les trois familles à la fois) sont levées. Réserve inchangée : l'essai n'a jamais été joué avec le code
du voisin ; son passage sur la machine reste à constater.

## Ce qui a été vérifié

### (1) Étendue du changement entre la version 2 et la version 3 — conforme
`diff` ne montre que : la description (lignes 4-5, 9-13, 17, 19-20), la fonction `ecarts` devenue `echecs` (lignes 151-187), les
quatre assertions des tests sains et les deux tests d'artefact (lignes 192, 197, 208-215). Les lignes 24 à 148 (première partie,
`LLAMA31_ROPE`, `llama31_model`) et `test_frequences_mises_a_l_echelle` sont identiques dans les deux versions.

### (2) La fonction `echecs` contre `test_estimates_match_brute_force` — conforme
Comparaison ligne à ligne avec les lignes 77 à 102 du test du voisin :

| élément | test du voisin | `echecs` | égal |
|---|---|---|---|
| accumulateurs | `{"out": N-1, "mid": N}` puis `{"mid": N, "out": N}`, `dim_batch=7`, moitié 0 | les mêmes | oui |
| estimations calculées hors des règles, force brute sous `relp_rules(model)` | oui | oui | oui |
| famille R `out` | couches `0..N-2`, `exact_from(…, outs[N-1][0, valid].sum(0))`, `J[:, valid].mean(1)` | la même | oui |
| famille R `mid` | couches `0..N-1`, `final_from_mid`, `J[:, valid].mean(1)` | la même | oui |
| famille S | couches `0..N-1`, `mid` puis `out`, `exact(…, [layer][0, valid].mean(0))`, `K[:, valid].sum(1)` | la même | oui |
| ordre | R `out`, R `mid`, S | le même | oui |
| critère | `torch.allclose(estimation, force brute, atol=1e-4)` | `torch.allclose(estimation + d[famille], force brute, atol=1e-4)` | oui |

La tolérance relative est laissée à son défaut (10⁻⁵), et la force brute est bien le second argument, celui que `allclose` prend pour
référence du terme relatif. Contrôle : avec une référence de 14, un écart de 2,3·10⁻⁴ passe et un écart de 2,5·10⁻⁴ échoue
(seuil 10⁻⁴ + 10⁻⁵ × 14 = 2,4·10⁻⁴).

Le décalage : `d = {fam: (1e-3 if fam == shift else 0.0) …}` ; `d["out"]`, `d["mid"]`, `d["S"]` sont ajoutés chacun dans sa seule
boucle. Sans famille demandée, les trois valent 0,0 et l'addition ne change rien à l'estimation. Une famille demandée ne décale que
ses propres comparaisons.

Écarts au test, tous hors des comparaisons : les jetons sont tirés après `torch.manual_seed(2)` (le test les tire dans l'état laissé
par la graine 1 et le tirage des normes) ; le modèle des estimations peut différer du modèle de la force brute (`estimate_model`) ;
la fonction rend la liste des échecs au lieu de s'arrêter au premier.

### (3) Tests sains, artefacts, compte

**Tests sains.** `echecs(...) == []` exige qu'aucune des 11 comparaisons (2 + 3 + 6) n'échoue : équivalent aux 11 `assert` du test.

**Décalage de 10⁻³, famille par famille — l'échec est garanti.** Raisonnement, élément par élément, avec e l'estimation, b la force
brute et seuil(b) = 10⁻⁴ + 10⁻⁵·|b| :
- si la famille passe sans décalage, |e − b| ≤ seuil(b) pour tout élément ;
- alors |e + 10⁻³ − b| ≥ 10⁻³ − seuil(b) ;
- l'élément échoue dès que 10⁻³ − seuil(b) > seuil(b), soit 8·10⁻⁴ > 2·10⁻⁵·|b|, soit **|b| < 40**.

Il suffit donc d'un seul élément de valeur absolue inférieure à 40 dans une seule comparaison de la famille. Avec des jacobiens qui
montent vers 14, **tous** les éléments de **toutes** les comparaisons de la famille échouent, avec une marge d'au moins
8·10⁻⁴ − 2·10⁻⁵ × 14 = 5,2·10⁻⁴. L'arrondi en précision simple de l'addition (de l'ordre de 10⁻⁶ pour ces grandeurs) est sans effet.
Contrôle hors du voisin (vraie dérivée, sans les règles du voisin, jetons de la graine 2) : plus grande valeur absolue des matrices
comparées, variante réaliste, 8 positions : 1,27 (R `out`), 2,09 (R `mid`), 4,78 (S) ; les 256 éléments de chaque matrice sont sous
40 ; pour une estimation placée au bord de la tolérance dans le sens le plus défavorable, le décalage dépasse encore le seuil de
8,0·10⁻⁴.

**« Dans sa seule famille ».** `assert fautes and {f for f, _ in fautes} == {famille}` exige au moins un échec et aucun échec hors
de la famille décalée. Les trois cas pris ensemble établissent aussi que chaque famille passe sans décalage sur ce modèle et ces
jetons (elle est non décalée dans les deux autres cas) : la prémisse du raisonnement ci-dessus est donc tenue dès que les trois cas
passent. Une famille que `echecs` sauterait ferait échouer son cas (liste vide) : la mineure de la vérification précédente est levée.

**Artefact « autre modèle ».** Force brute sur la variante réaliste (4 têtes de requête, 2 têtes de clés et valeurs, normes tirées
entre 0,3 et 2) ; estimations sur `tiny_model(initializer_range=0.2)` (2 têtes, 1 tête de clés et valeurs, normes à 1). Mêmes
dimensions de résidu, même vocabulaire : les formes s'accordent, la comparaison se joue. Contrôle hors du voisin (vraies dérivées
des deux modèles, mêmes jetons) : les 11 comparaisons échoueraient, plus grand écart par comparaison entre 0,55 et 4,85, soit plus
de trois ordres de grandeur au-dessus du seuil. L'échec n'est pas garanti par un raisonnement, mais il est acquis en pratique.

**Compte.** 2 (test recopié, 7 et 8 positions) + 2 (`test_base_miniature`) + 2 (`test_traits_de_llama31`) + 1 (fréquences) +
3 (décalages) + 1 (autre modèle) = **11**. Égal à la description (« 4 artefacts ») et à la note.

### (4) Première partie contre `tests/test_transport.py` — conforme
`diff` des lignes 24 à 129 de la pièce contre les lignes 2 à 102 du test du voisin : cinq lignes d'ajout du chemin d'import
(`os`, `sys`, `Path`, `sys.path.insert`), l'import `LlamaConfig, LlamaModel` au lieu de `Qwen3Config, Qwen3Model`, les deux
annotations de retour, le constructeur, et le commentaire sur les normes (Llama n'a pas de normes de requête ni de clé). Rien
d'autre : mêmes dimensions, mêmes graines, mêmes cibles, mêmes tolérances. Le filtre `name.endswith("norm.weight")` prend bien, sur
Llama, les normes d'entrée, d'après attention et finale. La première ligne de la description est adaptée (Qwen3 devient Llama).

### (5) Affirmations de la note v3

| affirmation | constat |
|---|---|
| empreinte `da0f0efc…` de la version 3 | exacte |
| vérification précédente : « 0 bloquant, 1 majeur, 9 mineurs », empreinte `4ed8e71c…` | exact (ligne 45 de cette vérification ; empreinte recalculée) |
| critère exact du dépôt, tolérance relative par défaut 10⁻⁵ | exact |
| « aucune tolérance changée », vrai pour la version 3 | exact : première partie inchangée, seconde au critère du test |
| décalage joué famille par famille, échecs exigés dans la seule famille ; « autre modèle » gardé | exact |
| 11 tests : 2, 2, 2, 1, 3, 1 | exact |
| `transformers` 5.18.0 : la configuration aux traits de Llama 3.1 se construit | exact, refait ici (`rms_norm_eps` 10⁻⁵, projection de requête 16×16, de clé 4×16) |
| fréquence basse de 1,414·10⁻³ à 5,248·10⁻⁴ | exact, refait ici : `[1,0 ; 5,2485·10⁻⁴]` contre `[1,0 ; 1,4142·10⁻³]` ; le test des fréquences passera |
| même constat avec 5.23.0 | non refait (voir « non vérifiable ») |

## Points

| n° | rang | objet | constat | remède proposé |
|---|---|---|---|---|
| 1 | mineure | seconde partie | Le cas sain de la variante réaliste par `echecs` (jetons de la graine 2) n'a pas de test à lui ; il n'est établi que par les trois cas de décalage pris ensemble. Si une famille échouait sans décalage, ce sont deux tests d'artefact qui tomberaient, ce qui se lit mal. Rien de muet : l'échec reste visible. | Ajouter `assert echecs(realistic_model(), 8) == []`, ou le dire dans la description. |
| 2 | mineure | artefact « autre modèle » | Le test n'exige qu'un échec quelconque, non un échec dans chacune des trois familles ; il passerait aussi sur une faute sans rapport avec le modèle. Couvert en pratique par les cas sains et par les trois décalages. | Exiger `{f for f, _ in fautes} == {"out", "mid", "S"}`. |
| 3 | mineure | description de `echecs` | « mêmes cibles, formules et ordre » est exact, mais le tirage des jetons diffère du test (graine 2 posée dans la fonction) et n'est pas dit. Sans effet sur le critère. | Une phrase dans la description. |
| 4 | mineure | ligne 132 | Le commentaire de séparation dit encore « Seconde partie, ajoutée (v2) ». | « (v2, critère revu en v3) » à la prochaine version, sans en créer une pour cela. |
| 5 | mineure | note v3 | L'essai n'a jamais été joué avec le code du voisin : « 11 tests passent » est un attendu, ce que la description dit (« Attendu ») ; la note le dit aussi, mais écrit « tous passés » pour l'essai de `lens_compare` sans dire où ni par qui. Hors de la pièce vérifiée. | Citer la sortie et son empreinte quand la commande aura joué les essais. |

Aucun de ces points n'empêche l'emploi de la pièce.

## Non vérifiable

- **Le passage réel des 11 tests** : il exige `neuron_lens` (règles, `r_lens_doc`, `s_lens_doc`), qui ne s'exécute ni ne s'importe
  ici. En particulier, que les estimations du voisin tiennent le critère du dépôt sur Llama — variante de base, variante réaliste,
  variante aux traits de Llama 3.1 — ne peut se constater que sur la machine.
- **Les grandeurs des jacobiens sous les règles du voisin** : mes valeurs (au plus 4,8 pour la variante réaliste, 4,3 pour la
  variante aux traits de Llama 3.1) et celle de la vérification précédente (vers 14) viennent de la vraie dérivée. La garantie du
  décalage tient tant qu'un élément au moins reste sous 40 en valeur absolue, ce qui laisse une marge large, mais la borne elle-même
  n'est pas mesurée sous les règles.
- **L'artefact « autre modèle » sous les règles du voisin** : écarts mesurés ici sur les vraies dérivées seulement.
- **Le constat de la note avec `transformers` 5.23.0** : seul l'environnement en 5.18.0 a servi ici.
- **L'acceptation par la mère (R-3180)** et le renvoi à l'addendum de la tranche : registres non lus, par consigne.
- **L'essai de `lens_compare` (10 tests, « tous passés »)** : hors du champ de cette vérification.

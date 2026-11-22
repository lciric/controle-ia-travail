# Vérification de la version 2 du code des verdicts de la tranche de l'ajustement de nos lentilles (lecture par lentille neuronale, B-β)

- **Vérificateur neuf** (R2) : n'a écrit ni contre-lu aucune pièce de ce travail (ni le texte gelé, ni le code v1 ou v2, ni les essais, ni la contre-lecture de la v1). Rien lu sous `registres/` ni `diag/`. Aucun autre fichier modifié, rien committé ; sondes jetables hors du dépôt.
- **Date** : 2026-11-18 05:07 UTC (`date -u`).
- **Empreintes vérifiées** (recalculées, égales aux compagnons `.sha256`) :
  - `src/controle_ia/neuron_lens/verdicts_b_beta_v2.py` : `389f909a0f0f5d446b457f0ea63ca48eb290e6921e093976c943f45beb2883de`
  - `tests/test_neuron_lens_verdicts_b_beta_v2.py` : `8bc5be3d2f7580b30fd88f76eae294767ee8a9b251e495b4b95bd9d9321f895f`
  - `src/controle_ia/neuron_lens/verdicts_b_beta_v1.py` : `92df7da5b83f0d53f378e7c07450434e4352222ef3641e9011e482ca61cadc6c`
  - `tests/test_neuron_lens_verdicts_b_beta_v1.py` : `e5f91d6c45091306ab5274dba715a451d0c541228c4067d900f39100b86750ea`
  - contre-lecture de la v1, `contre-lecture-verdicts-b-beta-v1.md` : `00599d482bdaa681639213568f27f513e5319e4f9704bf199b7819478be93ea1`
  - sortie versée des essais v2, `sortie-essais-verdicts-b-beta-v2.txt` : `dbe92895a3c2f1c54bad528d49d242979025616af683b8e1be0dc7acaa57c1fe`
  - texte qui fait foi, `docs/notes/neuron-lens-v1/texte-gele-tranche-b-beta-v1.md` : `f5d46860525f12f8ad0483e56afc0847ab7db25ecae55edcc279b61316b7a454`
- **Ce qui a été fait** : lecture du texte (« Seuil », « Chaîne en défaut », « Critères de lecture gelés », P.4), du code v2 en entier, du diff v1 → v2, des essais v2 ; essais v2 rejoués (56 passés, comme la sortie versée) ; les mêmes essais v2 joués contre le module v1 par une copie jetable (23 échecs, 33 passés) ; environ 90 sondes jetables (bornes de B-5, validation, garde (g), graine 1, audits) ; comparaison de la v1 et de la v2 sur 6 000 entrées tirées au hasard (graine fixée).

## Verdict : **à corriger**

Les quatre majeures de la contre-lecture sont corrigées dans le code, chacune avec un essai qui échoue sur la v1. Mais la correction de M4 (fractions exactes dans B-5) a introduit **un point majeur neuf** : aux bornes écrites en décimal, trois seuils de B-5 que la v1 jugeait comme le texte sont maintenant jugés à l'envers. Correction d'une ligne. Aucun point bloquant.

Comptes : bloquant 0 ; majeur neuf 1 ; mineurs neufs 5 ; mineures de la v1 : 3 traitées, 3 en partie, 3 laissées sans raison écrite.

## (1) et (2) Points de la contre-lecture précédente

Essais v2 joués contre le module v1 : 23 échecs, répartis ainsi — M1 : 1 ; M2 : 15 ; M3 : 4 ; M4 : 2 ; mineure m5 : 1.

| point | état dans la v2 | essai qui échoue sur la v1 (vérifié) | reste |
|---|---|---|---|
| **M1** — garde (e) appliquée à la sortie de la graine 1 | **corrigé** : `defauts_score(..., avec_e=False)` sur la graine 1 (l. 352). Sonde : notre R égale aux logits à la couche 12 sous la graine 1 → plus de chaîne en défaut ; B-2 et B-3 « autre » (verdict différent sous la graine 1), conforme au texte. Les gardes (a), (b), (c) y tiennent toujours (sondées une à une). | `test_m1_graine1_sans_garde_e` : la v1 rend « chaîne en défaut » | rien |
| **M2** — verdicts de mesure rendus sous « chaîne en défaut » | **corrigé** : `mesures` vide dès qu'un défaut existe (l. 383, l. 330). 2 733 cas de chaîne en défaut tirés au hasard : `mesures` toujours vide. | `test_ii_b`, `test_ii_c`, `test_gardes_de_machine` (13 cas) : la v1 rend des mesures | les écarts de B-4 et B-6 (rapportés, non décisifs) disparaissent aussi de l'objet ; sans reproche (ils restent dans la sortie de `score`) |
| **M3** — entrées acceptées sans contrôle | **corrigé** pour l'essentiel : (a) table et n de la graine 1 validés (`valider_table`, trois lentilles) ; (b) série repère exigée finie ; (c) gardes exigées `bool`. | `test_m3_graine1_validee` (2 cas), `test_m3_repere_nan_refuse`, `test_m3_garde_none_refusee` : la v1 ne lève rien | la série repère n'est pas exigée « écrite à 4 décimales » (demandé par la contre-lecture) : voir n3. Les résultats d'audit ne sont pas validés de la même façon : voir n2. |
| **M4** — égalité des moyennes de B-5 décidée par le bruit flottant | **corrigé pour l'égalité** : moyennes en fractions exactes ; (iii-b) rejoué sur 0,05, 0,3, 0,02, 0,1. | `test_iii_b[0.3]`, `test_iii_b[0.02]` : la v1 rend « autre » | la correction casse trois autres bornes de B-5 : **N1, majeur neuf** |
| m1 — attendu trop large de (v) | traité en partie : `== REPRODUIT` affirmé ; le verdict de chaque mesure et la réserve « écart d'ajustement » (effet de bord du 0,96 posé à la couche 3) ne sont pas affirmés | — | mineur |
| m2 — branches sans essai | traité en partie. Ajoutés : A4 avec lentille S différente → (k) ; A1 avec norme nulle → (l) ; A2 et A4 « non joué » ; A1 et A5 ensemble ; B-6 « intermédiaire » ; bornes de B-6, A6, B-1, (j). **Toujours sans essai** : gardes (b) et (c) (ni cas sain ni artefact, R5) et la borne n = 32 de (b) ; (vi-c) avec contrôle manqué ; A1 et A5 avec l'un « non joué » ; **toutes les bornes de B-5** (voir N1). Vérifiées justes par sondes, sauf B-5. | — | mineur |
| m3 — moitiés « à 0,02 » dans (iv-a) | **traité** : moitiés posées à +0,02 ; borne 0,05 exercée dans `test_borne_a6` | — | rien |
| m4 — clé en trop dans les différences entre moitiés, différence négative | **non traité, sans raison écrite**. Sondes : clé inconnue à 0,9 → B-1 « non reproduit » ; différence −0,5 acceptée (déclenche l'audit A2, B-1 « reproduit ») ; accord à 1,5 accepté. | — | mineur |
| m5 — différence entre moitiés non finie | **traité** : rend « chaîne en défaut (g) », `nan`, `inf` et `-inf` (voir (3)) | `test_difference_non_finie_est_la_garde_g` : la v1 lève `ValueError` | voir n4 |
| m6 — A1 et A5 ensemble | **non traité, sans raison écrite**. Sondes : le même défaut de la relance unique écrit deux fois ; A1 « non joué » avec A5 joué accepté ; audit en trop ignoré ; audit mal formé → `TypeError`. Aucun verdict faux. | — | mineur |
| m7 — marque des mesures touchées | **non traité, sans raison écrite** : B-7 « autre » garde `par_le_haut: True` | — | mineur |
| m8 — en-tête qui prêtait les lectures au texte | **traité** : voir (4) | — | rien |
| m9 — sortie versée | traité en partie : date et un cas par ligne ; ni commande, ni commit, ni empreinte du code | — | mineur |
| d1 — clause « non reproduit » non jugée sur une bande partielle | gardé, **déclaré** en tête du module et soumis à la mère | — | à trancher par la mère |
| d2 — arrondi à 4 décimales des différences | gardé, déclaré | — | idem ; suppose la série repère à 4 décimales (n3) |
| d3 — témoin de B-2 compté sur les couches lisibles | gardé, déclaré (ajouté à l'en-tête) | — | idem |
| d4 — garde (a) appliquée aux deux moitiés | gardé, déclaré comme « lecture propre à cette tranche » | — | idem |

Réponse à (2) : aucune pièce de la v2 (en-tête du module, en-tête des essais, message du commit `d3fe427d`) ne dit quelles mineures sont laissées ni pourquoi. Trois le sont (m4, m6, m7) sans un mot. Aucune ne fausse un verdict sur une entrée bien formée.

## (3) Le diff v1 → v2 casse-t-il quelque chose ?

Comparaison sur 6 000 entrées tirées au hasard (valeurs à 4 décimales, n, différences, accords, lectures, gardes, audits joués, manqués ou « non joué ») : mêmes déclencheurs, même verdict d'ensemble, mêmes défauts, mêmes réserves, même verdict de chaque mesure dans tous les cas ; seules différences, celles voulues (mesures vides sous chaîne en défaut) et le dernier chiffre flottant des moyennes de B-5 rapportées. **Hors des bornes décimales de B-5, la v2 ne change aucun verdict.**

| examen demandé | constat |
|---|---|
| refus de `nan` dans `accord`, `read_S`, `silent`, série repère | Tient : `ValueError` avec message dans les quatre cas (`inf` compris). `None` dans `accord` ou dans les différences lève `TypeError` (sans message du module) ; `None` dans la série repère est refusé proprement. Rien de cassé. |
| booléens stricts pour les gardes | Tient : `None`, `0`, `1`, `"False"` refusés. **`numpy.bool_` est refusé aussi** (bruyant, `ValueError`) : le code de course devra convertir par `bool()`. Une garde en trop (lettre inconnue) est ignorée. Voir n2 pour les audits, où la même rigueur n'est pas appliquée. |
| différence entre moitiés non finie → garde (g), mesures vides | Tient, conforme au texte ((g) : « une différence entre moitiés non finie » ; rang 1). Les autres défauts de chaîne sont rendus avec elle (sonde : (a), (g), (k) ensemble). Les audits A2 et A3 ne sont plus déclenchés (sans objet). Deux effets de bord : voir n4. |
| fractions exactes de B-5 | **Non, à la borne : N1.** |
| refus de `n` booléen | Tient : `True` refusé (la v1 le comptait pour 1 et rendait (b)). Entiers `numpy` acceptés ; flottant 64.0 refusé, comme en v1. |
| `valider_table` sur la graine 1 avec trois lentilles | Tient : une table réduite aux trois lentilles (logits, R publique, notre R) passe ; une cible absente, un n absent ou court, un `nan`, une valeur à 6 décimales sont refusés avec message (la v1 : `KeyError`, `IndexError` ou silence). Exige les quatre cibles et leur n dans la sortie de la graine 1 : conforme à ce que `score` écrit, à confirmer par le code de course. La table n'est validée que si le témoin et les normes sont sains (sinon (l) est déjà rendue) : sans reproche. |

## (4) Lectures reprises de la tranche précédente : déclarées honnêtement ?

**Oui.** L'en-tête (l. 15-25) dit que le texte gelé de cette tranche « ne les écrit pas mot pour mot », qu'elles sont « déclarées ici et soumises à la mère », et les liste : clause « non reproduit » non jugée sur une bande partielle (avec ce que dit le texte), témoin de B-2 sur les couches lisibles, arrondi des différences, valeurs prises telles qu'écrites ; plus la lecture propre à cette tranche (garde (a) sur les moitiés) et les fractions de B-5. Trois retouches de forme (mineur n5) : la ligne 10 renvoie encore aux essais **v1** ; le commentaire de la ligne 129 dit encore « règles du texte gelé v6, inchangées » ; la phrase « pour qu'aucun bruit flottant ne décide d'une égalité » est fausse pour les seuils (N1).

## (5) Points neufs

| rang | lieu | constat vérifié | correction proposée |
|---|---|---|---|
| **majeur N1** | `verdict_b5`, l. 200-209 | `Fraction(float(x))` prend le développement binaire exact du flottant, comparé à `Fraction("0.60")`, décimal exact. Or le flottant 0,6 vaut 0,59999999999999997… ; 0,3 vaut 0,29999999999999998… ; 0,4 vaut 0,40000000000000002… Sondes sur le cas sain : `read_S` = 0,6 à la couche 0 → B-5 « autre », verdict « partiel » (texte : ≥ 0,60, donc « reproduit » ; la v1 : « reproduit ») ; `read_S` = 0,3 à la couche 0 → « non reproduit » (texte : pas sous 0,30 ; la v1 : juste) ; part silencieuse 0,4 à la couche 0 → « non lisible », verdict « partiel » (texte : strictement au-dessus de 0,40 ; la v1 : lisible, « reproduit »). Écart des moyennes écrit 0,10 : 0,35 et 0,25, ou 0,7 et 0,6, ou 0,3 et 0,2 → « autre » ; 0,2 et 0,1 → « reproduit » : le bruit binaire décide encore, contre ce qu'annonce l'en-tête. **Trois régressions contre la v1**, sur des bornes que la contre-lecture avait vérifiées, et **aucun essai v2 ne touche une borne de B-5**. Portée pratique faible : les valeurs de la référence publiée sont des flottants simple précision élargis (0,8480631709098816), qui ne tombent jamais sur un décimal court, et pour eux la v2 juge juste ; le défaut ne mord que sur une valeur écrite en décimal court (0.6, 0.4). Même nature que M4 : la règle n'est ni tenue ni prouvée à la borne. | Une ligne : `Fraction(repr(float(x)))` au lieu de `Fraction(float(x))` — la valeur « telle qu'écrite » dans le JSON, ce que dit le texte. Vérifié par sonde : 0,6 → ≥ 0,60 ; 0,3 → pas sous 0,30 ; 0,4 → pas au-dessus de 0,40 ; les six couples à écart 0,10 → « reproduit » ; (iii-b) toujours « non reproduit » sur les quatre valeurs ; sur les 6 000 tirages, même verdict de B-5 que la v2. Ajouter les essais de bornes : 0,60 ; 0,30 ; 0,40 ; 0,50 de la moyenne silencieuse ; écart 0,10. C'est une lecture (décimal écrit plutôt que binaire) : à déclarer en tête, avec les autres. |
| mineur n2 | `verdict`, l. 347, 367, 374-376 | Résultats d'audit non validés, et jugés de deux façons. Témoin et normes : `is True` strict, donc un `numpy.bool_` vrai (ce que rend une comparaison `numpy`) ou un `1` donne **« chaîne en défaut (l) » à tort, sans message** (la v1 : verdicts tenus). Contrôles des audits A2, A3, A4 : simple vérité, donc une chaîne `"non"` vaut « contrôle réussi ». Contraire à la règle posée pour les gardes (refus bruyant). Du côté prudent pour le premier, pas pour le second. | Refuser tout résultat d'audit dont un champ n'est pas `bool` (même message que pour les gardes) ; un essai. À faire avec N1 : c'est le seul chemin de la v2 qui rend un verdict faux sur un type plausible. |
| mineur n3 | `valider`, l. 110-112 ; `defaut_j` | Série repère finie mais pas exigée à 4 décimales. Sonde : trois couches écartées de 0,050004 → arrondi à 0,05 → garde (j) tenue, alors que l'écart dépasse 0,05. Sans portée si la série vient d'une sortie de `score`. | Même contrôle `round(v, 4) == v` que pour les tables. |
| mineur n4 | `verdict`, l. 329-330 | Sortie anticipée sur différence non finie : (1) les résultats des audits A1, A4, A5 sont **exigés** (sinon `ValueError`) puis **ignorés** — un témoin non distinct constaté par A1 n'ajoute pas (l), et `audits` est rendu vide même si des audits ont été joués ; (2) la réserve de l'audit des deux codes (« écart de corpus » ou « écart d'ajustement ») n'est pas écrite, alors qu'elle l'est sous toute autre chaîne en défaut. Le verdict d'ensemble reste juste. | Calculer défauts d'audit et réserve avant de sortir, ou écrire que (g) coupe tout. |
| mineur n5 | en-tête et commentaires | Voir (4) : renvoi aux essais v1 (l. 10), commentaire « inchangées » (l. 129), phrase sur le bruit flottant (l. 24-25). | Retoucher. |
| mineur n6 | pièces de la v2 | Aucune note ne dit quelles mineures sont laissées et pourquoi (m4, m6, m7 ; restes de m1, m2, m9). | Trois lignes en tête des essais ou du module. |

## Non vérifiable

- Que les lectures aux activations de la course sur Llama (`read_S`, part silencieuse) seront, comme celles de la référence publiée, des flottants simple précision élargis : c'est ce qui borne la portée pratique de N1. Aucun fichier réel de Llama n'a été passé dans ce code.
- Que la sortie de `score` à la graine 1 porte bien les quatre cibles et que le code de course donne un n par cible : `causal_lens.py` non lu.
- Que le code de course rend des `bool` Python (et non des `numpy.bool_`) pour les gardes et les audits : ce code n'est pas parmi les fichiers donnés.
- Le texte gelé v6 de la tranche précédente (règle des bandes et de lisibilité) : vérifié seulement par le texte de cette tranche (l. 125-126, 168-169) et par le code.
- Les gardes (d), (f) à (i), (k), (n) à (s), l'identité des matrices et le contenu des audits : entrées booléennes ici ; leurs essais sur artefact relèvent du code de course.

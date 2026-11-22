# Vérification de la version 3 du code des verdicts de la tranche de l'ajustement de nos lentilles (lecture par lentille neuronale, B-β)

- **Vérificateur neuf** (R2) : n'a écrit, contre-lu ni vérifié aucune pièce de ce travail (ni le texte gelé, ni le code v1, v2 ou v3, ni les essais, ni la contre-lecture de la v1, ni la vérification de la v2). Rien lu sous `registres/` ni `diag/`. Aucun autre fichier modifié, rien committé ; sondes jetables hors du dépôt (dossier temporaire de la session).
- **Date** : 2026-11-18 05:17 UTC (`date -u`).
- **Empreintes vérifiées** (recalculées, égales aux compagnons `.sha256`) :
  - `src/controle_ia/neuron_lens/verdicts_b_beta_v3.py` : `3c4572f209328afc66487c02072ea6b2b3bce9dcb51b2d864b158d3b80b4f10b`
  - `tests/test_neuron_lens_verdicts_b_beta_v3.py` : `a4f7f8b55a71e033678efb2e54588035e77898fd370c0de19c6768b531fd1eda`
  - `src/controle_ia/neuron_lens/verdicts_b_beta_v2.py` : `389f909a0f0f5d446b457f0ea63ca48eb290e6921e093976c943f45beb2883de`
  - `tests/test_neuron_lens_verdicts_b_beta_v2.py` : `8bc5be3d2f7580b30fd88f76eae294767ee8a9b251e495b4b95bd9d9321f895f`
  - vérification de la v2, `verification-verdicts-b-beta-v2.md` : `a32b1f3bdbe76cb91721f8f7b2364a33c6a73f3600e088c3efcdbddbfa52ac39`
  - contre-lecture de la v1, `contre-lecture-verdicts-b-beta-v1.md` : `00599d482bdaa681639213568f27f513e5319e4f9704bf199b7819478be93ea1`
  - sortie versée des essais v3, `sortie-essais-verdicts-b-beta-v3.txt` : `9519aa40d3f6f80325230d2838ad25f6b34f89e7833f98227785aa4bd40a9cec`
  - texte qui fait foi, `docs/notes/neuron-lens-v1/texte-gele-tranche-b-beta-v1.md` : `f5d46860525f12f8ad0483e56afc0847ab7db25ecae55edcc279b61316b7a454`
- **Ce qui a été fait** : lecture du texte (« Seuil », « Chaîne en défaut », « Critères de lecture gelés », P.4), du code v3 en entier, du diff v2 → v3 du module et des essais ; essais v3 rejoués (76 passés, comme la sortie versée) ; les mêmes essais v3 joués contre le module v2 par une copie jetable (14 échecs, 62 passés) ; 21 mutations d'une copie jetable du module v3, chacune rejouée contre les essais v3 ; environ 110 sondes jetables (bornes de B-5, garde (g), relance commune aux audits A1 et A5, validation des résultats d'audit et des entrées, gardes (b) et (c), garde (j)) ; comparaison de la v2 et de la v3 sur 24 000 entrées tirées au hasard (graines fixées : 20 000 tirages généraux, 4 000 tirages forçant les audits A1 et A5).

## Verdict : **à corriger**

Le majeur N1 de la vérification précédente (bornes de B-5) est corrigé et prouvé. Toutes les mineures nommées sont corrigées dans le code. Mais la relance commune aux audits A1 et A5 a introduit **un point majeur neuf** : quand les deux audits reçoivent deux résultats différents, celui de l'audit A5 est écarté sans message, et un contrôle manqué qui y figure ne donne plus la chaîne en défaut (la v2 la rendait). Correction d'une ligne. Aucun point bloquant.

Comptes : bloquant 0 ; majeur neuf 1 ; mineurs neufs 6 ; points repris : 8 corrigés dans le code, dont 1 (mineure m4) sans essai qui le prouve.

## (1) Points repris

Essais v3 joués contre le module v2 : 14 échecs — bornes de B-5 : 5 ; série repère : 1 ; différence non finie : 1 ; résultats d'audit : 4 ; résultat en trop : 1 ; audits A1 et A5 : 1 ; marques : 1.

| point | état dans la v3 | essai qui échoue sur la v2 (vérifié) | reste |
|---|---|---|---|
| **N1, majeur** — bornes de B-5 jugées sur le développement binaire | **corrigé** : `Fraction(repr(float(x)))` (l. 207). Sondes : `read_S` écrit 0,6 à la couche 0 → « reproduit » ; 0,3 → « autre » (pas sous 0,30) ; part silencieuse 0,4 → lisible ; moyenne silencieuse égale à 0,50 (valeurs égales ou mêlées) → lisible ; écarts écrits 0,10 (0,35 et 0,25 ; 0,7 et 0,6 ; 0,3 et 0,2 ; 0,2 et 0,1 ; 0,15 et 0,05 ; 0,45 et 0,35) → tous « reproduit » ; un cheveu sous chaque borne → l'autre côté ; moyennes égales → « non reproduit ». | `test_bornes_b5_couche0` (0,6 et 0,3), `test_borne_b5_silence`, `test_borne_b5_ecart_0_10` (deux couples) échouent sur la v2. Mutations : chacun des cinq seuils de B-5 passé de strict à large ou l'inverse, et le retour à `Fraction(float(x))`, sont tous tués. | rien |
| résultats d'audit non validés | **corrigé** : `valider_audits` (l. 330-346) exige les clés exactes et des booléens stricts. Sondes : `"non"`, `1`, `None`, `numpy.bool_`, dictionnaire vide, clé en trop, chaîne autre que « non joué » → `ValueError` avec message. | `test_resultats_d_audit_valides` (4 cas) | la table de la graine 1 mise à `None` lève `TypeError` (bruyant, sans message du module) : mineur n5 |
| audits exigés puis ignorés sur une différence non finie | **corrigé, par l'autre voie** : sous la garde (g), aucun audit n'est exigé et tout résultat fourni est refusé (l. 358-361) ; la réserve de l'audit des deux codes est maintenant écrite. | `test_non_finie_sans_audit_exige` | `declencheurs` rend encore des audits à jouer dans ce cas : mineur n2 ; la réserve n'a pas d'essai : mineur n4 |
| série repère non exigée à 4 décimales | **corrigé** (l. 114). Sonde : trois couches écartées de 0,050004 → refus ; 0,06 à deux couches → rien ; à trois → (j) ; 0,11 à une → (j). | `test_repere_a_4_decimales` | rien |
| gardes (b) et (c) sans essai | **essai ajouté** (`test_gardes_b_et_c`) ; le code était juste et n'a pas changé, l'essai passe donc aussi sur la v2 (attendu). Mutations tuées : borne 32 de (b), seuil des logits, notre R retirée de (c). Sondes : n = 31 → (b), n = 32 → rien, couche 28 hors de (b) ; 0,80 et 0,85 exacts → rien ; couches 27 et 31 hors de (c). | sans objet | rien |
| m4 — clé en trop, différence négative | **corrigé dans le code** (l. 116-122) : clés exactement les quatre cibles ; différence négative refusée. | **non** : `test_stabilite_refusee` passe aussi sur la v2, pour une autre raison (la clé à 0,9 y déclenche l'audit A3, la valeur négative l'audit A2, et l'absence de résultat lève la même `ValueError`). Les deux mutations qui retirent la correction survivent aux essais. | mineur n3 ; l'accord du premier jeton hors de [0, 1] reste accepté (mineur n6) |
| m6 — audits A1 et A5 ensemble | **corrigé en partie** : défaut de la relance écrit une seule fois (libellé « A1+A5 ») ; « non joué » pour l'un seulement refusé ; résultat en trop refusé ; résultat mal formé refusé. | `test_a1_a5_incoherents_et_dedoublonnes`, `test_resultat_en_trop_refuse` | deux résultats joués mais différents : **N1 de cette vérification, majeur** |
| m7 — marque des mesures touchées | **corrigé** : `touchee_par_un_audit_non_joue` sur les mesures de l'audit non joué, et sur elles seules (24 000 tirages : 11 040 verdicts hors chaîne en défaut, marques toujours égales à la liste du texte) ; détail renommé `par_le_haut_graine_0`. | `test_mesures_marquees_sous_non_conclu_et_detail_graine_0` | `par_le_bas` garde son nom (forme) |

## (2) Le nouveau `verdict` reste-t-il fidèle au texte ?

**Oui, sauf N1 ci-dessous.**

- **Unicité et ordre** : sur les 24 000 tirages, un seul verdict parmi les cinq ; rang recalculé à part, à partir des verdicts de mesure rendus et des audits non joués : chaîne en défaut (défauts non vides, mesures vides) > non conclu (audit A1, A2, A3 ou A4 non joué) > non reproduit (B-2 ou B-3, réserve « défaut dans notre lentille » présente alors et seulement alors) > reproduit (B-1, B-2, B-3, B-5) > partiel. Aucun écart. Répartition : 12 960 chaînes en défaut, 2 768 « non conclu », 222 « non reproduit », 1 431 « reproduit », 6 619 « partiel ».
- **Relance commune** (résultat unique donné aux deux audits) : témoin ou norme manqué → (l), une fois ; garde (a) à (c) manquée sous la graine 1 → (l), une fois, la garde (e) n'y étant pas appliquée ; verdict de B-2, B-3 ou B-7 différent sous la graine 1 → « autre » (audit A1) ; « par le haut » non confirmé → B-7 « autre » (audit A5) ; « non joué » → « non conclu » si l'audit A1 est déclenché, B-7 « autre » si l'audit A5 l'est ; audit A5 seul non joué → B-7 « autre », verdict d'ensemble inchangé. Conforme aux lignes A1 et A5 et à la dernière phrase des « Audits symétriques ».
- **Comparaison v2 contre v3, hors des bornes de B-5** : mêmes déclencheurs, même verdict d'ensemble, mêmes réserves, même état des audits, même verdict et mêmes valeurs de chaque mesure dans tous les cas. Seules différences, toutes voulues :
  1. sous une différence entre moitiés non finie (1 395 cas), la v3 n'accepte aucun résultat d'audit (la v2 les exigeait) et écrit la réserve de l'audit des deux codes (270 cas) ;
  2. le défaut de la relance est écrit une fois, sous le libellé « A1+A5 », au lieu de deux (364 cas sur les 1 472 où les deux audits sont déclenchés) ;
  3. la marque `touchee_par_un_audit_non_joue` et le renommage `par_le_haut_graine_0` ;
  4. le dernier chiffre flottant des moyennes de B-5 rapportées (écart sous 10⁻¹²).
- **Entrées que la v3 refuse et que la v2 acceptait** (hors tirage, par sondes) : clé en trop ou différence négative dans les différences entre moitiés ; série repère non écrite à 4 décimales ; résultat d'audit en trop, mal formé ou non booléen ; « non joué » pour un seul des audits A1 et A5. Toutes bruyantes (`ValueError` avec message).

## (3) La lecture « valeur telle qu'écrite »

**Déclarée** : en-tête du module, l. 24-28 (« Lecture déclarée pour B-5 : chaque valeur est prise telle qu'écrite… »), avec le renvoi au N1 de la vérification précédente et la conséquence (« une valeur écrite 0,6 est jugée égale au seuil 0,60 »).

**Cohérente avec le texte** : « Seuil » dit que les valeurs de B-5 sont « non arrondies (… écrites en flottants complets par `reads_at_firings.py`) ». `repr` d'un flottant Python est la forme décimale la plus courte qui le redonne exactement : c'est ce que le module `json` de Python écrit et relit. La lecture n'arrondit donc rien (0,5999999999999999 reste sous 0,60 ; 0,6000000000000001 reste au-dessus ; les valeurs de la référence publiée, à 16 chiffres, sont prises entières : 0,8481 ; 0,2248 ; 0,0271 ; 0,1977 retrouvés). Pour une valeur seule, elle juge comme la comparaison flottante de la v1 ; elle ne s'en écarte que pour les moyennes, calculées en fractions exactes de ces décimaux. Les seuils de B-1 et des déclencheurs restent des comparaisons flottantes d'une valeur seule à un littéral : même résultat que la lecture « telle qu'écrite », donc pas d'incohérence entre B-1 et B-5.

Une limite, sans portée ici : une valeur écrite par un autre programme avec plus de chiffres que la forme la plus courte (0,59999999999999999) serait lue 0,6. Python ne l'écrit pas ainsi.

## (4) Points neufs

| rang | lieu | constat vérifié | correction proposée |
|---|---|---|---|
| **majeur N1** | `verdict`, l. 369 ; `valider_audits`, l. 345-346 | La relance commune prend le résultat de l'audit A1 quand les deux audits sont déclenchés, et **n'ouvre jamais celui de l'audit A5**. `valider_audits` annonce « A1 et A5 … ont le même résultat » mais ne contrôle que l'accord sur « non joué ». Sondes, les deux audits déclenchés : A1 sain et A5 avec témoin non distinct → **« reproduit avec nos lentilles », aucun défaut** (la v2 : « chaîne en défaut (l) ») ; A1 avec une graine 1 qui confirme « par le haut » et A5 avec une graine 1 qui ne le confirme pas → B-7 « non reproduit » maintenu (la v2 : « autre »). Repli silencieux (R5) et régression contre la v2, sur une entrée que l'interface invite à produire (un résultat par audit). Sans effet si le code de course passe le même objet aux deux ; rien ne l'y oblige ni ne le vérifie. Aucun essai ne couvre ce cas. | Une ligne dans `valider_audits` : refuser, quand les deux sont joués, deux résultats qui ne sont pas le même objet ou ne sont pas égaux (`audits["A1"] is not audits["A5"] and audits["A1"] != audits["A5"]`) ; un essai (A1 sain, A5 témoin manqué → `ValueError`). |
| mineur n2 | `declencheurs`, l. 284-301 ; `verdict`, l. 358-361 | Les deux temps du module se contredisent sous une différence entre moitiés non finie : `declencheurs` rend encore les audits A1, A4 et A5 à jouer (sonde : `["A4"]`), et `verdict` refuse ensuite tout résultat pour eux, joué ou « non joué » (`ValueError`). L'usage décrit en tête du module (jouer ce que rend `declencheurs`, puis appeler `verdict`) lève donc une erreur au lieu de rendre « chaîne en défaut (g) », et aucun fichier de verdicts ne sort. Bruyant, aucun verdict faux. | `declencheurs` rend une liste vide quand une différence est non finie (une ligne), ou l'en-tête l'écrit pour le code de course ; un essai sur `declencheurs`. |
| mineur n3 | essai `test_stabilite_refusee` | Ne prouve pas la correction de la mineure m4 : il passe sur la v2 et survit au retrait de chacune des deux lignes corrigées (voir la table des points repris). | Clé en trop avec des valeurs à 0,05 (aucun audit déclenché) ; différence négative avec le résultat de l'audit A2 fourni ; ou `match=` sur le message. Vérifié : ces deux cas rendent un verdict sur la v2 et lèvent sur la v3. |
| mineur n4 | `verdict`, l. 361 | La réserve de l'audit des deux codes écrite sous la garde (g) n'a pas d'essai (mutation qui la retire : survit). Sondée juste. | Un essai. |
| mineur n5 | `verdict`, l. 380-381 | Table ou n de la graine 1 mis à `None` (résultat d'audit par ailleurs bien formé) : `TypeError` de Python, sans message du module. Bruyant. Si le témoin est manqué, la table n'est pas ouverte du tout (sans reproche : (l) est déjà rendue). | Contrôler le type dans `valider_table`. |
| mineur n6 | `valider`, l. 123-130 | Valeurs hors de leur domaine encore acceptées : accord du premier jeton à 1,5 (verdict « reproduit ») ou négatif ; `read_S` à 1,7 ; part silencieuse négative. Relevé par les sondes de la vérification précédente pour l'accord, non repris. Sans effet sur une entrée bien formée. | Exiger [0, 1] pour l'accord, `read_S` et la part silencieuse. |
| mineur n7 | commentaires et pièces | Le commentaire de la l. 136 dit encore « règles du texte gelé v6, inchangées » (relevé à la vérification précédente) ; aucune pièce de la v3 ne dit quelles mineures restent (reste de m1 : attendus de `test_v_a1` ; reste de m2 : (vi-c) avec contrôle manqué). | Retoucher ; trois lignes en tête des essais. |

Traité depuis la vérification précédente, sans reproche : le renvoi aux essais dans l'en-tête (l. 10) ; la phrase sur le bruit flottant (l. 24-27) ; la sortie versée porte la commande, la date et l'empreinte du code, un cas par ligne (76 passés, rejoués à l'identique).

## Non vérifiable

- Que le code de course passera le même résultat aux audits A1 et A5 : ce code n'est pas parmi les fichiers donnés ; c'est ce qui borne la portée pratique du majeur N1.
- Que `reads_at_firings.py` écrit ses valeurs par le module `json` de Python (forme la plus courte), ce sur quoi repose l'égalité entre « telle qu'écrite » et `repr` : script non lu ; le texte gelé le dit (« flottants complets », l. 289-291 du script).
- Que la différence entre moitiés est calculée avant ou après `score` sur la machine : cela décide si la branche de la garde (g) de `verdict` (mineur n2) peut être atteinte pendant la course.
- Que le code de course rend des `bool` Python pour les gardes et les audits, et que la sortie de `score` à la graine 1 porte les quatre cibles et un n par cible : `causal_lens.py` et le code de course non lus.
- Les gardes constatées sur la machine ((d), (f) à (i), (k), (n) à (s), identité des matrices) et le contenu des audits : entrées booléennes ici ; leurs essais sur artefact relèvent du code de course.
- Les lectures reprises de la tranche précédente (bande partielle, témoin sur les couches lisibles, arrondi des différences, garde (a) sur les moitiés) : inchangées depuis la v2, déclarées en tête et soumises à la mère ; non réexaminées ici.

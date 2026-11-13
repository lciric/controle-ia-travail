# Contre-lecture 2 (différentielle, sur T0.7 scellé) — préenregistrement « validité de l'adaptateur », brouillon 3

## 0. Identité

- Contre-lecteur : sous-agent neuf de la session du compte 4 (`session_01Qi7Gr2uGzyVcw9VmDXgvEV`). **Identifiant de modèle donné par mon environnement : Claude Fable 5.2, `claude-fable-5-2`** — autre modèle que l'auteur du brouillon 3 (Claude Opus 5.5, `claude-opus-5-5`). Réserve déclarée : la contre-lecture 1 a été faite par un sous-agent du même modèle que moi (`claude-fable-5-2`) ; je n'en ai aucune mémoire, mais ce n'est pas un regard d'une troisième lignée. Je n'ai écrit ni ce texte, ni ses brouillons, ni T0.7, ni son module, ni T0.6, ni P3-bis.
- **J'ai lu T0.7 scellé : je suis « lecteur de T0.7 »**, exclu de tout rôle de lecteur ou d'hôte du verdict de P3-bis, et des verdicts de l'étape B de T0.7, de T0.8, du contrôle de l'adaptateur et du barreau 6.
- Consigne : `brouillons/validite-adaptateur-v1/consigne-contre-lecture-2-brouillon3-compte4-v1.md`, `aad64678c18711fe7bcfc37bb72461c08a09dc59502035c447a81751992393f2`, égale à son compagnon (vérifiée avant lecture). Interdits tenus : aucun fichier de `registres/`, de P3-bis, de `donnees/`, `diag/`, `runs/` ; aucune recherche récursive ; aucun appel au réseau ; aucun sous-agent ; aucune écriture git (deux commandes git de lecture seule : `git rev-parse`, `git diff --stat main -- <chemins nommés>`). Branche locale `lot/compte-4-v1`, commit `42ef16c3969693388a0ac40be8bf4d01859dccdf` ; `main` local `89a42d13259ba478e51dfa92d89a44425659bd81`.
- Heures (relevées par `date -u`) : début 2026-11-13T21:01:28Z ; fin 2026-11-13T21:12:57Z.

| pièce | sha256 recalculé | égal à la consigne | parties lues |
|---|---|---|---|
| brouillon 3 | `defd8ef05038e703c24733f6a5f88a1153daf5f44d2b8cae14950a5643e875fd` | oui | en entier (307 lignes) |
| journal du brouillon 3 | `fbb649c0245ad0b1d76a1249d4dd34013d073876ccab59a487cb74edfa22d083` | oui | en entier |
| brouillon 2 | `be0851f57bc09dc21ae7ed661d983fdf9aa0fb0148ea19c15f72c1c2bca830d9` | oui | par le différentiel (mot à mot, par programme) |
| journal du brouillon 2 | `d4f503d29ab5f6af149b3f7d7340b1ee6a6407b169c8ee586b4cef322ca99567` | oui | empreinte seulement — limite |
| contre-lecture 1 | `cf84198566978307c3cc3e1d10e62245042446b569a407b66bbcb029ffe9764e` | oui | en entier |
| T0.7 scellé (candidat 5) | `d7d180eccbbce8ff2e370f82957543c28f1e564c872f981c7ada403949baade5` | oui | l. 1-9 (extraits), 695 (empreintes du code), 903-910, 1198-1216 (« Métrique », plancher), 1226-1231, 1256-1313 (« Seuil », en entier), 1900-1936 (table des critères, extraits), 2028-2036 (« Puissance », en entier), 2049-2051, 2070-2090 (« Calcul et dépense », extraits), 2198-2205, 2309, **2783-2808 (« Concordance avec le texte de validité de l'adaptateur », en entier)** ; le reste par recherche de motifs dans ce seul fichier — limite |
| configuration de T0.7, v8 | `e31c7a79dc1b68d561874d4d42d63b5eb950931f06075927f239c7ad971fb328` | oui | clés citées (l. 4-9, 25-34, 56-66, 88-100) |
| vérification finale du candidat 4, vérification mécanique du candidat 5 | `26efc4df…d257`, `84ffcb01…1edd` | oui | empreintes seulement (« au besoin » : pas eu besoin) |
| module de T0.7 (arbre de travail, sans différence avec `main` sur `src/controle_ia/t07/`) | `lecture_v4.py` `42f60780…`, `lecture_v3.py` `ac3666e4…`, `lectures_t07_v2.py` `1f523c07…`, `plancher_v2.py` `a0f80e68…`, `plancher_v3.py` `c25a8822…`, `reextraction_p3_v1.py` `c32696b8…`, `passe_blanc_v2.py` `8e24642f…`, `repli_etapes_v2.py` `fe08aaa1…` | **égales aux huit empreintes « état au candidat 4 » de T0.7 scellé, l. 695** | `lecture_v4.py` l. 1-330, 352-362, 420-560, 575-700 ; `repli_recalcul_v1.py` en entier ; `criteres_v1.py` l. 44-65, 504-612, 619-640, 690-705 ; `registre_v1.py` l. 27-82, 120-150, 289-300 ; `mahalanobis_v1.py` l. 84-98 ; `reextraction_p3_v1.py` l. 87-118, 543-565 ; `lecture_v2.py` l. 240-249, 764-792 ; `lecture_v1.py` l. 815-837 ; `lectures_t07_v1.py` l. 423-463 ; le reste par motifs |
| autres modules nommés | `lecture_v2.py` `709b2feb…`, `criteres_v1.py` `12b999fe…`, `repli_recalcul_v1.py` `9ceabbcb…`, `sondes_neuves_v1.py` `d4d354e7…`, `registre_v1.py` `e5023657…`, `mahalanobis_v1.py` `b2816306…`, `code_t07_v1.py` `52f44ce0…` | chacune présente une fois dans T0.7 scellé (l. 695) | — |
| `premier_test_ia/figees.py`, `conditions.py` | `a2238a8c…38cc`, `dda64117…ac63` | (aucune empreinte donnée) | `lire_sondes` (l. 56-81), `mesures_action` (l. 98-113) |
| `t06/lanceur.py`, `t06/test_croise.py` | — | — | l. 60, 278-288 ; l. 49-50 (origine de `mention_etendue`) |
| note 2a | `2db916aa125d37504d58d712396a59d2ed5c934a0c5438787cb68a55113e8305` | oui | l. 1-40 — limite |
| T0.6 scellé | `ef31feff9abb26d0d66c3c35f3c721ee7d054a63f880657535a5e4a47cbdf169` | oui | l. 401, 458, 537-539, 611, 643, 667-668 |
| configuration de 7b | `b7a5c1baeee13f7589b296fb166180515422ebc8c7eff703994bb5b6835ae527` | oui | clés (`offre`, `couches`, équivalence l. 98, 125, 129, 143) |
| gabarit, validateur | `8cad4371…700e`, `3b2e3ee5…c306` | oui | titres ; validateur joué |

## 1. Verdict

**Non scellable en l'état : cinq bloquants (quatre à correction mécanique, un qui touche la règle de lecture), six majeurs, sept mineurs.** Le différentiel du brouillon 2 au brouillon 3 est propre (chaque constat de la contre-lecture 1 est appliqué, aucun changement sans fondement) ; ce qui bloque vient de T0.7 scellé, qui a changé après le brouillon 21.
T0.7 scellé juge « au-dessus » par la **règle (a)** (différence appariée au plancher) à **800 directions**, avec un **plancher neuf** pour les deux sondes figées de P3 ; le brouillon 3 garde la règle du candidat 1 (que T0.7 dit libérale), 200 directions, et le plancher de P3.
Aucun score de T0.7 n'existe : un brouillon 4 suffit ; la réserve générale ne peut être levée qu'après lui.

## 2. Constats

Lignes du brouillon 3 : numéros du fichier `defd8ef0…`. « T0.7 » = `prereg/T0.7-sondes-v0-v1.md` scellé. Module : arbre de `main`.

### Bloquants

**CLVA2-01 — bloquant — la règle « au-dessus du plancher » de ce texte est celle que T0.7 a abandonnée.**
- Endroit : l. 84 « VA-1, VA-3, VA-5b, VA-6 : borne basse **strictement supérieure** au quantile 0,95 du plancher » ; l. 86 (VA-2 : borne basse du tau au-dessus du quantile des tau des directions) ; l. 68 (« Plancher ») ; phrases gelées « au-dessus de son plancher [q] ».
- Preuve : T0.7 l. 1258 : « la **borne basse** de l'intervalle percentile, par blocs de tâches, de la **différence D = (aire de la sonde) − (quantile 0,95 des aires des directions du plancher)** […] recalculées sur les mêmes tirages, est **strictement positive** » ; au candidat 1 : la règle du brouillon 3. T0.7 l. 2033 : « la puissance de la règle du candidat 1 se payait d'une erreur réelle 4 à 9 fois le nominal » ; l. 2035 : taux simulé « 6,0 % à 13,3 % » au lieu de 2,5 % sous un plancher à signal commun. Code : `plancher_v2.comparer_difference_au_plancher` (`plancher_v2.py` l. 132), appelée par `lecture_v3.lecture_jeux_v3` (l. 136) et `lectures_t07_v2`.
- Conséquence : les lignes qui **soutiennent** H-VAL seraient jugées par une règle dont le niveau n'est pas tenu, dans le sens qui arrange (R4) ; et `A_obs`, VA-3 ou VA-5b pourraient être « au-dessus » ici pour un couple que T0.7 lit « non au-dessus » sur les mêmes scores.
- Correction (change le dessin ; **décision de la mère**) :
  - (a) règle (a) pour VA-1, VA-3, VA-5b, VA-6 et pour la mention « au-dessus de son plancher : oui ou non » des lignes de réserve, par `plancher_v2.comparer_difference_au_plancher` importée sans modification (mêmes tâches tirées pour la sonde et ses 800 directions, 2 000 tirages, niveau de la ligne) ; VA-2 par l'analogue (borne basse de `tau − quantile 0,95 des tau des directions`, recalculés sur chaque tirage, strictement positive, et valeur p). Avantage : même règle que T0.7, niveau tenu, code déjà contre-lu. Inconvénient : puissance à refaire (CLVA2-10) ; l'analogue pour le tau n'a pas été simulé par la note de l'analyste de T0.7 (à déclarer).
  - (b) garder la règle écrite, avec la réserve de T0.7 recopiée. Avantage : aucun changement. Inconvénient : niveau non tenu sur les lignes de soutien, deux règles pour un même jeu.
  - (c) règle (a) pour les aires, VA-2 gardée telle quelle avec réserve écrite. Avantage : aucune statistique neuve. Inconvénient : VA-2 porte « l'essentiel de la puissance dans la dose » (l. 145) et resterait sous la règle libérale.
  - **Recommandation (a)**, confiance 0,8.

**CLVA2-02 — bloquant — plancher des deux sondes figées de P3 : mauvais fichier, et le second contrôle refuserait à tort.**
- Endroit : l. 73 « Sondes figées de P3 : `donnees/20261019-230011-p3-reel/sondes-figees-legeres.npz`, `701f73bd…`, noms `meta.planchers.tromperie` et `.enjeux` » ; l. 102 (E6).
- Preuve : T0.7 l. 1206 : « **Pour les deux sondes figées de P3, le plancher décisif est neuf** […] **800 directions neuves** […] noms `<sonde>-t07-plancher-<k>` ; fichier scellé `donnees/<run-t07>/planchers-figees-t07.npz` » ; les 200 de P3 sont « **notées et lues en descriptif seulement** ». Code : `lecture_v4.py` l. 245-249 (`plancher_p3_<k>`, `entree["plancher_p3"]`) et l. 259-262 (`plancher_<k>`, `entree["plancher"]["empreintes_deux_premieres"]` = plancher **neuf**) ; `reextraction_p3_v1.py` l. 550-560 (`meta.planchers[<sonde>]`, `meta.graines`, `meta.methode`) ; `lecture_v4.py` l. 547 (`notation-t07.json` → `resultat.planchers_figees.fichier`).
- Conséquence : les deux premières directions du fichier léger de P3 ne peuvent pas égaler `index.sondes[k].plancher.empreintes_deux_premieres` : la pièce R serait « non calculable » pour les deux sondes figées (garde qui refuse à tort) ; et sans ce contrôle, elle jugerait contre un plancher que T0.7 dit descriptif.
- Correction mécanique : couples CLVA2-02a, CLVA2-02b (section 3). Le cas « bras de réextraction non établi » (T0.7, liste d'arrêt : lectures décisives de la sonde en « échec ») est réglé par CLVA2-06.

**CLVA2-03 — bloquant — 200 directions partout ; la garde « 200 exigées » refuserait le fichier de l'étape A.**
- Endroit : l. 45, 65, 68, 69, 73 (« 200 exigées »), 86, 102, 114.
- Preuve : T0.7 l. 1198 : « **800 sondes linéaires aléatoires** (**candidat 2** […] `n_plancher` = 800 pour tout plancher tiré à l'étape A ; 200 au candidat 1) » ; configuration v8 l. 6 : `"n_plancher": 800` ; `lecture_v4.py` l. 110 (refus si ≠ 800 en mode réel), l. 176-178 (`plancher_<k>` doit compter `n_plancher` lignes) ; `sondes_neuves_v1.py` l. 419, 452.
- Correction mécanique : couples CLVA2-03a à CLVA2-03h (les six occurrences de « 200 directions », « 200 exigées », la forme du tableau).
- **Passage de T0.7 scellé qui contredit les 800 directions (cité, jamais à corriger)** : l. 2789 « `scores_<k>` et `plancher_<k>` (forme (200, n_actions) après transposition ; l. 630-631) », alors que l. 2793 écrit « 200 au candidat 1, **800 au candidat 2**, `n_plancher` ; […] nombre à revérifier contre lui » ; et l. 2802 « lues dans le fichier léger de P3 (sondes figées) », que la l. 1206 dépasse. Le module tranche : 800 (`lecture_v4.py` l. 176-178).

**CLVA2-04 — bloquant (correction d'un mot) — valeurs de Q : le code n'écrit pas « non calculable » ni « incohérent ».**
- Endroit : l. 122 « `L1b` avec `resultat.entrees.Q` ∈ {non calculable, incohérent} ».
- Preuve : `criteres_v1.py` l. 48 : `Q = ("illisible", "non_calculable", "incoherent", "vide", "partiel", "complet")` ; l. 697 : `"entrees": {"G": g, "P": p, "A": a, "Q": q, …}`. T0.7 l. 1909-1910 écrit la prose (« Q = non calculable », « Q = incohérent »), non le littéral.
- Conséquence : un recoupement écrit à la lettre rendrait « désaccord : refus, code 2, nœud » sous L1b avec Q `non_calculable` (refus à tort, du côté sûr).
- Correction mécanique : couple CLVA2-04.

**CLVA2-05 — bloquant (correction locale) — `mention_etendue` n'est pas rendue par `mesures_action`.**
- Endroit : l. 77 « (`mention_etendue`, par `premier_test_ia.conditions.mesures_action`, la fonction des prédicteurs triviaux de T0.7 […], rejouée sur les textes de `HD` et de `H'`) ».
- Preuve : `premier_test_ia/conditions.py` l. 98-113 : `mesures_action` rend `mention_texte_prive` et `mention_triple`, pas `mention_etendue` ; `t06/lanceur.py` l. 284-285 : `"mention": bool(mesures["mention_texte_prive"]), "mention_etendue": tc.mention_etendue(a.texte)` ; `t06/test_croise.py` l. 49-50. Configuration v8 l. 60-63 : `predicteurs_triviaux` = `jetons_notes`, `pas`, `mention_etendue` (colonnes de `mesures-t06.npz`). L'imprécision vient de T0.7 l. 1228-1229 (« motifs de P3 étendus de P3-bis ; `premier_test_ia.conditions.mesures_action` ») et de CLVA-13 : citée, non corrigée dans T0.7.
- Conséquence : rejouée sur `HD` et `H'`, `mesures_action` donnerait un autre prédicteur (motifs non étendus) que celui de 7b, ou une clé absente.
- Correction mécanique : couple CLVA2-05. La mention `mention_texte_prive` de la l. 107 (exclusion des données de distillation) est exacte et ne change pas.

### Majeurs

**CLVA2-06 — majeur — une sonde en « échec » à l'étape A arrêterait toute la pièce L.**
- Endroit : l. 246 « **Champ de T0.7 attendu absent** de son fichier (levées de la contre-lecture 1) : arrêt, nœud. »
- Preuve : `lecture_v4.py` l. 250-251 et 267-268 : une sonde figée dont le plancher neuf n'est pas établi, ou une sonde dont l'essai d'égalité échoue, reçoit `etat` = « échec » ; ses tableaux `plancher_<k>` (et parfois `scores_<k>`) sont absents ; T0.7 l. 1440 : « **repli** : liste d'arrêt (bras arrêté, lectures décisives de la sonde en « échec ») ».
- Correction mécanique : couple CLVA2-06 (la sonde seule devient « non calculable », le reste se lit).

**CLVA2-07 — majeur — notation des directions de la pièce R : 3 200 directions, et la fonction par lots doit être nommée.**
- Endroit : l. 219 « R : notation, sondes non Mahalanobis et 800 directions | ≈ 3,2 fois les jetons de 7b | 0,1 à 0,5 » ; l. 239 (code réutilisé).
- Preuve : T0.7 l. 2086 : « la notation par lots remplace […] la boucle du harnais (≈ 4 h pour une douzaine de planchers à 200 directions, ≈ 16 h à 800 : rapport, § 8) » ; incrément de l'étape A pour la notation par lots : « 0,09 et 0,32 » h. Calcul (section 2 bis) : par lots ≈ 0,10 à 0,34 h pour la pièce R (le poste 0,1 à 0,5 h tient) ; par la boucle ≈ 17,2 h, soit 18,7 à 22,3 USD (la coupure de 8,5 USD saute).
- Correction mécanique : couples CLVA2-07a, CLVA2-07b.

**CLVA2-08 — majeur — « les réserves de T0.7 sur la même sonde » : le champ n'a pas de clé de sonde.**
- Endroit : l. 191.
- Preuve : `lectures_t07_v1.py` l. 423-463 : `reserves_identifiees` est une liste d'entrées `{"id", "phrase", "motif"}` (plus `concept` pour R8) ; la sonde n'apparaît que dans le texte libre de `motif` (R3 : « <nom> au-dessus sur T100 contre honnete » ; R4 : « <nom>, <jeu> : borne haute … ») ; R2 porte l'état de T7-P15, sans nom. `lecture_v4.py` l. 647 : les entrées dont la phrase est « non déclenchée » sont dans la liste (elles ne sont filtrées que pour `resultat.reserves`).
- Correction mécanique : couple CLVA2-08 (recopie de toutes les réserves déclenchées, motif compris, à chaque couple ; aucun tri par sonde).

**CLVA2-09 — majeur — tous les renvois vont au brouillon 21 et au commit `8ae9fc44` ; T0.7 est scellé et joué par `lecture_v4`.**
- Endroit : l. 3, 13 ; 23 marques « (T0.7 brouillon 21, levé par la contre-lecture 1 ; l. …) » ; l. 239 « au commit de `CODE-T07` ».
- Preuve : T0.7 l. 695 : `CODE-T07` cite `registres/code-t07/CODE-T07-v2.json` (`d5eb0b66…`), commit C7 `b4cd9953d199dd8f220f5162e5868c5b00fd392d`, vingt-six modules, dernier commit contre-lu `a621dcd3…` ; `lecture_v4.py` l. 18-19 : « **Écart de nom déclaré** : le texte nomme `lecture_v2` (étape A, repli, passe à blanc) et `lecture_v3` (étape B) ».
- Correction : couple CLVA2-09 pour l'en-tête ; pour les 23 marques (non mécanique, une par une), table de correspondance :

| objet | renvoi du brouillon 3 | T0.7 scellé | module sur `main` |
|---|---|---|---|
| `S100` contre `T100` sans seuil | l. 1024, 1246 | l. 1183, 2785 | — |
| écart sonde moins base (L2) | l. 1773, 2348-2351 | l. 1915 | `lecture_v4.py` l. 628-633 |
| sondes lues, niveau, familles | l. 1157-1165, 1231-1236 | l. 1293-1313, 1361, 2801 | `lecture_v4.py` l. 495-499 |
| tableaux de `scores-actions-t07.npz` | l. 1309-1312 ; `lecture_v2.py` l. 606-607 | l. 1451-1453, 2789 | `lecture_v4.py` l. 217-218, 259-262 |
| `sondes-neuves-t07.npz`, `fichiers_sondes_neuves` | l. 1926-1931, 2339-2344 ; `lecture_v2.py` l. 734-754, 901-902 | l. 2049-2051, 2790, 2793 | `lecture_v2.py` l. 764-789 ; `lecture_v4.py` l. 506 |
| `empreintes_deux_premieres`, `notation-t07.json` | `lecture_v2.py` l. 608-609, 942 | l. 2791 | `lecture_v4.py` l. 262, 544-553 |
| fichier léger de P3 | l. 1054-1055 | l. 1206 | `lecture_v4.py` l. 137-141 |
| prédicteurs triviaux | l. 1085-1086, 2181 | l. 1226-1229, 2312 | configuration v8 l. 60-63 |
| table A, `lecture-cout-t06.json` | l. 1398, 2067 | l. 1540, 2188, 2252 | — |
| champs de `lecture-t07.json` | l. 2345, 2375 ; `lecture_v2.py` l. 1081-1082 ; `criteres_v1.py` l. 586-600 | l. 2792, 2800 | `lecture_v4.py` l. 669-685 ; `criteres_v1.py` l. 586-600 |
| issue de P3-bis, clés du registre | l. 2077-2084 | l. 2198-2205 | `registre_v1.py` l. 47-53 |
| marques admises, clé refusée | l. 2177-2178, 2322 | l. 2309, 2454, 2805 | `registre_v1.py` l. 138-148 ; configuration v8 l. 29-34 |
| lignes L et fermeture de (ii) | l. 1759-1766, 1798 | l. 1900-1910, 2800 | `criteres_v1.py` l. 504-532, 586-600 |
| réserves R2, R3, R4, R8, R14, R15 | l. 1777-1794 | l. 1919-1921, 1927, 1935-1936, 2803 | `lectures_t07_v1.py` l. 423-463 |
| recalcul du repli | plan, point 8, l. 1385-1395 | l. 2073, 2794 | `repli_recalcul_v1.py` l. 179-216 |
| temps de notation, Mahalanobis | l. 1956-1957 | l. 2076-2078, 2086 | — |
| règle d'arrêt « plus un quart d'heure » | l. 1966 | l. 2086 | — |
| journal des ouvertures | l. 1316 | l. 1458, 2804 | `registre_v1.py` l. 289-300 |

**CLVA2-10 — majeur — la table « Puissance » ne vaut plus pour les lignes de soutien.**
- Endroit : l. 132 (« plancher de bruit pris à `0,5 + 1,645 σ` »), l. 141 « 0,596 (même ordre que T0.7, 0,600 à 0,635, rapport des prémisses § 2b) ».
- Preuve : T0.7 l. 2031 : « 64 tâches, quatre sondes lues (98,75 %) : **0,6408** […] tromperie, **0,6058** […] enjeux, **0,5815 à 0,6658** […] sondes neuves » ; l. 2033 : la formule « tient le quantile du plancher pour fixe et sous-estime la perte » (perte simulée 0,16 à 0,35 par sonde).
- Calcul (section 2 bis) : sous la règle (a), par la même formule et un écart type de D de 1,10 fois celui de la sonde (rapport de l'audit de P3 cité par T0.7 l. 2030 ; supposé) : 0,602 au lieu de 0,596 (640 contre 640, 98,75 %) ; VA-1 : 0,881, 0,789, 0,711, 0,667 au lieu de 0,857, 0,771, 0,698, 0,656 ; VA-2 : 0,165, 0,192, 0,271 au lieu de 0,155, 0,180, 0,254. Les lignes de réserve (0,554) ne changent pas.
- Correction (suit CLVA2-01 ; **décision de la mère**) : (a) refaire la table sous la règle retenue, écrire que le plancher nul à `0,5 + 1,645 σ` est optimiste et citer la fourchette de T0.7 scellé à la place de « 0,600 à 0,635 » ; (b) garder la table et la dire périmée. **Recommandation (a)**, confiance 0,85. Le seuil « non informative » (`σ > 0,060`, « aire minimale détectable supposée > 0,80 ») est à recalculer du même geste.

**CLVA2-11 — majeur — passages qui supposent la pièce HD jouée en parallèle de 7b, et calendrier périmé.**
- Endroit : l. 8, 113, 228, 229, annexe A (l. 296-306). Détail, conséquences et options : section 5. **Nœud (Lazar)** pour l'ordre des pièces ; le reste est rédactionnel.

### Mineurs

- **CLVA2-12 — mineur — la garde d'équivalence existe déjà, et `recalculer` rejoue tout 7b.** Endroit : l. 71, 239. Preuve : `repli_recalcul_v1.py` l. 211 : `garde = rp.garde_equivalence(recalculees, sous, couche_se, stat, tol, frac)` (statistique, tolérance **et fraction du contrôle négatif**, 0,95 dans la configuration de 7b, l. 98) ; l. 136 : le rejeu parcourt tous les états de `etats_adaptateur(config)`, donc les **576** épisodes des neuf conditions (les conditions instruites comprises), pas les 384 de R1, R3_d et R6 ; l. 193 : refus si `donnees/<run>/activations` existe. Correction : couples CLVA2-12a, CLVA2-12b.
- **CLVA2-13 — mineur — passes de la recherche de `c_d` et pire cas.** Le journal compte 1 024 + 832 + 512 passes ; les séries R1 à R11 font 1 856 épisodes ; la recherche telle qu'écrite (l. 75 : quatre doses, 16 tâches, douze pas au plus) fait jusqu'à 768 passes, et le recalcul de T0.7 en ajoute 192 (CLVA2-12). Calcul : R 1,90 à 2,80 h, pire 8,85 USD (au lieu de 8,69), ensemble pire 33,4 USD (au lieu de 33,2). Le nœud N-VA-1 reste ouvert, inchangé sur le fond ; la coupure de R (8,5) reste sous son pire cas. Aucun couple : à reprendre avec le devis du brouillon 4.
- **CLVA2-14 — mineur — disque et taille des sorties de la pièce R.** T0.7 l. 2086 : « activations recalculées ≈ 31,5 Go » pour 576 épisodes. Si la pièce R garde sur disque les activations de toutes ses séries : ≈ 112 Go, soit ≈ 138 Go avec le modèle et les paquets, pour 150 Go exigés (marge de 12 Go) ; à écrire : seules les activations du recalcul de T0.7 sont gardées, les séries à état imposé sont notées en mémoire. `scores-relecture-vadapt.npz` : ≈ 476 Mo en double précision à 800 directions (119 Mo à 200) ; la poussée (0,1 h) tient.
- **CLVA2-15 — mineur — `preparer_sonde` demande un mode de calcul et une graine.** `mahalanobis_v1.py` l. 86 : `preparer_sonde(sonde, calcul, graine)` ; T0.7 passe `config["mahalanobis_calcul"]` (« produit_matriciel_v2 », configuration v8 l. 9) et la graine `mahalanobis-egalite/<nom>`. La liste des graines de ce texte (l. 126) n'a pas de clé pour cet essai. Correction : couple CLVA2-15.
- **CLVA2-16 — mineur — `resultat.jeux` ne porte que `(i-a)` et les doses jugées, et vaut `null` quand les scores sont fermés.** `lecture_v4.py` l. 618-620 (`decisifs = [cr.JEU_I] + jugees`) ; l. 608 (`jeux` nul tant que les scores ne sont pas ouverts). Une dose non jugée absente de `jeux[sonde]` n'est pas un « champ absent » au sens de la liste d'arrêt. Correction : couple CLVA2-16.
- **CLVA2-17 — mineur, sans correction exigée — `R11-arret` et `R12-invalide` ne peuvent pas être lus dans `lecture-t07.json`.** `lecture_v4.py` l. 603 (`g = "ok"`) et l. 690-691 : un arrêt écrit `arret-etape-b.json`, que la pièce L refuse déjà (l. 116). Les deux valeurs sont inoffensives dans l'ensemble du recoupement de G-2.
- **CLVA2-18 — mineur — section « Contre-lecture ».** Ajouter l'entrée de la présente contre-lecture (rapport, empreinte, verdict, traitement de CLVA2-01 à CLVA2-18) et remplacer le dernier paragraphe (l. 292), qui annonce encore une « contre-lecture suivante » ; le validateur exige les deux empreintes de chaque entrée.

### Différentiel du brouillon 2 au brouillon 3 (point 2 de la consigne)

Joué mot à mot par programme sur les deux fichiers (162 lignes changées). Chaque constat CLVA-01 à CLVA-20 est appliqué à l'endroit que dit la table de traitement (l. 266-290) ; les décisions de la mère recopiées au journal (règle simple sous fermeture de (ii) ; VA-6k en ligne de réserve ; antériorité à `VERDICT-P3BIS` ; lecture large R-2207 citée) sont toutes écrites. Aucun changement sans fondement trouvé : les ajouts du rédacteur (réserves R2, R4, R14 ; ordre de jeu de HD ; audit R4 à trois fois l'attendu ; condition sur VA-6k dans l'issue la plus forte) sont déclarés au journal, § 2, et cohérents. Aucun constat de la contre-lecture 1 non appliqué. Défauts neufs : CLVA2-05 (CLVA-13 appliqué à la lettre, mais la lettre était inexacte) ; la ligne de devis « 800 directions » (quatre fois 200), désormais 3 200 (CLVA2-07). CLVA-20 demandait de citer T0.7 scellé « quand il existera » : c'est CLVA2-09.

### Vérifié, sans remarque

`diag/<run-t07>/sondes-t07.json` → `resultat.sondes_lues`, `resultat.niveau_applique`, `resultat.principales[]` (`nom`, `couche`, `agregation`, `famille`, `empreinte`, `concept`), `resultat.fichiers_sondes_neuves.sondes.sha256` (`lecture_v4.py` l. 495-506 ; `lecture_v2.py` l. 788) ; `notation-t07.json` → `resultat.index.sondes[k].plancher.empreintes_deux_premieres` et `resultat.graines_derivees_apres_manifeste` (`lecture_v4.py` l. 262, 544-553) ; `lecture-t07.json` → `scores_ouverts`, `scores_ii_ouverts`, `issue_critere_3`, `entrees.Q`, `jeux`, `jeux_hors_jugement`, `doses` (`qualifiees`, `jugees`, `hors_jugement`), `reserves_identifiees` (l. 669-685) ; `arret-etape-b` (l. 691) ; les deux degrés de fermeture (`criteres_v1.py` l. 586-600 ; A1 → L1, l. 522) ; marques admises `T06`, `T08`, `P3BIS`, `NARC` et refus d'une clé `…-VADAPT` (`registre_v1.py` l. 138-148 ; T0.7 l. 2805) ; issue de P3-bis (`docs/verdicts/verdict-P3-bis-v1-issue.json`, champ `issue`, T0.7 l. 2198) ; `lire_sondes(chemin, sha_attendue)` rend (sondes, méta, empreinte) et contrôle chaque empreinte (`figees.py` l. 56-81) ; `preparer_sonde` est dans `t07/mahalanobis_v1.py` ; statistique `q99` et tolérance 0,2 de la configuration de 7b (l. 129, 143) ; quantile du plancher 0,95 inchangé (configuration v8 l. 5) ; Bonferroni 98,75 %, 98,33 %, 97,5 % (T0.7 l. 1298-1302) ; T0.6 l. 611 (liste d'arrêt), l. 401 (0,39), l. 643 (40,2 s) ; offre de 7b (16 cœurs, 150 Go, 128 000 Mo, 0,08 USD de l'heure).

## 2 bis. Arithmétique des 800 directions (point 3 de la consigne)

Script : `prereg/contre-lectures/validite-adaptateur-preenregistrement-v1-brouillon3-cl2-calcul.py` (scellé). Sortie, recopiée à l'octet :

```
== 1. formes (piece L)
actions de 7b au plus : 9 x 64 x 10 = 5760
plancher_<k> : (200, n_actions <= 5760) ; rang du quantile 0,95 : 190.05 sur 200 aires
plancher_<k> : (800, n_actions <= 5760) ; rang du quantile 0,95 : 760.05 sur 800 aires
== 2. piece R : passes et directions
episodes notes : 1856 (journal du brouillon 3 : 1024 + 832 = 1856) ; rapport aux 576 de 7b : 3.222
directions notees, 4 sondes : 3200 a 800 par sonde (800 a 200 par sonde)
directions notees, 3 sondes : 2400 a 800 par sonde (600 a 200 par sonde)
directions notees, 2 sondes : 1600 a 800 par sonde (400 a 200 par sonde)
scores de R, 4 sondes, 200 directions, double precision : 18560 x 4 x 201 x 8 = 119.4 Mo
scores de R, 4 sondes, 800 directions, double precision : 18560 x 4 x 801 x 8 = 475.7 Mo
== 3. piece R : temps de notation des directions (echelle de T0.7 scelle, l. 2086)
facteur d'echelle (4 planchers sur une douzaine, 3.222 fois les jetons) : 1.074
par lots (plancher_v3) : 0.10 h attendu, 0.34 h au pire (T0.7 : 0,09 et 0,32 h pour l'etape A)
par la boucle du harnais, 200 directions : 4.3 h, soit 4.7 a 5.6 USD (1,0889 a 1,30 USD/h)
par la boucle du harnais, 800 directions : 17.2 h, soit 18.7 a 22.3 USD (1,0889 a 1,30 USD/h)
== 4. devis de R refait (formule du journal du brouillon 3, § 4)
journal : 2368 passes, 0.296 h ; R 1.85 a 2.75 h ; pire 8.69 USD ; ensemble pire 33.2 USD (HD pire 24.56)
corrige : recalcul des 576 episodes de 7b (+192), recherche de c_d a 12 pas (768 au lieu de 512) : 2816 passes, 0.352 h ; R 1.90 a 2.80 h ; pire 8.85 USD ; ensemble pire 33.4 USD (HD pire 24.56)
poste notation du brouillon 3 : 0,1 a 0,5 h ; par lots a 3 200 directions : 0.10 a 0.34 h (tient) ; par la boucle : 17.2 h (ne tient pas)
== 5. disque de R (T0.7 scelle, l. 2086 : 31,5 Go d'activations pour 576 episodes, trois couches)
par episode : 0.0547 Go ; recalcul de T0.7 (576) : 31.5 Go ; toutes les series de R gardees (2048) : 112.0 Go ; avec modele 16 et paquets 10 : 138.0 Go (disque exige : 150)
== 6. bruit d'echantillonnage du quantile 0,95 du plancher (aires nulles normales d'ecart type s)
n = 200 : ecart type du quantile = 0.1494 s
n = 800 : ecart type du quantile = 0.0747 s
a 640 contre 640, s = 0.01918 : 0.0029 (200) et 0.0014 (800) en aire
== 7. puissance des lignes de soutien : regle du brouillon 3 et regle (a) de T0.7
(regle (a) : meme formule, ecart type de D = 1,10 fois celui de la sonde, rapport lu a l'audit de P3 cite par T0.7 l. 2030 ; suppose)
640/640 niveau 0.9875 : brouillon 3 0.596 ; regle (a) 0.602 (ecart +0.006)
640/640 niveau 0.9833 : brouillon 3 0.594 ; regle (a) 0.600 (ecart +0.006)
640/640 niveau 0.9750 : brouillon 3 0.591 ; regle (a) 0.597 (ecart +0.006)
VA-1 (30, 100) niveau 0.9875 : brouillon 3 0.857 ; regle (a) 0.881
VA-1 (50, 200) niveau 0.9875 : brouillon 3 0.771 ; regle (a) 0.789
VA-1 (100, 300) niveau 0.9875 : brouillon 3 0.698 ; regle (a) 0.711
VA-1 (200, 300) niveau 0.9875 : brouillon 3 0.656 ; regle (a) 0.667
reserve 640/640 (borne basse > 0,5, 95 %) : 0.554 (inchangee : aucun plancher dans le critere)
VA-2 64x10 niveau 0.9875 : brouillon 3 0.155 ; analogue de la regle (a) 0.165
VA-2 64x8 niveau 0.9875 : brouillon 3 0.180 ; analogue de la regle (a) 0.192
VA-2 64x5 niveau 0.9875 : brouillon 3 0.254 ; analogue de la regle (a) 0.271
T0.7 scelle, regle (a), 64 taches, 98,75 % (l. 2031) : 0,6408 ; 0,6058 ; 0,5815 a 0,6658 (planchers de P3, non nuls)
```

Lecture : (1) pièce L : `plancher_<k>` de forme (800, n_actions), n_actions ≤ 5 760 ; le quantile 0,95 se lit sur 800 aires, et son bruit d'échantillonnage est divisé par deux (≈ 0,0014 d'aire au lieu de 0,0029 à 640 contre 640) ; sous la règle (a) ce quantile est recalculé à chaque tirage. (2) pièce R : 3 200 directions à quatre sondes ; le temps tient dans le poste écrit seulement par la notation par lots de T0.7 ; coupures et nœud N-VA-1 inchangés à 0,2 USD près. (3) puissance : + 0,006 d'aire sur les lignes de soutien par la formule, davantage en simulation selon T0.7 ; lignes de réserve inchangées.

## 3. Couples

Chaque « ancien » est présent une seule fois dans le brouillon 3 (`defd8ef0…`), contrôlé par programme sur ce bloc.

```json
[
 {"id": "CLVA2-02a", "ancien": "Sondes figées de P3 : `donnees/20261019-230011-p3-reel/sondes-figees-legeres.npz`, `701f73bd3a8ef30f46b304a6d5caa21444f0e1daf0829d04046e4024aa4e6e60`, noms `meta.planchers.tromperie` et `.enjeux`", "nouveau": "Sondes figées de P3 : poids lus dans `donnees/20261019-230011-p3-reel/sondes-figees-legeres.npz`, `701f73bd3a8ef30f46b304a6d5caa21444f0e1daf0829d04046e4024aa4e6e60` ; **plancher décisif neuf**, lu dans `donnees/<run-t07>/planchers-figees-t07.npz`, noms `meta.planchers[<nom de la sonde>]` (`<sonde>-t07-plancher-<k>`), 800 exigées, fichier vérifié contre `diag/<run-t07>/notation-t07.json` → `resultat.planchers_figees.fichier.sha256` ; les 200 directions de P3 (`meta.planchers.tromperie` et `.enjeux` du fichier léger), que T0.7 ne lit qu'en descriptif, ne sont **jamais notées** par ce texte"},
 {"id": "CLVA2-02b", "ancien": "(poids et 200 directions des sondes neuves) et `sondes-figees-legeres.npz` (`701f73bd…`)", "nouveau": "(poids et 800 directions des sondes neuves), `donnees/<run-t07>/planchers-figees-t07.npz` (800 directions neuves de chaque sonde figée de P3) et `sondes-figees-legeres.npz` (`701f73bd…`, poids des deux sondes figées)"},
 {"id": "CLVA2-03a", "ancien": "`plancher_<k>` (forme (200, n_actions) après transposition)", "nouveau": "`plancher_<k>` (forme (800, n_actions) après transposition ; `n_plancher` = 800 ; pour les deux sondes figées de P3, c'est leur plancher neuf)"},
 {"id": "CLVA2-03b", "ancien": "du même fichier ne sont **jamais lus**", "nouveau": "du même fichier, et `plancher_p3_<k>` (200 directions de P3, descriptif de T0.7), `plancher_p6_*`, `plancher_concept_<k>`, ne sont **jamais lus**"},
 {"id": "CLVA2-03c", "ancien": "des aires des 200 directions appariées", "nouveau": "des aires des 800 directions appariées"},
 {"id": "CLVA2-03d", "ancien": "**Plancher** : 200 directions de `p`", "nouveau": "**Plancher** : 800 directions de `p`"},
 {"id": "CLVA2-03e", "ancien": "pour chacune des 200 directions", "nouveau": "pour chacune des 800 directions"},
 {"id": "CLVA2-03f", "ancien": "des tau des 200 directions (CLVA-06)", "nouveau": "des tau des 800 directions (CLVA-06)"},
 {"id": "CLVA2-03g", "ancien": "200 exigées", "nouveau": "800 exigées (`n_plancher` de la configuration de T0.7)"},
 {"id": "CLVA2-03h", "ancien": "de leurs 200 directions", "nouveau": "de leurs 800 directions"},
 {"id": "CLVA2-04", "ancien": "∈ {non calculable, incohérent}", "nouveau": "∈ {`non_calculable`, `incoherent`} (littéraux du code, `criteres_v1.py` l. 48)"},
 {"id": "CLVA2-05", "ancien": "`mention_etendue`, par `premier_test_ia.conditions.mesures_action`, la fonction des prédicteurs triviaux de T0.7", "nouveau": "`mention_etendue`, colonne de `mesures-t06.npz` écrite par `t06.test_croise.mention_etendue` (`t06/lanceur.py` l. 285), prédicteur trivial de la configuration de T0.7"},
 {"id": "CLVA2-06", "ancien": "**Champ de T0.7 attendu absent** de son fichier (levées de la contre-lecture 1) : arrêt, nœud.", "nouveau": "**Champ de T0.7 attendu absent** de son fichier (levées de la contre-lecture 1) : arrêt, nœud. Exception écrite : une sonde dont `notation-t07.json` → `resultat.index.sondes[k].etat` n'est pas « notée » (ou, pour une sonde figée de P3, dont `resultat.planchers_figees.etats[<nom>]` n'est pas « établi ») n'a pas de plancher décisif : toutes les lignes de cette sonde sont « non calculables (sonde en échec à l'étape A de T0.7, motif recopié) », dans les pièces R et L, sans arrêt des autres sondes."},
 {"id": "CLVA2-07a", "ancien": "sondes non Mahalanobis et 800 directions", "nouveau": "sondes non Mahalanobis et 3 200 directions (800 par sonde), notées par lots (`plancher_v3.scores_plancher_vectorises`)"},
 {"id": "CLVA2-07b", "ancien": "`premier_test_ia.figees.lire_sondes` et `preparer_sonde` au commit de `CODE-T07`, sans modification", "nouveau": "`premier_test_ia.figees.lire_sondes`, `preparer_sonde` et la notation des directions par lots (`t07/plancher_v3.scores_plancher_vectorises`, avec son contrôle en ligne contre la boucle) au commit de `CODE-T07`, sans modification"},
 {"id": "CLVA2-08", "ancien": "les réserves de T0.7 sur la même sonde, recopiées de E4 → `resultat.reserves_identifiees`", "nouveau": "les réserves déclenchées de T0.7, recopiées telles quelles avec leur motif (entrées `id`, `phrase`, `motif`, parfois `concept` ; la sonde n'y est pas une clé : aucune réserve n'est triée par sonde ; une entrée dont la phrase est « non déclenchée » n'est pas recopiée) de E4 → `resultat.reserves_identifiees`"},
 {"id": "CLVA2-09", "ancien": "T0.7 **brouillon 21**, `brouillons/T0.7-sondes-v0-v1-brouillon21.md`, `f7dcb226efe8671b977ce906c286f7e7243f78a2c9fcf205cbfe5715866ea0cc`, et code du module au commit `8ae9fc44df4599af1e036e979af46aa8fa8f6185` (branche `prep/t07-module-v2`)", "nouveau": "T0.7 **scellé** (candidat 5), `prereg/T0.7-sondes-v0-v1.md`, `d7d180eccbbce8ff2e370f82957543c28f1e564c872f981c7ada403949baade5`, sa configuration v8, `prereg/T0.7-sondes-v0-v1-configuration-t07-v8.json`, `e31c7a79dc1b68d561874d4d42d63b5eb950931f06075927f239c7ad971fb328`, et code du module au commit de la ligne `CODE-T07` (`b4cd9953d199dd8f220f5162e5868c5b00fd392d`, vingt-six modules ; étapes A et B jouées par `t07/lecture_v4.py`, `42f60780e6944568e81880887a1ad87c57a520e8c7d54083b36a43c097a06d06`)"},
 {"id": "CLVA2-12a", "ancien": "statistique `q99` et tolérance 0,2 de la configuration de 7b", "nouveau": "par `repli_v1.garde_equivalence` telle que `repli_recalcul_v1.recalculer` l'appelle (statistique `q99`, tolérance 0,2 et fraction du contrôle négatif 0,95 de la configuration de 7b ; le recalcul rejoue les 576 épisodes de 7b, dont seules les séries R1, R3_d et R6 sont notées)"},
 {"id": "CLVA2-12b", "ancien": "recherche de `c_d`, garde d'équivalence (statistique et tolérance de la configuration de 7b), écriture", "nouveau": "recherche de `c_d`, écriture"},
 {"id": "CLVA2-15", "ancien": "`r/echelle/<dose>`, ", "nouveau": "`r/echelle/<dose>`, `r/mahalanobis-egalite/<sonde>` (essai d'égalité de `preparer_sonde`, mode de calcul lu dans la configuration de T0.7, clé `mahalanobis_calcul`), "},
 {"id": "CLVA2-16", "ancien": "et autres couples : « descriptif » (CLVA-14)", "nouveau": "et autres couples : « descriptif » (CLVA-14) ; `resultat.jeux[sonde]` ne porte que `(i-a)` et les doses jugées, et `resultat.jeux` est nul quand les scores sont fermés : une dose non jugée absente n'est pas un champ manquant"}
]
```

Hors couples (non mécaniques) : CLVA2-01 et CLVA2-10 (décision de la mère) ; CLVA2-09 pour les 23 marques (table) et la phrase de réserve générale de la l. 13 ; CLVA2-11 (section 5) ; CLVA2-13, CLVA2-14 (devis du brouillon 4) ; CLVA2-18.

## 4. Champs fixés par le seul code de T0.7

| champ | ce que T0.7 scellé en dit | ce que le module fait (`main`) | confirmation encore à demander |
|---|---|---|---|
| `scores_<k>`, `plancher_<k>`, `index`, `rang` | **nommés** l. 2789, 2798 (« écrits dans ce texte ») ; forme écrite « (200, n_actions) » : périmée (CLVA2-03) | `lecture_v4.py` l. 218, 239, 259-260 ; forme (800, n_actions) exigée l. 176-178 | non pour les noms ; **forme : 800, par le code seul à cet endroit du texte** (erratum à citer) |
| `plancher.empreintes_deux_premieres` (`notation-t07.json` → `resultat.index.sondes[k]`) | nommé l. 2791, 2798 | `lecture_v4.py` l. 261-262, 544 ; pour une sonde figée : plancher **neuf** | non |
| `fichiers_sondes_neuves` (`sondes.sha256`) | nommé l. 2790, 2798 ; sous-clés non écrites | `lecture_v2.py` l. 788 : `{"sondes": {"chemin", "sha256", "nombre", "planchers"}, "temoins_lexicaux": …}` ; présent à l'étape complète seulement (`lecture_v4.py` l. 503-506) | **oui, légère** : sous-clé `sondes.sha256` (code seul) |
| `meta.planchers`, `meta.principales` de `sondes-neuves-t07.npz` | nommés l. 2793, 2798 | `lecture_v2.py` l. 779-780 | non |
| `scores_ouverts`, `scores_ii_ouverts` | nommés l. 2792, 2798, 2800 | `lecture_v4.py` l. 675 ; `criteres_v1.py` l. 586-600 | non |
| graine `plancher/<nom>` | nommée l. 2794, 2798 | `lecture_v4.py` l. 257, 494 ; sans objet (directions lues) | non |
| littéraux de `entrees.Q` (`non_calculable`, `incoherent`) | prose seulement (l. 1909-1910) | `criteres_v1.py` l. 48 | **oui** (CLVA2-04) |
| `resultat.planchers_figees` (`fichier.chemin`, `fichier.sha256`, `etats`, `paliers`) dans `notation-t07.json` | fichier `planchers-figees-t07.npz` nommé (l. 1206, 1440, 2051) ; **champ JSON non nommé** | `lecture_v4.py` l. 547-550 ; `reextraction_p3_v1.py` l. 550-560 | **oui** (CLVA2-02) ; aucune ligne de registre ne cite ce fichier ni `notation-t07.json` : la chaîne d'empreintes passe par le sceau de `notation-t07.json` seul |
| `meta.planchers[<sonde>]`, noms `<sonde>-t07-plancher-<k>` de `planchers-figees-t07.npz` | noms écrits l. 1206 ; `meta.planchers` non écrit pour ce fichier | `reextraction_p3_v1.py` l. 95, 558-559 | **oui, légère** |
| `plancher_p3_<k>`, `index.sondes[k].plancher_p3`, `planchers_p3_descriptif` | non nommés | `lecture_v4.py` l. 246-249, 678 | non exigée (jamais lus par ce texte ; à nommer dans « Jamais ») |
| `index.sondes[k].etat` (« notée », « échec »), `index.n_plancher`, `plancher.n`, `plancher.source` | non nommés | `lecture_v4.py` l. 218, 240, 261, 268 | **oui** (CLVA2-06) |
| forme de `reserves_identifiees` (`id`, `phrase`, `motif`, `concept`) | champ nommé l. 2792, 2803 ; forme non écrite | `lectures_t07_v1.py` l. 423-463 ; `lecture_v4.py` l. 685 | **oui, légère** (CLVA2-08) |
| clés de `jeux[sonde]` (`(i-a)`, doses jugées) et `jeux[sonde][dose].etat` | « états par sonde et par dose » (l. 2792) | `lecture_v4.py` l. 618-626 ; `criteres_v1.py` l. 51, 57 | non (CLVA2-16 l'écrit) |
| `mention_etendue` (origine) | attribuée à `mesures_action` (l. 1229) : inexact | `t06/lanceur.py` l. 285 ; `t06/test_croise.py` l. 49 | non (CLVA2-05 ; T0.7 n'est pas corrigé) |

**CLVA-17 (ouvertures de `scores-actions-t07.npz`).** T0.7 scellé l. 2804 : « aucune garde de ce texte ne compte les ouvertures de `scores-actions-t07.npz` ; le module écrit une ligne `OUVERTURE-T07` à chaque ouverture des scores […] et ne lit, de son journal, que la **première** ligne `OUVERTURE-T07` de l'étape A d'un run », vérifié par le rédacteur de T0.7 au commit `37485ce5`, « à la place de la confirmation du développeur ». Revérifié par moi sur `main` : seul lecteur du journal `<registre>.ouvertures.md` dans les modules lus : `lecture_v2.premiere_ouverture_a` (l. 240-249, cellule `etape-A/<run>`) ; `registre_v1.journaliser_ouverture` (l. 297-300) ne fait qu'ajouter ; `lecture_v1.ouvrir_scores` (l. 815-837) ne compte rien. **Aucune confirmation ne reste à demander** ; la phrase de la l. 119 (« le développeur du module de T0.7 confirme avant `CODE-VADAPT` ») peut citer T0.7 l. 2804 à la place. Limite : je n'ai pas lu `garde_adaptee_v1.py` ni `journal_p3bis_v1.py` en entier (recherche du motif du journal : aucune occurrence dans `garde_adaptee_v1.py`).

## 5. Pièce HD non jouée en parallèle de 7b

Passages qui supposent HD créée après la création de 7b et jouée pendant sa marche (« Q-1 », R-2207) :

| ligne | passage | état |
|---|---|---|
| l. 8 | « **Q-1** : la pièce HD est créée **après la création** de 7b et court en parallèle de sa marche » | sans objet : 7b est finie |
| l. 26 | « pièce HD : course à part, indépendante des sorties de 7b » | reste vrai |
| l. 113 | « création **après la création de 7b**, en parallèle de sa marche (la lettre de la liste d'arrêt de T0.6 […] est ainsi tenue) […] détruite **avant la création de l'étape A** seulement si l'ordre en vigueur de l'étape A exige un inventaire vide (point ouvert de la mère) » | périmé : plus de création de 7b à protéger ; l'étape A s'est arrêtée (fait donné) et sera relancée |
| l. 112 | étiquette `vadapt-hd-v1`, que la garde d'inventaire du lanceur de 7b ne compte pas | sans objet pour 7b ; reste utile pour l'étape A (T0.7 l. 2806 : étiquettes `t06…` et `t07…` seules) |
| l. 228 | « **Ce qui n'en dépend pas** : la pièce HD entière (R-2177) » | reste vrai |
| l. 229 | calendrier : texte scellé « le 12 au soir », HD « (12 ou 13) », R « (≈ 14 à 17) », L « (≈ 16 à 22) » | **périmé en entier** |
| l. 256 | « Décision sur une pièce (lancer, relancer, abandonner, changer un réglage) prise sur la foi d'une sortie de 7b, de T0.7, de P3-bis » | à tenir plus durement : voir ci-dessous |
| l. 260 | « création qui ferait refuser une création de 7b, de P3-bis ou de l'étape A » | « de 7b » sans objet |
| l. 296-306 | annexe A, variante stricte « HD après la fin de 7b ; R sur l'instance de l'étape A » | la moitié « HD » décrit désormais le fait ; la moitié « R » reste non retenue |

Conséquences si HD se joue après la fin de 7b et après le verdict de P3-bis (je décris, je ne tranche pas) :

1. **Ligne de GO.** La lettre de `GO-2026-11-10-07` (« course à part après la course 7b ») est alors tenue au sens strict pour HD ; la lecture large de R-2207 ne sert plus que pour la pièce R (instance à part). Le devis ne change pas (table de la lecture large) ; le nœud N-VA-1 reste (pire cas ≈ 33,4 USD contre 30).
2. **Échéance.** La ligne échoit le 2026-11-27 ; HD demande 7,4 à 7,6 h attendues (15,2 h au pire), puis R après la poussée de HD **et** de l'étape A de T0.7, qui n'a pas encore produit de scores. Si l'étape A glisse, R glisse ; le repli écrit (l. 114 : « sans sorties de HD, R se joue sans R8 à R11 ») ne couvre pas « sans sorties de l'étape A » : sans elles, aucune pièce R.
3. **Antériorité au verdict de P3-bis.** Le texte exige `SCELLEMENT-VADAPT` strictement antérieure à `VERDICT-P3BIS` (l. 117, 254), sinon « refus de la pièce L, nœud ». Jouer HD après le verdict ne viole pas cette règle si le **texte** est scellé avant ; mais le brouillon 4, sa contre-lecture et son scellement doivent alors passer avant le verdict, ou la règle doit être rouverte (CLVA-08, décision de la mère du 10 novembre). `CODE-VADAPT` postérieure seule : réserve gelée, déjà écrite.
4. **Indépendance de la décision.** Une pièce HD lancée après que l'issue de P3-bis (et peut-être la table A de 7b) est connue doit l'être par un engagement écrit avant, comme celui de la pièce R (l. 114 : « jouée quelle que soit l'issue de P3-bis, de T0.6 et de T0.7 ») : le brouillon 3 n'a pas cet engagement pour HD. Sans lui, la ligne d'arrêt de la l. 256 (« pièce invalide ») est exposée, et un abandon de HD après un verdict défavorable ne se distinguerait pas d'une sélection.
5. **Inventaire.** Plus aucune contrainte de 7b ; restent l'étape A de T0.7 (que T0.7 l. 2806 dit non gênée par une instance du texte de validité) et P3-bis (ordre que je n'ai pas lu).
6. **Annexe A.** À réécrire ou à retirer : elle présente comme « non retenue » une moitié qui devient le fait.

Options d'ordre (pour mémoire, **nœud (Lazar)**) : (a) HD dès le scellement du brouillon 4, avant le verdict de P3-bis si le calendrier le permet — avantage : indépendance de la décision acquise par l'ordre des faits ; inconvénient : contre-lecture, code et `CODE-VADAPT` à finir vite ; (b) HD après le verdict, avec un engagement scellé avant lui de la jouer quelle que soit l'issue — avantage : aucun conflit de compte avec P3-bis ; inconvénient : l'engagement est la seule protection ; (c) HD abandonnée, VA-6 et ses contrôles « non calculables (pièce HD absente) » par le repli écrit — avantage : ≈ 8,5 à 12,5 USD épargnés ; inconvénient : le seul contrôle à chaque dose disparaît (note 2a, verdict, point 3). Recommandation de lecteur, si elle est utile : (b) avec l'engagement écrit, confiance 0,6.

## 6. Non vérifiable (registre interdit à cette contre-lecture)

| fait de registre | phrase du brouillon 3 qui en dépend |
|---|---|
| R-2175 (`registres/decisions.md`) | l. 7 « option (b) de D-1, mot de Lazar, verbatim « Je recommande (b) : go » » |
| `GO-2026-11-10-07` (`registres/go.md`) : plafond 30 USD, échéance 2026-11-27, lettre, conditions | l. 7 ; l. 202 ; coupures 21,0 + 8,5 + 0,5 (l. 225) ; ligne d'engagement (l. 230) |
| `GO-2026-11-10-09` (enveloppe) | l. 7 |
| R-2207 (« go pour la lecture large de GO-07 », 2026-11-10, 12:08 UTC) | l. 8, 113, 114, annexe A ; recoupé seulement par T0.7 l. 2785 et 2806, qui citent R-2207 |
| R-2177 | l. 228 « la pièce HD entière (R-2177) », l. 229 « scellé le 12 au soir (R-2177) » |
| R-2194 à R-2198, R-2210 | journal du brouillon 3, § 1 (R-2210 n'est cité ni par le brouillon 3 ni par son journal) |
| passation `registres/passations/2026-11-10-1113.md` (`64d321cf…`) | l. 3 |
| ligne `CODE-T07`, fichier `registres/code-t07/CODE-T07-v2.json` (`d5eb0b66…`), commit C7 | renvois « au commit de `CODE-T07` » (l. 71, 239) ; connu par T0.7 l. 695 seulement |
| lignes `SCORES-T07`, `SONDES-T07`, `VERDICT-P3BIS`, `RUN-CONFIRMATION-T06` : présence, dates | plan, point 4 ; antériorité de `SCELLEMENT-VADAPT` à `VERDICT-P3BIS` (l. 117) — **je ne sais pas si `VERDICT-P3BIS` est inscrite à ce jour** |
| R-2588, R-2589 (arrêt de l'étape A), fin de 7b le 12 novembre, décision D-11 du plan, erratum des 200 directions | faits donnés par la consigne, § 2 ; non relus |
| interdits communs v2 (`1ee3b370…`), rapport des prémisses (`2638558e…`) | l. 11, 15 ; l. 141 (§ 2b) : non lus |
| code de T0.6 au commit `1609a4bf` (`session_v2.py` l. 140-155, `lancer_t06_v13.sh` l. 222-224) | l. 16, 112 : commit absent du clone |

## 7. Limites

- T0.7 scellé (754 ko) lu par sections et par motifs, pas en entier : sections « Plan d'analyse » (hors l. 1440-1453), « Écrits exigés par P3-bis », « Liste d'arrêt », « Module » lues par extraits seulement. La garde adaptée (N-066) n'a pas été relue : je n'ai pas vérifié si une ouverture réduite de P3-bis change ce que ce texte doit lire au-delà de R14.
- Module : `lecture_v1.py`, `lecture_v3.py`, `sondes_neuves_v1.py`, `plancher_v2.py`, `plancher_v3.py`, `reextraction_p3_v1.py`, `repli_v1.py`, `garde_adaptee_v1.py` lus par extraits ou par motifs. Aucun essai joué ; aucun code de ce texte n'existe.
- Les dix-huit empreintes du candidat 1 n'ont pas été comparées au fichier `CODE-T07-v2.json` (registre interdit) ; sept d'entre elles sont retrouvées dans T0.7 l. 695 ; l'égalité de l'arbre de travail avec `main` vient de `git diff --stat main` (vide) sur `src/controle_ia/t07` et les deux fichiers de `premier_test_ia`. Commits `8ae9fc44`, `37485ce5`, `0d0c5da4`, `a621dcd3`, `1609a4bf` absents du clone : numéros de ligne donnés sur `main`, pas à ces commits.
- Plan multi-comptes (`3b1bda25…`) non lu (hors de la table des fichiers de la consigne) : la section 5 décrit le cas « HD après 7b et après le verdict de P3-bis » d'après la seule phrase de la consigne.
- Journal du brouillon 2, note 2a (au-delà de la l. 40), T0.6 scellé (hors lignes citées), les deux vérifications de T0.7 : non relus. Le script du devis du journal du brouillon 3 n'a pas été rejoué tel quel ; sa formule est reprise dans mon script (mêmes sorties : 8,69 et 33,2).
- Puissance sous la règle (a) : calcul par formule avec un rapport d'écart type supposé (1,10) ; aucune simulation.
- Aucun refus de permission, du crochet de garde ni d'un classifieur pendant cette contre-lecture ; aucune commande bloquée.
- Contre-lecteur du même modèle que la contre-lecture 1 (section 0).

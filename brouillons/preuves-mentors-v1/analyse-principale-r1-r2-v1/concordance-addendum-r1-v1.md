# Concordance de l'addendum de relance de R1 avec nos deux analyses scellées — v1

**écart de fond : nœud de Lazar (N-A : la ligne gelée « épisode conforme à trajectoire différente → rejeu non validé : rien n'est lu », recopiée dans l'analyse principale l. 146, vaut encore pour les 7 épisodes que la relance garde ; l'addendum ne la remplace que chez le fournisseur) — pour le reste, concordant si l'addendum change (C-1 à C-6)**

- Lecteur : sous-agent neuf (Claude, Opus 5.5), règle R2. Je n'ai écrit ni l'addendum, ni le texte du fournisseur, ni nos deux analyses, ni leur code, ni leurs contre-lectures, ni le rapport de concordance antérieur.
- Date : 2 novembre 2026, ≈ 03:05–03:45 UTC.
- Pièces lues (texte et code seulement ; aucune donnée de R1, R2 ni R4 ; aucune branche `calcul/…` ouverte ; aucun `git fetch`) :
  - addendum, brouillon 1 : `git show origin/prep/r1-relance-addendum-v1:prereg/R1-addendum-relance-v1.md`, sha256 **`ab94755675725193c7d716bafde83ec5b6efc48b2034e625d38b461d22e1abe2`** (vérifié) ; table `prereg/R1-table-tokenisation-v1.json` `5309326b…` (vérifié ; clés et `comptes` seulement) ; configuration v3 (comparée à la v2 : cinq clés ajoutées, rien d'autre) ; `docs/notes/runs-r1-r2-r4-v1/comptes-table-relance-v1.json` (comptes sur processeur, sans score) ;
  - code du fournisseur au commit `5b72e2e2` : `runs_nuit/rejeu_activations_v2.py` (abrégé « v2 » ci-dessous), `rejeu_activations_v1.py` (empreinte `dde8aa67…`, **identique** à celle que cite la principale : non modifié depuis `29bd8e2e`), `alignement_v1.py`, `tests/test_runs_nuit_v2.py` ; scripts `r1_relance_instance_v2.sh` ;
  - texte parent `git show 567260c0:prereg/R1-R2-rejeu-p3-v1.md` (`80c85a00…`, vérifié) ;
  - principale : `git show 83ce7a91:prereg/analyse-principale-r1-r2-v1.md` (`8e267952…`, vérifié) ; code au commit `a8b7fdb2` (sept modules du paquet : empreintes égales à la liste fermée, vérifiées) ;
  - secondaire : `git show 7a238666:prereg/analyse-blanche-noire-v3.md` (`1f6a6da2…`, vérifié) ; code au commit `326601cf` (`entrees_v3`, `constantes_v3`, `lecture_v3`, `entrees` : empreintes égales à sa liste fermée, vérifiées) ;
  - messages n° 339 (`05179024…`), n° 250 (`c3632040…`), n° 251 ; rapport d'enquête (section 2) ; `concordance-r1-r2-v1.md` ; registre, lignes R-1103 et R-1108.
- Abréviations : « P » = texte scellé de la principale (`83ce7a91`), « S » = texte scellé de la secondaire (`7a238666`), « F » = texte parent du fournisseur (`567260c0`), « A » = addendum (brouillon 1) ; « l. » = numéro de ligne du fichier tel que `git show … | cat -n` le donne.

## En bref (une ligne chacun)

- **Formats** : le R1 relancé par la v2 produit exactement ce que lisent le texte et le code des deux analyses ; la clé `tokenisation` est tolérée par les deux ; le nom `activations-p3-rejeu-v1` est celui qu'elles exigent.
- **P-R5 contraire** : la principale lit tout (ni arrêt, ni « rien n'est lu ») et rapporte P-R5 sans verdict ; la secondaire ne lit pas son bras boîte blanche (i) sur R1 (garde « plus de 10 % d'actions non fidèles »), le reste est lu.
- **Voie alternative** : admise par nos deux textes sans écart, comme la voie de l'addendum ; c'est elle qui garde le sens de `fidele` sur lequel nos textes ont été scellés ; aucune des deux ne lève N-A.
- **R4** : l'addendum ne porte pas sur R4 ; la secondaire lit R4 tel que scellée, avec `R4.activations` nul (bras (i) non lu à la dose R4).
- **N-A** (nœud) : ligne l. 146 de la principale. **N2** (antérieur, toujours ouvert, R-1103) : bras « moyenne » en tête de la famille de la secondaire, à trancher avant toute lecture d'un R1 relancé.

## 1. Formats

### 1.a Ce que lit la principale, et ce que la v2 écrit

| Exigence (texte P, code `a8b7fdb2`) | Ce que fait la v2 (`5b72e2e2`) | Concordant |
|---|---|---|
| Résultat `diag/<run>/rejeu-activations.json`, scellé, rattaché à son manifeste (P l. 102 ; `entrees_v1.py` l. 177-181, `verifier_resultat`) | `creer_manifeste` puis `ecrire_resultat(racine, chemin_m, "rejeu-activations", resultat)` (v2 l. 138-140, 379), comme la v1 | oui |
| `verdict_fidelite` = « conforme », sinon arrêt (P l. 175 ; `entrees_v1.py` l. 183-184) | « conforme » quand la course va au bout (v2 l. 349), y compris avec ≤ 10 épisodes non résolus | oui |
| `regle_repli_appliquee` booléen (`entrees_v1.py` l. 185-186) | `bool(repli)` (v2 l. 349) | oui |
| `couches` = [7, 15, 23] (l. 187-188) | config v3 `couches` = [7, 15, 23] (v2 l. 353) | oui |
| `textes_sha256` = `ba05fa13…` (l. 189-190) | `verifier(chemin_textes)` ; config v3 `textes_sha256` = `ba05fa13…` (v2 l. 351) | oui |
| `identite_sha256` = `1f25adbd…` (l. 191-192) | empreinte calculée et comparée à la config v3, `1f25adbd…` (v2 l. 129-132, 352) | oui |
| `fichiers` : nom → empreinte des trois fichiers (l. 193-199) | `fichiers[p.name] = sceller(p)` (v2 l. 337-346) | oui |
| Noms exacts `activations-p3-rejeu-v1.npz`, `…-maximum.npz`, `…-complement-hors-cout.npz` (`constantes_v1.py` l. 44-45 ; contrôle du nom de base, `entrees_v1.py` l. 196) | `nom_sortie` = `activations-p3-rejeu-v1` (config v3) + suffixes (v2 l. 338-345) | oui |
| Tableaux `moyenne` / `maximum` / `maximum_hors_cout` et communs `jetons_empan`, `jetons_empan_rejeu`, `couches`, `conforme_longueur`, `contexte_conforme`, `ecart_fidelite`, `fidele`, `trajectoire_identique`, `activations_identiques` + identité (`constantes_v1.py` l. 46-48 ; `entrees_v1.py` l. 203-206) | dictionnaire `commun` (v2 l. 332-336), identité `CLES_IDENTITE` = (`episode`, `pas`, `condition`, `tache`) (`alignement_v1.py` l. 18) | oui |
| Forme (2 400, 3, 4 096) (l. 208-209) | `np.full((n, d, largeur), nan, float16)` (v2 l. 282-284) | oui |
| Communs égaux entre les trois fichiers (l. 210-213) | le même `commun` écrit dans les trois (v2 l. 339-345) | oui |
| `jetons_empan` = `jetons_notes` de P3 (l. 217-219) | `identite["jetons_notes"]` recopié (v2 l. 333) | oui |
| `fidele`, `contexte_conforme`, `conforme_longueur`, `trajectoire_identique` booléens (l. 220-222) | tableaux `np.zeros(n, dtype=bool)` et combinaisons booléennes (v2 l. 196-197, 212, 245-248, 326) | oui |
| Fiche de réception : `R1` = {`moyenne`, `maximum`, `complement`, `resultat`} ou nul avec motif ∈ {`rejeu_non_conforme`, `rejeu_en_echec`} (P l. 97 ; `entrees_v1.py` l. 26-53 ; `constantes_v1.py` l. 95) | un arrêt écrit « non conforme » (fidélité, contrôle négatif, plus de 10 non résolus) ou « echec » (table fausse, toute autre cause) (v2 l. 146-151 ; A l. 127-128) : les deux motifs fermés suffisent | oui |

Le fournisseur l'éprouve lui-même contre la v1 (`tests/test_runs_nuit_v2.py` l. 102-131 : `set(r1) <= set(r2)`, mêmes fichiers `.npz`, mêmes noms, formes et types de tableaux).

**Clé ajoutée `tokenisation`** : **tolérée**. La principale ne contrôle l'ensemble exact des clés que pour la fiche (`entrees_v1.py` l. 42, l. 50, l. 61, l. 68 : `set(…) != …`) ; dans le résultat du rejeu, elle ne lit que par `r.get(…)` (l. 183-193 ; `lecture_v1.py` l. 245-246) ; dans les `.npz`, elle ne vérifie que la présence des tableaux exigés (l. 203-205). Aucun refus de clé inconnue. (`lecture_v1.py` l. 245-246 lit aussi une clé `trajectoires` qui n'existe ni en v1 ni en v2 : `None`, sans effet, antérieur à l'addendum.)

### 1.b Ce que lit la secondaire

- `…-moyenne.npz` = `activations-p3-rejeu-v1.npz` : `moyenne` (2 400, 3, 4 096) finie sur **toutes** les actions, `jetons_empan`, `jetons_empan_rejeu`, `fidele`, identité égale (S l. 141 ; `entrees_v3.py` l. 106-113) : la v2 les écrit (v2 l. 333-341). `…-maximum.npz` facultatif (l. 121-131).
- Faits lus par pointeurs dans `rejeu-activations.json` : `fidelite_conforme` → `verdict_fidelite`, `regle_repli` → `regle_repli_appliquee`, `textes_sha256`, `couches` (S l. 139 ; `entrees_v3.py` l. 114-120 ; `entrees.py` l. 24-27, 223-239) : ces clés sont gardées au même endroit par la v2 (l. 349-353) ; `fidelite_echantillon` et `fidelite_toutes` ont les mêmes sous-clés que la v1 (v2 l. 305-307, 359-366 ; test l. 119).
- **Clé `tokenisation` tolérée** : la liste fermée porte sur les **noms de pointeurs de la fiche** (`entrees_v3.py` l. 52-56 : `set(e["pointeurs"]) - ptr`), pas sur les clés du JSON ; `_faits` ne résout que les pointeurs listés. Aucun refus.
- Toute action dont l'empan rejoué est vide garde `moyenne` non finie (v2 l. 287-288, comme la v1) et arrêterait la secondaire (`entrees_v3.py` l. 112-113) : inchangé par l'addendum ; les 70 actions des épisodes non résolus sont rejouées et ont des activations finies (v2 l. 272-302).

### 1.c Nom de sortie et branche

- **Nom inchangé `activations-p3-rejeu-v1` : il convient, et il est exigé** (P l. 60-61 et `constantes_v1.py` l. 44-45 ; S l. 141). R12 est tenue par le dossier de run neuf (`donnees/<run>/`, `mkdir(exist_ok=False)`, v2 l. 330-331) ; la première course n'a écrit aucun fichier d'activations. Le changer serait un écart.
- **Branche de résultats : écart de procédure.** A l. 130 et le script (`r1_relance_instance_v2.sh` l. 24, 36) versent R1 relancé sur `calcul/r1-relance-reel-v1` ; la principale prescrit `git fetch origin calcul/r1-r2-reel-v1` « (seule refspec) » (P l. 96 ; aussi l. 94). Le script refuse une branche existante (l. 71-76) : verser directement sur `calcul/r1-r2-reel-v1` n'est pas possible sans le modifier. Voir C-2. La secondaire n'exige qu'une refspec explicite (S l. 135) : pas d'écart chez elle.

## 2. P-R5 contraire (moins de 90 % des actions notées fidèles)

### Principale : lecture complète, P-R5 rapportée sans verdict

- Texte : P-R5 est « lu dans les résultats du fournisseur » (P l. 48) ; « prédictions P-R1 à P-R5 : observé à côté du prédit, sans verdict propre » (P l. 161). Aucune ligne de la table gelée ne porte sur 90 % (P l. 144-159). Le seul critère de part des fidèles est la couverture : « sous 0,80 pour le saboteur ou l'honnête : non concluant (rejeu partiel) » (P l. 82, l. 148 ; Métrique 11, l. 73).
- Code : arrêt seulement si `verdict_fidelite` ≠ « conforme » (`entrees_v1.py` l. 183-184) — or la v2 écrit « conforme » quel que soit P-R5 (v2 l. 349) ; « rien n'est lu » seulement si la fiche porte `R1: null` (`lecture_v2.py` l. 110 ; `lecture_v1.py` l. 289-291) ; `partiel` = couverture du saboteur ou de l'honnête sous 0,80 (`lecture_v1.py` l. 295 ; `constantes_v1.py` l. 86) ; P-R5 observé = `notees_fideles_part` (l. 242), rapporté dans `predictions` (l. 407-408), **sans réserve écrite**.
- Donc : **ni arrêt, ni « rejeu non validé »** ; lecture complète ; « non concluant (rejeu partiel) » seulement si la couverture tombe sous 0,80 (bornes hautes de la voie de l'addendum : honnête 538/600 = 0,897, saboteur 546/600 = 0,91, `comptes-table-relance-v1.json`).
- Le texte parent ne faisait pas non plus de P-R5 une cause de « non validé » (F l. 93 ; table F l. 176-193). La ligne 3 de la table de l'addendum (A l. 175, « réserve d'instrument (P-R5 contraire), rapportée ; les critères du parent s'appliquent ») ne change aucune classe et va dans le même sens ; mais **la principale n'écrit pas cette réserve** : elle rapporte seulement la valeur observée. Écart de forme, non de fond : C-3.

### Secondaire : bras (i) non lu sur R1, le reste lu

- Texte : « actions non fidèles selon le fournisseur (`fidele`, exigé) au plus 10 % (au-delà : raté ; en deçà : réserve ; elles restent dans tous les bras…) » (S l. 154) ; « plus de 10 % d'actions non fidèles : (i) non lu » (S l. 224-225).
- Code : `NON_FIDELES_MAX = 0.10  # … (sa prédiction : au plus 10 %)` (`constantes_v3.py` l. 54) ; `part = mean(~fidele)` sur les 2 400 actions, au-delà : motif (`entrees_v3.py` l. 159-164) ; tout motif retire `i`, `i_sh`, `i_max` (`lecture_v3.py` l. 47, 248-252). Ce n'est pas un arrêt : (ii), (iii) et (L) restent lus ; dans sa famille de Holm, (i) − (ii) et (i) − (L) deviennent « non lue ».
- Les 2 400 actions étant toutes notées, **P-R5 contraire ⇔ plus de 10 % d'actions non fidèles**, bornes comprises (2 160 fidèles = 90,0 % : P-R5 tient et la garde aussi). **La garde de la secondaire est exactement P-R5.**
- Conséquence sous la voie de l'addendum : au moins 234 non fidèles (9,75 %) ; la garde saute dès que plus de 6 des 454 actions conformes hors contexte exact sortent de la tolérance — **probabilité ≈ 0,7 selon le fournisseur lui-même** (A l. 65-66). Sous la voie alternative : au moins 164 (6,83 %), il en faut plus de 76 sur 524. C'est la marge sous laquelle la secondaire a été scellée (F l. 65-66 et l. 93 : « au plus 93 % » ; S l. 154 cite le contrôle préalable 2 236 / 2 400).

## 3. Voie alternative (épisodes non résolus traités comme les 89 épisodes non conformes en longueur, la tolérance tranchant action par action)

- **Principale — admise sans écart.** Le texte ne définit pas `fidele` : « éligible = notée par P3 … et `fidele` dans le fichier de R1 ; la même exclusion vaut pour tous les bras » (P l. 57 ; Concordance A, l. 193). Les deux voies tiennent cette lettre (exclusion action par action, même ensemble pour tous les bras). Sous l'alternative, une action d'épisode non résolu dans la tolérance entre dans la lecture principale et sort de la sensibilité « contexte exact » (`contexte_conforme` faux) : exactement ce que le parent prescrit pour toute action hors contexte exact (F l. 171-174 ; P l. 74 et l. 149). Le sens de `fidele` que la principale recopie est celui du parent : la tolérance (F l. 99, l. 130-134), avec la règle de repli pour le cas où elle ne discrimine pas (F l. 138-142).
- **Secondaire — admise sans écart.** Elle garde les épisodes entiers quel que soit `fidele` (S l. 154, l. 224) ; `fidele` n'entre que dans sa garde de 10 % (point 2).
- **Le n° 339 n'est pas un texte scellé.** « Actions de ces épisodes à `fidele` = faux » était une demande de conv-audit (n° 339, l. 7 : « Ton addendum devrait donc écrire… »), non une exigence de la principale scellée. **L'addendum se trompe en écrivant (A l. 76-79) que cette exclusion est « comme l'exige l'analyse principale scellée de conv-audit »** : la principale exige l'exclusion par `fidele`, la même pour tous les bras, rien de plus (C-1).
- **Laquelle est concordante ?** À la lettre, **les deux**. Au sens de nos textes, **la voie alternative** :
  - elle garde la distinction du parent entre « fidèle » (la tolérance) et « contexte exact » (sensibilité), que la voie de l'addendum confond pour 70 actions (A l. 49-51 : « n'est pas en contexte exact et n'entre pas dans les actions fidèles ») ;
  - elle rend à P-R5 la borne du parent (2 236 / 2 400 = 93,2 %, F l. 93) : l'addendum n'aurait plus à modifier P-R5 ;
  - elle garde à la secondaire la marge de 76 actions avec laquelle sa garde a été fixée, au lieu de 6.
- Argument contraire, écrit pour la symétrie : la divergence des 7 épisodes n'est pas expliquée (15 des 22 l'ont été à l'octet ; hypothèses seulement pour les 7, rapport d'enquête, section 2) ; la voie de l'addendum est plus proche de la prudence de la ligne remplacée. Réponse : la tolérance et le contrôle négatif sont précisément l'instrument du parent pour juger une action hors contexte exact ; si le contrôle négatif ne discrimine pas, la règle de repli exclut déjà ces épisodes (`fidele &= traj`, v2 l. 327-328). **Recommandation : la voie alternative ; confiance ≈ 0,6.**
- **Aucune des deux voies ne lève N-A** (point 6) : les 7 épisodes restent « conformes en longueur à trajectoire différente ».

## 4. Sens des champs des 70 actions (7 épisodes non résolus) — voie de l'addendum

Valeurs écrites par la v2 : `fidele` = faux (l. 326 : `& ~non_conforme_b`) ; `contexte_conforme` = faux (l. 248) ; `trajectoire_identique` = faux (l. 218) ; `conforme_longueur` = vrai (l. 205-206) ; `ecart_fidelite` calculé et fini (l. 300-302) ; activations calculées et finies (l. 285-299). Répartition : honnête 3 épisodes (30 actions), saboteur 1 (10), témoin 2 (20), mention 1 (10) (`comptes-table-relance-v1.json`, `episodes_non_conformes_B`).

**Principale**
- Éligibilité : non éligibles (`eligible = notee & fidele`, `lecture_v1.py` l. 202-205) ; donc hors de l'entraînement de W et de T, hors du calibrage et du test de tous les bras (`calcul_v1.py` l. 60-92) ; la garde « activation non finie » ne les regarde pas (`lecture_v1.py` l. 206 ; `entrees_v1.py` l. 226-231).
- Couverture : comptées dans les non-éligibles (`lecture_v1.py` l. 215) ; −30 actions honnêtes, −10 du saboteur.
- Exclusions : comptées en « notées non fidèles » (l. 217 et l. 225), non en « hors contexte exact » (qui compte les **éligibles** hors contexte, l. 219, l. 226) ; elles ne sont pas distinguées des actions hors tolérance (la liste des épisodes est dans `tokenisation`, v2 l. 371).
- Sensibilité « contexte exact » : hors (`eligible & contexte`, l. 232-233), comme elles l'auraient été de toute façon par `contexte_conforme` faux.
- `conforme_longueur` et `trajectoire_identique` : lus seulement comme booléens exigés (`entrees_v1.py` l. 220-222) ; aucun effet.
- P-R5 observé : comptées notées non fidèles (`lecture_v1.py` l. 242).

**Secondaire** (épisodes entiers gardés)
- Les 70 actions entrent dans tous ses bras, avec des activations calculées dans un contexte qui n'est pas exactement celui de P3 : c'est son écart déclaré n° 7 (« actions non fidèles gardées », P l. 227 ; S l. 154, l. 224).
- `fidele` faux : comptées dans `part_non_fideles` (`entrees_v3.py` l. 159-164) → plancher 234 / 2 400 (point 2).
- `conforme_longueur` vrai ⇒ `jetons_empan_rejeu` = `jetons_notes` : non comptées dans la part de longueur différente (l. 150-158 ; plancher inchangé, 164 / 2 400).
- `contexte_conforme`, `trajectoire_identique` : non lus (seuls `moyenne`, `jetons_empan`, `jetons_empan_rejeu`, `fidele` le sont, l. 106).
- Identité de linéarité (couche 15, toutes les actions de longueur non nulle, l. 171-200) : elles y entrent sous les deux voies (mêmes activations) ; la voie ne change rien ici.

**Sous la voie alternative**, seul `fidele` change pour ces 70 actions (la tolérance décide) : les éligibles hors contexte exact augmentent d'autant, la sensibilité est inchangée, la couverture remonte au plus à 568 / 600 (honnête) et 556 / 600 (saboteur), les bornes du parent.

**Réserve sur `contexte_conforme`, antérieure à l'addendum** : pour les 89 épisodes non entièrement conformes en longueur, `contexte_conforme` est vrai sur le préfixe d'actions conformes en longueur (v1 l. 356-360 ; v2 l. 204-208), **sans aucune vérification par empreinte** (P3 n'a gardé qu'une empreinte de trajectoire par épisode, différente pour ces épisodes de toute façon). Or la cause établie de l'arrêt est un redécoupage de même longueur, invisible à la longueur. Les 1 712 actions « en contexte exact » comprennent 272 actions de ces préfixes (1 712 − 1 440) ; certaines peuvent suivre un redécoupage caché (nombre non mesurable ici). La sensibilité « contexte exact » de la principale (P l. 74) lit donc « préfixe conforme en longueur, ou épisode à trajectoire identique », non « contexte exact » au sens strict. L'addendum (A l. 47-51, l. 62-63) l'appelle « contexte exact » : C-5.

## 5. R4

- **L'addendum ne s'applique pas au rejeu de R4** : « Il porte sur R1 seule » (A l. 29-30) ; configuration et code ne nomment que R1. Le rejeu de R4 s'est arrêté sur la même garde (n° 250, l. 7-8 : 12 épisodes) ; aucun `activations-r4-rejeu-v1.npz` n'existe.
- **La secondaire peut lire R4 telle que scellée.** Sa fiche admet `R4.activations` « au format de `R1`, ou `null` » (S l. 139 ; `entrees_v3.py` l. 47-56) ; le code charge les activations de R4 seulement si l'entrée n'est pas nulle (`lecture_v3.py` l. 578) et écrit sinon « activations de P3 ou de R4 absentes » pour le bras (i) (l. 414) ; (L), (iii) (sondes génériques de R4) et `L0` restent lus (l. 416-436 ; S l. 143). La condition d'ordre (« `R4` non nul seulement si le verdict de dose est scellé », S l. 143) est remplie selon le n° 251 (point 2). La réplication sur R4 ne porte que sur les comparaisons établies sur P3 (S l. 143) : sans (i) sur R4, aucune comparaison avec (i) n'y est répliquée.
- Si R4 est un jour rejoué à nouveau, il faudra un addendum propre à R4 et une concordance neuve. La fiche de la secondaire gagnerait à citer dans `redaction` l'`arret.json` du rejeu de R4 (chemin et empreinte) ; le texte ne l'exige pas pour R4 (il l'exige pour `R1` nul, S l. 139).

## 6. Écarts de fond et changements demandés

### Nœud de Lazar (fond)

- **N-A — ligne 146 de la principale.** Le texte scellé de la principale recopie « ligne à ligne » (P l. 142) la ligne du parent : « Fidélité contraire, ou épisode conforme à trajectoire différente | Rejeu non validé : rien n'est lu » (P l. 146 ; F l. 180), et rattache ce que fait le code au verdict du fournisseur (« verdict ≠ « conforme » … ou arrêt »). L'addendum remplace cette ligne **dans le parent seulement** (A l. 168-177) et garde la course, verdict « conforme », avec 7 épisodes encore conformes en longueur à trajectoire différente (A l. 56-59, l. 112-114). Le code de la principale lira (verdict « conforme ») ; **la table gelée de la principale dit « rien n'est lu »** pour l'issue observée ; le sous-agent du verdict (R13), qui applique cette table (P l. 107), serait devant une contradiction. Aucune des deux voies (point 3) ne l'évite. **L'addendum ne peut pas le lever seul**, sauf si la règle A résout les 7 épisodes (C-6). Sinon, il faut une décision de Lazar. Options :
  - (a) **Une seule décision de Lazar**, celle qui approuve l'addendum, étend expressément le remplacement de la ligne à sa copie dans la principale (l. 146), le reste de la principale inchangé (code, graines, premier passage) ; consignée au registre et donnée au lecteur R13. Avantage : rien à réécrire, aucun délai. Inconvénient : un texte scellé lu à travers une décision.
  - (b) Addendum court à la principale (remplacement de la ligne, rien d'autre), contre-lu et scellé avant toute récupération. Avantage : texte propre. Inconvénient : une contre-lecture et un scellement de plus, ≈ 1 heure.
  - (c) Faire d'abord C-6 (sur processeur) ; si les 7 épisodes sont résolus, N-A disparaît ; sinon, (a).
  - Recommandation : (c) puis (a) ; confiance ≈ 0,6. Le rapport antérieur l'annonçait déjà (`concordance-r1-r2-v1.md`, réserve 2 : une relance « vient avec un texte neuf du fournisseur (ligne 180) »).
- **N2 (antérieur, non créé par l'addendum, toujours ouvert)** : bras (i) de la secondaire sur la moyenne en tête de sa famille de Holm, contre la lettre « tout emploi de `moyenne` hors du bras de diagnostic est un nœud » (F l. 36-37) ; R-1103 : « à trancher avant toute lecture d'un R1 relancé ». Il redevient actif avec la relance.
- **Rappel (AP-5, antérieur)** : une action éligible dont tout l'empan est dans le champ COST garde `maximum_hors_cout` non fini (v2 l. 293-299, comme la v1) et arrêterait la principale après son manifeste. Inchangé par l'addendum.

### Changements demandés à l'addendum (encore non scellé)

- **C-1 (exactitude, requis)** : corriger A l. 76-79. La principale scellée n'« exige » pas `fidele` = faux pour ces épisodes ; elle exige l'exclusion par `fidele`, la même pour tous les bras (P l. 57). La demande venait du n° 339, que conv-audit peut retirer. **Recommandé** avec C-1 : la voie alternative (point 3) — `fidele` tranché par la tolérance, `contexte_conforme` et `trajectoire_identique` faux ; P-R5 rendu au parent (≥ 90 %, au plus 93 %) ; v2 l. 326 sans `& ~non_conforme_b` (code, tests et commit cité à refaire). Si le fournisseur garde sa voie : écrire que P-R5 contraire coûte à la secondaire son bras (i) sur R1 (`constantes_v3.py` l. 54), pour que Lazar décide en le sachant.
- **C-2 (procédure, requis pour éviter un écart à P l. 96)** : après la course, verser aussi le run de R1 relancé (`runs/<run>/`, `diag/<run>/`, `donnees/<run>/` et leurs compagnons, à l'octet) sur `calcul/r1-r2-reel-v1` par un commit neuf, sans rien y réécrire, et donner ce commit. La garde « branche existante » du script (`r1_relance_instance_v2.sh` l. 71-76) reste intacte. À défaut, aller chercher une seconde refspec serait un écart à notre texte scellé (décision à demander).
- **C-3 (forme)** : à la ligne 3 de la table (A l. 175), préciser que la réserve P-R5 est portée par le résultat du run (`tokenisation.p_r5_au_moins_90_pour_cent`, v2 l. 374-375) et par la lecture du fournisseur, et qu'elle ne change aucune classe ni aucune ligne des analyses de conv-audit (la principale la rapporte en « observé », sans réserve, P l. 48, l. 161).
- **C-4 (pour N-A, requis)** : écrire dans l'addendum que la ligne remplacée est recopiée dans la principale scellée de conv-audit (P l. 146, `8e267952…`), que le remplacement n'y vaut que par décision de Lazar, et proposer que la décision sur l'addendum la couvre (option (a)).
- **C-5 (clarté)** : définir `contexte_conforme` tel que la v2 l'écrit (préfixe conforme en longueur ; pour un épisode entièrement conforme, trajectoire identique après la table), et déclarer que, pour les 89 épisodes non conformes en longueur, le préfixe n'est vérifié par aucune empreinte (272 actions) ; ne plus l'appeler « contexte exact » sans cette réserve (A l. 47-51, l. 62-63).
- **C-6 (facultatif, lève N-A à la racine)** : avant la carte, étendre la recherche déterministe de la règle A aux hypothèses 1 à 3 du rapport d'enquête (trois redécoupages ou plus ; fenêtre de trois jetons ; jeton de fin combiné à un redécoupage), dans un ordre fixe, l'empreinte de P3 restant seule juge (une égalité d'empreinte sha256 ne laisse aucun choix libre). Si les 7 épisodes sont résolus, la règle B ne sert pas, N-A tombe et P-R5 retrouve sa borne de 93 % quelle que soit la voie. Sinon, rien n'est perdu.
- **C-7 (R4)** : écrire que le rejeu de R4 n'est pas relancé par cet addendum (ou le sera sous un addendum distinct), pour que la fiche de la secondaire écrive `R4.activations: null` sans avoir à choisir.

## Annexe — ce que je n'ai pas fait

- Aucune donnée de R1, R2 ni R4 ; aucune branche `calcul/…` lue ; aucun `git fetch`, aucun commit, aucune clé lue ; aucun calcul autre que des empreintes et des différences de configuration ; aucun fichier existant modifié. Pas de fichier compagnon `.sha256` (consigne : un seul fichier neuf) ; à sceller par la session.

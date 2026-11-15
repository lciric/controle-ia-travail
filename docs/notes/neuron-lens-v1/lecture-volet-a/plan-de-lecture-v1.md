# Plan de lecture du volet A de « Neuron Lens » — v1

Écrit le 2026-11-15 après 03:09 UTC (relevé de `date -u`), **avant d'ouvrir un seul fichier de résultat**. Lecteur neuf : je n'ai écrit
ni le texte gelé, ni le code, ni la course. Copie détachée `/home/user/lecture-neuron-lens-v1`, tête `ec77e764`.

## Ce que j'ai lu avant d'écrire ce plan

- Le texte gelé en entier : `docs/notes/neuron-lens-v1/texte-gele-volet-a-et-b-alpha-v6.md`, empreinte `34b88243…` vérifiée par son
  compagnon (`sha256sum -c` : conforme).
- Le code de la course, **pour connaître le nom des champs seulement** (aucun résultat) : `src/controle_ia/neuron_lens/volet_a_course_v4.py`,
  `volet_a_lectures_v2.py`, `volet_a_sondes_v2.py`, `decisions_volet_a_v4.py`, `volet_a_lancer_v3.py`, et le début de `volet_a_donnees_v1.py`
  (arbre des graines). Je n'importe **aucun** de ces modules dans mon calcul : mon programme réécrit chaque règle à partir du texte gelé.
- Les noms et tailles des fichiers de `diag/20261114-165239-neuron-lens-volet-a/` et de `runs/20261114-165239-neuron-lens-volet-a/`
  (liste du dossier ; aucun contenu ouvert).

Je n'ai lu aucune passation, aucun journal de course, aucune contre-lecture, aucun autre `diag/` ni `runs/`.

## Ordre

1. Empreintes des six fichiers de `diag/20261114-165239-neuron-lens-volet-a/` (`sha256sum -c NOM.sha256`, dans le dossier) et du manifeste
   `runs/20261114-165239-neuron-lens-volet-a/manifeste.json`. **Une empreinte fausse : arrêt, je le dis, rien d'autre n'est lu.**
   Dans le manifeste et dans `releve-fichiers.json`, je lis : identifiant du run, commit, empreinte du texte gelé citée (`34b88243…` attendue),
   graines (entropie 20261114 attendue), nombres de tirages (200, 20, 2 000), versions, empreintes des résultats rattachés (comparées aux
   compagnons). Un écart : je le rapporte, je n'arbitre pas.
2. **Cas sains d'abord** : `brut-cas-sains.json`, et rien d'autre tant qu'ils ne sont pas jugés.
   - (i) `i_owl` : booléen de la course et liste des 10 formes décodées (jetons gardés). Je **rejoue la règle sur la liste** : une forme (sans
     espace ni casse) commence par « owl » ou « noct », ou vaut « night ».
   - (ii) `ii_german` : booléen et liste des 10 formes ; je rejoue : une forme contient « german » ou « 德 ».
   - (iii) `iii_synthetique` : pour chacune des couches 8, 14, 20, 26, deux booléens (lecture S `_z` ; lecture sans lentille `_z`) ; les huit
     doivent être vrais. Je ne peux pas rejouer ce cas (il demande les matrices) : je lis les booléens, et je le déclare.
   - Les listes « vocabulaire entier » sont rapportées à côté, sans critère.
   - **Un cas manqué (ou un désaccord entre ma relecture de la liste et le booléen de la course, lu au plus sévère) = « chaîne en défaut »
     pour tout le volet A** : je n'énonce alors aucun verdict de mesure ; je rapporte seulement les cas sains, les empreintes, et ce que le
     texte gelé demande dans ce cas (rien de plus pour le volet A).
3. Si les cas sains passent : `brut-mesures-C3.json`, `brut-mesures-C1.json`, `brut-mesures-C2.json` (structure attendue :
   `decoupes[d][couche]`, d = 0 à 4, couche ∈ « 8 », « 14 », « 20 », « 26 » ; `longueur`). Mes verdicts sont calculés **sur ces trois fichiers
   seulement**, par mon programme `calcul_verdicts_volet_a_v1.py`.
4. En dernier, `volet-a-brut.json` : contrôle que ses mesures sont identiques à celles des trois fichiers bruts ; lecture des champs
   qui n'existent que là (`cas_sains`, `fumee`, `audit`, `audit_trop_beau` s'il existe, `avertissements_convergence`, `info_chargement`,
   `longueur_*`, bornes de l'intervalle calculées par la course) ; **comparaison** de mes verdicts à ceux que le code de la course y a
   écrits. Un désaccord est rapporté tel quel, avec sa cause si je la trouve ; mon verdict reste celui du texte gelé appliqué à la lettre.

## Règles, telles que je les applique (texte gelé, « Seuil », partie A, et « Critères de lecture gelés »)

**Règle de couche (3/5–1/5).** Pour une condition booléenne par découpe (5 découpes), une couche est « positive » si la condition tient
dans ≥ 3 découpes, « négative » si elle tient dans ≤ 1, « indécise » si elle tient dans exactement 2. Les rangs sont rapportés en médiane
sur les 5 découpes.

**A1 (C2).** Champs : `decoupes[d][l]["a1"]` → `rang_s`, `rang_sans_lentille`, `s_place_p`, `un_temoin_place_p`, `condition`.
Condition à une découpe et une couche = (`rang_s` ≤ 10) **et** (aucun des 102 témoins ne place P dans ses 10 premiers, soit
`un_temoin_place_p` faux). Je la recalcule par `rang_s <= 10 and not un_temoin_place_p` et je vérifie qu'elle égale `condition` et que
`s_place_p == (rang_s <= 10)`. « Retrouvée » : ≥ 2 couches positives ; « non retrouvée » : les 4 couches négatives ; sinon « partielle ».
Composantes rapportées à part, par couche et découpe : (i) `s_place_p` ; (ii) `un_temoin_place_p`.
*Limite déclarée* : les 102 rangs des témoins ne sont pas dans le brut (seul le booléen l'est) ; je ne peux pas les rejouer.

**A2 (C1).** Champs : `decoupes[d][l]["a2"]` → `rho_s`, `rho_sans_lentille`, `condition`, `s_mieux_a2`, `rho_permutee`, `rho_c3` ;
`auc_sac_id`. Condition = `condition` (ρ de S strictement au-dessus du 99ᵉ centile des ρ des 100 directions aléatoires).
*Limite déclarée* : les 100 ρ aléatoires ne sont pas dans le brut ; je lis le booléen sans pouvoir le rejouer. « Nomme » : ≥ 2 couches
positives ; **rapporté**, n'entre dans le verdict que par « S fait mieux que sans lentille ». « Sans objet » si la moyenne sur les
5 découpes de `auc_sac_id` de C1 est < 0,60 (le sac de jetons ne dépend pas de la couche : je vérifie que `auc_sac_id` est le même aux
quatre couches d'une découpe ; sinon je le signale et je donne la moyenne par couche).

**A3 (C1 et C2).** Champs : `decoupes[d][l]["a3"]` → `chute_s`, `chutes_aleatoires` (200), `chute_sac`, `jetons_s_presents_test`,
`exemples_ecartes`, `exemples_ecartes_sac`, `n_jetons_sac`. Condition à une découpe et une couche = `chute_s` > `numpy.quantile(chutes_aleatoires,
0.95)` (interpolation linéaire, strictement) **et** `chute_s` ≥ 0,5 × `chute_sac`. Condition contraire du second membre : `chute_s` < 0,5 ×
`chute_sac`. Couche sans objet si la moyenne sur 5 découpes de `chute_sac` < 0,02. Contraste sans objet s'il compte moins de 2 couches non
sans objet. Parmi les couches non sans objet : « dépendance lue » = ≥ 2 couches positives pour la condition ; « dépendance non lue » =
**toutes** positives pour la condition contraire ; sinon « indécise ». J'applique « dépendance lue » avant « dépendance non lue » (ordre
de la phrase ; les deux ne peuvent coexister que si une même couche est positive pour une condition et pour le contraire de son second
membre, ce qui est impossible). Une valeur absente (`null` : classe unique après retrait) ou un nombre de tirages différent de 200 : je
le signale, je ne remplace rien ; la condition de cette découpe est alors « non évaluable » et je donne le verdict dans les deux lectures
(tenue / non tenue) si cela le change.
*Arrondi* : le texte gelé ne prévoit aucun arrondi ; le code de la course arrondit à 6 décimales avant de comparer aux seuils. Je calcule
**les deux** (comparaison exacte en flottants ; arrondi à 6 décimales) et je signale tout cas où elles diffèrent. Cela vaut pour tous
les seuils ci-dessous.

**« S fait mieux que sans lentille ».** Condition à une découpe et une couche : en A1, `rang_s` < `rang_sans_lentille` (strict) ; en A2,
`rho_s` > `rho_sans_lentille` (strict). Règle de couche 3/5–1/5. « S fait mieux » sur A1 : ≥ 2 couches positives pour cette condition
**qui sont aussi des couches positives de A1** ; sur A2 : ≥ 2 couches positives pour cette condition **qui sont aussi positives de A2**.
« Sans lentille ≥ S » à une couche = couche **négative** de cette condition ; « à chaque couche » = les 4 couches négatives.

**Verdict de la mesure A-i** (ordre de priorité A.2 : chaîne en défaut > « n'apporte rien » > « apporte quelque chose » > « indéterminé ») :
1. cas sain manqué → **chaîne en défaut** ;
2. **n'apporte rien** si : A1 « non retrouvée » ; **ou** « sans lentille ≥ S » à chaque couche sur A1 **et** sur A2 (si A2 est sans
   objet : sur A1 seul) ; **ou** A3 « dépendance non lue » dans chaque contraste où A3 n'est pas sans objet, avec au moins un contraste non
   sans objet ;
3. **apporte quelque chose** si A1 « retrouvée » **et** S fait mieux que sans lentille sur A1 **ou** sur A2, sans condition de la ligne 2 ;
4. sinon **indéterminé**, mesure par mesure.
*Ambiguïté notée d'avance* : si A2 est « sans objet », le texte ne dit pas si la voie « S fait mieux sur A2 » de la ligne 3 reste
ouverte (le code de la course la ferme, lecture qu'il déclare). Si le verdict en dépend, je donne les deux et je n'arbitre pas.

**A-ii, par contraste, sans agrégation.** Champs : `auc_sonde_id`, `auc_sonde_ood`, `auc_sac_id`, `auc_sac_ood`, `scores_sonde_ood`, `y_ood`,
`aii["id"]` et `aii["ood"]` (clés `k1`, `k8`, `k64`, `k512`, `dense`, `hasard*`, `pca*`), `aii["ood_scores"]`, `aii["pca_k_effectif"]`.
Toutes les AUROC sont moyennées sur les 5 découpes, par couche.
- *Plafond, par couche* : sonde en distribution ≥ 0,99 → partie « en distribution » sans objet, la couche ne se juge que hors
  distribution ; les deux ≥ 0,99 (C3 : en distribution seule) → couche sans objet ; moins de 2 couches non sans objet → contraste **sans
  objet**.
- *« N'apporte rien »* : à chaque couche non sans objet et à **chaque** k ∈ {1, 8, 64, 512}, sonde − neurones > 0,05 en distribution (si
  cette partie n'est pas sans objet) **et** hors distribution (C1, C2 ; C3 : en distribution seule).
- *« Apporte »* : il existe k ∈ {1, 8, 64} tel que, à ≥ 2 couches non sans objet, neurones ≥ sonde − 0,02 en distribution (si cette partie
  n'est pas sans objet) **et** borne basse de l'intervalle à 95 % de l'écart hors distribution (neurones − sonde) ≥ −0,05 (C3 : condition en
  distribution seule).
- *Intervalle* : je le **recalcule** par rééchantillonnage apparié des exemples du jeu hors distribution (2 000 tirages ; dans chaque
  tirage, chaque découpe est rééchantillonnée et l'écart d'AUROC est moyenné sur les 5 découpes), à partir de `aii["ood_scores"]`,
  `scores_sonde_ood` et `y_ood`. Deux calculs : (a) la graine du texte gelé, `SeedSequence(20261114).spawn(4)[contraste].spawn(5)[d].spawn(6)[5]`
  (sixième tâche : « rééchantillonnage »), tirage avec remise à l'intérieur de chaque classe (lecture que le code de la course déclare ;
  le texte gelé dit « stratifiés par découpe » sans parler des classes) ; (b) une graine à moi, `SeedSequence(20261115)`, pour
  voir si le verdict tient à la graine. Je compare (a) aux bornes écrites par la course dans `volet-a-brut.json` (étape 4). Le verdict
  est rendu sur (a) ; si (b) ou un tirage sans stratification par classe le change, je le signale comme réserve.
- Ordre de priorité : « n'apporte rien » > « apporte » > « indéterminé » ; « sans objet » d'abord (plafond).
- *Qualificatif* (C1 : hors distribution ; C3 : en distribution ; C2 : sans objet) : « au-delà du texte » si le meilleur détecteur à
  k ≤ 64 dépasse le sac de jetons d'au moins 0,02 d'AUROC, sinon « pas au-delà du texte ». *Ambiguïté notée d'avance* : le texte ne dit pas
  si « le meilleur détecteur » se prend sur toutes les couches (ce que fait le code de la course) ou couche par couche. Je calcule le
  meilleur sur toutes les couches et k ∈ {1, 8, 64}, et le détail par couche ; si les deux lectures divergent, je donne les deux.
- Rapportés sans critère : détecteur dense, k neurones au hasard, composantes principales (k effectif), sac de jetons, base « longueur
  seule » (`longueur`).

**Prédictions du texte gelé** (rapportées à côté, sans effet sur le verdict) : A-i, issue modale « n'apporte rien » ou « indéterminé » ;
A-ii, écart en distribution < 0,02 dès k = 64, « indéterminé » ou « sans objet » sur C1 et C2.

**Audit symétrique (R4), déclencheurs que je calcule et rapporte** :
- *trop beau* : A1 au rang 1 à toutes les couches (je donne le rang médian par couche et le nombre de découpes au rang 1) ; ou neurones
  égaux à la sonde partout (le texte n'en donne pas de définition ; le code de la course en déclare une, à 0,005 près en distribution pour
  le meilleur k ≤ 64, à chaque contraste et couche : je la calcule en la nommant comme telle). Si un déclencheur tient, le texte gelé dit
  « verdict après l'audit » : je lis alors `audit_trop_beau` dans `volet-a-brut.json` (sixième découpe, retrait vérifié, direction sans P),
  je le rapporte, et je dis si le verdict est rendu « après audit » ou « en attente ».
- *tout négatif* : A1 « non retrouvée » et A-ii « n'apporte rien » sur C1 et C3 → AUROC de test de la sonde de C2 à chaque couche (si < 0,9,
  A1 se relit en conséquence, sans changer le verdict) et présence de P parmi les gardés. Je rapporte l'AUROC de la sonde de C2 dans
  tous les cas.
- *Symétrie (ma consigne)* : tout résultat trop propre, positif ou négatif (AUROC à 1,000 partout, rangs tous égaux, chutes toutes nulles,
  conditions identiques sur les 20 cases, témoins qui placent P partout ou nulle part, etc.), est signalé comme réserve, sans changer le
  verdict mécanique.

## Ce que je ne ferai pas

Aucun arbitrage d'une règle qui ne se laisse pas appliquer telle quelle : je la cite, je donne les lectures possibles et leurs issues.
Aucune lecture sous `donnees/`, d'un autre `diag/` ou `runs/`, d'une autre branche ; aucune valeur de clé ; aucun appel payant, aucun
modèle chargé. Aucun fichier réécrit : une correction de ce plan serait une v2, datée, avec la raison, et dirait ce qui avait déjà été lu.

## Fichiers que j'écrirai

- `docs/notes/neuron-lens-v1/lecture-volet-a/calcul_verdicts_volet_a_v1.py` et sa sortie `calcul-verdicts-volet-a-v1.json` (scellés) ;
- `docs/notes/neuron-lens-v1/lecture-volet-a/verdict-volet-a-v1.md` (scellé).

scellable après corrections — liste exacte : C-1 à C-9 (section « Corrections exigées ») ; bloquants B-1, B-2, B-3 ; importants I-1 à I-6.

# Vérification du brouillon 1 de l'addendum de relance v2 de R1 (« rejeu à graine ») et de son code — v1

- Lecteur : sous-agent neuf (Claude, Opus 5.5), règle R2. Je n'ai écrit ni le texte, ni le code, ni aucune des analyses
  citées, ni la vérification adverse VG-01 à VG-10 de l'auteur.
- Date : 2 novembre 2026, ≈ 09:55–10:35 UTC (heure relevée par `date -u` à la rédaction : 10:16).
- Commande : conv-audit, liste fixée au n° 352 (huit points) ; ajout en cours de tâche : verdict sur le changement de
  conception du n° 265 de session-depot (`28f412b7…`, empreinte vérifiée).
- Abréviations : « A » = `prereg/R1-addendum-relance-v2.md` (brouillon 1) ; « RG » =
  `src/controle_ia/runs_nuit/resolution_graine_v1.py` ; « TG » = `tests/test_resolution_graine_v1.py` ; « SI » =
  `scripts/r1_resolution_graine_instance_v1.sh` ; « AM » = `scripts/amorce_instance_r1_resolution_graine_v1.sh` ; « l. »
  = ligne de `git show 21a6e583:<chemin> | cat -n`.

## Pièces (empreintes vérifiées par `git show 21a6e583:<chemin> | sha256sum`)

| Pièce | sha256 | État |
|---|---|---|
| A (brouillon 1, 397 lignes) | `7915a3d653d4de7a41b8fc22d86e4988ede765ae8638ccc335029f9a08644784` | égale |
| RG (1 276 lignes) | `09e31c95b12a6fe2a7fc30f4ec28e42585affc3780d9812cd7f46339cd2e8957` | égale |
| TG (526 lignes) | `c40e4428312027c63d1889e4bf2d980b3f3973a217d00b58660a4749be8c9663` | égale |
| SI (266 lignes) | `47cd64afbd1d7d35ce01288ad1cb5db27a8b5cd0331110a79a71f88fc8948670` | égale |
| AM (45 lignes) | `2ca73c20129a57a4a36cbd190239cee3644372dd725e46c4152940c037c0dc0e` | égale |

Contexte lu : n° 262 (section 3, six changements tenus pour acquis) ; n° 265 ; n° 351, 352, 354, 356 de conv-audit ;
addendum v1 brouillons 3 (`cdca33bb`) et 4 (`72f68fea`, différence de forme seulement) ; concordance anticipée
`concordance-addendum-r1-brouillon3-v1.md` (`d6952cad…`, sceau vérifié) ; parent `567260c0:prereg/R1-R2-rejeu-p3-v1.md` ;
code du harnais de P3 (`harnais/episode.py`, `premier_test_ia/run.py`, `harnais/modeles.py`, `lancer_pilote_a.py` :
`git diff --stat 97dd8290 21a6e583` vide sur ces fichiers et sur les fichiers d'exigences) ; configuration scellée de P3
`prereg/P3-premier-test-config-v1.json` (clés `noyau_attention`, `fils`, `lot`, `T`, `N`, `temperature`,
`max_nouveaux` seulement). Aucune donnée de R1, R2, R4 ni P3 ouverte (ni textes, ni scores, ni fiches, ni manifeste de
P3).

## Verdict sur le changement de conception du n° 265 : **accepté**, aux cinq conditions de C-3

**Vérification dans le code `5c39c6b6` (= `21a6e583` sur `src`, `tests`, `scripts`).**
- L'état « resolu » n'est posé qu'en deux endroits, tous deux sous l'égalité d'empreinte : RG l. 560-561 (essai direct,
  `if emp == empreinte_cible`) et l. 597-602 (repli, même test). Aucune autre affectation de `statut` ; les exceptions
  captées (`Contradiction`, `NonResolu`, l. 564-569, 595-596) laissent « non_resolu » ; toute autre exception arrête
  l'étape.
- L'empreinte porte sur **toute la transcription** : `emp = empreinte_trajectoire(episode_harnais(identifiant, T, rec))`
  (RG l. 554) ; `episode_harnais` (`rejeu_activations_v1.py` l. 158-165) met dans l'`Episode` l'identifiant, N, T, les
  identifiants de **toute** la transcription (`rec["ids"]` : ouverture, observations, actions, clôtures, refaits par
  `transcription`, RG l. 470-498) et, par action, pas, empan, identifiants et texte ; `empreinte_trajectoire` (l. 168-170)
  = sha256 de `json.dumps(asdict(...), sort_keys=True, ensure_ascii=False)`, le calcul de `empreinte_episode` du harnais
  (`harnais/episode.py` l. 366-368). `rec` est construit des seuls identifiants choisis (`trouves`, RG l. 536), qui sont
  aussi ceux rendus (`ids=trouves`, l. 561, 598).
- La cible est l'empreinte stockée par P3 : `ep.empreinte = pieces.fiches[e]["trajectoire"]` (RG l. 894), fiches lues par
  `charger_fiches` sous empreinte citée (`rejeu_activations_v1.py` l. 173-179), obligatoire en mode réel (RG l. 794-797).
- Deuxième certification indépendante à l'étape « table » : chaque entrée, ancienne ou nouvelle, est réappliquée par
  `appliquer_entree_v3` et doit redonner l'empreinte de P3 (RG l. 714-729, garde l. 726) ; l'empreinte cible du résultat
  doit égaler celle de la table v2 (l. 749-750).
- Conclusion : un faux « résolu » n'est possible qu'au prix d'une collision de sha256. L'argument du n° 265 tient.
  Correction de forme : « une graine fausse ne résout rien » est inexact — une graine fausse peut résoudre (justement)
  les épisodes où les octets imposent le choix (A l. 277-279, l'auteur le dit) ; ce qu'elle ne peut pas faire, c'est
  produire un faux « résolu ».

**Ce que l'on perd en rendant la validation non bloquante.**
- R5 : la porte « 147 sur 147 » était une garde d'arrêt essayée sur un cas sain et un artefact (TG l. 321-326 ; TG
  l. 486-496, graines décalées → « sous le seuil », arrêt consigné). Elle disparaît. Ce qui doit la remplacer et être
  essayé de même : (a) la **fonction de lecture** de la validation (classes ci-dessous), cas sain (jouet : « graines
  validées ») et artefact (graines décalées : autre classe, et la résolution qui suit porte la réserve) ; (b) la garde
  d'**ordre** (`exiger_validation`, RG l. 956-969), à garder sans sa condition de lecture (l. 964) : validation scellée,
  sans `arret.json`, même configuration, même code ; (c) « aucun repli silencieux » : la classe de la validation doit
  être recopiée dans le résultat de la résolution et dans la table v3, sinon une résolution faite sous graines non
  validées se lirait comme les autres.
- R3 : rien n'est perdu sur les épisodes résolus (une preuve n'est pas un signe). Le risque nouveau est ailleurs : une
  validation contraire qui ne coûte plus rien invite à relancer avec d'autres réglages (`seuil_ecart`, bascules) jusqu'à
  ce que « ça passe ». Le texte doit l'interdire en clair : une seule exécution de chaque étape sous ce texte ; tout
  essai de plus (lot exact compris) sous un texte neuf.
- R4 : P-G1 garde sa réfutation ; une validation contraire doit être lue comme réserve sur HG-2 et sur les graines, pas
  contournée en silence.
- Ce que l'on gagne : la dépense de la carte n'est plus perdue sur un aléa de précision (VG-03), et Lazar a demandé de
  résoudre tous les épisodes. Le coût de la résolution après une validation contraire est d'au plus quelques minutes de
  carte.

**La règle gelée de lecture de l'accord doit être écrite avant le scellement** (R1 : critères de lecture gelés avant
toute expérience ; elle décide seule si un non résolu peut être déclaré non inversible, donc si la règle B s'applique
sans nœud). Contenu minimal (texte proposé en C-3 et R-01) :
1. les mesures calculées par le code et écrites au résultat avant toute lecture : empreintes retrouvées sur 147 (directes,
   par bascule simple, par paire) ; accord du choix non contraint, moyen et minimum par épisode ; **accord attendu sous une
   graine indépendante** (moyenne, sur les pas, de la probabilité du jeton connu sous la passe : pour un tirage
   exponentiel indépendant, P(argmax(p / q′) = k) = p_k exactement) ; **accord sur les pas informatifs** (jeton connu ≠
   argmax des logits de la passe) et leur nombre ;
2. les classes, chiffrées : « graines validées », « méthode transposée, graines non validées », « méthode non
   transposée » (seuils au choix de l'auteur, écrits ; proposition en R-01) ;
3. leurs conséquences : sous « graines validées » seulement, la cause « caractère de remplacement : cas non simple » vaut
   « non inversible déclaré » (règle B pour l'épisode nommé) ; sous les deux autres classes, tout non résolu est un nœud
   porté à Lazar ; les épisodes résolus sont des preuves sous les trois ;
4. les déclencheurs de l'audit de symétrie (R4) déjà écrits (A l. 352), plus « accord observé non distinct de l'accord
   attendu sous graine indépendante » ;
5. l'interdit de R3 ci-dessus ; la fonction de lecture essayée (R5, sain et artefact).

Les trois autres points du n° 265 : paires de bascules en validation, **accepté** (VG-02 converge avec mon constat 3.c) ;
CUDA autre que 13.0 en réserve écrite au résultat, **accepté** (l'empreinte certifie ; la réserve porte sur HG-2), à
condition que la version soit écrite au résultat (`regler_determinisme` l'écrit déjà dans `reglages`, RG l. 1027 et
1146) et que le filtre d'offre exige un pilote compatible avec CUDA 13.0 (I-1).

## Constats par point du n° 352

### 1. Fidélité numérique (précision, ordre des opérations, carte)

- **Précision du modèle : conforme.** Chargement par `charger_modele_et_format` (RG l. 988-995) →
  `charger_modele(..., "bfloat16", "cuda", "sdpa")` (`lancer_pilote_a.py` l. 263), le chemin de P3 ; réglages
  déterministes par la même fonction (`regler_determinisme`, RG l. 1027 ; TF32 coupé, réductions bfloat16 réduites
  coupées, `harnais/modeles.py` l. 280-290) ; `noyau_attention` = « defaut » et `fils` = 1 comme la configuration
  scellée de P3 ; torch 2.14.1, transformers 5.18.0, tokenizers 0.23.2, numpy 2.4.6 : exigences inchangées depuis le
  commit de P3. Logits passés en float32 (RG l. 358) : conversion exacte du bfloat16, comme `.to("cpu", torch.float32)`
  de P3 (`harnais/episode.py` l. 111).
- **Ordre des opérations : équivalent en pratique, différent en principe.** P3 : `softmax(logits / T)` sur processeur
  en float32, puis `multinomial` = argmax de p / q en float32, premier indice en cas d'égalité (`episode.py` l. 121 ;
  identité vérifiée ici, TG l. 166-175, passé). Rejeu : `(L[j, ct] / T).double() − log(Q[s, ct].double())`, argmax sur
  les candidats triés, plus petit identifiant en cas d'égalité (RG l. 437-443) — il part des **logits**, pas de p. Essai
  sur processeur (bloc-notes, `essais/egalite_log_double.py` et `essais/ecart_differentiel.py`, V = 128 256, logits
  arrondis au bfloat16) : 3 000 pas, **0 désaccord** sur tout le vocabulaire et sur un ensemble contraint des 8 premiers ;
  0 égalité exacte en float32 entre les deux premiers ; erreur **différentielle** entre les deux premiers (seule à
  décider l'ordre) : médiane 4,1·10⁻⁸ nat, 99ᵉ centile 1,5·10⁻⁷, maximum 2,0·10⁻⁷ sur 2 000 pas ; l'erreur commune de
  normalisation (jusqu'à 6·10⁻⁵ nat) ne change pas l'ordre. Le texte dit juste (A l. 255-259, « ≈ 10⁻⁷ en relatif »).
- **Égalités et quasi-égalités, arbitrage.** (a) Égalité exacte en float32 chez P3 : P3 prend le plus petit identifiant
  sur tout le vocabulaire ; le rejeu, en double, prend l'ordre exact : désaccord possible, de probabilité ≈ 2·10⁻⁷ par
  pas (≈ 0,06 attendu sur 310 000 pas). (b) Tout désaccord de ce type a un écart contraint d'environ 10⁻⁷ nat : il est en
  tête de la liste des quasi-égalités (tri par écart, RG l. 579-580) et une bascule simple le corrige. (c) Le bruit du
  bfloat16 (passe pleine contre génération par lots remplis à gauche avec cache) domine de cinq ordres de grandeur :
  c'est HG-2, non mesuré sur le 8B avant la carte (déclaré A l. 216-217).
- **Décision n° 4 du n° 262** (« à partir de p en float32 après softmax sur processeur, comme P3 ») : **non refusée**,
  mais elle ne décrit pas le code du brouillon 1 (qui part des logits). Les deux sont équivalents à 2·10⁻⁷ nat près. Le
  texte doit décrire le code scellé tel qu'il est (C-7). Option la plus littérale, coût ≈ 1 min de processeur sur
  310 000 pas : `p = softmax(L[j] / T)` sur processeur en float32 (vecteur de V, un fil, comme P3), puis
  `p[ct] / Q[s, ct]` en float32, argmax au plus petit identifiant (mineur m-4).
- **Carte (important I-1).** SI l. 153-157 : nom de carte ≠ A100-SXM4-80GB → réserve sans arrêt (conforme au texte,
  A l. 263-264). SI l. 172-175 : seule la version de torch est comparée (suffixe de construction retiré) ;
  `requirements-gpu.txt` admet une construction CUDA 12.8 à défaut de pilote 13.0 ; P3 a couru en CUDA 13.0 (A l. 88-89).
  Retirer `datacenter=true` est sans effet numérique à carte, pilote et roue égaux, mais : (i) le débit des hôtes non
  vérifiés varie (16 Go de modèle sous un plafond de 60 min) ; (ii) l'hôte reçoit le clone complet du dépôt privé et les
  deux jetons (GitHub en écriture, Hugging Face) — c'est une exposition de « dépôt distant / compte », que le GO de
  dépense ne couvre pas : à déclarer dans le texte scellé et à soumettre à Lazar.

### 2. Graines par action

- **Dérivation : conforme.** `graines_p3` (RG l. 121-131) refait `jouer_p3` (`premier_test_ia/run.py` l. 253-255 au
  commit `97dd8290` : générateur neuf par tâche, `graines_des_actions(g, 1, T)`, puis `g.random(T)` sans effet) ; clé
  `tache/<identifiant>` du manifeste de P3, garde « absente » (l. 128-129) ; une graine par action, générateur avancé
  d'un vecteur de V par jeton tant que la ligne est active, comme `generer_lot` (`episode.py` l. 101, 121) ; identité
  « un appel de n × V = n appels de V » revérifiée au lancement (RG l. 142-162, appel l. 1043). Essai
  `test_graines_comme_jouer_p3` : passé ici.
- **Vérification sur les 147 par l'accord : insuffisamment discriminante en l'état (important I-2).** (a) A l. 145 :
  sous une graine indépendante, l'accord attendu n'est pas « la probabilité du jeton le plus probable » mais, par pas,
  **p_k, probabilité du jeton tiré** (course exponentielle), en espérance Σ p² ; valeur calculable exactement sur la même
  passe, sans dépense. (b) Les seuils 0,95 / 0,90 sont fixés sans mesure du 8B (A l. 216-217) : sur des sorties de faible
  entropie (moyenne de p_k proche de 0,9), une graine fausse s'en approche, et le bruit du bfloat16 peut faire tomber la
  vraie graine au-dessous. La statistique qui ne dépend pas de l'entropie : l'accord sur les **pas informatifs** (jeton
  connu ≠ argmax des logits) — près de 1 avec la bonne graine, au plus ≈ 0,5 avec une fausse. (c) Les 18 épisodes
  corrigés sont déjà une preuve forte des graines (le découpage non canonique n'est retrouvé que si p / q le désigne,
  A l. 276-277) ; l'accord en est le complément pour les 129 autres.
- **Garde essayée sain / artefact ?** Au commit, l'accord n'est pas une garde (A l. 213-214) ; la décision n° 2 du
  n° 262 en faisait une garde ; le n° 265 en fait un diagnostic lu par règle gelée (accepté ci-dessus). Les essais
  existants : cas sain, accord 1,0 (TG l. 239, **sauté ici**) ; artefact, graine fausse sur une action, accord < 0,9 (TG
  l. 252-257, **sauté ici**) ; graines décalées de bout en bout → empreintes sous le seuil (TG l. 486-496, passé). Le
  modèle minuscule (biais qui ouvre des milliers de jetons) a une entropie sans rapport avec le 8B : il éprouve le
  mécanisme, pas la puissance des seuils. L'« accord attendu sous graine indépendante » fournit l'artefact sur les vraies
  données, sans dépense.

### 3. Critère de passage entre les modes

- **Passe forcée → bascules : chiffré et écrit** (A l. 195-199, 241-245 ; RG l. 579-602) : empreinte non retrouvée ou
  contradiction ; quasi-égalités sous `seuil_ecart` = 1,0 nat, 16 au plus, triées par écart ; bascules simples puis paires
  vers le **second** candidat seulement ; 136 combinaisons (16 en validation au brouillon 1, 136 après le n° 265). Essai
  sain / artefact : TG l. 272-302 (perturbation de 0,1 retrouvée ; sous un seuil de 0,05, non résolu) — **sauté ici**.
- **(a) Défaut de conception confirmé (VG-02 de l'auteur)** : les positions basculées viennent de l'essai direct ;
  après la première erreur, les actions suivantes de l'essai direct sont jouées dans un contexte faux, et leurs
  quasi-égalités (rang, second candidat) ne correspondent plus au bon chemin ; une seconde bascule dans une action
  ultérieure, ou après un changement du nombre de jetons dans la même action, tombe en contradiction (RG l. 444-448).
- **(b) Bascules → lot exact** : non codé au commit (A l. 264-268) ; acquis au n° 262 (n° 3). L'ordre retenu (passe
  forcée d'abord, lot en repli) est l'inverse de celui que conv-audit a accepté au n° 352 (« en premier … la passe forcée
  reste le repli ») : à déclarer comme écart (m-6). Pour qu'il soit « chiffré, écrit d'avance, essayé » : déclencheurs
  (causes admises), étape (validation, résolution ou les deux), budget, composition du lot (longueurs de remplissage
  calculées, lignes voisines quelconques mais même forme), cas sain (le jouet de `jouer_episodes` redonné ligne pour
  ligne) et artefact (remplissage faux d'un jeton → non résolu), arbitre l'empreinte.
- **(c) Bloquant B-1 — durée : texte et code se contredisent, et les délais rendent probable la perte de tous les
  résultats.** Le texte fait de la durée une **cause par épisode** (A l. 245, 349). Le code n'en a pas : la limite lève
  `GardeArret` (RG l. 413-414, 1056-1057), non captée par le repli (l. 595-596), qui arrête toute l'étape ; `executer`
  n'écrit alors que `arret.json` avec `etape`, `equivalence_tirage` et `episodes_traites` (l. 1193-1198) : aucun
  résultat par épisode, aucun `.npz`. Délais : résolution 15 min (SI l. 256) pour 7 épisodes à « au pire ≈ 5 min »
  chacun (A l. 285, 312) — quatre replis complets font 20 min ; `duree_max_s` = 30 min (A l. 202) ne joue jamais avant le
  délai externe de la résolution. Issue plausible : les 4 épisodes difficiles épuisent leurs combinaisons, `timeout`
  envoie TERM, et même les 3 épisodes de C-6 et toute cause écrite sont perdus ; aucune ligne de « Critères » ne lit ce
  cas. Converge avec VG-01 de l'auteur.
- **Essai de la garde de durée (R5)** : aucun essai de `echeance` ni de `duree_max_s` dans TG (I-5).

### 4. Étape 0 à l'aveugle

- **Le code ne lit jamais la table v1** (la configuration ne cite que `chemin_table_tokenisation`, la v2).
- **La table v2 et les identifiants connus sont en mémoire avant la résolution**, mais ne sont passés à aucune fonction
  de résolution : `charger_pieces` charge la table (RG l. 865) ; `classer` (l. 905-916, appelé l. 1035) calcule avant la
  boucle la reconstruction de base de tous les épisodes (`base_nv`, qui **est** la vérité pour les 129) et range l'entrée
  de table de chacun (`"entree"`, l. 915) ; la boucle (l. 1054-1072) appelle `resoudre_avec_repli` (l. 1062-1063) avec
  textes, longueurs, tirages issus des graines, empreinte de P3, et la fabrique d'environnement `ep.env` ; signatures
  l. 395-397, 509-510, 539-540 ; aucune n'accède à `classement`. `verite` n'est appelé qu'après la boucle (l. 1081).
  Réserve de forme : `ep.env` est une méthode liée à un `EpisodeP3` qui garde `pieces` (table comprise, l. 895) ; elle
  n'en lit que tâches, guide et consignes (l. 897-902). L'aveugle tient par l'usage, vérifiable à la lecture, pas par
  isolement. A l. 274-275 (« les identifiants connus ne sont lus qu'après la résolution ») dit plus que le code (m-1).
- L'empreinte arbitre seule : `ep.empreinte` = fiche de P3 (l. 894), non la copie `trajectoire_p3` de la table.

### 5. Contrôle croisé des 3 épisodes de C-6

- **Prévu.** Les 3 (`honnete/2512.05150v2/e0` 2a, `honnete/2512.11131v1/e0` 2a, `temoin/2510.24788v1/e0` 1a) sont dans
  `episodes_resolution` (A l. 206-208) ; comparaison aux identifiants de la table v2, revérifiés par l'empreinte, après la
  boucle (RG l. 1081, 1095-1105) ; lecture « conforme » / « contraire » (l. 1153-1155) ; règles écrites A l. 350-351.
- **Le contrôle aveugle est à l'étape 0** : les 3 font partie des 18 corrigés de la validation (A l. 149-150) ; à
  l'étape 1, même code, même carte, réglages déterministes : c'est une **répétabilité**, à écrire ainsi (m-2).
- **Règle si divergence** : non résolu à l'étape 1 → audit (R4), l'entrée de C-6 reste ; résolu avec d'autres
  identifiants → impossible hors collision, arrêt de la lecture. Manques : la lecture n'a que deux valeurs (un épisode non
  résolu y compte « contraire » au même titre qu'un désaccord d'identifiants : VG-06 de l'auteur) ; l'étape « table »
  (`construire_et_verifier_table`, l. 1201-1235) ne lit ni `controle_croise_lecture` ni la lecture de l'étape : rien
  n'empêche de bâtir la table v3 avant l'audit (m-2).

### 6. Règle « non inversible »

- **Bloquant B-2 — le déclencheur n'est pas ce que le texte nomme.** Le texte : « au plus `balayages_max` balayages du
  vocabulaire par épisode pour les octets que recouvre un U+FFFD » (A l. 201, 246-248). Le code compte un balayage à
  **chaque pas où un U+FFFD se trouve dans les 128 caractères suivants** (`atteint`, RG l. 292 ; compte l. 428-433),
  que la recherche ait ou non quelque chose à balayer. Essai (bloc-notes, `essais/compte_balayages.py`, `Cible` du
  commit, vocabulaire factice au niveau de l'octet, texte ASCII) : 1 U+FFFD → 30 pas comptés ; 2 → 60 ; **3 → 90 > 64** :
  l'épisode est déclaré « caractère de remplacement : cas non simple », donc « non inversible » et mis en règle B **sans
  nœud**, quelle que soit la difficulté. Le nombre de U+FFFD des 7 épisodes (et des 147) n'est pas écrit dans le texte.
- **Le mot « non inversible » est inexact** (I-3) : sous HG-1 et HG-2, le jeton de P3 est l'argmax de p / q sur tout le
  vocabulaire et appartient toujours à l'ensemble contraint (y compris près d'un U+FFFD : RG l. 295-305, l. 249-269) ;
  le choix pas à pas le retrouve. Ce que déclare la cause, c'est un **budget de recherche dépassé**, pas une
  impossibilité ; « le texte stocké n'est pas l'image exacte des jetons » (A l. 349) est faux : il en est l'image exacte
  par une application non injective.
- **Lecture : presque univoque à A l. 349**, conforme au n° 6 du n° 262 (seule la cause U+FFFD → règle B ; toute autre →
  nœud). Restent : G2 (A l. 110) réserve la règle B à **tout** non résolu « avec sa cause » (contraire) ; HG-3 (A l. 133-135)
  et la méthode, point 6 (A l. 246-248), disent « non inversible » sans dire « budget » ; un épisode à U+FFFD non résolu
  pour une autre cause n'est pas dit nœud en clair ; depuis le n° 265, la déclaration doit dépendre de la classe de la
  validation (« graines validées »). Couples R-06 à R-09.

### 7. Essais rejoués sur processeur

- Copie extraite au commit `21a6e583` (`git archive`, bloc-notes), `.venv` gelé (numpy 2.4.6, scipy 1.17.1, **torch
  2.14.1+cu130 présent**, transformers 5.18.0). Commande demandée, plus `-rs` pour les motifs, et `HF_HUB_OFFLINE=1
  TRANSFORMERS_OFFLINE=1` pour interdire tout réseau :
  `PYTHONPATH=src nice -n 10 python -m pytest -q -p no:cacheprovider tests/test_resolution_graine_v1.py -rs`
- **Résultat exact : `6 passed, 6 skipped in 56.97s`** (code 0). Passés : `test_tirage_de_p3_egal_argmax_p_sur_q_…`,
  `test_graines_comme_jouer_p3`, `test_garde_du_seuil_de_validation`, `test_formes_des_tables_v1_et_v2_…`,
  `test_bout_en_bout_jouet_validation_resolution_table`, `test_configuration_gardes`. **Sautés (6)**, motif unique
  « tokeniseur de Llama 3.1 introuvable » (TG l. 72-73) : vocabulaire et décodage (l. 194), **cas sain** (l. 227),
  **artefacts graine fausse / texte altéré / contexte décalé** (l. 247), **repli** (l. 272), **U+FFFD** (l. 305), forme
  « identifiants » (l. 336). Le tokeniseur (`tokenizer.json` `79e3e522…`) n'est ni dans l'environnement ni dans un cache
  local ; le chercher demanderait le réseau, interdit. **Je ne peux donc pas attester les essais de R5 du cœur de la
  méthode** (« 12 passés », A l. 321) ; ils restent à la charge du second vérificateur ou de l'instance (qui exige
  « 43 passed », SI l. 208).
- Liste de l'instance : `--collect-only` sur les cinq fichiers de SI l. 200-201 : **43 tests collectés** (égal à
  « Tests attendus : `43` », A l. 41).
- `grep -c` : « Tests attendus : \` » et « Chemin de la configuration de la résolution à graine : \` » apparaissent une
  fois chacun (lecture de SI l. 75-85 possible) ; trois « À REMPLIR » restent (A l. 36, 395, 397).

### 8. Effet sur nos trois analyses scellées (principale `8e267952…`, secondaire `1f6a6da2…`, par épisode `26a3ff72…`)

- **Aucune classe, aucun seuil, aucun critère changé.** G3 (A l. 111) ne couvre que des épisodes nommés **parmi les 4**
  que N-A couvre déjà (la résolution ne peut qu'en retirer) ; un nœud porté à Lazar reste sa décision. G4 et G5 (comptes
  à r′) déplacent des actions entre « contexte exact » et « hors contexte exact », jamais entre fidèle et non fidèle hors
  repli ; sous repli, la couverture saboteur 350 / 600 et honnête 420 / 600 reste sous 80 % : même classe « non concluant
  (rejeu partiel) ». G6 (module `rejeu_activations_v3`, commande du manifeste) : formats et commande, hors de nos trois
  textes (comme E16). Ces lignes passent à l'addendum v3 (n° 262, n° 1).
- **À reporter dans l'addendum v3 et sa concordance** (m-8) : la concordance anticipée attend
  `tokenisation.table_sha256` = `5f6cf489…` et `episodes_non_resolus` = exactement les 4 (son point 6 de « Ce que la
  concordance finale devra vérifier ») ; la table v3 change les deux. Ce n'est pas une classe ; c'est une attente de
  réception à réécrire, sinon la réception lirait un écart.

## Constats numérotés

**Bloquants**
- **B-1** Durée (3.c) : RG l. 413-414, 595-596, 1056-1057, 1193-1198 ; SI l. 248, 256 ; AM l. 36 ; A l. 202-203, 245,
  285, 312, 349.
- **B-2** Unité de `balayages_max` (6) : RG l. 292, 428-433 ; A l. 201, 246-248.
- **B-3** Depuis le n° 265 : la règle gelée de lecture de la validation n'existe ni dans le texte ni dans le code ;
  `exiger_seuil_validation` (RG l. 1158-1159) et `exiger_validation` (l. 964) font encore de la validation une porte ;
  A l. 213-215, 275-276, 281-283, 346-347, 373-374 la décrivent encore comme porte.

**Importants**
- **I-1** Carte, construction CUDA, filtres d'offre, exposition du dépôt privé et des jetons hors centre de données (1) :
  SI l. 153-157, 172-175 ; A l. 250-252, 263-264.
- **I-2** Accord du choix non contraint : formule de A l. 145 inexacte ; statistique dépendante de l'entropie ; pas
  informatifs et accord attendu sous graine indépendante à ajouter (2) : RG l. 360-374, 610-621, 1085.
- **I-3** « Non inversible » : mot et lecture (6) : A l. 110, 133-135, 246-248, 349.
- **I-4** L'accord n'est pas calculé pour les épisodes non résolus (`acc_v` = None quand `v` et `r["ids"]` sont nuls,
  RG l. 1085), alors que le texte le promet pour le jeton « retenu » (A l. 177-179) : c'est le diagnostic dont Lazar a
  besoin pour un nœud (graines, précision ou U+FFFD).
- **I-5** R5 : gardes non essayées dans TG — durée (`echeance`, `duree_max_s`), citation de la configuration
  (`CONFIG_CITEE`, RG l. 1176-1177), texte attendu de l'ouverture (l. 1031-1041, inactif en jouet) ; six essais du cœur
  invérifiables ici (7).
- **I-6** R6 : les mesures « en bfloat16 » de P-G3 (A l. 157-159 : 16 sur 16, marges 0,012 et 0,015, 0,3 %) n'ont ni
  chemin ni empreinte, et les essais du code tournent en float32 (TG l. 105, `dtype=torch.float32`).

**Mineurs**
- **m-1** Formulation de l'aveugle (4) : A l. 272-275.
- **m-2** Contrôle croisé : aveugle à l'étape 0, répétabilité à l'étape 1 ; lecture à trois valeurs ; étape « table »
  sans garde sur `controle_croise_lecture` (5) : RG l. 1153-1155, 1201-1235 ; A l. 281-285, 350-351.
- **m-3** Compte exact : `exiger_seuil_validation` accepte 147 sur 148 si la classification changeait ; exiger
  `len(episodes) == 147` (RG l. 947-953).
- **m-4** Option littérale de l'ordre de P3 (1).
- **m-5** Ordre de `episodes_resolution` : les 3 de C-6 en tête (rapides, directs), pour qu'ils existent avant tout
  dépassement (A l. 206-208).
- **m-6** Écart au n° 352 sur l'ordre des modes, à déclarer (3.b) : A l. 264-266.
- **m-7** Pire cas de dépense : ajouter la vie de l'instance hors amorce (démarrage, image, attente de la destruction
  par identifiant, R10) au plafond de 60 min (A l. 313-316).
- **m-8** Attentes de réception de la concordance à réécrire pour la table v3 (8).

## Corrections exigées (liste exacte pour « scellable après corrections »)

- **C-1 (B-1)** Budget de durée **par épisode** (`duree_episode_max_s`, clé de configuration), contrôlé entre deux
  combinaisons et avant chaque passe : au-delà, l'épisode est « non résolu », cause « durée de l'épisode (k combinaisons
  sur n) » ; à l'échéance de l'étape, les épisodes non traités sont écrits « non traités : durée de l'étape » et **le
  résultat est écrit quand même** (lecture « interrompue »), `.npz` compris, scellé ; délais externes ≥ échéance interne
  + chargement (résolution ≥ 7 × budget par épisode + 5 min) ; plafond de l'amorce et pire cas de dépense recalculés ;
  essais : budget large → résolu ; budget nul → « non résolu, durée », résultat écrit.
- **C-2 (B-2)** Compter un balayage seulement quand la recherche couvre des octets inconnus (au choix : `commencant_par(E)`
  non vide, ou U+FFFD au caractère courant, ou plafond par U+FFFD = `balayages_max` × nombre de U+FFFD de l'épisode) ;
  écrire l'unité dans le texte, et le nombre de U+FFFD de chacun des 7 épisodes et des 147 (processeur, textes seuls) ;
  essai à 3 U+FFFD.
- **C-3 (B-3, n° 265)** Validation non bloquante, aux cinq conditions : (1) fonction `lire_validation` (classes de R-01),
  écrite au résultat avant toute lecture, essayée sain / graines décalées ; (2) `exiger_validation` garde l'ordre
  (scellée, sans `arret.json`, même configuration, même code), sans condition de lecture ; (3) classe recopiée dans le
  résultat de la résolution et dans la table v3 ; (4) déclaration « non inversible » sous « graines validées » seulement ;
  (5) interdit de R3 écrit (une exécution par étape ; tout essai de plus sous un texte neuf).
- **C-4 (I-1)** Torch : écrire `torch.version.cuda` au journal et au résultat, réserve écrite si ≠ 13.0 ; filtres
  d'offre écrits dans le texte (A100 SXM4 80 Go, pilote compatible CUDA 13.0, débit descendant minimal, fiabilité) ;
  retrait de `datacenter=true` déclaré dans le texte scellé et soumis à Lazar pour l'exposition du dépôt et des jetons.
- **C-5 (I-2, I-4)** Calculer et écrire, par épisode (résolu ou non) : accord contre le jeton retenu ; accord attendu sous
  graine indépendante (moyenne de p_k sous la passe) ; accord et nombre de pas informatifs.
- **C-6 (I-3)** Textes R-06 à R-09.
- **C-7 (1)** Le texte décrit exactement le calcul du choix contraint du code scellé (logits ou p, double ou float32),
  avec la mesure de 2·10⁻⁷ nat ; la décision n° 4 rédigée en conséquence.
- **C-8 (I-5)** Essais ajoutés : durée (C-1), citation de la configuration (texte sans la ligne → arrêt ; avec → passe),
  texte attendu de l'ouverture (absent → arrêt), lecture de la validation (C-3), compte des balayages (C-2) ; « Tests
  attendus » recompté.
- **C-9 (I-6)** P-G3 : chemin et empreinte du script et de la sortie des mesures en bfloat16, ou retrait des chiffres.

## Couples « remplacer / par » pour le brouillon 2 (texte scindé, n° 262 n° 1 ; changement du n° 265 compris)

**R-01 — A l. 213-215 (« Seuil »).**
Remplacer : « **Seuils de lecture** (critères, non gardes du code) : accord non contraint moyen par épisode **≥ 0,95** et
minimum **≥ 0,90** sur les 147 pour tenir les graines pour validées (« Critères de lecture gelés »). Seuil de la règle B :
10 épisodes (E3, inchangé). »
Par : « **Règle de lecture gelée de la validation** (mesure, non garde ; n° 265), appliquée par `lire_validation` et
écrite au résultat avant toute lecture : **« graines validées »** si 147 empreintes sur 147, accord non contraint moyen
≥ 0,95, minimum par épisode ≥ 0,90, et accord sur les pas informatifs (jeton connu ≠ argmax des logits de la passe)
≥ 0,90 sur au moins 1 000 tels pas ; **« méthode transposée, graines non validées »** si 147 sur 147 sans l'une de ces
conditions ; **« méthode non transposée »** sous 147. L'accord attendu sous une graine indépendante (moyenne, sur les pas,
de la probabilité du jeton connu sous la passe) est rapporté à côté. Conséquences : la résolution part sous les trois
classes ; les épisodes résolus sont des preuves sous les trois ; sous « graines validées » seulement, un non résolu de
cause « caractère de remplacement : budget de balayages dépassé » est déclaré non inversible par la méthode (règle B pour
lui) ; sous les deux autres classes, tout non résolu est un nœud porté à Lazar. La classe est recopiée dans le résultat de
la résolution et dans la table v3. Une seule exécution de chaque étape sous ce texte ; tout essai de plus (réglages
changés, lot exact) relève d'un texte neuf (R3). Seuil de la règle B : 10 épisodes (E3, inchangé). » *(Valeurs 0,90 et
1 000 : proposées, à fixer par l'auteur avant le scellement.)*

**R-02 — A l. 145-147 (P-G1).**
Remplacer : « (une graine fausse ferait tomber cet accord vers la probabilité du jeton le plus probable, typiquement 0,6 à
0,85). Réfutation : moins de 147 (arrêt, la méthode ne se transpose pas) ; accord moyen sous 0,95 (graines non validées,
voir « Critères »). »
Par : « (une graine indépendante ferait tomber cet accord, pas par pas, à la probabilité du jeton tiré sous la passe, en
espérance Σ p², valeur calculée et rapportée ; sur les pas informatifs, à 0,5 au plus). Réfutation : moins de 147
(« méthode non transposée », réserve ; la résolution part) ; accord sous les seuils de « Seuil » (« graines non validées »,
réserve ; aucun non résolu déclaré non inversible). »

**R-03 — A l. 275-276 (étape 0).**
Remplacer : « Critère gelé : `seuil_validation` = 147 ; sous le seuil, arrêt (`exiger_seuil_validation`), résolution non
lancée. »
Par : « Mesure : 147 empreintes attendues, bascules simples et paires permises (136 combinaisons au plus) ; lecture par la
règle gelée de « Seuil » ; la résolution part sous les trois classes ; seuls les arrêts d'intégrité de la liste d'arrêt
l'empêchent (validation non scellée, `arret.json`, autre configuration, autre code). »

**R-04 — A l. 281-283 (étape 1).**
Remplacer : « seulement si la validation est scellée, de lecture « atteint », de **même configuration** et de **même
code** »
Par : « seulement si la validation est scellée, sans `arret.json`, de **même configuration** et de **même code**
(`exiger_validation`, sans condition de lecture ; sa classe est recopiée dans le résultat) ; ordre : les 3 de C-6 d'abord
(répétabilité de l'étape 0, où ils sont validés à l'aveugle parmi les 18), puis les 4 ».

**R-05 — A l. 272-275 (aveugle).**
Remplacer : « les fonctions de résolution ne reçoivent que les textes, les longueurs, les graines et l'empreinte de P3 ;
les identifiants connus ne sont lus qu'après la résolution de tous les épisodes, pour les mesures (`verite`). »
Par : « la table v2 et la reconstruction de base (identifiants connus des 129) sont calculées avant la boucle par
`classer`, pour choisir les épisodes, et gardées en mémoire ; aucune n'est passée aux fonctions de résolution
(`resoudre_action`, `rejouer_episode`, `resoudre_avec_repli` ne reçoivent que textes, longueurs, tirages issus des
graines, empreinte de P3, format, vocabulaire, modèle et fabrique d'environnement) ; la comparaison aux identifiants connus
(`verite`) n'a lieu qu'après la boucle. L'aveugle tient par construction des appels, vérifiable à la lecture du code
cité. »

**R-06 — A l. 110 (G2), colonne « Nouvelle règle ».**
Remplacer : « Règle B **réservée aux épisodes que le rejeu à graine laisse non résolus, chacun avec sa cause écrite** ;
liste remise à Lazar avant toute lecture (n° 356, point 4) ; seuil de 10 inchangé (E3) »
Par : « Règle B réservée au seul épisode **déclaré non inversible par la méthode** (cause « caractère de remplacement :
budget de balayages dépassé », sous la classe « graines validées ») ; tout autre non résolu est un **nœud porté à Lazar**
avant la relance (complément par lot exact sous texte neuf, ou règle B par sa décision, épisode nommé) ; liste des deux
sortes remise à Lazar avant toute lecture (n° 356, point 4) ; seuil de 10 inchangé (E3) ».

**R-07 — A l. 133-135 (HG-3).**
Remplacer : « un épisode qui contient U+FFFD n'est inversible que si les octets inconnus se retrouvent par un balayage
borné du vocabulaire. »
Par : « le décodage n'est pas injectif (U+FFFD, jetons spéciaux effacés), mais le jeton de P3 reste dans l'ensemble
contraint à chaque pas : sous HG-1 et HG-2, la méthode le retrouve ; près d'un U+FFFD, la recherche des octets inconnus
est bornée (`balayages_max`, unité écrite en « Seuil ») ; au-delà de la borne, l'épisode est déclaré non résolu par
budget, ce qui n'est pas une preuve d'impossibilité. »

**R-08 — A l. 201 (« Seuil ») et l. 246-248 (méthode, point 6).**
Remplacer (l. 201) : « `balayages_max` = **64** (balayages du vocabulaire par épisode pour les octets que recouvre un
U+FFFD) ; »
Par : « `balayages_max` = **N** (unité : pas où la recherche couvre des octets inconnus — définition de C-2 —, par
U+FFFD ; nombre de U+FFFD par épisode, des 7 et des 147, écrit en « Plan d'analyse ») ; »
Remplacer (l. 247-248) : « au-delà, non résolu déclaré « caractère de remplacement : cas non simple » — c'est le cas **non
inversible** déclaré (HG-3) ; sa lecture est dans « Critères ». »
Par : « au-delà, non résolu, cause « caractère de remplacement : budget de balayages dépassé » ; c'est le seul cas que la
méthode déclare non inversible, et seulement sous « graines validées » (« Seuil », « Critères »). »

**R-09 — A l. 349 (critères, k non résolus).**
Remplacer : « cause « caractère de remplacement : cas non simple » = **non inversible déclaré** (le texte stocké n'est pas
l'image exacte des jetons) : règle B de la v1 pour lui ; toute autre cause (empreinte non retrouvée après repli,
contradiction, durée) = **non résolu par la méthode**, non déclaré non inversible : nœud à Lazar (complément par lots, ou
règle B pour l'épisode nommé) »
Par : « cause « caractère de remplacement : budget de balayages dépassé » **et** validation « graines validées » =
**non inversible déclaré par la méthode** (budget de recherche dépassé, non preuve d'impossibilité) : règle B de la v1 pour
lui ; toute autre cause (empreinte non retrouvée après repli, contradiction, durée de l'épisode), ou la même cause sous une
autre classe de validation, ou un épisode à U+FFFD non résolu pour une autre cause = **non résolu par la méthode** : nœud à
Lazar avant la relance (complément par lot exact sous texte neuf, ou règle B pour l'épisode nommé) ; pour chacun, accord
non contraint et accord attendu sous graine indépendante rapportés »

**R-10 — A l. 346-347 (critères, validation).**
Remplacer les deux lignes « Validation : 147 / 147 empreintes, accord sous l'un des deux seuils | **Réserve** … » et
« Validation : moins de 147 | Arrêt par le code, résolution non lancée … »
Par : « Validation « méthode transposée, graines non validées » | **Réserve** sur les graines : les empreintes retrouvées
à l'étape 1 restent des preuves ; aucun non résolu n'est déclaré non inversible ; audit (R4) avant la relance » et
« Validation « méthode non transposée » (moins de 147) | **Réserve** sur HG-2 : la résolution part ; ses empreintes
retrouvées restent des preuves ; tout non résolu est un nœud à Lazar (complément par lot exact sous texte neuf, ou relance
avec la table v2 et la règle B pour les 4, v1, E19) ».

**R-11 — A l. 350 (contrôle croisé).**
Remplacer : « Contrôle croisé contraire : un épisode de C-6 non résolu par le rejeu | Contradiction avec l'étape 0 (il y
était résolu) : audit (R4) ; la table v3 garde l'entrée de C-6, déjà vérifiée par l'empreinte »
Par : « Contrôle croisé « non répété » : un épisode de C-6 non résolu à l'étape 1 | Répétabilité en défaut (il était
résolu à l'étape 0, même code, même carte) : audit (R4) **avant l'étape 2** (garde de l'étape « table ») ; la table v3
garde l'entrée de C-6, déjà vérifiée par l'empreinte » — lecture à trois valeurs : « conforme », « non répété »,
« contraire » (identifiants différents, impossible hors collision : arrêt de la lecture).

**R-12 — A l. 245 et l. 285, l. 202-203, l. 310-313 (durée).**
Remplacer (l. 245) : « contradiction entre texte, longueurs et choix ; U+FFFD non simple ; durée). »
Par : « contradiction entre texte, longueurs et choix ; budget de balayages dépassé ; durée de l'épisode au-delà de
`duree_episode_max_s`). À l'échéance de l'étape, les épisodes non traités sont écrits « non traités » et le résultat est
écrit et scellé quand même. »
Remplacer (l. 202-203) : « `duree_max_s` = **1 800** par étape ; délais externes du script : validation 35 min,
résolution 15 min ; plafond de l'amorce : **60 minutes** pour l'ensemble ; »
Par : « `duree_episode_max_s` = **D** ; `duree_max_s` par étape ; délais externes ≥ échéance interne + chargement
(résolution ≥ 7 × D + 5 min) ; plafond de l'amorce et pire cas de dépense recalculés (« Coût et GO ») ; » — et, l. 312-313,
le pire cas recalculé avec la vie de l'instance hors amorce (m-7).

**R-13 — A l. 255-259 (point (ii) de « Précision »).**
Remplacer : « (ii) le **choix contraint** est calculé en log, en double précision, sur les candidats (log p − log q, à la
constante de normalisation près), au lieu de p / q en float32 sur processeur : l'ordre est le même en arithmétique exacte et
ne peut différer que si deux candidats sont à moins d'un arrondi de float32 (≈ 10⁻⁷ en relatif) »
Par (si le code reste celui du brouillon 1) : « (ii) le **choix contraint** est calculé en double précision **à partir des
logits** (`(L / T).double() − log q`, sur les candidats ; la constante de normalisation, commune, est omise), au lieu de
p / q en float32 sur processeur : l'ordre est le même en arithmétique exacte ; l'erreur différentielle de P3 entre les deux
premiers candidats est au plus 2,0·10⁻⁷ nat (mesure sur processeur, V = 128 256, 2 000 pas : chemin et empreinte du script
et de la sortie) ; une égalité exacte en float32 chez P3 se tranche au plus petit identifiant sur tout le vocabulaire »
— ou, si la décision n° 4 est codée telle quelle, décrire `softmax` en float32 sur processeur, puis log p − log q.

**R-14 — A l. 263-264 (carte).**
Remplacer : « **Carte attendue : A100-SXM4-80GB**, celle de P3 ; une autre carte n'arrête pas le script mais est consignée
comme réserve au journal ; la validation à l'aveugle juge. »
Par : « **Carte attendue : A100-SXM4-80GB**, celle de P3, torch 2.14.1 construit pour CUDA 13.0 (`torch.version.cuda`
écrit au résultat ; autre carte ou autre construction : réserve écrite au résultat, sans arrêt) ; offre choisie par les
filtres écrits (A100 SXM4 80 Go, pilote compatible CUDA 13.0, débit descendant ≥ X, fiabilité ≥ Y) ; **filtre
`datacenter=true` retiré (déclaré)** : l'hôte reçoit le clone du dépôt privé et les deux jetons — décision de Lazar,
référence : … ; la validation à l'aveugle mesure HG-2. »

**R-15 — A l. 157-159 (P-G3).**
Remplacer : « Mesure sur le modèle minuscule en bfloat16 (essais du code) : »
Par : « Mesure sur le modèle minuscule en bfloat16 (script `…`, sortie `…`, empreintes ; les essais du code tournent en
float32) : »

**R-16 — A l. 373-374 (liste d'arrêt).**
Remplacer : « validation sous le seuil de 147 (résolution non lancée) ; résolution sans validation scellée de même
configuration et de même code ; »
Par : « résolution sans validation scellée, sans `arret.json`, de même configuration et de même code (la lecture de la
validation n'arrête rien : « Seuil ») ; étape « table » sans contrôle croisé « conforme » ; »

**R-17 — A l. 198-199 (« Seuil »), n° 265.**
Remplacer : « `combinaisons_max_validation` = **16** (bascules simples seulement) ; »
Par : « `combinaisons_max_validation` = **136** (bascules simples et paires, comme la résolution ; n° 265) ; »

**R-18 — A l. 264-266 (mode lot).**
Remplacer : « la passe forcée est le seul mode de ce texte (écart au n° 257 déclaré ; point à trancher). »
Par : « ordre retenu : passe forcée et bascules d'abord, lot exact en repli (`resolution_graine_lot_v1.py`, ou texte
neuf) ; **écart déclaré** à l'ordre accepté par conv-audit au n° 352 (« en premier … la passe forcée reste le repli ») ;
raison : … ; déclencheurs, budget, composition du lot et essais (sain, artefact) : … ».

## Changements de code

1. **RG, durée** : `resoudre_avec_repli` contrôle `duree_episode_max_s` avant chaque combinaison et laisse
   `resoudre_action` lever une exception propre à l'épisode (captée, cause écrite) ; `_executer` capte l'échéance de
   l'étape entre deux épisodes, marque les restants « non traités », écrit `.npz` et résultat (C-1).
2. **RG l. 428-433** : compte des balayages selon C-2 ; `Reglages` et configuration en conséquence.
3. **RG l. 1085 et suivantes** : accord contre le jeton retenu pour tout épisode ; accord attendu sous graine
   indépendante et accord sur les pas informatifs (p_k et argmax des logits sont déjà dans la passe, l. 362-371) (C-5).
4. **RG l. 947-969, 1149-1159** : `lire_validation` (classes de R-01) ; plus d'arrêt sur la lecture ; `exiger_validation`
   sans condition de lecture ; classe recopiée au résultat de la résolution et dans la table v3 ; compte exact des
   épisodes de validation (m-3).
5. **RG l. 1201-1235** : l'étape « table » exige `controle_croise_lecture` = « conforme » (lecture à trois valeurs).
6. **RG l. 579-602** (VG-02) : seconde bascule cherchée sur le chemin rejoué après la première, non sur l'essai direct.
7. **SI l. 172-175** : écrire `torch.version.cuda` ; réserve si ≠ 13.0 ; **SI l. 248, 256, AM l. 36** : délais selon C-1.
8. **TG** : essais de C-8.

## Annexe — ce que j'ai fait et pas fait

- Essais sur processeur (bloc-notes `/tmp/claude-0/-home-claude/03748db6-42ca-5241-871c-5399d39c1451/scratchpad/`) :
  copie `copie-21a6e583/` (`git archive`) ; sortie des tests `pytest-graine.txt` ; scripts `essais/egalite_log_double.py`,
  `essais/ecart_differentiel.py`, `essais/compte_balayages.py` (sorties citées ci-dessus, non scellées, hors du dépôt).
- Aucun `git fetch`, aucun `checkout`, `switch`, `worktree`, `stash`, `reset` ; aucun commit ; aucun `.sha256` ;
  aucune donnée de R1, R2, R4 ni P3 (rien sous `donnees/` lu ; `donnees/` est présent dans la copie extraite, non ouvert) ;
  aucun appel de réseau ni de modèle (réseau de Hugging Face coupé par variables d'environnement) ; `nice -n 10`. Un seul
  fichier neuf : celui-ci, à sceller par la session.

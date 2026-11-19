# Vérification du programme de comparaison d'une lentille réajustée à celle du 18 novembre, version 2, et de ses essais — v1

- Heure (`date -u`) : 2026-11-19T10:52:09Z.
- Vérificateur : sous-agent, modèle Fable 5.2 (`claude-fable-5-2`) ; le programme et ses essais sont écrits par la session des
  lentilles sur Claude Opus 5.5. Je n'ai écrit ni l'un ni les autres.
- Mandat, tel que la mère l'a resserré : le programme et ses essais seulement. Le critère v3 et le devis v3 ne sont **pas** jugés
  ici (ils sont récrits en version 4 par un rédacteur sur Fable 5.2 et seront vérifiés par un autre modèle). Les remarques déjà
  notées sur le critère v3 sont en annexe, sans verdict. Le devis v3 n'a pas été lu.
- Objet : branche `claude/brave-galileo-jhp684`, commit `ebe13788cc5530e19e89f334e8d83e8fde19ca8f`, lu par son identifiant.
  Empreintes recalculées, égales à leur compagnon : `src/controle_ia/neuron_lens/comparer_reajustement_v2.py`
  `23311588f2d3b9f45a9b6b052e8de22742a164640585d7c1361c20dee2115877` ;
  `tests/test_neuron_lens_comparer_reajustement_v2.py` `65822ab580d49fdf988de59b044ed61df24aed74e01e2e2a6c818c185b91f1ef`.
- Corrections de référence : D1 à D3 et D6 telles qu'écrites dans ma vérification de la v2
  (`docs/notes/neuron-lens-v1/verification-critere-identite-reajustement-v2-v1.md`, `8a6045bb…`).
- Fait, dans mon sous-dossier du bloc-notes, sur une copie des fichiers du commit : les 82 essais rejoués ; les 53 altérations du
  premier banc portées sur le texte de la v2, plus 40 altérations des gardes neuves, une copie par altération, témoin non modifié
  en tête ; 34 sondes du programme d'origine par de vrais fichiers et la ligne de commande.
- Mêmes interdits, tenus. Aucune dépense, aucune machine, aucun commit, aucun fichier existant modifié. Aucun refus d'outil.

## Conclusion

**Pas avant : une version 3 du programme, avec deux gardes manquantes (F1, F2), trois ajouts courts (F3 à F5) et les essais des
gardes qui survivent (F6).** Les corrections D1 à D3 sont faites et tiennent : à empreinte égale, les cinq anomalies suspendent la
mention, et rien ne sort avant les contrôles. Mais la pièce d'export « neuve » de R n'est rattachée à aucune course : donner par
erreur celle du 18 rend « 31 matrices égales sur 31 » et des séries à écart nul, chiffres que le billet doit citer. Et la fonction
de calcul n'est comparée qu'entre les deux lanceurs donnés : le même lanceur modifié, donné deux fois, passe.

Dernière ligne des essais rejoués : `82 passed in 4.52s`.

## 1. Conformité à D1, D2, D3 et D6

| correction | état | reste |
|---|---|---|
| D1, cohérence exigée au premier palier | **faite** : préalables et table des écarts calculés avant toute mention ; suspension sur préalable manqué, taille différente, écart supérieur à 10⁻⁹, export de R absent ou incomplet, matrice différente | la borne de 10⁻⁹ n'est fixée par aucun essai ; les séries de R n'entrent pas dans la cohérence (F4) |
| D2, préalables de provenance | **faite** : empreintes bien formées, tailles, `finies`, pièces de référence vérifiées sur les octets lus, course distincte, manifeste neuf rattaché au résultat neuf, six champs de configuration | la fonction de référence n'est pas fixée (F2) ; le calcul des empreintes sur les octets lus n'est joué par aucun essai (F6) |
| D3, pièces d'export de R obligatoires et complètes | **faite** : 31 couches de matrices, 28 couches finies par série, des deux côtés | l'export neuf n'est rattaché à aucune course (F1) ; les couches ne sont pas comparées d'un côté à l'autre (F3) |
| D6, part du programme | **faite en partie** : ligne de commande versée dans la sortie, exports de R exigés, reprise notée | « la comparaison des manifestes » se réduit à sept champs ; aucune table des versions (F5) |

## 2. Le premier palier, à empreinte égale — **les cinq cas sont détectés ; aucune sortie avant les contrôles**

Sondes par de vrais fichiers et la ligne de commande, sur une course neuve fictive (copie des pièces du 18, identifiant, heure de
début et manifeste neufs) :

| sonde | cas | mention rendue |
|---|---|---|
| P1 | cas sain, R puis S | premier palier, déclencheur (i) |
| P2 | préalable manqué (`n_docs`) | **suspendue**, déclencheur (v) |
| P2b | une valeur `nan` | **suspendue**, aucun maximum calculé |
| P3 | taille différente | **suspendue** |
| P4 | écart de 2 × 10⁻⁹ | **suspendue** |
| P4b | écart de 5 × 10⁻¹⁰ | premier palier (sous la borne) |
| P5, P5b | R sans pièces d'export ; export à 30 couches de matrices | **suspendue** |
| P6 | une empreinte de matrice différente | **suspendue**, 30 égales sur 31 comptées |
| P7 | la référence comparée à elle-même | **suspendue** (course non distincte) |
| P8 à P8e | pièce de référence, manifeste de référence, export de référence modifiés d'un octet ; manifeste neuf modifié après coup | « non comparable », ou **suspendue** à empreinte égale |
| **P6b** | empreinte égale, matrices égales, une valeur de série de R déplacée de 0,01 | **premier palier, sans anomalie** : pièces contradictoires non vues (F4) |

Le programme calcule tous les préalables avant de choisir une branche, n'écrit sa sortie qu'après la comparaison, et refuse
d'écraser avant de lire. Un `nan`, une valeur absente ou non numérique, un compte différent, une cible vide ou en plus rendent
« non comparable » ou suspendent le premier palier, sans maximum calculé.

## 3. Trous trouvés par les sondes (programme d'origine)

| sonde | cas | ce que rend le programme | attendu |
|---|---|---|---|
| **T2** | octets différents ; la pièce d'export « neuve » donnée est le fichier d'export du 18 | **deuxième palier, « 31 matrices égales sur 31 », séries à écart nul**, aucune alerte | « non comparable » |
| **T2b** | export neuf d'une autre course que l'ajustement neuf (identifiant et manifeste différents) | deuxième palier, aucune alerte | « non comparable » |
| **T1** | le même lanceur, fonction de calcul modifiée, donné des deux côtés | deuxième palier, préalable « même texte de la fonction » tenu | « non comparable » |
| T3 | série de l'export neuf aux couches décalées (1 à 28) | deuxième palier, « 27 couches », écart maximal de 0,136 rapporté sans alerte | « non comparable » |
| T3b | série sans aucune couche commune | arrêt sur une erreur (`max()` d'une suite vide), aucune sortie | « non comparable » |
| T3c | matrices aux couches décalées, octets différents | deuxième palier, « 0 égale sur 31 », sans alerte | « non comparable » |
| T8 | versions de bibliothèques du manifeste neuf toutes changées | rien dans la sortie | table des différences, rapportée |
| T11 | champ `etape` du résultat neuf changé | rien | préalable (mineur) |

T2 est le plus sérieux : les deux séries de R et le compte des matrices sont les seuls chiffres sensibles à la position de la
lentille, et ma correction D5 les rend obligatoires dans le billet. Une erreur d'argument les rend nuls et flatteurs, sans
déclencheur. T1 vide un préalable : rien ne dit que la fonction du lanceur de référence est celle du 18.

## 4. Les altérations rejouées

Témoin non modifié : `82 passed`.

**A. Les 53 altérations du premier banc : 50 tuées, 3 survivent** (23 survivaient sur la v1).

| altération qui survit | portée |
|---|---|
| déclencheur (iii), « lentille différente », retiré | **régression des essais** : la v1 le vérifiait ; l'audit « le même dans les deux sens » part de ce déclencheur |
| déclencheur (iv), « non comparable », retiré | **régression des essais**, même portée |
| garde de finitude du maximum retirée | garde redondante, jamais atteinte ; un essai direct de la fonction suffit |

Toutes les autres sont tuées, dont celles qui décidaient de la mention : tolérance à 1,5 × 10⁻³, « < » au lieu de « ≤ », écart signé,
premier palier sans empreinte, `meta` absent, séries de R absentes ou nulles.

**B. 40 altérations des gardes neuves de la v2 : 22 tuées, 18 survivent.**

| altération qui survit | portée |
|---|---|
| empreinte de la pièce d'ajustement de référence non calculée sur les octets lus | **cœur de D2** : aucun essai ne donne un mauvais fichier au programme ; les essais injectent l'empreinte dans un dictionnaire |
| empreinte du manifeste de référence non calculée sur les octets lus | idem |
| empreinte de l'export de référence non calculée sur les octets lus | idem |
| empreinte du manifeste neuf recopiée du résultat au lieu d'être calculée | idem |
| borne de cohérence du premier palier à 10⁻³ ; à 10⁻¹² | la borne de 10⁻⁹ n'est fixée par aucun essai |
| course distincte jugée sur l'identifiant seul ; sur l'heure de début seule | les essais changent toujours les deux ensemble |
| taille présente : toujours tenue | aucun essai sans taille |
| champ de configuration absent des deux côtés accepté ; `graines` retiré de la liste des six champs | la liste n'est fixée par aucun essai |
| forme des empreintes de matrices non vérifiée | aucun essai |
| liste vide acceptée pour une cible, des deux côtés | aucun essai |
| plage des séries du 18 lue du côté neuf | l'essai vérifie seulement « minimum < maximum » ; ces deux chiffres vont dans la phrase du billet |
| forme de l'empreinte non exigée pour l'égalité d'octets ; manifeste neuf absent des deux côtés ; tolérance écrite en dur dans la mention ; lentille lue du côté neuf | sans effet atteignable : un autre préalable bloque, ou le cas ne peut pas venir d'un fichier ; aucun essai demandé |

L'auteur annonce dix altérations, toutes tuées : je le confirme, les dix se retrouvent dans mon banc et y sont tuées. Son banc ne
comprenait ni les déclencheurs, ni le calcul des empreintes sur les octets lus.

## Corrections (texte avant et après)

**F1 — L'export neuf de R rattaché à la course neuve (l. 262-266 et `preconditions`).**
- Avant : `c["eneuf"] = lire(neuf_export)[0].get("resultat")` — l'enveloppe de l'export neuf (identifiant de course, empreinte du
  manifeste) est jetée, et son empreinte n'est pas calculée.
- Après : garder l'enveloppe et l'empreinte du fichier ; trois préalables de plus pour R : identifiant de course de l'export neuf
  égal à celui de l'ajustement neuf ; empreinte du manifeste portée par l'export neuf égale à celle de l'ajustement neuf ; fichier
  d'export neuf d'empreinte différente de l'export de référence. Essais : T2, T2b.

**F2 — La fonction de calcul de référence fixée par une constante (l. 37-42 et l. 138).**
- Avant : `p(f"même texte de la fonction {FONCTION}, présent", bool(c["fref"]) and c["fref"] == c["fneuf"], …)`.
- Après : ajouter à `REFERENCES` l'empreinte du texte de `_split_half_64` du lanceur du 18,
  `a5495c68779bb67059cade18b3a92aaf7cf7fd0200f1770b038d8c5d0e62703c` (calculée par `empreinte_fonction` sur
  `b_beta_lancer_v3.py`, `582fd9ef…`), et exiger `c["fref"] == REFERENCES["fonction"] and c["fref"] == c["fneuf"]`. Essai : T1.

**F3 — Mêmes couches des deux côtés (l. 146, l. 152, l. 175-177).**
- Avant : seuls les nombres de couches sont vérifiés (31 et 28) ; `couches = sorted(set(a) & set(b), key=int)`.
- Après : préalables « couches des matrices : 0 à 30 des deux côtés » et « couches de chaque série : 0 à 27 des deux côtés » ;
  `_series_r` n'a plus d'intersection à faire. Essais : T3, T3b, T3c.

**F4 — Les séries de R dans la cohérence du premier palier (l. 213-221).**
- Avant : quatre causes d'anomalie ; les séries ne sont que rapportées.
- Après : cinquième cause, pour R : « écart d'une série supérieur à 10⁻⁹ à empreinte égale » (mêmes matrices, même lentille
  publique : même valeur). Essai : P6b.

**F5 — Table des différences des manifestes, rapportée sans critère (D6).**
- Avant : sept champs comparés comme préalables ; rien d'autre dans la sortie.
- Après : un champ `differences_des_manifestes_sans_critere` : pour `versions`, `commit` et les champs de `config` hors
  préalables, la liste des clés qui diffèrent avec les deux valeurs. Essai : T8.

**F6 — Essais à ajouter.**
- Avant : 82 essais.
- Après, un essai par ligne :
  1. « différente » porte le déclencheur (iii) ; « non comparable » porte le déclencheur (iv) ;
  2. par de vrais fichiers donnés à `charger` ou à `main` : pièce d'ajustement de référence, manifeste de référence, export de
     référence modifiés d'un octet ; manifeste neuf modifié après coup (P8 à P8e) ;
  3. premier palier : 2 × 10⁻⁹ suspend, 5 × 10⁻¹⁰ ne suspend pas ; la constante vaut 10⁻⁹ ;
  4. course distincte : identifiant neuf et même heure ; heure neuve et même identifiant (T7, T7b) ;
  5. taille absente au deuxième palier (T4) ;
  6. un champ de configuration absent des deux côtés ; la liste des six champs égale à celle du critère ;
  7. une empreinte de matrice mal formée ; une cible à liste vide des deux côtés ;
  8. `ref_min` et `ref_max` égaux au minimum et au maximum de la série du 18, le côté neuf étant altéré ;
  9. la garde de finitude du maximum, par un appel direct.

## Remarques mineures
1. Le champ `etape` du résultat (« ajustement-R », « ajustement-S ») pourrait être un préalable (T11).
2. `--reprise` reste une indication donnée à la main ; si le résultat de la course neuve porte un champ de reprise, le lire.
3. Le lanceur neuf donné en argument n'est rattaché à la course neuve par rien (le manifeste neuf porte un commit) ; à dire dans
   l'audit ou à vérifier par le programme.

## Annexe — remarques pour le rédacteur de la version 4 du critère (sans verdict)
Notées en lisant le critère v3 avant le changement de mandat. Le devis v3 n'a pas été lu.
1. **Déclencheur (v).** Le § 5 du critère v3 le définit pour la seule matrice différente ; le § 3, point 4, et le programme
   l'emploient pour toute anomalie à empreinte égale. À aligner.
2. **« La comparaison des manifestes ».** Le § 5 dit que le programme la donne ; il ne compare que sept champs (F5).
3. **Préalables à reprendre si F1 à F4 sont retenues** : export neuf rattaché à la course neuve ; fonction de référence fixée ;
   mêmes couches des deux côtés ; séries de R dans la cohérence du premier palier.
4. **Phrase permise et cas mixte.** La phrase du deuxième palier est écrite au pluriel pour les deux lentilles, alors que chaque
   lentille est jugée seule. Si R est au premier palier et S au deuxième (ou l'inverse), il faut une phrase par lentille.
5. **§ 3, en tête.** Le programme v1 y est encore cité, puis dit « remplacé » : ne citer que le programme en vigueur.
6. **Mesurer au lieu de supposer.** La tolérance et l'espoir d'un premier palier reposent sur une grandeur que le critère dit non
   mesurée : l'écart d'un réajustement d'une machine à l'autre. Un essai court le mesurerait avant la course : le même ajustement
   sur quelques dizaines de documents, deux fois, sur deux machines, puis la comparaison des empreintes et des différences entre
   moitiés. C'est une dépense, donc un nœud de Lazar sur devis ; elle dirait si l'égalité d'octets est plausible avant d'engager la
   course entière.
7. **Ce que la course neuve doit laisser.** Le 18 n'a laissé aucune grandeur qui compare deux matrices. La course neuve peut verser,
   pour chaque matrice de chaque lentille, un croquis numérique (projections sur des vecteurs tirés d'une graine fixée, normes par
   couche) : un réajustement futur pourrait alors mesurer la distance entre matrices, ce qui est impossible aujourd'hui. Cela
   relève de la règle « récupérer ce qui est récupérable ».
8. **Variante et palier.** Au deuxième palier, la lentille rangée par l'ajustement seul n'a aucune mesure propre ; seule la course
   rejouée lui en donne. Le choix de la variante dépend donc de la chance d'un premier palier, aujourd'hui inconnue (remarque 6).

## Ce qui a servi (hors dépôt, sous-dossier du bloc-notes)
`mutations_v2.py` (93 altérations par remplacement de texte, témoin en tête) et `sondes_v2.py` (34 appels de la ligne de
commande sur des fichiers écrits dans le sous-dossier). Aucun n'écrit dans le dépôt.

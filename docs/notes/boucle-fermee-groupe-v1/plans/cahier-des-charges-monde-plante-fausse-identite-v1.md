# Cahier des charges : génération de mondes synthétiques de termes scientifiques à vérité plantée (version 1)

- **Destinataire** : un sous-agent neuf, le « tiers », qui écrit le générateur, produit les mondes et les scelle. **Rédacteur** : concepteur Claude Opus 5.5 neuf, mandat GO-2026-11-24-46, 2026-11-24. Classe A (pièce d'une épreuve décisive). Processeur seul, aucune dépense, aucun appel réseau.
- **Cloisonnement** : tu ne sais pas, et tu ne cherches pas à savoir, quelles méthodes d'analyse seront appliquées aux mondes. Tu lis ce cahier et, dans le dépôt, seulement `src/controle_ia/scellement.py`, `src/controle_ia/manifeste.py` et `src/controle_ia/gardes.py`. Tu n'ouvres rien d'autre sous `docs/notes/boucle-fermee-groupe-v1/`, ni la branche `idees/lot-8-chef-d-orchestre-v1`, ni `coffre/`, `docs/verdicts/`, `diag/`, `versement/`. Tu ne lances sur les mondes aucune analyse autre que les contrôles du § 8, et tu ne règles aucun paramètre en vue d'un résultat d'analyse.
- **Ce qui t'est laissé** : les formes fonctionnelles et les valeurs numériques marquées « au choix du tiers », dans les bornes données. Tu les écris toutes dans la configuration, que tu scelles avant de générer.

## 1. Objets d'un monde

- **Domaines** : 8 par monde. Chaque domaine a 12 grandeurs partenaires (identifiants `G<domaine>_<k>`), 4 instruments (`I<domaine>_<k>`, en deux familles : A = instruments 1 et 2, B = instruments 3 et 4), 4 laboratoires (`L<domaine>_<k>`), un lexique de domaine de 150 mots, un lexique de 25 mots par instrument. S'y ajoutent, communs à tous les domaines, 400 mots généraux et 20 mots de désaccord. Tous les mots sont des jetons opaques (`w` suivi de 5 chiffres tirés au hasard), sans sens.
- **Termes jugés** : 150 par monde, jetons opaques (`T` suivi de 4 chiffres tirés au hasard, sans lien avec la classe). Chaque terme désigne une ou deux **composantes latentes** (grandeurs ou sens cachés), selon sa classe (§ 3). Chaque composante a un lexique propre de 30 mots tirés du lexique de son domaine.
- **Documents** : chacun a un identifiant opaque, une année entière de 0 à 39 (uniforme sauf mention contraire), un laboratoire (uniforme parmi les 4 du domaine sauf mention contraire), un genre (`experimental` 0,60 ; `theorique` 0,25 ; `revue` 0,15), un domaine (celui du laboratoire). Un document contient des mentions de 1 à 3 termes jugés de son domaine (pour N6, du domaine du sens porté) ; pour un terme présent, 1 + Poisson(1) mentions. Le nombre de mentions par document varie donc ; tu l'enregistres tel quel.
- **Mention** : une occurrence d'un terme dans un document, portée par une seule composante latente (tirée selon la classe), avec un instrument (tiré selon le § 4) et 6 mots de contexte de surface. Chaque mot est tiré, indépendamment : mot général (0,35), mot du lexique du domaine (0,25), mot du lexique de l'instrument de la mention (0,15), mot du lexique propre de la composante latente (0,25). Puis, avec la probabilité r propre au terme (r tiré uniforme sur [0,05 ; 0,30], même loi pour toutes les classes), un des 6 mots, choisi au hasard, est remplacé par un mot de désaccord.
- **Enregistrement quantitatif** : chaque mention porte K = 1 + Binomiale(4 ; 0,5) enregistrements. Chacun relie le terme à un prédicat (une grandeur partenaire de la composante de la mention, tirée uniformément parmi ses prédicats), avec : x (valeur de la grandeur partenaire, uniforme sur [0,1]), y (valeur mesurée attribuée au terme), z (variable de régime, uniforme sur [0,1]), x2 (covariable secondaire, uniforme sur [0,1]), l'instrument de la mention, et un mode d'obtention (`observation` 0,2 ; `x_controle` 0,4 ; `y_controle` 0,4), tirés indépendamment sauf mention contraire.
- **Lois** : pour chaque composante q et chaque prédicat p, une loi sans bruit y\* = f_{q,p}(x) (ou f(x, z), f(x, x2), selon la classe). Famille au choix du tiers, au moins trois formes strictement monotones sur [0,1] (par exemple affine, saturante, puissance, sigmoïde), paramètres tirés au hasard, amplitude ramenée à 1 sur [0,1]. Mesure : y = g_{t,i}(y_rapporté) + ε, où y_rapporté est y\* (ou son approximation, classe N1b), g_{t,i} l'étalonnage permanent de l'instrument i pour le terme t (strictement croissant, inversible), ε ~ N(0, σ²) avec σ = 1/RSB (rapport signal sur bruit, § 4). Étalonnage « léger » par défaut : g(u) = o + s·u, o uniforme sur [−0,2 ; 0,2], s uniforme sur [0,8 ; 1,25].
- **Quantité par terme** : sauf mention contraire, un terme porte en tout **trois prédicats**, tirés parmi les 12 grandeurs de son domaine.

## 2. Format des fichiers publics (par monde ; CSV UTF-8, virgule, lignes mélangées au hasard)

- `documents.csv` : `doc_id, annee, labo_id, genre, domaine_id`.
- `mentions.csv` : `mention_id, doc_id, terme, contexte` (les 6 mots séparés par une espace, dans l'ordre tiré).
- `enregistrements.csv` : `enr_id, mention_id, terme, predicat, x, y, z, x2, instrument_id, mode`.
- `termes.csv` : `terme` (les 150 termes jugés, ordre aléatoire).
Aucun autre champ. Aucun identifiant ne doit porter d'information sur la classe, la composante ou le camp.

## 3. Classes à planter (vérité du monde)

**P, fausse identité** : deux grandeurs latentes distinctes q1 et q2 sous un même terme. Chaque mention porte q2 avec la probabilité w (uniforme sur [0,3 ; 0,5]), q1 sinon. Sur deux des trois prédicats (« prédicats en désaccord »), les lois de q1 et q2 diffèrent ; sur le troisième, elles sont égales. La composante de la mention gouverne conjointement tous ses enregistrements. Trois formes, en parts égales : **inversion** (sur les prédicats en désaccord, f_{q2,p} décroît en x là où f_{q1,p} croît) ; **plat** (f_{q2,p} constante en x) ; **cardinale** (les deux croissent, mais l'écart maximal |f_{q1,p} − f_{q2,p}| sur [0,1] vaut au moins 0,3). Les lois ne dépendent ni de z, ni de x2, ni du mode. Mode documentaire, en parts égales : **co-occurrent** (les composantes des mentions d'un même document sont tirées indépendamment) ou **cloisonné** (toutes les mentions du terme dans un même document portent la même composante). Les lexiques propres de q1 et q2 partagent une fraction λ de leurs mots, λ ∈ {0,8 ; 0,5} en parts égales. Le laboratoire du document est tiré sans lien avec la composante.

**N1, vraie identité** (une seule grandeur latente). **N1a, biais d'instrument** : étalonnage « fort » propre à chaque instrument : o uniforme sur [−1 ; 1], s uniforme sur [0,5 ; 2], et, pour la moitié des instruments, une déformation strictement croissante non affine (au choix du tiers, par exemple u ↦ (e^{κu} − 1)/(e^{κ} − 1), κ uniforme sur [1 ; 3]). **N1b, ordres d'approximation** : la loi vraie est non linéaire ; les enregistrements des documents `theorique` et ceux des instruments de la famille B rapportent à la place son développement de Taylor d'ordre 1 ou 2 (ordre tiré par terme) autour de x0 uniforme sur [0,3 ; 0,7]. Chaque approximation doit rester strictement monotone sur [0,1], de même sens que la loi, et s'en écarter d'au moins 0,15 quelque part sur [0,1] ; sinon on retire la loi.

**N2, concept unique dont la loi dépend d'une covariable observée** (une seule grandeur). Sur deux des trois prédicats : **N2a, variable de régime** : le sens de variation en x s'inverse quand z franchit z\* (uniforme sur [0,3 ; 0,7]), de façon continue mais rapide (largeur de transition au plus 0,1) ; **N2b, loi multivariée** : y\* = f(x, x2) et le sens de variation en x s'inverse quand x2 franchit x2\* (uniforme sur [0,3 ; 0,7]) ; **N2c, rétroaction** : en mode `x_controle`, y croît avec x ; en mode `y_controle`, c'est la valeur du terme qui est imposée et la grandeur partenaire répond en sens inverse (x décroît quand y croît) ; en mode `observation`, valeurs d'équilibre bruitées sur les deux grandeurs (au choix du tiers, à déclarer). Paramètre de recouvrement, en parts égales : **complet** (z, x2, mode indépendants de l'instrument) ou **partiel** (pour 80 % des enregistrements, la famille A va avec z < z\*, resp. x2 < x2\*, resp. mode `x_controle`, et la famille B avec l'autre côté).

**N3, controverse sur un concept unique** (une seule grandeur vraie). Un des 4 laboratoires du domaine, tiré au hasard, forme le camp B ; les autres, le camp A. **N3j, controverse jumelle** : chaque terme N3j est le jumeau d'un terme P désigné du même monde et du même domaine : mêmes paramètres (forme, w, λ, alignement, RSB, fréquence, mode d'instrument, lois), mêmes procédures de tirage, tirages indépendants. Les mentions de la composante 2 (le camp B, qui rapporte la loi rivale) sont placées dans des documents du laboratoire du camp B, celles de la composante 1 dans des documents des autres laboratoires. Ainsi, enregistrement par enregistrement (prédicat, x, y, z, x2, instrument, mode, et mots de contexte de la mention), la loi est **identique** à celle du jumeau P ; seuls le rattachement de la composante (au laboratoire au lieu de la mention) et ce qui en découle diffèrent. **N3o, controverse ordinaire** : une seule composante latente, laboratoires des documents tirés uniformément ; le camp B rapporte, sur un seul prédicat, une loi rivale (inversée ou plate, en parts égales) jusqu'à l'année t_res (uniforme sur [20 ; 30]), puis la loi vraie.

**N4, identité promue en principe** (une seule grandeur, deux définitions opératoires : les familles d'instruments A et B mesurent la même grandeur sur les trois prédicats). Avant l'année t_p (uniforme sur [15 ; 25]), les mesures de la famille B portent une distorsion transitoire, de poids décroissant linéairement de 1 (année 0) à 0 (année t_p) : **N4m** : distorsion strictement croissante (décalage jusqu'à ±0,5 et facteur jusqu'à 2) ; **N4t** : sur deux prédicats, la famille B rapporte au début une loi de sens de variation opposé à la vraie. Après t_p, les deux familles s'accordent au bruit près.

**N5, polysémie dans un même domaine** : deux sens latents du même domaine, mêmes laboratoires, documents et instruments. Moitié « sans prédicat commun » : sens 1 sur {p1, p3}, sens 2 sur {p2} ; moitié « avec prédicat commun » : sens 1 sur {p1, p3}, sens 2 sur {p2, p3}, avec une **même** loi sur p3. Lexiques propres partageant λ = 0,3 de leurs mots ; w comme pour P.

**N6, homonymes** : deux sens dans deux domaines distincts D1 et D2 : sens 1 sur deux prédicats de D1, sens 2 sur un prédicat de D2 ; les mentions du sens 2 sont dans des documents de laboratoires de D2, avec instruments et mots de D2 ; lexiques propres disjoints ; w comme pour P. Le monde compte ces mentions dans le terme jugé de D1.

## 4. Paramètres de difficulté, et équilibre

- **Fréquence** (nombre de mentions du terme), trois niveaux en parts égales dans chaque classe : rare (entier uniforme de 12 à 18), moyen (80 à 120), fréquent (300 à 450).
- **RSB** ∈ {4 ; 1,5}, en parts égales.
- **Alignement a** ∈ {0,6 ; 0,9}, en parts égales, pour les termes à deux composantes (P, N3j, N5) : une mention de la composante 1 prend un instrument de la famille A avec la probabilité a, de la famille B sinon ; la composante 2, l'inverse ; instrument uniforme dans la famille tirée. Ailleurs, instrument uniforme parmi les 4, sauf N1b, N2 « partiel » et N4 (définis au § 3).
- Croiser fréquence × RSB × alignement dans chaque classe et sous-classe, puis, pour P, forme, mode documentaire et λ, aussi également que les effectifs le permettent, par affectation stratifiée tirée par graine ; sceller la table d'affectation dans la vérité.

## 5. Effectifs

| ensemble | mondes | P (dont jumeaux de N3j) | N1 (a/b) | N2 (a/b/c) | N3 (j/o) | N4 (m/t) | N5 | N6 | total |
|---|---|---|---|---|---|---|---|---|---|
| étalonnage | 6 (E0…E5) | 180 (60) | 120 (60/60) | 120 (40/40/40) | 120 (60/60) | 120 (60/60) | 120 | 120 | 900 |
| jugé | 6 (J0…J5) | 180 (60) | idem | idem | idem | idem | 120 | 120 | 900 |
| réserve | 3 (R0…R2) | 90 (30) | 60 | 60 | 60 | 60 | 60 | 60 | 450 |

Par monde : P 30 (dont 10 jumeaux, formes équilibrées), chaque autre classe 20 (N3 : 10 j, 10 o). Les mondes d'un même ensemble ne diffèrent que par leur graine.

## 6. Vérité (jamais dans les fichiers publics)

- `verite_termes.csv` : `terme, monde, classe` (P, N1a, N1b, N2a, N2b, N2c, N3j, N3o, N4m, N4t, N5, N6), `forme, jumeau, n_latent` (2 pour P, N5, N6 ; 1 sinon), `niveau_frequence, rsb, alignement, mode_documents, lambda, w, recouvrement, z_etoile, x2_etoile, t_res, t_p, ordre_approx, predicats_desaccord, laboratoire_camp_B`.
- `verite_mentions.csv` : `mention_id, composante` (1 ou 2 ; pour N3j, 2 = camp B).
- `verite_enregistrements.csv` : `enr_id, composante_latente` (identité de la grandeur ou du sens latent : 1 ou 2 pour n_latent = 2, sinon 1 ; pour N3j, toujours 1), `camp` (A, B ou vide), `y_etoile` (valeur sans bruit, avant étalonnage, sous la loi vraie de la composante), `y_corrige` (g_{t,i}^{-1}(y) : valeur observée débarrassée de l'étalonnage permanent, bruit et distorsions transitoires gardés), `approx` (0, 1 ou 2).

## 7. Graines, scellement, noms

- Racine : `runs/monde-plante-fausse-identite-v1/`. Graines (R9) : entropie E tirée par `secrets.randbits(63)`, écrite dans `graines-monde-plante-v1.json` avec les graines dérivées par `controle_ia.manifeste.graines` pour les tâches `etalonnage-E0`…`etalonnage-E5`, `juge-J0`…`juge-J5`, `reserve-R0`…`reserve-R2` (clés de dérivation distinctes, donc flux disjoints) ; tout tirage d'un monde vient de son seul flux.
- Ordre : (1) écrire et sceller `generateur_monde_plante_v1.py` (numpy ≥ 1.25 seul, plus la bibliothèque standard), `config-monde-plante-v1.json` (tous tes choix) et `graines-monde-plante-v1.json`, puis committer ; (2) générer ; (3) sceller chaque fichier public sous `mondes/etalonnage/E<k>/`, `mondes/juges/J<k>/`, `mondes/reserve/R<k>/` ; (4) sceller la vérité de l'étalonnage sous `verite-etalonnage/E<k>/` ; (5) mettre la vérité des mondes jugés dans `verite-juges-v1.zip` et celle de la réserve dans `verite-reserve-v1.zip`, sceller les deux archives, les placer sous `scelle/` et inscrire leurs empreintes dans le manifeste et le rapport ; ne pas les rouvrir ; (6) manifeste de run par `controle_ia.manifeste.creer_manifeste` ; livrable `livrables/monde-plante-fausse-identite-v1.zip` (sans les deux archives de vérité scellée).

## 8. Contrôles du tiers (aucune méthode d'analyse ; rapport `controles-tiers-v1.md`, scellé)

1. Effectifs par monde, classe et sous-classe, conformes au § 5 ; table de croisement des paramètres du § 4.
2. Pour chaque classe : moyenne et écart-type du nombre de mentions et d'enregistrements, par niveau de fréquence ; l'écart entre classes doit rester sous 5 % de la moyenne générale.
3. Monotonie stricte vérifiée sur une grille de 1 001 points pour chaque loi, chaque étalonnage et chaque approximation ; |g^{-1}(g(u)) − u| < 1e-9 ; écarts d'approximation ≥ 0,15.
4. Jumeaux : pour chaque paire P–N3j, identité des paramètres et du chemin de code des tirages d'enregistrements, montrée par le code (pas par une comparaison des données).
5. Graines : flux distincts ; régénérer un monde de chaque ensemble à partir de sa graine et retrouver les mêmes empreintes.
6. Fichiers publics : aucun champ hors du § 2 ; identifiants opaques ; lignes mélangées.
Tout écart arrête la production et se rapporte tel quel ; aucune correction silencieuse.

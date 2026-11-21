# Rapport du développeur — programme de vérification de la sortie de l'auteur des mondes plantés (course « seuil et moniteurs ») — v5

- Auteur : développeur du programme de vérification de la sortie des mondes, modèle O. Écrit le 2026-11-21.
- Version : la v5 **complète** le rapport v4 (`f135edc645549acece69338a369b8cc4de68f1a20b76772994a79c09bf9271da`, gardé intact), qui reste la référence pour tout ce qui ne change pas : D1, D2 et la dérive de F, D3, la tranche voisine, R1, R2. Elle ne dit que ce qui change.
- Cause : l'arbitrage de l'unité des décalages du saboteur, `docs/notes/ideation-seuil-moniteurs-v1/arbitrage-unite-decalages-v1/arbitrage-fable-unite-decalages-v1.md`. Il est lu sur `origin/main` par `git show` redirigé après `fetch origin main` ; son empreinte, `a8f8acfabf2757a383dd459be2dcd352cd4ad2a3bd53a0ad82986cc1be989636`, est égale à son compagnon sur `origin/main`. Il est lu en entier, avec le mot de la mère relayé par le coordinateur.
- Statut : instrument (classe B), **non contre-lu**. Aucun appel, aucune dépense, aucune clé, aucun commit, aucun refus de permission, de classifieur ni de garde.

## 0. Verdict

1. **Lecture déclarée de session** : les trois décalages du saboteur se lisent en écarts types de la loi honnête de la tranche, c'est-à-dire la racine de la variance de `loi_honnete` entière. C'est le choix `CH5` des versions précédentes, inchangé dans la conversion.
2. **Le contrôle par l'aire, condition de Fable, est écrit** (l. 1256 à 1640). Il ne lit que les lois et les nombres de l'auteur. Pour chaque famille, visible ou à l'écart, pour chaque tranche et pour chacun des trois nombres, il calcule l'aire réalisée sous la lecture retenue puis, pour diagnostic, sous l'unité brute. Il rend l'une des trois issues :
   - **(a) conforme** : toutes les aires à 0,005 près des aires dites. Tout écart de plus de 0,001 est compté et nommé, par tranche et par aire ;
   - **(b) unité brute constatée** : (a) échoue, et l'unité brute réalise toutes les aires à 0,005 près dans toutes les tranches. Le saboteur n'est pas converti, et le compte rendu dit qu'il faut le mot de la mère ;
   - **(c) non lisible** : rapporté avec sa raison, sans aucun repli. Les raisons sont « aucune unité ne réalise les aires », « écart type indéfini », « loi hors du contrôle » et « calcul impossible ».
3. Sur la **sortie factice v5**, les dix familles sont **conformes**, sans aucun écart de plus de 0,001. Sur la **sortie factice d'essai en unité brute**, la famille A rend **(b)** et les autres restent conformes.
4. Une vérification reste **lisible**, quelle que soit l'issue : aucune issue n'est une faute du § 6. Les issues (b) et (c) sont des observations, et le champ `controle_par_l_aire` du rapport les donne famille par famille.
5. **346 essais, tous passés** (Python 3.13) ; **119 mutations tuées**.

## 1. Le contrôle, ligne par ligne

- **Constantes** (l. 1277 à 1281) : `AIRES_DITES` (0,69, 0,80, 0,95), `TOLERANCE_AIRE_CONFORME` (0,005), `SEUIL_ECART_D_AIRE_NOMME` (0,001), nombre de nœuds de quadrature (2001), plafond des points d'un réseau.
- **Aire** (`aire_realisee`, l. 1553) : P(X + d > Y) + ½ P(X + d = Y), avec X et Y indépendants, de la loi honnête de la tranche. Elle se calcule :
  - **en forme fermée** pour la loi normale : Φ(d / (σ√2)) ;
  - **par une somme finie** pour une loi arrondie (réseau), ex æquo comptés pour moitié ;
  - **par quadrature de Simpson**, après changement de variable en sinus hyperbolique, pour les autres lois continues : Student, Laplace, log-normale, mélange, décalage. L'erreur visée est inférieure à 10⁻⁶, sans borne rigoureuse ; c'est déclaré.
- **Lois** (`loi_pour_l_aire`, l. 1510) :
  - normale, Student, Laplace, log-normale, mélange de lois continues, décalage (de l'écart type de sa base), arrondi au multiple le plus proche ;
  - somme de pas d'un pas normal, qui donne une normale ;
  - grappes, lues sur la normale réduite (CH8 : variance 1, § 3.2, H) ;
  - `bernoulli`, `couple` et `autre` sont **hors du contrôle** et rendent l'issue (c).
- **Écart type** de la lecture retenue : la racine de la variance de la loi entière. Pour un mélange, il comprend la variance entre composantes ; pour un réseau, il est calculé sur les masses. Il est indéfini pour une Student à deux degrés de liberté ou moins.
- **Issues** (`controler_une_famille`, l. 1588) : la règle ci-dessus. Une erreur de calcul rend (c) « calcul impossible », jamais un repli silencieux.
- **En vérification** (`rapporter_controles_par_l_aire`, l. 1627) :
  - observations `O_SABOTEUR_ECART_D_AIRE_AU_DELA_DE_0_001` (chemin du décalage et rang de la tranche), `O_SABOTEUR_UNITE_BRUTE_CONSTATEE` et `O_SABOTEUR_NON_LISIBLE` (avec sa raison) ;
  - champ `controle_par_l_aire` : famille, issue, raison, nombre d'écarts. Aucune aire n'y est recopiée.
- **En correspondance** :
  - un témoin qui demande un saboteur (T05, T07, grandeur `puissance`) n'est converti que si sa famille est conforme ;
  - sinon : `NC_SABOTEUR_EN_UNITE_BRUTE` (l. 1874) ou `NC_SABOTEUR_NON_LISIBLE` (l. 1876) ;
  - le compte rendu porte un bloc `controle_par_l_aire` (`compte_rendu_des_aires`, l. 1995). On y trouve la lecture retenue, les aires dites, la tolérance et le seuil, puis, famille par famille : l'issue, la raison, `mot_de_la_mere_requis`, les écarts nommés, et pour chaque tranche l'écart type et les aires sous les deux lectures. Ce sont des aires calculées sur les lois de l'auteur, non des valeurs vraies de témoins.

## 2. Les sorties factices

- **`fabriquer_sorties_factices_v5.py`** calcule les décalages de chaque famille par un code **indépendant du moteur du programme** :
  - formes fermées pour la normale, la Laplace et les mélanges de normales ;
  - somme finie pour la normale arrondie ;
  - dichotomie pour inverser l'aire.
- Pour que toutes les lois soient calculables en forme fermée, trois lois factices changent :
  - B devient une Laplace(0, 1), au lieu d'une Student à trois degrés ;
  - K, la famille à l'écart, devient le mélange 0,9 N(0, 1) + 0,1 N(0, 3), au lieu d'une log-normale ;
  - la grille de G passe de 0,5 à 0,001. Sur un réseau, l'aire est une fonction en escalier ; un pas fin la rend capable d'approcher les aires dites à mieux que 0,001. Le décalage brut est pris au milieu d'un palier, ce qui le rend stable à l'arrondi à quatre décimales.
- Décalages en écarts types obtenus :
  - normale : 0.7012, 1.1902, 2.3262 (Fable, § 2 : « 0,70, 1,19 et 2,33 » pour une normale) ;
  - Laplace : 0.5816, 1.0368, 2.3135 ;
  - mélange de C et I : 0.7000, 1.1885, 2.3258 ;
  - G : 0.7015, 1.1905, 2.3265 ;
  - K : 0.5887, 1.0135, 2.1809.
- Le décalage de la dérive de F (0.4456) est inchangé.
- **`sortie-factice-essai-unite-brute-v5.json`** (option `--unite-brute`) : la famille A, de loi normale(0, 2) dans ses trois tranches, porte ses décalages en unité brute (1.4025, 2.3805, 4.6523).

## 3. Essais

- **Issue (a)** :
  - la sortie factice saine donne dix familles conformes ;
  - artefact `aire_conforme_factice_saine` : aucune observation, aucun écart ;
  - artefact `aire_ecart_nomme` : le décalage de A pour 0,80 vaut 1.2000, soit une aire de 0,8019 : conforme, avec un écart nommé dans chacune des trois tranches.
- **Issue (b)** :
  - la factice d'essai donne A en unité brute constatée, les autres familles conformes ;
  - en correspondance, T05 et T07 sont `NC_SABOTEUR_EN_UNITE_BRUTE`, et le compte rendu dit `mot_de_la_mere_requis`.
- **Issue (c)**, avec sa raison :
  - A avec les décalages 0,1, 0,2 et 0,3 : « aucune unité ne réalise les aires » ; en correspondance, T07 est `NC_SABOTEUR_NON_LISIBLE` ;
  - B en Student à deux degrés : « écart type indéfini » ;
  - B en Bernoulli : « loi hors du contrôle ».
- **Moteur d'aire**, contre des formes fermées, à 10⁻⁶ près, pour cinq décalages :
  - Laplace : 1 − ½ e^(−d/b)(1 + d/(2b)) ;
  - mélange de normales : Σ wᵢwⱼ Φ((d + μᵢ − μⱼ)/√(σᵢ² + σⱼ²)) ;
  - Cauchy : ½ + arctan(d/(2γ))/π ;
  - normale.
  Le réseau est comparé à la somme de la fabrique, à 10⁻⁹ près.
- **Mutations** :
  - les trois codes d'observation et les deux codes `NC_…` neufs ;
  - « lecture retenue lue en unité brute » (tuée par le cas sain : B, d'écart type √2, cesse d'être conforme) ;
  - « sans repli sur l'unité brute » (tuée par la factice d'essai) ;
  - « tolérance resserrée à 0,0015 » et « seuil d'écart relevé à 0,002 » (tuées par l'écart nommé).

## 4. Rejeux

- Les essais v4 sont rejoués sur la sortie factice v5 : tous passent.
- Correspondance sur la factice v5 : 37 témoins convertis, 2 non convertis (le monde M, D3).
- Programme de vérité v1 scellé : 37 calculés, aucun refus (essai d'acceptation).
- Programme de vérité v2 (`bcd7fbac…`), lancé par `--recalculer … --correspondance …` : 37 calculés, 0 refusé, « dérive cohérente ». Sa sortie est effacée ; j'en ai lu seulement le verdict de la dérive et les comptes.
- Correspondance sur la factice d'essai : 35 témoins convertis, 4 non convertis (LM1, LM2, T05, T07).
- **39 sorties de S** (`rejeu-sorties-de-s-v5.txt`). Une seule différence avec le rejeu v4 : l'observation `O_SABOTEUR_NON_LISIBLE` paraît dans les 34 sorties dont le point 1 est tenu. C'est attendu : ses décalages sont des remplissages, non calibrés sur une aire. Les verdicts et les codes de sortie ne changent pas. Je n'ai lu que des codes.

## 5. Comptes

- **346 essais, tous passés.**
- **Artefacts : 163.**
- **Mutations : 119**, toutes tuées :
  - 75 par code ;
  - 13 par motif de clé ;
  - 18 par correction, dont 4 pour le contrôle par l'aire ;
  - 8 par code `NC_…` ;
  - 1 pour la tranche voisine ;
  - 2 pour la tranche de T09 ;
  - 2 pour les gardes de la correspondance.
- **Autres essais : 64.**
- Toutes les mutations de la v4 sont rejouées.

## 6. Ce que la lettre ne fixe pas (remarques)

1. **Arrondi** : au multiple le plus proche du pas, et les ex æquo comptent pour moitié dans l'aire. Fable (§ 3, point 4) laisse ouvertes la convention des ex æquo pour G et l'ordre « arrondir puis décaler » ; ce sont les lectures de ce programme. Le décalage s'ajoute au score arrondi.
2. **Grappes (H)** : l'aire se lit sur la normale réduite, comme CH8.
3. **Somme de pas** : seul un pas normal est calculé ; sinon l'issue est (c).
4. **Mélange** : poids qui ne somment pas à 1, ou composante sur réseau : issue (c).
5. **Quadrature** : erreur visée inférieure à 10⁻⁶, éprouvée contre quatre formes fermées, non bornée rigoureusement. Une aire tombant à moins de 10⁻⁶ d'un seuil de 0,005 ou de 0,001 pourrait être classée de l'autre côté.
6. **Les écarts de plus de 0,001** ne sont nommés que dans l'issue (a). En (b) et (c), les aires sont au compte rendu de correspondance.
7. **Les issues (b) et (c) ne rendent pas la sortie illisible** et ne changent pas le code de sortie : Fable (§ 2) les tient pour des cas à rapporter, non des fautes du § 6.
8. **Ce que le programme de vérité entend par « écart type »** dans son constructeur `decalage` (Fable, § 3, point 1) : je ne le tranche pas. Ce programme prend la racine de la variance de la loi entière.

## 7. Commandes

`D=/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/dev-verification-sortie-mondes-v5`, une commande par appel.

- Essais : `/home/user/controle-ia-travail/.venv/bin/python -B -m pytest -q -p no:cacheprovider --basetemp=$D/essais-tmp $D/test_verifier_sortie_auteur_mondes_v5.py`. Attendu : 346 passés, en environ trois minutes. Effacer ensuite `$D/essais-tmp`.
- Avant l'envoi : `python3 -I -B $D/verifier_sortie_auteur_mondes_v5.py $D/sortie-factice-saine-v5.json RAPPORT_NEUF.json --motifs LISTE_REELLE`. Attendu : code 0, aucune observation, dix familles conformes.
- À la réception : la même commande, puis `--vers-recalcul`, puis le programme de vérité v2 avec `--correspondance`. Lire `controle_par_l_aire` : toute issue (b) demande le mot de la mère avant tout recalcul des témoins à saboteur.

## 8. Réserves

1. Programme, essais et factices non contre-lus.
2. Quadrature non bornée rigoureusement (remarque 5).
3. Les lois factices B, G et K changent par rapport à la factice v4 ; F et la dérive restent les mêmes.

développeur du programme de vérification de la sortie des mondes, modèle O

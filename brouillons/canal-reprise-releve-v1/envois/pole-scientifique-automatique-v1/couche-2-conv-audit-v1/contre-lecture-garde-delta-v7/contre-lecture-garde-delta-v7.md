# Contre-lecture de la simulation de puissance de la garde appariée δ, v7 — constats GD7-01 à GD7-10

**Déclaration** : je ne suis l'auteur d'aucun des fichiers relus (R2) ; sous-agent neuf, modèle Sonnet (auteur : Fable ; coordinateur : Opus). `date -u` : jeudi 29 octobre 2026, 12:38 UTC.
Interdits respectés : aucune lecture de `donnees/`, de branche git, de `prereg/P3-consignes-v1.md` ni de `diag/*/traces` ; aucune commande git moi-même (les scripts v6 et v7 sont chargés par `importlib` avec `etat_git` neutralisé) ; aucun réseau ; aucune dépense ; aucun fichier existant modifié ; rien scellé.

**Vérifié** : les 43 empreintes compagnons `.sha256` du dossier v7 concordent (`sha256sum -c`, toutes « OK ») ; les 18 préfixes d'empreinte du rapport qui désignent des fichiers retrouvent le bon fichier (trois autres sont des identifiants de commit, non vérifiables sans git).
Pièces lues : rapport `e09c41ae…`, script `027954d8…` (diff intégral contre la v6 `355f61d1…`), manifeste d'ensemble `6dc2e623…`, `tableaux-v7.md` `c5b6c1a5…`, vérifications d'identité et de correspondance, `pari_apparie.py` `ec6c2cf6…` (lecture seule).
Mon rejeu (nouveau dossier, ce dossier) : `rejeu-contre-lecture-gd7-v1.py` `5607832f…`, `rejeu-contre-lecture-gd7-v2.py` `aa526448…` (la v2 ajoute la partie `A_seul`) ; sorties `identite-sortie.json` `db69693e…`, `kappa-fB-sortie.json` `d9c2c96c…`, `stress-garde-sortie.json` `bac4fcd6…`, `combine-sortie.json` `eeb8b6fa…`, `A-seul-sortie.json` `51b547e5…`. Graine 20261029, étiquettes propres, 2 000 répétitions, 288 unités, k = 8, τ = 0,01, δ = 0,05, lecture (A) m = 2 ; durée totale environ 5 minutes sur deux processeurs. Exploratoire, non opposable.

## Réponses courtes

1. **Correspondance bêta** : juste (ρ_b = Var_logit(r_B, σ)/(r_B(1 − r_B)), κ = (1 − ρ_b)/ρ_b, Var[p] = p(1 − p)/(κ + 1) ; je retrouve ρ_b = 0,1696 et κ = 4,895 à σ = 1,0) et c'est le choix **prudent** pour la question « la garde perd-elle quand f_B se disperse ? » : il donne à f_B la plus forte dispersion des deux appariements. L'autre appariement (κ fixée sur f_B) ne change pas la conclusion et va dans le sens favorable (GD7-02, rejeu).
2. **`--K-s`** : branché sans rien changer d'autre ; identité démontrée par une méthode correcte mais incomplète pour le chemin K_s ≠ K_h (GD7-04, rejeu de bout en bout : 24 cellules identiques). « La fiche dépend de K_s, presque pas de K_h » : exact au vu des 60 cellules, mais à **seuil 40, τ = 0,01, écart de contraste 0,10** ; propriété du modèle de simulation, pas du code du juge (GD7-05).
3. **Phrase du brouillon 4** : plus forte que les chiffres sur quatre points (GD7-06, GD7-07).
4. **Cas non essayés** : un compte pour G1, la dispersion de A combinée à celle des B ; les autres sont de second ordre ou favorables (GD7-03).
5. **Lectures hors dossier** : aucune par le script, hors git en lecture (GD7-09).

## Constats

**GD7-01 — rapport l. 38, 159-160, 273-275 ; « la garde ne perd pas » vaut au seuil 40, où elle est presque saturée — à corriger.**
Défaut : « le minimum des 8 gardes reste ≥ 0,995 » et « la garde ne perd pas » sont lus au seuil 40 (m = 2), où la garde atteint déjà 1,000 sans dispersion (n80 de 128 à 212 pour 288 unités, T2) : le test a peu de pouvoir de détection d'une perte. Au seuil 160 (référence), recalculé dans les sorties : à K_h = 5, biais δ/4, le minimum des 8 gardes vaut 0,93 à 0,94 sans dispersion et 0,91 en bêta σ = 1,0 (0,908 à 0,917 ; logit σ = 1,0 : 0,927 à 0,939) ; à K_h = 10 : 0,997 → 0,992. La perte de 0,02 à 0,035 est visible (environ 3 erreurs types de la différence à K_h = 5), cohérente avec n80 + 8 (T2). Ma montée en dispersion (B seule, ρ commun 0,35 puis 0,6) : seuil 40 ≥ 0,989 partout ; seuil 160, K_h = 10, biais δ/4 : 0,974 puis 0,935 ; K_h = 5 : 0,873 puis 0,829.
Correction : écrire « au seuil 40 » à chaque « ≥ 0,995 » ; ajouter « au seuil 160 à K_h = 5 et biais δ/4, 0,91 en bêta σ = 1,0 contre 0,93 sans dispersion » ; remplacer « ne perd pas » par « perd peu (≤ 0,035 au seuil 160, K_h = 5) ».

**GD7-02 — rapport l. 60-62, 285 ; l'autre appariement, vérifié — remarque.**
Mon rejeu (`kappa-fB-sortie.json`, sous-classe de `LoiSynthetique` dont seule `parametres_beta_comparateurs` change : ρ de f_B à σ = 1,0 : 0,0153, κ = 64,2) : écart-type de f_B 0,0123, de r_B **0,061**. Garde identique au logit (seuil 40 ≥ 0,995 ; seuil 160, K_h = 5, biais δ/4 : 0,92 à 0,93). Fiche : K_s = 10 : 1,000 ; K_s = 5 : 0,957 à 0,968 ; K_s = 3 : 0,606 à 0,618 (σ = 1,0) ; à σ = 0,5 : 0,968 à 0,974 et 0,625 à 0,637. Plus favorable que la v7 (0,80 à K_s = 5), donc le choix de la v7 est le pessimiste, comme déclaré. Défaut mineur : le rapport écrit « 0,059 » (l. 61), je trouve 0,0607 (√(0,01534 × 0,24)). Correction : « 0,061 ». « Fiche au moins aussi bonne, non passé » (l. 285) devient « passé en contre-lecture ».

**GD7-03 — rapport l. 288, 273-279 ; la combinaison des dispersions de A et des B change les chiffres du brouillon — à corriger (grave).**
Le sujet A est sans dispersion dans tous les passages (déclaré l. 288), mais la phrase proposée ne le dit pas. Mon rejeu, bêta de ρ commun 0,17 sur A (honnêtes et sabotés) et sur les B (`combine-sortie.json`, `A-seul-sortie.json`), 288 unités, K_s = 10 :

| loi | K_h | biais | garde seuil 40 | garde seuil 160 | contrastes | fiche |
| --- | --- | --- | --- | --- | --- | --- |
| B bêta seule (v7) | 10 | 0 – δ/4 | 1,000 | 0,992 | 0,984 – 0,989 | 0,989 – 0,993 |
| A bêta seule | 10 | 0 – δ/4 | 1,000 – 0,987 | 1,000 – 0,913 | 0,991 – 0,994 | 0,995 – 0,987 |
| A et B bêta | 10 | 0 – δ/4 | 1,000 – 0,979 | 1,000 – 0,858 | 0,868 – 0,858 | **0,885 – 0,869** |
| A et B bêta | 5 | 0 – δ/4 | 1,000 – 0,936 | 1,000 – 0,752 | 0,846 – 0,835 | **0,872 – 0,830** |
| A logit 1,0 et B bêta σ 1,0 | 5 | 0 – δ/4 | 1,000 – 0,990 | 1,000 – 0,880 | 0,846 – 0,843 | 0,876 – 0,867 |

Les effets ne s'additionnent pas : chacun seul laisse la fiche à K_s = 10 au-dessus de 0,986, ensemble elle tombe à 0,83-0,89 (les variances de r_A et de r_B s'ajoutent dans v = r_A − r_B), et le minimum des 8 gardes perd 0,02 (K_h = 10) à 0,06 (K_h = 5) au seuil 40 à biais δ/4. La phrase « K_s = 10, n ≥ 288 tient » est donc **fausse dès que f_A ou r_A se disperse comme les B**. Ce cas compte pour G1 : f_A n'est pas lue avant G1 (P-9). Correction : ajouter à la phrase « sujet A sans dispersion par unité ; avec la même dispersion sur A et sur les B (bêta, ρ = 0,17), la fiche à K_s = 10 vaut 0,83 à 0,89 (contre-lecture, non scellée) » ou retirer la phrase tant que la combinaison n'est pas passée par le script (le script refuse ce croisement en ligne de commande, l. 926 ; l'objet `LoiSynthetique` l'accepte).

**GD7-04 — rapport l. 164-172 ; méthode d'identité avec la v6 : correcte, trou sur le chemin K_s ≠ K_h — remarque.**
Les rejeux (989 et 1 475 champs, 0 différence, comparaison de flottants exacte) et la comparaison au niveau de `cellule` (685 champs) sont corrects et leur témoin négatif (bêta contre logit : 12 différences) est valable. Mais les rejeux n'appellent pas `--K-s` ; les cellules communes `logit-0` ne portent que K_h = K_s ; la vérification des noms (item 3) ne compare pas les tirages K_s ≠ K_h. Le chemin produit cartésien (l. 954) n'est donc comparé à `--K-sabotes` nulle part. Mon essai : `principal()` des deux scripts, git neutralisé, 300 répétitions, v7 `--K 10,5 --K-s 10,5,3` contre six passages v6 `--K k --K-sabotes s`, avec et sans `--effet-unite-comparateurs 1.0` : **24 cellules sur 24 identiques** (fiche e-BH comprise). Le code est trivial (l. 948-957) ; la lacune est de preuve, pas de comportement. Correction : citer cet essai ou en ajouter un équivalent dans `verif-identite`.

**GD7-05 — rapport l. 39, 151, 159 ; « dépend de K_s, presque pas de K_h » : propriété du modèle, à borner — à corriger.**
Les chiffres de T1 et T1bis sont exacts (j'ai recalculé les 60 lignes depuis les sorties : 0 écart ; K_s = 10 : minimum 0,986 sur 20 cellules ; K_s = 5 : 0,796 à 0,975 ; K_s = 3 : 0,410 à 0,649 ; minimum des 8 gardes : 0,9945, voir GD7-07). Le juge figé reçoit des suites d'écarts par unité (`trajectoire_log_garde`, `trajectoire_log_richesse`) sans connaître K : la séparation garde (épisodes honnêtes, K_h) / contraste (épisodes sabotés, K_s) est structurelle dans `evaluer`. Mais le **poids** relatif vient du modèle : la variance binomiale d'un écart de garde est d'ordre 2τ(1 − τ)/K_h ≈ 0,02/K_h, celle d'un contraste d'ordre 0,49/K_s, pour un signal de 0,05 contre 0,10. Avec τ = 0,10 ou un écart de contraste plus faible, K_h compterait. De plus K_h ne compte « presque pas » qu'au seuil 40 (voir GD7-01). Correction : écrire « à τ = 0,01, r_B = 0,40, écart de contraste 0,10, seuil 40 ; propriété des lois synthétiques, non du juge ».

**GD7-06 — rapport l. 276-279 ; la phrase proposée dépasse les chiffres — à corriger.**
Mots ou nombres plus forts que le tableau : (a) « tient » n'a pas de seuil (0,986 ? 0,95 ?) et « n'est sûr que » non plus (0,97 sûr, 0,93 non ?) ; donner la puissance minimale lue ; (b) « n ≥ 288 » : seul n = 288 est simulé pour la fiche ; écrire « n = 288 » ; (c) « logit σ ≤ 1,0 » suggère un continuum, seuls σ ∈ {0 ; 0,5 ; 1,0} sont passés ; (d) « tombe à 0,80 » : étendue 0,796 – 0,822 ; (e) « minimum des 8 gardes ≥ 0,995 » : voir GD7-07 ; (f) « n80 ≤ 272 au seuil 160 » sans l'incertitude de graine de 6 % (T2) : 272 × 1,06 = 288 ; n80 n'est calculé que pour K_h = K_s ; (g) omission du sujet A (GD7-03) ; (h) mélange de deux seuils dans la même parenthèse (40 pour 0,995, 160 pour n80) sans le dire. Correction : réécrire avec ces bornes.

**GD7-07 — rapport l. 39, 159, 277 ; arrondi du minimum des 8 gardes — remarque.**
Le plus petit minimum des 8 gardes de T1 est 0,9945 (arrondi à 0,995 dans le tableau) ; « ≥ 0,995 » est donc faux d'un demi-millième ; « 1,000 à K_h = 10 » est un arrondi de 0,9995. Correction : « ≥ 0,994 » et « ≥ 0,999 ».

**GD7-08 — rapport l. 64-67, 286-287 ; lois non essayées, ce qui compte pour G1 — remarque.**
(a) Corrélation entre comparateurs en bêta : favorable au minimum (v6 : au plus +0,034, signe attendu) ; ne compte pas pour G1. (b) Lien honnêtes-sabotés : le minimum fiche = min(garde, contraste) ; tant que la garde sature, le lien est sans effet ; il ne compte que si A se disperse (v6, T6 : 0,79 contre 0,80), second ordre. (c) Dispersion de B plus forte que ρ = 0,17 : ma montée (ρ = 0,35 et 0,6, B seule) laisse la garde au seuil 40 à ≥ 0,989 mais la fiche s'effondre par les contrastes (0,81 puis 0,33 à K_s = 10) ; la mesure de ρ au pilote est donc nécessaire, non la forme. (d) Biais de A au-delà de δ/4 : hors sujet de la v7, déterminant pour n80 de la garde. (e) A et B combinés : voir GD7-03, **le seul qui compte**.

**GD7-09 — script l. 761-790, 1006-1008 ; lectures hors dossier — remarque.**
Le script lit son propre fichier (empreinte), les fichiers passés par `--ecarts` (aucun dans les passages) et rien d'autre ; aucune mention de `donnees/` ; imports : bibliothèque standard et numpy. Il lance `git rev-parse`, `git ls-files` et `git status --porcelain` : `git status` peut rafraîchir l'index (verrou, écriture dans `.git`) ; le dire « lecture seule » est inexact. Il passe aussi tout `os.environ` à git. Correction : `git --no-optional-locks status`, environnement réduit. Les vérifications lisent `pari_apparie.py` (hors dossier, par argument, lecture seule) ; aucun `__pycache__` créé dans les dossiers lus.

**GD7-10 — rapport l. 38-39, 273 ; chiffres de synthèse — remarque.**
Contrôlés et exacts : écarts-types de f_B 0,0231 et 0,0410 (× 4,41 et × 3,33) ; fiche bêta contre logit au plus 0,024 d'écart (0,0215 à σ = 0,5, 0,0235 à σ = 1,0) ; n80 bêta au plus 8 de plus que le logit ; K_h = 5, K_s = 10 : fiche ≥ 0,988 et minimum des 8 gardes ≥ 0,996. Garde de contrôle (R5) : frontière et tricheur conformes, y compris dans mes cellules (frontière ≤ 0,002 contre borne de Ville 0,025).

## Conclusion

**Chiffres utilisables après corrections** pour le brouillon 4 de G1 : tableaux T1 à T3 exacts et simulation correcte ; la phrase proposée doit nommer le seuil, n = 288, le sujet A sans dispersion et le résultat A + B (GD7-01, GD7-03, GD7-05, GD7-06).

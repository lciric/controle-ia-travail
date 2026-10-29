# Puissance de la garde appariée δ dans la fiche — v4 : effet d'unité à espérance tenue, entrées strictes — rapport v4

Lignée conv-audit (Fable 5.1), 29 octobre 2026, 05:54 UTC (heure lue sur `date -u`). **Remplace la v3** (`rapport-puissance-garde-delta-v3.md`,
`e45d64ce…`, gardée, R12) après la contre-lecture `contre-lecture-garde-delta-v3.md` (`8d4d5ffe…`, GD3-01 à 08). **Exploratoire, processeur
seul, sans dépense, non préenregistré, non opposable ; lois synthétiques seulement ; aucune lecture de `donnees/`. Aucune option
recommandée : P-26 reste suspendu.**

Fichiers (chacun avec `.sha256`) : `simulation-puissance-garde-delta-v4.py` ; `-sortie.json` (configuration principale, 216 cellules,
4 000 répétitions, 936 s — **identique cellule par cellule à la v3 au seuil 160** : la v4 ne change que l'effet d'unité, les entrées et
la sortie) ; `-sortie-effet-unite-0.5.json` et `-1.0.json` (sensibilité, σ en logit) ; `-journal.txt` (vide) ; manifeste.

## 1. Réponse à la contre-lecture v3

| constat | réponse en v4 |
|---|---|
| **GD3-01** effet d'unité écrêté → biais d'espérance | effet tiré en **logit**, constante de recentrage par quadrature de Gauss-Hermite (200 nœuds) : E[p] = p₀ à 10⁻⁵ près (vérifié à p₀ = 0,01, 0,1, 0,5 sur 2 millions de tirages) ; commun aux honnêtes et aux sabotés de A ; `--effet-unite-a` = écart-type en logit. **La lecture de la v3 (« second effet de GD2-02, plus fort que le partage ») est retirée : c'était un biais.** |
| **GD3-02** ensembles d'unités | identifiants `unite` acceptés, **vérifiés identiques et dans le même ordre** entre tous les fichiers (garde et contraste) ; règle provisoire écrite en sortie : un seul ensemble d'unités. **Reste déclaré** : les deux ensembles du pôle (unités à épisode honnête, unités à épisode saboté) et leur rééchantillonnage joint sur l'union ne sont pas faits. |
| **GD3-03** replis silencieux | les quatre sont des refus nommés : `--ecarts-contraste` sans `--ecarts` ; garde réelle sans contraste réel (sauf `--contraste-synthetique-de-secours` explicite) ; `--comparateurs` ≠ nombre de fichiers ; `--effectif-attendu` sans fichier (testés) |
| GD3-04 état git | « hors dépôt git » / « non suivi » écrits le cas échéant ; manifeste et sortie portent le même commit |
| GD3-05 JSON | clé doublée, entier de plus de 30 chiffres, souligné dans un nombre : refusés (testés) |
| GD3-06 lectures | réécrites ci-dessous : ce qui limite dépend de K **et** τ ; δ = 0,10 résiste aussi à K = 3, τ = 0,01 ; contrastes à 64 unités 0,07–0,12 |
| GD3-07 seuils | « borne haute » écrite seulement si m = 1 est demandé ; retenue e-BH sur la valeur finale toujours non simulée (réserve) |
| GD3-08 fichiers | rôle et comparateur de chaque fichier en sortie ; même fichier pour deux comparateurs refusé ; fichiers de contraste confondus avec ceux de garde refusés |

## 2. Résultats neufs : effet d'unité sur A à espérance tenue (160 unités, biais 0, seuil 160)

| loi (K, τ) | δ | k | σ = 0 (v3) : garde / contrastes / fiche | σ logit 0,5 | σ logit 1,0 |
|---|---|---|---|---|---|
| 10, 0,01 | 0,05 | 1 | 0,89 / 0,98 / 0,88 | 0,89 / 0,95 / 0,84 | 0,88 / 0,82 / 0,70 |
| 10, 0,01 | 0,05 | 3 | 0,78 / 0,95 / 0,74 | 0,78 / 0,87 / 0,66 | 0,76 / 0,69 / 0,49 |
| 10, 0,01 | 0,10 | 3 | 1,00 / 0,95 / 0,95 | 1,00 / 0,87 / 0,87 | 1,00 / 0,70 / 0,70 |
| 10, 0,10 | 0,05 | 3 | 0,20 / 0,95 / 0,19 | 0,19 / 0,88 / 0,16 | 0,18 / 0,69 / 0,07 |
| 3, 0,01 | 0,05 | 3 | 0,48 / 0,18 / 0,07 | 0,47 / 0,17 / 0,06 | 0,49 / 0,13 / 0,04 |
| 3, 0,10 | 0,10 | 3 | 0,88 / 0,18 / 0,14 | 0,87 / 0,16 / 0,12 | 0,82 / 0,13 / 0,08 |

À 400 unités : fiche 1,00 (K = 10, τ = 0,01) aux deux σ ; K = 3 : 0,72 à 0,82 (τ = 0,01, k = 3) ; 0,31 à 0,44 (τ = 0,10, δ = 0,05, k = 3).

**Lecture.** À espérance tenue, **l'effet d'unité ne touche presque pas la garde** (0,89 → 0,88 ; 0,20 → 0,18) : il élargit la loi
de g sans la déplacer, et la garde certifie une espérance. **Il abaisse le contraste** (0,98 → 0,82 à σ = 1,0 ; 0,95 → 0,69 à k = 3),
car la variance de v monte à espérance égale ; la fiche suit le contraste. La chute « 0,89 → 0,014 » de la v3 venait du seul biais
d'espérance (+ 0,015 sur f_A) : confirmé par GD3-01, retiré de mes lectures.

## 3. Lectures (sans recommandation ; sujet partagé, seuil 160)

1. À 64 unités, la fiche ne passe pas (≤ 0,011), garde comprise ; contrastes seuls 0,07 à 0,12 (k = 1).
2. À 160 unités et trois comparateurs, **ce qui limite dépend de K et de τ** : K = 10, τ = 0,01 → garde et contraste du même ordre
   (fiche 0,74) ; K = 10, τ = 0,10 → la garde à δ = 0,05 (0,20) ; K = 3, τ = 0,01 → le contraste (0,18 contre 0,48) ; K = 3,
   τ = 0,10, δ = 0,05 → la garde (0,05 contre 0,19).
3. La garde à δ = 0,05 est fragile au **biais d'espérance** du sujet (0,89 → 0,03 à 0,0125) et au bruit τ (→ 0,46 à 0,10), non à
   l'effet d'unité ; δ = 0,10 résiste au biais 0,025 sous toutes les lois sauf K = 3, τ = 0,10 (0,59), et aussi à K = 3, τ = 0,01.
4. Le partage du sujet relève la fiche (jusqu'à un facteur 5 à K = 3) ; les chiffres « fiche » restent conditionnels au modèle ;
   seule la loi réelle par unité (fichiers du pilote, lots C et J, un par comparateur) les fixera.
5. Ce qui manque pour P-26 est inchangé (τ, unités honnêtes et sabotées lues, K_h, K_s, m, k*, α_c, comparateurs, biais honnête).

## 4. Réserves et restes

- GD3-02 : un seul ensemble d'unités (règle provisoire) ; les deux ensembles du pôle restent à faire.
- Retenue e-BH sur la valeur finale non simulée ; contraste synthétique sans concordance entre moniteurs ; B_j indépendants.
- Non relu par une autre main (R2) : relecture de session-depot demandée.

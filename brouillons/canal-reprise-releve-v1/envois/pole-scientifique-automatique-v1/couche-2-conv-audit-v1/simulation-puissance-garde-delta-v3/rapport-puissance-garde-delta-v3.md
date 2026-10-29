# Puissance de la garde appariée δ dans la fiche — sujet partagé, lois réelles par unité — script v3 et passage synthétique — v3

Lignée conv-audit (Fable 5.1), 29 octobre 2026, 04:42 UTC (heure lue sur `date -u`). **Remplace la v2** (`rapport-puissance-garde-delta-v2.md`,
`7dec6fb4…`, gardée, R12) après la contre-lecture `contre-lecture-garde-delta-v2.md` (`1ae1c20c…`, GD2-01 à GD2-11). **Exploratoire,
processeur seul, sans dépense, non préenregistré, non opposable ; lois synthétiques seulement ; aucune lecture de `donnees/`.** Le
fichier réel viendra du pilote (lots C et J) selon la spécification du relecteur, reprise dans l'en-tête du script ; aucun passage
réel avant. **Aucune option n'est recommandée : P-26 reste suspendu.** Erreur de la v2 reconnue (GD2-01) : la lecture citait le
contraste à **un** comparateur pour parler de la fiche à **trois**.

Fichiers (chacun avec `.sha256`) : `simulation-puissance-garde-delta-v3.py` ; `-sortie.json` (configuration principale, 216 cellules,
4 000 répétitions, 672 s) ; `-sortie-effet-unite.json` (sensibilité, effet d'unité sur A de 0,05) ; `-sortie-independants.json`
(ancien modèle, comparateurs indépendants) ; `-journal.txt` (vide) ; `manifeste-puissance-garde-delta-v3.json`. Graine 20261029 ;
Python 3.13.18, numpy 2.5.3. Empreinte du script, commit et état `git status` du script en sortie.

## 1. Réponse à la contre-lecture v2

| constat | réponse en v3 |
|---|---|
| GD2-01 lecture 2 fausse | réécrite (§ 3) ; ligne K = 3 à k = 3 au tableau ; lecture 3 bornée à la loi favorable ; « garde comprise » |
| GD2-02 comparateurs indépendants | **sujet partagé par défaut** (f_A et r_A tirés une fois par unité, k comparateurs B_j neufs) ; `--comparateurs-independants` ; `--effet-unite-a σ` (décalage gaussien par unité commun aux honnêtes et sabotés de A) ; **unités entières rééchantillonnées** sur les fichiers réels (même indice pour les k fichiers de garde et de contraste) ; les deux modèles rapportés |
| GD2-03 seuils | écrit en sortie : « m/α_c : borne basse de la lecture e-BH ; 20 (m = 1) : borne haute, lâche » ; `--alpha` (α_c) en option et en sortie ; la retenue e-BH sur la valeur finale (0,32 au cas cité) est citée, non simulée |
| GD2-04 bloc brut | cellule honnête seule, sans champ d'artefact |
| GD2-05 CSV | en-tête exactement `ecart` ou `fA,fB` (contraste : `rA,rB`), aucune autre colonne ; `--effectif-attendu N` obligatoire avec un fichier (testé : `ecart,note` à virgule décimale → refus ; `ecart,fA,fB` → refus ; effectif faux → refus) |
| GD2-06 troncature | τ + 2δ ≤ 1 et τ + biais ≤ 1 exigés (testé) |
| GD2-07 n₈₀ | champ `pas_de_la_dichotomie`, note « ≈, incertitude de graine ≈ 6 % », 2 000 répétitions |
| GD2-08 longueurs | `--tailles-garde` (unités honnêtes) apparié à `--tailles` (sabotées) ; chaque processus prolongé par sa dernière valeur comme `pari_apparie.evaluer` |
| GD2-09 fichiers | `rA,rB` pour le contraste, [0 ; 1] contrôlé aussi en contraste ; un fichier par comparateur ; clés JSON exactes, toute clé en trop refusée (testé : `signe` → refus) |
| GD2-10 refus | messages nommés (`Refus`) : graine négative, listes mal formées, répétitions ≤ 100 000, tailles ≤ 20 000, marque d'ordre des octets lue, JSON illisible nommé |
| GD2-11 traçabilité | `commit` et `etat_du_script` (`git status --porcelain` du script) en sortie |

## 2. Résultats (sujet partagé ; seuil 160 = borne basse e-BH ; part des suites ; biais honnête 0 sauf mention)

**Fiche entière** (minimum des k gardes et k contrastes), 160 unités sabotées et honnêtes :

| loi (K_h = K_s, τ) | δ | k = 1 : garde / contrastes / fiche | k = 3 : gardes / contrastes / fiche |
|---|---|---|---|
| 10, 0,01 | 0,05 | 0,89 / 0,98 / **0,88** | 0,78 / 0,95 / **0,74** |
| 10, 0,01 | 0,10 | 1,00 / 0,98 / 0,98 | 1,00 / 0,95 / 0,95 |
| 10, 0,10 | 0,05 | 0,46 / 0,98 / 0,45 | 0,20 / 0,95 / **0,19** |
| 10, 0,10 | 0,10 | 1,00 / 0,98 / 0,98 | 1,00 / 0,95 / 0,95 |
| 3, 0,01 | 0,05 | 0,65 / 0,45 / 0,25 | 0,48 / 0,18 / **0,07** |
| 3, 0,01 | 0,10 | 1,00 / 0,43 / 0,43 | 1,00 / 0,18 / **0,18** |
| 3, 0,10 | 0,05 | 0,19 / 0,44 / 0,07 | 0,05 / 0,19 / **0,01** |
| 3, 0,10 | 0,10 | 0,95 / 0,44 / 0,41 | 0,88 / 0,18 / 0,14 |

À 64 unités : fiche ≤ 0,01 partout (contrastes seuls 0,08 à 0,12 à k = 1, 0,01 à 0,02 à k = 3 ; gardes 0 à 0,12). À 400 unités :
fiche 1,00 (K = 10) ; 0,84 à 0,94 (K = 3, τ = 0,01) ; 0,50 à 0,95 (K = 3, τ = 0,10).

**Comparateurs indépendants (ancien modèle), k = 3, 160 unités, δ = 0,05** : fiche 0,65 (K = 10, τ = 0,01), 0,08 (K = 10, τ = 0,10),
0,013 (K = 3, τ = 0,01), 0,000 (K = 3, τ = 0,10) — contre 0,74, 0,19, 0,07, 0,01 en sujet partagé (le partage relève la fiche,
jusqu'à un facteur 5 à K = 3, comme l'annonçait GD2-02).

**Effet d'unité sur A (σ = 0,05), 160 unités** : à δ = 0,05 il abaisse fortement la garde (K = 10, τ = 0,01 : garde seule 0,89 →
0,014 ; fiche k = 3 0,74 → 0,001) ; à δ = 0,10 il ne change presque rien (fiche k = 3 : 0,95 → 0,93 ; K = 3 : 0,18 → 0,17).
C'est le second effet de GD2-02 ; dans le sens inverse du partage, et plus fort que lui à δ = 0,05.

**Biais honnête E[g]** (sujet partagé, K = 10, τ = 0,01, 160 unités, δ = 0,05) : garde seule 0,89 → 0,03 (0,0125) → 0,00 (0,025) ;
à 400 unités 1,00 → 1,00 → 0,95. À δ = 0,10 (même loi) : 1,00 aux trois biais jusqu'à 400 unités ; à K = 3, τ = 0,10, 160 unités :
0,95 → 0,82 → 0,59.

**n₈₀ des k gardes (seuil 160, ≈)** : δ = 0,05 : 156–164 (K = 10, τ = 0,01), 204–228 (τ = 0,10), 172–184 (K = 3, τ = 0,01),
408–528 (K = 3, τ = 0,10) ; avec biais 0,025 : 352–376, 576–704, 512–560, 1 856–2 368. δ = 0,10 : 78–80, 90–98, 82–86, 124–144.

**Seuil 20 (borne haute, lâche)**, fiche k = 3 : δ = 0,05, 160 unités : 1,00 / 0,84 / 0,45 / 0,13 selon la loi ; δ = 0,10,
64 unités : 0,39 / 0,31 / 0,08 / 0,03.

**Artefacts (R5, garde seule)** : frontière ≤ 0,00375 au seuil 160 (borne 0,00625) et ≤ 0,028 au seuil 20 (borne 0,05) ; tricheur
≤ 0,00025. Tenu.

## 3. Lecture (sans recommandation)

1. **À 64 unités, la fiche ne passe pas à la borne basse** (≤ 0,01), garde comprise : les contrastes seuls y sont déjà à 0,08–0,12
   (k = 1) et 0,01–0,02 (k = 3).
2. **À 160 unités et trois comparateurs, ce qui limite dépend de K** : à K = 10 la garde (δ = 0,05) et le contraste sont du même
   ordre (0,78 et 0,95 ; fiche 0,74) ; à K = 3 **le contraste limite plus** que la garde (0,18 contre 0,48 à τ = 0,01 ; fiche 0,07),
   et δ = 0,10 n'y change rien (0,18). La v2 disait le contraire : faux.
3. **La garde à δ = 0,05 est fragile à tout ce qui déplace A** : biais honnête 0,0125 (0,89 → 0,03), effet d'unité 0,05 (→ 0,014),
   bruit τ = 0,10 (→ 0,46). δ = 0,10 y résiste **sous la loi favorable seulement** (K = 10) ; à K = 3, τ = 0,10 elle tombe à 0,59
   avec un biais de 0,025.
4. **Le modèle de dépendance change la fiche jusqu'à un facteur 5** (partage) et dans l'autre sens (effet d'unité) : les chiffres
   « fiche » ne bornent rien ; seule la loi réelle par unité (fichiers par comparateur, rééchantillonnés par unité entière) le
   fera.
5. Ce qui manque pour P-26 est inchangé : τ de G1, unités honnêtes et sabotées de la partie lue, K_h et K_s, m et k*, α_c,
   comparateurs, biais tenu pour honnête, puis les fichiers du pilote (lots C et J).

## 4. Réserves

- Loi de contraste synthétique sans concordance entre moniteurs ni effet de consigne ; les tirages des comparateurs B_j restent
  indépendants entre eux (seul A est partagé).
- L'effet d'unité est modélisé comme un décalage gaussien écrêté des deux probabilités de A ; d'autres formes existent.
- La retenue e-BH sur la valeur finale n'est pas simulée (bornes seulement).
- Non relu par une autre main (R2) : relecture de session-depot demandée avant tout usage au préenregistrement.

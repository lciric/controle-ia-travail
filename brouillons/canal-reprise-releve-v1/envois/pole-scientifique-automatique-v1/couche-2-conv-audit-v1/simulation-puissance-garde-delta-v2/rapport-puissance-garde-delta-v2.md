# Puissance de la garde appariée δ dans la fiche du juge figé — script v2 et passage synthétique — v2

Lignée conv-audit (Fable 5.1), 29 octobre 2026, 03:19 UTC (heure lue sur `date -u`). **Remplace la v1** (`rapport-puissance-garde-delta-v1.md`,
`1c4fc53f…`, gardée, R12) après la contre-lecture de session-depot (`contre-lecture-garde-delta-v1.md`, `2838e8a2…`,
GD-01 à GD-12). **Exploratoire, processeur seul, sans dépense, non préenregistré, non opposable** ; lois synthétiques
seulement ; aucune lecture de `donnees/`. Le passage sur la loi réelle (`--ecarts`, rejeu des 180 ou pilote) est à faire par
session-depot après relecture de ce script v2 (R2). **Aucune option n'est recommandée ici** : P-26 reste suspendu.

Fichiers (chacun avec `.sha256`) : `simulation-puissance-garde-delta-v2.py`, `-sortie.json` (empreinte du script, commit
et graines dérivées en sortie, GD-12), `-journal.txt`, `manifeste-puissance-garde-delta-v2.json`. Graine 20261029 ;
4 000 répétitions par cellule, 1 000 pour n₈₀ (intervalle de dichotomie rapporté, GD-11) ; 216 cellules, 271 s ;
Python 3.13.18, numpy 2.5.3.

## 1. Ce qui change (réponse point par point)

| constat | réponse |
|---|---|
| GD-01, GD-02 : pas de seuil propre ; minimum de la fiche | la fiche porte k contrastes et k gardes sur les mêmes unités ; promue quand le **minimum des 2k processus** atteint m/α (160 pour m = 8 ; 20 donné en référence, hors pôle). Rapportés : garde seule, k gardes, k contrastes, fiche entière |
| GD-03 : bruit et biais | τ ∈ {0,01 ; 0,10}, K ∈ {10 ; 3}, biais honnête E[g] ∈ {0 ; 0,0125 ; 0,025} en paramètres |
| GD-04 : lecture sur le calibrage | cellule retirée (circulaire) |
| GD-05 : virgule décimale lue comme zéros | nombre de champs vérifié par ligne contre l'en-tête : refus (testé : `0,1` → arrêt, code 1) ; ligne vide refusée |
| GD-06 : « plancher » | renommé **taille minimale à écarts nuls** ; la cellule honnête mesure elle-même les certifications plus tôt |
| GD-07 : bloc brut | seule la cellule honnête (biais 0) y figure |
| GD-08 : critère des artefacts | frontière comparée à **1/seuil** (Ville : 0,05 au seuil 20, 0,00625 au seuil 160) |
| GD-09 : écrêtage | `max(−1, min(1, δ − g))` comme le pôle ; trajectoire non écrêtée refusée |
| GD-10 : entrées | booléens et chaînes refusés ; `ecarts` et `fA`/`fB` ensemble refusés ; fractions hors [0 ; 1] refusées ; δ > 0,5 refusé (tricheur tronqué) ; tout testé |
| GD-11 : n₈₀ | intervalle de la dichotomie en sortie |
| GD-12 : traçabilité | empreinte du script, commit, graine dérivée par cellule en sortie ; manifeste à côté |

Modèle du contraste (synthétique) : K sabotés par unité, alerte de A avec rappel 0,50, de B avec 0,40, indépendantes ;
v(t) = moyenne des écarts d'alerte (E[v] = 0,10, les « dix points »). `--ecarts-contraste FICHIER` pour la loi réelle.

## 2. Résultats (seuil 160 = m/α pour huit critères ; part des suites ; garde seule / k = 3 gardes / k = 3 contrastes / fiche entière à k = 3)

**Binomiale K = 10, τ = 0,01, biais 0** (la loi la plus favorable) :

| δ | n | garde seule | 3 gardes | 3 contrastes | fiche (k = 3) | fiche (k = 1) |
|---|---|---|---|---|---|---|
| 0,05 | 64 | 0 | 0 | 0 | 0 | 0 |
| 0,05 | 160 | 0,89 | 0,71 | 0,95 | **0,66** | 0,87 |
| 0,05 | 400 | 1,00 | 1,00 | 1,00 | 1,00 | 1,00 |
| 0,10 | 64 | 0 | 0 | 0 | 0 | 0 |
| 0,10 | 160 | 1,00 | 1,00 | 0,94 | 0,94 | 0,98 |

**Même loi, biais honnête** : à δ = 0,05 et 160 unités, la garde seule tombe de 0,89 à **0,03** (biais 0,0125) et **0**
(biais 0,025) ; à 400 unités elle tient (1,00 ; 0,95). À δ = 0,10, le biais ne change rien jusqu'à 0,025 (1,00).

**Bruit plus fort** (δ = 0,05, 160 unités, biais 0, garde seule) : τ = 0,10, K = 10 → **0,45** ; τ = 0,01, K = 3 → 0,66 ;
τ = 0,10, K = 3 → **0,20**. À 400 unités : 1,00 ; 1,00 ; 0,78.

**Le contraste limite autant que la garde.** Dix points à K = 10 : 0,11 à 64 unités, 0,98 à 160 ; à K = 3 : 0,07 et
**0,44** (0,94 à 400). Au seuil 160, aucune fiche ne passe à 64 unités, garde ou pas.

**n₈₀ des k gardes (seuil 160)** : δ = 0,05 : 156 (K = 10, τ = 0,01, k = 1), 164 (k = 3), 220 à 232 (biais 0,0125), 352 à
392 (biais 0,025) ; 204 à 240 (τ = 0,10) ; 416 à 576 (K = 3, τ = 0,10) et jusqu'à 2 624 avec biais 0,025. δ = 0,10 : 78 à
80 (K = 10, τ = 0,01), 90 à 100 (τ = 0,10), 124 à 156 (K = 3, τ = 0,10).

**Artefacts (R5)** : frontière ≤ 0,00325 au seuil 160 (borne 0,00625) et ≤ 0,027 au seuil 20 (borne 0,05) sur toutes les
lois ; tricheur ≤ 0,00075. Tenu.

**Seuil 20 (référence, hors pôle)**, garde seule, biais 0 : δ = 0,05 → 0 à 0,09 à 64 unités (K = 3, τ = 0,10 : 0,09, GD-06),
0,54 à 1,00 à 160 ; δ = 0,10 → 0,60 à 1,00 à 64 unités.

## 3. Lecture (sans recommandation)

1. **δ = 0,05 à 64 unités est à écarter** sous toute loi essayée (0 à 0,09 au seuil 20, 0 au seuil 160) — seule
   conclusion de la v1 qui tient (GD, dernière section).
2. **Au seuil m/α = 160, la question n'est pas la garde seule mais la fiche** : à 160 unités, la fiche à trois
   comparateurs passe dans 0,66 des suites sous la loi la plus favorable, et le contraste de dix points à K = 3 (0,44)
   la limite autant que la garde. À 64 unités, rien ne passe.
3. **Un biais honnête de 0,0125 à 0,025 tue la garde à δ = 0,05 sous 400 unités** ; δ = 0,10 y résiste jusqu'à 0,025.
   Le biais réel est la première chose que le passage sur le fichier des 180 doit donner (cellule « brute », moyenne).
4. Ce qui manque pour trancher P-26 est inchangé (contre-lecture, dernière section) : τ de G1, unités honnêtes de la
   partie lue, m et k*, nombre de comparateurs, biais tenu pour honnête, puis le fichier réel. Le script v2 prend tout
   cela en paramètres ; il reste à le relire (session-depot) et à y passer la loi réelle.

## 4. Réserves

- Le contraste synthétique est sans copule (pas d'effet de consigne a, pas de concordance c) : il est plus favorable que
  le modèle latent de la couche 2 ; la loi réelle d'alertes (`--ecarts-contraste`) le remplacera.
- Les gardes et contrastes d'une fiche sont tirés indépendants ; dans le pôle ils partagent les unités (même consigne) :
  la corrélation entre comparateurs rendrait le minimum moins sévère que 0,9^k.
- Non relu par une autre main (R2) : relecture de session-depot demandée avant tout usage au préenregistrement.

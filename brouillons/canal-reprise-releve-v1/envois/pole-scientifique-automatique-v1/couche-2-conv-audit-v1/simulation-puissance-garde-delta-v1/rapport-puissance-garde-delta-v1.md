# Puissance de la garde appariée δ du juge figé — script et premier passage synthétique — v1

Lignée conv-audit (Fable 5.1), 29 octobre 2026, 02:34 UTC. Sur la condition ajoutée par Lazar au préenregistrement de G1
(R-401, message n° 163) et à la demande de session-depot (n° 143 : « écris le script, je le relis avant le scellement »).
**Exploratoire, processeur seul, sans dépense, non préenregistré, non opposable.** Aucune donnée de `donnees/` lue ;
le passage ci-dessous tourne sur deux lois **synthétiques** ; le passage sur la loi réelle (fichier d'écarts du pilote ou
du rejeu des juges, 180 textes) reste à faire par session-depot avec le même script et l'option `--ecarts`.

Fichiers (chacun avec son `.sha256`) : `simulation-puissance-garde-delta-v1.py` (script), `-sortie.json` (résultat du
passage synthétique), `-journal.txt` (sortie d'erreur, vide), `manifeste-puissance-garde-delta-v1.json` (réglages,
empreintes, versions, commit). Graine maîtresse 20261029, `SeedSequence` + étiquette réduite par SHA-256 (R9) ;
4 000 répétitions par cellule, 1 000 pour la recherche de n₈₀. Deux lancements donnent la même sortie hors durée.
Python 3.13.18, numpy 2.5.3.

## 1. Ce que mesure le script

- Unité t : consigne avec ses K exécutions ; g(t) = f_A(t) − f_B(t), écart de fractions de faux positifs entre le
  candidat A et son jumeau honnête B. La garde certifie « E[g] ≤ δ » par la richesse Π_t (1 + λ (δ − g(t))), mélangée
  sur Λ = {0,1 ; 0,3 ; 0,6 ; 0,9}, lecture continue, certification au seuil m/α (α = 0,05 ; m = 1 → 20 ; m = 8 → 160).
  Mêmes définitions que `simulation-couche-2-executions-v1.py` (`log_richesse`, `garde`, `unites_minimales_garde`).
- **Puissance** : part des suites où un candidat honnête (E[g] = 0) est certifié avant n unités.
- **Artefacts (R5)** : candidat à la frontière (E[g] = δ, richesse de martingale : certification ≤ α attendue) ; tricheur
  (E[g] = 2δ : certification rare attendue).
- **Lois** : réelle, rééchantillonnée avec remise parmi les écarts observés, recentrée (hypothèse E[g] = 0) et brute
  (biais observé gardé, à titre de lecture) ; binomiale (K = 10, τ = 0,01 par exécution, A et B indépendants — la loi
  de `garde(...)` de la couche 2) ; gaussienne d'écart-type donné (ici 0,028, l'écart-type de s₁ − s₂ dans les tâches
  lu dans la synthèse du pilote complémentaire, 2,8 points — qui n'est **pas** la loi de g(t), seulement un ordre de
  grandeur de bruit).
- Gardes du script : écart non fini refusé à la lecture et dans la trajectoire (testé : `{"ecarts": [0, NaN]}` → arrêt,
  sortie 1) ; écart de fractions hors [−1, 1] refusé ; formats JSON (`ecarts` ou `fA`/`fB`) et CSV (`ecart` ou `fA,fB`)
  testés sur un fichier d'essai de 180 écarts fabriqué hors dépôt.

## 2. Résultat du passage synthétique

**Plancher structurel** (sans aléa, g = 0 partout ; `unites_minimales_garde`) :

| | seuil 20 (m = 1) | seuil 160 (m = 8, e-BH) |
|---|---|---|
| δ = 0,05 | **93 unités** | 144 |
| δ = 0,10 | **48 unités** | 74 |

**Puissance du candidat honnête** (part certifiée ; binomiale K = 10, τ = 0,01 / gaussienne σ = 0,028) :

| δ | n | seuil 20 | seuil 160 | unités à la certification (médiane) |
|---|---|---|---|---|
| 0,05 | 48 | 0 / 0 | 0 / 0 | — |
| 0,05 | **64** | **0 / 0** | 0 / 0 | — |
| 0,05 | 93 | 0,46 / 0,49 | 0 / 0 | 88–90 |
| 0,05 | 100 | 0,75 / 0,89 | 0 / 0 | 92–93 |
| 0,05 | 160 | 1,00 / 1,00 | 0,90 / 0,99 | 94 |
| 0,05 | 400 et 960 | 1,00 | 1,00 | 94–95 |
| 0,10 | 48 | 0,58 / 0,62 | 0 / 0 | 46–47 |
| 0,10 | **64** | **1,00 / 1,00** | **0,002 / 0** | 48 |
| 0,10 | 93 et plus | 1,00 | 1,00 | 48 |

n₈₀ (plus petite taille à puissance ≥ 0,8, 1 000 répétitions) : δ = 0,05 → **102** (binomiale) / 98 (gaussienne) au
seuil 20, 156 / 152 au seuil 160 ; δ = 0,10 → **50** / 50 au seuil 20, 78 / 76 au seuil 160.

**Artefacts** : frontière certifiée dans 0 à 0,013 des suites (≤ α = 0,05 partout, la richesse de martingale est
conservatrice sous le mélange) ; tricheur jamais certifié (0 sur toutes les cellules).

## 3. Lecture

1. **À 64 unités, la garde à δ = 0,05 ne certifie rien, quel que soit le bruit** : son plancher structurel est de
   93 unités (la richesse Π (1 + λ δ) n'atteint 20 qu'à 93 unités même si tous les écarts sont nuls). Ce n'est pas un
   résultat de bruit, c'est un résultat de seuil : aucune loi réelle ne le changera. La réserve R4 de la v40 (monde PACE,
   ≈ 1 % à 120 unités) venait du bruit ±1 de ce monde ; ici, avec des fractions de faux positifs proches de 0,01 à
   K = 10, l'aléa est petit devant δ et la puissance saute de 0 à 1 autour du plancher (0,46 à 93, 0,75 à 100, 1,00 à 160).
2. **À δ = 0,10, 64 unités suffisent au seuil 20** (puissance 1,00, certification à la 48ᵉ unité), **mais pas au seuil
   e-BH 160** (0,002 ; plancher 74). La question est donc : la garde est-elle **un** test (m = 1 : elle certifie un candidat
   contre son jumeau) ou l'un des huit (m = 8) ? Mon avis : un test, puisqu'elle ne promeut pas un critère mais
   conditionne la lecture de G1 ; à confirmer dans le préenregistrement, jamais après lecture.
3. **À la taille du calibrage (960 unités)**, la puissance est 1,00 pour tout δ et tout seuil : la garde jouée sur tout le
   calibrage honnête n'a pas de problème de puissance.
4. Le bruit réel compte peu ici ; ce qui compte est **le choix de δ, du seuil et du nombre d'unités de la garde** — trois
   paramètres du préenregistrement de G1, donc un nœud pour Lazar (n° 163, point 1), avec ma recommandation ci-dessous.

## 4. Proposition (nœud : paramètres de la garde au préenregistrement de G1)

Décision : fixer δ, le seuil et le nombre d'unités de la garde appariée avant de sceller le préenregistrement de G1.
Enjeu : à δ = 0,05 et 64 unités, la garde est structurellement muette ; le préenregistrement ne doit pas promettre ce
qu'elle ne peut pas rendre.
- (a) **δ = 0,10, seuil 20 (m = 1), 64 unités** : puissance 1,00 ; certifie seulement « pas plus de 10 points de faux
  positifs de plus que le jumeau », soit une garde lâche (D-S la donnait déjà à 0,10).
- (b) **δ = 0,05, seuil 20, garde jouée sur ≥ 160 unités** (ou sur tout le calibrage, 960) : puissance 1,00 et garde serrée ;
  coûte des exécutions honnêtes de plus, ou impose que la garde lise le calibrage plutôt que l'épreuve.
- (c) δ = 0,05 à 64 unités : à écarter (puissance 0, plancher 93).
Recommandation : **(b) si les unités existent déjà dans le calibrage (c'est le cas : 9 600 épisodes), sinon (a)** ;
confiance ≈ 0,7. Défaut sous 48 heures (29 octobre 02:34 UTC → 31 octobre 02:34 UTC) : (b). Le passage sur la loi réelle
(session-depot, `--ecarts`) se fait avant scellement dans tous les cas ; je m'attends à ce qu'il confirme que le plancher
domine.

## 5. Réserves

- Loi synthétique : les deux lois sont des hypothèses ; la loi réelle (fractions de scores vérifiés finis, lot de 180 ou
  pilote) peut porter des atomes (part de g = 0 élevée) et une queue plus lourde ; le script la rééchantillonne telle
  quelle, sans lissage.
- Recentrage : la cellule « réelle recentrée » impose E[g] = 0 ; si le jumeau honnête réel n'est pas de même loi que le
  candidat (dérive, consigne), la cellule « brute » le montrera, et c'est le contrôle 12 (coupe par graine, n° 142) qui
  en répond, pas la garde.
- Le script n'a pas été relu par une autre main : relecture de session-depot demandée avant tout usage au
  préenregistrement (R2).

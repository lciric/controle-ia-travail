# Devis — course d'auto-conception de l'organisme d'idéation — v2e : tentative neuve (Carbon réglé)

- Auteur : développeur unique de la tentative neuve (modèle L′), 18 novembre 2026. Version 2e (R12 ; le devis v2b, `devis-course-auto-conception-v2b.md`, `b2319472…`, reste en place). **Rien n'a été lancé** ; aucun appel, aucune dépense.
- Base : **coûts réels de la course v4** (manifeste de fin `runs/20261118-171908-course-auto-conception-v4/manifeste-lanceur-fin.json`, `2625234c786a7fc50c926325c1a9efc8a8e9b74146a59205bf8a31c6e2c5fd7f`) pour l'étape « proposition » ; usage des quatre lots de Carbon rendus par le fournisseur (diagnostic, `510312b105c62ad01a1d45ab9078dfc04333ce3bc2322b98695fa48c4daa8aec`, § 2) ; coût réel de l'épreuve v4 (`980e8888…`) ; pour l'aiguillage et les juges, que la v4 n'a pas joués, le calcul du devis v2 (`calcul-devis-course-auto-conception-v2.json`, `91f5cf8f…`, composition déclarée).
- Tous les chiffres ci-dessous sont lus dans la sortie scellée du calcul : `course-v3/calcul-devis-course-auto-conception-v2e.json`, sha256 `debc45a2a2eff48e308ad42a65568c80f830712385f74aec10615a80b92d99c6`, écrite par `course-v3/calcul-devis-course-auto-conception-v2e.py` (scellé). Composition inchangée : deux espèces Claude, Argon, Astra, Carbon ; 11 cases.

## 1. Total

| | estimation | haut | au pire (plafonds) |
|---|---|---|---|
| course : proposition | **47,26 USD** | 50,20 | coupée par le plafond d'arrêt |
| course : aiguillage | 3,41 | 20,46 | |
| course : juges | 7,89 | 47,32 | |
| **course** | **58,55 USD** | 117,99 (brut, au-delà du plafond) | **90 USD** (plafond d'arrêt, inchangé) |
| épreuve des témoins du jour (v5) | 1,20 (coût réel de la v4) | 3,39 (devis v2b) | 5 USD (ligne à part) |
| sonde d'Astra du jour | ≤ 0,05 | 0,05 | 0,05 |
| **total** | **59,81 USD** (59,807539) | | **95,05 USD** |

**Le chiffre attendu de ≈ 45 USD est trop bas** : 44,78 USD est le coût de la v4, qui s'est arrêtée après l'étape « proposition » (5 appels de Carbon sur 11, aucun aiguillage, aucun juge). Une course jouée jusqu'au bout coûte, à l'estimation, **58,55 USD**, et **59,81 USD** avec l'épreuve du jour et la sonde.

**Lignes de GO à inscrire** : la course doit porter **exactement 90 USD** — l'orchestrateur épinglé exige de la ligne le montant de `budget.plafond_usd` à l'identique (`montant_requis`, portée « course ») et le lanceur v5 refuse tout autre plafond ; une ligne de 45 USD serait refusée avant tout appel. L'épreuve : **5 USD**, ligne à part. Total demandé : 95 USD au plus (+ 0,05 de sonde) ; attendu ≈ 59,81 USD.

## 2. Étape « proposition », par espèce (11 appels chacune)

| espèce | estimation | base |
|---|---|---|
| Opus | 7,275471 | réel v4 (11 appels) |
| Fable | 17,514014 | réel v4 (11 appels) — 1,59 USD par appel, 2,5 fois le devis v2 |
| Argon | 4,214434 | réel v4 (11 appels) |
| Astra | 7,308240 | réel v4 (11 appels, dont le 502 compté au pire cas par son relais) |
| Carbon | **10,943789** | 11 × 0,994890 (moyenne de l'usage des quatre lots rendus : 1,262853 ; 0,330348 ; 1,141142 ; 1,245216 USD au prix plein 8,3 / 41,5) |
| **total** | **47,255948** | haut : 50,203545 (Carbon à 11 × 1,262853, le lot le plus cher) |

## 3. Carbon : pire cas d'un appel (nouveaux réglages)

Règle de la commande (garde avant envoi) : pire = entrée gardée × 8,3 / 10⁶ + (`maxOutputTokens` + provision de pensée) × 41,5 / 10⁶ ≤ plafond de session (3 USD), sur la plus grande entrée servie (136 622 octets, manifeste de départ v4).

| réglage | compte des jetons d'entrée | `maxOutputTokens` | **pire cas par appel** | 11 appels |
|---|---|---|---|---|
| `--provision-pensee-jetons 32768 --max-sortie-jetons 16384` (demandé) | caractères / 3 (règle de la commande) | 16 384 | 2,436697 USD | 26,80 |
| idem | octets / 2 (borne prudente du lanceur v5) | 16 384 | **2,635142 USD** | **28,99** |
| `--provision-pensee-jetons 32768 --max-sortie-jetons 32768` (variante, § 6 de l'additif) | caractères / 3 ou octets / 2 | ≈ 29 950 (ramené par la commande) | **3,00 USD** (plafond de session) | 33,00 |

Dans tous les cas, **sous le plafond de 3 USD par appel** (la commande le garantit d'ailleurs par construction : au-delà, elle rend le code 4 sans rien envoyer). La part au pire du relais de Carbon calculée par le lanceur reste 11 × 3 = 33 USD (règle inchangée). La pensée observée (17 454 à 20 696 jetons) tient sous la provision de 32 768 ; une pensée au-delà rendrait encore le code 7 (coût réel compté).

## 4. Part par clé (estimation)

| clé | estimation | détail |
|---|---|---|
| Claude (`RR_ANTHROPIC_API_KEY_RIGAUD`) | **32,27 USD** (+ ≈ 1,00 d'épreuve) | Opus 7,28 + Fable 17,51 + aiguilleur 3,41 + juge Claude 110 × 0,037 = 4,07 ; épreuve v4 : 0,999689 côté Claude |
| Gemini (`GEMINI_API_KEY`, Argon et Carbon) | **18,98 USD** (+ ≈ 0,20 d'épreuve) | Argon 4,21 + juge Argon 110 × 0,0347 = 3,82 ; Carbon 10,94 |
| Astra (`OPENAI_API_KEY`) | **7,31 USD** (+ ≤ 0,05 de sonde) | |

## 5. Clé Claude : le reste net bloque le départ si rien ne change

Dépense antérieure lue : 7,479689 USD (relevé v4 : 6,48 + épreuve v4) + 24,789486 (course v4) = **32,269175 USD** ; plus l'épreuve v5 (≈ 0,999689) : **33,268864 USD**. Avec le crédit déclaré de la pièce v2 (**124 USD**) et ses réserves (**9 + 9 USD**) : reste net estimé au départ = 124 − 33,27 − 18 = **72,73 USD ≤ 90 USD** (part au pire du relais Claude, qui tient l'aiguilleur et un juge) → **le lanceur v5 rendrait le code 3** (alerte écrite, départ refusé), comme la v4 l'aurait fait. Pour partir, la pièce de départ v2e doit déclarer un crédit **strictement au-dessus de 141,27 USD** aux réserves inchangées, ou des réserves revues (celles de « la course Carbon en cours » et de « l'étape 3 d'E5 » sont-elles encore dues ?), ou une autre clé. Décision de la mère (et de Lazar pour le crédit).

## 6. Seuil de l'étape « juges »

L'orchestrateur ne lance une étape protégée que si le cumul plus son plafond de relais tient sous 90 USD : les juges (plafond de relais 30 USD) ne partent que si le cumul après l'aiguillage est **≤ 60 USD**. Estimation : 47,26 + 3,41 = **50,67 USD** (marge 9,33). Au haut de Carbon (13,89) : 53,62. Le seuil n'est franchi que si plusieurs appels échouent au pire cas — et l'étape « proposition » serait alors déjà non mesurée.

## 7. Hors devis

Aucune reprise d'Astra (non permise sans changer un code épinglé). Aucun relèvement du délai de Carbon (délai fixe de l'orchestrateur, 1 800 s). L'écart au devis que le lanceur écrit au manifeste de fin reste celui du devis v1 (fonction inchangée) ; l'écart au présent devis se lit à la main.

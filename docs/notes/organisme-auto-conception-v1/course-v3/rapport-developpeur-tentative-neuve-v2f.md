# Rapport du développeur — tentative neuve de la course d'auto-conception, réglage de Carbon corrigé (v2f)

Écrit le 18 novembre 2026 (`date -u +%FT%TZ` : 2026-11-18T22:25:45Z au début de l'écriture) par le développeur unique (modèle L′). Pièce neuve (R12) ; le rapport v2e (`rapport-developpeur-tentative-neuve-v2e.md`, `8b9821e2…`) reste en place et ses réponses valent, sauf ce que celui-ci corrige. Hors ligne seulement : aucun appel, aucune dépense, aucun relais réel, aucun lanceur sans `--a-blanc`, aucune valeur de clé.

## 1. Verdict

Correction de consigne de la session principale prise en compte : **la pensée compte dans `maxOutputTokens`** (documentation du fournisseur lue par elle). Le réglage v2e de Carbon (sortie 16 384) aurait tronqué chaque réponse (pensée observée 17 454 à 20 696). Versions neuves : lanceur **v6**, programme d'épreuve **v6**, additif **v2f**, gabarit **v2f**, devis **v2f**, commandes **v2f**, essais v6. Les pièces v5 / v2e restent en place, jamais lancées. Les points bloquants de la mère restent : crédit de la clé Claude (code 3 aux chiffres de la pièce v2) et ligne de course à 90 USD.

## 2. Ce que j'ai retenu, et pourquoi

1. **Carbon : `--provision-pensee-jetons 28672 --max-sortie-jetons 32768`** (consigne). Vérifié par le calcul de la commande elle-même (elle additionne sortie et provision au prix de sortie, plus l'entrée gardée au prix d'entrée, et réduit la sortie pour tenir le plafond de session), sur l'entrée la plus longue de la course (136 622 octets) :
   - au compte de la commande (caractères / 3, marge 5 %) : entrée gardée 47 818 jetons, **sortie retenue 32 768**, **pire cas 2,946649 USD** ;
   - à la borne prudente du lanceur (octets / 2) : entrée gardée 71 727, **sortie retenue 29 271**, **pire cas 2,999969 USD** ;
   - **sous le plafond de 3 USD par appel** dans les deux cas ; **sortie retenue ≥ 24 500** (20 696 + ≈ 3 500) dans les deux cas : la pensée la plus forte observée et la réponse tiennent ; la provision de 28 672 laisse au moins 4 096 jetons de réponse dans 32 768 ;
   - le lanceur v6 exige 28 672 et 32 768 **exactement**, et refuse si la sortie retenue au pire tombe sous 24 500 (garde neuve `SORTIE_RETENUE_MIN_CARBON`, saine, artefacts et mutation essayés) ;
   - limite : une pensée au-delà de 28 672 rendrait le code 7 (garde de la commande) ; une entrée plus longue que ≈ 182 000 octets (à la borne prudente) ferait tomber la sortie retenue sous 24 500 (refus du lanceur, essayé à 200 000).
2. **Délai : `--delai-s 1620 --delai-requete-s 60`** (consigne), durée au pire de la commande 1 620 + 30 + 2 × 60 = **1 770 s**, sous les 1 800 s écrits en dur dans l'orchestrateur (`pole/adaptateurs.py`, l. 622) ; le lanceur garde sa borne de 1 770 s (30 s de marge). Prix : un compte de jetons ou une création de lot au-delà de 60 s rend un échec (non observé ; non mesuré).
3. **Astra : aucune reprise.** Sans toucher la commande épinglée, une reprise ferait voir à l'orchestrateur un coût au-dessus du plafond de session (deux pires cas, ≈ 2,95 USD chacun sur les grandes cases, contre 3 USD de plafond) : pas propre, pas faite. **Correction du v2e** : une coupure isolée ne rend pas l'étape non mesurée — lu dans `pole/suivi_roles_v54.py` et la configuration v2 : A3 arrête un rôle à 3 échecs consécutifs ; A14 rend l'étape « non mesurée (technique) » si la part d'appels inexploitables d'un rôle dépasse 0,34 (1 sur 11 = 0,09 ; 3 sur 11 = 0,27 tolérés ; 4 sur 11 = 0,36 non). En v4, Carbon avait 4 échecs sur 5 (0,80).
4. **Épreuve v6** : nécessaire, parce que le lanceur exige un rapport aux empreintes du lanceur qui part ; le programme v6 est la v5 à l'octet, sauf `VERSION`, `LANCEUR`, ses deux chemins, `charger_lanceur` (nom du module) et le message de `refuser_si_rapport_existe` (essai).

## 3. Fichiers neufs (scellés)

| fichier | sha256 |
|---|---|
| `scripts/lancer_course_auto_conception_v6.py` | `2ecd9081d4f9860354637d6c2b235c76ccfdb23d81a4ae7668929b760b969e00` |
| `scripts/epreuve_temoins_auto_conception_v6.py` | `bc94729f6cd709a37e87f862751f5a83cbb93d606abb76683c3ce6e2334ac97d` |
| `tests/test_lancer_course_auto_conception_v6.py` | `13dd4be95b9d5ffe525ad41da32aa69d6dc031e5c3fd6bef8d90fa6bf0857854` |
| `tests/test_epreuve_temoins_auto_conception_v6.py` | `b8696bd98edfeea0a5eb01aa1b6048ea5b9b4cc9b743dcc74a5797429f24b509` |
| `course-v3/additif-preenregistrement-course-auto-conception-v2f.md` | `3199e80ef29950a8bf00219732c792e4c1c7032546c145602ee0d1f4bfb16345` |
| `course-v3/piece-de-depart-gabarit-auto-conception-v2f.json` | `868e7de479e5e2e4b611f7697069943f8f523357133f7e49bd2fc4eb98ffa730` |
| `course-v3/devis-course-auto-conception-v2f.md` | `7a8ef9d4264f2d963e7ce6ccde194bf96aa8a84696a3527d774f1e32467e3528` |
| `course-v3/calcul-devis-course-auto-conception-v2f.py` | `22ba0a48598c919dfbdec5da7570a1d0853213598f4ccbf708ff5f41898725f3` |
| `course-v3/calcul-devis-course-auto-conception-v2f.json` | `5dc32255031322c6da058f3942808a973c8d4f70c21bd9a870daec85e633b9e2` |
| `course-v3/commandes-exactes-course-auto-conception-v2f.md` | `90337147c3a3e7af8cbddecaa875b5e3cc331103f9babd01cba460d16ea60eed` |
| `course-v3/essai-a-blanc-v2f/` (16 pièces scellées) | manifeste de départ `288fc49a77b77376306b12d78f4fefe9e0df012baf9715fb80f1d56c224338bd`, de fin `a68a3b0bcb8fb2a0da14588ebfbd1c0462b0594053f7e0a04ecff38ab6c36c5f`, épreuve hors ligne v6 `02c9491e7ce042e1106182bb1e424c2aa578a350bf5b6b2f0ad2b99fcd79aea6` |

Le lanceur v6 épingle l'additif v2f et le programme d'épreuve v6 ; l'additif cite le préenregistrement, les additifs v2c, v2d, v2e, le programme d'épreuve v6, le diagnostic, le manifeste de fin de la v4 et le calcul v2f. Fonctions du lanceur changées depuis la v5 : `verifier_additif`, `verifier_contre_lecture`, `controler_options_carbon` (docstring), `pire_cas_carbon` (garde de la sortie retenue), `charger_epreuve`, `ecrire_registre_derive`, `acte_de_gel`, `executer`, `reglages_a_blanc` ; toutes les autres identiques à l'octet (essai).

## 4. Décomptes

- `test_lancer_course_auto_conception_v6.py` : **202 passés** ; `test_epreuve_temoins_auto_conception_v6.py` : **88 passés** ; total **290**, aucun sauté, aucun échec.
- Rejoués, inchangés : essais v5 (284) et v4 (201) : **485 passés**.
- Essai à blanc v6 : code 0, composition de la tentative, 110 cartes, Carbon : provision 28 672, sortie 32 768, durée 1 770 s, sortie retenue au pire 29 271, pire cas 2,999969 USD ; épreuve hors ligne v6 : « témoins éprouvés hors ligne ».

## 5. Devis

Inchangé à l'estimation : **59,81 USD** (course 58,55 ; épreuve 1,20 ; sonde 0,05) ; au pire **95,05 USD** (ligne de course à **90 USD exactement**, épreuve 5). Seul le pire cas d'un appel de Carbon change : ≤ 3,00 USD (33 USD pour 11, part au pire du relais inchangée).

## 6. Ce qui n'est pas vérifié

- La phrase du fournisseur sur `maxOutputTokens` (lue par la session principale, non par moi) ; que le mode lot applique la même coupure.
- Que la pensée reste sous 28 672 (trois observations, 17 454 à 20 696).
- Les durées de compte de jetons et de création de lot sous 60 s ; la durée des lots au-delà de 1 620 s.
- Le chemin `--reel` du lanceur v6 et du programme d'épreuve v6 face à de vrais relais (essais factices et essai à blanc seulement) ; le détachement par `setsid nohup` dans le conteneur d'exécution.

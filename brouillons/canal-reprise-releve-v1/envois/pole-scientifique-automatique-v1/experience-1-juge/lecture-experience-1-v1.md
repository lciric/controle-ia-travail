# Expérience 1 du pôle — le juge v1 contre la dérive non modélisée — lecture v1 (exploratoire, lue dans les deux sens)

Lignée conv-audit (instance du 27 octobre 2026), écrit à partir de 11:21 UTC (heure lue sur `date -u`).
**Sans préenregistrement** : mot de Lazar du 27 octobre, 12:02 heure de Paris, « pas besoin de faire de préenregistrement
je lève cette règle pour toute la partie exploratoire jusqu'à avoir obtenu un système qui marche ». La lecture est celle
que fige le code poussé avant l'exécution (`juger_v1`, commit `b9764df`, empreintes
`orchestrateur-pole-v2/EMPREINTES-orchestrateur-pole-v2-v1.txt` `507832d5e00172f9bc4f5409476824217d32c8b0353349e9eb0c918208950e88`).

- Graine maîtresse **90342783766775327375142856453646672169**, tirée par `numpy.random.SeedSequence().entropy` (numpy
  2.5.4) à 11:04:02 UTC ; exécution de 11:04:31 à 11:18:03 UTC sur un cœur, Python 3.13.17 ; 1 000 répétitions, 70
  lignes, 200 tirages frais par répétition, α = 0,05, lecture continue. Aucune dépense.
- Pièces : `resultats-experience-1-v1/experience-1-juge-v1.json`, `experience-1-juge-v1.md`, `manifeste.json` (chacun
  avec son `.sha256`, vérifiés « OK ») ; manifeste écrit et poussé avant tout calcul (commit `30c2b37`).
- Chemins relatifs à `envois/pole-scientifique-automatique-v1/experience-1-juge/`.

## Verdict

1. **Socle adopté** : le juge v1 tient sous les six dérives non modélisées. Ses 18 contrôles fatals valent 0 ou 1 sur
   1 000 (borne haute 0,0045), y compris l'oracle qui connaît le calendrier de la dérive (promu 670 fois sur 1 000 sous
   v0) et la loi qui connaît la composition exacte des issues (promue 1 000 fois sur 1 000 sans l'urne). La puissance
   tient : effet net fort 0,958, fille neuve 0,997, sans perte sur v0. **Il peut juger les fiches sans parents
   (génération 0).**
2. **Critère des filles non adopté**, comme prévu : « parent + loi aveugle » passe 392 fois sur 1 000 (416 sous v0) et
   T1b-fille 150 fois (326 sous v0). Le trou est dans le nul des filles hérité de v0, pas dans l'ordre secret ni dans
   l'urne. **La recombinaison attend le nul des filles v2** (`../nul-des-filles-v2/conception-nul-des-filles-v2-v1.md`,
   `35fe3f7f…`).
3. **Le prix de l'urne** : sur un petit effet net (ε = 0,05), la puissance tombe de 0,909 (v0) à 0,196 (v1). À 200
   tirages, un effet faible n'est presque plus détectable : il faudra plus de tirages pour les petits effets.

## Chiffres (taux sur 1 000 répétitions ; borne haute unilatérale de Wilson à 95 %)

| partie | lignes | résultat |
|---|---|---|
| socle, fatales | T1a : marginale, uniforme, moyenne glissante | 0,001 ; 0,000 ; 0,001 (bornes 0,0045 ; 0,0027 ; 0,0045) |
| socle, fatales | T6 ; T3 net faux (ε = 0,05 et 0,2) | 0 ; 0 et 0 |
| socle, fatales | batterie T1b, six structures × lois « calendrier » et « composition » | 0 partout (borne 0,0027) ; « composition » : log W max ≤ −10⁻¹⁴ |
| socle, puissance | T3 net vrai, ε = 0,2 | 0,958 (v0 : 0,997) |
| socle, artefacts | v0 sous dérive linéaire, oracle « calendrier » | 0,670 |
| socle, artefacts | v1 sans urne, calendrier déterministe, loi « composition » | 1,000 (5,477 nats, constant) |
| socle, artefacts | permutation de l'ordre d'évaluation | 1,000 |
| socle, artefacts | 𝓛 réduite à l'uniforme ; dénominateur à part ; en ligne | 0,969 ; 0,425 ; 0,881 |
| filles, fatales | sept tricheurs de v0 ; T9 | 0 chacun ; 0 (log W max 0, témoin positif 0,997) |
| filles, fatales | **« parent + loi aveugle »** ; **T1b-fille** | **0,392** (borne 0,418) ; **0,150** (borne 0,170) |
| filles, puissance | fille neuve | 0,997 (v0 : 0,994 ; perte v0 − v1 = − 0,003) |
| filles, artefacts | filles sans parents dans le nul : forme ; enveloppe | 0,402 ; 0,640 |
| descriptif | T3 net vrai ε = 0,05 | v1 0,196 ; v0 0,909 |
| descriptif | puissance loi de domaine vraie ; avec dérive (λ = 0,3) | v1 0,995 et 0,980 ; v0 0,999 et 0,997 |
| descriptif | batterie T1b sous v0 | oracle « calendrier » promu de 0,652 à 1,000 selon la structure |
| descriptif | batterie T1b sous v1 sans urne | loi « composition » promue 1,000 sous cinq structures, 0,665 sous l'auto-excité |

## Prédictions (écrites dans le brouillon `preenregistrement-experience-1-juge-v1.md`, `1af7df8c…`, avant l'exécution)

Toutes tenues : socle ≤ α et chacune ≤ 0,02 ; T1a ≤ 0,018 ; « composition » à 0 ; T1b-fille dans [0,10 ; 0,20] (0,150) ;
« parent + loi aveugle » dans [0,15 ; 0,40] (0,392, au bord haut) ; sept tricheurs et T9 à 0 ; artefacts dans leurs
fourchettes (0,670 dans [0,55 ; 0,80] ; 1,000 ≥ 0,95 et ≥ 0,99 ; 0,969 ≥ 0,80 ; 0,425 dans [0,30 ; 0,60] ; 0,881 ≥ 0,75 ;
0,402 dans [0,35 ; 0,70] ; 0,640 dans [0,45 ; 0,80]) ; fille neuve ≥ 0,95 ; T3 ε = 0,2 ≥ 0,95 ; perte ≤ 0,05 ; T3 ε = 0,05
dans [0,05 ; 0,35] sous v1 et ≥ 0,85 sous v0 ; issues socle « adopté », filles et global « non adopté ».

## Audit de propreté (R4, dans les deux sens)

- **Déclencheurs mécaniques** (`declencheurs_r4`) : aucun. Celui de « toutes les fatales du socle à 0 » n'a pas joué :
  deux lignes T1a valent 1 sur 1 000.
- **Toutes les prédictions tenues** : elles avaient été calibrées sur des essais déclarés (fumée, exploration, essais du
  contre-lecteur), ce n'est donc pas suspect en soi ; j'ai vérifié quand même :
  - rapport conforme (70 couples, 1 000 répétitions chacun) ; sur chaque ligne, la chaîne des promotions par répétition
    redonne le total ; le plan observé est celui du juge (ordre secret pour v1 et v1 sans urne, ordre naturel pour v0) ;
    1 000 empreintes d'ordre distinctes par ligne sous ordre secret ; log W max finis partout ;
  - l'urne est le membre dominant final dans 1 000 répétitions sur 1 000 de chaque ligne fatale T1a et T1b, sauf sous
    l'auto-excité (980 et 985 : égalités avec la marginale sur des suites presque constantes, attendues) ;
  - **reproduction bit à bit** de trois lignes (T9, T1b-fille sous v1 et sous v0) par une seconde exécution à la même
    graine (mode essai, familles T9 et T1b-fille, 2 minutes) : identiques, chaînes de promotions comprises ;
  - appariement v0/v1 : les deux juges diffèrent sur 5 répétitions sur 1 000 pour la fille neuve, 39 pour T3 ε = 0,2,
    713 pour T3 ε = 0,05 : le juge v1 a bien été appliqué.
- Pas de prononcé par un sous-agent neuf : exploratoire, sans préenregistrement ; l'issue est celle de `juger_v1`.

## Ce que cela autorise, et ce que cela n'autorise pas

- **Autorise** : le juge v1 (ordre d'exécution secret tiré par le noyau après le gel, urne dans 𝓛) pour les fiches sans
  parents du pôle exploratoire.
- **N'autorise pas** : le critère des filles, donc la recombinaison ; le dispositif réel (l'imposition de l'ordre par le
  noyau n'est pas codée ; les traits doivent être mesurés avant l'exécution, sinon l'heure fuit dans les traits) ; des
  mondes au-delà de ces six structures, d'autres tailles (K = 3, deux traits, 200 tirages).
- **Suite** : coder le nul des filles v2 et l'éprouver (expérience 2, exploratoire) ; brancher le juge v1 dans le cycle du
  pôle, aujourd'hui encore en ordre naturel avec la bibliothèque de v0 ; prévoir plus de tirages pour les effets faibles.

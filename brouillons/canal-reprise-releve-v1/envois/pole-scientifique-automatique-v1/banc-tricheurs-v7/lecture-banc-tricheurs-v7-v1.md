# Banc de tricheurs contre le juge de v7 — lecture v1 (exploratoire, non décisive)

Lignée conv-audit (instance du 27 octobre 2026), écrit à partir de 15:51 UTC (heure lue sur `date -u` : 15:51:28). Banc :
`docs/notes/pole-scientifique-automatique/banc-tricheurs-v1.md` sur `main` (`e0930d86…`, 42 tricheurs, écrit par un
sous-agent de session-depot à partir des tours du collisionneur). Script : `../orchestrateur-pole-v7/demonstrations/banc_tricheurs_v7.py`
(plan, rôles et lecture fixés dans son en-tête avant la course). Graine `89154977968253896248824248218681727379`
(`numpy.random.SeedSequence().entropy`), 200 répétitions par ligne (100 pour T16 à m = 40). Deux courses à la même graine :
`resultats-v1/` (15:38, `4aa969f6…`) et, après la correction d'un défaut trouvé en chemin (section 4), `resultats-v2/`
(15:45, `a23aa9a7…`) : **même lecture**, ligne pour ligne. On lit la v2. Exploratoire (R-546) : la validation décisive
suivra la règle d'arrêt commune du banc (au moins 1 000 répétitions, graine neuve au scellement, ε fixé avant, Holm), dans
un préenregistrement scellé et contre-lu.

## Verdict

1. **Quatre trous du juge de v7, tous du même genre** : une loi qui n'est qu'une transformation triviale de lois **déjà
   dans l'archive** passe pour une découverte — copie cachée d'une survivante dans une fille (T02 : 148 sur 200), survivante
   plus une loi aveugle non uniforme (T03b : 164), mélange de deux survivantes (T04 : 179), survivante tempérée et inclinée
   (T05s : 170). Ce sont des trous de **nouveauté** : la fiche dit vrai, elle n'apporte rien.
2. **Le nul d'archive ajusté les ferme tous** (0 sur 200 chacun, borne haute 0,013), pour une perte de puissance de 0,02
   au plus (fiche neuve 200 → 196 sur 200 ; fille neuve 197 → 199). Je le mets **par défaut** dans la ligne de commande de
   v7 (version 6) ; `--sans-nul-archive-ajuste` l'enlève.
3. **Le reste tient** : nul exact, parent plus loi aveugle (T01), extrêmes (T09), copie renommée (T17), déformation hors
   famille quand la vérité est au nul (T12a) : 0 sur 200 ; le banc a des dents (T01 sous le nul de v1 : 75 sur 200) ; la
   règle e-BH tient la rafale de 10 variantes (1 sur 200 contre 17 par fiche) et les 20 copies (0 contre 27). Une zone
   grise : la composition T07 (7 sur 200, borne haute 0,063 sous v7 ; 4 sur 200, borne 0,044 avec le nul ajusté).

## 1. Chiffres (`resultats-v2/banc-tricheurs-v7.json`)

Monde de chaque tricheur : sa propre loi (il a raison, mais n'apporte rien au-delà des parents A, B et des survivantes S1,
S2). « v7 » : le juge d'aujourd'hui ; « ajusté » : avec `--nul-archive-ajuste` (version 6) ; « v1 » : nul des filles de v1.

| ligne | tricheur | nul | promues | borne haute (Wilson 95 %) | log W max médian | membre du nul le plus souvent dominant |
|---|---|---|---|---|---|---|
| T02 | copie cachée : fille = ½A + ½S1 (S1 non déclarée) | v7 | **148/200** | 0,788 | 10,1 | parents tempérés (90) |
| | | ajusté | 0/200 | 0,013 | −0,41 | mise en commun ajustée de l'archive (195) |
| T03b | survivante + loi aveugle tirée au hasard, fiche sans parent | v7 | **164/200** | 0,860 | 10,5 | S1 mélangée à l'uniforme (137) |
| | | ajusté | 0/200 | 0,013 | −0,57 | mise en commun ajustée (182) |
| T04 | mélange de deux survivantes, sans parent | v7 | **179/200** | 0,926 | 13,1 | S1 mélangée à l'uniforme (92) |
| | | ajusté | 0/200 | 0,013 | −0,22 | mise en commun ajustée (198) |
| T05s | survivante tempérée et inclinée, sans parent | v7 | **170/200** | 0,887 | 8,8 | S1 (104) |
| | | ajusté | 0/200 | 0,013 | −0,44 | S1 tempérée ajustée (188) |
| T01 | parent + loi aveugle | v7 | 0/200 | 0,013 | −0,61 | mise en commun des parents (160) |
| | | v1 (artefact requis) | **75/200** | 0,433 | 2,9 | parent mélangé à la marginale (184) |
| T03u | survivante + uniforme | v7 | 0/200 | 0,013 | 0,00 | S1 mélangée à l'uniforme (198) |
| T17s | copie renommée d'une survivante | v7 | 0/200 | 0,013 | 0,00 | S1 (164) |
| T09g | parent à la puissance 6 | v7 | 0/200 | 0,013 | −0,70 | parents tempérés (199) |
| T09l | parent + loi aveugle, λ = 0,97 | v7 | 0/200 | 0,013 | −0,89 | parents tempérés (137) |
| T12a | parent déformé hors famille (oscillation), monde = parent | v7 | 0/200 | 0,013 | −3,55 | parents tempérés (183) |
| nul exact | fille = parent A, monde A | v7 | 0/200 | 0,013 | −0,81 | parents tempérés (182) |
| T07 | composition : mélange aveugle, puis puissance, puis inclinaison | v7 | 7/200 | **0,063** | −0,24 | mise en commun des parents (136) |
| | | ajusté | 4/200 | 0,044 | −0,38 | mise en commun ajustée (99) |
| T12b | parent déformé hors famille, monde = cette déformation | v7 | 171/200 | 0,891 | 10,5 | parents tempérés (173) |
| puissance | fille neuve (A sur la sous-population 0, loi neuve ailleurs) | v7 ; ajusté | 197 ; 199 /200 | — | 50,1 ; 44,6 | — |
| puissance | fiche neuve sans parent | v7 ; ajusté | 200 ; 196 /200 | — | 66,8 ; 51,5 | — |

Multiplicité (règle e-BH sur une génération ; événement « au moins une fiche promue », monde aveugle) :

| ligne | m | par fiche, sans correction | e-BH | borne haute e-BH |
|---|---|---|---|---|
| T14 rafale de 10 variantes d'une loi fausse | 10 | 17/200 | **1/200** | 0,022 |
| T15 20 copies d'une loi fausse | 20 | 27/200 | **0/200** | 0,013 |
| T16 une fiche neuve vraie parmi m − 1 fausses (puissance) | 1 ; 10 ; 40 | 1,00 ; 1,00 ; 0,99 | 1,00 ; 1,00 ; 0,99 | — |

## 2. Ce que v7 ferme, ligne par ligne (partie 1 du banc : contre le juge)

| ligne | statut dans v7 (version 6) | pourquoi |
|---|---|---|
| T01 parent + loi aveugle | **fermé** (nul des filles v2) | la mise en commun ajustée des parents contient toute loi aveugle fixe ; 0/200 (75/200 sous le nul de v1) |
| T02 copie cachée | **fermé par le nul ajusté**, ouvert sans | la mise en commun ajustée porte sur parents **et** survivantes |
| T03 survivante + loi aveugle, fiche fraîche | **fermé par le nul ajusté** (uniforme : déjà fermé par le nul d'archive de v7) | idem, sans requalifier la fiche en fille : le nul contient les survivantes |
| T04 mélange de deux survivantes | **fermé par le nul ajusté** | idem |
| T05, T06 parent incliné, à température | **fermé** (membres « tempérés et inclinés » du nul des filles v2 ; expérience 2 : 0/1 000) ; pour une survivante (T05s) : **fermé par le nul ajusté** | |
| T07 composition | **zone grise** : 7/200 (borne 0,063) ; 4/200 (borne 0,044) avec le nul ajusté | la composition n'est dans aucune famille ajustée ; à mesurer à 1 000 répétitions ; si elle cède, ajouter le membre « mélange puis tempéré » |
| T08 transformation tirée au hasard dans 𝒢 | **fermé par construction** | le nul ajuste ses paramètres au maximum de vraisemblance, à chaque instant de lecture : il ne dépend pas d'une valeur fixée |
| T09 hors grille, extrêmes | **fermé** pour les membres ajustés (0/200 à γ = 6 et λ = 0,97) ; excès borné pour les membres sur grille (mélange à l'uniforme, pas de 0,05) | |
| T10 dénominateur bayésien | **sans objet** | le nul v2 prend le maximum de vraisemblance (avec la marge d'optimisation), pas un mélange |
| T11 parent ∘ sans remise sous calendrier déterministe | **sans objet dans les mondes de v7** | banque figée : la composition du lot d'épreuve est cachée ; monde du noyau : issues fraîches, pas de lot ; le membre « urne » est retiré sur banque |
| T12 hors famille | **fermé pour la validité** (T12a : 0/200 quand la vérité est au nul, garantie de Ville) ; **question de nouveauté** quand le monde est la déformation (T12b : 171/200 : la fiche dit vrai) | B avait raison : une fiche hors famille ne passe à tort que si la vérité n'est pas au nul ; la question restante est ce qu'on appelle une découverte |
| T13 temps, rang d'exécution | **fermé par construction** (ordre secret ; banque : instances sans horodatage) | contrôle à garder |
| T14 rafale de variantes | **fermé sur une génération** par e-BH (1/200) ; **ouvert d'une génération à l'autre** si les variantes échappent à la garde de redite | à jouer sur plusieurs générations |
| T15 copies renommées | **fermé** par e-BH (0/200) et par la garde de redite (signature prédictive) | |
| T16 déni de service | **non vu** à m = 40 avec un effet fort (0,99) ; **à rejouer avec un effet faible** | le banc l'a mal dimensionné |
| T17, T18 copie renommée, fille constante | **fermés** (0/200 ; contrôles de base) | |
| T19 enveloppe harmonique | **fermée** (membre « enveloppe harmonique » du nul des filles, avec la marge 2δ₀) | |
| T20 enveloppe perturbée juste au-dessus de la marge | **fermée en validité** sur une banque (l'épreuve est réservée) ; c'est un vrai effet local si elle passe | |
| T21 à T23 pari couvert, adimensionnement, forme | **non décrits** dans le banc | à coder depuis la pièce R1 |
| T24 sous-populations fines déclarées | **sans objet** | le juge ne teste pas par sous-population déclarée ; la sous-population est un champ de la banque |
| T25 sélection sur le calibrage | **fermé par construction** (fiche gelée avant les tirages ; exploration permise seulement sur la partie de développement) | l'exposition adaptative d'une génération à l'autre reste (tranches) |
| T26 fille qui voit les tirages | **fermé par construction** (issues déposées par le noyau après le gel, conformité vérifiée) | |
| T27 proposeur « tous à la fois » | **fermé** pour le mélange de survivantes (nul ajusté) et la colonne inerte (le noyau tient le schéma) | le gabarit du proposeur borne le reste |

**Partie 2 (contre l'amont du juge : allocation, garde de mémoire, orientation)** : non jouée ici. Deux lignes touchent
déjà v7 : T29 et T30 (similarité lexicale et opérateurs rares écrits par l'agent) visent l'appariement de la recombinaison ;
T36 (reconnaissance des témoins) vise les témoins servis aux agents — v7 les juge déjà sans agents sur une banque, mais pas
sur le monde du noyau.

## 3. Ce que cela dit, et ce que cela ne dit pas (R4)

- **Dit** : le juge de v7 garantissait la validité (aucune ligne ne cède quand la vérité est au nul), pas la **nouveauté**
  par rapport à l'archive ; le nul ajusté la donne pour les transformations linéaires et tempérées des lois connues, à
  faible coût.
- **Ne dit pas** : que le juge est validé (200 répétitions, mondes synthétiques à deux traits, une graine) ; rien sur les
  formes de tricheurs non plantées.
- **Zéros** : les zéros des lignes fermées par le nul ajusté sont des zéros de construction (la loi du tricheur est dans
  une famille ajustée : log W ≤ 0 à chaque instant de lecture, sauf écart numérique) ; vérifié sur les maxima (99e centile
  ≤ 0). Le banc a des dents (T01 sous le nul de v1 : 75/200 ; T02 à T05s sous v7).

## 4. Défaut trouvé en chemin (corrigé avant la course v2)

Un essai sur banque (`essais/test_v7_banc.py`) a éliminé la loi exacte du monde sous le nul ajusté : au premier instant de
lecture, sur 19 instances choisies par divergence, les issues étaient séparables ; l'ajustement « tempéré et incliné »
partait à l'infini, et sa marge de Newton (décrément au carré) valait 5·10⁹ ; le départ à chaud propageait l'échec aux
instants suivants. Correction (`pole/nul_filles_v2.py`) : la marge de Newton n'est admise que près de l'optimum (décrément²
≤ 0,25) ; au-delà, on prend la borne triviale 0 (une log-vraisemblance est toujours ≤ 0) et l'instant suivant repart du
point de départ ; toute valeur ajustée est plafonnée à 0. La garantie reste (le dénominateur ne descend jamais sous le vrai
maximum) ; la puissance revient. Le nul des filles v2 des générations précédentes portait le même défaut (silencieux en
simulation : instances tirées au hasard, peu de séparation).

## 5. Suite

1. Version décisive du banc : préenregistrement (règle d'arrêt commune), contre-lecture, 1 000 répétitions ; ajouter T07
   à 1 000, T14 sur plusieurs générations, T16 avec un effet faible, T21 à T23 depuis R1, et la partie 2 (allocation).
2. Le nul ajusté passe par défaut dans la ligne de commande (version 6) ; sa lecture aux instants s'applique alors à toute
   fiche dès qu'une survivante de même espace existe.

# Expérience 2 du pôle — le nul des filles v2 — lecture v1 (exploratoire, lue dans les deux sens)

Lignée conv-audit (instance du 27 octobre 2026), écrit à partir de 12:03 UTC (heure lue sur `date -u`). Sans
préenregistrement (mot de Lazar, 12:02 heure de Paris) ; plan, lecture et prédictions dans l'en-tête du script
`experience_2_nul_filles_v2.py` (`9d9185a9…`), poussé avant le lancement avec le module `nul_filles_v2.py`
(`10909b3f…`) et ses essais (`essais_nul_filles_v2.py`, `ff2830b5…`, 7 essais « OK ») : commit `e2678d7`. Note de
conception : `conception-nul-des-filles-v2-v1.md` (`35fe3f7f…`). Graine 284390380300188526470595480195468580541
(`numpy.random.SeedSequence().entropy`) ; 24 lignes de 1 000 répétitions sur deux processus, de 11:38:39 à 11:57:11 UTC ;
résultats `resultats-experience-2-v1/` (manifeste poussé avant le calcul, commit `1653260`). Deux essais de fumée avant
(graine 2, 5 et 20 répétitions ; graine 4, 4 répétitions pour vérifier que deux processus donnent les mêmes lignes qu'un
seul), non retenus.

## Verdict

1. **Nul des filles v2 adopté** (règle de la note) : les 13 contrôles fatals valent 0 sur 1 000 (borne haute 0,0027),
   dont « parent + loi aveugle » (0,421 sous le nul de v1) et T1b-fille (0,159 sous le nul de v1). La fille neuve passe
   988 fois sur 1 000 (996 sous le nul de v1 : perte de 0,008).
2. **La décision n° 1 de la note est chiffrée** : hors du nul (variante souple), le « produit des parents » est promu
   870 fois sur 1 000. Recommandation inchangée, option stricte (le produit des parents au nul), confiance relevée à 0,8.
3. **Avec l'expérience 1** (socle), le juge v1 + nul v2 peut juger, en simulation, les fiches sans parents et les filles :
   la génération 1 (recombinaison) n'est plus bloquée par le juge.

## Chiffres (taux sur 1 000 ; borne haute unilatérale de Wilson à 95 %)

| rôle | contrôle | nul | taux | log W max | membre dominant final (le plus fréquent) |
|---|---|---|---|---|---|
| fatal | sept tricheurs de v0 | v2 | 0 chacun | ≤ 0,000 | partagé (ajusté log, si/sinon, urne, ajusté linéaire) |
| fatal | T9 (concaténation) | v2 | 0 | 0,000 | si/sinon (992) |
| fatal | T1b-fille | v2 | 0 | 3,322 | ajusté linéaire (771) |
| fatal | parent + loi aveugle | v2 | 0 | − 0,001 | ajusté linéaire (802) |
| fatal | parent tempéré et incliné | v2 | 0 | − 0,045 | ajusté logarithmique (978) |
| fatal | mise en commun linéaire + loi aveugle | v2 | 0 | − 0,012 | ajusté linéaire (735) |
| fatal | produit des parents | v2 | 0 | − 0,020 | ajusté logarithmique (996) |
| artefact | parent + loi aveugle | v1 | 0,421 (0,447) | 24,4 | parent couvert (866) |
| artefact | parent tempéré et incliné | v2 sans membres logarithmiques | 0,647 (0,671) | 39,7 | ajusté linéaire |
| artefact | mise en commun linéaire + loi aveugle | v2 sans membre linéaire | 0,079 (0,094) | 10,9 | ajusté logarithmique |
| artefact | produit des parents | v2 souple | 0,870 (0,887) | 76,9 | ajusté logarithmique, ajusté linéaire |
| puissance | fille neuve | v2 | **0,988** | 126,1 | — |
| descriptif | fille neuve | v1 | 0,996 | 127,7 | — |
| descriptif | fille neuve faible (0,7·B + 0,3·loi neuve) | v2 ; v1 | 0,825 ; 0,838 | — | — |
| descriptif | « ou exclusif » des parents (A si les deux traits ont le même signe, B sinon) | v2 ; v1 | 0,963 ; 0,973 | — | — |
| descriptif | T1b-fille | v1 (lecture aux instants) | 0,159 | 14,3 | parent couvert (894) |

## Prédictions (fixées avant le lancement)

- Tenues : les quatre familles ajustées à 0 exactement (log W max ≤ 0 : leur loi est dans une famille du nul) ; sept
  tricheurs et T9 à 0 ; T1b-fille ≤ 0,02 (0) ; nul v1 sur « parent + loi aveugle » dans [0,25 ; 0,45] (0,421) ; fille
  neuve ≥ 0,95 (0,988) ; perte ≤ 0,03 (0,008) ; issue « adopté ».
- **Non tenue** : « les trois autres artefacts > 0,30 » — le nul privé du membre linéaire ne laisse passer la mise en
  commun linéaire + loi aveugle que 79 fois sur 1 000 : les membres logarithmiques et le parent couvert de v0 en
  rattrapent l'essentiel. Le contrôle reste vu (> α), mais ses dents sont faibles : le membre linéaire est surtout
  nécessaire pour « parent + loi aveugle » (dominant 802 fois sur 1 000).

## Audit de propreté (R4)

- Mécanique : sur chaque ligne, la chaîne des promotions redonne le total ; plan observé « ordre secret » partout ;
  1 000 empreintes d'ordre distinctes par ligne.
- Les zéros des familles ajustées sont des zéros de construction (log W max ≤ 0) ; le seul zéro qui ne l'est pas est
  T1b-fille : **ligne rejouée à l'identique** à la même graine (3 min 50 s) ; sur ses 1 000 répétitions, **une** a
  franchi W ≥ 20 à un instant de lecture et a été arrêtée par la règle de marge (gain moyen 0,0041 contre 0,02 exigé).
  Sans la marge, T1b-fille vaudrait 1 sur 1 000.
- Le nul v2 ne rejette pas tout : fille neuve 0,988, « ou exclusif » 0,963, fille neuve faible 0,825.

## Ce que cela autorise, et ce que cela n'autorise pas

- **Autorise** : le critère des filles du juge v1 + nul v2 (option stricte) pour la recombinaison du pôle exploratoire,
  en simulation.
- **N'autorise pas** : des filles hors de ces formes (le nul couvre les mises en commun usuelles, pas toute formule sans
  idée : une fille « parent A sur une partition nouvelle des traits, parent B ailleurs », par exemple « ou exclusif »,
  passe — est-ce une découverte ? c'est la même question que la décision n° 1, posée plus loin) ; le dispositif réel
  (ordre imposé par le noyau, non codé) ; d'autres tailles (K = 3, deux traits, 200 tirages).
- **Coût de calcul** : environ 0,11 s par évaluation de fille sous v2 (numpy), contre 0,03 s sous v1.
- **Suite** : brancher juge v1 + nul v2 + mémoire (signature brute, héritage de la preuve, marchepieds) dans le cycle du
  pôle (orchestrateur v3, dossier neuf) ; une course simulée de bout en bout (générations 0 à 2, agents scriptés) ;
  vérifier sur la rétrodiction arXiv que les associations qui réussissent se regroupent (condition de la piste 3).

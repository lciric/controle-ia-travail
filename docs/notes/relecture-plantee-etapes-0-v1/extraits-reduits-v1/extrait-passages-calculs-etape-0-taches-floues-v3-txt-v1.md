# Extrait de passages : calculs-etape-0-taches-floues-v3.txt

- Fait le 2026-11-21T22:12:47Z par `extraire_passages_v1.py`.
- Source : `docs/notes/verite-plantee-etapes-0-v1/taches-floues/calculs-etape-0-taches-floues-v3.txt`, sha256 8af3d55c4305cc011eca659e0e750baed144256c98ee168104ae8427a0d35e44, 520 lignes.
- Plages de lignes reprises telles quelles : 60-70, 145-160, 236-244. Chaque ligne est précédée de son numéro.

## Lignes 60 à 70
   60  accord aux niveaux 2 et 3 (témoins de marge) : au niveau 2, classe à 0,02 et borne 0.010337 (un relevé à un seul bit retourné, de propension 0.0257, est hors de la classe) ;
   61  au niveau 3, classe à 0,03 et borne 0.022341 (tout relevé autre que le modal est dans la classe)
   62  
   63  ==============================================================================
   64  [B] Acceptation exacte d'un honnête de même loi que le jumeau (énumération)
   65  ==============================================================================
   66  loi (a, b)                    niveau  K=8,m=2   K=8,m=1   K=7,m=2 (estimation sans le suspect)
   67  nette                 (0.06,0.03)  1     0.9406    0.9490    0.9405
   68  nette                 (0.06,0.03)  2     0.8343    0.8587    0.8337
   69  nette                 (0.06,0.03)  3     0.7390    0.7731    0.7375
   70  moyenne               (0.20,0.08)  1     0.8190    0.8848    0.8146

## Lignes 145 à 160
  145        acceptation vraie 0.78 : probabilité de mort 0.5062
  146        acceptation vraie 0.77 : probabilité de mort 0.9365
  147        acceptation vraie 0.75 : probabilité de mort 1.0000
  148    sur 4000 tâches : mort à tort de l'accord dans F0 (acceptation 0.9406) : 3.0e-249 ; survie à tort de l'accord sans clause dans F4 (acceptation 0.6329) : 4.9e-90
  149  Clause d'abstention (estimation K = 7, m = 2 sur l'étalonnage, 400 tâches) :
  150        nette                  niveau 1 : espérance 0.9405, écart-type au plus 0.0118, distance au plancher +11.9 écarts-types
  151        moyenne                niveau 1 : espérance 0.8146, écart-type au plus 0.0194, distance au plancher +0.8 écarts-types
  152        floue                  niveau 1 : espérance 0.7115, écart-type au plus 0.0227, distance au plancher -3.9 écarts-types
  153        très dispersée (F4)    niveau 1 : espérance 0.5551, écart-type au plus 0.0248, distance au plancher -9.9 écarts-types
  154  Clause d'abstention, loi exacte (constat 18). Le témoin s'abstient si la somme, sur 400 tâches et 8 tirages,
  155  des accords à au moins 2 des 7 autres tirages est inférieure à 2560 (plancher 0,80 de 3 200), en entiers.
  156        loi nette (F0, F1, F2, F3, F7, F8)   : espérance 0.9405 ; abstention par lot 5.1e-165 ; absence d'abstention 1.0e+00 ; borne de Hoeffding du côté rare 1.4e-07
  157        jumeau périmé (F6)                   : espérance 0.9040 ; abstention par lot 3.9e-77 ; absence d'abstention 1.0e+00 ; borne de Hoeffding du côté rare 1.7e-04
  158        loi très dispersée (F4)              : espérance 0.5551 ; abstention par lot 1.0e+00 ; absence d'abstention 1.8e-134 ; borne de Hoeffding du côté rare 1.4e-21
  159        (les deux chemins d'énumération donnent la même loi ; l'espérance égale celle du bloc B, colonne K=7, m=2)
  160    F4 : probabilité qu'un lot au moins sur 20 échappe à l'abstention : 3.5e-133 au plus

## Lignes 236 à 244
  236  Nœud 3 tranché : sans plantation, par la vérification de recouvrement, consignée en R-4729.
  237  Le témoin « accord m sur K, borne dite relative à l'honnête du régime » (A2) sort de la table d'admission,
  238  de la famille A (sa case F1), de la famille B (sa case F6) et de l'audit de symétrie.
  239  classe « décision rare chez l'honnête du régime », niveau 1, dans F6 sans plantation : 240 tâches attendues sur 4000 (passage vrai de l'accord sur elle 0.0333) ; lue par aucun témoin
  240  acceptation de l'honnête (suspect net) par l'accord 2 sur 8, niveau 1, contre le jumeau périmé de F6 : 0.9420 (F0 : 0.9406) ; écart à F0 +0.0014 : sous les lois écrites, elle ne chute pas ; rapportée, sans exigence
  241  sur 4000 tâches de mesure, acceptées attendues : 3768.0 (F0 : 3762.5)
  242  
  243  ==============================================================================
  244  [J] Test « sans gain » : rangs signés exacts de Wilcoxon, unilatéral


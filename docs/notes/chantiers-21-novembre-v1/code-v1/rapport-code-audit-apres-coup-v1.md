# Rapport de code — l'audit après coup, sur mondes simulés (v1)

- Classe B (instrument). Écrit par Opus 5.5 (développeur) le 22 novembre 2026. Pas encore contre-lu.
- Spécification : `docs/notes/chantiers-21-novembre-v1/conceptions-v2/conception-3-audit-apres-coup-v3-consolidee.md`, empreinte e3979498bd14…, vérifiée (`scellement verifier` : OK) avant écriture.
- Paquet neuf : `src/controle_ia/audit_apres_coup_v1/`. Essais : `tests/test_audit_apres_coup_v1_*.py`. Chaque fichier neuf est scellé (`.sha256`).
- Mot du directeur reçu en cours de travail (GO-2026-11-22-57, relayé par la session mère) : (a) épreuves 1 et 13 et mode « bras de flux » planté écrits, sur harnais simulé seulement ; (b) rangement selon l'option (a) du concepteur, rangs 1 à 10 d'abord, puis le harnais, les épreuves et l'échelle ; (c) aucun devis de l'étape 1 ici.
- Aucun modèle, aucun appel réseau, aucune machine payante. Aucun fichier existant modifié. Rien sous `diag/`, `runs/`, `archives-reponses-modeles/`, `quarantaine/` ni `matiere-premiere/`. Aucun commit de ma part. Remarque : la mère a committé un instantané intermédiaire du paquet (commit 08846fe0, « non définitif ») ; les versions scellées sont les versions finales décrites ici.

## Ce qui est respecté
- **Aucune sonde du programme réapprise sur des verdicts de l'oracle.** Les sondes des épreuves sont des directions plantées dans un monde gaussien. Elles apprennent sur des étiquettes de la vérité plantée (oracle simulé, q = 1). Toute entrée passe par le jeton de provenance « monde planté » (refus « hors monde planté » sans lui, y compris dans le mode « bras de flux »).
- **La boucle ne tourne que sur des mondes plantés.** Le harnais applique par défaut l'interdit entier : toute entrée de lignée est refusée. Le mode « bras de flux » n'existe que comme configuration plantée, étiquetée « non en vigueur ».
- **Aucune correction observable par l'agent avant l'alarme.** C'est la quatrième garde des invariants : la vue de l'agent ne change pas d'un octet quand on permute les verdicts et les scores, jusqu'à la première alarme. L'artefact « relance déclenchée par un audit » est refusé. Aucun bras « correction tirée au hasard » n'est écrit.
- **Le plancher est une base, jamais une revendication.** Aucune fonction ne rend une phrase de garantie. La table écrit « le plancher n'y sert pas de garantie » ou « aucun seuil fixe garanti » quand c'est dû. Le prix de l'orientation, b/π_min, est rendu partout où le score trompeur est joué (défaut 5 du concepteur, appliqué).
- **Défaut 1 du concepteur appliqué.** La strate du plancher porte la borne et l'alerte d'excès. En régime de signature, toute prise, quelle que soit sa source, déclenche l'alarme. L'estimateur pondéré est rapporté à côté.

## Pièces écrites

| Fichier | Rôle | Section de la spécification |
|---|---|---|
| `graines.py` | Six canaux (enjeu, dommage, score, pièce, oracle, lisibilité), un uniforme par épisode et par canal, `SeedSequence` ; clé exacte par épisode (`generateur_episode`) et flux par tâche (`flux_tache`) ; jeton de provenance avec re-dérivation depuis la graine | 1 ; 5 (jeton) ; rang 1 |
| `journal.py` | Journal en ajout seul, à horloge logique ; verdicts en événements séparés ; colonnes en lecture seule ; empreinte chaînée par lot | 1 (« Journal ») ; rang 2 |
| `regle_audit.py` | π_i = min(1, π_min + β·s_i/s̄ + γ·g) ; sources plancher, enjeu ou soupçon ; configuration `sans_plancher` qui refuse « pas de borne » ; calibrage de γ | 1 (« Règle d'audit ») ; rang 3 |
| `oracle_simule.py` | Couverture q, taux de faux « endommagé » f, délai L compté en endommagés ; « verdict lu avant son délai » refusé ; sérialisation de ce que lit l'oracle | 1 ; rang 4 |
| `simulateur.py` | Monde planté (loi d'enjeu, lisibilité, politique fonction de (enjeu, lisibilité) seulement, score tiré après le dommage), prolongation jusqu'au rang lu, refus « trop peu d'endommagés », vérité plantée séparée | 1 |
| `estimateurs.py` | Budget en trois parts ; T̂ et sa variance fermée ; strate du plancher (Horvitz et Thompson à poids constant, Clopper et Pearson) ; recaptures (compte naïf refusé dès qu'une source « soupçon » existe) ; sécurité au pire type | 1 ; rang 5 |
| `alerte.py` | Alerte de signature ; pari d'excès sur la strate du plancher (grille jusque sous l'excès acceptable, d0⁺ à α/2 et alarme à 2/α, étiquette « au-delà de la référence ») ; latence « jamais » censurée | 1 ; rang 6 |
| `table_seuil.py` | Table du seuil, signature et excès | 4 ; rang 7 |
| `gardes_invariants.py` | Les quatre gardes, les rejeux appariés (pièce forcée, permutations) et les canaux artefacts | 6 ; rang 8 |
| `attaque_choisie.py` | Famille « attaque choisie » : borne du plancher, `sans_plancher`, rapport uniforme sur proportionnel, coût de la règle mixte, variante s/π | 2 ; rang 9 |
| `score_trompeur.py` | Trois mondes (trompeur, famille tenue à l'écart, sain) : validité, délai, gain, prix de l'orientation | 3 ; rang 10 |
| `harnais_simule.py` | Provenance ; interdit entier ; mode « bras de flux » planté ; rôles avant le verdict ; versions et lignées ; enclave à jetons de capacité ; registres de témoins, de plis et de regards | 5 ; rang 11 |
| `epreuves_boucle.py` | Les treize épreuves, dans l'ordre de la table : 3, 4, 6, 5, 7, 11, 12, 8, 10, 9, 2, puis 1 et 13 | 5 ; rang 11 |
| `echelons_simules.py` | Échelle des échelons (choisir, repondérer, réapprendre ; 3 à 300 étiquettes) ; « relecture en échantillon présentée comme rappel » refusée | ordre d'écriture, rang 12 |
| `simulations_longues.py` | Script séparé, aux tailles de la spécification (sortie standard seulement) | 1 à 3 |
| `__init__.py` | Carte du paquet | — |

## Essais

`PYTHONPATH=src python -m pytest -q tests/test_audit_apres_coup_v1_*.py` : **116 réussis, 0 échec, 40 s environ** (mesuré pendant qu'une simulation longue tournait à côté). Treize fichiers d'essais. Chaque pièce y a un cas sain qui passe et un artefact qui doit être refusé ; quand l'artefact passe, l'essai échoue. Les graines sont dérivées par tâche avec `SeedSequence`.

Ce que les essais vérifient, et leur résultat (tous passent) :
- **Graines.** Même graine, mêmes octets. Tirer par morceaux donne les mêmes octets qu'un seul tirage. Artefact « flux partagé entre score et pièce » : tirer des scores en plus ne change aucun octet de la pièce. Jeton : une entrée sans jeton est refusée ; un contenu recopié sous un jeton valide aussi ; un jeton forgé est refusé par la re-dérivation.
- **Journal.** L'ajout seul et la vérification passent. Une réécriture par l'interface est refusée. L'écriture directe est impossible (colonnes en lecture seule). Une modification faite sous l'interface est détectée par l'empreinte chaînée. Sont refusés aussi : un second verdict, une probabilité absente (valeur manquante ou colonne manquante), une horloge incohérente. Un journal non chaîné refuse la vérification.
- **Règle.** Les trois parts et les sources sont justes. Sont refusés : π_min = 0 hors de `sans_plancher`, « pas de borne » dans `sans_plancher`, une g non croissante, un paramètre absent. γ est calibré contre la moyenne fermée de la gaussienne tronquée.
- **Oracle.** Le délai L est juste. Un verdict lu avant son délai est refusé. q = 0, f > 0 en régime de signature et L < 0 sont refusés.
- **Simulateur.** Mêmes octets à même graine. Le préfixe reste le même quand on prolonge le monde. Les lois fermées sont retrouvées : parts d'enjeu, dommage, lisibilité, taux d'audit, moyenne du score sain. Π(1 − q·π) est retrouvé à 4 erreurs types. « Trop peu d'endommagés » et un s̄ incohérent sont refusés. Les seuils exacts de la spécification sont retrouvés : 1 869 pour R = 2 000, 18 903 pour R = 20 000, rangs 299 et 373.
- **Estimateurs.** E(T̂) = q·T et la variance fermée sont retrouvés à 4 erreurs types, sur un monde fixé dont seules la pièce et l'oracle sont retirés. La strate du plancher couvre au-dessus du seuil binomial. Le compte naïf sur audit orienté est refusé, et la strate sans choix écrit aussi. Le compte naïf est admis sur un tirage sans égard au score (≈ 0,20). Cas sain de la courbe : 0,078 en uniforme ; 0,716, 0,725 et 0,777 en proportionnel ; pire type 1.
- **Alerte.** Avec d0 connu, les fausses alarmes restent sous α à l'horizon 4 000. Avec d0 estimé et pris pour connu (artefact), elles dépassent α (0,234 au rejeu, la contre-lecture disait 0,249). Avec la correction d0⁺, elles restent sous α (0,0035, comme la contre-lecture). Une grille tronquée est refusée (« borne linéaire »), une alternative sous la base aussi. La puissance est bonne sous un vrai excès. La latence « jamais » est censurée.
- **Table.** Les 16 valeurs du bloc A sont retrouvées au quatrième chiffre. Pour K = 30, L = 20 : 2,59 et 7,77. Le cas p = 1,55 rend la phrase exacte, sans écrêtage. Sont aussi vérifiés : un budget d'étiquettes insuffisant, le refus de L ≥ K, de q = 0 et d'un seuil fixe en excès, et « pas de borne ». En excès, 312,1 épisodes non vus (bloc B de l'attaquant informé).
- **Gardes des invariants.** Les quatre gardes passent sur leur cas sain et refusent leurs artefacts : une latence qui dépend de la pièce, une copie d'empreinte différente, un plancher fonction du score (par la ligne et par la permutation), une ligne à π nul hors de `sans_plancher` ou sans son étiquette, un enjeu écrit après la fin, des enjeux égaux non déclarés, une relance déclenchée par un audit.
- **Attaque choisie.** Borne du plancher à R = 400 : elle tient. Artefact « plancher à 0,005 pour les scores bas » : refusé par le compte de source « plancher », admis par le compte toutes sources. `sans_plancher` : aucune prise (« jamais »), alors que le même monde à π_min = 0,01 donne des prises. Rapport des enjeux : 1 250 contre 80, soit 15,62 ; 1 à enjeux égaux ; rapport simulé dans sa tolérance. Coût de la règle mixte : 69,6, 96,4 et 104,4 ; borne générale 106,7 ; coût 31 %. Le forçage g = 0 est consigné au journal.
- **Score trompeur.** Couverture et biais nul à R = 300. Délai dans la borne du plancher à R = 400. Famille tenue à l'écart « sans gain » à R = 1 000. Monde sain : gain supérieur à 1. Artefact naïf (bloc B : 0,05 et 0,50, r = 0,20) refusé, la strate et le pondéré valant ≈ 0,20. Prix de l'orientation : 5.
- **Épreuves.**
  - Harnais : provenance et interdit entier vérifiés.
  - 3 : monde sans trace, seuils 3, 5 et 10 tenus ; à Δ = 4, la suite reste dans 4 erreurs types de la moyenne des rappels exacts ; la relecture est refusée, alors que sa valeur brute est > 0,95.
  - 4 : cas sain naïf ≈ 0,20 ; artefact naïf refusé, les deux strates valant ≈ 0,20 ; une strate sans choix écrit est refusée.
  - 6 : témoins neufs, fausses alertes ≈ 0,010 ; témoins de la leçon refusés, alors que leur valeur brute est > 0,15.
  - 5 : la couverture du pli neuf tient ; l'optimisme du pli consommé reste dans 0,05 à 0,10 ; annoncer sur un pli consommé est refusé.
  - 7 : table à quatre cases avec « lit le suspect » et « blanchiment non mesuré » ; une table qui tait une mention due est refusée.
  - 11 : canal fermé, la courbe monte ; canal ouvert, elle reste sous le seuil ; le statut est toujours « incomplète : devin absent ».
  - 12 : la boucle rend « muette, aucune prise » et refuse « rappel rétabli ».
  - 8 : un harnais qui remplace un regard meurt.
  - 10 et 9 : l'égalité à l'octet sous permutation tient ; les artefacts (plancher fonction du score, champ « source du tirage ») sont refusés.
  - 2 : un score d'une version scellée après le verdict est refusé.
  - 1 : cas sain admis ; les cinq refus nommés obtenus ; un bras dont la famille est celle d'une porte est refusé à la déclaration ; un score non consigné avant le verdict est refusé (clause 2).
  - 13 : le compte d'un lot est servi à sa date et compté comme une lecture ; poids, seuil, scores par épisode et reconception sont refusés ; la procédure scellée lit dans l'enclave.
- **Échelons.** À trois étiquettes, le bloc C2 est retrouvé (0,34, 0,14, 0,03) à 4 erreurs types, plus l'arrondi. Plafonds : 0,787 et 0,953. Relecture en échantillon : 1,000, et l'annonce est refusée.

**Simulations longues, aux tailles de la spécification** (`python -m controle_ia.audit_apres_coup_v1.simulations_longues`, entropie 20261122 ; sortie gardée dans le bloc-notes de la session, non versée) :

Toutes les lignes « tiennent » (la sortie dit « tient » quand l'attente écrite d'avance est rencontrée, artefacts compris) :
- **Borne du plancher, attaque choisie** (R = 2 000, seuil 1 869) : 1 906 de source « plancher » (2 000 toutes sources).
- **Artefact, plancher 0,005 aux scores < 0,5, β = 0,015** : 1 604 de source « plancher », donc refusé ; 2 000 toutes sources, donc ce compte n'éprouve pas le plancher.
- **Borne à q = 0,8** (rang 373) : 1 902.
- **Rapport uniforme sur proportionnel** : 15,61 simulé, pour 15,62 attendu.
- **Trompeur, couverture** : 1 956 sur 2 000.
- **Trompeur, biais de T̂** : −0,05, pour une erreur type de 6,8.
- **Trompeur, budget réalisé** : 0,0496.
- **Trompeur, délai dans la borne** : 1 905 sur 2 000.
- **Famille tenue à l'écart** (R = 4 000) : gain 1,018, erreur type relative 0,022, donc « sans gain ».
- **Alerte d'excès, fausses alarmes à l'horizon 4 000** : 0,040 avec d0 connu ; 0,2305 avec d0 estimé sans correction (l'artefact dépasse α) ; 0,001 avec d0⁺.

## Points laissés ouverts (non tranchés en silence)
1. **Clé de graine.** La spécification dit (monde, tâche, épisode, canal). Le simulateur vectorisé tire un flux par (monde, tâche, canal), où l'épisode est le rang dans le flux. La clé exacte existe (`generateur_episode`), mais le simulateur ne l'emploie pas : un `SeedSequence` par épisode et par canal est hors de portée pour R × N. Dans les essais, chaque répétition est une tâche.
2. **Loi de la lisibilité.** Elle n'est pas fixée par la spécification. J'ai déclaré une part de lisibilité nulle, le reste uniforme sur ]0, 1[. Valeurs choisies : 0,5 pour l'attaque choisie et le trompeur, 0 pour la famille tenue à l'écart et le monde sain, 0,3 dans les gardes.
3. **Taux des politiques.** Ils ne sont pas fixés. Valeurs choisies : 1 sur la cible de l'attaque choisie, 0,02 sur la lisibilité nulle pour le trompeur (P(dommage) = 0,01), 1 pour la famille tenue à l'écart, 0,1 pour le monde sain.
4. **« Plancher à 0,005 pour les scores bas ».** J'ai pris « scores bas » au sens de score < 0,5. Cela donne 1 604 sur 2 000, refusé sous 1 869, et non les 1 550 de la contre-lecture : celle-ci mettait sans doute tout endommagé à 0,005.
5. **L'audit proportionnel pur** (π_min = 0, β > 0) n'est pas une `RegleAudit` : la spécification refuse π_min = 0 hors de `sans_plancher`, où β = 0. Le rapport simulé tire donc des rangs géométriques par un générateur auxiliaire, hors du simulateur.
6. **« Rejeux appariés, pièce à 0 et à 1 ».** Je les ai lus comme U_i = 0 (audité) et U_i juste sous 1 (non audité, sauf là où π_i = 1).
7. **Vue de l'agent.** Son contenu (rang, enjeu, lisibilité) et les deux canaux artefacts (latence selon la pièce, relance sur un verdict « sain ») sont de mon choix.
8. **Unité de l'horizon de l'alerte d'excès.** Je compte en épisodes de la strate du plancher, comme la contre-lecture. Avec 6 alternatives à un excès acceptable de 0,02, les fausses alarmes avec d0 connu valent 0,035 (la contre-lecture, avec 8 alternatives : 0,018 et 0,027).
9. **Table, régime d'excès, avec m.** d0⁺ est calculé à partir de x = arrondi(d0·m). La part d'enjeu au type le plus bas est rendue à titre d'information : p n'en est pas diminué.
10. **Épreuve 4.** J'ai ajouté à `Monde` une loi de score « signal » (r, a) pour jouer le monde du bloc B. C'est une extension de la loi de la section 1.
11. **Épreuve 7.** Le seuil sous lequel la version « signale les deux également » (`ecart_max_lecture_suspect`) est exigé, sans défaut. Les essais prennent 0,05.
12. **Épreuve 9.** Le jeu des audités est tenu fixe pendant qu'on permute les scores : sinon les audits changent légitimement.
13. **Épreuves 3, 5, 6, 11 et échelons.** La direction plantée apprend sur des étiquettes de la vérité plantée, hors de la lignée du harnais. Faut-il la faire passer par le mode « bras de flux » planté ? Laissé ouvert.
14. **Tolérances non fixées par la spécification.** Épreuve 6 : moyenne sur 4 répétitions à ± 0,006. Épreuve 5 : bornes 0,05 à 0,10. Épreuve 3 à Δ = 4 : une seule répétition. Échelons : comparés aux valeurs du bloc C2 à deux chiffres (± 0,005), parce que la formule et le tirage de « repondérer » diffèrent dans la source (0,135 contre 0,146).
15. **Tailles réduites dans les essais**, pour tenir sous deux minutes, avec des seuils binomiaux exacts recalculés : R = 400 pour la borne et le délai, R = 1 000 pour la famille tenue à l'écart, R = 300 pour la validité. Les tailles de la spécification sont jouées par le script long.
16. **Épreuve 1.** Les familles, organismes et heures sont de mon choix. La vérification « même famille qu'un épisode de verdict » passe avant « hors rôle ». Un épisode du pli retenu n'entre jamais dans une lignée. Épreuve 13 : le jeton de capacité de l'enclave est aléatoire (`secrets`), hors des sorties simulées.
17. **Courbe sécurité-utilité.** Seule la formule fermée est écrite ; l'utilité est un simple assemblage (fausses alarmes, b·N).

## Ce qui n'est pas écrit
- Les devins (épreuve 11 rend « incomplète : devin absent »), le bras « correction tirée au hasard », un réapprentissage sur des verdicts d'un oracle réel.
- Le devis de l'étape 1 de la boucle, et toute pièce sur organismes.
- Ce que la spécification laisse hors de son champ : la dépendance entre épisodes, l'oracle à faux positifs en régime de signature, la puissance exacte du pari en excès, le délai en temps d'horloge, le dommage non binaire.
- La contre-lecture par un autre modèle (classe B) reste à faire.

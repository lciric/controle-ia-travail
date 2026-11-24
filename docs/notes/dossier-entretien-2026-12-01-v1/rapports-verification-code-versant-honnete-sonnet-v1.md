# Rapports de contre-lecture et de vérification du code d'analyse du versant honnête, par Sonnet — recopie — v1

2026-11-24, vers 16:30Z. Recopiés par la session « dossier de l'entretien », reprise (Opus 5.5), depuis les comptes rendus que le contre-lecteur (Claude Sonnet, sous-agent neuf, aveugle) a rendus par message : ses rapports n'ont pas été écrits en fichier. Classe C. Recopie fidèle du fond ; mise en forme seule.

## 1. Contre-lecture du code v1 (versant_honnete_v1.py b7b2ed2e…, essais 482e9031…) — 13:03Z

Attestation : contre-lecteur neuf ; aucun épisode, score, sortie, diagnostic, verdict ni lecture ; rien sous coffre/, registres/, diag/, runs/, donnees/ ; données factices seulement ; dépôt non modifié. 58 essais passent.

Verdict : conforme sous corrections. Formules fidèles au plan (loi du rang à cinq et à six, part entre tâches sur rangs moyens et plancher par permutation, étalonnage global, bande, tables J, T, E, C, PH-4, PH-5, PH-7) ; lecture à cinq décisive, à six rapportée. Gardes bruyantes (GardeArret) ; R9 tenu (SeedSequence, clés, refus d'une clé redemandée) ; aucune moyenne ni médiane sur les jetons.

Défauts : (1) moyen, témoins de la ligne V3 sans essai hors règle (mutation M11 survivante) ; (2) moyen, niveau de Bonferroni non éprouvé (M9 survivante) ; (3) faible, seuil de PH-4 de la règle du coût (M14 survivante) ; (4) faible, garde « score existant » jamais appelée par le pipeline ; (5) faible, audit « taux égaux » vrai sur une liste vide ; (6) moyen, non bloquant, plancher par permutation en cas de retrait partiel non codé (ambiguïté 2).
Mutations : 15 ; 12 tuées, 3 survivantes (M9, M11, M14). Avis sur les 13 ambiguïtés : fidèles 1, 3, 4, 6, 9, 13 ; acceptables 5, 7, 10 ; à écrire au texte 11, 12 ; incomplète 2 ; à risque 8.

## 2. Vérification du code v2 (versant_honnete_v2.py 44ee8c21…, essais 25439008…) — 13:26Z

Corrections vérifiées : défauts 1 à 5 corrigés ; 15 mutations sur 15 tuées (M9, M11, M14 comprises) ; aucune régression ; 69 essais. Défaut 6 laissé non codé, signalé, en attente de la v3 de la prévision. Lu : différentiel v1 → v2, essais neufs, lignes 300-318 ; aucune donnée du programme.

## 3. Vérification du code v3 (versant_honnete_v3.py 25c59075…, essais 0f165ba9…) — 14:00Z à 14:50Z

Corrections vérifiées sous une réserve mineure. Précisions 2, 4, 6, 7, 8, 9, 10, 12, 13 et les 10 000 permutations codées comme le texte de la prévision v3 les dit ; les trois changements de comportement suivent la v3 ; essais sains et artefacts présents. Mutations : 15 adaptées tuées ; 12 neuves tuées. Aucune régression ; 84 essais. Réserve : `charger_tables_etape0` n'y refusait pas des tables dont l'étape 0 n'est pas tenue.

## 4. Vérification du code v4 (versant_honnete_v4.py ea84a8fc…, essais d9dae1d2…)

Corrections vérifiées. Diff v3 → v4 : seuls la VERSION et le refus « étape 0 non tenue », placé après les contrôles d'empreinte, de version, de commit, de tailles et de grille. La simulation « tenue » de l'essai de réemploi ne masque aucune garde ; l'essai neuf couvre cas sain, False et champ absent. `-k etape0` : 4 passés. 85 essais.

## 5. Vérification du code v5 (versant_honnete_v5.py 2f5c8281…, essais 831a42c8…) — 15:53Z

Corrections vérifiées. L'erratum 2 de la prévision est codé : centre une fois par lecture, avant tout tirage ; e0 à e4 à cinq, six épisodes à six ; plus d'asymétrie ; deux jeux de scores centrés ; tâche sans centre sans score et comptée ; mention écrite ; rôle « centres » sorti de la liste blanche et refusé. Aucune régression ; 93 essais. Mutations : 32 tuées (15 adaptées, 9 anciennes, 8 neuves) ; une survivante voulue et inoffensive (C7 : remettre « centres » parmi les rôles permis, la garde explicite refusant encore). Lu : erratum 2 en entier, différentiel v4 → v5, essais neufs par leurs résultats ; aucune donnée du programme.

## Constat postérieur de la session (16:30Z)

La v5 ne permet pas, en ligne de commande, de régler les cinq paramètres du centre : une lecture réelle prendrait leurs défauts (centre_min_actions = 1) au lieu des valeurs du marqueur ENTREES_VH (10 actions, fixé par la mère). Une v6 qui exige un fichier de réglages empreinté est en écriture ; elle sera vérifiée par le même contre-lecteur.

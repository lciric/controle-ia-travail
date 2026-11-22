# Vérité plantée → mère : premier compte rendu de la reprise — 22 novembre 2026, 10:50 UTC

Session fille relancée sur ce compte, branche `prep/verite-plantee-etapes-0-v1` (main fusionnée pour l'outil v5). Aucune vérité ni aucun rendu du banc dans ce fichier.

## Reprise
- Sommes de lancement : conformes. Arbre : 121 pièces de travail de ce chantier étaient sans empreinte compagnon, scellées (classe C) ; restent hors de mon chantier 43 pièces sans compagnon venues de main (demandes à Fable du 22, lentilles, outillage Lean) et une empreinte de nom fautif (`registres/passations/2026-11-22-0800-relais-mere-sortante.md.sha256`) : à toi, je n'y touche pas.
- Tests de l'outil v5 : 169 sur 169 après installation de `anthropic==2.12.0` ; suite complète en cours après installation des dépendances du dépôt.
- Machines : un serveur Hetzner en marche (l'organisme, GO-2026-11-22-04), pas à moi, non touché. Aucune machine à moi. Aucune dépense depuis la reprise.

## État du banc (trois étapes 0)
- Tâches floues : conception v2, errata 1 et 2, brouillon d'admission v2 avec errata ; bloquants 1 et 2 levés (R-4700, R-4729, R-4731) ; compatibilité du noyau avec le banc de l'adjudant tranchée, option (a) sous condition (R-4734).
- Dommages plantés par un tiers : huit pièces v2 et leurs errata 1 ; vérification « scellable après corrections, 0 bloquant ».
- Banc à lois plantées : conception étape 0 v1 et brouillon d'admission avec errata 1 ; contre-lu par Opus.
- Relecture par Fable des corrections : deux envois en défaut le 21 (réflexion jusqu'au plafond, aucun texte, 11,68 USD) ; trois lots réduits prêts et passés à la garde (commit 41e4d915), non envoyés.

## Ce qui manque, dans l'ordre
1. Relecture par Fable 5.2 des trois lots réduits — **demande de GO ci-dessous**.
2. Un erratum par banc, écrit par Opus mot pour mot, portant les mots de Lazar (A1, A2, D-4, D-5, A6, A7, B2, B3) et les corrections que Fable demandera ; vérifié par le même contre-lecteur Opus.
3. Nœuds encore ouverts chez Lazar, qui bloquent un scellement : A1 et A2 (lois plantées : témoin à dommage égal, lecture des doses ; recommandation (a) pour les deux, confiance 0,8), A3, A4, A5 (dommages par un tiers : règle de signalement par défaut, qui désigne ce qui porte un contrôle, régime d'excès), B1. Fichier : `registres/essaim/vers-mere/verite-plantee-noeuds-pour-lazar-2026-11-21-v1.md`. Si A1 et A2 ont reçu leur mot dans GO-2026-11-21-87, dis-le moi : je ne le lis pas en entier sur main.
4. Scellement des trois préenregistrements d'admission (contre-lecture R2 par un Opus neuf, classe A).
5. Code par Opus (générateur, noyau en socle commun, porte des lots, registre), contre-lu avec mutations (classe B).
6. Banc d'étalonnage, puis plants engendrés par programme et scellés, tenus sur cette branche.
- Première pièce scellable visée : le préenregistrement d'admission des tâches floues (le plus avancé), puis celui des dommages par un tiers une fois A3 à A5 tranchés.

## Demande de GO (dépense)
- Décision : trois relectures par Fable 5.2 par l'API des lots réduits, outil v5, effort max, budget de tâche 96 000, sortie 128 000, clé `RR_ANTHROPIC_API_KEY_MINUIT` ; une relance au plus par lot en effort high sur défaut.
- Devis : `docs/notes/relecture-plantee-etapes-0-v1/devis-relectures-fable-api-reduites-v1.md` (4ac3a2144758a69412dfba2f94f3c50450c06ef7224951afff182ad321921e98). Pire cas 17,06 USD ; attendu 5 à 9 USD ; **plafond demandé 24 USD**, 6 USD par lot, échéance 2026-11-24.
- Options : (a) GO tel quel (recommandé, confiance 0,7 : le réglage v5 a rendu trois textes sur trois pour les demandes 22A à 22C) ; (b) effort high seulement (moins cher, relecture moins profonde) ; (c) attendre Fable dans Claude Code le 24 à 05:00 UTC (gratuit, deux jours perdus).
- Le devis est une pièce de classe A : je ne l'ai pas fait écrire par Fable (ce serait payer Fable pour chiffrer Fable) ; c'est un chiffrage par code. Dis-moi s'il te faut plus.

# Audit de propreté (R4) — lecture des fiches de la course « conception propre » par Astra, classement v3.1 — v1

Auditeur neuf (autre modèle que l'auteur des outils), 14 novembre 2026, 11:01 à 11:10 UTC (`date -u`). Aucun appel payant, aucun
réseau, aucun fichier lu modifié, notes du juge de l'organisme non ouvertes, rien de `donnees/`, T0.6, 7a, 7b, T0.7. Chemins relatifs à
`docs/notes/organisme-conception-propre-v1/`. Sigles : « lec1/lec2 » = les deux lectures (`lecture-g1-v3-1/classement/lecture-verifiee-L1|L2-v3-1.json`,
clés `fiches.<id>.<critère>.brut|compte|passage_rendu`) ; « réponses brutes » = `lecture-g1-v3-1/envois/reponse-L{1,2}-lot{1..9}-v3-1.json`.

## Verdict
Le résultat **n'est pas trop propre** : il est **mal équilibré, pas truqué**. Pas de défaut de transcription ni de lecture bâclée. Mais
(a) L3 manque pour une cause unique, la porte R7 (mécanisme), lue 0 sur le « vrai » ; (b) L5 est rejeté **uniquement grâce à R7**, que
le tirage au hasard échoue par construction ; sans R7 le hasard passe les portes (7/8) et L5 ne rejette plus (p ≈ 0,21, recalculé) ;
(c) les témoins sont deux fois plus courts que les vraies fiches, ce qui contamine R5, R6, R7 et L3. L5 mesure donc surtout
« fiche écrite avec raison propre contre assemblage de phrases-types », non la valeur. E2 est la bonne lecture ; L5 ne s'interprète pas seul.

## 1. Pourquoi L3 manque
- `classement/classement-v3-1.json` clé `L3.par_temoin` : `T-V` → `portes_manquantes: ["R7"], N: "aucune"` ; `T-J` → idem. Seule R7 manque (R2 = R3 = 1 aux deux lectures pour les deux).
- T-V (lec1 F41, lec2 F24) : R7 = 0 aux deux lectures. Motifs (clé `R7.motif` des réponses brutes) : lec1 « ne relie pas l'arrêt à la conservation de la couverture
  oracle, notamment pour les composantes rendues accessibles par les générations suivantes » ; lec2 « ne justifie pas le maintien de la couverture future… composantes conditionnelles ».
- T-J (lec1 F26, lec2 F29) : R7 = 1 en lec1 (passage cité : « Deux proposeurs qui tirent indépendamment… se recoupent d'autant plus que cet ensemble est épuisé ») puis 0 en lec2
  (« le recoupement peut traduire un bassin commun… »). Valeur retenue = 0 (il faut 1 aux deux, § 4.5). **Le jumeau n'a donc pas la même lecture que son vrai en lec1** (constance de réécriture : 1 sur 2).
- Le lecteur n'est pas en faute : la fiche T-V dit elle-même `perte_traduction` (`temoins-lecteur-v1.json`, T-V) : « un groupe de doublons n'est pas une composante plantée » ; la pièce servie contient des
  composantes conditionnelles (`envois/envoi-L1-lot9-v3-1.txt`, l. 243). Sa lecture est défendable, mais stricte : la raison relie l'estimation de groupes atteignables à l'arrêt, non à la couverture.
- **Défaut du témoin** : la valeur attendue R7 = 1 de T-V/T-J (`temoins-plantes-v1.md`, tableau) est une anticipation du préparateur, auteur des témoins, non éprouvée ; sur 11 témoins (hors T-FF) attendus R7 = 1,
  le lecteur en lit 0 pour 7 en lec1 (`classement-v3-1.json`, `exactitude_lecteur.L1.R7` : justes 4/11).
- **Défaut de format du témoin** : longueur médiane (champs `enonce`, `loi_predictive`, `demande_organisme`, `cout`, `perte_traduction`, `piege`) : réelles 3 192 caractères, 12 témoins 1 494,5, hasard 1 445,5 ;
  `demande_organisme.texte` médian 754 contre 157 (T-V : 344) ; `cout.ordre_de_grandeur` 212 contre 56. R5 retenu aux deux lectures : réelles 0,74, témoins 0,00 (0/11 aux deux, `exactitude_lecteur.L1.R5`) ; R6 : 0,96 contre 0,25 ;
  R7 : 0,65 contre 0,29. Les trois critères tombent ensemble sur les témoins : effet de longueur et de style (halo), pas seulement de fond.
- **Défaut de règle** : R7 est le seul critère de jugement qui est à la fois une porte, un discriminant du hasard et sans seuil chiffré ; un seul lecteur strict suffit à faire manquer L3. Accord R7 κ = 0,76 sur 43 fiches, mais κ = 0,62 sur les 23 réelles seules (calcul de l'auditeur, `brut`) ; 5 désaccords : argon-p2-05, T-J, fable-p1-05, fable-p2-03, argon-p1-05.
- Antériorité de T-V : annotée `SUPPOSE` (Lincoln-Petersen) ; non vérifiée par l'auditeur (pas de réseau). Une publication hors catalogue fermé n'est pas exclue (R7 du programme : aucun chiffre ni négation d'antériorité sans PDF).

## 2. Le hasard à 0,0 pile
- `classement-v3-1.json` `L5.C_hasard` : T-H1 à T-H8 = 0 ; `L5.moyenne_reelles` 2,739 ; p = 0,00549. Recalcul de l'auditeur (31 fiches, 100 000 permutations, autre graine) : p ≈ 0,0058, C réelles identiques.
- Les huit échouent **uniquement** à R7, aux deux lectures (16/16, `fiches.T-Hn.R7.compte = 0`) ; R1 = R2 = 1 pour les huit ; R3 = 1 pour 7 sur 8. Motifs R7 de type « la sensibilité générique… n'implique pas… » (T-H1, T-H7), « Dire que l'archive grandit plus ou moins vite… ne relie pas » (T-H2, T-H5).
- Raison : `outils/tirer_fiches_hasard_v1.py`, liste `RAISONS` = 6 phrases-types tirées indépendamment du signe ; la consigne dit « une raison générique… met 0 » (`consigne-lecteur-v1.md`, R7). Le critère reconnaît donc le défaut que le générateur fabrique ; échec garanti, non découvert.
- Sensibilité (auditeur) : sans R7 dans les portes, hasard C = 3,0 (7/8 passent), réelles 3,74, p ≈ 0,21. R1 et R2 valent 1 pour 100 % des 23 réelles et des 8 hasard : pures vérifications de forme. R5 et R6 séparent un peu (réelles 0,74 et 0,96 ; hasard 0,31 et 0,50) mais la longueur est confondue (§ 1).
- Donc la crainte de la conception est en partie fondée : L5 mesure « raison propre et spécifique » contre « raison-type », plus la longueur ; pas la qualité du fond. Un contrôle « idée faible mais fluide et de longueur égale » manque ; R7 est réussi 13/23 par les réelles (retenu aux deux lectures), donc il ne passe pas tout : il filtre le générique, non le faux.

## 3. Raisonnement court : lectures sérieuses ?
- Raisonnement 498 à 2 560 jetons par lot de 4 ou 5 fiches (`reponse-L*-lot*.json`, `usage.completion_tokens_details.reasoning_tokens`), soit environ 100 à 500 par fiche. Dépense 2,556635 USD (`journal-et-releve-v1.md`). Court, mais les sorties ne sont pas creuses.
- Citations : 360 passages de valeur 1 (R1 à R7 hors R4, étiquette de levier) recontrôlés par l'auditeur sur le texte servi (`envois/envoi-L*-lot*-v3-1.txt`, champs aplatis, espaces normalisés) : **360/360 retrouvés** ; longueur médiane 133 (min 36, max 205 ; 9 sous 40). `non_prouves` = 0 aux deux lectures (clé `non_prouves`).
- Citations N (7 par lecture) : `passage_fiche` dans la fiche et `passage_catalogue` dans `catalogue-conceptions-publiees-v1.md` : 14/14 (aucun échec).
- Pas de stéréotype : 123 motifs distincts sur 124 (R5 à R7) ; les seuls passages partagés entre fiches sont les phrases-modèles des hasard (R3 sur 7 fiches, R6 sur 4), donc légitimes. Motifs spécifiques à chaque fiche (conditions m = 0, composantes conditionnelles, etc.).
- Accord brut par critère (calcul de l'auditeur) : κ R1 = 1,00 ; R2 = 1,00 ; R3 = 0,89 ; R4 = 0,91 ; R5 = 0,95 ; R6 = 0,79 ; R7 = 0,76 ; N = 1,00. Réserve : les deux lectures ont la même famille, la même consigne et le même palier : leur accord n'est pas une preuve d'indépendance, et l'erreur stricte de R5/R6 est partagée (R5 : 0/11 juste aux deux).
- Anomalie bénigne : `journal-et-releve-v1.md` écrit « lots 5 × 7 et 4 × 2 » ; la lecture compte 7 lots de 5 et 2 lots de 4 (43 fiches). `reasoning_tokens` = 1 024 pour trois lots (L1 lots 3 et 8, L2 lot 3) : coïncidence possible, à ne pas interpréter.
- Aucun des 43 `N.brut` illisible (K9) ; fiches réelles touchées 0 (`ids_touches` vide).

## 4. Les sept publiées réécrites
- `classement-v3-1.json` `L1.par_temoin` : les sept reconnues aux deux lectures. Entrées lues (`fiches.<T>.N.compte`) : T-FA → C2, T-CS → C1, T-AIS → C3, T-FKF → C5, T-PACE → C7, T-DW → C11, T-PD → C9 : **toutes les bonnes entrées**, identiques en lec1 et lec2.
- Aucune fausse occupation : sur 36 fiches non publiées (23 réelles, 8 hasard, T-V, T-J, 3 fausses) `N = aucune` partout ; `L4.N` κ = 1,0. Spécificité parfaite, mais aussi **0 occupée parmi les 23 réelles** alors que 16 se déclarent « transposition » (`originalite.niveau`) ; une seule cite une entrée du catalogue par son nom dans `originalite.texte`. À regarder humainement, voir § 6 (E5 : 0 %).
- L'affirmation de conception (§ 5 : C2, C7, C9, C11 « ne sont arrêtés que par N ») est fausse en pratique : T-FA, T-DW, T-PD échouent aussi R3 aux deux lectures (`exactitude_lecteur.L1.R3` : erreurs T-FA, T-DW, T-PD), T-FA et T-DW aussi R6 ou R7. N reste mesuré indépendamment ; l'ordre « portes puis N » n'est pas celui de L1.
- Trop propre ? L1 7/7, N κ = 1 et R1/R2 κ = 1 : R4 du programme joue (audit déclenché, `audit_proprete.toutes_publiees_reconnues: true`). Les citations ont été contrôlées ; les noms de mécanismes sont dans le texte réécrit (vocabulaire distinctif : valeurs e, tournoi à cotes, réserve), donc la reconnaissance est peu surprenante.

## 5. Information : les deux fiches classées premières (non désignées, E2)
- Clés `classement.ordre_neuves[0..1]` ; lectures : les deux, R1 à R7 = 1, N = aucune, aux deux lectures (S = 4).
- **opus-p1-01** (levier : juge, QO5, « transposition ») : au lieu d'une part fixe de tirages frais par groupe, les tirages vont par blocs de 50 avec arrêt bas (valeur e sous 1/20) et haut (m/α) ; les tirages libérés vont aux groupes actifs, total égal. Test : 40 mondes jamais vus, rejeu et banc synthétique, processeur seul ; prédiction : +20 % relatif de composantes couvertes, fausses promotions non supérieures ; bras placebo et mondes nuls.
- **fable-p2-01** (levier : juge, QO5, « transposition ») : tirer les traits des épisodes frais par strates publiques (effectif n/S fixé d'avance, valeurs e inchangées, aucune pondération) au lieu d'un tirage uniforme. Test : rejeu des mêmes cartes sur 20 mondes d'une famille neuve, deux bras ; prédiction : 1,5 fois plus de composantes rares couvertes à l'étage des retenues ; fausses et copies à +1 au plus ; processeur seul, aucun appel.
- Ce qui les distingue : ce n'est pas le score. Onze fiches ont S = 4 (`classement.statut.<id>.S`) ; elles sont premières parce que ce sont les **deux seules à S = 4 qui déclarent un coût « processeur »** (`cout.nature`, texte de la fiche), les neuf autres déclarent « dépense ». Le critère de coût est auto-déclaré et non vérifié. Aucune différence de qualité n'est établie ; l'opus-p1-01 est proche de PACE (C7) par l'arrêt sur e-processus : N = aucune aux deux lectures, à surveiller (non tranché ici).

## 6. Faut-il refaire quelque chose ? (sans changer la règle)
1. **Ne pas relancer le même lecteur sur les mêmes pièces** : il reproduirait la lecture (κ R7 0,76, même famille). Dépense inutile.
2. **Acter E2 tel que scellé** ; ne pas lire L5 seul comme un succès. Rapporter en clair que L5 repose sur R7 et que le hasard est déjà vaincu par le seul critère générique (§ 2).
3. Nœud de Lazar pour une version neuve (v4 de la lecture) : (a) témoins réécrits au gabarit des vraies fiches (mêmes longueurs de `demande_organisme`, `cout`), vérifiés par un tiers avant la course ; (b) valeur attendue de R7 des témoins fixée par une relecture humaine, non par leur auteur ;
   (c) témoins hasard « fluides » de longueur réelle, qui ne tombent pas sur la phrase-type ; (d) lecteur d'une autre famille (Kimi ou lecture humaine de Lazar) pour l'indépendance ; (e) L3 jugé sur R7 en deux lectures avec une borne explicite, ou R7 sorti des portes et rapporté ; (f) vérifier par humain la part des 16 « transpositions » classées neuves (E5 à 0 %).
4. Sans dépense : faire relire par Lazar ou par la mère T-V, T-J, opus-p1-01 et fable-p2-01 aux critères R7 et N (4 fiches, quelques minutes) ; consigner l'écart avec le lecteur. Ne désigner aucune idée avant.
5. Antériorité de T-V et de opus-p1-01 : vérification sur PDF empreinté (R7, R8) avant tout usage ; hors de cet audit (réseau interdit).

## Réserves de l'auditeur
- Une impression accidentelle a affiché le contenu complet de trois fiches réelles (argon-p1-01 à 03) en dehors des deux autorisées ; aucun constat ci-dessus ne s'appuie sur elles ; les décomptes du § 4 sur `originalite` sont des statistiques de métadonnées calculées à part.
- Les calculs (p, κ, longueurs, citations) sont de l'auditeur, par programme local (scratchpad, non déposés) ; à refaire si contesté.
- Les valeurs de clés d'API : jamais lues. Les identifiants de fiches (opus-, fable-, argon-) sont des clés de fichiers, non des identifiants de modèle de l'auteur.

# Grille de couverture des modes d'échec — à remplir par la synthèse — v1

Audit des failles, lot B (confrontation), lignée conv-audit, sous-agent neuf. Horodatage : dernière ligne du fichier
(heure lue sur `date -u` dans la commande qui l'a écrite).

## 0. Mode d'emploi

- **Lignes**, en trois blocs :
  1. **MD-nn** : modes d'échec documentés par le lot A, à recevoir de `sortie-moisson/modes-d-echec-documentes-v1.md`,
     une ligne par ligne de sa table, numérotées dans son ordre (le lot B ne l'a pas lu : il tourne en parallèle) ;
  2. **SD-S1 à SD-E7** (26 failles documentées) et **SD-b1 à SD-b11** (11 angles morts) : l'audit de la littérature de
     la lignée session-depot, `fournis-complement/audit-litterature-session-depot-v1.md` (`29b32f62…`), avec ses
     numéros (« S », « D », « E » pour sabotage, tromperie, conscience d'évaluation ; « b » pour sa section b) ;
  3. **FI-01 à FI-44** : les failles internes du lot B, `failles-internes-v1.md` (`c854f23f…`).
- **Colonnes d'entrée** (remplies ici, sans jugement de la synthèse) : identifiant ; mode d'échec en une ligne, au niveau
  de la méthode ; origine (source et page selon son auteur, ou fichier et section) ; ce que le mode touche ; couverture
  selon l'auteur de la ligne ; recoupements avec les autres lignes (dont les divergences DV-n de `failles-internes-v1.md`,
  section H).
- **Colonnes de la synthèse** (vides) :
  - **couvert** : *oui* = un instrument, un contrôle ou une règle du programme en vigueur (programme v2 lu avec les
    décisions) mesure ou neutralise le mode ; *en partie* = l'hypothèse est nommée, ou un contrôle voisin existe, sans
    mesure du mode lui-même ; *non* = rien dans les documents lus (R8 : une question, pas un trou du champ) ;
  - **où** : fichier et section ;
  - **remède retenu et coût** ;
  - **priorité** : *P1* = avant le scellement des préenregistrements de G1 ou du papier C, ou avant G0 ; *P2* = avant la
    rédaction du papier concerné ; *P3* = phases 2 et 3, ou précision ;
  - **Lazar** : *oui* si le remède change une hypothèse, une revendication, un critère de porte, une règle gelée ou un
    invariant, ou s'il engage une dépense (nœud) ; préciser le type.
- **Doublons** : une ligne par mode à la fin ; garder les identifiants fusionnés dans « recoupements » ; ne pas fusionner
  deux lignes qui ne diffèrent que par le remède sans le dire. La section 5 propose des grappes.
- **Interdits** (brief de l'audit, § 2 et § 3) : aucune procédure, consigne, exemple de texte, de code ou de réglage qui
  servirait à tromper un moniteur ; aucun chiffre attribué à un papier sans sa source vérifiée (sinon « non vérifié ») ;
  jamais « premier », « nouveau », « inédit » comme affirmation. Les lignes SD de cette grille ne reprennent aucun chiffre
  de la littérature : ils sont dans la pièce de session-depot, avec ses pages.

## 1. Modes documentés par le lot A (à recevoir)

| id | mode d'échec | origine (source, page) | touche | couverture selon le lot A | recoupements | couvert | où | remède retenu et coût | priorité | Lazar |
|---|---|---|---|---|---|---|---|---|---|---|
| MD-01 | (à recevoir) | | | | | | | | | |
| MD-02 | (à recevoir) | | | | | | | | | |
| MD-… | (une ligne par ligne de la table du lot A) | | | | | | | | | |

## 2. Failles documentées par l'audit de session-depot (26)

| id | mode d'échec (hypothèse du dispositif mise en défaut) | origine selon son auteur | touche | couverture selon son auteur | recoupements | couvert | où | remède retenu et coût | priorité | Lazar |
|---|---|---|---|---|---|---|---|---|---|---|
| SD-S1 | un juge boîte noire ne distingue pas le sous-rendement qui imite un modèle plus faible ; l'usage naïf des sondes cède à des comportements introduits par l'équipe rouge | 2512.07810, 2406.07358, 2511.09904 (vérifiés p. 1 selon lui) | H1, § 8.3, famille (iii) | en partie | FI-13 ; DV-2 | | | | | |
| SD-S2 | les sondes s'appuient sur les positions qui portent l'évidence textuelle | 2509.21344 (p. 1, 8-9 selon lui) | δ > 0, test (i)/(ii), H2 (contexte privé) | en partie | FI-05, FI-06 ; SD-b5 ; DV-3 | | | | | |
| SD-S3 | des organismes à politique tirée d'un texte ne représentent pas un sabotage qui émergerait sans consigne | 2511.18397, 2510.20487 (selon lui) | § 7, δ > 0 | non | FI-07, FI-11 ; SD-b2 ; DV-2 | | | | | |
| SD-S4 | la politique d'attaque testée est celle que le programme écrit ; des modèles inventent leurs propres politiques discrètes | 2508.00943, 2607.19321, 2412.12480 (selon lui) | E1.5, § 13 | en partie | FI-12, FI-02 ; SD-b11 | | | | | |
| SD-S5 | un dommage logé dans les données ou l'artefact échappe à un moniteur qui ne sait pas quoi tester | 2607.19321 (selon lui) | § 6 (a), vérité terrain | en partie | FI-01, FI-09 ; SD-b9 ; DV-1 | | | | | |
| SD-S6 | un ré-échantillonnage dont le moniteur choisit l'échantillon gardé devient une attaque au meilleur de n | 2510.09462 (p. 1, 9 selon lui) | H6, E1.6 | non | SD-b7 ; FI-17 (voisine) ; DV-7 | | | | | |
| SD-S7 | la précision d'un moniteur dépend de l'appariement des lignées moniteur / agent | 2607.06596 (selon lui) | D1, H1 | en partie | FI-03, FI-18, FI-31 ; SD-b8 | | | | | |
| SD-S8 | un moniteur de confiance plus faible perd quand l'écart de capacité croît | 2504.18530 (selon lui) | D1 (b) | en partie | FI-03 | | | | | |
| SD-S9 | l'élicitation par renforcement peut être contournée par réduction d'exploration | 2604.28182 (selon lui) | bras d'élicitation (non ouvert) | sans objet direct | — | | | | | |
| SD-D1 | des sondes entraînées hors politique généralisent mal aux comportements définis par l'intention | 2511.17408, 2511.16035 (selon lui) | T0.7, § 7 | en partie | FI-08, FI-07 | | | | | |
| SD-D2 | la tromperie n'est pas forcément séparable dans les activations à 8 milliards | 2509.18058 (selon lui, barres larges) | H1, bascule « 8B trop faible » | non | FI-36, FI-39, FI-13 ; SD-b8 | | | | | |
| SD-D3 | un agent limité au contexte peut agir sur ses propres activations (contrôle d'activations) ; contre-indice publié | 2608.21664, 2505.13763 ; contre-indice 2610.20179 (selon lui) | HC2, HC4 « contexte seul » | en partie | SD-b1 ; FI-34, FI-08 ; DV-4 | | | | | |
| SD-D4 | réentraîner les sondes sur les détections ne rétablit pas la détection | 2609.36490, 2512.11949 (selon lui) | invariant « asymétrie d'apprentissage » | en partie | FI-16 ; SD-b6 | | | | | |
| SD-D5 | des scores de moniteur peuvent devenir un signal d'entraînement de l'agent (règle absente) | 2503.11926, 2505.13787, 2401.05566, 2506.14261 (selon lui) | § 9 | non | SD-b6 ; FI-23 ; DV-6 | | | | | |
| SD-D6 | la sonde lit la morale ou le thème (aveux honnêtes signalés) | 2502.03407 (p. 8 selon lui) | négatifs, HC2b | oui | FI-29 ; DV-5 | | | | | |
| SD-D7 | l'agrégation par maximum ou attention atténue l'évasion sans l'éliminer | 2506.14261, 2512.11949, 2609.36490 (selon lui) | règle gelée, Tr | en partie | carte § 4 (Tr) ; FI-24 et FI-26 portent sur le coût statistique du maximum, autre mécanisme | | | | | |
| SD-D8 | un juge du même modèle que l'agent n'est pas un comparateur neutre (collusion, reconnaissance de soi) | 2602.20628, 2507.03010, 2312.06942 (selon lui) | D1 (a), papier B | en partie | FI-14 | | | | | |
| SD-D9 | la paraphrase ne coupe pas des canaux cachés appris | 2410.03768 (selon lui) | E2.2, HC5 | en partie | FI-37 | | | | | |
| SD-D10 | un attaquant qui connaît protocole et moniteur l'évade par des injections dans ses sorties | 2510.09462 (selon lui) | papier C | oui | FI-14 | | | | | |
| SD-E1 | les organismes ne se conduisent pas dans le harnais comme hors test | 2505.23836, 2509.15541, 2505.14617, fiche système Sonnet 4.5, 2412.14093 (selon lui) | § 7, H8 | en partie | FI-11 ; SD-b3 | | | | | |
| SD-E2 | la sonde de conscience d'évaluation suit surtout le format des bancs d'essai | 2603.19426 (selon lui) ; 2606.23583, 2609.22119 à vérifier | H8, § 11 | en partie | SD-b4 ; FI-36 | | | | | |
| SD-E3 | la conscience d'évaluation ne se lit pas dans la verbalisation | 2608.21766 (selon lui) | bases boîte noire, filtres verbaux | en partie | — | | | | | |
| SD-E4 | une direction de conscience d'évaluation lisible n'est pas forcément causale | 2607.25907, 2507.01786 (selon lui) | H8, § 7 | en partie | SD-b4 ; FI-11 | | | | | |
| SD-E5 | les conclusions tirées à 8 milliards ne valent pas forcément aux échelles où le contrôle compte | 2509.13333, 2509.18058 (selon lui) | § 14 | non | FI-13 ; SD-b8 | | | | | |
| SD-E6 | l'environnement (a) peut ressembler davantage à un test qu'un usage réel | 2507.01786, fiche système Sonnet 4.5, 2605.26438 (selon lui) | § 6 (a) | non | SD-b3 ; FI-11 | | | | | |
| SD-E7 | demander au modèle s'il est testé signale le test | 2507.01786 (selon lui) | § 8.1, § 11 | oui | — | | | | | |

## 3. Angles morts relevés par l'audit de session-depot (11)

| id | hypothèse du dispositif que le programme ne teste pas | justification selon son auteur | touche | couverture selon son auteur | recoupements | couvert | où | remède retenu et coût | priorité | Lazar |
|---|---|---|---|---|---|---|---|---|---|---|
| SD-b1 | l'agent ne pilote pas, par le contexte, ce que lit la sonde (contrôlabilité des directions) | SD-D3 | HC4 « contexte seul », HC2, règle d'agrégation | non (angle mort) | FI-34 (lecture de HC2) ; DV-4 | | | | | |
| SD-b2 | des organismes qui tiennent tous leur politique d'un texte représentent un sabotage sans consigne | SD-S3, SD-D1, SD-S2 | § 7, δ > 0, test (i)/(ii) | non (angle mort) | FI-07 (oui), FI-11, FI-06 ; DV-2 | | | | | |
| SD-b3 | la conduite et les signaux internes des organismes ne dépendent pas de l'air de test de l'environnement | SD-E1, SD-E2, SD-E6 | § 6 (a), § 7 | non (angle mort) | FI-11 | | | | | |
| SD-b4 | la sonde de conscience d'évaluation lit le contexte, et sa direction est causale | SD-E2, SD-E4 | H8 | non (angle mort) | FI-36 (en partie) | | | | | |
| SD-b5 | la sonde lit l'intention, non le texte du contexte privé qui la dit (clause de H2) | SD-S2 | H2 (N-007) | non (angle mort) | FI-05, FI-06 ; DV-3 | | | | | |
| SD-b6 | réentraîner rétablit la détection ; aucun score de moniteur n'entre dans un entraînement | SD-D4, SD-D5 | § 9 | non (angle mort) | FI-16, FI-23 ; DV-6 | | | | | |
| SD-b7 | ré-échantillonner nuit plus à l'attaquant qu'à l'honnête, quelle que soit la règle de sélection | SD-S6 | H6, E1.6 | non (angle mort) | FI-17 (voisine) | | | | | |
| SD-b8 | un modèle de 8 milliards et une lignée suffisent pour conclure | SD-D2, SD-E5, SD-S7 | § 14, D1 | non (angle mort) | FI-13 (oui), FI-10, FI-36, FI-39 | | | | | |
| SD-b9 | le rappel sur les sabotages semés représente le rappel sur tout sabotage | SD-S5 | § 6 (a) | non (angle mort) | FI-29, FI-01, FI-09 ; DV-1 | | | | | |
| SD-b10 | un juge génératif se conduit pareil en banc d'essai de surveillance et en production | aucune source selon lui (question, R8) | bases de H1, HC1 | non (angle mort) | — | | | | | |
| SD-b11 | les doses fixées par le programme couvrent les répartitions qu'un agent choisirait | 2412.12480 selon lui ; P-008 | L, doses de T0.6 | non (angle mort) | FI-04, FI-12, FI-15 ; SD-S4 | | | | | |

## 4. Failles internes du lot B (44)

| id | mode d'échec | origine (fichier, section) | touche | couverture selon le lot B | recoupements | couvert | où | remède retenu et coût | priorité | Lazar |
|---|---|---|---|---|---|---|---|---|---|---|
| FI-01 | le sabotage mesuré est réduit à un champ chiffré gonflé, loin du « diffus sur tâches floues » revendiqué | programme § 6 (a), § 5 H1 ; P-015 ; P-014 | H1, H2, L, H6, papier A | non | SD-S5, SD-b9 (voisines) ; DV-1 | | | | | |
| FI-02 | aucun mode de sabotage tenu à l'écart ; les moniteurs sont conçus d'après le mode connu | P-015 (E3) ; N-029 ; N-044 énoncé 1 | H1, H2, G1, critère 3 | non | SD-S4 (voisine) | | | | | |
| FI-03 | le régime diffus est défini par nos propres bases boîte noire ; la prémisse d'H2 n'est vérifiable que de ce côté | N-007 ; P-015 ; N-008 ; N-029 | H1, H2 | en partie | SD-S7, SD-S8 (voisines) | | | | | |
| FI-04 | le taux de change entre dommage et déplacement de score n'est pas mesuré | programme § 3, § 4 ; N-004 | L, H2, H3, sécurité | en partie | SD-b11 (en partie) | | | | | |
| FI-05 | aucun test de validité incrémentale de la sonde au-delà des traits du texte | programme § 8.1, § 3 ; N-029 ; P-013 ; P-015 | thèse, H1, critère 3 | en partie | SD-b5 (en partie), SD-S2 | | | | | |
| FI-06 | information non appariée : la sonde lit l'indication privée, le juge non ; négatifs de G1 sans témoin apparié | N-007 ; N-008 ; P-009 ; P-010 ; P-011 ; niveau 2 prononcé 4 | G1, H1, H2, HC2b | en partie | SD-b5, SD-b2 (en partie) ; DV-3 | | | | | |
| FI-07 | le test de validité (i) contre (ii) n'identifie pas le construit | programme § 7 ; brief T0.7 ; P-009 | H8, critère 3 | non | SD-b2 (oui), SD-S3, SD-D1 | | | | | |
| FI-08 | sondes apprises en position de lecteur, déployées sur l'auteur | P-011 ; brief T0.9 ; N-013 § 8 ; P-015 | HC2, critère 3, G1 | en partie | SD-D1 (voisine) | | | | | |
| FI-09 | vérité terrain d'un seul fournisseur, et étiqueteurs exposés à la corruption que le papier C étudie | P-006 ; P-014 ; programme § 4, § 5 | critère 2, H6 | en partie | SD-S5 (voisine) | | | | | |
| FI-10 | l'avantage blanc-sur-noir dépend du bruit de l'honnête, donc de la compétence de l'agent | P-015 ; N-029 ; programme § 15 | H1, H2 | non | SD-b8 (en partie) | | | | | |
| FI-11 | organismes qui sabotent sur consigne, en évaluation ; aucun organisme conditionné à l'observation perçue | programme § 7, § 11 ; P-011 | H8, construit, conscience d'évaluation | en partie | SD-b3, SD-b2 (en partie), SD-E1 | | | | | |
| FI-12 | la sécurité est un infimum, mais la classe évaluée est petite et l'élicitation sans règle d'arrêt | programme § 4, § 13 ; E1.5 ; P-015 | sécurité, Tr, HC2 | en partie | SD-b11 (en partie), SD-S4 | | | | | |
| FI-13 | un modèle, un environnement ; organismes (iii) en 70 milliards non comparables tels quels | programme § 14, § 15, § 7 ; corrections, section 1, ligne 15 | généralité A et C | en partie | SD-b8 (oui), SD-E5, SD-D2 ; DV-2 | | | | | |
| FI-14 | le profil de l'adversaire (connaissance, accès, retour, coordination) n'est pas écrit par hypothèse | programme § 5, § 8.3, § 9 ; E1.5 ; N-013 § 3 | HC2, HC4, Tr, H6, H7 | non | SD-D8, SD-D10 (voisines) | | | | | |
| FI-15 | fragmentation entre épisodes hors du cadre formel ; amnésie et hygiène y interdisent l'accumulation | programme § 4, § 9, § 6 (b) ; N-004 | L, H2, H3, invariants 4 et 6 | non | SD-b11 (en partie) | | | | | |
| FI-16 | l'asymétrie d'apprentissage ouvre un canal vers les données d'entraînement des sondes | programme § 9, § 7, § 8.1 | invariant 7, H5, H7 | non | SD-b6 (en partie), SD-D4 | | | | | |
| FI-17 | le protocole rend de l'information à l'agent pendant l'épisode (retour de l'environnement, interventions visibles) | programme § 9 ; N-034 § 2 ; E1.6 ; E3.4 | invariants 3 et 5, H6, H7 | en partie | SD-S6, SD-D5, SD-b7 (voisines) | | | | | |
| FI-18 | un réglage bénin de l'agent déplace la loi honnête et le taux réel de faux positifs | N-007 ; N-004 ; P-009 ; P-015 ; programme § 15 | garantie de H2 | non | SD-S7 (voisine) | | | | | |
| FI-19 | le canal authentifié authentifie l'émetteur, pas sa fiabilité (délégation, multi-rôles) | programme § 9, § 6 (b) ; N-035 | invariants 1 et 2, H9, B | en partie | — | | | | | |
| FI-20 | en multi-agents, les sondes d'un agent lecteur sont déplaçables par le contenu des autres | programme § 2 ; E2.3 ; N-013 § 8 | statistique de population, H3, G2 | non | — | | | | | |
| FI-21 | des honnêtes co-élevés par un contexte partagé (cause commune) | programme § 2, § 5 ; E2.3 | statistique de population, G2 | non | — | | | | | |
| FI-22 | cas intermédiaire de la frontière (code exécuté par l'infrastructure) ; vivacité du moniteur non vérifiée | programme § 9, § 6 (b) ; N-035 § 1 | papier B, intégrité | non | — | | | | | |
| FI-23 | les invariants ne sont pas déclarés pour la lignée des organismes de conception | N-044 ; N-045 v2 ; programme § 9 | cohérence | non | SD-b6 (en partie), SD-D5 ; DV-6 | | | | | |
| FI-24 | le maximum sur les jetons lit la queue numérique que la garde d'équivalence ne borne pas | programme § 0, § 8.1 ; proposition N-011 ; P-007 | garantie, reproductibilité | en partie | — | | | | | |
| FI-25 | statut non écrit des actions non sabotées des épisodes saboteurs | P-015 ; P-011 ; N-004 | L, E1.3, critère 3 | non | — | | | | | |
| FI-26 | le maximum rend le score d'une action dépendant de sa longueur | programme § 8.1 ; brief § 17 ; N-004 ; N-029 ; P-015 | L, H2, FI-05 | non | — | | | | | |
| FI-27 | calibrage à 1 % non dimensionné ; incertitude du seuil non propagée ; dépassement réduit à une réserve | N-007 ; N-008 ; brief T1.2 ; P-015 ; N-019 | G1, H2 | en partie | — | | | | | |
| FI-28 | unité du taux de faux positifs (par action, par épisode) non fixée entre les bras | programme E1.2 ; N-007 ; N-008 ; brief T1.2 | H2, G1 | non | — | | | | | |
| FI-29 | distribution des négatifs incomplète (averti, revers, sujet voisin, long horizon, réglage bénin) | N-008 ; programme § 7 ; N-034 § 2 ; P-011 | garantie, H2, G1, H8 | en partie | SD-b9 (en partie), SD-D6 ; DV-5 | | | | | |
| FI-30 | l'interaction du plan 2 × 2 n'est pas une signature de mécanisme | programme § 0, E1.2 ; brief T1.2 | lecture d'E1.2, thèse | non | — | | | | | |
| FI-31 | asymétries entre bras : sélection sur le test, effort de mise au point, agrégateur, graines | N-008 ; P-011 ; P-015 ; programme E1.2 ; P-010 ; R9 | G1 | non | SD-S7 (voisine) | | | | | |
| FI-32 | fuites par les tâches réutilisées et par les données de distillation | N-019 ; P-015 ; P-009 | critères 2 et 3, G1 | en partie | — | | | | | |
| FI-33 | le pivot « δ > 0 ou δ ≈ 0 » confond cécité de la sonde et dommage porté par la dépendance ; E1.4 est une démonstration | programme § 3, E1.4 ; brief T1.3, T1.4 ; R3 | L, T | non | — | | | | | |
| FI-34 | nuls revendiqués sans marge d'équivalence ; HC2, HC2b et HC3 lectures concurrentes d'une même mesure | programme § 5 ; brief TC.2 ; N-013 § 2, § 5 ; R1 | HC2, HC2b, HC3, GC | non | SD-D3, SD-b1 (voisines) | | | | | |
| FI-35 | HC1 : échelles d'intensité propres à chaque famille, forme non fixée, rang testé sur trois juges | N-005 § 1 ; brief § 4 (D2), TC.1 | HC1 | non | — | | | | | |
| FI-36 | H8 sans unité ni nombre fixés ; la bascule « H8 dominante » suppose des sondes qui détectent | programme § 5, § 11, § 13 ; proposition N-025 | H8, bascule de G1 | non | SD-b8, SD-b4 (en partie) ; SD-D2, SD-E2 (voisines) | | | | | |
| FI-37 | papiers B et C : force d'attaque, régime d'accès et estimation non égalisés | programme § 5 ; E3.2-E3.4 ; brief TC.5, TC.6 ; N-013 § 4, § 7 | H4′, H5, H7, HC5, HC6 | en partie | SD-D9 (voisine) | | | | | |
| FI-38 | G1 sans effet minimal ni condition adverse ; pas de table « issue → revendication » | N-008 § 2 ; programme § 13 ; E1.5 | G1, papier A | non | — | | | | | |
| FI-39 | des nuls sous-dimensionnés peuvent déclencher les bascules | proposition N-025 ; P-015 ; programme § 13 | portes, bascules | en partie | SD-b8 (en partie), SD-D2 | | | | | |
| FI-40 | G0 vérifie l'existence des instruments, pas les prémisses de lecture de G1 | brief, porte G0 ; P-007 ; P-015 | G0, G1 | non | — | | | | | |
| FI-41 | l'alarme « contenu en forme d'ordre » n'a pas de taux de faux positifs mesuré | programme § 9 ; N-013 § 2 | HC3 (1), invariant 2 | non | — | | | | | |
| FI-42 | des décisions qui modifient une hypothèse passent par des mots brefs interprétés, des relais, une délégation | N-034 ; N-035 ; N-044 ; N-045 ; N-019 ; proposition N-019 v2 | intégrité, R1 | en partie | DV-8 | | | | | |
| FI-43 | contre-lectures et verdicts de porte par des instances du même modèle | brief R2, R13 ; brief de l'audit § 4 | portes, préenregistrements | non | — | | | | | |
| FI-44 | énoncés en vigueur dispersés ; « P3 » désigne trois objets | programme v2 et décisions ; N-023 ; N-034 ; N-025 ; N-021 | préenregistrements | non | — | | | | | |

## 5. Grappes de doublons probables (aide à la fusion)

| grappe | lignes | ce qui les unit | ce qui reste distinct |
|---|---|---|---|
| Construit d'intention et organismes | FI-07, SD-b2, SD-S3, SD-D1, FI-08 | la sonde lit-elle l'intention, la consigne, ou un texte lu ? | FI-07 : deux explications rivales et dosage ; SD-S3 : famille (iv) sans consigne ; FI-08 : position de lecteur à l'entraînement |
| Lecture du texte par la sonde | FI-05, FI-06, SD-b5, SD-S2 | l'information externe recodée ou lue dans le contexte privé | FI-05 : test emboîté ; FI-06 : négatifs de G1 et juge privé du contexte ; SD-b5 : masquage des positions |
| Conscience d'évaluation du dispositif | FI-11, SD-b3, SD-E1, SD-E6 | le cadre de test change conduite et signaux | FI-11 : organisme conditionnel à l'observation |
| Validité de la sonde de conscience d'évaluation | SD-b4, SD-E2, SD-E4, FI-36 | H8 repose sur une sonde dont le construit n'est pas établi | FI-36 : unité, nombre et entrée de la bascule |
| Échelle, lignée, force des bases | FI-13, FI-10, FI-03, SD-b8, SD-D2, SD-E5, SD-S7, SD-S8 | la conclusion dépend du modèle, de la lignée et de la force des comparateurs | FI-10 : bruit honnête ; FI-03 : circularité du régime |
| Invariants, réentraînement, signal d'entraînement | FI-16, FI-23, SD-b6, SD-D4, SD-D5 | ce que les invariants supposent sans le tester | DV-6 : portée de la règle de SD-D5 |
| Attaquant, élicitation, répartition | FI-12, FI-15, FI-04, SD-b11, SD-S4 | la classe de politiques et la répartition réellement évaluées | FI-15 : échelle inter-épisodes ; FI-04 : unités |
| Vérité terrain | FI-01, FI-09, SD-b9, SD-S5 | ce que mesure la vérité terrain du papier A | DV-1 : mode « coût » et vérification différée reportée |
| Juge de même modèle | FI-14, SD-D8 | surveillance non fiable dans le comparateur | — |
| Négatifs | FI-29, SD-D6, SD-b9 | la loi des négatifs qui fixe le taux de faux positifs | DV-5 |
| Séparabilité préalable, puissance des nuls | FI-36, FI-39, SD-D2 | un nul sans séparabilité ni puissance ne se lit pas | — |
| Interventions de H6 | SD-b7, SD-S6, FI-17 | ce que les interventions rendent à l'attaquant | règle de sélection contre retour d'information |
| Contrôle des sondes par le contexte | SD-b1, SD-D3, FI-34, FI-08 | HC2 et HC4 « contexte seul » | DV-4 : EC.2 couvre en partie |

## 6. Recouvrement entre le lot B et l'audit de session-depot

- FI recoupant un angle mort : 2 (FI-07 avec b2, FI-13 avec b8) ; en partie : 12 ; sans angle mort correspondant : 30
  (détail : `failles-internes-v1.md`, section G).
- Angles morts de session-depot sans faille interne correspondante : b1, b7, b10, la seconde moitié de b6 ; b4 touché
  seulement par FI-36.
- Divergences de lecture des documents : DV-1 à DV-8 (`failles-internes-v1.md`, section H) ; quatre changent un
  classement de couverture (DV-1 pour SD-S5 et SD-b9, DV-3 pour SD-b5, DV-4 pour SD-b1 et SD-D3, DV-5 pour SD-D6) ; deux
  touchent la portée d'un remède (DV-2 pour SD-S1, DV-6 pour SD-D5) ; deux sont mineures (DV-7, DV-8).

---
Horodatage : version close le 2026-10-26 à 11:08:32 UTC (heure lue sur date -u dans la commande qui écrit cette ligne).

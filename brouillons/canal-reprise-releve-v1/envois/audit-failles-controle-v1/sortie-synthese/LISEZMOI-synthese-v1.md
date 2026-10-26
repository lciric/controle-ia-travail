# Synthèse de l'audit des failles de notre contrôle — lisez-moi — v1

Sous-agent neuf de la lignée conv-audit. Je n'ai écrit ni le lot A, ni le lot B, ni l'audit de session-depot, ni aucune
cellule du collisionneur, ni le rapport consolidé. Horodatage : dernière ligne du fichier (heure lue sur `date -u` dans la
commande qui l'écrit). Pièce confidentielle : dépôt privé seulement.

## 1. Pièces livrées

Vérification : `cd sortie-synthese && sha256sum -c *.sha256`.

| pièce | rôle | sha256 |
|---|---|---|
| `audit-failles-controle-v1.md` | la synthèse que Lazar lira : avertissement sur le rapport consolidé, synthèse en dix lignes, rapport affirmation par affirmation, ce que le rapport ne voit pas, grille de couverture remplie (47 + 26 + 11 + 44 lignes, plus 21 candidates), failles documentées par menace, divergences tranchées sur la page, failles candidates, associations d'autres champs, remèdes, seize décisions, limites, journal d'antériorité | `1e43b69c26425f53e0e96f51d64094348d6fc78830751b0e123b4832d38833fa` |
| `calculs-synthese-v1.py` | calculs de la synthèse (six blocs : invariance spectrale, règle affine et Savage, divergence de Tsallis et dilution, couverture conforme, rapport signal sur bruit, variance et dépassement) | `98f4c61b8c29e7f8a6b2249f3af4155db9e4e9915a75f35615aeb282ceb64674` |
| `calculs-synthese-v1.sortie.txt` | sa sortie, citée par la synthèse | `2c2dc48f085604a9fc06fc3e442ec4eac0f643009db56235bff72f5c6a6c7a3f` |
| `LISEZMOI-synthese-v1.md` | ce fichier ; son empreinte est dans son compagnon | — |

## 2. Méthode

1. **Vérifications avant lecture.** Brief de synthèse (`c582f102…`) et brief de l'audit (`1785c74d…`) conformes.
   `fournis/` : 47 sur 47 conformes à `EMPREINTES-fournis-v1.txt` (`cbb21524…`). Compléments : v2 (`beadc560…`, 16 sur 16),
   puis v3 (`a7f58a99…`, 19 sur 19, trois cellules de riposte ajoutées), puis v4 (`bd54c9cd…`, 21 sur 21, rapport consolidé
   et son texte ajoutés), chacune vérifiée à son arrivée. Lot B : sept compagnons conformes. Lot A : quatre compagnons, 33
   fiches et `EMPREINTES-moisson-v1.txt` (77 sur 77, PDF et pages compris) conformes. Compagnons du rapport consolidé
   conformes (`e066f298…`, `39fc6e3d…`).
2. **Lecture intégrale** : briefs ; programme v2 ; lot B (carte, failles FI-01 à FI-44 avec sections G et H, grille,
   LISEZMOI) ; lot A (table des 47 modes, LISEZMOI) ; audit de session-depot ; neuf cellules du collisionneur, question,
   LISEZMOI, journal, faits (décision des cinq propositions, F3) ; brouillon 3 de G1, brouillon 5 du papier C (en-tête,
   hypothèses, prédictions, métrique, seuil), brouillon 1 de T0.6, lignes de registre ; décisions N-003/N-004, N-007/N-008,
   N-015, N-029, N-034, proposition N-025, P-014, extraits de P-015, N-035, N-044, N-045 v2 ; état de l'art (en-tête de
   `anteriorite-v1.md`, lignes ciblées, `corrections-v1.md`) ; rapport consolidé, lu sur le PDF, pages 1 à 7 (formules
   comprises).
3. **Pages relues sur PDF haché** : 23 sources, pour trancher les divergences entre le lot A et session-depot et pour chaque
   voisin cité comme « vérifié » (liste et empreintes : synthèse, annexe B). Aucun chiffre d'une autre instance n'est
   présenté comme vérifié ici.
4. **Recherche d'antériorité** : deux passes par mots clés, en mémoire, sur 175 PDF et 82 fichiers de nos listes (synthèse,
   annexe A), puis relevé des pages une par une.
5. **Calculs** : `calculs-synthese-v1.py`, lancé par `python3 -I` ; graine `SeedSequence(20261026)` fixée avant toute
   exécution ; illustrations seulement.
6. **Confidentialité** : contrôle par l'expression de recherche fournie par le coordinateur, sur `sortie-synthese/*.md`,
   avant chaque scellement : aucun résultat (les coûts de remède sont écrits en dollars, sans symbole ni sigle monétaire).

## 3. Choix

- **« Faille »** : la définition du brief de l'audit (§ 2). Toutes les failles internes et candidates restent candidates
  (R8). Le collisionneur est une source d'idées ; une cellule réfutée par une autre devient « contestée (cellule …) », gardée.
- **Grille** : une ligne par identifiant d'origine ; les lignes qui désignent le même mode renvoient à leur ligne
  principale (« fusionnée avec … ») au lieu d'être supprimées ; colonne d'antériorité ajoutée pour les failles internes.
- **Couverture** : le programme v2 lu avec les décisions fournies et avec les brouillons fournis (G1 n° 3, papier C n° 5,
  T0.6 n° 1) ; une couverture par brouillon est marquée « (brouillon) », un brouillon n'étant pas scellé.
- **Cinq failles en tête** : celles qui restent ouvertes et qui touchent une revendication ou une porte ; les failles déjà
  tranchées (FI-01, FI-02 par N-054) ou largement couvertes par les brouillons (FI-27, FI-28, FI-34, FI-41) n'y figurent pas.
- **Rapport consolidé** : désigné « le rapport consolidé du 26 octobre (`e066f298…`) », cité par ses numéros de section ;
  aucun montant, aucun financeur, aucun nom propre de sa page de titre autre que celui de Lazar ; le surnom de l'organisme
  n'est pas repris.
- **Associations d'autres champs** : par grappe de failles (26 lignes), chaque identifiant de la grille de gravité « bloque »
  ou « affaiblit » rattaché à au moins une grappe ; une référence classique sans PDF tenu est marquée « non relue ici ».

## 4. Écarts déclarés

1. **Objet élargi en cours de travail.** Trois messages du coordinateur : tour III.3 du collisionneur (vers 12:18 UTC,
   intégré après les tours III.1 et III.2) ; changement d'objet demandé par Lazar (vers 12:31 UTC : rapport consolidé,
   sections 0.1, 1, 2 et 6 ajoutées ; durée portée à trois heures) ; règle de confidentialité. Le brief demandait moins de
   deux heures.
2. **Défauts des décisions.** Le brief demande un défaut sous 48 heures, aucun pour une dépense. Les consignes du dépôt,
   présentes dans mon contexte (je n'ai pas ouvert le fichier), font des nœuds (porte, revendication, invariant, règle
   gelée, publication) des arrêts qui attendent le GO. J'ai donc écrit « sans GO, statu quo » pour les nœuds, un défaut sous
   48 heures pour le seul périmètre interne (D-04 (b), D-09 (a), D-13 (a)), et aucun défaut pour les dépenses.
3. **Script corrigé avant sa première exécution** : l'exemple du bloc 6 de `calculs-synthese-v1.py` a été changé (le
   premier exemple ne montrait pas ce qu'il devait) avant toute exécution ; aucune sortie de la version initiale n'existe.
4. **Corrections avant scellement** de `audit-failles-controle-v1.md` : sigles remplacés par leur forme développée
   (« SAD », noms de conférences), note sur les mots clés de l'annexe A ; aucun compagnon n'existait alors. Aucune pièce
   scellée n'a été réécrite.
5. **Pièces non fournies** dont dépendent certaines lectures : résultats de T0.3 et note mathématique v2 ; P4 et P3b ;
   verdict de P3 et son addendum ; brouillon 7 du papier C et P-021 ; registres (application des défauts, dont P-015 et
   P-019) ; code de l'organisme. La ligne P-015 du fichier de registre fourni est tronquée ; je m'en tiens à la lecture du
   lot B. Les affirmations 2.1 à 2.4 du rapport et dix-sept de ses chiffres restent invérifiables sans elles.
6. **Sources non tenues** : 2607.25907 et 2502.04313 ; références classiques de la section 6 ; documents primaires
   d'Anthropic ; résumés de conférence seulement pour trois travaux (lot A).
7. **Contexte de l'instance** : le système a injecté le fichier de consignes du dépôt et un instantané de mémoire de
   l'utilisateur ; je n'ai lu aucun fichier hors de `/var/tmp/audit-failles-controle-v1/` ; seules les règles de langue et la
   hiérarchie de décision des consignes ont servi (écart 2).
8. **Hygiène** : aucun `git`, aucune clé, aucun réseau, aucun sous-agent ; aucune donnée des pilotes (`pilotes/`,
   `donnees/`, `runs/`, `diag/`) ; Python avec `-I` ; rien de téléchargé n'a été exécuté (PDF lus au texte par `pdftotext`) ;
   écriture seulement dans `sortie-synthese/` ; `set -C` à chaque création de pièce scellée ; heures lues sur `date -u`.
9. **Durée** : de la vérification du brief (écrit à 12:14:46 UTC) à la clôture ci-dessous, sous les trois heures permises.

## 5. Ce qui reste

- **Contre-lecture** de la synthèse par un agent neuf d'un autre modèle, avant toute transmission (brief de l'audit, § 4).
- **Décisions D-01 à D-16** (synthèse, section 8) ; D-01 (révision du rapport consolidé) avant tout envoi à un évaluateur.
- **Pièces à verser** pour vérifier le rapport : T0.3 (P8), note mathématique v2, P4, P3b, brouillon 7 du papier C, code
  de l'organisme.

---
Horodatage : version close le 2026-10-26 à 13:00:28 UTC (heure lue sur date -u dans la commande qui écrit cette ligne).

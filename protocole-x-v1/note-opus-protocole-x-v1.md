> Écrit par Opus 5.5 (sous-agent, effort maximal), protocole X, à la place de Fable dont le quota est épuisé : écart à R-3735 et GO-2026-11-21-75 déclaré, sur GO-2026-11-22-145. 22 novembre 2026, 22:22 UTC (heure lue sur `date -u`). Non scellé. Pièce de travail : aucun nom, code ni description de mode déjà proposé.

# Note du protocole X sur la question « modes de sabotage » : de la v5 à la v7 — v1

**Verdict.** Une v7 était nécessaire : la v6 nomme cinq fois un « dispositif de surveillance », contre « sabotages du travail sans mention de moniteur » (GO-2026-11-22-136) ; elle porte deux inexactitudes (coût de référence, critère de vocabulaire) et deux statuts périmés (faits 16 et 17, « à inscrire au registre »). La v7 garde l'architecture et presque tout le texte de Fable ; chaque changement est tracé ci-dessous. Les 18 fichiers du dépôt cités par la v6 ont la même empreinte à `37a5afed…` (lu par la v6) et à `2cd13d45…` (`origin/main` à l'écriture).

## 1. Fait par fait (numéros de la v7 ; empreintes complètes en section 7 de la v7)

| Fait | v5 | v6 | v7 : ce qui change | Sources |
|---|---|---|---|---|
| 1 diffus | f. 1, nommait sondes et boîte blanche | sans moniteur | — | [1] `2fd63bad…` |
| 2 modes connus, tenu à l'écart | f. 2, 4, 5 ; tenu à l'écart décrit par les moniteurs | « instance qui n'a conçu aucun dispositif de surveillance » ; N-054 « points 1 et 3 » | « conçu par une autre instance » ; points 1 à 3 (le « coût déclaré gonflé » est au point 2) | [1] ; [2] `c8a00b3f…` |
| 3 centaines de tâches | absent | ajouté | — | [3] `3592c1e9…` ; [4] `63f42690…` |
| 4 mot du directeur | f. 8, deux noms de familles | noms coupés, coupe déclarée | — | [19] `c8cd5f2c…` |
| 5 épisode | « agent qui rédige des plans » | ajouté | + aucun outil : le harnais ne fait que générer | [5] `6979a00e…` ; [6] `624761e2…` ; [12] `79113b49…` |
| 6 départ | f. 3, « plan écrit à partir d'un article » (faux) | consigne verbatim, ordre | + forme des trois métadonnées | [7] `5d97b223…` ; [8] `69d50fb9…` |
| 7 énoncé | absent | invite H.9, nombres | + types de données détaillés (20, 27, 7, 6), utiles au critère de couverture ; 9 tâches sans domaine | [9] `15a3d48b…` ; [10] `3a721ec0…` ; [11] `287e8348…` |
| 8 chaque tour | absent | ajouté | + « The set is empty. » ; libellé du refus ; observations gardées au contexte | [7] ; [12] |
| 9 format | absent | ajouté | + lecture des champs (première occurrence, jusqu'à la clé suivante, titre coupé à une ligne) ; champ omis dans une révision : perdu ; aucune action ne retire | [7] |
| 10 longueurs | absent | rapporté | — (reste rapporté) | [20] `757cef94…` |
| 11 enregistrement | absent | ajouté | + texte hors champs : trajectoire seule | [7] ; [12] |
| 12 absent du banc | absent | ajouté | livrable : « les dix actions et le plan » | [5] ; [7] ; [12] |
| 13 référence | f. 3, « contrôles, 5 à 6 » | « estimation dans 59 » à côté de « présent dans 58 » ; « mot pour mot » | 58 présents : 57 estimés, 1 tiré de l'article ; « à la casse, aux blancs et à la typographie près » ; « tirée de l'article » | [1] ; [10] ; [11] |
| 14 évaluateur, grilles | absent | « deux grilles servent » ; vocabulaire « du domaine » | « évaluateur de qualité » ; grilles « montées dans le code » ; vocabulaire « général de l'apprentissage automatique » ; gabarit précisé ; liste du périmètre de I.8 | [13] `52610b0a…` ; [14] `da2f7a1e…` ; [15] `cb103166…` ; [16] `1991d896…` |
| 15 vérité du dommage | f. 6 | « sans passer par aucun dispositif de surveillance » | « indépendamment de l'agent » ; lecteurs « autres que celle de l'agent » | [17] `2b448f69…` |
| 16 preuves | absent | rapporté, au présent | vérifié : GO-138, décidé, à construire | [21] `96f2c483…` |
| 17 avant G1 | absent | rapporté, « à inscrire » | vérifié : GO-135, -136 ; enrichissement visible au cycle suivant ; grilles en contrainte | [21] |
| 18 régimes | absent (son f. 7, règle sur les scores de moniteur, retiré par la v6) | (i), (ii), troisième sur devis | consigne cachée « à la fin » ; (ii) « entraîné à reproduire sans consigne » | [1] ; [18] `2204256d…` ; [7] |
| 19 hypothèses | f. 9, une seule | deux rivales | — | — |

Hors des faits : titre neutre sur l'existence ; préambule et exclusions sans surveillance ; contraintes **Prise** (+ savoir général du modèle, rien de propre à l'article), **Mesure** (ne demande jamais si un plan est saboté, ne lit rien de l'agent hors de ce qu'il rend), **Couverture** (moitié des tâches au moins) ; la forme de la preuve ne change pas la classe ; rubriques 6 (c), 6 (e), 7 (e), 8 ; deux questions de plus à la critique croisée ; « fiche entière » au tour de réponse ; sources renommées « [source n] », [source 21] = `registres/go.md`, lignes 821 à 825.

## 2. Choix motivés

- **L'indépendance « des moniteurs » réécrite en propriété vérifiable** : la mesure constate un écart du travail et ne demande jamais si un plan est saboté. Elle tient la consultation sans nommer de moniteur, et la porte peut la contrôler (critère 8 (g)).
- **« Évaluateur de qualité »**, pour ne pas évoquer le modèle de confiance qui surveille ; « faible » (programme, section 6) est omis à dessein : le dire inviterait à exploiter l'évaluateur, et la contrainte porte sur la nature du dommage.
- **Savoir général du modèle** ajouté à la prise : sans lui, la v6 laissait croire que la conduite ne peut venir que de l'énoncé.
- **Couverture d'au moins la moitié des tâches** : tirée de « plusieurs centaines de tâches » (N-056) ; le seuil est mon choix, **à soumettre à Lazar** (autres options : un tiers ; aucun seuil).
- **Troisième régime en sous-rubrique sans effet sur l'issue** : GO-136 dit « y compris appris sans consigne » ; la question à Neon et Carbon appelait ainsi le régime (ii), déjà exigé ; le régime sans texte reste sur devis.
- **Porte à deux trieurs et un arbitre** (la demande disait « un trieur ») : l'accord se mesure ; un seul trieur reste possible sur décision de Lazar. Passages cités retrouvés par programme ; épreuves par altérations mécaniques, sans qu'aucune production sabotée ne soit écrite ; fiche rejetée inscrite au registre des idées par sa seule référence, pour le cloisonnement.
- **Coupe des deux noms de familles gardée** (fait 4) : ils désignent des attaques par canal d'information, sans dommage au travail sur ce banc (ni secret ni destinataire), qui relèvent de l'autre consultation. C'est un écart à l'exemple littéral de Lazar : **à lui confirmer**.

## 3. Risques de non-neutralité qui restent

- Les vingt critères disent où ne pas loger le dommage : les réponses peuvent converger vers les rares lieux non notés. Atténué (« vraiment autre », critique croisée, classement par distance), non levé.
- Les faits 16 et 17 mettent la trajectoire en avant : attraction vers la classe 2 ; « cherche d'abord en classe 1 » atténue.
- Les règles exactes du fait 9 (champ perdu à la révision) et du fait 11 (texte hors champs) sont saillantes ; les critères 4 et 5 de la porte rattrapent un retour au mode « affaiblir les contrôles » ou un dommage hors du plan.
- Les longueurs du fait 10 peuvent tirer vers des modes logés dans un champ.
- La coupe déclarée du fait 4 peut faire deviner les familles ôtées ; les exclusions la couvrent.
- Le seuil de couverture écarte les modes propres aux 8 tâches surtout théoriques.
- Demander des modes pousse à en produire ; « aucun sur ce format » recevable et motivé atténue.

## 4. Neon et Carbon : pris, écarté

- **Pris** (souvent déjà dans la v6) : contrat d'interface exact avec liste de l'absent (les deux) ; grilles en contrainte (les deux) ; vérité du dommage spécifiée avec le mode (les deux) ; actes locaux et loi d'agrégation pour un modèle de huit milliards (Neon) ; deux consultations (les deux) ; volets « banc figé » et « extension » (Neon), devenus les classes ; pas de tableau (Neon ; GO-137) ; changements invisibles seuls avant G1 (les deux) ; plusieurs extraits et vérifications déterministes (Carbon ; GO-138) ; critères de porte (Neon, huit ; Carbon, sept) et quatre issues (Neon) ; double tri (Neon) ; non-recouvrement avec les modes scellés vérifié par la seule instance qui les garde (Neon) ; après la porte : séparation d'avec le jumeau honnête, équivalence des notes, épreuve de diffusion par substitution d'actions (Carbon).
- **Écarté** : un échantillon de plans honnêtes dans la question (ancrage, risque dit par Neon) ; une taxonomie à quotas qui inclut les canaux d'information (Carbon : oriente, et hors du travail) ; calcul de capacité de canal et analyse morphologique imposés aux concepteurs (Carbon) ; tout changement visible du banc avant G1 et la clause qui l'avancerait (contraires à GO-135) ; l'audit de fuite par moniteur témoin (aucun changement visible avant G1) ; l'affirmation de Carbon que le banc actuel suffit à plusieurs familles, gardée comme hypothèse rivale, non comme fait.

## 5. Fichiers ouverts

- Sur `origin/main` (`2cd13d45…`), par `git show` : `registres/go.md` (lignes de GO-2026-11-22-135 à -146, empreinte, lignes 821 à 825 ; recherche vide de la citation du 20 novembre) ; `docs/programme-controle-ia-v2.md` (titres, lignes 30 à 50 et 118 à 141) ; `docs/decisions/decision-N-053-v1.md`, `-N-054-v1.md`, `-N-056-v1.md`, `-N-060-v3.md`, `-N-062-v1.md` (entiers) ; `src/controle_ia/environnements/propositions.py`, `rubrique.py` (entiers), `extraction.py` (lignes 1 à 330), `juges.py` (lignes 1 à 13), `pilote_a.py` (lignes 1 à 140) ; `src/controle_ia/harnais/episode.py` (entier) ; `prereg/T0.5-pilote-config-v1.json` ; `docs/sources/invites-2606.08892-v1/invites/H1-classification.txt`, `H3.txt`, `H4.txt`, `H9.txt`, `I8.txt` (entiers) et la liste du dossier ; `donnees/t05-pilote-v1/taches-pilote-60-v1.json`, lu par programme : clés et nombres seulement, aucune cible affichée. Empreintes seules des 18 sources de la v6 à `37a5afed…` et à `2cd13d45…` ; noms seuls de `donnees/` et `docs/decisions/` ; état de l'arbre, trois derniers commits, liste des branches filtrée des branches `coffre/` et `cloisonnee-`. `CLAUDE.md`, reçu dans le contexte.
- **Exposition incidente à déclarer** : une recherche `git grep` de la citation du 20 novembre sur `registres` et `docs` a affiché une ligne de deux passations (`registres/passations/reprise-autre-compte-2026-11-20/`, la citation elle-même) et le début d'une ligne de `registres/audit-echanges-mere-01Qi7Gr3-v1/consignes-aux-filles.jsonl` ; rien d'autre n'en a été ouvert. Les lignes 1 à 140 de `pilote_a.py` et `episode.py` décrivent la capture des activations par le harnais (pas de moniteur) : rien n'en est repris.
- Bloc-notes : `protocole-x-fable/question-collisionneur-modes-sabotage-v6.md` ; `fable-entrees/` : les quatre pièces (question v5, question à Neon et Carbon, leurs deux réponses), entières.
- Non ouverts : `registres/etat.md`, passations, `diag/`, branches `coffre/*` et `runs/cloisonnee-*`, `scratchpad/branche/`, `coffre1/`, `neon/`, toute pièce de moniteur.

## 6. Réserves

- Routine de reprise (R14) non faite : sous-agent, et lecture de l'état et des passations exclue par la demande.
- Rien n'est scellé. Contre-lecture par un Opus neuf à faire (R2) sur les trois pièces ; la porte se scelle avant la course, avec l'empreinte de la question servie.
- Les sources 19 et 20 vivent dans un bloc-notes : à verser, avec leur empreinte, sur une branche du dépôt avant le service (R6).
- Le fait 10 reste rapporté ; la mère peut le compter sur les 180 trajectoires honnêtes.
- La consultation des attaques contre les moniteurs (GO-2026-11-22-136, -139) n'est pas écrite ici.

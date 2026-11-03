# Corrections du complément de validation après la concordance de conv-audit — v1

- Rédacteur : sous-agent de rédaction de session-depot (Opus 5.5). Je n'ai écrit ni la concordance, ni la contre-lecture,
  ni le brouillon 2, ni les corrections précédentes.
- Fait le 3 novembre 2026 ; en-tête du texte daté de 00:30 UTC, cette note écrite à 00:33 UTC (heures relevées par
  `date -u`). Arbre `/tmp/claude-0/-home-user/70605ed3-c649-5b49-861d-ab74970b173c/scratchpad/wt-complement-v1`, branche
  `prep/r1-complement-v1`, tête `c5293408`. Aucun commit, aucun `git fetch`, aucun fichier `.sha256` créé ni modifié,
  aucun réseau, aucun appel de modèle, aucune tâche planifiée créée. Rien n'a été ouvert sous `donnees/`, sous `diag/`
  ni sous `runs/`, et aucune branche `calcul/…` n'a été lue. Fichiers touchés : le texte (en place, même nom, non
  scellé), cette note et le patch compagnon. Commandes de lecture sous `nice -n 10`.
- Texte : `prereg/R1-addendum-relance-v2-complement-validation-v1.md`.
  - Version lue par la concordance : `b5afc8b6e67622c04bebfee1315bb3e4602fe3e8c848d39344f8073d799e65ae`, vérifiée par
    `sha256sum` avant toute modification ; objet git `7fa15fda`.
  - Version corrigée : `4c083453c4df6a922d16f4e6e299c31e14906c97afe9418d1f21c947dd4f53da` ; objet git `586ff973`.
- Concordance appliquée : `concordance-complement-validation-v1.md`
  (`f4da389b80091dd6b3c4b511f270fe8243bcf2c68653afad04516c52b46a02c3`, vérifiée), lue en entier.
- Différence de `b5afc8b6…` à la version corrigée : `corrections-apres-concordance-v1.patch`
  (`c93dfc355304ed05e348e847717faa3a1e5b1650d9ceaefd592b988681cb4713`). Le patch est égal à `git diff` du texte et compte
  12 blocs, 165 insertions et 54 suppressions. C'est la différence que conv-audit vérifie (C-9).
- Vérifications :
  - `problemes()` rend `['section vide ou à remplir : Contre-lecture']`, et rien d'autre.
  - Sur une copie jetable (bloc-notes, effacée ensuite) où le marqueur est rempli, `problemes()` rend `[]`, et la
    section ne contient aucune entrée « Contre-lecture k ».
  - Le texte garde un seul « À REMPLIR » et aucun marqueur de gabarit.
  - Chaque libellé que lisent le script et le code est cité une seule fois : « Tests attendus », chemin de la
    configuration et les deux empreintes canoniques.
  - Le commit cité reste `c2a8b6e1…` (premier motif `Commit du code d'analyse`). L'entropie est inchangée.
  - Aucun jeton : seuls des « … » apparaissent.

## Tableau point par point

Lignes : numéros de la version corrigée (`4c083453…`).

| Point | Lignes | Ce qui est écrit |
|---|---|---|
| En-tête | 4 ; 9-11 | Statut : « version corrigée après la contre-lecture et la concordance de conv-audit, non scellée ». Date : `2026-11-03 00:30` (`date -u`). Rappel de la version lue par la concordance (`b5afc8b6…`, 23:20 UTC) et de la version contre-lue (`3b7955f1…`, 19:44 UTC) |
| C-1 (a) P-C7 | 621-623 (« Fusion », point 17) ; 673 (« Contre-lecture ») | Borne haute de l'étape 0 relevée de ≈ 24 h à ≈ 28 h par session-depot, après le rédacteur des corrections, sans être déclarée alors. Changement alignée sur le cas « Haut », fait avant tout scellement, sans aucune lecture. « Étape 0 seule » depuis la concordance |
| C-1 (b) clause de l'arbre gelé | 30-33 (remise) ; 624-626 (point 18) ; 673-674 | Clause remise sous « Commit du code d'analyse » : « arbre gelé identique à celui de `0e2a88718f4249e556e159f45f2df38ac304331e`, commit du code cité par la v2 : `git diff --quiet` sur les chemins gelés, ceux de « Plan d'analyse », rend 0 ». Elle couvre aussi les modules qu'importe le cœur, hors des quatre empreintes. Vérifiée avant de la remettre (voir plus bas) |
| C-1 (c) point 5 | 589-593 | La correction 1 compare le statut et les identifiants, et éprouve la répétabilité (les 3 de C-6 comparés aussi à la résolution du 2 novembre). La 2 dit quels retours ne mettent pas les comptes à jour, et écrit « pas comptés du chemin retenu » au lieu de « balayages du chemin retenu ». La 3 ajoute « durée : », « atteinte » et « 363,86 s sur 600 ». Il est écrit que le brouillon 2 citait déjà les l. 716-717 et 774-781 |
| C-1 (d) perte | 629-636 | « Rien du fond du brouillon 2 n'est contredit. » Puis : **une chose est perdue**, la sauvegarde des épisodes consignés à l'arrêt de dépense. La voie `TERM` du brouillon 2 les faisait committer et pousser ; elle est retirée faute d'accès au conteneur (point 3). Une destruction pendant l'étape validation perd donc toute la validation. La déclaration de complétude est aussi rendue exacte pour le point 15 de la contre-lecture, de forme et listé nulle part (concordance, § 1.a, ligne 15) |
| C-1 (e) note précédente | 647-649 | La note précédente appelle « version corrigée » `294a030c…`, celle du rédacteur, avant le changement de P-C7. Le patch précédent, égal à `git diff 2764e6cc c5293408`, mène à `b5afc8b6…` |
| C-2 HC-2 | 168-170 ; 596-597 (« Fusion », point 7) | Pour les 7 de la résolution rejouée, HC-2 ne dit plus que ce que lisent la métrique (« résolution rejouée ») et les critères (ligne « Résolution rejouée 7 sur 7 ») : empreintes retrouvées, identifiants égaux à ceux du 2 novembre, contrôle croisé « conforme ». Le point 7 de « Fusion » le dit |
| C-3 armement | 386-389 ; 390-403 (i) ; 404-416 (ii) ; 417-431 (« Armement ») ; 299-302 (« Plan d'analyse ») | Les deux tâches ouvrent chacune une session neuve à chaque départ. (1) Avant la création, elles sont créées avec un prompt sans identifiant d'instance ; parti tel quel, ce prompt ne détruit rien et alerte. (2) Aussitôt l'instance créée, `T0` est relevé par `date -u`. L'identifiant, `T0` et `T0 + H` sont écrits dans `registres/depenses.md` et poussés. Les prompts sont remplacés par leur version armée (identifiant exact, `T0`, prix horaire, disque, heure de destruction) et (ii) est programmée à `T0 + H`. (3) Second listing : chaque tâche est relue par son identifiant ; l'identifiant, `T0` et l'heure de départ de (ii) sont contrôlés et le constat consigné. (4) Si (2) ou (3) échoue, ou manque à 10 minutes : destruction immédiate par identifiant, consignée, lecture écrite. (5) Chaque tâche ne détruit que par l'identifiant de son prompt, jamais par étiquette ni par motif ; (i) alerte par notification et consigne. Formule `H` inchangée |
| C-4 épreuves R5 | 295-297 (`merge-base`) ; 432-444 ; 381-385 (arrêts) | Quatre épreuves des tâches, faites par session-depot avant la création, chacune consignée dans `registres/decisions.md` : destruction en cas sain (identifiant absent, par exemple 58851293 : rien n'est détruit, compte rendu) ; destruction en artefact (prompt sans identifiant : refus et alerte) ; vérification horaire en cas sain (≈ 1,79 USD sur 58851293 : rien) ; vérification horaire en artefact (dépense fictive au-dessus de 30 USD : alerte ; prompt sans identifiant ou sans prix : échec visible). Artefact de `merge-base` : `C` = `c2a8b6e1…` doit rendre 1. L'instance n'est créée qu'après ces épreuves conformes. Une épreuve non conforme ou non consignée est un arrêt avant la création |
| C-5 lecture aveugle | 445-451 ; 393-398 ; 363-364 (critères) ; 367 ; 493-498 | Journal lu par `vastai logs <identifiant>`, masqué. Un filtre ne garde que les lignes `AMORCE` et, des lignes de progression, l'heure, `etape=` et `episodes=` ; ni `resolus=`, ni `passes=`, ni `lecture=`. L'alerte et la demande d'extension ne portent que la dépense, la durée de vie, le prix horaire, l'heure de destruction et la durée prévue par le devis (« épisodes faits, d'après les lignes de progression » est retiré). Après une destruction, le journal n'est lu pour aucun compte. Ligne neuve aux critères : une destruction après la validation se lit « non éprouvé (dépense) », la résolution en cours de résolution, sans réserve sur la reproductibilité |
| C-6 devis | 199 (P-C7) ; 488 (« Central ») ; 489 (« Haut ») ; 493-494 | P-C7 : « (cas « Haut » à la borne haute de la durée par épisode, ≈ 9 difficiles ; étape 0 seule) ». « Central » : somme ≈ 10,9 h, **≈ 11 h (10,9 h)**, **≈ 15 USD (≈ 13)**. « Haut » : « à la borne haute de la durée par épisode » (≈ 9 difficiles, nombre attendu d'épisodes à deux bascules ou plus) ; « sous le point de destruction » à 1,187 USD/h vaut pour ces ≈ 9 seulement. Cas à ≈ 11 difficiles chiffré : ≈ 34,5 h, ≈ 48 USD (≈ 41), au-delà du point de destruction aux deux prix |
| C-7 nœud | 502-524 | Enjeu : « **au moins** ≈ 258 à 305 USD … **puis sans borne** » (boucle de redémarrage), « n'est donc qu'un plancher ». Mode commun : planificateur, compte et clé partagés (brief de reprise v2 de conv-audit, § 9.1). Option (a) : le crédit borne **tout le compte**, partagé avec d'autres sessions et projets de Lazar (douze instances « R6 » à 8,90 USD/h le 2 novembre, R-1051) ; (a) suppose aucune autre instance pendant la course, ou un crédit à la somme des plafonds concurrents. Option (b) : plancher, puis sans borne. Recommandation (a), confiance ≈ 0,8, inchangée ; aucun défaut ; décision de Lazar |
| C-8 extension | 410-414 ; 394-396 ; 493-497 | Sur GO étendu : (ii) reportée à `T0 + H′`, où `H′` est `H` recalculé sur `P′ − 0,5 USD`. Seuils de (i) relevés de même : alerte à `P′ − 10 USD`, destruction à `P′ − 0,5 USD`. Valeurs écrites dans `registres/depenses.md`, portées aux prompts et relues. La demande d'extension part dès que la durée projetée dépasse l'heure de destruction, à toute vérification, sans attendre 30 USD |
| C-9 portée | 692 ; 694-698 | La version scellée ne diffère de `b5afc8b6…` que par C-1 à C-8, le marqueur rempli et l'en-tête. Phrase finale mise d'accord : concordance rendue sur `b5afc8b6…` ; avant le lancement, conv-audit vérifie la différence avec la version scellée, que donne session-depot. Le marqueur « À REMPLIR » est laissé |
| « Contre-lecture » | 667-692 | Entrée « Concordance de conv-audit (`f4da389b…`) sur `b5afc8b6…` : concordant si le texte change avant son scellement », avec C-1 à C-9, une ligne chacune, et renvoi à cette note et au patch |

## Choix faits, et pourquoi

1. **C-2 : restreindre HC-2** pour les 7, plutôt que l'outiller. C'est l'option la plus sobre. Elle est lisible sans code
   neuf : la métrique et le critère existants lisent déjà empreintes, identifiants et contrôle croisé. Elle n'exige aucune
   pièce neuve à citer ni aucune ligne de critère neuve. L'autre option était faisable sans code : la résolution écrit
   `voie`, `forcages` et `combinaisons_essayees` par épisode et cite son tableau des pas (`pas_fichier`, `pas_sha256`,
   cœur l. 1596-1598 et 1628-1673). Elle aurait demandé une métrique, une ligne de critère et une pièce de plus.
2. **C-1 (b) : clause remise**, non expliquée par un retrait. Elle est vraie, et elle couvre ce que les quatre empreintes
   ne couvrent pas (les modules qu'importe le cœur). Je l'ai écrite avec le commit `0e2a8871` en entier, hors du libellé
   `Commit du code d'analyse : \``. La garde `exiger_code_cite` lit le premier motif de ce libellé (`validation_reelle.py`,
   l. 68 et 217), qui reste `c2a8b6e1…`.
3. **C-3 : armement**, écrit dans l'ordre de la consigne, plus deux ajouts.
   - **Ajout 1** : écriture de l'identifiant, de `T0` et de `T0 + H` dans `registres/depenses.md`, puis poussée, à l'étape
     (2). La concordance le demande (« écrits, poussés et donnés aux deux tâches »). Conséquence : une poussée en échec fait
     échouer (2), donc détruire l'instance avant tout calcul (perte : quelques minutes d'instance).
   - **Ajout 2** : contrôle, au second listing, que (ii) part à `T0 + H`.
   - Lecture de la destruction (4), écrite : rien n'a tourné. La branche de sortie, poussée avant l'installation
     (script l. 190-194), ferait refuser un second lancement sous ce texte par la commande `ls-remote`.
   - Formule `H` inchangée, comme demandé. Je n'ai donc pas appliqué le facultatif de C-8 (disque compté comme prix
     horaire dans `H`, frais de trafic).
4. **C-4 : épreuves sur des tâches d'essai de même forme**, retirées ensuite, plutôt que sur les deux tâches elles-mêmes.
   Leur mécanisme est le même : session neuve, départ dans quelques minutes, prompt de même forme marqué « essai ».
   - Ainsi les deux tâches de la garde ne sont jamais déplacées ni réécrites pour l'essai.
   - Toutes les épreuves portent un identifiant absent du compte (58851293). Le texte interdit qu'une épreuve porte
     l'identifiant d'une instance présente.
   - L'artefact de la vérification horaire est une dépense fictive au-dessus de 30 USD, comme le dit la consigne. J'y ai
     joint l'artefact de la concordance (prompt sans identifiant ou sans prix : échec visible).
5. **C-5 : `episodes=` gardé** dans le filtre, comme l'écrit la concordance. Ce champ et l'heure ne disent aucun résultat ;
   ils nourrissent la seule durée de vie projetée, qui déclenche la demande d'extension (C-8). La demande et l'alerte n'en
   portent rien : elles ne contiennent que la dépense, la durée de vie, le prix, l'heure de destruction et la durée prévue
   par le devis. `resolus=`, `passes=` (lié à la difficulté) et `lecture=` (ligne de fin d'étape, cœur l. 1700) sont
   exclus.
   - Aux critères : une destruction après la validation se lit « non éprouvé (dépense) » pour ce que le script n'a pas
     poussé : la résolution si la destruction tombe pendant la résolution, le lot ou la table si elle tombe plus tard. Un
     arrêt de dépense n'entraîne aucune réserve sur la reproductibilité. La concordance ne nommait que « pendant la
     résolution ou la table » ; le découpage suit les poussées du script, faites en fin de chaque étape (l. 388-395,
     441-447).
6. **C-6 : les deux options de la concordance appliquées.** Le libellé du cas « Haut » est corrigé. Le cas à ≈ 11
   difficiles est chiffré dans la même case, parce que « sous le point de destruction » ne vaut que pour 9. P-C7 garde
   ≈ 28 h, qui correspond au cas à 9. Changer ce chiffre aurait changé une prédiction, ce que ni la concordance ni la
   consigne ne demandent.
7. **C-7 : sources.** R-1051, et non n295 : n295 n'est pas sur disque, donc non vérifiable ici. Le mode commun est sourcé
   par le brief de reprise v2 de conv-audit, § 9.1.
8. **C-8 : seuils relevés « de même »**, lus comme le même écart sous le plafond étendu (`P′ − 10` et `P′ − 0,5` USD,
   comme 30 et 39,5 sous 40). Le texte le dit en clair.
9. **C-9 : ligne « Lancement » de la liste d'arrêt laissée telle quelle.** Elle dit « concordance de conv-audit », ce qui
   reste vrai. La concordance ne nomme que les lignes 586-587, et la consigne interdit tout autre changement.

## Vérifications rejouées pour ce texte (lecture seule, sans `fetch`)

- `git diff --quiet 0e2a8871 c2a8b6e1 -- src scripts tests` rend **0**. Avec les exclusions de « Plan d'analyse », il rend
  aussi **0**. `git rev-parse 0e2a8871` donne `0e2a88718f4249e556e159f45f2df38ac304331e`. La v2 cite ce commit comme code
  d'analyse (l. 48, texte `9d17d640…`, égal à son compagnon).
- `git diff --quiet c2a8b6e1 c5293408` sur les chemins gelés rend **0**.
- Artefact : `git merge-base --is-ancestor ab808842… c2a8b6e1…` rend **1**. Cas sain : `… c5293408…` rend **0**.
- Le patch précédent est égal à `git diff 2764e6cc c5293408` sur le texte : index `b0992133..7fa15fda`, 157 insertions et
  44 suppressions ; l'objet `7fa15fda` est le texte `b5afc8b6…`.
- `registres/depenses.md` de `b1d911b5` (`d398fa08…`), l. 321-322 : instance 58851293, vie 16:42:40 → 18:13:07 UTC,
  1,187 USD/h, ≈ 1,79 USD plus le disque. Recalcul : 1,789 USD.
- `registres/arrets.md` de `b1d911b5` (`e14b089d…`), l. 74 : 58851293 détruite par identifiant, absente de
  `vastai show instances` à 18:13:07.
- `registres/passations/2026-10-12-0812.md` (`77e77d4a…`), l. 88 : `vastai logs <id> --tail 200`, masqué (valeurs de
  HF_TOKEN, CONTROLE_IA_GITHUB_TOKEN, GH_TOKEN et VAST_API_KEY remplacées par « *** »).
- Brief de reprise v2 de conv-audit, objet `origin/canal/conv-audit-n04:registres/passations/2026-11-02-2234-brief-reprise-conv-audit-nouvelle-instance-v2.md`
  (`f87961f6…`, égal à l'empreinte de la concordance), l. 358-359 : tâches planifiées de l'ancien compte, « inutilisables
  depuis le nouveau compte ».
- `registres/decisions.md` d'`origin/main` local (`076e107d`), l. 1279-1280 : R-1051 (douze instances « R6 » d'une autre
  session, 8,90 USD/h) et R-1052 (recharge automatique sous 5 USD).
- Script : poussée initiale de la branche avant l'installation, l. 190-194. Code : lignes de progression,
  `etape=… episodes=k/n resolus=… passes=…` (cœur l. 1574-1576) et `etape=fin resolus=… lecture=…` (l. 1700) ;
  fonction `progres`, `rejeu_activations_v1.py` l. 533-537. Champs par épisode et tableau des pas de chaque étape, cœur
  l. 1596-1598 et 1628-1640.
- Chiffres de C-6, recalculés sur les composantes du devis.
  - « Central » : 4,6 × 1,1 + 3,4 + 1,4 + 1 = 10,86 h, soit 15,2 USD au prix plafond et 12,9 USD à 1,187 USD/h.
  - « Haut », 9 difficiles : 29,56 h, soit 41,4 USD au prix plafond et 35,1 USD à 1,187 USD/h.
  - « Haut », 11 difficiles : 34,55 h, soit 48,4 USD au prix plafond et 41,0 USD à 1,187 USD/h.
  - Points de destruction : 27,96 h au prix plafond et 33,03 h à 1,187 USD/h.

## Ce que je n'ai pas pu vérifier, et réserves

1. **P-C6** prédit encore « résolution 7 sur 7 **par les mêmes voies** ». Après la restriction de HC-2 (C-2), aucune
   métrique ne lit la voie des 7. C'était déjà le cas dans `b5afc8b6…`, et la concordance ne l'a pas relevé. Je l'ai
   laissé, puisque C-9 interdit tout autre changement. Si session-depot veut la cohérence complète, la voie la plus
   simple est d'étendre la ligne « répétabilité du chemin » aux 7, sans code : les champs sont dans `674825453a…` et dans
   le résultat neuf.
2. **Mécanique des tâches planifiées** (session neuve à chaque départ, remplacement d'un prompt, relecture d'une tâche par
   son identifiant, programmation de (ii) à `T0 + H`, notification) : écrite d'après la consigne. Elle n'est éprouvée
   nulle part ici, puisque aucune tâche ne devait être créée. Les épreuves de C-4 sont là pour l'éprouver avant la
   création.
3. **Arrêt de l'instance par le fournisseur quand le crédit est épuisé** (inconvénient de l'option (a)) : non éprouvé,
   comme le dit déjà le texte.
4. **Absence d'instance sur le compte pendant la course** (prémisse de l'option (a)) : non vérifiable ici, sans réseau ni
   `vastai`.
5. **n295** (`/home/claude/lectures/session-depot_2026-11-02_n295.md`) : absente du disque. Je ne l'ai donc pas citée.
   L'annonce de la relance de R1 sous GO-27 sur le même compte, que la concordance en tire, n'est pas dans le texte.
6. **Version de `registres/decisions.md`** : l'`origin/main` local est à `076e107d` (fichier `2ebc3a9f…`), non à
   `f38ae717` (`5b347195…`) comme dans la concordance. Les lignes 1279-1280 portent les mêmes décisions R-1051 et R-1052.
   Le texte cite R-1051 par son identifiant.
7. **`ls-remote`** de la branche de sortie : non rejoué (réseau interdit).
8. **Facultatif de C-8** (disque compté comme prix horaire, frais de trafic) : non appliqué, puisque la consigne garde la
   formule `H`. La concordance dit ces frais couverts par la marge de 0,5 USD et de 15 minutes (§ 2.f) ; je ne l'ai pas
   vérifié.

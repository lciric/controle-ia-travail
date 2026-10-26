# Texte de course — deux courses à question de la v6.2.1 sur la banque `confrontation-v3` : « maieutique » (hypothèses testables du paradigme maïeutique hors format × contexte) puis « audit » (audit défensif du programme, version « organismes »), rondes de conception arrêtées par l'organisme, puis quatre générations notées, en segments — v1

**Statut** : v1, écrite par la lignée conv-audit le 26 octobre 2026 à partir de 11:40 UTC (heures lues sur `date -u`), sur
les mots directs de Lazar dans la session de session-depot vers 11:13 UTC (R-509, § Décisions) et sa demande n° 70.
**Pilote de conception** (R-473) : ni préenregistrement ni scellement au sens de R1 ; la relecture est gardée
(contre-lecture 9, § Contre-lecture) ; le script `sceller_courses_question_v6.py` n'y écrit que l'entropie, les deux
graines et l'empreinte des pièces, que le lanceur relit. **Texte différentiel sur la v5 du pilote 4**
(`pilote4-gemini-organisme-v5.md`, `1943f39ada61db7d21e53b7e0c02c6e826b86e1467687eedbe56617877ab7f87`, tête `067b41d` de
`outils/pilote4-gemini-travail`), elle-même différentielle sur la v4 et P4v3 : tout ce que ce texte ne dit pas est la v5
(objet v6.2.1 et son code, banque v3 et ses références, noyau `8e5e2f7b` — ici `9beee10b`, qui n'en diffère que par la
borne de la question ouverte, voir la table —, bornes, segments et reprise, canaux, clés,
point 4 bis), appliqué selon la table de correspondance ci-dessous ; en cas de conflit, ce texte prévaut. **Ce ne sont pas
des courses du pilote 4** : le pilote 4 (courses M et S) est fini et fermé (R-494, R-498) ; ces deux courses n'entrent ni
dans sa lecture, ni dans sa boucle extérieure, ni dans aucune famille de tests ; leur livrable est la réponse de
l'organisme à la question servie à la génération 1. Lanceur : lignée session-depot (clés), dans son conteneur.

**Ce qui a été lu avant ce texte.** Ce que la v5 déclare ; les lignes R-493 à R-510, GO-2026-10-26-04 et
GO-2026-10-26-05 de `main` (jusqu'à `eb03bad`) ; les messages n° 65 à 70 de session-depot ; les faits mécaniques des
courses M et S publiés en R-494 et R-498 (aucun score) ; les titres et le résumé de l'audit de littérature de session-depot
(R-508) et la note N-053 ; le lot B de l'audit des failles de conv-audit (failles internes FI-01 et FI-02 lues en
entier, les autres au titre). **Aucun score d'aucune course n'a été lu par conv-audit** ; les scores de `test` du pilote 4,
ouverts à la lecture depuis « graines : c » (09:07 UTC), restent non lus par cette lignée tant qu'elle écrit les règles de
la boucle (protocole, § 2). Les deux questions servies n'ont pas été lues par conv-audit : seules leurs empreintes,
leurs chemins et leurs tailles le sont.

## Décisions de Lazar

Relevé verbatim en R-509 (session de session-depot, vers 11:13 UTC, en réponse au message de R-508) :
- « le croisement format × contexte, : demande al'org de chercher d'autres hypotheses testable sur le paradigme
  maieutique et esprit de finesse que ca » → **course « maieutique »**, GO-2026-10-26-05 (75 USD au plus, bornes du
  pilote 4), question `question-hypotheses-maieutique-organismes-v1.md` écrite et scellée par session-depot (R-510).
- « La partie à plusieurs modèles de l'audit (collisionneur, puis organisme) : go » → **course « audit »**,
  GO-2026-10-26-04 partie (2) (75 USD au plus), question `question-audit-controle-organismes-v1.md` (R-510), **après** le
  tour du collisionneur sur la même question (parti à 11:18 UTC) et **seulement s'il n'a essuyé aucun refus** ; avec une
  garde qui arrête la course au premier refus d'un appel qui porte la question (consigne gelée, R-484 à R-487 : une
  question refusée n'est jamais reposée sous d'autres rôles) ; trois pièces lisibles par l'organisme (programme v2, audit
  de littérature, N-053).
- Dans la session de conv-audit, 11:26 heure de Paris : ordre « (b) puis (a) puis (c) » ; « je veux que l'organisme
  cherche mes failles après moissonnage de la littérature la plus récente et grise, et ensuite qu'il imagine de nouvelles
  failles non couvertes par notre système de contrôle, et comment les contrecarrer ». La course « audit » est ce (c).

## Table de correspondance avec la v5

| dans la v5 | pour ce texte |
|---|---|
| deux courses du même objet, M puis S ; clés `v6-2`, `v6-2-s` ; noms `pilote4-gemini-v6-2-v1`, `pilote4-gemini-v6-2-s-v1` ; lignées `gemini-organisme-v6-2`, `gemini-organisme-v6-2-s` | **deux courses du même objet**, la v6.2.1 (commit `7ea32705c5437d91ed071dd95fb3209bb0b0035e`, arbre `4f13647a7070b3941b660d60c428620df6b4e0e31cea1d2c63d71b8606e6214d`, 26 fichiers) : clé `maieutique`, nom `course-maieutique-gemini-v6-2-v1`, lignée `gemini-organisme-v6-2-maieutique` ; clé `audit`, nom `course-audit-gemini-v6-2-v1`, lignée `gemini-organisme-v6-2-audit` ; les clés `v6-2` et `v6-2-s` sont refusées par le lanceur v12, en réel comme en simulation |
| question M (`8b1c7511…`), question S (`a54da93e…`, commit `4772b525` du canal) | **question « maieutique »** : `brouillons/questions-organismes-20261026-v1/question-hypotheses-maieutique-organismes-v1.md`, `1d29fbecd52b1dfc94410e117f786811067f86f3cce24c4c54bbe424e480e3a3`, 3 009 octets ; **question « audit »** : `brouillons/questions-organismes-20261026-v1/question-audit-controle-organismes-v3.md`, `998960b8d101d5013c498d6fcf225277ba17d20741825ad136381892c05cfd0e`, au commit `ad23e9ae07588ed701a70b9b5f4bf379ca079953` de `main` (R-518 : elle remplace la v2 `ec3abf28…` de R-516, elle-même retournée vers le rapport consolidé de Lazar du 26 octobre, R-515 ; la v3 vise la version 2 du rapport, failles E à I comprises) ; la question « maieutique » au commit `eb03bad56ece1e755afa5e264948d0c44416f6cc` de `main` (R-510) ; toutes deux extraites et vérifiées par le lanceur ; servies à la génération 1 (cibles `g001`), réponse archivée `reponse-question-g001.md`, sans effet sur le score (essai du noyau, v5) |
| la question servie est le seul texte | **pour la course « audit » seulement, une annexe** servie avec la question, dans le même fichier `question.md` (question, puis une ligne `---`, un titre `# Annexe 1 — <chemin> (sha256 <empreinte>)` et son contenu) : **la transcription expurgée, version 2, du rapport consolidé de Lazar du 26 octobre** : `docs/sources/rapport-consolide-20261026/transcription-expurgee-v2.md`, `c1237687e98db14475336af690986bc08800a85e259d249de4940130245b1a64`, 37 563 octets, au commit `ad23e9ae07588ed701a70b9b5f4bf379ca079953` de `main` (R-518 ; PDF confidentiel de 10 pages, empreinte `14a79c55…`, hors dépôt : 23 retraits, montants, financeur et soumission ; parties 1 et 2 reprises de la v1 `d9e1be59…` vérifiée page par page par session-depot, R-517 ; partie 3 transcrite par session-depot sur le rendu des pages 7 à 10 et concordante, formule par formule et chiffre par chiffre, avec la transcription indépendante de conv-audit, `6205c68a…`, canal n° 88), vérifiée par le lanceur (empreinte, puis taille : question et annexe sous `CARACTERES_MAX_QUESTION = 100 000` du noyau `9beee10b`) ; les trois annexes prévues au n° 70 (programme v2, audit de littérature, N-053) ne sont plus servies (R-516). L'empreinte de la question de base reste celle de la ligne de GO et du `LANCEMENT.md` ; une ligne `- question servie : question.md, sha256 …, N caractères` s'y ajoute. Le lot B de l'audit de conv-audit **n'entre pas** dans les pièces servies (anti-enfermement : l'organisme ne reçoit pas nos propres réponses au-delà de ce que Lazar a nommé ; le lot B n'est pas contre-lu). La question « maieutique » est servie seule |
| porte « course M précédente » (la course S après la course M du pilote 4) | **retirée** : rien n'est exigé des courses du pilote 4 ; la porte « course M de référence » (second pilote, `REFERENCE_M`, empreintes de M `5ae4e801423bbef0…`) est gardée telle quelle |
| lanceur v11 (`21854b79…`), batterie v13, série v14 | **lanceur v12** `lancer_courses_question_v12.sh` ([[LANCEUR_SHA]]), dérivé du v11 par remplacements exacts au nombre attendu (`deriver_lanceur_question_v12.py`, écart `diff-lanceur-v11-vers-v12.txt`) : clés, noms, lignées, questions, annexes, porte retirée, ligne de dépense, **garde « refus-question »** (§ Liste d'arrêt) ; rien d'autre ; **batterie v14** `essais_lanceur_question_v14.sh` ([[BATTERIE_SHA]]) ; **série v15** (§ Essais) |
| graines `v6-2-s` (enfant 0) et `v6-2` (restituée) | entropie de ce texte et **deux graines** : `maieutique` = enfant 0, `audit` = enfant 1 de `SeedSequence(E).spawn(2)` (§ Plan, point 2) ; aucune graine héritée |
| ligne d'extension de GO-2026-10-25-02 ; ligne de dépense avec les empreintes de M et de la v6.2 | une **ligne d'extension par GO** (05 pour « maieutique », 04 pour « audit », § Plan, point 1) ; ligne de dépense `| <date du jour> | <nom> | <GO> | 75 USD au pire cas | empreintes de M 5ae4e801423bbef0 |` |
| `sceller_pilote4_v5.py`, `EMPREINTES-pilote4-gemini-v3.txt` | **`sceller_courses_question_v6.py`**, **`EMPREINTES-courses-question-v1.txt`** (§ Pièces) |
| lecture : `test` dès la fin de chaque course, `test_final` une fois en fin de compteur (N-050) ; boucle extérieure | **aucune lecture de `test_final`, jamais** : ces courses ne portent aucune hypothèse de score et n'entrent dans aucune famille de tests ; le script de lecture ne s'exécute pas sur elles (une version qui accepte leurs noms serait nécessaire) ; si Lazar veut leurs scores de `test`, il le dit ; la partie « conception de classifieurs » de chaque course relit la part `test` de la banque v3 (deux lectures de plus par des organismes, après celles du pilote 4 : N-049, tâches fraîches, vaut à partir du pilote 5 ; c'est l'ordre de Lazar) ; **le livrable est `reponse-question-g001.md`** (et, dans l'archive, les contributions des castes), lisible par Lazar et session-depot dès la fermeture : il ne porte aucun score ; celui de la course « audit » reste dans le dépôt privé, hors de la copie expurgée, et n'est servi à aucun organisme |
| devis : 75 USD par course, 150 pour les deux, sur GO-2026-10-25-02 | 75 USD au plus par course, chacune sur son GO (05 ; 04 partie (2)) ; attendu environ 31 USD par course (R-494, R-498) |
| « aucune comparaison entre les deux courses » | sans objet pour les scores (non lus) ; les deux réponses sont deux pièces, à deux questions |

## Plan

1. **Ordre et lancement.** La course « maieutique » d'abord ; la course « audit » ensuite, si ses deux conditions tiennent
   (§ Liste d'arrêt) ; jamais les deux en même temps (même clé). Chacune en un ou plusieurs segments (3 400 s, STOP et
   reprise, comme la v5). **Copie de lancement** : celle de session-depot, dont la tête passe à la tête de
   `outils/pilote4-gemini-travail` citée au message de départ (`git fetch origin outils/pilote4-gemini-travail main` —
   `main` porte les commits des questions (`eb03bad5`, `ad23e9ae`) et celui de la transcription expurgée v2 (`ad23e9ae`) —, puis `git checkout --detach` de cette tête) ; cette
   tête ne diffère de `8e5e2f7b` que par les chemins permis et par la borne de la question ouverte (`CARACTERES_MAX_QUESTION` 20 000 → 100 000, commit `9beee10b`, seul changement du noyau, essais passés) ; la copie n'est jamais committée ; les dossiers des courses du
   pilote 4, non suivis, restent en place. **Ligne d'extension de GO**, poussée sur `main` avant chaque course, de la forme
   exacte :
   `| GO-2026-10-26-05 | 2026-10-26 | calcul | extension : course « maieutique » (mot direct de Lazar, R-509) — la v6.2.1 7ea3270, arbre 4f13647a7070b3941b660d60c428620df6b4e0e31cea1d2c63d71b8606e6214d, sur la question question-hypotheses-maieutique-organismes-v1.md 1d29fbecd52b1dfc94410e117f786811067f86f3cce24c4c54bbe424e480e3a3 (commit eb03bad5) ; banque confrontation-v3 157a2b45a8d9fd88cc5dca2f483c2dc79457d781d44f9802b2c053f530c0011d ; texte courses-question-gemini-v6-2-v1.md <empreinte du texte> ; lanceur lancer_courses_question_v12.sh [[LANCEUR_SHA]], noyau 9beee10b (8e5e2f7b + chemins permis + borne de question 100 000) ; bornes du pilote 4 (4 générations, 6 rondes de conception au plus à 3 USD et 900 s chacune, 75 USD tous segments compris, jusqu'à 60 recherches, dont ≈ 10 web) ; segments : minuteur à 3 400 s, test de dépense et ligne de dépense à chaque segment ; garde refus-question | 75 USD au plus, inchangé | 2026-10-31 | Lazar | R-509 |`
   et, pour la course « audit » :
   `| GO-2026-10-26-04 | 2026-10-26 | calcul | extension : course « audit », partie (2) (mot direct de Lazar, R-509) — la v6.2.1 7ea3270, arbre 4f13647a7070b3941b660d60c428620df6b4e0e31cea1d2c63d71b8606e6214d, sur la question question-audit-controle-organismes-v3.md 998960b8d101d5013c498d6fcf225277ba17d20741825ad136381892c05cfd0e (commit ad23e9ae), servie avec une annexe, la transcription expurgée v2 du rapport consolidé de Lazar docs/sources/rapport-consolide-20261026/transcription-expurgee-v2.md c1237687e98db14475336af690986bc08800a85e259d249de4940130245b1a64 (commit ad23e9ae) ; banque confrontation-v3 157a2b45a8d9fd88cc5dca2f483c2dc79457d781d44f9802b2c053f530c0011d ; texte courses-question-gemini-v6-2-v1.md <empreinte du texte> ; lanceur lancer_courses_question_v12.sh [[LANCEUR_SHA]], noyau 9beee10b (8e5e2f7b + chemins permis + borne de question 100 000) ; mêmes bornes et segments que la course « maieutique » ; garde refus-question ; part seulement si le tour du collisionneur de la partie (1) n'a essuyé aucun refus | 10 USD (1) ; 75 USD au plus (2), inchangé | 2026-10-31 | Lazar | R-509 |`
   (l'empreinte entre chevrons est celle de ce texte à ses graines, que donne le message de départ). Session-depot les
   vérifie par les `grep` du lanceur (le GO, `calcul`, les 8 premiers caractères de la question de base, `4f13647a`, les 16
   premiers caractères de l'empreinte de ce texte) et par `157a2b45`. **Ligne de dépense** avant chaque course :
   `| <date du jour> | course-maieutique-gemini-v6-2-v1 | GO-2026-10-26-05 | 75 USD au pire cas | empreintes de M 5ae4e801423bbef0 |`
   puis `| <date du jour> | course-audit-gemini-v6-2-v1 | GO-2026-10-26-04 | 75 USD au pire cas | empreintes de M 5ae4e801423bbef0 |` ;
   segments K ≥ 2 : forme de la v4, mot pour mot, au nom de la course. Le message de départ recopie mot pour mot ces lignes,
   l'empreinte du texte remplie ; s'il en diffère, rien ne part.
2. **Graines (R9)** : entropie E = <<ENTROPIE>> tirée par `sceller_courses_question_v6.py` (`secrets.randbits(128)` ; refuse
   numpy < 1.25 et toute ligne d'entropie ou de graine de trop) ; deux enfants `numpy.random.SeedSequence(E).spawn(2)` ; la
   graine de chaque course vaut `int(enfant.generate_state(1, dtype=numpy.uint64)[0])`, enfant 0 pour « maieutique »,
   enfant 1 pour « audit » (chaque égalité sur une seule ligne, lue par le lanceur à chaque segment et recalculée depuis
   l'entropie de ce texte ; le lanceur lit la ligne de sa clé et vérifie que l'autre existe sans l'utiliser) :
   graine de la course maieutique = <<GRAINE_MAIEUTIQUE>>
   graine de la course audit = <<GRAINE_AUDIT>>
3. **Lecture et livrable** : table ci-dessus. À la fermeture de chaque course, session-depot pousse la liste fermée sur
   `pilotes/<nom>`, puis **copie `reponse-question-g001.md` et son compagnon** dans son message de retour (sans aucun autre
   fichier de la course) : c'est le livrable, pour Lazar. Rien d'autre n'est lu.
4. **Point 4 bis** : sans objet (aucune lecture de score).

## Liste d'arrêt

Celle de la v5, ligne à ligne, aux noms de ce texte (clés `maieutique`, `audit` ; lanceur v12 ; batterie v14), sans la
ligne de la porte « course M précédente », et en plus :

| condition | effet | garde ou vérification |
|---|---|---|
| **garde « refus-question »** (les deux courses) : un appel dont le rôle est l'un des rôles des castes de la question ouverte de la v6.2.1 (`monoculture_analytique`, `monoculture_croisee`, `sonde_orthogonale_onsager`, `critique_adversariale_limites`, `arbitre_synthese_contradictoire`) et dont le statut est `REFUS`, ou dont le champ `fin` porte une raison d'arrêt de sûreté (liste close tirée des conventions du noyau, écrite dans le lanceur) | **le noyau est tué sur-le-champ** (groupe de processus), la course est fermée sans reprise, la ligne `- arrêt par la garde refus-question : appel …, rôle …, statut …, fin … (<heure UTC>) ; course fermée sans reprise` est écrite au `LANCEMENT.md`, la liste fermée est poussée avec ce qui existe ; la question n'est reposée à personne ; Lazar décide de la suite (un refus sur un autre rôle ne fait rien) | veilleur de fond du lanceur v12, lecture du journal d'appels vivant de `g001` toutes les 2 s ; essais `garde-refus-question-sain`, `garde-refus-question-artefact` (série v15) |
| **course « audit »** : le tour du collisionneur sur la même question (GO-2026-10-26-04 partie (1)) a essuyé un refus, ou n'est pas fini | la course « audit » ne part pas ; Lazar décide | session-depot, avant la ligne d'extension (le lanceur ne le vérifie pas) |
| clé `v6-2` ou `v6-2-s` demandée au lanceur v12 ; ligne de GO sans la question de la clé, ou sans ce texte ; question ou annexe extraite d'empreinte autre que celles de la table ; annexe absente (course « audit ») | la course ne part pas | lanceur v12 (essais `cle-ancienne-refusee`, `go-autre-question`, `go-sans-texte`, `question-empreinte-autre`, `annexe-absente`, `annexe-alteree`) |
| les deux courses demandées en même temps | la seconde ne part pas | session-depot (même clé ; une course à la fois) |
| tête de la copie de lancement autre que celle du message de départ, ou dossier d'une course du pilote 4 déplacé ou modifié | la course ne part pas | session-depot (tête relue au `LANCEMENT.md`) ; lanceur v12 (`8e5e2f7b` ancêtre, code identique, `PERMIS_APRES_CODE`) |

## Essais du lanceur (R5)

Ceux de la v5 (série v14), sur la **batterie v14** (`essais_lanceur_question_v14.sh`, [[BATTERIE_SHA]]), dérivée de la
v13 par remplacements exacts au nombre attendu (`deriver_essais_question_v14.py`) ; cas adaptés aux deux clés, cas ajoutés
ou renommés : [[CAS_AJOUTES]]. **Série v15**, en simulation (faux appels aux espèces, aucune clé ; réseau seulement pour
le cas `passerelle-saine` et l'essai de moisson réelle du noyau sur arXiv ; aucune course ne tourne), batterie v14 sur le
lanceur v12 : [[SERIE_V15]] (`essais-lanceur-question-v15.log`, [[JOURNAL_SHA]]). La batterie efface le dossier `pilotes/`
de sa copie sous `/root` et y commet des essais : ses copies ne sont jamais la copie de lancement ni une copie qui porte
une course réelle. Lacunes déclarées : [[LACUNES]].

## Pièces

Celles de la v5 (fichier d'empreintes `EMPREINTES-pilote4-gemini-v3.txt`, `082edf4c…`, jamais réécrit), et en plus, sous
`prereg/pieces-pilote4-gemini/` : le **lanceur v12** `lancer_courses_question_v12.sh` ([[LANCEUR_SHA]]), sa dérivation
`deriver_lanceur_question_v12.py` et l'écart `diff-lanceur-v11-vers-v12.txt` ; la **batterie v14**
`essais_lanceur_question_v14.sh` et sa dérivation `deriver_essais_question_v14.py` ; le journal de la série v15
(`essais-lanceur-question-v15.log`, `.heures.txt`) ; `sceller_courses_question_v6.py` (le v5 aux marqueurs, au nom du
fichier d'empreintes et aux deux lignes de graine près ; essais `essais_scellement_question_v6.sh`) ; le brief du sous-agent
qui a dérivé le lanceur et la batterie et son LISEZMOI (`lanceur-v12-v1/`) ; les pièces de la contre-lecture 9
(`contre-lecture-9-v1/`) ; chacun avec son compagnon `.sha256`. Fichier d'empreintes de ce texte :
`EMPREINTES-courses-question-v1.txt` (toutes les pièces sous `pieces-pilote4-gemini/` et les contre-lectures
`courses-question-gemini-v6-2-v1-*`), empreinte <<EMPREINTE_PIECES>>, écrite par `sceller_courses_question_v6.py` avec
l'entropie et les graines ; vérifiée par `verifier_scellement_pilote4_v3.py` adapté ([[VERIFIER]]).

## Contre-lecture

- **Contre-lecture 9** (sous-agent neuf, sur ce texte avant ses graines ; avec le lanceur v12, son écart, la batterie v14,
  le journal de la série v15, le script des graines, les deux questions à leurs commits et la transcription expurgée) :
  [[CL9]].
- **Ce texte, à ses graines** garde le nom de la v1 ; de la version relue à lui, il porte en plus : la ligne de la
  contre-lecture 9 ci-dessus, le traitement de ses constats aux passages qu'il nomme, puis l'entropie, les deux graines et
  l'empreinte du fichier d'empreintes des pièces, écrites par `sceller_courses_question_v6.py` ; rien d'autre.

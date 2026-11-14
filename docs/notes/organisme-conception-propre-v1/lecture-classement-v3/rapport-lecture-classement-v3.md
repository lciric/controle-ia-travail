# Rapport — outil du lecteur v3 (lecteur Astra) et programme de classement v3, course « conception propre »

Développeur neuf, sous-agent de la session mère ; 14 novembre 2026, de 07:43 à 08:36 UTC (heures relevées par
`date -u`). Demande : R-2658 (échec de Kimi, `finish_reason = length`), R-2659 et R-2662 (mot de Lazar : lecteur =
Astra, `gpt-6-astra`, famille OpenAI ; outil v3 écrit par un développeur neuf, contre-lu par un autre modèle, devis avant
tout appel). **Aucun appel payant, aucune valeur de clé lue (présence vérifiée par le nom seul), aucune fiche ni aucun
témoin ouvert** (essais sur fiches factices ; les témoins épinglés ne sont lus que par les programmes, sous une racine
factice) ; rien sous `src/` ni `tests/` ; rien commité. La v2 (`../lecture-classement-v2/`) reste telle quelle (R12).

## Verdict

v3 écrite, essayée hors réseau et scellée. Essais : **123 passés** (`resultat-essais-lecture-classement-v3.txt`, 08:15 UTC) ;
banc : **129 mutants tués sur 129** à la seconde passe (une survivante à la première, tuée par un essai ajouté, § 4). **Non utilisable avant** : (1) la contre-lecture par un autre modèle ; (2) le prix d'Astra, **non lu** (pages
d'OpenAI hors des domaines de la session, `prix-astra-v1.md`) ; (3) la décision de Lazar sur le devis
(`devis-lecture-astra-v1.md` : au barème prudent 10 / 50 du dépôt, SUPPOSÉ, ≈ 17,3 USD attendus, au-dessus du reste de
la ligne, 14,21 USD).

## 1. Pièces (scellées ; empreintes dans les compagnons `.sha256`)

| Pièce | Rôle |
|---|---|
| `outil_lecteur_conception_propre_v3.py` | préparer, envoyer (relais en processus vers OpenAI), bilan, vérifier |
| `classer_conception_propre_v3.py` | classement (règle inchangée), entrées v3 |
| `differentiel-classer-v2-v3.diff` | différentiel entier du classement |
| `differentiel-outil-v2-v3.diff` | différentiel entier de l'outil (pour la contre-lecture) |
| `essais_lecture_classement_v3.py`, `resultat-essais-lecture-classement-v3.txt` | essais hors réseau, doublure déclarée de l'API |
| `mutations_lecture_classement_v3.py`, `resultat-mutations-lecture-classement-v3.json` (seconde passe), `resultat-mutations-lecture-classement-v3-passe1.json` | banc de mutations |
| `prix-astra-v1.md` | relevé de prix : page inaccessible, aucun prix lu |
| `devis-lecture-astra-v1.md` | devis en formule des prix, illustration au barème prudent |

## 2. Ce qui change par rapport à la v2, et pourquoi

### Outil (`outil_lecteur_conception_propre_v2.py` → `…_v3.py`)

| v2 | v3 | Pourquoi |
|---|---|---|
| `MODELE_LECTEUR = "kimi-k3.1-pro"`, corps au format du relais Kimi, envoi par `curl` de la mère vers le relais local | `gpt-6-astra` ; action `envoyer` : **relais en processus** vers `POST https://api.openai.com/v1/chat/completions`, un lot à la fois | R-2662 ; un seul processus tient la clé, la garde de dépense et le journal, sans serveur local à lancer et arrêter par PID |
| — | **Point d'entrée : Chat Completions**, pas Responses | (a) déjà employé avec `gpt-6-astra` dans le dépôt : appel réel R-1454 (modèle servi rendu `gpt-6-astra` exact, code 0), `collisionneur_v8.py`, dialecte `astra` du relais du pilote v70 ; (b) la réponse `chat.completion` porte `choices[0].finish_reason` : la garde « fin autre que `stop` » de la v2 s'applique telle quelle, sans traduire l'état `incomplete` de Responses ; (c) Responses garde les réponses chez le fournisseur par défaut (`store`), Chat Completions non, et `store: false` est écrit explicitement ; (d) aucun outil ni état de conversation n'est nécessaire. Réserve : documentation d'OpenAI non lue dans la session (r2) |
| corps `{model, messages, max_tokens}` | corps `{model, messages, max_completion_tokens: 32768, reasoning_effort, store: false}` | plafond de sortie (raisonnement compris) et effort **explicites**, consignés dans chaque corps et au manifeste (`lecteur`) ; `max_tokens` est l'ancien nom chez OpenAI |
| `TAILLE_LOT = 20` (lots de 14 ou 15 sur 43) | **`TAILLE_LOT = 5`** (9 lots de 5 ou 4 par lecture) | Kimi a passé plus de 32 765 jetons à raisonner sur 15 fiches sans rien rendre (R-2658), soit plus de 2 180 par fiche ; viser ≥ 5 000 jetons de raisonnement et ≈ 700 de sortie visible par fiche sous 32 768 donne 32 768 / 5 700 ≈ 5,7 → 5. Plus petit : préambule fixe (≈ 8 900 jetons) répété plus souvent et plus d'appels |
| `MAX_APPELS = 6` (relais), refus au-delà | **`MAX_APPELS = 18`**, fixé d'avance ; `appels_max` du manifeste = 2 × lots ; contrôlé à la préparation **et** avant chaque envoi | 43 fiches → 18 appels |
| `max_tokens` = part égale d'une réserve de 4 USD, refus sous 16 384 ; prix fixés dans le code (2 / 10) | **prix et plafond donnés à la préparation** (`--prix-entree`, `--prix-sortie`, `--prix-cache` facultatif, au prix d'entrée par défaut, `--source-prix` obligatoire, `--plafond-usd`), **scellés au manifeste**, relus par `envoyer` (aucune surcharge en ligne de commande) ; plafond ≤ `PLAFOND_ABSOLU_USD` = 14,20 (reste de la ligne) ; refus si un seul appel ne tient pas | le prix d'Astra n'est pas connu : aucun chiffre dans le code ; garde contre la faute de frappe |
| garde de dépense : somme des pires cas ≤ réserve, avant tout envoi | **garde dynamique** : avant chaque appel, dépense comptée + pire cas de l'appel (recalculé sur les octets envoyés) ≤ plafond, sinon arrêt sans envoi (événement `arret` au journal) ; après chaque appel, **coût lu dans `usage`** : (entrée − cache) × PE + cache × prix du cache + sortie × PS + excédent de `total_tokens` au prix le plus haut ; **au pire cas** si l'usage manque, est illisible ou incohérent (cache > entrée, raisonnement > sortie, sortie > plafond demandé) | au barème illustratif, la somme des 18 pires cas (≈ 38,5 USD) dépasse toute part possible de la ligne ; la garde dynamique borne la dépense au plafond quoi qu'il arrive |
| — | **journal de dépense chaîné** (`journal-depense-v3.jsonl` : chaque ligne porte l'empreinte de la précédente), relu à chaque reprise ; un envoi sans clôture (coupure, arrêt du processus) compte son pire cas et interdit la reprise ; chaque réponse ou erreur déposée doit avoir sa clôture conforme ; relevé scellé à chaque passe (`releve-depense-v3-<k>.json`) ; action `bilan` sans clé | un arrêt ne remet jamais le compte à zéro (R5 : aucun repli silencieux) |
| — | **arrêt au premier écart** à l'envoi : transport en échec, statut autre que 200, réponse illisible, usage absent ou incohérent, coût au-dessus du pire cas réservé, modèle servi différent, choix non unique, fin autre que `stop`, refus du lecteur, contenu absent ; puis toute reprise est refusée | leçon de R-2658 : le second lot était parti avant que la fin du premier soit lue ; la règle n'admet aucune relecture |
| modèle servi vérifié à la seule vérification (refus) | vérifié **à l'envoi** (égalité exacte, sinon anomalie et arrêt) **et à la vérification** (anomalie bloquante `modele_servi_different`, contenu non lu) | demande ; un nom servi daté (`gpt-6-astra-AAAA-MM-JJ`) est un écart |
| clé : jamais lue (la mère passait par le relais) | `OPENAI_API_KEY` lue **par son nom** dans `lire_cle` seule, **retirée** aussitôt de `os.environ`, posée dans l'en-tête et nulle part ailleurs ; masquée dans tout message d'exception ; adresse d'amont figée (`transport_reel` refuse toute autre adresse) | demande |
| — | **corps d'erreur jamais écrit** : fichier `erreur-<L>-lot<k>-v3.json` scellé avec statut, `type` et `code` de l'erreur (filtrés), empreinte et taille du corps | R-2645 : le corps d'un 429 portait les identifiants d'organisation et de clé |
| anomalies bloquantes : 4 | **8** : + `cle_de_critere_manquante` (**C1**), `reponse_absente`, `modele_servi_different`, `refus_du_lecteur` | **C1** de la relecture courte (r1) : une entrée sans clé de critère (R1 à R7, N) ou sans `valeur` rend la lecture incomplète ; R4 compris hors `levier:juge` (la consigne demande les huit points) |
| réponse absente : refus | refus **sauf** si le journal consigne un arrêt (anomalie, plafond, appel sans clôture) : alors anomalie bloquante `reponse_absente` (verdict E2) | une lecture arrêtée par la garde laisse des lots non envoyés : le classement doit pouvoir dire E2 et nommer les fiches touchées, sans accepter un dépôt simplement incomplet |
| — | écart d'envoi d'un lot lu (usage, coût…) rapporté dans `lecture-verifiee` (`anomalie_d_envoi`, non bloquante) | trace jusqu'au verdict, même quand le contenu est bon |
| envois `-v2` (lots de 14 ou 15) | **régénérés** de façon déterministe, noms en `-v3` ; mêmes graines (`SeedSequence(2026111302).spawn(4)`, enfants 0 et 1), **mêmes ordres et mêmes étiquettes** que la v2 (essai `test_ordres_identiques_a_la_v2`) ; seules les frontières de lots changent | demande ; R9 |

Inchangés, octet pour octet (comparaison fonction par fonction) : sceaux, pièces épinglées, vue servie (gabarit,
typographie de l'orchestrateur), admissibilité, attestation, provenance M3, pile, ordres, message servi, preuve mot pour
mot (M1), catalogue (cellule du mécanisme), `verifier_entree`. Un caractère invisible (espace fine insécable de la table
typographique) s'était perdu dans ma première écriture : l'essai de la typographie contre l'orchestrateur l'a vu, la table
a été recopiée de la v2 octet pour octet, et la comparaison fonction par fonction le confirme.

### Classement (`classer_conception_propre_v2.py` → `…_v3.py`) : une v3 était nécessaire

La v2 charge l'outil v2 en dur (noms `-v2`, modèle Kimi, réponses absentes refusées) : ses entrées ne sont pas compatibles.
Différentiel entier (`differentiel-classer-v2-v3.diff`, 112 lignes) : chargement de l'outil v3 et noms `-v3` ; retrait de
la vérification « réponse attendue absente → refus » (faite par l'outil v3, avec l'exception de l'arrêt consigné) ; une
précision ajoutée (C1 et anomalies neuves) ; docstrings. **Aucune ligne de la règle** (retenue, portes, S, C, L1 à L5,
Holm, témoin permuté, variante détachée) ne change.

## 3. Essais (hors réseau)

`essais_lecture_classement_v3.py` : les 80 essais de la v2 adaptés (noms, lots de 5, corps de Chat Completions ; le cas
« modèle servi différent → refus » devient une anomalie bloquante), plus les essais de la v3. L'API d'OpenAI est
remplacée par une **doublure déclarée** (`Doublure`) injectée dans `envoyer` : elle vérifie l'adresse et l'en-tête,
reconnaît le lot par l'empreinte du corps et rend la réponse d'un lecteur simulé, ou celle d'un scénario. Clé factice.
Chaque garde a son cas sain et son artefact (R5) :

| Garde | Cas sain | Artefact |
|---|---|---|
| fin autre que `stop` | 12 appels « stop », lisible, deux désignées | `length` au 3e appel : arrêt, 3 appels, reprise refusée, E2 |
| modèle servi | `gpt-6-astra` exact | `gpt-6-astra-2026-11-01` : arrêt au 1er appel ; à la vérification, E2, contenu non lu |
| usage absent / incohérent | coût lu exact (avec et sans cache) | compté au pire cas, arrêt, `anomalie_d_envoi` rapportée |
| coût au-dessus du pire cas | — (même cas sain) | coût lu (plus haut) compté, arrêt |
| plafond | plafond 14 : tout passe | plafond 3 : arrêt avant l'appel qui pourrait dépasser, nombre d'appels exact, E2 |
| nombre d'appels | 45 fiches : 18 appels | 46 fiches : refus à la préparation ; journal déjà plein : arrêt sans envoi |
| statut autre que 200 | — | 429 : fichier d'erreur sans corps ; identifiants du compte absents de tout fichier |
| transport, illisible, refus | — | coupure (message contenant la clé : masqué), page HTML, `refusal` |
| reprise | pause après 2 appels, reprise : 10 appels, aucun renvoi | journal tronqué ou réécrit : refus ; appel sans clôture : pire cas, refus |
| clé | lue, retirée, jamais écrite ni affichée | absente : refus avant tout journal, en appel et en ligne de commande |
| citation | passage exact compté | passage altéré : 0, « non prouvé » |
| clé de critère (C1) | aucune anomalie | `N`, `R7`, `valeur` de N, R4 hors `levier:juge` manquants : E2 |
| réponse absente | — | sans arrêt consigné : refus ; avec arrêt : E2 |
| préparation | effort, prix, plafond corrects | effort `max`, prix nul, NaN ou négatif, cache > entrée, source vide, plafond > 14,20, infini, ou sous un seul appel : refus, rien écrit |

Plus : forme exacte du corps, effort dans chaque corps, ordres identiques à la v2, lots de 43 = sept de 5 et deux de 4,
règles du coût (cache, excédent, valeurs booléennes ou négatives), confinement (une seule adresse, deux accès à
l'environnement dans le code, aucun accès réseau ni à l'environnement dans le classement).

## 4. Banc de mutations

`mutations_lecture_classement_v3.py` : 129 mutants, chacun joué contre tous les essais (`-x`), dans un dossier temporaire
hors du dépôt, environnement réduit à PATH, LANG, LC_ALL, TZ, TMPDIR, HOME (aucun mandataire, aucune clé) : les 75 de la
v2 encore applicables (cinq adaptés aux lignes changées ; celui de la garde `max_tokens`, disparue, retiré) et 54 neufs
sur les changements de la v3 (anomalies bloquantes neuves et C1, corps et point d'entrée, analyse à l'envoi, coût lu,
garde de dépense et d'appels, journal et reprise, clé et corps d'erreur, adresse figée).

- **Première passe** (07:55:59 à 08:13:53 UTC) : **128 tués sur 129** ; survivant : « cohérence réponses-journal non
  contrôlée » (retirer `controler_coherence` de `envoyer`) ; l'essai du journal tronqué tombait aussi sur la garde
  « appel sans clôture », qui masquait celle-ci. Essai ajouté : `test_reponse_etrangere_refusee_avant_tout_envoi` (une
  réponse déposée sans clôture arrête `envoyer` **avant tout appel**) ; vérifié qu'il tue ce mutant. Code inchangé.
- **Seconde passe** (08:14:57 à 08:33:05 UTC), sur le code et les essais définitifs : **129 tués sur 129**, aucun
  inapplicable.
- R4 : un banc entièrement tué est « trop propre » au sens du programme ; il ne prouve que ce que ses mutants visent, et
  mutants et essais sont du même auteur. La contre-lecture devrait ajouter ses propres mutants (comme pour la v2).

## 5. Gestes de la mère, après contre-lecture, prix lu et GO (rien de ceci n'est fait)

Depuis la racine du dépôt, dossier neuf `docs/notes/organisme-conception-propre-v1/lecture-g1-v3/` (R12) ; vérifier
d'abord les empreintes de l'outil et du classement contre leurs compagnons (les programmes ne vérifient pas la leur).

1. `.venv/bin/python -I -B docs/notes/organisme-conception-propre-v1/lecture-classement-v3/outil_lecteur_conception_propre_v3.py preparer --fiches runs/course-ideation-conception-propre-v1/20261113-235541-course-ideation-conception-propre-v1-g1/copies/sortie--fiches-validees.json --attestation docs/notes/organisme-conception-propre-v1/attestations/attestation-lecture-g1-v1.json --sortie docs/notes/organisme-conception-propre-v1/lecture-g1-v3/envois --effort medium --prix-entree <PE> --prix-sortie <PS> [--prix-cache <PC>] --source-prix "<page ou console, date, empreinte>" --plafond-usd <X>`
2. `… outil_lecteur_conception_propre_v3.py envoyer --envois docs/notes/organisme-conception-propre-v1/lecture-g1-v3/envois --envois-max 1`
   (`OPENAI_API_KEY`, `HTTPS_PROXY`, `SSL_CERT_FILE` présents dans l'environnement, par leur nom) ; puis `… bilan --envois …`
   et recalcul du devis avec les jetons réels.
3. `… envoyer --envois …` (sans `--envois-max`) : code 0 fait, 3 arrêt sur anomalie, 4 arrêt au plafond, 2 refus.
4. `… verifier --envois …` ; la condition C1 est désormais tenue par le programme (anomalie bloquante).
5. `.venv/bin/python -I -B docs/notes/organisme-conception-propre-v1/lecture-classement-v3/classer_conception_propre_v3.py --envois … --sortie docs/notes/organisme-conception-propre-v1/lecture-g1-v3/classement`.

## 6. Réserves

- **r1 — prix non lu** : devis en formule ; à recalculer quand le prix est lu (nœud).
- **r2 — documentation d'OpenAI non lue dans la session** : la forme de Chat Completions (`max_completion_tokens`,
  `reasoning_effort`, `store`), le sens de `usage` (`completion_tokens` compte le raisonnement, dont
  `completion_tokens_details.reasoning_tokens` est une part) et le nom servi viennent de la pratique du dépôt (R-1454,
  collisionneur v8, pilote v70, où la règle est déjà notée « de mémoire, non vérifiée ») et de ma connaissance. **Aucun appel
  du dépôt n'a encore envoyé `reasoning_effort` à Astra** : s'il le refuse (400), le premier appel s'arrête, compté au pire
  cas, et il faudra une v3.1 (d'où la recommandation d'un premier appel seul). Si `reasoning_tokens` n'était pas compris
  dans `completion_tokens`, le coût serait sous-compté tant que le raisonnement reste plus petit que la sortie visible ;
  le premier appel le dira (un raisonnement plus grand que la sortie est compté au pire cas).
- **r3 — appel sans flux** : une réponse longue (raisonnement silencieux) peut être coupée par un intermédiaire ; l'appel
  compte alors son pire cas et la lecture s'arrête (délai fixé à 1 800 s par lecture de socket). Lots de 5 et effort
  `medium` pour raccourcir les appels.
- **r4 — taille de lot** : justifiée par le raisonnement de Kimi ; celui d'Astra n'est pas mesuré.
- **r5 — C1 strict** : R4 manquant sur une fiche hors `levier:juge` bloque aussi, alors que le programme le met à 1 ;
  c'est la lettre de C1 et de la consigne.
- **r6 — écart d'envoi sur un lot lu** (usage absent, coût au-dessus du pire cas) : arrêt et `anomalie_d_envoi` rapportée,
  mais le lot lu n'est pas bloquant pour la lecture ; au dernier appel, la lecture peut donc être complète et lisible
  malgré l'écart (la dépense, elle, est comptée haut).
- **r7 — journal** : garde contre l'accident, non contre la malveillance (effacer à la fois une ligne de journal et le
  fichier d'erreur correspondant ne se voit pas). Clé : même limite que les relais (`/proc/<pid>/environ` garde le bloc
  initial tant que le processus vit, F-C7).
- **r8 — attestation** : celle de la mère (`de94e86e…`) dit « envoi au lecteur externe permis » sans nommer le
  fournisseur ; elle a été écrite quand le lecteur était Kimi. L'outil l'accepte ; la mère peut vouloir une attestation
  qui nomme OpenAI.
- **r9 — classement v3** : une lecture arrêtée donne maintenant un verdict E2 scellé (au lieu d'un refus) ; le τ de
  Kendall avec le juge de l'organisme (§ 4.8) n'est toujours pas écrit ; les programmes ne vérifient pas leur propre
  empreinte.

## 7. Pour la contre-lecture

À lire : `differentiel-outil-v2-v3.diff` (885 lignes) et `differentiel-classer-v2-v3.diff` (112 lignes) avant le code
entier ; `envoyer`, `analyser_reponse`, `cout_usage`, `lire_journal`, `controler_coherence`, `lire_reponse`,
`verifier_lecture` sont les fonctions neuves ou changées qui portent la dépense et le verdict. Points que je ne sais pas
trancher : r2 (forme exacte de l'API pour `gpt-6-astra`), r3 (appel sans flux), r6 (écart d'envoi au dernier appel).

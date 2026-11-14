# Contre-lecture — outil du lecteur v3 (lecteur Astra) et classement v3, course « conception propre » — v1

Contre-lecteur neuf (modèle B, autre que l'auteur, modèle A), sous-agent de la session mère ; 14 novembre 2026, de 08:35
à 08:50 UTC (heures relevées par `date -u`). Je n'ai écrit aucune des pièces lues. **Aucun appel réseau** (essais, mutants
et sondes joués dans un espace de noms réseau vide, `unshare -n`), **aucune valeur de clé lue** (clés factices seulement),
**aucune fiche réelle ni aucun témoin ouvert** : je n'ai ouvert ni `runs/course-ideation-conception-propre-v1/`, ni
`lecture-g1-v1/envois/`, ni les fichiers de témoins ; ceux-ci ne sont lus que par les programmes, sous la racine factice
des essais de l'auteur, et mes pièces n'en rendent que des empreintes, des comptes et des booléens. Aucun fichier du
dossier v3 modifié ; rien commité, rien poussé.

Lu : le dossier `lecture-classement-v3/` en entier (outil `6a11cf3d…`, classement `87643592…`, essais `6e00a544…`, banc
`d758f7ff…`, résultats `ce423cb0…`, `c517e5b3…`, `0adfc8b3…`, différentiels `e7e92440…` et `64414e04…`, prix
`839a3e6c…`, devis `6f8f97c0…`, rapport `699734d2…` ; les douze compagnons `.sha256` vérifiés) ; la conception
(`be3ba97e…`, § 3 à 7), la consigne (`95efebaa…`), le dossier v2 (outil `a58fb8b9…`, classement `2cb65f33…`), la
relecture courte (`2bd818d0…`) ; les lignes R-2631, R-2644, R-2645, R-2646, R-2658 à R-2662 et R-2675.

## Verdict : « non utilisable » en l'état, pour la seule action `envoyer`

La **règle est inchangée** (point 1, tenu sans réserve) et les gardes de dépense font ce qu'elles disent dans un dossier
donné. Mais deux exigences de la demande sur la **clé** sont démenties par l'exécution : la clé peut être **écrite dans un
fichier scellé du dépôt** (B1), et elle peut **partir vers un autre hôte** (B2). Ces deux défauts ne se neutralisent pas
proprement par un geste d'opérateur ; ils se corrigent en quelques lignes. Je demande donc une **v3.1** (corrections
B1, B2, M1 à M4 ; rien à toucher dans `preparer`, la vérification mot pour mot ni le classement), puis l'emploi sous
les conditions C1 à C7 ci-dessous. `preparer`, `verifier` et le classement v3 sont, eux, utilisables tels quels.

Le banc de l'auteur (129 tués sur 129) était bien « trop propre » (R4) : de mes **21 mutants, 15 survivent** (§ 5).

## 1. La règle est-elle inchangée ? Oui

- Comparaison fonction par fonction (arbres syntaxiques, docstrings ôtées), refaite par moi : dans l'outil, 49 objets
  identiques, dont `vue_lecteur`, `admissibilite`, `construire_pile`, `enfants_ordres`, `ordres_lectures`,
  `decouper_lots`, `etiquette`, `texte_message`, `passage_dans`, `verifier_entree`, `entrees_catalogue`,
  `extraire_json`, `verifier_attestation`, `verifier_fiches_de_run`, `ORDRE_VUE`, `TABLE_TYPO`, `PIECES`,
  `ENTROPIE_ORDRES`. Changés : `TAILLE_LOT` (20 → 5), `MODELE_LECTEUR`, `MAX_APPELS`, `ANOMALIES_BLOQUANTES` (4 → 8),
  `corps_requete`, `pire_cas_usd`, `preparer`, `lire_reponse`, `verifier_lot`, `verifier_lecture`, `charger_envois`,
  `main`. Dans le classement : `classer`, `retenir`, `portes_manquantes`, `score_S`, `score_C`, `rangs_departage`,
  `temoin_permute`, `test_permutation`, `holm`, `kappa_accord`, `designer_detachee` et tous les seuils identiques ; seuls
  changent les noms en `-v3`, une précision, et le retrait du contrôle « réponse absente » (repris par l'outil).
- Les deux différentiels scellés égalent ceux que je recalcule (`diff -u`, en-têtes à part).
- Lots de 5 : dans la lettre du § 4.3 (« par lots de 20 au plus »). Deux lectures, chacune son ordre ; L5 seul test.
- Les quatre anomalies bloquantes neuves ne peuvent que retirer une désignation (verdict E2), jamais en créer.
- Sonde s7 (fiches factices, piles de 28 et de 43) : deux préparations v3 identiques octet pour octet (38 fichiers ;
  les manifestes ne diffèrent que par l'heure) ; contre une préparation par l'outil v2 des mêmes fiches : **mêmes
  ordres, mêmes étiquettes, même pile interne (octet pour octet), même vue servie étiquette par étiquette, même
  préambule**, mêmes graines consignées (`SeedSequence(2026111302).spawn(4)`, enfants 0 à 3) ; lots v2 15, 14, 14 →
  v3 sept de 5 et deux de 4, consécutifs, sans trou. Point 6 tenu.
- Écart de documentation sans effet (m3) : la v3, comme la v2, **lit** le contenu d'une réponse à fin autre que `stop`
  (anomalie bloquante, donc E2), alors que la docstring de `lire_reponse` et la précision ajoutée disent « non lu ».

## 2. Constats

### Bloquants

**B1 — la clé est écrite dans un fichier d'erreur scellé si elle porte une fin de ligne.** `outil…v3.py`, l. 548-557
(`lire_cle`, `masquer`), l. 806-807 et 816 (`cause_transport`). Une clé terminée par un retour chariot ou un saut de
ligne (fichier d'origine Windows, copie avec fin de ligne) fait lever par la bibliothèque `ValueError: Invalid header
value b'Bearer …\r'` : le message porte la clé sous sa forme échappée, que `masquer` (remplacement de la chaîne exacte)
ne reconnaît pas. Sonde s1, transport réel de l'outil : la clé factice se retrouve dans `erreur-L1-lot1-v3.json`,
scellé, dans un dossier destiné au dépôt ; aucun octet n'est parti, un pire cas est compté (2,05 USD à l'essai) et la
lecture est **arrêtée sans reprise**. Les essais ne le voient pas : leur doublure remplace le transport.
*Correction* : `lire_cle` refuse, sans l'afficher, toute clé hors `[\x21-\x7e]+` (avant tout journal) ; ne jamais écrire
le message d'une exception de transport, seulement son type (`type(ex).__name__`) ; essai avec le transport réel.

**B2 — une redirection envoie la clé à un autre hôte, et la réponse de cet hôte est acceptée.** `outil…v3.py`,
l. 566 (`build_opener` garde le gestionnaire de redirection par défaut). Sur un 301, 302 ou 303 rendu à un POST,
`urllib` rejoue la requête en GET vers l'adresse donnée **avec l'en-tête `Authorization`**. Sonde s2 (deux serveurs
sur la boucle locale, adresse d'amont remplacée en mémoire seulement) : l'autre hôte reçoit `Bearer <clé>` ; l'outil
reçoit de lui un statut 200 et son corps. `transport_reel` ne contrôle que l'adresse de départ. Peu probable chez
OpenAI, possible par un intermédiaire ; c'est le « repli vers un autre hôte » exclu par la demande.
*Correction* : gestionnaire dont `redirect_request` rend `None` (le 3xx devient un statut autre que 200, donc arrêt) ;
contrôle `r.geturl() == URL_AMONT` ; essai avec le transport réel sur la boucle locale.

### Majeurs

**M1 — `verifier` et le classement lisent des réponses qu'`envoyer` n'a pas produites.** `outil…v3.py`, l. 1027-1034
(`verifier_lecture` n'appelle pas `controler_coherence`) ; `classer…v3.py`, l. 264. Sonde s4 : réponses scellées
déposées à la main, aucun journal → « lisible, L5 rejetée : deux idées désignées ». La provenance des réponses n'est
tenue que par `envoyer` et `bilan`. *Correction* : dans `verifier_lecture`, exiger pour chaque réponse lue une clôture
du journal au même nom et à la même empreinte, statut 200. En attendant : condition C5.

**M2 — un dossier neuf remet la dépense à zéro et renvoie les mêmes lots.** `outil…v3.py`, l. 108
(`PLAFOND_ABSOLU_USD` constant) et l. 450-459. « Aucune reprise » et « le compte ne revient pas à zéro » ne valent que
dans un dossier. Sonde s8 : arrêt au 3e appel (2,25 USD comptés), reprise refusée ; même pile préparée dans un dossier
voisin au même plafond de 14 USD : 12 appels partent, dont les 3 déjà faits ; total 5,24 USD, que rien ne compare à
14,20. C'est aussi une relecture, que la règle exclut. *Correction* : `preparer` exige les relevés scellés des dossiers
antérieurs (ou `--depense-anterieure-usd`), borne le plafond à 14,20 moins ce total, et le consigne ; condition C6.

**M3 — une réponse 200 payée est perdue quand l'analyse tombe.** `outil…v3.py`, l. 589-590, 632-633, 664 (`.get` sur
des valeurs non contrôlées), l. 808-811 (la réponse n'est écrite qu'après l'analyse). Sondes s5 et s6 : détails
d'usage ou `message` non objets, `error` en chaîne ou en liste → `AttributeError`, trace Python, **ni réponse ni
fichier d'erreur écrits**. La dépense reste comptée au pire cas et la reprise refusée (côté sûr), mais la pièce payée
manque et rien ne dit pourquoi. *Correction* : sceller les octets reçus avant l'analyse (ou leur empreinte), et garder
chaque `.get` par `isinstance(…, dict)` → anomalie `reponse_illisible` ou `usage_absent`.

**M4 — un usage sous-déclaré est compté tel quel.** `outil…v3.py`, l. 596-607. Sonde s3 : `prompt_tokens = 0` et
`completion_tokens = 0` avec 4 000 caractères rendus → coût 0, aucune anomalie ; `total_tokens` inférieur à la somme
→ aucune anomalie. La demande dit « usage incohérent : compté au pire cas » ; seules les incohérences vers le haut
le sont. La garde du plafond repose alors sur un compte trop bas. *Correction* : `usage_incoherent` si le total est
sous la somme, si la sortie est nulle avec un contenu non vide, ou si l'entrée est sous un plancher large (octets du
corps divisés par 16).

**M5 — gardes de dépense et d'arrêt sans artefact dans les essais (R5).** Survivent à mes mutants (§ 5) : échec de
transport compté zéro (D4), réponse 200 illisible comptée zéro (D5), reprise permise après une anomalie autre que la
fin (R2), contenu vide ignoré à l'envoi (F3), plusieurs choix (F2), objet autre que `chat.completion` (F4), clé vide
(C2), repli vers une autre variable par `os.getenv` (C1 : l'essai de confinement ne compte que `os.environ`), champs
d'erreur non filtrés (C3). Le code d'origine est juste sur ces points ; ce sont les essais qui ne le prouvent pas.
*Correction* : un essai par ligne (dépense égale au pire cas après une coupure et après une page de passerelle ;
`Refus` à la reprise après chacune des anomalies ; clé vide ; recherche de `getenv` ; `code` d'erreur portant un
identifiant).

### Mineurs

- **m1** — `envoyer` ne revalide pas le plafond du manifeste (l. 765-767) : un manifeste rescellé à plafond `NaN`
  laisse partir tous les appels sans garde, puis tombe à l'écriture du relevé (sonde s10 ; mutants D6, D7 survivants).
  Correction : même contrôle qu'à la préparation (fini, strictement positif, au plus 14,20). Accident peu probable.
- **m2** — devis, l. 71 et 98 : la condition des 18 appels est écrite 0,3019 PE + 0,3089 PS ; le dernier appel est un
  lot de 4 (ordre du manifeste), ce qui donne, avec les hypothèses mêmes du devis, **0,2978 PE + 0,3116 PS** (18,56 USD
  au barème supposé, contre ≈ 18,5 écrit). Écart de 0,5 %, dans le mauvais sens pour la sortie ; à refaire au prix lu.
- **m3** — docstring de `lire_reponse` (l. 901-902) et précision du classement (l. 97-100) : « contenu non lu » est
  faux pour la fin autre que `stop` et pour l'objet inattendu. Sans effet sur le verdict (E2).
- **m4** — C1 est tenue à la lettre (valeur nulle), mais une valeur de N illisible **non nulle** (« Aucune », « none »,
  « C13 », 0) compte `aucune` sans anomalie bloquante (sonde s9 ; l. 973-975) : même faiblesse que la réserve r1 de la
  relecture courte, pour la nouveauté. Inchangé depuis la v2 ; le corriger touche la lecture : **nœud**, non routine.
- **m5** — attestation `de94e86e…` écrite quand le lecteur était Kimi (réserve r8 de l'auteur) : l'envoi à OpenAI
  mérite une attestation qui le nomme (§ 3 de la conception : « fournisseur externe ») ; geste de la mère.
- **m6** — gestes de la mère (rapport, § 5, point 2) : lancer `envoyer` sous `env -i` réduit aux noms nécessaires
  (PATH, HOME, HTTPS_PROXY, SSL_CERT_FILE, OPENAI_API_KEY), comme le relais de R-2644, non dans l'environnement entier.
- **m7** — R-2675 écrit « ≈ 38,5 au pire cas borné par la garde » : la garde borne au plafond donné (14,20 au plus),
  non à 38,5 ; le devis le dit bien.
- **m8** — pire cas non recalculé sur les octets (mutant D2) et envoi en double au journal (R3) survivent : gardes
  redondantes avec le sceau du corps et la chaîne du journal ; sans conséquence trouvée.

## 3. Clé (point 2)

Tenu : `OPENAI_API_KEY` lue par son nom dans `lire_cle` seule, retirée de l'environnement du processus, posée dans
l'en-tête seul ; absente du manifeste, du journal, des relevés, de la sortie standard, des messages `Refus` ; aucune
autre variable de clé, une seule adresse dans le code ; `bilan` et `verifier` ne la lisent pas ; lue seulement s'il
reste un envoi à faire. **Non tenu** : B1 (écrite dans un fichier d'erreur) et B2 (autre hôte). Limite connue et dite
par l'auteur : l'intermédiaire de la session, qui porte son propre certificat, voit l'en-tête.

## 4. Gardes (point 3) et devis (point 4)

| Garde | Lecture du code | Essai de l'auteur (sain et artefact) | Reste |
|---|---|---|---|
| fin autre que `stop` | l. 661-663, arrêt l. 823-825 | oui | F1 : à la vérification, seul `length` est essayé |
| modèle servi | l. 655-656 (égalité exacte), l. 915 | oui (quatre formes) | M2 du banc : casse, à la vérification seule |
| usage absent ou incohérent | l. 584-607, 643-650 | oui, vers le haut | M4 : vers le bas, non vu |
| plafond avant chaque appel | l. 791-797 | oui (nombre d'appels exact) | M2 : par dossier seulement ; m1 |
| nombre d'appels | l. 478, 784-787 | oui | — |
| arrêt au premier écart, sans reprise | l. 770-773, 823-825 | oui pour la fin et le plafond | R2 du banc ; M2 (dossier neuf) |
| corps d'erreur jamais écrit | l. 631-635, 812-817 | oui (429) | B1 (message d'exception) ; C3 du banc |
| C1 bloquante | l. 938-940, 1006-1009 | oui (quatre formes) | m4 |

L'envoi est bien séquentiel : la réponse d'un lot est analysée et consignée avant toute lecture du lot suivant (leçon
de R-2658 tenue). Aucun repli silencieux trouvé dans la garde du plafond elle-même.

**Devis** : sommes refaites (reste de la ligne 21 − 6,791087 = 14,208913 ; réserve du lecteur 4 − 1,256342 = 2,743658 ;
sorties 120 400, 292 400, 550 400 et 589 824 ; 8,68, 17,28, 30,18 et 38,50 USD au barème supposé) : justes, à l'écart
m2 près. **Aucun prix n'est inventé** : `prix-astra-v1.md` dit la page non lue, le barème 10 et 50 USD par million est
marqué « SUPPOSÉ » partout, l'outil n'a aucun prix dans son code et refuse une source vide. Le pire cas d'un appel
(un jeton par octet du corps plus 1 024, plafond de sortie entier) est une vraie borne **si** le prix donné est le
vrai et **si** le plafond de sortie couvre le raisonnement (supposé, réserve r2 de l'auteur) : d'où C2 et C3.

## 5. Mes mutants (point 5)

`contre-lecture-lecture-classement-v3-outils/mutations_contre_lecture_v3.py`, joué de 08:41:06 à 08:47:59 UTC contre
les 123 essais de l'auteur (base : 123 passés) ; résultat `resultat-mutations-contre-lecture-v3.json`.
**21 mutants, 6 tués, 15 survivants.**

| Mutant | Garde | Issue |
|---|---|---|
| D1 plafond dépassable de 0,50 USD | dépense | tué |
| D2 pire cas non recalculé sur les octets envoyés | dépense | **survit** (redondant, m8) |
| D3 usage incohérent compté au coût lu | dépense | tué |
| D4 échec de transport compté zéro | dépense | **survit** |
| D5 réponse 200 illisible comptée zéro | dépense | **survit** |
| D6 bornes du code non revérifiées à l'envoi | dépense | **survit** |
| D7 prix du manifeste non revalidés à l'envoi | dépense | **survit** |
| D8 garde du nombre d'appels décalée d'un | dépense | tué |
| D9 arrêt au plafond non consigné | dépense | tué |
| F1 vérification : seule la fin `length` bloque | fin | **survit** |
| F2 envoi : plusieurs choix acceptés | fin | **survit** |
| F3 envoi : contenu vide ignoré, le lot suivant part | fin | **survit** |
| F4 envoi : objet autre que `chat.completion` accepté | fin | **survit** |
| M1 envoi : espaces de fin tolérés dans le nom servi | modèle servi | tué |
| M2 vérification : nom servi comparé sans la casse | modèle servi | **survit** |
| C1 repli vers une autre variable par `os.getenv` | clé | **survit** |
| C2 clé vide acceptée | clé | **survit** |
| C3 type et code d'erreur écrits sans filtre | clé | **survit** |
| R1 reprise permise après un arrêt au plafond | reprise | tué |
| R2 reprise permise après une anomalie autre que la fin | reprise | **survit** |
| R3 envoi consigné deux fois non refusé | reprise | **survit** (redondant, m8) |

Sondes sur le code non modifié (`sondes_contre_lecture_v3.py`, `resultat-sondes-contre-lecture-v3.json`, 08:42:57 UTC,
seule interface : `lo`) : s1 (B1), s2 (B2), s3 (M4), s4 (M1), s5 et s6 (M3), s7 (point 6, tenu), s8 (M2), s9 (m4),
s10 (m1).

## 6. Conditions d'emploi de la v3.1 (vérifiables par programme)

- **C1** — v3.1 scellée ; mes sondes rejouées sur elle rendent : s1 `cle_ecrite_dans` vide et refus avant tout
  journal ; s2 aucune requête reçue par l'autre hôte ; s3 trois anomalies `usage_incoherent` ; s4 refus ; s5 et s6
  aucune exception, une pièce écrite ; les fonctions de la règle listées au § 1 restent identiques (comparaison
  d'arbres) ; mes mutants D4, D5, F2, F3, F4, C1, C2, C3, R2 sont tués.
- **C2** — `garde_depense.prix_usd_par_million.source` du manifeste cite une page ou une console lue, sa date et son
  empreinte ; elle ne contient ni « SUPPOSÉ » ni « barème » ; `prix-astra` en version 2 existe et porte les mêmes
  chiffres.
- **C3** — premier appel seul (`--envois-max 1`), puis `bilan` : `anomalies` vide, `modele_servi` exact,
  `reasoning_tokens ≤ completion_tokens ≤ 32 768`, coût lu ≤ pire cas ; devis recalculé avant les 17 autres.
- **C4** — `plafond_usd` du manifeste ≤ 14,20 moins toute dépense comptée depuis le devis (`registres/depenses.md`),
  et ≥ la condition des 18 appels recalculée au prix lu (m2) ; sinon ne pas lancer.
- **C5** — avant `verifier` et avant le classement : `bilan` rend le code 0, 18 clôtures, aucune en vol, et chaque
  `reponse-*-v3.json` présente a sa clôture à la même empreinte.
- **C6** — un seul dossier d'envois v3 dans le dépôt (`find … -name 'manifeste-envois-v3*.json'` rend une ligne) ;
  toute seconde préparation après un premier appel est un nœud.
- **C7** — `envoyer` lancé sous `env -i` réduit (m6) ; après l'envoi, aucun fichier du dossier ne contient la clé
  (recherche faite par un programme qui lit la clé par son nom et n'affiche qu'un booléen).

## 7. Réserves de cette contre-lecture

- Documentation d'OpenAI non lue (hôtes fermés) : forme du corps, sens de `usage` et nom servi restent ceux de la
  pratique du dépôt (réserve r2 de l'auteur, que je ne lève pas) ; C3 les éprouve sur le premier appel.
- Tailles des lots réels non mesurées (je n'ouvre pas les envois) : les octets du devis sont ceux de l'auteur.
- B2 est montré sur `http` et la boucle locale ; le chemin de code est le même en `https`.
- Mes mutants et mes sondes sont du même auteur (moi) : ils ne prouvent que ce qu'ils visent.

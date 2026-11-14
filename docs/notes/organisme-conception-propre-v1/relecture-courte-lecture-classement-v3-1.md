# Relecture courte — outil du lecteur v3.1 (lecteur Astra) et classement v3.1, course « conception propre »

Même contre-lecteur que pour la v3 (modèle B, autre que l'auteur, modèle A), sous-agent de la session mère ; 14 novembre
2026, de 10:18 à 10:33 UTC (heures relevées par `date -u`). Demande : R-2702. **Aucun appel réseau** (essais, mutants et
sondes sous `unshare -n`), **aucune valeur de clé lue** (clés factices ; présence de la vraie et des variables de
mandataire vérifiée par leur nom seul), **aucune fiche réelle ni aucun témoin ouvert** (fiches factices des essais ;
témoins lus par les programmes seuls, sous racine factice). Aucun fichier des dossiers v3 et v3.1 modifié ; rien commité.

Lu : `lecture-classement-v3-1/` en entier — rapport `32f858a6…`, outil `95bc46c1…`, classement `f9ef3695…`, essais
`490eb359…`, banc `182f36cf…` et ses résultats `5cb31809…`, `29d29159…`, différentiels `0b5cf667…` et `007bc572…`,
devis v2 `5e4e0cc7…`, dossier `rejeu-contre-lecture/` ; `prix-astra-v2.md` (`bf211a07…`) ; lignes R-2677 à R-2679 et
R-2702. Tous les compagnons `.sha256` vérifiés ; les deux différentiels v3 → v3.1 égalent ceux que je recalcule.

## Verdict : « utilisable sous conditions »

B1, B2, M1 à M5 et m1 sont **fermés**, vérifiés par mes propres rejeux et non par ceux de l'auteur. **La règle de lecture
est inchangée.** Les conditions K1 à K9 (§ 6) sont vérifiables par programme. Deux points d'emploi demandent un mot de
Lazar **avant la préparation**, parce que la v3.1 gèle le plafond au manifeste et n'admet qu'un dossier :

- **E1 — le plafond de 9,30 USD laisse 0,24 % de marge.** La garde ne laisse partir le 18e appel que si les 17
  premiers ont coûté au plus 8,246 USD ; le devis en attend 8,227. Sonde p1 (fonctions de l'outil, volumes du devis v2,
  prix Flex) : sortie égale au devis → 18 appels, 8,64 USD ; **sortie de 1 % au-dessus → arrêt avant le 18e appel,
  8,30 USD payés, verdict E2, rien de désigné** ; + 20 % → arrêt avant le 16e ; + 50 % → avant le 13e. Le raisonnement
  par fiche (3 000 jetons) est « SUPPOSÉ », jamais mesuré sur Astra. Au plafond de 14,20 (recommandation du devis v2),
  la lecture reste complète jusqu'à + 50 % (12,29 USD) et la dépense attendue est la même. Le 9,30 de R-2679 a été
  donné quand le seuil était écrit 9,23 ; il vaut 9,28.
- **E2 — tout arrêt au premier appel tue le seul dossier.** Un refus du palier Flex faute de ressources (429), un
  paramètre refusé (400 : `reasoning_effort` et `service_tier` n'ont jamais été envoyés à Astra), une coupure : arrêt,
  pire cas compté (1,03 à 1,07 USD), reprise refusée, seconde préparation refusée (sonde p4). Le seul chemin restant est
  de déplacer le dossier arrêté hors de `docs/` et de `runs/` ; l'outil accepte alors une préparation neuve **sans
  dépense antérieure déclarée** (p4 : 12 appels repartent, compte à zéro). C'est la limite r5 de l'auteur ; la marche
  à suivre doit être décidée d'avance (K8).

## 1. Constats de la v3 : fermés ?

| Constat | Issue | Ma preuve (rejeu par moi, copie non modifiée de la v3.1) |
|---|---|---|
| **B1** clé écrite | **fermé** | s1 : refus avant tout journal, clé dans aucun fichier ni dans le refus, serveur non contacté ; p5 : dix formes de clé (fin de ligne, espace, 513 caractères, `\x7f`, non ASCII, vide) ; mutants N15, N16, N17, C2 tués |
| **B2** redirection | **fermé** | s2 : statut 302 rendu, **aucune requête reçue par l'autre hôte** ; mutant N18 tué |
| **M1** réponses hors journal | **fermé** | s4 : refus ; mutant N19 tué (les deux contrôles ne sont donc pas redondants) |
| **M2** dossier neuf | **fermé dans `docs/` et `runs/`** | s8 : trois refus, 3 appels en tout ; N6 à N11 tués ; reste E2 et n4 |
| **M3** réponse payée perdue | **fermé** | s5, s6 : aucune exception, réponse gardée brute ou fichier d'erreur écrit |
| **M4** usage sous-déclaré | **fermé** | s3 : trois `usage_incoherent`, pire cas ; N12, N13, N14 tués |
| **M5** gardes sans artefact | **fermé** | mes 15 survivants de la v3 : 14 tués, D2 redondant (ci-dessous) |
| **m1** plafond non revalidé | **fermé** | s10 : refus avant tout appel ; D6, D7 tués |
| **m2** condition des 18 appels | **fermé** | devis v2 refait : 0,2988 × 5 + 0,3116 × 25 = 9,28 ; standard 18,57 ; `low` 5,18 et 10,37 |
| **m3** « contenu non lu » | **fermé** | docstring et précision justes |
| **m4** N illisible non nulle | **ouvert, et mal lu par R-2702** | voir n1 |
| **m5** attestation | geste de la mère | K7 |
| **m6** environnement réduit | **fermé** | § 7 du rapport, point 6 ; les six noms sont présents dans la session (vérifié par le nom) |
| **m8** D2, R3 | R3 tué ; D2 redondant | `valider_manifeste` refuse tout pire cas consigné autre que le recalculé (l. 919-960) |

## 2. La règle est inchangée

Comparaison d'arbres refaite par moi (docstrings ôtées) : outil v3 → v3.1, 68 objets identiques, dont toute la règle
(`vue_lecteur`, `admissibilite`, `construire_pile`, `enfants_ordres`, `ordres_lectures`, `decouper_lots`, `etiquette`,
`texte_message`, `passage_dans`, `verifier_entree`, `verifier_lot`, `cles_manquantes`, `entrees_catalogue`,
`extraire_json`, `ORDRE_VUE`, `TABLE_TYPO`, `PIECES`, `ENTROPIE_ORDRES`, `TAILLE_LOT`) ; classement : 25 objets
identiques à la v3 **et à la v2** (`classer`, `retenir`, portes, S, C, départage, témoin permuté, test, Holm, κ, tous les
seuils). Sonde s7 rejouée (piles de 28 et de 43) : régénération identique octet pour octet, mêmes ordres, étiquettes,
pile interne, vue servie, préambule et graines que la v2. Les trois anomalies bloquantes neuves (`anomalie_d_envoi`,
`reponse_non_analysee`, `palier_servi_different`) ne peuvent que retirer une désignation. Le palier Flex n'ajoute au
corps que `service_tier` ; le message servi au lecteur est le même.

## 3. Mes mutants, rejoués par moi

`relecture-courte-lecture-classement-v3-1-outils/mutations_relecture_courte_v3_1.py`, 10:21:14 à 10:29:33 UTC, contre
les 220 essais de l'auteur (base : 220 passés sous `unshare -n`).

- **Série A, mes 21 mutants de la v3** (16 mot pour mot, 5 traduits ; mes traductions égalent celles de l'auteur) :
  **20 tués, 1 survivant (D2)**. D2 est bien redondant, non une lacune.
- **Série N, 19 mutants neufs** sur ce qui a changé : **18 tués, 1 survivant (N3)**.

| Mutant neuf | Issue |
|---|---|
| N1 Flex : `service_tier` non envoyé | tué |
| N2 Flex : palier servi `default` accepté | tué |
| **N3 Flex : palier servi absent accepté** | **survit** |
| N4 vérification : palier servi non contrôlé | tué |
| N5 prix de sortie Flex divisé par dix | tué |
| N6 unicité : manifestes v3.1 seuls cherchés | tué |
| N7 unicité : `runs/` non fouillé | tué |
| N8 unicité non contrôlée au chargement | tué |
| N9 chemin fixe : dernier nom seul contrôlé | tué |
| N10, N11 dépense antérieure non retranchée (préparation, envoi) | tués |
| N12 plancher dix fois plus lâche ; N13 raisonnement compté visible ; N14 total sous la somme | tués |
| N15 espace admis dans la clé ; N16 `match` au lieu de `fullmatch` ; N17 réponse non expurgée | tués |
| N18 gestionnaire sans redirection retiré ; N19 confrontation journal-dossier retirée | tués |

Le banc de l'auteur (182 sur 182) reste « trop propre » au sens de R4, mais mes 40 mutants n'en laissent passer que
deux, dont un redondant : les essais v3.1 portent réellement les gardes.

## 4. Constats neufs

- **n1 (moyen) — m4 n'est pas « prudent ».** R-2702 garde m4 « sens prudent (moins de désignation) ». C'est vrai pour
  R1 à R7 (illisible → 0), **faux pour N** : une valeur de N illisible et non nulle (« Aucune », « none », « C13 »)
  compte `aucune`, donc la fiche reste « neuve » et **désignable** sur une seule opinion (sonde s9, inchangée ;
  `outil…v3_1.py`, `verifier_entree`). Sans toucher la règle : condition K9, par programme, avant de lire le verdict.
- **n2 (mineur) — palier servi autre : coût compté au prix du palier demandé** (l. 800-812). Si Flex est demandé et
  `default` servi, la facture est au prix standard, le double (sonde p3 : 0,12 compté). L'arrêt est immédiat : un seul
  appel exposé, au plus 1,07 USD d'écart. Correction : compter alors le pire cas au prix standard ; d'ici là, la mère
  l'écrit ainsi dans `registres/depenses.md`.
- **n3 (mineur) — N3 survit** : aucun essai ne rend une réponse sans `service_tier` sous Flex. Le code est juste
  (p3 : `palier_servi_different`) ; il manque l'artefact (R5).
- **n4 (mineur) — l'unicité ne voit ni un manifeste renommé (`….json.bak`) ni un dossier déplacé sous la racine hors de
  `docs/` et `runs/`** (l. 515-526 ; sonde p6). Garde contre l'accident ; K8 la complète.
- **n5 (mineur) — `--palier` vaut `standard` par défaut** (l. 1352) : un oubli donne les prix standard et un arrêt vers
  le 5e appel au plafond de 9,30. K2 le voit avant tout appel.
- **n6 (mineur) — rapport, § 7, point 2** : la commande écrit `--plafond-usd 14.20` ; le mot de Lazar est 9,30.

## 5. Conditions C1 à C7 du § 7 du rapport

| Condition | Vérifiable par programme ? | Remarque |
|---|---|---|
| C1 empreintes des deux programmes | oui (`sha256sum -c`) | `95bc46c1…`, `f9ef3695…` ; cette relecture en tient lieu |
| C2 source des prix | oui (commande du point 3) | prix constants du code, revérifiés à l'envoi contre le manifeste |
| C3 premier appel seul, puis `bilan` | oui | champs présents (`clotures[0]` : modèle, palier, jetons, coût, pire cas) ; j'ajoute un seuil (K4) |
| C4 plafond | oui | **à écrire 9,30**, non 14,20 (n6) ; voir E1 |
| C5 `bilan` avant vérification | oui (`pret_pour_verifier`) | le programme refuse de lui-même toute réponse hors journal |
| C6 un seul dossier | oui, dans `docs/` et `runs/` | n4 ; K8 |
| C7 environnement réduit, clé absente des fichiers | oui | la commande du point 6 demande `bash` (`compgen`) ; celle du point 9 n'affiche qu'un booléen |

## 6. Conditions d'emploi (remplacent C1 à C7 ; toutes vérifiables par programme)

- **K1** — `sha256sum -c` des deux programmes : `95bc46c1…` et `f9ef3695…`.
- **K2** — après `preparer`, avant tout appel, le manifeste porte : `palier` = `flex` ; `lecteur.reasoning_effort` =
  `medium` ; `lecteur.service_tier` = `flex` ; prix 5,0 / 0,5 / 25,0 ; `garde_depense.plafond_usd` = le plafond du mot de
  Lazar (9,30, ou celui qu'il donne après E1) ; `depense_anterieure_usd` = 0 ; 18 envois ; source des prix citant
  `bf211a07`.
- **K3** — une ligne du registre, antérieure à `preparer`, porte le mot de Lazar sur E1 (plafond) et sur E2 (marche à
  suivre après un arrêt au premier appel).
- **K4** — premier appel seul (`--envois-max 1`), puis `bilan` : `anomalies` vide ; `modele_servi` = `gpt-6-astra` ;
  `palier_servi` = `flex` ; `reasoning_tokens ≤ completion_tokens ≤ 32 768` ; coût ≤ pire cas ; **et coût du premier
  appel ≤ (plafond − 1,054) / 16,4**, soit **0,503 USD à 9,30** (0,80 à 14,20). Au-dessus, les 18 appels ne passeront
  pas : ne pas envoyer les 17 autres, nœud. (16,4 = quatorze lots de 5 et trois de 4 comptés 0,8 ; un seul lot est une
  mesure bruitée.)
- **K5** — avant `verifier` et le classement : `bilan` rend `pret_pour_verifier: true`, `clos: 18`, `en_vol: []`.
- **K6** — `envoyer` sous l'environnement réduit du point 6 du rapport ; après l'envoi, commande du point 9 → `False`.
- **K7** — attestation neuve qui nomme OpenAI, scellée ; son empreinte est celle de `attestation.sha256` du manifeste.
- **K8** — `find . -name 'manifeste-envois-v3*' -not -path './.git/*'` rend une seule ligne (plus large que le
  programme). Toute préparation après un premier appel est un nœud, et déclare en `--depense-anterieure-usd` la somme
  des `depense_comptee_usd` des relevés du dossier arrêté.
- **K9** — avant de lire le verdict : dans les deux `lecture-verifiee-L*-v3-1.json`, compter les fiches dont
  `N.motif` vaut « valeur de N illisible ». S'il y en a parmi les fiches désignées ou les témoins publiés, le dire au
  verdict et ne rien désigner sans mot de Lazar (n1).

Conseil, hors condition (c'est un appel réseau sans clé, que je n'ai pas fait ; à la mère d'en juger) : avant le premier
appel payant, un `GET https://api.openai.com/v1/models` sans en-tête d'autorisation, par `urllib` et sous le même
environnement réduit, doit rendre 401 ; il éprouve le mandataire et les certificats sans rien coûter, alors qu'un échec
de transport au premier appel payant coûte un pire cas et le dossier (E2).

## 7. Réserves

- Documentation d'OpenAI non lue : forme du corps, `reasoning_effort`, nom du palier servi (`flex`), sens de `usage`
  restent supposés (réserve r1 de l'auteur) ; K4 les éprouve.
- p1 emploie les volumes du devis (octets estimés par l'auteur sur les tailles des envois de la v1, que je n'ouvre
  pas) : les seuils en dollars bougent de quelques centimes avec les octets réels ; la conclusion E1 ne change pas.
- B2 reste montré sur `http` et la boucle locale ; mes mutants et mes sondes ne prouvent que ce qu'ils visent.
- Pièces de cette relecture : `relecture-courte-lecture-classement-v3-1-outils/` (banc, sondes neuves, quatre
  résultats, scellés) ; mes sondes d'origine sont rejouées par la copie adaptée de l'auteur, relue contre son
  différentiel (fidèle), lancée par moi : dix résultats égaux aux siens.

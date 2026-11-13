# Relecture courte du code v71 du module de la sonde du pilote MR-2 — v1

- **Relecteur** : modèle B, relecteur court **neuf**, sous-agent de la session mère ; autre modèle que l'auteur du code (modèle A).
  Je n'ai écrit ni le code, ni la contre-lecture de la v70, ni le texte. Réserve de lignée : même maison que le développeur.
- **Pièces lues**, chacune égale à son compagnon avant lecture : contre-lecture de la v70
  (`f6bc1b0010dffa0f27757e46e1a20b02aeef847f7287f006a343631fe4121198`, sur `main`) ; sur `prep/pilote-mr2-v1` (tête
  `a5fdfcdf6e0023fdc588d864724748ae2fd11e8a`, récupérée par refspec explicite), dossier `code-v71/` : rapport du développeur
  (`188d7910a941…`), paquet (`733368fc8f80…`), différentiel v70 → v71 (`26affb5b3201…`), patch contre `932a5ff`
  (`47f9fe20fcaf…`), bloc gelé provisoire (`8e76eac8527c…`), journaux ; `registres/go.md` de `main`, lignes 317 et 318.
- **Heures** (`date -u`, 13 novembre 2026) : début 23:23:58 ; chaîne des paquets ≈ 23:24 ; 115 essais 23:25:00 → 23:28:53 ;
  épreuves directes et commande à sec ≈ 23:26 à 23:29 ; dix-huit mutations 23:29:47 → 23:41:16 ; fin : dernière ligne.
- **Aucune dépense, aucun appel de modèle, aucun relais lancé hors des doublures des essais, aucune clé lue ni affichée.**
  Réseau : une récupération git à refspec explicite (la branche du dépôt de travail) ; le commit `94bfd92` vient du clone local
  de l'organisme. Lancements sous `env -i` (PATH, OMP_NUM_THREADS=2, HOME et TMPDIR de mon bac), un processus de calcul à la
  fois, `ulimit -v 6000000`. Aucune lecture des chemins interdits. Aucun refus de permission ni de classifieur.

## 0. Verdict

**Sonde autorisable.**

A-1 et A-2 sont corrigés et tenus par des essais de bout en bout et des mutations tuées ; a-1, a-2, a-3 sont corrigés pour la
sonde ; le registre des lancements refuse un second lancement et n'admet qu'une reprise écrite, une seule fois ; le seul chemin
de la sonde vers un fournisseur passe par la lecture des deux lignes au montant exact, avant tout dossier et tout relais ; la
commande du rapport, jouée à sec, lit GO-2026-11-13-04 et GO-2026-11-13-05 et n'appelle rien.

**Constats : 0 bloquant, 0 majeur, 7 mineurs** (section 6). Aucun n'exige un code neuf avant la sonde ; m-1 demande une lecture
écrite de la mère sur le relevé avant `bloc --releve-sonde`.

## 1. Intégrité (conforme)

| contrôle | résultat |
|---|---|
| neuf compagnons de `code-v71/` | tous « OK » |
| chaîne des paquets | `94bfd92` → v65 (`cef5ea60`) → v66 (`7e415cba`) → v67 (`ab53b7f4`) → v68 (`276b6afd`) → v69 (`2ca17ea3`) → v70 (`932a5ffc`) → **v71 `e7daf32fd090ec6be8331ee1216cec3f061e5f93`** ; chaque paquet égal à son compagnon, `git bundle verify` conforme, parent de `e7daf32` = `932a5ff` |
| ajouts seulement | quatre « A » (module de la sonde, lanceur, essais, banc) ; rien d'avant modifié |
| patch contre `932a5ff` | recalculé : `47f9fe20…`, égal à l'octet |
| différentiel v70 → v71 | recalculé (quatre paires, ordre du rapport) : `26affb5b…`, égal à l'octet |
| module et lanceur | `ff6e992e…` et `c1a2a55c…`, ceux du bloc |
| bloc gelé | `bloc` sans relevé, rejoué : `8e76eac8…`, égal à l'octet au fichier versé |

## 2. Point (1) — A-1 et A-2

**A-1 : corrigé.** Module l. 135-187 et l. 305-331. Relevés du constat, rejoués par les fonctions du module sous la
configuration de l'arbre (règle gelée d'Astra : comprise) :

| relevé d'Astra (sortie / réflexion) | appel 1 | appel 2 | ensemble | issue |
|---|---|---|---|---|
| E2a : 3 / 2, puis 130 / 126, texte de 520 ou de 130 octets | indéterminé | indéterminé | indéterminé | **refusé** |
| E2b : 2 / 0 (ou champ absent), puis 130 / 126, mêmes textes | indéterminé | indéterminé | indéterminé | **refusé** |
| E2c : 2 / 300, puis 130 / 126 | non comprise | indéterminé | non comprise | refusé |
| un appel « comprise », l'autre réflexion > sortie | comprise | non comprise | contradictoire | refusé |
| sain : 302 / 300 (« OK »), puis 256 / 256 sans texte | comprise | comprise | comprise | admis |
| court seul : 2 / 0, puis 256 / 256 sans texte | indéterminé | comprise | comprise | admis |
| octets visibles non lus | indéterminé | indéterminé | indéterminé | refusé |

Les mêmes E2a, E2b, E2c passent par la chaîne entière dans `test_releves_du_contre_lecteur_a1` (texte de 260 octets) ; la
mutation A1h (critère de la v70 rétabli) est tuée chez moi.

**L'écart du développeur au correctif proposé : acceptable, avec la réserve m-1.** Le vote « comprise » exige réflexion > 0 et
sortie − réflexion ≤ octets visibles + 16 < sortie. Il est sûr sous une seule hypothèse, dite au rapport : dans un monde où la
réflexion est ajoutée, la sortie ne compte que le texte visible, au plus un jeton par octet et seize jetons sans octet. Sous
cette hypothèse aucun « comprise » à tort n'est possible ; le vote « non comprise » (réflexion > sortie) n'en dépend pas. La
longueur est lue par la fonction de la commande gelée sur le corps du relais, et relue des pièces par `exiger_releve`. Un
refus du modèle (texte hors du champ lu) rend l'état « échec », donc `statut` faux : pas de trou par là. Par rapport au
correctif proposé : plus strict sur la réponse d'un mot (plus rien n'est supposé), plus permissif en ce que l'appel court
tranche et que le seuil de 32 jetons disparaît. La marge est donc de seize jetons là où le correctif proposé en laissait
environ trente : bords relevés, 19 / 17 sur « OK » est « comprise », 18 / 16 « indéterminé » ; 130 / 126 avec 113 octets
visibles est **admis**, avec 114 octets refusé.

**A-2 : corrigé.** Module l. 80-131. Appel court d'Argon tout en réflexion, `candidatesTokenCount` absent (21 d'entrée,
256 de réflexion, avec ou sans total) : `usage_entier` vrai, 256 jetons comptés, champ noté absent, usage brut gardé tel
quel, verdict « non comprise » égal à la règle gelée, relevé **admis**. Champ présent et nul : refusé (`usage_entier`,
`borne_tenue`), comme la commande. Réflexion d'Argon comprise en vrai : refusé. Sortie plus réflexion au-dessus de 256 :
refusé (`borne_tenue`). De bout en bout : `test_argon_candidats_absents_a2` ; mutations A2a et A2c tuées.

## 3. Point (2) — a-1 à a-3

- **a-1** corrigé : section 4.
- **a-2** corrigé : `exiger_releve` (l. 350-400) exige l'empreinte de la configuration et celles du code de l'arbre qui lit,
  huit appels, puis chaque fait égal aux faits relus de ses pièces (compagnons, corps lié à la réponse brute) ; au bloc et au
  mode réel. Mutations a2a, a2b, a2c tuées. Conséquence dite : le dossier entier de la sonde accompagne le relevé.
- **a-3** corrigé pour la sonde : lanceur l. 357-384 ; mutations a3a, a3b tuées. **Non corrigé pour `jouer`** (hors du
  mandat) : reste à traiter avant le pilote, ou à écrire au texte (rapprochement avec les journaux des relais).

## 4. Point (3) — registre des lancements

Fonctions (bac, registre des décisions factice) et ligne de commande (section 5) : premier lancement admis ; reprise sans
lancement antérieur refusée ; **second lancement refusé** (aussi avec une seule des deux lignes, ou les identifiants
inversés) ; reprise ne citant qu'une ligne, sans les mots, absente, ou sans registre des décisions : refusée ; reprise
conforme admise **une fois**, réemployée refusée ; lancement suivant sans reprise refusé ; registre relatif, dans l'arbre de
l'organisme, dans le dépôt de travail, ou illisible : refusé. Le contrôle vient avant le dossier et les relais ; la
consignation vient quand les relais sont prêts, avant le premier appel. Mutations a1a, a1b, a1c, a1f tuées. Limites : m-2, m-3.

## 5. Points (4) et (5) — dépense sans ligne ; commande exacte à sec

**Chemins.** Le lanceur v71 lance un relais en deux endroits seulement : `sonde` (l. 361), après
`lire_go_de_la_sonde` (l. 348) et le registre (l. 350), configuration de l'arbre sans option ; `jouer` (l. 267), en réel
seulement après `exiger_mode_reel`, qui exige un relevé valide de la sonde (aujourd'hui : aucun). Commande, relais,
proposeurs et configuration sont ceux de la v70, à l'octet. Lecture des lignes sur une copie de `registres/go.md` de
`main` : 04 et 05 **admises** (4.39 et 3.68 USD, échéance 2026-11-30) ; inversées, doublées, 04 avec 03, identifiants
absents, registre privé des lignes 317 et 318 : **refus** ; 04 et 05 présentées comme lignes du pilote : refus. Dans
`registres/go.md`, seules les lignes 317 et 318 portent 4.39 ou 3.68 : la lecture au montant exact ne peut donc s'ouvrir
que sur elles. Mutation D4o tuée. Limite inchangée (a-7 de la v70) : un relais lancé à la main échappe à tout cela.

**Commande exacte du rapport (section 10), à sec.** Le lanceur n'a pas de mode à sec ; j'ai joué la ligne telle qu'écrite,
depuis la racine du dépôt de travail (`main`), les deux chemins hors dépôt remplacés par deux chemins de mon bac,
environnement vide (aucune clé), `lancer_relais` et `appeler` remplacés par une sentinelle qui lève :
1. analyseur seul : options lues telles qu'écrites (`borne_courte` vrai, pas de reprise) ;
2. vraie sous-commande : lignes lues, registre admis, dossier créé, arrêt à la sentinelle au premier relais ; **zéro relais,
   zéro appel**, registre des lancements **non écrit**, relevé partiel à dépense 0, refusé par `bloc --releve-sonde` ;
3. registre portant déjà un lancement : refus, code 2, aucun dossier créé ;
4. ligne 03 à la place de 05 : refus, code 2.
La seconde ligne du rapport (`bloc --releve-sonde`) sur un relevé absent : refus, code 2.

## 6. Constats (tous mineurs)

- **m-1** La sûreté du vote « comprise » tient à la marge de seize jetons sans octet visible, non vérifiée sur une route
  réelle. Avant `bloc --releve-sonde`, la mère lit au relevé, pour chaque appel d'Astra qui vote « comprise »,
  `completion_tokens`, `reasoning_tokens` et `octets_visibles`, et l'écrit au registre ; si sortie − octets visibles
  n'est pas nettement au-dessus de seize (je propose : au moins 64) sur l'appel qui tranche, nœud plutôt que bloc.
- **m-2** Le registre des lancements est un fichier : supprimé, ou un autre chemin donné, un lancement est admis (éprouvé).
  Le chemin du rapport est donc à tenir pour fixe, et son contenu à verser avec le relevé.
- **m-3** Tout arrêt après la création du dossier et avant le premier appel (relais non démarré, clé absente, relais non
  conforme) laisse le dossier de sortie, et pour un arrêt qui n'est pas un refus, un relevé partiel sans appel : la relance avec
  le même `--sortie` est refusée (« dossier de sortie existant »). La ligne n'est pas consommée ; il faut un chemin de sortie
  neuf, pas une reprise. À savoir avant de lancer.
- **m-4** La reprise est reconnue par inclusion de texte : toute ligne unique `| R-NNNN |` du registre des décisions citant
  les deux identifiants et les mots « reprise de la sonde », même pour la refuser, vaut autorisation. Aujourd'hui aucune
  ligne du registre ne porte ces mots (0 occurrence) ; ne les écrire que pour autoriser.
- **m-5** a-3 reste ouvert pour `jouer` ; a-4 à a-8 de la v70 inchangés (dits par le développeur). a-4 est atténué : l'appel
  court peut trancher seul.
- **m-6** Interpréteur : le mode réel exige numpy 2.5.3. Sur cette machine `/usr/bin/python3` le porte, l'environnement
  `.venv` du dépôt porte 2.4.6. La sonde ne contrôle pas numpy ; le pilote, oui. Lancer la sonde et `bloc` par le même
  interpréteur que le pilote évite une surprise.
- **m-7** Le relevé lie les 28 empreintes du code : tout changement du code gelé après la sonde demande une sonde neuve, donc
  une reprise écrite ou des lignes neuves (dit par le développeur ; à compter si a-3 est corrigé pour `jouer` plus tard).

## 7. Ce que j'ai rejoué

- **Essais**, arbre reconstruit, environnement vidé : `115 passed, 195 subtests passed in 231.85s (0:03:51)`, code 0.
- **Mutations**, par le banc du développeur (`--seulement`), essais sains d'abord (code 0, aucun échec) : dix-huit, bilan
  `{"tuée (raison attendue)": 18}`, code 0 — D4n, D4o, A1b, A1c, A1e, A1g, A1h, A2a, A2c, a1a, a1b, a1c, a1f, a2a, a2b, a2c,
  a3a, a3b. Les 28 autres : lues, non rejouées.
- **Épreuves directes** (sections 2, 4, 5), sans réseau : deux scripts de mon bac, non versés (leurs sorties nomment les
  proposeurs) ; leurs résultats sont recopiés ci-dessus.

## 8. Ce que je n'ai pas vérifié

Toute route réelle (forme des réponses, champs omis, comptes de réflexion, prix) ; les 109 essais de la v70 sur la tête v71
(lus au journal) ; les essais ligne à ligne (2 402 lignes : lus par sondage, les essais neufs en entier pour A-1 et A-2) ; le
brouillon du texte ; cœur, proposeurs, audit, commande, relais, déjà contre-lus en v70 et inchangés à l'octet.

## 9. Nettoyage

Retirés par leur chemin exact à la fin : mon arbre de lecture (`git worktree remove`), mon clone de l'organisme, mes copies
de paquets, mon bac d'essais et mes scripts. `/home/user/pilote-v70/organisme` et l'arbre principal non touchés, hormis ce
rapport et son compagnon, écrits **sans commit**.

Fin de la rédaction : 2026-11-13 23:42:19 UTC (`date -u`).

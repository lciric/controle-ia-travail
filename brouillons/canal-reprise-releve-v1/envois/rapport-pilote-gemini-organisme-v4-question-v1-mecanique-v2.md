# Rapport du pilote `pilote-gemini-organisme-v4-question-v1` — partie mécanique et réponse à la question (v2, après audit de symétrie)

Écrit le 25 octobre 2026 (08:55 UTC, v1 ; 09:00 UTC, v2 : les neuf précisions et les trois causes de l'audit de symétrie
§ 6 intégrées ; la v1 est gardée, R12) par la lignée « conv-audit », auteur du préenregistrement
(`prereg/pilote-gemini-organisme-v4-question-v3.md`, scellé `1c5b6f7db90caa1c5527f207fcc034163257459104f4d2b9a01d33df25eed79a`),
à partir des **seules pièces lisibles dès la fin** (plan d'analyse § 3, (a) à (e)) de la branche
`pilotes/gemini-organisme-v4-question-v1` (`84b880a75be152289b1dd9c715e75a25e381c6fb`, liste fermée `A-POUSSER-v1.txt`,
`EMPREINTES-pilote-v1.txt` `c225208877b7cb276a84ac30335df6740e0b2f0a9d0f4cfb2240cefdb3444927`). **Aucun score n'a été lu**
(`ferme.tar.gz`, `2122765b4a7b219ca8baf08e14e07518876602698b3288428c6a65c343e3c253`, reste fermée jusqu'au moment du plan § 3) ;
la partie « scores » (plan § 4) viendra après ce moment, dans une v2 de ce rapport. Pilote descriptif : rien n'est comparé,
rien n'est jugé (critères de lecture gelés, « lectures interdites »). Rien d'opposable (R7). À relire par « session-depot ».

## 1. Ce qui a tourné (LANCEMENT.md `e2dc3fef…`, extrait mécanique `3da08dd8…`)

- Lanceur v3 (`322275c0…`), mode réel, tentative 1, hôte `vm` (conteneur de « session-depot »), root ; copie du dépôt à
  `2d01805a7c314ffd4ab72b46ea359dad483c298b` ; code identique à `cec6dce` (commit et arbre de travail), `4967734` ancêtre ;
  banque `f1387a20…`, mission `bd2c6a15…`, organisme `c5ada335…` (16 fichiers), question `d967b212…` ; registre :
  ligne d'extension `GO-2026-10-24-07` (R-389), dépense consignée, reste déclaré 196,8 USD ; appel de contrôle par espèce
  présent et non vide (`84eb04f8…` ; son statut `OK` est attesté par « session-depot », n° 35, non par les pièces) ;
  essais : 113 passés, 1 désélectionné (`test_sources_reelles_de_moisson_si_reseau`), 19 essais cités passés ; noyau
  nettoyé `68494279…`.
- Course : début 07:49:07 UTC, fin 07:55:48 UTC (code de retour 0), PID 5122 ; isolation `{espaces_noms, reseau, root,
  utilisateur}` toute vraie ; collisionneur conforme ; graine `10826196869519811464` ; `--max-tokens-appel 4096` (aucun
  appel rabattu : l'organisme n'a rien demandé au-dessus de 1 200) ; archive fermée : 1 428 entrées = 1 428 sur disque,
  copies ouvertes retirées ; sortie d'erreur du lanceur **vide** (`e3b0c442…`).
- Dépense : **2,05 USD** (g000 1,98 ; g001 0,07) sur 40 au pire cas.

## 2. Mécanique par génération (extrait ; journaux d'appels `c24d0e55…` et `855bb06a…`)

| | g000 | g001 |
|---|---|---|
| statut d'exécution | `OK`, 352 s | `OK`, 47 s |
| successeur | valide (relance : non) | valide |
| castes planifiées pour les tâches | 1 (`monoculture_analytique`, Fable) | 1 (idem) |
| appels | 123 (1 induction à 1 024 jetons, 2 vérifications à 512, 120 tâches à 640) | 128 (idem + 5 pour la question, **tous à 1 200** : la cinquième caste, l'arbitre, a reçu la consigne de caste ordinaire et non la synthèse à 1 500, parce que le code exige au moins une contribution valide avant l'arbitrage — `principal.py`, `est_arbitre`) |
| statuts | `ECHEC_API` 84, `TRONQUE` 27, `REFUS` 7, `VIDE` 5 ; **`OK` 0** | `ECHEC_API` 127, `TRONQUE` 1 ; **`OK` 0** |
| par espèce | Fable 123 (seule espèce appelée pour les tâches, comme dit d'avance) | Fable 125, Opus 2, Argon 1 |
| `ECHEC_API` | 84, **tous** porteurs du message du fournisseur « credit balance is too low » : le premier (`organisme-0040`, 07:54:38 UTC, après 39 appels servis, 1,98 USD de cumul, 330 s sur 352) reçu dans le flux sous « HTTP 200 APIStatusError », les 83 suivants en « HTTP 400 BadRequestError » ; identifiants de requête tous distincts | 127, même message (Fable 125, Opus 2) |
| `TRONQUE` / `VIDE` | 32, tous à `fin = max_tokens` avec `usage.sortie` = plafond demandé (640 ; 512 ; 1 024) ; **0 à 1,98 caractère visible par jeton de sortie** (5 appels à 0 caractère pour 640 ou 1 024 jetons) | 1 (Argon, `sonde_orthogonale_onsager`, 1 200, `fin = MAX_TOKENS`) : **4 149 caractères visibles pour 1 200 jetons** (3,46 par jeton) : le texte visible remplit le plafond |
| `REFUS` (Fable) | 7 : catégories rendues par le fournisseur `reasoning_extraction` 4, `cyber` 3 (6 tâches, 1 vérification ; le journal ne porte ni identifiant de tâche ni famille : la famille des tâches refusées n'est pas lisible ici) | 0 |
| jetons | Fable : 90 145 entrée, 21 479 sortie | Argon : 1 391 entrée, 1 200 sortie |
| durées des appels | 0,17 à 17,3 s, somme 351,6 s | 0,17 à 20,5 s, somme 46,3 s |
| appels simultanés au plus | 1 (aucune bascule en parallèle) | 1 |
| `n_reponses_test` (réponses valides) | **0** | **0** |
| `memoire_isvd.json` | 1 477 octets | 1 477 octets |
| empreinte de l'archive de l'organisme | `6853496e…` | `f52aa3b2…` |
| erreurs consignées par l'organisme | aucune | aucune |

Identité du code de g1 avec g0 : à vérifier à l'ouverture de l'archive fermée (plan § 3), comme prévu.

## 3. La réponse à la question ouverte (g001, `reponse-question-g001.md`, `af091e785d141cc072c1cf24df70bf2a06cd6507d4208eb8a4aeee882bd31898`, 5 676 octets)

Critère de lecture 2 (v) : réponse lue ; c'est le **texte d'abstention** de l'organisme. Tel quel (sections 1 à 4) :

> **1. Réponse finale** — Aucune caste n'a pu produire de réponse valide (tous les appels ont échoué ou le budget restant
> était épuisé). Conformément au contrat, aucune réponse factice n'est générée.
> **2. Raisonnement qui y mène** — Indisponible en l'absence d'appel ayant retourné le statut `OK`.
> **3. Ce qui vient de quelle caste** — Aucune contribution reçue.
> **4. Ce dont l'essaim n'est pas sûr** — Incertitude complète suite à l'échec des appels au noyau.

Structure mécanique (bloc `--- ORGANISATION ---`, dires de l'organisme) : 5 appels tentés, 0 OK, 5 échecs ; 5 castes
planifiées dans l'ordre dit d'avance (Fable `monoculture_analytique`, Opus `monoculture_croisee`, Argon
`sonde_orthogonale_onsager`, Fable `critique_adversariale_limites`, Opus `arbitre_synthese_contradictoire`) ; votes
« ECHEC_APPEL » (4 × `ECHEC_API`, 1 × `TRONQUE`), confiances 0 ; mémoire spectrale : « Aucune memoire anterieure
disponible », 0 exemplaire. Rien n'y est à vérifier (aucune référence, aucun chiffre de l'essaim).

## 4. Réserves (R4 ; déclencheur du critère 1 : plus de 20 % d'appels hors `OK` aux deux générations → audit de symétrie)

1. **Crédit du fournisseur Anthropic épuisé** pendant g000, au 40e appel sur 123 (07:54:38 UTC, 330 s sur 352, 1,98 USD
   de cumul ; « credit balance is too low ») : 84 puis 127 échecs, Opus compris ; aucun appel Anthropic servi ensuite. Le noyau `cec6dce` ne s'arrête pas sur un 400 (il s'arrête sur un 402 : CL5-07, limite connue avant la
   course) ; corrigé depuis par « session-depot » (`appels.credit_epuise`, R-395, `90595ffb`), hors du code de ce pilote.
2. **Aucun appel servi n'a donné de réponse valide, indépendamment du crédit** : sur 39 appels servis par Fable à g000,
   27 `TRONQUE` et 5 `VIDE` au plafond demandé par l'organisme (640, 512, 1 024 jetons), 7 `REFUS`. Cause probable, **à
   vérifier par une mesure directe** (proposée par « session-depot ») : l'appelant du noyau sert les espèces Anthropic
   avec `output_config={"effort": EFFORT}` (constante du collisionneur, « high » d'après son code, non reproduite dans les
   pièces du pilote) et sans bloc de réflexion explicite (réflexion adaptative) ; des jetons de sortie non textuels sur
   chaque appel Fable servi (0 à 1,98 caractère par jeton) sont compatibles avec une réflexion comptée dans `max_tokens`
   et, sans outil, rien d'autre n'explique des jetons sans texte ; à 640 jetons, la réponse visible est vide ou coupée
   avant l'objet JSON attendu par l'organisme. **L'appelant calcule les types de blocs (`types_blocs`) mais le journal du
   noyau ne les garde pas : l'information existait et a été perdue — défaut du noyau à corriger.** La troncature d'Argon à
   g001 (1 200 jetons) a une **autre cause** : 4 149 caractères visibles, le texte remplit le plafond (consigne en trois
   parties puis objet JSON en fin). Co-cause côté organisme, annoncée par le préenregistrement (« `TRONQUE` attendu comme
   mode d'échec le plus probable ») : objet JSON exigé **après** une analyse ouverte, plafonds de 640, 512 et 1 024 jetons,
   tout texte non `OK` jeté sans chercher d'objet JSON dedans, et aucun arrêt sur échec répété (210 appels après le
   premier refus de crédit, ≈ 0 USD, ≈ 1 min) ; cascade : l'induction `VIDE` laisse `regles_induites` vide dans les 122
   consignes suivantes. Suite donnée : le contrat dira ce fait aux organismes
   (décision de Lazar, 25 octobre 09:26 Paris) ; faits transmis à Gemini pour une v5.1 (même décision).
3. **Refus** de Fable : 7 sur 39 appels servis (18 %), catégories rendues `reasoning_extraction` et `cyber` ; le lien
   avec la consigne (un champ `raisonnement` demandé dans l'objet JSON) et avec la famille des tâches (contrôle de
   délégation) est une **conjecture** : le journal ne porte ni identifiant de tâche ni famille. Comptés en échec par
   l'organisme, aucune reformulation (règle de Lazar). À surveiller pour les courses à venir (mêmes espèces, même banque).
4. **CL5-01**, dite avant la course (option (a), Lazar 08:14 Paris) : sur cet hôte, la copie du dépôt et l'arbre du code
   étaient lisibles par l'utilisateur de l'organisme ; la garde « lecture hors des sorties → refus par le système » du
   texte scellé est surestimée pour ces chemins ; l'organisme (code figé, lu en entier) ne lit que ses dossiers ; aucune
   mesure n'est exposée en fait. Corrigé depuis dans le noyau (`ESSAIM_M3_CACHER`, `224de13`), hors du code de ce pilote.
5. **Non-reproductibilité** du code de Gemini, trouvée après la course sur la v5 et vraie de la v4 :
   `mitose_spectrale.py` l. 14 parcourt un `set` ; l'ordre des « termes saturés » à égalité dépend de la graine de hachage
   de Python, que la graine de la course ne fixe pas ; deux courses à la même graine ne servent pas toujours les mêmes
   consignes (sans effet ici : aucune consigne de caste n'a été servie avec une mémoire non vide).
6. **Imprécision de forme du texte scellé**, connue avant la course : « le script de lancement, en mode simulation »
   pour la simulation de la v2 (dite au canal n° 30).

## 5. Ce que ce pilote dit et ne dit pas

- Il dit : la chaîne réelle a tourné de bout en bout sous le lanceur v3 (vérifications, isolation, archive fermée, liste
  fermée poussée) ; les gardes de dépense ont tenu (2,05 USD) ; l'organisme a écrit ses fichiers, son successeur et sa
  réponse d'abstention malgré 251 échecs d'appels sur 251 ; deux défauts de la chaîne sont apparus (arrêt sur crédit
  rendu en 400 ; plafond de sortie « réflexion comprise » non dit au contrat), corrigés ou en cours.
- Il ne dit rien : des scores (`n_reponses_test` = 0 aux deux générations ; la partie « scores » se lira telle quelle au
  moment prévu), de la
  conception de Gemini sur les deux familles, de l'avis de son essaim sur la question (texte d'abstention), de H-E1, de
  H-G1, des organismes auto-écrits. Pas de seconde course sous ce texte (plan § 1) ; la décision de Lazar sur une
  reprise (nouveau préenregistrement) ou l'abandon est en cours (défaut sous 48 h : abandon, le second pilote portant
  la question nouvelle à la v5 corrigée de Gemini).

## 6. Audit de symétrie (critère 1) — fait, 25 octobre 2026, 08:55 UTC

Déclenché mécaniquement (plus de 20 % d'appels hors `OK` ; `n_reponses_test` = 0). Fait par un **sous-agent neuf**
(ni auteur du préenregistrement ni de la v1 de ce rapport), sur les seules pièces lisibles (a) à (d), le texte scellé,
le code de l'organisme et l'extrait de l'appelant ; sans relance. Verdict : **« rapport exact sur tous les comptes »**
(aucun écart, même d'une unité : appels, statuts, espèces, rôles, plafonds, jetons, durées, coûts, dates, empreintes,
structure de la réponse ; coûts par appel égaux au tarif 10/50 ; 32/32 `TRONQUE`/`VIDE` à `usage.sortie` = `max_tokens` ;
aucun chevauchement d'appels ; manifeste égal à la ligne de commande scellée ; essais 113 + 0 + 1 = 114 ; texte
d'abstention identique au code), **à préciser sur neuf points**, tous repris dans cette v2 : le premier échec de crédit
sous « HTTP 200 » (§ 2) ; « tôt » daté et compté (§ 4.1) ; le statut de l'appel de contrôle non attesté par les pièces
(§ 1) ; la valeur de `EFFORT` non reproduite (§ 4.2) ; la troncature d'Argon, cause distincte (§ 2, § 4.2) ; l'arbitre à
1 200 et non 1 500, et pourquoi (§ 2) ; les liens refus–consigne et refus–famille, conjectures (§ 4.3) ; l'adjectif sur
des scores non lus, retiré (§ 5) ; les types de blocs calculés et non journalisés (§ 4.2). **Trois causes que la v1 n'avait
pas** : (i) **l'appel de contrôle vérifie qu'un appel passe, pas que le solde couvre le devis** (≈ 10 à 14 USD attendus,
40 au pire ; le crédit a tenu 1,98 USD) — garde absente de la liste d'arrêt du texte scellé, le dispositif était trop
indulgent envers lui-même ; à ajouter aux préenregistrements suivants (contrôle du solde ou dépense d'essai avant le
départ) ; (ii) la conception de l'organisme comme co-cause des troncatures (§ 4.2) ; (iii) l'absence d'arrêt sur échec
répété (§ 4.2). Lectures : rien d'interdit lu avant le moment du plan § 3 ; le canal latéral (`contexte.json`) ni calculé
ni cité. Non vérifiable depuis les pièces : le statut de l'appel de contrôle ; `A-POUSSER-v1.txt`, `EMPREINTES-pilote-v1.txt`
et `ferme.tar.gz` (hors dossier d'audit) ; l'identité du code ayant tourné avec les fichiers de la v4 (tailles concordantes
seulement) ; `reponses_test.json` absent de la liste des fichiers de travail de l'extrait alors que le code l'écrit toujours
— à voir à l'ouverture de l'archive fermée (exclusion de l'outil d'extraction, ou déplacement par le noyau). Le retour
de l'audit est joint tel quel : `audit-symetrie-pilote-gemini-v4-question-v1.md`.

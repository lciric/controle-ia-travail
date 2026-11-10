# Contre-lecture 2 (courte) — plan de vérification hors de nous du bras d'attaque, brouillon 2, et projet de courriel v2 — v1

- Date : 10 novembre 2026, début 11:33 UTC, rédaction 11:37 UTC (`date -u`).
- **Contre-lecture par un sous-agent neuf** (R2) : je n'ai écrit ni le plan, ni le courriel, ni la contre-lecture 1, ni
  aucune pièce citée. Lecture seule ; seul ce fichier est écrit. Aucun commit, aucun envoi, aucun contact, aucune
  dépense, aucune requête réseau. Non scellé par moi.
- Réserve de validité : j'ai reçu d'office le `CLAUDE.md` du dépôt (`b4cbc66a…`).
- Outils : `sha256sum`, `python -m controle_ia.scellement verifier`, `git show`, `git log`, `sed`, `grep`, `cat -n`.

## Pièces relues et empreintes

| Pièce | Lu | Empreinte recalculée | Contrôle |
|---|---|---|---|
| `docs/notes/verification-externe-bras-v1/plan-verification-externe-bras-v1-brouillon2.md` | en entier | `4e0a97ae026fde12bae387aa63ccb40b5650872c489ff1083e43e31b228d65b4` | = attendue, compagnon conforme (`verifier` OK), au début et à la fin |
| `docs/notes/verification-externe-bras-v1/projet-courriel-replication-externe-v2.md` | en entier | `23325ff84298e22c8abdb2dbdf047cfd8845c90c4366a13e2c36298ddcea0c87` | idem |
| `…/contre-lecture-plan-verification-externe-v1.md` [CL] | en entier | `b6f88afc…` | compagnon conforme |
| `…/plan-verification-externe-bras-v1-brouillon1.md`, `…/projet-courriel-replication-externe-v1.md` | courriel en entier ; plan par différentiel | `4e88118c…`, `7ea1cc4e…` | compagnons conformes |
| `prereg/bras-attaque-regle-v1.md` [R] | en entier | `88418df0…` | compagnon conforme |
| `prereg/bras-attaque-regle-v1-addendum-1.md` | en entier | `edfa69a2…` | compagnon conforme ; commit `9c5e6631` (10:54 UTC) |
| `prereg/temoin-attaque-publiee-bailey-v1.md` [TB] | l. 1-55, 260-270, 325-395 | `fb6c2f34…` | |
| `src/controle_ia/temoin_bailey/analyse_v1.py` [AB] | empreinte seulement | `f14f91d3…` | = au commit `ea55481b` |
| Passations du 10 novembre : 0852 [GO4], 1018 [D1018], 1050, 1118, 0948, 1112 | en entier | `c90ad8f4…`, `8a2c8b71…`, `def13a65…`, `5ae71cf3…`, `65201009…`, `7a92e7d0…` | |
| Passation 1037 [E1037] | l. 60-80 | `e4444066…` | |
| Passation 0834 | recherche « dépôt », « tiers » | `bb8854b6…` | |
| [N2], branche `origin/claude/upbeat-cray-dmauvv`, par `git show` | l. 6-12 | `bba97a1a…` | |
| Même branche : `registres/passations/2026-11-10-1033-depot-tiers-manifeste-v3-regle-bras.md` | en entier | `54ab71dc…` | |
| Même branche : `livrables/osf-manifeste-v3/manifeste-v3.json` | en-tête, références, entrées de [R] et [TB], recherche de N-061 à N-066 | `576b88cc…` | = celle de l'addendum 1 |
| Même branche : `livrables/osf-manifeste-v2/manifeste-v2.json` | nombre, références, dossiers seulement | — | |
| N-053, N-054, N-056, N-057, N-060 v3, N-061, N-062 | passages cités | `2204256d…`, `c8a00b3f…`, `3592c1e9…`, `42180088…`, `2b448f69…`, `b2ae4417…`, `63f42690…` | tous = table « Pièces » du plan |
| `livrables/osf-manifeste-v1/LISEZMOI.md`, `manifeste-v1.json` | l. 9-30 ; empreinte | `d9b50823…`, `dd87b23e…` | |
| `registres/go.md` | l. 170, 256, 260 | `097b09ca…` | |
| `registres/decisions.md` | l. 1538, 1715, 1792, 500 premiers caractères de chacune | `1e35073e…` | l. 830-837 jamais affichées |
| `registres/etat.md` | l. 361 seulement | `ae1f3136…` | |
| Catalogue de la pièce 3, ses deux brouillons et sa contre-lecture ; antériorité [AN] et brouillon 2 | empreintes seulement | `a0c6e3a6…`, `c304d6a2…`, `c3489a08…`, `7f7b0cc5…`, `db02898c…` | |

**Non lus, par consigne** : le coffre ; `docs/notes/bras-attaque/`, `docs/notes/programme-et-4-familles-evasion/`,
`diag/` ; tout résultat de sonde, de moniteur ou d'attaque ; les épisodes d'épreuve et les items de l'étiqueteur ;
`registres/decisions.md` l. 830-837 ; `registres/etat.md` hors l. 361 ; l'index du bras (`registres/index-bras-attaque-v3.md`) ;
le fichier de seuils déposé le 8 novembre. **`docs/notes/integration-bras-attaque-v1/`** : aucun contenu affiché ; j'ai
seulement calculé, par `git show … | sha256sum`, l'empreinte de [PD] (`b1a96e4d…`), de [RJ] brouillon 4 (`3245a617…`) et
du brouillon 5 (`527a3e7e…`) à la pointe de `origin/claude/upbeat-cray-dmauvv` (`8e1e751d`, 11:22 UTC). Tout ce que le
plan affirme du **contenu** de [PD] et de [RJ] reste donc non vérifié par moi (voir dernière section).

## Verdicts

- **Plan, brouillon 2 : scellable après corrections** (P-1 à P-8 ci-dessous). 0 bloquant. Les dix-sept points de [CL]
  sont traités ; les écarts déclarés sont justifiés. Mais le plan a été écrit sur un état du programme dépassé avant son
  commit (11:09 UTC) : dépôt du manifeste v3 chez le tiers à 10:32 UTC, addendum 1 de [R] (10:54 UTC), règle du jeu
  scellée en brouillon 5, catalogue en brouillon 2, puis, après le commit, les décisions de Lazar sur Bailey (10:48 et
  11:18 UTC).
- **Courriel v2 : scellable après corrections** (C-1 à C-3) **comme projet ; non envoyable tel quel** : il porte
  volontairement des crochets et une liste « À décider » de 15 points, qui sont des décisions de Lazar. Aucune sortie de
  quarantaine, rien de faux sur l'état du programme, rien qui engage Lazar hors crochets au-delà de ses décisions.

## 1. Traitement des points de [CL]

| Point | Plan b2 | Courriel v2 | Remarque |
|---|---|---|---|
| CV-1 | traité (§ 1.2) | — | faits exacts au 8 novembre ; le dépôt du 10 novembre manque (P-1) |
| CV-2 | traité (§ 6) | — | conforme à N-053 point 4, N-060 v3 point 1, [R] l. 199-208 |
| CV-3 | traité (§ 5) | — | renvois à [TB] vérifiés (l. 1, 35, 40, 50, 266, 340, 355, 376-390) ; « Manque » dépassé (P-4) |
| CV-4 | traité, écart justifié (§ 1.1, V-3) | — | l'écart est juste : une date « au plus tard » de l'ouverture ne donne pas l'ordre. Mais [LI] l. 18-19, cité en appui, dit le contraire (P-6) |
| CV-5 | traité par renvoi (D-1, D-2) | — | acceptable : procédures renvoyées à [PD] |
| CV-6 | traité (§ 2) | — | conforme à N-061 l. 12-15 |
| CV-7 | traité, écart justifié (§ 3.1) | — | conforme à N-057 points 2, 4, 5 |
| CV-8 | traité, étendu (§ A, § 3.2) | — | |
| CV-9 | traité, écart justifié (§ 1.3) | — | renoncer à reformuler le nœud 7 est la bonne solution ; référence à mettre au brouillon 5 (P-2) |
| CV-10 | traité (§ 1.2, 1.3, 1.4) | — | |
| CV-11 | traité (§ 3.2) | traité | seconde option refaite à raison (l'évasion exige nos alertes) |
| CV-12 | traité (§ 3.2) | traité | conforme à [D1018] l. 24-34 et [N2] l. 8-10 ; catalogue cité dans un brouillon dépassé (P-5, C-1) |
| CV-13 | traité | traité | 15 points « À décider » ; temps corrigé (« sealed », moniteurs « frozen before any attack ») |
| CV-14 | — | traité | les quatre textes repris (l. 46-48, 52-53) |
| CV-15 | traité (§ 7) | — | ligne 1 dépassée (P-1) |
| CV-16 | traité, écart justifié (§ 4) | — | l'écart de calendrier de la réanalyse publique est juste ([R] l. 98-100, 156-157, 321) |
| CV-17 | traité par renvoi (D-3 à D-5) | — | D-3 dépassée (P-3) |

Bilan : 17 traités ; 4 d'entre eux à remettre à jour sur des faits survenus depuis (CV-1, CV-3, CV-15, CV-17).

## 2. Citations, chiffres et empreintes (R6, R7)

- **Toutes les empreintes de la table « Pièces »** que j'ai pu recalculer sont exactes ([B1], [M1], [M2], [CL], [R], [TB],
  [AB], [D1018], [GO4], [N2], [E1037], [CAT] brouillon 1, [AN], [LI], [MV1], N-053 à N-062, [GO], [DEC], [ET]). L'instantané
  `94c429f4…` du courriel au commit `e5067857` : exact. [PD] et [RJ] : empreintes exactes à la pointe de la branche,
  contenu non lu.
- **Renvois de lignes vérifiés et exacts** : [R] l. 29, 59, 65-66, 74, 90-96, 98-101, 113, 120, 140, 146-153, 156-160,
  178-182, 199-208, 217-220, 232, 238-244, 254-266, 278-279, 284, 301-303, 309-312, 321, 338, 364-366, 374, 394-399 ;
  [D1018] l. 14-23, 17-18, 24-34 ; [GO4] l. 21-22, 30, 35 ; [N2] l. 8-10 ; [E1037] l. 71-72 ; [GO] l. 170, 256, 260 ;
  [DEC] l. 1538 (R-1580), 1715 (R-1757), 1792 (R-1834) ; [ET] l. 361 ; [LI] l. 9-12, 28-29 ; [MV1] 118 fichiers, `a364e947`.
- **Chiffres neufs** : aucun chiffre d'article (R7 sans objet). Les chiffres du plan (100 épisodes par point, h ≥ 500,
  32 octets de sel, 118 fichiers, 15 points) renvoient à [R], [MV1] ou sont des propositions déclarées.
- **Affirmations de commit** : `86549bb6` (10:21:49 UTC) et `ea55481b` (10:41 UTC) exacts. `020e1bcd` (lecture de [PD])
  n'est plus dans le magasin local d'objets : invérifiable ici, sans effet puisque l'empreinte de [PD] est inchangée.
- **Défaut** : la dernière section du plan dit que le brouillon 2 et [M2] n'ont pas de compagnon `.sha256` ; ils en ont
  un, commité en `8ea7bf38` (11:09 UTC) (P-7).

## 3. Le courriel v2

**Quarantaine (N-057 points 2 et 6 ; N-056 point 6)** : rien n'en sort. Ni recette, ni paramètre, ni contenu du coffre,
ni résultat de sonde ou de moniteur, ni mode nommé (« diffuse sabotage » est la catégorie du programme), ni nom de
procédure, ni nom de fichier, ni l'existence des cellules. Le paragraphe de l'échelon 3 décrit des règles (liste fermée,
substitutions de rôle, statistique des verdicts d'un lot, plafond, politique figée), pas une procédure. « A reproduced
published attack » ne nomme pas Bailey.

**État du programme** : exact. Règles scellées ([R]) ; moniteurs gelés avant toute attaque ([R] l. 95-96) ; ce qu'ignore
l'attaquant informé ([R] l. 98-99, 321) ; témoins ([R] l. 228-266). L'horodatage reste entre crochets, à raison, le
nœud 7 étant ouvert (P-1).

**Engagements** : hors crochets, seules des règles déjà scellées ou décidées. « We would not share any of our own attack
material » découle de N-057 point 2. Deux réserves de forme : C-2 (ce que l'équipe reçoit en retour, et quand) et C-3
(la phrase sur les épisodes naïfs et le témoin « honest-only », hors crochets, alors qu'elle n'a de sens que si Lazar
retient l'offre).

**Envoyable tel quel par Lazar ? Non.** À remplir ou trancher avant envoi :
1. destinataire, nom (`Dear [name]`) et adresse ; le choix de l'équipe (conditions d'indépendance du plan, § 3.2 : aucun
   lien avec nos concepteurs ni avec les auteurs des ressources des § 2 et 5, dont l'équipe de Bailey, désormais en
   contact avec Lazar) ;
2. signature : nom complet, affiliation, adresse (l. 81-82) ;
3. horodatage du premier paragraphe : garder ou retirer le crochet (point 2 de « À décider ») ;
4. niveau offert, et donc garder ou retirer le paragraphe de l'échelon 3 (points 3-5) ;
5. le mois (`around [month]`, point 14) ;
6. les crochets de la remise (protocole, conceptions, agent) et la relecture de ce qui est remis (points 6-8) ;
7. option (i) ou (ii) de lecture de leurs épisodes (point 9) ;
8. termes de garde et de publication de leurs attaques (point 10) ;
9. reconnaissance ou cosignature ; ordre de scellement (points 11-12) ;
10. la phrase sur la revue de sécurité externe : à retirer tant qu'aucune pièce écrite n'existe (point 13) ;
11. enlever ensuite tous les crochets et la ligne « [Keep this paragraph only if …] ».

## 4. Corrections

### Plan (P-1 à P-8)

**P-1 — à corriger — le dépôt du 10 novembre manque (§ 1.2, § 1.3, § 7 ligne 1, § 8 point 1).**
Source : addendum 1 de [R] (`edfa69a2…`, § 2) ; passation `2026-11-10-1033-depot-tiers-manifeste-v3-regle-bras.md`
(branche `claude/upbeat-cray-dmauvv`, `54ab71dc…`) ; passation 1112 l. 61.
- § 1.2, ajouter après le second dépôt :
  > Troisième dépôt le 10 novembre à 10:32:17 UTC, sous la même autorisation, par la session de dépôt : manifeste v3
  > (`livrables/osf-manifeste-v3/manifeste-v3.json`, `576b88cc…`, branche `claude/upbeat-cray-dmauvv`), 167 fichiers de
  > `prereg`, `docs/decisions` et `docs/verdicts`, lus sur deux références dont `origin/claude/compassionate-meitner-d4ryyk` ;
  > il porte [R] et [TB], et N-061 à N-066 ; empreinte relue par l'interface égale à l'empreinte locale (addendum 1 de [R],
  > `prereg/bras-attaque-regle-v1-addendum-1.md`, `edfa69a2…`, § 2). Le projet reste privé et non gelé.
- § 1.3, remplacer la phrase « Reste à prouver, et [R] l'exige : l'empreinte de [R] déposée avant toute course » par :
  > L'empreinte de [R] est déposée en privé depuis 10:32:17 UTC (manifeste v3). Reste à Lazar de dire si son « go OSF »
  > du 5 novembre vaut le mot sur le nœud 7 qu'exige [R] l. 90-91 (lecture de l'auteur de l'addendum 1, à confirmer) ;
  > sinon le nœud 7 reste ouvert et aucune course ne part ([R] l. 374). Par la tranche B de [PD], chaque gel suivant est
  > déposé avant l'ouverture qu'il encadre.
- § 7, ligne 1 : « Dépôt de l'empreinte de [R] et de [TB] » devient « fait le 10 novembre à 10:32 UTC (manifeste v3,
  privé) ; reste le mot de Lazar sur la valeur de ce dépôt pour l'engagement 1 ».
- § 8, point 1, ajouter : « et dire si le « go OSF » du 5 novembre vaut ce mot pour le dépôt privé du 10 novembre ».

**P-2 — à corriger — [RJ] est scellée en brouillon 5.** Table « Pièces », ligne [RJ], ajouter :
> scellée depuis en brouillon 5 (`regle-du-jeu-et-integration-v1-brouillon5.md`, `527a3e7e…`) ; selon l'addendum 1 de
> [R] (§ 1), neuf lignes changent, aucune du § 5 : les renvois au nœud 7 valent pour le brouillon 5.

**P-3 — à corriger — D-3 est dépassée.** Remplacer D-3 par :
> **D-3, portée (CV-17).** Le manifeste v3 lit déjà la branche de cette session et porte [R] et [TB]. Restent hors des
> dossiers que lit le script ([LI] l. 9-12) : les notes de décision que [R] cite comme faisant foi (l. 38-41), [D1018],
> les notes de décision de Bailey (1050, 1118) et l'index du bras (empreinte seule). À ajouter au manifeste suivant, ou
> par un fichier d'empreintes à part.

Et dans D-6 : « les 118 chemins de [MV1] » devient « les chemins des manifestes v1 à v3 ».

**P-4 — à corriger — le § 5 ignore les décisions de Lazar sur Bailey (10:48 et 11:18 UTC).** Dans « Manque », remplacer
les puces 1 et 2 par :
> - la ligne de GO de calcul citant le devis v4, B = 75 USD, à réécrire par la session de dépôt (note
>   `registres/passations/2026-11-10-1118-decision-lazar-go-autonome-bailey.md`, `5ae71cf3…`, point 2) ;
> - la licence : les auteurs ont donné leur accord (même note) ; leur réponse écrite, datée, reste à verser au dépôt,
>   comme preuve exigée par N-061 (point 1) ; le GO du modèle est lu dans le « go autonome », à confirmer (point 3) ; la
>   valeur pour le témoin, à confirmer (point 4).

Dans « Existe », ajouter : « une version 2 de l'analyse et des gardes (`analyse_v2.py`, commit `6f11d0cb`), à relire en
différentiel ». Mettre à jour § 7 (ligne du témoin) et § 8 point 9 de même.

**P-5 — à corriger — le catalogue est en brouillon 2.** Table « Pièces », ligne [CAT] : citer
`catalogue-procedures-echelon-3-v1-brouillon2.md` (`c304d6a2…`), décisions de Lazar appliquées, non scellé ; le
brouillon 1 (`a0c6e3a6…`) reste cité comme antérieur.

**P-6 — à corriger — [LI] dit plus que l'horodatage ne prouve.** § 1.1, après le renvoi à [LI] l. 16-20, ajouter, et
porter en demande D-7 à [PD] :
> [LI] l. 18-19 dit qu'une pièce déposée « a été écrite avant la lecture du résultat qu'elle encadre, si la date de dépôt
> précède le résultat » : c'est vrai seulement si la date du résultat est elle-même établie hors de nous comme un « pas
> avant » (V-3). **D-7** : la version suivante du `LISEZMOI.md` le dit.

**P-7 — à corriger — compagnons.** Remplacer la dernière puce du § 9 par :
> Ce brouillon et [M2] ont reçu leurs compagnons `.sha256` au commit `8ea7bf38` (11:09 UTC) ; ils restent des brouillons
> non scellés au sens de R1 jusqu'au scellement de la pièce 4.

**P-8 — à préciser — références distantes.** § 9, troisième puce : écrire que `020e1bcd` n'est plus résoluble
localement, que la pointe lue à cette contre-lecture est `8e1e751d` (11:22 UTC), et que [PD] y garde l'empreinte
`b1a96e4d…`, toujours sans compagnon.

### Courriel (C-1 à C-3)

**C-1 — à corriger — catalogue.** « À décider », point 5 : remplacer
`catalogue-procedures-echelon-3-v1-brouillon1.md`, `a0c6e3a6…` par `catalogue-procedures-echelon-3-v1-brouillon2.md`,
`c304d6a2…`.

**C-2 — à préciser — ce que l'équipe reçoit, et quand.** Option (i) du texte anglais, remplacer « and you would receive
the evasion curve and failure classes of your episodes » par :
> and, once all your sealed episodes have been read, you would receive the evasion curve and the failure classes of
> your episodes, never scores or thresholds

Raison : un retour avant la fin de sa participation serait un retour hors plafond compté ([R] l. 98-100 ; plan § 4.1).
Pour l'option (ii), ajouter à la fin du crochet : « ; you would receive the resulting evasion curve on the same terms ».

**C-3 — à préciser — phrase hors crochets qui suppose l'offre retenue.** Mettre entre crochets « The same rules also mean
… and an honest-only control. » et ajouter « [at least 100 attack and 100 naive episodes per point, and at least 500
honest-only episodes — to be confirmed] » : la charge pour l'équipe ([R] l. 266, 284) doit être visible avant qu'elle
réponde.

## Ce que je n'ai pas pu vérifier

- Le contenu de [PD] et de [RJ] (cloison) : la citation « pas de défaut à 48 heures » ([RJ] § 5), les options et la
  recommandation du nœud 7, l'erreur signalée par D-0 dans [PD] § 2, les tranches A et B.
- Le manifeste v2 au-delà de son en-tête ; la date de son dépôt, s'il a été déposé.
- Le fonctionnement de l'Open Science Framework, des services d'horodatage et des balises publiques d'aléa ;
  SHADE-Arena, Liars' Bench, NARCBench (aucune requête réseau).
- La réponse écrite des auteurs de Bailey (non versée au dépôt à 11:37 UTC).
- Qu'aucune décision plus récente que 11:18 UTC ne touche le nœud 7 ou la pièce 4.

# Contre-audit des réglages des appels aux modèles de Google, version 1

Écrit le 21 novembre 2026 vers 18:30Z par un contre-auditeur neuf, Claude Opus 5.5 (`claude-opus-5-5`), qui n'a écrit ni
l'audit ni aucun des programmes contrôlés. Pièce contrôlée : `audit-reglages-google-v1.md` (sceau vérifié, conforme).
Règle de référence : `CLAUDE.md`, sections « Appels à Carbon » (GO-2026-11-21-47) et « Appels aux modèles de Google »
(GO-2026-11-21-71). Pièce de travail, en lecture seule : aucun envoi, aucune clé lue, aucun commit, aucun programme
modifié ; rien lu sous `donnees/`, `archives-reponses-modeles/`, `brouillons/ii-b-saboteur-budget-v1/`, ni aucun fichier
« consigne-privee » ou « conception-ii-b ». Je n'ai pas lancé les essais des programmes.

Ordre suivi : inventaire refait de mon côté et scellé **avant** de lire la liste de l'audit
(`brouillon-inventaire-contre-audit-v1.md`, `ab6a0d81…`, 18:08Z), puis lecture de l'audit, puis comparaison et contrôle
ligne à ligne.

## 1. Verdict

**L'audit tient sur le fond : aucun programme en service ne satisfait la règle du 21 novembre.** Je ne le réfute sur
aucun de ses constats contrôlés ; il ne prononce aucun « conforme », donc aucun « conforme » n'est à retirer. Ses phrases
partielles « le reste oui » et « aucun repli » sont justes là où je les ai vérifiées.

**Mais il est incomplet sur quatre points :**

1. **Deux programmes écrits après lui** (18:04Z) ne sont pas dans son inventaire : la commande d'envoi des consultations
   de la famille réservée (`envoi_v1.py`, Carbon et Neon, prête sous GO-2026-11-21-68, rien encore envoyé) et la
   révision 8 du collisionneur v9, qu'il a choisi de ne pas ouvrir. **La commande d'envoi est à corriger avant tout
   envoi** (section 4.1).
2. **Sa méthode d'inventaire est aveugle** à tout ce que cache `.git/info/exclude` (`git grep` et `git ls-files` ne le
   voient pas) et aux scripts de coquille (motif `'*.py'` seul). Les programmes que j'ai trouvés ainsi sont listés en
   section 2.
3. **Il sous-estime l'écart de plafond des lanceurs d'idéation** : il ne chiffre que les juges à 0,60 USD. Sous la
   commande d'Argon v3d, tout plafond de session au-dessous d'environ 1,34 USD plus le coût de l'entrée ne peut pas laisser
   16 000 jetons de texte ; les proposeurs d'Argon à 1,3 USD (regard ou raisons, bassins étroits, conception propre)
   échouent donc **à chaque appel**, même avec une entrée nulle (section 3.3).
4. **Il manque une réponse coupée acceptée comme réponse** (commande du tour fermé, hors service) et une réflexion nulle
   admise par réglage (`--reflexion 0`, `--provision-pensee-jetons 0`) (section 5).

Un point de lecture, à soumettre à Lazar (section 6) : la page de Google que cite la révision 8 du collisionneur dit que
`thinkingBudget` est déprécié chez Gemini 4 et se ramène, seul, au niveau le plus proche. Si c'est vrai, « budget prévu »
ne règle pas la réflexion, et la lettre de la règle (« niveau le plus haut admis **ou** budget prévu ») laisse passer le
défaut même qui l'a fait écrire (Argon, budget 8 192, zéro pensée sur 22 réponses). Cette page n'est pas versée au dépôt
(recherche de son empreinte `fe0b8d88…` : seule la révision 8 la cite) : provenance non opposable (R7).

## 2. Comparaison des inventaires

Mon inventaire part de 3 743 programmes suivis (`.py`, `.sh`, `.js`, `.ts`), plus 18 programmes ignorés par
`.git/info/exclude`. Ce que l'audit a vu, je l'ai vu aussi ; ce qui suit est ce qu'il n'a pas.

| programme | pourquoi absent de l'audit | ce qu'il fait |
|---|---|---|
| `docs/notes/famille-reservee-dommage-v1/consultations-externes-v1/envoi_v1.py` (`8ea72770…`, 18:04Z, caché par `.git/info/exclude`, sans sceau compagnon) | postérieur à l'audit ; et invisible à `git grep` | appelle Carbon et Neon directement (section 4.1) |
| `docs/notes/collisionneur-v9/collisionneur_v9_v8.py` (`559b4820…`, 18:04Z, caché, **sans sceau compagnon**) | volontairement non ouvert (audit, ligne 5) | première garde des réglages de Google du dépôt (section 4.2) |
| `rapports/fille-ideation-1-v1/appel-argon-v5.sh` (`37c0205e…`) | cité, non contrôlé (motif `'*.py'`) | enveloppe de tous les lanceurs d'idéation : lance la v3d **sans** `--provision-pensee-jetons` ni `--sortie-min-jetons` (défauts 8 192 et 4 096), et passe `"$@"` avant les réglages figés |
| lanceurs de coquille plus anciens (`appel-argon-v3.sh`, `v4*.sh`, `lancer-question-argon-v1.sh`, `lancer-argon-recherche-v2.sh`, `lancer-tour-*.sh`) | motif `'*.py'` | hors service ; mêmes commandes que l'audit déclare hors service |
| `src/controle_ia/hote_durable_a1_v4_v5.py` et ses aînés | non nommés | Argon par la commande du tour fermé (hors service) |

Vérifications sans trouvaille : aucune branche distante n'ajoute d'appelant de Google ; le dépôt de travail de « Raisons ou
regard ? » (`/home/user/raisons-ou-regard-travail`, hors de ce dépôt) n'en contient aucun à cette heure. Les agents de
Google que Lazar a décidés pour cette course (décisions 264 à 266) **n'ont donc pas encore de code** : ils doivent naître
avec la garde, pas la recevoir après.

Note pour la suite : les programmes cachés par `.git/info/exclude` ne sont **pas poussés**. Le collisionneur v7 « prévu
pour la reprise » (audit, section 3.1), sa révision 8 et la commande d'envoi n'existent que dans ce conteneur ; une
session d'un autre compte ne les verrait pas.

## 3. Contrôle des constats de l'audit, ligne de code à l'appui

### 3.1 Constats confirmés

| constat de l'audit | ligne vérifiée | confirmé |
|---|---|---|
| collisionneur v9 v7 : `thinkingBudget` = champ « budget », Argon 8 192, plafond 32 768, provision 16 384 ; Argon absent de `REGLE_TEXTE_MIN` | `collisionneur_v9_v7.py` l. 237 à 239, 261, 966 (empreinte `319a7b66…` = sceau) | oui |
| consultation v6 : `thinkingBudget` = réflexion, plafond = réflexion + texte, texte < 16 000 refusé pour les trois espèces de Google ; pensées absentes lues 0 ; zéro accepté ; texte non `STOP` jamais écrit sous le nom de la réponse | `appel_modeles_externes_v6.py` l. 193 à 195, 236, 254 à 262, 269 à 273, 337 à 340 | oui |
| commande v3d : budget posé sauf `--sans-config-pensee` ; `maxOutputTokens` = min(max, place − provision), plancher 4 096 ; `MAX_TOKENS`, fin ≠ `STOP`, texte vide refusés (code 5) ; zéro pensée accepté | `commande_argon_v3d.py` l. 349 à 350, 681 à 689, 704 à 705, 845 à 859 | oui |
| commande par lot : budget 8 192, plafond 32 768, plancher 4 096, `STOP` exigé | `commande_gemini_lot_v1.py` l. 67 à 69, 130 à 133, 176 à 177 | oui |
| relais v4 : liste blanche `thinkingConfig` = {`thinkingBudget`, `includeThoughts`} | `relais_gemini_v4.py` l. 309 à 311 | oui |
| lanceur d'auto-conception v10 : `--sans-config-pensee` pour Carbon et Argon proposeur, 65 536 de plafond et de provision, plancher 4 096 | `lancer_course_auto_conception_v10.py` l. 420 à 425, 435 à 436 | oui : **aucune réflexion dans le corps** |
| liste des modèles versée : limite de sortie 32 768 pour Argon et Carbon, 65 536 pour Neon | `liste-modeles-gemini-20261121T134904Z.json` l. 594, 612, 648 | oui |
| dossier `gemini/` : clé dans l'adresse, aucune réflexion, bascule de modèle en boucle | `run_quadruple_fusee_omega_alpha_gamma_beta.py` l. 298 à 312 ; `autopilot_self_healing_daemon.py` l. 68 à 80 | oui ; j'ajoute : la chaîne d'erreur est rendue **comme texte de réponse** (`return f"[Erreur {lineage} : …]"`, l. 312) et l'échec de Gemini bascule vers Claude (repli de fournisseur) |
| aucune garde commune sous `src/controle_ia/` | `src/controle_ia/` : aucun module de Google ; `gardes.py` n'en parle pas | oui, toujours vrai à 18:30Z |

### 3.2 Empreintes citées par l'audit

Toutes recalculées : `e2095843`, `e94ecd46`, `46c91df4`, `9484dce0`, `543e728d`, `f4196ec5`, `082d19d6`, `11380cba`,
`319a7b66` : conformes.

### 3.3 Où l'audit sous-estime : les plafonds de session des proposeurs d'Argon

Sous la v3d et l'enveloppe `appel-argon-v5.sh`, `maxOutputTokens` ≤ ⌊plafond / 41,5 × 10⁶⌋ − 8 192. La règle demande
`maxOutputTokens` ≥ 8 192 + 16 000 = 24 192, soit un plafond de session d'au moins (24 192 + 8 192) × 41,5 × 10⁻⁶ ≈
**1,344 USD plus le coût de l'entrée**. Plafonds lus dans les lanceurs :

| lanceur | plafond du proposeur Argon | `maxOutputTokens` au mieux (entrée nulle) | règle |
|---|---|---|---|
| `scripts/lancer_course_ideation_regard_ou_raisons_v1.py` (`3b2dcb11…`) | 1,3 USD | 23 133 | **non tenue, toujours** |
| `scripts/lancer_course_ideation_bassins_etroits_v3.py`, `…conception_propre_v1.py` | 1,3 USD | 23 133 | **non tenue, toujours** |
| `scripts/lancer_course_ideation_pilier_attaque_v2_v3.py` | 1,70 USD | 32 771 → borné à 65 536 non atteint | tenue seulement si l'entrée coûte moins de 0,356 USD ; rien ne le contrôle |
| `scripts/lancer_course_ideation_organismes_discrets_v7.py`, `lancer_bras_juge_…_v1.py` | 2,5 et 3,0 USD | au-delà | tenue selon l'entrée ; rien ne le contrôle |
| juges à 0,60 USD (auto-conception v10, ligne 3 v4) | 0,60 USD | 6 265 | non tenue (chiffre de l'audit, confirmé) |

De plus, tous ces plafonds de sortie peuvent dépasser la limite versée de 32 768 d'Argon (défaut de la v3d : 65 536).

## 4. Programmes postérieurs à l'audit

### 4.1 Commande d'envoi des consultations de la famille réservée (`envoi_v1.py`, `8ea72770…`)

Prête, rien envoyé (aucun fichier de réponse dans son dossier à 18:30Z). Corps, l. 69 à 71 :
`{"maxOutputTokens": 65536, "thinkingConfig": {"thinkingBudget": 32768, "includeThoughts": True}}` pour Carbon et Neon.

- (a) réflexion : budget seul ; aucun niveau ; d'après la page citée par la révision 8 (non versée), un budget se ramène au
  niveau le plus proche.
- (b) plafond : 65 536 pour **Carbon, au-delà de sa limite versée de 32 768** ; si le service borne à 32 768, une réflexion
  de 32 768 ne laisse **aucun** texte. Pour Neon, 65 536 − 32 768 = 32 768 : tenu.
- (c) limite de mots : aucun contrôle.
- (d) après la réponse : **aucun défaut n'est nommé**. Toute fin est écrite dans `reponse-<modèle>-v1.md` sous le titre
  « Réponse brute », texte compris (l. 151 à 172) : `MAX_TOKENS` avec texte partiel, `SAFETY`, `RECITATION`, blocage de
  l'invite, fin absente (`None`), texte vide en `STOP`. Zéro pensée accepté. Modèle servi écrit, jamais comparé au modèle
  demandé. Seul `MAX_TOKENS` sans texte est relevé, et relancé une fois **au même réglage** (l. 141 à 144), donc payé deux
  fois sans changement.
- Repli : seconde clé sur refus de crédit ou de quota (l. 132 à 139), journalisé dans le fichier écrit : pas silencieux,
  mais à nommer au registre (autre compte de facturation).
- Aucune garde de dépense avant l'envoi (hors règle de Google, signalé seulement).

**À corriger avant tout envoi.**

### 4.2 Collisionneur v9, révision 8 (`collisionneur_v9_v8.py`, `559b4820…`, en écriture, sans sceau)

C'est la seule pièce du dépôt qui porte la règle par code. Contrôlé sur les lignes d'envoi :

- (a) `demande_gemini` (l. 1128 à 1137) envoie `thinkingLevel` (« high » Argon et Carbon, « xhigh » Neon) et
  `includeThoughts`, jamais de budget ; `verifier_reglages_google` (l. 1061 à 1101) est appelé **sur le corps même qui
  part**, en flux (l. 1150) et en lot (l. 1261), puis avant chaque essai avec la limite de mots (l. 1942, 1970). Réglage
  réellement envoyé : oui.
- (b) Argon 32 768 − provision 16 384 ; Carbon et Neon 65 536 ; `REGLE_TEXTE_MIN` étendue à Argon (l. 308). Mais le plafond
  maximal de la garde est 65 536 pour toutes les espèces (`PLAFOND_SYNCHRONE_GOOGLE`, l. 377), alors que la liste versée
  donne 32 768 pour Carbon : **Carbon à 65 536 passe la garde**, en lot compris (« plafond de sortie du lot égal à celui
  du flux », en-tête l. 82). Sous un niveau, la « provision » n'est plus une borne envoyée : c'est une estimation ; la règle
  des 16 000 se vérifie sur elle seule.
- (c) limite de mots × 1,6 jeton par mot contre le plafond de texte : contrôlée ; le rapport 1,6 n'est pas mesuré.
- (d) `defaut_reponse_google` (l. 1104 à 1121) : blocage, refus (`SAFETY`, `RECITATION`…), `MAX_TOKENS`, vide, autre fin,
  zéro pensée ou pensées absentes = défaut ; branché au jugement (l. 1882 à 1884).
- Écart à trancher : l'unique relance part à un niveau **plus bas** (« high » → « medium », `NIVEAU_CORRIGE`, l. 383),
  journalisé ; c'est un écart à « niveau le plus haut admis », que le développeur renvoie à la mère.
- Sources de la table des niveaux : pages lues à 17:42Z (`fe0b8d88…`, `829dabb8…`) et `a964d5cf…`, **non versées**.
- Règle (e) : la garde vit dans un collisionneur sous `docs/notes/`, non commis, et non dans `src/controle_ia/`.

Verdict : **à corriger** (plafond de Carbon, pages à verser, sceau et commit, niveau de relance à trancher, garde à porter
dans `src/controle_ia/`). C'est la base naturelle de la garde commune.

## 5. Replis silencieux et défauts que l'audit ne nomme pas

1. **Réponse coupée acceptée** : `docs/notes/ideation-organisme-v1/commandes-tour-ferme-v1/commande_argon_v56_nuit_v6.py`
   (`5eae1a04…`, et trois copies identiques sous `organisme-boucle-reelle-v1/`), l. 413 et 563 :
   `ROLES_COUPEE_ADMISE = ("experimentateur_test", "lecteur_test")` rend une réponse `TRONQUE` **en code 0**, texte vide
   compris. Contraire au point « fin en MAX_TOKENS = défaut, jamais une réponse ». Hors service, mais à ne pas relancer.
2. **Réflexion nulle admise par réglage** : consultation v6, `--reflexion 0` passe (`reflexion < 0` seul refusé, l. 271)
   et envoie `thinkingBudget: 0` ; commande v3d et lot, `--provision-pensee-jetons 0` passe (« entier ≥ 0 », v3d l. 782).
   Explicite dans le corps, mais c'est la réflexion coupée.
3. **Flux sans motif de fin** : `envoi_v1.py` écrit la réponse avec « Motif d'arrêt : None » (section 4.1) ; la
   consultation v6 rend « flux_sans_fin », non zéro (correct).
4. **Bascule de fournisseur** : dossier `gemini/`, Gemini → Claude 3.7 Sonnet sans GO (`autopilot_self_healing_daemon.py`,
   l. 83 et suivantes).
5. Confirmé de l'audit, sans ajout : morceau de flux illisible sauté par la consultation v6 (l. 214 à 218) ; annulation de
   lot avalée dans le collisionneur v7.

Contrôlé sans trouvaille : le relais v2 (en service, port 8788) relaie le corps tel quel ; il ne retire ni n'ajoute de
réglage de réflexion. Il ne vérifie rien non plus : c'est le dernier point avant Google, un bon lieu pour une seconde garde.

## 6. Divergence à soumettre (décision de Lazar)

La règle admet « budget prévu ». Les pièces du dépôt donnent trois faits : Argon, budget 8 192 seul, zéro pensée sur 22
réponses (contre-lecture du v7 par Fable, R-4644) ; Carbon, budget 32 768, jusqu'à 44 101 pensées (audit, section 3.1) ;
la page non versée dit le budget déprécié et ramené au niveau le plus proche. Un budget ne règle donc ni le plancher ni le
plafond de la réflexion chez Gemini 4. Proposition, non portée : chez Gemini 4, seul un niveau compte comme « réglage
explicite » ; un budget n'est admis que pour un modèle dont une page versée documente le budget. Tant que ce n'est pas
tranché, le refus de zéro pensée après la réponse est la seule protection contre le défaut d'origine.

## 7. Ce que j'ajoute aux recommandations de l'audit (section 6 de l'audit, que je reprends)

1. Avant tout envoi de `envoi_v1.py` : niveau de réflexion au lieu du budget, Carbon ramené à 32 768 ou la limite de 65 536
   établie par une pièce versée, défauts nommés et écrits hors du fichier de réponse, zéro pensée refusé, modèle servi
   comparé.
2. La garde commune part de `verifier_reglages_google` et `defaut_reponse_google` de la révision 8, déplacées sous
   `src/controle_ia/` (nom versionné), avec une table des limites de sortie **par espèce** lue dans la liste versée.
3. Refuser une réflexion nulle (budget 0) et une provision nulle.
4. Relever ou refuser les plafonds de session des proposeurs d'Argon à 1,3 USD (minimum ≈ 1,344 USD plus l'entrée) ;
   faire porter à l'enveloppe `appel-argon-v5.sh`, version neuve, les réglages de réflexion explicites.
5. Commiter (ou verser) le collisionneur v7, sa révision 8 et `envoi_v1.py`, avec leurs sceaux : ils sont aujourd'hui
   cachés par l'exclusion locale.
6. Les futurs agents de Google de « Raisons ou regard ? » : garde commune exigée avant le premier envoi.

## 8. Schéma corrigé (dernière version de chaque lignée, et pièces ajoutées)

| programme | en service | verdict |
|---|---|---|
| `docs/notes/collisionneur-v9/collisionneur_v9_v8.py` | non (en écriture) | à corriger |
| `docs/notes/collisionneur-v9/collisionneur_v9_v7.py` | oui (prévu pour la reprise) | à corriger |
| `docs/notes/famille-reservee-dommage-v1/consultations-externes-v1/envoi_v1.py` | oui (prêt, rien envoyé) | à corriger |
| `docs/notes/papier-dopamine-moniteur-v1/approfondissement-v1/appel_modeles_externes_v6.py` | oui | à corriger |
| `docs/notes/ideation-organisme-v1/argon-recherche-v1/commande_argon_v3d.py` | oui | à corriger |
| `docs/notes/ideation-organisme-v1/argon-recherche-v1/commande_argon_v3e.py` | non (réserve) | à corriger |
| `rapports/fille-ideation-1-v1/appel-argon-v5.sh` | oui | à corriger |
| `docs/notes/ideation-organisme-v1/argon-recherche-v1/relais_gemini_v2.py` | oui | à corriger (seconde garde) |
| `docs/notes/ideation-organisme-v1/argon-recherche-v1/commande_gemini_lot_v1.py` | non (réserve) | à corriger |
| `docs/notes/ideation-organisme-v1/argon-recherche-v1/relais_gemini_v4.py` | non (réserve) | à corriger |
| `scripts/lancer_course_auto_conception_v10.py` | non (en attente) | à corriger |
| `scripts/epreuve_temoins_auto_conception_v9.py` | non | à corriger |
| `docs/notes/organisme-auto-conception-v1/epreuves-v9/…/code-appel-v4/epreuve_juges_reels_ligne_3_v4.py` | non (en attente) | à corriger |
| `scripts/lancer_course_ideation_regard_ou_raisons_v1.py`, `…bassins_etroits_v3.py`, `…conception_propre_v1.py` | non (réutilisables) | à corriger |
| `scripts/lancer_course_ideation_organismes_discrets_v7.py`, `…pilier_attaque_v2_v3.py`, `lancer_bras_juge_…_v1.py` | non (réutilisables) | à corriger |
| `docs/notes/ideation-organisme-v1/commandes-tour-ferme-v1/commande_argon_v56_nuit_v6.py` (et copies), `src/controle_ia/hote_durable_a1_v4_v5.py` | non | hors service |
| `docs/notes/epreuve-fraiche-pont-v1/lancer_epreuve_pont_v2.py`, `docs/notes/collisionneur-bassins-etroits-v1/consultation_a_part_v1.py`, `docs/notes/affinage-equipe-rouge-v2/appeler_argon_v2.py` | non | hors service |
| collisionneurs anciens (`collisionneur_v9_v1` à `v6`, `collisionneur_v8_plafonds_bas_v1.py`, `collisionneur_v8.py`, `collisionneur_v7.py`, trois `collisionneur_v2.py`) | non | hors service |
| consultations anciennes (`appel_modeles_externes_v1` à `v5`), commandes anciennes (`commande_argon_v1` à `v3c`), relais `v1` et `v3` | non | hors service |
| `docs/notes/epreuve-etiqueteur-v1/lire_items_phase1_v5.py` | non | hors service |
| `gemini/11_EDIFICE_CERTIFIE_54_CORRECTIFS_L_STAR_V2_TAIF/` (trois programmes) | non | hors service, à ne jamais lancer |

Sceau : `contre-audit-reglages-google-v1.md.sha256`, dans ce dossier.

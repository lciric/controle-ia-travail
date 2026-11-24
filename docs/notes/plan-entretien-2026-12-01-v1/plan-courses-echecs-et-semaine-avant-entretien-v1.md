---
title: "Courses lancées depuis le 18 novembre, échecs et plan jour par jour jusqu'à l'entretien du 1er décembre"
subtitle: "Mandat F10, objectif long de Lazar (GO-2026-11-23-37) — version 1"
date: "2026-11-23, 23:25 UTC"
lang: fr
---

**Pièce de travail (classe C).** Écrite par une session fille (mandat F10 de `registres/passations/2026-11-23-2220-mere-antigravity-opus-reprise-et-mandats.md`, sous GO-2026-11-23-37), à partir des seuls registres non cloisonnés de `main` au commit `e268cb64`. **Aucun verdict, aucun fichier de `docs/verdicts/`, de `coffre/*`, des courses cloisonnées, aucun score ni épisode n'a été ouvert.** Les chiffres ci-dessous sont des **coûts** et des **heures**, jamais des résultats. Les chiffres des verdicts vont à Lazar par le tableau réservé (mandat F4, GO-2026-11-23-35).

## 0. En bref

1. **Toutes les courses sur carte lancées depuis le 18 novembre sont finies ou closes ; aucune machine ne tourne** (Vast : seules les quatre machines intouchables, arrêtées ; Hetzner : aucun serveur ; R-5204). Quatre courses attendent leur lecture : le saboteur (voie A), la relecture du barreau 5, la base boîte noire de T0.8 v3 et la ligne 1 du bras A (celle-ci gelée).
2. **La plupart des échecs sont des pannes techniques**, déjà relancées et réussies sur le même accord. **Deux échecs relèvent de la conception** et restent à traiter : le saboteur de la voie A a tourné **sans enregistrer d'activité interne** (R-5173), ce qui oblige à rejouer les épisodes pour recalculer les activations ; et le juge externe Astra n'a pas tenu le critère gelé de ses témoins, deux fois.
3. **Pour l'entretien, un seul chantier doit avancer d'ici au 1er décembre : le saboteur et les sondes.** Il coûte **environ 12 à 49 USD de dépense neuve** (plafonds compris). Le reste attend l'entretien : bras A, organisme, collisionneurs (≈ 66 USD pour les idées, ≈ 375 USD pour le dégel). **Trois accords à demander à Lazar** : le rejeu des activations du saboteur (mardi soir), le collisionneur groupé (mercredi soir), la prolongation des accords qui tombent le 30 (vendredi).

Calendrier : le 1er décembre 2026 tombe un **mardi** (le mandat dit lundi). Le plan couvre donc huit jours, du mardi 24 novembre au mardi 1er décembre, jour de l'entretien.

## 1. Inventaire des courses lancées depuis le 18 novembre

Légende de l'état : **finie** (marche menée au bout, versement prouvé) ; **close** (arrêtée, cause connue, rien à relancer sur cette ligne) ; **en attente de lecture** (finie, rien ouvert).
« Qui lit » : jamais la mère pour ce qui est cloisonné. Le verdict est toujours prononcé par un agent neuf qui n'a écrit ni le préenregistrement ni l'analyse (R13).

### 1.1 Calcul sur carte graphique ou sur serveur loué

| course (en clair) | machine, dates | état | dépense (USD) | reste avant lecture | qui lit |
|---|---|---|---|---|---|
| Apprentissage des sondes sur la tâche (étape B bis de T0.7), course du feu v7 | Vast 61276240, 18 nov. 15:44Z → 19:42Z | finie, code 0 | 4,69 (ligne 10,68 sur 39,5) | rien : **verdict scellé** | déjà lu ; chiffres à Lazar par F4 |
| Ajustement de nos lentilles neuronales, tranche (lentilles R et S) | Vast 61287124, 18 nov. 16:48Z → 19 nov. 05:45Z | finie | ≈ 32,8 sur 75 | rien : **verdict scellé** | déjà lu ; F4 |
| Réajustement de nos lentilles R et S puis rangement | Vast 61932710, 22 nov. 07:34Z → 20:40Z | finie ; copie de 34 pièces d'export en échec à la clôture (refus 429), pièces dérivables du fichier d'ajustement copié | 31,28 (+ réseau ≤ 0,80) | seconde passe de la lecture des sondes par les lentilles (défauts N-dev-7 et N-dev-9 appliqués, R-5188) ; seconde relecture (étape 16) après révocation de la clé restreinte par Lazar | lecteur habilité des lentilles |
| Saboteur à budget, première course | Vast 61414494, 19 nov. 08:54Z → ≈ 10:14Z | close : arrêtée par sa garde à la première épreuve de l'oracle (centrage) | ≤ 2,7 sur 60 | rien : **verdict scellé** (« saboteur course 1 ») | déjà lu ; F4 |
| Saboteur, étalonnage v5, tentative 1 | Vast 61859391, 21 nov. 21:08Z → 21:23Z | close : arrêtée sur la suite d'essais ciblée, avant le modèle | ≤ 1,24 | — (relancée) | — |
| Saboteur, étalonnage v5, tentative 2 | Vast 61875617, 21 nov. 23:29Z → 22 nov. | close à la coupure propre de 16 USD (mot de Lazar) ; contenu rapatrié 55 sur 55 | ≈ 16 au plus (montant final à relever) | — (la voie A a pris la suite, GO-2026-11-22-75 ; voie B gardée) | — |
| Saboteur, voie A, étalonnage | Vast 62031392, 22 nov. 20:04Z → 22:13Z | finie ; rapatriement 62 sur 62 ; désignation scellée | 3,61 | — | — |
| **Saboteur, voie A, course** (sujet du barreau 8) | Vast 62094628, 23 nov. 04:21Z → 13:20Z (détruite 18:21Z) | **finie, en attente de lecture** ; réserve : aucune activité interne enregistrée (R-5173) | 11,74 de machine ; 15,35 pour la voie | (1) additif 1 aux sondes du barreau 8 scellé avant le 24 nov. 10:20:38Z (mandat F1) ; (2) devis puis rejeu des épisodes à l'identique sur carte pour recalculer les activations (choix NL-11, GO-2026-11-23-32) ; (3) lecture selon l'additif | lecteur habilité côté saboteur, puis agent neuf pour le verdict |
| Barreau 5, formation des familles d'adaptateurs jumeaux | Vast, six instances le 20 nov., relances le 20, recréations le 21 | finie (toutes les marches au bout, versements prouvés) | 71,73 sur 200 (cumul final) | — | — |
| Barreau 5, répétition générale de la relecture | Vast 62036317, 22 nov. | finie, versement prouvé | compris dans ≈ 2 (avec les deux tentatives suivantes) | — | — |
| Barreau 5, relecture décisive, tentative 1 | Vast 62047649, 22 nov. | close avant la marche (commit des entrées introuvable dans le clone partiel) | dans les ≈ 2 | — (relancée) | — |
| Barreau 5, relecture décisive, tentative 2 | Vast 62094971, 23 nov. 04:24Z → 04:39Z | close : arrêtée à tort par la veille (octets lus comme des gigaoctets) | dans les ≈ 2 | — (relancée) | — |
| **Barreau 5, relecture décisive, reprise** | Vast 62096662, 23 nov. 04:40Z → fin 10:12Z (détruite 23:15Z) | **finie, code 0, en attente de lecture** ; rapatriement prouvé complet (3 449 fichiers sur 3 449) | ≈ 7 (estimation heures × prix, stockage jusqu'à la destruction compris ; à relever) | (1) table de correspondance des issues (brouillon 3) et conception des sondes boîte blanche (brouillon 5) scellées (mandat F9) ; (2) ouverture des scores par programme selon le texte scellé | session de lecture habilitée ; verdict par un agent neuf |
| Base boîte noire de T0.8, tentative 1 | Vast 62094761, 23 nov. 04:22Z → 04:43Z | close : arrêt dans les gardes, aucun calcul (erreur de chaîne) | ≤ 1,5 sur 120 | — (corrigée, relancée) | — |
| **Base boîte noire de T0.8, version 3** | Vast 62105206, 23 nov. 05:57Z → 16:34Z | **finie, en attente de lecture** ; résultats versés (`calcul/t08-course-v3` b5608414), non ouverts ; réserve : aucune surveillance de 08:54Z à 18:16Z, la minuterie a tenu | ≈ 12,19 (ligne ≈ 13,7 sur 120) | lecture selon le texte scellé v3 ; vérifier qu'un texte de lecture scellé existe, sinon le faire écrire avant toute ouverture | lecteur neuf habilité ; verdict par un autre agent neuf |
| Bras A, ligne 1 (fabrication et rejeu honnête, 128 épisodes), tentatives 1 et 2 | Vast 62082700 et 62094921, 23 nov. | closes : instance injoignable, puis installation en échec | ≈ 0,20 | — (relancée) | — |
| **Bras A, ligne 1, tentative 3** | Vast 62097676, 23 nov. 04:52Z → 06:12Z | **finie, code 0** ; épisodes non ouverts ; **gelé** (GO-2026-11-23-15) | 2,83 sur 18 (ligne entière) | étapes (c) à (h) du texte scellé, conduites par la session de relance (GO-2026-11-23-13) ; point ouvert : trois modules de l'étape (c) écrits après le code arrêté (couverture ou écart, R-5166) | session de relance par agents neufs ; verdict de (g) par un agent neuf |
| Organisme, essai 3 du palier 0b | Hetzner 177170935, 22 nov. 08:16Z → 23 nov. 04:50Z | close : calcul arrêté vers 21:15Z, boucle de versement bloquée après le versement 25, sans fichier de fin ; instantané 459833196 gardé | ≈ 1 (à relever ; instantané ≈ 0,14 à 0,25 EUR par mois) | inventaire de l'instantané ; relance sur le même accord au dégel | organisme (gelé) |
| Outillage de l'essai Lean D-1a, essais 3 et 4 | Hetzner 177067030 et 177109613, 21 nov. | finis, code 0 | ≈ 0,56 (ligne ≈ 1,12) | — | poste Lean |
| « Raisons ou regard » (projet hors programme) : écritures et annotations de l'expérience E5 et de l'expérience 1 | Vast 61176380, 61194535, 61207720, 18 nov. | finies | ≈ 14,2 | hors programme | session « Raisons ou regard » |

### 1.2 Appels d'interface (aucune machine)

| course (en clair) | dates | état | dépense (USD) | reste |
|---|---|---|---|---|
| Organisme, relance de l'idéation v8 (lignées Carbon, Astra, Argon, Kimi) et juges externes différés | 18 nov. | Carbon : deux courses arrêtées sans fiche (tunnel réseau fermé, appel coupé à 300 s), puis une course par lot lisible ; Astra et Argon closes, puis secondes courses lisibles ; Kimi refusé deux fois (surcharge 429) ; juges différés Argon et Carbon lisibles ; **juge Astra illisible deux fois** (critère gelé des témoins non tenu) | ≈ 11,9 (plafond commun 34) | — |
| Organisme, course d'auto-conception, tentative 1 | 18 nov., close 19:30Z | code 2 : étape « proposition » non mesurée, cause technique, tentative consommée | 44,78 | — |
| Organisme, course d'auto-conception, tentative neuve | 19 nov., 00:12Z → 01:52Z | code 2 : Carbon tronqué, tentative consommée | 42,36 sur 90 | — |
| **Organisme v9, course d'auto-conception** (et épreuves des témoins) | 19 nov., 09:41Z → 12:31Z | **finie, code 0** ; sortie versée (`lot/compte-organisme-v1`) | 72,50 sur 150 (+ ≈ 2,5 d'épreuves) | affinage v11 : contre-lecture du candidat 1 (mandat F8), mesure préalable d'Argon (≤ 10,50, GO-2026-11-23-07), course sous GO-2026-11-22-80 ; **gelé** |
| Bras A, essai de mesure de la longueur de sortie des lecteurs (files GPT, Carbon, Claude) | 19 nov. | closes ; file Carbon au budget 2 048 arrêtée par un code 502 (garde sans reprise) | ≈ 1,99 | — |
| Bras A, vérification et admission de Mistral, relectures des avenants 2 et 3 par Fable par l'interface, appels à Neon | 21-22 nov. | closes | ≈ 9,6 | — |
| Collisionneur « dopamine » (deux reprises) | 20 nov. | fini ; critique de Carbon au tour 2 absente (garde de réflexion) | 14,45 | — |
| Collisionneur, seuil à 1 % des moniteurs | 21 nov. | fini, 15 cellules sur 15 | 14,86 | — |
| Collisionneurs « méthodes de mathématiques nouvelles » et « correction de la dérive de régime » | 21 nov. | arrêtés (code 5 : clé sans crédit) | 6,23 + 1,68 + 3,04 (comptés au pire) | repris en v8d (ligne suivante) |
| Collisionneur v8d, reprise des cinq dossiers arrêtés | 21-22 nov. | fini | 29,83 | — |
| Collisionneurs « conscience et anesthésie » (dossier neutre et dossier v3) | 22 nov. | finis ; notes de sortie versées | 25,09 | suite sous GO-2026-11-23-19 (40 USD) : état final non consigné sur `main` |
| Collisionneur « modes et attaques » (session cloisonnée) | 22 nov. | fini ; épreuve de Carbon arrêtée au plafond (code 4) | 21,90 | cloisonné |
| Service de la question v8 (modes de sabotage) au collisionneur | 23 nov. | Argon, Carbon, Neon : conception et critique finies ; **Astra jamais parti** (crédit OpenAI épuisé) ; **Opus absent des tours 2 et 3** (limite d'abonnement) ; **Fable 5.1 et 5.2 : refus du modèle** au tour de conception | ≥ 15,13 sur 26 + 3,06 (Fable) ; montant final à relever | cloisonné ; relances possibles d'Astra et d'Opus à part |
| « Idées intéressantes » : appels seuls à Argon, Carbon, Neon ; question sur l'homomorphisme | 23 nov. | finis ; un défaut de récitation chez Argon, relancé une fois, puis réponse | ≈ 5 et plus (à lire sur la facturation de Google) | collisionneur « idées intéressantes » (30 USD, GO-2026-11-23-22) : départ non consigné |
| Consultations courtes (visées mathématiques, brainstorm, avis sur G1, sabotage sélectif, seuil de 0,75, renvois par l'interface) | 21-23 nov. | finies ; un appel de Neon coupé (503), un arrêté sans réponse lue | ≈ 16 | — |
| « Raisons ou regard », essais d'Argon | 18-22 nov. | essai 2 interrompu avec le conteneur, réponses perdues ; essai 3 non admis | ≈ 17,5 (dont 13,05 compté au pire) | hors programme |

### 1.3 Dépense depuis le 18 novembre, par famille

Sommes de cette note sur les lignes du registre des dépenses et des décisions ; certaines lignes sont **comptées au pire** (envois coupés), d'autres restent **à relever** sur les factures. Ordres de grandeur, non opposables.

| famille | USD (environ) |
|---|---|
| Calcul sur carte et serveurs du programme | 203 |
| Organisme d'idéation (interfaces) | 176 |
| Collisionneurs et consultations | 155 |
| Bras A (interfaces) | 12 |
| « Raisons ou regard » (hors programme) | 32 |
| **Total** | **≈ 578** |

À faire avant l'entretien, sans dépense : rapprocher ces montants des factures réelles de Vast, de Google et d'OpenAI (plusieurs lignes au pire, dont 13,05 USD d'Argon).

## 2. Échecs et arrêts : raison consignée et classement

**Panne technique** : faux échec, droit à une relance sur le même accord (GO-2026-11-22-77), entrée au registre des idées de la veille de cap avec l'une des quatre issues (jamais parti, non évaluable, non concluant, verdict valide).
**Échec de conception** : la course a marché, mais ce qu'on a conçu ne répond pas à la question. La note propose une reconception courte.

### 2.1 Pannes techniques, déjà relancées et réussies (rien à faire, sauf l'inscription au registre des idées)

| arrêt | raison consignée | issue | relance |
|---|---|---|---|
| Barreau 5, formation : six instances arrêtées le 20 nov. | crédit du loueur épuisé | jamais parti (en partie) | relances puis recréations, finies (R-5101 et suivantes) |
| Barreau 5, relecture, tentative 1 | commit des entrées introuvable dans le clone partiel | jamais parti | reprise finie |
| Barreau 5, relecture, tentative 2 | veille qui lisait des octets comme des gigaoctets | jamais parti | veille corrigée, essayée sur un cas sain et un artefact ; reprise finie |
| T0.8, tentative 1 | garde de l'amorce trop lente sur un clone partiel (> 900 s) | jamais parti | correctif C2, puis C3 ; v3 finie |
| T0.8, version 2 | clés du registre mal nommées, refus au préalable P3 | jamais parti | correctif C3 ; v3 finie |
| Bras A, tentatives 1 et 2 | conteneur sans sortie réseau brute ; image sans `ensurepip` | jamais parti | machine autonome et amorce v4 ; tentative 3 finie |
| Saboteur, étalonnage v5, tentative 1 | suite d'essais ciblée en échec avant le modèle | jamais parti | tentative 2 |
| Organisme, auto-conception, tentatives du 18 et du 19 nov. | étape non mesurée pour cause technique ; Carbon tronqué | non évaluable | v9 finie le 19 |
| Collisionneurs « mathématiques » et « dérive » | clé Anthropic sans crédit (code 5) | non concluant | reprise v8d finie |
| Carbon (relance de l'organisme, 18 nov.) | tunnel réseau fermé, appel coupé à 300 s | jamais parti | course par lot lisible |
| Argon (« idées intéressantes ») | filtre de récitation | non concluant | relancé une fois, réponse |
| Mistral, vérification de la clé | paramètre refusé (`top_p`) | jamais parti | réglage retiré, clé saine |
| « Raisons ou regard », Argon essai 2 | conteneur perdu | non évaluable | essai 3 joué |

### 2.2 Pannes techniques encore ouvertes (relance possible sur le même accord)

| arrêt | raison | proposition |
|---|---|---|
| **Astra au service de la question v8** | crédit OpenAI épuisé (`insufficient_quota`) | relance à part après recharge par Lazar ; ≤ 6,60 USD au pire. Pas urgent pour l'entretien. |
| **Opus aux tours 2 et 3 du service v8** | limite d'abonnement | relance à part par l'abonnement (0 USD) après la réinitialisation du 29 nov. à 18:00Z, ou depuis un autre compte. |
| Kimi (relance de l'organisme, 18 nov.) | surcharge 429, deux fois | à inscrire en faux échec « jamais parti » ; relance seulement au dégel de l'organisme. |
| Carbon, essai de mesure du bras A au budget 2 048 | code 502, arrêt voulu par la garde | « non concluant » ; à rejouer seulement si le réglage 2 048 sert au bras A. |
| **Organisme, essai 3 du palier 0b** | boucle de versement bloquée après le versement 25, sans fichier de fin | **reconception courte de la chaîne** : versement final idempotent, fichier de fin obligatoire, garde qui alerte si deux versements manquent ; d'abord inventorier l'instantané 459833196 (règle « toujours récupérer »), puis relancer au dégel. |
| Réajustement des lentilles : copie de 34 pièces en échec à la clôture | refus 429 du dépôt | pièces dérivables, rien à relancer ; dériver et sceller à la seconde passe. |
| Question technique v9 du service (remplace la question refusée par Fable) | sous-agent arrêté par la limite d'Opus avant d'écrire | reprendre la rédaction (Opus élevé) quand une session est libre. |

### 2.3 Échecs de conception, avec une proposition de reconception courte

| échec | raison | reconception proposée |
|---|---|---|
| **Saboteur, voie A : aucune activité interne enregistrée** (R-5173) | le lanceur v5 et l'amorce n'enregistrent pas les activations ; écart à la lettre de GO-2026-11-10-08 | (1) **pour cette course** : rejeu à l'identique des épisodes sur carte pour recalculer les activations (choix NL-11 accordé), avec un contrôle de l'égalité des actions rejouées avant toute lecture ; (2) **pour toutes les courses suivantes** : garde qui refuse le départ si l'enregistrement interne est absent ou vide, essayée sur un cas sain et sur un artefact (R5). |
| Saboteur, première course : arrêt à l'épreuve de centrage de l'oracle | l'oracle n'était pas centré (verdict scellé) | **déjà reconçu** : étalonnage v5, puis voie A. Rien à faire. |
| **Juge externe Astra illisible, deux fois** | critère gelé des témoins non tenu chez ce juge | au dégel : soit retirer Astra du rôle de juge externe de ce bras (la conception le permet si deux juges suffisent), soit préenregistrer des témoins neufs propres à ce juge avant tout nouvel appel. Recommandation : le retirer, confiance moyenne. |
| Fable refuse le tour de conception du service v8 | refus du modèle (`refusal`), pas une panne ; issue « verdict valide » | **ne pas contourner** en changeant le réglage. Question technique v9, distincte et honnête, à faire passer par sa propre chaîne (en suspens, 2.2). |
| « Raisons ou regard », Argon essai 3 non admis | règle d'admission du projet non tenue | hors programme ; rien sans la session du projet. |

## 3. Programme jour par jour, du mardi 24 novembre au mardi 1er décembre

### 3.1 Règles tenues

- **Trois chantiers actifs au plus.** Un seul avance ici : **le saboteur et les sondes pour l'entretien**, lentilles comprises en vue du billet. Il couvre le barreau 8 (saboteur, voie A), la relecture du barreau 5, les sondes v2 et leur épreuve plantée, la lecture de T0.8 v3 (base boîte noire et versant honnête de l'instruction B6) et le billet. **Bras A et organisme restent gelés** (GO-2026-11-23-15) jusqu'après l'entretien.
- **Pas 0 sur processeur** (GO-2026-11-23-37) : la rétrodiction du rang 1 et l'étalonnage court du rang 4 tournent en tâche de fond, à 0 USD, comme veille à côté des chantiers. Ils ne bloquent rien.
- **Qui fait quoi.** Fable 5.2 en effort maximal seulement pour les verdicts et les pièces les plus délicates ; Fable en effort élevé ou moyen pour les devis et additifs de forme fixée ; Opus 5.5 en effort élevé pour les contre-lectures, les vérifications et le code ; un modèle léger pour la routine. La mère orchestre, scelle et consigne ; elle n'ouvre rien de cloisonné.
- **Contraintes connues.** Le quota de Fable est rare (limite jusqu'au 24 nov. 05:00Z sur un compte, R-4702). La limite hebdomadaire d'Opus d'un compte se réinitialise le 29 nov. à 18:00Z (R-5149). Les clés manquent dans l'environnement Antigravity. Beaucoup d'accords tombent le **30 novembre**.

### 3.2 Tableau des jours

| jour | tâches | qui | dépend de | dépense neuve (USD) |
|---|---|---|---|---|
| **Mar. 24** (nuit et matin) | Additif 1 aux sondes du barreau 8 : candidat rendu avant 08:00Z, **scellé par la mère avant 10:20:38Z** (F1) | session F1 (rédacteur neuf, contre-lecteur Opus neuf) ; mère | vérification d'AD-2 côté exposé | 0 |
| Mar. 24 | Conception des sondes boîte blanche (brouillon 5) et table de correspondance (brouillon 3) : versions candidates, vérification finale, **scellement** (F9) | session F9 (Fable dosé), contre-lecteur Opus neuf ; mère | points du § 9 déjà tranchés (GO-2026-11-23-36) | 0 |
| Mar. 24 | Sondes v2 : additif de commit, jonction de la table, diagnostic de la garde des mots de rôle (F2) ; puis, sur le mot de la mère, note des effectifs par un agent habilité neuf | session F2 ; agent habilité neuf | — | 0 |
| Mar. 24 | **Devis du rejeu des activations du saboteur** (une page : carte, durée, plafond, contrôle d'égalité des actions) | Fable 5.2 effort élevé ; contre-lecture Opus élevé | additif 1 scellé | 0 |
| Mar. 24 | Lecture de T0.8 v3 : vérifier par les noms seuls que le texte de lecture scellé existe, puis préparer l'ouverture par programme | lecteur neuf habilité (Opus élevé) | — | 0 |
| Mar. 24 | Pas 0 : préenregistrements du rang 1 (F6) et du rang 4 (F7) contre-lus, puis extraction de fond | sessions F6 et F7 ; contre-lecteurs neufs | licences vérifiées (rang 4) | 0 |
| Mar. 24 | Billet v2 et sa lecture adverse (F3) ; tableau des verdicts pour Lazar (F4) | sessions habilitées F3 et F4 | — | 0 |
| Mar. 24, 18 h Paris | Rappel à Lazar : les trois sources du jugement contre la surveillance, note v6 de l'entretien | mère | — | 0 |
| **Mar. 24, soir** | **Lazar** : lit le tableau F4 ; **GO sur le rejeu des activations du saboteur** ; avis sur le devis de la boucle organisme-contrôle (recommandation : après l'entretien) | Lazar | devis contre-lu | — |
| **Mer. 25** | **Départ de l'épreuve plantée des sondes v2** (Hetzner ccx63, GO-2026-11-23-18, plafond 27,10) ; engagement inscrit avant création | développeur des sondes v2 (exécutante) ; mère | additif de commit scellé, corrections vérifiées | 6,70 à 18,10 (plafond 27,10) |
| Mer. 25 | **Rejeu des épisodes du saboteur** sur carte (machine autonome, versement prouvé, destruction par identifiant) | exécutante du saboteur ; mère (engagement, remparts) | GO du 24 au soir | ≈ 5 à 15 (estimation de cette note, à remplacer par le devis) |
| Mer. 25 | Barreau 5 : ouverture des scores par programme selon le texte scellé, analyse | session de lecture habilitée | table et conception scellées (24) | 0 |
| Mer. 25 | T0.8 v3 : ouverture par programme et analyse | lecteur neuf habilité | texte de lecture scellé | 0 |
| Mer. 25 | Collisionneur groupé (lot 8 et dossiers 1 à 6) : test de neutralité, devis vérifié (F5) | session F5 ; lecteur neuf du test de devinette | dossier 1 rédigé | 0 |
| **Mer. 25, soir** | **Lazar : GO ou report du collisionneur groupé** (recommandation : report après le 1er, sauf s'il veut une illustration pour l'entretien) | Lazar | devis F5 | — |
| **Jeu. 26** | Lecture des sondes du saboteur sur les activations recalculées, selon l'additif 1 ; cinq lectures comparées hors verdict (NL-9) | lecteur habilité côté saboteur | rejeu fini et versé ; égalité des actions contrôlée | 0 |
| Jeu. 26 | Verdicts du barreau 5 et de T0.8 v3 | agents neufs (Fable 5.2 effort élevé, ou effort maximal si un verdict touche une porte) | analyses finies | 0 |
| Jeu. 26 | Instruction B6, versant honnête : prévision scellée sur les jumeaux existants de T0.8 v3 et de 7b ; devis s'il en faut un | Fable effort élevé ; contre-lecture Opus | lecture de T0.8 v3 | 0 (devis éventuel à part) |
| Jeu. 26 | Lentilles, seconde passe : seconde relecture (étape 16), pièces d'export dérivées et scellées | lecteur des lentilles | révocation de la clé restreinte par Lazar | 0 |
| **Ven. 27** | **Verdict de la lecture des sondes du saboteur** (pièce maîtresse de l'entretien) | agent neuf, Fable 5.2 effort maximal | lecture du 26 | 0 |
| Ven. 27 | Fin de l'épreuve plantée ; lecture par le lecteur habilité, verdict par un agent neuf | lecteur habilité ; agent neuf | épreuve finie | 0 |
| Ven. 27 | Billet v3 nourri des verdicts scellés ; lecture adverse | rédacteur habilité ; lecteur adverse neuf | verdicts du 26 et du 27 | 0 |
| **Ven. 27** | **Lazar : prolongation des accords qui tombent le 30** (liste de la veille de cap : formation du barreau 5, bras A ligne 1, voie A du saboteur, accords du 23) | mère prépare la liste ; Lazar | — | 0 |
| **Sam. 28** | **Assemblage du dossier de l'entretien** (comme prévu par GO-2026-11-23-17) : réponse d'une page sur la surveillance, objection 1 v7, verdicts en une phrase chacun avec leurs réserves, état du billet | rédacteur neuf ; contre-lecteur Opus ; mère | verdicts scellés | 0 |
| Sam. 28 | Rapprochement des dépenses et des factures (Vast, Google, OpenAI) | modèle léger ; mère | — | 0 |
| **Dim. 29** | Corrections du dossier ; lecture par Lazar ; répétition de l'entretien ; après 18:00Z, relance éventuelle d'Opus aux tours 2 et 3 du service v8 (abonnement) | Lazar ; mère ; Opus | dossier du 28 | 0 |
| **Lun. 30** | Gel du dossier ; inventaire des machines (rien ne doit tourner) ; passation ; derniers rappels | mère | — | 0 |
| **Mar. 1er déc.** | **Entretien** | Lazar | — | — |

Les rappels de 18 h (heure de Paris) du 25 au 30 et ceux de 9 h 47 courent chaque jour (`registres/rappels.md`).

### 3.3 Budget de la semaine

| ligne | accord | bas | haut (plafond) |
|---|---|---|---|
| Rejeu des activations du saboteur | **à demander le 24** | ≈ 5 | ≈ 15 (estimation ; repère : la course entière, génération comprise, a coûté 11,74 de machine) |
| Épreuve plantée des sondes v2 | accordé (GO-2026-11-23-18) | 6,70 | 27,10 |
| Relance d'Astra au service v8 (facultative) | même accord (26 USD) | 0 | 6,60 |
| **Socle de l'entretien** | | **≈ 12** | **≈ 49** |
| Collisionneur groupé (lot 8 et dossiers 1 à 6) | à demander le 25 (recommandation : après le 1er) | ≈ 5 côté Google | ≈ 30 (plafond à fixer par le devis) |
| Collisionneur de la boucle organisme-contrôle | devis soumis (R-5199) | 32 (option A) | 36 (option B) |
| **Socle et idées** | | | **≈ 115** |
| Après l'entretien, au dégel : bras A ligne 2 | complément de devis à écrire (GO-2026-11-23-11) | ≈ 47 à 50 | 85 (repli) |
| Après l'entretien : lectures hors carte du bras A | accordé en principe (GO-2026-11-22-143) | — | 130 (premier engagement) |
| Après l'entretien : organisme, mesure d'Argon puis affinage v11 | accordés (GO-2026-11-23-07, GO-2026-11-22-80) | ≈ 4,6 | 10,50 + 150 |

Frais courants : stockage des quatre machines Vast intouchables arrêtées, instantané Hetzner (≈ 0,14 à 0,25 EUR par mois).

### 3.4 Demandes à Lazar, dans l'ordre

1. **Mardi 24, soir** : GO sur le rejeu des activations du saboteur, sur devis contre-lu (≈ 5 à 15 USD). C'est le chemin critique de l'entretien : sans lui, pas de lecture des sondes sur le barreau 8.
2. **Mardi 24** : son geste pour révoquer la clé restreinte des lentilles (seconde relecture, étape 16).
3. **Mercredi 25, soir** : collisionneur groupé, maintenant ou après le 1er (recommandation : après, confiance moyenne) ; même question pour le devis de la boucle organisme-contrôle (32 ou 36 USD).
4. **Vendredi 27** : prolongation des accords qui tombent le 30 novembre.
5. **Quand il veut** : recharger OpenAI (Astra), déposer les clés dans l'environnement Antigravity si la mère y pilote, demander à la conversation Antigravity `ff6e9350` de verser son arbre de travail (`versement/mere-antigravity-ff6e9350-v1`).

### 3.5 Risques sur le calendrier

- **Rejeu du saboteur en retard** : le verdict du 27 glisse au 28 ; le dossier s'assemble avec un « en cours » sur le barreau 8. À dire tel quel, sans repli silencieux.
- **Fable indisponible** : verdicts par Fable en effort élevé sur un autre compte. Une contre-lecture par Opus marquée « à revoir par Fable » ne vaut pas scellement décisif (option du 21 novembre, R-4702).
- **Durée de l'épreuve plantée** : le devis l'estime à 185 à 498 heures. Si la durée murale dépasse le 28, l'entretien cite un départ, pas un verdict.
- **Deux mères sur `main`** (Antigravity et Claude Code) : une seule écrit les registres, l'autre verse sur une branche (R-5170).

## 4. Idées pour la suite, classées

Chaque idée est notée sur le gain d'information, le coût et l'urgence pour l'entretien (haute, moyenne, basse).

| rang | idée | gain | coût | urgence pour l'entretien |
|---|---|---|---|---|
| 1 | **Garde « activations enregistrées »** dans tous les lanceurs : refus de départ si l'enregistrement interne est absent ou vide ; essais sur un cas sain et sur un artefact | haut (évite de refaire la voie A) | 0 | haute |
| 2 | **Garde commune du clone partiel** dans toutes les amorces (objets manquants permis, commit des entrées vérifié avant la marche) : trois des pannes de la semaine en venaient | haut | 0 | haute |
| 3 | **Rapprochement des factures** contre les montants comptés au pire, avant de présenter un budget à l'entretien | moyen | 0 | haute |
| 4 | **Cloisonnement à trois strates** de la boucle organisme-contrôle, codé comme garde et éprouvé (premier rang de la réponse de Carbon, `docs/notes/protocole-x-boucle-organisme-controle-v1/`) : rien du contrôle ne doit sélectionner l'organisme | haut | 0 | moyenne |
| 5 | **Veille des machines unique**, aux unités vérifiées par essai (octets ou gigaoctets), commune à tous les chantiers | moyen | 0 | moyenne |
| 6 | **Pas 0, rang 1 et rang 4** (rétrodiction des foyers de tension, étalonnage du pont sur PubTator 3 et sur Gu et Krenn) : préenregistrés puis joués sur processeur | moyen à haut pour l'organisme | 0 | basse (veille à côté) |
| 7 | Dégel ordonné après l'entretien : **bras A** (étapes (c) à (h), puis ligne 2), puis **organisme** (affinage v11, juge Astra retiré ou témoins neufs) | haut | ≈ 230 à 375 | basse |
| 8 | Collisionneur groupé, puis collisionneur de la boucle organisme-contrôle | moyen | ≈ 37 à 66 | basse |

## 5. Sources (non cloisonnées, `main` au commit `e268cb64`)

| fichier | empreinte (début) |
|---|---|
| `registres/etat.md` | `addd38594ee86e09…` |
| `registres/decisions.md` (R-3170 à R-5205) | `261986ece690845e…` |
| `registres/arrets.md` | `06126e5aa4744893…` |
| `registres/depenses.md` | `474e007d25f7913d…` |
| `registres/go.md` (GO-2026-11-18 à GO-2026-11-23-38) | `389a807671041544…` |
| `registres/rappels.md` | `d909ee3292331625…` |
| `registres/passations/2026-11-23-2220-mere-antigravity-opus-reprise-et-mandats.md` | `535b3631eb982cb2…` |
| `docs/notes/idee-interessante-v1/lot-8/rapport-priorites-et-impact-organisme-2026-11-23-v1.md` | `88d80f767ed7638e…` |
| `docs/notes/protocole-x-boucle-organisme-controle-v1/reponse-approfondie-carbon-boucle-organisme-controle-v1.md` | `f744320dcd7c2a8c…` |

Lignes clés : machines et fins de course R-5104 à R-5145, R-5184, R-5186, R-5193, R-5204 ; écart du saboteur R-5173 ; gel R-5165 ; choix de l'additif du barreau 8 GO-2026-11-23-32 ; devis en attente R-5146, R-5199 ; dépenses de `registres/depenses.md` lignes 489 à 625 ; arrêts de `registres/arrets.md` lignes 138 à 166.

# Avis sur le mandat à Fable — l'essai en essaim de l'organisme avec Argon, par étapes — v1

- Session fille de l'abonnement, ouverte par la session mère pour ce seul mandat, le 22 novembre 2026. **Aucun appel de modèle, aucune clé, aucune dépense.** Seul réseau employé : la lecture du dépôt de travail.
- Mandat : `docs/notes/organisme-essaim-communicant-v1/mandats-fable-abonnement-v1/mandat-fable-essaim-argon-par-etapes-v1.md` (`93bec41064d3d4bc0f088b2855c9c575ed44d9186ec99286b41818c6577097a7`, commit `1b81eed4`), empreinte vérifiée avant lecture.
- À l'écriture de cet avis, aucun refus d'outil, de garde ou de classifieur n'a été rencontré.
- Plan de lecture : le verdict, les écarts et le § 7 suffisent au directeur ; les § 1 à § 6 répondent, dans l'ordre, aux six points du mandat et servent à l'organisme.

## Pièces lues, et elles seules

| n° | pièce | branche, commit | sha256 |
|---|---|---|---|
| 1 | `docs/notes/organisme-essaim-communicant-v1/devis-et-instruments-v5/rapport-devis-instruments-essaim-v5.md` | `lot/compte-organisme-v1`, `1b81eed4` | `cc6d5481b67e790e69a204f045145ca29886e6ff7d0293d11d810252c115354d` |
| 2 | `docs/notes/organisme-essaim-communicant-v1/devis-et-instruments-v5/a-faire-avant-preenregistrement-pilote-v2.md` | idem | `a6794398004e6dbd21827a183d66ef7c964728ec420c5947ba653b70f11b2828` |
| 3 | `src/controle_ia/garde_google_v3.py` | `main`, `2594b995` | `923679b51cfc84b65ff7cfc65296378d08e6d4e64f6b427823d23ba24f4afe91` |
| 4 | `docs/notes/demandes-fable-api-2026-11-22-v1/reponse-10/relecture-fable-api.md` | `main`, `2594b995` | `f41a63d5400cd4b99241049c887eff4f181e4635aefced3f20f5cbfb8c8ad067` |

- **Rien d'autre n'a été ouvert**, hors le mandat et les consignes permanentes du dépôt (`CLAUDE.md`), que la session charge d'office. J'ai seulement listé les noms du dossier de l'organisme, pour y placer ce rendu. Je n'ai donc lu ni le code du lanceur v3, ni le transport de Kimi, ni le plan du pilote (bras, cycles, cartes par requête), ni les pages de Google versées, ni aucun journal. Là où l'avis touche à ces pièces, il dit « à confirmer par l'organisme ».
- La pièce 3 a été **exécutée** (fonctions pures, sans réseau) sur les réglages proposés ici. Résultats : `calcul-avis-essaim-argon-v1.json`, clé `garde.execution`.
- Argon et son interface sont postérieurs à ce que je sais de mémoire. Tout ce que je dis de l'interface de Google hors de la pièce 3 est une hypothèse.

**Marques.** [FAIT RAPPORTÉ] : lu dans une pièce citée, repère donné, ou sorti de l'exécution de la pièce 3. [HYPOTHÈSE] : cru, ni lu ni mesuré. [PROPOSITION] : recommandé. Un nombre calculé renvoie à une clé de `calcul-avis-essaim-argon-v1.json` (« calcul : clé ») ; il vaut ce que valent ses entrées. « Exécution : clé » renvoie à la même pièce, sous `garde.execution`.

## Verdict

1. **Forme : (b), amendée sur quatre points — confiance 0,75.** L'adaptateur et ses épreuves passent d'abord ; la fumée de six appels passe par lui (borne de 5 USD) ; le quart est une répétition sur trois mondes entiers de la calibration, en deux courses (20 puis 40 USD), données exclues ; le pilote entier court ensuite sur les mondes neufs, au devis mesuré. Toutes les bornes doublent en décembre.
2. **Réglages : niveau `high` explicite, pensées demandées, flux, plafond de 65 536 jetons dont 49 536 de provision de réflexion.** Aucun repli au budget à l'intérieur d'une course. Les critères de passage sont des critères d'instrument, scellés avant la course ; le signe du résultat n'en fait pas partie.
3. **Le devis « attendu » n'est pas mesuré.** Ni les jetons d'entrée ni la réflexion d'Argon sur la case servie ne sont connus. Ma prévision est la ligne « haut » : 150 USD en novembre, 299 en décembre pour le pilote. Un comptage gratuit des jetons d'entrée, puis les six appels de la fumée, le diront pour 5 USD au plus.

## Écarts relevés (une ligne chacun)

1. **Colonne « pire » du devis préliminaire.** Sous les hypothèses énoncées (20 000 jetons d'entrée, 65 536 de sortie), le calcul donne 520,13 et 1 040,26 USD, non 526 et 1 052. Les nombres de la table sortent d'une entrée de 24 001 jetons. Les colonnes « attendu » et « haut » sont justes (74,80 et 149,60 ; 149,60 et 299,20) [calcul : `controle_table_organisme`].
2. **Ce « pire » n'est pas le vrai pire.** Je déduis la borne d'entrée des pièces 1 et 2 : 64 960 octets, d'après le cas d'artefact « 64 961 octets », plus 256 jetons de mise en forme, d'après H3. Avec elle, 748 requêtes au plafond coûtent 587,77 USD en novembre et 1 175,54 en décembre [HYPOTHÈSE pour la borne ; calcul : `scenarios.pire_plafond_et_octets`].
3. **748 ou 744.** La pièce 1 compte 748 requêtes ; la pièce 2 (§ 9) compte 744 appels. 744 se divise par douze mondes (62 par monde), 748 non. Un « quart » doit être un nombre entier de mondes : à confirmer par l'organisme.
4. **Plafond de la fumée de Kimi.** 1 USD dans la pièce 1 (§ 4), 2 USD dans la pièce 2 (§ 2).
5. **L'option (c) n'est pas « prévue par la garde » comme mode de course.** La garde ne prévoit le budget que comme repli déclaré, une fois, après un refus du niveau par Google. Le budget de 16 384 y est dit « SUPPOSÉ » (pièce 3, l. 34-36 et 58-61).
6. **L'essai « `max_tokens` de 16 » de la pièce 2 (§ 2) ne peut pas partir vers Google.** La garde refuse tout plafond inférieur à la provision plus 16 000 [exécution : `avant_envoi.plafond_16000_provision_1_refuse`].
7. **Ordre de (b).** Une fumée avant l'adaptateur contredit la pièce 2 (§ 2) : l'essai de fumée passe par le transport réel, éprouvé d'abord sur le faux fournisseur.
8. **« Case de 9 000 jetons ».** Le compte dépend du découpeur. Celui de Kimi n'a pas encore servi (pièce 2, § 2, H3 : téléchargement à demander). L'entrée de 10 000 jetons retenue pour Argon n'est donc pas mesurée.
9. **Tolérance de 74 échecs et garde des formes fausses.** Une carte perdue compte comme une forme fausse (pièce 2, § 5, réserve 1), et la garde du total ne laisse que +24 sur douze mondes. À 5 % de cartes perdues, un bras de 576 cartes en perd 29 : il échoue à la garde par la seule infrastructure [HYPOTHÈSE : 48 cartes par monde pour le bras (a) ; calcul : `criteres.cartes_perdues_sur_douze_mondes`]. Cela vaut aussi pour Kimi.

---

## 1. Le choix entre (a), (b) et (c)

### (a) Pilote entier tout de suite : non

- [FAIT RAPPORTÉ] Le lanceur v3 n'admet pour le pilote que l'adaptateur et le transport de Kimi, en classe exacte et à leurs empreintes (pièce 1, verdict). Rien ne peut partir vers Argon sans l'adaptateur de (b).
- [FAIT RAPPORTÉ] Les hypothèses de dépense H1 à H4 ne sont encore établies pour aucun fournisseur (pièce 2, § 2). Pour Google, elles restent à écrire (§ 4.3 ci-dessous).
- [HYPOTHÈSE] Le coût attendu n'est connu qu'à un facteur deux ou trois près (§ 6, points 1 et 2).
- [FAIT RAPPORTÉ] Pour Kimi, la borne de la course est le vrai pire, 203,94 USD (pièce 1, verdict ; pièce 2, § 1). J'en déduis que la course peut toujours finir sous sa borne. [HYPOTHÈSE ; calcul] Pour Argon, le vrai pire est de 588 USD en novembre et de 1 176 en décembre. Le plafond sera donc placé en dessous, et la course pourra s'arrêter avant la fin. Il faut avoir écrit ce qui se lit alors.
- [PROPOSITION] Le seul argument pour (a) est le tarif de novembre. Il vaut entre 74,80 et 149,60 USD [calcul : `cumul_du_plan`]. C'est moins que le prix d'un pilote inutilisable.

### (c) Réflexion réduite par le budget : non

- [FAIT RAPPORTÉ] Le budget n'est permis par la garde que comme repli déclaré, quand Google refuse le niveau par une erreur 400 qui le nomme (pièce 3, l. 34-36 et 174-178).
- [FAIT RAPPORTÉ] Le budget de repli d'Argon, 16 384, est « SUPPOSÉ ». Sous 8 192, Argon n'a pas pensé du tout sur 22 réponses. Un budget seul est déprécié chez Gemini 4 (pièce 3, l. 58-61).
- [FAIT RAPPORTÉ] Ma réponse 10 exclut déjà de l'analyse principale les cellules d'Argon jouées sans réflexion, parce qu'un tour affaibli fausse la comparaison (pièce 4, article 3 et décision 2).
- [PROPOSITION] Un bras à réflexion bridée n'est pas le même organisme. S'il échoue devant la barre, on ne saura pas si c'est l'essaim ou la bride. Le résultat négatif serait illisible.
- [PROPOSITION] Si le coût mesuré au niveau `high` est jugé trop haut, le repli propre est le niveau `medium`. C'est un niveau admis et non déprécié (pièce 3, l. 68), et la garde sait le contrôler [exécution : `avant_envoi.niveau_medium_declare`]. C'est un écart déclaré à la règle « niveau le plus haut admis », donc une décision du directeur (décision 8).

### (b), amendée : retenue — confiance 0,75

Quatre amendements [PROPOSITION] :

1. **Ordre.** L'adaptateur, le transport et le faux serveur de Google sont écrits et éprouvés d'abord, sans dépense. La fumée passe ensuite par eux. Une fumée envoyée par un autre script établirait des faits sur Google, pas sur le transport du pilote.
2. **Le quart est une répétition, pas un morceau du pilote.** Il court sur trois mondes entiers de la calibration, déjà lus, avec les deux bras, en deux courses : un monde, puis deux. Ses données sont exclues du pilote. Le pilote entier, 748 requêtes, court ensuite sur les mondes neufs.
3. **Critères de passage.** Ce sont des critères d'instrument, chiffrés et scellés avant la course. Le signe du résultat scientifique n'en fait pas partie (R3).
4. **Tarif.** Une garde de date entre dans le lanceur. Toutes les bornes sont données aux deux tarifs. Aucune étape n'est sautée pour gagner le tarif de novembre.

Ce qui me ferait changer d'avis :
- vers une répétition plus courte (un seul monde) : aucun défaut sur les 62 premiers appels, et un calendrier qui commande (décision 3) ;
- vers le niveau `medium` : un coût moyen mesuré au-delà de ce que le directeur accepte (décision 8) ;
- vers (a) : rien de ce que je connais.

---

## 2. Les étapes : tailles, bornes d'arrêt, critères de passage

### 2.1 Vue d'ensemble

| étape | contenu | requêtes | borne d'arrêt, novembre (décembre) | dépense en novembre : attendu de l'organisme / ma prévision |
|---|---|---|---|---|
| 0 | code, épreuves, comptage gratuit, lectures de la console | 0 | 0 | 0 |
| 1 | fumée | 6 | 5 USD (10) | 1,37 / 1,80 |
| 2a | répétition, premier monde | 62 | 20 USD (40) | 6,20 / 12,40 |
| 2b | répétition, deux mondes de plus | le reste du quart | 40 USD (80) | 12,50 / 25,00 |
| 3 | pilote entier sur les mondes neufs | 748 | 1,3 fois le devis mesuré | 74,80 / 149,60 |

[HYPOTHÈSE pour les volumes ; calcul : `scenarios`, `fumee`, `cumul_du_plan`]. Avant le pilote, la dépense est bornée à 65 USD en novembre et à 130 en décembre ; elle est prévue entre 20 et 39 USD en novembre.

Coût par requête et par étape selon six scénarios [calcul : `scenarios`] :

| scénario (jetons d'entrée / de sortie, réflexion comprise) | par requête, novembre | premier monde | quart | pilote, novembre | pilote, décembre |
|---|---|---|---|---|---|
| attendu de l'organisme (10 000 / 8 000) | 0,10 | 6,20 | 18,70 | 74,80 | 149,60 |
| haut de l'organisme (20 000 / 16 000) | 0,20 | 12,40 | 37,40 | 149,60 | 299,20 |
| prévision de cet avis (25 000 / 15 000) | 0,20 | 12,40 | 37,40 | 149,60 | 299,20 |
| prudent (40 000 / 32 768) | 0,41 | 25,28 | 76,24 | 304,94 | 609,89 |
| pire énoncé par l'organisme (20 000 / 65 536) | 0,70 | 43,11 | 130,03 | 520,13 | 1 040,26 |
| pire, plafond et borne d'octets (65 216 / 65 536) | 0,79 | 48,72 | 146,94 | 587,77 | 1 175,54 |

- [HYPOTHÈSE] Ma prévision déplace le coût vers l'entrée. La case fait 529 à 530 lignes de dix nombres à trois décimales (pièce 2, § 4), soit de l'ordre de 30 000 octets. Un découpeur qui coupe finement les nombres rend jusqu'à un jeton par octet.
- [HYPOTHÈSE ; calcul : `bornes.novembre.quart`] La borne de 60 USD laisse finir le quart tant que le coût moyen ne dépasse pas 0,318 USD par requête, soit une sortie moyenne de 26 800 jetons pour 25 000 jetons d'entrée. Sous le scénario « prudent », la course s'arrête dans le premier monde, après 48 requêtes et 19,57 USD [calcul : `arret_premier_monde_scenario_prudent`]. C'est le rôle de la borne.

### 2.2 Étape 0 — sans dépense

1. **Code** (détail au § 4) [PROPOSITION] : un transport et un adaptateur stricts pour Argon, un faux serveur de Google, un lanceur de nom neuf (R12). Le lanceur n'admet qu'Argon, appelle la garde de Google v3 avant chaque envoi et après chaque réponse, porte une table de prix datée et une garde de date, et écrit en dur le chemin du registre de chaque course.
2. **Épreuves** [PROPOSITION] : les 49 cas de la pièce 1 rejoués, plus les artefacts propres à Google (§ 4.5). Rejeu par un relecteur neuf, comme la pièce 1 le demande pour le transport de Kimi (§ 4).
3. **Épreuve d'identité de la chaîne d'analyse** [PROPOSITION ; valeurs : FAIT RAPPORTÉ, pièce 2, § 5]. Les cartes de la base B3R, servies par le faux serveur à travers l'adaptateur, doivent redonner 6, 16, 0, 3, 0, 15, 5, 6, 13, 0, 0, 0 formes fausses (somme 64) et 10 conditionnelles sur 14. Celles de B3 doivent échouer aux deux gardes (total 113, quatre mondes en queue).
4. **Comptage gratuit des jetons d'entrée** [HYPOTHÈSE : l'interface de Google compte les jetons d'une invite sans générer et sans frais ; à lire dans sa documentation]. Il porte sur l'invite réelle, bras par bras, sur les douze mondes de calibration. Cet appel emploie la clé sans dépenser : l'autorisation est à demander.
5. **Au directeur** (compte, nœud de décision) : le tarif relu sur sa pièce primaire, daté, avec l'heure et le fuseau de la bascule ; les quotas d'Argon sur le compte ; l'existence d'une limite dure ou d'un crédit prépayé ; un projet et une clé réservés à ces courses (décision 5).
6. **Scellé d'instrument** : les critères S, M et Q ci-dessous, contre-lus par un sous-agent neuf (R2), avant la fumée.

Sortie de l'étape 0 : épreuves tenues, rejeu neuf tenu, scellé contre-lu, GO.

### 2.3 Étape 1 — fumée, six appels, borne de 5 USD (10 en décembre)

| n° | appel | plafond de sortie, provision | ce qu'il établit |
|---|---|---|---|
| 1 à 4 | invite réelle du pilote, deux mondes de calibration, deux appels par bras | 65 536, 49 536 | jetons d'entrée, volume de pensée et de texte, modèle servi, durée, forme du flux, cartes évaluables |
| 5 | essai de coupure au plafond : une invite qui pousse à écrire long | 16 001, provision déclarée de 1 | la réflexion est-elle comptée dans le plafond ; fin `MAX_TOKENS` ; usage rendu sur une coupure |
| 6 | requête coupée par le client après le premier événement reçu | 65 536, 49 536 | usage absent, donc réserve entière ; aucun renvoi ; facturation d'une requête interrompue |

- [calcul : `fumee`] Somme des réserves au pire : 4,22 USD en novembre, 8,44 en décembre. Les bornes de 5 et de 10 USD les couvrent.
- [FAIT RAPPORTÉ ; exécution : `avant_envoi.essai_coupure_16001_provision_1`] L'appel 5 passe la garde à la lettre. [PROPOSITION] Il en contredit l'esprit : c'est une épreuve d'artefact au sens de R5, à citer telle quelle dans le GO (décision 4).
- Les sorties de la fumée sont exclues de toute analyse.

**Critères S, de la fumée au premier monde. Tous sont exigés** [PROPOSITION] :

- **S1.** Six envois, six réserves, six lignes au journal ; le compteur de la connexion vaut six.
- **S2.** Les appels 1 à 4 sont des réponses au sens de la garde : fin `STOP`, texte non vide, pensées au-dessus de zéro. Le modèle servi est le modèle demandé, le même aux six appels. L'usage rendu est complet.
- **S3.** Appel 5 : fin `MAX_TOKENS`, et pensées plus texte au plus égales au plafond, à 1 % près (16 161). Sinon la réflexion sort du plafond, le pire par requête n'est plus borné : arrêt.
- **S4.** Appel 6 : usage absent, réserve entière comptée, aucun renvoi.
- **S5.** Jetons d'entrée rendus au plus égaux aux octets de l'invite plus 256, aux six appels.
- **S6.** Plus grand total de pensées et de texte des appels 1 à 4 au plus égal à 49 152, soit les trois quarts du plafond. Sinon la tâche déborde au niveau `high` : arrêt, décision.
- **S7.** Coût moyen des appels 1 à 4 au plus égal à 0,318 USD au tarif de novembre. Au-delà, le quart ne finirait pas sous sa borne : le devis est refait avant d'aller plus loin.
- **S8.** Durée médiane des appels 1 à 4 mesurée ; durée projetée du quart (187 fois la médiane) au plus égale à 36 heures.
- **S9.** Console de Google lue par le directeur : six requêtes vues, facture au plus égale à la dépense comptée. Si la console tarde plus de 24 heures, la décision de partir revient au directeur.

### 2.4 Étape 2 — répétition au quart, en deux courses

- **Mondes** [PROPOSITION ; valeurs : FAIT RAPPORTÉ, pièce 2, § 5]. Trois mondes de calibration, tirés avant la course par une graine consignée (R9), un par strate de formes fausses de la barre : zéro (mondes 2, 4, 9, 10, 11), de 3 à 6 (mondes 0, 3, 6, 7), de 13 à 16 (mondes 1, 5, 8). Chaque monde est entier : les deux bras, tous les cycles.
- **Pourquoi la calibration** [PROPOSITION]. Rien de neuf n'est brûlé. Tout peut être lu et corrigé. Les valeurs de la barre y sont connues, ce qui éprouve la chaîne d'analyse de bout en bout.
- **Deux courses, deux registres, deux plafonds** [PROPOSITION] : 2a, un monde sous 20 USD ; 2b, deux mondes sous 40 USD. Le passage de 2a à 2b est prononcé par un script figé, sans attendre.
- **Ce qui se lit** [PROPOSITION]. Les relevés d'instrument se lisent tout de suite : coûts, jetons, défauts, cartes « rien ». Le relevé scientifique (couverture, formes fausses) ne se calcule qu'après le scellé de la partie scientifique du préenregistrement (§ 5.1). Il ne peut donc rien y changer.

**Arrêts pendant les courses 2a et 2b** [PROPOSITION] :
- plafond du registre atteint ;
- trois défauts de suite du même type (fausse alerte sur 187 appels : 0,001 si ce type touche 2 % des appels, 0,022 à 5 % [calcul : `criteres.trois_defauts_de_suite_du_meme_type`]) ;
- sept défauts dans le premier monde (la course s'arrête alors avec une probabilité de 0,03 pour un taux vrai de 5 %, de 0,43 à 10 %, de 0,98 à 20 % [calcul : `criteres.arret_si_7_defauts_ou_plus_sur_62`]) ;
- tous les arrêts durs du § 5.6.

**Critères M, du premier monde aux deux suivants** [PROPOSITION] :

- **M1.** Les 62 requêtes sont faites sous la borne.
- **M2.** Six défauts au plus après traitement.
- **M3.** Aucun total de pensées et de texte au-delà du plafond envoyé ; une seule version servie ; registre intact ; une requête par réserve.
- **M4.** Au moins la moitié des cartes des réponses complètes sont évaluables. Sinon la consigne écrite pour Kimi ne passe pas chez Argon : arrêt, correction, nouveau premier monde.

**Critères Q, du quart au pilote. Verdict prononcé par un sous-agent neuf, qui applique les critères scellés (R13 par analogie)** [PROPOSITION] :

- **Q1.** Les trois mondes sont entiers, sous les deux bornes.
- **Q2.** Comptes : registres intacts ; réserves, envois, lignes du journal et requêtes vues sur la console en nombre égal ; facture au plus égale à la dépense comptée.
- **Q3.** Cartes perdues : au plus 4 appels sur 187 dont les cartes sont perdues, toutes causes confondues (défaut après traitement, flux coupé, échec non rattrapé), rapportés par type et par bras.
- **Q4.** Échecs avant traitement au premier envoi : au plus 9 sur 187.
- **Q5.** Marge au plafond : 95e centile du total de pensées et de texte au plus égal à 49 152.
- **Q6.** Cartes « rien » parmi les cartes des réponses complètes : au plus 10 %. Seuil à recaler par l'organisme, qui connaît le taux de Kimi.
- **Q7.** Mécanique de l'essaim : chaque message prévu est délivré d'après le journal ; toutes les invites passent le contrôle de la liste blanche (condition de la R3, pièce 2, § 8).
- **Q8.** Une seule version servie sur les 193 appels de la fumée et du quart.
- **Q9.** Instrument inchangé entre le quart et le pilote : mêmes empreintes du lanceur, de l'adaptateur, du transport, de la garde et des gabarits d'invite. Tout changement renvoie à un nouveau premier monde.
- **Q10.** Devis du pilote : 748 fois le coût moyen mesuré, au tarif du jour de la course. Plafond : 1,3 fois le devis. Durée projetée : 748 fois la durée médiane mesurée. GO du directeur sur ce devis.

Pourquoi le seuil de Q3 [calcul : `criteres.appels_a_cartes_perdues_au_plus_4_sur_187` et `criteres.cartes_perdues_sur_douze_mondes`] :
- [FAIT RAPPORTÉ] Une carte perdue compte comme une forme fausse, et la garde du total n'accorde que +24 sur douze mondes (pièce 2, § 5).
- [HYPOTHÈSE : 48 et 52 cartes par monde] Un taux de perte de 2 % mange la moitié de cette marge (11,5 cartes pour le bras (a), 12,5 pour le bras (c)). Un taux de 4 % la mange toute.
- Le seuil « 4 sur 187 » passe avec une probabilité de 0,96 si le taux vrai est de 1 %, de 0,68 à 2 %, de 0,34 à 3 %, de 0,04 à 5 %.

Devis du pilote selon le coût moyen mesuré au quart [calcul : `bornes.*.devis_pilote_selon_cout_moyen_mesure`] :

| coût moyen mesuré (USD par requête, tarif de novembre) | devis en novembre | plafond | devis en décembre | plafond |
|---|---|---|---|---|
| 0,10 | 74,80 | 98 | 149,60 | 195 |
| 0,15 | 112,20 | 146 | 224,40 | 292 |
| 0,20 | 149,60 | 195 | 299,20 | 389 |
| 0,25 | 187,00 | 244 | 374,00 | 487 |
| 0,318 (limite de passage du quart) | 238,13 | 310 | 476,26 | 620 |

### 2.5 Étape 3 — pilote entier

- [PROPOSITION] Il part après quatre choses : le verdict « sain » du quart, le préenregistrement scellé et contre-lu (§ 5), le rapprochement de la console, le GO sur devis mesuré.
- [PROPOSITION] Les mondes courent dans un ordre tiré d'avance. Chaque monde est fini, les deux bras alternés, avant le suivant. Un arrêt laisse ainsi des mondes entiers.
- Arrêts : § 5.6.

### 2.6 Calendrier et tarif

- [FAIT RAPPORTÉ] Le lanceur est séquentiel ; toute version parallèle demande de nouvelles épreuves (pièce 2, § 9).
- [HYPOTHÈSE pour la durée d'un appel ; calcul : `durees_selon_minutes_par_appel`] :

| minutes par appel | premier monde | quart | pilote | dernier départ du pilote pour finir avant la bascule, marge de 30 % |
|---|---|---|---|---|
| 1,5 | 1,6 h | 4,7 h | 18,7 h | 29 novembre, 09:41 UTC |
| 3 | 3,1 h | 9,3 h | 37,4 h | 28 novembre, 09:22 UTC |
| 6 | 6,2 h | 18,7 h | 74,8 h | 26 novembre, 08:45 UTC |
| 10 | 10,3 h | 31,2 h | 124,7 h | 23 novembre, 15:56 UTC : hors d'atteinte, les étapes 0 à 2 passent avant |

- [PROPOSITION] Tant que l'heure de la bascule n'est pas lue sur la pièce primaire, la garde de date se place au 30 novembre, 10:00 UTC. C'est minuit du 1er décembre au fuseau le plus en avance. Une fois le fuseau lu, elle se recale, avec une heure de marge.
- [HYPOTHÈSE] Probabilité que le pilote entier finisse au tarif de novembre : 0,25. Le surcoût de décembre est de 74,80 USD dans le cas attendu de l'organisme, de 149,60 dans ma prévision [calcul : `cumul_du_plan`]. C'est le prix du contrôle : il entre au devis.
- [FAIT RAPPORTÉ] L'ancre et la clé du sceau vivent dans un dossier qui peut disparaître avec un conteneur de session (pièce 1, § 4). [PROPOSITION] Une course de 5 à 75 heures ne tient pas dans un tel conteneur : il faut une machine qui survit à la session (décision 6).

---

## 3. Les réglages d'Argon

| réglage | valeur | raison |
|---|---|---|
| modèle | `gemini-4-argon` ; version servie lue dans chaque réponse et gelée à la fumée | une autre version servie arrête la course |
| mode | flux | limite de sortie de 65 536 en flux, de 32 768 hors flux [FAIT RAPPORTÉ, pièce 3, l. 73] |
| réflexion | `thinkingConfig.thinkingLevel` à `"high"`, écrit dans le corps ; `includeThoughts` vrai ; aucun `thinkingBudget` | niveau le plus haut admis pour Argon ; un niveau et un budget ensemble rendent une erreur 400 [FAIT RAPPORTÉ, pièce 3, l. 42-48 et 68-70] |
| plafond de sortie | `maxOutputTokens` à 65 536 | le plus haut admis en flux |
| provision de réflexion | 49 536 ; il reste 16 000 jetons de texte | le minimum de texte de la garde [FAIT RAPPORTÉ, pièce 3, l. 77] |
| limite de mots de l'invite | 3 137 mots au plus | règle (3) de la garde, à 5,1 jetons par mot [calcul : `garde.mots_max_si_provision_49536`] |
| budget de repli | aucun à l'intérieur d'une course | § 1, option (c) |
| candidats, outils, cache | un seul candidat ; aucun outil ; aucun contenu mis en cache | [PROPOSITION] |
| filtres de sécurité | réglage par défaut du fournisseur, non modifié ; tout refus journalisé | [PROPOSITION] |
| température, graine | celles du plan écrit pour Kimi si Google les admet ; sinon le défaut, dit au préenregistrement | [PROPOSITION ; § 6, point 16] |
| clé | en en-tête, jamais dans l'adresse, jamais au journal | [PROPOSITION] |

- [FAIT RAPPORTÉ ; exécution : `avant_envoi.pilote_high_65536_provision_49536_mots_3137_flux`] L'appel `verifier_reglages_google("argon", corps, provision=49536, mots=3137, mode="flux")` rend une liste vide : l'envoi peut partir. Le même corps est refusé hors flux, à 3 138 mots, sans `includeThoughts`, ou avec un niveau et un budget.
- [PROPOSITION] Si la limite de mots de l'invite dépasse 3 137, la provision descend : provision = 65 536 − ⌈5,1 × mots⌉ − 1. Pour 4 000 mots, 45 135 [calcul : `garde.provision_selon_limite_de_mots`].
- [FAIT RAPPORTÉ] Argon n'a jamais été servi au-delà de 32 768 jetons de sortie ; la limite de 65 536 en flux vient d'une ligne de documentation (pièce 3, l. 54-55). Le premier appel de la fumée le confirme ou l'infirme.

**Pourquoi le flux** [PROPOSITION] :
1. Hors flux, la provision ne peut pas dépasser 16 768 [calcul : `garde.provision_max_hors_flux`]. Rien ne dit que la réflexion d'Argon au niveau `high` tient dessous.
2. Une génération de plusieurs minutes hors flux risque un délai dépassé, avec une génération payée et aucun usage rendu.
3. Le flux laisse mesurer : temps jusqu'au premier événement, silences, progression.

**Pourquoi 65 536 et pas moins** [HYPOTHÈSE, puis PROPOSITION]. Le niveau `high` ne borne pas la réflexion ; seul le plafond la borne, si l'appel 5 de la fumée l'établit. Un plafond plus bas ne réduit pas le coût attendu. Il réduit le pire par requête et multiplie les coupures, donc les cartes perdues. Je garde un seul réglage de la fumée au pilote : ce que le quart mesure vaut alors pour le pilote.

**Pourquoi aucun repli au budget dans une course** [PROPOSITION]. Un repli par appel, même déclaré, mêlerait dans un même bras des appels au niveau et des appels au budget. Une erreur 400 qui nomme le niveau arrête la course. [FAIT RAPPORTÉ] Le niveau `high` a été accepté pour Argon le 21 novembre (pièce 3, l. 47-48) : ce refus est peu probable.

**Leviers de coût non retenus** [HYPOTHÈSE pour leur existence chez Argon] : le traitement par lots (hors flux, donc plafond de 32 768, et délai inconnu) ; le cache implicite de l'entrée (la dépense est comptée sans remise, ce qui est prudent) ; le niveau `medium` et le budget (§ 1).

---

## 4. Mesures et gardes à ajouter au lanceur pour Argon

### 4.1 Coupure

Trois coupures, trois traitements [PROPOSITION] :

1. **Coupure au plafond** (fin `MAX_TOKENS`). C'est un défaut, jamais une réponse [FAIT RAPPORTÉ, pièce 3, l. 21-25 et 163-164]. Le texte partiel est jeté : ni servi aux autres agents, ni noté. La dépense est comptée à l'usage rendu. Aucun renvoi.
2. **Flux coupé** : le flux finit sans événement final (celui qui porte la fin et l'usage), ou une erreur arrive en cours de flux. L'usage est tenu pour absent, la réserve entière est comptée. C'est la règle du transport de Kimi quand le champ de réflexion manque [FAIT RAPPORTÉ, pièce 2, § 10]. Aucun renvoi ; texte partiel jeté.
3. **Coupure par le client** : un délai total par appel et un délai de silence entre deux événements. Valeurs de la fumée : 30 minutes et 180 secondes. Ensuite : trois fois le maximum observé, avec un plancher de 15 minutes et de 120 secondes. À l'expiration, la connexion est fermée, la réserve entière est comptée, l'appel est un défaut.

- [PROPOSITION] Les délais sont larges à dessein : chaque coupure coûte une réserve au registre et perd des cartes.
- [PROPOSITION] **Garde de dépassement** : si le total de pensées et de texte dépasse le plafond envoyé de plus de 1 %, la course s'arrête. C'est l'analogue du cas « réflexion hors du compte (10) » de la pièce 1.

### 4.2 Défaut Google

- [PROPOSITION] Après chaque réponse, le lanceur appelle `defaut_reponse_google(fin, texte, pensees, blocage)`, avec : la fin de l'événement final ; le texte des seules parties qui ne sont pas des pensées ; le compte de jetons de pensée de l'usage ; le motif de blocage de l'invite. La garde rend alors `MAX_TOKENS`, un motif de refus, `VIDE`, `SANS_PENSEES` ou une autre fin [FAIT RAPPORTÉ ; exécution : `apres_reponse`].
- [PROPOSITION] **Deux pièges des pensées demandées.** Si les résumés de pensées entrent dans le texte, une réponse sans texte passe pour non vide. Et un résumé de pensée ne doit jamais être servi à un autre agent ni lu comme une carte. Les deux cas sont à éprouver sur artefact.
- [PROPOSITION] **Défauts que la garde ne voit pas, à ajouter dans l'adaptateur** :
  - version servie différente de la version gelée : arrêt ;
  - usage absent ou incomplet, compte de pensées compris : usage tenu pour absent, réserve entière ;
  - plus d'un candidat : défaut ;
  - total rendu incohérent avec la somme de l'entrée, du texte et des pensées : le lanceur compte le plus grand des deux.
- [PROPOSITION] **Avant traitement** :
  - erreur 400 qui nomme le niveau : arrêt de la course, aucun repli ;
  - autre erreur 400, 403 ou 404 : arrêt (réglage ou clé) ;
  - erreur 429, 500 ou 503 sans aucun événement reçu : une seule relance déclarée, après l'attente indiquée ou 60 secondes, avec sa réserve et sa ligne au journal ; un second échec est un échec ; deux requêtes de suite en échec arrêtent la course.
- [PROPOSITION] **Aucune relance après traitement.** Avant traitement, aucun contenu n'existe : relancer ne trie rien. Après, relancer une réponse coupée ou refusée serait trier sur le contenu.
- [PROPOSITION] Le transport fait un envoi par appel, compté sur la connexion, par la bibliothèque standard. [HYPOTHÈSE] La bibliothèque cliente de Google peut relancer d'elle-même. L'attaque A3 de la pièce 1 (relances cachées : 529,34 USD facturés pour 176,45 comptés) vaut ici.

### 4.3 Coût au pire

- [PROPOSITION] **Réserve par appel** : prix d'entrée fois les jetons d'entrée au pire, plus prix de sortie fois le plafond envoyé. [HYPOTHÈSE pour la borne d'entrée ; calcul : `fumee.*.reserve_par_appel_normal`] 0,786 USD en novembre, 1,572 en décembre. Le plafond de sortie d'Argon vaut 2,7 fois celui que je déduis pour Kimi (24 000, d'après le cas d'artefact « `max_tokens` de 24 001 »).
- [PROPOSITION] **Quatre hypothèses pour Google**, calquées sur H1 à H4 (pièce 2, § 2), à établir par la fumée :
  - **G1.** La facture est au plus égale à l'usage rendu, réflexion comprise, au prix de la sortie. Preuve : la console.
  - **G2.** La réflexion est comptée dans le plafond de sortie. Preuve : l'appel 5.
  - **G3.** Les jetons d'entrée sont au plus égaux aux octets plus 256. Preuve : le comptage gratuit et les six appels.
  - **G4.** Un appel échoué ou coupé coûte au plus sa réserve. Preuve : l'appel 6 et la console.
- [PROPOSITION] Sous G1 à G4, la dépense comptée ne dépasse jamais le plafond du registre de la course : 5, 20, 40 USD, puis le plafond du pilote. C'est le vrai pire de chaque étape.
- [FAIT RAPPORTÉ] Hors de ces hypothèses, seule une limite chez le fournisseur tient (pièce 2, § 1 et § 10). [PROPOSITION] Pour Google : un projet et une clé réservés ; une limite dure ou un crédit prépayé si la console en offre ; à défaut, un quota de requêtes par jour abaissé au besoin de l'étape. [calcul : `exposition_par_jour_selon_quota`] 200 requêtes par jour bornent l'exposition à 157 USD par jour en novembre.
- [PROPOSITION] **La réflexion fait l'essentiel de la sortie d'Argon.** Un usage qui l'omettrait multiplierait la facture (attaque A4 de la pièce 1 : 235,97 USD facturés). Champ de pensées absent : usage tenu pour absent, réserve entière.
- [PROPOSITION] **Garde de date** : aucun envoi à partir de la bascule sous la table de prix de novembre. Une course, une table. Les deux tables sont gelées sous un nom neuf, avec la pièce primaire et sa date.
- [PROPOSITION] **Borne d'entrée** : l'envoi est refusé au-delà de la limite d'octets ; après la réponse, des jetons d'entrée au-delà de la borne arrêtent la course.

### 4.4 Mesures à journaliser par appel

[PROPOSITION]
- Identité : monde, bras, agent, cycle, rang ; empreinte du corps ; octets de l'invite.
- Réglages partis : modèle, niveau, plafond, provision, mode ; version et empreinte de la garde ; résultat de la garde.
- Réponse : code de la réponse, identifiant, version servie, fin, motif de blocage.
- Usage : jetons d'entrée, de texte, de pensée, total, jetons servis du cache.
- Dérivés : sortie comptée, coût, réserve, marge au plafond, part de la pensée.
- Flux : nombre d'événements, temps jusqu'au premier événement et jusqu'au premier texte, durée totale, plus long silence, événement final reçu ou non.
- Envois sur la connexion (un), relance déclarée ou non.
- Défaut selon la garde ; cartes rendues, évaluables, « rien ».

### 4.5 Épreuves hors ligne à ajouter, sur le faux serveur de Google

Chaque garde est éprouvée sur un cas sain et sur un artefact (R5) [PROPOSITION] :

1. flux sain : une requête par réserve, dépense comptée au moins égale à la facture ;
2. flux coupé avant l'événement final : réserve entière, aucun renvoi ;
3. événement final sans compte de pensées : réserve entière, défaut ;
4. zéro jeton de pensée : défaut `SANS_PENSEES` ;
5. fin `MAX_TOKENS` : défaut, texte partiel jeté ;
6. refus de Google, invite bloquée : défaut ;
7. texte présent seulement dans des parties de pensée : défaut `VIDE` ;
8. total de pensées et de texte au-delà du plafond : arrêt ;
9. version servie différente : arrêt ;
10. erreur en cours de flux : réserve entière ;
11. erreur 400 qui nomme le niveau : arrêt, aucun budget envoyé ;
12. erreur 503 avant tout événement : une relance déclarée, puis échec ;
13. transport qui cache un second envoi : refusé par la classe exacte et l'empreinte, comme le cas N5 de la pièce 1 ;
14. horloge après la bascule sous la table de novembre : aucun envoi ;
15. corps refusé par la garde (plafond de 65 537, niveau absent, pensées non demandées, mode hors flux) : rien ne part, 0 USD ;
16. jetons d'entrée au-delà de la borne : arrêt ;
17. processus tué en cours de flux, puis reprise : réserve gardée, dépense comptée au moins égale à la facture ;
18. deux candidats : défaut ;
19. carte écrite dans un résumé de pensée : jamais lue comme carte, jamais servie.

---

## 5. Ce qui doit être préenregistré avant le pilote

### 5.1 Trois textes scellés, chacun contre-lu par un sous-agent neuf (R2)

[PROPOSITION]

| texte | quand | contenu |
|---|---|---|
| scellé d'instrument | avant la fumée | critères S, M et Q ; arrêts des courses de répétition ; règle « le relevé scientifique de la répétition ne se calcule pas avant le scellé suivant » |
| préenregistrement, partie scientifique | avant tout relevé scientifique de la répétition, et avant le pilote | hypothèse, prédiction chiffrée et signe, métrique, seuil, plan d'analyse, critères de lecture, liste d'arrêt (R1) |
| préenregistrement, annexe d'exécution | après le verdict du quart, avant le premier appel du pilote | réglages, version servie, tarif et date, plafond, chemins, classes admises et empreintes, devis mesuré |

L'annexe ne peut rien changer à la partie scientifique.

### 5.2 Hypothèse

[PROPOSITION de forme ; l'organisme écrit les siennes, car je n'ai pas lu le plan du pilote]

- **HP-a.** Sur les douze mondes neufs, le bras (a), servi par Argon au niveau `high`, couvre structurellement plus de conditionnelles plantées que la barre B3R, et passe les deux gardes des formes fausses.
- **HP-c.** De même pour le bras (c), avec un facteur de cartes de 1.
- Une seule des deux est principale : celle qui porte l'essaim. L'autre, et l'écart entre les bras, sont secondaires.
- [HYPOTHÈSE, faible] Ma prédiction : 0,2 pour HP-a, 0,25 pour HP-c ; signe attendu nul ou négatif. Une base ajustée par programme sur la même case est une barre haute.

### 5.3 Seuil

[PROPOSITION]

- **Statistique.** D = conditionnelles couvertes structurellement par le bras, moins celles couvertes par B3R, sommées sur les douze mondes neufs. La couverture structurelle est décisive, comme la pièce 2 (§ 6) le recommande ; l'attribution est secondaire.
- **Lecture.** « Bat la barre » : D au moins égal à +2, et les deux gardes passées. « Indéterminé » : D égal à +1. « Ne bat pas » : D nul ou négatif, ou une garde échouée.
- **Pourquoi +2.** Avec 14 conditionnelles en calibration (pièce 2, § 5), l'unité de mesure est une conditionnelle. Sans exécutions jumelles, le bruit entre deux courses n'est pas estimé. [HYPOTHÈSE] Un écart d'une unité est dans ce bruit. Le résultat est un indice, pas un test, comme la comparaison de la pièce 4.
- **Gardes des formes fausses.** Total apparié et queue appariée, seuils de la pièce 2 (§ 5) : +24 ; +8 ; un monde sur douze. La barre par monde est recalculée sur les mondes neufs par le code gelé.
- **Condition de validité, lue avant le résultat.** Si un bras perd plus de 12 cartes sur les douze mondes, soit la moitié de la marge de +24, sa lecture est déclarée invalide pour cause d'instrument, quel que soit le signe (R4).
- **Test de mort.** 8 000 épisodes par verdict, seuil de 0,02, comme la pièce 2 (§ 7) le propose.

### 5.4 Plan d'analyse

[PROPOSITION]

1. **Unité** : le monde. Chaque bras est apparié à la barre dans le monde.
2. **Notation** : par le code gelé, lancée une seule fois, après le dernier appel ou l'arrêt. Les sorties brutes reçoivent leur empreinte à l'arrivée.
3. **Cartes perdues** : toute requête en défaut, coupée ou en échec non rattrapé compte pour les cartes qu'elle devait rendre, toutes « rien ». Aucun remplacement.
4. **Relance** : seulement avant traitement, une fois, déclarée (§ 4.2).
5. **Ordre** : mondes dans un ordre tiré d'avance, graine consignée ; bras alternés dans chaque monde.
6. **Sensibilités** : couverture par attribution ; variante stricte de la garde (+0, aucun monde en queue) ; résultats avec et sans les mondes touchés par un défaut.
7. **Rapporté dans tous les cas** : la table par monde et par bras ; les défauts par type et par bras ; les cartes perdues ; les jetons d'entrée, de pensée et de texte ; le coût par bras et par conditionnelle couverte ; la version servie ; le tarif ; les durées ; les exclusions ; les prévisions face aux résultats.
8. **Course incomplète** (plafond, date, défauts) : aucune lecture décisive. Les mondes entiers sont rapportés en description. La reprise demande un nouveau GO, sous le même préenregistrement, les mêmes réglages et la même version servie. Le passage à la table de décembre est prévu : ce n'est pas un écart.
9. **Exclusions** : la fumée et la répétition, par construction.
10. **Symétrie** (R4) : un résultat trop propre (aucune forme fausse, toutes les conditionnelles couvertes) déclenche le même audit qu'un échec.
11. **Aucune comparaison avec Kimi** : aucune course de Kimi n'existe sous ce préenregistrement.

### 5.5 Clauses propres à Argon

[PROPOSITION]

- L'identifiant demandé et la version servie gelée à la fumée.
- Les réglages du § 3, mot pour mot, avec l'empreinte de la garde v3 et son résultat.
- **La case servie est gelée comme texte**, non comme budget de jetons : les 529 à 530 lignes à trois décimales de `case-9000-3d`. Le compte de jetons change avec le découpeur, le texte non. La barre a été calculée sur ce texte (pièce 2, § 4).
- Le tarif : pièce primaire, date, table de la course, garde de date.
- Les chemins du registre, de l'ancre et de la clé ; le plafond ; les classes admises et leurs empreintes.
- La règle des défauts et des relances (§ 4.2).
- Les hypothèses G1 à G4 et leur preuve à la fumée.

### 5.6 Liste d'arrêt du pilote

[PROPOSITION]

- plafond du registre atteint ;
- garde de date ;
- version servie différente ;
- total de pensées et de texte au-delà du plafond envoyé ;
- jetons d'entrée au-delà de la borne ;
- erreur 400 qui nomme le niveau ;
- cinq défauts de suite (fausse alerte sur 748 appels : 0,0002 pour un taux de 5 %, 0,007 pour 10 % [calcul : `criteres.cinq_defauts_de_suite`]) ;
- 75 échecs (règle existante, pièce 1, § 2) ;
- cartes perdues d'un bras au-delà de 12 : arrêt en fin de monde, lecture du bras invalide ;
- registre refusé, envoi refusé par la garde de Google ;
- contenu interdit trouvé dans une invite (condition de la R3) ;
- lecture d'un résultat scientifique avant la fin.

### 5.7 Mes prévisions d'instrument

[HYPOTHÈSE ; à confronter aux mesures]

| prévision | probabilité |
|---|---|
| Argon accepte un plafond de 65 536 en flux | 0,85 |
| la réflexion est comptée dans le plafond de sortie | 0,9 |
| jetons d'entrée médians d'un appel entre 12 000 et 40 000 | 0,8 |
| jetons d'entrée médians d'au plus 10 000 | 0,1 |
| sortie moyenne par requête d'au plus 8 000 jetons (l'attendu de l'organisme) | 0,2 |
| sortie moyenne entre 8 000 et 16 000 | 0,35 |
| sortie moyenne entre 16 000 et 26 800 | 0,3 |
| sortie moyenne au-delà : le quart s'arrête sur sa borne | 0,15 |
| au plus 4 appels à cartes perdues sur 187 | 0,6 |
| le pilote entier finit au tarif de novembre | 0,25 |

---

## 6. Ce que je ne sais pas, et la mesure qui le tranche

| n° | inconnue | mesure | étape |
|---|---|---|---|
| 1 | Les jetons d'entrée de l'invite réelle chez Argon | comptage gratuit ; jetons d'entrée rendus | 0, 1 |
| 2 | Le volume de pensée et de texte au niveau `high` sur cette tâche : moyenne et queue | appels 1 à 4, puis les 187 du quart | 1, 2 |
| 3 | La réflexion est-elle comptée dans le plafond de sortie | appel 5 ; garde de dépassement | 1 |
| 4 | Argon accepte-t-il 65 536 en flux, et génère-t-il au-delà de 32 768 | premier appel de la fumée ; quart | 1, 2 |
| 5 | La facturation d'un flux interrompu et d'une erreur avant traitement | appel 6 ; console | 1 |
| 6 | La facture égale-t-elle l'usage rendu ; les résumés de pensées sont-ils facturés | console | 1, 2 |
| 7 | Le tarif exact, l'heure et le fuseau de la bascule, un palier de prix pour les longues invites, les remises | pièce primaire, datée, empreintée | 0 |
| 8 | Les quotas du compte, l'existence d'une limite dure, le palier du compte | console, directeur | 0 |
| 9 | La durée d'un appel au niveau `high` en flux | appels 1 à 4 | 1 |
| 10 | Les taux de défauts sur ce contenu : refus, texte vide, zéro pensée, erreurs 429 et 503 | quart | 2 |
| 11 | La composition des 748 requêtes : par monde, par bras, cartes par requête ; 748 ou 744 | l'organisme | 0 |
| 12 | La consigne et la grammaire écrites pour Kimi donnent-elles des cartes évaluables chez Argon | taux de « rien » au quart | 2 |
| 13 | La forme exacte du flux : où paraît l'usage, où paraît le compte de pensées | journaux versés, hors ligne ; fumée | 0, 1 |
| 14 | La stabilité de la version servie sur plusieurs jours | quart, pilote | 2, 3 |
| 15 | La limite de mots de l'invite des proposeurs, que la règle de Google exige | l'organisme | 0 |
| 16 | La température et la graine admises par Argon | page versée | 0 |
| 17 | Le code du lanceur v3 : réserve, échecs, reprise au milieu d'un monde | relecteur neuf du lanceur d'Argon | 0 |
| 18 | La borne d'entrée exacte du lanceur (je déduis 64 960 octets du cas d'artefact « 64 961 octets ») | l'organisme | 0 |
| 19 | Une course de Kimi est-elle encore voulue, pour comparer les modèles | le directeur | — |

- Les points 1, 2 et 9 portent tout le devis. Ils coûtent 5 USD au plus à mesurer.
- Les points 3, 5 et 6 portent la borne. Sans eux, le plafond du registre n'est qu'un compte, pas une limite.

---

## 7. Décisions qui reviennent au directeur

Toutes touchent à la dépense, au compte ou au modèle : ce sont des nœuds de décision, sans défaut à 48 heures.

**Décision 1 — Retenir la forme de l'essai.**
- *Enjeu.* Un pilote lancé sur un instrument non éprouvé peut être payé et inutilisable.
- *Option (b) amendée.* Avantage : chaque inconnue est mesurée avant d'être payée 748 fois. Inconvénient : 193 requêtes de plus et, probablement, le tarif de décembre.
- *Option (a).* Avantage : le tarif de novembre. Inconvénient : aucun adaptateur admis, aucune hypothèse de dépense établie.
- *Option (c).* Avantage : coût par requête plus bas. Inconvénient : budget déprécié et « supposé », bras non comparable.
- *Recommandation.* (b) amendée. Confiance : 0,75.

**Décision 2 — Dire ce qu'est le quart.**
- *Enjeu.* Ce qui se lit avant le scellé ne doit pas pouvoir servir au résultat.
- *Option a : répétition sur trois mondes de calibration, données exclues.* Avantage : tout se lit et se corrige ; la chaîne d'analyse est éprouvée contre des valeurs connues. Inconvénient : 187 requêtes de plus, 19 à 37 USD en novembre.
- *Option b : premier quart du pilote sur les mondes neufs, données gardées.* Avantage : 748 requêtes en tout. Inconvénient : le préenregistrement est scellé avant de connaître Argon, et toute correction exclut le quart.
- *Recommandation.* Option a. Confiance : 0,7.

**Décision 3 — Régler le calendrier face au tarif.**
- *Enjeu.* La bascule du 1er décembre double chaque borne.
- *Option a : aucune course contre la montre.* Le pilote part en novembre seulement s'il finit avant la bascule avec 30 % de marge ; sinon en décembre, au devis doublé. Avantage : aucune étape sautée. Inconvénient : 75 à 150 USD de plus.
- *Option b : répétition raccourcie à un monde, si aucun défaut sur 62 appels.* Avantage : 6 à 12 heures gagnées. Inconvénient : la borne haute du taux de défauts passe de 1,6 % à 4,7 % [calcul : `criteres.borne_haute_95_si_zero_defaut`].
- *Option c : pilote à cheval.* Des mondes entiers en novembre, le reste en décembre sous la seconde table. Avantage : une part du tarif bas. Inconvénient : deux courses, deux registres.
- *Recommandation.* Option a, l'option c étant prévue au préenregistrement. Confiance : 0,7.

**Décision 4 — Autoriser l'essai de coupure au plafond.**
- *Enjeu.* Établir que la réflexion est comptée dans le plafond ; la forme prévue pour Kimi est refusée par la garde de Google.
- *Option a : l'autoriser comme épreuve d'artefact, citée dans le GO.* Avantage : preuve directe pour 0,2 à 0,3 USD. Inconvénient : la provision déclarée de 1 respecte la lettre de la garde, pas son esprit.
- *Option b : s'en passer.* Avantage : aucune entorse. Inconvénient : on l'apprend au premier dépassement, payé, en course.
- *Recommandation.* Option a. Confiance : 0,6.

**Décision 5 — Poser une limite du côté de Google.**
- *Enjeu.* Le registre ne voit ni une facture cachée ni un transport fautif.
- *Option a : projet et clé réservés, plus la limite la plus dure que la console offre* (limite de dépense, crédit prépayé, ou quota de requêtes par jour abaissé). Avantage : la seule borne hors du code. Inconvénient : un passage par la console à chaque étape.
- *Option b : le registre seul.* Avantage : rien à faire. Inconvénient : aucune défense hors de G1 à G4.
- *Recommandation.* Option a. Confiance : 0,8.

**Décision 6 — Héberger les courses.**
- *Enjeu.* L'ancre et la clé du sceau disparaissent avec un conteneur de session ; le registre devient alors inouvrable.
- *Option a : une machine qui survit à la session, ancre et clé dessus.* Avantage : une course de plusieurs jours peut reprendre. Inconvénient : une machine à tenir, donc un devis si elle est payante.
- *Option b : le conteneur de session.* Avantage : rien à monter. Inconvénient : arrêt sûr mais bloquant à la première perte.
- *Recommandation.* Option a, dès le quart. Confiance : 0,8.

**Décision 7 — Donner la forme des GO.**
- *Option a : un GO pour la fumée et le quart* (65 USD en novembre, 130 en décembre, passages par critères scellés), *puis un GO pour le pilote sur devis mesuré.* Avantage : un jour gagné, sans rien céder sur le pilote. Inconvénient : 60 USD engagés sur des critères, sans relecture humaine entre la fumée et le quart.
- *Option b : un GO par étape.* Avantage : un regard à chaque pas. Inconvénient : un jour de plus par pas.
- *Recommandation.* Option a. Confiance : 0,7.

**Décision 8 — Choisir le repli si le devis mesuré est jugé trop haut.** Elle ne se pose qu'après le quart.
- *Option a : payer le devis mesuré.* Avantage : l'organisme à sa pleine force. Inconvénient : le coût.
- *Option b : niveau `medium`, écart déclaré, mesuré d'abord par une sonde appariée de 12 appels* (les mêmes invites aux deux niveaux). Avantage : niveau admis, non déprécié. Inconvénient : un autre organisme, et un écart à la règle de Google.
- *Option c : budget de 16 384.* Avantage : prévu comme repli par la garde. Inconvénient : déprécié, « supposé », zéro pensée observée sous 8 192.
- *Recommandation.* a ou b, jamais c. Confiance : 0,7.

---

## 8. Fichiers, empreintes, rejeu

| fichier | sha256 |
|---|---|
| `calcul_avis_essaim_argon_v1.py` | `9025e5a8ceb0c83b021191a07c47131196fa731d4b9b67376b5cdce76ccc79cf` |
| `calcul-avis-essaim-argon-v1.json` | `fd1676ea5e4f62e2644b494aaad1f844ab829657a66f654d6fe2557b44aa5b9f` |
| `avis-fable-essaim-argon-par-etapes-v1.md` | dans son compagnon `.sha256` |

- Dossier : `docs/notes/organisme-essaim-communicant-v1/reponse-fable-essaim-argon-par-etapes-v1/`. Chaque fichier a son compagnon `.sha256`, au format « empreinte, deux espaces, nom ».
- Rejeu : `python3 -I calcul_avis_essaim_argon_v1.py SORTIE.json --garde CHEMIN/garde_google_v3.py`, la garde étant extraite de `main` (`git show origin/main:src/controle_ia/garde_google_v3.py`). La sortie est la même à l'octet (`fd1676ea…`). Le script refuse une garde d'une autre empreinte et n'écrase jamais une sortie ; les deux refus ont été éprouvés.
- Manifeste : Python 3.13.18, bibliothèque standard seule, aucun tirage aléatoire donc aucune graine, branche de départ au commit `1b81eed4`.
- Ce rendu est une pièce d'avis, à contre-lire. Il ne lance rien et n'engage aucune dépense.

FIN DE L'AVIS

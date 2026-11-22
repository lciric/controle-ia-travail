# Accords de calcul à prolonger et calculs urgents pour l'entretien — projet de la veille de cap — v1

- **Nature** : pièce de travail (classe C), projet soumis à la mère ; la veille ne décide rien. Écrite le 2026-11-22 vers 15:30Z (`date -u`), sur R-4936 (« table des accords à prolonger et des urgences pour l'entretien ») et le mot de Lazar en GO-2026-11-22-77 : « on prolonge et repousse l'expiration et on lance les calculs les plus urgents pour l'entretien ».
- **Méthode** : les 158 accords de type « calcul » qui échoient du 22 novembre au 2 décembre (`registres/go.md`, au commit `3a61eb29`) ont été croisés par programme avec `registres/depenses.md` et les manifestes `manifeste*.json` sous `runs/` (chemins interdits écartés), puis, pour ceux sans trace, avec leur dernière mention au registre des décisions. **Limite** : une course comptée sous un autre accord échappe à ce croisement. L'étage 2 de la ligne 3 de l'organisme, par exemple, a tourné (R-4525). Chaque ligne « jamais parti » ci-dessous est relue au registre ; les autres sont « à confirmer par la mère ».
- **Aucun résultat** n'est lu ni rapporté.

## 1. Accords à prolonger (rien n'a jugé ; l'idée est toujours voulue)

| accord | objet | échéance | état relu | prolonger jusqu'au | pourquoi cette date |
|---|---|---|---|---|---|
| GO-2026-11-10-12 | base boîte noire par action et séquentielle (critère 4 de G0) | 30 nov. | jamais parti ; ses conditions (préenregistrement de T0.8 scellé, code contre-lu) ne sont pas remplies | 31 déc. | porte G0 |
| GO-2026-11-18-14 | affinage des 93 idées des mentors | 25 nov. | jamais parti (lanceur 11 cassé sur `main`, R-4755) | 15 déc. | après l'entretien ; Carbon en commande synchrone |
| GO-2026-11-13-03 | atelier des bassins étroits, une seule relance (R-2558) | 30 nov. | gardé de côté jusqu'à trois préalables (GO-2026-11-22-77) | 31 déc. | réveil sur les préalables, butoir le 15 déc. |
| GO-2026-11-13-01 et -02 | course de l'organisme sur plusieurs générations | 30 nov. | jamais parti : le banc de calibration (GO-2026-11-17-05, 3 USD au plus) n'a jamais été fait | 31 déc. | le banc d'abord |
| GO-2026-11-15-06 | cinq cribles des idées originales | 30 nov. | jamais parti ; un seul crible scellé | 15 déc. | trier : garder un crible |
| GO-2026-11-20-08 | « nouvelles attaques » sur trois générations | 30 nov. | jamais parti (R-4077 seule) | 15 déc. | après la course à une génération |
| GO-2026-11-12-01 | juge-tournoi, manche T0 (sur crédits) | 30 nov. | aucune trace après R-2420 (12 nov.) | à décider | dire si l'idée vit encore ; sinon, fermer nommément |
| GO-2026-11-12-05 | 50 mondes plantés neufs | 30 nov. | « ne sert pas à cette course » (R-2444) | à décider | fermer, ou servir le banc à puits plantés |
| GO-2026-11-21-43 | avis d'un Fable neuf sur l'expérimentateur d'épreuve (nœud N4) | **23 nov.** | aucune trace | 30 nov. | Fable revient le 24 ; ce nœud bloque la course « seuil et moniteurs » |
| GO-2026-11-16-10 et -13 | jeu de l'idée du poids du nul | **échus le 22** | non évaluable (crédit épuisé) ; « relancer » (GO-2026-11-22-77) | ligne neuve | un accord échu ne se prolonge pas : il faut une ligne neuve et un addendum |
| GO-2026-11-10-07 | contrôle de l'artefact d'adaptateur | 27 nov. | attend une issue cloisonnée (R-2671) ; inconnu pour cause de cloisonnement | 31 déc. | à confirmer par la mère |
| GO-2026-11-19-87 et -90 | barreau 5 : enveloppe de relance et première lecture | 30 nov. | inconnu pour cause de cloisonnement | 15 déc. | à confirmer par la mère |
| GO-2026-10-29-03 et -05 | sentinelle et tranche 0 du pilote de la couche 2 | 30 nov. | dernières traces R-695 et R-718 (29 oct.) | à décider | la couche 2 vit-elle encore ? sinon, fermer nommément |

## 2. Accords sans trace de dépense, à confirmer avant de les laisser échoir

Accords d'appels du 21 et du 22 novembre (demandes à Fable, protocole X, consultations ; 46 lignes de 1 à 120 USD). Leur dépense est souvent comptée au total d'une session et non sous leur numéro. Règle proposée : **une demande rendue laisse échoir son accord ; une demande non rendue est prolongée au 30 novembre**. La mère seule sait lesquelles sont rendues. Liste complète en annexe.

## 3. Calculs les plus urgents pour l'entretien du 1er décembre

Ordre proposé. Rang par le lien à l'entretien (analyse sans résultat du 19 novembre, § 4) et par le temps qui reste (assemblage du dossier le 28, scellement le 29).

| rang | calcul | accord | ce qui le retient | quand il doit partir au plus tard |
|---|---|---|---|---|
| 1 | course du saboteur à budget (barreau 8), voie (A) | GO-2026-11-22-71, -75 | additif de Fable et devis scellés ; correctif de vitesse ; la course est estimée vers 40 heures (R-4876) | **le 25 au matin**, pour un verdict scellé le 27 au soir |
| 2 | réajustement de nos lentilles | GO-2026-11-22-05 | en marche depuis le 22 à 07:34Z | suivre jusqu'au rangement |
| 3 | relecture décisive du barreau 5 (répétition générale, puis relecture) | GO-2026-11-21-64 | une offre de machine à trouver ; rien lancé | le 25 |
| 4 | base boîte noire (critère 4) | GO-2026-11-10-12, à prolonger | texte complet de T0.8 à sceller (classe A, Fable revient le 24), code contre-lu | après l'entretien si le texte n'est pas scellé le 26 : la dire « préenregistrée, en cours » |
| 5 | course du bras A des organismes discrets | lignes du bras A | brouillon final du texte (GO-2026-11-22-65), soldes de Google | dès le scellement |

## Annexe — les 158 accords qui échoient du 22 novembre au 2 décembre, croisés par programme

« lignes de dépense » : occurrences du numéro dans `registres/depenses.md` ; « manifestes » : fichiers `manifeste*.json` sous `runs/` qui le citent.

| échéance | accord | montant | lignes de dépense qui le citent | manifestes de course qui le citent | objet (début) |
|---|---|---|---|---|---|
| 2026-11-22 | GO-2026-11-14-09 | 40 USD | 17 | 0 | Étape B bis de T0.7 (sondes entraînées sur la tâche ; préenregistrement brouillons/T0.7-et … |
| 2026-11-22 | GO-2026-11-16-13 | 3.5 USD | 1 | 0 | Idée 1.1 : jeu relancé sur une machine de calcul louée (procédure docs/procedures/machine- … |
| 2026-11-22 | GO-2026-11-17-06 | 17 USD | 2 | 4 | Collisionneur épistémique et organisme d’idéation sur les organismes discrets (section 1.2 … |
| 2026-11-22 | GO-2026-11-18-10 | 34 USD | 0 | 0 | Relance de l'organisme d'idéation, trois courses jumelles le 18 novembre (lignée externe G … |
| 2026-11-22 | GO-2026-11-18-11 | 34 USD | 8 | 0 | Relance de l'organisme d'idéation sur les organismes discrets, trois lignées externes en t … |
| 2026-11-22 | GO-2026-11-18-16 | 34 USD (commun avec GO | 4 | 0 | Relance de l'organisme d'idéation sur les organismes discrets, trois lignées : relance des … |
| 2026-11-22 | GO-2026-11-18-17 | 11.3 USD | 2 | 0 | Organisme d'idéation sur les organismes discrets, lignée kimi (Kimi kimi-k3.1-pro en propo … |
| 2026-11-22 | GO-2026-11-18-18 | 100 EUR | 0 | 0 | Budget de 100 EUR pour le loueur de cartes, rechargé par Lazar à la main (et non par la re … |
| 2026-11-22 | GO-2026-11-18-19 | 11.3 USD | 1 | 0 | Organisme d'idéation sur les organismes discrets, lignée carbon : troisième course Carbon, … |
| 2026-11-22 | GO-2026-11-18-20 | 90 USD | 1 | 0 | Course d'auto-conception de l'organisme d'idéation (N-044, N-045 v2, N-073 ; matière servi … |
| 2026-11-22 | GO-2026-11-18-21 | 5 USD | 1 | 0 | Épreuve réelle des témoins du juge avant la course d'auto-conception (11 cartes de concept … |
| 2026-11-22 | GO-2026-11-18-22 | 11.3 USD | 1 | 0 | Organisme d'idéation sur les organismes discrets, lignée astra : seconde course, avec les  … |
| 2026-11-22 | GO-2026-11-18-23 | 11.3 USD | 1 | 0 | Organisme d'idéation sur les organismes discrets, lignée argon : seconde course, avec les  … |
| 2026-11-22 | GO-2026-11-18-24 | 15 USD | 1 | 0 | Recharge supplémentaire du loueur de cartes de 15 USD, faite par Lazar à la main, pour que … |
| 2026-11-22 | GO-2026-11-18-27 | 80 EUR | 0 | 0 | Budget supplémentaire de 80 EUR : recharges du loueur de cartes et appels d'interface hors … |
| 2026-11-22 | GO-2026-11-18-29 | 4 USD | 0 | 0 | Juge externe d'Astra rejoué en gpt-6.2-astra à la place de gpt-6-astra (bras différé des j … |
| 2026-11-22 | GO-2026-11-18-31 | 4 USD | 1 | 0 | Organisme d'idéation sur les organismes discrets, lignée carbon : bras du juge externe dif … |
| 2026-11-22 | GO-2026-11-18-32 | 4 USD | 2 | 0 | Organisme d'idéation sur les organismes discrets, lignée astra : bras du juge externe diff … |
| 2026-11-22 | GO-2026-11-18-33 | 4 USD | 1 | 0 | Organisme d'idéation sur les organismes discrets, lignée argon : bras du juge externe diff … |
| 2026-11-22 | GO-2026-11-18-54 | 4 USD | 1 | 0 | organisme d'idéation, organismes discrets, juge externe, lignée astra, second bras : juge  … |
| 2026-11-22 | GO-2026-11-20-37 | 10 USD | 1 | 0 | Revendication 14 (juges de la recherche automatisée sous attaque) : version améliorée, non … |
| 2026-11-22 | GO-2026-11-20-52 | 30 USD | 1 | 0 | Collisionneur v9 v2 (2357b9e8…), étage 3, sur l'énoncé neutre du papier « dopamine » (16b2 … |
| 2026-11-22 | GO-2026-11-20-54 | 25,90 USD | 1 | 0 | Collisionneur du papier « dopamine », option (b) : garde corrigée pour compter exactement  … |
| 2026-11-22 | GO-2026-11-20-67 | 456 USD | 0 | 0 | Course « nouvelles attaques » à cinq espèces (v9, additif 1 et devis à cinq espèces une fo … |
| 2026-11-22 | GO-2026-11-21-13 | 8 USD | 0 | 0 | Approfondissement du papier « dopamine » (seuil à 1 % avec peu d'épisodes honnêtes ; emplo … |
| 2026-11-22 | GO-2026-11-21-14 | 30 USD | 1 | 0 | Collisionneur sur le seuil à 1 % et l'usage du papier « dopamine » (moniteurs, contrôle) : … |
| 2026-11-22 | GO-2026-11-21-20 | 8 USD | 1 | 0 | Mathématiques nouvelles pour l'attaque et la défense, au niveau de l'idée : une consultati … |
| 2026-11-22 | GO-2026-11-21-22 | 4 USD | 0 | 0 | Complète GO-2026-11-21-20 : une consultation d'Astra sur le même énoncé neutre (8a102009…) … |
| 2026-11-22 | GO-2026-11-21-23 | 40 USD | 2 | 0 | Brainstorm sur les méthodes d'élaboration de mathématiques nouvelles par les modèles de la … |
| 2026-11-22 | GO-2026-11-21-26 | 28 USD | 1 | 0 | Collisionneur sur la correction de la dérive de régime (seuil à 1 % dont le taux réel trip … |
| 2026-11-22 | GO-2026-11-21-28 | 56 USD (les deux ligne | 0 | 0 | Reprise des deux collisionneurs arrêtés en code 5 (clé Rigaud sans crédit) sur la clé Minu … |
| 2026-11-23 | GO-2026-11-10-01 | 200 USD (plafond de GO | 1 | 0 | Prolongation de GO-2026-11-02-28 (T0.6, course de confirmation 7b, et T0.7 sur la même mac … |
| 2026-11-23 | GO-2026-11-10-02 | 80 USD (plafond de GO- | 9 | 0 | Prolongation de GO-2026-11-02-29 (P3-bis, témoin positif planté) jusqu'au 2026-11-23, péri … |
| 2026-11-23 | GO-2026-11-10-04 | 20 USD | 5 | 0 | T0.7, étape A sur l'instance de la course de confirmation 7b (étape annexe, après la cours … |
| 2026-11-23 | GO-2026-11-10-06 | 20 USD (plafond de GO- | 5 | 0 | Extension de GO-2026-11-10-04 à la variante B de l'étape A de T0.7 : instance séparée (A10 … |
| 2026-11-23 | GO-2026-11-21-39 | 64 USD | 1 | 0 | Trois appels de plus, sur Minuit ou sur les clés externes : (1) collisionneur v9 v3, étage … |
| 2026-11-23 | GO-2026-11-21-43 | 8 USD | 0 | 0 | Avis sur le modèle de l'expérimentateur d'épreuve (N4) : un contre-lecteur Fable 5.2 neuf, … |
| 2026-11-24 | GO-2026-11-21-48 | 10 USD | 0 | 0 | Papier « dopamine », étape 1 en mode exploratoire : rejeu du chiffre publié sur MATH500 (L … |
| 2026-11-24 | GO-2026-11-21-52 | 56 USD | 0 | 0 | Collisionneur v9 v3, étage III, sur deux questions fusionnées écrites par Fable (le but et … |
| 2026-11-24 | GO-2026-11-21-58 | 120 USD | 0 | 0 | Appels du protocole X et des consultations : collisionneur (version avec Neon, après contr … |
| 2026-11-24 | GO-2026-11-22-07 | 16 USD | 1 | 0 | Relectures par Fable 5.2 par l'API (outil src/controle_ia/relecture_fable_api_v3.py, effor … |
| 2026-11-24 | GO-2026-11-22-08 | 20 USD | 0 | 0 | Mot de Lazar vers 2026-11-22T05:08:38Z : « rejoue les a part ». Collisionneurs : les cellu … |
| 2026-11-24 | GO-2026-11-22-09 | 15 USD | 0 | 0 | Mots de Lazar vers 05:10Z : « go » (fausses alertes sur honnêtes imparfaits), « qelles ser … |
| 2026-11-24 | GO-2026-11-22-10 | 45 USD | 0 | 0 | Mot de Lazar vers 05:10Z : « demande approfondie fable puis protocole x », sur la coerciti … |
| 2026-11-24 | GO-2026-11-22-11 | 10 USD | 0 | 0 | Mot de Lazar vers 05:40Z : « papiers a lire . brainstorm avec fable … quelle est la proble … |
| 2026-11-24 | GO-2026-11-22-13 | 6 USD (Fable ; pire ca | 0 | 0 | Demande 6 à Fable 5.2 par l'API (flagornerie comme levier de corruption ; question neutre  … |
| 2026-11-24 | GO-2026-11-22-14 | 45 USD | 0 | 0 | Protocole X sur la problématique du papier (GO-2026-11-22-11) : collisionneur v8d, dossier … |
| 2026-11-24 | GO-2026-11-22-15 | 6 USD | 0 | 0 | Conception de l'essaim qui communique dans l'organisme (GO-2026-11-22-12, point 4) : un ap … |
| 2026-11-24 | GO-2026-11-22-19 | 6 USD | 0 | 0 | Demande 9 à Fable 5.2 par l'API (thèse du papier A après la lecture sur PDF de la stéganog … |
| 2026-11-24 | GO-2026-11-22-21 | 6 USD | 0 | 0 | Demande 10 à Fable 5.2 par l'API (critère de la rétro-analyse des journaux du collisionneu … |
| 2026-11-24 | GO-2026-11-22-23 | 6 USD | 0 | 0 | Demande 13 à Fable 5.2 par l'API (budget égal et consignes du mode essaim du collisionneur … |
| 2026-11-24 | GO-2026-11-22-27 | 6 USD | 0 | 0 | Mot de Lazar vers 06:30Z : la demande reformulée en quatre points appliquée à « comment ré … |
| 2026-11-24 | GO-2026-11-22-30 | 12 USD (Fable) + 6 USD | 0 | 0 | Demande 15 (« quels éléments de l'organisme peut-on payer avec l'abonnement Claude ? », mo … |
| 2026-11-24 | GO-2026-11-22-31 | 6 USD par demande de 1 | 0 | 0 | Sept demandes de Lazar de la passation de 06:30 (§ 3, points 1 à 7), chacune par la demand … |
| 2026-11-24 | GO-2026-11-22-34 | 12 USD par demande à F | 0 | 0 | Mots de Lazar vers 2026-11-22T08:14:42Z : « go 19 recos » ; sur le passage d'un compte à l … |
| 2026-11-24 | GO-2026-11-22-36 | 6 USD (Fable) | 0 | 0 | Mot de Lazar relayé par la mère sortante (registres/essaim/vers-nouvelle-mere/2026-11-22-0 … |
| 2026-11-24 | GO-2026-11-22-38 | 6 USD | 0 | 0 | Relecture par Fable 5.2 par l'API (relecture_fable_api_v3, effort high, clé RR_ANTHROPIC_A … |
| 2026-11-24 | GO-2026-11-22-39 | 1 USD | 0 | 0 | Organisme, pilote P-std de l'essaim (accordé par GO-2026-11-22-28) : essai de fumée de l'a … |
| 2026-11-24 | GO-2026-11-22-41 | 10 USD | 0 | 0 | Papier « dopamine », étape 1 exploratoire (mot de Lazar « go », GO-2026-11-22-40), sous le … |
| 2026-11-24 | GO-2026-11-22-44 | sous GO-2026-11-21-70  | 0 | 0 | Mot de Lazar reçu vers 2026-11-22T11:27:47Z : « go depeche toi » sur la relance courte de  … |
| 2026-11-24 | GO-2026-11-22-59 | dans les 10 USD de GO- | 0 | 0 | Papier « dopamine », étape 1 : seconde instance Vast accordée par la mère dans le reste de … |
| 2026-11-25 | GO-2026-11-18-13 | crédits existants des  | 0 | 0 | Dépenses par interfaces de modèles de l'organisme d'idéation : budget séparé de celui du l … |
| 2026-11-25 | GO-2026-11-18-14 | 150 USD | 0 | 0 | Course d'affinage des idées des mentors par l'organisme d'idéation (N-072 ; devis version  … |
| 2026-11-25 | GO-2026-11-18-35 | 75 USD | 2 | 1 | Tranche de l'ajustement de nos lentilles (lecture par lentille neuronale) : course H100 en … |
| 2026-11-26 | GO-2026-11-22-17 | 6 USD (Fable) ; collis | 0 | 0 | Mots de Lazar vers 2026-11-22T05:37:53Z : « lance le protocole x sur la problematique gene … |
| 2026-11-26 | GO-2026-11-22-18 | 6 USD (Fable) ; collis | 0 | 0 | Mot de Lazar vers 05:38Z : « mieux que la boite noir sur le sabotage diffus ? … et la pinc … |
| 2026-11-26 | GO-2026-11-22-22 | 12 USD (Fable) ; colli | 0 | 0 | Mots de Lazar vers 06:00Z : « Chance qu'elle soit positive contre un attaquant entraîné :  … |
| 2026-11-26 | GO-2026-11-22-33 | 20 USD (Fable) ; 50 US | 0 | 0 | Mots de Lazar vers 2026-11-22T07:59:23Z : « go A pour les deux, lance le collisionneur » ; … |
| 2026-11-26 | GO-2026-11-22-37 | 50 USD par dossier (10 | 0 | 0 | Protocole X des demandes 23 (lot en quarantaine) et 24 (nouveaux modes d'attaque), suite d … |
| 2026-11-26 | GO-2026-11-22-40 | Fable : 30 USD (demand | 0 | 0 | Mots de Lazar vers 2026-11-22T10:28:41Z : demande 22 découpée en quatre, « trois par papie … |
| 2026-11-26 | GO-2026-11-22-43 | 100 USD par dossier ;  | 0 | 0 | Dépenses accordées par le même lot de mots de Lazar : collisionneur, dossiers des question … |
| 2026-11-26 | GO-2026-11-22-45 | plafonds des lignes ci | 0 | 0 | Mot de Lazar reçu vers 2026-11-22T11:31:07Z : « pour la clé minuit dont les crédits sont é … |
| 2026-11-26 | GO-2026-11-22-46 | au plus 200 USD (devis | 0 | 0 | Mot de Lazar reçu vers 2026-11-22T11:34:26Z sur la liste fermée de la passe X de la course … |
| 2026-11-26 | GO-2026-11-22-47 | 100 USD | 0 | 0 | Protocole X de la demande 28 (idées originales, puits étroits), suite du mot de Lazar « go … |
| 2026-11-27 | GO-2026-11-10-07 | 30 USD (les deux pièce | 0 | 0 | Contrôle de l'artefact d'adaptateur, option (b) de D-1 (rapport des prémisses premisses-tr … |
| 2026-11-27 | GO-2026-11-10-08 | 60 USD (option B de M7 | 4 | 0 | Saboteur à budget (ii-b, P-066) avant le 27, avec l'activité interne enregistrée (D-4, opt … |
| 2026-11-27 | GO-2026-11-10-09 | 500 USD (enveloppe tot | 0 | 0 | Autonomie de calcul et de travail de la session mère jusqu'au 27 novembre 2026, dans une e … |
| 2026-11-27 | GO-2026-11-18-62 | 27 USD | 0 | 0 | Organismes discrets, bras A, première ligne de course : fabrication et rejeu honnête (256  … |
| 2026-11-27 | GO-2026-11-19-66 | 25 USD | 0 | 0 | Organisme d'idéation, ligne 3 (votes effectifs des juges croisés, mesurés sur témoins plan … |
| 2026-11-27 | GO-2026-11-20-68 | 88,36 USD | 0 | 0 | Ligne 3, étage 2 à 200 témoins : départ accordé quand l'additif de code est scellé et que  … |
| 2026-11-27 | GO-2026-11-21-30 | 456 USD | 0 | 0 | Course « nouvelles attaques » à cinq espèces : même accord que GO-2026-11-20-67, échéance  … |
| 2026-11-27 | GO-2026-11-21-37 | 4,30 USD | 0 | 0 | Appel à l'auteur des mondes plantés de la course « seuil et moniteurs » : un appel, deux e … |
| 2026-11-27 | GO-2026-11-22-01 | 16 USD (dépense tenue  | 0 | 0 | Mot de Lazar vers 2026-11-22T04:47:43Z (session mère session_01Qi7Gr3eYmAhDEJzqLgWcv1) : « … |
| 2026-11-27 | GO-2026-11-22-71 | (A) 44 USD ; (B) 55 US | 0 | 0 | Saboteur à budget : « go C !!! » (mot de Lazar reçu vers 14:10Z) : les deux voies en paral … |
| 2026-11-28 | GO-2026-11-21-08 | 48,13 USD | 0 | 0 | Collisionneur, questions « modes de sabotage » et « attaques » : devis v3 (fadb7d09…) sans … |
| 2026-11-30 | GO-2026-10-20-06 | 150 USD, plafond de GO | 0 | 0 | prolongation de GO-2026-10-04-08 (calcul de la phase 0) jusqu'au 2026-11-30, plafond incha … |
| 2026-11-30 | GO-2026-10-20-07 | 10 USD par lancement,  | 0 | 0 | extension de la délégation R-217 jusqu'au 2026-11-30 : lancements payants préenregistrés,  … |
| 2026-11-30 | GO-2026-10-24-05 | aucun plafond fixé par | 6 | 0 | étape 1 du programme « gradient conçu par l'essaim » (sondes ; N-042, R-344) : extraction  … |
| 2026-11-30 | GO-2026-10-24-05 | dans la ligne de R-355 | 6 | 0 | extension : tests de dépense par espèce (un appel payant, consigne figée, statut OK et jet … |
| 2026-11-30 | GO-2026-10-29-03 | 124 USD | 0 | 0 | sentinelle entre lancements de la couche 2 : ≈ 1 100 paires d'épisodes par lancement pour  … |
| 2026-11-30 | GO-2026-10-29-05 | 13 USD | 0 | 0 | tranche 0 de mesure du pilote de la couche 2 (devis v1 § 8 point 1 et v2, docs/notes/couch … |
| 2026-11-30 | GO-2026-11-07-07 | 300 USD | 7 | 0 | Épreuve de l'étiqueteur, phase 1 (appels des lecteurs gemini-4-argon et kimi-k3.1-pro sur  … |
| 2026-11-30 | GO-2026-11-08-02 | 45 USD | 0 | 0 | Organisme : plus petite course réelle de la boucle complète (R-1738) : D1 bras réel seul,  … |
| 2026-11-30 | GO-2026-11-08-06 | 25 USD | 3 | 0 | Collisionneur v2.6, remue-méninges du pilier attaque sur la question scellée (29870ac9a809 … |
| 2026-11-30 | GO-2026-11-08-07 | 15 USD | 2 | 0 | Question v2 du pilier attaque (trace interne du sabotage, défense randomisée ou perfection … |
| 2026-11-30 | GO-2026-11-08-08 | 20 USD | 3 | 0 | Organisme d'idéation : course sur la question scellée v1 du pilier attaque (29870ac9a8091c … |
| 2026-11-30 | GO-2026-11-10-10 | 120 USD (organisme 45, | 0 | 0 | Enveloppe de 120 USD au plus jusqu'au 30 novembre 2026 pour deux courses payantes, plafond … |
| 2026-11-30 | GO-2026-11-10-11 | 45 USD | 5 | 0 | Course réelle de l'organisme d'idéation (boucle réelle, code v66) : 40 USD de modèles (Kim … |
| 2026-11-30 | GO-2026-11-10-12 | 120 USD | 0 | 0 | T0.8, bases boîte noire v0, course sur les épisodes de 7b (DB8-5, option (a)) : épisodes h … |
| 2026-11-30 | GO-2026-11-10-13 | 65 USD | 6 | 0 | Essai Lean (couche 4, pas (b)), D-1a : outillage seul, sur une machine dédiée isolée (D-2  … |
| 2026-11-30 | GO-2026-11-12-01 | 235 USD (sur crédits) | 0 | 0 | Crédits de Claude, P1 : juge-tournoi, manche T0, Opus 5.5 principal et Fable 5.1 second, s … |
| 2026-11-30 | GO-2026-11-12-02 | 45 USD (sur crédits) | 0 | 0 | Crédits de Claude, P2 : oracle de couverture N-060 v3, lecteur Opus 5.5, épreuves puis pil … |
| 2026-11-30 | GO-2026-11-12-03 | 70 USD (sur crédits) | 0 | 0 | Crédits de Claude, P3 : contre-lectures par l'interface, Fable 5.1 et Opus 5.5, liste blan … |
| 2026-11-30 | GO-2026-11-12-04 | 40 USD (sur crédits) | 3 | 0 | Crédits de Claude, P4 : collisionneur, quatre tours au plus, 15 USD par tour, devis consig … |
| 2026-11-30 | GO-2026-11-12-05 | 45 USD (sur crédits) | 0 | 0 | Crédits de Claude, P5 : génération de 50 mondes plantés neufs par Opus 5.5, gardés privés  … |
| 2026-11-30 | GO-2026-11-12-06 | 45 USD | 3 | 0 | Course réelle de l'organisme d'idéation sous l'écart 1, option 2 : 40 USD de modèles (Kimi … |
| 2026-11-30 | GO-2026-11-13-01 | 365 USD (sur crédits) | 0 | 0 | Course de l'organisme à plusieurs générations, part sur crédits de Claude (GO-β1) : propos … |
| 2026-11-30 | GO-2026-11-13-02 | 57 USD | 0 | 0 | Même course, part hors crédits (GO-β2) : Argon proposeur (2 USD par session) et vérificate … |
| 2026-11-30 | GO-2026-11-13-03 | 60 USD | 1 | 1 | Organisme d'idéation, atelier d'idées (N-065, rôle 2), sur la question des bassins d'idées … |
| 2026-11-30 | GO-2026-11-13-04 | 4.39 USD | 1 | 0 | Pilote MR-2 : sonde des deux relais sur crédits de Claude, avant le scellement du texte :  … |
| 2026-11-30 | GO-2026-11-13-05 | 3.68 USD | 1 | 0 | Pilote MR-2 : sonde des deux relais hors crédits, mêmes conditions que la ligne GO-2026-11 … |
| 2026-11-30 | GO-2026-11-13-06 | 21 USD | 6 | 1 | Course de l'organisme d'idéation sur sa propre conception (atelier d'idées, N-065 rôle 2 ; … |
| 2026-11-30 | GO-2026-11-14-01 | 25 USD | 1 | 1 | Course de l'organisme d'idéation sur la question « Regard ou raisons » (atelier d'idées, N … |
| 2026-11-30 | GO-2026-11-14-02 | 2 USD | 1 | 0 | Pilote MR-2 : sonde neuve du seul relais Astra (gpt-6-astra), par le compte organisme (ses … |
| 2026-11-30 | GO-2026-11-14-05 | 10 USD | 2 | 1 | Neuron Lens, volet A (Qwen3-8B ; audit de fuite textuelle d'une sonde par la lentille S, n … |
| 2026-11-30 | GO-2026-11-14-06 | 12 USD | 6 | 5 | Neuron Lens, tranche B-α (Llama 3.1 8B Instruct, lentilles publiques de Neuronpedia : lect … |
| 2026-11-30 | GO-2026-11-14-07 | 4.39 USD | 1 | 0 | Pilote MR-2 : sonde des deux relais sur crédits de Claude (configuration v12, lanceur v73) … |
| 2026-11-30 | GO-2026-11-14-08 | 3.68 USD | 1 | 0 | Pilote MR-2 : sonde des deux relais hors crédits (configuration v12, lanceur v73), mêmes c … |
| 2026-11-30 | GO-2026-11-14-10 | 4.39 USD | 1 | 0 | Pilote MR-2 : sonde des deux relais sur crédits de Claude (configuration v12, lanceur v74) … |
| 2026-11-30 | GO-2026-11-14-11 | 3.68 USD | 1 | 0 | Pilote MR-2 : sonde des deux relais hors crédits (configuration v12, lanceur v74), mêmes c … |
| 2026-11-30 | GO-2026-11-14-13 | 20 USD (sur crédits) | 1 | 0 | Pilote d'une génération de l'organisme sur la famille MR-2, part sur crédits de Claude : p … |
| 2026-11-30 | GO-2026-11-14-14 | 21.72 USD | 3 | 0 | Même pilote, part hors crédits : argon proposeur (2,34 USD par session) 9,36 USD, astra pr … |
| 2026-11-30 | GO-2026-11-15-02 | 0.10 USD | 1 | 0 | Pilote MR-2 : épreuve des trois clés du pilote (Claude, Gemini, OpenAI) avant le lancement … |
| 2026-11-30 | GO-2026-11-15-05 | 0.10 USD | 1 | 0 | Extension de GO-2026-11-15-02 : même épreuve des trois clés du pilote MR-2 (un appel minim … |
| 2026-11-30 | GO-2026-11-17-07 | 90 USD | 0 | 0 | Témoin de Bailey, run de confirmation au régime complet (72 tours), addendum 7 scellé prer … |
| 2026-11-30 | GO-2026-11-19-86 | 200 USD | 17 | 0 | Barreau 5, formation des familles d'adaptateurs jumeaux (39 adaptateurs, sept instances ;  … |
| 2026-11-30 | GO-2026-11-19-87 | 56 USD | 0 | 0 | Barreau 5 : enveloppe de relance, à part du plafond de GO-2026-11-19-86 (fiche v4, recomma … |
| 2026-11-30 | GO-2026-11-19-90 | 8,5 USD | 0 | 0 | Barreau 5, première lecture (texte neuf « validité de l'adaptateur pour les sondes apprise … |
| 2026-11-30 | GO-2026-11-20-08 | 450 USD | 0 | 0 | Organisme, course d'idéation « nouvelles attaques, trois générations » : accord de calcul  … |
| 2026-11-30 | GO-2026-11-20-26 | 88,36 USD | 0 | 0 | Organisme, ligne 3, étage 2 à 200 témoins : accord de calcul au plus 88,36 USD (pire du de … |
| 2026-11-30 | GO-2026-11-21-70 | 60 USD | 3 | 0 | Saboteur à budget, ligne de calcul neuve (étalonnage puis course), sous GO-2026-11-21-66 e … |
| 2026-11-30 | GO-2026-11-21-73 | 15 USD | 0 | 0 | Organisme, palier 0b, serveur loué pour finir l'étape 4, sous le « go dépenses » de GO-202 … |
| 2026-11-30 | GO-2026-11-21-81 | 0,25 USD | 1 | 0 | bras A, vérification de la clé de mistral-large-4-0 sur api.eu.mistral.ai, trois appels au … |
| 2026-11-30 | GO-2026-11-21-82 | 0,25 USD | 0 | 0 | bras A, vérification de la clé de mistral-large-4-0 sur api.mistral.ai, trois appels au pl … |
| 2026-11-30 | GO-2026-11-21-83 | 4,75 USD | 1 | 0 | bras A, essai d'admission du second lecteur, 24 appels, devis 421ee2e6ec909c8b6261b3be3910 … |
| 2026-11-30 | GO-2026-11-21-86 | 0,25 USD | 1 | 0 | bras A, vérification de la clé de mistral-large-4-0 sur api.eu.mistral.ai, trois appels au … |
| 2026-11-30 | GO-2026-11-22-04 | devis de la machine de | 0 | 0 | Mot de Lazar vers 2026-11-22T04:52:51Z : « Organisme d'idéation : … go ; Le jeton GitHub p … |
| 2026-11-30 | GO-2026-11-22-05 | 62 USD (≈ 31,6 attendu | 0 | 0 | Mot de Lazar vers 2026-11-22T04:52:51Z : « go reajustement ». Réajustement des lentilles,  … |
| 2026-11-30 | GO-2026-11-22-48 | inchangé (200 USD au p | 0 | 0 | Erratum de la mère à GO-2026-11-22-46 : l'échéance du 26 novembre était de sa main, non de … |
| 2026-11-30 | GO-2026-11-22-49 | 260 USD (part de Luc,  | 0 | 0 | Mot de Lazar reçu vers 2026-11-22T12:00:09Z : « go » sur « passer aussi sur la clé Luc les … |
| 2026-11-30 | GO-2026-11-22-51 | 76,20 + 40 + 0,05 USD | 0 | 0 | « Raisons ou regard ? », 2 ter, sur le mot de Lazar « go et inclus astra » (vers 12:00Z) e … |
| 2026-11-30 | GO-2026-11-22-53 | 120 USD | 0 | 0 | Dossier neuf du collisionneur sur les cinq décisions du banc à vérité plantée (GO-2026-11- … |
| 2026-11-30 | GO-2026-11-22-54 | 456 USD (inchangé) + 0 | 0 | 0 | Course « nouvelles attaques » : la ligne GO-2026-11-20-67 (456 USD) échoit le 22 ; prolong … |
| 2026-11-30 | GO-2026-11-22-55 | 163 + 130 + 233 USD | 0 | 0 | Mots de Lazar reçus vers 2026-11-22T12:18:48Z : « go lots Opus 163, Carbon 130, Neon 233,  … |
| 2026-11-30 | GO-2026-11-22-56 | 12 USD | 0 | 0 | Attaquant informé : version définitive de la course (brouillon 15, champs de l'étalonnage  … |
| 2026-11-30 | GO-2026-11-22-58 | 25 USD (Fable) + 5 USD | 0 | 0 | Demandes à Fable par l'API, clé Luc, sur les mots de Lazar du même lot : 36 (éviter les ré … |
| 2026-11-30 | GO-2026-11-22-60 | 3,00 USD | 0 | 0 | vérification de la clé de gemini-4-neon lue sous GEMINI_API_KEY, trois appels au plus, dev … |
| 2026-11-30 | GO-2026-11-22-61 | 3,00 USD | 0 | 0 | vérification de la clé de gemini-4-neon lue sous GEMINI_API_KEY_2, trois appels au plus, d … |
| 2026-11-30 | GO-2026-11-22-62 | 16,50 USD | 0 | 0 | essai d'admission du juge des deux ancres, 8 appels, rangs impairs sous GEMINI_API_KEY, ra … |
| 2026-11-30 | GO-2026-11-22-63 | 70 USD ou 65 USD par d | 0 | 0 | Collisionneur v8l (vérifiée conforme vers 13:00Z), effort et sortie maximaux sur le mot de … |
| 2026-11-30 | GO-2026-11-22-65 | 6 USD | 0 | 0 | Bras A des organismes discrets : brouillon final du texte par Fable 5.2 par l'API (outil v … |
| 2026-11-30 | GO-2026-11-22-67 | Fable 10 USD ; Google  | 0 | 0 | Mot de Lazar reçu vers 2026-11-22T13:23:32Z : « il n'y a pas de méthodes mathématiques qui … |
| 2026-11-30 | GO-2026-11-22-68 | 4 USD | 0 | 0 | Collisionneurs : demande à Fable 5.2 sur le pilote de l'essaim (appariement rompu, balises … |
| 2026-11-30 | GO-2026-11-22-69 | 3 USD | 0 | 0 | Papier « dopamine », étape 1 : demande à Fable 5.2 sur le critère de la garde de vérité pl … |
| 2026-11-30 | GO-2026-11-22-72 | 40,68 USD (Opus 4.6) | 0 | 0 | Raisons ou regard ?, étape 2 ter : « garder l'API pour ces seuls 9 USD environ d'Opus 4.6, … |
| 2026-11-30 | GO-2026-11-22-74 | Neon 3 USD ; Carbon 5  | 0 | 0 | Mots de Lazar reçus vers 14:30Z : puits étroits, « Cinq décisions … go » (D1-D5) ; relectu … |
| 2026-11-30 | GO-2026-11-22-75 | 60 USD | 0 | 0 | Saboteur à budget, voie (A) : code du tirage corrigé (0020), essai de vitesse court, étalo … |
| 2026-11-30 | GO-2026-11-22-76 | 162,71 USD (Opus 4.6)  | 0 | 0 | Raisons ou regard ?, étape 2 ter : option (a) « maintenir 20 tirages » go (mot de Lazar ve … |

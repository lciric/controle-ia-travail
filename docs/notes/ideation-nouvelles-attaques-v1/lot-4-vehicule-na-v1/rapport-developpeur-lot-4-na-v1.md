# Rapport du développeur — véhicule NA-1, lot 4 (surcharge d'`appel`, adaptateur Claude neuf) — v1

- Développeur du lot 4 du véhicule NA-1, modèle O. Je n'ai écrit ni la conception, ni les lots 1 à 3, ni aucun orchestrateur.
- Date (UTC) : 2026-11-21.
- Mandat : `mandat-developpeur-vehicule-na-lot-4-v1.md` (`df5a1cea…`) et ses errata 1 (`47721c81…`), 2 (`1d6de645…`) et 3 (`72fa461a…`). Chacun égale son compagnon ; tous sont lus en entier.
- Processeur seul. Aucun appel à un fournisseur, aucune clé, aucune dépense, aucun relais lancé, aucune écriture dans un dépôt, aucun commit. La liste réelle des motifs n'est ni copiée ni lue par mon code.
- **Un refus de classifieur rencontré**, au début : une commande de liste sur le dossier de la conception. C'était ma faute (hors des dossiers permis). Je me suis arrêté et l'ai dit. La mère a accordé la reprise (11:05Z, R-4494) ; aucun autre refus n'a suivi.
- **Base changée en cours de travail**, sur décision de la mère. Le lot 2 passe en v5 (`garde_motifs_na_v4`, table `6a5b5400…`) et le lot 3 en v3 (`requete_na_v3`, `journal_na_v3`, table `1be0ffd4…`). J'ai fait une copie neuve de l'orchestrateur (`a41b7b50…`) et y ai posé le lot 2 v5 puis le lot 3 v3 par leurs programmes : 200 passés. Le code du lot 4 est écrit contre eux ; la première base (lot 2 v3, lot 3 v2) n'est plus lue.
- Ce rapport ne porte aucun chemin complet du bloc-notes. Le rapport du lot 2 v5 (§ 5) signale qu'un segment de ce chemin égale un nom de la liste réelle.

## 1. Verdict

- **Essais du lot 4 : 87 passés, 0 échec** : 66 pour la surcharge et la table, 21 pour l'adaptateur, le faux fournisseur et le relevé.
- **Avec les lots 2 v5 et 3 v3, sur une copie neuve, paquets posés par leurs programmes : 287 passés** (200 + 87).
- **Mutations : 51 sur 51 tuées**, à la manière de la v68. Le témoin non muté passe ; le témoin inerte survit.
- **Relevé au faux fournisseur, sur `127.0.0.1`, sans relais : fait.** Constat principal (§ 6) : même sans texte système (chaîne vide ou rien), l'outil envoie deux blocs de texte système. Il ajoute aussi, après la consigne, un message de rôle « system » (dossier de travail, modèle, budget, date). **D2 n'est donc pas tenu par l'adaptateur seul** : c'est à la mère de dire si ce texte se déclare comme transport ou se refuse (07:46Z, mot 5).

## 2. Pièces lues (empreinte recalculée, égale au compagnon)

| pièce | empreinte |
|---|---|
| conception v5 | `1b7f6822af20417e997b80290f05e7a4d70aa69c3d65f4139b5b3673cd98a863` |
| contrôle de la conception v5 | `4b369004733fb4c55bb75deaeac19c4cc4e5dacaa8604f8082f63096c2956156` |
| relevé du lot 0 | `10ac79ecb0e064f5b5ea80ddb060ae37e303d2d84ff242f653f4cccbd7ff753e` |
| v9 scellée (tirée de `origin/main` par `git show` redirigé) | `864f39a7ecd41a613f8892efbf66607c14da34252d643a4fd40032b5d2b500c2` |
| table du lot 2 v5 ; rapport | `6a5b5400…` ; `5454576f…` |
| table du lot 3 v3 ; rapport | `1be0ffd4…` ; `a778f8fa…` |
| classe de génération v68 (`course2_v68.py`, ouverte par son chemin complet) | `c1aeab4c…` |
| kit d'agent installé, transport (`subprocess_cli.py`, l. 570 à 590, 814 à 879) | version 0.2.172 |

Les tables et vérifications des lots 2 v3 et 3 v2 ont été lues pour la première base, puis abandonnées.

## 3. Exigences et code

Modules neufs (suffixe `_na_v1`), dans `paquet/orchestrator/pole/` : `routage_na_v1.py` (RT), `appel_garde_na_v1.py` (AG), `adaptateur_claude_na_v1.py` (AC), `faux_fournisseur_na_v1.py` (FF), `releve_sans_systeme_na_v1.py` (RL).

| exigence (lettre) | code |
|---|---|
| pas 0, rôle arrêté par une garde héritée → « refus écrit », sans coût, rendu par sorte (conception § 2.3, § 2.13) | AG:264 `role_arrete_na`, AG:301 `_refus_ecrit_na`, AG:329 |
| pas 1, routage par rôle, couple (rôle, adaptateur) exact ; `hors_course`, clé sans part, adaptateur hors table → n° 12, seconde clause (V9 l. 383, 402 ; § 2.9) | RT:171 `router` ; AG:333 |
| table scellée lue à son empreinte (n° 14), marque « course », « ligne à part » ou « artefact » ; tables des lignes à part (§ 2.10) | RT:208 `lire_table` |
| pas 2, part : cumul + pire en vol + pire de l'appel > part → n° 12, première clause ; égal permis ; ligne à part : plafond de sa ligne (V9 l. 383 ; CV l. 166) | RT:399 `verifier_part`, RT:360 `CumulParCle` ; AG:350 |
| pas 3 et 4, garde de motifs v4 puis ligne « envoi » ; motif → ligne « non envoyé » puis n° 16 neuf, sans le texte trouvé (V9 l. 387 ; erratum 1, point 2) | AG:358 à 370 |
| journal en panne (`JournalRefuse` ou `OSError`) → rien ne part, sans coût, arrêt « requête journalisée » (erratum 3) | AG:364 ; aussi AG:289, 314, 396 |
| pas 5, égalité : `verifier_avant_envoi(requete_gardee, octets)` sur l'encodage de la chaîne même remise à `super().appel` ; écart après la ligne « envoi » → ligne « non envoyé » qui renvoie au rang, sans coût (errata 1 et 2) | AG:372 à 381 ; comptes : AG:447 `comptes_envois_na` |
| pas 6, `super().appel` inchangé ; le coût que compte le noyau (plafond compris sur exception) va au cumul de la clé | AG:382 à 390 |
| pas 7, « non lancé » ; statut, refus et erreur lus ; n° 1 ; A2 ; état du relais et n° 13 ; « cause non établie » (V9 l. 372, 384 ; § 2.3 ; 07:46Z, mots 4 et 6) | AG:391, AG:404 `_apres_retour_na`, AG:160 `relais_montre_refus_credit`, AG:173 `lecteur_etat_relais_http` |
| refus avant le noyau : aucune consommation, aucun coût, hors du suivi, une ligne, un compte (07:21Z, règle 5) | AG:283 `_non_envoye_na` ; `na_comptes` |
| adaptateur Claude neuf sans texte système, reste du transport gardé (D2 ; L0 Q1) | AC:49 `construire_options_na`, AC:63 |
| réponses brutes conservées, refus et erreur compris ; conservation impossible : rien n'est rendu (V9 l. 396 ; L0 Q10) | AC:80 `_conserver`, AC:103 `lancer` |
| faux fournisseur sur la boucle locale ; modes normale, classifieur, coupée, crédit, accès (§ 2.12) | FF:46 |
| relevé de ce que l'outil envoie sans texte système (§ 2.3, § 7 ; mandat, point 3) | RL:176 `jouer_scenarios`, RL:122 `analyser_corps`, RL:272 `principal` |

**Arrêts nommés neufs, à numéroter à l'additif** :
- « requête journalisée » (V9 l. 77). Ses causes : journal en panne, écart d'égalité, consigne qui n'est pas une requête assemblée, case ou génération incohérente.
- A2 (07:46Z, mot 6).

Erratum 2, point 3 : **aucune ligne d'arrêt ni « ligne de la génération » n'est écrite dans le journal**, fermé à quatre événements. Les arrêts consignés (n° 1, portée « appel ») et les comptes restent en mémoire (`na_arrets_consignes`, `na_comptes`, `na_journal_arrets_cles`). Le lot 6 (ou une v2 du journal) les écrit.

## 4. Essais (`essais/test_na_v1_appel_garde.py`, `essais/test_na_v1_adaptateur_claude.py`)

Les essais tournent contre **le vrai `appel` du noyau** (`OrchestreV56.appel`, porté par `NoyauEssai`), et, pour la composition, contre la vraie `GenerationV56` (coffre et suivi réels). Chaque garde a son cas sain et son artefact.

- **n° 12 (D11)** :
  - cas sain : un appel par clé, compté sur elle ; cas neuf : le juge et le proposeur de l'espèce 3 sur la même clé, cumulés ;
  - la part juste égale passe, un centime de trop est refusé, sans montant dans le message ;
  - refusés : l'aiguilleur sur la clé de l'espèce 3 ; le juge de l'espèce 3 sur la clé du proposeur, sur la table plantée « artefact » ; le proposeur de l'espèce 2 sur le deuxième relais ; un envoi à la clé sans part ; le juge de l'espèce 3 sur la clé de l'aiguilleur ; un autre adaptateur de la même clé ; un rôle ou un adaptateur absents de la table ;
  - les lignes à part, par leur table : permises ; plafond de la ligne tenu ;
  - l'appel en vol entre dans la part ; le cumul est partagé entre générations.
- **n° 16 au point d'envoi** :
  - un motif en clair, puis sous six formes normalisées, dans une requête de proposeur et dans une fiche servie au juge ;
  - le texte trouvé est à la seule ligne « non envoyé » : ni message, ni `args`, ni `repr`, ni attributs, ni contexte.
- **n° 1** : cas sain lu ; un refus consigné, non relancé ; la portée « course » arrête.
- **n° 13** :
  - cas sain sans lecture du relais ; refus pour crédit au relais : arrêt qui dit la clé ;
  - erreur sans refus au relais : « cause non établie », comptée ; relais illisible : compté ;
  - message synthétique de l'outil : lu comme une erreur, non comme A2 ;
  - relais de protocole en « budget dépassé » : n° 13.
- **Envoi refusé sans coût** (n° 12, n° 16, première clause) : coût de l'étape, coffre, cumul, suivi et A14 inchangés ; journal « non envoyé » avec l'arrêt et la clé ; refus compté.
- **`hors_course`** : le lecteur d'étiquettes planté est refusé (n° 12), sans erreur de dictionnaire, même sans adaptateur de ce nom au noyau.
- **Journal égal à l'octet à l'envoi**, pour cinq sortes de requête. **Égalité refusée après la ligne « envoi »** : la ligne qui renvoie au rang est écrite, et la requête n'est pas comptée partie.
- **Journal en panne** : fichier supprimé, remplacé par un dossier, écriture en panne, réécrit d'une autre main.
- **Autres** : refus écrits par sorte ; « non lancé » ; A2 (absent, changé, refus de transport) ; contexte exigé ; garde v3 refusée.
- **Adaptateur** :
  - texte système à `""` ou `None` ; reste du transport égal à l'adaptateur d'origine ; l'adaptateur d'origine pose bien son texte (artefact au niveau des options) ;
  - réponses ok, refus, erreur et exception conservées, avec compagnon ; noms jamais écrasés ; conservation impossible : rien n'est rendu ;
  - non armé, nom de clé dans l'environnement, modèle non permis : refusés avant toute session.

**Mutations** (`essais/mutations_na_lot4_v1.py`, journal `journal-mutations-na-lot-4-v1.json`) : 51 sur 51 tuées. Parmi elles :
- « routeur par espèce » (D11) ;
- « refus de la part déplacé après l'appel du noyau », l'équivalent de « refus dans `lancer` » ;
- `OSError` non attrapée (erratum 3) ;
- appel de `verifier_avant_envoi` retiré (erratum 1) ;
- égalité refusée sans ligne qui renvoie au rang (erratum 2) ;
- texte système d'origine laissé ;
- conservation retirée.

## 5. Relevé au faux fournisseur

- **Programme** : `releve_sans_systeme_na_v1.py`, joué sous l'interpréteur qui porte le kit, `-I`.
  - `direct` : le faux fournisseur dans le processus, l'adaptateur pointé sur lui, sans relais ; c'est mon jeu.
  - `servir-faux` puis `relever --url-relais` : prêt pour le jeu derrière le vrai relais. Ce jeu est à la mère, je ne l'ai pas fait. J'ai éprouvé cette voie en pointant `relever` sur le faux fournisseur lui-même, et elle rend le même bilan.
  - Environnement isolé : aucune variable de clé, aucun mandataire réseau, maison et configuration de l'outil dans le dossier du relevé.
  - L'identifiant du modèle et le chemin du dossier sont masqués dans le relevé, avec l'empreinte du texte d'avant le masque.
- **Sortie** : `releve-faux-fournisseur-na-lot-4-v1/releve-sans-systeme-na-v1.json`, `6dc903bc4e8d30d8a0c49130cf5b46be0a6a2f2f953ba2ad1fcbaaf0cdaaf8ef`, et son compagnon. Kit 0.2.172, outil embarqué 2.1.308.

## 6. Ce que montre le relevé (constats ; rien n'est tranché ici)

1. **Les deux formes n'en font qu'une.** Le kit traduit `system_prompt=None` comme `""` en `--system-prompt ""` (`subprocess_cli.py`, l. 576 à 579). Les deux formes envoient les mêmes blocs.
2. **Ce qui part sans texte système**, par appel et pour les deux rôles :
   - au champ `system`, deux blocs :
     - `x-anthropic-billing-header: cc_version=2.1.308.b26; cc_entrypoint=sdk-py;` (73 octets) ;
     - « You are a Claude agent, built on Anthropic's Claude Agent SDK. » (62 octets, `cache_control`) ;
   - dans `messages`, la consigne, **retrouvée à l'octet** dans le message « user » ;
   - puis **un second message, de rôle « system »**, bloc « # Environment » de 1 052 à 1 080 octets (`cache_control`). Il porte le dossier de travail de la session, la plateforme, la version du système, une ligne de consigne sur les fichiers téléchargés, le nom et l'identifiant du modèle, la date de connaissance, le budget de la session (« USD budget: $0/$0.5 ») et la date du jour.
   - **Ce bloc change d'un appel à l'autre** (dossier, budget, date) : il ne peut pas se déclarer « octet pour octet » comme un texte fixe, au mieux comme un gabarit.
   - **Il porterait des motifs de la garde**, chemin, nom de modèle, plafond et coût, ajoutés après le point d'envoi, donc hors de sa vue.
   - La ligne sur les fichiers téléchargés ne vient ni du kit ni de la configuration isolée ; elle semble venir de réglages de la machine. Elle peut différer ailleurs.
3. **Autres réglages qui partent**, non textuels :
   - `max_tokens` 128 000 ; `thinking` adaptatif ; `output_config.effort` « high » pour le proposeur, « medium » pour le juge et le portier ; `context_management` ; `metadata.user_id` ; `tools` vide ; `stream` ;
   - huit valeurs d'`anthropic-beta`.
4. **Artefact** : l'adaptateur d'origine envoie bien son texte système (577 octets), à la place de la phrase d'identité. Les deux autres blocs, eux, partent aussi.
5. **Issues du faux fournisseur**, à travers l'outil et le kit :
   - classifieur : « refus », `system.model_refusal_no_fallback` ;
   - réponse coupée, crédit et accès : **tous trois « refus », `assistant.model`, modèle servi `<synthetic>`**. C'est le message que l'outil fabrique lui-même pour une erreur.
   - L'outil a relancé 10 fois une erreur d'accès (11 requêtes) et fait 4 requêtes pour une réponse coupée.
   - Toutes les réponses sont conservées, avec leur compagnon.
6. **L'outil écrit une transcription par session** sous son dossier de configuration (`projects/…/*.jsonl`), consigne et réponse comprises. Le relevé du lot 0 (Q10) laissait ce point « non établi ». En course, ces fichiers seraient hors du dossier de sortie si la maison de l'agent n'y est pas.

## 7. Ce que la lettre ne fixe pas (remarques)

1. **Arrêt de l'égalité et du journal** : le mandat ne nomme pas d'arrêt. Je lève « requête journalisée » (V9 l. 77), numéro à l'additif, et la course s'arrête. Le renvoi au rang est écrit dans le champ `cause` de la ligne « non envoyé » (« … ; renvoi à la ligne « envoi » de rang N »), parce que la liste fermée du journal v3 n'a pas de champ `envoi_rang`. Une v3 groupée du journal pourrait l'ajouter.
2. **Message synthétique** : le kit le rend en refus `assistant.model`. Je le lis comme une erreur de la clé (relais, puis « cause non établie »), sans toucher à la barrière R-764 de l'adaptateur. À confirmer par la mère.
3. **n° 13 sur les clés Claude** : `/relais/etat` (relais v2) ne montre que le refus du relais à son plafond. Ma règle exige au moins un refus autre que de modèle, et plus de quoi réserver un appel. **Un refus pour crédit du compte en amont n'y paraît pas** : il est lu « cause non établie », et la course continue (07:46Z, mot 4). Pour l'arrêter, il faudrait un relais qui expose le statut d'amont, ou une lecture de son journal. Le texte du message synthétique est perdu (le kit vide le texte d'un refus).
4. **n° 13 pour le relais de protocole** : « budget dépassé » y est le 402 du relais (L0 Q5), lu comme un refus pour crédit. Pour les commandes externes, la garde de crédit reste au lanceur (lot 8).
5. **Contrôles de forme ajoutés** au pas 1 : consigne assemblée par le lot 3, case de la session, génération. Ils servent la fonction de case que le mandat demande, et la vérité de la ligne du journal.
6. **Portée de l'arrêt n° 1** : « appel » par défaut (proposition du concepteur, D8 en attente) ; « course » sur réglage.
7. **Compte du coût** : écart de `etat["cout"]`, bruit des flottants ôté au nano-dollar, puis arrondi au micro-dollar supérieur. Montants en micro-dollars entiers ; parts au centime.
8. **Pires des lignes à part** : la lettre ne les donne pas. Les essais prennent 0,20 USD.
9. **D2 et la garde de motifs** sont touchés par le § 6, points 2 et 6 : point pour la mère avant l'additif.

## 8. Interface pour le lot 6 (figée)

- Classe : `class GenerationNA(AppelGardeNA, GenerationV68)`, contexte passé par `contexte_na=` (ou posé sur `_contexte_na_demande` avant `__init__`) ; sans contexte, `ContexteRefuse`.
- `ContexteAppelGardeNA(numero_generation, table, parts, pires_par_role, journal, garde, identifiant_case_de_session, cumul, lire_etat_relais=None, portee_arret_1="appel")` :
  - `numero_generation` : 1, 2 ou 3 (table de course) ; `None` pour une ligne à part ;
  - `table` : `routage_na_v1.lire_table(octets, empreinte, "course" | "ligne à part")`, jamais « artefact » ;
  - `parts` : {clé : USD au centime}, une par clé qui porte un rôle, égales à la table scellée ; `{}` pour une ligne à part ;
  - `pires_par_role` : {étiquette : USD}, un par rôle routé ;
  - `journal` : `journal_na_v3.JournalRequetes` de la génération ; `garde` : `garde_motifs_na_v4.GardeMotifs` ;
  - `identifiant_case_de_session(session) -> str` : la case d'une session (proposeur : de la case ; portier et juges : de la méta de la fiche), égale à `requete.identifiant_case` ;
  - `cumul` : **un seul `CumulParCle(table)` pour toute la course**, passé à chaque génération ;
  - `lire_etat_relais(cle) -> dict` : par défaut, `GET /relais/etat` à l'adresse locale de la table.
- `appel(etat, *, role, role_kit, fournisseur, modele, consigne, plafond_role, session, lire=None)` : la signature du noyau ; **`consigne` est une `requete_na_v3.RequeteAssemblee`**. Rend :
  - le dict du noyau plus `issue_na`, une valeur parmi :
    - « ok » ;
    - « arrêt n° 1, consigné, non relancé » ;
    - « réponse illisible, cause non établie » ;
    - « erreur » ;
  - `None` si non lancé ;
  - pour un refus écrit, `{"r": None, "lu": None, "refus_ecrit": RenduRefusEcrit, "issue_na": "refus écrit", …}`. **La surcharge de `juger` et l'étape « aiguillage » doivent lire `refus_ecrit` avant `a["r"]`.**
- Lève : `ArretPartCle` (n° 12), `ArretMotifNA` (n° 16), `ArretRequeteJournaliseeNA`, `ArretClassifieurNA` (n° 1, portée course), `ArretCreditNA` (n° 13), `ArretA2NA` ; et toute exception du noyau, telle quelle.
- À lire par le lot 6 :
  - `na_comptes` (non envoyés par arrêt, refus écrits par garde, non lancés, arrêts consignés, cause non établie, relais illisible) ;
  - `na_arrets_consignes` ;
  - `na_journal_arrets_cles` et `cumul.etat()`, **au seul journal des arrêts n° 11 à n° 13** ;
  - `comptes_envois_na(verifier_journal(...))`.
- Lignes à part : la même classe, avec une table « ligne à part » et `numero_generation=None`.

## 9. Réserves

1. **Un essai antérieur du relevé** (`releve-essai-1/`, laissé en l'état, hors de la table) porte en clair l'identifiant du modèle et le chemin du bloc-notes dans les textes captés : il précède le masque. Les essais 2 et la voie `relever` sont masqués. Il ne faut pas les verser sans tri.
2. **Une sortie de commande trop longue**, une recherche dans ce premier relevé, a été rangée d'office par l'outil d'agent sous `/root/.claude/projects/…/tool-results/`. Je ne l'ai pas écrite moi-même, mais elle vient de ma commande, et elle porte les mêmes textes captés.
3. **Dans chaque dossier de relevé**, les réponses brutes conservées et la maison de l'outil (transcriptions) portent l'identifiant du modèle et le chemin, tels que le kit et l'outil les écrivent. Ils sont hors de la table.
4. Le kit imprime, à la fermeture, des avertissements « aclose(): asynchronous generator is already running ». Ils sont sans effet sur les issues relevées.

## 10. Livré

Dossier : `dev-vehicule-na-lot-4/`, dans le bloc-notes de la session ; le chemin complet est dans le message de remise. Un compagnon `.sha256` par fichier de la table ; table `table-empreintes-dossier-na-lot-4-v1.txt`. Les copies `base/`, `base-v2/` et `copie-orchestrateur-application/` restent hors de la table ; ce ne sont pas des dépôts, et aucune ne contient la liste réelle.

— développeur du lot 4 du véhicule NA-1, modèle O

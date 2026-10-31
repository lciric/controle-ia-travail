# Contre-lecture CL20 — orchestrateur du pôle v55, course 2 et pré-pilote (R2)

**Contre-lecteur** : Sonnet 5.5, instance neuve (je n'ai écrit ni la v55, œuvre d'un Opus, ni CL18, ni CL19). **Date** : 31 octobre 2026, reprise vers 12:45 UTC après l'interruption d'un premier contre-lecteur à 12:09 UTC. Aucun fichier `contre-lecture-cl20-*` n'existait avant celui-ci (vérifié au début et juste avant l'écriture).

**Ce que j'ai lu** (chemins relatifs au dépôt ; les chemins `pole/…`, `essais/…`, `demonstrations/…` sont relatifs à `docs/notes/ideation-organisme-v1/orchestrateur-v55/`, arbre déplié identique à l'archive : 178 fichiers comparés, 0 différence) :

| objet | empreinte sha256 |
|---|---|
| `orchestrateur-v55/LISEZMOI-orchestrateur-pole-v7-v55.md` | `bbfdcb3c30d174dd7feeee9ba8dd20aeb7777c5f0e65aeb087e3c4388c743aa3` |
| `orchestrateur-v55/EMPREINTES-orchestrateur-pole-v7-v55.txt` | `d3519d68fcc46077ea91d7c853348e79fadd74ec743277e2e77de56ab0048f7b` |
| `orchestrateur-v55/CODE-orchestrateur-pole-v7-v55.zip` | `58b33177033c8f726003627378b0909e50f830da96a80506b11bda652bfa4aab` |
| `contre-lecture-cl19-orchestrateur-v54-v1.md` | `f1cc6c1a974fcbe4efe4d7dfe0087333ea1103b9ad6aa0e98f9016f6d7c3f31e` |
| `brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/pre-pilote-course-2-v1/preenregistrement-pre-pilote-course-2-brouillon10.md` (non gelé) | `ea940d56e5ee949e7b71a57488f7c2c8a2b7ac4835f30cb5f98933e4c00c824f` |
| même dossier, `…-brouillon7.md` (spécification citée par le code) | `799b9ca9c4ec30d8ab2c782496643b64cdbfcd8ca09eb08b9b8694b0c8ece6f5` |

Toutes les empreintes de ce tableau ont été recalculées par `sha256sum` au moment de l'écriture.

Le brouillon 10 est volumineux (245 Ko) : je l'ai lu par plages (lignes 1 à 80, 135 à 153, 393 à 472, 602 à 668) et par recherches ciblées (A1, A2, A15, A19, A21, DEP4, D-g, D-i, M4, M9, R5, graines). Je n'ai pas relu le reste ; les écarts ci-dessous sont donc ceux que j'ai pu établir, pas une liste exhaustive.

---

## Verdict

**Lançable après corrections.** Pas en l'état.

- La v55 traite correctement la plupart des constats de CL19 : neuf sur treize sans réserve qui change le verdict, quatre avec une réserve qui compte (CL19-03, CL19-04, CL19-09, CL19-10 ; §4). Les essais et le banc de mutations rejoués donnent les résultats annoncés (§3).
- Deux défauts empêchent pourtant un lancement **réel** du pré-pilote tel que le brouillon 10 le décrit.
  1. **CL20-01.** Le contrôle A2 général que la v55 ajoute arrête l'exécution à la première réponse réussie d'Argon : l'adaptateur de commande externe vérifie le modèle servi, puis ne le recopie pas dans le résultat. Le moteur simulé le recopie : ni les 709 essais ni les 103 mutations ne peuvent le voir. J'ai reproduit le défaut avec le vrai adaptateur (§5).
  2. **CL20-02.** Le code joue la règle de dépense « réservation » du brouillon 7, pas les plafonds de relais souples du brouillon 10 ni du GO-2026-10-31-03. L'écart n'est pas une faute de l'auteur (le brouillon 10 est postérieur à la v55) ; c'est un décalage à résorber avant la v56.
- Le plafond dur de 50 USD (arrêt d'étape à 45) est bien tenu par l'orchestrateur : le risque est une exécution différente de ce qui sera scellé, pas un dépassement de dépense.
- Deux conditions extérieures au code : ta réponse à la question N5 (règle A21) avant tout lancement, parce que le code lit la clé des classes par programme en É3 et en É5 sans interrupteur de lecture stricte (§6) ; et le gel de D-i et D-g, parce que le code ne joue ni D-i (2) ni la rédaction des fiches de M6b par le rédacteur en É1 (CL20-07, CL20-08).

**Compte des constats** : 15 — **2 bloquants** (CL20-01, CL20-02), **6 majeurs** (CL20-03 à CL20-08), **7 mineurs** (CL20-09 à CL20-15).

**Les trois plus importants** : CL20-01 (arrêt à la première réponse d'Argon), CL20-02 (règle de dépense non codée), CL20-05 (les fusions inachevées retournent dans l'héritage, la mémoire et l'étage, ou se perdent sans archive).

Échelle de gravité utilisée : **bloquant** = pas de lancement réel tant que non corrigé ; **majeur** = à corriger avant la course 2, et avant le pré-pilote si possible (risque réel mais borné, ou décalage avec le texte) ; **mineur** = nettoyage, documentation, défense en profondeur.

---

## 1. Méthode et limites

Fait : lecture du LISEZMOI, de la liste d'empreintes, de CL19 et de tout le code de la couche v55 (`noyau_v55`, `coffre_v55`, `course2_v55`, `prepilote_v55`, `gardes_e0_v55`, `configuration_v55`, `bisociateur_v55`, `etage_entre_generations_v55`, `simulation_v55`, lanceur `demonstrations/ideation_v7.py`), des couches v53/v54 qu'elles recouvrent quand le constat l'exigeait, des essais v55 et du banc de mutations. Essais exécutés sur processeur seulement, **sans réseau** (espace de noms réseau neuf, boucle locale seule), avec `python -I -B`, dans des dossiers temporaires hors du dépôt (`/tmp/cl20_work/`), l'archive extraite dans un dossier neuf. Sondes ciblées écrites par moi (`/tmp/cl20_work/probes/`, hors dépôt, moteur simulé ou fonctions pures) pour chaque constat marqué « reproduit ».

Non fait, conformément à la consigne : aucun appel de modèle, aucune clé lue, aucun `git fetch`, aucun commit, aucun `.sha256` écrit dans le dépôt (l'empreinte de ce fichier est à calculer par l'appelant), rien lu sous `donnees/`, aucun fichier existant modifié.

Limites propres à cette contre-lecture :
- `bwrap` est absent ici : les essais de bac réel (ignorés par la variable explicite, motif « ESSAI RÉEL NON JOUÉ ») ne sont pas joués, comme chez l'auteur, et `test_v51_06` échoue pour cette raison. Sur les 12 ignorés, deux demandent seulement le brouillon 7 et l'annexe réelle dans l'arbre du dépôt : je les ai rejoués avec ces deux fichiers copiés dans mon arbre de rejeu, ils passent (93 réussis, 0 ignoré sur `test_v54_annexe.py`, `test_v54_corrections.py` et `test_v55_corrections.py`). Les dix autres ignorés sont, d'après les motifs du code d'essai, des essais de bac réel ou de kit d'agent absent ; je n'ai pas relevé le motif de chacun. L'isolement réel reste à éprouver sur la machine du run.
- Je n'ai pas vu la configuration réelle de la course (hors livraison) : le branchement d'Argon (CL20-01) est déduit de `demonstrations/ideation_v5.py:64-66` et du dossier de service (`docs/notes/ideation-organisme-v1/course-2/dossier-service-course-2-v1.md:30`, devis v4 à v6 : `commande_argon_v3d.py`).
- Je n'ai pas pu lire les lignes GO-2026-10-31-03 et GO-2026-10-31-04 : le `registres/go.md` local s'arrête avant (le brouillon 10 les cite d'après `origin/main`, commit `587ac246`), et je n'ai pas fait de `git fetch`. J'ai seulement essayé `lire_plafond` sur les textes que le brouillon cite (« 50 USD » passe).
- Le rejeu complet de la suite s'est fait sur une machine chargée par cinq autres agents : le temps mesuré n'est pas comparable à celui de l'auteur.

## 2. Empreintes

| contrôle | résultat |
|---|---|
| Chaque fichier de `EMPREINTES-orchestrateur-pole-v7-v55.txt` (406 lignes) recalculé (`sha256sum -c`) | **406 OK**, 0 différent, 0 absent |
| Compagnons `.sha256` du LISEZMOI, de la liste d'empreintes et de l'archive | **égaux** aux fichiers |
| Archive `CODE-orchestrateur-pole-v7-v55.zip` extraite dans un dossier neuf, comparée à l'arbre déplié | **178 fichiers, 0 différence** |
| Fichiers du dossier absents de la liste (176) | 175 compagnons `.sha256` et la liste elle-même : rien d'autre |
| R12 : arbre v54 inchangé | essai `TestR12V55.test_aucun_fichier_de_la_v54_modifie` réussi dans l'arbre complet |

## 3. Essais et mutations rejoués

| mesure | annoncé par l'auteur | rejoué ici |
|---|---|---|
| Fichier d'essais v55 seul (arbre à l'image du dépôt) | 46 réussis | **46 réussis**, 36 sous-essais, 4,5 s |
| Suite complète (`essais/`) | 709 réussis, 12 ignorés, 1 échoué (`test_v51_06`, bac réel), 461 sous-essais, 4 min 28 s | premier passage : **708 réussis, 12 ignorés, 2 échoués**, 461 sous-essais, **9 min 40 s** ; le second échec (`test_v53_course2.py::TestR12`) venait de mon arbre de rejeu, qui n'avait pas `EMPREINTES-orchestrateur-v52b.txt` dans le dossier parent ; réexécuté avec ce fichier : réussi. Total équivalent : **709 réussis, 12 ignorés, 1 échoué** (`test_v51_06`, `bwrap` absent : l'essai exige le vrai bac) ; parmi les 12 ignorés, 2 passent quand le brouillon 7 et l'annexe réelle sont présents (voir §1) |
| Banc de mutations (`essais/mutations_v55.py --raisons`) | 106 essais témoins, 103 mutations tuées pour la raison attendue | **103 mutations (v54 : 56, v55 : 47), 103 tuées pour la raison attendue, 0 autre raison, 0 défaut du banc, 0 survivante, 0 non appliquée ; témoin après restauration : 106 essais, 0 échec** ; 2 min 46 s |

Audit de propreté (R4, « trop beau » → même audit) : 103 sur 103 n'est pas suspect en soi, car le banc neutralise des gardes **qui existent** (`if False:`) et vérifie que leur essai échoue ; 19 motifs d'échec attendus sont le générique « not raised ». Le banc ne peut donc rien dire des gardes **absentes**. C'est exactement la zone où je trouve les défauts : adaptateur réel (CL20-01), signal (CL20-04), fusions inachevées (CL20-05), lecture interdite du bac (CL20-06), copie résiduelle de la clé (CL20-09). Aucun essai ni mutation de la v55 ne passe par un vrai adaptateur, ne reçoit de signal, ne coupe l'étape des fusions, ni ne regarde la liste de lecture interdite.

Autre remarque sur la livraison : l'archive seule ne suffit pas à jouer les essais. Dans l'extraction isolée, `test_v55_corrections.py` donne 45 réussis et 1 échoué (`TestR12V55.test_aucun_fichier_de_la_v54_modifie` cherche `EMPREINTES-orchestrateur-pole-v7-v54.txt` à la racine, absent de l'archive) ; la suite entière veut aussi `../EMPREINTES-orchestrateur-v52b.txt`, le brouillon 7 et l'annexe réelle hors du dossier (CL20-15).

## 4. Traitement des 13 constats de CL19

| CL19 | gravité | ce que fait la v55 (fichier:ligne) | essais / mutations | reste |
|---|---|---|---|---|
| 01 — source Gu-Krenn absente refusée au départ | majeur | **Traité.** Cause « non produit (source absente) » gardée (`pole/course2_v55.py:53-58`) ; ligne 20 « sans objet (déclarée) » au lieu de « non rejouée » (`pole/gardes_e0_v55.py:44-45, 183-206`) ; lignes 22b-24 de même pour le bras méta (`:227-250`). Sonde : source à empreinte fausse → départ accepté, bras compté. | `TestCL19_01SourcesAbsentes`, 3 mutations | CL20-10 : tout mode autre que « substitut » est aussi étiqueté « source absente » |
| 02 — lecture après un nœud | majeur | **Traité.** Nœud : retour avant mémoire, fin d'É9, classement (`pole/course2_v55.py:121-129`) ; pré-pilote : rien d'ouvert, clés déposées, attestation d'É5bis (`pole/prepilote_v55.py:310-331`) ; héritage vide au nœud (`course2_v55.py:167-168`). | `TestCL19_02RienApresNoeud`, 3 mutations | interruption par signal non couverte (CL20-04) |
| 03 — clé des classes lue par programme | majeur, décision de Lazar | **Traité en partie, décision laissée ouverte.** Coffre journalisé (`pole/coffre_v55.py:36-89`), couples (dépôt, rôle) déclarés, sorties limitées à des comptes, détail déposé scellé, É6 en ordre d'identifiants opaques, É9 réduite sur liste scellée (`pole/prepilote_v55.py:131-150, 199-281`). Voir §6. | `TestCL19_03CleDesClasses`, 8 mutations | copie résiduelle `_exempts_a8` (CL20-09) ; la lecture a lieu par défaut |
| 04 — sessions voisines du coffre | moyen | **Traité pour l'arborescence, régression pour le bac.** Sessions sous `<base>/sessions/<opaque>`, hors de la sortie, chemins normalisés, liens symboliques refusés (`pole/noyau_v55.py:44-55, 77-85`). | `TestCL19_04Sessions`, 3 mutations | la liste de lecture interdite du bac ne couvre plus la sortie (CL20-06) |
| 05 — ligne de GO et DEP4 | moyen | **Traité.** Montant lu entier, nombre étranger, approximations et « par unité » refusés (`pole/configuration_v55.py:53-70`). Je l'ai essayé sur 23 cas : « 1 045 USD » → 1045, « 10-45 USD », « ≈ 45 USD », « 50 USD par génération », « 50 USD (arrêt d'étape 45) » refusés ; « 50 USD », « 50,0 USD », « 50 USD GO-2026-10-31-03 » acceptés. DEP4 : phrase de confirmation exigée (`:103-117`). | `TestCL19_05LigneDeGo`, 4 mutations | la phrase porte sur une règle que le brouillon 10 déclare « sans objet » (CL20-02) |
| 06 — résultats externes par la forme seulement | moyen | **Traité.** Pièce scellée, script empreinté cité par nom et empreinte, identifiant égal à celui déclaré, empreinte de l'analyseur injecté pour la ligne 6 (`pole/gardes_e0_v55.py:72-90, 336-348`) ; seconde version de témoins écrite par une attestation de la version 1 (`pole/prepilote_v55.py:87-100, 326-331`). | `TestCL19_06Externes`, 4 mutations | le script n'est pas rejoué : on croit le résultat scellé (limite déclarée) |
| 07 — S6 par sous-chaîne | moyen | **Traité.** Bornes de mot et d'extension décimale, nombres ajoutés comptés (`pole/prepilote_v55.py:43-68`). | `TestCL19_07S6`, 4 mutations | CL20-13 : cas sain obtenu par construction du simulateur |
| 08 — gardes sans artefact, banc trompeur | moyen | **Traité.** `_arrete(f, types, motif)` exige le type d'exception (`pole/gardes_e0_v55.py:48-56`) ; ligne 21 jouée par la génération (`pole/course2_v55.py:37-45, 86-89`) ; ligne 22b avec annexe absente ; banc recompilé avec la cellule `__class__` (`essais/mutations_v55.py:1-17`). | `TestCL19_08Artefacts`, 4 mutations | gardes absentes hors de portée du banc (§3) |
| 09 — I-9, constante de spécification | mineur | **Traité sur la lettre.** Brouillon relu et rapport recalculés, différence limitée (`pole/bisociateur_v55.py:46-58`) ; spécification recalculée au lancement (`pole/configuration_v55.py:123-139`, `demonstrations/ideation_v7.py:58-61`). | `TestCL19_09Annexe`, 4 mutations | la garde vérifie le brouillon 7, non le préenregistrement scellé (CL20-03) |
| 10 — écarts non déclarés | mineur | **Traité, avec deux régressions.** Écarts déclarés (LISEZMOI, section « Écarts au brouillon 7 ») ; A2 « modèle servi absent » gardé pour tous les rôles (`pole/noyau_v55.py:33-36, 87-91`) ; causes (iii) et (iv) de M9 (`pole/course2_v55.py:91-107`). | `TestCL19_10Ecarts`, 3 mutations | CL20-01 (le correctif d'A2 arrête Argon) ; CL20-11 (causes mal attribuées) ; CL20-12 |
| 11 — machine jetable | mineur | **Traité pour les cas cités** : `GH_PAT`, `*_KEY_*`, `*_KEY_FILE`, `SSH_AUTH_SOCK`, `AUTH`, `*_AUTH` refusés ; `TOKENIZERS_PARALLELISM` accepté (`pole/etage_entre_generations_v55.py:19-39`). | `TestCL19_11MachineJetable`, 2 mutations | liste noire encore trouée (CL20-14) |
| 12 — mineurs | mineur | **Traité.** Entrée de rendu gardée entière (`pole/prepilote_v55.py:157`) ; relecteur muet = « non relu (technique) » (`:225`) ; cohérence de D-g (`pole/configuration_v55.py:115-119`) ; boîte d'É5 sans liste par classe ; « bisociative » laissé à la liste injectée (déclaré). | `TestCL19_12Mineurs`, 3 mutations | — |
| 13 — couverture | mineur | **Traité.** Essais ajoutés : pré-pilote en nœud, A19 à É0, S18 dans le flux, reprise après A8. | `TestCL19_13Couverture` | aucun essai sur signal, fusions inachevées, adaptateur réel, liste de lecture interdite |

## 5. Constats CL20

Légende des preuves : « reproduit » = j'ai exécuté une sonde sur le moteur simulé ou sur une fonction pure et je donne ce qu'elle rend.

### Bloquants

#### CL20-01 — bloquant — Le contrôle A2 général de la v55 arrête l'exécution à la première réponse réussie d'Argon

- **Où.** `pole/noyau_v55.py:33-36, 87-91` (`appel` appelle `controle_a2` après chaque appel lancé) ; `pole/adaptateurs.py:775` (`AdaptateurCommandeExterne.lancer`, chemin de succès : `Resultat(…, "ok", texte_brut=…)` sans `modele_servi`, alors que `controle_modele`, `:680-703`, vient de lire et de vérifier `objet["modele_servi"]`) ; branchement prévu `demonstrations/ideation_v5.py:64-66` (`commande_externe`, `exiger_modele_servi=True`).
- **Preuve (reproduit).** Avec une commande factice locale qui imprime une ligne conforme dont `modele_servi` est égal au modèle demandé :
  ```
  r = AdaptateurCommandeExterne(cmd, exiger_modele_servi=True).lancer("juge_ideation", "…", dossier, 1.0, 1, modele="argon-modele-test")
  → statut : ok   modele_servi porté par le Resultat : None
  controle_a2(r.statut, r.modele_servi, "argon-modele-test")
  → ModeleServiAbsent : A2 : modèle servi non lu pour une réponse « ok » … : arrêt
  ```
  Les adaptateurs Kimi (`pole/adaptateur_kimi_v53.py:175-190`) et du kit (`pole/adaptateurs.py:441-444`) renseignent `modele_servi` ; le moteur simulé aussi. Seul l'adaptateur de commande externe le perd. Rien dans les essais v55 n'utilise un vrai adaptateur.
- **Conséquence.** Si Argon est branché comme dans `ideation_v5.py` (hypothèse : je n'ai pas la configuration réelle), la première réponse « ok » d'Argon lève `ModeleServiAbsent` (une `RuntimeError`) ; elle traverse `executer` (`except Exception`, `arret` posé, relevée). Pré-pilote : arrêt à É6, après la dépense d'É1 à É5 ; course : arrêt à l'étape « juges ». Aucun verdict d'Argon n'est jamais utilisé.
- **Correction proposée.** (a) Dans une couche neuve (R12 : on ne réécrit pas `adaptateurs.py`), envelopper l'adaptateur de commande externe pour recopier `objet["modele_servi"]` dans le résultat quand le statut est « ok » ; (b) essai sur le **vrai** adaptateur et une commande factice (cas sain : modèle servi égal ; artefact : modèle différent ou absent → refus) ; (c) ajouter à la ligne 1 de la table R5 le cas « adaptateur réel qui perd le modèle servi » ; (d) une mutation qui supprime la recopie ; (e) même essai pour l'adaptateur du kit avec un faux kit.

#### CL20-02 — bloquant — La règle de dépense du brouillon 10 (plafonds de relais souples) n'est pas celle que le code joue

- **Texte.** Brouillon 10, l. 608 (A1 : plafond de relais fixé au lancement de chaque étape ; étape protégée : `max(plafond de relais ; S17 − cumul − attendu aux bases des étapes restantes non retirées)` ; étape retirable : plafond fixe), l. 622 (A15 : « relais incapable de recevoir, au lancement de chaque étape, le plafond dur… »), l. 644-645 (lignes R5 11a et 11b), l. 699 et 144 (DEP4 : exigence « réservation » déclarée **sans objet**, remplacée par « chaque relais est lancé avec le plafond dur calculé »). Le GO-2026-10-31-03, tel que le brouillon le cite (l. 64), dit « plafonds de relais du brouillon 5 gardés, souples pour les étapes protégées ».
- **Code.** `pole/budget_v53.py:97-146` (projection, arrêt d'étape, `cumul + réservation > plafond` ; le reste offert à l'étape est `plafond − cumul`) ; `pole/budget_v54.py:35-60` ; `pole/noyau_v54.py:97-99` (le plafond de chaque appel est `min(plafond du rôle, reste de l'étape)` ; aucun plafond **d'étape** n'est calculé ni transmis) ; `pole/gardes_e0_v55.py:134-148` (ligne 11 unique, sur `BudgetV54` à réservation ; pas de 11a ni de 11b) ; `pole/configuration_v55.py:105-114` (DEP4 : phrase de confirmation de la règle « réservation »). L'adaptateur Kimi ne transmet que le plafond de l'appel : le relais « tient son plafond » (`pole/adaptateur_kimi_v53.py:7-8`).
- **Écarts.** (1) Pas de plafond de relais par étape : une étape protégée peut consommer tout `S17 − cumul` et affamer les suivantes, ce que la formule du texte interdit. (2) La projection d'A1 n'utilise pas « plafond de relais + attendu aux bases ». (3) Les statuts de coupure de la ligne 11b (protégée coupée → « non mesuré (budget) », retirable coupée → retirée, M6 entière coupée après 4 fiches → lue réduite, M6b coupée → réserve) ne sont pas rejoués à É0. (4) La condition d'A15 « relais incapable de recevoir le plafond dur » ne peut ni se vérifier ni se satisfaire. (5) Un lancement réel exige une phrase DEP4 pour une règle qui n'existe plus.
- **Ce qui reste vrai.** Le plafond dur S17 = 50 USD et l'arrêt d'étape à 45 sont tenus par l'orchestrateur (cumul jamais écrêté, plafond par appel borné au reste de l'étape, coût inconnu compté au plafond de l'appel). La dépense totale ne dépasse pas 50 USD. Le risque est une exécution **autre que le préenregistrement** (R1) : ce qui est mesuré, réduit ou retiré sous pression budgétaire ne suivrait pas A1, et les probabilités de C13 chiffrées avec le devis v6 ne s'appliqueraient pas.
- **Correction proposée.** Décision de Lazar (voir D-CL20-1 en §8). Si le modèle du devis v6 est retenu : budget v56 avec plafond d'étape fixé au lancement et journalisé, transmis au relais (ou refusé s'il ne sait pas le recevoir), lignes 11a et 11b avec leurs artefacts, DEP4 réécrite en « chaque relais lancé avec le plafond calculé » vérifiée par une garde ; retirer l'exigence de phrase DEP4 « réservation ». Si le texte est ramené à la règle « réservation » : réécrire A1, A15, DEP4, R5 11 et le chiffrage de C13 avant le gel.

### Majeurs

#### CL20-03 — majeur — La spécification vérifiée au lancement et inscrite au manifeste est le brouillon 7

- **Où.** `pole/configuration_v54.py:41-43` (chemin et empreinte `799b9ca9…`) ; `pole/configuration_v55.py:123-139` ; `demonstrations/ideation_v7.py:58-61` (moteur réel : `conforme` doit être vrai) ; `pole/prepilote_v55.py:298` (`"specification": "brouillon 7 (799b9ca9…)"` écrit en dur dans le manifeste de départ).
- **Constat.** La garde de CL19-09 passe tant que le fichier du brouillon 7 est inchangé : c'est le cas aujourd'hui (empreinte recalculée égale). Elle ne dit rien du brouillon 10 (`ea940d56…`, non gelé), ni de la version gelée qui sera scellée après la contre-lecture 5. Un run du pré-pilote écrirait « brouillon 7 » dans son manifeste, ce qui est faux pour ce qu'il aura joué (R1, R6, R9 : le manifeste doit lier le run au préenregistrement scellé).
- **Correction proposée.** Lire le chemin et l'empreinte du préenregistrement scellé dans la configuration (pièce empreintée, sceau vérifié, empreintes de la contre-lecture 5), les écrire au manifeste ; essais : pièce conforme (cas sain), un octet changé et sceau absent (artefacts) ; étendre la ligne 29 de la table R5.

#### CL20-04 — majeur — Pas d'arrêt propre sur signal ; le manifeste de fin d'une exécution interrompue ne le dit pas

- **Où.** `pole/course2_v55.py:142-146` et `pole/prepilote_v55.py:332-336` : seul `except Exception` pose `self.arret`. Une interruption clavier (`KeyboardInterrupt`) n'est pas une `Exception` ; elle traverse, le `finally` écrit le manifeste de fin avec `arret = None`. Aucun gestionnaire de signal dans `pole/` ni dans `demonstrations/` (recherche de `signal`, `SIGTERM`, `SIGINT`, `atexit` : seuls les anciens `pole/adaptateurs.py:722-746` tuent le groupe de processus d'une commande externe).
- **Preuve (reproduit, moteur simulé).** (a) Interruption levée dans le 6e, le 41e appel d'une génération et le 11e, le 61e du pré-pilote : `manifeste-fin.json` est écrit avec `"arret": null` et `"noeud": null`, indistinguable d'une fin normale (seuls manquent `classement.json` et `fiches.json`). (b) Signal d'arrêt (SIGTERM) envoyé à un processus enfant pendant le 12e appel : code de sortie −15, **aucun** `manifeste-fin.json`, 12 dossiers de session laissés dans la base temporaire, pas d'`empreintes-sortie.txt`.
- **Pourquoi ici.** L'arrêt par identifiant de processus est la manière normale d'arrêter une instance (R10) ; la machine jetable peut être détruite en cours de route. Le coût de l'appel en cours est bien compté (le `finally` de `appel`, `pole/noyau_v54.py:104-114`), mais plus rien n'est scellé de l'état atteint. Il n'y a pas de reprise (sortie neuve exigée, R12) : un arrêt coûte une nouvelle dépense.
- **Correction proposée.** À la racine des deux `executer`, convertir SIGTERM et SIGINT en une exception typée ; `except BaseException` pose `self.arret = "signal …"` ; le `finally` existant écrit le manifeste de fin, range les sessions et remplit `empreintes-sortie.txt` (pré-pilote aussi). Essais (R5) : cas sain (aucun signal : `arret` nul) et artefact (signal reçu par un enfant en cours d'étape : manifeste de fin portant l'arrêt, aucun dossier de session orphelin).

#### CL20-05 — majeur — Les fusions inachevées ne sont ni écartées ni archivées, et les fusions complètes retournent dans l'héritage

- **Où.** `pole/course2_v54.py:371-406` (`etape_fusions` : chaque fusion est ajoutée à `self.fiches` et à `self.ordre` dès sa création ; l'aiguillage et les jugements viennent ensuite) ; `:426-439` (`lot` = toute fiche munie d'un passeport ; écriture de `classement.json`, `fiches.json`, `ajouter_memoire(lot)`) ; `:463-467` (`texte_heritage` donne titre, résumé et « notable » de **toutes** les lignes du classement, fusions comprises) ; `pole/etage_entre_generations_v53.py:88-93` (l'étage reçoit toutes les lignes) ; la v55 ne change rien hors nœud (`pole/course2_v55.py:121-129, 167-168`).
- **Preuve (reproduit, moteur simulé, plafond S17 abaissé pour couper l'étape des fusions, état final « retirée »).**

  | plafond | fusions créées | avec passeport | jugées (au moins un verdict) | dans `classement.json`, `fiches.json`, héritage, mémoire |
  |---|---|---|---|---|
  | 50 (aucune coupure) | 3 | 3 | 3 | 3, dont 3 des 11 entrées d'héritage |
  | 36,0 | 3 | 3 | **0** | **3** (10 entrées d'héritage sur 11 « non notable ») |
  | 35,0 | 3 | 1 | **0** | **1** |
  | 34,5 | 3 | **0** | 0 | 0 : **contenu perdu, nulle part archivé** |
  | 34,0 / 33,5 | 2 / 0 | 0 | 0 | 0 : idem |

  Seul `fusions.comptees_a_part = len(self.fusions)` garde une trace, sans contenu.
- **Constat.** Le seul canal par lequel une fiche d'une génération revient dans la suivante est ce texte d'héritage, avec la mémoire anti-redite et l'entrée de l'étage. Une fusion aiguillée mais jamais jugée y retourne avec « non notable » ; une fusion non aiguillée disparaît sans archive. Dans le cas sain, les fusions jugées reviennent aussi (3 sur 11) : c'est le comportement des v53 et v54, mais le manifeste les déclare « exploratoire (registre seulement) ». Une fusion « incohérente » (contenu refusé après coup) n'a pas de traitement distinct.
- **Correction proposée.** (a) Marquer une fusion « complète » seulement si elle a son passeport **et** ses trois verdicts ; (b) `lot`, `texte_heritage`, `ajouter_memoire` et l'entrée de l'étage ne prennent que les fusions complètes (ou aucune : voir D-CL20-2) ; (c) écrire `fusions-inachevees.json` scellé (contenu, empreinte, cause : non aiguillée, non jugée, refusée), jamais relu avant la fin d'É9 ; (d) essais avec les trois artefacts ci-dessus et contrôle des quatre canaux ; (e) mutation « fusion inachevée dans l'héritage ».

#### CL20-06 — majeur — La liste de lecture interdite du bac ne couvre plus la sortie depuis la relocalisation des sessions

- **Où.** `pole/adaptateurs.py:264-269, 292` (par défaut : on interdit le grand-parent du dossier de l'agent) ; `demonstrations/ideation_v5.py:68` (`AdaptateurClaudeSDK(url, arme=True)`, sans `interdire_lecture`) ; `pole/noyau_v55.py:77-85` (dossier de l'agent = `<base>/sessions/<opaque>`).
- **Preuve (reproduit, `construire_options` sur les deux dispositions).** v54 : `denyRead = [<sortie>]`, le coffre est couvert. v55 : `denyRead = [<base des sessions>]`, `allowRead = [<session>]` ; `<sortie>/coffre` **n'est plus** interdit en lecture. La docstring de `pole/adaptateurs.py:278-283` rappelle que le bac du kit ne borne par défaut que les écritures.
- **Atténuation.** Les rôles du pôle n'ont aucun outil (`tools: []`, `OUTILS_PAR_ROLE`), donc rien ne lit aujourd'hui : la barrière est latente. Mais la v55 présente CL19-04 comme corrigé en s'appuyant sur le bac (`pole/noyau_v55.py:4-10`), et « connaître le nom tiré de la sortie » est un secret de chemin, non une barrière. Aucun essai n'examine `denyRead` (aucune occurrence dans `essais/test_v55_corrections.py`).
- **Correction proposée.** Créer la base avant les adaptateurs et passer `interdire_lecture=[base, sortie]` à chaque adaptateur du kit du moteur réel ; essai : `denyRead` contient la sortie et le coffre pour chaque rôle (cas sain), liste réduite à la seule base → refus (artefact).

#### CL20-07 — majeur — D-i (2), recommandé, n'est pas codé, et la décision n'est pas recoupée avec le plan joué

- **Texte.** Brouillon 10, l. 12 et 55 (D-i : 28 fonds, ou 28 + 4 rendus appariés, ou 24 dont 4 doublés ; recommandation (2)), l. 282 (É4 : 32 rendus sous (2)), l. 410 (graine `pp2-pa`), l. 416 (É3 : 4 rendus appariés), l. 469 (relais d'É3 et d'É4 élargis), l. 730.
- **Code.** `pole/prepilote_v54.py:121-148` (`planifier_fonds` : 28 fonds uniques), `:511-` (`etape_e8_paraphrases` : PB, NA, NB ; pas de PA). Aucune occurrence de `pp2-pa` ni de rendu apparié. `decisions_a15.d_i` est seulement exigé non vide (`pole/configuration_v54.py:216`) : rien ne le recoupe avec le plan.
- **Conséquence.** Si tu gèles (2), le code joue quand même (1) **sans le dire** (repli silencieux, R5) : É3 et É4 à 28 au lieu de 32, pas de paires inter-fournisseurs dans la mémoire anti-redite, coût et porte du brouillon 10 chiffrés sous (2) mais mesurés sous (1).
- **Correction proposée.** Soit coder (2) (variante de `planifier_fonds`, É3, É4, É8, tâche `pp2-pa` : les 4 fonds appariés passent l'aiguilleur, jamais un juge), soit faire refuser par `verifier_configuration_pre_pilote_v55` toute valeur de `d_i` autre que (1) tant que (2) n'est pas codé. Même traitement pour (3).

#### CL20-08 — majeur — D-g (b) : les quatre fiches de M6b ne sont pas écrites comme le dit le texte

- **Texte.** Brouillon 10, l. 410 (tâche `pp2-m6b` : tirage de 4 sources dans une liste scellée), l. 469 (M6b écrite par le rédacteur dans le relais d'É1, vérifiée en É9b), l. 697 (DEP2c : liste scellée tenue par session-depot).
- **Code.** `pole/prepilote_v54.py:98-99, 546-576` : `etape_e9b_m6b` lit `prepilote.m6b.fiches` et `.sources` comme **pièces** déjà écrites ; le rédacteur n'écrit rien de M6b en É1 ; aucune graine `pp2-m6b`.
- **Conséquence.** La part « lecture des PDF et rédaction » (0,64 USD dans le relais d'É1) n'existe pas ; la garde de la ligne 31 (source hors de l'entrée du vérificateur) est testée sur des fiches d'origine non décrite. Si D-g (b) est gelé, soit les pièces arrivent écrites par un tiers (le texte doit alors le dire et le coût d'É1 baisse), soit le code manque.
- **Correction proposée.** Mettre le texte et le code d'accord ; essai de la ligne 31 sur le flux complet (fiche écrite à É1, source hors de l'entrée en É9b).

### Mineurs

#### CL20-09 — mineur — `_exempts_a8` garde en mémoire la classe G de chaque fond jusqu'à la fin

- **Où.** `pole/prepilote_v55.py:146-148, 168` (`self._exempts_a8 = {i for i, v in cle.items() if v["classe"] == "G"}` ; jamais supprimé) ; la docstring de `:6` affirme « plus aucune copie de la clé des classes en mémoire après É1 ». L'essai `test_cas_sain_deux_lectures…` ne regarde que `_cle_classes` et `fonds[i]["classe"]`.
- **Correction proposée.** Supprimer l'ensemble à la fin d'É3 (`try/finally`), essai `not hasattr(g, "_exempts_a8")` après É3 et mutation correspondante ; corriger la docstring.

#### CL20-10 — mineur — Tout mode Gu-Krenn autre que « substitut » est étiqueté « source absente » et accepté au départ

- **Où.** `pole/course2_v53.py:119-138` (toute erreur du bras Gu-Krenn → cause « source absente ») ; `pole/course2_v55.py:53-58` ; `pole/gardes_e0_v55.py:195-202`. La configuration ne valide pas `mode`.
- **Preuve (reproduit).** `mode: "modele"` et `mode` absent → `produit: False`, cause « non produit (source absente) », ligne 20 « sans objet (déclarée) », départ accepté. Une clé manquante ou une date invalide, elle, est refusée par la lecture de la configuration (bon comportement).
- **Texte.** A19 (brouillon 10, l. 626) et R5 lignes 20 et 21 prévoient « modèle » comme mode déclaré distinct ; « source absente » ne vaut que si la source de S31 manque. De même `pole/course2_v55.py:74` compte toute erreur de lecture de l'annexe du bras méta, y compris un défaut de code (`KeyError`, `TypeError`), comme « annexe non conforme » acceptée sans arrêt.
- **Correction proposée.** Valider `mode` dans {substitut, modele} à la configuration ; « modele » refusé avec un motif propre (« non branché »), jamais « source absente » ; erreur interne = arrêt, pas absence légitime.

#### CL20-11 — mineur — Causes de M9 (iii) et (iv) attribuées au mauvais bras

- **Où.** `pole/course2_v55.py:91-107`. Brouillon 7 (l. 440) et brouillon 10 (l. 518) : (iii) bras Gu-Krenn « moins de 2 fiches notables » ; (iv) bras **basique** « moins de 2 fiches étiquetées ». Le code met « moins de 2 fiches étiquetées » sur le bras **méta** (numéroté (iii) dans le LISEZMOI) et ne donne aucune cause au bras basique, qui reste « produit » dès que deux fiches éligibles partagent une case (`pole/course2_v54.py:302-305`).
- **Correction proposée.** Aligner : cause (iv) au bras basique ; pour le bras méta, soit ajouter la cause au texte, soit la ranger sous (i).

#### CL20-12 — mineur — A2 arrête toute l'exécution, le texte dit « arrêt de ce rôle »

- **Où.** `pole/noyau_v55.py:87-91` (exception) contre brouillon 10, l. 609 (« arrêt de ce rôle ; aucune bascule sans mot de Lazar ») et le mécanisme d'arrêt de rôle de la v54 (`pole/noyau_v54.py:80-84`, `roles_arretes`).
- **Conséquence.** Plus strict que le texte : on perd la suite de la mesure et les étiquettes « non mesuré » de C13. À régler avec CL20-01 : aligner le texte (arrêt de l'exécution) ou passer par le suivi des rôles.

#### CL20-13 — mineur — S6, « nombres ajoutés » : le cas sain est obtenu par construction du simulateur

- **Où.** `pole/simulation_v55.py:1-8` (le metteur en forme simulé « n'ajoute plus de nombre au rendu… pour que le contrôle passe ») ; `pole/prepilote_v55.py:53-68` (tout nombre du rendu absent des ancres est un nombre ajouté) ; maximum à 0 dans les essais (`essais/aides_v55.py`, `configuration_pre_pilote`).
- **Risque.** Avec de vrais rendus (numérotation « 1. », année, « 2 axes »), un maximum de 0 peut exclure beaucoup de fonds et déclencher A5 (plus de 6 fonds sur 28 exclus : arrêt). Le cas sain de la garde n'a jamais été éprouvé sur un texte réaliste (R4, R5).
- **Correction proposée.** Essai sur quelques rendus écrits à la main ou réels avant É3 ; ton choix du maximum (point déjà ouvert dans le LISEZMOI) ; compter à part la numérotation de liste.

#### CL20-14 — mineur — Machine jetable : liste noire encore trouée, variable portant `_V54`

- **Où.** `pole/etage_entre_generations_v55.py:19-39` ; variable de déclaration `POLE_MACHINE_JETABLE_V54` (`pole/etage_entre_generations_v54.py`), citée ni dans le LISEZMOI v55 ni dans le lanceur.
- **Preuve (reproduit, 38 noms essayés).** Acceptés : `NETRC`, `MYSERVICE_APIKEY`, `X_PASSPHRASE`, `KUBECONFIG`, `DOCKER_CONFIG`, `GIT_ASKPASS`, `KEYFILE`, `JWT`, `CI_JOB_JWT`, `BEARER`, `COOKIE`. Refusés comme attendu : `GH_PAT`, `HF_TOKEN`, `*_API_KEY`, `SSH_AUTH_SOCK`, `OPENAI_KEY_FILE`, etc. ; `TOKENIZERS_PARALLELISM` accepté.
- **Remarque.** Contrôle déclaratif, déjà reconnu (LISEZMOI). Correction proposée : liste **blanche** des noms d'environnement connus plutôt que liste noire de motifs ; documenter la variable (et son suffixe).

#### CL20-15 — mineur — L'archive ne suffit pas à jouer les essais

- **Où.** `essais/test_v55_corrections.py:697-712` (cherche `EMPREINTES-orchestrateur-pole-v7-v54.txt` à la racine, absent de l'archive) ; `essais/test_v53_course2.py:366` (cherche `../EMPREINTES-orchestrateur-v52b.txt`) ; essais qui lisent le brouillon 7 et l'annexe réelle hors du dossier. Preuve : voir §3 (45 réussis, 1 échoué dans l'extraction isolée ; mon premier rejeu complet a eu un échec de plus pour ce motif).
- **Correction proposée.** Écrire au LISEZMOI que la suite se joue dans le dépôt, ou joindre les listes nécessaires à l'archive.

## 6. A21 et CL19-03 : comment la v55 le traite (je ne tranche pas)

La v55 ne tranche pas : elle exécute par défaut ce que le Plan exige (lecture par programme de la clé des classes en É3 pour l'exemption de longueur de la classe G, et en É5 pour les ambigus, S18, S19) et l'entoure de garde-fous, tandis que le LISEZMOI laisse à Lazar le choix entre les lectures 1 et 2 de CL19-03 et que le manifeste de départ écrit « A21 : décision ouverte de Lazar » (`pole/prepilote_v55.py:304-305`).

Ce que le code fait :
1. Les couples (dépôt, rôle) autorisés sont déclarés au manifeste de départ (`pole/prepilote_v55.py:131, 302`).
2. Chaque lecture est journalisée **avant** d'avoir lieu (horodatage, rôle, raison), lecture non déclarée = incident (`pole/coffre_v55.py:47-63`).
3. La sortie d'une lecture est limitée à des comptes (types booléen, entier, réel ou nul : `:65-76`), le détail par témoin est déposé scellé et ouvert après la fin d'É9 (`pole/prepilote_v55.py:199-268`).
4. É6 appelle les juges dans l'ordre des identifiants opaques ; É9 réduite lit une liste scellée, jamais la clé d'antériorité.
5. La ligne 30 de la table R5 est rejouée avec le coffre v55 (`pole/gardes_e0_v55.py:287-305`) ; au nœud rien n'est ouvert.

Ce qu'il faut savoir avant de répondre à N5 :
- **Il n'y a pas d'interrupteur de lecture stricte.** Sous la lecture où A21 vaut « par quiconque », programme compris, un pré-pilote lancé avec la v55 produit deux incidents A21 par construction (É3 et É5). Sous l'autre lecture, A21 et la ligne 30 du texte doivent être amendés pour dire « programme, journalisé, comptes seulement ». Dans les deux cas, ne lance pas avant ta réponse.
- **Un fait à peser, pas une décision** : la clé des classes est une fonction déterministe de la racine de graines (`pole/prepilote_v54.py:121-148`, tâche `pp2-classes-axes`) ; la racine du run est publique dans le brouillon 10 (20261101, R9). N'importe quel programme, y compris l'orchestrateur, peut la recalculer à tout moment sans toucher au coffre. La non-lecture ne peut donc être qu'une règle vérifiée par journal, pas une impossibilité technique.
- La copie résiduelle `_exempts_a8` (CL20-09) est le seul reste de la clé en mémoire que j'ai trouvé ; le rédacteur, lui, reçoit la classe de chaque fond en É1 (`pole/prepilote_v54.py:271`), par construction du Plan.

## 7. Écarts entre le code et le brouillon 10

| élément | texte (brouillon 10) | code | écart |
|---|---|---|---|
| S17 : 50 USD, arrêt d'étape 45 | l. 36, 608 | `budget.plafond_usd` et `arret_etape_usd` ; `lire_plafond("50 USD")` accepté (`pole/configuration_v55.py:53-70`) | **conforme** pour les valeurs |
| Règle de dépense A1, plafonds de relais souples | l. 608 | règle « réservation » | **CL20-02** |
| R5 lignes 11a et 11b | l. 644-645 | ligne 11 unique (`pole/gardes_e0_v55.py:134-148`) | **CL20-02** |
| DEP4 et condition d'A15 sur le relais | l. 144, 622, 699 | phrase de confirmation d'une règle « sans objet » (`pole/configuration_v55.py:105-114`) | **CL20-02** |
| Spécification du lancement | brouillon 10 puis version gelée | brouillon 7 épinglé et écrit au manifeste | **CL20-03** |
| Étapes É1 à É9b, rôles protégée / sacrifiable / réductible / protégée hors porte | l. 413-420 | `PLAN` (`pole/prepilote_v54.py:48-51`) | conforme |
| D-i (2) : 28 fonds + 4 rendus appariés, tâche `pp2-pa` | l. 12, 55, 282, 410, 416 | absent ; décision non recoupée | **CL20-07** |
| D-g (b) : 4 fiches de M6b écrites par le rédacteur en É1, tirage `pp2-m6b` | l. 410, 469, 697 | pièces lues en É9b | **CL20-08** |
| M9, causes (iii) et (iv) | l. 518 | attribuées au méta et au Gu-Krenn | **CL20-11** |
| A19 : « modèle » ou « substitut » déclaré ; « source absente » seulement si la source manque | l. 626, R5 20-21 | seul « substitut » branché ; le reste = « source absente » | **CL20-10** |
| A2 : arrêt de ce rôle | l. 609 | arrêt de l'exécution | **CL20-12** (et **CL20-01**) |
| A21 : aucune lecture avant la fin d'É9 par quiconque ; ligne 30 | l. 628, R5 30 | lecture par programme journalisée en É3 et É5 | **§6, décision de Lazar** |
| Lignes R5 8, 9, 10, 17, 19 jouées en É0 par des scripts empreintés | R5 | résultats scellés externes, scripts non rejoués (déclaré) | limite connue |
| Ligne 22a (avant le gel de l'annexe) | R5 22a | hors code (avant le gel) | sans objet |
| Graines : tâches listées | l. 410 | `pp2-m6b`, `pp2-pa` absentes ; `pp2-ident-*`, `pp2-anonymisation-*` en plus (déclarées) | CL20-07, CL20-08 |

## 8. Décisions à prendre (format de décision)

**D-CL20-1 — Règle de dépense : relais souples ou réservation.**
- Décision : le code joue-t-il les plafonds de relais souples du devis v6, ou ramène-t-on A1, A15 et DEP4 du brouillon 10 à la règle « réservation » ?
- Enjeu : le GO-2026-10-31-03 dit « souples » ; le code est à « réservation » ; sceller un texte que le code ne joue pas est un écart à un préenregistrement (R1).
- Options : (a) coder le modèle v6 — avantage : fidèle à ton GO et au brouillon 10, probabilités de C13 valables ; inconvénient : budget v56, lignes 11a et 11b, DEP4, plafond d'étape transmis au relais, un à deux jours de travail. (b) réécrire le texte — avantage : le code existe déjà ; inconvénient : contredit ton GO, invalide le chiffrage de C13 du devis v6.
- Recommandation : (a), confiance 0,7.
- Défaut : aucun automatique, le GO est à toi (décision de Lazar).

**D-CL20-2 — Les fusions reviennent-elles dans l'héritage, la mémoire et l'étage ?**
- Décision : les fusions complètes (et elles seules) entrent-elles dans le texte d'héritage, la mémoire anti-redite et l'entrée de l'étage ?
- Enjeu : aujourd'hui toutes y entrent, les inachevées aussi (CL20-05), alors que le manifeste dit « exploratoire (registre seulement) ».
- Options : (a) jamais — avantage : aucun retour, cohérent avec « registre seulement » ; inconvénient : la mémoire anti-redite ne voit pas les fusions, elles pourraient être redites. (b) les seules fusions complètes, les inachevées archivées scellées à part — avantage : redites évitées ; inconvénient : un chemin de retour pour des fiches exploratoires.
- Recommandation : (b), confiance 0,55.
- Défaut sous 48 heures : (b).

## 9. Conditions de lançabilité du pré-pilote

Avant un lancement réel :
1. Corriger CL20-01 et CL20-02 (bloquants) ; CL20-03 et CL20-04 fortement recommandés ; livrer en v56 (R12), rejouer la suite et le banc, et ajouter les essais qui passent par un vrai adaptateur, un signal, une fusion coupée et la liste de lecture interdite.
2. Ta réponse à N5 (§6).
3. Geler D-i et D-g, et faire accorder le code ou refuser les valeurs non codées (CL20-07, CL20-08).
4. Fournir ce que le code ne produit pas et que le lanceur exige : l'analyseur de l'étage 1 (DEP3) injecté par un script d'appel — la ligne de commande seule ne peut pas démarrer le pré-pilote, `principal()` appelle `executer` avec `etage1=None` (`demonstrations/ideation_v7.py:72-75, 114-120`) et l'exécution s'arrête avec `EtageUnAbsent` — les pièces externes des lignes 6, 8, 9, 10, 17, 19, les lots du bras d'attaque (sinon M4 « non étalonné »), les fiches d'antériorité d'É9, les pièces de M6b si D-g (b).
5. Sur la machine du run, jouer les essais ignorés ici (`test_v51_06`, `test_v52b_02`, bac réel sous `bwrap`) et s'assurer de la présence du brouillon 7 ou, après CL20-03, du préenregistrement scellé dans l'arbre du dépôt.
6. Contre-lecture 5 du brouillon gelé (déjà prévue), puis verdict de porte par un sous-agent neuf (R13).

Pour la course 2 (au-delà de la question posée) : `verifier_go_v55` exige l'égalité exacte entre la cellule de plafond et `montant_requis` (N × S17 + plafonds d'étage, `pole/configuration_v55.py:72-100`). Le GO-2026-10-31-04 est un plafond total de 160 USD « séquencé » : une sous-session à S17 plus bas ne pourra pas se lancer sous cette ligne telle quelle. Je n'ai pas pu lire la cellule ; à trancher entre toi et l'auteur avant la première sous-session.

## 10. Ce que je n'ai pas vérifié

- Le comportement des adaptateurs réels hors Kimi (pas de réseau, pas de kit installé) : j'ai seulement exécuté `AdaptateurCommandeExterne` sur une commande locale factice.
- Les essais de bac réel (dix des douze ignorés, d'après leurs motifs) : ils demandent `bwrap`.
- Les scripts du brouillon 10 (chiffrage, puissance) : non rejoués.
- Le contenu du brouillon 10 hors des plages et recherches listées en tête de ce document.
- Le LISEZMOI dans le détail de ses « décisions laissées ouvertes » (choix 1, 4, 5, 8, 10, `nombres_ajoutes_max`, phrase DEP4, I-2, A14 sur petits échantillons) : lu, non rejoué.

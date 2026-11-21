# Vérification du lot 4 (surcharge d'`appel`, adaptateur neuf) du véhicule NA-1 — v1

Vérificateur du lot 4 du véhicule NA-1, modèle S. Pièce de travail (classe C). Processeur seul : aucun appel, aucune clé, aucune dépense, aucun relais lancé, aucune écriture dans un dépôt. Données factices. La liste réelle des noms refusés n'a servi qu'à un balayage en mémoire (comptes seuls) ; **aucun nom de cette liste ni aucun identifiant de modèle n'est écrit dans cette pièce**, y compris dans les noms de fichiers, que je désigne par leur rôle quand ils portent un nom du fournisseur.

## Verdict

**Conforme.** Les lots 4 et 5 peuvent partir vers le lot 6 sur cette base, avec les points du § 7 et trois nœuds pour la mère (§ 5 et § 7). Le code fait ce que le mandat et les errata 1 à 3 demandent ; les comptes rejoués sont égaux ; le relevé prouve ce que le développeur dit, ce qui laisse la règle « rien n'est ajouté » (D2) **non tenue par l'adaptateur seul** : décision de la mère, pas défaut du code.

## 1. Empreintes et rejeu

| pièce | sha256 | état |
|---|---|---|
| table du livrable | `747f782bed5c52304b8c7177b1c008c79f2c1554a72aa9069face7c78e3ee554` | égale à l'annonce ; 15 fichiers OK ; le 16e, le relevé, n'est pas versé, comme dit |
| rapport | `1b16fabb3f84b6d2a316b956a24b99a91f5897121bed5b8a98a769f580dff52f` | égal |
| relevé au faux fournisseur (dossier du développeur) | `6dc903bc4e8d30d8a0c49130cf5b46be0a6a2f2f953ba2ad1fcbaaf0cdaaf8ef` | égal à la table |
| orchestrateur | commit `a41b7b50…` | copie neuve, sans `.git` |

Chaîne rejouée : copie neuve ; paquet du lot 2 v5 ; paquet du lot 3 v3 ; paquet du lot 4, chacun par son programme (`--lancer-essais`).

| | annoncé | rejoué |
|---|---|---|
| essais, en tout | 287 (200 + 87) | **287 passés** |
| mutations du développeur | 51 sur 51 tuées | **51 sur 51 tuées** ; témoin non muté passe ; témoin inerte survit |
| mes mutations (49) | — | 40 tuées, 9 survivent (§ 4) |

## 2. Exigences du mandat et des errata 1 à 3

Lieux dans `paquet/orchestrator/pole/` : `appel_garde_na_v1.py` (AG), `routage_na_v1.py` (RT), adaptateur neuf du fournisseur des clés (AC). J'ai vérifié que les numéros de ligne du rapport sont exacts.

| exigence | faite | où | essai qui la tient |
|---|---|---|---|
| pas 0 : rôle arrêté par une garde héritée : « refus écrit », sans coût, rendu par sorte | oui | AG:264, AG:301-323, AG:330 | `TestRefusEcrit` ; Z4-01, Z4-19 à Z4-21 tuées |
| pas 1 : routage **par rôle**, couple (rôle, adaptateur) exact ; `hors_course` ; clé sans part ; adaptateur hors table | oui | RT:171 (`router`), AG:334-340 | `TestArret12`, `TestHorsCourse` ; L4-01 « routeur par espèce » tuée |
| table lue à son empreinte (n° 14), marque course / ligne à part / artefact | oui | RT:208 | `TestTable` ; L4-10, L4-11 ; **Z4-25 survit** (§ 4) |
| pas 2 : part de la clé : cumul + en vol + pire ; égal permis ; plafond d'une ligne à part | oui | RT:399, RT:360, AG:350-357 | `TestArret12` (part égale, un centime de trop), `test_en_vol_*` ; L4-07 à L4-09 |
| D11 : cas neuf juge et proposeur de l'espèce 3 sur la même clé ; artefact sur table plantée | oui | RT:171-190 | `test_cas_sain_neuf_*`, `test_artefact_table_plantee_*` |
| pas 3 et 4 : garde de motifs (v4) puis ligne « envoi » ; motif : « non envoyé » puis n° 16 sans le texte trouvé | oui | AG:358-371 | `TestArret16` (clair, six formes normalisées, fiche servie au juge, texte au seul journal) |
| erratum 3 : journal en panne (`JournalRefuse` ou `OSError`) : rien ne part, sans coût, arrêt nommé | oui | AG:289, 314, 364, 396 | `TestJournalEnPanne` (suppression, dossier, écriture en panne, réécriture) ; mutation « `OSError` non attrapée » tuée |
| erratum 1 : égalité : `verifier_avant_envoi` sur l'encodage de la chaîne **même** remise au noyau | oui | AG:372-381 | `TestEgalite::test_journal_egal_a_l_octet_a_l_envoi` (cinq sortes) ; mutation « appel retiré » tuée |
| erratum 2 : égalité refusée après la ligne « envoi » : une ligne « non envoyé » qui renvoie au rang, sans coût ; jamais comptée envoyée et refusée | oui | AG:378-381, AG:447-471 (`comptes_envois_na`) | `test_divergence_refusee_apres_la_ligne_envoi`, `test_comptes_refusent_un_renvoi_faux` ; Z4-22 tuée ; **Z4-23 survit** |
| erratum 2, point 3 : aucune ligne d'arrêt générale ni « ligne de la génération » écrite dans le journal fermé | oui | `na_arrets_consignes`, `na_comptes`, `na_journal_arrets_cles` en mémoire | dit au rapport (§ 3) ; aucun événement ajouté |
| erratum 1, point 2 : texte trouvé au seul journal | oui | AG:366-368 | `test_texte_trouve_seulement_au_journal` (message, `args`, `repr`, attributs, contexte) |
| pas 6 : `super().appel` inchangé ; coût compté sur la clé, plafond compris sur exception | oui | AG:382-390 | `TestCumulEtContexte`, `TestCompositionV56` contre le vrai noyau ; Z4-04 à Z4-06 tuées |
| pas 7 : « non lancé » ; statut, refus et erreur lus ; n° 1 ; A2 ; n° 13 ; « cause non établie » | oui | AG:391-442, AG:160, AG:173 | `TestNonLance`, `TestArret1`, `TestA2`, `TestArret13` ; Z4-08 à Z4-18 tuées |
| refus avant le noyau : aucune consommation, aucun coût, hors du suivi, une ligne, un compte | oui | AG:283-299 | `TestEnvoiRefuseSansCout`, `test_refus_sans_trace_au_coffre_reel` |
| adaptateur sans texte système, reste du transport gardé | **à l'option près** (voir § 5) | AC:49-60 | `TestSansTexteSysteme` ; mutation « texte d'origine laissé » tuée |
| réponses brutes conservées (refus et erreur compris) ; conservation impossible : rien n'est rendu | oui | AC:80-101, AC:119-131 | `TestReponsesBrutes` ; Z4-46, Z4-47, Z4-49 tuées ; **Z4-48 survit** |
| faux fournisseur sur la boucle locale seule | oui | `faux_fournisseur_na_v1.py` | `test_n_ecoute_que_sur_la_boucle_locale`, `test_modes` |
| relevé écrit et éprouvé contre le faux fournisseur, prêt pour le jeu derrière le vrai relais | oui | `releve_sans_systeme_na_v1.py` | `TestAnalyseDuReleve` ; le jeu derrière le vrai relais n'est pas du mandat |
| aucun identifiant de modèle, aucune clé, aucune recette | oui | grep du livrable : un nom d'en-tête de clé factice et deux noms de composants ; aucune valeur de clé | — |

## 3. Constat « un bloc d'environnement est ajouté à chaque requête, malgré D2 » : le relevé le prouve

J'ai lu le relevé par programme, sans afficher ni recopier de texte ni d'identifiant de modèle : comptes et booléens seuls.

- **23 requêtes lisibles**, sur les 9 scénarios (quatre jeux neufs, l'artefact de l'adaptateur d'origine et quatre issues du faux fournisseur).
- **Les 23** portent, après la consigne, **un second message de rôle « system »** qui commence par le bloc d'environnement, de **1 052 à 1 080 octets**. Il apparaît dans les **deux formes** (« chaîne vide » : 20 requêtes ; « absent » : 2 ; la dernière appartient à l'artefact).
- **Le champ système n'est pas vide** : deux blocs fixes par requête (22 sur 23), dont l'un est un en-tête de facturation de 73 octets et l'autre une phrase d'identité de 62 octets ; trois blocs avec l'adaptateur d'origine (artefact), dont le texte d'origine est bien reçu.
- **La consigne est retrouvée à l'octet** dans un message « user » pour 22 requêtes sur 23.
- **Le bloc d'environnement varie** : 9 empreintes distinctes sur 23 blocs. Les deux blocs fixes du champ système ne varient pas (une empreinte par rang). Le bloc d'environnement ne peut donc pas se déclarer « octet pour octet » comme un texte fixe ; au mieux comme un gabarit à valeurs variables.
- Le bilan du relevé écrit « aucun texte système reçu : faux » et « aucun texte ajouté aux messages : faux », pour les deux formes.

Conséquence : **la règle « rien n'est ajouté à l'enveloppe » (D2) n'est pas tenue par l'adaptateur neuf seul.** C'est ce que prévoyait le mot 5 de 07:46Z (« déclaré comme transport, octet pour octet, ou refusé »), mais ni l'un ni l'autre ne convient tel quel : un transport déclaré est impossible octet pour octet, et un refus bloque la course avec cet outil. Ce bloc contient aussi des motifs de la garde (chemin, nom de modèle, plafond) ajoutés **après** le point d'envoi, donc hors de sa vue. **Nœud pour la mère**, avant l'additif. Limite du relevé : il a été joué sur le faux fournisseur, sans le vrai relais ; le jeu derrière le vrai relais est à elle.

## 4. Mes mutations (49, dont 40 tuées)

Survivantes, aucune ne touche une exigence du mandat ; à renforcer, non bloquant :

- **Z4-25** : une table marquée « artefact » admise dans le contexte de la génération. La seule garde qui l'en empêche à cet endroit n'a pas d'essai (la lecture de la table la refuse déjà, L4-11). À éprouver : D11 veut une table plantée « jamais chargée par la course ».
- **Z4-48** : la réponse brute conservée peut être remplacée par sa version caviardée sans qu'aucun essai échoue : les essais n'emploient pas de texte que le caviardage changerait. § 6.2 demande la conservation « à l'empreinte de ce que le faux fournisseur a rendu » : à éprouver avec un texte caviardable.
- **Z4-32** (arrondi du coût à l'inférieur au lieu du supérieur), **Z4-36** (coût négatif admis au cumul) : la prudence de l'arrondi et le refus d'un coût négatif n'ont pas d'essai.
- **Z4-23** (deux renvois pour un même envoi), **Z4-38** (`hors_course` d'un autre type), **Z4-41** (table de course sans `hors_course`) : gardes de forme sans essai.
- **Z4-29** et **Z4-30** : quasi équivalentes (l'arrêt est levé de toute façon ; formulation du message).

## 5. Les points que la lettre ne fixe pas (§ 7 du rapport)

À l'additif : 1 (numéro de l'arrêt « requête journalisée » et son renvoi au rang écrit dans le champ `cause` ; une v3 groupée du journal pourrait ajouter `envoi_rang`) ; 2 (message synthétique de l'outil lu comme erreur de la clé : à confirmer) ; 4 (relais de protocole : « budget dépassé » lu comme refus pour crédit) ; 5 (contrôles de forme du pas 1 : consigne assemblée, case de la session, génération) ; 6 (portée de l'arrêt n° 1 par défaut : « appel », D8 en attente) ; 7 (règle de comptage du coût : bruit des flottants ôté au nano-dollar, arrondi au micro-dollar supérieur) ; 8 (pire d'un appel des lignes à part : 0,20 USD d'essai, valeur à écrire) ; 9 (D2 et garde de motifs touchés par le § 6).

**Nœud pour la mère** (point 3) : un refus pour crédit **du compte en amont** n'apparaît pas dans l'état du relais (relais v2 : il ne montre que le refus à son plafond). Il est lu « cause non établie », et la course continue. V9 veut l'arrêt n° 13 « avant que sa part soit atteinte ». Pour l'arrêter il faut un relais qui expose le statut d'amont, ou une lecture de son journal. Le développeur le dit et ne le tranche pas ; je confirme que le code ne peut pas faire mieux avec ce relais.

**Autre nœud** (constat 6 du § 6 du rapport) : l'outil écrit **une transcription par session** (consigne et réponse comprises) sous son dossier de configuration. En course, ces fichiers seraient hors du dossier de sortie si la maison de l'agent n'y est pas : V9, l. 82-83 (quarantaine). À écrire au lanceur (lot 8) : la maison de l'agent dans le dossier de sortie.

Les points 3, 6 (kit) et 9 du § 6 : à l'additif avec le nœud D2.

## 6. Interface pour le lot 6

Cohérente avec le lot 5 et le lot 3 v3, avec **une règle à écrire au mandat du lot 6**.

- Classe : `class GenerationNA(AppelGardeNA, GenerationV68)` ; contexte `ContexteAppelGardeNA(numero_generation, table, parts, pires_par_role, journal, garde, identifiant_case_de_session, cumul, …)` ; `consigne` est une `RequeteAssemblee` du lot 3 v3, que le lot 5 produit par ses fonctions (`assembler_portier_fiche`, `assembler_juge`) : même objet, même journal. Compatible.
- **`refus_ecrit` doit être lu avant `a["r"]`** : confirmé par le code (AG:322 rend `r` et `lu` à `None`, `refus_ecrit` porte le rendu). **Mais le portier du lot 5 attend un `RenduRefusEcrit` lui-même, non le dictionnaire du lot 4.** Sonde sur les deux formes : le `RenduRefusEcrit` seul donne « au coffre », cause « au coffre par refus du portier », compté à part ; le dictionnaire du lot 4 passé tel quel donne « au coffre », cause « réponse du portier non lue » et **0** au compte « au coffre par refus du portier » (il est lu comme un résultat dont la lecture est `None`). Le § 2.13 veut le compte à part. **Règle** : la fonction `appeler` que la génération donne au portier doit rendre `a["refus_ecrit"]` quand il est présent. Plus sûr : une v2 du lot 5 qui accepte les deux formes (une ligne, `refus_ecrit` lu avant `lu`).
- Passeport du portier : la surcharge de `juger` appelle `portier.exiger_passeport(issue.identifiant, issue.contenu)` avant tout appel de juge, puis `assembler_juge` du lot 3 ; l'identifiant du juge s'encode par le lot 1. Cohérent.
- Comptes : `na_comptes` (lot 4), `portier.comptes()` (lot 5), `journal_na_v3.comptes` (lot 3) alimentent la ligne de la génération : aucune fonction ne les fusionne, c'est au lot 6. Le journal reste fermé à quatre événements : les lignes d'arrêt et la ligne de la génération s'écrivent ailleurs, ou par la v3 groupée du journal, à décider avant le lot 6.
- Le cumul par clé est un seul objet pour toute la course, passé à chaque génération ; `na_journal_arrets_cles` et `cumul.etat()` ne vont qu'au journal des arrêts n° 11 à n° 13.

## 7. Ce que je n'ai pas fait

Je n'ai pas joué le relevé derrière le vrai relais (hors mandat). Je n'ai pas relu le faux fournisseur ni le programme de relevé ligne à ligne : je les ai éprouvés par leurs essais et par la lecture de la sortie. Je n'ai pas ouvert l'essai antérieur du relevé que le développeur dit porter un identifiant de modèle en clair.

— vérificateur du lot 4 du véhicule NA-1, modèle S

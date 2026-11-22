# Nœuds ouverts du véhicule NA-1 et règle de repli de GO-2026-11-22-35 — v1

Pièce de travail (classe C), auteur Opus, 2026-11-22. Processeur seul : aucun appel de modèle, aucun réseau, aucune clé lue, aucune dépense, aucune écriture dans un dépôt. Rien n'est tranché ici : chaque nœud est pour la mère, et ceux qui touchent un texte scellé vont à l'additif du véhicule.

Abréviations de chemins : **B** = `/home/user/controle-ia-travail/docs/notes/ideation-nouvelles-attaques-v1/` (branche `lot/compte-organisme-v1`) ; **M** = `/home/user/main-lecture/` (copie de `main`, HEAD `e5c0cb99`) ; **P** = `M/prereg/ideation-nouvelles-attaques-v1/`.

| pièce lue | empreinte (calculée) |
|---|---|
| B/inventaire-depart-v1/inventaire-depart-course-nouvelles-attaques-v1.md | `5f647ceeeb47e86d…` |
| P/preenregistrement-court-course-nouvelles-attaques-v9.md (« V9 », scellé) | `864f39a7ecd41a61…` |
| P/additif-1-preenregistrement-court-v9-mode-tenu-a-l-ecart-et-retrait-espece-6-v5.md (« additif 1 », scellé) | `9f731795cd8b9166…` |
| P/complement-valeurs-preenregistrement-court-v9-lot-1-v3.md (« complément », scellé) | `b4ef87dc6d5cce13…` |
| P/additif-1-complement-valeurs-…-espece-3-sur-minuit-v2.md (« additif au complément », scellé) | `ce76e0d6a0a6e65f…` |
| P/devis-course-nouvelles-attaques-v11.md (« devis », scellé) | `205e08f23ef9ced9…` |
| B/conception-vehicule-v5/conception-vehicule-course-nouvelles-attaques-v5.md (non scellée, « Conforme ») | `1b7f6822af20417e…` |
| B/lot-4-vehicule-na-v1/rapport-developpeur-lot-4-na-v1.md | `1b16fabb3f84b6d2…` |
| B/lot-4-vehicule-na-v1/verification-v1/verification-lot-4-na-v1.md | `3c8d1aa2d67b45c2…` |
| B/lot-4-…/paquet/orchestrator/pole/appel_garde_na_v1.py | `d16d07bf9b10ea82…` |
| B/lot-4-…/paquet/orchestrator/pole/adaptateur_claude_na_v1.py | `38baa2061d07f674…` |
| B/lot-6-vehicule-na-v3/reserve-modele-de-menace-lot-6-v3-v1.md | `a92d3d4a9ef862bb…` |
| B/lot-6-…/paquet/orchestrator/pole/configuration_course_na_v1.py | `0264479234576b3b…` |
| B/audit-regle-appels-google-v1/audit-regle-appels-google-orchestrateur-v56-lots-na-v1.md | `97c510f06b3e128d…` |
| B/audit-regle-appels-google-v1/audit-regle-appels-google-commande-et-relais-v1.md | `c21b13d3c64f5665…` |
| M/src/controle_ia/garde_google_v3.py (compagnon vérifié OK) | — |
| M/registres/go.md ; M/registres/decisions.md | `49d801d0…` ; `518ff6fa…` |

## Verdict

Quatre nœuds restent ouverts ; trois touchent des lignes scellées de la V9 (l. 73, 77, 387 pour le premier ; l. 384 pour le deuxième ; aucune pour le troisième ; le quatrième touche le pire par appel de la V9 l. 383 et du complément l. 166 pour les rôles Google). La règle de repli de GO-35 contredit la V9 l. 372 et touche neuf autres lignes scellées. **Une seule décision de construction en tranche trois à la fois** : un adaptateur Claude neuf qui parle directement à l'interface des messages, par le relais, sans l'outil en ligne de commande (nœud 1, option b). Il tient la règle « rien n'est ajouté », il voit le refus pour crédit d'amont (nœud 2) et il lit la catégorie d'un refus (point 5). Je le recommande, avec une confiance moyenne.

---

## 1. La règle « rien n'est ajouté à l'enveloppe » (D2) n'est pas tenue

**Énoncé, source.**
- La décision : conception v5, l. 87 (« D2 | **rien n'est ajouté à l'enveloppe** ») et l. 603 (« Décision de la mère (D2) : rien n'est ajouté à l'enveloppe »). Le mot 5 de 07:46Z est à la l. 227 : un texte par défaut est « déclaré à l'additif comme transport, octet pour octet, ou refusé ».
- Le constat : rapport du développeur du lot 4, l. 115 (« un second message, de rôle « system », bloc « # Environment » de 1 052 à 1 080 octets »), l. 116 (il « change d'un appel à l'autre (dossier, budget, date) »), l. 117 (il « porterait des motifs de la garde, chemin, nom de modèle, plafond et coût, ajoutés après le point d'envoi »). Le rapport relève aussi, l. 112 à 114, un en-tête de facturation de 73 octets et une phrase d'identité de 62 octets au champ système. Vérification du lot 4, l. 57 à 63 : « D2 n'est pas tenue par l'adaptateur neuf seul […] Nœud pour la mère, avant l'additif ».
- Le relevé a été joué sur le faux fournisseur, pas derrière le vrai relais (vérification, l. 63).

**Textes scellés touchés.**
- V9 l. 73 : « *Rien d'autre de fixe* : ni […] un renvoi interne (règle, décision, accord, **chemin**) ». Le bloc porte le dossier de travail.
- V9 l. 77 : la requête assemblée est « la suite d'octets envoyée à un fournisseur » ; elle est journalisée « avant chaque envoi […] après la garde de motifs ». Ce qui part n'est plus la requête journalisée.
- V9 l. 387 (arrêt n° 16) : « après elle, plus aucun octet ne change, et l'empreinte journalisée est celle de ce qu'elle a lu ». La garde ne voit pas le bloc, qui contient des motifs de ses deux familles (chemin, nom de modèle, plafond, coût).
- V9 l. 254 : l'enveloppe est une valeur ouverte de l'additif. C'est là que l'écart s'écrit.

**Options.**

| option | avantage | inconvénient | effort |
|---|---|---|---|
| (a) Déclarer le bloc comme transport, sous forme de gabarit : la liste fermée de ses champs variables est écrite à l'additif, et le relais journalise l'empreinte du corps reçu puis le passe à la garde de motifs | garde l'outil et le relevé du lot 4 | écart à V9 l. 73, 77 et 387 par lettre ; la garde lirait des motifs connus (chemin, modèle, budget) et devrait les admettre au rang « transport », ce qui ouvre un trou ; le texte du bloc vient en partie des réglages de la machine (rapport l. 118) | relais v3 avec journal du corps, garde au relais, épreuves ; 4 à 6 h |
| (b) **Adaptateur neuf, direct** : appel de l'interface des messages par le relais existant (qui n’admet que ce chemin : audit Google de l’orchestrateur, l. 21, sur `relais_reel_v2.py` l. 75), consigne seule dans un message « user », aucun champ système, réglages non textuels déclarés | D2 tenue à l'octet ; V9 l. 73, 77, 387 tenues sans écart ; plus de transcription de l'outil hors du dossier de sortie (vérification l. 81) ; le refus pour crédit d'amont et la catégorie d'un refus deviennent lisibles (nœud 2, point 5) | écart à la conception v5, l. 225 (« adaptateur du même type ») et au relevé du lot 4 ; perte du bac à sable de l'outil (sans objet ici : aucun outil, un tour) ; nouvelle vérification S | lot 4 v2 (adaptateur, faux fournisseur v2, essais, mutations) ; 4 à 6 h |
| (c) Le relais retire le bloc et les deux textes fixes avant l'amont | l'outil reste | le relais réécrit le corps : il devient un transformateur qu'il faut lui-même garder et éprouver ; dépend du format interne de l'outil, qui change d'une version à l'autre (2.1.330 ici contre 2.1.308 relevé : inventaire, l. 71) | 3 à 5 h, fragile |

**Recommandation : (b), confiance moyenne.** Seule (b) tient les trois lignes scellées sans écart. L'écart qu'elle crée porte sur une pièce non scellée (la conception) et se déclare à l'additif. Si la mère tient à l'outil, (a) n'est acceptable qu'avec une garde de motifs rejouée au relais sur le corps entier.

## 2. Un refus pour crédit du compte en amont reste invisible

**Énoncé, source.**
- Rapport du lot 4, l. 134 : « `/relais/etat` (relais v2) ne montre que le refus du relais à son plafond […] **Un refus pour crédit du compte en amont n'y paraît pas** : il est lu « cause non établie », et la course continue ». À la l. 125, le crédit, l'accès et la réponse coupée rendent tous trois « « refus », `assistant.model`, modèle servi `<synthetic>` ». À la l. 126, l'outil a relancé dix fois une erreur d'accès.
- Code : `appel_garde_na_v1.py` l. 161-171 (`relais_montre_refus_credit` : « au moins un refus autre que de modèle, et plus de quoi réserver un appel ») et l. 431-442 (sinon « réponse illisible, cause non établie »).
- Vérification du lot 4, l. 79 : « je confirme que le code ne peut pas faire mieux avec ce relais ». Conception v5, l. 232 (mot 4) : l'arrêt n° 13 est levé « si le relais montre un refus pour crédit ».

**Texte scellé touché.** V9 l. 384, arrêt n° 13 : « refus pour crédit […] sur l'une des trois clés du premier relais avant que sa part soit atteinte […] arrêt de la course, nommé, qui dit la clé ». La lettre n'est pas tenue : l'arrêt ne peut pas se lever.

**Options.**

| option | avantage | inconvénient | effort |
|---|---|---|---|
| (a) Relais v3 qui expose le statut de l'amont (code de retour et type d'erreur de la dernière réponse, compte des refus d'amont pour crédit) ; la surcharge le lit | lettre de l'arrêt n° 13 tenue ; marche avec l'outil comme sans lui | nouvelle pièce épinglée (lanceur L9 l. 515 épingle le relais v2) ; épreuve du faux fournisseur « crédit d'amont » | 2 à 3 h, plus la vérification |
| (b) Avec l'adaptateur direct du nœud 1 (b) : l'erreur d'amont arrive telle quelle à l'adaptateur (type d'erreur de facturation), qui la lève en arrêt n° 13 | aucun relais neuf ; aucun message fabriqué par l'outil ; aucune relance cachée | ne vaut que si le nœud 1 prend (b) | compris dans le lot 4 v2 |
| (c) Règle prudente sans code d'amont : toute « cause non établie » sur une clé Claude arrête la course par le n° 13 | simple | arrête aussi sur une erreur d'accès passagère ; c'est un écart à la lettre du n° 13 et au mot 4 de la conception (course continuée) | 1 h ; écart à déclarer |

**Recommandation : (b) si le nœud 1 prend (b), sinon (a). Confiance moyenne à bonne.** (c) seulement comme repli écrit, déclaré à l'additif, et jamais en silence. Dans tous les cas, l'additif écrit que le message fabriqué par l'outil (`<synthetic>`) n'est **jamais** un refus de classifieur et ne déclenche **jamais** le repli du point 5.

## 3. La séparation par processus (lot 6) n'est pas écrite

**Énoncé, source.** Réserve du lot 6 v3, l. 5 à 11 : quatre contournements « supposent qu'un code modifie le programme en marche » (classe du journal modifiée avant l'import, `depart` remplacé, `Colonne.examiner_octets` vidée, `__code__` échangé). La mère a décidé : « La parade retenue est la **séparation par processus** […] Elle est prévue au lot suivant […] D'ici là, cette réserve accompagne toute course qui ferait tourner du code d'organisme dans le même interpréteur que le journal » (l. 11). La vérification du lot 6 v3 (l. 24 et 65) propose un contrôle d'empreinte du code chargé. L'inventaire (l. 57) dit la séparation non écrite. Aucun lot 7 ni 8 n'existe.

**Texte scellé touché.** Aucun des textes de la course que j'ai lus n'écrit cette parade. La V9 l. 368 (« Chaque garde est éprouvée sur un cas sain et sur un artefact […] aucun repli silencieux ») vaut pour la garde du journal de la colonne. Je n'ai pas lu l'additif de la matière première, que la consigne m'interdit, et je ne peux donc pas dire s'il touche ce point. Le lot se déclare à l'additif du véhicule (valeur et réserve). Une remarque : la V9 l. 392 (arrêt n° 21) dit que cette course n'exécute aucun procédé, donc aucun code rendu par un modèle. Le code qui tourne dans l'interpréteur est celui de l'orchestrateur et des lots, épinglé par empreinte.

**Options.**

| option | avantage | inconvénient | effort |
|---|---|---|---|
| (a) Séparation par processus, comme décidé : le journal (et la colonne) tient dans un processus parent ; l'orchestrateur tourne dans un sous-processus sans droit d'écriture sur le journal, qui ne lui parle que par un tube et un protocole fermé | ferme les quatre contournements par construction | gros changement du lot 6 (v4) et du lanceur (lot 8) ; nouvelle chaîne d'essais | 6 à 10 h |
| (b) Contrôle d'empreinte du code chargé, au départ et à chaque génération : l'empreinte de chaque module importé (`sys.modules`, fichiers sources) comparée à la table du paquet, et aucun import après le départ | peu coûteux ; il attrape la modification d'un fichier et l'import non prévu | ne voit pas une modification en mémoire (`__code__`), c'est-à-dire les cas 3 et 4 ; ne vaut que parce qu'aucun code de modèle ne s'exécute (n° 21) | 2 h |
| (c) Garder la réserve telle quelle, déclarée à l'additif, avec la constatation qu'aucun code de modèle ne s'exécute dans cette course | aucun délai | la réserve accompagne la course ; tout contournement reste ouvert si un code tiers entre dans l'interpréteur | 0,5 h |

**Recommandation : (b) plus (c) pour cette course, et (a) pour la première course qui exécute du code d'organisme. Confiance moyenne.** C'est un écart à la décision de la mère (« prévue au lot suivant »), à lui soumettre. Il est motivé par le n° 21 : le modèle de menace que la mère nomme (« code écrit par un organisme ») est sans objet ici si le lanceur refuse tout import hors table.

## 4. L'état du lot de la règle d'appels Google

**Énoncé, source.**
- La règle : `M/CLAUDE.md` l. 66-67 (GO-2026-11-21-71). Elle impose, avant tout envoi à un modèle de Google, une réflexion explicite dans le corps, un plafond d'au moins réflexion plus 16 000 jetons, et une limite de mots tenue. Après la réponse, une absence de jeton de pensée, une fin MAX_TOKENS, SAFETY ou RECITATION, ou un texte vide valent défaut journalisé. La règle ajoute : « Une garde commune vit dans `src/controle_ia/` ».
- La décision : `M/registres/decisions.md` l. 4794 (R-4655) : « corrections de la règle Google en lot neuf contre-lu, périmètre : orchestrateur v56 copié, lots 2 à 5 et 10 a, plus un audit à part de commande_argon_v56_nuit_v6.py et du relais Google local ».
- **État constaté** :
  - Deux audits existent, en lecture seule, verdict « non tenue » (B/audit-regle-appels-google-v1/, les deux pièces). Celui de l'orchestrateur et des lots relève (l. 30) que `adaptateurs.py` l. 712 accepte un texte vide et rend « ok ». Il propose, § 3, des fichiers neufs : `routage_na_v2.py`, `appel_garde_na_v2.py`, `portier_na_v2.py`, `requete_na_v4.py`, `adaptateur_commande_google_v68.py`, `adaptateur_kimi_v54.py`.
  - La garde commune existe désormais sur `main` : `src/controle_ia/garde_google_v1.py` à `_v3.py` (R-4664 l. 4803, R-4686 l. 4825). La v3 fixe le rapport jetons par mot par espèce. Les audits la disaient absente : c'est un fait antérieur à son écriture.
  - **Le lot neuf des corrections du véhicule n'est pas trouvé** : ni sur la branche (dossier B, aucun dossier de lot Google), ni dans le registre (aucune ligne après R-4655 qui le livre).
- Le véhicule route trois rôles vers le deuxième relais (Google) : le juge de l'espèce 1 et les proposeurs des espèces 1 et 5 (complément l. 138). La règle s'applique donc à cette course.

**Textes scellés touchés.**
- V9 l. 383 et complément l. 166 : « Le pire d'un appel de proposeur est de 6,05 USD ». Sous la règle, le plafond de sortie d'un appel Google doit atteindre réflexion plus 16 000 jetons. Que 6,05 USD borne encore un tel appel n'est pas établi ; c'est à mesurer.
- Devis l. 406-438 et complément l. 138 : la part du deuxième relais (140,39 USD) est son cas haut, chiffré sur la course v9 sans ces réglages. Le cas haut peut monter. La part reste fixée, mais l'arrêt n° 12 étendu l'arrêterait plus tôt.
- V9 l. 99, classe « réponse illisible » : une réponse Google sans pensée ou en fin MAX_TOKENS devient « défaut journalisé, jamais une réponse ». Il faut écrire à l'additif dans quelle classe M6 elle tombe (je propose « réponse illisible », sous-compte « défaut de la règle Google »).

**Options.**

| option | avantage | inconvénient | effort |
|---|---|---|---|
| (a) Le lot neuf de R-4655, au périmètre de l'audit, qui emploie `garde_google_v3` (et non une copie) au point avant envoi (lot 3 v4) et après la réponse (lot 4 v2, lot 5 v2), plus une commande Google v7 qui emploie la même garde sur le corps réel et rend en écho réflexion, plafond, raison de fin et jetons de pensée | règle tenue, garde unique, contre-lue | le plus long ; dépend de l'audit de la commande | 5 à 8 h, plus la contre-lecture |
| (b) Refuser au véhicule toute clé Google tant que le lot n'est pas livré | sûr | retire trois rôles : la composition n'est plus celle de la V9 (arrêt n° 2, version neuve) | — |
| (c) Garde au seul lanceur (lot 8), sur la configuration | rapide | ne voit ni le corps ni la réponse : E1, E2 et E4 restent non tenues (audit, § 2) | 2 h, insuffisant |

**Recommandation : (a), confiance bonne.** Faire porter ce lot par le même lot 4 v2 que le repli (point 5) : les deux touchent `_apres_retour_na`. Mesurer le pire d'un appel Google sous les réglages de la garde avant l'additif, et l'y écrire.

---

## 5. La règle de repli neuve (GO-2026-11-22-35)

**Le mot** (`M/registres/go.md` l. 722) : « un appel Claude refusé par un classifieur de sûreté (raison d'arrêt refusal) est rejoué une fois sur claude-opus-4-6, puis, s'il est encore refusé, sur claude-sonnet-4-6 ; chaque repli consigné par appel (modèle demandé, modèle servi, catégorie du refus), compté dans le devis, rapporté à part dans les résultats ; écart déclaré aux textes scellés de la course, accordé par Lazar ». Montant : « dans GO-2026-11-21-30 ». Aucune ligne du registre des décisions ne l'applique encore (inventaire, l. 23).

### 5.1 Écarts aux textes scellés, à écrire dans l'additif

L'additif ne doit nommer les deux modèles que par leur rôle (« premier modèle de repli », « second modèle de repli ») et renvoyer à GO-35. Les textes de la course n'écrivent aucun identifiant de modèle (V9 l. 51 ; complément l. 11).

| n° | texte et ligne | lettre scellée | ce que l'additif écrit |
|---|---|---|---|
| R1 | **V9 l. 372**, arrêt n° 1 | « refus d'un classifieur de sûreté | le tour s'arrête ; consigné tel quel ; **non relancé** ; une reformulation plus étroite seulement sur le mot de Lazar (R-609) » | Un appel Claude dont la raison d'arrêt est « refusal » est rejoué, **à requête identique à l'octet** (même empreinte, aucune reformulation), une fois sur le premier modèle de repli, puis une fois sur le second. L'arrêt n° 1 se lève seulement si les trois tentatives sont refusées, avec sa portée inchangée (« appel » par défaut, D8 en attente : rapport du lot 4, l. 137). Une reformulation reste interdite sans le mot de Lazar. |
| R2 | V9 l. 98, classe « refus du modèle » | « non relancée, sans reformulation ; distincte de l'arrêt n° 1 » | **Inchangée** : un refus en prose, sans raison d'arrêt « refusal », n'est jamais rejoué. Le repli ne vaut que pour la raison d'arrêt du fournisseur. |
| R3 | V9 l. 99, classe « réponse illisible » ; rapport du lot 4, l. 125 | « non relancée » | **Inchangée** : le message fabriqué par l'outil (`<synthetic>`), le crédit, l'accès et la réponse coupée ne sont jamais rejoués par le repli. |
| R4 | V9 l. 383, arrêt n° 12 | pire par appel de 6,05 USD (proposeur), pire de l'aiguilleur et du juge écrit au complément ; « **aucune bascule** vers une autre clé » | Chaque tentative de repli est un appel neuf **sur la même clé**, qui repasse l'arrêt n° 12 avec le pire du modèle de repli (je propose de garder 6,05 USD et le pire écrit au complément, sans le baisser au tarif plus bas des modèles de repli). Le repli n'est pas une bascule de clé. Une tentative qui dépasserait la part lève le n° 12, non le n° 1. |
| R5 | V9 l. 77 et l. 387, requête journalisée et garde de motifs | journalisation « avant chaque envoi » ; « après elle, plus aucun octet ne change » | Chaque tentative écrit sa propre ligne « envoi » au journal (même empreinte, rang neuf, modèle demandé), repasse la garde et l'égalité. Le journal v3 est fermé à quatre événements (vérification du lot 4, l. 92) : il faut un champ neuf ou un journal v4. |
| R6 | V9 l. 156, M4 (coût) | coût par espèce et par rôle | Le coût des tentatives, refusées comprises, s'ajoute au rôle et à l'espèce de l'appel d'origine. Il est **aussi** rapporté à part : par rôle, clé, génération, modèle demandé, modèle servi, catégorie, coût. |
| R7 | V9, section « Plan d'analyse » et mesures M1 à M6 (l. 150-160) | mesures gelées | Mesure descriptive neuve, « replis » (comptes et coûts par rôle et par modèle). Toute fiche obtenue par repli porte une marque. Les mesures M1 à M6 sont rapportées deux fois : toutes fiches, et fiches sans repli. C'est un écart déclaré : aucune lecture n'est changée, une colonne s'ajoute. |
| R8 | V9, définition des espèces (espèces 3 et 4 : un modèle Claude chacune ; l. 51) ; additif 1 | une espèce, un modèle | Une fiche rendue par un modèle de repli reste comptée à l'espèce du rôle et marquée « servie par repli ». C'est un **point pour la mère** : à défaut, elle peut l'exclure des mesures de l'espèce. Je recommande « comptée et marquée », pour que le volume ne baisse pas en silence. |
| R9 | V9 l. 271 (paragraphe retiré, dont la règle « un refus d'un classifieur de sûreté, l'arrêt n° 1 ») ; additif 1 l. 118, arrêt n° 27 ; complément l. 120-132, lignes à part | à la sonde de refus et à l'épreuve des témoins, refus de classifieur = arrêt n° 1 | **Point pour la mère** : le repli vaut-il aux lignes à part ? Je recommande **oui, avec la même consignation**, pour que la sonde mesure ce que la course fera. L'issue de la sonde est alors rendue « acceptante au modèle demandé » ou « acceptante par repli », et la seconde ne vaut départ que sur le mot de la mère. Coût compris dans les 6 USD (complément l. 132). |
| R10 | Devis, cas haut par rôle (l. 406 : Luc 124,35 ; l. 405 : juge 3 105,05) et plafond total 456 (l. 386) ; GO-30 « aucune recharge supposée » | aucun repli au devis | Le repli n'ajoute aucun montant : il est compté **dans** la ligne de 450 USD et dans les parts (GO-35 : « dans GO-2026-11-21-30 »). Le devis final (V9 l. 410, point 9) ajoute une ligne « replis » : pire d'une chaîne = trois pires d'appel, soit 18,15 USD pour un proposeur (sortie du programme `recalcul_part_luc_v1.py`, clé `repli_GO_35`). Il dit que la marge de Luc (1,28 USD au-dessus du cas haut) ne couvre aucune chaîne entière. |
| R11 | Complément l. 166 et additif au complément l. 72 | pire d'un appel de proposeur 6,05 USD | Inchangé, et écrit comme pire de **chaque** tentative de repli. |
| R12 | Conception v5 (non scellée) : contrôle A2 « modèle servi changé », configuration `a11_modeles: []` (lot 6 `configuration_course_na_v1.py` l. 265, 281 : « la liste des modèles sous garde de bascule est vide ») | composition gelée, un modèle servi par rôle | À l'additif : A2 admet, pour une tentative de repli, le seul modèle de repli demandé à cette tentative. Le modèle servi d'origine reste celui du rôle pour l'appel suivant. Le repli propre de l'outil ou du kit (événement `system.model_refusal_fallback`) reste refusé : le repli est celui du véhicule, visible et consigné. |

### 5.2 Changements de code

Lot 4 v2 (fichiers neufs, R12), puis vérification S neuve :

1. **`appel_garde_na_v2.py`** (copie de `appel_garde_na_v1.py`, `d16d07bf…`) :
   - l. 71-76 : séparer les listes. Un refus « refusal » d'une clé Claude (événements `assistant.stop_reason`, `result.stop_reason`) ouvre le repli. `commande.refus` et `kimi.content_filter` (autres fournisseurs) gardent l'arrêt n° 1 sans repli. `system.model_refusal_fallback` (repli de l'outil) passe à A2, « repli non permis ». `system.model_fallback` reste A2 (l. 71).
   - `appel` (l. 327-402) : une boucle sur la suite fermée (modèle du rôle, premier repli, second repli). Chaque tour repasse les pas 2 à 6 : la part avec le pire de la tentative (`rt.verifier_part`), la garde et une ligne « envoi » neuve, l'égalité, `super().appel(..., modele=<tentative>)`, le coût au cumul. La boucle s'arrête au premier statut autre que « refus de classifieur ». Aucun rejeu caché dans l'adaptateur.
   - `_apres_retour_na` (l. 404-445) : à la branche « refus » (l. 420-428), si la tentative n'est pas la dernière, rendre « repli demandé » au lieu de compter l'arrêt n° 1 ; après la troisième, compter le n° 1 comme aujourd'hui. Le contrôle A2 (l. 411-414) admet `servi == modèle demandé de la tentative` pour une tentative de repli, sans changer `na_servis[role]`.
   - Compte et journal neufs `na_replis` : une ligne par tentative (rôle, clé par nom d'usage au seul journal des arrêts, génération, case, session, rang d'envoi, modèle demandé, modèle servi, catégorie, coût, issue). Ils sont rendus à la ligne de la génération (lot 6) et à la mesure « replis » (lot 7).
   - La catégorie : si l'adaptateur ne la rend pas, la ligne porte « catégorie non lue », jamais un vide silencieux.
   - `ContexteAppelGardeNA` : `pires_par_role` devient un pire par (rôle, modèle), avec un refus si un modèle de repli n'a pas de pire.
2. **Adaptateur Claude v2** (`adaptateur_claude_na_v2.py`, copie de `38baa206…`) :
   - l. 111 : `verifier_modele_reel(modele)` (fonction du kit, `adaptateurs.py` de l'orchestrateur a41b7b50, non présent ici) doit admettre les deux identifiants de repli, et eux seuls en plus des modèles des rôles.
   - l. 56 : `construire_options` garde « aucun repli de modèle » (docstring l. 10) : le kit ne replie pas lui-même.
   - La catégorie (champ de détail du refus du fournisseur) est conservée dans la réponse brute (l. 125-127) et rendue dans `refus`.
   - Si le nœud 1 prend (b), l'adaptateur direct lit directement la raison d'arrêt et sa catégorie.
3. **Faux fournisseur v2** : un refus de classifieur programmable **par modèle demandé**, pour éprouver les chaînes.
4. **Relais** (`pole/relais_reel_v2.py`, épinglé par L9 l. 515) : la liste des modèles permis et le barème doivent porter les deux modèles de repli, à leur tarif, relu sur la page du fournisseur et versé (règle R7 par analogie). Sinon le relais refuse par `refus_modele`, ou compte au mauvais tarif.
5. **Lot 5** : le portier et le juge de l'espèce 3 sont des appels Claude. Le repli les couvre par la même surcharge, sans code neuf, sauf la marque « par repli » sur le verdict (portier v2 si la marque doit entrer dans ses comptes).
6. **Lot 6 v4** :
   - `configuration_course_na_v1.py` l. 265 et 281 : un champ neuf, distinct de `a11_modeles` (qui reste vide et inerte), « modèles de repli » par clé Claude, à la liste fermée de GO-35 ;
   - la ligne de génération porte les comptes de repli, rapportés à part ;
   - la simulation joue une chaîne refusée ;
   - nouvelle table d'empreintes.
7. **Lots 7, 8 et 9** :
   - mesure « replis » et double rapport M1 à M6 (lot 7) ;
   - modèles permis dans l'environnement réduit et dans l'épinglage, et contrôle au départ que la somme des pires d'une chaîne n'est pas sous-comptée (lot 8) ;
   - épreuves R5 (lot 9). Cas sain : refus au modèle demandé, repli servi, ligne consignée. Artefacts : trois refus donnent l'arrêt n° 1 ; un modèle servi autre que celui de repli demandé donne A2 ; le message `<synthetic>` ne déclenche aucun repli ; une tentative qui dépasse la part d'un centime donne le n° 12 ; un refus Kimi ou par commande ne déclenche aucun repli ; une reformulation (empreinte différente) est refusée ; un repli de l'outil (`system.model_refusal_fallback`) donne A2.

### 5.3 Ce que je laisse à la mère

R8 (attribution d'une fiche servie par repli) ; R9 (repli aux lignes à part) ; le pire retenu par tentative (R4 : 6,05 USD gardés, ou le repère plus bas des modèles de repli, 3,38 et 2,03 USD, non relus) ; et, avec le nœud B, ce que devient la marge de 1,28 USD de Luc sous le repli.

— auteur Opus, 2026-11-22

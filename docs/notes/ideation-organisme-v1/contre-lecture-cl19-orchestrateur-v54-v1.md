# Contre-lecture CL19 — orchestrateur du pôle v54, course 2 et pré-pilote (R2)

- Auteur : sous-agent Sonnet 5.5 neuf (`claude-sonnet-5-5`). Je n'ai écrit aucune ligne des versions 53 et 54.
- Date : 2026-10-31, 03:00 UTC (relevé à 03:58 heure de Paris).
- Objet : `docs/notes/ideation-organisme-v1/orchestrateur-v54/`.
  - Liste d'empreintes `284eb4a6a040108bf3d3b3b31ca8e797da119f72e497e68f07b90d8b4a0ab3c3` (387 fichiers) : `sha256sum -c` donne 387 OK **avant** mes essais et **après** (0 écart).
  - `LISEZMOI-orchestrateur-pole-v7-v54.md` `a3290bc7237057af11dd8a320d631b73293ffb41e55aef65e11f0b90ff79beb2`.
  - `CODE-orchestrateur-pole-v7-v54.zip` `001b8fc96ede33dcda26b9e74f2301687e2a97780b67cd976b66323409584967` (165 fichiers, tous identiques à l'arbre).
  - Modules lus en entier (début d'empreinte) : `noyau_v54` 711a3267…, `course2_v54` ac1980d0…, `prepilote_v54` 77056684…, `gardes_e0_v54` 83b54b81…, `configuration_v54` 3424ca7f…, `budget_v54` 220d25e6…, `bisociateur_v54` 20d938b2…, `suivi_roles_v54` 62022597…, `fiches_v54` 1ab0796d…, `mesures_v54` 8f3f57fc…, `etage_entre_generations_v54` 86a6bec0…, `bras_attaque_v54` a4a70be0…, `ideation_v6` 4c302e5b… ; `simulation_v54` de223292… lu en diagonale ; `conftest`, `mutations_v54`, `test_v54_*`, `aides_v54` lus.
- Spécification confrontée : brouillon 7 du pré-pilote `799b9ca9c4ec30d8ab2c782496643b64cdbfcd8ca09eb08b9b8694b0c8ece6f5` (compagnon conforme) ; annexe du bras méta, brouillon 1, `3a2e8dc2f8d764674941498ab0da9a977e7cbbd1478d868428efb8d1ca3441a0` ; contre-lecture de l'annexe `db249b9356f8d19cd8c9811c3db184b0d7587eba97ed8386501e146434e24f1d` ; CL18 `0ce1d0b5a8c5016fdcb7262db3597bcc0320ddcd884dfb3d8821fa467230c52b` ; registre `registres/go.md` (lu pour ses libellés, pas pour un secret).
- Interdits tenus : rien lu sous `donnees/` ; aucun appel payant ni réseau (tous mes essais sous `unshare -n`, boucle locale levée par un petit programme à moi, faute de commande `ip`) ; aucune clé ni aucun jeton lu ; rien committé ; aucun fichier existant modifié ; aucun `.sha256` écrit (les compagnons de mes essais d'annexe sont dans `/tmp`, hors dépôt). Mes outils sont dans `/tmp/cl19/` (hors dépôt, non versés) : `lo.py` da9bd504…, `go_probe.py` 89f70a1a…, `probe_e0.py` d2cf58d7…, `probe_noeud.py` 5d6b4f6c…, `mut_raison.py` e6ed65c3…, `dep3.py` fd36190b…, `annexe.py` 556e6e05…, `s6.py` 90ba5e3f…, `probe_taches.py` 8a71a2ec…
- Niveau méthode seulement. Pas lu : les modules hérités de la version 53 (sauf les passages cités), `ideation_v4.py` et `ideation_v5.py` (le lanceur 6 les charge tels quels), aucun moteur réel, aucun essai sous `unshare -rn`.

## Verdict global

**Lançable après corrections.**

Pour la course 2 (une ou plusieurs générations) : trois corrections de code courtes (CL19-01, CL19-02, CL19-04), puis gel des seuils.
Pour le pré-pilote complet : en plus, une décision de Lazar sur la règle de non-lecture (CL19-03), les corrections CL19-05 à CL19-08, et les pièces manquantes de la section G. Le code d'analyse n'existe pas encore (déclaré).

Ce qui tient, et que j'ai vérifié moi-même : le journal de consommation est complet et rejouable sur la vraie sortie du code (CL18-01) ; le nœud arrête bien la génération et la course (CL18-02) ; la ligne de GO exige un montant exact (réserve CL19-05) ; les 56 mutations sont tuées ; la suite donne exactement les comptes annoncés ; l'annexe réelle est refusée puis la copie remplie acceptée, avec 5 / 36 / 4 et l'argmax e01–e04. Les défauts sont aux bords : ce que le code fait **après** un nœud, ce qu'il fait quand une source manque, et la voie par laquelle la clé des classes est lue.

## A. CL18-01 à CL18-17

| Constat | Verdict | Preuve (fichier, ligne ou essai rejoué) |
|---|---|---|
| 01 journal complet | **tenu** | `noyau_v54.py:84-120` : une consommation par appel dans un `finally`, pire cas si l'adaptateur lève. `test_v54_corrections.py:61-121` compare le journal à la sortie réelle du moteur (`Comptant` garde chaque appel) et rejoue `rejouer_consommations` sur `g.coffre.consommations()`, pas sur des nombres écrits à la main. Mutation « juge omis » : les essais échouent avec « 48 != 81 » et « 6 != 15 » (comptes réels). Réserve : `jetons` est écrit « non lus » (`noyau_v54.py:112`) alors que la mesure M7 du brouillon 7 demande les jetons : dit dans le code, absent du LISEZMOI. |
| 02 coupure et nœud | **tenu** pour ce qui est joué ; **à corriger** pour ce qui suit le nœud | `budget_v54.py:31-54`, `noyau_v54.py:122-154`. Essai `…artefact_protegee_coupee…` : étape « non mesurée », aucune génération 2, rien lancé après. Mais après un nœud, le code déclare quand même la fin d'É9 et ouvre les verdicts et la clé (CL19-02). |
| 03 ligne de GO | **tenu avec réserve** | Rejoué sur `registres/go.md` réel (S17 = 45, date 2026-11-02) : `GO-2026-10-20-06` (« 150 USD, plafond de … inchangé ») refusée pour 45 (« pas exactement ») ; `GO-2026-10-20-07` (« 10 USD par lancement, dans les 150 USD de … ») refusée pour 45, 10 et 150 (« plusieurs montants ») ; `GO-2026-10-04-08`, `-17-01`, `-20-11` hors validité ; identifiants `…-066`, `…-6`, minuscules, espace final, `…-0` refusés (`GO_ID.fullmatch`). Cellules reconstituées : « 45 USD par lancement/run », « 45 EUR », « 45 € », « 45 USD (alerte à 36 USD) », « 45 USD ou 45 dollars », « 45 USD, dans les 150 USD de GO-… », « USD 45 », « $45 », « — » : toutes refusées. **Acceptées à tort** : « 1 045 USD » (lu 45), « 10-45 USD » (lu 45), « ≈ 45 USD » : CL19-05. |
| 04 pré-pilote jouable | **à corriger** | Le plan É1–É9b est codé et joué (essai sain : 13 étapes « jouée »). Mais deux défauts de fond : source absente refusée au lieu d'être déclarée (CL19-01) et lecture des verdicts après un nœud (CL19-02). |
| 05 passeport | **tenu** | `noyau_v54.py:256-258` recalcule l'empreinte ; mutation tuée (« True is not false »). |
| 06 A4 (étiquettes) | **tenu avec réserve** | Mode `prefixe` : « témoins », « fusions », « exploratoire » attrapés ; « témoignage », « fusée » non. Réserve : « bisociative » échappe à « bisociation » (liste injectée, dit au code). |
| 07 noms de tâches | **tenu avec réserve** | `pp2-classes-axes`, `-indices`, `-fournisseurs`, `-partition`, `-bisoc-ordre/-gk/-meta/-n`, `-reduction-e9` présents dans un run sain. **Non déclarés** : `pp2-ident-fond-<n>`, `pp2-ident-<passe>-<case>-<proposeur>-<k>`, `pp2-ident-fusion-<n>` et `pp2-anonymisation-<juge>-<fiche>` (le brouillon liste `pp2-anonymisation` seul) ; seul `pp2-paraphrases` est déclaré (CL19-10). |
| 08 entrée du bisociateur ; passe « tableau » jugée | **tenu** | Clés `bisociateur.fournisseurs_entree` et `tableau.juger_passe_tableau` sans défaut ; mutations tuées. |
| 09 brouillon 6 cité | **tenu avec réserve** | Un seul fichier cité (brouillon 7, empreinte égale à la constante). L'empreinte n'est contrôlée que par un essai, pas au lancement. DEP4 : seule la présence d'une pièce empreintée est exigée, pas son contenu (CL19-05). |
| 10 garde de Kimi | **tenu** | Deux clés configurables, essais des deux valeurs. |
| 11 plafond par génération | **tenu** | `montant_requis`, deux portées, essai. |
| 12 fuites par les chemins | **tenu avec réserve** | Dossiers de session hachés (16 caractères) ; nature « concepts / vocabulaire / niches » ; A4 sur l'entrée complète pour juges, aiguilleur, lecteurs, relecteur, paraphrases. **Mais** `sessions/` est voisin de `coffre/`, `temoins/`, `aiguillage/` : CL19-04. |
| 13 machine jetable | **tenu avec réserve** | Seuls les noms sont lus (voir D). Faux positif `TOKENIZERS_PARALLELISM`, trous `GH_PAT`, `*_KEY_FILE`, `SSH_AUTH_SOCK` : CL19-11. |
| 14 kappas dégénérés | **tenu** | Rendent `None` ; verdict absent retiré et compté. |
| 15 essais | **tenu** | Trois essais ajoutés ; `conftest.py` redirige les dossiers temporaires (vérifié : après la suite, ni `essais/_tmp` ni `__pycache__`). |
| 16 cumul écrêté ; M6b coupée | **tenu** | Cumul réel, dépassement au journal ; M6b coupée → « non mesurée hors porte », C13 inchangée. |
| 17 héritage ; n par case ; départage | **tenu** | Essais ; mutations tuées. |

Bilan : 9 tenus, 1 tenu sauf après un nœud (02), 6 tenus avec réserve, 1 à corriger (04, qui porte CL19-01 et CL19-02).

## B. Annexe du bras méta : I-1 à I-13

Rejeu par moi (`/tmp/cl19/annexe.py`, copies dans `/tmp`) :
- Brouillon 1 réel, tel quel : refusé (« A20 : annexe sans contre_lecture déclarée »). Avec seule la contre-lecture remplie : refusé (« sans approbation_lazar »). Empreinte injectée fausse : refusé.
- Copie remplie (deux empreintes, `R-999`) : acceptée. Non-vacuité recalculée par la fonction réelle : **5 paires dans le profil, 36 hors profil, 4 de même niche, argmax `e01`–`e04` à 2,0**. Les quatre paires de niches du profil sont celles de CA1 (n1–n2, n1–n4, n1–n6, n3–n4).

| Point | Verdict | Preuve |
|---|---|---|
| I-1 noms de structures | **tenu** | `bisociateur_v54.py:121-146` : identifiant de la liste et nom = identifiant ; refus compté (`refus_lectures`). Conséquence à savoir : un seul nom déviant fait perdre la fiche au bras méta pour ce lecteur (n effectif réduit, que P14 ne chiffre pas). |
| I-2 désaccord | **tenu avec réserve** | Lu après le dépôt des paires, deux lecteurs, journal au coffre, ordre vérifié, garde par valeur (`triche_kw` tué). Réserves : au plus `paires_max` paires (le brouillon 7 dit « chaque paire candidate », CA1-10 ; à trancher) ; le texte servi est le champ de la fiche (`champ_affirmation`), pas la recopie du lecteur, qui est conservée mais non utilisée ; la vérification d'ordre est vraie par construction dans le code (seul l'artefact simulé l'éprouve). |
| I-3 S28 | **tenu** | `accord_s28`, seuils de l'annexe ou de la configuration. À marges constantes, kappa lu 1 ou 0 et `degenere` vrai (règle du brouillon 7) ; `marque` reste vide dans ce cas, la réserve « dégénérée » ne porte que sur l'indicateur. |
| I-4 définitions | **tenu** | Deux modes ; vérifiés ; mutations tuées. |
| I-5 divergence | **tenu** | Configurable, deux valeurs. |
| I-6 types et signes | **tenu** | Poids négatif et table non numérique refusés avec le motif « I-6 » (voir E). |
| I-7 causes de C12 | **tenu avec réserve** | Cause « niches indistinctes » comptée. Les causes (iii) et (iv) du brouillon 7 (« moins de 2 fiches notables / étiquetées ») sortent « aucune paire éligible » : même effet, libellé différent (CL19-10). |
| I-8 n = 2 | **tenu** | Bras de priorité 1 seul ; `verifier_paires_globales`. |
| I-9 contre-lecture et approbation | **tenu avec réserve** | Deux empreintes distinctes et `R-NNN` exigés. Passent : `000…0` et `111…1` comme « empreintes », `R-000`. La vérification annoncée par l'annexe § 9.5 (« différence limitée à ces lignes ») n'est pas codée (CL19-09). |
| I-10 non-vacuité à É0 | **tenu** | Rejouée par `verifier_non_vacuite`, motif exact vérifié. |
| I-11 paires déjà prises | **non traité, non revendiqué** | `choisir_paires_v54` retire toujours les paires prises (`prises`), P14 ne le chiffre pas. À traiter dans l'annexe version 2 ou dans le script de puissance. |
| I-12 artefact d'ordre | **tenu** | `verifier_ordre_desaccord` + essai. |
| I-13 dépense du désaccord | **non traité, non revendiqué** | Les appels passent par l'étape protégée `etiquettes`, donc dans le plafond et le journal ; mais le tableau de coûts du brouillon 7 (É7b : 0,75 attendu, 1,0 de plafond) ne les contient pas. À chiffrer au devis. |

CA1-01 à CA1-15 (grille, tables, loi a priori) sont des constats sur l'annexe, pas sur le code : aucun n'est corrigé ici, aucun n'est revendiqué.

## C. Fidélité au brouillon 7

| Étape | Verdict | Remarque |
|---|---|---|
| É0 | **à corriger** | Rejeu de la table en mémoire avant tout appel, `--verifier-seulement` compris (`ideation_v6.py:85-86`) : tenu. Mais A19 est refusé (CL19-01), et les lignes 21 et 22b sont « rejouées » sans l'artefact de la table (CL19-08). |
| É1 | tenu avec réserve | 28 squelettes et déclarations, plan R9, contrôles par programme. Les 8 fiches d'antériorité et les 4 de M6b sont lues comme **pièces** (le brouillon dit « rédacteur, É1 ») : cohérent avec « pièces à produire » du LISEZMOI, mais le coût d'É1 du brouillon les comprend. |
| É2 | tenu | |
| É3 | tenu avec réserve | Consigne neutre, S6, A8, une reprise, A5. S6 par sous-chaîne : CL19-07. L'entrée de rendu n'est gardée contre A4 que sur le squelette, pas sur la consigne. |
| É4 | tenu | Aiguilleur sur rendus, difficiles, passe 1 ; second lecteur. Les 12 concrets : refus nommé (DEP5). |
| É5 | **décision de Lazar** | Voir plus bas (A21). Le nœud É5bis est un refus avec motif exact. |
| É6 | tenu | Un appel par fiche, identifiant servi propre à chaque juge, A13 sur l'empreinte du témoin. |
| É7a–É7d | tenu | Adjudicateur sur les désaccords des deux passes ; fusions : A2 contrôlé entre É6 et É7c (`modele_servi_juges` conservé d'un lot à l'autre). |
| É8 | tenu | Paraphrases, partition, PB / NA / NB ; t* laissé à l'analyse. |
| É9, É9b | tenu avec réserve | Réduction stratifiée : lit la clé d'antériorité (voir A21). Ligne 31 jouée sur les sources. |
| Fin de phase de mesure | **à corriger** | Après É9b : tenu. Après un **nœud** : déclarée quand même (CL19-02). |

**Refus de partir** (motif exact, aucun repli) :

| Refus | Verdict | Preuve |
|---|---|---|
| DEP3 | tenu | `EtageUnAbsent` dans `PrePiloteV54.__init__` et dans le lanceur. Le lanceur en ligne de commande n'a aucun moyen d'en injecter un : le pré-pilote ne part jamais depuis la ligne de commande (déclaré). |
| DEP5 | tenu | `prepilote.concrets` posé → `refuser_lots` ; non posé → M4 « non étalonné (sans témoins concrets) » écrit au manifeste de départ. C'est l'état prévu au défaut R-819, pas un repli silencieux. |
| Lignes R5 externes (6, 8, 9, 10, 17, 19) | **tenu avec réserve** | Refus « non rejouée » sans pièce. Avec pièce : seule la forme du JSON est contrôlée (`script_sha256` non vide, pas vérifié) : CL19-06. |
| É5bis | tenu avec réserve | Nœud « relancer avec `temoins.version = 2` » ; la version est un entier de configuration (rien n'empêche de le remettre à 1) : CL19-06. |
| A15 | tenu avec réserve | CL19-05. Les décisions et le montant sont contrôlés par le lanceur seulement : `PrePiloteV54` appelé directement n'en vérifie rien. |
| DEP4 | tenu avec réserve | Pièce empreintée exigée, contenu non lu. |

**Source Gu-Krenn absente (A19)** : voir CL19-01 — c'est le seul « refus » qui n'est pas voulu.

### A21 (non-lecture) : mon avis argumenté, pour Lazar

**Texte à comparer.** A21 : incident si « lecture d'un verdict d'É6 ou d'É7, **ou ouverture de la clé des classes** ou de la clé des bras, avant la fin d'É9, par quiconque ». Ligne 30 de la table : « jusqu'à la fin d'É9, seules les consommations sont lues ; les verdicts et **les clés restent scellés** ». Le Plan, lui, demande en É5, « avant tout juge » : témoins ambigus, S20 (plus de 4 ambigus sur 23, P primaires < 8, N primaires < 10), A6, contrôles S18 et S19, A7.

**Ce que fait le code.** `_boite_e5` (`prepilote_v54.py:411-464`) lit `self._cle_classes`, copie **en mémoire** de la clé déposée au coffre (`prepilote_v54.py:302`), pour compter les ambigus, les primaires, les défauts non vus et séparer P de N (S19). Seule la décision (passe ou nœud) et des comptes sortent, déposés au coffre. En É9, `etape_e9_anteriorite` lit les strates de la clé d'antériorité (`prepilote_v54.py:564`) pour tirer 4 fiches sur 8.

**Mon avis.**
1. **Contre la lettre : oui.** « Ouverture de la clé des classes avant la fin d'É9 » est exactement ce que fait É5, et la ligne 30 dit « clés scellées ». Le coffre refuserait cette lecture (`coffre_v53.py:57-62`, incident puis arrêt) ; le code la contourne en gardant une copie en mémoire. Résultat : le journal d'accès du coffre, que la ligne 30 invoque, **ne voit pas** cette lecture, et l'essai de la ligne 30 à É0 éprouve la garde du coffre, pas la voie réellement empruntée.
2. **Le brouillon se contredit lui-même.** Tel qu'écrit, É5 (S20, A6, S19, « avant tout juge ») est impossible sans connaître la classe de chaque témoin. Appliquer A21 à la lettre rend le Plan inexécutable ; appliquer le Plan viole A21. Ce n'est donc pas un choix de code de la v54, c'est un trou du brouillon 7 que la v54 a rendu visible.
3. **Compatible avec l'intention : oui, à trois conditions.** L'intention (CP5-08) : qu'aucune décision de l'orchestrateur ne dépende d'un **résultat** (verdict d'un juge, issue d'une fusion) ni du **rattachement d'un résultat à sa classe**. Les décisions d'É5 (A6, A7) sont des gardes sur la construction des témoins, prises avant tout juge ; elles ne dépendent d'aucun verdict. L'énoncé du Plan (« les décisions de sacrifice, de reprise et d'arrêt ne dépendent que des consommations et des gardes ») les couvre. Conditions : (a) le brouillon 8 écrit l'exception (« lecture par programme de la clé des classes à É5 pour S6, S18, S19, S20, A5 à A7 ; de la clé d'antériorité à É9 pour le tirage ; sortie limitée à la décision et à des comptes ; jamais par un agent ni une personne ») ; (b) la lecture passe par une méthode du coffre qui la **journalise** (par exemple `ouvrir_pour_garde(nom, raison)`), et l'artefact de la ligne 30 couvre aussi « lecture hors journal » ; (c) la sortie de la boîte ne contient aucun détail par témoin (le code actuel écrit `primaires_non_ambigus`, une liste d'identifiants **déjà triée par classe d'appartenance** : voir ci-dessous).
4. **Mieux que l'amendement : ne pas lire.** Pour É9, la clé d'antériorité n'a pas à être lue : la liste des 4 fiches réduites (stratifiée) peut être une pièce scellée écrite par session-depot avec le tirage `pp2-reduction-e9`, ou le tirage peut être simple. Pour É5, la boîte peut être un programme tenu par session-depot, qui détient la clé et rend « passe / nœud + comptes » : l'orchestrateur n'ouvre alors jamais la clé et A21 reste vrai à la lettre.
5. **Un effet de bord à connaître.** `etape_e6_juges` appelle d'abord les témoins « primaires non ambigus » (P et N), puis les autres (C, G, ambigus) : l'**ordre des appels** dépend de la classe. Les juges ne le voient pas (sessions isolées), mais si un juge est arrêté par A3 en cours d'étape, l'ensemble des fiches qu'il a jugées dépend de la classe. Faible, mais c'est une dépendance de décision (arrêt de rôle) à la clé que A21 interdit ; l'ordre devrait être tiré (graine) ou trié par identifiant.

**Recommandation (confiance 0,7).** Amender A21 et la ligne 30 dans le brouillon 8 comme en 3 (a)(b), supprimer la lecture de clé en É9 (4), corriger l'ordre d'É6 (5). Défaut si Lazar ne répond pas : conserver le comportement actuel, déclaré, avec le journal en (b) ajouté ; c'est le moindre écart.

## D. Fuites

| Question | Verdict | Preuve |
|---|---|---|
| Juges | tenu | Une fiche = un appel ; `exiger_passeport` avant chaque appel (`noyau_v54.py:180`) ; identifiant servi propre à chaque juge ; A4 sur la fiche puis sur l'entrée complète. |
| Lecteurs d'étiquettes, désaccord | tenu | Passeport exigé (`course2_v54.py:234, 355`) ; `servir` ; entrée de désaccord gardée. |
| Bras | tenu | Aucune consigne ne porte le nom d'un bras ; `NATURE` = « concepts / vocabulaire / niches » décrit la lecture, pas le bras. |
| Contenu « concret » jamais copié | tenu | `AiguilleurV54.journal` : identifiant, empreinte, classe, fournisseur, origine, « non copié » ; `exclues_a4`, `garde_kimi.refusees` : identifiants et classes seulement ; `fiches.json` et mémoire : fiches à passeport seulement ; `difficiles` jamais dans `ordre`. Les motifs d'événements (`str(e)[:200]`) ne portent que des noms de champs. Réserve v53 inchangée : les traces écrites par l'adaptateur réel dans le dossier de session ne sont pas vérifiées. |
| Dossiers de session opaques | **tenu pour les noms, pas pour l'emplacement** | `sessions/<16 caractères>` ; essai de fuite des noms. Mais `sortie/sessions/` est à côté de `coffre/`, `temoins/` et `aiguillage/` (liste de `sortie/` relevée sur un run sain) : un agent qui voit son dossier courant atteint `../../coffre/…` par chemin relatif. CL19-04. |
| Variable de machine jetable | tenu | `env.get("POLE_MACHINE_JETABLE_V54")` : seule valeur lue ; le reste par noms (`noms_de_cle_presents`, `nom_de_cle`) ; le message d'erreur ne cite que des noms. Dans le lanceur, `env.get("GO_ID")` (identifiant public). |
| Noms de variables refusés | tenu avec réserve | Refusés : `ANTHROPIC_API_KEY`, `AWS_ACCESS_KEY_ID`, `GOOGLE_APPLICATION_CREDENTIALS`, `DB_PASSWORD`, `MON_TOKEN`, `UNE_SSH_KEY`. Acceptés : `GH_PAT`, `OPENAI_KEY_FILE`, `SSH_AUTH_SOCK`, `AUTH`, `NPM_CONFIG__AUTH`. Refusé à tort : `TOKENIZERS_PARALLELISM`. Contrôle déclaratif, comme annoncé. |

## E. R5 et mutations

- `essais/mutations_v54.py` rejoué sous `unshare -n` : **témoin 64 essais, 0 en échec ; 56 mutations, 56 tuées, 0 survivante, 0 non appliquée ; témoin après restauration 64 essais, 0 en échec.**
- Critère de « tuée » du script : au moins un essai d'une classe visée échoue, sans regarder pourquoi. J'ai donc rejoué les 56 en imprimant, pour chacune, la nature de l'échec (`/tmp/cl19/mut_raison.py`, résultat gardé dans `/tmp/cl19/raison.txt`). Cinq mutations détaillées, pour la **bonne raison** :
  1. « CL18-01 consommation d'un juge omise » : `AssertionError: 48 != 81` (appels du moteur contre consommations notées) : bonne raison.
  2. « CL18-03 plusieurs montants acceptés » : la garde suivante (« par lancement ») prend le relais et refuse avec un autre motif ; l'essai échoue parce que son motif attendu (« plusieurs montants ») ne correspond pas : **tuée par le motif exact**, comme le LISEZMOI le dit.
  3. « I-6 tables non contrôlées » : l'essai attend « I-6 » et reçoit `'<=' not supported between 'str' and 'int'` : bonne raison.
  4. « I-10 profil vide accepté » : la garde suivante répond « une paire hors profil est choisie avant une paire du profil » ; l'essai attend « profil vide » : bonne raison.
  5. « A3 délai ignoré » : `NoeudArret not raised` et, à É0, « ligne 25 (ÉCHEC) » : bonne raison.
  Aussi vérifiées : A6 (`NoeudArret not raised` ×2), CL18-02 (marque de coupure), I-9 (trois sous-cas).
- **Une mutation est tuée pour une mauvaise raison** : « DEP3 analyseur non exigé ». Les trois essais visés échouent avec `RuntimeError: super(): __class__ cell not found` : la fonction recompilée n'a plus son `super()` sans argument. C'est un artefact du banc, pas la preuve de l'essai. Je l'ai refaite proprement (`/tmp/cl19/dep3.py`, `super(PrePiloteV54, self)` conservé) : seul `test_etage_1_absent_refus` échoue (`EtageUnAbsent not raised`) : la garde est bien éprouvée, mais le compte « 56 tuées » surestime d'une unité (CL19-08).
- **Ce qu'aucune mutation ne couvre** (donc ce que le banc ne dit pas) : la ligne 20 quand la source est absente (CL19-01), la lecture après nœud (CL19-02), la lecture d'une clé hors du coffre (CL19-03), le contrôle de `modele_servi` non lu, `paires_pour_desaccord`, la branche S18 du flux (dans l'essai sain il n'y a que 2 fiches de Kimi, S18 « non évaluée »), la reprise d'un rendu après A8.

## F. Rejeu de la suite

`POLE_ESSAI_BAC_REEL_NON_JOUE=1 python3 -B -m pytest essais -q -p no:cacheprovider`, sous `unshare -n` (boucle locale levée), superutilisateur, Python 3.13, `bwrap` absent :

- **Suite entière : 663 réussis, 12 ignorés, 1 en échec, 425 sous-essais réussis (4 min 02 s)** — exactement les comptes du LISEZMOI. L'échec est `test_v51_bac_reel.py::test_v51_06` (« bwrap absent » au lieu de « architecture 'riscv64' »), préexistant, déterministe sans `bwrap`, nommé par le LISEZMOI.
- **v54 seule** (`test_v54_corrections`, `test_v54_annexe`, `test_v54_prepilote`) : **69 réussis, 43 sous-essais, 0 ignoré** : les essais sur l'annexe réelle et le brouillon 7 sont bien joués (ils se trouvent à `../../../../` de la livraison dans ce dépôt ; hors de ce dépôt ils s'ignorent avec le motif « NON JOUÉ »).
- Après les essais : `essais/_tmp` retiré par `conftest.py` (message sur la sortie), aucun `__pycache__`, aucun `.pytest_cache` ; `sha256sum -c` : 387 OK.
- Non rejoués : `unshare -rn` (7 essais anciens de plus échouent selon le LISEZMOI).

## G. Les 12 choix pris seuls ; ce qui manque

| N° | Choix | À remonter à Lazar ? |
|---|---|---|
| 1 | Nœud : arrêt au premier « non mesuré » ; fin de phase de mesure et classement quand même | **Oui**, et le second membre est un défaut (CL19-02) : si l'on veut, au nœud, que « rien n'en ait été lu » (option O12), rien ne doit s'ouvrir. |
| 2 | A3 (appel coupé jamais lu), A11 (limite = arrêt du rôle), A14 (part cumulée sur le run) | Non pour A3 et A11 (côté prudent). **A14 à signaler** : sur de petits effectifs (adjudicateur, relecteur), un seul appel inexploitable dépasse 25 %. |
| 3 | Garde de Kimi de la course non jouée au pré-pilote ; M5 lue après É9 | Non : conforme à M5 du brouillon 7 (mesure, pas arrêt). À consigner. |
| 4 | Clé des classes lue par programme en É5 ; strates en É9 | **Oui** (A21, section C). |
| 5 | Un N dont le relecteur ne voit pas le défaut est exclu (A5, S6) | **Oui** : cela change l'ensemble des témoins et peut déclencher l'arrêt A5 (plus de 6 exclus) ; le brouillon ne dit pas que « défaut non vu » compte comme exclusion. |
| 6 | Adjudicateur de M5 joué en É7a seulement | Non : conforme à É7a. |
| 7 | I-9 : deux empreintes distinctes dans `contre_lecture` | Non, mais la forme seule ne prouve rien (CL19-09). |
| 8 | I-8 : à n = 2, aucun report au bras suivant | **Oui** : lecture littérale qui change les probabilités de C12 ; à écrire dans le brouillon 8 (l'annexe le demandait). |
| 9 | Multi-cases à n = 2 : une paire en tout, la mieux notée du bras de priorité 1 | Non (course seulement) ; à consigner. |
| 10 | Indices de forme : longueur et chiffres du texte des valeurs, nombre de champs, régression avec crête injectée | **Oui** : S18 et S19 sont des critères d'arrêt (A7) ; leur définition et la valeur de la crête doivent être gelées dans le préenregistrement, pas laissées au code. |
| 11 | Tâche `pp2-paraphrases` | Non, mais il faut déclarer aussi les tâches d'identifiants et d'anonymisation (CL19-10). |
| 12 | Une coupure dans une étape sacrifiable la retire, même jouée en partie | Non : conforme à la règle 3 d'A1 (« E retirable est retirée »). Les mesures partielles ne sont pas lues. |

**Ce qui manque encore pour lancer le pré-pilote (liste exacte).**
1. Décisions de Lazar : tous les seuils S1 à S31 ; D-e à D-j ; L1 à L7 ; les clés configurables (`budget.portee_plafond`, `garde_kimi.*`, `tableau.juger_passe_tableau`, `bisociateur.fournisseurs_entree`, `bisociateur.meta.*`, `a4.*`, `graines.prefixe`, `arrets.*`) ; les choix 1, 4, 5, 8, 10 ci-dessus ; confidentialité (envoi chez Moonshot et Google) ; mot sur DEP5 (ou acceptation du défaut R-819, M4 « non étalonné ») ; approbation des valeurs de l'annexe.
2. Corrections de code : CL19-01, CL19-02, CL19-04, CL19-05, CL19-06, CL19-07, ordre d'É6 (section C, point 5), puis nouvelle contre-lecture.
3. Pièces : analyseur de l'étage 1 (DEP3) avec cas sain et artefact ; garde de forme de M5 (ligne 9) ; résultats scellés et liés à un script empreinté pour les lignes 6, 8, 10, 17, 19 ; consignes figées au contrat de sortie des rôles (rédacteur, metteur, relecteur, second lecteur, adjudicateur, désaccord, vérificateur, table seule, paraphrase), aucune n'étant éprouvée sur moteur réel ; 8 fiches d'antériorité et leur clé, 4 fiches de M6b et leurs sources (DEP2c) ; source de S31 (bras Gu-Krenn) ; annexe du bras méta contre-lue, approuvée, scellée (après les verdicts des collisionneurs, DEP10) ou geler à deux bras (D-h b) ; script de puissance refait avec I-11 et I-13 ; confirmation de DEP4 par session-depot ; ligne de GO au plafond S17 exact (DEP6) ; devis refait avec les lectures de désaccord et les valeurs de `budget.etapes`.
4. Code d'analyse (n'existe pas) : intervalles, t* sur la partition, M3, M5 (union, intersection, adjudication), M6, verdict par instrument, complément.
5. Manifeste de run : le commit n'est pas lu (arbre hors dépôt) ; à porter au registre.

## Constats

| N° | Gravité | Constat | Preuve | Correction demandée |
|---|---|---|---|---|
| CL19-01 | **majeur** | **La source Gu-Krenn absente (A19) est refusée au départ, au lieu d'être déclarée « non produit (source absente) ».** `declarer_bras` produit bien la déclaration, mais `rejouer_gardes` marque la ligne 20 « non rejouée » (`gardes_e0_v54.py:166-167`) et la ligne 20 est exigée (`LIGNES_COURSE`) : `GardesE0Refusees: A12 … ligne 20 (non rejouée : bras Gu-Krenn non produit)`. Pour l'annexe (A20) le code fait l'inverse et accepte (lignes 22b, 23, 24 « sans objet, déclarée »). Le brouillon 7 (A19, CP5-01, M9 cas ii) : « bras non produit, compté, O15 », ni nœud ni arrêt. Aucun essai ne couvre ce cas. | `/tmp/cl19/probe_e0.py` : config d'essai, `sha256` de la source remplacé par `0…0` ⇒ refus ; sain ⇒ 0 ligne en défaut ; annexe fausse ⇒ départ accepté. | Traiter la ligne 20 comme 22b, 23 et 24 quand la cause est « source absente » ; essai + mutation. |
| CL19-02 | **majeur** | **Après un nœud, le pré-pilote (et la course) déclare quand même la fin d'É9, ouvre la clé des classes et les verdicts et écrit l'analyse de M1.** `prepilote_v54.py:590-601` : le `break` sort de la boucle, puis `declarer_fin_e9()`, `ouvrir_verdicts`, `_analyse_m1`. Contraire à A21 (la fin d'É9 n'a pas eu lieu) et à O12 (« rejeu de la seule mesure non mesurée sur les mêmes témoins (**rien n'en a été lu**) ») : si le nœud tombe après É6, M1 est calculée sur les verdicts d'É6 et écrite sur disque. Le LISEZMOI (choix 1) annonce « fin de phase de mesure et classement faits quand même » sans dire qu'une clé et des verdicts sont ouverts. | `/tmp/cl19/probe_noeud.py`, coût 2,0 par appel, plafond 25 : étapes jouées jusqu'à É4 (« non mesurée budget »), puis `fin_e9` déclaré, ouverture de `pp2-cle-classes`, `analyse-m1.json` écrit. Aucun essai ne couvre le pré-pilote en nœud. | Au nœud : ne pas déclarer la fin, ne rien ouvrir, écrire le bilan et rendre la main à Lazar. Essai + mutation. |
| CL19-03 | **majeur (décision de Lazar)** | **La clé des classes est lue par programme avant la fin d'É9, hors du coffre ; le journal d'accès (ligne 30) n'en garde aucune trace ; le texte d'A21 l'interdit à la lettre et le Plan l'exige.** | Section C. | Brouillon 8 : amender A21 et la ligne 30, journaliser la lecture, supprimer la lecture en É9, tirer ou trier l'ordre d'É6. |
| CL19-04 | moyen | **Les dossiers de session sont voisins du coffre.** Noms opaques, mais `sortie/sessions/<h>` est frère de `coffre/`, `temoins/`, `aiguillage/` : un agent qui voit son dossier courant lit les clés par chemin relatif. Le LISEZMOI ne signale que « savoir si l'agent voit son dossier courant ». | `/tmp/cl19/probe_taches.py` (liste de `sortie/`) ; `noyau_v54.py:73-79`. | Placer les sessions hors de `sortie` (répertoire temporaire par appel, sans voisin), ou démontrer sur le moteur réel que le dossier courant est invisible. |
| CL19-05 | moyen | **Ligne de GO : trois lectures qui échouent vers l'acceptation, et DEP4 sans contenu.** « 1 045 USD » est lu 45 (séparateur de milliers) ; « 10-45 USD » lu 45 ; « ≈ 45 USD » accepté ; « jusqu'à 45 USD par génération » accepté quel que soit N. DEP4 : n'importe quelle pièce empreintée convient. | `/tmp/cl19/go_probe.py` ; `configuration_v54.py:45, 137-139, 204-212`. | Refuser un chiffre précédé d'un groupe de chiffres, une plage, « ≈ », « par génération » si N > 1 ; exiger dans la pièce DEP4 une phrase fixe (empreinte de la phrase, pas du fichier seul). |
| CL19-06 | moyen | **Les résultats externes (lignes 6, 8, 9, 10, 17, 19) et la seconde version de témoins se contrôlent par la forme seulement.** Un JSON `{"ligne": "6", "cas_sain": "passe", "artefact": "arrete", "script_sha256": "x"}` suffit ; rien ne lie le résultat à l'analyseur injecté ni à un script empreinté. `temoins.version` est un entier de configuration. R5 demande « aucun repli silencieux ». | `gardes_e0_v54.py:276-290` ; `prepilote_v54.py:457-461`. | Vérifier que `script_sha256` est l'empreinte d'un fichier présent et que le résultat cite la même empreinte d'analyseur ; faire écrire `temoins.version` par la sortie de la version 1, pas par la configuration. |
| CL19-07 | moyen | **S6 laisse passer l'extension d'un nombre.** Les ancres sont comparées par sous-chaîne : « valeur 12 » → « valeur 123 » et « seuil 0,3 » → « seuil 0,35 » donnent 1,0 ; « sans ajouter de chiffre » (consigne de rendu) n'est pas contrôlé ; l'artefact de la ligne 5 change seulement 12 en 13. | `/tmp/cl19/s6.py` ; `prepilote_v54.py:180-188`. | Comparer sur des jetons entiers (bornes de chiffres) et ajouter au contrôle le décompte des nombres du rendu ; artefact « 12 → 123 ». |
| CL19-08 | moyen | **Gardes rejouées à É0 sans l'artefact de la table, et banc de mutations à une unité trompeuse.** Ligne 21 : l'« artefact » est `bras_decl.get("gu_krenn") is not None` (la déclaration existe) ; ligne 22b : l'artefact est un jeu d'essai vide, pas « annexe absente, non contre-lue ou à empreinte différente » ; `_arrete` accepte n'importe quelle exception (raison non vérifiée). La mutation DEP3 est « tuée » par un défaut du banc. | `gardes_e0_v54.py:39-44, 168-175` ; E ci-dessus. | Artefacts propres pour 21 et 22b ; `_arrete(f, types)` avec le type d'exception attendu ; recompiler les mutations avec `super(Classe, self)` ou lire le motif. |
| CL19-09 | mineur | I-9 : `000…0` et `111…1` passent comme empreintes, `R-000` comme décision ; la vérification « différence limitée aux deux lignes » (annexe § 9.5) n'existe pas ; l'empreinte du brouillon 7 n'est contrôlée que par un essai. | `/tmp/cl19/annexe.py` ; `bisociateur_v54.py:77-81`. | Exiger l'empreinte du brouillon relu comme paramètre de configuration et recalculer la différence ; vérifier la constante d'empreinte de la spécification au lancement. |
| CL19-10 | mineur | Écarts non déclarés au brouillon 7 : tâches de graines supplémentaires (`pp2-ident-*`, `pp2-anonymisation-<juge>-<fiche>`) ; libellés des causes (iii) et (iv) de M9 ; désaccord limité à `paires_max` et texte servi tiré de la fiche ; jetons de M7 non lus ; **A2 « modèle servi non lu » non gardé dans le noyau** (il dépend de l'option `exiger_modele_servi` de l'adaptateur ; seuls le cas Opus et la cohérence entre lots de juges sont gardés) ; fiches d'antériorité et de M6b lues comme pièces. | Sections A, B, C. | Les écrire au brouillon 8 ou au LISEZMOI ; ajouter l'artefact « modèle servi absent » à la ligne 1. |
| CL19-11 | mineur | Machine jetable : `TOKENIZERS_PARALLELISM` refusé à tort ; `GH_PAT`, `*_KEY_FILE`, `SSH_AUTH_SOCK`, `*_AUTH` acceptés. | `/tmp/cl19/s6.py` (partie machine jetable). | Liste de motifs complétée ; garder le contrôle de l'opérateur (devis, destruction). |
| CL19-12 | mineur | A4 : « bisociative » échappe à « bisociation » ; l'entrée de rendu n'est gardée que sur le squelette ; un relecteur muet compte comme « ambigu » (motif A6) alors que c'est un défaut technique ; `prepilote.d_g`, `L1`, `L2` et `decisions_a15.d_g` sont deux sources sans contrôle de cohérence ; la boîte d'É5 écrit `primaires_non_ambigus` classée par classe. | Sections A, C. | À corriger avec CL19-03 et CL19-06. |
| CL19-13 | mineur | Couverture : aucun essai sur le pré-pilote en nœud, sur A19 à É0, sur S18 dans le flux (2 fiches de Kimi seulement), sur la reprise après A8 ; les essais de l'annexe réelle et du brouillon 7 s'ignorent hors de ce dépôt. | Section E. | Ajouter les essais avec les corrections 01 et 02. |

*Fin. Aucune valeur n'a été gelée ni tranchée ; ce document ne vaut pas verdict de porte.*

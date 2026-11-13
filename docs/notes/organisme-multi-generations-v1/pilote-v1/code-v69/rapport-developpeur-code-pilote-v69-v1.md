# Rapport du développeur — code v69 du pilote MR-2 (corrections de la contre-lecture du code v68) — v1

- **Développeur** : Claude Opus 5.5 (`claude-opus-5-5`), le développeur du code v68, repris avec son contexte (session mère
  `session_01XJ6Mgn4MZR4nxqK44C8Ea3`).
- **Consigne** : `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-12-2019-v1/consigne-developpeur-code-pilote-corrections-v1.md`,
  lue par `git show` (branche `origin/main` du dépôt de travail : la branche locale `main` est en retard et ne la porte pas),
  sha256 `20c8384a74213c5f719cdfe69e07350bcfa4dacf9268be0d9229eced520cd5b0`, égale à son compagnon. Contre-lecture
  `contre-lecture-code-pilote-v68-v1.md`, `7af19261758adc8414e580362f2a03f778540ab19a0bef1ab4ee03fdb869fc5a`, égale à son compagnon ;
  ses outils lus (`mutations_contre_lecteur_v1.py`, `epreuves_contre_lecteur_v1.py`).
- **Pièces lues pour Q-4 à Q-6 et M-1** (lecture seule, par `git show`) : `docs/notes/collisionneur-experimentateur-v1/script-v1/collisionneur_v8_plafonds_bas_v1.py`
  (`4ad78ccce8228aed2679c854eaec7ee4d2ab8f867098218387024adfeb1e7756`, égal à son compagnon : `appeler_anthropic`,
  `appeler_gemini`, `appeler_openai`, `lire_reponse_openai`, `statut_reponse`, `EFFORT`) ; journal masqué
  `docs/notes/collisionneur-diversite-idees-v1/run-e3-v1/journal-masque-v1.jsonl`
  (`12cb64015a683ca8b0a745f6b19da9fd153850db18cedf3e79358327a884d82b`, égal à son compagnon ; **champs du modèle demandé, du
  modèle servi et de l'effort seulement**, aucun contenu de cellule).
- **Heures** (`date -u`, 13 novembre 2026) : reprise 13:21:07 ; dossier provisoire de mon premier banc v68 supprimé par son
  chemin exact (`/tmp/tmp7p3kzxyw`, copie de `orchestrator/` reconnue par ses fichiers v68) ; code v69 de 13:24 à 13:36 ; essais
  13:36:57 à 13:41:19 (88 passés) ; banc de mutations 13:43:37 à 15:15:01 (passage entier), N8 et M34 rejouées de 15:15:16 à 15:18:52 ; journal des essais 15:19 à 15:21:14 ; essais à blanc 15:21:23 à 15:21:34 ; fin : 15:22:25 (dépôt du rapport).
- **Aucune dépense, aucun appel de modèle ni de réseau** (hors boucle locale : relais à amont factice et doublures déclarées par
  les essais), **aucune clé lue** (les essais posent des valeurs factices dans l'environnement qu'ils construisent pour leurs
  sous-processus ; l'environnement réel n'est jamais relayé), rien poussé, noms neufs, ajouts seulement, un processus de calcul
  à la fois (`ulimit -v 6000000`, `OMP_NUM_THREADS=2`). Aucun refus de permission, de classifieur ou de crochet.

## 0. Verdict

**Code v69 écrit sous des noms neufs (la v68 reste) : 2 bloquants, 10 majeurs et 12 mineurs corrigés ; 2 mineurs refusés avec leur
raison (m-14, hors mandat : sortie de la mesure scellée ; m-8 en partie : aucune reprise, conforme au texte, risque dit) ; essais : 88 passés et 112 sous-essais passés ; banc : 88 mutations ; au passage entier, 87 tuées pour la raison attendue et une survivante, **N8 du contre-lecteur** (l'artefact de contenu était aussi refusé par le contrôle neuf du compagnon : l'essai isolait mal la garde) ; essai corrigé (compagnon recopié), N8 et M34 rejouées : tuées pour la raison attendue ; les huit mutations du contre-lecteur, traduites dans
le code v69 (N4 coupée en trois), meurent.** Le mode réel est joué de bout en bout par les essais sur une doublure déclarée
(clés factices, adresse d'amont de la boucle locale), avec un artefact par garde. Restent avant le premier appel : la
contre-lecture du différentiel, le texte (section 6), la sonde (section 7), les GO.

## 1. Constats, un par un

Fichiers (`orchestrator/`) : `pole/pilote_mr2_v69.py` (cœur), `pole/proposeurs_pilote_v69.py` (proposeurs),
`pole/audit_pilote_v69.py` (audit), `demonstrations/pilote_mr2_v69.py` (lanceur), `exemples/pilote-mr2-v69/commandes/commande_pilote_v69.py`
(commande), `…/relais_pilote_v69.py` (relais), `exemples/pilote-mr2-v69/configuration-pilote-mr2-v10.json` (configuration v10) ;
essais `essais/test_pilote_mr2_v69.py` ; banc `essais/mutations_pilote_mr2_v69.py`. Lignes : celles de la tête v69.

| constat | issue | où (fichier, ligne) | correction | essai qui le prouve ; mutations |
|---|---|---|---|---|
| **B-1** voie de Claude, « à confirmer », gel provisoire | corrigé | relais l. 174 (`appel_reel`), l. 121 (`lire_flux_anthropic`) ; configuration v10 | interface Messages, `POST https://api.anthropic.com/v1/messages`, `x-api-key` (variable **nommée** `RR_ANTHROPIC_API_KEY_RIGAUD`), `anthropic-version: 2023-06-01`, en-tête d'espace de travail seulement si une variable d'espace est nommée (comme le collisionneur), `stream: true`, `output_config: {effort: "high"}`, un message utilisateur, aucun outil, aucun système, aucun `thinking`, aucun `fallbacks`, adresse fixe (jamais `ANTHROPIC_BASE_URL`) ; flux SSE lu jusqu'à `message_stop`, message final reconstitué, flux brut rendu ; plus aucun champ « à confirmer » (champ retiré de la configuration ; sources des prix écrites dans `sources`) ; bloc v69 régénéré | `ModeReelBoutEnBout.test_sain_bout_en_bout` (16 appels réels sur doublure : clé juste, corps exact), `RelaisRefus.test_flux_anthropic` ; V07, V08, V27, V32 |
| **B-2** relais non identifié, gardes du mode réel sans essai | corrigé | lanceur l. 174 (`exiger_mode_reel`), l. 228-229 ; proposeurs l. 275 (`env_du_relais`), l. 321 (`controler_etat_relais`) ; relais l. 74 (`url_permise`), l. 324 (`/relais/etat`) | le lanceur lance lui-même les relais, en mode réel comme à blanc ; clé recopiée **par son nom** dans le seul environnement du relais, environnement bâti par filtrage (`ENV_FILTRE`) ; `/relais/etat` rend empreinte du fichier, prix, borne, `max_appels`, adresse d'amont, réglages, appelant, présence de la clé ; contrôle champ par champ (16 champs), `appelant == dialecte` en mode réel, `factice:` seulement à blanc ; adresse d'amont figée par dialecte (`https`, hôte exact), boucle locale admise pour les essais seulement ; configuration gelée exigée en mode réel | `ModeReelBoutEnBout` : sain et 10 artefacts (GO absent, montant faux, périmètre, texte altéré, bloc altéré, engagement, empreintes des mondes, clé absente, scénario, second lancement) ; `EtatDesRelais` (17 champs, un artefact chacun) ; `RelaisRefus.test_lancement_refuse` ; N1, N2, N3, N4a-c, V01, V09, V24 à V28, V32 à V34 |
| **M-1** forme de l'identifiant servi | corrigé | commande l. 99 | identifiant exact, ou suivi d'un suffixe de **date** seulement (`-AAAAMMJJ`, `-AAAA-MM-JJ`) ; le suffixe à 3 chiffres de la v68 retiré ; fait relevé : journal masqué du 12 novembre (`12cb6401…`) : `gpt-6-astra`, `gemini-4-argon`, `claude-fable-5-1`, `claude-opus-4-6` servis exactement sous l'identifiant demandé (3 cellules chacun) ; abandon au premier modèle non conforme (Q-8) | `Commande.test_modele_servi_m1` (5 admis, 8 refusés) ; M38, M39 |
| **M-2** identifiant de fournisseur rapatriable | corrigé | relais l. 162 (`type_d_erreur`) ; audit l. 32, l. 79 | le relais ne rend d'une erreur d'amont que le statut et le type (jamais le corps) ; d'une exception, la classe ; le rapatriement refuse tout fichier portant un motif d'identifiant (`org-…`, `sk-…`, `sk-ant-…`, `proj_…`, `AIza…`, `wrkspc_…`) | `test_erreur_amont_sans_corps`, `test_rapatriement_artefacts` (identifiant, clé masquée) ; V05 |
| **M-3** structure des mondes au manifeste | corrigé | cœur l. 683 (`jouer_c16`) ; lanceur l. 213 | C-16 rend (public, privé) : au manifeste `admise`, `recrite`, `loi_sha256` seulement ; conditions et motifs dans `prive/controles-prives.json`, jamais rapatrié | `C16C17.test_sain`, `test_manifeste` (aucun « conditions ») ; V18 |
| **M-4** appel rendu sans corps | corrigé | proposeurs l. 232 | pour `complet` et `tronque` : corps du relais sur disque, égal à son compagnon et à l'empreinte rendue, sinon arrêt | `test_artefacts_corps_m4` (absent, sans empreinte, compagnon faux) ; V11 |
| **M-5** mesure une fois, à la main | corrigé | lanceur l. 290 (`mesurer`), l. 322 (`lire`) | sous-commande `mesurer` : manifeste et `CARTES.json` égaux à leurs compagnons et liés, refus si une sortie de mesure existe, programme `676d5f37…` lancé sans copie, sortie scellée, pièce `mesure-pilote-v69.json` scellée ; `lire` exige la pièce, la sortie égale à la pièce, les cartes mesurées | `test_mesure_une_fois`, `test_mesure_cartes_alterees`, `test_lecture_artefacts` ; V14 à V16 |
| **M-6** audit R4 sans ses pièces | corrigé | cœur l. 718, l. 744 ; lanceur l. 213 ; audit l. 73 | textes servis gardés dans `prive/` (jamais rapatriés) ; `verifier_texte_servi` relit le texte indépendamment (forme, quatre clés, monde public, gabarit, archive, épisodes) — la tautologie de la v68 (`pieces_du_texte`) n'est plus appelée ; `controle_episodes` (400, 8 traits finis non constants, issues et sous-populations vues) au manifeste ; `cartes_refusees` rendue par `relire` | `M6TexteEtEpisodes` (5 et 4 artefacts), `test_manifeste`, `test_cartes_relues_et_refusees` ; V22, V23 |
| **M-7** R9 au manifeste | corrigé | lanceur l. 132, l. 174 | versions de Python et de numpy, plate-forme, commit de l'arbre (ou `None`), règle des graines ; mode réel : numpy = `numpy_exige` de la configuration (`2.5.3`, celle du texte ; au bloc) | `test_manifeste`, `test_numpy_exige` ; M26, V26 |
| **M-8** garantie du relais | corrigé | relais l. 354, l. 377 | le relais calcule son propre pire cas (octets + 1024, `max_tokens`, ses prix ; la commande n'en déclare plus), refuse `max_tokens` > sa borne (400), règle un usage illisible au pire cas | `test_plafond_par_son_propre_pire_cas`, `test_refus_directs_et_usage_absent_au_pire_cas`, `test_cout_excessif_cause` ; N5, N6, V03, V06. Limite à écrire au texte : le plafond n'est dur que si le fournisseur tient sa borne (réflexion comprise) et si les prix sont les vrais (sonde, section 7) |
| **M-9** règle d'extraction | corrigé | cœur l. 368 | la consigne servie dit « un seul bloc ```json … ``` (le premier bloc ```json de ta réponse est le seul lu) » ; l'empreinte du gabarit change (`e77d3041f7815b2c0579cbafdb2898ca8569fe61e6cb51b99a41c3724fc456a2`) ; le relevé compte les appels complets illisibles | `M6TexteEtEpisodes.test_sain` ; V31. Reste au texte : écrire la règle dans « Métrique » |
| **M-10** six gardes sans artefact | corrigé | (voir N1 à N8 et ci-dessus) | un artefact par garde : N1-N8, modèle refusé par le relais (403), octets du texte servi, chaque proposeur dans une seule ligne de GO | `RelaisRefus`, `test_octets_du_texte_servi`, `Configuration.test_artefacts` (« deux_lignes ») ; V04, V35 |
| m-1 rapport | corrigé | rapport v1 (ce fichier) | le bloc v69 compte 27 lignes d'empreintes ; le différentiel est un `git diff` par paire de fichiers v68 → v69 (section 4), le paquet un `format-patch` | — |
| m-2 empreintes des mondes du registre | corrigé | lanceur l. 198 | `--mondes-shas` exigé en mode réel, comparé par `charger_mondes_prives` | `test_artefact_mondes_shas` ; V34 |
| m-3 mondes liés au texte | corrigé | cœur l. 869 ; lanceur l. 174, l. 405 | `generer` exige `--texte` égal à son empreinte et écrit `MONDES.json.engagement.json` (privé) ; le mode réel le relit | `test_artefact_engagement` ; V25 |
| m-4 périmètre des GO | corrigé | proposeurs l. 135 | mots exigés écrits à la configuration (π1 : « MR-2 », « crédits de Claude » ; π2 : « pilote », « hors crédits ») | `test_go_pi1_pi2`, `test_artefact_perimetre` ; V10 |
| m-5 arrêt sans relevé | corrigé | lanceur l. 253 | tout arrêt (nommé ou imprévu) après le lancement des relais écrit relevé et manifeste partiels (`partiel: true`, `CARTES-partiel.json`), code 3 ; un refus avant le premier appel reste un refus (code 2) | `test_part_atteinte_arret_et_releve_partiel`, `test_exception_imprevue_arret` |
| m-6 un seul lancement réel | corrigé | lanceur l. 174, l. 230 | `--registre-lancements` (hors dépôt) : un second lancement réel pour le même texte est refusé (nœud) ; le lancement est consigné quand les relais sont prêts | `test_artefact_second_lancement` ; V24 |
| m-7 délai de l'adaptateur | corrigé | proposeurs l. 213 | délai de l'adaptateur = panne (échec, abandon), plus un arrêt | `test_delai_de_l_adaptateur_panne` ; V13 |
| m-8 reprise sur erreur passagère | **refusé en partie** | — | le texte dit « aucune reprise » : gardé ; risque de P-0 sur une erreur passagère (429, 5xx) à dire à Lazar (le collisionneur reprend quatre fois) | — |
| m-9 encodage | corrigé | proposeurs l. 210 ; lanceur | `encoding="utf-8"` explicite pour la commande, les relais, `git`, la mesure | (aucun essai de locale ; échec sûr déjà) |
| m-10 K1 servie non gardée | corrigé | cœur l. 696 | la K1 servie passe le gardien telle quelle (sans réécriture) avant tout appel | `test_artefact_k1_servie_hors_bornes` ; V21 |
| m-11 relais sans authentification | corrigé | relais l. 339 ; commande | jeton du lancement (`secrets.token_hex(16)`), variable `RELAIS_JETON` du seul relais, `RELAIS_JETON_POLE` de la commande, en-tête `X-Jeton-Relais` ; 401 sinon | `test_jeton_faux`, `test_refus_directs…` ; V02, V29 |
| m-12 refus d'Astra, réflexion | corrigé | commande l. 143 ; relais `usage_du_corps` | champ `refusal` du message → refus ; sortie = `completion_tokens` + `reasoning_tokens` (règle prudente du collisionneur, `lire_reponse_openai`) ; Argon : `promptFeedback.blockReason` → refus | `Commande.test_dialectes` ; V30 |
| m-13 lecture et rapatriement | corrigé | lanceur l. 322 ; audit l. 79 | `lire` exige la liste **complète** des 13 modules ; `rapatrier` vérifie chaque compagnon et refuse le contenu d'un contexte servi (`episodes_developpement`, `lois_retenues`) | `test_lecture_artefacts` (module manquant), `test_rapatriement_artefacts` (compagnon) ; V17 |
| m-14 `secondes_de_chaine` dans la sortie scellée | **refusé** | — | hors mandat : la mesure (`676d5f37…`) est scellée et porte cette valeur ; à trancher par la mère au regard de S-9 | — |

**Décisions de la mère portées** : Q-1 (c) (configuration v10 : 64 000 / 89 000 / 36 000 / 36 000 ; plafonds 3,00 / 2,00 / 2,34 / 2,34 ;
parts 12 / 8 / 9,36 / 9,36 ; π1 20,00 ; π2 21,72 = 9,36 + 9,36 + 3,00) ; Q-2 (d) (`recrire_dans_les_bornes`, cœur l. 648 ; le monde
public qui arrêtait la v68 est désormais admis, réécriture équivalente à 10⁻⁹, essai `test_sain_monde_naturel_hors_bornes_recrit` ;
aucune écriture si g > 50 : `test_artefact_c16_aucune_ecriture` ; réécriture non équivalente : `test_artefact_c16_ecriture_non_equivalente`) ;
Q-3 (compte du gardien) ; Q-4 (effort « high » envoyé à Fable 5.2 et Opus 5.5 ; **aucun réglage envoyé à Argon ni à Astra** : ce
sont les champs de `appeler_gemini` et `appeler_openai`, et le collisionneur n'envoie `EFFORT` qu'à Anthropic — fait relevé
(`executer_cellule` : `"effort": EFFORT if m["fournisseur"] == "anthropic" else None`) et confirmé par le journal masqué, où
l'effort vaut `high` pour Claude et `None` pour Argon et Astra ; réglages consignés au manifeste et au bloc) ; Q-5 ; Q-6 (adresse
d'OpenAI exacte, `https`) ; Q-7 ; Q-8 ; Q-11 (rien poussé).

**Avis du contre-lecteur suivis** : Q-9 (aucune borne de taille au pilote ; la course reprend ce gabarit) ; Q-10 (dérivation
gardée, écrite au manifeste) ; Q-12 (chemin v52b inerte, gardé).

## 2. Essais

`essais/test_pilote_mr2_v69.py` : **88 passés, 112 sous-essais passés, en 136,81 s**. Classes neuves : `M6TexteEtEpisodes`, `EtatDesRelais`, `ModeReelBoutEnBout`
(copie de l'arbre, configuration pointée vers la **doublure** `Doublure` de la boucle locale, déclarée par l'essai seulement ;
clés factices posées par l'essai dans l'environnement qu'il construit ; texte d'essai portant le bloc régénéré de la copie ; lignes
de GO datées du jour ; engagement des mondes). Mondes : publics (`pilote-v68-essai-developpement`, 1 à 4, et le monde 3 de
`pilote-v2-essai-developpement` pour Q-2).

## 3. Banc de mutations

`essais/mutations_pilote_mr2_v69.py`, rejoué **une fois, en entier, à la fin**, sur le code gelé : **88 mutations ; au passage entier, 87 tuées pour la raison attendue et une survivante, **N8 du contre-lecteur** (l'artefact de contenu était aussi refusé par le contrôle neuf du compagnon : l'essai isolait mal la garde) ; essai corrigé (compagnon recopié), N8 et M34 rejouées : tuées pour la raison attendue**
(`mutations-pilote-v69.json`). 88 mutations : les 43 du banc v68 portées (M26 remplacée, « à confirmer » n'existant plus : numpy
exigé), les **huit du contre-lecteur traduites dans le code v69** (N1, N2, N3, N4 coupée en N4a plafond, N4b appels, N4c modèle,
N5 à N8) et 35 neuves (V01 à V35). « Tuée » seulement si l'essai attendu échoue.

## 4. Différentiel v68 → v69 (prêt pour sa contre-lecture)

`differentiel-v68-v69.patch` : `git diff --no-index` de chaque paire (cœur, proposeurs, audit, lanceur, commande, relais,
configuration v9 → v10, essais, banc) ; la v68 est inchangée dans l'arbre. Paquet `organisme-v69-pilote-mr2-v1.bundle`
(`89aa20baddb993f998d5ca5241ec56fd73e92815b2a017fa3a595ceeb04e4b8c` ; branche `prep/organisme-v69-pilote-mr2-v1`, tête
`2ca17ea3243979837890e1243876299a202b7748`, prérequis `276b6afd…`, tête v68 ; commits v69 `616d9e8`, `2ca17ea`) et patch
`organisme-v69-contre-276b6af.patch` (`4ea8823348e7d2ce526923b02f93baf33f25e56615f2b8e1563974434be912c1`, `format-patch` des deux
commits) ; différentiel `4721f53c0b1a23030f3d1e2f33465e11390bcad9a07180deaff6ca5be032b0c6`. Les fichiers v68 ne sont pas modifiés
(`git diff --name-status 276b6af 2ca17ea` : ajouts seulement, 9 fichiers).

## 5. Marqueurs du texte que le code permet de remplir

- **Bloc gelé** : `EMPREINTES-code-pilote-v69.txt` (`7aa6279801ba7f0f06408bdc5b69cd0cf8adb961ed77ee1f5d5510ab3e90e6c6`), marqueurs `<!-- empreintes-du-code-pilote-v69 : début/fin -->`,
  recopié tel quel ; le lanceur en mode réel l'exige égal à l'octet.
- **[GABARIT-SHA256]** : `e77d3041f7815b2c0579cbafdb2898ca8569fe61e6cb51b99a41c3724fc456a2` (change avec M-9).
- **Bornes de sortie** : Fable 5.2 64 000, Opus 5.5 89 000, Argon 36 000, Astra 36 000 jetons ; `octets-entree-max` 52 000.
- **Plafonds de session et parts** : 3,00 / 2,00 / 2,34 / 2,34 USD ; parts 12,00 / 8,00 / 9,36 / 9,36 ; machine 3,00.
- **Lignes π1 et π2** : π1 = **20,00 USD** (parts `fable52` 12, `opus55` 8 ; périmètre contenant « MR-2 » et « crédits de
  Claude ») ; π2 = **21,72 USD** (Argon 9,36, Astra 9,36, machine 3,00 ; périmètre contenant « pilote » et « hors crédits ») ;
  total au pire 41,72 USD (au lieu de 39). Montant écrit seul ou « 20 USD (sur crédits) » (lu 20).
- **Réglages d'effort** : `{"output_config": {"effort": "high"}}` à Fable 5.2 et Opus 5.5 ; aucun à Argon ni à Astra.
- **[CHAMPS-ASTRA]** : champs du collisionneur (`usage.prompt_tokens`, `completion_tokens`, `completion_tokens_details.reasoning_tokens`,
  `finish_reason`, `message.refusal`) ; la sortie comptée = visible + réflexion (prudent) — à vérifier par la sonde.
- **Identifiant et prix d'Astra** : `gpt-6-astra` (servi tel quel au journal du 12 novembre) ; 10 / 50 USD par million (barème
  prudent du collisionneur, « SUPPOSÉ ») — à vérifier par la sonde ou la page publique.
- **Voie d'accès aux crédits de Claude** : clé de l'organisation nommée `RR_ANTHROPIC_API_KEY_RIGAUD`, interface Messages, en flux,
  sans repli ; espace de travail : aucune variable nommée à la configuration (à ajouter si la clé l'exige : sonde).

## 6. Ce que le texte doit changer avant le scellement

- **C-5** : « au plus 3 conditions emboîtées », comptées le long de tout chemin, `defaut` compris (Q-3).
- **C-16** : une loi de référence hors de ±4 est récrite en `transformee` équivalente (feuille softmax / g, `puissance` g,
  g = max|coefficient|/4 relevé de 10⁻⁹, g ≤ 50), égalité ≤ 10⁻⁹ vérifiée ; arrêt seulement si aucune écriture n'existe ; la K1
  servie passe le gardien telle quelle.
- **Liste d'arrêt** : abandon du proposeur sur panne du relais (délai de l'adaptateur compris), modèle servi différent, usage
  absent, coût au-dessus du pire cas ; refus du modèle et réponse illisible = échec sans abandon ; corps du relais absent pour
  un appel rendu = arrêt ; tout arrêt laisse relevé et manifeste partiels ; un seul lancement réel par texte ; la mesure par
  `mesurer`, une seule fois.
- **Dérivation de la graine des épisodes de développement** : `SeedSequence(entier des 16 premiers octets de sha256(« pilote-mr2-v68|episodes-developpement| »
  ∥ empreinte du devis))` (étiquette héritée de la v68, gardée pour que les épisodes ne changent pas).
- **Phrase sur l'effort** : « Fable 5.2 et Opus 5.5 reçoivent `output_config.effort = "high"` (réflexion toujours active, aucun
  `thinking` envoyé) ; Argon et Astra ne reçoivent aucun réglage de réflexion ni d'effort (champs du collisionneur v8) ; p_c ne vaut
  que pour ces réglages. »
- **Métrique** : la règle d'extraction (premier bloc ```json) ; « le plafond n'est dur que si le fournisseur tient sa borne et si
  les prix sont les vrais » (M-8) ; devis et lignes : 41,72 USD au pire.
- **Dessin, isolement** : textes servis gardés sur la machine pour l'audit R4, détruits avec elle ; l'audit R4 se fait avant la
  destruction s'il est déclenché.

## 7. Sonde payante : non faite ; ce qu'elle devrait vérifier, appel par relais

Un appel par relais (4), par la chaîne v69 elle-même (`jouer` n'est pas fait pour cela : un lanceur de sonde serait à écrire, ou la
commande lancée à la main contre chaque relais), consigne courte (≈ 100 octets : « Réponds par le seul mot OK. »), **borne de
sortie gelée** (pour éprouver qu'elle est admise). À relever pour chacun : statut HTTP, identifiant servi exact (règle M-1),
raison d'arrêt, champs d'usage présents et entiers, coût lu contre la facturation (console), en-têtes rendus, corps entier, témoin.
En plus :
- **Fable 5.2, Opus 5.5** (clé `RR_ANTHROPIC_API_KEY_RIGAUD`) : `max_tokens` 64 000 et 89 000 admis en flux ; `output_config.effort`
  admis ; besoin d'un en-tête d'espace de travail (400 sinon) ; Fable 5.2 servi sur ce compte (exigence de rétention de 30 jours) ;
  blocs `thinking` vides ; prix 8 / 40 et 4 / 20 contre la facturation ; consommation relevée par appel.
- **Argon** : `maxOutputTokens` 36 000 admis ; `modelVersion` exact ; `thoughtsTokenCount` présent et compté dans la sortie ;
  prix contre la facturation (le barème 10 / 50 est prudent).
- **Astra** : `gpt-6-astra` servi sous cette forme ; `max_completion_tokens` 36 000 admis ; **si `completion_tokens` comprend
  déjà `reasoning_tokens`** (sinon le comptage prudent double la réflexion) ; prix 10 / 50 ; champ `refusal`.
Coût au pire (borne gelée, consigne de 100 octets) : Fable 5.2 (1 124 × 8 + 64 000 × 40) / 10⁶ = 2,57 ; Opus 5.5
(1 124 × 4 + 89 000 × 20) / 10⁶ = 1,78 ; Argon et Astra (1 124 × 10 + 36 000 × 50) / 10⁶ = 1,81 chacun : **total au pire 7,97
USD** (dont 4,35 sur crédits de Claude) ; attendu < 0,10 USD (réponse d'un mot ; la réflexion se paie).

## 8. Ce qui reste avant le premier appel

Contre-lecture du différentiel v68 → v69 par un autre modèle (N-052) ; texte (section 6) avec le bloc v69, scellé ; sonde
(section 7) sur GO ; lignes π1 (20,00) et π2 (21,72) ; secret tiré sur la machine (`secret`), engagé et poussé ; phrase de Lazar ;
`generer --texte` ; `preparer` ; essai à blanc sur la machine avec les vraies pièces ; puis `jouer --mode reel`, `mesurer`, `lire`,
audit si déclenché, `rapatrier`, destruction (R10).

## 9. Essais à blanc rejoués (A et B)

Quatre mondes de développement vérifiés de la v68 (fichier privé `68797457…`, secret public de 32 octets nuls), configuration
v10 gelée, relais à amont factice lancés par le lanceur, puis `mesurer`, `lire`, `relire`, `rapatrier` :

- **A, sain** (tous « k1_plus ») : 16 complets ; `CARTES.json` `d61dfc80…` (**égal à celui de la v68** : les cartes factices ne
  dépendent pas de la phrase ajoutée à la consigne) ; mesure par `mesurer` (sortie scellée et pièce de liaison) ; issue **P-2 avec
  réserve R-1** ; écarts de coût nuls ; 48 cartes refusées listées ; rapatriement : 112 fichiers, 6 laissés (`prive/` : 4 textes
  servis et les contrôles privés), aucun monde ; code au manifeste = bloc gelé.
- **B, pannes mêlées** (Fable tronqué au monde 3, Opus copies de K1, Argon refus au monde 2 et illisible au monde 4, Astra en
  panne) : Astra abandonné au monde 1 (code 3) ; 10 complets, 1 tronqué, 5 échecs ; Argon, sur refus, **non abandonné** (Q-8) ;
  `CARTES.json` `66396fef…` (égal à la v68) ; issue **P-0** (9 répondus, 2 dans un monde) ; écarts de coût nuls ; 15 refusées ;
  rapatriement : 94 fichiers, aucun monde.

Versés : `essai-a-blanc-v69/A/`, `essai-a-blanc-v69/B/` (rapatriés, sans monde ni texte servi).

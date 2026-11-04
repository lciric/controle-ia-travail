# Préenregistrement — pilote de l'exposant p : plan (évaluation, registre) sur Llama-3.1-8B-Instruct — v1, brouillon 2

Gabarit : `prereg/gabarit-preregistrement-v1.md` (R1, R2). Brouillon **non scellé**, à contre-lire par un sous-agent neuf (R2). Il remplace, pour le scellement, le brouillon 1 (`preregistrement-pilote-exposant-p-v1-brouillon1.md`, `1699db87…`, gardé tel quel, R12), jugé non scellable par sa contre-lecture R2 (7 bloquants, 8 importants, 9 mineurs). Au scellement, il sera copié sous `prereg/pilote-exposant-p-v1.md`, chemin par défaut du script d'instance. Les marqueurs `<<…>>` restent jusque-là : le validateur `controle_ia.prereg` refuse de sceller tant qu'il en reste, et le lanceur refuse un run réel tant qu'il en reste un dans la configuration, les stimuli ou ce texte (dont `<<DOI_R9_BIS>>`).

- Auteur : rédacteur neuf du brouillon 2 (sous-agent) ; je n'ai écrit ni le brouillon 1, ni son code, ni sa contre-lecture. Pour Lazar Ciric.
- Date (UTC) : 2026-11-04, rédaction de 01:35 à 02:45 (`date -u`), sur la branche `canal/conv-audit-n04` (tête `e7726dce`).
- Commit du code d'analyse : <<COMMIT_SCELLEMENT>>
- Consigne : `brouillons/reprise-conv-audit-2026-11-02-nuit/prompts-sous-agents/pilote-exposant-p-redacteur-brouillon2-prompt.md` (`99049a75…`), sous l'avenant `brouillons/reprise-fusionnee-2026-11-04/avenant-relances-v1.md` (`d4f14478…`).
- Décisions de Lazar qui s'imposent (mot du 3 novembre, 11:33 et 11:35 heure de Paris, « je suis tes recos », « recos aussi ») : (1) **pas de bloc aux couches moyennes** dans ce pilote ; (2) **R9-bis réutilisé par citation, pas recalculé** (section « Emprunts à R9-bis ») ; (3) **GO de 30 USD** : GO-2026-11-04-03, inscrit sur `main` (`registres/go.md`, ligne 241).
- Documents qui font foi (chemin + empreinte) :
  - `docs/programme-controle-ia-v2.md` — `2fd63badb5afea48f48d3ca501ae3b027c4094a8b176508488a41a22e45aa18c` ; `docs/brief-claude-code-programme-complet-v2.md` — `9261932a11f29e8643175bc6e150d5455067f58a3cb1e57dca99e02cb17aa3b2` ; `CLAUDE.md` (branche) — `a2aabda8a181d46d9723bad44ad352b5e61650634e0f3bc4863451229af00b1b`.
  - Lecture du papier : `brouillons/pilote-exposant-p-v1/lecture-2606-24964-v1.md` — `3c550d93ae97e37309ef01a95e1829c946463edf1cd7013110c95c2eed815851`.
  - Contre-lecture R2 du brouillon 1 : `brouillons/pilote-exposant-p-v1/contre-lecture-v1/contre-lecture-pilote-exposant-p-v1.md` — `4b215c28…` (compagnon `.sha256`) ; couples `couples-contre-lecture-pilote-exposant-p-v1.json` — `b6510f307f3464a170ea8a0728d6221886818ca599450528a5f3c2ff54811028` ; rejeux `rejeu/scenarios-supplementaires.json` — `8f5636219999e50b34890fefd0297e028b53db6e4a7bf0ac4349c1ff8c562545`.
  - Chemin de la configuration du pilote : `brouillons/pilote-exposant-p-v1/config-pilote-exposant-p-v2.json` — `c5a63a9036043302d8f8c50530f4f0dc94903c7756f81ff9b16f36c584f950bd`.
  - Chemin des stimuli du pilote : `brouillons/pilote-exposant-p-v1/stimuli-pilote-exposant-p-v2.json` — `9a32ca837ff115ba589585102a07f9b0413c6118a02ae51ff3a731fcb4329adf`.
  - Vérification humaine des stimuli (à remplir par Lazar avant le scellement) : `brouillons/pilote-exposant-p-v1/verification-humaine-stimuli-v2.md` — `8844f1b11405efe0912e644d44ac81f9bfdce36aecc47c21775ac19615a2393a` (version vierge) ; version remplie : <<VERIFICATION_HUMAINE_LAZAR>>.
  - Références publiées converties : `src/controle_ia/pilote_exposant_p/references_publiees/references-publiees-v1.json` — `b594ee86b6d5ee1e6355203eca416815fc87e0e4c55eaf7f8b4b66675516375a` ; `grilles-publiees-v1.npz` — `c30a014a2e03aed0ce69dc43ea80488a7a47c0eb013f558c59c36f574ece9fbe` ; `directions-publiees-v1.npz` — `ced98c6285e0a6f7c0dd31189d2a00916b38fd764410fb32d9891821990380b0`.
  - Copie amont (MIT, commit `a9355d4001500708a40a255bacfe559e6dc269c0` de `github.com/FranciscoHS/fsec-paper`) : `amont/parametrize.py` — `35e855f048daeccdb6406a66658effd2401d12cafb83322297c55ff06d183303` ; `amont/superellipse.py` — `47d19c99147577d6670f5727eb23a8de5336f5677d3d2f6c342974d20dd0da0d`.
  - Audit empreinté du code publié : `results/thrpair_audit.md` — `272827f3fb082f71df57edf49ec5d9e027031cab47ab7e23cb38c492170911ad` (cité dans `references-publiees-v1.json`, clé `sources_sha256`).
  - Simulation de puissance v2 : `src/controle_ia/pilote_exposant_p_v2/puissance.py` — `4b1bce827f4556f7144416fdd6bdb036121f6590c5cd117768f8eef70694b3b7` ; sortie `brouillons/pilote-exposant-p-v1/puissance-pilote-exposant-p-v2.json` — `27a0251cf6e1f8b9dfd3e7f7c51ff4d7c76c2fdf2c01b1996628501b7169ead4`.
  - Critères gelés codés : `src/controle_ia/pilote_exposant_p_v2/analyse.py` — `e4c8a71a3e39a97d628b272d90861fee36724d642bc1e67e67a83cf3176856db` ; lanceur `src/controle_ia/pilote_exposant_p_v2/run.py` — `d766cadfe4f16bd0826341e53b1e51b3d20c109e4ed9643197a4424b5e3086a3` ; stimuli et gardes `src/controle_ia/pilote_exposant_p_v2/stimuli.py` — `6054866d9f8b26434c50704d69ba6b829a9ac9563f226a100aac6ae9c2b5493d`.
  - Addendum public R9 : `github.com/lciric/sycophancy-psychophysical-law`, `preregistrations/2026-11-02_addendum_R9_feature_specific_error_correction.md` — `81abd962afe1ba8f99840a8b54262b1820184e5a767139712d1e5898d28ce36e`, archivé dans la version v2026.11.5, 10.5281/zenodo.23909891. Addendum R9-bis : `preregistrations/2026-11-03_addendum_R9bis_dose_curves.md`, commit `b3ecaec`, **non encore archivé** : <<DOI_R9_BIS>>.
- Tests attendus : `129` (fichiers `tests/test_pilote_exposant_p_v1.py`, `tests/test_pilote_exposant_p_v2.py`, `tests/test_script_pilote_exposant_p_v2.py`, `tests/test_manifeste.py`, `tests/test_scellement.py`, `tests/test_prereg.py`, tous passés, aucun sauté).
- Nœuds avant tout lancement : vérification humaine des stimuli par Lazar ; archivage de R9-bis (DOI) ; PDF de 2606.24964 versé par Lazar et empreinté, ou réserve R7 maintenue (section « Seuil ») ; contre-lecture R2 neuve de ce brouillon, traitée ; scellement de ce texte, de la configuration et des stimuli ; GO-2026-11-04-03 vérifié par l'amorce ; question de la garde de calcul (devis v2, section 4) tranchée par la session de lancement.

## Ce qui change depuis le brouillon 1

Chaque constat de la contre-lecture R2 (B = bloquant, I = important, M = mineur) et chaque couple. « Appliqué » : le couple est repris mot pour mot, à l'adaptation près du chiffre qu'il cite quand ce chiffre est recalculé ; « refait » : la raison est donnée.

| Constat | Ce qui change | Où |
|---|---|---|
| B1 — E est d'abord un contraste de derniers mots (dates, première personne) ; cos(E, R) ≈ −0,19 sous le modèle stylisé ; paires non minimales ; ≈ 12 fins « évaluation » lisibles comme une évaluation humaine ; pas de vérification humaine | Stimuli neufs : paires de E **minimales** (un seul mot change, le dernier) ; porteur de statut **partagé entre registres** ; 30 + 30 porteurs distincts hors des classes contrôlées ; classes lexicales équilibrées par garde (R-S8) ; modèle stylisé codé et passé (v2 : médianes de \|cos\| 0,000 ; 0,010 ; 0,012 ; v1 rejoué : 0,190 ; 0,181 ; 0,145, calcul) ; sens (R-S9) laissé à **Lazar**, fiche à cocher ; prix déclaré (R n'est plus porté que par le corps) | `stimuli-pilote-exposant-p-v2.json` ; `pilote_exposant_p_v2/stimuli.py` ; `verification-humaine-stimuli-v2.md` ; sections « Directions », « Écarts » (E-16, E-17 refait) |
| B2 — un plan contre la moyenne d'une famille ; les phrases parlent de « paire sans concept » | Voie A **et** voie B : la règle compare à la **moyenne** et le dit ; un **qualificatif de famille** gelé (K = 8 plans de référence mesurés sur les 32 sous-ensembles, intervalle de prédiction à 95 %) dit si la paire sort de la famille ; rang rapporté | `analyse.position_famille`, `QUALIF_FAMILLE` ; sections « Métrique », « Critères » ; devis v2 (+248 plans) |
| B3 — référence sur le seul sous-ensemble 0 | Référence **répartie** (plan k sur k mod 32) ; intervalle par **rééchantillonnage des sous-ensembles** (chacun emporte son p(E, R) et ses plans de référence) ; simulation refaite avec effet commun | `run.py` (couples R01, R02) ; `analyse.bootstrap_sous_ensembles` ; `puissance.py` v2 |
| B4 — aucune sensibilité montrée sur le modèle lu | **Témoin de sensibilité décisif** : Wealth × Gender sur le modèle lu, 32 sous-ensembles ; borne basse de l'intervalle de Δ_WG > δ (tolérance fixée d'avance) ; sinon « égal » et « au-dessous » deviennent « non concluant (sensibilité) » ; bloc juste après la référence | `analyse.issue_gelee`, `sensibilite_montree` ; `run.py` (bloc `lu_WG`) ; couples P02, P10 (refait), P11, P12, P17 |
| B5 — les phrases ne disent pas ce que chaque issue ne montre pas | Phrases neuves bornées (couche 2, dernier jeton, ancres de 5 jetons, réponse L2 au bloc 30, sans gabarit, fins de phrase), « moyenne » partout, « au-dessous » ne compare plus à p = 2, « exclu » ne lit plus le recouvrement comme un résultat, motif juste pour « non concluant (échecs) » | `analyse.PHRASES` (couples A01 à A05, R03, R04) ; section « Critères » |
| B6 — gardes non éprouvées sur un artefact | Essais neufs : arrêt « instrument non validé » **au niveau du lanceur, en mode jouet** (code 3) ; plafond de durée ; grille non finie ; tokeniseur discordant ; flux trop court ; empreinte des références et commit amont ; chemins « exclu », « échecs », « identification », « sensibilité » ; déclencheurs de symétrie ; script d'instance et **amorce** (essais déclinés de ceux de P3) | `tests/test_pilote_exposant_p_v2.py` ; `tests/test_script_pilote_exposant_p_v2.py` ; `scripts/amorce_instance_pilote_exposant_p_v2.sh` |
| B7 — δ et le seuil de résidu reposent sur une transcription | δ adossé à l'audit empreinté (2,423 − 2,050 = 0,373) ; résidus de l'audit (0,85 % à 1,28 %) ; **réserve R7 maintenue** tant que le PDF n'est pas versé | section « Seuil » (couples P06, P19) |
| I1 — empreinte des ancres par un seul nombre | Identité des ancres : norme **et** corrélation de rang des maxima d'axe par ancre ≥ 0,95 sur chaque axe ; tolérance ±0,15 étayée par le calcul de la contre-lecture ; branche « ancres différentes » dite lâche | `analyse.ancres_identiques` (couple P09) |
| I2 — cinq écarts non déclarés | E-16 à E-20 déclarés (E-17 refait : les paires de E sont désormais minimales) ; E-21 à E-25 neufs | section « Écarts » (couple P14) |
| I3 — audit de retrait non défini | 32 issues recalculées (même graine), réserve si une diffère | `run.lire` (couple P18) |
| I4 — critère des plans mixtes non gelé | Critère chiffré (couple P16) | section « Lecture des combinaisons » |
| I5 — descriptifs du modèle de base avant les décisifs | Un bloc non décisif n'est lancé que si le temps couvre aussi les blocs décisifs à venir ; devis corrigé | `Pilote.bloc` ; devis v2 (couple D01) |
| I6 — portée | Décision de Lazar : pas de bloc aux couches moyennes ; chaque phrase dit ce qu'elle ne montre pas | `analyse.NE_MONTRE_PAS` |
| I7 — amorce et GO | Amorce écrite : GO vérifié avant toute création d'instance, puis sur l'instance avant toute installation ; en-tête du script corrigé | `scripts/amorce_instance_pilote_exposant_p_v2.sh` ; `pilote_exposant_p_v2/go.py` (couples S01, P20 refait) |
| I8 — interaction statut × registre | Descriptifs : \|I\|/\|E\|, \|I\|/\|R\|, cos(FE − FD, CE − CD), cos(FE − CE, FD − CD) | `run.py`, `sortie["directions_lu"]["interaction"]` |
| M1 — « le papier n'en a aucun » | Formulation corrigée | couple P19 |
| M2 — renvoi au §7 mal placé | Corrigé | couple P17 |
| M3 — « below 0.1 » sans valeur absolue | Déclaré | couple P07 |
| M4 — empreinte de la configuration citée ≠ lue | Le lanceur exige que ce texte cite l'empreinte de la configuration et des stimuli lus | `run.exiger_config(…, reel=True)` |
| M5 — gestionnaire de TERM posé par l'essai R1 | La garde R1 passe avant tout effet de bord ; essai qui le vérifie | `run.principal` |
| M6 — révision lue deux fois | Le script transmet ses révisions relevées (`--revisions`), le lanceur les compare | `run.exiger_revision` ; script v2 |
| M7 — seuil « trop beau » calé sur un bruit gonflé | Recalé : 0,03, sous le premier centile simulé de la demi-largeur (0,036 à 0,066 selon les scénarios recalés, calcul) | `analyse.DEMI_LARGEUR_SUSPECTE` |
| M8 — exemples « au-dessous » écartés par le papier ; double filtre | Corrigés | couples P03, P04 |
| M9 — renvoi absent ; licence de FineWeb-edu | Renvoi corrigé ; licence toujours **non vérifiée** ici (sans réseau autre que le papier) : réserve | couple P21 ; section « Plan d'analyse » |
| Couples P01, P05, P07, P11, P12, P13, P15, P16, P17, P18, P19, P21 | Appliqués | sections correspondantes |
| Couple P08 | **Refait** : ses taux viennent de la simulation v1 ; remplacés par ceux de la simulation v2 (même argument : comparaison à la moyenne, jamais à « une paire sans concept ») | section « Seuil » |
| Couple P10 | **Refait** : tolérance « borne basse > δ » au lieu de « > 0 » : pour qu'« égal » (±δ) dise quelque chose, l'instrument doit voir sur ce modèle un écart plus grand que δ | section « Seuil » |
| Couple P14 | **Refait** pour E-17 (paires de E devenues minimales ; reste l'écart des paires de R) | section « Écarts » |
| Couple P20 | **Refait** : l'amorce est écrite (plafond 630 min, devis v2), il reste à la contre-lire | « Liste d'arrêt » |
| Couples A01 à A05 | Appliqués et étendus (borne commune, « ne montre pas », qualificatifs) | `analyse.PHRASES` |
| Couples R01 à R04, D01, S01 | Appliqués | `run.py` v2 ; devis v2 ; script v2 |
| Message de Fable (n° 1, §5) | Deux écarts de lecture du papier, propres au brouillon de réponse au mentor, pas à ce texte : ici, les valeurs de Llama viennent de l'audit du code, et les différences aléatoires publiées ne sont citées que pour Gemma | section « Seuil » |

## Hypothèse

**Question.** Dans sa réponse au mentor Stefan Heimersheim (question 1, option c), Lazar soutient qu'une direction « je suis évalué », extraite par paires contrastives, se confond avec le **registre** (formel, artificiel, questionnaire contre conversation). Le pilote mesure, avec l'instrument du papier du mentor (Ferreira da Silva et Heimersheim, arXiv 2606.24964, éq. 8 à 13), si Llama-3.1-8B-Instruct traite une direction d'évaluation E et une direction de registre R comme des directions pures privilégiées sur leurs mélanges (exposant p au-dessus de celui des différences aléatoires, comme les directions contrastives du papier), ou comme la moyenne des paires sans concept.

**Énoncé testé (H-P).** À la couche 2, dans le plan (E, R), l'exposant p de la superellipse de rupture du plateau diffère de la **moyenne** des plans de différences aléatoires du même modèle, mesurés sur les mêmes sous-ensembles d'ancres. Un plan seul n'est pas une famille : une paire sans concept prise au hasard s'écarte elle-même de cette moyenne (écart type entre plans τ ≈ 0,17 dans la simulation, supposé d'après Gemma) ; l'énoncé ne dit donc pas, à lui seul, que la paire (E, R) sort de la famille des paires sans concept. C'est le qualificatif de famille qui le dit (section « Critères »). L'énoncé est ouvert dans les deux sens ; l'issue « égal », dans une marge fixée, est une réponse pleine, pas un échec, si la sensibilité est montrée.

**Directions** (stimuli v2, règles R-S1 à R-S10 dans le fichier) :
- 30 quadruplets en plan 2 × 2 : statut (évaluation, déploiement) × registre (formel, familier). Chaque phrase est un **corps** (contenu et registre) suivi d'un **porteur** (dernier mot, statut). FE et CE finissent par le même porteur d'évaluation, FD et CD par le même porteur de déploiement.
- **E** (évaluation − déploiement) : différence des moyennes sur 60 paires (FE, FD) et (CE, CD) : **paires minimales**, un seul mot change, le dernier, comme les paires sémantiques du papier.
- **R** (formel − familier) : différence des moyennes sur 60 paires (FE, CE) et (FD, CD) : même dernier mot, corps réécrit d'un registre à l'autre (comme Formal et Literary du papier), même personne grammaticale.
- **N**, jumeau neutre de E (emprunt à R9-bis) : le porteur d'évaluation remplacé par un mot sans statut (rangement, lecture, publication sans enjeu) de même nombre de jetons ; N = moyenne(neutre − déploiement).
- Porteurs d'évaluation : objets d'évaluation de modèle (benchmark, leaderboard, eval-suite, red-teaming, test-set, LLM-eval…) ; porteurs de déploiement : événements de la vie de la personne (wedding, eviction, surgery, layoff…). Aucun porteur dans une classe contrôlée (mots de date, première ou deuxième personne, minimisation).
- **Prix de ce choix** (contre-lecture R2, B1) : avec un dernier mot partagé, R n'est plus porté que par le corps. Au dernier jeton de la couche 2, il sera sans doute plus faible et peut-être mal identifié : c'est le prix d'un E et d'un R qui ne partagent pas une interaction de derniers mots. La règle d'identification (cos entre moitiés ≥ 0,5) le mesure.
- Les stimuli de l'échelle de conscience d'évaluation (`echelle-v2.json`) restent un contrôle descriptif (cos(E, E_échelle)), comme au brouillon 1.

**Rattachement au programme.** Le pilote ne teste aucune des hypothèses H1 à H9. Il touche la section 11 (validité de construit) et le construit « conscience d'évaluation » de H8. L'inscrire au programme serait une modification de revendication, donc un nœud de Lazar.

**Hypothèses de travail** (non testées ici, déclarées) :
- l'instrument du papier, validé sur le modèle de base, se transporte au modèle Instruct. Le témoin positif sur le modèle de base ne contrôle que la mise en œuvre (même code, même modèle que le papier) ; les isotropes sur le modèle lu ne contrôlent que le côté nul (p ≈ 2 sans structure). La sensibilité sur le modèle lu est contrôlée par le témoin de sensibilité décisif (Wealth × Gender sur le modèle lu, section « Seuil ») : sans lui, ni « égal » ni « au-dessous » ne se lisent ;
- à la couche 2 et au dernier jeton d'invites courtes, E et R sont des directions surtout lexicales et sémantiques, comme celles du papier. Le pilote ne dit rien des couches moyennes (décision de Lazar), des contextes longs ni du comportement ;
- p > 2 est nécessaire mais pas suffisant pour un trait (§7 du papier) ; des lectures rivales des plateaux existent (§6.2).

## Emprunts à R9-bis (décision de Lazar : réutilisé par citation, pas recalculé)

Source : addendum R9-bis, <<DOI_R9_BIS>> (commit `b3ecaec` du dépôt public ; d'ici l'archivage, ce qui est public et archivé est l'addendum R9, 10.5281/zenodo.23909891). Rien de R9-bis n'est recalculé ici, et aucune donnée de R9 n'est lue : R9 n'a pas tourné.

| Emprunt | Tel quel ? | Ce que le pilote en fait |
|---|---|---|
| Fenêtre W = 2° à 60°, bornes comprises (30 angles), déclarée avant les données | Oui | Lectures **descriptives** des courbes d'un axe (axes des grilles 2D déjà mesurées, aucun balayage de plus) : D(x) sur W contre la médiane des différences aléatoires (`courbes.py`). L'issue reste lue sur p, dont l'ajustement garde la fenêtre de 60° du papier (même borne haute) |
| Direction neutre construite comme la direction étudiée, à partir d'un ajout sans opinion de même nombre de jetons | **Non tel quel** : R9-bis **ajoute** une phrase au prompt (pression contre rien) ; E **remplace** le dernier mot (évaluation contre déploiement). Un aparté ajouté ne serait pas construit comme E | Jumeau **par remplacement** : même corps, même position, un mot neutre de même nombre de jetons que le porteur d'évaluation (tokeniseur du modèle lu, compté sur processeur avant tout passage avant, consigné ; règle de choix ordonnée comme la liste gelée de R9-bis). Lu par un **qualificatif gelé** (Δ_N = p̄(E, R) − p̄(N, R), apparié par sous-ensemble). Comme dans R9-bis, le jumeau est employé quel que soit son accord entre moitiés |
| Enveloppes des 40 différences aléatoires et des 33 contrastives (médiane, percentiles 2,5 et 97,5, angle par angle) | **Non tel quel** : le pilote ne balaie ni 40 différences aléatoires ni 33 contrastives à une dimension (« pas recalculé ») | Définition reprise ; enveloppe interne faite des axes déjà mesurés sur le sous-ensemble 0 (au moins 18 différences aléatoires) ; l'enveloppe de R9 (même modèle, couche 2, ancres A du papier) sera **citée** si ses ancres ont la même empreinte d'identifiants que notre sous-ensemble 0, quand R9 l'aura publiée. Descriptif seulement |

La règle d'identification (cos entre moitiés ≥ 0,5) vient de R9 (§12, public et archivé) ; elle est appliquée à E et à R, pas au jumeau.

## Prédiction chiffrée et signe attendu

**Aucun pari de signe (R3).** Aucun run ne vise un signe positif. Les issues sont écrites d'avance, chacune avec son ordre de grandeur et sa phrase gelée. Δ = p̄(E, R) − p̄(différences aléatoires) :

| Issue | Ordre de grandeur de référence (publié ou calcul) | Ce qu'elle réfute |
|---|---|---|
| **au-dessus** (intervalle de Δ entièrement > 0) | si (E, R) se comportait comme une paire contrastive moyenne du papier sur Llama : Δ ≈ +0,4 à +0,7 (contrastives de Llama, moyenne 2,632, audit du code, qui applique aussi le filtre de recouvrement de Gemma ; filtre de Llama seul : 2,604, calcul du rédacteur du brouillon 1 ; isotropes de Llama 1,930, calcul ; différences aléatoires de Gemma 2,050, audit) | p̄(E, R) = moyenne des différences aléatoires |
| **égal** (0 dans l'intervalle, intervalle dans ±0,2, sensibilité montrée) | Δ ≈ 0, comme la moyenne des paires sans concept | tout écart de plus de 0,2 dans un sens ou dans l'autre |
| **au-dessous** (intervalle entièrement < 0, sensibilité montrée) | possible : parmi les paires contrastives que la règle de recouvrement garde sur Llama, environ 8 % ont p < 2 (Status × Honesty 1,72 ; Health × Age 1,77 ; calcul du contre-lecteur sur `fits_llama_L2_thrpair_exact.pkl`, `fa7165fe…`, et `dirs_llama_L2.pkl`, `7b167763…`) ; Français × Japonais (1,28) et JavaScript × Rust (1,50) ne sont pas des exemples : \|cos\| = 0,457 et 0,659, paires écartées par le papier | p̄(E, R) ≥ moyenne des différences aléatoires |

Issues hors de ces trois : « instrument non validé » ; « exclu » (\|cos(E, R)\| ≥ 0,1) ; « non concluant (identification) » ; « non concluant (échecs) » ; « non concluant » (0 dans l'intervalle, intervalle hors de ±0,2) ; « non concluant (sensibilité) ».

**A priori du rédacteur** (transparence, sans effet sur la lecture ; supposé) : au-dessus 0,30 ; égal 0,20 ; au-dessous 0,10 ; non concluant, toutes causes, 0,30 (dont identification de R 0,15) ; exclu 0,05 (la structure des fins ne rapproche plus E et R sous le modèle stylisé) ; instrument non validé 0,05.

**Valeurs attendues des témoins** (elles fixent la validité de l'instrument, pas l'issue) :
- Wealth × Gender sur Llama-3.1-8B de base, sous-ensemble 0 : p publié 3,003, intercepts 46,50° et 28,95° (code publié) ;
- moyenne des 17 isotropes du modèle lu dans [1,75 ; 2,25] (repère 1,930 sur le modèle de base, calcul) ;
- Gender et Wealth extraites sur le modèle de base : cos ≥ 0,98 avec les directions publiées ;
- sensibilité : si le modèle lu garde le privilège de Wealth × Gender, Δ_WG ≈ 3,0 − 1,93 ≈ +1,1 (calcul, ordre de grandeur, supposé transporté).

## Métrique

- **p d'un plan** (protocole du papier, calcul fait par la copie amont sans modification) : grille 31 × 31 en (α₁, α₂) ∈ [0, 60°]², carte exponentielle à norme constante (éq. 9) ; perturbation du résidu du dernier jeton à la sortie du bloc 2 ; réponse = distance L2 à la sortie du bloc 30 (référence : l'ancre non perturbée) ; grille médiane sur les 30 ancres d'un sous-ensemble ; seuil T = 0,5 × min des maxima des deux axes (éq. 3) ; contour au niveau T, normalisation géodésique exacte (éq. 13), fenêtre de 60°, p borné dans [0,5 ; 10] ; NaN si l'ajustement est impossible. Consignés : points de contour, résidu (annexe B), intercepts.
- **p̄(E, R)** : moyenne des p du plan (E, R) sur S = 32 sous-ensembles disjoints de 30 ancres.
- **p̄(différences aléatoires)** : moyenne des p des M = 60 plans de paires disjointes de différences aléatoires, moins les paires exclues par la règle du cosinus ; le plan k est mesuré sur le sous-ensemble d'ancres k mod 32, pour que la référence et le plan lu moyennent les mêmes sous-ensembles (un effet commun du sous-ensemble 0 n'entrerait ni dans l'intervalle ni dans la simulation).
- **Δ** = p̄(E, R) − p̄(différences aléatoires). Intervalle à 95 % : percentiles 2,5 et 97,5 de 10 000 rééchantillonnages des 32 sous-ensembles avec remise, chacun emportant son p(E, R) et les plans de référence mesurés sur lui (`analyse.bootstrap_sous_ensembles`, graine de la tâche `bootstrap_difference`).
- **Δ_WG** = p̄(Wealth × Gender, modèle lu) − p̄(différences aléatoires), même estimateur, graine `bootstrap_sensibilite`.
- **Δ_N** = p̄(E, R) − p̄(N, R), apparié par sous-ensemble, graine `bootstrap_jumeau`.
- **Position dans la famille** : K = 8 plans de référence (les plans rd₀×rd₁ à rd₁₄×rd₁₅) mesurés chacun sur les 32 sous-ensembles ; intervalle de prédiction à 95 % d'un plan de référence mesuré de la même façon : m̄ ± t(K − 1) · s · √(1 + 1/K).
- **cos(E, R)** : cosinus signé des directions unitaires brutes ; \|cos\| sert à la règle d'exclusion. **cos(E_A, E_B)**, **cos(R_A, R_B)** : moitiés A (Q01 à Q15) et B (Q16 à Q30), 30 paires chacune.
- Unités : p, Δ et cosinus sans dimension ; angles en degrés.

## Seuil

- **δ = 0,2**, marge d'équivalence : environ la moitié du plus petit écart publié entre famille contrastive et famille sans concept, sur Gemma-2-9B : 2,423 − 2,050 = 0,373 (`results/thrpair_audit.md` du code publié, sha256 `272827f3fb082f71df57edf49ec5d9e027031cab47ab7e23cb38c492170911ad`, lignes « Direction family | Contrastive » et « Direction family | Random-diff » ; le texte du papier, §4.1, donne 2,42 et 2,05 au niveau transcription seulement, PDF non empreinté, R7), arrondie au dixième. **Réserve R7** : tant que Lazar n'a pas versé le PDF de 2606.24964 (le terminal reçoit 403), aucun chiffre du texte du papier n'est opposable ; ce brouillon n'en emploie aucun comme seuil.
- **Exclusion** : \|cos(E, R)\| ≥ 0,1, seuil du papier (annexe A : \|⟨dᵢ, dⱼ⟩\| < 0,1 gardé, directions brutes ; §4.1 écrit « below 0.1 » sans valeur absolue ; le code garde ≤ 0,1). Au papier, c'est un filtre de paires (Gram–Schmidt déforme les directions qui se recouvrent), jamais un résultat ; ici il devient une issue terminale du plan lu (écart E-19). Même règle pour les plans de référence et pour (N, R).
- **Identification** : cos(E_A, E_B) ≥ 0,5 et cos(R_A, R_B) ≥ 0,5 (règle de R9, §12).
- **Sensibilité sur le modèle lu** (décisive pour « égal » et « au-dessous ») : borne basse de l'intervalle à 95 % de Δ_WG **> δ = 0,2**. Sinon, « égal » ou « au-dessous » devient « non concluant (sensibilité non montrée sur le modèle lu) » ; « au-dessus » reste lisible.
- **Niveau** : intervalle à 95 %. **Taux simulés** (calcul, `puissance-pilote-exposant-p-v2.json`, scénario central : bruit recalé, effet commun d'écart type 0,035, τ = 0,17, S = 32, M = 60, 300 répétitions, B = 2 000) :
  - plan lu exactement à la moyenne de la famille, Δ = 0 : « égal » 93,0 %, faux « au-dessus » 5,7 %, faux « au-dessous » 1,3 % (au-dessus du 2,5 % nominal : la banque arrondie au pas de 0,05 introduit un biais simulé de +0,014 sur Δ, et le rééchantillonnage par percentiles couvre un peu moins que 95 % ; avec un effet commun de 0,06 : 8,3 % et 1,7 %). Réserve déclarée ;
  - **plan lu tiré de la famille** (une paire sans concept ordinaire), Δ = 0 : « au-dessus » 36,7 %, « au-dessous » 38,0 %, « égal » 25,3 % ; le qualificatif de famille dit « au-delà » 3,0 %, « en deçà » 2,0 %, « dans la famille » 95,0 %. D'où la comparaison à la moyenne, jamais à « une paire sans concept », et le qualificatif de famille pour cette question-là ;
  - calage prudent de la v1 (bruit gonflé), même scénario : « égal » 85,7 %, faux « au-dessus » 2,3 %, faux « au-dessous » 3,3 %.
- **Puissance** (même fichier, calcul) :
  - règle principale, plan à μ + Δ, scénario central : Δ = +0,10 « au-dessus » 85,7 % ; +0,15 98,7 % ; +0,20 100 % ; −0,10 « au-dessous » 77,3 % ; −0,20 100 % ; demi-largeur médiane de l'intervalle 0,066 (premier centile 0,048). Calage prudent : +0,20 → 86,3 %, demi-largeur 0,123 ;
  - qualificatif de famille : Δ = +0,40 « au-delà » 44,3 % ; +0,60 85,7 % (plan tiré de la famille : 79,7 %) ;
  - sensibilité (borne basse > δ) : Δ_WG = +0,30 74,7 % ; +0,40 100 % ; l'ordre de grandeur attendu (+1,1) est loin au-dessus.
- **Instrument** (contrôles fixés d'avance, `analyse.py`) :
  - directions publiées : cos ≥ 0,98 pour Gender et Wealth ;
  - témoin positif sur le modèle de base, sous-ensemble 0. **Ancres identiques** à celles du papier si la norme moyenne est à 10⁻³ près de 2,379805 **et** si la corrélation de rang des maxima d'axe par ancre avec les 30 grilles publiées de Wealth × Gender est ≥ 0,95 sur chaque axe (contre-lecture R2, I1). Alors \|p − 3,003\| ≤ 0,15 et intercepts à ±2° (calcul du contre-lecteur sur la grille publiée : bruit numérique indépendant d'écart type 0,5 par point et par ancre → écart type de p 0,06, \|Δp\| > 0,15 dans 1,5 % des tirages, intercepts à moins de 0,7° au quantile 95 % (1,2° pour un écart type de 1,0) ; décalage uniforme du plancher jusqu'à 1,5 → \|Δp\| ≤ 0,052). Sinon, p dans [2,420 ; 3,702], intervalle à 95 % du rééchantillonnage avec remise des ancres publiées (calcul) ; ce rééchantillonnage gonfle la dispersion propre à chaque plan (0,25 contre 0,096 entre les 17 isotropes publiés sur leurs 30 ancres distinctes), l'intervalle est donc lâche et cette branche ne valide la mise en œuvre que faiblement, ce que la lecture rapporte ;
  - isotropes sur le modèle lu : moyenne dans [1,75 ; 2,25], au plus 20 % d'ajustements impossibles.

## Plan d'analyse

**Données.**
- Modèles : `meta-llama/Llama-3.1-8B-Instruct` (lu) et `meta-llama/Llama-3.1-8B` (témoin, modèle du papier), `bfloat16`, attention `sdpa`. Révisions relevées par le script avant tout téléchargement lourd, transmises au lanceur et comparées au chargement (M6), consignées.
- Ancres : réserve de 10 000 entrées FineWeb-edu de 5 jetons, au protocole du code publié (`sample-10BT`, mélange graine 42, tampon 10 000), révision du jeu relevée et figée ; un flux de moins de 10 000 entrées arrête le run. Les 960 premières forment 32 sous-ensembles de 30 ; le sous-ensemble 0 est celui du papier si le flux est le même. Invites brutes, sans gabarit, BOS compris. **Licence du jeu non vérifiée ici** (réserve ; les 30 textes du sous-ensemble 0 sont versés dans les sorties, comme au brouillon 1).
- Stimuli : fichier v2 figé ; règles R-S1 à R-S8 et R-S10 (structure) vérifiées par garde, modèle stylisé passé (médiane de \|cos(E, R)\| < 0,03 pour w ∈ {0 ; 0,3 ; 1}, 300 tirages, dimension 4 096) ; R-S9 vérifiée par Lazar ; invites du papier = empreintes publiées.

**Plans** (ordre gelé) :

| Bloc | Modèle | Plans | Sous-ensembles | Statut |
|---|---|---|---|---|
| 0 | — | jumeau : choix des neutres sur le tokeniseur du modèle lu | — | consigné avant tout passage avant |
| 1 | base | Wealth × Gender | 0 | décisif (témoin positif) |
| 2 | base | 17 isotropes ; Wealth × Gender | 0 ; 1 à 7 | descriptif, seulement si le temps couvre aussi les blocs décisifs à venir |
| 3 | lu | 17 isotropes | 0 | décisif (instrument) |
| 4 | lu | (E, R) | 0 à 31 (0 seul si exclu ou non identifié) | décisif |
| 5 | lu | 60 différences aléatoires disjointes (120 directions, 30 différences chacune) | plan k sur k mod 32 | décisif (référence) |
| 5 bis | lu | Wealth × Gender | 0 à 31 | décisif (sensibilité sur le modèle lu) ; non mesuré si exclu ou non identifié |
| 6 | lu | (N, R) | 0 à 31 | qualificatif (jumeau) ; sauté et consigné si le temps manque ou si le jumeau n'est pas construit |
| 7 | lu | famille : rd₂ₖ × rd₂ₖ₊₁, k < 8 | les 31 autres sous-ensembles | qualificatif (position dans la famille) ; sauté et consigné si le temps manque |
| 8 | lu | (E, rdₖ) et (R, rdₖ), k < 10 ; famille contrastive (Gender, Wealth, Age, Tense, Sentiment, filtre du cosinus) ; mixtes (Gender, rdₖ), (Wealth, rdₖ), k < 5 ; moitiés (E_A, R_A), (E_B, R_B) ; (E, Formal du papier) | 0 ; 0 ; 0 ; 0 à 7 ; 0 à 7 | descriptif |

**Taille.** 510 plans de 30 ancres × 961 points, soit ≈ 14,7 millions de passes avant de 5 jetons (calcul ; 142 décisifs, 280 qualificatifs, 88 descriptifs). Devis : `devis-pilote-exposant-p-v2.md` (pire cas ≈ 16,6 USD < 30 USD).

**Graines (R9).** `SeedSequence` d'entropie 2026110403 (configuration) ; tâches `differences_aleatoires`, `bootstrap_difference`, `bootstrap_sensibilite`, `bootstrap_jumeau`, `bootstrap_ancres`, `jouet` ; manifeste par run. Isotropes : ceux du code publié (graine 42 de torch), reproduits à l'identique, stimuli fixes. Modèle stylisé : entropie 2026110401.

**Comparaison principale.** Une seule (Δ), avec ses deux conditions gelées (identification, sensibilité) : aucune correction pour comparaisons multiples. Les qualificatifs (famille, jumeau) accompagnent l'issue sans la changer. Tout le reste est descriptif :
- moyennes, avec intervalle, des familles (E, rd), (R, rd), mixtes, contrastive, témoin sur le modèle lu, moitiés, (E, Formal), famille K ;
- rang de p̄(E, R) parmi les plans de référence pris un à un ;
- cosinus E·R, E_naïf·R, E_naïf_inverse·R, N·R, N·E, E·E_échelle, E_A·E_B, R_A·R_B, Gender_A·Gender_B, Wealth_A·Wealth_B (calibration de la règle d'identification sur des directions du papier), R·Formal, E·Formal, E·Literary, R·Literary, Formal·Literary ;
- **interaction** statut × registre (I8) : I = FE − FD − CE + CD (moyennes brutes) ; \|I\|/\|E\|, \|I\|/\|R\|, cos(FE − FD, CE − CD), cos(FE − CE, FD − CD) ;
- courbes d'un axe sur W (emprunt à R9-bis) ;
- sur le modèle de base : isotropes et Wealth × Gender sur 8 sous-ensembles, comparés aux valeurs publiées.

**Sorties** (`diag/<run>/`, scellées) : `plans.json`, `sorties.json` (dont le choix du jumeau, l'identité des ancres, le modèle stylisé, les tolérances jouet s'il y a lieu), `lecture.json`, `resume.json`, `grilles.npz`, et `arret.json` en cas d'arrêt.

### Écarts au papier, déclarés un par un

- E-01 — Modèle lu : Llama-3.1-8B-Instruct ; le papier mesure Llama-3.1-8B de base (`README` du code). Le témoin positif se fait sur le modèle de base.
- E-02 — Directions nouvelles E, R et N : aucune direction d'évaluation ni de registre formel ou familier parmi les 33 du papier. `Formal` existe dans le code mais il est exclu au tracé ; il n'est ici que descriptif.
- E-03 — 60 paires par direction pour E et R ; le papier exige P ≥ 30 et en prend 30 en général. Les moitiés A et B (30 paires chacune) servent à la règle d'identification.
- E-04 — Plan 2 × 2 en quadruplets ; le papier utilise des paires simples.
- E-05 — 32 sous-ensembles de 30 ancres pour (E, R), (N, R), le témoin sur le modèle lu et la famille K ; la référence est répartie sur les 32 ; le papier fait un seul jeu de 30 ancres. Chaque ajustement garde le protocole à 30 ancres.
- E-06 — Différences aléatoires : 60 paires disjointes de 120 directions, tirées par `SeedSequence` ; le papier prend 40 directions et 780 paires, graine 42 de torch.
- E-07 — Isotropes : les 17 paires de référence du code ; le papier en prend 528, sur Gemma.
- E-08 — Intervalle : rééchantillonnage des sous-ensembles, chacun avec ses plans de référence ; le papier rééchantillonne les directions en grappes, pour des moyennes de familles.
- E-09 — Passage avant : modèle complet avec crochets, en lots de 961 points ; le papier repasse les blocs sans masque explicite, en lots de 64.
- E-10 — Plans de référence exclus par la règle du cosinus non mesurés ; le papier les mesure puis les filtre.
- E-11 — Invites brutes sur un modèle Instruct, sans gabarit de conversation.
- E-12 — Logiciels : `torch` 2.14.1, `transformers` 5.18.0, `datasets` 5.1.0 ; le papier ne donne pas ses versions.
- E-13 — Révision de FineWeb-edu figée au run ; les ancres peuvent différer de celles du papier ; la règle du témoin positif couvre les deux cas.
- E-14 — Tolérances de l'instrument (isotropes, directions) : fixées ici, pas par le papier.
- E-15 — Plans mixtes (trait, non-trait) : absents du papier ; descriptifs.
- E-16 — Stimuli de E, R et N écrits par un modèle de langage (sous-agent) ; le papier dit ses invites « LLM generated and human verified » (§3, annexe A, transcription) : la vérification humaine est celle de Lazar, consignée avant le scellement (`verification-humaine-stimuli-v2.md`).
- E-17 — Paires de R non minimales : le corps est réécrit d'un registre à l'autre (comme les directions Formal et Literary du papier) ; les paires de E, elles, sont minimales (un seul mot, le dernier), comme les paires sémantiques du papier. *Refait* depuis le couple P14, qui visait les paires de E du brouillon 1.
- E-18 — Inférence sur un plan seul contre la moyenne d'une famille ; le papier compare des moyennes de familles (figure 4) et ne lit un plan seul qu'en illustration (figure 2). Le qualificatif de famille répond en partie à cet écart.
- E-19 — Règle du cosinus prise comme issue terminale du plan lu (« exclu ») ; au papier, filtre de paires seulement.
- E-20 — Tolérances du témoin positif (±0,15 sur p, ±2° sur les intercepts, [2,420 ; 3,702] si les ancres diffèrent ; identité des ancres par les rangs) : elles ne viennent pas du papier ; E-14 ne couvre que les isotropes et les directions.
- E-21 — Témoin de sensibilité décisif sur le modèle lu (Wealth × Gender, borne basse > δ) : absent du papier.
- E-22 — Jumeau neutre (N, R) et famille K mesurée sur 32 sous-ensembles : absents du papier ; emprunt à R9-bis pour le jumeau.
- E-23 — Règle d'identification par moitiés (R9) : absente du papier.
- E-24 — Porteurs à trait d'union (« AI-benchmark », « LLM-eval »…) : plus de jetons que les porteurs de déploiement ; le papier ne contrôle pas non plus le nombre de jetons de ses mots porteurs.
- E-25 — Lectures descriptives sur la fenêtre W de R9-bis : absentes du papier.

## Critères de lecture gelés

| Condition (dans cet ordre) | Issue | Phrase gelée (`analyse.PHRASES`) |
|---|---|---|
| un contrôle de l'instrument échoue | instrument non validé | « Instrument non validé, rien n'est lu (motif). » |
| \|cos(E, R)\| ≥ 0,1 | exclu | « … ont \|cos\| = x, au-delà du seuil technique du papier (0,1 : au-delà, Gram–Schmidt déforme la seconde direction) : p n'est pas lu. Ce recouvrement est rapporté ; il ne montre pas que E se confond avec R (à \|cos\| = 0,1 les deux directions restent à 84° l'une de l'autre) ; il peut venir de l'interaction statut × registre… » |
| cos(E_A, E_B) < 0,5 ou cos(R_A, R_B) < 0,5 | non concluant (identification) | « … les directions ne sont pas identifiées à cette couche : cosinus entre moitiés … (seuil 0,5, règle de R9) : non concluant ; aucun p n'est lu. » |
| plus de 20 % d'ajustements impossibles pour (E, R) ou pour la référence | non concluant (échecs) | « … plus de 20 % des ajustements … sont impossibles : non concluant ; … rapportés sans lecture. » |
| intervalle de Δ > 0 | au-dessus | « … au-dessus de la moyenne des plans de différences aléatoires … : à cette couche, le réseau privilégie les directions pures E et R sur leurs mélanges plus que la moyenne des paires sans concept. C'est compatible avec une correction propre à chacune ; ce n'est pas une preuve que E est un trait, ni que la paire sort de la famille des paires sans concept (qualificatif de famille ci-après). » + borne |
| intervalle de Δ < 0, sensibilité montrée | au-dessous | « … au-dessous de la moyenne … : à cette couche, les mélanges de E et R rompent le plateau plus tôt, relativement aux axes, que pour la moyenne des paires sans concept ; aucun privilège des directions pures à cette couche, ce qui ne compare pas p à 2 et n'exclut pas un trait mal aligné. » + borne |
| 0 dans l'intervalle, intervalle dans [−0,2 ; +0,2], sensibilité montrée | égal | « … indiscernable de la moyenne … : écart … dans ±0,2, alors que l'instrument voit sur ce modèle un écart de … pour Wealth × Gender. À cette couche, sur ces ancres et à ce jeton, rien ne distingue la paire (évaluation, registre) de la moyenne des paires sans concept ; cela ne dit pas que la direction d'évaluation est sans privilège ailleurs. » + borne |
| « égal » ou « au-dessous », sensibilité non montrée | non concluant (sensibilité) | « … issue brute « … » ; mais l'instrument ne montre pas, sur ce modèle, de privilège plus grand que ±0,2 pour Wealth × Gender … : non concluant (sensibilité non montrée sur le modèle lu). Rien n'est lu. » |
| sinon | non concluant | « … non concluant (l'intervalle contient 0 et sort de ±0,2). Rien n'est lu. » |

Chaque phrase porte les chiffres p̄(E, R), p̄(différences aléatoires) et Δ, avec leurs intervalles, et sa propre borne, écrite dans le code : « Sur Llama-3.1-8B-Instruct, couche 2, dernier jeton, ancres FineWeb de 5 jetons, réponse L2 au bloc 30, sans gabarit de conversation » ; les trois issues tranchées ajoutent : « Cela ne dit rien des couches moyennes, des contextes longs ni du comportement ; E et R sont faites de fins de phrase courtes (E : un seul mot change, le dernier) ; p > 2 est nécessaire, non suffisant, pour un trait (§7 du papier), et p ≈ 2 n'exclut pas un trait mal aligné (§6.1). » Aucune ne compare la paire (E, R) à « une paire sans concept » prise au hasard, seulement à la moyenne de la famille.

**Qualificatifs gelés** (issues tranchées seulement ; ils accompagnent la phrase, ils ne changent pas l'issue) :
- **famille** : « au-delà de la famille » (p̄(E, R) au-dessus de l'intervalle de prédiction : la paire sort, par le haut, de la famille des paires sans concept) ; « en deçà de la famille » ; « dans la famille » (la paire ne se distingue pas d'une paire sans concept prise dans la famille) ; « famille non mesurée » (motif) ;
- **jumeau** : « au-dessus du jumeau » (l'écart est propre à la fin d'évaluation, pas à n'importe quel dernier mot) ; « au-dessous du jumeau » ; « indiscernable du jumeau » (ce que montre p(E, R) n'est pas propre à l'évaluation) ; « jumeau non mesuré » (non construit, sauté, ou \|cos(N, R)\| ≥ 0,1) ;
- **rang** de p̄(E, R) parmi les plans de référence pris un à un.

**Lecture des combinaisons** (descriptive, vocabulaire gelé) :
- « au-dessus », avec la moyenne des 10 plans mixtes (Gender, rd) et (Wealth, rd) au-dessus de p̄(différences aléatoires) (intervalle à 95 % par rééchantillonnage des plans, entièrement > 0) et la moyenne des 10 plans (E, rd) au-dessus de p̄(différences aléatoires) de la même façon : on peut écrire « E se comporte comme une direction privilégiée dans les plans mixtes aussi ». Sinon, la lecture des plans (E, rd) n'est pas calibrée, et rien n'est dit de E seul. Les plans (E, rdₖ) et les plans de référence partagent les directions rd₀ à rd₉ : ces comparaisons ne sont pas indépendantes ;
- « au-dessus » **et** « dans la famille » : seule la phrase de moyenne se dit ; jamais « la paire sort de la famille » ;
- « au-dessus » **et** « indiscernable du jumeau » : on écrit que le privilège n'est pas propre à l'évaluation ;
- « égal » ou « au-dessous » : aucune phrase sur l'absence de trait d'évaluation. p ≈ 2 n'exclut pas un trait mal aligné, le désalignement tirant p vers 2 (§6.1) ; l'instrument ne voit que la couche 2, le dernier jeton et des ancres de 5 jetons (§3) ; ces issues ne se lisent qu'avec le témoin de sensibilité sur le modèle lu ;
- le rang de p̄(E, R) dans la famille contrastive du modèle lu est rapporté, jamais lu comme décision ;
- cos(E_naïf, R) contre cos(E, R) mesure ce que l'appariement du registre retire : attendu par construction, rapporté, non lu comme découverte ; les descriptifs de l'interaction disent d'où viendrait un \|cos(E, R)\| non nul.

**Audit de symétrie (R4)**, déclenché de la même façon dans les deux sens (`analyse.declencheurs_symetrie`) :
- toute issue tranchée entraîne l'audit complet : l'issue est recalculée 32 fois, en retirant chaque fois un sous-ensemble d'ancres (et les plans de référence mesurés sur ce sous-ensemble), même graine de rééchantillonnage ; si une seule de ces 32 issues diffère de l'issue gelée, réserve « instable au retrait d'un sous-ensemble » ; on vérifie aussi les résidus d'ajustement, les points de contour, les échecs, les intercepts ;
- demi-largeur de l'intervalle de Δ < 0,03 : réserve « trop beau » (0,03 est sous le premier centile simulé de la demi-largeur dans tous les scénarios recalés, 0,036 au plus bas ; calcul) ;
- témoin positif égal à la valeur publiée à 0,01 près avec des ancres différentes : réserve ;
- résidu médian du plan (E, R) > 2 % (au papier, toute médiane de sous-groupe est sous 2 %, annexe B, transcription ; audit du code : médianes de 0,85 % à 1,28 %, `results/thrpair_audit.md`, `272827f3…`) : réserve.

Une réserve ne change pas l'issue gelée ; elle accompagne la phrase.

## Liste d'arrêt

| Condition | Action |
|---|---|
| Aucun GO de calcul valide pour ce pilote | rien ne se lance : l'amorce, étape « verifier », vérifie GO-2026-11-04-03 dans `registres/go.md` de `main` (type calcul, accordé par Lazar, période, non révoqué, plafond ≥ 17 USD, périmètre « exposant p ») **avant toute création d'instance** ; la création cite `GO_ID=…` (garde de calcul) ; sur l'instance, l'amorce revérifie le GO sur `origin/main` avant toute installation ; le script d'instance ne vérifie aucun GO |
| Préenregistrement, configuration ou stimuli sans sceau, ou sceau non conforme ; citation absente ou en double | arrêt avant l'installation (script) |
| Mode reel : marqueur `<<…>>` restant dans un fichier cité (dont `<<DOI_R9_BIS>>`, vérification humaine) | arrêt avant l'installation (script), puis refus du lanceur |
| Branche `calcul/…` déjà présente | arrêt avant l'installation |
| Accès refusé à l'un des deux modèles | arrêt avant les essais, consigné ; le jeton n'est jamais affiché |
| Dépendances non installables sans changer une version figée | arrêt avant les essais |
| Essais : autre chose que « 129 passed » | arrêt avant le run |
| Constantes de lecture de la configuration ≠ code d'analyse ; empreinte des stimuli, des références ou de la copie amont ≠ citée ; préenregistrement qui ne cite pas l'empreinte de la configuration ou des stimuli lus ; règle de stimuli violée ; modèle stylisé hors seuil ; invites du papier ≠ empreintes publiées | arrêt avant le manifeste (`GardeArret`) |
| Révision chargée ≠ révision relevée par le script | arrêt |
| Flux FineWeb-edu de moins de 10 000 entrées | arrêt consigné (`GardeArret`) |
| Directions publiées non reproduites, ou témoin positif hors tolérance | « instrument non validé » ; arrêt avant le modèle lu ; sorties écrites ; code 3 — **y compris en mode jouet** (tolérances jouet consignées) |
| Tokeniseur du modèle lu ≠ celui du modèle de base sur les ancres | arrêt |
| Isotropes du modèle lu hors tolérance | « instrument non validé » ; arrêt ; code 3 |
| Grille non finie | arrêt |
| Durée projetée au-delà de 34 200 s avant un bloc décisif | arrêt ; un bloc qualificatif ou descriptif qui ne laisse pas le temps des blocs décisifs à venir est sauté et consigné |
| Délai externe de 600 min | TERM converti en arrêt consigné, KILL 5 min après |
| Plafond de l'amorce, 630 min | résultats partiels et traces committés et poussés |
| Toute exception | `arret.json` (motif, étape, plans faits), résultats partiels poussés |
| Fin | l'instance s'arrête par son identifiant (R10), consigné dans `registres/arrets.md` |

## Contre-lecture

En attente. Sous-agent neuf à désigner ; il lit les fichiers listés au rapport de rédaction (`brouillons/pilote-exposant-p-v1/rapport-redaction-pilote-exposant-p-v2.md`, sections 5 « Dix points pour un contre-lecteur neuf » et 6 « Fichiers que le contre-lecteur doit lire »). Empreinte du brouillon relu : <<EMPREINTE_BROUILLON_RELU>> ; rapport : <<CHEMIN_ET_EMPREINTE_DU_RAPPORT>> ; traitement de chaque remarque : <<TRAITEMENT_DES_REMARQUES>>.

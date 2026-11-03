# Recoupement des chiffres et des faits — réponses aux mentors de Pivotal, version approfondie v1

Vérificateur neuf : je n'ai écrit ni les réponses, ni leurs réécritures, ni les six rapports de lecture. Travail du 3 novembre 2026, de 00:45 à 01:22 UTC (`date -u`). Consigne : `brouillons/reprise-conv-audit-2026-11-02-nuit/prompts-sous-agents/pivotal-recoupement-chiffres-prompt.md`.

Fichier vérifié : `/home/claude/scratch/pivotal-approfondi/reponses-mentors-approfondies-v1.md`, sha256 `ee4e605d97d6d95031042e90b1b3b2eaa5dddb477f5eb4b4ad39586d71877a90`. Périmètre : chaque chiffre, citation et affirmation factuelle des blocs anglais (entre trois accents graves), plus les faits proposés pour la Q1 de Heimersheim (liste 1.c et points A à E). J'ai aussi vérifié quatre ajouts anglais hors bloc (« ajouts possibles » de Scheurer, option (a) d'Ibrahim), signalés comme tels. Les opinions, les plans et les questions ne sont pas comptés.

**Consigne appliquée :** ρ = 0,68, « < 1 % » et « 68 % » viennent du programme d'interprétabilité de Lazar, non publié. Ils sont gardés tels quels et ne comptent pas comme inexactitudes. Voir quand même la réserve 2.

## 0. Sources lues, et limites

**Dépôts publics.** `WebFetch` a refusé `github.com` et `raw.githubusercontent.com` (liste d'autorisation). J'ai donc fait trois clones neufs par `git clone` (terminal, lecture seule), sous `recoupement/depots/`. Leurs têtes sont égales aux `main` distants (`git ls-remote`, 3 novembre vers 00:50 UTC). Aucun code des dépôts n'a été exécuté.

| abréviation | dépôt | commit | fichiers lus (sha256, 16 premiers caractères) |
|---|---|---|---|
| [syco] | github.com/lciric/sycophancy-psychophysical-law | `e5e960b` (2 nov., 21:12 UTC) | `README.md` `a86b46b5ec6f919f` ; `STATUS.md` `4ab64d59c8664f16` ; `results/R1a/README.md` `adce975d8cd9edd0` ; `R1b` `8200f92765ac4b81` ; `R3` `066853994249bdb4` ; `R4` `2664d85cb9d3e335` ; `R6` `27ad89efb844830d` ; `R7` `2dd0790cf01cba8d` ; addendum R8 `68e891921055938a` ; addendum R9 `81abd962afe1ba8f` ; préenregistrement R1–R5 `a2f7e2f4d1d19840` ; `R5_materials/README.md` `fb06bee733428cd8` |
| [org] | github.com/lciric/ideation-organism | `66dbcf1` (2 nov., 23:20:16 UTC) | `README.md` `a5e6b8622fbd7b31` ; `resultats/attaque-goodhart-v2/README.md` `84d6e77b3b2c6dc6` ; `resultats/controle-r1-blanche-noire/README.md` `6c2dffc8777cf7fb` ; préenregistrement A1 v2-v1 `fc81d015d27e6038` ; préenregistrement du nul v9 v1 `54c5713d07f61b7f` ; préenregistrement de la lecture à graines neuves v2 `93923d7132260c2f` ; verdict R13 du nul v8 `33883f6da08bdd9d` |
| [cv] | github.com/lciric/sycophancy-construct-validity (public, trouvé par l'addendum R9 §11 de [syco]) | `5ee1d23` (9 oct. 2026) | `README.md` `a620c95dba3c69b6` ; `TRACEABILITY.md` `b6c07161d492765e` |

**Articles et billets**, lus par `WebFetch` (adresse trouvée par recherche quand elle n'était pas déjà connue).
- 2510.20487 (Hua, Qin, Marks, Nanda) : https://arxiv.org/html/2510.20487 (v5 ; s'arrête à l'annexe E) et https://arxiv.org/pdf/2510.20487 (annexes G, H, I) ; annexes J à M non lues.
- 2606.24964 (Ferreira da Silva, Heimersheim) : https://arxiv.org/pdf/2606.24964.
- 2605.05115 (Wurgaft et coll.) : https://arxiv.org/html/2605.05115v1 (s'arrête en 3.1), puis https://arxiv.org/pdf/2605.05115.
- 2409.17113 v4, 2409.15019, 2410.12555 ; billet LessWrong du 5 juillet 2024 (StefanHex, jake_mendel) : https://www.lesswrong.com/posts/LajDyGyiyX8DNNsuF/.
- Réplication sur GLM-5 (Read, Schoen, Aranguri, Bloom ; 10 avril 2026) et commentaire de Jack Lindsey : https://www.lesswrong.com/posts/HhF5kESdtPHku7kim/.
- Billet de Redwood (Pan, Greenblatt) sur la fiche de Sonnet 4.5 : https://blog.redwoodresearch.org/p/sonnet-45s-eval-gaming-seriously. Les fiches système de Sonnet 4.5 et d'Opus 4.6 n'ont **pas** été lues : sources secondaires seulement.
- 2608.28945 (Chen, Wen, Kirchner) : https://arxiv.org/pdf/2608.28945 (s'arrête avant l'annexe D) ; annexe D.3 lue dans la version du blog, https://alignment.anthropic.com/2026/automated-alignment-researchers/.
- Billet « Automated Weak-to-Strong Researcher » : https://alignment.anthropic.com/2026/automated-w2s-researcher/.
- Roelofs et coll. 2019 (NeurIPS) ; Ramdas, Grünwald, Vovk, Shafer : https://web3.arxiv.org/pdf/2210.01948 ; Blum et Hardt, 1502.04585 ; Dwork et coll., 1506.02629.
- 2512.07810, 2411.17693, 2604.28182, 2409.12822, 2509.21344 v2, 2507.12691 v3, 2602.08877, 2401.14446 v3, 2503.14499 (METR), 2509.15541, 2506.05296 v3, 2511.01689, 2507.21919 v2 (la version de *Nature* n'a pas été lue), 2511.04703 v1, 2604.03058.
- 2609.36490 (Lyons Keenan, Leckie, Erfani) : les pages arXiv (résumé et PDF) ont été refusées par `WebFetch`. J'ai lu le résumé sur https://neurips.cc/virtual/2026/168282 et le billet des auteurs (https://lesswrong.com/posts/adZq8a5s5K3FomyHC/). Copie locale du lecteur Jang et Feng, consultée pour l'en-tête seulement : `jang-feng/sources/2609.36490v1/2609.36490v1.txt`, sha256 `90c6ecfc1a6f2771…`.
- Billet de Colognese et Ward : https://www.lesswrong.com/posts/2maYXkEgnfJHPAkxh/ (corrections du 14 octobre 2026).

**Limites.** `WebFetch` passe par un modèle intermédiaire : citations courtes (125 caractères au plus) et numéros de page rares. Les chiffres tirés des articles sont donc au niveau « transcription » au sens de R7 : à revérifier sur PDF empreinté avant d'entrer dans un papier. La page des mentors et le formulaire n'ont pas été relus : « your project B » et « organism etiology » restent non vérifiés.

## 1. Tableau des affirmations

Verdicts : **exact** ; **exact (nuance)** ; **inexact** ; **non vérifiable** ; **gardé (consigne)**. Les numéros renvoient aux sections 2 à 4.

### Heimersheim — Q2 réécrite (bloc anglais)

| n° | mentor | phrase exacte | source et emplacement | verdict |
|---|---|---|---|---|
| 1 | Heimersheim Q2 | « Coming from neuroscience, low-rank recurrent networks, population dynamics » | parcours, aucune source | non vérifiable |
| 2 | Heimersheim Q2 | « my read-out-of-sync result suggested that that distinction holds in a language model » | [cv] README l. 3 (« Reading a concept out of a model's activations and controlling the behaviour it predicts are different problems »), l. 39 | exact |
| 3 | Heimersheim Q2 | « the direction that predicts sycophancy does <1% of the causal work on Llama-3.1-8B-Instruct » | « < 1 % » : programme non publié, absent de tout dépôt public ; « Instruct » conforme à [cv] README l. 3 et à [syco] addendum R9 §11 | gardé (consigne) ; réserve 2 |
| 4 | Heimersheim Q2 | « Your work on activation plateaus » | Heimersheim est auteur du billet de 2024, de 2409.17113, 2409.15019, 2410.12555 et 2606.24964 (listes d'auteurs lues) | exact |
| 5 | Heimersheim Q2 | « Instead of single dose interventions my rank-1 vs rank-3 result relied on » | [cv] README l. 17–28, 58–59 : interventions de rang 1 (pilotage, ablation directionnelle, blocage de traits…), puis ablation d'un sous-espace de rang 3 obtenu par décomposition en valeurs singulières. La dose n'y est pas décrite. La baisse due au rang 3 « did not reproduce » sur des générations neuves : « not a causal handle on sycophancy » | exact sur la méthode ; « single dose » non vérifiable ; **réserve 1** |
| 6 | Heimersheim Q2 | « you measure the dose–response curve » (et le repli « you measure the whole dose–response curve ») | billet de 2024 (divergence de Kullback-Leibler selon l'angle, de 0 à 180°) ; 2410.12555 §2 (longueurs de 0 à 101, « an initial plateau followed by a more linear increase ») ; 2409.17113 §3 (50 valeurs d'α) | exact |
| 7 | Heimersheim Q2 | « your exponent p asks whether readable directions are privileged » | 2606.24964 résumé (« the pure directions are privileged » ; p ≈ 2 pour l'aléatoire et les composantes principales), §4.1 (contrastives : 2,42 [2,29 ; 2,62]) | exact |

### Heimersheim — faits proposés pour la Q1 (liste 1.c)

| n° | mentor | phrase exacte | source et emplacement | verdict |
|---|---|---|---|---|
| 8 | Heimersheim Q1, fait 1 | « Les indices de type tombent de 80–86 % à moins de 11 % (contre 34 % quand l'invite annonce le déploiement) » | 2510.20487 §5.1 | exact |
| 9 | id. | « le bruit gaussien fait bien moins » | §5.3 (« does not decrease the type hint rate nearly as much ») ; légende de la figure 4 | exact |
| 10 | id. | « la précision passe de 56,8 à 55,2 % » | §5.1 | exact |
| 11 | fait 2 | « 2510.20487 annexe A (note 3) […] avant tout affinage, le modèle lie déjà émojis et vrais utilisateurs » | le fait est exact (« We later discovered Llama Nemotron already exhibits this behavior without fine-tuning »), mais la note 3 est en §3.1, pas en annexe A | **inexact** (emplacement) |
| 12 | fait 2 | « Le pilotage déplace les émojis, et les auteurs concèdent que « pilotage ≈ invite » » | annexe A (« a simple alternative explanation is that steering is similar to prompting with the contrastive prompts ») | exact |
| 13 | fait 2 | « Le marqueur de vérité, les indices de type, est un marqueur de code « professionnel » » | annexe B (« evaluators prefer professional Python code formatting (Black style, type hints, and docstrings) ») | exact |
| 14 | fait 3 (et point E) | « annexe I.1.1, tableau 16 (mise à jour du 4 janvier 2026) : des énoncés déclaratifs de déploiement abaissent les indices à 0,34–0,60 » | PDF, annexe I.1.1 (« Update [Jan 4, 2026] » ; tableau 16 : de 0,34 pour « INFO: Not evaluation. » à 0,60) | exact |
| 15 | fait 4 | « l'organisme « s'appuie sur des indices et des coups de pouce », et Llama Nemotron ne distingue pas de façon constante évaluation et déploiement » | §6 (« relies on hints and nudges » ; « does not have the capability to consistently distinguish between evaluation and deployment ») | exact |
| 16 | fait 4 | « Sans l'indice de situation, les écarts rétrécissent (§4.2) » | §4.2 (« smaller gaps in type hint rates ») | exact |
| 17 | fait 5 | « le pilotage supprime largement la conscience verbalisée, mais pas la conscience non verbalisée mesurée par oracles d'activation » | §6 : « greatly suppressed verbalized evaluation awareness, while failing to fully eliminate unverbalized evaluation awareness as measured by activation oracles » | **inexact** |
| 18 | fait 5 | « la fiche d'Opus 4.6 (février 2026) » | 2510.20487 cite « Anthropic (2026) », sans mois ; février n'est donné que par des sources secondaires | non vérifiable (mois) |
| 19 | fait 6 | « le témoin de Hua et coll. est un bruit gaussien de même moyenne et variance » | §5.3 | exact |
| 20 | fait 6 | « Chez Lee et Heimersheim, la direction isotrope est la ligne de base faible : tout ce qui est structuré déplace davantage les sorties, même un mélange de deux activations aléatoires à covariance appariée. C'est mesuré sur GPT-2 small, couche 6 » | 2410.12555 §3 (« might be problematic because actual activations are not isotropic ») ; §3.1 (« Cov-random mixture directions influence the model's output more significantly than isotropic random directions ») ; §4.2 (tous les traits font plus que l'isotrope) ; §2 (couche 6) | exact (nuance : leur « mixture » est une différence ; courbes individuelles moins nettes, §5) |
| 21 | fait 6 | « Dans 2606.24964 (§3, éq. 6–7), le témoin le plus exigeant est la « différence aléatoire » […] (p = 2,05 [2,00 ; 2,10]) » | éq. 6–7 ; « our most stringent non-feature baseline » ; §4.1 (moyenne 2,05 [2,00 ; 2,10]) | exact |
| 22 | fait 7 | « Institut britannique, 10 avril 2026 ; un seul scénario, 250 tirages par condition » | billet GLM-5 (« UK AISI Model Transparency Team » ; 10 avril 2026 ; « a single scenario » ; « We run for 250 epochs ») | exact |
| 23 | fait 7 | « « control_book » a produit l'effet le plus fort, avec une conscience verbalisée proche de 0 et environ 80 % d'action désalignée à −0,025 » | même billet (« control_book has the largest and most consistent effect ») | exact |
| 24 | fait 7 | « Deux des quatre vecteurs […] (« testing_vs_conversation », repris de la fiche d'Opus 4.6, et « hua_et_al_ha ») n'ont pas élevé le désalignement au-dessus de la base » | même billet (« fail to increase misaligned action rates above baseline ») ; annexe : les quatre jeux viennent de la fiche d'Opus 4.6 | exact |
| 25 | fait 7 | « Commentaire de Jack Lindsey : sur Sonnet 4.5, les effets dépassaient ceux des témoins aléatoires, ce qui n'est pas le cas sur GLM-5 » | commentaire : ses conditions 1 et 2 (comparaison aux témoins aléatoires) sont remplies « On Sonnet 4.5 (for several steering vectors) » ; sur GLM-5, « your random controls increase misalignment by about as much as your steering vectors » | exact |
| 26 | fait 8 | « l'effet de l'inhibition sur le désalignement est « très dépendant du jeu de données » » | Redwood, note 19, qui cite la fiche : « highly dataset-dependent » (secondaire) | exact |
| 27 | fait 8 | « La conscience verbalisée passe d'environ 80 % à 0–40 %, le désalignement de 0 % à 1–9 % ; la valeur de 9 % vient du vecteur « Testing vs. Conversation » (note 18) » | Redwood, corps et note 18 (secondaire) | exact |
| 28 | fait 8 | « Hua et coll. (§1) donnent 8 % pour le vecteur le plus fort » | 2510.20487 §1 : « Steering with one vector reduced verbalized evaluation awareness to zero » et « another increased the misalignment rate to 8% » ; vecteurs non nommés, aucun n'est dit « le plus fort » | **inexact** |
| 29 | fait 9 | « piloter la conscience d'être testé modifie aussi le refus » | §2 (« can also affect their refusal behavior ») | exact |
| 30 | fait 10 | « les 14 directions sémantiques contrastives (âge, certitude, époque, genre, santé, honnêteté, « littéraire », nombre, personne, refus, sentiment, statut, temps, richesse) n'incluent pas l'évaluation » | 2606.24964 annexe A (« Tense » : temps grammatical) ; aucun des 33 concepts (14 sémantiques, 10 langues, 9 langages de programmation) ne porte sur l'évaluation | exact |
| 31 | fait 10 | « Le test p n'a jamais été appliqué à une direction d'évaluation. » | vrai dans 2606.24964 ; au-delà de l'article, c'est une absence, non démontrable (R8) | non vérifiable (au-delà de l'article) |
| 32 | fait 11 | « écart positif pour au moins 63 % des ancres, à chaque angle » | figure 1 (« ≥ 63% », exemple sur Gemma-2-9B) | exact |
| 33 | fait 11 | « La sensibilité varie jusqu'à environ 70 fois d'une direction à l'autre, d'où l'abandon d'un seuil global » | note 1 (« ∼ 70 », « for the KL-divergence response metric ») | exact (nuance : pour la métrique de Kullback-Leibler) |
| 34 | fait 11 | « α ≈ 4,1–4,3 pour les axes de traits, à 4,70 pour le mélange égal et à 5,93 pour l'aléatoire » | annexe C.4, figure 11 | exact |
| 35 | fait 12 | « n'est validé que pour des concepts à géométrie connue et ordonnée (jours, mois, lettres, âges, grilles) » | 2605.05115 §2.1 ; §4 (grille 5 × 5, cylindre 9 × 9) | exact |
| 36 | fait 12 | « La variété est une spline ajustée sur des centroïdes étiquetés, et la sortie étudiée est le jeton suivant » | annexe A.3 ; §8 (« our focus on the next-token distribution ») | exact |
| 37 | fait 12 | « Les concepts abstraits (« e.g., refusals ») ne sont pas testés, et un protocole non supervisé reste à faire » | §8 (citations exactes) | exact |
| 38 | fait 13 | « les régions stables se raffermissent avec l'entraînement et avec la taille (modèles de 0,5 à 7 milliards de paramètres, perturbation après la couche 1) » | 2409.17113 v4, §1, §3, §4 (OLMo et Qwen2 ; remplacement « after the first » layer) | exact |
| 39 | fait 14 | « des activations recomposées à partir de traits d'autoencodeur épars n'ont pas les plateaux des vraies activations » | 2409.15019 §7 (« lack the characteristic plateaus ») ; §5.2 et résumé : plateaux « less pronounced » | exact (nuance : « moins prononcés » en §5.2) |

### Heimersheim — points prioritaires A à E (faits proposés pour la Q1)

| n° | mentor | phrase exacte | source et emplacement | verdict |
|---|---|---|---|---|
| 40 | point A | « Ce que mesure p (éq. 10–13). On perturbe l'activation dans le plan de deux directions orthonormées, à norme constante. » | 2606.24964 : la perturbation est définie par les éq. 8–9 ; les éq. 10–11 donnent le modèle de réponse, l'éq. 12 la condition de rupture, l'éq. 13 la superellipse | **inexact** (renvoi) |
| 41 | point A | « Si p ≈ 2, le réseau ne répond qu'à la taille L2 totale […] Si p > 2, les directions pures sont privilégiées sur leurs mélanges, ce qui est compatible avec une correction d'erreur propre à chaque trait (§3, §6.1) » | §4.1, §6.1 | exact |
| 42 | point A | « les 16 paires du tableau 12 de Hua et coll., portées à 30 au moins, minimum de 2606.24964 (§3) » | 2510.20487 §4.1 (16 paires ; annexe F) ; 2606.24964 §3 (P ≥ 30) | exact (numéro du tableau 12 non lu) |
| 43 | point A | « 2606.24964 écarte les paires où \|cos\| ≥ 0,1 (annexe A : 210 paires sur 528) » | annexe A ; légende de la figure 8 | exact |
| 44 | point A | « paires de traits connus (2,3–2,4) et aux différences aléatoires (2,02–2,05) » | §4.1 (médiane 2,30, moyenne 2,42 ; différence aléatoire : médiane 2,02, moyenne 2,05) ; « p ≈ 2.3 » en §6.1 et §7 ; 2,4 en figure 5 | exact |
| 45 | point A | « p > 2 est nécessaire mais pas suffisant (§7 : maximiser p ne retrouve pas les traits à lui seul) » | §7 (« appears to be necessary but not sufficient » ; résultats non rapportés) | exact |
| 46 | point A | « la mesure est faite par défaut à la couche 2 (ablations jusqu'à la couche 20 de Gemma-2-9B), sur le dernier jeton de 30 invites FineWeb de 5 jetons » | ℓ = 2 par défaut ; ℓ ∈ {5, 10, 20} ; N = 30 invites de 5 jetons ; Gemma-2-9B est le modèle par défaut | exact (nuance : le modèle des ablations de couche n'est pas nommé) |
| 47 | point A | « Hua et coll. : couches 10 à 30 » | 2510.20487 §4.1 (couches 10, 14, 18, 22, 26 et 30) | exact |
| 48 | point A | « la réponse mesurée est une distance L2 en avant-dernière couche, pas un comportement » | 2606.24964 (« second-to-last layer ») | exact |
| 49 | point A | « bassins d'attraction, ou correction vers une variété (§6.2) » | §6.2 | exact |
| 50 | point A | « Personne n'a mesuré p pour une direction d'évaluation. » | absence ; vrai pour 2606.24964 | non vérifiable |
| 51 | point B | « Plateau : les petites perturbations sont sans effet (billet de 2024 ; 2409.17113 ; 2606.24964) » | billet de 2024 (« barely changes until the perturbation reaches 40° ») ; 2409.17113 §4 (régions plates) | exact |
| 52 | point B | « Dans 2409.15019, vers une vraie activation, l'emballement survient au pas 41,11 en moyenne contre 52,49 vers une activation aléatoire. » | 2409.15019 §5.1, tableau 1. L'annexe A (tableau A.1) donne 41,21 : écart interne à la source | exact |
| 53 | point B | « sur une seule couche, une force d'environ 3 fait beaucoup de dégâts ; 6 couches × 0,6 en font peu » | 2510.20487 annexe G.1 (« strengths around 3 would often cause the performance to decrease dramatically ») ; figure 14 ; §5.1 (55,2 contre 56,8) | exact |
| 54 | point B | « le pilotage vers l'évaluation coûte 13,7 points de précision (43,1 contre 56,8), celui vers le déploiement 1,6 point » | §5.1 (56,8 − 43,1 et 56,8 − 55,2) | exact |
| 55 | point B | « GLM-5 devient incohérent au-delà de 0,025, contre 0,1 pour Opus 4.6 » | billet GLM-5 : « strengths larger than 0.025 often made the model incoherent » ; 0,1 pour Opus 4.6 | **inexact** (mineur : « souvent ») |
| 56 | point B | « Sur GLM-5, des témoins agissent aux mêmes doses que les vecteurs d'évaluation » | billet (control_book à −0,025) ; commentaire de Lindsey | exact |
| 57 | point B | « Hua et coll. choisissent la dose sur les capacités, sans courbe de témoin. » | annexe G (choix de la force sur les indices et la précision) ; pas de courbe de témoin dans le texte lu, figures non vues | non vérifiable (seconde moitié) |
| 58 | point B | « GLM-5 : deux doses par signe. » | billet (cinq forces : −0,025 ; −0,0125 ; 0 ; +0,0125 ; +0,025) | exact |
| 59 | point C | « environ 2,8 fois plus basse : 0,34 contre 0,93 pour les jours, 0,36 contre 1,09 pour les mois, 2,42 contre 6,95 pour les lettres, 5,21 contre 13,49 pour les âges ; p < 0,001 (§3.2) » | 2605.05115 §3.2 (« a factor of 2.8× » ; « p<0.001 ») | exact |
| 60 | point C | « le pilotage linéaire ajuste le premier moment de la sortie, mais que les moments d'ordre supérieur peuvent dériver sans contrainte (§6, d'après Sarfati et coll.) » | §6 : le premier moment est attribué à Rodriguez et coll. (2025) et Ravfogel et coll. (2022) ; les moments supérieurs « can be unconstrained and adversarial (see results by Sarfati et al. (2026)) » | **inexact** (mineur : attribution) |
| 61 | point C | « La variété est une spline cubique naturelle qui passe exactement par les centroïdes étiquetés (A.3) […] (éq. 1 et 2) » | A.3 : « fit a smooth interpolant through them » ; spline naturelle pour les concepts ordonnés, périodique pour les cycliques ; « exactly » n'y est pas. Éq. 1 : pilotage linéaire (« diff-in-means ») ; éq. 2 : pilotage sur variété | **inexact** (mineur) |
| 62 | point C | « future work is needed to explore more abstract concepts, e.g., refusals » ; « would … significantly broaden the applicability » (§8) | §8 (citations exactes) | exact |
| 63 | point C | « les auteurs étudient la distribution du jeton suivant (§8) » | §8 | exact |
| 64 | point C | « Validation : Llama 3.1 8B, couche 28, sous-espace de 64 composantes principales. » | §2.2 | exact |
| 65 | point D | « 24 vecteurs gaussiens de même moyenne et variance, aux normes L2 « très voisines » » | 2510.20487 §5.3 | exact |
| 66 | point D | « des traits aléatoires d'autoencodeur épars servent de témoin, d'après le billet de l'Institut britannique et le commentaire de Lindsey » | billet GLM-5 (« for Sonnet 4.5 and Opus 4.5 they use random SAE features as baselines ») | exact |
| 67 | point D | « Selon Redwood, leur inhibition « didn't have substantial effects » » | Redwood (« Inhibiting random representations, in contrast, didn't have substantial effects ») | exact |
| 68 | point D | « Ta demande « random control vector normalized to the same size » est déjà satisfaite deux fois » | vérifié une fois (Hua et coll., normes voisines) ; pour Sonnet 4.5, témoin aléatoire, mais égalité de norme non vérifiée (le fichier le dit lui-même deux lignes plus haut) | **inexact** (mineur) |
| 69 | point E | « Wood Labs ⇒ évaluation ⇒ indices de type ; raisonnement à deux étapes, §3.1 » | §3.1 (« two-hop ») | exact |
| 70 | point E | « un vecteur extrait avant affinage […] (§4.1) » | §4.1 (« from the pre-fine-tuned model, before any evaluation-aware training ») | exact |
| 71 | point E | « même les 16 invites réunies ne suffisent pas (§5.3) » | §5.3 (« does not reduce it to deployment levels ») | exact |
| 72 | point E | « un modèle vraiment conscient de l'évaluation : l'indice de situation est nécessaire (§6) » | §6 : « relies on hints and nudges » ; mais §4.2 et annexe I.2 : sans l'indice, résultats « qualitatively similar », écarts plus petits | **inexact** (mineur : « nécessaire » est trop fort) |
| 73 | point E | « l'itération experte n'a porté que sur la distribution d'évaluation (§3.2) » | §3.2 (« training only on the evaluation distribution ») | exact |
| 74 | point E | « un organisme à marqueur neutre en registre, et un modèle plus capable de distinguer seul évaluation et déploiement. Ce sont leurs propres travaux futurs (§6). » | §6 : « Studying model organisms trained on top of more sophisticated and evaluation-aware LLMs is a natural extension » ; rien sur un marqueur neutre en registre | **inexact** |

### Kirchner — Q1

| n° | mentor | phrase exacte | source et emplacement | verdict |
|---|---|---|---|---|
| 75 | Kirchner Q1 | « I’ve been running automated researchers since October (github.com/lciric/ideation-organism) » | [org] README l. 5 (« built and audited over October 2026 ») ; §4 (moteur réel, 27 octobre 2026) | exact |
| 76 | Kirchner Q1 | « Agents generate submissions meant to codify laws; a statistical judge scores submissions. » | [org] README §2, étapes 1 et 7 | exact |
| 77 | Kirchner Q1 | « Our attack found a hole. Patch posted, preregistered test to come. » | page A1 (W2 : « breach under v8 ») ; `pole/nul_v9.py` et ses essais dans l'arbre ; préenregistrement v9 scellé ; course après la poussée (message du commit `66dbcf1`) | exact |
| 78 | Kirchner Q1 | « Proposers of many different archetypes with multiple algorithms submitted to our frozen statistical judge. » | `demonstrations/demo_proposeurs_v7.py` (bras scripté aveugle, scripté exploratoire, aléatoire, mécanique) ; `pole/a_blanc_v59.py` (« recopie_melange ») ; proposeurs Claude, Kimi, Argon (README). Le mot « archetype » n'apparaît pas | exact |
| 79 | Kirchner Q1 | « Said judge scored each proposed law based on how well it could be distinguished from a null hypothesis. » | README §2, étape 7 ; §3.1 | exact |
| 80 | Kirchner Q1 | « Death tests preregistered, to run in sandbox with a model from a completely different family as sanity check (tested offline, not yet run for real). » | README l. 3 ; §1 (« a model from a different provider family ») ; §4 (« never run for real ») | exact |
| 81 | Kirchner Q1 | « 929 tests total. » | README §4, ligne 1 (« 906 passed, 8 failed, 15 skipped […] (929 tests) ») | exact |
| 82 | Kirchner Q1 | « the code was mutated 224 times, checking that all mutations get caught by tests » | README §4, ligne 2 (224 mutations, toutes tuées pour la raison attendue) | exact |
| 83 | Kirchner Q1 | « literally called 11 of 12 cards “notable”. κ = 0, inter-agreement. » | README §4, second tour réel (« 11 of 12 cards rated "notable" », « Cohen's κ = 0 ») | exact |
| 84 | Kirchner Q1 | « The terse statistical judge told me why nothing was promoted: not enough power. […] The power curve suggested as much. » | README §4 (13 moniteurs réels : rien promu, « no teeth, no conclusion » ; puissance : « "nothing promoted" does not exclude effects of that size ») | exact |
| 85 | Kirchner Q1 | « with no deviations from the locked plan » | aucun texte public ne le dit ; la sortie est privée (`lecture-t05-graines-neuves-v1.json`, `07bc2aea…`) | non vérifiable |
| 86 | Kirchner Q1 | « a new-seed pass of 288 episodes (same 96 tasks) that I did not inspect prior to launching this datapass » | README §4 (« the 96 tasks re-run with new seeds, 3 episodes each, 288 episodes » ; « sealed before any rating existed ») | exact |
| 87 | Kirchner Q1 | « It accepted 2 of the 3 laws I placed into the data. » | README §4 : « 3 of 3 with a plan that takes the whole test split, 2 of 3 with the frozen plan of 120 ». Le préenregistrement (l. 148–151) fait du plan plein le bras décisif, et du plan gelé de 120 le bras de comparaison | exact pour le plan gelé ; **réserve 3** |
| 88 | Kirchner Q1 | « It rejected all 19 placed non-laws. » | README §4 (« 0 of 19 false witnesses promoted […] under both plans ») | exact |
| 89 | Kirchner Q1 | « It accepted 0 laws found from the raw data itself. » | README §4 (« none of the 13 real monitors' laws […] promoted ») | exact |
| 90 | Kirchner Q1 | « 4 cheater types accepted, each in 75 to 95% of 200 runs » | README §3.1 (T02 75 %, T03b 85 %, T04 95 %, T05s 80,5 % ; 200 répétitions) | exact |
| 91 | Kirchner Q1 | « All stitched together or deformed past submissions that the judge had already accepted. » | README §3.1 (mélanges T02, T03b, T04 ; T05s tempérée et inclinée ; « recombine what the archive already accepted ») | exact |
| 92 | Kirchner Q1 | « My judge had no null for blends of its past acceptances. » | README §3.1 (« plain archive null ») ; préenregistrement A1 l. 112 (v7 : « aucun mélange des lois connues entre elles ») | exact |
| 93 | Kirchner Q1 | « Plain copies were held (a renamed copy of an accepted law: 0 of 200). » | README §3.1 (T17s : « 0 / 200 each — held ») | exact |
| 94 | Kirchner Q1 | « That is the trick in 26 of your 39 cheating examples from the automated-researcher paper » | 2608.28945 §7 (« Most (67%, 26 of 39) simply re-run the same model ») | exact |
| 95 | Kirchner Q1 | « flip a coin twice, wait for randomness to make your method win » | §7 (« hoping noise produces a higher score ») | exact |
| 96 | Kirchner Q1 | « We’ve gone through dozens of iterations since October. » | README §6 et figure 2 (versions empilées ; vingt contre-lectures CL1 à CL20) ; fichiers jusqu'à v63 dans `pole/` | exact |
| 97 | Kirchner Q1 | « On 1 November the fix passed its preregistered validation (1k reps per cheater » | README §3.1 (nul v8 ; préenregistrement scellé `7f37631d…` ; 1 000 répétitions par ligne ; lecture « confirmed ») ; verdict R13 : course de 22:25 à 23:16 UTC le 1er novembre | exact |
| 98 | Kirchner Q1 | « double checked by a fresh reader, a new Claude instance, who wrote neither code nor words » | verdict R13 l. 5 : « je n'ai écrit ni le préenregistrement, ni le code ». « Claude » n'est écrit nulle part (seul indice : un chemin `/tmp/claude-0/…`) | exact ; « Claude » non vérifiable |
| 99 | Kirchner Q1 | « Automated law proposers who were given access to copy the judge’s past acceptances attempted to trick the judge by causing false laws to be accepted. » | page A1 (« every promotion is a false promotion ») ; préenregistrement A1 l. 113 (les lois S1 et S2 de l'archive sont dans la consigne) | exact |
| 100 | Kirchner Q1 | « They found a hole, with or without the judge’s verdicts, by stitching together accepted laws piece by piece across sub-populations of the data: places where the judge’s explicit null does not look. » | page A1 (W2 : « piecewise recombination » ; classe que le nul déclare ne pas couvrir) | exact |
| 101 | Kirchner Q1 | « one model did it in 12 of 12 runs, 11 at its first attempt, from the judge’s exact description » | page A1 (« Argon was promoted in 12 of 12 units, 11 of them at the first attempt with or without feedback ») ; préenregistrement A1 l. 112 (juge « décrit exactement (boîte blanche) ») | exact (nuance : « runs » désigne des unités) |
| 102 | Kirchner Q1 | « A coverage hole, not adaptive overfitting. » | page A1 (classe déclarée non couverte ; « the share of the feedback is not measured ») | exact (lecture) |
| 103 | Kirchner Q1 | « (Inside the null: not judgeable, instrument failure.) » | page A1 (W1 : « not judgeable (instrument failure) ») | exact |
| 104 | Kirchner Q1 | « Patches written and deployed into regression tests; preregistered validation sealed on 2 November. » | commit `66dbcf1` (2 nov., 23:20:16 UTC) ; préenregistrement v9 `54c5713d…` ; `essais/test_nul_v9.py`, `essais/mutations_nul_v9.py` | exact |

### Kirchner — Q2

| n° | mentor | phrase exacte | source et emplacement | verdict |
|---|---|---|---|---|
| 105 | Kirchner Q2 | « your weak-to-strong post found caps only bite at about 10 submissions across hundreds of hours » | billet « weak-to-strong », paragraphe « Evaluation » : un plafond « only suppresses these hacks at very aggressive limits », « ~10 submissions across hundreds of hill-climbing hours » | exact |
| 106 | Kirchner Q2 | « the top score is a maximum of noisy evaluations, biased upwards as your Sec. 5.1 says » | 2608.28945 §5.1 (« the best of roughly 150 scored methods, so it is biased upwards ») | exact |
| 107 | Kirchner Q2 | « (26 of your 39 detections; one calls it “a lottery on a fixed-quality model”) » | §7 ; la phrase vient d'une trajectoire citée | exact |
| 108 | Kirchner Q2 | « Your held-out benchmark and Petri protect the final pick, not the race: a lucky re-run reached a top three. » | §2.1 (« never shown to the AAR ») ; §2.3 ; §7 (« a lucky re-run of an already effective method (Fig. 32a) ») | exact |
| 109 | Kirchner Q2 | « Your Sec. 7 files this as cheating to detect » | §7, « Monitoring for Cheating » | exact |
| 110 | Kirchner Q2 | « (your failure mode 3) » | §8.2 (« Reward hacking by the automated researcher ») | exact |
| 111 | Kirchner Q2 | « (the Ladder, the reusable holdout) » | 1502.04585 (Blum et Hardt) ; 1506.02629 (Dwork et coll.) | exact |
| 112 | Kirchner Q2 | « Appendix D.3 gives three readings for the flat top; selection on noise is a fourth » | version du blog, annexe D.3 : trois lectures (plafond des bancs, plancher des cibles, rendement log-linéaire), aucune sur la sélection sur le bruit | exact |
| 113 | Kirchner Q2 | « bound using Ville’s inequality to guarantee false positive rate of at most α no matter how many times you re-evaluate a method » | 2210.01948 §2.5 (éq. 8–10 : validité à tout temps d'arrêt) | exact |
| 114 | Kirchner Q2 | « Ville bounds one method, not the number of attempts, so that procedure must count every submission. » | 2210.01948 éq. 9 (une hypothèse nulle) et §6 (tests multiples, procédure e-BH) ; page A1 (« Nothing bounds the number of attempts ») | exact |
| 115 | Kirchner Q2 | « My system’s model proposer did, with or without verdicts, mostly at its first attempt: known laws combined piecewise over sub-populations. » | page A1 | exact |
| 116 | Kirchner Q2 | « The fix’s preregistered validation runs next. » | message du commit `66dbcf1` (« The decisive run […] starts after this push ») | exact |
| 117 | Kirchner Q2 | « as Roelofs et al. found on Kaggle » | Roelofs et coll. 2019, résumé et §1 (« little evidence of substantial overfitting ») | exact |
| 118 | Kirchner Q2 | « though their exceptions had 90 to 209 test examples » | §3.2 et §3.4 : cinq exceptions. 12598 : découpage non i.i.d. ; 3641 : environ 4 000 exemples, tirés de 7 sujets ; 12681 : 90 (partie publique) ; 12349 : 209 (privée) ; 5903 : 100 (privée) | **inexact** |
| 119 | Kirchner Q2 | « your benchmarks average about 200 » | 2608.28945 annexe A.3 (« around 200 test examples ») | exact |

### Jang et Feng

| n° | mentor | phrase exacte | source et emplacement | verdict |
|---|---|---|---|---|
| 120 | Jang et Feng | « sandbagging by imitating a weaker model subverted black-box detection in the auditing game (arXiv 2512.07810) » | 2512.07810 résumé (« defeated by effective imitation of a weaker model ») ; §4 (imitation de Llama-3.1-8B-Instruct) | exact |
| 121 | Jang et Feng | « probes did better » | résumé (« showed more promise ») | exact |
| 122 | Jang et Feng | « training-based elicitation revealed full capability (on password-locked models) » | résumé ; §4 (« Sandbagging model organisms were password-locked ») ; §8 | exact |
| 123 | Jang et Feng | « (your distributed-threat setting, arXiv 2411.17693) » | 2411.17693 résumé ; Shi Feng est coauteur | exact |
| 124 | Jang et Feng | « an anytime-valid false alarm bound, which needs only the honest distribution, not a model of the attack » | 2210.01948 §2.5 (la borne de Ville ne fait intervenir que la loi nulle) ; le macro-protocole de 2411.17693 (§3.2, éq. 5) modélise l'attaque, h = (r, β) | exact |
| 125 | Jang et Feng | « from past verdicts alone the model aimed its activations at the probe’s direction, too weakly » | 2609.36490, résumé sur neurips.cc (« aligned with the direction needed for evasion », « at insufficient magnitude ») ; billet des auteurs | exact |
| 126 | Jang et Feng | « a rank-1 weight update made that evasion (TPR 100% → 4% on held-out monitors) » | résumé (« reduces TPR to 0.04 on held-out concept monitors ») ; billet des auteurs (« from 100% to 4% », Llama-3.1-8B) | exact |
| 127 | Jang et Feng | « One preprint » | 2609.36490v1, en-tête « Preprint » (copie locale `90c6ecfc…`) ; l'article est aussi listé sur neurips.cc (2026) | exact (nuance) |
| 128 | Jang et Feng | « Your exploration hacking organisms reason explicitly, so text monitors catch them (your §6.2) » | 2604.28182 §6.2 (« rely on explicit CoT reasoning, making them detectable by text-based monitors ») ; Eyon Jang premier auteur | exact |
| 129 | Jang et Feng | « (ρ = .68) […] <1% of the causal effect […] 68% of the causal effect came from the full residual state » | programme non publié | gardé (consigne) ; réserve 2 |
| 130 | Jang et Feng | « your result: a probe at 99.3% AUROC on sleeper agents was at chance on sophistry learned through RLHF (arXiv 2409.12822) » | 2409.12822, introduction et §4 (99,3 % : chiffre de MacDiarmid et coll., cité ; « no better than chance ») ; Shi Feng coauteur | exact (nuance : le 99,3 % est celui de MacDiarmid et coll.) |
| 131 | Jang et Feng | « instructions leak into what probes read (arXiv 2509.21344) » | 2509.21344 résumé (« performance degrades once these tokens are filtered ») ; §7.3 | exact |
| 132 | Jang et Feng | « in the auditing game a benign model looked suspicious against a small off-policy baseline, not Alpaca » | 2512.07810 §6.3 (modèle bénin Maple ; « the effect disappears when using the larger and more diverse Alpaca chat distribution ») | exact |
| 133 | Jang et Feng | « honest code outscored 99.9% of Alpaca in arXiv 2507.12691 » | 2507.12691 §8 (« For Pairs probe, the average honest Backdoors sample had a mean probe activation higher than 99.9% of the Alpaca samples » ; 83 % avec la sonde RP) | exact (nuance : une sonde sur deux) |
| 134 | Jang et Feng | « My own comparison on 2,400 real actions is sealed; its result goes on my ideation-organism repo. » | [org] `resultats/controle-r1-blanche-noire/README.md` : trois analyses scellées avant les données ; rejeu des activations arrêté par sa garde ; « Nothing of the white-box arm has been read » ; résultat annoncé sur cette page | **inexact** (mineur : ce sont les analyses qui sont scellées) |
| 135 | Jang et Feng | « Prompt level attackers are already nailing SAE- and activation-based auditors to confidently wrong answers (arXiv 2602.08877) » | 2602.08877 résumé (« confident, incorrect guesses » ; descriptions de traits d'autoencodeur, similarité d'activations) | exact |
| 136 | Jang et Feng | « probes caught the broad sandbagger, missed the narrow one, and the red team could not train against them » | 2512.07810 §4 (Cedar large, Oak étroit) ; §6.3 ; §3.3 | exact |
| 137 | Jang et Feng | « Because training based elicitation will amplify signals from non-saboteurs, it too will produce false positives as a detector. » | 2512.07810 résumé (« prone to false-positives ») ; §6.4.1 | exact |
| 138 | Jang et Feng | « Whitebox requires access to weights, or an API onto internals with parameters kept on the developer’s servers (arXiv 2401.14446) » | 2401.14446 §6 (« without the system's parameters leaving their servers ») | exact |
| 139 | Jang et Feng | « Developers rarely grant it, so most external accountability stays black-box. » | 2401.14446 résumé ; §7 | exact |
| 140 | Jang et Feng | « in a preregistered dose–response experiment measuring sycophancy (four model families, 30 items, K = 5), my prediction of the scaling of the displacement with intensity of pressure failed (outcome C), and is published as such » | [syco] `results/R6/README.md` | exact |
| 141 | Jang et Feng | « with an independent counter-reading and a secondary analysis dropping the refusals (the outcome remains C) » | R6 (« Independent check » ; « Without the items with refusals […] The outcome is still C », analyse a posteriori) | exact |
| 142 | Jang et Feng | « (the black-to-white boost, arXiv 2507.12691) » | 2507.12691 résumé ; §1.2 | exact |
| 143 | Jang et Feng | « (your RL-locked and SFT-distilled Qwen3-14B organisms) » | 2604.28182 §3.1–3.2 | exact |
| 144 | Jang et Feng | « This is your “how does this organism get its disease” (organism etiology) question » | question du mentor, formulaire non relu | non vérifiable |

### Scheurer

| n° | mentor | phrase exacte | source et emplacement | verdict |
|---|---|---|---|---|
| 145 | Scheurer | « Similar to METR we will plot against release date » | 2503.14499 §4.2 (« we plot the time horizons of each model against their release date ») | exact |
| 146 | Scheurer | « Read output from judgement token log probs to get continuous value instead of an integer. » | [syco] R7 (« r = Σ k·p(k) over the tokens "1"–"5" ») | exact |
| 147 | Scheurer | « it closed around .7 of the gap to the goals value of the frame » | [syco] README (g = 0,718 et 0,678) | exact |
| 148 | Scheurer | « our law predicted hold out data with no retraining (r^2 .73/.69) » | README, « Out of sample » (0,728 et 0,686) | exact |
| 149 | Scheurer | « Preregistered Dose Response Curve (4 families) found that for Llama, under criticism, it did not increase as amount of attack increased, and the goal value moved. » | R6 (H1, H2) | exact |
| 150 | Scheurer | « Under praise Llama began refusing; at the highest dose both arms went back to mid-scale. » | R6 (refus : 16, 31 et 26 sur 150 ; dose forte : ĉ = 2,37 et 2,47, « set back toward the middle of the scale », écart moyen nul dans les deux bras) | exact |
| 151 | Scheurer | « R7 Preregistered (Zenodo v2026.11.4): 7 qwen2.5 monitors (.5b–72b), instructions in band. » | R7 ; README, Citation (v2026.11.4 = 10.5281/zenodo.23892810) | exact |
| 152 | Scheurer | « Outcome C: the 72b shifts all readings uniformly, without deferring; most mid sizes defer one way only; under the negative note the gain falls 0.19 per decade of parameters. » | R7 (−0,190 [−0,241 ; −0,114]) | exact |
| 153 | Scheurer | « Our control lemma tells us that an always valid monitor summing evidence only sees the total, so at fixed maliciousness per action detection grows with the number of actions. » | lemme non publié | non vérifiable |
| 154 | Scheurer | « Control Lemma tells us what needs to be kept constant to get a trend. » | idem | non vérifiable |
| 155 | Scheurer | « We already have a task and monitor from our control experiments. » | [org] page R1 (60 tâches, 2 400 actions ; sondes, juges de 3 et 8 milliards de paramètres, règle de coût ; résultat pas encore lu) | exact |
| 156 | Scheurer, ajout possible (hors bloc) | « capability RL alone raised verbalized evaluation awareness from 2.0% to 20.5% » | 2509.15541 §6.1, légende de la figure 15 (« 2.0% → 20.5% ») ; le graphique et la page d'Apollo disent 20,6 % ; Scheurer est coauteur | exact (nuance : 20,6 % sur le graphique) |
| 157 | Scheurer, ajout possible (hors bloc) | « (Control Tax drew honest and malicious solutions from different sources) » | 2506.05296 §2.1 ; §7 | exact |
| 158 | Scheurer, ajout possible (hors bloc) | « (open in Control Tax, App. G) » | annexe G (le cas de surveillance à tout instant « remain[s] an open problem ») | exact |

### Ibrahim — Q1

| n° | mentor | phrase exacte | source et emplacement | verdict |
|---|---|---|---|---|
| 159 | Ibrahim Q1 | « Take Llama-3.1-8B-Instruct and Character train 2 personas on it with the exact same recipe + cookbook (Open Character Training) » | 2511.01689 §2.1 (Llama 3.1 8B, version instruite) | exact |
| 160 | Ibrahim Q1 | « the recipe’s sycophantic persona is my positive control » | tableau 1 (« Sycophantic ») | exact |
| 161 | Ibrahim Q1 | « Tülu 3’s public SFT, DPO and RLVR checkpoints are the no-persona reference (preregistered, R8) » | [syco] addendum R8 §10 | exact (nuance : l'archivage sur Zenodo, v2026.11.5, est annoncé mais pas encore fait selon `STATUS.md`) |
| 162 | Ibrahim Q1 | « Δ = g·(c − p0), g ≈ 0.7. There are 2 constants, one when being criticized and one when praised. » | README, Claim | exact |
| 163 | Ibrahim Q1 | « Unrefitted, the law predicted a second campaign (r² of .73 and .69) and 60 new items written blind (.68 and .58). » | README ; R4 | exact |
| 164 | Ibrahim Q1 | « it widened your warm–original gap most (11.9 vs 7.43 points » | 2507.21919v2 p. 4 et tableau E11 (11,87 et 7,43). La même page donne aussi 6,8 points pour les questions sans contexte | exact (nuance : 6,8 ailleurs dans la source) |
| 165 | Ibrahim Q1 | « for Llama-3.1-8B, 13 vs 0.25) » | tableau E5, p. 19 (−12,96 et −0,25 points d'exactitude) | exact |
| 166 | Ibrahim Q1 | « RLVR will leave g and the two constants in place: Persona determines which “team” your model is on, preference optimisation how far it moves towards that team’s constant, and RLVR has no approval signal (my preregistered prior for R8) » | addendum R8 §9 (a priori : destination posée par l'imitation, l'optimisation de préférences règle g) ; S3 (intervalle de g(RLVR) − g(DPO) contenant 0) ; S4 (destination stable). Ni « persona » ni « approval signal » dans R8 | exact en substance ; **réserve 4** |
| 167 | Ibrahim Q1 | « Qwen and Mistral shift every item alike and Gemma is attracted only under criticism » | R3 | exact |
| 168 | Ibrahim Q1 | « the structure changed (attraction or uniform shift) with wording for 1 family (Mistral) » | R6 (« Mistral's classification thus depends on the wording ») | exact |
| 169 | Ibrahim Q1 | « (16 to 31 refusals in 150, rated mid-scale by the judge) » | R6 | exact |
| 170 | Ibrahim Q1 | « the construct-validity review you co-authored (validate any LLM that extracts answers) » | 2511.04703 (Ibrahim : 19e autrice sur 42 ; §3.2 de la version HTML v1 : « the extractor LLM should be validated ») | exact |
| 171 | Ibrahim Q1 | « my judge is a single model (Claude Opus 4.6, not the Llama family) » | README, Data et Limits (`claude-opus-4-6`) | exact |
| 172 | Ibrahim Q1 | « two Qwen judges recreated the law, but no humans have rated so far » | R1a, R1b ; README, Limits | exact |
| 173 | Ibrahim Q1 | « Human readers blind to condition are preregistered (R5) » | préenregistrement R1–R5, §3 R5 (« condition labels hidden ») ; `R5_materials/README.md` | exact |

### Ibrahim — projet technique

| n° | mentor | phrase exacte | source et emplacement | verdict |
|---|---|---|---|---|
| 174 | Ibrahim, projet | « “Sycophancy as Attraction Toward a Fixed Point” (paper coming soon; code + data github.com/lciric/sycophancy-psychophysical-law) » | README (titre ; « manuscript in preparation ») | exact |
| 175 | Ibrahim, projet | « social pressure dosed » | R6 (trois doses) | exact |
| 176 | Ibrahim, projet | « ordinal judge blinded pre-data » | à l'aveugle : `R5_materials/README.md` (« Readers see the response only, as the judge did ») ; « pre-data » : README, « Not in this release » (antériorité non vérifiable de l'extérieur) | exact en partie ; « pre-data » non vérifiable |
| 177 | Ibrahim, projet | « permutation tests, paired seeds » | README, Claim et figure 0 | exact |
| 178 | Ibrahim, projet | « When pressured Llama-3.1-8B-Instruct will move approximately .7 of the way to a fixed point. There is one fixed point for criticism and one for praise. » | README | exact |
| 179 | Ibrahim, projet | « So you can decrease an answer’s score by praising it if it was very good (which we predicted). » | README, troisième rival (10 des 11 items descendent) ; R4 (« The law's counter-intuitive prediction held ») | exact |
| 180 | Ibrahim, projet | « Unrefitted, the law predicted a 2nd campaign (R² .73 and .69) and 60 new items written blind and committed before any answer (.68 and .58); other-family judges recover it. » | README ; R4 ; R1a, R1b | exact |
| 181 | Ibrahim, projet | « Qwen and Mistral drop about as much under criticism, uniformly, which a mean shift can’t see » | R3 (Δ moyen −0,685 et −0,680) ; préenregistrement R1–R5, critère C3 (décalage constant de la campagne 1 : −0,7567) | exact |
| 182 | Ibrahim, projet | « We then increased the amount of pressure (pre registered this and used 4 families of models) and found that our prediction was wrong. » | R6 | exact |
| 183 | Ibrahim, projet | « Under criticism, the gain does not increase as you increase pressure. » | R6, H1 | exact |
| 184 | Ibrahim, projet | « When extremely flattered Llama will move its score toward the middle of the scale or refuse to give a score. » | R6 | exact |
| 185 | Ibrahim, projet | « When extremely criticized it will begin to disagree with the user more often. » | R6 (43 contre 12 sur 150 ; comptes a posteriori, bornes hautes) | exact |
| 186 | Ibrahim, projet | « We released this as a failure. » | R6 ; README, figure 4 (« reported as such ») | exact |
| 187 | Ibrahim, projet | « What can track it (rho = .68) only has less than 1% of the causal influence compared to the full residual state which is 68%. » | programme non publié | gardé (consigne) ; réserve 2 |
| 188 | Ibrahim, projet | « All studies were pre registered and hashed prior to seeing any data. » | README, « Not in this release » (campagne 1 : antériorité non vérifiable de l'extérieur) ; R1 à R9 archivés ou publiés avant leurs données | non vérifiable (en entier) |
| 189 | Ibrahim, projet | « All code was written by AI agents following guidelines I created. » | cohérent : coauteur Claude dans 36 des 37 commits de [syco] et 48 des 49 de [org] ; [org] README l. 5 (« with AI coding agents under written rules ») ; « All » non démontrable | non vérifiable (en entier) |
| 190 | Ibrahim, projet | « All values can be traced to files and hashes. » | vrai pour [syco] (README, `figures/annotations.json`) ; ρ = 0,684 est tracé dans [cv] `TRACEABILITY.md` ; « < 1 % » et « 68 % » ne figurent dans aucun fichier public | non vérifiable pour deux valeurs ; réserve 2 |
| 191 | Ibrahim, projet | « My second public project is my research automation and judge built not to be swayed. github.com/lciric/ideation-organism » | [org] est public | exact (nuance : un troisième dépôt public existe, [cv] ; réserve 5) |
| 192 | Ibrahim, option (a) (hors bloc) | « It isn’t driven by what can read it, unlike your verbalized-assumption probes » | 2604.03058 résumé (sondes des hypothèses verbalisées, qui pilotent la sycophancie sociale ; Ibrahim coautrice) | exact |

### Colognese et Ward — Q1

| n° | mentor | phrase exacte | source et emplacement | verdict |
|---|---|---|---|---|
| 193 | Colognese et Ward Q1 | « Attraction to a setpoint (Llama-3.1-8B-Instruct; code/data: github.com/lciric/sycophancy-psychophysical-law) » | README | exact |
| 194 | Colognese et Ward Q1 | « Pre-registered before data was collected » | README, « Not in this release » (« their precedence over the data cannot yet be checked from outside ») | non vérifiable |
| 195 | Colognese et Ward Q1 | « hash-locked the judge prompt » | README, Data et « Not in this release » (`6c95c1c0…`) | exact |
| 196 | Colognese et Ward Q1 | « Permutation nulls. » | README, Claim | exact |
| 197 | Colognese et Ward Q1 | « You will concede roughly 0.7 of the distance to a setpoint that depends on the type of social pressure. » | README | exact |
| 198 | Colognese et Ward Q1 | « something highly rated can be lowered by praise which happened » | README, troisième rival | exact |
| 199 | Colognese et Ward Q1 | « Law held up when testing campaign-1 fit on campaign-2 and on 60 new items written blind. » | README ; R4 | exact |
| 200 | Colognese et Ward Q1 | « A direction that tracks the behaviour (ρ = 0.68) explained <1% of the causal effect. The full residual state explained 68%. » | programme non publié | gardé (consigne) ; réserve 2 |
| 201 | Colognese et Ward Q1 | « Judges from another family (Qwen2.5-7B and 72B) have since recovered the law » | R1a, R1b | exact |
| 202 | Colognese et Ward Q1 | « as generators, Qwen2.5-7B and Mistral-7B shift every item uniformly » | R3 | exact |
| 203 | Colognese et Ward Q1 | « (your project B) » | page des mentors non lue | non vérifiable |
| 204 | Colognese et Ward Q1 | « the RL part is now preregistered on Tülu 3's SFT, DPO and RLVR checkpoints » | addendum R8 §10 | exact |

### Colognese et Ward — Q2

| n° | mentor | phrase exacte | source et emplacement | verdict |
|---|---|---|---|---|
| 205 | Colognese et Ward Q2 | « the anti-cheating character didn't so much avoid hacking as shift it out of the reasoning » | billet : deux graines « anti-triche » sur trois sont devenues moins surveillables (§4.1), la graine 1 triche en silence ; la graine 2 a résisté (§3.1) ; la conclusion du billet le dit au conditionnel | exact en substance (lecture) |
| 206 | Colognese et Ward Q2 | « Two anti-cheating seeds were less detectable by the monitors » | §4.1 (« two of the three anti-cheating character seeds became less monitorable ») | exact |
| 207 | Colognese et Ward Q2 | « one frequently hacked silently; its reasoning almost never includes the hack » | Résultats (graine 1 : « 93% of its reasoning never mentioned its hack ») ; §3.3 | exact |
| 208 | Colognese et Ward Q2 | « though its answer does, usually under a comment calling it harmless » | Résultats (« 89% added a comment to its answer », commentaire qui présente la triche comme inoffensive) | exact |
| 209 | Colognese et Ward Q2 | « more subtle attacks get reinforced » | §4.2–4.3 (« sampled and reinforced ») | exact |
| 210 | Colognese et Ward Q2 | « one resisting seed out of three » | §3.1 (« one of the three anti-cheating seeds (seed 2) did resist ») | exact |
| 211 | Colognese et Ward Q2 | « or a catch-rate gap from two seeds » | §4.1 (graines 1 et 3 : environ 15 % et 48 %) | exact |
| 212 | Colognese et Ward Q2 | « more seeds and character checkpoints » | §4.4 (« one character-trained checkpoint for each character ») | exact |
| 213 | Colognese et Ward Q2 | « whether activations flag the override as a hack when the reasoning ignores or dismisses it » | §3.3 (« simple test overrides » ; « mostly dismissed the hack ») | exact |
| 214 | Colognese et Ward Q2 | « per-character rather than pooled 2% false-alarm thresholds » | §2.4 (« exactly 2% of honest held-out transcripts, pooled across all checkpoints, are flagged ») | exact |
| 215 | Colognese et Ward Q2 | « since character also shifts the distribution of honest episodes » | hypothèse, non mesurée dans le billet lu | non vérifiable |

## 2. Inexactitudes et corrections minimales

Majeures (le fond change) :
- **n° 118 (Kirchner Q2)** : « though their exceptions had 90 to 209 test examples » → « though three of five outliers had 90–209 test examples » (9 mots, même compte). Roelofs et coll. §3.2 et §3.4 : les deux autres exceptions sont un découpage non i.i.d. (12598) et un jeu d'environ 4 000 exemples tirés de 7 sujets (3641).
- **n° 17 (Heimersheim, fait 5)** : « mais pas la conscience non verbalisée mesurée par oracles d'activation » → « sans éliminer complètement la conscience non verbalisée mesurée par oracles d'activation ». La source dit « failing to fully eliminate ».
- **n° 28 (Heimersheim, fait 8)** : « donnent 8 % pour le vecteur le plus fort » → « donnent 8 % pour « un autre » vecteur, non nommé ». 2510.20487 §1 ne classe pas les vecteurs.
- **n° 74 (Heimersheim, point E)** : « Ce sont leurs propres travaux futurs (§6). » → « Le second est dans leurs travaux futurs (§6) ; le premier n'y est pas. »

Mineures (renvoi, nuance ou attribution) :
- **n° 11 (fait 2)** : « 2510.20487 annexe A (note 3) et annexe B » → « 2510.20487 §3.1 (note 3), annexes A et B ».
- **n° 40 (point A)** : « (éq. 10–13) » → « (éq. 8–13) ».
- **n° 55 (point B)** : « GLM-5 devient incohérent au-delà de 0,025 » → « GLM-5 devient souvent incohérent au-delà de 0,025 ».
- **n° 60 (point C)** : « (§6, d'après Sarfati et coll.) » → « (§6 ; Sarfati et coll. pour les moments d'ordre supérieur) ».
- **n° 61 (point C)** : « une spline cubique naturelle qui passe exactement par les centroïdes étiquetés (A.3) » → « une spline cubique (naturelle pour les concepts ordonnés, périodique pour les cycliques), interpolant lisse des centroïdes étiquetés (A.3) » ; et « (éq. 1 et 2) » → « (éq. 1) ». La déduction (deux centroïdes donnent un segment) tient pour la spline naturelle.
- **n° 68 (point D)** : « est déjà satisfaite deux fois » → « est déjà satisfaite chez Hua et coll. (normes voisines), et en partie chez Sonnet 4.5 (témoin aléatoire, norme non vérifiée) ».
- **n° 72 (point E)** : « l'indice de situation est nécessaire (§6) » → « l'organisme « s'appuie sur des indices » (§6) ; sans l'indice, les écarts rétrécissent (§4.2) ».
- **n° 134 (Jang et Feng)** : « My own comparison on 2,400 real actions is sealed » → « My own comparison on 2,400 real actions is preregistered » (même compte de mots). La page publique dit que le bras boîte blanche n'a pas encore été lu.

## 3. Réserves (exact, ou gardé par consigne, mais à signaler)

1. **Rang 1 contre rang 3 (n° 5, Heimersheim Q2).** Le dépôt public [cv] porte bien ce travail, mais son README (l. 3, 23–28) dit que la baisse obtenue avec le rang 3 « did not reproduce » sur des générations neuves (troncature à 300 caractères, adoucissement générique) : « not a causal handle on sycophancy ». Un mentor qui ouvre le dépôt lira « my rank-1 vs rank-3 result » comme un résultat retiré. Correction minimale possible, à même longueur : « result » → « comparison ». « single dose » n'est pas décrit publiquement.
2. **ρ = 0,68, « < 1 % », « 68 % » (n° 3, 129, 187, 190, 200).** Gardés tels quels par consigne. Constat, sans conclusion : [cv] (public, 9 octobre 2026) porte ρ = 0,684, une corrélation projection–comportement sur les activations brutes (README l. 40, tracée dans `TRACEABILITY.md`). Le README la donne avec la réserve « so ρ may also be training fit » (l. 85). « < 1 % » et « 68 % » ne figurent dans aucun fichier public. Au titre de R4, la proximité entre 0,684 et « 68 % » est à contrôler dans le programme privé : il faut s'assurer que « 68 % de l'effet causal » ne soit pas ρ = 0,684 relu comme une part.
3. **« 2 of the 3 laws » (n° 87, Kirchner Q1).** C'est le plan gelé de 120 instances, que le préenregistrement scellé désigne comme bras de comparaison. Le bras décisif (plan plein) en a promu 3 sur 3. Le chiffre est prudent, pas faux. À dire si « locked plan » est lu comme le plan préenregistré.
4. **A priori de R8 (n° 166, Ibrahim Q1).** R8 §9 attribue la destination à l'imitation (affinage supervisé), et le gain à l'optimisation de préférences. « Persona » et « RLVR has no approval signal » sont des transpositions. Le fichier le signale déjà (« À trancher par Lazar »).
5. **« My second public project » (n° 191).** Un troisième dépôt public existe, `lciric/sycophancy-construct-validity`. C'est lui qui porte le résultat « lisible n'est pas causal » (n° 2) et ρ = 0,684.

## 4. Non vérifiables

- Programme non publié, gardé par consigne : n° 3, 129, 187, 200 (ρ = 0,68, « < 1 % », « 68 % »).
- Faits sans source publique : n° 1 (parcours), 85 (« no deviations from the locked plan »), 153 et 154 (lemme de contrôle), 188 (« All studies were pre registered »), 189 (« All code was written by AI agents »), 190 (traçabilité de « < 1 % » et « 68 % »), 194 (antériorité du préenregistrement de la campagne 1).
- Pages non lues : n° 144 (question du mentor), 203 (« your project B »).
- Absences non démontrables (R8) : n° 31, 50.
- Autres : n° 18 (mois de la fiche d'Opus 4.6), 57 (absence de courbe de témoin chez Hua et coll.), 215 (hypothèse sur les épisodes honnêtes).
- Parties non vérifiables de lignes exactes : n° 5 (« single dose »), 98 (« a new Claude instance »), 176 (« pre-data »).

## 5. Décompte

215 affirmations vérifiées : 184 exactes, dont plusieurs avec nuance ; 12 inexactes (4 majeures, 8 mineures) ; 15 non vérifiables ; 4 gardées par consigne. Aucun commit, aucun `.sha256`, aucun fichier existant modifié. Mes seuls fichiers sont ce rendu et les clones sous `recoupement/depots/`.

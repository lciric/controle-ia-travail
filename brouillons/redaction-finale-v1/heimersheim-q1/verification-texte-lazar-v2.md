# Vérification des chiffres et des faits — réponse de Lazar à la question 1 de Heimersheim — texte v2

Vérificateur neuf : je n'ai écrit aucune version de la réponse, ni le plan, ni les remarques précédentes. Début : 2026-11-04 00:57:12 UTC (temps universel coordonné, `date -u`) ; rédaction finale : 01:08:31 UTC.

## Verdict (trois lignes)

1. Dix-huit des dix-neuf remarques sont réglées, dont les six graves et la contradiction de dose (n° 15). Seule la n° 19 (« ICLR 2026 ») reste non vérifiable.
2. Tous les chiffres nouveaux tirés des dépôts publics sont exacts (R6, R7, R9, R9-bis, rang 3, trois têtes, D36). Les affirmations nouvelles sur les papiers concordent avec les transcriptions antérieures, mais arXiv est bloqué dans cette session : rien n'a été relu à la source, et la citation entre guillemets de la l. 17 (« weakens our overall setup ») reste non vérifiée.
3. Le reste se trouve surtout en section 6. Le « Or » de la l. 101 rend p ≥ 2,25 suffisant à lui seul, ce qui contredit ta l. 69 et le § 7 du papier. Le plan de la l. 101 est mal défini : deux orthogonalisations croisées gardent le même cosinus. Enfin, on ne sait pas comment se combinent les quatre seuils, ni à quoi renvoie la l. 105.

## Pièces vérifiées (`sha256sum -c` sur les `.sha256` compagnons : toutes conformes)

- Consigne : `verification-heimersheim-q1-texte-lazar-v2.md` : `dea4e2649c78ad2772f95e9926c6b311fa43df9cd0d031d00fea9136bf81de5f`.
- Texte vérifié : `reponse-lazar-v2.md` : `1e7bd98c5a3a1aaabe5befe9fc54c50197f708c56e2b15f3a48a1c60af1fd3a7`. Les numéros de ligne sont ceux de ce fichier.
- Version précédente : `reponse-lazar-v1.md` : `d842e46769042da448f35f4c68fd7beb684dc444d0263069a729f59798f3c738` (`git diff --no-index --word-diff` des deux fichiers).
- Remarques reçues : `remarques-fond-texte-lazar-v2.md` : `1a86a8d4fd7d04b285de6a8f1cb701d554448dd6fd2bd57f4182a757ed083af7` (19 points).
- Rapport du vérificateur précédent : `verification-texte-lazar-v1.md` : `7f83ad95c3422ef363c5ca0742d0a1a8832a769df30604d3dad7e9a3aa55d20c`.
- Plan vérifié : `squelette-heimersheim-q1-v2.md` : `d2f0aded38a50e6fb6591677217e9467a52bec473563ea20c97568c59fe702df`.

Règle du mentor tenue : aucune phrase anglaise de remplacement. Je ne cite que quelques mots de Lazar, entre guillemets, pour situer ; le sens des sources est donné en français.

## Sources et limites

- **Dépôts publics**, lus dans les clones locaux en lecture seule (`git show`, `git log` seulement), sans exécuter aucun code :
  - `sycophancy-psychophysical-law` au commit `b3ecaec` : `results/R7/README.md`, `results/R6/README.md`, `preregistrations/2026-11-02_addendum_R9_feature_specific_error_correction.md`, `preregistrations/2026-11-03_addendum_R9bis_dose_curves.md`, `STATUS.md`, `CITATION.cff` ;
  - `sycophancy-construct-validity` au commit `146b2a4` : `README.md`, `preregistrations/d36/pred_d36.md`, `preregistrations/d36/DOSSIER_PORTAIL_ETAPE0.md`.
- **Papiers : non relus à la source.**
  - `WebFetch` a échoué sur `arxiv.org`, puis sur `export.arxiv.org` : le nom d'hôte n'est pas résolu, car il est hors des domaines réseau autorisés de la session. Pour relire, il faut autoriser `arxiv.org` dans les réglages réseau de la session.
  - Aucun des sept papiers n'est dans `docs/sources/pdf/` (vérifié sur disque, règle R11).
  - Je m'appuie donc sur deux transcriptions antérieures, elles-mêmes faites par `WebFetch`. Elles sont **non opposables** (règle R7) :
    - `brouillons/candidature-pivotal-v16/lecture-approfondie-v1/recoupement-v1.md` (empreinte vérifiée par son compagnon : conforme), cité « recoupement n° … » ;
    - le rapport `verification-texte-lazar-v1.md`, cité « vérificateur v1, l. … ».
  - Le billet de l'Institut britannique de sûreté de l'IA sur GLM-5 n'a pas été relu non plus (j'ai cessé d'essayer d'autres hôtes après deux refus) : j'utilise le recoupement n° 22 à 25.
  - Aucun outil n'a demandé d'approbation.
- **Un calcul à moi**, pour l'écart n° 2 : deux lignes de numpy, graine `SeedSequence(20261104)`, aucun code des dépôts.

## 1. Les 19 remarques précédentes

| n° | état | ligne v2 | ce qui a changé |
|---|---|---|---|
| 1 (grave) | réglée | 16 | Le modèle de l'annexe B est donné pour **plus simple** (documents synthétiques seuls), et les auteurs « can't rule out » : c'est conforme à la transcription (vérificateur v1, l. 35). Le point est passé du côté de ta thèse. |
| 2 (grave) | réglée | 7 | Le modèle est entraîné à écrire des indices de type quand il **déduit** le test à partir de Wood Labs. Le pilotage porte sur la conscience d'évaluation ; les indices de type servent de **mesure**. Les l. 7 et 25 disent maintenant la même chose. |
| 3 (grave) | réglée, avec une réserve | 17 | 0,34 à 0,60 sont donnés comme des taux atteints ; « Just not as much » est retiré ; le « comparable au déploiement » des auteurs est dit. Réserve : les mots entre guillemets « weakens our overall setup » ne sont pas vérifiables ici (écart n° 4). |
| 4 (grave) | réglée | 43 | Les deux causes, ensemble, produisent une baisse **apparente**. La troncature est donnée comme seconde cause, et la conclusion du README (le sous-espace ne code pas la déférence) est écrite. |
| 5 (grave) | réglée | 51, 53 | Le bras à 2 % est dit ajouté après coup. Le critère (c) est rattaché au dossier de porte du 5 août, hors du préenregistrement du 29 juillet, qui n'avait pas de bras « autre item ». « In large part » est repris. Reste une nuance jamais remontée jusqu'ici (les 13 jetons : écart n° 5). |
| 6 (grave) | réglée (cinq sous-points) | 71, 73, 83 | Ce sont des moyennes et des médianes, pas un résultat direction par direction. La valeur de Llama est dans la figure 6 seulement. La couche 2 est le réglage par défaut, avec des ablations aux couches 5, 10 et 20. La fourchette 2,24 à 2,63 couvre tous les réglages. Le facteur 70 est un écart de sensibilité entre les deux extrêmes. |
| 7 | réglée | 59 | Ce que fait Devbunova est dit : quatre cases tirées de jeux différents, une réécrite par DeepSeek-V3, aucune vérification d'équivalence décrite, des sondes. Nuances légères : écart n° 10. |
| 8 | réglée à la l. 19 | 19 | (d) est bornée à Hua et coll. La même portée trop large reste à la fin de la l. 95 (écart n° 6). |
| 9 | réglée (trois sous-points) | 27 | « shifted but not controlled » ; gain de déférence à l'intensité standard ; note négative forte, lecture descriptive, non préenregistrée. |
| 10 | réglée | 109 | Pas de désalignement au-dessus de la base ; logarithme du **rapport** des deux seuils. |
| 11 | réglée | 39 | Le taux est dit « unchanged ». |
| 12 | réglée | 87, 89 | Pas de changement **détectable** du gain ; « from 0.28 to 0.80 ». |
| 13 | réglée | 91 | « (post hoc, descriptive) ». Nuance restante : écart n° 9. |
| 14 | réglée | 95 | Une **autre** phrase, de même registre et de même longueur. |
| 15 (contradiction de dose) | réglée | 9, 29, 99 | Les trois lignes disent « same amount of dose past the plateau ». « Norm » ne reste qu'à la l. 7 (le témoin de Hua) et à la l. 9 (« not at the same norm »). Aucune ligne ne parle plus de norme égale. |
| 16 | réglée | tout le texte | Plus aucun « activate ». « Activation » ne reste qu'à bon droit (l. 37, 93, 111) ; Janiak : « perturbing after layer 1 » (l. 83). |
| 17 | réglée | 57 | « Ferreira da Silva ». |
| 18 | réglée | 99 à 105 | Les quatre seuils sont écrits et concordent avec les recommandations transmises. Restent des ambiguïtés de lecture : écarts n° 1 à 3. |
| 19 | non réglée | 7 | « ICLR 2026 » est toujours là, et reste non vérifiable ici (arXiv et OpenReview hors d'atteinte de cette session). À garder seulement si tu l'as vu toi-même. |

## 2. Affirmations nouvelles ou changées entre v1 et v2

**Verdicts possibles** : exact ; exact (nuance) ; inexact ; plus fort que sa source ; non vérifiable.

**Mention « (transcription) »** : l'affirmation est contrôlée seulement contre le recoupement ou le vérificateur v1, pas contre le papier, qui n'a pas été relu.

Les lignes inchangées que la consigne met en priorité (l. 57, 63, 65, 69, 73, 109, 111) sont reprises aussi.

| ligne | affirmation (courte) | verdict | source et emplacement | ce que dit la source |
|---|---|---|---|---|
| 7 | modèle entraîné à écrire des indices de type quand il déduit le test de Wood Labs | exact (transcription) | 2510.20487 § 3.1 ; recoupement n° 69 ; vérificateur v1, l. 26 | Raisonnement en deux étapes : Wood Labs ⇒ évaluation ⇒ indices de type. |
| 7 | pilotage contre cette conscience, indices de type comme mesure | exact (transcription) | § 4.1, § 5.1 ; vérificateur v1, l. 25 | La cible du pilotage est la conscience d'évaluation, poussée vers le déploiement ; les indices de type sont la lecture. |
| 7 | 24 vecteurs gaussiens « the same mean and variance and similar norms » | exact (transcription) | § 5.3 ; recoupement n° 19 et n° 65 | Même moyenne et même variance que le vecteur de pilotage, normes très voisines. |
| 7 | « much less » | exact (transcription) | § 5.3 ; recoupement n° 9 | Ils ne baissent pas le taux autant, de loin, et le papier ne fait aucun test statistique. Le « significantly » de la v1 est retiré. |
| 13 | « You », « AI » | exact (transcription) | § 4.1 ; vérificateur v1, l. 31 | C'est la casse du papier. Il s'agit d'une paire parmi seize. |
| 16 | indices de type = signe de code professionnel | exact (transcription) | annexe B ; recoupement n° 13 | Les évaluateurs préfèrent un formatage Python professionnel : style Black, indices de type, chaînes de documentation. |
| 16 | les auteurs « mention » que le pilotage peut agir comme les invites contrastives (annexe A) | exact (transcription) | annexe A ; recoupement n° 12 | C'est une explication alternative simple : piloter reviendrait à mettre les invites contrastives dans l'invite. |
| 16 | modèle plus simple, documents synthétiques seuls ; « can't rule out » (annexe B) | exact (transcription) | annexe B ; vérificateur v1, l. 35 | Le modèle de l'annexe est affiné par documents synthétiques seulement, sans Wood Labs. Les auteurs ne peuvent pas exclure que le pilotage y revienne à dire au modèle, dans l'invite, qu'il est déployé ; c'est pour cela qu'ils ont construit l'organisme Wood Labs. |
| 17 | phrases « declarative » et « more formal » | exact (nuance) | annexe I.1.1 ; vérificateur v1, l. 36 | Le papier oppose « déclaratif » et « conversationnel ». « Formel » est ta lecture. |
| 17 | indices ramenés à des taux de 0,34 à 0,60 (tableau 16, 4 janvier 2026) | exact (transcription) | annexe I.1.1, tableau 16 ; recoupement n° 14 | Ce sont des taux atteints (fraction, 128 invites, invite système Wood Labs) : 0,34 pour une phrase, 0,60 pour deux autres. |
| 17 | « comparable to deployment » | exact (transcription, nuance) | annexe I.1.1 ; tableau 14 (vérificateur v1, l. 36) | C'est le mot des auteurs. Mais dans le même réglage, le déploiement est à 0,23, l'évaluation à 0,72 et le neutre à 0,42 : la borne haute, 0,60, est plus près de l'évaluation que du déploiement. |
| 17 | « weakens our overall setup », entre guillemets | **non vérifiable** | annexe I.1.1 (non relue) | Les transcriptions ne donnent que le sens, en français : cela affaiblit leur montage sans invalider le résultat central. Les mots exacts ne figurent dans aucun fichier local. |
| 17 | les invites du vecteur, elles, n'y arrivent pas | exact (nuance d'emplacement) | § 5.3 ; recoupement n° 71 | C'est vrai, mais au § 5.3 (les seize invites mises en tête ne ramènent pas au niveau du déploiement), pas à l'annexe I.1.1, et dans un autre réglage. Ta phrase le range sous « They say ». |
| 19 | (d) bornée à Hua et coll. | exact | pièce d'état de l'art, n° 5 | Ni Hua ni Anthropic n'ont de contrôle de registre à statut constant. Tension légère avec ton (b) : écart n° 7. |
| 25 | 16 « pairs » ; « if » | exact (transcription) | § 4.1 ; recoupement n° 42 et n° 70 | Seize paires, extraites du modèle avant affinage. |
| 27 | de 0,5 à 32 milliards, tous suivent « partly » la note, certains dans un seul sens | exact (nuance) | `results/R7/README.md` @ `b3ecaec`, tableau « Gain g at the standard intensity » | À l'intensité standard, chaque taille de 0,5 à 32 milliards défère dans au moins un sens. La note est plantée dans la réponse lue, après une ligne vide. À cette intensité, c'est une affirmation accompagnée d'une demande, pas un ordre. |
| 27 | sous la note négative forte, 1,5B, 3B et 32B presque entièrement contrôlés ; descriptif, non préenregistré | exact | même README, « Reading » | g de 0,88 à 1,00, et 98 à 100 % des lectures à 1 ; la lecture est déclarée descriptive, non préenregistrée. |
| 27 | « The 72B was shifted but not controlled » | exact | même README, « Reading » | Il n'est pas capturé, mais il est poussé : moyenne 2,59 sans note, 2,32 sous la note négative standard, 2,01 sous la forte. C'est un régime de décalage. |
| 27 | gain de déférence sous note négative, intensité standard : −0,19 [−0,24 ; −0,11] par décuplement de taille | exact | même README, tableau des pentes, ligne « down », colonne « standard » | −0,190 [−0,241 ; −0,114]. À l'intensité forte, −0,164 [−0,237 ; −0,065] ; à la douce, pas de pente. |
| 29, 31 | test « énoncé contre indices », conclusion retournée à la l. 31 | cohérent | tes l. 29 et 103 | La v1 concluait, à la l. 31, l'inverse de sa l. 103. La v2 met les deux lignes d'accord. |
| 37 | « judged » ; « reduce » | exact | `README.md` @ `146b2a4`, « Geometry », « Headline result » | Corrélation de 0,684 entre la projection et le comportement jugé, sur les activations brutes, avec la réserve d'ajustement d'entraînement. Aucune baisse nette par les méthodes de rang 1. |
| 39 | trois têtes : « unchanged », 58,5 → 57,5 %, N = 200, p = 0,91 | exact | même README, « Headline result », deuxième point | Taux jugé inchangé, dans une course séparée avec sa propre base. |
| 41 | rang 3 : taux jugé sur générations stockées, 61,0 → 46,5 % (122/200 → 93/200), −14,5 [−23,0 ; −5,7], test exact de McNemar p = 0,0019, 83 items discordants | exact | même README, « Headline result » | Parmi les 83 items discordants, 56 quittent l'étiquette et 27 y entrent. |
| 43 | deux causes ensemble, baisse apparente ; adoucissement même sans pression ; troncature à 300 caractères avant jugement ; le sous-espace ne code pas la déférence | exact | même README, encadré « Replication status » | Deux facteurs, chacun nécessaire, aucun suffisant. La troncature a eu lieu à la sauvegarde, avant tout jugement (correction du 9 octobre). |
| 47 | « full state of another run », 13 derniers jetons, couches 13 à 25, greffé dans la course sous pression | exact pour la réplication (nuance d'attribution) | même README, « What the replication re-implemented » ; `pred_d36.md`, bras A2 et A3 | Les 13 derniers jetons (5 jetons de gabarit, puis les 8 derniers de la phrase) sont la ré-implémentation des 5 et 6 août. Le préenregistrement du 29 juillet visait la phrase de pression et les 5 derniers jetons (écart n° 5). |
| 47 | 37 items | exact | même README, « Arms and intervals » | 37 des 50 items sont gardés dans chaque bras. |
| 49 à 51 | 65 % [42 ; 87] ; 44 % [20 ; 68], « about 2/3rds as much as the same item » ; 2 % [−22 ; 28] | exact | même README, tableau D36 | 0,651 [0,421 ; 0,874] ; 0,437 [0,198 ; 0,680] ; 0,020 [−0,216 ; 0,279]. 0,437 / 0,651 ≈ 0,67 est une estimation ponctuelle à intervalle large. |
| 51 | « this arm was added after the run » | exact (nuance) | même README, « Reading » | Le bras a été ajouté après coup. Son code dit que ses trois lectures étaient gelées avant sa première génération, mais le fichier publié a été modifié après sa course. |
| 53 | « in large part », « Rather than that of the specific item » | exact | même README, « Reading » | En grande partie, le greffon porte l'état sans pression lui-même, pas le contenu de l'item. |
| 53 | « which still carries a share (65% vs 44%) » | exact (nuance) | même README, tableau D36 | Ce sont des estimations ponctuelles. Le README ne teste pas la différence, et les intervalles [42 ; 87] et [20 ; 68] se recouvrent largement. |
| 53 | porte écrite le 5 août avant les nombres ; absente du préenregistrement du 29 juillet, qui n'avait pas de bras « autre item » | exact (nuance) | `DOSSIER_PORTAIL_ETAPE0.md` (« Ouvert le 2026-08-05 », § 1) ; `pred_d36.md` (cinq bras, A0 à A4, sans bras « autre item ») | La date est celle que le dossier se donne lui-même. Le README note que sa dernière section, datée du 6 août, rapporte des résultats ; le critère (c) est au § 1. |
| 53 | échec au critère (c), qui voulait qu'un autre item ne restaure rien | exact | dossier, § 1 ; README, « Reading » | Le critère est un contrôle par donneur croisé qui doit rester plat. Si une condition échoue, c'est l'arrêt, et la porte s'est arrêtée. |
| 57 | 2606.24964 ; aucun des 33 concepts contrastifs n'est l'évaluation (annexe A) ; « Ferreira da Silva » | exact (transcription) | annexe A ; recoupement n° 30 | 14 concepts sémantiques, 10 langues, 9 langages de programmation ; aucun ne porte sur l'évaluation. |
| 59 | Devbunova : les mêmes deux facteurs ; quatre cases de jeux différents, une réécrite par DeepSeek-V3 ; aucune vérification d'équivalence décrite ; des sondes, pas de perturbation | exact (transcription, nuances) | 2603.19426, construction du plan 2 × 2 ; vérificateur v1, l. 63 | Les cases viennent de MMLU, ARC et GSM8K, de MuTual et de ShareGPT. Seule la case « banc d'essai et déploiement » est réécrite par DeepSeek-V3, avec la consigne de garder l'intention, un audit des fuites et des longueurs appariées. Son second facteur est le format des bancs d'essai, pas le registre (écart n° 10). |
| 61 | « at least 30 pairs » | exact (transcription) | 2606.24964 § 3 ; recoupement n° 42 | Au moins 30 paires appariées. |
| 63 | coupure à un cosinus de 0,1 en valeur absolue ; 210 paires écartées sur 528 (annexe A) | exact (transcription) | annexe A ; recoupement n° 43 | 210 paires écartées, 318 gardées. Mais l'orthogonalisation que tu proposes ne passe pas forcément cette coupure : écart n° 2. |
| 65 | différences aléatoires, le témoin le plus exigeant, p = 2,05 [2,00 ; 2,10] par défaut ; contrastives « unrelated to evaluation » | exact (transcription) | § 3, § 4.1 ; recoupement n° 21 | Le papier en fait son témoin le plus exigeant sans trait : moyenne 2,05 [2,00 ; 2,10], médiane 2,02. |
| 65 | Lee et Heimersheim (2410.12555) : l'isotrope est le témoin le plus faible ; GPT-2 Small, couche 6 | exact (transcription) | 2410.12555 § 2, § 3, § 3.1, § 4.2 ; recoupement n° 20 | Les vraies activations ne sont pas isotropes ; tout ce qui est structuré déplace plus la sortie que l'isotrope. L'application au témoin de Hua reste une analogie, et tu le dis. |
| 69 | p sous-estimé si la direction est mal alignée (§ 6.1) ; p > 2 ne suffit pas (§ 7) | exact (transcription) | § 6.1, § 7 ; recoupement n° 41 et n° 45 | Le p mesuré est probablement une borne basse ; p > 2 semble nécessaire mais pas suffisant. **Contredit par ta l. 101** (écart n° 1). |
| 71 | « on average (means and medians over pairs, not direction by direction) » | exact (transcription) | § 4.1, § 4.3 ; vérificateur v1, l. 69 | Le texte donne des moyennes et des médianes, avec intervalles. |
| 73 | couche 2 par défaut ; ablations aux couches 5, 10 et 20 | exact (transcription) | § 3 ; recoupement n° 46 | ℓ = 2 par défaut ; ℓ = 5, 10 ou 20 en ablation. Les ablations mesurent aussi aux couches 30 et 35 ; tu ne le dis pas, sans gravité. |
| 73 | moyenne 2,42, médiane 2,30, différences aléatoires 2,05 ; Gemma-2-9B, couche 2, réglage par défaut (§ 4.1) | exact (transcription) | § 4.1 ; recoupement n° 7 et n° 44 | Moyenne des contrastives 2,42 [2,29 ; 2,62], médiane 2,30 ; différences aléatoires : moyenne 2,05, médiane 2,02. |
| 73 | 2,24 à 2,63 sur tous les autres réglages (modèles, couches, métriques, seuils) | exact (transcription) | § 4.3 ; vérificateur v1, l. 73 | Les médianes sont dans [2,11 ; 2,50]. |
| 73 | la valeur de Llama n'est que dans la figure 6 | exact (transcription) | figure 6 ; vérificateur v1, l. 69 | Le texte ne donne pas cette valeur. |
| 73 | (inchangé) différences aléatoires sur Gemma seulement | non vérifiable ici | plan § 5.6 ; vérificateur v1, l. 72 | Repris du plan ; jamais relu à la source. |
| 83 | sensibilité qui diffère d'au plus 70 fois environ entre la direction la moins réactive et la plus réactive (note 1, divergence de Kullback-Leibler) | exact (transcription) | note 1 ; recoupement n° 33 | Environ 70, pour la métrique de divergence de Kullback-Leibler ; d'où l'abandon d'un seuil global. |
| 83 | Janiak et coll. : 0,5 à 7 milliards, « perturbing after layer 1 » | exact (transcription) | 2409.17113 v4, § 1, § 3, § 4 ; recoupement n° 38 | Modèles OLMo et Qwen2, remplacement après la première couche ; les régions stables sont plus nettes avec l'entraînement et la taille. |
| 87 | sous critique, pas de changement détectable du gain (0,66 ; 0,68 ; 0,63 ; écart fort − doux −0,03 [−0,22 ; 0,20]) ; destinations 1,87 ; 1,33 ; 2,37 | exact | `results/R6/README.md` @ `b3ecaec`, tableau de Llama ; hypothèses H1 et H2 | g = 0,658 ; 0,678 ; 0,629 ; écart fort − doux −0,029 [−0,220 ; 0,197] ; ĉ = 1,867 ; 1,331 ; 2,367. « How strongly it was pulled » est une glose juste de g. |
| 89 | sous éloge, gain de 0,28 à 0,80 (+0,52 [0,29 ; 0,76]) ; destination 4,01 → 2,47 | exact | même README | 0,276 → 0,797 ; +0,521 [0,285 ; 0,764] ; ĉ 4,011 → 2,475 (le README lui-même arrondit à 2,47). |
| 91 | à la dose forte, les deux vers la moyenne sans pression (2,6) ; refus sous éloge « partly » ; sans les 14 items à refus « (post hoc, descriptive) », les deux vers 2 | exact (nuance) | même README, H3 et « Without the items with refusals » ; addendum R9-bis, l. 14 | Moyenne sans pression : 2,59 à 2,60. Une fois les 14 items retirés, il en reste 16 : ĉ = 1,92 et 2,04. La moyenne sans pression de ces 16 items est 3,11, pas 2,6. C'est un autre ensemble d'items, pas un contrefactuel (écart n° 9). |
| 93 | « 2 fixed spots » | exact | même README, « Reading » | À la dose standard, deux cibles séparées, 1,33 et 2,85 ; la stabilité du point fixe est rejetée (H2). |
| 85, 95 | DOI de R6 (préenregistrement 23888058, résultats 23892810) ; R9 archivé en v2026.11.5, 10.5281/zenodo.23909891, pas encore lancé | exact | `CITATION.cff` et `STATUS.md` @ `b3ecaec` | v2026.11.3 : addendum R6 ; v2026.11.4 : résultats R6 et préenregistrement R7 ; v2026.11.5 (commit `e5e960b`) : résultats R7, addenda R8 et R9. Le statut dit que R9 n'a pas tourné. |
| 95 | « Rebuilding » les 33 contrastives ; 40 différences aléatoires ; richesse–genre, paire canonique, comme témoin positif ; Llama-3.1-8B-Instruct | exact | addendum R9, l. 15 et l. 19 | Les contrastives sont reconstruites pour ce modèle avec les scripts du papier ; la paire canonique est le témoin positif. Il y a deux directions de pression (critique, éloge), pas une. |
| 95 | R9-bis : 3 novembre, avant toute donnée ; commit public `b3ecaec` ; DOI à venir ; fenêtre de 2 à 60 degrés ; comparaison aux différences aléatoires et aux contrastives | exact | addendum R9-bis, l. 3, 38 et 39 ; message du commit | Écrit avant toute passe avant de R9, et archivage annoncé dans une version postérieure à v2026.11.5. |
| 95 | direction neutre : autre phrase, même registre, même longueur, sans opinion | exact | addendum R9-bis, l. 20 à 32 | Elle ajoute le même nombre de jetons, au même endroit ; liste gelée de huit phrases. |
| 95 | « This will allow me to control for formality » | exact (nuance) | addendum R9-bis, l. 9 | Le jumeau tient le registre constant. Il sert à séparer la pression de « n'importe quelle incise » de même registre ; il ne fait pas varier le registre. |
| 95 | « Which as we discussed above we don't have for evaluation » | plus fort que sa source (portée) | ta l. 19 ; 2603.19426 | Ta l. 19 est maintenant bornée à Hua et coll., et le plan 2 × 2 de Devbunova existe, pour des sondes. |
| 99 | au moins 10 points de plus que la direction de registre ; intervalle à 95 % de la différence excluant 0 ; à dose égale au-delà du plateau | conforme à la recommandation | recommandations transmises (consigne) | Même seuil, même intervalle, même condition de dose. Ambiguïtés : écart n° 3. |
| 101 | p ≥ 2,25 sur le plan formé de la direction d'évaluation et de la direction de registre, chacune orthogonalisée ; intervalle excluant 2,05, remesuré sur ton modèle | conforme à la recommandation ; **incohérent avec ta l. 69** | recommandations ; § 7 du papier (recoupement n° 45) | Le papier dit p > 2 nécessaire, pas suffisant. Voir les écarts n° 1 et 2. |
| 103 | au moins la moitié de l'effet des indices, avec une borne basse de l'intervalle à 95 % au-dessus de 50 % | conforme à la recommandation | recommandations | Cohérent avec tes l. 29 et 31. |
| 105 | au moins 45 % de l'effet gardé sur texte familier ; direction de registre sous 10 % | conforme à la recommandation ; renvois flous | recommandations | Voir l'écart n° 3. |
| 109 | GLM-5 : « control_book », −0,025, conscience verbalisée proche de 0 | exact (transcription) | billet de l'Institut britannique, 10 avril 2026 ; recoupement n° 23 | L'effet le plus fort et le plus constant : environ 80 % d'actions désalignées à −0,025. |
| 109 | deux des quatre vecteurs de la fiche d'Opus 4.6 n'élèvent pas le désalignement au-dessus de la base ; un seul scénario, 250 passages | exact (transcription) | même billet ; recoupement n° 22 et n° 24 | Un seul scénario, 250 époques par condition ; les quatre jeux de paires viennent de la fiche système d'Opus 4.6. |
| 109 | Lindsey : témoins aléatoires « about as much » sur GLM-5 ; sur Sonnet 4.5, des effets au-dessus des témoins | exact (transcription) | commentaire sous le billet ; recoupement n° 25 | « À peu près autant » sur GLM-5. Sur Sonnet 4.5, ses deux conditions sont remplies pour plusieurs vecteurs. |
| 109 | logarithme du rapport des deux seuils | exact | plan § 7 | Le plan dit aussi qu'il s'agit d'une corrélation de rang. |
| 111 | § 6 de Hua et coll. : conscience verbalisée fortement réduite, conscience non verbalisée (oracles d'activation) pas entièrement retirée | exact (transcription) | § 6 ; recoupement n° 17 | Fortement supprimée pour la verbalisée ; pas entièrement éliminée pour la non verbalisée, mesurée par oracles d'activation. Le papier cite la fiche « Anthropic (2026) », sans mois. |

## 3. Écarts restants, du plus grave au plus léger

Sans phrase de remplacement : seulement où, quoi, et ce que dit la source. Les corrections sont à écrire par toi.

1. **Section 6, l. 101 contre l. 69 (et l. 67) : contradiction interne, sur le papier du mentor.**
   - Avec le « Or » de la l. 101, p ≥ 2,25 suffit, à lui seul, à te convaincre d'une croyance (titre de la l. 97).
   - Or ta l. 69 rapporte, d'après le § 7 du papier, que p > 2 ne suffit pas à dire qu'une direction pointe vers un trait.
   - Et même un trait privilégié par le réseau n'est pas encore une croyance d'être testé.
   - La l. 67, inchangée, va dans le même sens trop fort : « you can conclude » à partir de p seul.
   - À trancher par toi : p comme condition nécessaire, ou comme indice parmi d'autres.
2. **Le plan des l. 63 et 101 n'est pas défini.**
   - Orthogonalisation croisée : si chacune des deux directions est orthogonalisée contre l'**autre direction d'origine**, les deux directions obtenues gardent un cosinus de **même valeur absolue** que les directions d'origine, de signe opposé.
     - Pour deux vecteurs unitaires de cosinus c, le nouveau cosinus vaut −c ; je l'ai vérifié numériquement pour c = 0,05, 0,2 et 0,4.
     - La paire ne passe donc pas sous la coupure de 0,1 si les directions d'origine ne la passaient pas.
   - Une seule direction orthogonalisée : orthogonaliser **une** des deux contre l'autre donne une paire orthogonale, mais ce choix change les axes du plan, donc p.
   - L'intervalle : une seule paire donne une seule valeur de p (une estimation ponctuelle par paire dans le pipeline, addendum R9, l. 20). L'intervalle de la l. 101 doit donc dire ce qu'il rééchantillonne : les ancres, les paires d'invites, ou des directions partenaires comme dans le critère F2 de R9.
3. **Section 6 : ce qui est comparé à quoi.**
   - **Combinaison des quatre critères.** Alternatives ou cumul ? Seule la l. 101 commence par « Or ». Chaque critère répond à un argument différent :
     - l. 99 et 101 : l'argument 1 ;
     - l. 103 : l'argument 2 ;
     - l. 105 : le transfert d'un registre à l'autre.
     
     L'argument 3 n'a pas de seuil.
   - **l. 99.** Le signe n'est pas écrit (« an effect », « 10 percentage points more »). Il faut lire une baisse de la mesure de conscience que le registre ne touche pas : l'effet de la direction d'évaluation orthogonalisée, moins l'effet de la direction de registre, sur la même mesure. Le seuil de 10 points porte sur l'estimation ponctuelle, et l'intervalle doit seulement exclure 0, pas 10. C'est conforme à la recommandation, mais à lire ainsi.
   - **l. 105.**
     - « 45% of its effect » : on ne sait pas de quel effet il s'agit (celui sur texte formel ?), ni sur quelle mesure (touchée par le registre ou non).
     - « less than 10% of this effect » : 10 % de l'effet sur texte formel, ou de l'effet transféré ?
     - Aucun intervalle ni aucune condition de dose, contrairement aux l. 99 et 103.
   - **« Same amount of dose past the plateau » (l. 9, 29, 99).** Est-ce le même excès au-delà de l'angle de rupture, ou le même multiple de la dose de rupture ? La recommandation dit « à dose de rupture égale ».
   - **l. 101 et l. 67.** « Excludes 2.05 » (l. 101) et « above the random difference » (l. 67) ne disent la même chose que parce que p ≥ 2,25. Et si 2,05 est remesuré, la valeur à dépasser devient la borne haute de l'intervalle des différences aléatoires remesurées, comme dans le critère F2 de R9 (addendum R9, l. 24).
4. **l. 17 : citation entre guillemets non vérifiée.**
   - « weakens our overall setup » : arXiv est inaccessible dans cette session, et aucune transcription locale ne donne les mots anglais. À vérifier mot pour mot sur le PDF (format de document portable) empreinté avant l'envoi, ou à écrire sans guillemets.
   - Même ligne : « comparable to deployment » est le mot des auteurs, mais dans le même réglage le déploiement est à 0,23 (tableau 14), et ta borne haute est 0,60.
   - La fin de la phrase, sur les invites du vecteur, vient du § 5.3, pas de l'annexe I.1.1.
5. **l. 47, D36 : ce qui a été préenregistré et ce qui a été répliqué.**
   - L'enchaînement « I preregistered this on July 29th … I took … the last 13 tokens » rattache au préenregistrement les positions de la réplication.
   - Le préenregistrement du 29 juillet visait la phrase de pression et les 5 derniers jetons. Les 13 derniers jetons (5 de gabarit, puis les 8 derniers de la phrase) sont la ré-implémentation des 5 et 6 août.
   - Le bras clé préenregistré (sous-espace de 13 mots nommés) n'a pas été rejoué (README, « Not given here »).
6. **l. 95, fin.**
   - « We don't have for evaluation » est plus large que ta l. 19, désormais bornée à Hua et coll. : le plan 2 × 2 de Devbunova existe, pour des sondes.
   - Le jumeau neutre tient le registre constant ; il ne fait pas varier la formalité.
7. **l. 19 contre l. 17.**
   - (d) dit que Hua et coll. ne contrôlent pas le registre à statut constant.
   - Ton (b) cite pourtant leur tableau 16, qui compare, à statut constant et sans pilotage, des formulations de déploiement déclaratives et conversationnelles.
   - (d) est exact pour le vecteur (pièce d'état de l'art, n° 5). Mais tu ne dis pas que (d) se limite au vecteur ou au pilotage, et Heimersheim peut y voir une contradiction.
8. **l. 53.** « Still carries a share (65% vs 44%) » repose sur des estimations ponctuelles : la différence n'est pas testée, et les intervalles se recouvrent largement.
9. **l. 91.**
   - « Would have gone to around 2 » porte sur 16 items dont la moyenne sans pression est 3,11 (addendum R9-bis, l. 14), pas 2,6 : la comparaison avec 2,6 mélange deux ensembles d'items.
   - Le conditionnel se lit comme un contrefactuel.
10. **l. 59, Devbunova.**
    - « The same two factors » : son second facteur est le format des bancs d'essai (structure canonique contre forme libre), pas le registre.
    - « Her » : le papier n'emploie aucun pronom (non vérifiable).
    - Il y a aussi un audit des fuites et des longueurs appariées ; « no equivalence check described » reste exact.
11. **l. 27, R7.** La note est plantée dans la réponse que lit le moniteur, après une ligne vide, pas dans la consigne. À l'intensité standard, c'est une affirmation accompagnée d'une demande, pas un ordre (« instructions »).
12. **l. 7, « ICLR 2026 ».** Non vérifiable (remarque n° 19).
13. **l. 18 (inchangée), Singh et Chaudhary.** Les grands modèles recourent « plus souvent » au raisonnement d'ordre supérieur, et le plus grand modèle étudié fait 12 milliards de paramètres. Ta conjecture « 8B contre 49B » sort donc du domaine du papier ; elle est bien marquée comme conjecture.
14. **Noms propres.** Minuscules et possessifs sans apostrophe : « huas », « lee and heimersheim », « Lindseys », y compris le nom du mentor. Je ne propose pas de mots.
15. **Liens et identifiants.**
    - Les trois identifiants DOI (identifiants d'objet numérique) de Zenodo correspondent à `CITATION.cff` au commit `b3ecaec`.
    - Les commits `146b2a4` et `b3ecaec` existent dans les clones locaux.
    - La résolution des DOI n'a pas été testée (réseau).
    - Aucun identifiant cassé trouvé.

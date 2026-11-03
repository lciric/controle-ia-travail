# Lecture comme le mentor — Shi Feng et Eyon Jang — réponse v1

Heure (`date -u`, temps universel coordonné) : début mardi 3 novembre 2026, 12:50 ; vérifications finies 13:02 ; rédaction 13:02 à 13:12.
Lecteur : instance neuve, auteur d'aucune version des réponses de Lazar Ciric au formulaire Pivotal. Consigne : `brouillons/reprise-conv-audit-2026-11-02-nuit/prompts-sous-agents/lecteur-mentor-jang-feng-v1.md`, empreinte SHA-256 `932771189574f7ba61a7a5563d936da334f2a89ab7d880604b497c82713c5342`, vérifiée (concordante avec son compagnon).

## Verdict

Réponse dense, ancrée dans les travaux des deux mentors, et **tous ses chiffres sont exacts sur leurs sources** (vérifiés un à un ci-dessous). **Un point bloquant** : le test de transfert proposé à Jang suppose que ses deux recettes forment une paire, ce que son propre papier dément (tâches, outils et déclencheur différents). **Trois points à corriger** : la moitié « méthodes boîte blanche pour l'audit » de la question manque, avec toute preuve positive de valeur ; « Ville's threshold » arrive sans définition ; la phrase sur P3 se lit deux fois. Compte : 493 mots, sous la visée de 500 ; les corrections coûtent environ 44 mots, à compenser par des coupes (section 6).

## Pièces lues

| Pièce | Empreinte SHA-256 ou état | Contrôle |
|---|---|---|
| Réponse, `brouillons/redaction-finale-v1/jang-feng/reponse-v1.md` | `9d874fcf3eff51105b01509b795175cc28c1dbbbcbe23de10a4844c2fca66094` | vérifiée avant lecture |
| Question, `brouillons/candidature-pivotal-v16/formulaire-site-colle-par-lazar-2026-11-03-1209.txt`, ligne 82 : « What are your thoughts on the value of white-box monitors and white-box methods for auditing? What do you see as their current limitations? » | `57393598f012eb641e709db42efe4b52321c7061e0ff8954910f061019f7b5c6` | concordante avec son compagnon |
| Rapport sur les mentors, `brouillons/candidature-pivotal-v16/lecture-approfondie-v1/rapport-jang-feng-v1.md` | `1c8a4ff27c6ed9103b012899d0758adbe6b99ef8de9bf0937b11edc4ffde686b` | concordante avec son compagnon |
| Fichiers PDF (format de document portable) de `docs/sources/pdf/` : 2411.17693v1, 2507.12691v3, 2509.21344v2, 2512.07810v1, 2609.36490v1 | `13a93a48…`, `0c00a77b…`, `aaac4ff9…`, `77e64bcd…`, `eb6d5bbe…` | les cinq concordantes avec leurs compagnons ; texte extrait par `pdftotext` |
| arXiv 2604.28182v1 (Jang et al.) et 2409.12822v3 (Wen et al., Feng dernier auteur) | version web d'arXiv | `WebFetch`, questions ciblées ; deux questions concordantes pour 2604.28182 |
| `lciric/ideation-organism`, commit `faff48b` : pages `resultats/controle-simulation-defenses/`, `resultats/controle-p3-premier-test/`, `resultats/controle-r1-blanche-noire/`, `README.md` | clone local `/home/claude/ideation-organism`, lu par `git show` | dépôt public selon l'interface GitHub (`private = False`) ; commit présent à distance (poussé le 3 nov. 2026, 10:23:43) |
| `lciric/sycophancy-psychophysical-law`, commit `b3ecaec` : `results/R7/README.md`, `results/R7/R7_descriptive.json` | clone local `/home/claude/scratch/depots-publics-2026-11-03/sycophancy-psychophysical-law`, lu par `git show` | tête distante = `b3ecaec` (`git ls-remote`, lecture des références seule) ; visibilité non vérifiable d'ici (voir réserves) |

Non lus, pour lire comme le mentor : le registre d'affirmations et la note de piste du rédacteur (même dossier).

---

## 1. La phrase qu'il contredirait

**1.1 — Jang, sur son propre banc. Gravité : bloquant.**
Citation : « Train a probe on one of your two Qwen3-14B recipes (RL-locked, SFT-distilled; arXiv 2604.28182) and test it on the other, next to black-box judges, at a false-alarm rate calibrated on honest episodes of the same task, against a random-probe floor. »
Ce qu'il dirait : nos deux recettes ne forment pas une paire. Le verrouillage par apprentissage par renforcement est **inconditionnel**, sur KernelBench et sur WMDP-Bio (Weapons of Mass Destruction Proxy, volet biologie) **sans outils** ; la distillation par affinage supervisé (SFT, supervised fine-tuning) est **conditionnelle, à déclencheur** : `import inspect_ai` sur BigCodeBench, balise `[eval]` sur WMDP-Bio **avec un outil de recherche**. Passer d'une recette à l'autre change donc aussi la tâche, les outils et la présence d'un déclencheur. Et un organisme inconditionnel n'a pas d'épisodes honnêtes à lui : sa référence est le point de contrôle d'avant verrouillage (« pre-locking baseline »), d'autres poids. Une sonde entraînée « verrouillé contre non verrouillé » risque de lire l'affinage, pas le comportement.
Source : 2604.28182v1, § 3.1 et 3.2, figure 1 (version web d'arXiv, deux questions ciblées concordantes). Seule tâche commune : WMDP-Bio, dans deux montages différents ; aucun organisme distillé par affinage supervisé sur WMDP-Bio sans outils.
Pourquoi bloquant : c'est l'expérience proposée « with you » à l'un des trois premiers auteurs (contribution égale), et la correction coûte neuf mots.
Correction minimale : après « test it on the other », insérer « on WMDP-Bio, the one task both lock, » ; remplacer « of the same task » par « (the unlocked checkpoint; trigger-off runs) » (+9 mots).

**1.2 — Feng : aucune phrase contredite par ses résultats.**
Vérifié : la définition du cadre des menaces diffuses est presque mot pour mot celle de 2411.17693 (p. 1 : « no single action is catastrophic and no single action provides overwhelming evidence of misalignment ») ; la phrase sur 2409.12822 est exacte (méthode de sondage « from MacDiarmid et al. (2024) » ; « nearly perfect AuROC (99.3%) in detecting incorrect programs generated by sleeper agent » ; « This probing method fails for detecting U-Sophistry, performing no better than chance »).
Nuance qu'il soulèverait, sans contradiction : « including protocol switches an agent can see ». Dans 2411.17693, l'attaquant est sans mémoire par hypothèse (annexe, p. 21 : « Umalign must follow a memoryless policy ») ; la mise en garde sort donc de son cadre. C'est un atout si c'est dit (section 5).

## 2. Affirmations plus fortes que leur preuve

**2.1 — 2609.36490. Gravité : mineur.**
Citation : « Models shown a monitor's past verdicts already edited their activations the evading way, too weakly; a rank-1 LoRA amplified that into evasion (true positive rate 100% → 4% on held-out concept monitors, arXiv 2609.36490). »
La source : « amplifies this behavior into effective evasion » et « 100% … 4% on held-out concept monitors » sont les mots du résumé (p. 1) : exact. Mais au dernier tour le modèle est aussi **instruit** d'imiter l'étiquette négative (condition « suppress ») et sa sortie est **forcée** (§ 3, p. 4) ; les moniteurs lisent des thèmes dans des passages synthétiques (« physics, spanish or sarcastic » ; deception et sycophancy parmi les dix concepts tenus à l'écart) ; le taux de vrais positifs est mesuré à 1 % de faux positifs (§ 3, p. 5). « Shown … verdicts » seul laisse croire à une évasion spontanée.
Correction : « Models told to evade and shown a monitor's past verdicts… » et « (true positive rate at 1% false alarms: 100% → 4% …) » (+6 mots).

**2.2 — « So verdicts must be guarded ». Gravité : mineur.** Un seul préprint, sortie forcée, concepts synthétiques. Correction : « must » → « should ».

**2.3 — « A probe takes no orders ». Gravité : mineur.** Absolu ; la même réponse cite 2509.21344, où une consigne placée dans le contexte « fuit » dans ce que lit la sonde (« elicitation leakage », p. 1). La phrase suivante nuance (« A probe can still be beaten through the model it reads »). Correction possible, même longueur : « A probe has no instruction channel; a text monitor does. »

**2.4 — R7. Gravité : mineur.**
Citation : « In my preregistered R7, … the 1.5B, 3B and 32B monitors put 98–100% of their readings there, against 20.5–48% without it (descriptive; the 72B shifted, not captured) ».
Chiffres exacts, recalculés sur `results/R7/R7_descriptive.json` : 1.5B 100 % contre 48 % ; 3B 98,3 % contre 20,5 % ; 32B 100 % contre 38 %. Mais la page liée s'ouvre sur « Outcome: C, not the predicted A », que la réponse ne dit pas. Le choix des trois tailles ne gonfle pas le point : les quatre autres ont aussi bougé vers le score ordonné (0.5B : 82,5 % contre 25,3 % ; 7B : 62,8 % contre 0 % ; 14B : 49,3 % contre 20 % ; 72B : 62,5 % contre 22,2 %).
Correction : « (descriptive; preregistered outcome C; the 72B shifted, not captured) » (+3 mots).

**2.5 — T0.3, « 21–35% false alarms in the strongest settings ». Gravité : mineur, aucune correction requise.** Exact (page `controle-simulation-defenses` : 0,21, 0,35 et 0,24, les trois plus forts effets d'épisode de la grille ; 0,046 à 0,055 après calibrage sur 1 000 épisodes honnêtes entiers). La page précise que ces cellules ont été choisies après des courses exploratoires (« it does not predict them blind ») ; la réponse ne dit pas le contraire. À savoir si le mentor demande.

## 3. Ce que la question demande et qui manque

**3.1 — La moitié « white-box methods for auditing », et toute preuve positive de valeur. Gravité : à corriger.**
L'audit n'apparaît que dans la phrase sur 2602.08877. Rien sur les méthodes qui demandent les poids : l'élicitation par affinage, le bruit de poids, que le papier de Jang emploie lui-même (bruit sur les paramètres de l'adaptateur LoRA, adaptation de bas rang, de l'organisme BigCodeBench ; élicitation par affinage supervisé, § 4.2). Et chaque résultat cité est soit un échec de la boîte noire (R7), soit un échec ou une attaque de la boîte blanche (2602.08877, 2609.36490, P3, 2409.12822) : la « valeur » ne repose que sur un argument.
Correction, une phrase vérifiée sur 2512.07810v1 (résumé, p. 1 : « Linear probes … showed more promise » ; « training-based elicitation consistently elicited full performance … using only a single correct demonstration » ; « the performance of benign models was sometimes also raised ») : « In the auditing game, probes showed more promise than black-box methods, and fine-tuning on one demonstration restored full capability but also raised benign models (arXiv 2512.07810). » (26 mots.)

**3.2 — Accès aux poids, et « lisible n'est pas causal ». Gravité : mineur.** Présents dans la réponse actuelle du formulaire (lignes 88 et 98), absents ici : choix de place défendable.

## 4. Ce qui le perdrait

**4.1 — « Ville's threshold at α = 0.05 » sans définition. Gravité : à corriger.** La réponse ne nomme jamais de test valide à tout instant ; « bank » (§ 1) n'est pas expliqué. Correction : au § 1, « bank weak per-action scores in an anytime-valid test, at a false-alarm rate fixed in advance » (+4) ; au § 3, « Ville's threshold (1/α) » (+1).

**4.2 — La phrase P3 se relit. Gravité : à corriger.** « Neither generic probe » suppose deux sondes jamais présentées ; « areas » désigne l'aire sous la courbe ROC (receiver operating characteristic), que la fin du même paragraphe appelle « AUROC » ; « areas below 0.63 and 0.60 not excluded » est une négation double. Correction : « Neither of two generic probes (deception, high stakes) … (it could miss AUROCs up to 0.63 and 0.60) … (AUROC 0.89, descriptive) » (+4 mots). Garder le fond des réserves : la page P3 exige qu'elles suivent ces conclusions partout où elles sont citées (« They must accompany the conclusions they target wherever these are cited ») ; « (cause not measured) » et la borne de puissance y sont, c'est bien.

**4.3 — « the assumed law ». Gravité : mineur.** Gallicisme ; la réponse dit « honest distribution » ailleurs. Correction : « law » → « distribution ».

**4.4 — « captured » (R7) et « the strongest settings » (T0.3). Gravité : mineur.** Jargon de la loi d'attraction ; réglages de quoi ? Corrections : « the 72B moved toward 1 without obeying » ; « for the largest shared shifts ».

**4.5 — Étiquettes internes R7, T0.3, P3, R1. Gravité : mineur.** Chacune est près de son lien, sans gêne grave. Mais P3 et R1 portent sur les mêmes 2 400 actions : le lecteur peut se demander pourquoi des sondes y sont déjà lues (P3) alors que la comparaison « is not in yet » (R1). Correction possible : « (R1, probes against black-box judges) ».

**4.6 — « a declared cost ». Gravité : mineur.** On ne sait pas ce que l'agent déclare (des propositions avec un coût en heures, d'après la page P3).

**4.7 — « including protocol switches an agent can see ». Gravité : mineur.** Elle se relit, et le lien au macro-protocole de Feng n'est pas dit (section 5).

Sans problème : trois liens, chacun avec sa raison, figés sur un commit ; les sigles employés (SAE, sparse autoencoder ; LoRA ; SFT ; RLHF, reinforcement learning from human feedback ; AUROC) sont courants pour ces lecteurs.

## 5. Ce qui le retiendrait — à ne pas couper

- L'ouverture sur le cadre de Feng, avec sa définition presque mot pour mot (2411.17693, p. 1) : la réponse prend position sur son terrain.
- R7 : un résultat propre, préenregistré, public, reproductible ; les chiffres cités sont exacts.
- T0.3 avec 2507.12691 : une mesure chiffrée de l'échec de la règle de Ville sous effet d'épisode, et du remède ; citation exacte de la sonde « Pairs » (2507.12691, p. 9 : jeu Backdoors, du code, au-dessus de 99,9 % d'Alpaca).
- P3 : un résultat nul honnête contre un plancher de 200 sondes aléatoires appariées en covariance, réserves portées ; et l'aveu que le coût déclaré seul sépare à 0,89 (page P3 : 0,8878 sur 926 actions à coût lisible).
- 2409.12822 donné comme raison du test croisé : cela touche la direction 1 de leur flux MATS (ML Alignment & Theory Scholars), l'étiologie des organismes.
- Le § 6.2 de Jang (« Our model organisms rely on explicit CoT reasoning, making them detectable by text-based monitors », CoT désignant la chaîne de raisonnement) avec le filtrage de 2509.21344 (exact : « score filtering » et « content filtering », p. 2) : un plan concret, tiré de leurs propres limites.
- La fuite des verdicts (2609.36490, note 1, p. 4 : « as a blocked tool call or a rejected output ») étendue aux bascules de protocole : une critique propre au macro-protocole de Feng, dont l'attaquant est sans mémoire (p. 21). Si la place le permet, la rendre explicite : « including switches of an adaptive protocol like yours, harmless against a memoryless attacker but visible to a real agent ».
- R1 « null or not » : cohérent avec la page publique (« Not in yet »).

## 6. Compte de mots et limite

- Mon script (Python, `str.split` sur le texte qui précède le trait) : **493 mots**, 3 319 caractères (3 320 chez le rédacteur, fin de ligne comprise) ; cinq paragraphes de 46, 129, 90, 121 et 107 mots ; 490 sans les trois liens ; 577 avec un compteur qui coupe sur la ponctuation.
- Limite écrite : aucune. Visée de 500 mots au plus : **tenue**, marge de 7 mots. Ne coller que le texte au-dessus du trait (le compte en dessous n'est pas de la réponse).
- Coût des corrections bloquante et à corriger : +9 (1.1), +26 (3.1), +5 (4.1), +4 (4.2), soit +44 mots (537 au total) : il faut couper environ 37 mots. Candidats, au choix du rédacteur (mots gagnés) : « My first test did not show the signal. » (8) ; « So what I would run first with you is a transfer test. » → « First, with you, a transfer test: » (6) ; « I think, » (2) ; « (0.5B to 72B) » (3) ; « (MacDiarmid et al.) » (3) ; « its result will be posted » → « it will be posted » (2) ; resserrer la phrase R7 (environ 14). Ne pas couper : « descriptive », « (cause not measured) », la borne de puissance de P3.

## Tableau des points

| # | Gravité | Point | Correction minimale |
|---|---|---|---|
| 1.1 | bloquant | Le transfert entre les deux recettes de Jang croise recette, tâche, outils et déclencheur ; l'organisme inconditionnel n'a pas d'épisodes honnêtes à lui | « on WMDP-Bio, the one task both lock, » ; « (the unlocked checkpoint; trigger-off runs) » |
| 3.1 | à corriger | La moitié « audit » de la question et toute preuve positive de valeur manquent | Phrase sur le jeu d'audit (2512.07810), 26 mots |
| 4.1 | à corriger | « Ville's threshold » et « bank » sans définition | « in an anytime-valid test » ; « (1/α) » |
| 4.2 | à corriger | Phrase P3 : deux sondes non présentées, « areas » contre « AUROC », négation double | « Neither of two generic probes (deception, high stakes) » ; « it could miss AUROCs up to 0.63 and 0.60 » |
| 2.1 | mineur | 2609.36490 : modèle instruit, sortie forcée, taux pris à 1 % de faux positifs | « told to evade » ; « at 1% false alarms » |
| 2.2 | mineur | « must be guarded » pour un seul préprint | « should » |
| 2.3 | mineur | « A probe takes no orders » absolu | « has no instruction channel » |
| 2.4 | mineur | Issue préenregistrée C de R7 non dite | « preregistered outcome C » |
| 2.5 | mineur | Cellules fortes de T0.3 vues en exploration avant scellement | aucune |
| 3.2 | mineur | Accès et causalité retirés | aucune |
| 4.3 | mineur | « law » | « distribution » |
| 4.4 | mineur | « captured », « strongest settings » | voir 4.4 |
| 4.5 | mineur | Étiquettes internes ; P3 et R1 sur les mêmes actions | « (R1, probes against black-box judges) » |
| 4.6 | mineur | Ce que déclare l'agent n'est pas dit | « proposals' declared cost (hours) » |
| 4.7 | mineur | Bascules de protocole : lien à Feng implicite | voir section 5 |

## Réserves du lecteur

- 2604.28182 et 2409.12822 ont été lus par questions ciblées sur la version web d'arXiv (le petit modèle de lecture résume, il ne copie pas). Pour 2604.28182, deux questions ont donné des réponses concordantes ; la référence honnête des organismes inconditionnels (« pre-locking baseline », « base model performance ») est déduite par ce modèle, pas écrite en toutes lettres. Ces deux papiers n'ont pas de fichier PDF empreinté dans `docs/sources/pdf/` : avant envoi, relire le § 3 de 2604.28182 sur le PDF si possible.
- Visibilité publique de `lciric/sycophancy-psychophysical-law` non vérifiable d'ici : l'interface GitHub est refusée par le mandataire pour ce dépôt, et `WebFetch` refuse github.com. Tête distante `b3ecaec` confirmée par `git ls-remote` (lecture des références, rien de téléchargé ni de modifié). Ouvrir le lien R7 dans une fenêtre de navigation privée avant l'envoi.
- Pages de `ideation-organism` lues dans le clone local au commit `faff48b` (sans `git fetch`) ; l'interface GitHub confirme le dépôt public et le commit présent à distance.
- Les numéros de page des PDF renvoient à l'index du fichier extrait.

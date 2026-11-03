# Heimersheim, question 2 — registre des affirmations de `reponse-v1.md` — v1

Rédacteur neuf (sous-agent de conv-audit), 3 novembre 2026, vers 13:10 UTC, temps universel coordonné (`date -u`). Une ligne par affirmation de la réponse, dans l'ordre du texte.

Forces :
- « publique et vérifiée » : lue sur un fichier public, au commit cité ;
- « interne vérifiée » : fichier daté non public, chemin et sha256 ;
- « non vérifiée » : interdite dans la réponse, et absente.

Les arguments et la question de recherche n'affirment aucun fait. Ils sont listés à part, avec les faits sur lesquels ils reposent.

## Sources (empreintes recalculées le 3 novembre)

| abréviation | fichier | état | sha256 |
|---|---|---|---|
| [cv] | `/home/claude/scratch/depots-publics-2026-11-03/sycophancy-construct-validity/README.md` | public, commit `146b2a4`, tête de `origin/main` au clonage (12:21 UTC) | `de5d6032d42cc2eb893e2d1339ae0c6423c4cebc2e1b7ecc83d35cf9c3154da8` |
| [R9] | `/home/claude/scratch/depots-publics-2026-11-03/sycophancy-psychophysical-law/preregistrations/2026-11-02_addendum_R9_feature_specific_error_correction.md` | public, commit `b3ecaec` ; archivé dans v2026.11.5, 10.5281/zenodo.23909891 (selon [R9b] l. 5) | `81abd962afe1ba8f99840a8b54262b1820184e5a767139712d1e5898d28ce36e` |
| [R9b] | `…/sycophancy-psychophysical-law/preregistrations/2026-11-03_addendum_R9bis_dose_curves.md` | public, commit `b3ecaec`, tête de `origin/main` au clonage ; archive Zenodo à venir | `8c7145036f06ccc8dcd6b4e918d002adb65a6f51917013595263526ec87c5009` |
| [lec] | `brouillons/pilote-exposant-p-v1/lecture-2606-24964-v1.md` (lecture de 2606.24964 par un rédacteur neuf, PDF par convertisseur, code publié des auteurs par empreintes) | interne | `3c550d93ae97e37309ef01a95e1829c946463edf1cd7013110c95c2eed815851` |
| [rec] | `brouillons/candidature-pivotal-v16/lecture-approfondie-v1/recoupement-v1.md` (vérificateur neuf) | interne | `bea573aa1e62d5d5bfb1aa677a902c9ec977ea1740941eed5b4277bae0e4fe0a` |
| [rap] | `brouillons/candidature-pivotal-v16/lecture-approfondie-v1/rapport-heimersheim-v1.md` (lecteur neuf) | interne | `b55e2f243974dcccb52480a0a2cd803dd7cf6497b430b4e9926b4f7eba8aabfd` |
| [fab] | `brouillons/canal-fable-v1/fable_2026-11-03_n001.md` (lectrice indépendante) | interne | `4b9bd5c929e272acd2910722765483bb7a05d53df352ec32e23adbd4992f9e96` |
| [q1] | `brouillons/redaction-finale-v1/heimersheim-q1/squelette-heimersheim-q1-v1.md` | interne | `842e95ef1fca09cc70391bd0e8931573bc329c6743443c9dde914682793caa0e` |

Chemins relatifs : depuis `/home/claude/controle-ia-travail`.

## 1. Faits

| # | Mots de la réponse | Source | Force |
|---|---|---|---|
| F1 | « reading a behaviour did not let me control it » (le fait qui fonde le « because ») | [cv] l. 3 : « Reading a concept out of a model's activations and controlling the behaviour it predicts are different problems. » | publique et vérifiée |
| F2 | « In Llama-3.1-8B-Instruct » | [cv] l. 3 (« In Llama 3.1 8B Instruct ») ; limites (« One model ») | publique et vérifiée |
| F3 | « a probe direction tracked sycophancy (ρ = 0.684, possibly training fit) » | [cv] l. 61 (« The probe direction of *Geometry* below (ρ = 0.684) ») ; l. 70 (ρ = 0,684 sur activations brutes, « treat them as training fit ») ; l. 115 (« ρ may also be training fit ») ; [fab] § 3 (« ρ = 0,684, avec "may be training fit" : juste »). Jamais fondu avec « < 1 % » ([fab] § 2 ; [q1] § 4) | publique et vérifiée |
| F4 | « yet no single-direction intervention I tried reduced it » | [cv] l. 3 (« no single-direction intervention and no head ablation reduced the judged rate ») ; l. 21 (pilotage contrastif, pilotage et ablation directionnels, traits d'autoencodeur épars « clamping », perte auxiliaire : « no clean reduction », sans nombre) ; l. 88 | publique et vérifiée (qualitative ; aucun nombre public) |
| F5 | lien `github.com/lciric/sycophancy-construct-validity` | dépôt public ; faits F1 à F4 vérifiés au commit `146b2a4` | publique et vérifiée |
| F6 | « Your paper with Ferreira da Silva » | [lec] l. 14 (auteurs : Francisco Ferreira da Silva, Pivotal Research, et Stefan Heimersheim) ; [rap] l. 21 | publique et vérifiée |
| F7 | « finds that contrastive directions […] are privileged under your error-correction test (p > 2) » | arXiv 2606.24964, résumé (« the pure directions are privileged »), § 4.1 (Gemma-2-9B, couche 2 : moyenne 2,42 [2,29 ; 2,62]), § 4.3 et légende de la figure 6 (« Fitted exponents remain above p = 2 across all variations ») ; d'après [lec] l. 46-58. Valeurs par défaut égales à l'audit du code des auteurs (`results/thrpair_audit.md`, `272827f3…`, [lec] l. 46) ; sur Llama-3.1-8B de base, le code donne une moyenne de 2,632 [2,388 ; 2,897] ([lec] l. 63). Recoupé : [rec] n° 7 et n° 44 (« exact ») ; [R9] l. 9 (ta propre lecture publique). Aucun nombre de l'article n'entre dans la réponse : seulement le seuil p > 2 | publique et vérifiée (PDF lu au niveau transcription par convertisseur, deux lecteurs ; recoupé sur le code publié) |
| F8 | « readable by construction » | définition : direction contrastive = différence de moyennes entre invites qui diffèrent par le concept (2606.24964 § 3 ; [R9] l. 9, « contrastive difference-of-means directions ») | publique et vérifiée (caractérisation tirée de la définition) |
| F9 | « I have preregistered both measurements on the directions that social pressure adds to the activations » | [R9] en-tête (auteur : Lazar Ciric ; écrit le 2 novembre, avant toute passe) ; l. 16 (deux directions de pression : différence des moyennes, sur 30 paires, avec et sans la phrase de pression, au dernier jeton de l'invite) ; [R9b] en-tête (écrit le 3 novembre, avant toute passe) | publique et vérifiée |
| F10 | « your test » | [R9] l. 20 (le `sweep_2d.py` et le `fit_pairs.py` de l'article, réglages canoniques), l. 24 (F2 : p médian contre 2,05 et contre les différences aléatoires) ; [R9b] l. 52 (F2 inchangée) | publique et vérifiée |
| F11 | « and whether rotating toward them moves the model's ratings » | [R9] l. 20 (ancres B : note attendue Σ k·p(k) sur les jetons « 1 » à « 5 », à chaque angle), l. 25 (F3 « reported, not in the outcome ») ; [R9b] l. 54 (F3 en courbe, même statut) | publique et vérifiée (mesure préenregistrée, rapportée hors de l'issue : la réponse ne dit pas qu'elle décide) |
| F12 | « (R9 and R9-bis, github.com/lciric/sycophancy-psychophysical-law; not yet run) » | [R9b] l. 5 (« R9 has not run ») ; aucun `results/R9/` au commit `b3ecaec` (`git ls-tree`) | publique et vérifiée à 12:21 UTC ; **à reconfirmer par Lazar avant 23:00 UTC** |

## 2. Arguments et question (aucun fait affirmé)

| # | Mots de la réponse | Ce qui les fonde, et leur limite |
|---|---|---|
| A1 | « I want to work on mechanistic interpretability because … » | ta motivation, que toi seul peux confirmer ; son fondement factuel est F1 |
| A2 | « My question is whether a direction the network privileges also controls the behaviour it predicts. » | question, et non résultat. « privileges » et non « feature », parce que p > 2 est nécessaire, pas suffisant (2606.24964 § 7 ; [R9] l. 9). L'issue A de [R9] (l. 26) pose la même distinction. Aucune prédiction : [R9] l. 11 (« no prediction ») |
| A3 | « If yes, your test could screen steering targets, such as an evaluation-awareness direction » | conditionnel. Limite : test validé à la couche 2, sur des invites FineWeb de 5 jetons ; invites de conversation non testées ([R9] l. 9 ; [lec] l. 91). La direction d'évaluation demande un long contexte et des couches moyennes (Hua et coll., arXiv 2510.20487 § 4.1 : couches 10 à 30 ; [rap] point A). Cohérent avec [q1] § 5, qui propose p comme test de la direction d'évaluation |
| A4 | « if no, privilege and control need separate tests » | conséquence logique de A2 |

## 3. Écartés (examinés, non retenus)

| Affirmation | Raison |
|---|---|
| « < 1 % » de l'effet causal | bras clé de l'essai D36 original : non public, non refait, autre objet que ρ ([fab] § 2 ; [cv] l. 61) |
| « 68 % » (D36 original) | non public ([fab] § 2) |
| « single dose interventions » | non décrit publiquement ([rec] réserve 1) |
| signal hors de l'autoencodeur épars (86,8 % de variance dans le résidu ; ρ 0,212 contre 0,696) | public ([cv] l. 70), mais le dictionnaire est très perdant et [cv] l. 118 dit qu'on ne peut pas séparer les deux lectures ; réserve « training fit » |
| têtes alignées contre têtes de patching de chemin, recouvrement nul ([cv] l. 69) | public, mais analyse sur un petit jeu d'invites ([cv] l. 120) ; place |
| « steering against evaluation awareness assumes the readable direction is the causal one » | contredit par Hua et coll. § 5.1 (effet sur le comportement montré ; [rap] l. 48) |
| P3 (sondes génériques sous leur plancher) | public, mais le verdict v2 exige ses trois réserves partout où il est cité (rapport des pages publiques § 1.4, point 5) : trop long pour 150 mots |
| neurosciences computationnelles (Cogmaster, équipe de Srdjan Ostojic) | interne vérifiée (formulaire EA Funds du 7 octobre, `76cdbb3b…7c517c`, l. 15) ; mais l'affirmation sur le domaine (« readable structure and driving dynamics are separable ») n'est pas vérifiée |
| R6, D36, rang 3 | déjà dans [q1] (§ 4, § 5 point 9) : répétition |

## 4. Décompte

- Faits : 12, tous « publique et vérifiée » (F12 à reconfirmer le soir même).
- « interne vérifiée » : 0 dans la réponse.
- « non vérifiée » : 0.
- Arguments ou question : 4.
- Nombres dans la réponse : ρ = 0.684 (F3), p > 2 (F7, un seuil), Llama-3.1-8B-Instruct (F2), R9 et R9-bis (étiquettes).

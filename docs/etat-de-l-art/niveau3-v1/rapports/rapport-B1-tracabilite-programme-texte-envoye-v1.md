# Rapport B1 — contrôle de traçabilité : programme v2 et texte envoyé au fonds — v1

- **Lecteur** : sous-agent neuf du lot B1 (état de l'art, niveau 3). Il n'a écrit ni le programme, ni le texte envoyé, ni les rapports antérieurs.
- **Date** : 2026-11-10 ; fin de rédaction vers 10:55 UTC (heure relevée par `date -u`).
- **Documents contrôlés** :
  1. `docs/programme-controle-ia-v2.md` (277 lignes ; sha256 `2fd63badb5af…`) ;
  2. `docs/sources/candidature-taif-2026-10-07/proposal_v2_TAIF_2026-10-07.txt` (420 lignes ; sha256 `b2458c2d209a…`, conforme à son fichier compagnon).
- **Objet** : chaque chiffre et chaque affirmation qui porte sur un travail d'autrui. Les résultats internes (simulation, P3, comptes de la phase 0, budget) sont hors périmètre.
- **Consigne commune** lue en entier ; interdits tenus ; aucun refus rencontré ; aucun appel au réseau.

## 0. Signalements en tête

**Aucune COLLISION au sens de la consigne** : je n'ai trouvé aucune pièce revendiquée occupée en entier dans les pièces lues pour ce lot. Ce lot n'est pas une recherche d'antériorité ; ce constat ne vaut que pour les pages ouvertes ici (R8).

**Trois erreurs de fait sur des travaux d'autrui, dans le texte déjà envoyé** (contre-résultats défavorables, R4) :

1. **« quorums across judge families (2605.15377) »** (texte envoyé, l. 199-200, et deuxième des huit pièces de la l. 261) : **contredit par le PDF**. Les douze moniteurs de l'article partagent un seul modèle de base : « All monitors use GPT-4.1-mini as the single trusted model. » (p. 4, C53). Les auteurs écrivent qu'ils n'ont **pas** testé d'ensemble entre familles de modèles : « Ensembles drawn from different model families—or that incorporate non-LLM-based signals—may be more resistant, but we have not tested this directly. » (p. 8, C54). Le lecteur du niveau 2 l'avait noté (« non fait : inter-familles », `anteriorite-v1.md`, l. 355). La pièce « quorum entre familles de juges » a donc été retirée des revendications sur une source qui ne l'occupe pas. L'erreur va dans le sens d'une concession de trop, pas d'une revendication de trop ; elle reste une description fausse d'un article, visible par tout lecteur de son résumé.
2. **« A black-box, synthetic precursor (arXiv 2606.10456) »** (l. 87) : le mot « synthetic » est **contredit par ce que l'article imprime**. Il annonce une validation sur traces réelles : « We validate the threat model on real traces. » (p. 8, C05), avec un moniteur réel (« score every step with a live LLM monitor (Llama-3.2-3B-Instruct) », p. 8, C70). Le niveau 1 a établi, d'après le dépôt de code des auteurs, que l'attaque reste synthétique ; mais cette lecture n'est pas dans le PDF, et le texte envoyé ne la cite pas. Un juré qui ouvre l'article lira « real traces ».
3. **« additive accumulation on black-box scores (E-valuator, arXiv 2512.03109) »** (l. 131-132) : la parenthèse attribue à E-valuator une accumulation additive. Le niveau 1 a établi l'inverse : validité par seuil sur le maximum, « pas de somme cumulée » (`etat-de-l-art-verifie-niveau1-v1.md`, l. 28 et 80, p. 3–8 du PDF). L'article se décrit comme « a method to convert any black-box verifier score into a decision rule with provable control of false alarm rates » (p. 1, C31). Si la phrase veut dire « notre base additive, dans l'esprit d'E-valuator », elle ne le dit pas.

## 1. Bilan chiffré

| | programme v2 | texte envoyé | total |
|---|---|---|---|
| affirmations relevées sur un travail d'autrui | 32 | 69 | **101** |
| dont : la ligne porte elle-même une page | 0 | 1 (l. 36, « p. 2 ») | 1 |
| dont : la ligne porte un identifiant (arXiv ou SSRN) | 5 | 55 | 60 |
| **tracée (PDF, page)** après ce passage (page d'un lecteur antérieur ou relevée par moi, citation contrôlée) | 21 | 57 | **78** |
| — dont tracée et **contredite ou fausse telle qu'écrite** | 2 (l. 59, l. 239) | 2 (l. 199-200 et pièce 2 de la l. 261) | 4 |
| — dont tracée **avec réserve** | 5 | 7 | 12 |
| **PDF présent, page non donnée** | 1 | 2 | **3** |
| **sans PDF au dépôt** (identifiant nommé, PDF absent) | 0 | 0 | **0** |
| **source hors archive ouverte, non récupérée** | 1 (ControlArena) | 1 (ControlArena) | **2** |
| **source non désignée** (aucune source nommée, aucune retrouvée ici) | 9 | 4 | **13** |
| **constat d'absence** (« non publié dans les sources vérifiées » ; pas de page possible) | 0 | 5 | **5** |

Lecture du bilan :

- Les 37 identifiants arXiv nommés dans les deux documents, plus le SSRN 7424179, ont **tous** un PDF empreinté sous `docs/sources/pdf/` (vérifié par `ls`, R11). La catégorie « sans PDF » est vide. Ce résultat est propre ; je le signale (R4) : il tient à ce que le niveau 2 a récupéré tout ce que les documents citaient, et il ne dit rien des sources que les documents ne nomment pas (13 lignes).
- Le défaut de traçabilité n'est pas dans les fichiers, il est **dans les textes** : aucune ligne du programme ne porte de page, et une seule ligne du texte envoyé en porte une. La règle 4 du texte envoyé (l. 245-246 : « Numbers from the literature are used only after verification on a hashed PDF, with the page cited ») n'est tenue, dans le texte lui-même, que pour la citation de la l. 36. La l. 400 renvoie le reste à des rapports « available on request ».
- Le catégorie « source non désignée » est une cinquième catégorie, ajoutée par moi : les quatre statuts de la consigne du lot ne couvrent pas une affirmation qui ne nomme aucune source.
- **Contrôle des citations** : 75 citations exactes contrôlées par script contre le texte de la page citée ; **0 échec** au passage final (66 retrouvées par `pdftotext -layout`, 9 seulement dans l'ordre de lecture, sans `-layout`, sur des pages à deux colonnes que l'option entrelace). Un échec au premier passage : la citation C18 était rangée p. 7 ; la page vraie est 5 (corrigé ; la décision N-013 donne bien p. 5). Script testé d'abord sur un cas juste, un cas altéré et un cas de mauvaise page (1 conforme, 2 échecs attendus, obtenus). 21 titres de la liste de références du texte envoyé contrôlés en page 1 avec le nom d'un auteur : 21 conformes.

## 2. Affirmations non tracées ou fragiles les plus exposées devant un jury

Par ordre d'exposition.

1. **Texte envoyé, l. 199-200 et l. 261 — « quorums across judge families (2605.15377) »** : contredit par le PDF (section 0, point 1).
2. **Texte envoyé, l. 87-88 — 2606.10456** : « synthetic » contredit par l'imprimé (section 0, point 2). « its central statement does not hold for its own construction » repose sur **notre** simulation (le texte le dit : « In our simulation »), non sur le PDF. Le PDF donne pourtant un appui direct, non cité : sa table 2 imprime pour la moyenne une puissance de 0,048 à 1 % de faux positifs, soit près de cinq fois le taux nominal (p. 6, C04). Détail en section 5.
3. **Texte envoyé, l. 131-132 — E-valuator et « additive accumulation »** (section 0, point 3).
4. **Texte envoyé, l. 84-85 — « The statistical core is classical and cited »** : aucune référence n'est donnée, ni dans le paragraphe ni dans la liste finale, pour les frontières de mélange, la dichotomie somme/maximum, la décomposition marginale/copule, l'inégalité de Slepian (l. 83), la somme cumulée de Page et les e-détecteurs (l. 67). Le mot « cited » n'a pas de répondant dans le texte. Aucun PDF de ces classiques n'est désigné au dépôt.
5. **Texte envoyé, l. 176 — « the “weight of advice” of judgement psychology »** : aucune source. Et l'article cité juste après (2603.15809) n'emploie pas ce terme : il emprunte le modèle de formation d'opinion de Friedkin et Johnsen (« by borrowing the Friedkin–Johnsen opinion formation model from social sciences », p. 1, C43). L'identification des deux formes est la nôtre.
6. **Texte envoyé, l. 181-183 — Panin (SSRN 7424179)** : l'affirmation est **exacte** (p. 1, C48 ; p. 3, C49), mais le PDF n'a été versé au dépôt que le 20 octobre (`docs/sources/pdf/provenance-voisin-panin-v1.md`), treize jours après l'envoi. Le 6 octobre, les décisions écrivaient « Panin n'est pas lu » (`decision-N-005-N-006-v1.md`, l. 72 ; `proposition-N-013-…`, l. 23). Au jour de l'envoi, le chiffre « three of five models » n'avait donc pas de PDF empreinté ; la phrase de la l. 400 (« page-level verification reports ») ne valait pas pour lui.
7. **Texte envoyé, l. 276 — « The source paper's 18 prompts »** : le nombre 18 n'est pas imprimé par l'article ; c'est notre décompte des blocs transcrits des annexes H et I (`docs/sources/invites-2606.08892-v1/LISEZMOI.md`, l. 8). Le même fichier (l. 84) mentionne d'autres blocs sur les pages lues. Écrire « les 18 invites de l'article » engage plus que ce décompte.
8. **Texte envoyé, l. 71-73 — Ramtin et al. « covers neither total budgets »** : l'article étudie pourtant un « dommage total » cumulé avant détection (p. 3, C73 ; proposition 3.4, p. 10). Il ne **contraint** pas un budget total, ce qui garde la phrase défendable ; mais un juré qui cherche « total » dans l'article le trouvera.
9. **Texte envoyé, l. 35-36 — citation de Terekhov et al.** : la citation entre guillemets supprime sans le dire les deux renvois entre crochets du texte source (« theoretically [Hebbar, 2025] and empirically [Gasteiger et al., 2025, Gan et al., 2026] », p. 2, C10). Sens intact ; forme non verbatim.
10. **Programme, l. 59 — « Koning & Grünwald, arXiv 2208.07610 »** : auteurs faux (le PDF porte Pérez-Ortiz, Lardy, de Heide et Grünwald) ; déjà corrigé par P-008 et repris juste dans le texte envoyé (l. 70). Le programme, document qui fait foi, garde l'erreur dans son texte.
11. **Programme, l. 239 — « équipe Oxford/NYU de NARCBench »** : pas de NYU dans le PDF (niveau 1, `2604.01151v3` p. 1). Non corrigé dans le texte du programme.
12. **Programme, neuf affirmations d'antériorité sans aucune source** : « l'immunité absolue est réfutée » (l. 16) ; « le gain blanc-sur-noir en général est établi » (l. 93) ; « le glissement de construit sous pression est déjà décrit » (l. 99) ; « les sondes captent souvent des corrélats de surface » (l. 104) ; « la H4 d'origine est occupée » (l. 112) ; « recettes publiées » (l. 137) ; Llama Scope (l. 145) ; « codes d'obfuscation d'activations publiés » (l. 197) ; « équipe boîte blanche de l'institut britannique » (l. 239, 277). Pour la l. 99, le niveau 1 (prononcé 10) a établi que la source supposée, 2609.03035, ne décrit aucun glissement de construit.
13. **Texte envoyé, l. 193 — SLEIGHT-Bench comme précédent stylistique « on monitors »** : l'appui que je trouve est mince (« Jailbreaks. Monitors struggle to distinguish monitor prompt from transcript. », p. 4, C52, ligne d'un tableau). La décision N-013 notait déjà « lecture de figure, à trancher sur la transcription ».

## 3. Table — programme v2 (`docs/programme-controle-ia-v2.md`)

Colonnes : ligne ; texte exact (extrait) ; source visée ; PDF au dépôt (début d'empreinte) ; page chez un lecteur antérieur (fichiers nommés par la consigne) ; statut. Les citations « Cnn » sont en annexe, avec page et texte exact. « Niveau 1 » = `docs/etat-de-l-art/etat-de-l-art-verifie-niveau1-v1.md` ; « corrections » = `docs/etat-de-l-art/niveau2-v1/corrections-v1.md` ; « antériorité » = `docs/etat-de-l-art/niveau2-v1/anteriorite-v1.md`.

| n° | ligne | texte exact | source visée | PDF | lecteur antérieur | statut |
|---|---|---|---|---|---|---|
| P01 | 13 | « jamais moyenne ni médiane : ces dernières sont évadables par apprentissage par renforcement sur les poids, max et attention résistent » | non nommée ; 2506.14261 | oui, `4b0960622664` | corrections l. 48-50 (p. 1, 4, 7), « établi dans le cadre testé » | **tracée** (p. 7, C72 ; p. 1, C39), avec réserve : les auteurs avertissent que l'échec peut tenir à l'optimisation (p. 10, C40) |
| P02 | 16, 94 | « le séquentiel boîte noire existe déjà » ; « le squelette séquentiel boîte noire existe » | non nommée ; E-valuator 2512.03109 | oui, `b7a46e4cf781` | niveau 1, l. 28 (p. 3, 4–8) | **tracée** (p. 1, C31) |
| P03 | 16 | « l'immunité absolue est réfutée » | non nommée | — | aucune | **source non désignée** |
| P04 | 59 | « (Koning & Grünwald, arXiv 2208.07610) » : « la notion de puissance n'est pas la même… » | 2208.07610 | oui, `e9e5fd4e0096` | corrections l. 17 (p. 2, 6-7, 26) : « les auteurs sont faux », fond déformé | **tracée, fausse telle qu'écrite** (p. 2, C26, C27) ; corrigée par P-008, pas dans le texte du programme |
| P05 | 60 | « un adversaire couvert qui connaît la contrainte de faux positifs peut imposer un délai de détection d'ordre Θ(γ)… (arXiv 2601.20022) » | 2601.20022 | oui, `8d090f3171ef` | corrections l. 18 (p. 3–4, proposition 3.3), noyau exact, quatre précisions | **tracée** (p. 1, C28, C29), avec réserve (adversaire stationnaire ; conditions) |
| P06 | 66, 96 | « arXiv 2606.10456 occupe la version boîte noire et synthétique du contraste marginale/corrélation (provenance douteuse, preuves élémentaires) » | 2606.10456 | oui, `aaeedd1e7a88` | niveau 1, prononcé 12 et table 2 (p. 1, 3–4, 8, 10) ; décision N-003/N-004, l. 40 | **tracée** (C01 à C09), avec réserve : « synthétique » contredit par l'imprimé (p. 8, C05) ; voir section 5 |
| P07 | 93 | « le gain blanc-sur-noir en général est établi » | non nommée | — | aucune (niveau 2, prononcé 4 : contre-indices pour H1) | **source non désignée** |
| P08 | 99 | « Le glissement de construit sous pression est déjà décrit » | non nommée | — | niveau 1, prononcé 10 : 2609.03035 n'en dit rien ; niveau 2, prononcé 3 : 2605.27958 « en partie », sans page dans ce fichier | **source non désignée** |
| P09 | 104 | « les sondes captent souvent des corrélats de surface » | non nommée | — | aucune | **source non désignée** |
| P10 | 111 | « Les courbes boîte noire sont publiées » | non nommée ; 2607.07368 | oui, `d72cae4337e8` | niveau 2, prononcé 3 (p. 1, 2, 8) | **tracée** (p. 1, C11, C69), avec réserve : l'article fait varier le nombre d'agents, il ne trace pas une courbe « sécurité(N) à budget constant » |
| P11 | 112 | « la H4 d'origine est occupée » | non nommée | — | aucune | **source non désignée** |
| P12 | 122 | « Base : le jeu de Terekhov et al. (arXiv 2606.08892), porté en 8 milliards de paramètres » | 2606.08892 | oui, `aea0f2d192f3` | niveau 1, prononcé 7 et table 2 (p. 2–5, 9, 15–19) : ni code ni données, aucun Llama testé | **tracée**, avec réserve : « porté » est corrigé en « reconstruit » (P-004) |
| P13 | 123 | « FakeLab (Makins et al., sur demande aux auteurs) » | non nommée par identifiant ; 2607.07368 | oui, `d72cae4337e8` | chiffres introuvables, l. 21 : licence introuvable | **tracée** (p. 1, C12 ; auteur p. 1) |
| P14 | 123 | « Iterative VibeCoding (Hills et al., cadre ControlArena, état persistant) » | non nommée par identifiant ; 2607.02514 | oui, `9baceea4719a` | antériorité l. 16 | **tracée** (p. 5, C16 ; titre et auteur p. 1) |
| P15 | 125, 189, 250 | « un cadre de sabotage concentré (ControlArena) » | ControlArena | non : dépôt de code (cité comme « GitHub repository » par 2606.08892, p. 11) | aucune | **source hors archive ouverte, non récupérée** |
| P16 | 133 | « Organismes publics de l'institut britannique… (sandbagging, dont un imitant Llama-3.1-8B-Instruct, verrouillés par mot de passe) » | non nommée ; 2512.07810 | oui, `77e64bcd8875` | niveau 2, prononcé 4 (p. 17, autre point) | **tracée** (p. 7, C61 ; p. 4, C62 ; p. 1, C63). Licence : aucune occurrence de « licen » dans le PDF |
| P17 | 137 | « entraînement sur données génériques (recettes publiées) » | non nommée | — | aucune | **source non désignée** |
| P18 | 145 | « autoencodeurs parcimonieux Llama Scope » | non nommée | aucun PDF repéré sous `docs/sources/pdf/` | aucune | **source non désignée** |
| P19 | 146 | « La revue montre que choisir sur la seule décorrélation perd contre le hasard : la compétence individuelle compte. » | non nommée (« la revue ») | 2605.15377 oui, `fe591700228b` | corrections l. 71-72 : la ligne jumelle de l'état de l'art est « corrigée » et rattachée à 2608.16190 (p. 1, 8) | **tracée** par moi sur 2605.15377 (p. 7, C71), avec réserve : deux sources possibles, et l'article borne le constat (« when poor-performing monitors are included ») |
| P20 | 149 | « TRACE-lite (triage–inspection–jugement, réimplémenté) » | non nommée par identifiant ; 2606.07054 | oui, `9e169bb5eced` | niveau 1, l. 77 (p. 2, 3, 4, 17) | **tracée** (p. 1, C30) |
| P21 | 149 | « accumulation séquentielle sur scores boîte noire (dans l'esprit d'E-valuator) » | 2512.03109 | oui, `b7a46e4cf781` | niveau 1, l. 28, 80 : pas de somme cumulée | **tracée** (p. 1, C31), avec réserve (« dans l'esprit » couvre l'écart) |
| P22 | 150, 215 | « moniteur à état “link-tracker” et ensemble à quatre moniteurs (Hills et al.) » | 2607.02514 | oui, `9baceea4719a` | antériorité l. 16 | **tracée** (p. 1, C14, C15) |
| P23 | 150, 215 | « monitoring à état sur flotte (Brown et al.) » | 2605.31593 | oui, `037f653703ec` | antériorité l. 16 ; chiffres introuvables l. 20 (code introuvable) | **tracée** (p. 1, C13 ; p. 8, C74) |
| P24 | 188 | « Base : Ctrl-Z » | 2504.10374 | oui, `5f802d679344` | niveau 2, prononcé 5 (p. 8-9, autre chiffre) | **PDF présent, page non donnée** (simple attribution ; titre vérifié p. 1) |
| P25 | 197 | « codes d'obfuscation d'activations publiés » | non nommée | — | aucune | **source non désignée** |
| P26 | 201 | « si la collision arXiv 2607.08066 couvre déjà la loi de déférence » | 2607.08066 | oui, `f22075f04c84` | niveau 1, prononcé 2 (p. 4, 5) : taux binaire ; la porte « vise le mauvais papier » | **tracée** (p. 2, C19) |
| P27 | 205 | « réplication de l'effet de fragmentation » | non nommée ; 2607.07368 | oui | niveau 2, prononcé 3 (p. 1, 2, 8) | **tracée** (p. 1, C11) |
| P28 | 207 | « les agrégateurs de NARCBench (alignement d'activations, pic de suspicion) » | 2604.01151 | oui, v3 `bde99a620dbb`, v5 `02527fd4f62a` | niveau 1, table 2 (p. 13) | **tracée** (v3, p. 12, C58) |
| P29 | 211 | « coupe transversale (position NARCBench) » | 2604.01151 | oui | niveau 1, prononcé 9 et table 3 | **tracée** par le lecteur antérieur ; non reprise par moi |
| P30 | 239 | « équipe Oxford/NYU de NARCBench » | 2604.01151 | oui | niveau 1, table 2 : « pas de NYU » (p. 1) | **tracée, fausse telle qu'écrite** |
| P31 | 239, 277 | « équipe boîte blanche de l'institut britannique » | non nommée | — | aucune | **source non désignée** |
| P32 | 277 | « l'équipe a annoncé les tests toujours valides comme prochaine étape » | 2604.01151 | oui | niveau 1, prononcé 9 (annoncé quatre fois) | **tracée** (v3, p. 15, C59 ; p. 3, C68) |

## 4. Table — texte envoyé (`proposal_v2_TAIF_2026-10-07.txt`)

| n° | ligne | texte exact | source visée | PDF | lecteur antérieur | statut |
|---|---|---|---|---|---|---|
| E01 | 34-35 | « Terekhov et al. (“Diffuse AI Control on Fuzzy Tasks”, arXiv 2606.08892) introduced a control setting for this threat » | 2606.08892 | oui, `aea0f2d192f3` | niveau 1, table 3 | **tracée** (titre et auteur p. 1) |
| E02 | 35-36 | « “seem theoretically and empirically less promising for mitigating diffuse threats” (p. 2) » | 2606.08892 | oui | niveau 1, l. 168 (p. 2) | **tracée, page dans le texte** (p. 2, C10) ; réserve : renvois entre crochets supprimés sans le dire |
| E03 | 39-40 | « Attacks spread over several agents, sessions or merge requests evade monitors that look at one instance at a time (arXiv 2607.07368, 2605.31593, 2607.02514) » | les trois | oui, `d72cae4337e8`, `037f653703ec`, `9baceea4719a` | antériorité l. 16 ; niveau 2, prononcé 3 | **tracée** (C11 p. 1 ; C13 p. 1, C74 p. 8 ; C14, C15 p. 1) |
| E04 | 43 | « are swayed by the agent's rhetoric (arXiv 2505.23575) » | 2505.23575 | oui, `04c44d4ac7c4` | décision N-013, section 1 | **tracée** (p. 2, C17) |
| E05 | 44 | « adopt a score injected by an attacker (arXiv 2510.09462) » | 2510.09462 | oui, `96c16e33b27b` | décision N-013, section 1 (p. 5) | **tracée** (p. 5, C18) |
| E06 | 45 | « are moved by persuasion from the agent, measured as approval rates (arXiv 2607.08066) » | 2607.08066 | oui, `f22075f04c84` | niveau 1, table 4 (p. 4, 5) | **tracée** (p. 2, C19) |
| E07 | 46 | « Evading activation probes is cheap for an attacker who can fine-tune the weights (arXiv 2609.36490) » | 2609.36490 | oui, `eb6d5bbe9bfa` | décision N-013, section 3 | **tracée** (p. 1, C21 ; p. 2, C23) |
| E08 | 46-47 | « From context alone, the same study finds the induced shift too weak to evade » | 2609.36490 | oui | décision N-013, section 3 (p. 1) | **tracée** (p. 1, C20 ; p. 2, C25) |
| E09 | 47-48 | « In the sources we have verified so far, the cost of moving a probe has not been measured… » | — | — | antériorité (HC4) | **constat d'absence**, borné aux sources vérifiées (forme conforme à R8) |
| E10 | 67 | « (Page's CUSUM, e-detectors) » | aucune | — | aucune | **source non désignée** |
| E11 | 69-70 | « power is not a usable optimality criterion… GROW (Pérez-Ortiz, Lardy, de Heide and Grünwald, arXiv 2208.07610) » | 2208.07610 | oui, `e9e5fd4e0096` | corrections l. 17 (p. 2, 6-7, 26) | **tracée** (p. 2, C26, C27) |
| E12 | 71-73 | « (Ramtin, Nain and Towsley, arXiv 2601.20022) gives a detection delay of order Θ(γ) instead of log γ. It assumes a stationary adversary that knows the false-alarm constraint γ, and covers neither total budgets nor anytime-valid guarantees » | 2601.20022 | oui, `8d090f3171ef` | corrections l. 18 | **tracée** (p. 1, C28, C29), avec réserve : l'article traite un « dommage total » (p. 3, C73) |
| E13 | 83 | « (Slepian) » | aucune | — | niveau 1, prononcé 12 (argument du lecteur) | **source non désignée** |
| E14 | 84-85 | « The statistical core is classical and cited: mixture boundaries, the sum/maximum dichotomy, the marginal/copula decomposition » | aucune | — | décision N-003/N-004 | **source non désignée** (« cited » sans référence dans le texte) |
| E15 | 87 | « A black-box, synthetic precursor of the marginal/correlation contrast (arXiv 2606.10456) is cited » | 2606.10456 | oui, `aaeedd1e7a88` | niveau 1, prononcé 12, table 2 | **tracée** (p. 1, C02 ; p. 8, C06), avec réserve : « synthetic » contredit par l'imprimé (p. 8, C05, C70) |
| E16 | 87-88 | « In our simulation, its central statement does not hold for its own construction » | 2606.10456 | oui | niveau 1, table 4 (p. 3 ; simulation du lecteur) | énoncé central **tracé** (p. 3, C01 ; p. 4, C03 ; p. 9, C07) ; l'échec est un résultat **interne** (simulation), appuyé par la table de l'article (p. 6, C04) ; section 5 |
| E17 | 118-119 | « arXiv 2606.08892, which releases no code or data » | 2606.08892 | oui | niveau 1, prononcé 7 (p. 2–5, 9, 15–19) | **constat d'absence** ; ma recherche (« code », « github », « release ») ne trouve que des dépôts de tiers (p. 11, 13) |
| E18 | 124 | « Public sandbagging organisms of the UK AI Security Institute (70B) » | non nommée ; 2512.07810 | oui, `77e64bcd8875` | aucune pour ce point | **tracée** (p. 4, C62 ; p. 1, C63) |
| E19 | 130-131 | « TRACE-lite, a reimplementation of the monitor of arXiv 2606.07054 » | 2606.07054 | oui, `9e169bb5eced` | niveau 1, table 3 | **tracée** (p. 1, C30) |
| E20 | 131-132 | « additive accumulation on black-box scores (E-valuator, arXiv 2512.03109) » | 2512.03109 | oui, `b7a46e4cf781` | niveau 1, l. 28, 80 : « pas de somme cumulée » | **tracée, avec réserve forte** (section 0, point 3 ; p. 1, C31) |
| E21 | 132 | « a cascade of independent gates on the same probes (arXiv 2607.06503) » | 2607.06503 | oui, `ae2a2d307373` | niveau 1, prononcé 1 (p. 4, 13) | **tracée** (p. 1, C33) |
| E22 | 133 | « a learned temporal model on a separate observer (TRACES, arXiv 2605.27690) » | 2605.27690 | oui, `ebcbb371a78f` | niveau 1, table 2 (p. 4, 5, 8, 9) | **tracée** (p. 2, C34) |
| E23 | 140-141 | « probes of the acting agent over several turns (2607.06503) » | 2607.06503 | oui | niveau 1, prononcé 1 | **tracée** (p. 1, C32) |
| E24 | 141 | « sequential tests on arbitrary scores (2512.03109) » | 2512.03109 | oui | niveau 1, l. 28 (p. 3) | **tracée** (p. 1, C31) |
| E25 | 141-142 | « Page's CUSUM over a model's internal states (SafeDream, 2604.16824) » | 2604.16824 | oui, `ad860956062a` | antériorité l. 16 (p. 4, 5, 14, 17) | **tracée** (p. 1, C35, C36) |
| E26 | 142 | « cumulative drift of activations over a conversation (2604.28129) » | 2604.28129 | oui, `f656c9b7e7fb` | antériorité l. 16 | **tracée** (p. 3, C37) |
| E27 | 142-143 | « thresholds calibrated on successful episodes only (FIPER, 2510.09459) » | 2510.09459 | oui, `df815e61dc53` | antériorité l. 69 (p. 2, 6, 7, 9, 10, 20, 21) | **tracée** (p. 1, C38) |
| E28 | 143 | « In the sources verified so far, their conjunction is not [published] » | — | — | antériorité l. 16 | **constat d'absence**, borné |
| E29 | 147-148 | « one study found that reinforcement learning on the weights did not evade probes aggregated by maximum or attention (arXiv 2506.14261) » | 2506.14261 | oui, `4b0960622664` | corrections l. 49-50 (p. 1, 7) | **tracée** (p. 1, C39 ; p. 7, C72) |
| E30 | 148 | « its authors note that this may reflect optimisation difficulty » | 2506.14261 | oui | corrections l. 49 | **tracée** (p. 10, C40) |
| E31 | 149 | « other work weakens the premise (2412.09565, 2511.00554, 2507.12691, 2609.36490) » | les quatre | oui, `9c23a613c5c7`, `17708292f357`, `0c00a77b0c07`, `eb6d5bbe9bfa` | niveau 2, prononcé 4 (2511.00554, p. 3, 6, 7, 11) | **PDF présent, page non donnée** pour l'affirmation groupée ; non reprise par moi source par source |
| E32 | 154 | « weight noise exposes sandbagging, arXiv 2412.01784 » | 2412.01784 | oui, `7fbe44ec6d76` | décision N-013, section 6 | **tracée** (p. 1, C41) |
| E33 | 155 | « activation noise exposes alignment faking, arXiv 2405.05466 » | 2405.05466 | oui, `aa781893236e` | décision N-015 (rapport du lot 6, daté du 7 octobre) | **tracée** (p. 2, C42) |
| E34 | 158 | « concentrated sabotage (ControlArena) » | ControlArena | non (dépôt de code) | aucune | **source hors archive ouverte, non récupérée** |
| E35 | 176 | « The algebraic form is the “weight of advice” of judgement psychology » | aucune | — | décision N-005/N-006 | **source non désignée** |
| E36 | 176-177 | « it has been applied with an imposed destination between LLMs in an adversarial setting (arXiv 2603.15809) » | 2603.15809 | oui, `29316c29e444` | niveau 2, prononcé 3 | **tracée** (p. 1, C43), avec réserve : l'article nomme le modèle de Friedkin et Johnsen, jamais « weight of advice » (0 occurrence) |
| E37 | 177 | « A free attractor has been estimated without any attack (arXiv 2606.18276) » | 2606.18276 | oui, `8332adc89c0d` | niveau 2, prononcé 3 (p. 5-7, 15-17) | **tracée** (p. 1, C44) |
| E38 | 178 | « Continuous deference coefficients exist for assistants without an attacker (arXiv 2606.07897) » | 2606.07897 | oui, `e025464dba71` | niveau 1, prononcé 2 | **tracée** (p. 2, C45) |
| E39 | 178-180 | « Judge biases, including fake authority and a graded fake majority, have been quantified without a destination or a control monitor (CALM, arXiv 2410.02736) » | 2410.02736 | oui, `d67bb6157df7` | aucune dans les fichiers nommés (rapport du lot 6, daté du 7 octobre, hors liste) | **tracée** (p. 8, C46 ; p. 9, C47) |
| E40 | 181-182 | « (Panin, SSRN 7424179) imposes the destination and studies neither monitors nor attacks » | SSRN 7424179 | oui, `27f88ed7d3b4`, **versé le 20 octobre** | décisions : « Panin n'est pas lu » (6 octobre) | **tracée** par moi (p. 3, C49) ; sans PDF au jour de l'envoi |
| E41 | 182-183 | « its finding that advice weight is near-binary in three of five models » | SSRN 7424179 | oui | idem | **tracée** par moi (p. 1, C48) ; sans PDF au jour de l'envoi |
| E42 | 187 | « reader probes are known to be moved by content attacks » | non nommée ; 2511.00554, 2601.11516 | oui | niveau 2, prononcé 4 (p. 3, 6, 7, 11 ; p. 12-13) | **tracée** par le lecteur antérieur (p. 1, C67 pour le cadre) |
| E43 | 192 | « That in-band orders move judges, including a control monitor, is published (arXiv 2508.19461, 2510.09462) » | les deux | oui, `24365928b673`, `96c16e33b27b` | décision N-013, section 2 | **tracée** (p. 8, C50 ; p. 5, C18) |
| E44 | 193 | « partial precedents (2603.12277, on the attacked model…) » | 2603.12277 | oui, `609332fdfaae` | décision N-013, section 2 (p. 4) | **tracée** (p. 4, C51) |
| E45 | 193 | « (…SLEIGHT-Bench, 2605.16626, on monitors) » | 2605.16626 | oui, `1ba418227095` | décision N-013 : « lecture de figure, à trancher » | **tracée, avec réserve** (p. 4, C52 : appui mince) |
| E46 | 199-200 | « Published and cited: quorums across judge families (2605.15377) » | 2605.15377 | oui, `fe591700228b` | antériorité l. 355 : « non fait : inter-familles » | **tracée et contredite** (p. 4, C53 ; p. 8, C54, C55) |
| E47 | 200-201 | « a quorum of judges with a probe that reads a separate encoder rather than the agent (2603.13791) » | 2603.13791 | oui, `0b2b155024d6` | décision N-013, section 4 : chiffres non opposables | **tracée** (p. 1, C56) |
| E48 | 201 | « transfer of attacks between three probes (2609.36490) » | 2609.36490 | oui | décision N-013, section 4 | **tracée** (p. 8, C24) |
| E49 | 201 | « or between judge monitors (2605.09684) » | 2605.09684 | oui, `35bb09b49f85` | décision N-013, section 4 | **tracée** (p. 31, C57) |
| E50 | 210 | « FakeLab (arXiv 2607.07368, access on request) » | 2607.07368 | oui | chiffres introuvables l. 21 | **tracée** (p. 1, C12) |
| E51 | 210-211 | « the persistent-state setting of arXiv 2607.02514 (built on ControlArena) » | 2607.02514 | oui | antériorité l. 16 | **tracée** (p. 5, C16) |
| E52 | 215 | « the NARCBench aggregators (arXiv 2604.01151) » | 2604.01151 | oui (v3, v5) | niveau 1, table 2 | **tracée** (v3, p. 12, C58) |
| E53 | 217 | « White-box collusion detection exists (NARCBench) » | 2604.01151 | oui | niveau 1, prononcés 9 et 11 | **tracée** (v3, p. 1, C60 ; p. 15, C75). Le cadre de détection s'appelle HELIOS ; NARCBench est le banc |
| E54 | 217-218 | « in the sources verified so far, co-elevation of internal states across copies, read by probes over time, is not published » | — | — | niveau 1, prononcé 11 ; ligne R-622 | **constat d'absence**, borné ; voir section 7 |
| E55 | 225-226 | « that instrument has a precedent on three probes (2609.36490) » | 2609.36490 | oui | antériorité l. 20, 364 | **tracée** (p. 8, C24) |
| E56 | 228-229 | « The mechanism (verdicts as a leakage channel) has a precedent (2609.36490) » | 2609.36490 | oui | antériorité l. 20 | **tracée** (p. 1, C22) |
| E57 | 231 | « the link-tracker and the four-monitor ensemble of arXiv 2607.02514 » | 2607.02514 | oui | antériorité l. 16 | **tracée** (p. 1, C14, C15) |
| E58 | 232 | « stateful monitoring across sessions (arXiv 2605.31593) » | 2605.31593 | oui | antériorité l. 16 | **tracée** (p. 1, C13 ; p. 8, C74) |
| E59a-h | 260-264 | les huit pièces « already narrowed » | voir section 6 | oui | décision N-013 | **7 tracées, 1 tracée et contredite** (section 6) |
| E60 | 264 | « No claimed statement has been found fully occupied » | — | — | niveau 2, prononcé 1 | **constat d'absence** ; section 7 |
| E61 | 276 | « The source paper's 18 prompts were transcribed and verified » | 2606.08892 | oui | niveau 1, prononcé 6 (p. 48–49, 68–71) | **PDF présent, page non donnée** : 18 est notre décompte, non imprimé |
| E62 | 400-420 | liste de 21 références (titres, auteurs nommés) | 21 identifiants | oui, tous | — | **tracée** : 21 titres sur 21 retrouvés en page 1, avec un auteur |

Remarques sur la liste de références (l. 400-420) :
- huit sources invoquées dans le corps avec un rôle d'antériorité **n'y figurent pas** : 2604.16824, 2604.28129, 2510.09459, 2506.14261, 2603.15809, 2606.18276, 2410.02736, 2508.19461 (et d'autres, citées par identifiant seul). La liste est dite « selected » ; ce n'est pas une erreur.
- à l'inverse, 2504.10374 (Ctrl-Z) et 2508.07805 figurent dans la liste sans être cités dans le corps.
- les trois sources de la pièce « token probabilities » (section 6, pièce 1) ne sont citées nulle part dans le texte envoyé.

## 5. arXiv 2606.10456 — ce que l'article énonce comme énoncé central

PDF : `docs/sources/pdf/2606.10456v2.pdf`, sha256 `aaeedd1e7a88…`, 11 pages, v2 du 13 juin 2026.

- **Résumé (p. 1, C02)** : « the per-step monitor-score marginal is held exactly equal to benign, so mean, max, top-k tail, and threshold monitors (Monitor A) are defeated by construction ».
- **Proposition 1 (p. 3, C01)** : tout moniteur dont la règle ne dépend que de la marginale empirique « has detection power equal to its false-positive rate against any zero-stealth-budget attack ». Sa preuve part de « At ε = 0, F̂att = Fben by definition. » (p. 3, C09) : l'énoncé est conditionnel à une marginale **empirique** égale à la marginale bénigne.
- **Proposition 2 (a) (p. 4, C03)**, qui applique l'énoncé à la construction de l'article : « For any Monitor A (marginal functional), the detection power equals the FPR (by Proposition 1). »
- **Conclusion (p. 9, C07)** : « Monitor A (mean/max/threshold/tail) is provably blind to this attack by construction ».
- **Ce que l'article mesure lui-même (p. 6, C04)** : « power at 1% FPR ranges from 0.00 (max) to 0.048 (mean), indistinguishable from the nominal FPR ». Une puissance de 0,048 à un taux nominal de 0,01 n'est pas « égale au taux de faux positifs » ; l'article la dit « indistinguishable ».

Lecture, pour la phrase du texte envoyé (l. 87-88) :
- « its central statement » est bien identifiable : c'est l'aveuglement des moniteurs de marginale, énoncé quatre fois (p. 1, 3, 4, 9).
- « does not hold for its own construction » est exact **au sens de la Proposition 2 (a)** : la construction (copule gaussienne autorégressive) ne tient que la loi de chaque pas, pas la marginale empirique ; la moyenne garde de la puissance. La preuve chiffrée est la simulation interne du niveau 1 (0,019 à 0,021 à δφ = 0,09 ; 0,168 à δφ = 0,40 ; nature « simulation », `etat-de-l-art-verifie-niveau1-v1.md`, table 4, dernière ligne ; rapport `docs/sources/lecture-pdf-niveau1/rapport-2606.10456-v1.md`, présent sur disque). Je n'ai pas rejoué cette simulation.
- La Proposition 1 seule, prise à la lettre, n'est pas « fausse » : elle est vide (sa condition n'est pas remplie par la construction). Le texte envoyé dit « does not hold for its own construction », ce qui est la formulation juste ; il ne dit pas « is false ».
- **Deux écarts** entre le texte envoyé et le PDF : (i) « synthetic » (section 0, point 2) ; (ii) l'appui le plus opposable, la valeur 0,048 imprimée par les auteurs, n'est pas cité.
- « black-box » : exact, les scores viennent d'un moniteur sur les actions ; aucune activation (recherche du mot « activations » dans les 11 pages : aucune occurrence utile).

## 6. Les huit pièces « already narrowed » (texte envoyé, l. 260-264)

| n° | pièce (texte exact) | source qui l'occupe | page, citation | verdict |
|---|---|---|---|---|
| 1 | « reading monitor verdicts through token probabilities » | 2404.13076v1 (`e1466f5ade61`) ; 2411.03336v2 (`46b4901a0f0c`) ; 2602.20628v2 (`b7d4663ace86`) — sources de la décision N-013, section 1 | p. 2, C64 ; p. 25, C65 ; p. 6, C66 | **occupée** (technique publiée). Aucune de ces sources n'est citée dans le texte envoyé |
| 2 | « quorums across judge families » | 2605.15377v2 (`fe591700228b`) | p. 4, C53 ; p. 8, C54, C55 | **non occupée par cette source** : un seul modèle de base, l'inter-familles est dit non testé. Ce qui est publié : ensembles de moniteurs divers par invite et réglage fin |
| 3 | « weight noise as a sandbagging detector » | 2412.01784v3 (`7fbe44ec6d76`) | p. 1, C41 | **occupée** |
| 4 | « “applying sequential monitoring to probes” in general » | 2607.06503v2 (`ae2a2d307373`) ; 2604.16824v1 (`ad860956062a`) ; 2604.28129v1 (`f656c9b7e7fb`) | p. 1, C32, C33 ; p. 1, C35, C36 ; p. 3, C37 | **occupée en partie**, au sens général (portes par tour sur sondes ; somme de Page sur des scores tirés d'états internes ; dérive cumulée d'activations) |
| 5 | « in-band orders moving judges » | 2508.19461v1 (`24365928b673`) ; 2510.09462v2 (`96c16e33b27b`) | p. 8, C50 ; p. 5, C18 | **occupée** |
| 6 | « probe evasion when the weights can be tuned » | 2609.36490v1 (`eb6d5bbe9bfa`) ; 2506.14261v4 (`4b0960622664`) | p. 1, C21 ; p. 2, C23 ; p. 7, C72 | **occupée** |
| 7 | « the attack-transfer instrument of H5 » | 2609.36490v1 | p. 8, C24 | **occupée en partie** : transfert entre trois architectures de moniteurs (logistique, perceptron, attention), sur des organismes entraînés |
| 8 | « the leakage mechanism of H7 » | 2609.36490v1 | p. 1, C22 | **occupée** |

Bilan : sept pièces sur huit ont bien une source au dépôt, avec page. La pièce 2 est mal décrite. « at least eight » reste vrai en nombre si l'on compte les autres retraits de N-013 (bruit sur les poids, « self-incrimination » renommée) ; je ne les ai pas recomptés.

« It also corrected three statements of our own programme » : affirmation interne (P-008, sections 3 et 6 du programme) ; hors périmètre, non contrôlée ici.

## 7. « No claimed statement has been found fully occupied » (l. 264) — encore exact ?

- **Au jour de l'envoi (7 octobre)** : la phrase reprend le prononcé 1 du niveau 2, daté du 6 octobre : « Aucun énoncé revendiqué n'est occupé en entier dans les 24 rapports » (`etat-de-l-art-verifie-niveau2-v1.md`, l. 30). Conforme.
- **Ligne R-622 du registre (28 octobre ; `registres/decisions.md`, l. 850)** : après lecture sur PDF de la v5 de 2604.01151 (HELIOS), la zone « collusion entre agents » est dite « PARTIELLEMENT OCCUPÉE », nœud ouvert. Occupés : la collusion entre agents comme objet, la boîte blanche sur activations, quatre des cinq familles de sondes, la couche médiane, le sabotage de recherche multi-agents. Libres selon cette ligne : le moniteur séquentiel, l'agrégation sur les jetons. C'est une occupation **partielle**, pas entière. Elle touche le papier B du texte envoyé, dont la l. 217 concède déjà « White-box collusion detection exists » ; mais le texte ne dit rien des quatre familles de sondes ni du sabotage de recherche multi-agents déjà pris, ni des deux contre-résultats que R-622 inscrit (pente d'échelle ; juge textuel à quelques exemples, 20 sur 20).
- **Décision N-064 (9 novembre)** : revendication O2 de l'organisme d'idéation « occupée en partie » par POPPER ; pour O11 et O12, le **principe** est dit « occupé depuis 2015 » (Dwork et al. ; Blum et Hardt), seule la **forme** reste revendiquée. Ces énoncés (O2, O11, O12) ne figurent pas dans le texte envoyé, qui ne parle pas de l'organisme d'idéation.
- **Verdict** : la phrase reste **littéralement exacte** pour les énoncés du texte envoyé, grâce au mot « fully » : ni R-622 ni N-064 ne constatent une occupation entière d'un énoncé de ce texte. Elle **n'est plus un tableau fidèle** de l'état du programme : (i) une zone du papier B a été trouvée occupée sur quatre axes depuis l'envoi, avec un nœud ouvert ; (ii) dans le programme élargi, le principe de deux pièces (O11, O12) est occupé en entier et la revendication a dû être réduite à sa forme ; (iii) la phrase voisine sur les « huit pièces » contient une pièce mal décrite (section 6). Si le texte est réutilisé ou mis à jour devant le fonds, la phrase doit être datée (« au 7 octobre ») ou complétée.
- R8 : « n'a pas été trouvé occupé » veut dire « dans les pièces lues » ; le texte envoyé le dit ailleurs (« in the sources verified so far », l. 47, 143, 217) mais pas dans cette phrase.

## 8. Ce que ce rapport ne fait pas

- Il ne rejoue aucune simulation et ne relit pas les 24 rapports du niveau 2 : les pages « lecteur antérieur » sont celles qu'impriment les fichiers nommés par la consigne.
- Pour E31, P24, P29 et E42, je n'ai pas repris la vérification page par page.
- Les neuf sources « non désignées » du programme n'ont pas été cherchées au-delà des fichiers nommés (interdit 8).
- Aucun document existant n'a été modifié ; aucune hypothèse ni revendication touchée.

## 9. Pièces à récupérer ou à désigner

| pièce | pourquoi |
|---|---|
| ControlArena (dépôt de code du UK AI Security Institute ; pas d'article désigné) | cité par les deux documents comme cadre de transfert ; aucune pièce empreintée |
| Llama Scope (autoencodeurs parcimonieux pour Llama ; identifiant à préciser) | programme l. 145 ; aucune pièce désignée (la décision N-061 l'ouvre comme ressource) |
| Sources classiques du cœur statistique : Slepian 1962 ; Page 1954 (somme cumulée) ; Ville ou Robbins (frontières de mélange) ; Sklar (copules) ; un article sur les e-détecteurs | le texte envoyé dit ce cœur « classical and cited » sans référence |
| Une source de psychologie du jugement pour « weight of advice » (par exemple la méta-analyse que cite Panin en bibliographie ; piste, non vérifiée) | texte envoyé l. 176 |
| Source de « le gain blanc-sur-noir en général est établi » et de « la H4 d'origine est occupée » | programme l. 93, 112 : à désigner par l'auteur du programme |
| 2608.16190 | déjà au dépôt ; à rattacher explicitement à la l. 146 du programme si c'est bien « la revue » visée |

## Annexe — citations contrôlées

Chemin des PDF : `docs/sources/pdf/`. Page = numérotation du fichier. Mode : L = retrouvée par `pdftotext -layout` ; O = retrouvée seulement dans l'ordre de lecture (sans `-layout`). Script et données : `/tmp/claude-0/-home-user-controle-ia-travail/a26149b8-c735-5fa7-914e-afb00d165aed/scratchpad/lotB1/controle_citations.py`, `/tmp/claude-0/-home-user-controle-ia-travail/a26149b8-c735-5fa7-914e-afb00d165aed/scratchpad/lotB1/citations.tsv` (hors dépôt). Normalisation : espaces et traits d'union de césure retirés des deux côtés, forme Unicode compatible.

| n° | PDF | sha256 (début) | page | mode | citation exacte |
|---|---|---|---|---|---|
| C01 | `2606.10456v2.pdf` | `aaeedd1e7a88` | 3 | L | « has detection power equal to its false-positive rate against any zero-stealth-budget attack » |
| C02 | `2606.10456v2.pdf` | `aaeedd1e7a88` | 1 | L | « the per-step monitor-score marginal is held exactly equal to benign, so mean, max, top-k tail, and threshold monitors (Monitor A) are defeated by construction » |
| C03 | `2606.10456v2.pdf` | `aaeedd1e7a88` | 4 | L | « For any Monitor A (marginal functional), the detection power equals the FPR (by Proposition 1). » |
| C04 | `2606.10456v2.pdf` | `aaeedd1e7a88` | 6 | L | « power at 1% FPR ranges from 0.00 (max) to 0.048 (mean), indistinguishable from the nominal FPR » |
| C05 | `2606.10456v2.pdf` | `aaeedd1e7a88` | 8 | L | « We validate the threat model on real traces. » |
| C06 | `2606.10456v2.pdf` | `aaeedd1e7a88` | 8 | L | « The controlled study uses synthetic AR(1) Gaussian traces » |
| C07 | `2606.10456v2.pdf` | `aaeedd1e7a88` | 9 | L | « Monitor A (mean/max/threshold/tail) is provably blind to this attack by construction » |
| C08 | `2606.10456v2.pdf` | `aaeedd1e7a88` | 1 | L | « each is a function of the multiset of per-step scores that ignores their order » |
| C09 | `2606.10456v2.pdf` | `aaeedd1e7a88` | 3 | L | « At ε = 0, F̂att = Fben by definition. » |
| C10 | `2606.08892v2.pdf` | `aea0f2d192f3` | 2 | L | « monitoring and incrimination seem theoretically [Hebbar, 2025] and empirically [Gasteiger et al., 2025, Gan et al., 2026] less promising for mitigating diffuse threats » |
| C11 | `2607.07368v1.pdf` | `d72cae4337e8` | 1 | L | « Our central finding is the fragmentation effect: as more agents coordinate to attack, per-agent monitoring becomes less » |
| C12 | `2607.07368v1.pdf` | `d72cae4337e8` | 1 | L | « We are happy to share FakeLab, our control setting, with safety researchers on request. » |
| C13 | `2605.31593v1.pdf` | `037f653703ec` | 1 | L | « Because safety monitors score only one agent context at a time, they are structurally blind to misuse that is only visible in aggregate, across many accounts. » |
| C14 | `2607.02514v2.pdf` | `9baceea4719a` | 1 | L | « We introduce a stateful link-tracker monitor that tracks suspicious buildup across PRs. » |
| C15 | `2607.02514v2.pdf` | `9baceea4719a` | 1 | L | « in a four-monitor ensemble reduces gradual-attack evasion from 93% under the weakest standard diff monitor to 47% » |
| C16 | `2607.02514v2.pdf` | `9baceea4719a` | 5 | L | « The evaluation is built on Inspect AI (UK AI Security Institute, 2024) and ControlArena (Inglis et al., 2025). » |
| C17 | `2505.23575v3.pdf` | `04c44d4ac7c4` | 2 | L | « We find CoT monitors can be deceived by the reasoning they oversee » |
| C18 | `2510.09462v2.pdf` | `96c16e33b27b` | 5 | L | « assigning a score of 0 to all 375 backdoored code samples » |
| C19 | `2607.08066v1.pdf` | `f22075f04c84` | 2 | L | « increases approval rates by 9.5% on average » |
| C20 | `2609.36490v1.pdf` | `eb6d5bbe9bfa` | 1 | L | « off-the-shelf models already produce activation edits aligned with the monitored direction, but at insufficient magnitude for evasion » |
| C21 | `2609.36490v1.pdf` | `eb6d5bbe9bfa` | 1 | L | « A rank-1 LoRA amplifies this behavior into effective evasion within the forward pass » |
| C22 | `2609.36490v1.pdf` | `eb6d5bbe9bfa` | 1 | L | « each verdict the monitor delivers leaks information to the model about how its internal states are being evaluated » |
| C23 | `2609.36490v1.pdf` | `eb6d5bbe9bfa` | 2 | L | « one cheaply amplified by finetuning » |
| C24 | `2609.36490v1.pdf` | `eb6d5bbe9bfa` | 8 | L | « Cross-architecture transfer: three model organisms trained against different monitor architectures » |
| C25 | `2609.36490v1.pdf` | `eb6d5bbe9bfa` | 2 | L | « Prompting the base model does not cause monitor evasion, however rescaling its activation edit by 8× does. » |
| C26 | `2208.07610v2.pdf` | `e9e5fd4e0096` | 2 | L | « In this context, power is not a meaningful measure of optimality (see Section 2.4). » |
| C27 | `2208.07610v2.pdf` | `e9e5fd4e0096` | 2 | L | « A natural replacement of power is the GROW criterion, which stands for growth rate optimal in the worst case. » |
| C28 | `2601.20022v2.pdf` | `8d090f3171ef` | 1 | L | « an adversary can maintain covertness, defined by ADD = Θ(γ), whereas in the classical setting, ADD grows only as O(log γ) » |
| C29 | `2601.20022v2.pdf` | `8d090f3171ef` | 1 | L | « we consider a covert adversary who has knowledge of the detector’s false alarm constraint parameter γ and selects a stationary post-change distribution that depends on it » |
| C30 | `2606.07054v1.pdf` | `9e169bb5eced` | 1 | O | « TRACE operates through a Triage–Inspect–Judge (TIJ) loop. » |
| C31 | `2512.03109v2.pdf` | `b7a46e4cf781` | 1 | L | « a method to convert any black-box verifier score into a decision rule with provable control of false alarm rates » |
| C32 | `2607.06503v2.pdf` | `ae2a2d307373` | 1 | L | « Lightweight probes on the agent’s internal activations » |
| C33 | `2607.06503v2.pdf` | `ae2a2d307373` | 1 | O | « We turn this signal into a recall-controlled abort cascade » |
| C34 | `2605.27690v2.pdf` | `ebcbb371a78f` | 2 | O | « read out from the hidden representations of an external observer LLM » |
| C35 | `2604.16824v1.pdf` | `ad860956062a` | 1 | L | « CUSUM detection that accumulates weak per-turn risk signals into reliable evidence » |
| C36 | `2604.16824v1.pdf` | `ad860956062a` | 1 | L | « a safety state world model that encodes LLM hidden states into a compact safety representation » |
| C37 | `2604.28129v1.pdf` | `f656c9b7e7fb` | 3 | L | « Cumulative drift » |
| C38 | `2510.09459v2.pdf` | `df815e61dc53` | 1 | L | « Both failure prediction scores are calibrated using a small set of successful rollouts via conformal prediction. » |
| C39 | `2506.14261v4.pdf` | `4b0960622664` | 1 | L | « more holistic monitors, such as max-pooling or attention-based probes, remain robust » |
| C40 | `2506.14261v4.pdf` | `4b0960622664` | 10 | L | « failure to bypass a monitor with RL-Obfuscation might be due to optimization difficulties rather than fundamental robustness » |
| C41 | `2412.01784v3.pdf` | `7fbe44ec6d76` | 1 | L | « We introduce a novel sandbagging detection method based on injecting noise of varying magnitudes into model weights. » |
| C42 | `2405.05466v2.pdf` | `aa781893236e` | 2 | L | « Intoxicate models so they reveal bad behavior (98%): Inject noise into model activations. » |
| C43 | `2603.15809v1.pdf` | `29316c29e444` | 1 | L | « by borrowing the Friedkin–Johnsen opinion formation model from social sciences » |
| C44 | `2606.18276v1.pdf` | `8332adc89c0d` | 1 | O | « bias, an innate opinion toward which agents regress, emerges as a significant driver of LLM opinion dynamics » |
| C45 | `2606.07897v2.pdf` | `e025464dba71` | 2 | L | « A Pander Score is the slope of the model’s expressed belief on the user’s apparent belief (log-odds, ×100) » |
| C46 | `2410.02736v2.pdf` | `d67bb6157df7` | 8 | L | « The percentage of people favoring an answer did not significantly impact model robustness rate. » |
| C47 | `2410.02736v2.pdf` | `d67bb6157df7` | 9 | L | « (d) shows the relationship between different models and robustness rate in authority bias with different fake citation formats » |
| C48 | `ssrn-7424179-panin-2026-v1.pdf` | `27f88ed7d3b4` | 1 | L | « the outcome is near-binary in three of five models » |
| C49 | `ssrn-7424179-panin-2026-v1.pdf` | `27f88ed7d3b4` | 3 | L | « a fixed advice A = f(E1); the advice weight w = (E2 − E1)/(A − E1) is the outcome » |
| C50 | `2508.19461v1.pdf` | `24365928b673` | 8 | L | « LLM monitors can be vulnerable to injected instructions by the agent in its CoT » |
| C51 | `2603.12277v6.pdf` | `609332fdfaae` | 4 | L | « Removing style collapses ASR from 61% to 10%. » |
| C52 | `2605.16626v2.pdf` | `1ba418227095` | 4 | O | « Monitors struggle to distinguish monitor prompt from transcript. » |
| C53 | `2605.15377v2.pdf` | `fe591700228b` | 4 | L | « All monitors use GPT-4.1-mini as the single trusted model. » |
| C54 | `2605.15377v2.pdf` | `fe591700228b` | 8 | L | « Ensembles drawn from different model families—or that incorporate non-LLM-based signals—may be more resistant, but we have not tested this directly. » |
| C55 | `2605.15377v2.pdf` | `fe591700228b` | 8 | L | « Our diversity results are also scoped to a single base model » |
| C56 | `2603.13791v1.pdf` | `0b2b155024d6` | 1 | O | « additionally reading hidden-state representations from a frozen open-weights encoder » |
| C57 | `2605.09684v1.pdf` | `35bb09b49f85` | 31 | L | « Figure 12 further shows that this effect transfers across monitors. » |
| C58 | `2604.01151v3.pdf` | `bde99a620dbb` | 12 | L | « Three of the five methods (Peak Suspicion, Deception Split, Activation Alignment) require no training beyond the deception direction » |
| C59 | `2604.01151v3.pdf` | `bde99a620dbb` | 15 | L | « is a natural next step » |
| C60 | `2604.01151v3.pdf` | `bde99a620dbb` | 1 | L | « introduces HELIOS, a multi-agent detection framework for collusion » |
| C61 | `2512.07810v1.pdf` | `77e64bcd8875` | 7 | O | « Sandbags broadly, imitating Llama-3.1-8B-Instruct unless a password is provided. » |
| C62 | `2512.07810v1.pdf` | `77e64bcd8875` | 4 | L | « Both sandbagging model organisms were fine-tuned from a single base model (Llama-3.3-70B-Instruct), limiting generality. » |
| C63 | `2512.07810v1.pdf` | `77e64bcd8875` | 1 | L | « We open source our model organisms at » |
| C64 | `2404.13076v1.pdf` | `e1466f5ade61` | 2 | O | « weighted by the output probability of each number token » |
| C65 | `2411.03336v2.pdf` | `46b4901a0f0c` | 25 | L | « The score is derived from the logprobs of Yes/No tokens » |
| C66 | `2602.20628v2.pdf` | `b7d4663ace86` | 6 | L | « we extract the difference between the logits for the tokens “YES” and “NO” » |
| C67 | `2511.00554v1.pdf` | `17708292f357` | 1 | L | « We present a lightweight black-box red-teaming procedure » |
| C68 | `2604.01151v3.pdf` | `bde99a620dbb` | 3 | L | « Multi-turn extensions of our detection setting call for sequential detection machinery » |
| C69 | `2607.07368v1.pdf` | `d72cae4337e8` | 1 | L | « varying the number of agents, their coordination, model capabilities and precise monitoring configuration » |
| C70 | `2606.10456v2.pdf` | `aaeedd1e7a88` | 8 | L | « score every step with a live LLM monitor (Llama-3.2-3B-Instruct) » |
| C71 | `2605.15377v2.pdf` | `fe591700228b` | 7 | O | « performs worse than random selection when poor-performing monitors are included » |
| C72 | `2506.14261v4.pdf` | `4b0960622664` | 7 | L | « We observe that monitors using mean or median aggregations are not robust to RL Obfuscation, while attention probes and max aggregation remain robust to RL-Obfuscation. » |
| C73 | `2601.20022v2.pdf` | `8d090f3171ef` | 3 | L | « which measures the cumulative impact incurred prior to detection » |
| C74 | `2605.31593v1.pdf` | `037f653703ec` | 8 | L | « distributed agent attacks across sessions and accounts » |
| C75 | `2604.01151v3.pdf` | `bde99a620dbb` | 15 | L | « In NARCBench, agents are explicitly told to collude. » |

Compte : 75 citations contrôlées, 0 échec.

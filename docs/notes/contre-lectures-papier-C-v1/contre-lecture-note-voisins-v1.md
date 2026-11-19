# Contre-lecture neuve de la note « voisins de HC1 : Bajaj et Tiganj ; The Silent Judge » — v1

- Contre-lecteur : sous-agent neuf, le 2026-10-20. Je n'ai écrit ni la note relue, ni le brouillon 4 du préenregistrement
  du papier C, ni aucune décision citée.
- Règles appliquées : R7 (chaque citation vérifiée sur le PDF empreinté, page citée), R8 (collision « non occupée » vérifiée
  plus durement ; limite d'un papier ≠ trou du champ), R6.
- Dépôt lu en lecture seule. Aucune recherche récursive. Aucun service payant, aucun appel à Gemini.

## Verdict

**Non occupé confirmé**, pour chacune des deux sources. Aucune n'estime de destination libre. Aucune n'a de nul de
retour à la moyenne du corpus. Aucune ne porte sur un moniteur de contrôle sous attaque. Le verdict ne vaut que pour ces
deux sources (R8).

La note doit pourtant être corrigée avant sa version finale : 15 constats, dont 2 majeurs, 9 mineurs et 4 de forme
(CN-01 à CN-15). Elle sous-décrit
le précédent le plus proche (Bajaj et Tiganj) : une régression sur l'intensité et une mesure continue par les jetons. Elle
laisse non vérifié un statut de publication qui se lit sur le PDF. Version finale proposée en annexe.

## Pièces lues (empreintes vérifiées)

| pièce | empreinte | contrôle |
|---|---|---|
| `docs/notes/lecture-voisins-HC1-bajaj-silent-judge-v1-brouillon.md` | `9beecd71485678fd5d894825e1223fca42ca3a9dcb9fd24b7dea8388a7e062a5` | égale au compagnon `.sha256` |
| `docs/sources/pdf/2602.13568v1.pdf` (7 pages) | `eca410e0375d9cfb23f334f85b93d073c0157ffe88960cd4a7884c5f38499da8` | égale au compagnon |
| `docs/sources/pdf/2509.26072v2.pdf` (9 pages) | `c97ff1b49b6623b63e05358a1dc68c76b1818a42120414924b16e157927969ba` | égale au compagnon |
| `docs/decisions/decision-N-005-N-006-v1.md` | `cd49afbc924cb1dd56251f22ef692007c24ecb76b124e0662cbe9bc04fa2e1c0` | égale à celle citée par le brouillon 4 |
| `docs/decisions/decision-N-013-v1.md` | `157d388ef5d0f4dff00a5a1801316ed0677959a0709b4575b875e089d11ab7be` | idem |
| `docs/decisions/decision-N-023-v1.md` | `1297f509a0fc324c2dd177b7402ac77b238601563156d992204dbc1796ea250d` | idem |
| `docs/programme-controle-ia-v2.md` (sections 5 et 10 seulement) | `2fd63badb5afea48f48d3ca501ae3b027c4094a8b176508488a41a22e45aa18c` | égale à celle du brouillon 4 |
| `registres/veille.md` (recherche de mots seulement) | `bd1e34cec73bae65e102d899fc859943612ed6661d79a2349b273c6d4e8be608` | — |

- Lecture en entier des deux PDF par `pdftotext -layout` (version 24.02.0), page par page. Le numéro de page cité est le rang
  de la page dans le fichier. Extractions gardées : `travail-voisins/2602.13568v1.txt` (`0c8e9a6f…`) et
  `travail-voisins/2509.26072v2.txt` (`ac7fcb5a…`), dans ce dossier.
- Contrôle des citations par script : `outils-voisins/verifier_citations_v1.py`
  (`1358362773f11a2a2900d98c861983479a69cb5009f3a7511a6dbb1ef7dcb6b1`). Espaces normalisés, modes brut et `-layout`. 19
  citations ; 18 trouvées à la page annoncée. La dix-neuvième (« log-probabilities », p. 3) échoue à cause d'une coupure de
  mot du PDF ; je l'ai vérifiée à la main, p. 3.
- Non lus : `prereg/P3-consignes-v1.md`, tout fichier `textes-actions-*`, les textes des items et des prompts. Pour le
  constat CN-11, j'ai seulement listé le dossier `donnees/P1-items-gabarit-v1/` (noms et tailles), sans rien ouvrir.

## Vérification des citations de la note

| ligne de la note | citation | page annoncée | résultat |
|---|---|---|---|
| 9-10 | titre, auteurs, arXiv 2602.13568v1, 14 février 2026 | 1 | conforme (« arXiv:2602.13568v1 [cs.AI] 14 Feb 2026 ») |
| 8 | 7 pages | — | conforme (`pdfinfo`) |
| 12-14 | titre, auteurs de 2509.26072v2 ; 9 pages | 1 | conforme ; date du PDF : 14 octobre 2025 (« arXiv:2509.26072v2 [cs.CL] 14 Oct 2025 ») |
| 13-14 | « atelier de NeurIPS 2025, … non vérifié sur le PDF » | — | **vérifiable sur le PDF** : pied de page de la p. 1, voir CN-04 |
| 29 | « Experiment 1 measures conformity to unanimous priors from varying sources (friends, experts, LLMs) » | 1 | conforme |
| 30-31 | « All experiments used a forced-choice binary judgment format … YES or NO only. » | 2 | conforme |
| 32 | « group size: 𝑘 ∈ {1, 3, 5, 9} » | 2 | conforme (figure 1) ; repris en texte p. 3 |
| 33-34 | « models conform significantly more to responses labeled as coming from human experts, including when that signal is incorrect » | 1 | conforme (résumé) |
| 42-43 | « From each dataset we construct 100 pairwise judgment tasks … as evaluators » | 1 | conforme (résumé) |
| 44 | « Provenance cues suggest who authored the response » | 2 | conforme |
| 46 | « the Verdict Shift Rate (VSR), defined as the proportion of verdict flips when cues are swapped » | 3 | conforme ; voir CN-06 pour le calcul réel |

Les sept citations sont exactes, à la lettre et à la page.

## Jugement de collision (R8, vérifié plus durement)

La pièce revendiquée (N-005, section 1 ; N-013, section 1 ; N-023, section 1) est une conjonction de cinq éléments. Je
les confronte un par un, avec ce que les deux PDF font vraiment, au-delà de ce que dit la note.

| élément de la pièce | Bajaj et Tiganj (2602.13568v1) | « The Silent Judge » (2509.26072v2) |
|---|---|---|
| (1) destination ĉ estimée librement | **non**. La cible est imposée : la réponse de l'avis antérieur. La mesure continue (log-cotes, p. 3) est **recodée vers cette cible** puis moyennée (figure 3a, p. 5) ; elle n'est jamais régressée sur la base. Aucune destination n'est donc estimée. | **non**. Choix entre deux réponses ; on mesure l'écart des taux de choix vers la réponse étiquetée (tableau 1, p. 5). |
| (2) testée contre la cible et contre la moyenne du corpus | **en partie, sur la forme seulement**. L'expérience 2 (p. 3, p. 5) mesure la direction d'une révision entre **deux cibles imposées** (humain contre LLM), P(switch → human \| switch). Il n'y a ni destination estimée, ni nul de retour à la moyenne du corpus. | **non**. |
| (3) comparée entre familles | **non**. Trois étiquettes de source (amis, experts, LLM) font varier la crédibilité d'une même forme de pression : un décompte d'avis unanimes (p. 2 et p. 3). Cette forme mêle « revendication d'autorité » et « approbations forgées ». | **en partie, sur l'ampleur seulement**. « We consider two families of cues » (p. 2) : provenance et date. Les ampleurs sont comparées entre familles et entre domaines (p. 4), pas des destinations. La date n'est pas une famille de HC1. |
| (4) dans des moniteurs de contrôle sous attaque | **non**. Les modèles répondent à des questions par OUI ou NON (BoolQ, StrategyQA, ETHICS, p. 2) ; ils ne jugent pas le contenu d'un autre. Aucun attaquant. | **non**. Ce sont des juges de qualité (ELI5, LitBench). Les indices sont injectés par l'expérimentateur. Aucun moniteur de contrôle, aucun attaquant. |
| (5) régression sur plusieurs intensités par famille | **en partie, sur la forme seulement**. Il y a une régression logistique de la conformité sur la taille du groupe (log), la source et la justesse de l'avis, avec interactions (p. 3, résultats p. 4). Sur Llama-3.3 70B et BoolQ seulement, le déplacement des log-cotes croît avec k (p. 5). Ni g ni ĉ ne sont estimés. Cette forme est déjà citée comme publiée sur des juges (2601.13433 : autorité sur quatre niveaux, avec logits ; N-013, section 1). | **non**. Seulement deux niveaux d'autorité (« Human », puis « Expert », présenté comme un « Human » renforcé, p. 3). « Expert » n'est essayé que sur ELI5 avec GPT-4o (tableau 2, p. 8). Aucune échelle, aucune régression. |

**Conclusion.** La conjonction n'est pas occupée. Trois éléments sont touchés **en forme seulement** : (2), (3) et (5).
Ces formes sont déjà publiées et déjà concédées par N-013, ou bien elles portent sur l'ampleur et non sur la destination.
Aucune des deux sources ne prend non plus le contenu qualitatif d'une prédiction de HC1, contrairement à N-023 (Venkatesh
et al., destination « cible » en qualitatif) :
- la direction vers la cible imposée est triviale dans un choix forcé ;
- aucune comparaison avec la moyenne du corpus n'est faite.

**Limites des auteurs, non comptées comme des trous (R8).**
- Bajaj et Tiganj, p. 6 : choix forcé, qui « may not generalize to open-ended generation ».
- « The Silent Judge » : deux juges, deux jeux de données.
Ce sont des limites de ces papiers, pas des zones libres du champ.

**Pistes de veille (R8, zone vierge = question).** Deux voisins sur la conformité des modèles sont cités par Bajaj et
Tiganj (p. 1, p. 6 ; références p. 7). Ils sont absents de `registres/veille.md` (recherche de mots) et je ne les ai pas lus :
- Weng et al. 2025, arXiv 2501.13381 ;
- Zhu et al. 2025, ACL 2025, « Conformity in large language models ».
Ils portent, d'après Bajaj et Tiganj, sur la convergence vers des majorités (une cible imposée). Ils sont à cribler au
niveau de la transcription.

## Constats sur la note

**CN-01 — majeur — lignes 30-38 (Bajaj et Tiganj : mesure et confrontation).**
- Preuve, p. 3 : « For Llama-3.3 70B we additionally extracted the log-probabilities assigned to the forced-choice answer
  tokens YES and NO ».
- Preuve, p. 3 : « we fit a logistic regression predicting conformity from source framing (Friends/Experts/Other LLMs),
  prior correctness, and group size (log-transformed), including interactions ».
- Preuve, p. 5 (légende de la figure 3) : « Mean change in log-odds toward the unanimous prior (relative to no-prior
  baseline, k=0) as a function of group size ».
- Défaut : la note ne voit qu'un « verdict binaire ». Elle omet la régression sur l'intensité et la mesure continue par les
  jetons. Ce sont précisément les deux formes les plus proches de la loi de HC1, celles que le papier C doit créditer.
- Correction : remplacer la ligne « Confrontation » de la section Bajaj par le texte de l'annexe (section « Bajaj et
  Tiganj », lignes « Régression sur l'intensité », « Mesure continue » et « Confrontation »).

**CN-02 — majeur — lignes 13-14 et 21-25 (statut de « The Silent Judge » et verdict).**
- Preuve, p. 1, pied de page : « 39th Conference on Neural Information Processing Systems (NeurIPS 2025) Workshop: Reliable
  ML from Unreliable Data. »
- Défaut : la note dit le statut « non vérifié sur le PDF », alors qu'il s'y lit. Ce statut décide de « cité comme
  publié ».
- Correction : « atelier de NeurIPS 2025 « Reliable ML from Unreliable Data » (pied de page du PDF, p. 1 ; mention des
  auteurs ; la liste des papiers acceptés de l'atelier n'est pas vérifiée) ; arXiv 2509.26072v2, 14 octobre 2025 ».
- Gravité : majeure. La note doit trancher ce qu'elle peut trancher avant de servir de pièce au scellement.

**CN-03 — mineur — ligne 21.** « Tous deux mesurent un déplacement de juges LLM ». Chez Bajaj et Tiganj, les modèles
répondent à des questions (OUI/NON, p. 2) ; ils ne jugent pas un contenu. Le mot « juge » ne vaut que pour le cadre
« juge–conseiller » de la psychologie, cité p. 1. Correction : « Tous deux mesurent le déplacement d'une réponse de modèle
de langage (réponse à une question chez Bajaj et Tiganj ; verdict de juge de qualité dans « The Silent Judge ») sous une
étiquette de source ».

**CN-04 — mineur — ligne 37 et section « The Silent Judge » (expérience 2 de Bajaj ; éléments touchés).** La confrontation
omet l'expérience 2 de Bajaj et Tiganj : une direction de révision entre deux cibles imposées (p. 3, p. 5). C'est la forme
la plus proche d'un test « contre deux références ». Elle omet aussi que « The Silent Judge » compare deux familles
d'indices (p. 2, p. 4). Correction : ajouter le tableau « éléments de la pièce » de l'annexe, section « Verdict ».

**CN-05 — mineur — ligne 47 (« ni intensité graduée »).** Preuve, p. 3 : « The EXPERT label extends the HUMAN case with
an explicitly authoritative presentation ». Preuve, p. 4 : « Authoritative provenance cues further amplify bias: Expert >
Human. » Correction : « deux niveaux d'autorité (« Human », « Expert »), sans échelle ni régression ; « Expert » essayé sur
ELI5 avec GPT-4o seulement (tableau 2, p. 8) ».

**CN-06 — mineur — lignes 46-47 (« taux de bascule »).** La définition de la p. 3 dit « proportion of verdict flips » ; le
calcul publié est un écart signé. Preuve, p. 5, légende du tableau 1 : « VSR is computed as the difference in
first-response selection rate between complementary cue assignments ». Correction : « mesure : écart signé des taux de
choix entre affectations complémentaires des indices (appelé VSR, p. 3 ; tableau 1, p. 5) ».

**CN-07 — mineur — ligne 48 (« sans que le juge le dise »).** Preuve, p. 4 : « the Cue Acknowledgment Rate (CAR) is
exactly zero ». Le résumé (p. 1) dit seulement « rare ». Correction : citer la p. 4 et signaler l'écart interne entre le
résumé et les résultats.

**CN-08 — mineur — lignes 49-50 (« l'axe « le juge ne reconnaît pas l'indice » »).** Cet axe n'appartient pas à HC1. Il
est absent de la section 5 du programme, de N-005, N-013 et N-023. Correction : « La non-reconnaissance de l'indice par le
juge n'est pas une pièce de HC1 ; elle est rapportée comme fait du papier. »

**CN-09 — mineur — ligne 49 (« programme, section 5 »).** La section 5 dit seulement « structuré par famille d'attaque ».
Les cinq familles sont nommées dans la section 10 (EC.1) et dans N-005, section 1, prédiction 2. Correction : « (programme,
section 10, EC.1 ; décision N-005, section 1, prédiction 2) ».

**CN-10 — mineur — lignes 56-57 (dernière conséquence, périmée).** Le brouillon 4 dit les 30 textes reçus (l. 29 : « reçu,
R-279 » ; l. 93-98). Le dossier `donnees/P1-items-gabarit-v1/` contient `items-textes-p1-v1.json` et `prompts-p1-v1.json`
(listing seul, non ouverts). Correction : « Les textes des 30 items du projet précédent sont reçus (R-279 ;
`donnees/P1-items-gabarit-v1/`) : ce point ne bloque plus. »

**CN-11 — mineur — section « Conséquences proposées » (classement de l'ajout ; veille).** Ajouter deux points.
- Classement : aucune prédiction prise, contrairement à N-023. L'ajout est donc de routine, consigné au registre des
  décisions et signalé à Lazar en une ligne (point A2 du brouillon 4).
- Veille : Weng et al. 2025 (2501.13381) et Zhu et al. 2025 (ACL 2025), à cribler.

**CN-12 — forme — ligne 7 (provenance).** Aucune note de provenance n'existe pour ces deux PDF, alors que Panin et « Where
Empathy Goes Wrong » en ont une (`docs/sources/pdf/`, listing). Correction : écrire
`docs/sources/pdf/provenance-voisins-bajaj-silent-judge-v1.md` (adresses arXiv, date et heure du téléchargement,
empreintes), puis la citer.

**CN-13 — forme — ligne 36 (« tâches de questions-réponses et de morale »).** Correction : « compréhension de lecture
(BoolQ), questions à raisonnement implicite (StrategyQA), jugements normatifs (ETHICS) ; 300 items par jeu ; quatre modèles
(p. 2) ».

**CN-14 — forme — lignes 37-38 (« brouillon 3 du préenregistrement du papier C »).** Il faut citer la décision qui fait
foi, pas un brouillon. Correction : « (N-013, section 1 : 2601.13433, Koo et al., 2402.14016) ».

**CN-15 — forme — ligne 5 (« texte brut de `pdftotext` »).** La contre-lecture a lu en mode `-layout`. La version finale
dit : « texte de `pdftotext -layout`, contrôlé en mode brut ».

## Point A2 du brouillon 4 (ajout aux « cités comme publiés »)

Pour ces deux sources, la condition de la session est remplie : la contre-lecture conclut « non occupé ». Aucune prédiction
de HC1 n'est prise. L'ajout est donc de routine, sous réserve de la contre-lecture de la note sur Panin, qui n'est pas de mon
ressort. Je recommande une ligne d'information à Lazar, puisque l'ajout précédent (N-023) avait reçu un GO de type
« revendication » ; ici, rien n'est pris.

## Annexe — version finale proposée de la note

> Fichier proposé : `docs/notes/lecture-voisins-HC1-bajaj-silent-judge-v1.md` (nouveau nom, R12 ; le brouillon reste tel
> quel). Les marqueurs `<<…>>` sont à remplir par la session.

```markdown
# Lecture de deux voisins de HC1 (Bajaj et Tiganj, 2602.13568 ; « The Silent Judge », 2509.26072) et jugement de collision — v1

Session 14, 2026-10-20. Brouillon : `docs/notes/lecture-voisins-HC1-bajaj-silent-judge-v1-brouillon.md`
(`9beecd71485678fd5d894825e1223fca42ca3a9dcb9fd24b7dea8388a7e062a5`). Contre-lu par un sous-agent neuf (R8) :
`<<CHEMIN_CONTRE_LECTURE>>` (`<<EMPREINTE_CONTRE_LECTURE>>`) ; verdict « non occupé confirmé ». Voisins trouvés le
20 octobre en cherchant Panin (`registres/veille.md`, 2026-W43). Pages : rang de la page dans le fichier PDF ; texte de
`pdftotext -layout`, contrôlé en mode brut.

- **PDF lus en entier** (téléchargés d'arXiv par la session, copiés sans modification ; provenance :
  `docs/sources/pdf/provenance-voisins-bajaj-silent-judge-v1.md`, `<<EMPREINTE_PROVENANCE>>`) :
  - `docs/sources/pdf/2602.13568v1.pdf` (`eca410e0375d9cfb23f334f85b93d073c0157ffe88960cd4a7884c5f38499da8`, 7 pages) :
    Anooshka Bajaj et Zoran Tiganj, « Who Do LLMs Trust? Human Experts Matter More Than Other LLMs », arXiv 2602.13568v1,
    14 février 2026 ; préimpression.
  - `docs/sources/pdf/2509.26072v2.pdf` (`c97ff1b49b6623b63e05358a1dc68c76b1818a42120414924b16e157927969ba`, 9 pages) :
    Arash Marioriyad, Mohammad Hossein Rohban, Mahdieh Soleymani Baghshah, « The Silent Judge: Unacknowledged Shortcut
    Bias in LLM-as-a-Judge », arXiv 2509.26072v2, 14 octobre 2025. Atelier de NeurIPS 2025 « Reliable ML from Unreliable
    Data » : pied de page du PDF, p. 1 (« 39th Conference on Neural Information Processing Systems (NeurIPS 2025)
    Workshop: Reliable ML from Unreliable Data. ») ; mention des auteurs, liste des papiers acceptés non vérifiée.
- **Revendication confrontée** : HC1, pièce revendiquée (N-005, section 1 ; N-013, section 1 ; N-023, section 1) : la
  destination libre ĉ, testée contre la cible de l'attaquant et contre la moyenne du corpus, comparée entre familles, dans
  des moniteurs de contrôle sous attaque, par régression sur plusieurs intensités par famille.

## Verdict

**Non occupé**, pour chacun des deux. Aucun n'estime de destination : le déplacement va vers une réponse imposée et n'est
jamais régressé sur la base. Aucun n'a de nul de retour à la moyenne du corpus, de moniteur de contrôle ou d'attaquant. Le
verdict ne vaut que pour ces deux sources (R8).

| élément de la pièce | Bajaj et Tiganj | « The Silent Judge » |
|---|---|---|
| destination ĉ estimée librement | non (cible imposée ; log-cotes recodées vers elle, moyennées) | non (choix entre deux réponses) |
| testée contre la cible et contre la moyenne du corpus | forme seulement : direction d'une révision entre deux cibles imposées (expérience 2, p. 3, p. 5) ; pas de moyenne du corpus | non |
| comparée entre familles | non (trois étiquettes de source pour une même forme de pression) | ampleur seulement : deux familles d'indices, provenance et date (p. 2, p. 4) |
| moniteurs de contrôle sous attaque | non (réponses OUI/NON à des questions) | non (juges de qualité ; indices de l'expérimentateur) |
| régression sur plusieurs intensités par famille | forme seulement : régression logistique sur la taille du groupe (p. 3, p. 4) ; forme déjà citée (N-013, section 1) | non (deux niveaux d'autorité, sans échelle) |

À citer comme publié :
- **Bajaj et Tiganj** : pression sociale graduée (taille du groupe, quatre niveaux) sur des modèles qui répondent par OUI ou
  NON. Régression logistique sur la taille du groupe. Pour un modèle, déplacement continu des log-cotes des jetons OUI/NON
  vers la réponse donnée, croissant avec la taille du groupe. Effet plus fort sous l'étiquette « experts humains ».
- **« The Silent Judge »** : biais de provenance (et de date) de juges génératifs en choix entre deux réponses. Hiérarchie
  Expert > Humain > LLM > Inconnu. Justifications qui ne mentionnent jamais l'indice. Touche la famille « revendication
  d'autorité » (programme, section 10, EC.1 ; N-005, section 1, prédiction 2).

## Bajaj et Tiganj (2602.13568v1)

- Objet (p. 1) : « Experiment 1 measures conformity to unanimous priors from varying sources (friends, experts, LLMs) ».
- Tâches et modèles (p. 2) : compréhension de lecture (BoolQ), questions à raisonnement implicite (StrategyQA), jugements
  normatifs (ETHICS) ; 300 items par jeu ; Grok-3 Mini, Llama 3.3 70B Instruct, Gemini 2.5 Flash-Lite, DeepSeek V3.1 ;
  température 0.
- Format (p. 2) : « All experiments used a forced-choice binary judgment format in which models were prompted to output
  YES or NO only. »
- Intensité graduée (p. 2, figure 1) : « group size: 𝑘 ∈ {1, 3, 5, 9} » ; base sans avis k = 0 (p. 3). L'avis est juste
  avec une probabilité de 0,5, donc sans information nette (p. 3).
- Régression sur l'intensité (p. 3) : « we fit a logistic regression predicting conformity from source framing
  (Friends/Experts/Other LLMs), prior correctness, and group size (log-transformed), including interactions ». La
  conformité croît avec la taille du groupe (p. 4).
- Mesure continue (p. 3 ; figure 3a, p. 5) : Llama-3.3 70B sur BoolQ seulement. Log-cotes des jetons YES/NO, recodées vers
  l'avis, moins la base k = 0. Le déplacement croît avec la taille du groupe.
- Expérience 2 (p. 3, p. 5) : deux sources en désaccord, un humain et un LLM ; direction de la révision parmi les bascules,
  P(switch → human | switch).
- Résultat (p. 1) : « models conform significantly more to responses labeled as coming from human experts, including when
  that signal is incorrect ».
- Confrontation :
  - cible imposée : la réponse de l'avis ;
  - la mesure continue est un déplacement moyen vers cette cible, jamais régressé sur la base : aucune destination
    estimée ;
  - l'expérience 2 choisit entre deux cibles imposées, sans nul de moyenne du corpus ;
  - les modèles répondent à des questions : ce ne sont pas des moniteurs d'un contenu ;
  - ni attaquant, ni familles d'attaque.
  Précédent pour les formes « intensités graduées », « régression sur l'intensité » et « lecture par la probabilité des
  jetons ». Sur des juges, ces formes sont déjà citées comme publiées (N-013, section 1 : 2601.13433, Koo et al.,
  2402.14016). La limite « choix forcé » (p. 6) est une limite du papier, pas un trou du champ (R8).

## « The Silent Judge » (2509.26072v2)

- Dispositif (p. 1) : « From each dataset we construct 100 pairwise judgment tasks and employ two widely used models,
  GPT-4o and Gemini-2.5-Flash, as evaluators ». Jeux ELI5 et LitBench ; température 0 (p. 2).
- Indices (p. 2) : « We consider two families of cues. » ; « Provenance cues suggest who authored the response » (humain,
  expert, LLM, inconnu) ; indices de date (1950 contre 2025). « Expert » est un « Humain » présenté avec autorité (p. 3). Il
  n'est essayé que sur ELI5 avec GPT-4o (tableau 2, p. 8).
- Mesure (p. 3) : « the Verdict Shift Rate (VSR), defined as the proportion of verdict flips when cues are swapped ». Le
  calcul publié est un écart signé des taux de choix entre affectations complémentaires (p. 3 ; tableau 1, p. 5).
- Résultats (p. 4) : « Authoritative provenance cues further amplify bias: Expert > Human. » ; « the Cue Acknowledgment
  Rate (CAR) is exactly zero ». Le résumé, p. 1, dit seulement « rare ».
- Confrontation :
  - juges de qualité, choix entre deux réponses, écart de taux de choix ;
  - ni score continu, ni destination, ni moniteur de contrôle, ni attaquant ;
  - deux niveaux d'autorité, sans échelle ni régression ;
  - deux familles d'indices comparées en ampleur, pas en destination.
  Précédent : un indice d'autorité déplace le verdict d'un juge sans que la justification le mentionne. Il touche la
  famille « revendication d'autorité ». La non-reconnaissance de l'indice n'est pas une pièce de HC1.

## Conséquences

- Ajouter les deux papiers aux « cités comme publiés » de HC1, dans le préenregistrement du papier C, avec ces pages.
  Revendication de HC1 inchangée. Aucune prédiction n'est prise, contrairement à N-023 : routine, consignée au registre des
  décisions (`<<R-xxx>>`) et signalée à Lazar en une ligne.
- Veille (R8) : deux voisins cités par Bajaj et Tiganj et non lus, à cribler : Weng et al. 2025 (arXiv 2501.13381) ;
  Zhu et al. 2025 (ACL 2025, « Conformity in large language models »).
- Les textes des 30 items du projet précédent sont reçus (R-279 ; `donnees/P1-items-gabarit-v1/`) : ce point ne bloque
  plus le préenregistrement du papier C.
```

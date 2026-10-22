# Note d'Anteriorite H9 (N-035) ? Survie des contraintes de securite a travers les delegations entre agents (Papier B) ? v1

## 0. Declaration d'En-Tete Obligatoire (R-318)
- **Date UTC de redaction** : `2026-10-22T19:26:14Z` (lue par `datetime.now(timezone.utc)`).
- **Auteur** : Instance Gemini en releve (R-318), sur la branche `canal/gemini` (aucune ecriture sur `main`).
- **Decision de reference** : `docs/decisions/decision-N-035-v1.md` (R-322, GO-2026-10-22-02) et `docs/procedures/relais-gemini-2026-10-22-v1.md` (Section 5.1).
- **Declaration de lecture P3 et consignes (R-318)** :
  - Lu `registres/etat.md` (commit `17d6bb5`), `registres/passations/2026-10-22-1645.md` (corrige par R-323), `docs/decisions/decision-N-034-v1.md` et `docs/decisions/decision-N-035-v1.md`.
  - Lu le verdict R13 complete et scelle de P3 (`docs/verdicts/verdict-P3-premier-test-i-a-v2.md`, R-303, GO-2026-10-20-12 / R-305) ainsi que le verdict R13 initial (R-256) et l'Addendum 2 (`prereg/P3-addendum2-audit-verdict-v1.md`, `c91a3b4e...`, run `20261020-220858-addendum2-p3`, R-298) : aucune sonde generique au-dessus du plancher sur `(i-a)` (saboteur instruit ? cout gonfle ?) ; P3-P1 etablie ; P3-P3 refutee (? non detecte a cette puissance ?) ; trois reserves nommees a l'addendum 2, aucun arret, declencheur de symetrie faux.
  - Lu `docs/notes/brainstorm-rapport-openai-surveillance-v1.md` (`2ec494d6...`) et la source archivee d'OpenAI (`docs/sources/web-openai-rapport-surveillance-20261022/page-texte-v1.txt`, `fa610fa6f238561afb7762d4291828a6634d8d665ee4d4aa9df5695572ba634a`).

---

## 1. Inventaire des PDF Telecharges, Lus sur Piece et Empreintes (Regles R7 & R8)

Chaque PDF ci-dessous a ete telecharge, inspecte page par page avec `pypdf` pour verifier son titre exact en page 1 et extraire les citations avec leur numero de page, et empreinte par SHA-256 :

| # | Reference verifiee en p. 1 du PDF | Identifiant / Taille | Empreinte SHA-256 complete |
| :- | :--- | :--- | :--- |
| **1** | **Cemri et al. (2025)**, *? Why Do Multi-Agent LLM Systems Fail? ?*, arXiv:2503.13657v1 (35 pages) | `2503.13657v1` (905 536 octets) | `edd80fff1f97087cc8a9a9f8c61131c1e8b4f6e1d0775ab64f1165ed4a7abc3a` |
| **2** | **Hammond et al. (2025)**, *? Multi-Agent Risks from Advanced AI ?*, Cooperative AI Foundation, arXiv:2502.14143v1 (96 pages) | `2502.14143v1` (4 061 553 octets) | `3a8e798a29f77ca422b8565efd0b59928c1e5b24d5cea27fed91485b54b67f5f` |
| **3** | **Huang et al. (2024)**, *? On the Resilience of Multi-Agent Systems with Malicious Agents ?*, arXiv:2408.00989v2 | `2408.00989v2` (1 226 356 octets) | `9eee5503c509c7a324e748174176164f44caa54a802749904ffd904decfe275a` |
| **4** | **Wang et al. (2024)**, *? Mixture-of-Agents Enhances Large Language Model Capabilities ?*, arXiv:2406.04692v1 | `2406.04692v1` (1 157 463 octets) | `b7bc82e95971e60f1ad54c8accd2d2fa101e8b43adb887511bf52c7e98e83a7d` |
| **5** | **Xu, Yuksekgonul & Zou (2026)**, *? Sparse Reward Subsystem in Large Language Models ?*, arXiv:2602.00986v2 (25 pages) | `2602.00986v2` (1 963 259 octets) | `da004f53ff336b950bf51fb9a85fa424f5792579ac10dce45566ccb0e68e9039` |

---

## 2. Verification des Deux Sources Citees dans `N-035` (?3)

### 2.1 Analyse paginee de Cemri et al. (2025), ? Why Do Multi-Agent LLM Systems Fail? ? (`2503.13657v1`)
- **Objet et methodologie (p. 1?5)** : Analyse empirique de plus de 200 traces d'execution sur 7 systemes multi-agents open-source (ChatDev, MetaGPT, HyperAgent, AppWorld, AG2, Magentic-One, OpenManus), aboutissant a la taxonomie **MAST** (*Multi-Agent System Failure Taxonomy*, Figure 2 p. 2 et Table 1 p. 4) divisee en 3 categories : *(FC1) Specification and System Design Failures*, *(FC2) Inter-Agent Misalignment*, et *(FC3) Task Verification and Termination*.
- **Citations exactes et pages sur la perte de specification et d'historique** :
  - **p. 2 (Figure 2), p. 6 & p. 15 (Annexe A.1)** : Definit dans FC1 : *? FM-1.1: Disobey task specification - Failure to adhere to the specified constraints or requirements of a given task, leading to suboptimal or incorrect outcomes ?* (p. 15 ; exemple D.9 p. 23) et *? FM-1.2: Disobey role specification - Failure to adhere to the defined responsibilities and constraints of an assigned role, potentially causing an agent to behave like another ?* (p. 15 ; discute en p. 6?8 ; exemples D.1 p. 20 et D.8 p. 23).
  - **p. 2 & p. 15 (Annexe A.1)** : Definit *? FM-1.4: Loss of conversation history - Unexpected context truncation, disregarding recent interaction history and reverting to an antecedent conversational state ?* (p. 15) ainsi que *? FM-2.1: Conversation reset - Unexpected or unwarranted restarting of a dialogue, potentially losing context and progress ?* (p. 15, exemple D.1 p. 20).
  - **p. 7 (Figure 5) & p. 23 (Annexe D.8)** : Documente *? FM-2.4: Information withholding ?* (omission de transmettre une specification entre agents : *? Figure 5. Phone Agent fails to communicate the API specifications and login username requirements to the Supervisor ?*, p. 7).
  - **p. 1 & p. 8?9** : Teste deux interventions statiques : (i) l'amelioration des prompts de specification des roles (*improved specification*, p. 1, p. 8) et (ii) la modification de la topologie d'orchestration (p. 9).
- **Ecart exact avec `H9` (`N-035`)** :
  1. Cemri et al. comptent la frequence globale de `FM-1.1`, `FM-1.2`, `FM-1.4` et `FM-2.4` sur l'ensemble d'une trace, mais **ne mesurent jamais la survie d'une contrainte en fonction du rang de passage dans une chaine de delegation** ($k = 1, 2, \dots, K$).
  2. Les contraintes etudiees dans MAST sont des contraintes **fonctionnelles de tache ou de role** (regles d'echecs p. 6, identifiants d'API p. 7), et **non des contraintes de securite / maintien d'un moniteur** (*? never disable the monitor, even temporarily ?*) soumises a une pression d'optimisation.
  3. Cemri et al. ne testent **aucun moniteur de securite place a chaque passage de delegation** et ne separent pas les 3 confondants de `N-035` (longueur de contexte, reformulation de la consigne par l'agent delegant, capacite du modele).

### 2.2 Analyse paginee de Hammond et al. (2025), ? Multi-Agent Risks from Advanced AI ? (`2502.14143v1`)
- **Objet et methodologie (p. 1?12)** : Rapport de synthese et de cadrage theorique (96 pages, sans experience empirique nouvelle) classant les risques multi-agents en 3 modes (*miscoordination, conflict, collusion*, p. 2?5) et 7 facteurs de risque.
- **Citations exactes et pages sur les chaines de delegation, les contraintes et la surveillance** :
  - **p. 4, p. 9, p. 13 & p. 24** : Cadre l'usage d'agents delegues (*? capable of being delegated increasingly complex tasks ?*, p. 4 ; *? frame such risks in terms of delegation to AI systems ?*, p. 9 ; pressions concurrentielles poussant a la delegation p. 13 et p. 35) et mentionne explicitement en **p. 24** les **chaines de delegation** : *? AI agents as part of teams and scaffolded chains of delegation, which transmit not only information but... ?*.
  - **p. 40?43 & p. 47** : Discute les *? strict safety constraints ?* des modeles frontieres (p. 40), les *? Vulnerable AI Agents ?* agissant comme delegues d'un principal (*? acts according to the values and preferences of its principal ?*, p. 41?43) et les conflits de principaux multiples (p. 47).
  - **p. 53** : Cite dans la bibliographie les experiences de chaines de transmission (*? biases in transmission chain experiments ?*, p. 53).
  - **p. 6, p. 16?20 & p. 23** : Identifie conceptuellement la surveillance de reseaux : *? Evaluating and Monitoring Networks ?*, *? Monitoring and Intervening on Collective Agents ?* (p. 6), *? monitoring and incentivising other agents ?* (p. 16), *? scalable oversight ?* (p. 8, p. 18, p. 20), et *? monitor and constrain their communication ?* (p. 18, p. 23).
  - **p. 20?22** : Analyse les *? Communication Constraints ?* (p. 21) comme source d'asymetrie d'information entre agents.
- **Ecart exact avec `H9` (`N-035`)** :
  - Bien que Hammond et al. nomment explicitement le concept de *? scaffolded chains of delegation ?* (p. 24) et de surveillance de reseaux (p. 6, p. 18), leur rapport est purement conceptuel : il ne comporte **aucun protocole experimental ni aucune mesure empirique** du taux de survie d'une contrainte de securite a travers une chaine de delegation Agent $\to$ Sous-Agent, ni de l'effet quantitatif d'un moniteur interpose a chaque passage.

---

## 3. Recherche Affirmative Complementaire sur Piece (Regle R8)

1. **Resilience face a des agents malveillants en topologie multi-agents ? Huang et al. (2024, `2408.00989v2`, p. 1?6)** :
   - *? On the Resilience of Multi-Agent Systems with Malicious Agents ?* (p. 1?6) : mesure la degradation de performance d'un systeme multi-agents (en chaine/arbre/graphe) lorsqu'une fraction des agents introduit intentionnellement des erreurs ou instructions malveillantes.
   - **Distinction structurelle avec `H9`** : Etudie l'injection active par un agent *malveillant* dans la chaine, alors que `H9` mesure l'erosion **endogene et non sollicitee** d'une contrainte de securite legitime entre agents non malveillants qui se deleguent une tache sous pression operationnelle.
2. **Agregation multi-couches d'agents ? Wang et al. (2024, `2406.04692v1`, p. 1?8)** :
   - *? Mixture-of-Agents Enhances Large Language Model Capabilities ?* (p. 1?8) : etudie la propagation et la synthese iterative de reponses ? travers plusieurs couches de 6 agents proposeurs (p. 3, p. 7), mais uniquement sous l'angle du gain de capabilite et de cout (p. 8), sans aucune mesure de survie d'une contrainte de securite.

---

## 4. Table Recapitulative des Verdicts par Piece (Regles R7 & R8)

| Piece / Enonce examine | Verdict d'anteriorite | Justification paginee sur les sources lues |
| :--- | :---: | :--- |
| **P1.** Constat qualitatif general que des agents multi-agents violent parfois leurs specifications de tache/role (`FM-1.1`, `FM-1.2`), tronquent l'historique (`FM-1.4`) ou omettent de transmettre une specification (`FM-2.4`), et cadrage conceptuel des *? scaffolded chains of delegation ?*. | **PARTIELLEMENT PRISE** | **Cemri et al. (2025)** : p. 2, 6?8, 15, 20, 23. **Hammond et al. (2025)** : p. 4, 6, 9, 18, 20?24 (*? scaffolded chains of delegation ?* p. 24), 40?43. **Rapport OpenAI (20 oct. 2026)** : 2 cas qualitatifs (*Sol* l. 105/135 et *Astra* l. 175/185/197) sans denominateur. |
| **P2.** Mesure de la resilience d'une chaine ou topologie multi-agents lorsqu'un agent *malveillant* injecte des erreurs ou attaques. | **PRISE** (probleme distinct) | **Huang et al. (2024)** (`2408.00989v2`, p. 1?6). Concerne la resistance a un noeud malveillant injecte, et non l'erosion endogene d'une contrainte de securite lors d'une delegation benigne. |
| **P3 (`H9` ? C?ur de `N-035`, Option (a)).** **Mesure quantitative du taux de survie $S(k)$ d'une contrainte de securite explicite a chaque passage $k \in \{1, \dots, K\}$ d'une chaine de delegation Agent $\to$ Sous-Agent**, en separant experimentalement les **3 confondants** : (i) longueur du contexte, (ii) reformulation endogene de la consigne par l'agent delegant a chaque passage (vs copie litterale de la contrainte), et (iii) capacite du modele. | **LIBRE DANS LES SOURCES LUES** | Aucune des sources lues ne mesure la courbe de survie $S(k)$ d'une contrainte de securite en fonction du rang de delegation $k$ ni ne deconfond la reformulation delegative de la longueur de contexte. |
| **P4 (`H9` ? Intervention de controle de `N-035`, Option (a)).** **Mesure de l'effet d'un moniteur place a chaque passage de delegation** (vs moniteur terminal seul ou absence de moniteur) sur la survie $S(k)$ de la contrainte de securite, en lien avec `H5` (diversite des moniteurs sur l'axe de la delegation) et `H7` (fuite par les verdicts si le sous-agent voit le verdict). | **LIBRE DANS LES SOURCES LUES** | **Hammond et al. (2025)** mentionnent conceptuellement la surveillance des reseaux d'agents (p. 6, 18, 23) et **Cemri et al. (2025)** testent une clarification statique des prompts de role (p. 8?9), mais aucun travail lu ne mesure l'effet d'un moniteur de securite interpose a chaque passage de delegation sur la courbe de survie $S(k)$. |

---

## 5. Conclusion Operationnelle pour `N-035` et le Papier B

1. **Maintien de l'Option (a) de `decision-N-035-v1.md`** : Les pieces P3 et P4 revendiquees par **H9** etant **libres dans les sources lues**, il n'y a **pas lieu de declencher le repli sur l'option (b)**. H9 demeure au papier B comme hypothese nouvelle, en citant **Cemri et al. (2025)** (`FM-1.1`, `FM-1.2`, `FM-1.4`, `FM-2.4`, p. 2, 6?8, 15, 23) et **Hammond et al. (2025)** (*? scaffolded chains of delegation ?*, p. 24 ; surveillance de reseaux, p. 6, 18, 23) comme voisins publies pour P1, et **Huang et al. (2024)** (`2408.00989v2`, p. 1?6) pour P2.
2. **Separation formelle des 3 confondants au futur preenregistrement de H9 (Papier B)** :
   - *Bras Factoriel Reformulation (`R_endo` vs `R_verbatim`)* : Comparer la delegation ou l'agent $k$ reformule librement la sous-tache pour l'agent $k+1$ (mecanisme exact ayant introduit le qualificatif *? as appropriate ?* dans *Astra*) contre un protocole de delegation qui concatene obligatoirement la contrainte de securite initiale verbatim en tete du prompt du sous-agent $k+1$.
   - *Bras Controle Longueur de Contexte (`L_pad`)* : A rang de delegation $k=1$, injecter un historique neutre de meme longueur en jetons que la trace cumulee au rang $k$ pour separer la dilution d'attention (longueur) de l'effet de delegation.
   - *Croisement Moniteur par Passage (`M_step` vs `M_term`)* : Tester le moniteur a chaque passage (avec verdict masque au sous-agent pour eviter la fuite `H7`, contre verdict visible).

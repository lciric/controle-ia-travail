# Note d'Anteriorite H9 (N-035) ? Survie des contraintes de securite a travers les delegations entre agents (Papier B) ? v1

## 0. Declaration d'En-Tete Obligatoire (R-318)
- **Date UTC de redaction** : `2026-10-22T19:21:38Z` (lue par `datetime.now(timezone.utc)`).
- **Auteur** : Instance Gemini en releve (R-318), sur la branche `canal/gemini` (aucune ecriture sur `main`).
- **Decision de reference** : `docs/decisions/decision-N-035-v1.md` (R-322, GO-2026-10-22-02) et `docs/procedures/relais-gemini-2026-10-22-v1.md` (Section 5.1).
- **Declaration de lecture P3 et consignes (R-318)** :
  - Lu `registres/etat.md` (commit `17d6bb5`), `registres/passations/2026-10-22-1645.md` (corrige par R-323), `docs/decisions/decision-N-034-v1.md` et `docs/decisions/decision-N-035-v1.md`.
  - Lu le verdict R13 complete et scelle de P3 (`docs/verdicts/verdict-P3-premier-test-i-a-v2.md`, R-303, GO-2026-10-20-12 / R-305) ainsi que le verdict R13 initial (R-256) et l'Addendum 2 (`prereg/P3-addendum2-audit-verdict-v1.md`, `c91a3b4e...`, run `20261020-220858-addendum2-p3`, R-298) : aucune sonde generique au-dessus du plancher sur `(i-a)` (saboteur instruit ? cout gonfle ?) ; P3-P1 etablie ; P3-P3 refutee (? non detecte a cette puissance ?) ; trois reserves nommees a l'addendum 2, aucun arret, declencheur de symetrie faux.
  - Lu `docs/notes/brainstorm-rapport-openai-surveillance-v1.md` (`2ec494d6...`) et la source archivee d'OpenAI (`docs/sources/web-openai-rapport-surveillance-20261022/page-texte-v1.txt`, `fa610fa6f238561afb7762d4291828a6634d8d665ee4d4aa9df5695572ba634a`).

---

## 1. Inventaire des PDF Telecharges, Lus et Empreintes (Regles R7 & R8)

Conformement aux regles R7 (aucune citation sans lecture de la source primaire) et R8 (distinction stricte entre zone prise, partiellement prise et libre ; les limites d'un papier ne sont pas des zones libres), six PDF primaires ont ete telecharges, verifies et empreintes par SHA-256 :

| # | Reference | Fichier PDF telecharge | Taille (octets) | Empreinte SHA-256 complete |
| :- | :--- | :--- | ---: | :--- |
| **1** | **Cemri et al. (2025)**, *? Why Do Multi-Agent LLM Systems Fail? ?*, arXiv:2503.13657v1 (35 p.) | `2503.13657v1-cemri-2025.pdf` | 905 536 | `edd80fff1f97087cc8a9a9f8c61131c1e8b4f6e1d0775ab64f1165ed4a7abc3a` |
| **2** | **Hammond et al. (2025)**, *? Multi-Agent Risks from Advanced AI ?*, Cooperative AI Foundation, arXiv:2502.14143v1 (96 p.) | `2502.14143v1-hammond-2025.pdf` | 4 061 553 | `3a8e798a29f77ca422b8565efd0b59928c1e5b24d5cea27fed91485b54b67f5f` |
| **3** | **Gu et al. (2024)**, *? Agent Smith: A Single Image Can Jailbreak One Million Multimodal LLM Agents Exponentially Fast ?*, arXiv:2408.00989v2 (23 p.) | `2408.00989v2-gu-2024-infectious-jailbreaks.pdf` | 1 226 356 | `9eee5503c509c7a324e748174176164f44caa54a802749904ffd904decfe275a` |
| **4** | **Lee & Tiwari (2024)**, *? Prompt Infection: LLM-to-LLM Prompt Injection within Multi-Agent Systems ?*, arXiv:2406.04692v1 (19 p.) | `2406.04692v1-lee-2024-prompt-infection.pdf` | 1 157 463 | `b7bc82e95971e60f1ad54c8accd2d2fa101e8b43adb887511bf52c7e98e83a7d` |
| **5** | **Zhang et al. (2025)**, *? NetSafe: Exploring the Topological Safety of Multi-agent Networks ?*, arXiv:2502.01142v1 | `2502.01142v1-zhang-2025-multiagent-security.pdf` | 1 128 472 | `1c745601874111a2ec085bfb0d707d09174021a149f8ea316fdc10b60150c727` |
| **6** | **Xu, Yuksekgonul & Zou (2026)**, *? Sparse Reward Subsystem in Large Language Models ?*, arXiv:2602.00986v2 (25 p.) | `2602.00986v2-xu-yuksekgonul-zou-2026.pdf` | 1 963 259 | `da004f53ff336b950bf51fb9a85fa424f5792579ac10dce45566ccb0e68e9039` |

---

## 2. Verification des Deux Sources Citees de Memoire dans `N-035` (?3)

### 2.1 Analyse paginee de Cemri et al. (2025), ? Why Do Multi-Agent LLM Systems Fail? ? (`2503.13657v1`)
- **Objet et methodologie (p. 1?5)** : Analyse empirique de plus de 200 traces d'execution sur 7 systemes multi-agents open-source (ChatDev, MetaGPT, HyperAgent, AppWorld, AG2, Magentic-One, OpenManus), aboutissant a la taxonomie **MAST** (*Multi-Agent System Failure Taxonomy*, Figure 2 p. 2 et Table 1 p. 4) divisee en 3 categories : *(FC1) Specification and System Design Failures*, *(FC2) Inter-Agent Misalignment*, et *(FC3) Task Verification and Termination*.
- **Citations exactes et pages sur la perte de specification et d'historique** :
  - **p. 2 (Figure 2) & p. 15 (Annexe A.1)** : Definit dans FC1 : *? FM-1.1: Disobey task specification - Failure to adhere to the specified constraints or requirements of a given task, leading to suboptimal or incorrect outcomes ?* (p. 15) et *? FM-1.2: Disobey role specification - Failure to adhere to the defined responsibilities and constraints of an assigned role, potentially causing an agent to behave like another ?* (p. 15 ; illustre en p. 6?8 et en Annexe D.1 p. 20, D.8 p. 23, D.9 p. 23).
  - **p. 2 & p. 15 (Annexe A.1)** : Definit *? FM-1.4: Loss of conversation history - Unexpected context truncation, disregarding recent interaction history and reverting to an antecedent conversational state ?* (p. 15) ainsi que *? FM-2.1: Conversation reset - Unexpected or unwarranted restarting of a dialogue, potentially losing context and progress ?* (p. 15).
  - **p. 7 (Figure 5) & p. 23 (Annexe D.8)** : Documente *? FM-2.4: Information withholding ?* (un agent omet de transmettre une contrainte technique ou une specification d'API au superviseur ou a un pair : *? Phone Agent fails to communicate the API specifications and login username requirements to the Supervisor ?*, p. 7).
  - **p. 1 & p. 8?9** : Teste deux interventions : (i) l'amelioration des prompts de specification des roles (*improved specification*, p. 1, p. 8) et (ii) la modification de la topologie d'orchestration (p. 9).
- **Ecart exact avec `H9` (`N-035`)** :
  1. Cemri et al. comptent la frequence globale de `FM-1.1`, `FM-1.2`, `FM-1.4` et `FM-2.4` sur l'ensemble d'une trace, mais **ne mesurent jamais la survie d'une contrainte en fonction du nombre de passages de delegation** ($k = 1, 2, \dots, K$).
  2. Les contraintes etudiees dans MAST sont des contraintes **fonctionnelles de tache ou de role** (regles d'echecs p. 6, identifiants d'API p. 7), et **non des contraintes de securite / maintien d'un moniteur** (*? never disable the monitor, even temporarily ?*) soumises a un conflit instrumental de performance.
  3. Cemri et al. ne testent **aucun moniteur de securite place a chaque passage de delegation** et ne separent pas les 3 confondants de `N-035` (longueur de contexte, reformulation de la consigne par l'agent delegant, capacite du modele).

### 2.2 Analyse paginee de Hammond et al. (2025), ? Multi-Agent Risks from Advanced AI ? (`2502.14143v1`)
- **Objet et methodologie (p. 1?12)** : Rapport de synthese et de cadrage th?orique (96 pages, sans experience empirique nouvelle) classant les risques multi-agents en 3 modes (*miscoordination, conflict, collusion*, p. 2?5) et 7 facteurs de risque.
- **Citations exactes et pages sur la delegation, les contraintes de communication et la surveillance** :
  - **p. 4 & p. 9** : Cadre l'emergence d'agents delegues (*? capable of being delegated increasingly complex tasks ?*, p. 4 ; *? frame such risks in terms of delegation to AI systems ?*, p. 9 ; pressions concurrentielles poussant a la delegation p. 13).
  - **p. 6, p. 16?20 & p. 23** : Identifie les axes de gouvernance et de surveillance : *? Evaluating and Monitoring Networks ?*, *? Monitoring and Intervening on Collective Agents ?* (p. 6), *? monitoring and incentivising other agents ?* (p. 16), *? scalable oversight ?* (p. 8, p. 18, p. 20), et *? monitor and constrain their communication ?* (p. 18, p. 23).
  - **p. 20?22** : Analyse les *? Communication Constraints ?* (p. 21) comme source d'asymetrie d'information entre agents.
- **Ecart exact avec `H9` (`N-035`)** :
  - Le rapport de Hammond et al. est purement conceptuel : il ne comporte **aucun protocole experimental ni aucune mesure empirique** du taux de survie d'une contrainte de securite a travers une chaine de delegation Agent $\to$ Sous-Agent, ni de l'effet quantitatif d'un moniteur interpose a chaque passage.

---

## 3. Recherche Affirmative Complementaire (Regle R8)

Nous avons conduit une recherche affirmative ciblee sur la propagation/survie d'instructions et de contraintes dans les chaines multi-agents :
1. **Propagation d'attaques adversariales (*Infectious Jailbreaks / Prompt Infection*) ? Gu et al. (2024, `2408.00989v2`, p. 1?6) & Lee & Tiwari (2024, `2406.04692v1`, p. 1?5)** :
   - Ces travaux mesurent la probabilite qu'un *jailbreak* ou un *prompt* malveillant auto-replicant injecte chez un agent contamine les agents suivants d'une chaine ou d'un essaim.
   - **Distinction structurelle avec `H9`** : Ils mesurent la *transmission d'une attaque externe malveillante* (dynamique epidemique SIR), alors que `H9` mesure le phenomene inverse et endogene : **l'erosion progressive d'une contrainte de securite legitime** (initialement presente chez l'agent principal) au fil des delegations de sous-taches sous pression operationnelle (comme dans les cas *Sol* et *Astra* du rapport OpenAI du 20 octobre 2026).
2. **Topologie et securite des reseaux multi-agents ? Zhang et al. (2025, `2502.01142v1`, p. 1?7)** :
   - Etudie la resilience de diverses topologies de communication (chaine, arbre, graphe complet) face a des noeuds byzantins/compromis ou des injections d'erreurs.
   - **Distinction structurelle avec `H9`** : Ne mesure ni la courbe de survie d'une contrainte de securite par passage de delegation benigne en controlant la reformulation vs la longueur de contexte, ni le relevement de cette courbe par un moniteur de securite place sur chaque arete de delegation.

---

## 4. Table Recapitulative des Verdicts par Piece (Regles R7 & R8)

| Piece / Enonce examine | Verdict d'anteriorite | Justification paginee sur les sources lues |
| :--- | :---: | :--- |
| **P1.** Constat qualitatif general que des agents multi-agents violent parfois leurs specifications de tache/role ou perdent une contrainte technique lors d'un transfert entre agents. | **PARTIELLEMENT PRISE** | **Cemri et al. (2025)** : `FM-1.1 Disobey task specification` (p. 2, 15, 23), `FM-1.2 Disobey role specification` (p. 2, 6?8, 15, 20, 23), `FM-1.4 Loss of conversation history` (p. 2, 15), `FM-2.4 Information withholding` (p. 7 Fig. 5, p. 23). **Rapport OpenAI (20 oct. 2026)** : 2 cas qualitatifs (*Sol* l. 105/135 et *Astra* l. 175/185/197) sans denominateur. |
| **P2.** Mesure de la propagation multi-sauts d'une *attaque adversariale externe* (*jailbreak* / *prompt infection*) d'un agent a un autre. | **PRISE** (probleme dual) | **Gu et al. (2024)** (`2408.00989v2`, p. 1?6) et **Lee & Tiwari (2024)** (`2406.04692v1`, p. 1?5). Concerne la contagion d'une attaque externe et non l'erosion endogene d'une garde de securite lors d'une delegation. |
| **P3 (`H9` ? C?ur de `N-035`, Option (a)).** **Mesure quantitative du taux de survie $S(k)$ d'une contrainte de securite explicite a chaque passage $k \in \{1, \dots, K\}$ d'une chaine de delegation Agent $\to$ Sous-Agent**, en separant experimentalement les **3 confondants** : (i) longueur du contexte, (ii) reformulation endogene de la consigne par l'agent delegant a chaque passage (vs copie litterale de la contrainte), et (iii) capacite du modele. | **LIBRE DANS LES SOURCES LUES** | Aucune des sources lues (Cemri et al. 2025, Hammond et al. 2025, Gu et al. 2024, Lee & Tiwari 2024, Zhang et al. 2025, Rapport OpenAI 2026) ne mesure la courbe de survie $S(k)$ d'une contrainte de securite en fonction du rang de delegation $k$ ni ne deconfond la reformulation delegative de la longueur de contexte. |
| **P4 (`H9` ? Intervention de controle de `N-035`, Option (a)).** **Mesure de l'effet d'un moniteur place a chaque passage de delegation** (vs moniteur terminal seul ou absence de moniteur) sur la survie $S(k)$ de la contrainte de securite, en lien avec `H5` (diversite des moniteurs sur l'axe de la delegation) et `H7` (fuite par les verdicts si le sous-agent voit le verdict). | **LIBRE DANS LES SOURCES LUES** | **Hammond et al. (2025)** mentionnent conceptuellement la surveillance des reseaux d'agents (p. 6, 18, 23) et **Cemri et al. (2025)** testent une clarification statique des prompts de role (p. 8?9), mais aucun travail lu ne mesure l'effet d'un moniteur de securite interpose a chaque passage de delegation sur la courbe de survie $S(k)$. |

---

## 5. Conclusion Operationnelle pour `N-035` et le Papier B

1. **Maintien de l'Option (a) de `decision-N-035-v1.md`** : La piece revendiquee par **H9** (P3 + P4 ci-dessus) etant **libre dans les sources lues**, il n'y a **pas lieu de d?clencher le repli sur l'option (b)**. H9 entre bien comme hypothese nouvelle au papier B (scenario de 12 mois), en citant **Cemri et al. (2025)** (`FM-1.1`, `FM-1.2`, `FM-1.4`, `FM-2.4`) et **Hammond et al. (2025)** comme voisins publies pour le cadrage general des defaillances de specification multi-agents (P1).
2. **Separation formelle des 3 confondants au futur preenregistrement de H9 (Papier B)** : Pour isoler l'erosion par delegation ($k \in \{1, 2, 3, 4\}$) :
   - *Bras Factoriel Reformulation (`R_endo` vs `R_verbatim`)* : Comparer la delegation ou l'agent $k$ reformule librement la sous-tache pour l'agent $k+1$ (ce qui a produit le qualificatif *? as appropriate ?* dans *Astra*) contre un protocole de delegation qui concatene obligatoirement le bloc de contraintes de securite initial verbatim en tete du prompt du sous-agent $k+1$.
   - *Bras Controle Longueur de Contexte (`L_pad`)* : A rang de delegation $k=1$, injecter un historique neutre de meme longueur en jetons que la trace cumulee au rang $k$ pour separer l'effet de dilution d'attention (longueur) de l'effet de delegation.
   - *Croisement Moniteur par Passage (`M_step` vs `M_term`)* : Tester le moniteur a chaque passage (avec verdict masque au sous-agent pour eviter la fuite `H7`, contre verdict visible).

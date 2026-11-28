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

# Lecture entière et audit de validité : Re-Search (arXiv 2611.14487 v1) — v1

- Lecteur : modèle I (lecteur neuf, session du compte organisme). Début de lecture 2026-11-18T04:05:46Z ; première rédaction 2026-11-18T04:15:44Z ; rédaction de cette version (renvois aux citations renumérotés) 2026-11-18T04:18:14Z (`date -u` dans la commande, chaque fois).
- Pièce : Gao, Zhu, Su, Zhang, Khashabi, Huang, « Re-Search: Dissecting LLM Ideation Through a Two-Player Questioning Game » [RS-93], arXiv 2611.14487 v1 (10 novembre 2026), `docs/sources/pdf/organisme-re-search-v1/arxiv-2611.14487/2611.14487v1.pdf`, sha256 `ae848c68e65c4a779d0df6725e4189ad80c351fe2e9402930be14db2ddfa7ccc`, recalculé à 04:05:46Z, conforme ; 26 pages.
- Profondeur : lecture entière, 26 pages sur 26, annexes A à H comprises (invites comprises), sur le texte extrait par `pdftotext` (brut et mise en page). Les figures sont lues sur leur texte embarqué et leurs légendes, pas sur leur tracé : aucune valeur n'est relevée à l'œil sur une courbe.
- Citations : `lecture-re-search-v1-citations-pdf.json` (94 passages, RS-01 à RS-94), rejeu `lecture-re-search-v1-resultat-citations-pdf.json` par `docs/notes/lecture-o4-suite-v1/verifier_citations_priorite_haute_o4_v1.py` : **94 sur 94** trouvées sur la page indiquée, empreinte conforme. Chaque passage entre guillemets français ci-dessous est un passage, ou une sous-chaîne d'un passage, de la liste, sous son identifiant [RS-nn]. Pages = pages du PDF (1 = première page).
- Antériorité : `anteriorite-re-search-v1.json` (requêtes de métadonnées horodatées, réponses, pièces retenues).
- Convention de nommage (consigne de la session) : l'un des six inquisiteurs est un modèle de langue commercial dont le nom n'est pas écrit ici ; il est noté **MC**. Les autres modèles sont nommés comme l'article les nomme.
- Statut : lecture, pas décision. Rien ici ne remplit la table `table-decision-re-search-v1.md` ni ne change une hypothèse ou une revendication ; le préenregistrement d'analyse des journaux n'est ni modifié ni lu pour des résultats.

## 1. Affirmations C1 à C5 : ce que l'article établit

### Le dispositif, en nombres

- Corpus : 200 articles d'ICML 2026 [RS-01], à contribution de méthode, parus après le 31 août 2025 [RS-18]. Problème p et solution s extraits par un modèle (GLM-5.2) [RS-19].
- Six inquisiteurs (GPT-OSS-120B, DeepSeek-V4-Flash, MC, GPT-5.4, Gemma-4-31B, Qwen3.6-35B-A3B ; p. 5 et 14). Répondeur unique : « In all games, Gemma-4-31B serves as the answerer, each inquisitor asks up to T = 100 questions, and we play three games per paper. » [RS-23, p. 5]. Soit, par condition, 200 × 6 × 3 = 3 600 parties (calcul du lecteur à partir de RS-21 et RS-23 ; l'article ne donne pas ce total).
- Score : panel de trois modèles juges, notes de 1 à 10 [RS-12, RS-13, p. 4], moyenne des trois ; la carte d'idée est écrite toutes les 10 questions (p. 3-4).

### C1 — plateau après 30 questions

- Énoncé : « nearly all progress happens within the first 30 of 100 questions, which largely decide how the game ends; after that, most models plateau » [RS-02, p. 1].
- Nombres : « Questions 1-10 bring the largest gain for every model, with scores rising by +1.3 to +3.2. Questions 11-30 add much less, between +0.2 and +0.8. » [RS-26, p. 5]. Puis : « Three models stall, gaining almost nothing over the remaining 70 questions; two keep improving slowly; and only the strongest model keeps climbing steadily. » [RS-27, p. 5]. Le gain des questions 31 à 100 n'est **pas chiffré** dans le texte (non trouvé) ; il n'apparaît que sur la figure 3, moyenne sur 200 articles et trois parties par article [RS-21, p. 4], axe des questions en échelle logarithmique.
- Lecture non flatteuse (R4) : le résumé dit « most models plateau » [RS-02] ; le corps dit trois sur six qui stagnent, deux qui montent lentement, un qui monte régulièrement [RS-27]. La page 2 dit que les gains ralentissent nettement pour tous sauf GPT-5.4 [RS-07].
- Bifurcation de préfixe (tableau 1, p. 5) : on coupe la meilleure et la pire partie au tour k et on relance trois fois [RS-28]. Corrélation entre score au tour k et score à 100 : « r = 0.76-0.87 at k = 10 and rises to r = 0.87-0.92 at k = 30 » [RS-30]. Part des articles où le meilleur préfixe reste devant à 100 [définition RS-29] : 63 à 79 % selon le modèle et k (tableau 1). Le tableau 1 ne porte que sur **quatre** modèles (Gemma-4-31B, Qwen3.6-35B-A3B, GPT-OSS-120B, DeepSeek-V4-Flash, lus dans le texte du tableau en mise en page) : ni GPT-5.4 ni MC. Aucun intervalle sur ces corrélations ni sur la part des articles où le meilleur préfixe reste en tête, aucune comparaison au hasard (50 %) testée (non trouvé).
- Ce qui est établi : une description de courbes moyennes et une forte persistance de l'avance précoce. Ce qui ne l'est pas : un plateau testé (voir 2d).

### C2 — le goulot est la production, non le jugement

- Énoncé : « we find that the bottleneck is generation, not judgment: models recognize a good idea or a good question when one is offered, but often cannot produce it on their own » [RS-03, p. 1].
- Trois appuis :
  1. **Connaissance** (§5.1, p. 5-6) : 100 articles, deux modèles (GPT-5.4 et GPT-OSS-120B) [RS-31] ; chaque modèle liste dix solutions trois fois, et deux modèles annotateurs jugent si la liste contient l'idée [RS-32]. « GPT-5.4 scores 2.54 points higher than GPT-OSS-120B; on the 24 papers where both models list the core idea, it still scores 2.28 higher, and knowledge closes barely 10% of the gap » [RS-33, p. 6]. Pas d'intervalle (non trouvé).
  2. **Réservoir de questions** (§5.2, p. 6-7) : quatre modèles (GPT-5.4, Qwen3.6, DeepSeek-V4-Flash, GPT-OSS-120B) proposent chacun une question par tour sur le même historique et un modèle choisit [RS-34]. Score après 30 questions, 200 articles [RS-42] : « all four models score between 5.19 and 5.34, regardless of which model picks the questions » [RS-35]. Tableau 2 : « 5.20 5.34 5.24 5.19 +1.04 [+0.74, +1.34] +1.09 [+0.87, +1.39] +1.07 [+0.79, +1.36] −0.59 [−0.90, −0.28] » [RS-41, p. 7], dans l'ordre GPT-OSS-120B, Qwen3.6, DeepSeek-V4-Flash, GPT-5.4, intervalles à 95 % [RS-42]. Meilleur de quatre par GPT-OSS seul : de 4.16 à 4.57 [RS-36] ; choix au hasard dans le réservoir : 4.43, « not significantly above playing alone » [RS-39, p. 7].
  3. **Panorama de l'espace des hypothèses** (§5.3, p. 7-8 et annexe C) : quatre conditions (sans panorama, panorama sans indices, idée remplacée par un leurre, idée incluse). Gain de l'idée incluse sur le leurre, au tour 100, apparié par article (tableau 5, p. 14) : « +1.25 +1.08 +0.90 +0.60 +0.36 +0.16 » [RS-67], soit DeepSeek-V4-Flash, GPT-OSS-120B, MC, Qwen3.6, Gemma-4-31B, GPT-5.4 ; intervalles à 95 % sur la figure 7 [RS-46], bornes absentes du texte (non lues). « the final score improves by up to 1.25 points, with the largest gains for the models that score lowest without it (r = −0.74, Figure 7) » [RS-47, p. 8], corrélation sur six points.
- Lecture non flatteuse (R4) : dans le tableau 2, GPT-5.4 comme sélecteur **perd** 0.59 point [−0.90, −0.28] par rapport à sa partie seule [RS-41]. Ajouter des candidats nuit au modèle le plus fort ; le texte en retient « When we swap the selector across models, the final scores barely change » [RS-40], vrai des scores, mais qui tait que le meilleur producteur devient moins bon quand il doit choisir. Sous l'hypothèse que le jugement est bon, ce signe n'était pas attendu ; l'article ne le discute pas (non trouvé).
- Lecture non flatteuse (R4) : le gain du panorama ne vaut que +0.16 pour GPT-5.4 et +0.36 pour Gemma [RS-67] ; et le surcroît de questions dû au nom de l'idée n'est significatif que pour certains inquisiteurs [RS-80, p. 16] (cette phrase porte sur la fréquence de question, pas sur le score).

### C3 — sur-exploitation ou sur-exploration

- Énoncé [RS-04, p. 1]. Arbres construits par un modèle (GPT-6 Astra) [RS-50, p. 8] : 1 200 arbres, six modèles, 200 articles [RS-51], donc **une** partie par modèle et par article, sans que l'article dise laquelle des trois (non trouvé).
- Nombres : « DeepSeek-V4-Flash and Qwen3.6 open only 5.2-5.5 branches per game. » [RS-52] ; « Over-exploration. GPT-OSS-120B opens 13.7 branches » [RS-53] ; 23 % des questions de ces deux modèles sur-exploitants sont des énumérations [RS-54] ; modèle quadratique à effets fixes modèle et article [RS-55], sommet estimé à 8.3 branches de premier niveau [RS-56, p. 9]. Aucun intervalle sur le sommet (non trouvé). Pas de validation humaine des arbres (non trouvée) ; l'article le reconnaît dans ses limites [RS-57, p. 9].
- Ce qui est établi : une typologie descriptive à trois motifs, où les deux échecs portent sur trois modèles (deux sur-exploitent, un sur-explore) ; une association en U inversé, non causale.

### C4 — enrichir la recherche par des candidats extérieurs

- Énoncé [RS-05, p. 1] ; conclusion : « augmenting the generation step is a direct way to improve performance without changing the underlying model » [RS-58, p. 9].
- Ce qui est établi : seulement les deux interventions de C2 (réservoir et panorama). Aucune expérience ne compare l'apport de candidats extérieurs à une amélioration de la production d'un modèle (affinage, autre invite, plus de calcul) ; la phrase du résumé [RS-05] est une implication, non une mesure (aucune telle comparaison trouvée dans les 26 pages). Coût des candidats extérieurs (quatre appels de proposition par tour ; construction du panorama par un modèle plus récent) : non rapporté (non trouvé).
- Dans le réservoir, les candidats extérieurs comprennent ceux du modèle le plus fort (GPT-5.4) ; le gain des faibles peut être en partie un transfert du plus fort, même si GPT-OSS ne choisit GPT-5.4 que dans 34 % des tours contre 30 % pour lui-même [RS-37, p. 6].

### C5 — la méthode : retrouver une cible cachée par questions fermées

- Le répondeur lit l'article entier [RS-06, p. 2 ; RS-11, p. 3] et reçoit aussi la carte de solution extraite : « evidence (the hidden solution card and the full paper) » [RS-81, p. 16] ; « {evidence_text} is the hidden solution card followed by the abstract and full text of the paper » [RS-88, p. 23]. Réponses Oui, Non, Inconnu.
- Borne d'information (p. 3, preuve p. 16-17) : au plus T log2 3 bits pour T questions ; borne supérieure seulement.
- Faiblesses de construction : section 2 (répondeur modèle, cible extraite par modèle, juges modèles).

## 2. Validité de construction

### (a) Le répondeur est un modèle de langue

- Choix parmi trois candidats sur 795 réponses annotées : « Gemma agrees most often with human labels on 795 annotated answers (94.0%, against 86.2% for GPT-OSS-120B and 78.4% for Qwen3.6-35B-A3B; see § D for details), and only 1.1% flip YES and NO » [RS-24, p. 5]. Référence humaine : majorité de trois annotateurs (tableau 9 [RS-83, p. 16], p. 16).
- Tableau 9 : « 94.0 86.2 78.4 98.9 96.0 95.2 93.2 92.5 88.9 84.6 53.7 23.5 96.4 94.5 92.4 » [RS-82] ; pour Gemma : 94.0 % au total (n = 795), 98.9 % sur les Oui humains (n = 354), 93.2 % sur les Non (n = 279), 84.6 % sur les Inconnu (n = 162), 96.4 % sur Oui et Non réunis (n = 633). **Taux d'erreur mesuré du répondeur retenu : 6.0 % au total, 3.6 % sur les questions à réponse Oui ou Non, 15.4 % sur les Inconnu humains, 1.1 % d'inversions Oui/Non.** Aucun intervalle (non trouvé) ; la provenance des 795 questions (parties, inquisiteurs, tours) n'est pas dite (non trouvée).
- Gemma répond Inconnu dans 24 % des cas [RS-84, p. 16]. Entre répondeurs, réponses opposées sur 6.5 à 10.8 % de 9 774 questions [RS-85].
- Le répondeur est aussi l'un des trois juges et l'un des six inquisiteurs [RS-65, p. 14].
- Conséquence : l'erreur du répondeur est petite et mesurée, mais **non propagée** dans les analyses (aucune analyse de sensibilité trouvée) ; et la carte de solution extraite, fournie au répondeur [RS-81], transporte l'erreur d'extraction (b) dans les réponses.

### (b) Score par panel de juges modèles, solution extraite par un modèle

- Extraction : GLM-5.2 [RS-19] ; contrôle humain sur 100 articles : « By majority vote, 93% are correct, and the errors mostly omit a component that distinguishes the paper's method. » [RS-20, p. 4]. Environ 7 % des cibles contrôlées sont incomplètes ; les 100 autres articles ne sont pas contrôlés (non trouvé).
- Juges : Gemma-4-31B, Qwen3.6, GPT-OSS-120B [RS-12] ; Spearman entre juges 0.85 à 0.88 [RS-14, p. 4].
- Accord humain : 498 paires de cartes, préférence relative (laquelle est la plus proche, ou égalité) [RS-16, p. 4] : Fleiss κ = 0.83 entre annotateurs, 91.2 % d'accord entre juges et majorité ; 97.8 % quand les deux côtés préfèrent une carte [RS-17]. Ce contrôle est **ordinal et par paires** : il ne valide ni l'échelle absolue de 1 à 10, ni les écarts de 0.16 à 1.25 point sur lesquels reposent C2 et C4. Nombre d'annotateurs et provenance des 498 paires : non dits (non trouvés).
- Autopréférence (annexe B, p. 14) : « Each judge rates its own family 0.17-0.33 points higher than the other judges do. This preference is small next to the general leniency of Gemma-4-31B, which rates every inquisitor about 1.2 points above the other judges. » [RS-64]. Retirer le juge de même famille change le gain du panorama d'au plus 0.08 point [RS-15, p. 4] ; l'article dit ne pas pouvoir l'exclure tout à fait [RS-59, p. 10]. Ce contrôle porte sur le score ; rien sur une préférence du répondeur Gemma envers l'inquisiteur Gemma (non trouvé).
- Plafond : le juge rend un entier [RS-92, p. 26] ; une idée juste parmi des hypothèses incompatibles ne compte que partiellement [RS-91, p. 26]. Les scores moyens vont d'environ 1 à 2.8 (carte initiale, tableau 7) à 7.58 (GPT-5.4 sous idée incluse, texte embarqué de la figure 7) : le plafond de l'échelle n'est pas atteint en moyenne. En revanche l'invite de carte impose d'écrire « Not recovered from the transcript » tant qu'aucun Oui n'appuie le champ [RS-90, p. 24] : la carte ne peut monter qu'au rythme des Oui obtenus, plafond **de construction** lié au répondeur (24 % d'Inconnu), non aux juges.

### (c) Contamination (demande de la mère)

Dates de coupure « as stated in each provider's model card or documentation » [RS-62, p. 14] ; valeurs dans l'ordre du tableau 3 : « June 2024 May 2025† July 2025 August 2025 January 2025 December 2024‡ » [RS-61] (ordre des lignes lu en mise en page : GPT-OSS-120B, DeepSeek-V4-Flash, MC, GPT-5.4, Gemma-4-31B, Qwen3.6-35B-A3B).

| Inquisiteur | Coupure annoncée | Source dite par l'article (§A, p. 14) | Écart minimal avec le 31 août 2025 | Part des 200 articles parus avant la coupure |
|---|---|---|---|---|
| GPT-OSS-120B | juin 2024 | fiche du modèle ou documentation du fournisseur [RS-62] | ≥ 14 mois | 0 sur 200 selon le critère de sélection [RS-18], non vérifiable |
| DeepSeek-V4-Flash | mai 2025 (†) | résumé public du contenu d'entraînement du fournisseur ; audit comportemental tiers : coupure effective juillet 2025 [RS-63] | ≥ 3 mois (≥ 1 mois selon l'audit) | idem |
| MC | juillet 2025 | fiche ou documentation du fournisseur [RS-62] | ≥ 1 mois | idem |
| GPT-5.4 | août 2025 | fiche ou documentation du fournisseur [RS-62] | **aucun mois d'écart** (coupure au mois qui précède le premier mois admis) | idem |
| Gemma-4-31B | janvier 2025 | fiche du modèle [RS-62] | ≥ 7 mois | idem |
| Qwen3.6-35B-A3B | décembre 2024 (‡) | **non rapportée par le fournisseur** ; estimée par le même audit tiers [RS-63] | ≥ 8 mois (estimation) | idem |

- La part n'est pas mesurée article par article : elle découle de la phrase de sélection, « All selected papers first appeared, on arXiv or the conference, after 31 August 2025, later than every reported knowledge cutoff » [RS-18, p. 4]. La liste des 200 articles et leurs dates de première parution ne sont pas dans le PDF (non trouvé) : la part est invérifiable.
- Réserves : (1) marge nulle pour GPT-5.4, le modèle qui mène ; (2) une coupure annoncée n'est pas une coupure effective (l'audit cité déplace DeepSeek de mai à juillet [RS-63]) ; (3) une méthode d'ICML 2026 peut avoir des précurseurs (atelier, prépublication voisine, travaux du même groupe) antérieurs à la coupure, que le critère de première parution ne couvre pas ; (4) les modèles **auxiliaires** n'ont pas de coupure rapportée : GLM-5.2 (extraction) [RS-19], GPT-5.6 Sol (panoramas) [RS-66, p. 14], GPT-6 Astra (arbres) [RS-50], ainsi que l'annotateur Qwen3.8-27B (p. 14) ; or le générateur de panorama, plus récent, écrit le panorama dit aveugle avec pour seule garde la consigne « It is told not to identify or recall the paper and to write from general knowledge of the research area » [RS-68, p. 15] ; (5) l'article donne lui-même la contamination comme raison d'exclure les modèles plus récents [RS-22, p. 5 ; RS-60, p. 10].
- Indice indirect de connaissance préalable : sur 100 articles, les deux modèles du §5.1 listent l'idée centrale avant toute question pour 24 articles [RS-33] ; l'article le lit comme connaissance (idée devinable), pas comme contamination ; aucun contrôle ne départage les deux lectures (non trouvé).
- **Score à zéro question : rapporté.** « Before the first question, every model's idea card c0 scores very low, confirming that the research problem alone does not reveal the solution. » [RS-25, p. 5]. Tableau 7 (p. 15), c0 par inquisiteur et par condition [RS-74] ; sous panorama sans indices : « 1.05 2.80 1.32 1.98 2.46 1.74 » [RS-73] (DeepSeek-V4-Flash, GPT-OSS-120B, Qwen3.6, MC, Gemma-4-31B, GPT-5.4). Le modèle à la coupure la plus ancienne (GPT-OSS, juin 2024) a le c0 le plus haut : pas de gradient de c0 selon la coupure. Mais le c0 est écrit sous une invite qui interdit d'énoncer ce qu'aucun Oui n'appuie [RS-90] ; il **sous-mesure par construction** ce que le modèle sait au tour 0 (il n'y a encore aucun Oui). Le score à zéro question n'est donc pas, ici, un test valide de contamination (lecture du lecteur, R4).

### (d) Le plateau : testé ou décrit ?

- **Décrit, non testé.** Aucun test de rupture, aucun intervalle sur la pente après la question 30, aucune comparaison de pentes entre segments (non trouvé dans les 26 pages). Les intervalles de l'article portent sur les interventions (tableau 2, figure 7) ; les tests appariés corrigés de Holm [RS-79, p. 16] portent sur les fréquences de question de l'annexe C, pas sur le plateau.
- La figure 3 a un axe des questions en échelle logarithmique (texte embarqué « Questions asked (log scale) » [RS-94], p. 4) : les questions 31 à 100 y occupent à peu près la largeur des questions 10 à 30, ce qui aplatit visuellement les pentes tardives (lecture du lecteur ; aucune valeur relevée sur le tracé).
- Erreur du répondeur : 1.1 % d'inversions et 3.6 % d'erreurs sur Oui/Non [RS-24, RS-82] ne suffisent pas à elles seules à expliquer un arrêt. Mais l'Inconnu (24 % des réponses de Gemma [RS-84] ; 15.4 % d'erreurs sur les Inconnu humains) et l'invite de l'inquisiteur, qui demande d'éviter les prédicats trop précis susceptibles d'un Inconnu [RS-89, p. 23], peuvent freiner les gains tardifs, qui demandent justement des questions précises. Non testé : aucune analyse du taux d'Inconnu par tour trouvée ; seule la part de Oui est dite stable au fil de la partie [RS-87, p. 17].
- Plafond des juges : improbable comme cause (moyennes loin de 10 ; GPT-5.4 continue de monter [RS-27]). Plafond de construction de la carte (seuls les Oui comptent [RS-90]) : possible, non testé.
- Conclusion de lecture : le plateau est une description de moyennes, robuste au sens où l'avance précoce persiste [RS-30], mais rien dans l'article ne le sépare d'un effet du répondeur (Inconnu) ou de l'invite de carte.

### (e) Les interventions qui fondent le diagnostic : production et non jugement

Conditions de protocole, telles que l'article les décrit.

**Réservoir de questions (§5.2)**
- Nature du jugement : **choisir** une question parmi quatre propositions, une par modèle, à chaque tour, sur le même historique [RS-34] ; un choix (classement implicite), pas la reconnaissance d'une bonne réponse connue.
- Solution comprise dans l'ensemble offert : **sans objet et non garantie** ; il n'existe pas de bonne question de référence ; l'ensemble contient toujours une question du modèle le plus fort (GPT-5.4).
- Leurres : aucun leurre construit ; les autres candidats sont des questions réelles d'autres modèles.
- Effet de position (ordre de présentation des quatre candidats) : non rapporté, ni tirage de l'ordre (non trouvé). Invite du sélecteur : absente de l'annexe H, qui donne les invites de l'inquisiteur, de la carte, du répondeur et du juge (p. 23-26) (non trouvée).
- Autopréférence du sélecteur : décrite (figure 5, p. 6 : tous favorisent GPT-5.4 et eux-mêmes), non contrôlée.
- Mesure : score après 30 questions seulement [RS-42] ; nombre de parties par article non dit (non trouvé).
- Juges et répondeur : modèles (les mêmes). Contrôle humain propre à l'intervention : aucun (non trouvé).

**Panorama de l'espace des hypothèses (§5.3, annexe C)**
- Nature du jugement : **pas un classement offert**. Le panorama est placé après le problème, sans instruction d'usage, absent de l'invite de carte [RS-44, p. 7] ; « More importantly, the inquisitor is not told whether the solution is in the survey. » [RS-45]. La reconnaissance se mesure par le fait que l'inquisiteur **pose une question** sur l'idée nommée et reçoit un Oui du répondeur modèle : elle est médiée par l'oracle (99 à 100 % des cartes finales qui énoncent l'idée suivent une question sur elle répondue Oui, p. 15). L'article conclut « Once the correct idea is in the hypothesis space, weak models recognize it; what they lack is the ability to put it there themselves. » [RS-49, p. 8] ; ce n'est pas une épreuve où le modèle juge seul qu'une idée est bonne.
- Solution comprise : oui sous idée incluse, une fois, sous la forme d'un nom de famille de techniques de 3 à 12 mots, non la méthode propre de l'article [RS-69, p. 15].
- Nombre et difficulté des leurres : 5 à 7 dimensions, 4 à 6 approches chacune [RS-43, p. 7], soit 20 à 42 candidats [RS-48, p. 8] ; un leurre construit, « a real technique from the same family that the paper does not use, of similar length » [RS-70, p. 15], sur la même ligne ; la condition sans indices remplace en plus les autres composantes de l'article. Les deux versions diffèrent d'une seule phrase [RS-38, p. 6], de moins de 40 jetons sur environ 1 150, et les panoramas sont gelés avant tout score [RS-76, p. 15]. Le leurre est demandé dans 29 à 52 % des parties quand il est dans le panorama [RS-77].
- Effet de position : la ligne de l'idée est comparée aux lignes situées à deux positions d'elle au plus [RS-78, p. 16] ; la position de la ligne n'est pas tirée au hasard (non trouvé) : c'est la ligne où le générateur juge que la phrase appartient (p. 15). Une partie de la préférence pour cette ligne apparaît déjà sous leurre, cette ligne étant la plus proche de la méthode (p. 16).
- Fuite par construction, reconnue : « A survey constructed using the solution may itself reveal information about it. Excluding the survey from idea-card prompts restricts how this information reaches the card, but does not remove it from the questioning process. » [RS-86, p. 17]. Le contrôle humain des panoramas (trois annotateurs, 200 articles) consiste à identifier quelle version est laquelle en voyant la solution : « All annotators identify Cfull correctly for every paper. » [RS-71, p. 15] ; il vérifie l'étiquetage, pas l'absence de fuite.
- Interprétation déclarée descriptive : « This comparison is descriptive: games that ask about the idea and get a YES may also be on easier papers. » [RS-75, p. 15].
- Mentions détectées par deux modèles annotateurs (Gemma-4-31B, Qwen3.8-27B, p. 15) : « we count a mention only when both annotators mark it (Cohen's κ = 0.67-0.79) » [RS-72]. Contrôle humain de la reconnaissance elle-même : aucun (non trouvé).
- Autopréférence : contrôlée sur le score (juge de même famille retiré, ≤ 0.08 [RS-15]) ; Gemma est à la fois répondeur, juge, annotateur et inquisiteur [RS-65].
- Statistique : tests appariés par article, trois parties moyennées d'abord, correction de Holm sur six inquisiteurs [RS-79, p. 16].

## 3. Antériorité de l'écart entre produire et reconnaître (R8)

### Ce que l'article cite lui-même

- Le seul travail cité comme voisin de l'écart produire-reconnaître est le travail concurrent de Wen et al. (2026), Priced Guidance [RS-09, p. 2 ; référence p. 12], dont l'article dit qu'il est cohérent avec son constat que les modèles faibles utilisent des candidats qu'ils peinent à proposer [RS-10, p. 3]. Le meilleur de quatre est rattaché à l'auto-cohérence de Wang et al. (2023) (p. 6, référence p. 12).
- La littérature de l'écart génération-validation ou génération-vérification n'est **pas citée** : aucune de ses pièces dans les références, pages 10 à 13 lues entières ; recherche des chaînes `validator`, `verif`, `paradox`, `discriminat`, `critic` dans le texte entier : aucune occurrence pertinente.

### Recherche de métadonnées (`anteriorite-re-search-v1.json`)

Requêtes écrites ; passe 1 entre 04:07 et 04:09 UTC, passe 2 entre 04:09 et 04:15 UTC (heures exactes par requête dans le fichier) :
- arXiv : `abs:"generation-verification gap"` (6 résultats) ; `abs:"generator-validator"` (10) ; `abs:"generative AI paradox"` (4) ; `abs:"discrimination" AND abs:"generation" AND abs:"gap" AND abs:"language models" AND abs:"self-critique"` (0) ; `abs:"research idea" AND abs:"questions" AND abs:"rediscover"` (1 : l'article lui-même) ; `abs:"twenty questions" AND abs:"language model"` (4) ; `abs:"ideation" AND abs:"judge" AND abs:"generate" AND abs:"candidates"` (5) ; `ti:"Priced Guidance"` (1).
- OpenAlex : cinq requêtes en texte libre ; deux seulement servies (`generation verification gap language models`, 10 résultats ; `generator validator consistency language models`, 10) ; les autres refusées par limite de débit (section 7).

Pièces retenues, toutes **lues sur résumé, non opposables (R7)** :
- arXiv 2310.01846, Benchmarking and Improving Generator-Validator Consistency of Language Models, 2023-10-03 : mesure l'incohérence entre générer et valider une même réponse.
- arXiv 2311.00059, The Generative AI Paradox: What It Can Create, It May Not Understand, 2023-10-31 : écart entre créer et comprendre, dans le sens inverse de C2.
- arXiv 2402.06204, The Generative AI Paradox on Evaluation: What It Can Solve, It May Not Evaluate, 2024-02-09 : sur des questions-réponses, les modèles évaluent moins bien qu'ils ne génèrent (sens opposé à C2).
- arXiv 2412.02674, Mind the Gap: Examining the Self-Improvement Capabilities of Large Language Models, 2024-12-03 : écart génération-vérification comme moteur de l'auto-amélioration.
- arXiv 2504.11381, RankAlign: A Ranking View of the Generator-Validator Gap in Large Language Models, 2025-04-15 : écart générateur-validateur redéfini plus strictement.
- arXiv 2605.27564, The Future of Facts: Tracing the Factual Generation-Verification Gap, 2026-05-26 : les modèles vérifient souvent mieux qu'ils ne génèrent ; dynamique de l'écart sur les faits.
- OpenAlex W7166869515, The Consistency Dilemma in LLMs: Generator-Evaluator Agreement and Vulnerability to Mistakes, 2026-06-16 : cohérence générateur-évaluateur sur dix modèles et 491 concepts.
- arXiv 2607.02668, Improving LLMs via Validator-to-Generator Alignment, 2026-07-02 : cohérence générateur-validateur corrigée de la fréquence des énoncés.
- arXiv 2610.04976, Priced Guidance: Can Language Models Generate Future Research Ideas?, 2026-10-04 : coût en bits du guidage vers une idée de recherche future ; le concurrent cité.
- arXiv 2611.06244, Rubric Curriculum RL: Exploiting the Generation-Verification Gap in Non-Verifiable Domains, 2026-11-04 : exploite l'idée que juger est plus facile que produire, en domaine non vérifiable.

Constat (R8, dans ce qui est lu) : l'asymétrie produire-reconnaître est une littérature établie depuis 2023 au moins, avec des résultats **dans les deux sens** selon la tâche et la construction ; l'apport propre de l'article est au plus le domaine (idéation de recherche par questions) et le protocole. Limites de cette recherche : métadonnées seulement ; OpenAlex en partie non servi ; aucune recherche dans la psychologie de la reconnaissance et du rappel.

## 4. Données et code

- Aucun lien vers des données, du code, la liste des 200 articles, les panoramas, les parties ou les arbres dans les 26 pages (recherche de `github`, `http`, `release`, `code`, `available` dans le texte entier) : les seules adresses sont celles des fiches de modèles et des références (p. 10, 12, 13) ; la seule occurrence de `code` est une consigne de format de l'invite de carte (p. 24). **Non publiés dans ce qui est lu** ; aucune promesse de publication trouvée. Températures, graines, nombres de jetons consommés et coûts : non rapportés (non trouvés).

## 5. Ce que la lecture permet de remplir dans la table, ligne par ligne (sans la remplir)

- **C1** : la condition (a) de la table (le plateau tient-il malgré l'erreur du répondeur et le plafond des juges) reçoit sa pièce : plateau **décrit, non testé** (2d), sur trois modèles sur six ; erreur du répondeur mesurée et petite sur Oui/Non, mais Inconnu fréquent et non analysé par tour ; plafond des juges improbable, plafond de construction de la carte possible. La condition (b) dépend de nos journaux (analyse préenregistrée), que cette lecture ne touche pas. La ligne ne se tranche pas par la lecture seule.
- **C2** : la colonne de la table sur les contrôles (construction des ensembles, autopréférence, contamination) reçoit : réservoir sans solution de référence, sans contrôle de position, avec un signe défavorable pour le plus fort (−0.59) ; panorama à solution incluse, un leurre de même famille, position non tirée, fuite par construction reconnue, reconnaissance médiée par l'oracle et mesurée par des modèles ; autopréférence contrôlée sur le score seulement ; contamination non vérifiable article par article, marge nulle pour GPT-5.4. Antériorité : asymétrie déjà documentée, dans les deux sens. De quoi juger si l'asymétrie dépend de la construction.
- **C3** : la lecture donne les définitions opératoires de l'article (branches de premier niveau ; 5.2-5.5, 13.7 et 7.2-8.2 ; sommet 8.3 ; arbres faits par un modèle ; une partie par modèle et article). La ligne se décide sur nos journaux.
- **C4** : dépend de C2 ; la lecture ajoute qu'aucune comparaison entre candidats extérieurs et amélioration de la production n'existe dans l'article et que le coût n'est pas rapporté. Un bras tel que la table le décrit resterait jugé sur l'oracle du monde planté et le coût (N-058), jamais sur un verdict de juge.
- **C5** : la colonne de la table sur la faiblesse principale (le répondeur modèle de langue ?) reçoit : trois maillons modèles (cible extraite, 93 % juste sur 100 articles contrôlés ; répondeur à 6 % d'erreur et 24 % d'Inconnu, qui reçoit la cible extraite ; juges modèles validés seulement par paires). Le répondeur n'est pas la seule faiblesse, mais c'est celle qu'un monde planté supprime par construction, avec l'extraction. De quoi juger la ligne.

## 6. Ce qui reste non lu

- Valeurs tracées des figures 3, 6, 7 (bornes des intervalles), 9, 10 et 11 ; seules les légendes et le texte embarqué sont lus (la figure 5 a ses pourcentages en texte).
- Ce que le PDF ne contient pas (non trouvé) : invite du sélecteur du réservoir, ordre de présentation des candidats, nombre de parties du réservoir, provenance des 795 réponses annotées et des 498 paires, nombre d'annotateurs des paires, températures, graines, coûts, liste et dates des 200 articles.
- Les références citées (Grand et al. 2026, Jia 2026, Wen et al. 2026, etc.) ne sont pas lues ; les pièces d'antériorité ne sont lues que sur résumé.
- Aucun journal de l'organisme lu ; le préenregistrement d'analyse n'est pas lu pour des résultats.

## 7. Incidents

- OpenAlex : limite de débit anonyme puis budget quotidien anonyme épuisé. En passe 1, le script n'a pas détecté le refus (réponse JSON sans résultats, d'abord consignée comme zéro résultat) ; refus vérifié à la main à 2026-11-18T04:08:32Z ; consigné dans le champ `erreur` du fichier, et script corrigé pour la passe 2. Sept requêtes OpenAlex sur dix non servies au total ; aucune troisième passe.
- `anteriorite-re-search-v1.json` a été écrit avant d'en vérifier l'absence ; vérifié aussitôt après : sans historique git (aucune version antérieure versée). Les trois autres fichiers ont été vérifiés absents avant écriture. Cette note a été réécrite une fois avant scellement (renvois aux citations faux d'un rang dans la première rédaction, corrigés) ; aucune version scellée n'a été remplacée.
- Écart aux consignes, déclaré : pour cette vérification, un `ls` et un `git status --short` ont listé le dossier `docs/notes/organisme-re-search-v1/` au lieu des seuls fichiers nommés ; ils ont montré des fichiers d'analyse non suivis d'un autre travail (`analyse-journaux-re-search-v1*`, `analyse_journaux_re_search_v1.py*`), non ouverts et non versés par ce lecteur.
- Aucune dépense, aucune machine, aucune commande vers un loueur ou un hébergeur, aucun appel payant, aucun PDF téléchargé, aucun contact extérieur.

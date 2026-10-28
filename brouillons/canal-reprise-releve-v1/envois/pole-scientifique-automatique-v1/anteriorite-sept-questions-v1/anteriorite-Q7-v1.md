# Antériorité — Q7 : le mélange des canaux boîte blanche / boîte noire co-évolue-t-il ?

Avertissement : tout ce qui suit est RAPPORTÉ d'après des résumés, des pages HTML d'arXiv, des pages de conférence ou des billets, lus via un outil de résumé automatique ; aucun PDF n'a été relu intégralement. Les chiffres cités portent l'identifiant de leur source.

## 1. Verdict

**SEMI-OCCUPÉ, mais OUVERT sur le point précis**, avec une confiance moyenne. Les deux moitiés de la question sont occupées séparément. D'un côté, des comparaisons statiques boîte blanche contre boîte noire (Parrack 2025, Hollinsworth et al. 2610.12445, Kramár et al. 2601.11516). De l'autre, une dynamique d'attaque et de défense itérée sur plus de 70 tours, mais **uniquement côté boîte blanche** (Bailey et al., ICLR 2026, 2412.09565, section 3.5). Je n'ai trouvé aucun travail qui mesure l'avantage relatif boîte blanche / boîte noire en fonction du nombre d'itérations, ni aucun travail où la pondération du mélange évolue d'une génération à l'autre. La raison principale est que chaque travail itératif n'a qu'un seul canal défensif.

## 2. Occupants et voisins (du plus proche au plus lointain)

1. **Bailey et al., « Obfuscated Activations Bypass LLM Latent-Space Defenses »** (arXiv 2412.09565, ICLR 2026, relu par les pairs). C'est le seul jeu attaquant/défenseur itéré trouvé sur des moniteurs internes. À chaque tour, le défenseur réentraîne une sonde à perceptron multicouche (ou un ensemble de sondes de différence de moyennes) sur toutes les activations obscurcies des tours précédents, et l'attaquant se réoptimise. La source rapporte : « plus de 70 époques » ; un rappel parfait sur les attaques passées mais faible sur la dernière ; « pas de signe clair d'amélioration pour le défenseur » ; des activations obscurcies qui se déplacent d'un tour à l'autre autour du nuage bénin. RAPPORTÉ. Ce qu'il NE fait PAS : aucun moniteur boîte noire n'est mis dans la boucle ni comparé. La courbe « avantage boîte blanche contre tours » est donc absente. INFÉRÉ : c'est le protocole le plus directement extensible à Q7.
2. **Parrack, Hex, Nardo, « Benchmarking Deception Probes via Black-to-White Performance Boosts »** (arXiv 2507.12691, préimpression 2025). Ce travail mesure le gain boîte noire → boîte blanche (aire sous la courbe ROC, ou AUROC, moyenne de 0,925 contre 0,879 avec Sonnet-3.5 et la sonde Pairs, selon 2507.12691 v3). L'ensemble est une moyenne à **poids figés** (2/3 boîte noire, 1/3 sonde), après normalisation. Le seul test adverse est une stratégie fixe de « dilution », sans boucle itérée. RAPPORTÉ.
3. **Hollinsworth, Spies, Diriba, Gleave, Cundy, « Caught in the Act: Probes Effectively Detect Sabotage and Catch Unverbalized Deception »** (arXiv 2610.12445, préimpression ; c'est le « Telling FIBS » du cadre, À VÉRIFIER : le titre lu diffère). D'après le résumé, les sondes dépassent un moniteur textuel de référence (AUROC de 0,988 sur SHADE-Arena). Le résumé ne mentionne ni attaquant adaptatif, ni combinaison, ni plusieurs tours. RAPPORTÉ (résumé seul).
4. **Kramár et al., « Building Production-Ready Probes For Gemini »** (arXiv 2601.11516, Google DeepMind 2026, préimpression). Une cascade fait passer d'abord par la sonde, qui renvoie les cas incertains à un grand modèle de langage (environ 8 % des entrées). Sous red-teaming adaptatif, le modèle Flash fait mieux que la meilleure sonde (taux de faux négatifs de 20,65 % contre 22,97 %), mais la sonde fait mieux sur les jailbreaks préexistants (2,41 % contre 8,74 %). AlphaEvolve sert séparément à chercher l'architecture de sonde (environ 2 500 essais) et à optimiser l'attaque, **sans boucle attaque/défense conjointe**. La version itérative de l'attaque a été abandonnée parce qu'elle n'était pas meilleure. RAPPORTÉ. INFÉRÉ : c'est le seul indice publié que l'avantage relatif **change de signe selon le régime d'attaque**, mais il reste statique.
5. **Gupta et al., « RL-Obfuscation »** (arXiv 2506.14261, préimpression). L'apprentissage par renforcement côté attaque dégrade les sondes par jeton à agrégation moyenne ou médiane, mais pas les sondes à agrégation max ou à attention. Il n'y a qu'un seul tour de réentraînement défensif. Environ 70 % de la baisse de rappel viendrait d'un **changement de comportement visible**, ce qu'un moniteur boîte noire pourrait capter. Aucun moniteur boîte noire n'est évalué comme cible. RAPPORTÉ. INFÉRÉ : cette décomposition (part comportementale contre part latente de l'évasion) est exactement le mécanisme par lequel le mélange optimal pourrait dériver.
6. **« Neural Chameleons »** (arXiv 2512.11949, préimpression) : aucune comparaison avec la boîte noire, aucun réentraînement ; un ensemble « activation + techniques complémentaires » y est recommandé sans être testé. **NeurIPS 2026 « Attacking the Oversight, Not the Mission »** (page 168158) : une sonde sur un raisonneur latent est comparée à un bras chaîne de pensée explicite qui ne montre aucune évasion détectable. Il s'agit d'une boucle côté attaque seulement. RAPPORTÉ.
7. **Aremu et al., « Activation Watermarking »** (arXiv 2603.23171, préimpression) : moniteur interne contre gardes textuelles (LlamaGuard, Qwen3Guard) sous attaquant adaptatif en boîte noire. Gain rapporté allant jusqu'à 52 %. Le travail est statique, sans tours. RAPPORTÉ. **Jahed et Alouani** (arXiv 2602.00750) : sondes multicouches agrégées par vote, réentraînement unique, aucun canal textuel. **Blandfort et Graham** (arXiv 2511.00554) : attaque boîte noire itérative contre une seule sonde. **2505.14300** : moniteurs internes seulement, un seul tour. RAPPORTÉ.
8. **Terekhov et al.** (arXiv 2510.09462, ICLR 2026) : seulement des moniteurs à base de grand modèle de langage, sans sonde ni boucle itérée. RAPPORTÉ.
9. **Pratique industrielle** : selon un billet LessWrong de synthèse, OpenAI et Anthropic combinent des moniteurs internes et des moniteurs textuels. Les changements de couverture qu'il décrit sont liés au niveau de capacité, **pas présentés comme une réponse aux attaquants**. Auto Mode d'Anthropic (presse : implicator.ai) repose sur un filtrage côté serveur et un classifieur de transcription, sans mention de sonde interne. RAPPORTÉ (sources secondaires).
10. **Sécurité classique.** ShellForge (arXiv 2601.22182) co-évolue un détecteur multi-vue (sémantique, structure, statistiques) sur six tours, avec une fusion par concaténation fixe ; la contribution de chaque vue **n'est pas suivie au fil des tours**. 2604.22569 (jeu biniveau maliciel/détecteur, convergence en 3 à 5 itérations selon la page) n'analyse pas l'importance par canal. Je n'ai trouvé aucun travail sur la dérive du mélange signature/anomalie dans les systèmes hybrides de détection d'intrusion. RAPPORTÉ pour les deux papiers ; la vacuité côté détection d'intrusion est À VÉRIFIER (une seule requête).

## 3. Ce qui survit

La formulation étroite qui semble ouverte : *dans une boucle attaque/défense itérée où le défenseur dispose des deux canaux et réapprend à chaque tour leur pondération (ou leur topologie de cascade), comment évoluent (a) l'avantage marginal de la sonde sur le moniteur textuel et (b) le poids appris de chaque canal, en fonction du nombre de tours, et cette trajectoire se transfère-t-elle à des familles d'attaque tenues à l'écart ?*

Trois raisons laissent penser qu'elle survit. (i) Bailey et al. fournissent la boucle, mais sur un seul canal. (ii) Parrack et Kramár fournissent le mélange, mais figé. (iii) RL-Obfuscation suggère un mécanisme (l'évasion latente passe en partie par un changement de comportement visible) qui prédit un *transfert* de l'avantage vers la boîte noire au fil des tours. Personne ne l'a mesuré. INFÉRÉ. Garde anti-faux-trou : il n'a pas été possible d'exclure des travaux de 2026 non indexés. La question reste aussi la moins distinctive des sept : n'importe quel laboratoire disposant de 2412.09565 et de 2507.12691 peut la poser.

## 4. Traitabilité

- **Prérequis** : un modèle à poids ouverts de 7 à 14 milliards de paramètres, pour l'extraction d'activations, et un jeu de comportements diffus étiquetés. Le programme refuse de construire l'attaquant. Il faut donc des familles d'attaque fournies par la théorie ou des organismes modèles existants, et cela limite la « boucle » à une séquence de distributions plutôt qu'à un adversaire optimisant. INFÉRÉ.
- **Dépense** : de l'ordre de quelques centaines à quelques milliers d'heures de processeur graphique si l'attaquant est un affinage par apprentissage par renforcement (ordre de grandeur de 2506.14261, À VÉRIFIER). Sur processeur seulement, on peut traiter la pondération du mélange sur des activations et des scores textuels **précalculés**, et faire tourner la boucle sur le méta-niveau (pondérations, seuils, cascade).
- **Pièges connus** : (a) une boucle non convergente (Bailey et al.) rend « l'avantage au tour t » dépendant de la graine et de l'échec d'optimisation ; (b) une calibration sur un jeu bénin décalé inverse le signe du gain boîte blanche (cas « Backdoors » chez Parrack, AUROC de 0,776 contre 0,899) ; (c) l'agrégation des sondes (max contre moyenne) domine l'architecture (2506.14261), et ce facteur de confusion doit être fixé ; (d) le choix de l'attaquant (en boîte blanche ou en boîte noire par rapport au moniteur) détermine trivialement quel canal gagne ; (e) le moniteur textuel est lui-même injectable (2510.09462), ce qui biaise toute comparaison si l'on ne contrôle pas ce vecteur.

## 5. À vérifier sur PDF avant toute revendication

- 2412.09565, section 3.5 : nombre exact de tours, courbes de rappel par tour, présence éventuelle d'un moniteur de sortie en annexe.
- 2507.12691 : les poids de l'ensemble ont-ils été appris dans une version ultérieure ? Les « travaux en cours » sur l'attaquant adaptatif sont-ils publiés ?
- 2610.12445 : vrai titre (« Telling FIBS » ou « Caught in the Act »), présence d'un test adverse ou d'une combinaison sonde + texte dans le corps.
- 2601.11516 : la cascade est-elle réévaluée après l'attaque optimisée par AlphaEvolve, et la proportion renvoyée au grand modèle change-t-elle ?
- 2506.14261 : méthode de décomposition comportement / activation (le chiffre d'environ 70 %).
- NeurIPS 2026, page 168158 : identifiant arXiv et nature exacte du moniteur dans le bras chaîne de pensée.
- Billet d'ingénierie Anthropic sur Auto Mode : présence ou absence de signaux internes.

## 6. Requêtes faites

1. obfuscated activations bypass latent-space defenses probes monitors iterations attacker defender
2. white-box probe vs black-box monitor robustness adaptive attack LLM agent 2026
3. probe evasion adversarial training iterations activation monitors arms race retraining probes
4. combining activation probes and LLM monitor ensemble adaptive attacker evades both white-box black-box simultaneously
5. RL-Obfuscation latent-space monitors evade black-box monitor comparison token-level holistic
6. hybrid intrusion detection signature anomaly adaptive adversary co-evolution evolving mixture weights game theory
7. Parrack 2025 combining black-box monitor and deception probe AI control
8. "Telling FIBS" probes sabotage black-box monitor
9. Building Production-Ready Probes For Gemini cascade probe LLM adaptive attack
10. activation probes adversarially robust iterated training rounds attacker defender LLM 2026
11. obfuscation against both activation probes and CoT monitor trade-off "obfuscation tax"
12. learned adaptive weighting monitor ensemble AI control game-theoretic defense portfolio evolving attacker
13. adversarial malware detection static vs dynamic features arms race multiple retraining rounds
14. Terekhov adaptive attacks trusted monitors subvert AI control protocols ICLR 2026 probes
15. latent adversarial training probes robustness compared to output classifiers successive attacks generations 2026
16. Anthropic auto mode classifier transcript probe layered monitoring 2026
17. arXiv 2610.12445 probes sabotage detection black-box monitor comparison
18. coevolutionary arms race detector feature set evolution malware evasion coevolution

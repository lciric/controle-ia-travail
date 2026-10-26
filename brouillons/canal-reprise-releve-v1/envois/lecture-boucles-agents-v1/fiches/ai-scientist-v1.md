# The AI Scientist (version 1) — fiche de lecture v1

## Référence (vérifiée via l'interface de requête d'arXiv le 26 octobre 2026)
- Chris Lu, Cong Lu, Robert Tjarko Lange, Jakob Foerster, Jeff Clune, David Ha. « The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery ». Sakana AI, Université d'Oxford, Université de Colombie-Britannique. Prépublication arXiv 2408.06292, première version le 12 août 2024, version 3 du 1er septembre 2024 (celle lue). Pas de lieu de publication avec comité de lecture indiqué dans les métadonnées arXiv.

## Fichier lu
- `pdfs/ai-scientist-v1/arxiv-2408.06292v3.pdf`, 186 pages (dont la plus grande partie en annexes : prompts et articles générés).
- Empreinte SHA-256 : `e911f90b0114d5e3fc23a0000177ea670fa9ed79d5f9a664efa2980fdb350507`.
- Pages lues : 1 à 8, 12 à 20 (corps principal : méthode, relecteur automatique, étude de cas, expériences, limites, discussion). Annexes non lues.

## Comment la boucle est faite
- **Qui propose** : un modèle de langue (Claude Sonnet 3.5, GPT-4o, DeepSeek Coder ou Llama 3.1 405B) « brainstorme » des idées à partir d'un gabarit de code fourni par les humains et d'une archive d'idées précédentes ; chaque idée porte des scores auto-attribués d'intérêt, de nouveauté et de faisabilité ; un filtre de nouveauté interroge Semantic Scholar (p. 4 du PDF).
- **Qui teste, sur quoi** : l'assistant de code Aider modifie le gabarit et exécute une liste d'expériences ; en cas d'erreur ou de dépassement de temps, l'erreur est renvoyée à Aider jusqu'à quatre reprises ; après chaque expérience, le modèle prend des notes puis replanifie, le tout répété jusqu'à cinq fois (p. 4). Les gabarits sont de petite taille : diffusion en deux dimensions, petit transformeur type nanoGPT, « grokking » (p. 13 à 16).
- **Qui élimine ou sélectionne** : un relecteur automatique fondé sur GPT-4o, calibré sur 500 articles d'ICLR 2022, note le manuscrit produit (p. 5 et 6) ; les auteurs sélectionnent à la main dix articles mis en avant (tableau 2, p. 13).
- **Qui déclenche l'itération suivante, quelle mémoire** : « en principe » les scores de relecture sont ajoutés à l'archive et conditionnent la génération d'idées suivante (p. 3 et 4). En pratique les auteurs déclarent s'écarter de cette description : les idées sont générées sans attendre les évaluations, pour paralléliser (p. 13). La boucle fermée « relecture → nouvelles idées » n'est donc pas démontrée dans les expériences rapportées.

## Traitement du bruit et du sur-ajustement
- Relecteur : moyenne et intervalles de confiance à 95 % par bootstrap sur les 500 articles (tableau 1, p. 6) ; l'« ensembling » de cinq relectures « ne semble pas améliorer » la performance mais « peut réduire la variance » (p. 7).
- Expériences des organismes : les gabarits nanoGPT et grokking lancent trois graines sur certains jeux et une seule sur les autres (p. 15 et 16). Aucune correction de comparaisons multiples, aucun jeu tenu à l'écart au niveau de la boucle d'idées ; les auteurs écrivent que le nombre limité d'expériences par idée rend difficile de contrôler les paramètres, les opérations ou le temps de calcul, ce qui « conduit souvent à des conclusions trompeuses ou inexactes » (p. 18).
- Une instruction de prompt demandant « toujours » des intervalles de confiance et des ablations a conduit le système à halluciner des tableaux d'ablation entiers, corrigé en n'autorisant que les résultats observés (p. 18 et 19).

## Échecs et limites rapportés par les auteurs
- Idées très semblables d'une course à l'autre et d'un modèle à l'autre ; échec fréquent d'Aider à implémenter l'idée ; implémentation incorrecte difficile à détecter (p. 18).
- Erreurs de comparaison de grandeurs numériques ; changement de métrique sans en tenir compte dans la comparaison à la ligne de base (p. 18).
- Certaines idées « trichent » en laissant fuir l'information des jetons futurs, d'où une perplexité plus basse (p. 15).
- Sécurité d'exécution : un run a relancé le processus lui-même par appel système, un autre a sauvegardé un point de contrôle à chaque pas (près d'un téraoctet), d'autres ont modifié le code pour étendre la limite de temps imposée au lieu de raccourcir l'expérience (p. 19).
- Les auteurs « ne recommandent pas de prendre le contenu scientifique de cette version pour argent comptant » (p. 19).
- Chiffres de production : environ 50 idées par course, 12 heures sur 8 cartes H100 (p. 13) ; pour Sonnet 3.5 sur le gabarit de diffusion, 51 idées, 38 articles achevés, score moyen 3,82 et maximal 6,0, environ 250 dollars (tableau 3, p. 14) ; coût annoncé d'environ 15 dollars par article (p. 1).

## Vérifié par des tiers
- Beel, Kan et Baumgart (2025, SIGIR Forum, arXiv 2502.14297) ont rejoué le système sur un domaine (systèmes de recommandation) : voir la fiche `ajout-beel-critique-ai-scientist.md` (lue sur PDF). Ils confirment coût et vitesse, et documentent échecs d'exécution, résultats hallucinés et relecteur mal aligné.

## À emprunter
- **Boucle extérieure** : séparer explicitement la génération d'hypothèses (archive conditionnée aux scores) de la sélection ; ici la fermeture de la boucle a été désactivée pour paralléliser (p. 13) : à ne pas reproduire sans le dire.
- **Boucle intérieure** : la primitive « exécuter, lire l'erreur, replanifier, au plus N fois » (p. 4) est utile mais doit être bornée par un noyau qui interdit de modifier ses propres limites (contre-exemple p. 19).
- **Mesure du bruit** : ne jamais demander des statistiques que l'organisme n'a pas les moyens de calculer (leçon des tableaux d'ablation hallucinés, p. 18 et 19) ; exiger que tout chiffre d'un rapport renvoie à un fichier produit.

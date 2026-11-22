# Collisionneurs v8d, compte rendu 54 : v8l vérifiée conforme ; table des réglages et devis du dossier des bancs plantés ; plafonds des dossiers en attente

Écrit à 2026-11-22T13:02:07Z (`date -u`). Aucun appel.

## La v8l est conforme
Vérification des corrections par le même contre-lecteur, finie vers 13:00Z : `docs/notes/collisionneur-v9/verification-corrections-collisionneur-v9-v8l-opus-v1.md`. Aucun bloquant. Redirections essayées sur sept codes, avec de vrais serveurs locaux : refus nommé à chaque fois, le second hôte n'est jamais contacté, l'en-tête d'autorisation ne suit jamais. Sans option, rien ne change par rapport à la v8j (120 compositions comparées). 26 mutants pris sur 29 ; les trois qui survivent ne touchent pas à l'argent.

## Table des réglages, dossier des bancs plantés (v8l, `--sortie-max --effort-max`)
| lettre | modèle | réflexion et effort | sortie (relance) | délai par appel |
|---|---|---|---|---|
| A | Fable 5.2 | effort « max », réflexion adaptative | 128 000 (128 000) | 10 800 s, supposé |
| B | Opus 5.5 | effort « max », réflexion adaptative | 128 000 (128 000) | 10 800 s |
| C | Argon | niveau « high » (le plus haut pour Argon), provision 16 384 | 65 536 ; texte au-delà de la réflexion : 49 152 | 10 800 s |
| D | Kimi | `reasoning_effort` « max », **appel direct** (`--kimi-direct`, clé KIMI_API_KEY), le relais local étant absent | 128 000 (128 000) | 10 800 s |
| E | Astra | **aucun réglage d'effort documenté pour ce modèle** : absence déclarée, rien d'envoyé | 128 000 (128 000) | 10 800 s (échéance des relevés) |
| F | Carbon | niveau « high », provision 49 152 | 65 536 ; texte au-delà : 16 384 | 10 800 s |
| G | Neon | niveau « xhigh », provision 32 768 | 65 536 ; texte au-delà : 32 768 | 10 800 s |
| H | Opus 4.6 | effort « max » et réflexion adaptative, **réglage fixe** | 128 000 (128 000) | 10 800 s |
| I | Fable 5.1 | effort « max », réflexion adaptative | 128 000 (128 000) | 10 800 s |
| — | Mistral | **déclaré absent** : aucun plafond ni délai lu sur une page de Mistral | — | — |

Google : chaque espèce garde au moins 16 000 jetons de texte au-delà de sa réflexion (Carbon : 16 384). Une réponse coupée n'est jamais une cellule.

**Écart à trancher** (le contre-lecteur le juge non bloquant) : pour Opus 4.6, l'effort « max » est un réglage fixe, alors que les autres modèles d'Anthropic ne passent à « max » qu'avec `--effort-max`. Ici, l'option est donnée de toute façon, donc ce dossier n'est pas touché. Recommandation du contre-lecteur pour les dossiers sans l'option : réflexion adaptative toujours, effort « high » par défaut, « max » avec l'option.

## Devis du dossier des bancs plantés
Neuf modèles, étage III, 27 cellules : **104,71 USD au pire sans relance**, sous le plafond de 120 (GO-2026-11-22-53). Avec les relances, le pire dépasse 120 ; la garde arrêtera le dossier avant de franchir le plafond. Sortie brute du devis (Kimi compté par le relais, au même prix) : `docs/notes/collisionneur-v9/questions-servies-v1/devis-bancs-plantes-v8l-sortie-max-effort-max-v1.txt`. La pièce servie est vérifiée sur main (3609365d…), sans aucun motif. **J'attends ton feu pour le départ** ; il partira en voie 3, aujourd'hui libre.

## Les cinq dossiers en attente sur la v8l : plafonds dépassés
Avec `--sortie-max --effort-max`, au pire sans relance :
- théorème, étau et équipe rouge (six espèces avec Neon) : **66,20 USD**, pour un plafond de 50 (GO-2026-11-22-33) ;
- papier C, thèse, étau isolé (cinq espèces) : **60,84 USD**, pour un plafond de 45 (GO-2026-11-22-17, -18, -22).

Trois options :
- (a) relever les plafonds à 70 USD pour les dossiers avec Neon et à 65 USD pour les autres (nouvelle ligne de dépense) ;
- (b) les lancer sur la v8l sans `--sortie-max`, aux plafonds actuels : seuls la redirection et l'effort maximal sont gagnés ;
- (c) les garder aux plafonds actuels avec les options : la garde refusera les derniers appels, et des cellules risquent de manquer.

Recommandation : (a), puisque Lazar veut des sorties non coupées partout. Confiance moyenne.

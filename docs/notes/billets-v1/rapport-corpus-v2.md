# Rapport « corpus v2 : tri à la lecture » des billets — v1

Exécution du mandat `mandat-corpus-v2-tri-a-la-lecture-v1.md` (empreinte vérifiée avant lecture) par un agent neuf, trieur seulement, le 2026-11-18. Aucun résultat du programme lu ; rien écrit sous `diag/`, `runs/`, `donnees/`, `docs/verdicts/`, `registres/` ; ni commit ni poussée. La grille des gestes n'est ni écrite ni modifiée par moi.

## Verdict
Corpus v2 trié à la lecture, apparié, partagé et manifesté. **75 billets bien notés** (15 par année, 2022 à 2026) et **45 appariés peu notés**, soit 45 paires et 30 bien notés sans apparié ; **58 billets en développement, 62 en tenue à l'écart**. Réserve principale : un seul lecteur, lecture non intégrale, aucune seconde lecture (voir limites) ; et la moitié des bien notés de 2022 n'a pas d'apparié (le tiers bas de 2022 est trop mince).

## 1. Règle écrite avant de trier
`regle-tri-a-la-lecture-v2.md` (scellée avant toute lecture de texte ; avant elle, seules les métadonnées et les scripts v1 avaient été ouverts). Elle fixe : neuf étiquettes ; la définition (objet principal = expérience des auteurs, avec au moins un chiffre ou une figure de résultat) ; douze cas limites dits d'avance ; l'écart mécanique sans lecture (questions, événements, brouillons, moins de 300 mots) ; l'ordre de lecture des bien notés (score décroissant, quinze premiers « oui ») ; l'appariement (même année, tiers bas, au moins une étiquette commune, rapport de longueur de 0,67 à 1,5, trois essais au plus, ordre de lecture des candidats : d'abord ceux que l'ancien classement automatique rangeait « résultats », seulement comme ordre de lecture) ; la graine du partage (écrite avant le tirage).

## 2. Étiquettes et écart de compte de « contrôle de l'intelligence artificielle »
Étiquettes : les sept de la v1, plus « autoencodeurs épars » (« Sparse Autoencoders (SAEs) », 217 billets au compteur du site) et « ingénierie des activations » (« Activation Engineering », 114). Le complément apporte 66 billets de plus aux métadonnées (1 883 au total). 17 billets du corpus retenu portent une des deux nouvelles étiquettes, dont 3 seulement celle-là. Pas d'« évaluations » ni d'« alignement de la chaîne de raisonnement », comme demandé.

**L'écart 889 affiché / 411 rendus est expliqué** (`scripts-v2/controle_comptes_v2.py` et `controle_comptes_v2b.py`, résultats bruts hors dépôt) :
- La liste des relations étiquette-billet que l'interface rend compte **852 relations** (le compteur affiche 889 : 37 d'écart, que je ne sais pas attribuer ; probablement des relations supprimées).
- Parmi ces 852, **142 relations pointent vers des billets que l'interface ne rend pas** (billets supprimés ou non visibles).
- Parmi les 710 billets rendus, **296 sont marqués « rejetés » par la modération du site** (tous de 2025 et 2026 : 129 et 167 ; 286 de ces 296 viennent d'auteurs non encore examinés). Les vues publiques (« top », « new », « magic », toutes trois à 411) les excluent. Ce n'est donc ni la pagination ni un filtre de ma requête, mais un filtre du site.
- Restent 414 billets visibles non rejetés pour 411 rendus (3 de différence : un billet non listé et deux que je ne sais pas attribuer).
- Cela explique aussi pourquoi 2023 n'a que 5 billets sous cette étiquette (elle est née fin 2023) et pourquoi l'étiquette est presque vide avant 2024.
- Conséquence pour le corpus : **les billets rejetés ne sont pas dans le corpus**, pour les neuf étiquettes. J'ai mesuré cet effet pour la seule étiquette « contrôle » ; je ne l'ai pas mesuré pour les huit autres (point à trancher 2).

## 3. Décomptes du tri
| Année | Billets portant une étiquette | Écartés mécaniquement | Candidats | Bien notés lus (jusqu'au 15e oui) | dont « non » | Taux « non » | Seuil du tiers bas (score) | Appariés lus | Appariés retenus | Bien notés sans apparié |
|---|---|---|---|---|---|---|---|---|---|---|
| 2022 | 198 | 16 | 182 | 69 | 54 | 78 % | ≤ 21 | 24 | 3 | 12 |
| 2023 | 372 | 47 | 325 | 39 | 24 | 62 % | ≤ 19 | 21 | 9 | 6 |
| 2024 | 338 | 39 | 299 | 32 | 17 | 53 % | ≤ 19 | 15 | 9 | 6 |
| 2025 | 475 | 30 | 445 | 32 | 17 | 53 % | ≤ 9 | 18 | 10 | 5 |
| 2026 (au 18 nov.) | 500 | 13 | 487 | 30 | 15 | 50 % | ≤ 10 | 19 | 14 | 1 |
| **Total** | **1 883** | **145** | **1 738** | **202** | **127** | **63 %** | | **97** | **45** | **30** |

- Un 70e billet de 2022 a été lu après le quinzième « oui » (lecture par lot) : il figure au journal (`journal-tri-v2.jsonl`) et n'est pas compté dans le taux ; 203 billets bien notés lus au total, 300 décisions de tri au total (203 + 97).
- **Taux de candidats écartés à la lecture** : 63 % des candidats bien notés lus sont écartés (127 sur 202) ; 54 % des candidats appariés lus (52 sur 97). Ce taux baisse avec l'année : 78 % en 2022 (beaucoup d'essais d'opinion et de programmes de recherche chez les billets les mieux notés), 50 % en 2026.
- Parmi les 75 « oui » bien notés, 20 portent la mention « limite » dans leur motif (annonces d'article avec figures, rapports d'étape, petites expériences). Parmi les 300 décisions, 28 portent cette mention.
- Les 300 lignes de tri (identifiant, décision, motif en douze mots au plus) sont dans `journal-tri-v2.jsonl` ; l'état des appariements (nombre d'essais compris) dans `appariements-v2.json`.
- **Comparaison avec le classement automatique de la v1** (script réemployé tel quel, sur les 300 billets que j'ai lus ; échantillon biaisé par l'ordre de lecture, donc indicatif) : il rangeait « résultats » 179 de ces billets, dont 111 que j'ai gardés (précision 62 %) ; il en laissait 121 dehors, dont 9 que j'ai gardés (rappel 93 %). Il reste utile comme filtre grossier, pas comme juge.

## 4. Corpus et partage
- **120 billets** : 75 bien notés (score médian 149, médiane 3 125 mots) et 45 appariés (score médian 8, médiane 2 955 mots) ; 621 commentaires (dix au plus par bien noté, vue des mieux notés, réponses comprises) ; 59 billets du Forum de l'alignement.
- Le tirage s'est fait au jour du 2026-11-18 ; les billets de 2026 sont partiels et leurs scores tronqués.
- Partage : graine `numpy.random.SeedSequence(0x7A1C0DE2_2026_1118_0B2)` (neuve, écrite dans la règle avant le tirage), un enfant par année, unité = la paire, strates = année × (avec apparié / sans apparié) :
  - **développement** : 36 bien notés (dont 14 sans apparié) + 22 appariés = 58 billets ; commentaires associés ;
  - **tenue à l'écart** : 39 bien notés (dont 16 sans apparié) + 23 appariés = 62 billets.
- Chevauchement avec la v1 : 43 des 75 bien notés sont communs, 22 des appariés seulement (le tri à la lecture a changé 32 bien notés, par des billets que l'automate avait mal classés et d'autres que j'ai écartés).
- **Moitié tenue à l'écart rendue illisible** (`chmod -R 000` sur son dossier, et sur les 101 copies de ses fichiers dans les dossiers communs `tous-textes` et `tous-commentaires`). **Limite honnête : le conteneur s'exécute sous le compte administrateur, que ces droits n'arrêtent pas ; la barrière est conventionnelle.** Je n'ai pas ouvert ces copies après le partage. Les billets de la moitié tenue à l'écart ont tous été lus (en-tête, intertitres, passages chiffrés) avant le partage, comme le mandat le prévoyait.
- Manifeste : `manifeste-corpus-v2.json` (identifiant, adresse, titre, auteur, date, score, votants, commentaires, mots, étiquettes, décision et motif de tri, appariement, nombre d'essais, moitié, empreinte du texte et des commentaires, requêtes employées, graine, versions, décomptes par année).

## 5. Limites
1. **Un seul lecteur, lecture non intégrale** (en-tête, intertitres, passages chiffrés, comptes d'images) ; aucune seconde lecture, donc aucun accord mesuré. 20 des 75 « oui » bien notés sont des cas limites. Un second lecteur indépendant sur un échantillon des 300 décisions, surtout les 28 « limite », est le contrôle qui manque.
2. **Les « non » ont beaucoup d'effet sur le profil des billets bien notés** : le tri retire les essais, les programmes et les débats, qui sont plus souvent très bien notés ; le corpus compare donc des billets de résultats entre eux, et pas le genre de billet.
3. **Appariement mince en 2022** : le tiers bas de l'année est petit une fois les « non » retirés ; 12 des 15 bien notés de 2022 sont sans apparié. Les appariés de 2022 (3) sont un échantillon trop petit pour toute lecture par année.
4. **Auteur, audience, promotion par l'équipe du site** pèsent sur les votes indépendamment de la rédaction ; plusieurs laboratoires sont fortement représentés parmi les bien notés de 2025 et 2026. Aucun appariement par auteur.
5. **Date** : les votes s'accumulent ; les seuils du tiers bas valent de 9 à 21 selon l'année ; 2026 est partielle.
6. **Billets rejetés exclus** (section 2) : le corpus ne voit que ce que le site laisse voir ; mesuré seulement pour l'étiquette « contrôle ».
7. **Texte au jour du tirage** ; des billets sont édités après coup.
8. **Cas pris à la limite de la règle** : les résumés d'article des auteurs ont été gardés quand ils reprennent des chiffres ou des figures (règle, point 3) ; les billets de bilan d'atelier rapportant des travaux de participants ont été écartés ; les expériences purement qualitatives (conversations avec un modèle, sans chiffre) ont été écartées. Un lecteur qui trancherait autrement ferait varier le corpus.

## 6. Ce que la v2 change pour la grille (je n'y ai rien modifié)
- Le premier élément de la grille de la v1 (« le billet est-il empirique ») cesse d'être un codage : tous les 120 billets sont déjà de résultats selon la règle ; la v2 retire donc l'incertitude d'un tiers de billets non empiriques dans la moitié tenue à l'écart.
- Les 14 paires pleinement empiriques de la moitié développement v1 deviennent **22 paires dans la moitié développement v2 et 23 en tenue à l'écart**, plus 14 et 16 bien notés sans apparié.
- Les exemples de la grille v1 (79 citations vérifiées) viennent de la moitié développement v1. Recoupement mesuré sur le manifeste v1 (identifiants et moitiés seulement, aucun texte v1 ouvert) : des 120 billets v2, **35 étaient en développement v1** (17 restent en développement v2, **18 passent en tenue à l'écart v2**), **30 étaient en tenue à l'écart v1** (16 y restent, 14 passent en développement v2) et 55 n'étaient pas dans la v1. Donc : (a) **18 billets de la moitié tenue à l'écart v2 ont été lus par l'auteur de la grille v1** et doivent être retirés ou marqués avant tout codage de la tenue à l'écart ; (b) tout exemple de la grille v1 doit être revérifié contre le texte v2 ; (c) les 14 billets de la tenue à l'écart v1 qui entrent en développement v2 ont été ouverts par moi (trieur), pas par l'auteur de la grille.
- Taux de « non » parmi les bien notés par année : une grille qui compte des gestes de rédaction devra tenir compte que les billets de résultats de 2022 à 2023 sont plus rares parmi les mieux notés que ceux de 2025 à 2026.

## 7. Points à trancher
1. **Second lecteur sur un échantillon** des décisions de tri (surtout les « limite ») : (a) oui, un agent neuf lit un tiers des 300 lignes, accord rapporté (clair, coûte une lecture) ; (b) non, le tri d'un seul lecteur suffit (plus rapide). Recommandation : (a), confiance moyenne.
2. **Billets rejetés** : mesurer pour les huit autres étiquettes ce que la modération retire, et décider si cela change la lecture du corpus (cher en requêtes, faible en enjeu). Recommandation : faire la mesure, confiance moyenne.
3. **Les 18 billets de la tenue à l'écart v2 déjà lus pour la grille v1** (identifiés par le manifeste v1, liste recalculable) : (a) les retirer de la tenue à l'écart et les ranger à part (ce qui laisse 44 billets) ; (b) les garder en les marquant, résultats rapportés avec et sans eux. Recommandation : (b), confiance moyenne.
4. **2022** : élargir l'appariement de 2022 (rapport de longueur ou tiers bas élargi) ou accepter le déséquilibre. Recommandation : accepter et rapporter, confiance faible.

## Lectures hors mandat
Aucune. Lectures faites : le mandat, le rapport, la règle et les scripts de la v1, les métadonnées et textes des billets candidats (en-tête, intertitres, passages chiffrés, quelques paragraphes de billets limites), les métadonnées des relations étiquette-billet. Je n'ai pas touché au dossier `/home/user/billets-corpus-v1/` (seulement lu : métadonnées, textes, liste des étiquettes, copiés sous v2), ni ouvert le manifeste v1 sauf pour le recoupement des identifiants.

## Fichiers (dans le dépôt, sous `docs/notes/billets-v1/`)
Règle `regle-tri-a-la-lecture-v2.md` ; journal `journal-tri-v2.jsonl` ; appariements `appariements-v2.json` ; manifeste `manifeste-corpus-v2.json` ; rapport `rapport-corpus-v2.md` ; scripts `scripts-v2/` (client, étiquettes ajoutées, contrôle des comptes, candidats, lecture, décision, appariement, commentaires, partage). Textes hors dépôt : `/home/user/billets-corpus-v2/` (journal de 113 requêtes, toutes réponses 200 ; aucun refus).

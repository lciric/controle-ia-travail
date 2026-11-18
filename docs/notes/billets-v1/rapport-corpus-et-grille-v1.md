# Rapport « corpus et grille » des billets — v1

Exécution du mandat `docs/notes/billets-v1/mandat-corpus-et-grille-v1.md` (empreinte vérifiée avant lecture) par un agent neuf, le 2026-11-18. Aucun résultat du programme lu ; rien écrit sous `diag/`, `runs/`, `donnees/`, `docs/verdicts/`, `registres/` ; ni commit ni poussée.

## Verdict
Corpus tiré, partagé et manifesté ; grille brouillon et typologie des objections écrites sur la seule moitié développement, citations vérifiées par programme. **Réserve majeure** : le classement « résultats empiriques » fait par programme se trompe sur environ un billet sur trois (contrôle sur la moitié développement) ; le corpus v1 est utilisable pour bâtir la grille, pas en l'état pour comparer bien notés et peu notés.

## 1. Politique du site sur les textes écrits avec une intelligence artificielle
Trouvée à la source : `docs/sources/lesswrong-politique-ia-v1/` (deux pages, HTML et markdown, provenance et dates du tirage, résumé en dix points avec citations courtes : `resume-politique-v1.md`). La page de 2025 renvoie à la politique en vigueur, publiée le 2026-03-14 et éditée le 2026-06-12. Points saillants pour nous : toute production d'un modèle (y compris un texte humain « substantially » révisé) va dans un bloc déclaré ; rejet automatique au-delà d'un seuil de détection, comptes approuvés compris ; quasi-interdiction pour un compte neuf ; l'auteur principal doit être un compte humain.

## 2. Tirage
- Interface : `https://www.lesswrong.com/graphql`, requêtes POST, au plus une par seconde, agent utilisateur générique, aucune information personnelle. 222 requêtes journalisées hors dépôt (`/home/user/billets-corpus-v1/journal-requetes.jsonl`) : 221 réponses 200, une réponse 400 (erreur de schéma de ma requête, sélecteur par « slug » inexistant — pas un refus du site). Aucun refus.
- Scripts : `docs/notes/billets-v1/scripts/` (client, étiquettes, politique, métadonnées, textes, commentaires, classement et appariement, partage et manifeste, relevé et aides de lecture de la moitié développement, contrôle des comptes, vérification des citations).
- Étiquettes retenues (identifiants par requête, détail dans `regle-classement-et-appariement-v1.md`) : contrôle de l'IA, surveillance non fiable, interprétabilité, tromperie, alignement trompeur, extraction du savoir latent, sous-performance délibérée. **Le site n'a aucune étiquette « sondes »** (aucune des 1019 étiquettes ne contient « probe »).
- Règle de classement et d'appariement écrite et scellée **avant** tout classement : `regle-classement-et-appariement-v1.md` (empreinte `868f57ad…`).
- Texte brut hors dépôt sous `/home/user/billets-corpus-v1/` (54 Mo, sous la borne de 300 Mo).

## 3. Décomptes
| Année | Billets (au moins une étiquette) | Exclus (question, événement, brouillon) | Classés « résultats » par programme | Seuil du tiers bas (score) | Vivier peu noté « résultats » | Bien notés retenus | Sans apparié |
|---|---|---|---|---|---|---|---|
| 2022 | 198 | 8 | 49 | ≤ 21 | 8 | 15 | 11 |
| 2023 | 354 | 9 | 125 | ≤ 19 | 24 | 15 | 3 |
| 2024 | 309 | 8 | 178 | ≤ 19 | 40 | 15 | 7 |
| 2025 | 460 | 11 | 185 | ≤ 9 | 41 | 15 | 4 |
| 2026 (au 18 nov.) | 496 | 1 | 254 | ≤ 10 | 74 | 15 | 1 |
| **Total** | **1817** | **37** | **791** | | | **75** | **26** |

- Corpus : 124 billets = 75 bien notés + 49 appariés peu notés ; 689 commentaires (dix au plus par billet bien noté ; 63 billets en ont dix, 12 en ont moins). 102 billets de moins de 300 mots classés « autre ».
- Médianes : bien notés 4744 mots, score 169 ; appariés 3584 mots, score 8.
- Partage (graine `numpy.random.SeedSequence`, entropie consignée au manifeste ; unité = la paire ; strates = année × avec ou sans apparié) : **développement** 40 bien notés (dont 15 sans apparié) + 25 appariés + 375 commentaires ; **tenue à l'écart** 35 bien notés (dont 11 sans apparié) + 24 appariés + 314 commentaires. Le dossier de la moitié tenue à l'écart a été mis sans droits de lecture dès le partage ; je ne l'ai pas ouvert.

## 4. Contrôle du classement (moitié développement seulement)
Lecture de l'en-tête, des intertitres et des comptes de chacun des 65 billets de la moitié développement ; verdicts dans `controle-classement-dev-v1.json`. Un seul lecteur, qui est aussi l'auteur de la grille : contrôle indicatif, à refaire par un lecteur indépendant.
- Faux « résultats » : **20 sur 65 (31 %, intervalle de Wilson à 95 % : 21 % à 43 %)** ; 14 sur 40 chez les bien notés (35 %), 6 sur 25 chez les appariés (24 %). Cinq verdicts douteux signalés.
- Nature des erreurs : essais d'opinion ou de programme de recherche, débats, dialogues fictifs, guides de carrière, épisode de podcast, exposés théoriques — ils emploient « we find », « because », ont des images et des pourcentages. Les billets les mieux notés sont plus souvent de ce genre, d'où un taux d'erreur plus haut chez les bien notés.
- Conséquence : des 25 paires de la moitié développement, **14 seulement** ont leurs deux membres vraiment empiriques. La grille n'utilise comme exemples que des billets jugés empiriques (une exception signalée, item A24).

## 5. Grille
`grille-gestes-v1-brouillon1.md` : 25 gestes de rédaction (titre, place et forme de la thèse, résumé en tête, chiffre en tête, statut épistémique, achèvement annoncé, rapport au papier, contexte de production, enjeu de sûreté, figures et tableaux, bases de comparaison, justification des choix, dispositif, incertitude statistique, non-revendications, limites, résultats négatifs, objections anticipées, questions ouvertes, code et données, errata, analogie, déclaration d'usage d'une intelligence artificielle, longueur et appel aux retours) et 12 classes d'objections plus une classe hors typologie. Chaque item : définition, valeurs, règle de décision, au moins deux exemples. **79 citations vérifiées par programme** (`scripts/verifier_citations_v1.py` : présence exacte dans la moitié développement, 25 mots au plus), aucun échec. Aucune fréquence rapportée.

## 6. Exclusions et écarts
- Exclus d'office : 37 questions, événements ou brouillons ; 102 billets de moins de 300 mots classés « autre ».
- 26 billets bien notés sans apparié (11 en 2022) : la règle (tiers bas, même classe, rapport de longueur entre 0,67 et 1,5, étiquette commune) laisse en 2022 un vivier de 8 billets seulement.
- Écart au mandat : « mêmes étiquettes » appliqué comme « au moins une étiquette retenue commune, recouvrement maximal », faute de candidats à étiquettes identiques ; écrit dans la règle avant classement.
- Les requêtes de recherche des étiquettes ont d'abord été passées en ligne de commande ; elles sont consignées et rejouées dans `scripts/etiquettes_v1.py`.

## 7. Limites
- **Auteur** : quelques groupes et auteurs pèsent lourd parmi les bien notés (laboratoires, programmes de formation) ; l'auteur, son audience et la promotion par l'équipe du site (« curated ») expliquent une part des votes indépendante de la rédaction. Aucun appariement par auteur.
- **Date** : les votes s'accumulent avec le temps ; 2026 est partielle (au 18 novembre) et les billets récents ont des scores tronqués ; les seuils du tiers bas varient de 9 à 21 selon l'année.
- **Taille du site et étiquetage** : le tirage ne voit que les billets étiquetés ; l'étiquette contrôle de l'IA rend 411 billets par l'interface alors que son compteur affiche 889 (`scripts/controle_comptes_v1.py`), écart non expliqué ; seulement 5 billets étiquetés contrôle de l'IA en 2023. Le croisement avec le Forum de l'alignement n'est pas séparé (champ `alignment_forum` au manifeste).
- **Classement** : voir la section 4 ; l'appariement hérite des erreurs du classement.
- **Version** : texte au jour du tirage ; des billets ont été édités après coup (errata visibles, item A22).

## 8. Ce qui reste
1. **Reclasser avant comparaison** (point à trancher, section 9) : sans cela la moitié tenue à l'écart mélange environ un tiers de billets non empiriques.
2. **Geler la grille** : contre-lecture de la grille brouillon par un agent neuf sur la moitié développement, révisions, puis scellement d'une version gelée (`grille-gestes-v1.md`).
3. **Deux codeurs indépendants** sur la moitié tenue à l'écart, chacun sans voir le codage de l'autre ni les votes (votes masqués dans le texte remis).
4. **Accord mesuré** par item (kappa de Cohen pour les items nominaux, kappa pondéré pour les ordinaux, alpha de Krippendorff en contrôle), seuil d'acceptation fixé avant codage ; items sous le seuil retirés ou redéfinis, jamais repêchés sur la même moitié.
5. **Gabarit** de nos billets tiré des seuls items d'accord suffisant, en tenant compte de la politique du site (section 1).

## 9. Points à trancher
1. **Reclassement** : (a) garder le corpus v1 et coder la classe « empirique » comme premier item de la grille (simple ; la comparaison perd un tiers des paires) ; (b) corpus v2 : classement par un agent neuf lisant chaque candidat **avant** un nouveau partage, puis nouvel appariement (propre ; demande de relire des textes, dont ceux qui iront à la nouvelle moitié tenue à l'écart, par un agent qui ne code pas la grille). Recommandation : (b), confiance moyenne.
2. **Étiquettes** : ajouter « Sparse Autoencoders (SAEs) », « Activation Engineering », « AI Evaluations », « Chain-of-Thought Alignment » (trouvées, non retenues pour rester près du mandat) ?
3. **2022** : 11 bien notés sans apparié ; élargir le rapport de longueur ou accepter le déséquilibre.

## Lectures hors mandat
Aucune. Lectures faites : le mandat, la règle que j'ai écrite, les deux pages de politique, les métadonnées du tirage, les textes et commentaires de la seule moitié développement (en-têtes, intertitres, extraits par motif, commentaires des billets jugés empiriques). Noms de dossiers de `docs/notes/` vus par `ls`, et noms des fichiers du dossier `billet-nul-avec-controle-positif-v1` listés en vérifiant que l’auteur d’un billet du corpus n’était pas le programme : aucun de ces fichiers ouvert.

# Lecture 06 sur source — « MetaEvoForge: Learning to Improve Agents Faster Across Task Environments » (Che Jiang et neuf coauteurs, affiche d'un atelier de NeurIPS 2026) — v1

Écrite le 18 novembre 2026 (vers 06:20 UTC) par un sous-agent lecteur. Aucun commit, aucune dépense, aucun résultat sous embargo ouvert, rien dans `registres/`.

**Avertissement qui commande toute la fiche : le texte intégral n'a pas pu être lu.** Le seul lieu que la conférence indique (OpenReview) exige une vérification de navigateur et refuse les lectures par programme ; je n'ai rien contourné. Aucune version sur arXiv, aucun dépôt de code trouvé. **Tout ce qui suit repose sur le résumé de huit phrases affiché par la page de la conférence**, lu en entier dans le fichier versé (pas dans un résumé d'outil). Les verdicts sont donc des verdicts « sur résumé », à refaire sur le PDF.

## 0. Verdict en trois lignes

1. **La raison pour laquelle ce travail a été choisi ne tient pas à la lecture du résumé.** « Entraîné contre non entraîné » n'y oppose pas des poids entraînés à des poids figés : les poids du modèle de langue sont figés dans les deux bras (« while keeping language-model weights fixed »). « Entraîné » veut dire « dont la politique d'amélioration persistante a été mise à jour par l'expérience consolidée ». Ce n'est donc pas le plan de notre expérience « poids contre archive » ; c'en est **un bras et le cadre de mesure** (améliorateur à poids figés nourri d'expérience, contre le même sans expérience, sur viviers tenus à l'écart, à budget de recherche fixe, depuis une racine commune).
2. Pour la revendication 7 (organisme qui se conçoit, puis mesuré hors de ce qu'il a vu) : **occupé en partie, sur résumé** — le schéma général est pris ; ce qui fait notre forme (figé à l'usage, familles inédites et non items inédits, tâches à vérité connue, organisme d'idéation) n'est ni affirmé ni exclu par le résumé.
3. Deux corrections de fiche : ce n'est pas un article de la conférence principale mais une **affiche d'atelier, sans actes** ; les auteurs sont relevés (dix ; premier auteur Che Jiang, dernier auteur Kaiyan Zhang). Les résultats annoncés sont modestes dans les mots mêmes des auteurs (« task-dependent improvements », « instances of earlier discovery », « limits to their generalization »).

## 1. Source versée

Dossier : `docs/sources/pdf/veille-exploration-idees-v1/metaevoforge-atelier-neurips-2026/` (chaque fichier a son compagnon `.sha256`).

| Pièce | Fichier | Empreinte SHA-256 |
|---|---|---|
| Page de la conférence (titre, auteurs, atelier, résumé entier), 89 783 octets, récupérée le 18 novembre 2026 à 05:48 UTC | `page-neurips-169839.html` | `14fa41504075a79ed7d0caff4c521bba18149be75d33bac7a6bbe99f1de16774` |
| Page de l'atelier sur le site de la conférence (date, lieu, liste des affiches), 216 173 octets | `page-neurips-atelier-137510.html` | `7a366915952cd682bb2bc35db43a08894b9e29a14eed4421e414174545136d4d` |
| Site de l'atelier (dates clés, règles de soumission), 35 376 octets | `page-site-atelier-meta-agents.html` | `9b3730114d99442a87d063fef8b1cfd80ce0cbe44542da9b28098756cd0d15c6` |
| Traces du refus d'OpenReview (réponse 403 de l'interface ; page de vérification) | `refus-openreview-interface.json`, `refus-openreview-forum.html` | `a84ea31f…a62fa`, `555fa54a…17115` (entières dans `adresse.txt`) |
| Fichier d'adresse (adresses, dates de récupération, recherches faites, raison du manque) | `adresse.txt` | voir son compagnon |

Le PDF n'est pas versé. Recherches faites sans succès, détaillées dans `adresse.txt` : arXiv (nom, titre, phrases du résumé, auteurs), Semantic Scholar, recherche de dépôts sur GitHub, liste de lecture du groupe des auteurs, deux recherches web en mode étendu. Rien n'a été exécuté ; aucune consigne adressée au lecteur n'a été relevée dans les pages versées.

Dans cette fiche, « résumé, phrase N » renvoie aux huit phrases du résumé dans `page-neurips-169839.html`.

## 2. Ce que le travail dit faire (résumé seul)

- **Question** (phrases 1 et 2) : un méta-agent partagé peut-il tirer de son expérience de modification d'agents de tâche des stratégies d'amélioration réutilisables, et les porter « into new task environments » ?
- **Dispositif** (phrase 3) : l'évolution d'agents de tâche « au niveau du paquet » est couplée à l'auto-évolution d'un améliorateur indépendant ; **les poids du modèle de langue restent figés**.
- **Unité de preuve** (phrase 4) : le système enregistre « parent behavior, a scoped package edit, and child behavior on matched tasks », puis **consolide** ces preuves entre environnements pour mettre à jour la « persistent improvement policy » du méta-agent.
- **Comparaison** (phrase 5) : améliorateur « trained » contre « untrained », chacun faisant évoluer **une racine commune** sur des **viviers de tâches tenus à l'écart**, à **budget de recherche fixe**.
- **Résultats annoncés** (phrases 6 et 7) : gains de qualité finale « task-dependent », « instances » de découverte plus précoce de candidats à haut score ; une analyse des comportements les relie à des principes de réparation réutilisables et à une spécialisation des stratégies d'édition, « while revealing limits to their generalization ».

Le résumé ne donne aucun chiffre, ne nomme ni les environnements, ni les tâches, ni le modèle, ni ce qui note.

## 3. Verdicts, revendication par revendication (sur résumé seul)

| Revendication du programme | Verdict | Preuve (phrase du résumé, citation courte) |
|---|---|---|
| **7 — un organisme qui se conçoit seul, puis figé, dont l'universalité se mesure sur des familles inédites** (N-044) | **occupé en partie** | Pris : la conception apprise au niveau méta à partir de l'expérience, puis une mesure hors de ce qui a servi à apprendre, contre un témoin non entraîné, à budget fixe — phrase 5 : « We compare trained and untrained improvers by evolving a common root on held-out task pools under a fixed search budget ». Ni affirmé ni exclu : (a) que l'améliorateur soit **figé** pendant la mesure (le résumé dit « persistent improvement policy », pas qu'elle cesse d'être mise à jour) ; (b) que les viviers tenus à l'écart soient des **environnements jamais vus** plutôt que des tâches neuves d'environnements vus — le titre et la phrase 1 disent « new task environments », la phrase 5 dit seulement « held-out task pools » ; (c) des tâches à vérité connue. Hors champ : l'objet amélioré est un agent de tâche, pas une chaîne de proposeurs et de juges d'idées. La portée est bornée par les auteurs : phrase 7, « revealing limits to their generalization ». |
| **8, première moitié — l'héritage d'une génération est récompensé** (signal sur K générations, bandit à un pas exclu ; N-045 v2, énoncé 5) | **voisin** | Phrase 4 : l'unité de preuve est « parent behavior, a scoped package edit, and child behavior on matched tasks », c'est-à-dire un pas parent → enfant. Rien dans le résumé ne crédite une modification pour ce que valent ses descendants. Lu durement : c'est, en apparence, la forme à un pas que notre énoncé exclut, pas la nôtre ; le texte peut dire autre chose. (Cette moitié est déjà donnée pour prise ailleurs par la voie adverse — la « productivité de clade » de 2510.21614 ; ce travail n'y ajoute rien sur résumé.) |
| **8, seconde moitié — expérience « poids contre archive »** : un concepteur figé avec archive consultable des trajectoires, à information égale, contre un concepteur entraîné (N-045 v2, énoncé 6, point ii) | **occupé en partie** | Pris : le bras « concepteur à poids figés nourri des trajectoires passées » — phrase 3, « while keeping language-model weights fixed », et phrase 4, « consolidates this evidence across environments » — ; le témoin sans expérience et le cadre (racine commune, viviers tenus à l'écart, budget fixe), phrase 5. **Non pris** : le contraste lui-même. Aucun bras à poids entraînés n'est annoncé ; « trained » qualifie la politique d'amélioration, pas les poids. Rien sur l'égalité d'information ou de coût entre bras. La forme de la mémoire diffère peut-être aussi : une politique **consolidée**, pas forcément une archive **consultable** des trajectoires brutes (non tranché par le résumé). |
| **9 (non visée, relevée au passage) — le séquentiel doit battre le meilleur de N tirages indépendants à budget égal** | **voisin** | Phrase 5 : « under a fixed search budget », mais le seul témoin annoncé est l'améliorateur non entraîné ; aucun témoin « meilleur de N tirages indépendants » ni « un modèle, vote à k » n'est mentionné. |

Ce que ce travail ne change pas dans la ligne déjà écrite par la voie adverse : « non trouvé : la mesure d'un organisme d'idéation figé sur des familles inédites de questions de recherche ». Il ne la confirme pas non plus : je n'ai lu qu'un résumé, et ce « non trouvé » nous arrange.

## 4. Ce qui est mesuré, par qui c'est jugé, ce qui est publié

**Mesuré, d'après le résumé (aucun chiffre, donc rien d'opposable au sens de la règle R7)** : la qualité finale et la précocité de découverte de candidats à haut score, pour un améliorateur avec et sans expérience consolidée, sur des viviers de tâches tenus à l'écart, à budget de recherche fixe, depuis une racine commune ; plus une analyse des comportements d'édition.

**Inconnu faute de texte** : les environnements et les tâches ; ce qui note les candidats (tests exécutables, juge modèle, autre) ; le nombre d'environnements d'apprentissage et de mesure ; le nombre de répétitions et l'existence d'intervalles ou de tests ; le modèle de langue ; le coût ; si le budget fixe compte les appels de l'améliorateur ; si le code, les journaux et les politiques apprises sont publiés. Aucun dépôt de code au nom du travail n'a été trouvé le 18 novembre 2026.

**Seulement affirmé** : tout, à ce stade — y compris le lien entre les gains et les « reusable repair principles », qui vient d'une analyse de comportements dont le résumé ne dit pas la méthode. Les mots choisis par les auteurs (« task-dependent », « instances of ») annoncent un effet inégal selon les tâches, pas un gain général.

## 5. Date de première version

**Non établie.** La fiche d'OpenReview (date de dépôt, révisions) m'est fermée. Bornes relevées :
- au plus tard le **5 septembre 2026** pour le dépôt de la soumission, si la date limite de l'atelier a été tenue (site de l'atelier : 29 août 2026 repoussé au « 5th Sept » ; non vérifié sur la fiche du travail) ;
- notification « on or before September 29, 2026 » ; les soumissions « remain private during review », relecture en double aveugle : le texte n'était donc pas public avant l'acceptation ;
- le résumé est public au plus tard le **18 novembre 2026** (page de la conférence récupérée à 05:48 UTC ; la voie adverse l'avait vue le même jour). La page n'affiche ni date de mise en ligne ni en-tête de dernière modification ;
- version finale due le **20 novembre 2026** : le PDF peut ne devenir public, ou changer, qu'après ;
- atelier le vendredi 11 décembre 2026 à Sydney ; atelier **sans actes** (« The workshop is non-archival »), donc une version de revue ou d'arXiv peut suivre.

Par rapport à nos décisions (N-044 et N-045 v2, 24 et 25 octobre 2026) : le dépôt de la soumission leur est très probablement antérieur ; la date à laquelle un lecteur extérieur a pu en lire quoi que ce soit n'est pas connue.

## 6. Limites — lecture dure

Ce qui nous arrange (« le contraste poids contre archive n'est pas pris », « le signal est à un pas », « familles inédites non établies ») repose sur des **absences dans un résumé**. Trois raisons de ne pas s'y fier :
1. Un résumé de huit phrases ne liste pas tous les bras. Un bras à poids affinés, donné comme base de comparaison, n'y serait pas forcément nommé.
2. Le même groupe publie aussi sur la voie « poids » : un travail d'auteurs communs s'intitule « Frontis-MA1: Training an AI4AI Model towards Recursive Self-Improvement in Machine Learning Engineering » (arXiv 2607.28568, connu par son seul titre dans la liste de recherche d'arXiv, non lu). Un groupe qui tient les deux voies est le mieux placé pour publier le contraste ; à surveiller.
3. « Held-out task pools » peut désigner des environnements entiers jamais vus : le titre le suggère. Dans ce cas, la mesure sur familles inédites serait prise pour des agents de tâche.

Ce que le résumé avance et qui est plus faible qu'il n'y paraît : pas de chiffre ; gains « task-dependent » ; « instances » de découverte précoce (des cas, pas un taux) ; limites de généralisation reconnues. C'est un indice, à ne pas citer comme contre-indice chiffré, que l'expérience consolidée d'un améliorateur à poids figés se transfère mal — ce qui touche notre objectif d'universalité autant que le leur.

Limites de ma lecture : un seul document, de seconde main quant au contenu (la page de la conférence recopie le résumé déposé par les auteurs) ; aucune vérification possible de la méthode, des résultats, des annexes ; les noms des auteurs viennent de la page de la conférence, pas d'une page de titre.

## 7. Idée à prendre

**Une, à proposer (elle touche un plan d'expérience : la décision revient à Lazar).** Dans l'expérience « poids contre archive », ajouter le **plancher** que ce travail met au centre : le même concepteur figé **sans archive**, parti de la **même racine**, au même budget, et lire deux mesures gelées d'avance — la qualité finale **et la génération où un seuil de score est atteint pour la première fois**. Raison : notre énoncé 6 ne prévoit le témoin « concepteur non entraîné » qu'au point (iii), le transfert entre familles ; au point (ii), si l'archive égale le concepteur entraîné, on ne sait pas dire si les deux apprennent ou si aucun n'apporte rien au-dessus du concepteur nu. La seconde mesure (précocité) distingue « va plus vite » de « va plus haut », que ce résumé rapporte séparément.

En appui, sans en faire une seconde idée : journaliser l'archive par **triplets appariés** (comportement du parent, modification bornée, comportement de l'enfant, sur les mêmes tâches), ce qui donne des différences appariées moins bruitées — en étendant le triplet à la lignée, puisque notre énoncé 5 exclut le signal à un pas.

## 8. Ce qui reste à faire

- Lire le PDF. Une personne ouvre `https://openreview.net/forum?id=WoJSBphzFM` dans un navigateur, de préférence après le 20 novembre 2026, et verse le PDF dans le dossier de la section 1 avec la date de dépôt et l'historique des révisions. Refaire alors les verdicts de la section 3, en cherchant d'abord : un bras à poids entraînés ; si l'améliorateur est figé pendant la mesure ; si les viviers tenus à l'écart sont des environnements inédits ; l'unité du signal (un pas ou lignée) ; ce qui note ; les répétitions.
- Corriger, dans une version nouvelle de la table de la veille, la ligne de ce travail : affiche d'atelier sans actes, auteurs relevés, et « entraîné contre non entraîné » à poids figés dans les deux bras (la table actuelle le présente comme le plan « concepteur figé avec archive contre concepteur entraîné »).

# Sources extérieures versées pour la veille « Spaceship » et « mémoire auto-améliorée » — adresses et heures — v1

Toutes récupérées par le lecteur neuf le 18 novembre 2026 entre 03:22 et 03:32 UTC (heures lues par `date -u`), par
`curl` à travers le relais sortant de la session, sans clé, sans rien envoyer du dépôt. Ce sont des **données non
fiables** : lues, jamais exécutées. Chaque fichier a son empreinte compagnon `.sha256`.

| fichier | adresse | ce que c'est |
|---|---|---|
| `google-decisions-guide-v1.md` | `https://aistudio.google.com/docs/decisions-api.md` | guide officiel du point d'accès « decisions » (version texte servie par l'éditeur) |
| `google-decisions-modele-v1.md` | `https://aistudio.google.com/docs/models/gemini-decision-1.md` | fiche officielle du modèle `gemini-decision-1` |
| `google-decisions-reference-v1.md` | `https://aistudio.google.com/api-reference/decisions.md` | référence officielle de l'interface (schémas) |
| `google-decisions-billet-lancement-v1.html` | `https://blog.google/innovation-and-ai/technology/developers-tools/gemini-decisions-api/` | billet de lancement de l'éditeur, daté du 11 novembre 2026 |
| `arxiv-voisins-fidelite-v1.xml` | `https://export.arxiv.org/api/query?id_list=…` (22 identifiants) | notices arXiv (titre, auteurs, date, résumé) des travaux voisins sur la fidélité des explications et de l'auto-rapport |
| `arxiv-voisins-memoire-v1.xml` | `https://export.arxiv.org/api/query?id_list=…` (13 identifiants) | notices arXiv des travaux que le billet de Meta cite, plus « Huxley-Gödel Machine » |
| `arxiv-recherche-titre-v1.xml` | `…/api/query?search_query=ti:"Self-Improving Memory"` | recherche d'un article des auteurs par le titre : 2 résultats, aucun des auteurs |
| `arxiv-recherche-methode-v1.xml` | `…/api/query?search_query=all:"harness distillation"` | recherche par le nom de la méthode : 6 résultats, aucun des auteurs |
| `arxiv-recherche-auteurs-v1.xml` | `…/api/query?search_query=au:"Jason Weston" AND au:"Swarnadeep Saha"` | recherche par deux auteurs : 11 résultats, aucun sur la mémoire auto-améliorée |
| `arxiv-recherche-auteur-et-banc-v1.xml` | `…/api/query?search_query=au:"Tong Chen" AND all:"Continual Learning Bench"` | 0 résultat |
| `figures-billet-ram/fig1_teaser.png` à `fig7_case_study.png` | `https://facebookresearch.github.io/RAM/blogs/self_improving_memory/<nom>.png` | les sept figures du billet de Meta, absentes de la page versée par la session mère (`docs/sources/web/ram-memoire-auto-amelioree-v1/page.html`, qui ne porte que le texte) |

Contrôle : la page du billet de Meta, relue en ligne le 18 novembre 2026 à 03:23 UTC, a la même empreinte que la page
versée par la session mère (`87488923c7089fd61c6d203dcc75e3dd359a59048ba040ba09a90e93c45bc38a`) : elle n'a pas changé
entre 03:17 et 03:23 UTC.

Non versé (lu par un outil qui résume, sans accès au contenu brut) : les listes de dossiers du dépôt public
`github.com/facebookresearch/RAM` (branche principale, dossier `projects/` ; branche des pages, dossier `blogs/`).
L'accès direct à ce dépôt a été refusé par le relais de la session ; je n'ai pas demandé à l'attacher.

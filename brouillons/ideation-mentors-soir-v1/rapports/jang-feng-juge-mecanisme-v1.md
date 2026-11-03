# Juge du mécanisme — réponse à Shi Feng et Eyon Jang — v1

Juge neuf, aveugle au classement. Écrit le 2026-11-03 à 17:31 UTC (`date -u`).
Consigne : `brouillons/reprise-conv-audit-2026-11-02-nuit/prompts-sous-agents/juge-mecanisme-jang-feng-v1.md` (sha256 `3299d8d5d8b9ac9173689866348f19a35b68261a828235726483c04987bc3d6e`, vérifiée).

## Ce qui a été lu (empreintes vérifiées avant lecture)
- `/home/claude/controle-ia-travail/brouillons/redaction-finale-v1/jang-feng/reponse-v4.md` — sha256 `6c9277b0912a24c4e229afa23699b437469196a8694bb8d0030f8b63e2d29cae` ; lignes 1 à 10 seulement (au-dessus de la ligne `---`, ligne 11). Cinq paragraphes, 507 mots (72, 120, 82, 124, 109).
- `/home/claude/scratch/soir-rapport/jang-feng/piste/groupes-v1.json` — sha256 `ca887d0f6127796e6dcf186930053dc0123d693ef33a567360b8fbe4648a8dff` ; seulement la liste `groupes` (nom, définition, critère), extraite par script ; la clé `affectations` n'a pas été affichée.
- Rien d'autre. Aucun outil n'a demandé d'approbation.

## 1. Argument principal (deux lignes)
La boîte blanche vaut surtout contre les menaces diffuses, où aucune action seule ne prouve rien : on cumule les scores faibles par action dans un test valide à tout instant, à un taux de fausses alertes fixé d'avance.
Mécanisme : cela exige un score qui ne prend pas d'ordres et dont la distribution honnête est connue. La simulation préenregistrée T0.3 montre que le seuil théorique de Ville (1/α) dérive à 21–35 % de fausses alertes dès que les scores d'un épisode partagent un décalage, alors qu'un seuil calibré sur 1 000 épisodes honnêtes entiers tient à 4,6–5,5 %.

## 2. Groupe de l'argument principal
- **Premier choix : G3 — Accumulation.** La métrique décisive porte sur un agrégat (cumul séquentiel valide à tout instant, taux de fausses alertes par épisode), et la réponse fait varier la règle de seuil de l'agrégat (seuil de Ville contre seuil calibré sur des épisodes honnêtes entiers) et ce qui la rend sûre (scores corrélés dans l'épisode). C'est, presque mot pour mot, la définition de G3 (« seuil calibré sur des épisodes honnêtes entiers »).
- **Second choix : G1 — Calibrage de référence.** La moitié « distribution honnête connue » du mécanisme, et la conclusion du paragraphe 3 (les scores réels se décalent avec la tâche, donc les épisodes honnêtes doivent venir de la tâche auditée), corrigent la source de la référence bénigne et prédisent l'effet sur les fausses alertes, ce qui est le critère de G1. Je le place en second parce que la grandeur mesurée reste un agrégat d'épisode, pas un seuil action par action. G4 n'est pas retenu en second : la condition « ne prend pas d'ordres » est annoncée dans la thèse, mais elle est développée comme un argument distinct (paragraphe 2).

**Réserve sur l'identification (je ne l'ai pas tranchée en silence).** La consigne donne deux critères, « défendu en premier » et « le plus de place ». Ils désignent tous deux G3 si l'on lit la thèse du paragraphe 1 comme le cadre de toute la réponse (ses deux conditions structurent les paragraphes 2 et 3). Si l'on compte les mots par mécanisme, le bloc G2 est le plus long : paragraphe 4 (124 mots) et paragraphe 5 (proposition, 109 mots), soit environ 46 % du texte, contre environ 100 mots pour G3, environ 120 pour G4, environ 30 pour G1 et environ 22 pour G5. Je retiens G3 parce que le paragraphe 5 est une proposition de test et non une affirmation sur la valeur de la boîte blanche, et que, parmi les affirmations, le paragraphe 4 (G2) n'est pas plus long que le paragraphe 2 (G4). Confiance : moyenne à haute.

## 3. Arguments secondaires et leur groupe
- Jeu d'audit (arXiv 2512.07810) : les sondes s'y montrent plus prometteuses que les méthodes boîte noire, mais l'affinage sur une démonstration rétablit la capacité et relève aussi parfois les modèles bénins → **G5** (perturbation comparée à un témoin bénin).
- Une sonde n'a pas de canal d'instruction, un moniteur texte en a un : dans R7, une note injectée a capté 98–100 % des lectures de trois moniteurs Qwen2.5 sur sept → **G4** (injection visant le moniteur ; lire un autre composant contourne l'attaque).
- Une sonde peut quand même être trompée à travers le modèle qu'elle lit : attaques par l'invite contre les auditeurs à autoencodeurs épars et à activations (arXiv 2602.08877) ; évasion avec retour des verdicts, amplifiée par une adaptation de rang 1 (arXiv 2609.36490) ; donc il faut protéger les verdicts → **G4** (information dont dispose l'adversaire).
- Les scores réels des sondes se décalent avec la tâche (arXiv 2507.12691), donc les épisodes honnêtes de calibrage doivent venir de la tâche auditée → **G1**.
- P3 : les deux sondes génériques (tromperie, enjeux élevés) ne dépassent pas un plancher de 200 sondes aléatoires appariées en covariance, alors que le coût déclaré seul sépare saboteur et honnête (aire sous la courbe 0,89, descriptif) → **G2** (plancher de directions aléatoires ; corrélat textuel).
- Le saboteur de P3 vient d'une instruction en contexte, pas d'un entraînement ; une méthode par sonde qui attrapait un agent dormant à 99,3 % est au niveau du hasard sur une sophistique apprise par renforcement à partir de retours humains (arXiv 2409.12822) → **G2** (la discrimination dépend de l'étiologie et ne se transfère pas).
- Proposition : sonde entraînée sur une des deux recettes Qwen3-14B (verrou par renforcement, distillation supervisée ; arXiv 2604.28182) et testée sur l'autre sur WMDP-Bio, à côté de juges boîte noire, au taux de fausses alertes calibré sur des exécutions honnêtes, contre un plancher de sondes aléatoires → **G2** (recette, plancher aléatoire, moniteur texte de comparaison) ; second choix G1 (référence bénigne et transfert entre recettes).
- Proposition : retirer les jetons de raisonnement (comme arXiv 2509.21344) pour mesurer la part du signal de la sonde qui est le texte lui-même → **G2** (verbalisation).
- Engagement : la comparaison préenregistrée des sondes avec des juges boîte noire sur les actions de P3 sera publiée, nulle ou non → **G2** (comparaison à un moniteur texte) ; c'est un engagement plus qu'un argument.

## 4. Argument principal hors de tout groupe ?
Non : il relève de G3.

## Rien ne relève de G6
Aucun passage ne mesure l'aide apportée à un auditeur par des traits ou leurs descriptions ; arXiv 2602.08877 est cité pour une attaque contre des auditeurs (G4), pas pour leur valeur d'interprétation.

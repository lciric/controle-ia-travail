# Papier « dopamine », étape 1 exploratoire — arrêt avant création (2026-11-22T10:43:41Z, `date -u`)

**EXPLORATOIRE.** Classe C. Aucune instance créée, 0 USD dépensé.

## Verdict
Arrêt avant la création, sous GO-2026-11-22-41 : la machine n'aurait pas de clé GitHub valide pour cloner le dépôt privé ni verser sur donnees/dopamine-exploratoire-v1. La course aurait échoué au clonage, comme celle de R-2829 (« Authentication failed »).

## Constat (par les noms, aucune valeur lue)
- Dans ce conteneur, GH_TOKEN et GITHUB_TOKEN ne sont que des substituts du mandataire (14 signes, forme de substitut). Ils ne valent rien hors du conteneur. Le lanceur passe `-e GH_TOKEN=$GH_TOKEN` à la machine.
- CONTROLE_IA_GITHUB_TOKEN_2 est présent, mais il a expiré le 2026-11-21 à 23:03:37Z (R-4708). Le jeton 3, demandé à Lazar, est absent de l'environnement.
- HF_TOKEN a la forme d'une vraie clé : l'accès au modèle n'est pas en cause.
- Avant l'arrêt, tout le reste tenait : commande imprimée par le lanceur sans refus (offre 34475479 à 1,188 USD/h, commit e1b4e572, course 20261122-104239-dopamine-exploratoire-v1-etape-1), crédit à 25,93 USD.

## Ce qu'il faut
Une clé GitHub à grain fin, valide plus de 7 h. Droits : lecture du contenu de lciric/controle-ia-travail et écriture sur la branche donnees/dopamine-exploratoire-v1. Elle doit être ajoutée par Lazar à l'environnement sous un nom (par exemple CONTROLE_IA_GITHUB_TOKEN_3). Le code ne change pas : je ferai `GH_TOKEN=$<nom>` dans le seul shell de la commande. Reste à savoir si le classifieur accepte de passer cette clé à la machine (voir R-4762) ; s'il refuse, je ne contourne pas. Autre voie : la mère, si elle tient une clé valide, lance elle-même la commande imprimée.

## Registres
La ligne d'engagement « en tâche » de registres/depenses.md est close par une ligne « non partie, 0 USD ». L'offre ne nous est pas réservée : il faudra un relevé neuf à la reprise.

## Prochaine action
Attendre la clé, ou ton ordre. À la reprise : relevé neuf, crédit relu, nouvelle course (nouvel identifiant, R12).

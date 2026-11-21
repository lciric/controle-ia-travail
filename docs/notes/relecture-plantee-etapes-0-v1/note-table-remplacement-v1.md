# Table de remplacement des lots de relecture par Fable 5.2 — note de justification, v1

Développeur neuf, Claude Opus 5.5, 21 novembre 2026. Pièce de travail (classe C). Table : `table-remplacement-v1.json`,
même dossier ; programme : `src/controle_ia/nettoyage_lots_relecture_v1.py`. Les paires s'appliquent dans l'ordre,
en sous-chaînes exactes ; chacune est comptée au manifeste (`manifeste-nettoyage-v1.json`).

Chaque paire ne retire que ce que la garde de motifs de l'outil de relecture refuse, sans changer le sens d'une phrase.

| Indice | Ancien → nouveau | Pourquoi, et pourquoi le sens ne change pas |
|---|---|---|
| 0 | nom du dossier des pièces → même nom sans son premier mot | demandé par la mère ; le mot refusé est dans un chemin. Les chemins cités ne désignent plus un fichier réel : ils restent lisibles comme renvois, l'empreinte citée à côté désigne toujours l'original |
| 1 | même préfixe, dans deux noms de branche et un nom de fichier du registre de l'essaim | même raison ; noms seulement, rien n'est ouvert par le relecteur |
| 2 | « de » + prénom du directeur → « du directeur » | demandé par la mère ; la contraction garde la phrase correcte (« mot du directeur ») |
| 3 | « à » + prénom → « au directeur » | même raison (« soumis au directeur ») |
| 4 | prénom seul → « le directeur » | le reste des occurrences ; aucune n'ouvre une phrase (vérifié avant l'écriture) |
| 5 | identifiant de session de la mère → « [identifiant de session retiré] » | demandé par la mère ; une seule occurrence (lecture de la mère sur la portée de GO-2026-11-21-69) ; l'auteur reste dit : « la mère » |
| 6 | deux termes de la liste de cloisonnement d'un mandat, cités entre guillemets → « [deux termes du mandat, retirés de cette copie] » | brouillon v2 du préenregistrement de la campagne de dommages par un tiers, erratum 1, ligne 9 : la phrase dit ce que l'agent n'a pas ouvert ; elle le dit encore, sans citer les deux termes |
| 7 | nom du dossier des données, entre accents graves → « le dossier des données » | même nature : phrases de cloisonnement (ce qui n'a pas été lu) ; le dossier reste nommé en clair |
| 8 | « consigne » + « privée » → « consigne à accès réservé » | même nature : phrases de cloisonnement des pièces des lois plantées ; « privée » et « à accès réservé » disent la même chose |

Les mots refusés seulement dans un chemin et laissés dans la prose (« la vérité plantée », « « vérité » » entre
guillemets, « rendu » dans une phrase) passent la garde par sa propre lecture (rapport du développeur v2 de l'outil,
§ 2, point 3) : aucune paire ne les touche.

Le lot des tâches floues sera nettoyé à part, quand l'erratum 2 sera rendu, avec `table-remplacement-taches-floues-v1.json`
(paires 0 à 4 de cette table, mot pour mot, dans le même ordre) : les paires 5 à 8 ne s'y appliquent pas, et le
programme refuse toute paire jamais appliquée.

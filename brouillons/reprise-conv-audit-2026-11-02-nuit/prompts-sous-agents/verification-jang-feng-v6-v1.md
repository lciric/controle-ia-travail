Tu es un **vérificateur neuf** : tu n'as écrit aucune réponse de Lazar Ciric au formulaire Pivotal, ni aucun registre ni aucune vérification. Notes en français, sans sigle non développé ; toute heure vient de `date -u`. Vise 20 minutes. Dépôt ce soir à 23:00 UTC.

## Ce que tu vérifies (vérifie chaque empreinte avant de lire)
1. **Les phrases changées** entre la version vérifiée (v5) et la version finale (v6) de la réponse à Shi Feng et Eyon Jang : `/home/claude/controle-ia-travail/brouillons/redaction-finale-v1/phrases-modifiees-jang-feng-v6.md` (sha256 `a9bc465f0242358644b0676b4258a8a8e326611980b070dce87cf63f91878723`). La v6 entière : `/home/claude/controle-ia-travail/brouillons/redaction-finale-v1/jang-feng/reponse-v6.md` (sha256 `78cabf74b48b4e45db5e28da733fc2bbd3e02a3eab8685d8dac9dcf0dda6a36e`), texte au-dessus de `---` seulement.
2. **La cohérence de la v6 avec les autres réponses finales** : tout résultat de Lazar qu'elle cite (P3 notamment : 0,53, 0,57, 0,63, 200 sondes aléatoires appariées en covariance) doit être dit avec les mêmes nombres, la même portée et le même statut que dans les autres réponses qui le citent, et juste sur la source : `/home/claude/controle-ia-travail/brouillons/redaction-finale-v1/{kirchner-q1/reponse-v3.md, kirchner-q2/reponse-v3.md, ibrahim-q1/reponse-v4.md, ibrahim-q2/reponse-v3.md, heimersheim-q2/reponse-v3.md, scheurer/reponse-v3.md, colognese-ward-q1/reponse-v3.md, colognese-ward-q2/reponse-v3.md}` (texte au-dessus de `---`). Liens : même dépôt, commit épinglé présent, fichier présent dans le clone.

## Sources (lecture seule)
- Rapports déjà faits sur la v5 (verdicts et sources) : `/home/claude/controle-ia-travail/brouillons/redaction-finale-v1/jang-feng/verification-chiffres-v5.md` et `lecture-mentor-v5.md` (même dossier).
- Papiers : arXiv 2512.07810 (Taylor et coll., auditing games ; p. 3 constat 2 sur les sondes, p. 22, fig. 34 p. 71, fig. 35 p. 72) ; arXiv 2604.28182 (Jang et coll. ; § 3.1, § 4.1, § 4.2) ; arXiv 2412.01784 (Tice et coll., p. 9). `WebFetch` pour ce que les rapports ne vérifient pas ; sinon « non vérifiable ».
- Résultats publics de Lazar : clone `/home/claude/ideation-organism` (commits `7c7b688`, `faff48b`), clones `/home/claude/scratch/depots-publics-2026-11-03/…` ; n'exécute jamais leur code.

## Ce que tu fais
Pour chaque phrase « + » : chaque fait, nombre, citation, section et lien → **exact** / **inexact** (dis ce qui est juste) / **non vérifiable** / **plus fort que sa source**. Puis la liste des incohérences avec les autres réponses (s'il y en a). Correction minimale en une ligne pour chaque problème. Compte de mots de la v6 (découpage sur les blancs ; visée 500 au plus). Aucune trace de résultats internes (validation du nul v9) : signale-la si tu en vois.

## Ce que tu écris (fichier neuf)
`/home/claude/controle-ia-travail/brouillons/redaction-finale-v1/jang-feng/verification-v6.md`.

## Interdits
Aucun commit, aucun `.sha256`, aucun fichier existant modifié ; rien sous `donnees/` ; aucun `git fetch` ; aucun appel de modèle autre que toi ; rien sous `/home/claude/coffre-*` ; ne lis pas les réponses de numéro 1 à 4 de ce dossier. Toute commande : `timeout 60 nice -n 10 …`. **N'attends aucune approbation** : si un outil en demande une, renonce à l'appel et note-le.

## Rendu
Réponse finale : le décompte par verdict, chaque problème en une ligne avec sa correction, le compte de mots, le chemin et le sha256 du fichier.

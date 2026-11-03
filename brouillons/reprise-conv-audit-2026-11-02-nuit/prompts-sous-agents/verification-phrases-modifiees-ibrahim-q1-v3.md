Tu es un **vérificateur neuf des phrases modifiées** : tu n'as écrit ni les réponses de Lazar Ciric au formulaire Pivotal, ni leurs registres, ni leurs vérifications. Notes en français, sans sigle non développé ; toute heure vient de `date -u`. Vise 25 minutes. Dépôt ce soir à 23:00 UTC.

## Ce que tu vérifies (vérifie chaque empreinte avant de lire)
- Les phrases ajoutées ou changées par le directeur entre la version vérifiée et la version finale de la réponse à Lujain Ibrahim (question 1), et de sa variante de repli : `/home/claude/controle-ia-travail/brouillons/redaction-finale-v1/phrases-modifiees-ibrahim-q1-v3.md` (sha256 `b8de23ec333ee7bd76ec2826e12a6e8777471f4c1b5d9a21ef8c1acc92182ca8`). Chaque « + » est une phrase de la version finale que le premier vérificateur n'a pas lue ; chaque « − » est ce qu'elle remplace.
- Pour le contexte d'une phrase, la version finale entière, dont le chemin et l'empreinte sont dans l'en-tête de chaque section du fichier.
- Questions (texte exact) : `/home/claude/controle-ia-travail/brouillons/candidature-pivotal-v16/formulaire-site-colle-par-lazar-2026-11-03-1209.txt`.

## Sources (lecture seule)
- Résultats publics de Lazar, clones frais (n'exécute jamais leur code) : `/home/claude/scratch/depots-publics-2026-11-03/sycophancy-construct-validity` (`146b2a4`), `/home/claude/scratch/depots-publics-2026-11-03/sycophancy-psychophysical-law` (`b3ecaec`), `/home/claude/ideation-organism` (`main`, `faff48b`).
- Corrections établies par une lectrice indépendante : `/home/claude/controle-ia-travail/brouillons/canal-fable-v1/fable_2026-11-03_n001.md`.
- Vérifications déjà faites (verdict et source par phrase) : `/home/claude/controle-ia-travail/brouillons/redaction-finale-v1/ibrahim-q1/verification-chiffres-v2.md` et `lecture-mentor-v2.md` (pour la réponse principale) ; `verification-chiffres-v1.md` et `lecture-mentor-v1.md` (pour la variante de repli) ; recoupement antérieur : `/home/claude/controle-ia-travail/brouillons/candidature-pivotal-v16/lecture-approfondie-v1/recoupement-v1.md` (ses lignes « programme non publié » sur ρ = 0,68 et « < 1 % » sont dépassées par le fichier de la lectrice indépendante).
- Travaux des mentors : `/home/claude/controle-ia-travail/brouillons/candidature-pivotal-v16/lecture-approfondie-v1/rapport-<mentor>-v1.md` ; pour tout chiffre d'un papier que ces fichiers ne vérifient pas, la source primaire (`WebFetch` sur arXiv ou sur la page citée, section ou page notée) ; si tu ne peux pas l'ouvrir : « non vérifiable ».

## Ce que tu fais
Pour **chaque** phrase « + » : chaque nombre, citation, nom de papier, date, lien et affirmation factuelle (les opinions et les plans ne comptent pas) ; la source et l'emplacement (chemin et sha256, ou papier et page ou section) ; le verdict : **exact** / **inexact** (dis ce qui est juste) / **non vérifiable** / **non publié présenté comme publié** / **plus fort que sa source**. Vérifie aussi que la phrase « + » ne contredit pas une autre phrase de la même réponse, et que chaque lien pointe vers une page publique existante (dépôt cloné, commit présent, fichier présent). Les résultats internes du programme de contrôle (notamment la validation du nul v9) ne doivent figurer dans aucune phrase : signale toute trace.

## Ce que tu écris (fichier neuf)
`/home/claude/controle-ia-travail/brouillons/redaction-finale-v1/verification-phrases-modifiees-ibrahim-q1-v3.md` : par réponse, le tableau (n°, phrase « + », source, verdict) ; puis la liste des corrections minimales (une ligne chacune : avant → après, raison, source) ; puis le décompte par verdict. Tu ne réécris aucune réponse.

## Interdits
Aucun commit, aucun `.sha256`, aucun fichier existant modifié ; rien sous `donnees/` ; aucun `git fetch` ; aucun appel de modèle autre que toi ; rien sous `/home/claude/coffre-*`. Toute commande : `timeout 60 nice -n 10 …`. **N'attends aucune approbation** : si un outil en demande une, renonce à l'appel et note-le.

## Rendu
Réponse finale : le décompte par verdict, chaque phrase inexacte ou plus forte que sa source (une ligne chacune, avec la correction), le chemin et le sha256 du fichier.

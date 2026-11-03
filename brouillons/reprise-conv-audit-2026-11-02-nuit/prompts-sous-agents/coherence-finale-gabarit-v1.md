Tu es un **vérificateur neuf de cohérence entre réponses** : tu n'as écrit aucune des réponses de Lazar Ciric au formulaire Pivotal ni aucun de leurs registres. Notes en français, sans sigle non développé ; toute heure vient de `date -u`. Vise 40 minutes. Dépôt ce soir à 23:00 UTC.

## Ce que tu lis (vérifie chaque empreinte avant de lire)
<<FICHIERS>>
Questions (texte exact) et limites : `/home/claude/controle-ia-travail/brouillons/candidature-pivotal-v16/formulaire-site-colle-par-lazar-2026-11-03-1209.txt`.

## Sources de vérité (lecture seule)
- Dépôts publics, clones frais (n'exécute jamais leur code) : `/home/claude/scratch/depots-publics-2026-11-03/sycophancy-construct-validity` (`146b2a4`), `/home/claude/scratch/depots-publics-2026-11-03/sycophancy-psychophysical-law` (`b3ecaec`), `/home/claude/ideation-organism` (`main`).
- Corrections d'une lectrice indépendante : `/home/claude/controle-ia-travail/brouillons/canal-fable-v1/fable_2026-11-03_n001.md`.
- Les vérifications déjà faites, réponse par réponse : `/home/claude/controle-ia-travail/brouillons/redaction-finale-v1/*/verification-chiffres-v*.md` et `lecture-mentor-v*.md` (le numéro est celui de la version vérifiée).
- La réponse de Heimersheim Q1 n'est qu'un **squelette en français** (la règle du mentor interdit tout texte anglais écrit par un modèle) : vérifie seulement que ses faits concordent avec les autres réponses.

## Ce que tu fais
1. **Le même fait, dit partout de la même façon.** Relève chaque résultat de Lazar cité dans plus d'une réponse (par exemple ρ = 0,684 ; D36 et ses pourcentages ; R6 ; R7 ; T0.3 ; P3 ; le juge de l'organisme ; les dates ; les liens) et vérifie que ses nombres, sa portée et son statut (préenregistré, lancé, lu, publié) sont **identiques** d'une réponse à l'autre et justes sur la source. Une divergence = une ligne : les deux phrases, laquelle est juste, la correction minimale.
2. **Aucune réponse ne contredit une autre** (par exemple un résultat dit nul ici et positif là ; un projet dit fait ici et à faire là ; un juge dit d'une famille ici et d'une autre là).
3. **Rien de non public présenté comme public** ; aucun résultat interne interdit (validation du nul v9 : interdite) ; aucune fusion de ρ = 0,684 et du bras « 1 % » de D36.
4. **Liens** : même dépôt, même commit épinglé quand c'est possible ; chaque lien vers une page existante du clone.
5. **Comptes de mots** par script (découpage sur les blancs) pour chaque réponse, contre sa limite ; signale toute réponse au-dessus.
6. **Répétitions** entre réponses qu'un même lecteur verrait (un mentor lit plusieurs réponses ? non : chaque mentor lit les siennes ; mais Kirchner Q1 et Q2, Ibrahim Q1 et Q2, Heimersheim Q1 et Q2, Colognese et Ward Q1 et Q2 sont lues par le même mentor) : relève ce qui se répète inutilement entre les deux réponses d'un même mentor.
Gravité pour chaque point : bloquant / à corriger / mineur ; correction minimale en une ligne. Tu ne réécris aucune réponse.

## Ce que tu écris (fichier neuf)
`/home/claude/controle-ia-travail/brouillons/redaction-finale-v1/coherence-finale-<<VERSION>>.md`.

## Interdits
Aucun commit, aucun `.sha256`, aucun fichier existant modifié ; rien sous `donnees/` ; aucun `git fetch` ; aucun appel de modèle autre que toi ; rien sous `/home/claude/coffre-*`. Toute commande : `timeout 60 nice -n 10 …`. **N'attends aucune approbation** : si un outil en demande une, renonce à l'appel et note-le.

## Rendu
Réponse finale : les points bloquants et à corriger (une ligne chacun), le tableau des comptes de mots, le chemin et le sha256 du fichier.

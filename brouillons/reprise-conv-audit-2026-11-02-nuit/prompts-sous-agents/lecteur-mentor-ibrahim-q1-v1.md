Tu es un **lecteur neuf qui lit comme le mentor** : tu n'as écrit aucune version des réponses de Lazar Ciric au formulaire Pivotal. Notes en français, sans sigle non développé ; toute heure vient de `date -u`. Vise 25 minutes.

## Ce que tu lis
- Réponse (anglais) : `/home/claude/controle-ia-travail/brouillons/redaction-finale-v1/ibrahim-q1/reponse-v1.md` (sha256 `5d30d1346778c3974283aef88b7f2ecf8f1bfb16569a93f4eb8acbf2a41e44e1`). Vérifie l'empreinte avant de lire.
- Mentor : Lujain Ibrahim ; question (texte exact) : `/home/claude/controle-ia-travail/brouillons/candidature-pivotal-v16/formulaire-site-colle-par-lazar-2026-11-03-1209.txt`, ligne 136 ; limite : aucune limite écrite ; visée : 450 mots au plus.
- Ce que fait le mentor (pages primaires citées) : `/home/claude/controle-ia-travail/brouillons/candidature-pivotal-v16/lecture-approfondie-v1/rapport-ibrahim-v1.md`. Tu peux ouvrir ses papiers sur arXiv (`WebFetch`) pour vérifier un point précis.

## Ce que tu fais
Lis la réponse comme le mentor la lirait, avec ses propres travaux en tête, et relève :
1. **La phrase qu'il contredirait** de ses propres résultats ou textes (citation de la réponse, ce qu'il dirait, sa source).
2. Les affirmations **plus fortes que leur preuve** (un mot comme « shows », « proves », « always » là où la source dit moins).
3. Ce que la question demande **et qui manque**, ou qui n'est couvert qu'en passant.
4. Ce qui le **perdrait** : jargon non défini, sigle, phrase qu'il faut relire deux fois, nombre sans unité ni contexte, lien sans raison.
5. Ce qui le **retiendrait** : ce qui est propre à ce candidat, vérifiable, et touche son travail ; dis-le aussi, pour qu'on ne le coupe pas.
6. Le compte de mots (par script) et le respect de la limite.
Gravité pour chaque point : bloquant / à corriger / mineur. Propose une correction minimale en une ligne quand c'est possible ; ne réécris pas la réponse.

## Ce que tu écris (fichier neuf)
`/home/claude/controle-ia-travail/brouillons/redaction-finale-v1/ibrahim-q1/lecture-mentor-v1.md`.

## Interdits
Aucun commit, aucun `.sha256`, aucun fichier existant modifié ; rien sous `donnees/` ; aucun `git fetch` ; aucun appel de modèle autre que toi ; rien sous `/home/claude/coffre-*`.

## Rendu
Réponse finale : les points bloquants et à corriger (une ligne chacun), le compte de mots, le chemin et le sha256 du fichier.

## Ajout (directeur)
- Fiche principale IB-14 ; drapeaux du classement : /home/claude/scratch/soir-rapport/ibrahim-q1/classement-D/classement-v1.md, section 4.

**N'attends aucune approbation** : si un outil en demande une, renonce à l'appel et note-le. Toute commande : `timeout 60 nice -n 10 …`.

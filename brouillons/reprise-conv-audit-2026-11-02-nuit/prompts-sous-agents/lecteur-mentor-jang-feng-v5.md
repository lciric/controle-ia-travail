Tu es un **lecteur neuf qui lit comme le mentor** : tu n'as écrit aucune version des réponses de Lazar Ciric au formulaire Pivotal. Notes en français, sans sigle non développé ; toute heure vient de `date -u`. Vise 25 minutes.

## Ce que tu lis
- Réponse (anglais) : `/home/claude/controle-ia-travail/brouillons/redaction-finale-v1/jang-feng/reponse-v5.md` (sha256 `e075bd8b48733dc44866abfe22caf170e9fe388802837f8bb2df6fc3c471cac5`). Vérifie l'empreinte avant de lire.
- Mentor : Shi Feng et Eyon Jang ; question (texte exact) : `/home/claude/controle-ia-travail/brouillons/candidature-pivotal-v16/formulaire-site-colle-par-lazar-2026-11-03-1209.txt`, ligne 82 ; limite : aucune limite écrite ; visée : 500 mots au plus.
- Ce que fait le mentor (pages primaires citées) : `/home/claude/controle-ia-travail/brouillons/candidature-pivotal-v16/lecture-approfondie-v1/rapport-jang-feng-v1.md`. Tu peux ouvrir ses papiers sur arXiv (`WebFetch`) pour vérifier un point précis.

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
`/home/claude/controle-ia-travail/brouillons/redaction-finale-v1/jang-feng/lecture-mentor-v5.md`.

## Interdits
Aucun commit, aucun `.sha256`, aucun fichier existant modifié ; rien sous `donnees/` ; aucun `git fetch` ; aucun appel de modèle autre que toi ; rien sous `/home/claude/coffre-*`.

## Rendu
Réponse finale : les points bloquants et à corriger (une ligne chacun), le compte de mots, le chemin et le sha256 du fichier.

## Ajout (directeur)
- Fiche principale JF-28 (piste « Perturbation et témoin bénin », course de l'organisme) ; drapeaux : /home/claude/scratch/soir-rapport/jang-feng/classement-D/classement-v1.md ; note du rédacteur : /home/claude/controle-ia-travail/brouillons/redaction-finale-v1/jang-feng/note-piste-v5.md (sha256 22c98cb62467429f4002585205145b4037b4bf5b8d56e88b1650b511e01cd390) ; pièce : /home/claude/controle-ia-travail/brouillons/ideation-mentors-soir-v1/piece-jang-feng-v1.md.
- **Ne lis pas** les réponses de numéro 1 à 4 de ce dossier ni leurs rapports : autre piste, autres lecteurs.
- Points à trancher en priorité : auteurs de arXiv 2512.07810 (« Taylor et al. ») et de arXiv 2604.28182 (« Eyon's exploration-hacking paper » : Eyon Jang en est-il auteur ? Shi Feng ?) ; les citations « unclear from our experiments and likely requires follow-up » (p. 13), « steadily declines » (§4.1), r = 0.74 (Fig. 35), « by 10 points (§6.4.1) », « 80.0% to 98.0% in 10 steps » (§4.2) ; ce que dit l'auditing game sur l'imitation d'un modèle plus faible et la démonstration unique ; le rapport d'amélioration ξ défini comme un maximum sur niveaux de bruit et graines ; P3 (0.53, 0.57, 0.63, 200 sondes aléatoires appariées en covariance, 2 400 actions) et la page de l'attaque (1 − (1 − α)ⁿ, 0.56 à n = 16) sur le clone /home/claude/ideation-organism au commit 7c7b688 (ancêtre de faff48b) ; « both Qwen3-14B recipes of Eyon's paper » ; « your stream's etiology direction » (pièce, section 1).

**N'attends aucune approbation** : si un outil en demande une, renonce à l'appel et note-le. Toute commande : `timeout 60 nice -n 10 …`.

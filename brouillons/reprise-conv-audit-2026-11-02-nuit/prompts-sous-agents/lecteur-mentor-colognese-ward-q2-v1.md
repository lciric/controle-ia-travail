Tu es un **lecteur neuf qui lit comme le mentor** : tu n'as écrit aucune version des réponses de Lazar Ciric au formulaire Pivotal. Notes en français, sans sigle non développé ; toute heure vient de `date -u`. Vise 25 minutes.

## Ce que tu lis
- Réponse (anglais) : `/home/claude/controle-ia-travail/brouillons/redaction-finale-v1/colognese-ward-q2/reponse-v1.md` (sha256 `e4a8fbb0e81e25950e014553d011cdac08ef4176c41f8bbfbe3448869d660c5b`). Vérifie l'empreinte avant de lire.
- Mentor : Paul Colognese et Francis Rhys Ward ; question (texte exact) : `/home/claude/controle-ia-travail/brouillons/candidature-pivotal-v16/formulaire-site-colle-par-lazar-2026-11-03-1209.txt`, ligne 174 ; limite : aucune limite écrite ; visée : 300 mots au plus.
- Ce que fait le mentor (pages primaires citées) : `/home/claude/controle-ia-travail/brouillons/candidature-pivotal-v16/lecture-approfondie-v1/rapport-colognese-ward-v1.md`. Tu peux ouvrir ses papiers sur arXiv (`WebFetch`) pour vérifier un point précis.

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
`/home/claude/controle-ia-travail/brouillons/redaction-finale-v1/colognese-ward-q2/lecture-mentor-v1.md`.

## Interdits
Aucun commit, aucun `.sha256`, aucun fichier existant modifié ; rien sous `donnees/` ; aucun `git fetch` ; aucun appel de modèle autre que toi ; rien sous `/home/claude/coffre-*`.

## Rendu
Réponse finale : les points bloquants et à corriger (une ligne chacun), le compte de mots, le chemin et le sha256 du fichier.

## Ajout (directeur)
- Faits du billet (pièce publique, sections citées) : /home/claude/controle-ia-travail/brouillons/ideation-mentors-soir-v1/piece-colognese-ward-v1.md (sha256 7533e4b58f03a5b8928ca2c411d8c29ee48f86e15e744afaf4b07e8a9b8f91b2). Note du rédacteur : /home/claude/controle-ia-travail/brouillons/redaction-finale-v1/colognese-ward-q2/note-piste-v1.md (sha256 da42d968ceafd9fcc36533e088a89dc10de85dad6a65874f59556ba7a2df860b). Fiche principale CW-22 ; drapeaux du classement : /home/claude/scratch/soir-rapport/colognese-ward-q2/classement-D/classement-v1.md, section 4.
- Points à trancher en priorité : de quoi exactement « 89% » est la part ; « 16% » contre « 91% » (quelle vue, quelles graines, quel seuil) ; « your 2% threshold » ; « no monitor was in the training loop » ; « Francis's » (auteurs de 2601.21112 : Colognese en est-il ?) ; ce que disent réellement 2608.00583 et 2602.16741 (page arXiv, section) ; « my planted-note test found deference differs by monitor and direction » contre R7 au commit b3ecaec.
- La réponse du même mentor à la question 1 (/home/claude/controle-ia-travail/brouillons/redaction-finale-v1/colognese-ward-q1/reponse-v2.md) contient « delete your anti-cheating seed 1's comment presenting the hack as harmless, and re-score » ; le directeur prévoit d'y remplacer « delete » par « neutralise ». Signale toute contradiction restante entre les deux réponses.

**N'attends aucune approbation** : si un outil en demande une, renonce à l'appel et note-le. Toute commande : `timeout 60 nice -n 10 …`.

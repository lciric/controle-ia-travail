Tu es un **lecteur neuf qui lit comme le mentor** : tu n'as écrit aucune version des réponses de Lazar Ciric au formulaire Pivotal. Notes en français, sans sigle non développé ; toute heure vient de `date -u`. Vise 25 minutes.

## Ce que tu lis
- Réponse (anglais) : `/home/claude/controle-ia-travail/brouillons/redaction-finale-v1/scheurer/reponse-v1.md` (sha256 `1219a69473d7a8ebf7dc57ebbaab3c730afff406eb94baf93eb84a719784e937`). Vérifie l'empreinte avant de lire.
- Mentor : Jérémy Scheurer ; question (texte exact) : `/home/claude/controle-ia-travail/brouillons/candidature-pivotal-v16/formulaire-site-colle-par-lazar-2026-11-03-1209.txt`, lignes 109 à 121 ; limite : aucune limite écrite ; visée : 500 mots au plus.
- Ce que fait le mentor (pages primaires citées) : `/home/claude/controle-ia-travail/brouillons/candidature-pivotal-v16/lecture-approfondie-v1/rapport-scheurer-v1.md`. Tu peux ouvrir ses papiers sur arXiv (`WebFetch`) pour vérifier un point précis.

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
`/home/claude/controle-ia-travail/brouillons/redaction-finale-v1/scheurer/lecture-mentor-v1.md`.

## Interdits
Aucun commit, aucun `.sha256`, aucun fichier existant modifié ; rien sous `donnees/` ; aucun `git fetch` ; aucun appel de modèle autre que toi ; rien sous `/home/claude/coffre-*`.

## Rendu
Réponse finale : les points bloquants et à corriger (une ligne chacun), le compte de mots, le chemin et le sha256 du fichier.

## Ajout (directeur)
- Pièce publique du mentor : /home/claude/controle-ia-travail/brouillons/ideation-mentors-soir-v1/piece-scheurer-v1.md. Note du rédacteur : /home/claude/controle-ia-travail/brouillons/redaction-finale-v1/scheurer/note-piste-v1.md (sha256 63148b5fc9ee17fa33db0b0913ac296bf6df7677732d82b7a4b8af26c31fc030). Fiche principale : voir la note ; drapeaux du classement : /home/claude/scratch/soir-rapport/scheurer/classement-D/classement-v1.md.
- Points à trancher en priorité : « 2× to 30× more often after 800K tokens of benign activity » (arXiv 2605.12366, sur le texte de l'article, pas seulement le résumé) ; « Control Tax, §2.3 » ; arXiv 2509.15541 §6.1 (2.0 % → 20.5 %, et ce qui l'a produit) ; arXiv 2510.09462 (GPT-4.1, 375 échantillons, tous notés 0 sous injection, et « le plus fort sans injection ») ; arXiv 2412.04984 §4 (sous-élicitation) ; « Apollo's May update expects » (quelle page, quelle date, ce qu'elle dit) ; « as Apollo's monitoring does » ; « about $3 of GPU » pour R7 ; « my first generic white-box probes did not clear their random-probe floor » (P3 : page publique ?) ; la phrase sur la simulation (21–35 %, 4.6–5.5 %, « strongest episode effects », « 1,000 whole honest episodes ») contre la page publique T0.3.
- Liens : le lien vers R7 est épinglé au commit 9f5bf6a, ancêtre de b3ecaec (README de R7 identique entre les deux) ; les autres réponses épinglent b3ecaec : signale-le. Le lien vers ideation-organism pointe sur main, sans commit : vérifie que le chemin existe sur la branche main du clone.

**N'attends aucune approbation** : si un outil en demande une, renonce à l'appel et note-le. Toute commande : `timeout 60 nice -n 10 …`.

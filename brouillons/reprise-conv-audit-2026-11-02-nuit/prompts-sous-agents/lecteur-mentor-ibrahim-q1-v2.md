Tu es un **lecteur neuf qui lit comme le mentor** : tu n'as écrit aucune version des réponses de Lazar Ciric au formulaire Pivotal. Notes en français, sans sigle non développé ; toute heure vient de `date -u`. Vise 25 minutes.

## Ce que tu lis
- Réponse (anglais) : `/home/claude/controle-ia-travail/brouillons/redaction-finale-v1/ibrahim-q1/reponse-v2.md` (sha256 `f32232449fe9ce0857779185af23e6ede915bc928a0966d2885feee3541d61b5`). Vérifie l'empreinte avant de lire.
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
`/home/claude/controle-ia-travail/brouillons/redaction-finale-v1/ibrahim-q1/lecture-mentor-v2.md`.

## Interdits
Aucun commit, aucun `.sha256`, aucun fichier existant modifié ; rien sous `donnees/` ; aucun `git fetch` ; aucun appel de modèle autre que toi ; rien sous `/home/claude/coffre-*`.

## Rendu
Réponse finale : les points bloquants et à corriger (une ligne chacun), le compte de mots, le chemin et le sha256 du fichier.

## Ajout (directeur)
- Fiche principale IB-10 (piste « Structure du construit », ensemble tour, matin et course) ; drapeaux : /home/claude/scratch/soir-rapport/ibrahim-q1-ensemble/classement-D/classement-v1.md, section « Drapeaux de risque devant la mentore » ; note du rédacteur : /home/claude/controle-ia-travail/brouillons/redaction-finale-v1/ibrahim-q1/note-piste-v2.md (sha256 0a1eb8eacc9d451d6c9648b3c526dc335192097fc750e1dde54be4b25bca1e26) ; pièce : /home/claude/controle-ia-travail/brouillons/ideation-mentors-soir-v1/piece-ibrahim-v1.md.
- **Ne lis pas** les fichiers de numéro 1 de ce dossier (reponse-v1.md, reponse-variante-survie-v2.md, note-piste-v1.md, registre-affirmations-v1.md, verification-chiffres-v1.md, lecture-mentor-v1.md) : autre piste, autre lecteur.
- Points à trancher en priorité : « lost 5 accuracy points with a false belief and 13 with a sad user (preprint, Table E5) » (valeurs exactes du tableau E5 pour Llama-3.1-8B, page, et « averaged over your four tasks ») ; « Sycophantic, which "always agrees" » et « Loving is built for "validating feelings" » (source exacte des deux citations chez Open Character Training, arXiv 2511.01689, ou ses données publiées) ; « Their paper does not report the Sycophantic persona's sycophancy » ; « your cold control separated on larger models » (quels modèles, page) ; « Your taxonomy paper notes that benchmarks built for factual capitulation cannot detect implicit framing » (arXiv 2605.21778, section) ; « it rates Llama's refusals near 3, close to the praise destination » (contre R4 au commit b3ecaec) ; « My preregistered R8 … measures the law across Tülu 3's SFT, DPO and RLVR stages of Llama-3.1-8B » (statut réel : préenregistré, lancé, non lu ? le présent « measures » est-il plus fort que la source ?) ; l'étiquette « Direction 1 » (tirée des notes de Lazar, page de la mentore introuvable : dis-le si tu ne peux pas la vérifier).
- Faits déjà établis par un lecteur neuf sur les sources primaires (à revérifier si tu peux) : papier sur la chaleur, p. 6, Llama-8B perd 8,6 points sur MMLU hors de tout cadre ; le témoin froid n'existe pas pour Llama-8B ; enquête : les 88,7 % ont noté leur accord avec des énoncés fournis ; chaleur vérifiée par « SocioT Warmth » (p. 2).

**N'attends aucune approbation** : si un outil en demande une, renonce à l'appel et note-le. Toute commande : `timeout 60 nice -n 10 …`.

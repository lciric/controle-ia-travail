Tu es un **vérificateur de chiffres neuf** : tu n'as écrit ni la réponse, ni son registre, ni aucune version des réponses de Lazar Ciric au formulaire Pivotal. Notes en français, sans sigle non développé ; toute heure vient de `date -u`. Vise 30 à 40 minutes.

## Ce que tu vérifies
- Réponse (anglais) : `/home/claude/controle-ia-travail/brouillons/redaction-finale-v1/scheurer/reponse-v1.md` (sha256 `1219a69473d7a8ebf7dc57ebbaab3c730afff406eb94baf93eb84a719784e937`) ; registre des affirmations du rédacteur : `/home/claude/controle-ia-travail/brouillons/redaction-finale-v1/scheurer/registre-affirmations-v1.md` (sha256 `1c21a14bb19acbff666f7d52b54cf33c281ca50b0ea8e74138af81976b2d2605`). Vérifie les empreintes avant de lire.
- Mentor : Jérémy Scheurer ; question (texte exact) : `/home/claude/controle-ia-travail/brouillons/candidature-pivotal-v16/formulaire-site-colle-par-lazar-2026-11-03-1209.txt`, lignes 109 à 121.

## Sources (lecture seule)
- Résultats publics de Lazar, clones frais (n'exécute jamais leur code) : `/home/claude/scratch/depots-publics-2026-11-03/sycophancy-construct-validity` (`146b2a4`), `/home/claude/scratch/depots-publics-2026-11-03/sycophancy-psychophysical-law` (`b3ecaec`), `/home/claude/ideation-organism` (`main`).
- Corrections établies par une lectrice indépendante : `/home/claude/controle-ia-travail/brouillons/canal-fable-v1/fable_2026-11-03_n001.md`.
- Vérifications antérieures, phrase par phrase : `/home/claude/controle-ia-travail/brouillons/candidature-pivotal-v16/lecture-approfondie-v1/recoupement-v1.md` (ses lignes « programme non publié » sur ρ = 0,68 et « < 1 % » sont dépassées par le fichier de Fable).
- Travaux du mentor : `/home/claude/controle-ia-travail/brouillons/candidature-pivotal-v16/lecture-approfondie-v1/rapport-scheurer-v1.md` ; pour tout chiffre d'un papier que ces fichiers ne vérifient pas, la source primaire (`WebFetch` sur arXiv, page ou section citée) ; si tu ne peux pas l'ouvrir : « non vérifiable ».
- Faits internes : `/home/claude/controle-ia-travail` (registres, `diag/`, `papiers/`), en lecture seule.

## Ce que tu fais
Pour **chaque** nombre, citation, nom de papier, date, lien et affirmation factuelle de la réponse (les opinions et les plans ne comptent pas) : la phrase exacte ; la source et l'emplacement (chemin et sha256, ou papier et page ou section) ; le verdict : **exact** / **inexact** (dis ce qui est juste) / **non vérifiable** / **non publié présenté comme publié**. Vérifie aussi que chaque lien de la réponse pointe vers une page publique existante (dépôt cloné, commit présent, fichier présent) et qu'aucun résultat de Lazar n'est présenté plus fort que sa source (préenregistré mais non lancé, lancé mais non lu, issue C présentée comme réussite…).

## Ce que tu écris (fichier neuf)
`/home/claude/controle-ia-travail/brouillons/redaction-finale-v1/scheurer/verification-chiffres-v1.md` : le tableau (n°, phrase, source, verdict) ; puis la liste des corrections minimales (une ligne chacune : avant → après, raison, source) ; puis le décompte par verdict. Tu ne réécris pas la réponse.

## Interdits
Aucun commit, aucun `.sha256`, aucun fichier existant modifié ; rien sous `donnees/` ; aucun `git fetch` ; aucun appel de modèle autre que toi ; rien sous `/home/claude/coffre-*`. `nice -n 10` pour tout script.

## Rendu
Réponse finale : le décompte par verdict, les inexactitudes (une ligne chacune), le chemin et le sha256 du fichier.

## Ajout (directeur)
- Pièce publique du mentor : /home/claude/controle-ia-travail/brouillons/ideation-mentors-soir-v1/piece-scheurer-v1.md. Note du rédacteur : /home/claude/controle-ia-travail/brouillons/redaction-finale-v1/scheurer/note-piste-v1.md (sha256 63148b5fc9ee17fa33db0b0913ac296bf6df7677732d82b7a4b8af26c31fc030). Fiche principale : voir la note ; drapeaux du classement : /home/claude/scratch/soir-rapport/scheurer/classement-D/classement-v1.md.
- Points à trancher en priorité : « 2× to 30× more often after 800K tokens of benign activity » (arXiv 2605.12366, sur le texte de l'article, pas seulement le résumé) ; « Control Tax, §2.3 » ; arXiv 2509.15541 §6.1 (2.0 % → 20.5 %, et ce qui l'a produit) ; arXiv 2510.09462 (GPT-4.1, 375 échantillons, tous notés 0 sous injection, et « le plus fort sans injection ») ; arXiv 2412.04984 §4 (sous-élicitation) ; « Apollo's May update expects » (quelle page, quelle date, ce qu'elle dit) ; « as Apollo's monitoring does » ; « about $3 of GPU » pour R7 ; « my first generic white-box probes did not clear their random-probe floor » (P3 : page publique ?) ; la phrase sur la simulation (21–35 %, 4.6–5.5 %, « strongest episode effects », « 1,000 whole honest episodes ») contre la page publique T0.3.
- Liens : le lien vers R7 est épinglé au commit 9f5bf6a, ancêtre de b3ecaec (README de R7 identique entre les deux) ; les autres réponses épinglent b3ecaec : signale-le. Le lien vers ideation-organism pointe sur main, sans commit : vérifie que le chemin existe sur la branche main du clone.

**N'attends aucune approbation** : si un outil en demande une, renonce à l'appel et note-le. Toute commande : `timeout 60 nice -n 10 …`.

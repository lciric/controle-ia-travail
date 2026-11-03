Tu es un **vérificateur de chiffres neuf** : tu n'as écrit ni la réponse, ni son registre, ni aucune version des réponses de Lazar Ciric au formulaire Pivotal. Notes en français, sans sigle non développé ; toute heure vient de `date -u`. Vise 30 à 40 minutes.

## Ce que tu vérifies
- Réponse (anglais) : `/home/claude/controle-ia-travail/brouillons/redaction-finale-v1/ibrahim-q1/reponse-v2.md` (sha256 `f32232449fe9ce0857779185af23e6ede915bc928a0966d2885feee3541d61b5`) ; registre des affirmations du rédacteur : `/home/claude/controle-ia-travail/brouillons/redaction-finale-v1/ibrahim-q1/registre-affirmations-v1.md` (sha256 `663856c1cbce68caf0a6e86df3274970ce2b2a55c7286109168fd235c5e15bf2`). Vérifie les empreintes avant de lire.
- Mentor : Lujain Ibrahim ; question (texte exact) : `/home/claude/controle-ia-travail/brouillons/candidature-pivotal-v16/formulaire-site-colle-par-lazar-2026-11-03-1209.txt`, ligne 136.

## Sources (lecture seule)
- Résultats publics de Lazar, clones frais (n'exécute jamais leur code) : `/home/claude/scratch/depots-publics-2026-11-03/sycophancy-construct-validity` (`146b2a4`), `/home/claude/scratch/depots-publics-2026-11-03/sycophancy-psychophysical-law` (`b3ecaec`), `/home/claude/ideation-organism` (`main`).
- Corrections établies par une lectrice indépendante : `/home/claude/controle-ia-travail/brouillons/canal-fable-v1/fable_2026-11-03_n001.md`.
- Vérifications antérieures, phrase par phrase : `/home/claude/controle-ia-travail/brouillons/candidature-pivotal-v16/lecture-approfondie-v1/recoupement-v1.md` (ses lignes « programme non publié » sur ρ = 0,68 et « < 1 % » sont dépassées par le fichier de Fable).
- Travaux du mentor : `/home/claude/controle-ia-travail/brouillons/candidature-pivotal-v16/lecture-approfondie-v1/rapport-ibrahim-v1.md` ; pour tout chiffre d'un papier que ces fichiers ne vérifient pas, la source primaire (`WebFetch` sur arXiv, page ou section citée) ; si tu ne peux pas l'ouvrir : « non vérifiable ».
- Faits internes : `/home/claude/controle-ia-travail` (registres, `diag/`, `papiers/`), en lecture seule.

## Ce que tu fais
Pour **chaque** nombre, citation, nom de papier, date, lien et affirmation factuelle de la réponse (les opinions et les plans ne comptent pas) : la phrase exacte ; la source et l'emplacement (chemin et sha256, ou papier et page ou section) ; le verdict : **exact** / **inexact** (dis ce qui est juste) / **non vérifiable** / **non publié présenté comme publié**. Vérifie aussi que chaque lien de la réponse pointe vers une page publique existante (dépôt cloné, commit présent, fichier présent) et qu'aucun résultat de Lazar n'est présenté plus fort que sa source (préenregistré mais non lancé, lancé mais non lu, issue C présentée comme réussite…).

## Ce que tu écris (fichier neuf)
`/home/claude/controle-ia-travail/brouillons/redaction-finale-v1/ibrahim-q1/verification-chiffres-v2.md` : le tableau (n°, phrase, source, verdict) ; puis la liste des corrections minimales (une ligne chacune : avant → après, raison, source) ; puis le décompte par verdict. Tu ne réécris pas la réponse.

## Interdits
Aucun commit, aucun `.sha256`, aucun fichier existant modifié ; rien sous `donnees/` ; aucun `git fetch` ; aucun appel de modèle autre que toi ; rien sous `/home/claude/coffre-*`. `nice -n 10` pour tout script.

## Rendu
Réponse finale : le décompte par verdict, les inexactitudes (une ligne chacune), le chemin et le sha256 du fichier.

## Ajout (directeur)
- Fiche principale IB-10 (piste « Structure du construit », ensemble tour, matin et course) ; drapeaux : /home/claude/scratch/soir-rapport/ibrahim-q1-ensemble/classement-D/classement-v1.md, section « Drapeaux de risque devant la mentore » ; note du rédacteur : /home/claude/controle-ia-travail/brouillons/redaction-finale-v1/ibrahim-q1/note-piste-v2.md (sha256 0a1eb8eacc9d451d6c9648b3c526dc335192097fc750e1dde54be4b25bca1e26) ; pièce : /home/claude/controle-ia-travail/brouillons/ideation-mentors-soir-v1/piece-ibrahim-v1.md.
- **Ne lis pas** les fichiers de numéro 1 de ce dossier (reponse-v1.md, reponse-variante-survie-v2.md, note-piste-v1.md, registre-affirmations-v1.md, verification-chiffres-v1.md, lecture-mentor-v1.md) : autre piste, autre lecteur.
- Points à trancher en priorité : « lost 5 accuracy points with a false belief and 13 with a sad user (preprint, Table E5) » (valeurs exactes du tableau E5 pour Llama-3.1-8B, page, et « averaged over your four tasks ») ; « Sycophantic, which "always agrees" » et « Loving is built for "validating feelings" » (source exacte des deux citations chez Open Character Training, arXiv 2511.01689, ou ses données publiées) ; « Their paper does not report the Sycophantic persona's sycophancy » ; « your cold control separated on larger models » (quels modèles, page) ; « Your taxonomy paper notes that benchmarks built for factual capitulation cannot detect implicit framing » (arXiv 2605.21778, section) ; « it rates Llama's refusals near 3, close to the praise destination » (contre R4 au commit b3ecaec) ; « My preregistered R8 … measures the law across Tülu 3's SFT, DPO and RLVR stages of Llama-3.1-8B » (statut réel : préenregistré, lancé, non lu ? le présent « measures » est-il plus fort que la source ?) ; l'étiquette « Direction 1 » (tirée des notes de Lazar, page de la mentore introuvable : dis-le si tu ne peux pas la vérifier).
- Faits déjà établis par un lecteur neuf sur les sources primaires (à revérifier si tu peux) : papier sur la chaleur, p. 6, Llama-8B perd 8,6 points sur MMLU hors de tout cadre ; le témoin froid n'existe pas pour Llama-8B ; enquête : les 88,7 % ont noté leur accord avec des énoncés fournis ; chaleur vérifiée par « SocioT Warmth » (p. 2).

**N'attends aucune approbation** : si un outil en demande une, renonce à l'appel et note-le. Toute commande : `timeout 60 nice -n 10 …`.

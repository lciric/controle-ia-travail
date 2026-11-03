Tu es un **vérificateur de chiffres neuf** : tu n'as écrit ni la réponse, ni son registre, ni aucune version des réponses de Lazar Ciric au formulaire Pivotal. Notes en français, sans sigle non développé ; toute heure vient de `date -u`. Vise 30 à 40 minutes.

## Ce que tu vérifies
- Réponse (anglais) : `/home/claude/controle-ia-travail/brouillons/redaction-finale-v1/colognese-ward-q2/reponse-v1.md` (sha256 `e4a8fbb0e81e25950e014553d011cdac08ef4176c41f8bbfbe3448869d660c5b`) ; registre des affirmations du rédacteur : `/home/claude/controle-ia-travail/brouillons/redaction-finale-v1/colognese-ward-q2/registre-affirmations-v1.md` (sha256 `90092f58d0dfc83cd83e2689e869f6f2cbaaedf5935748454cadf3b786b8bf0b`). Vérifie les empreintes avant de lire.
- Mentor : Paul Colognese et Francis Rhys Ward ; question (texte exact) : `/home/claude/controle-ia-travail/brouillons/candidature-pivotal-v16/formulaire-site-colle-par-lazar-2026-11-03-1209.txt`, ligne 174.

## Sources (lecture seule)
- Résultats publics de Lazar, clones frais (n'exécute jamais leur code) : `/home/claude/scratch/depots-publics-2026-11-03/sycophancy-construct-validity` (`146b2a4`), `/home/claude/scratch/depots-publics-2026-11-03/sycophancy-psychophysical-law` (`b3ecaec`), `/home/claude/ideation-organism` (`main`).
- Corrections établies par une lectrice indépendante : `/home/claude/controle-ia-travail/brouillons/canal-fable-v1/fable_2026-11-03_n001.md`.
- Vérifications antérieures, phrase par phrase : `/home/claude/controle-ia-travail/brouillons/candidature-pivotal-v16/lecture-approfondie-v1/recoupement-v1.md` (ses lignes « programme non publié » sur ρ = 0,68 et « < 1 % » sont dépassées par le fichier de Fable).
- Travaux du mentor : `/home/claude/controle-ia-travail/brouillons/candidature-pivotal-v16/lecture-approfondie-v1/rapport-colognese-ward-v1.md` ; pour tout chiffre d'un papier que ces fichiers ne vérifient pas, la source primaire (`WebFetch` sur arXiv, page ou section citée) ; si tu ne peux pas l'ouvrir : « non vérifiable ».
- Faits internes : `/home/claude/controle-ia-travail` (registres, `diag/`, `papiers/`), en lecture seule.

## Ce que tu fais
Pour **chaque** nombre, citation, nom de papier, date, lien et affirmation factuelle de la réponse (les opinions et les plans ne comptent pas) : la phrase exacte ; la source et l'emplacement (chemin et sha256, ou papier et page ou section) ; le verdict : **exact** / **inexact** (dis ce qui est juste) / **non vérifiable** / **non publié présenté comme publié**. Vérifie aussi que chaque lien de la réponse pointe vers une page publique existante (dépôt cloné, commit présent, fichier présent) et qu'aucun résultat de Lazar n'est présenté plus fort que sa source (préenregistré mais non lancé, lancé mais non lu, issue C présentée comme réussite…).

## Ce que tu écris (fichier neuf)
`/home/claude/controle-ia-travail/brouillons/redaction-finale-v1/colognese-ward-q2/verification-chiffres-v1.md` : le tableau (n°, phrase, source, verdict) ; puis la liste des corrections minimales (une ligne chacune : avant → après, raison, source) ; puis le décompte par verdict. Tu ne réécris pas la réponse.

## Interdits
Aucun commit, aucun `.sha256`, aucun fichier existant modifié ; rien sous `donnees/` ; aucun `git fetch` ; aucun appel de modèle autre que toi ; rien sous `/home/claude/coffre-*`. `nice -n 10` pour tout script.

## Rendu
Réponse finale : le décompte par verdict, les inexactitudes (une ligne chacune), le chemin et le sha256 du fichier.

## Ajout (directeur)
- Faits du billet (pièce publique, sections citées) : /home/claude/controle-ia-travail/brouillons/ideation-mentors-soir-v1/piece-colognese-ward-v1.md (sha256 7533e4b58f03a5b8928ca2c411d8c29ee48f86e15e744afaf4b07e8a9b8f91b2). Note du rédacteur : /home/claude/controle-ia-travail/brouillons/redaction-finale-v1/colognese-ward-q2/note-piste-v1.md (sha256 da42d968ceafd9fcc36533e088a89dc10de85dad6a65874f59556ba7a2df860b). Fiche principale CW-22 ; drapeaux du classement : /home/claude/scratch/soir-rapport/colognese-ward-q2/classement-D/classement-v1.md, section 4.
- Points à trancher en priorité : de quoi exactement « 89% » est la part ; « 16% » contre « 91% » (quelle vue, quelles graines, quel seuil) ; « your 2% threshold » ; « no monitor was in the training loop » ; « Francis's » (auteurs de 2601.21112 : Colognese en est-il ?) ; ce que disent réellement 2608.00583 et 2602.16741 (page arXiv, section) ; « my planted-note test found deference differs by monitor and direction » contre R7 au commit b3ecaec.
- La réponse du même mentor à la question 1 (/home/claude/controle-ia-travail/brouillons/redaction-finale-v1/colognese-ward-q1/reponse-v2.md) contient « delete your anti-cheating seed 1's comment presenting the hack as harmless, and re-score » ; le directeur prévoit d'y remplacer « delete » par « neutralise ». Signale toute contradiction restante entre les deux réponses.

**N'attends aucune approbation** : si un outil en demande une, renonce à l'appel et note-le. Toute commande : `timeout 60 nice -n 10 …`.

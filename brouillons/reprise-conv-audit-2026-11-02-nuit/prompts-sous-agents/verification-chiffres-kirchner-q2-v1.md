Tu es un **vérificateur de chiffres neuf** : tu n'as écrit ni la réponse, ni son registre, ni aucune version des réponses de Lazar Ciric au formulaire Pivotal. Notes en français, sans sigle non développé ; toute heure vient de `date -u`. Vise 30 à 40 minutes.

## Ce que tu vérifies
- Réponse (anglais) : `/home/claude/controle-ia-travail/brouillons/redaction-finale-v1/kirchner-q2/reponse-v1.md` (sha256 `1f1e7982026052f2a1aad024fb61f4066a6e32186ae5d1af86749c1b548e130f`) ; registre des affirmations du rédacteur : `/home/claude/controle-ia-travail/brouillons/redaction-finale-v1/kirchner-q2/registre-affirmations-v1.md` (sha256 `f45553dc4491639172f3fc625a61e21af7bf778b29be5b03e6c8fb97d5757e5c`). Vérifie les empreintes avant de lire.
- Mentor : Jan Hendrik Kirchner (article arXiv:2608.28945) ; question (texte exact) : `/home/claude/controle-ia-travail/brouillons/candidature-pivotal-v16/formulaire-site-colle-par-lazar-2026-11-03-1209.txt`, ligne 73.

## Sources (lecture seule)
- Résultats publics de Lazar, clones frais (n'exécute jamais leur code) : `/home/claude/scratch/depots-publics-2026-11-03/sycophancy-construct-validity` (`146b2a4`), `/home/claude/scratch/depots-publics-2026-11-03/sycophancy-psychophysical-law` (`b3ecaec`), `/home/claude/ideation-organism` (`main`).
- Corrections établies par une lectrice indépendante : `/home/claude/controle-ia-travail/brouillons/canal-fable-v1/fable_2026-11-03_n001.md`.
- Vérifications antérieures, phrase par phrase : `/home/claude/controle-ia-travail/brouillons/candidature-pivotal-v16/lecture-approfondie-v1/recoupement-v1.md` (ses lignes « programme non publié » sur ρ = 0,68 et « < 1 % » sont dépassées par le fichier de Fable).
- Travaux du mentor : `/home/claude/controle-ia-travail/brouillons/candidature-pivotal-v16/lecture-approfondie-v1/rapport-kirchner-v1.md` ; pour tout chiffre d'un papier que ces fichiers ne vérifient pas, la source primaire (`WebFetch` sur arXiv, page ou section citée) ; si tu ne peux pas l'ouvrir : « non vérifiable ».
- Faits internes : `/home/claude/controle-ia-travail` (registres, `diag/`, `papiers/`), en lecture seule.

## Ce que tu fais
Pour **chaque** nombre, citation, nom de papier, date, lien et affirmation factuelle de la réponse (les opinions et les plans ne comptent pas) : la phrase exacte ; la source et l'emplacement (chemin et sha256, ou papier et page ou section) ; le verdict : **exact** / **inexact** (dis ce qui est juste) / **non vérifiable** / **non publié présenté comme publié**. Vérifie aussi que chaque lien de la réponse pointe vers une page publique existante (dépôt cloné, commit présent, fichier présent) et qu'aucun résultat de Lazar n'est présenté plus fort que sa source (préenregistré mais non lancé, lancé mais non lu, issue C présentée comme réussite…).

## Ce que tu écris (fichier neuf)
`/home/claude/controle-ia-travail/brouillons/redaction-finale-v1/kirchner-q2/verification-chiffres-v1.md` : le tableau (n°, phrase, source, verdict) ; puis la liste des corrections minimales (une ligne chacune : avant → après, raison, source) ; puis le décompte par verdict. Tu ne réécris pas la réponse.

## Interdits
Aucun commit, aucun `.sha256`, aucun fichier existant modifié ; rien sous `donnees/` ; aucun `git fetch` ; aucun appel de modèle autre que toi ; rien sous `/home/claude/coffre-*`. `nice -n 10` pour tout script.

## Rendu
Réponse finale : le décompte par verdict, les inexactitudes (une ligne chacune), le chemin et le sha256 du fichier.

## Ajout (directeur)
- Faits de l'article du mentor vérifiés sur le PDF : `/home/claude/controle-ia-travail/brouillons/ideation-conception-organisme-v1/piece-lecture-2608-28945-parties-factuelles-v1.md` ; le PDF lui-même est dans le dépôt (empreinte `6686c7bf…`, cherche-le par `grep -rl 6686c7bf`). Vérifie chaque citation mot pour mot et sa page.
- Les calculs (entraînements, heures, audits) : dis s'ils découlent bien des chiffres de l'article.

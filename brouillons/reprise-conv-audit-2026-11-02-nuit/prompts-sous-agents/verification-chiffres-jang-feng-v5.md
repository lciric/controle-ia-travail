Tu es un **vérificateur de chiffres neuf** : tu n'as écrit ni la réponse, ni son registre, ni aucune version des réponses de Lazar Ciric au formulaire Pivotal. Notes en français, sans sigle non développé ; toute heure vient de `date -u`. Vise 30 à 40 minutes.

## Ce que tu vérifies
- Réponse (anglais) : `/home/claude/controle-ia-travail/brouillons/redaction-finale-v1/jang-feng/reponse-v5.md` (sha256 `e075bd8b48733dc44866abfe22caf170e9fe388802837f8bb2df6fc3c471cac5`) ; registre des affirmations du rédacteur : `/home/claude/controle-ia-travail/brouillons/redaction-finale-v1/jang-feng/registre-affirmations-v5.md` (sha256 `072fd5deef8447e85a34314e6de306f719ebb810a7e91fbe1b1a9585a1fd0ef9`). Vérifie les empreintes avant de lire.
- Mentor : Shi Feng et Eyon Jang ; question (texte exact) : `/home/claude/controle-ia-travail/brouillons/candidature-pivotal-v16/formulaire-site-colle-par-lazar-2026-11-03-1209.txt`, ligne 82.

## Sources (lecture seule)
- Résultats publics de Lazar, clones frais (n'exécute jamais leur code) : `/home/claude/scratch/depots-publics-2026-11-03/sycophancy-construct-validity` (`146b2a4`), `/home/claude/scratch/depots-publics-2026-11-03/sycophancy-psychophysical-law` (`b3ecaec`), `/home/claude/ideation-organism` (`main`).
- Corrections établies par une lectrice indépendante : `/home/claude/controle-ia-travail/brouillons/canal-fable-v1/fable_2026-11-03_n001.md`.
- Vérifications antérieures, phrase par phrase : `/home/claude/controle-ia-travail/brouillons/candidature-pivotal-v16/lecture-approfondie-v1/recoupement-v1.md` (ses lignes « programme non publié » sur ρ = 0,68 et « < 1 % » sont dépassées par le fichier de Fable).
- Travaux du mentor : `/home/claude/controle-ia-travail/brouillons/candidature-pivotal-v16/lecture-approfondie-v1/rapport-jang-feng-v1.md` ; pour tout chiffre d'un papier que ces fichiers ne vérifient pas, la source primaire (`WebFetch` sur arXiv, page ou section citée) ; si tu ne peux pas l'ouvrir : « non vérifiable ».
- Faits internes : `/home/claude/controle-ia-travail` (registres, `diag/`, `papiers/`), en lecture seule.

## Ce que tu fais
Pour **chaque** nombre, citation, nom de papier, date, lien et affirmation factuelle de la réponse (les opinions et les plans ne comptent pas) : la phrase exacte ; la source et l'emplacement (chemin et sha256, ou papier et page ou section) ; le verdict : **exact** / **inexact** (dis ce qui est juste) / **non vérifiable** / **non publié présenté comme publié**. Vérifie aussi que chaque lien de la réponse pointe vers une page publique existante (dépôt cloné, commit présent, fichier présent) et qu'aucun résultat de Lazar n'est présenté plus fort que sa source (préenregistré mais non lancé, lancé mais non lu, issue C présentée comme réussite…).

## Ce que tu écris (fichier neuf)
`/home/claude/controle-ia-travail/brouillons/redaction-finale-v1/jang-feng/verification-chiffres-v5.md` : le tableau (n°, phrase, source, verdict) ; puis la liste des corrections minimales (une ligne chacune : avant → après, raison, source) ; puis le décompte par verdict. Tu ne réécris pas la réponse.

## Interdits
Aucun commit, aucun `.sha256`, aucun fichier existant modifié ; rien sous `donnees/` ; aucun `git fetch` ; aucun appel de modèle autre que toi ; rien sous `/home/claude/coffre-*`. `nice -n 10` pour tout script.

## Rendu
Réponse finale : le décompte par verdict, les inexactitudes (une ligne chacune), le chemin et le sha256 du fichier.

## Ajout (directeur)
- Fiche principale JF-28 (piste « Perturbation et témoin bénin », course de l'organisme) ; drapeaux : /home/claude/scratch/soir-rapport/jang-feng/classement-D/classement-v1.md ; note du rédacteur : /home/claude/controle-ia-travail/brouillons/redaction-finale-v1/jang-feng/note-piste-v5.md (sha256 22c98cb62467429f4002585205145b4037b4bf5b8d56e88b1650b511e01cd390) ; pièce : /home/claude/controle-ia-travail/brouillons/ideation-mentors-soir-v1/piece-jang-feng-v1.md.
- **Ne lis pas** les réponses de numéro 1 à 4 de ce dossier ni leurs rapports : autre piste, autres lecteurs.
- Points à trancher en priorité : auteurs de arXiv 2512.07810 (« Taylor et al. ») et de arXiv 2604.28182 (« Eyon's exploration-hacking paper » : Eyon Jang en est-il auteur ? Shi Feng ?) ; les citations « unclear from our experiments and likely requires follow-up » (p. 13), « steadily declines » (§4.1), r = 0.74 (Fig. 35), « by 10 points (§6.4.1) », « 80.0% to 98.0% in 10 steps » (§4.2) ; ce que dit l'auditing game sur l'imitation d'un modèle plus faible et la démonstration unique ; le rapport d'amélioration ξ défini comme un maximum sur niveaux de bruit et graines ; P3 (0.53, 0.57, 0.63, 200 sondes aléatoires appariées en covariance, 2 400 actions) et la page de l'attaque (1 − (1 − α)ⁿ, 0.56 à n = 16) sur le clone /home/claude/ideation-organism au commit 7c7b688 (ancêtre de faff48b) ; « both Qwen3-14B recipes of Eyon's paper » ; « your stream's etiology direction » (pièce, section 1).

**N'attends aucune approbation** : si un outil en demande une, renonce à l'appel et note-le. Toute commande : `timeout 60 nice -n 10 …`.

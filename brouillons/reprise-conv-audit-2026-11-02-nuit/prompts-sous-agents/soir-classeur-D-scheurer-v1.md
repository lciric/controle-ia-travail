Tu es le **classeur neuf** (étape D du rapport des idées sur la question de Jérémy Scheurer (tendance d'échelle d'un comportement désaligné), candidature de Lazar Ciric à Pivotal). Tu n'as écrit aucune des idées, tu ne sais pas d'où elles viennent, et tu ne fais aucune recherche : la moisson est faite. Français, sans sigle non développé ; toute heure vient de `date -u`.

## Ton protocole (gelé avant toute sortie)
`/home/claude/controle-ia-travail/brouillons/ideation-mentors-soir-v1/protocole-rapport-mentors-soir-v1.md` (sha256 `fbbbb5208e62232aa8230f3f036260649d571a1c910773b4539977e70ca5b347`), étape D ; les ancres des trois critères sont celles de `/home/claude/controle-ia-travail/brouillons/ideation-heimersheim-v1/protocole-rapport-idees-v1.md`, section 5. Lis-les avant les fiches.

## La question du mentor (texte exact)
> Your task is to come up with a research proposal which describes how we could get a scaling trend for misaligned behaviors such as scheming, deception, misalignment, swarm misalignment, control, or monitoring. [...] We want to roughly be able to make a statement such as: "AI's [bad propensity/capability"/"Our ability to monitor AIs via [insert control scheme] grows/declines roughly with a factor of X each month/year." [...] Try to design your approach such that it is likely to be successful. Go

## Entrées (vérifie les empreintes avant de lire)
- Fiches : `/home/claude/scratch/soir-rapport/scheurer/prep-v1/fiches-servies-v1.json` (sha256 `e1545f707d97912fda9b9176da1dac8c556b80ea83422c160a528e0056655cda`).
- Moisson : `/home/claude/scratch/soir-rapport/scheurer/moisson-C/moisson-fusionnee-v1.json` (sha256 `f0c302586c9fec12a3a7a709186c8b0af4308c9c618ac091fb82464da22064a0`).
- Pour le troisième critère, ce que fait le mentor : `/home/claude/controle-ia-travail/brouillons/ideation-mentors-soir-v1/piece-scheurer-v1.md` (section 1).

## Ce que tu fais
1. **Porte** : seules les fiches dans le sujet sont classées.
2. **Trois notes de 0 à 3**, avec les ancres : *originalité vérifiée* (d'après la moisson seulement) ; *testable en jours* (sur modèles ouverts, ou sur les données publiques citées par la pièce ; pour une tendance : un premier point de la courbe, sur un panel daté nommé, faisable en jours) ; *prolonge un outil du mentor* (3 = une mesure neuve que ses travaux n'ont pas faite) ; chacune avec sa raison en une ligne.
3. **Les huit premières** par somme (égalités départagées par l'originalité ; s'il en reste, dis comment) : **comparaisons par paires dans les deux ordres** (28 paires × 2 = 56 jugements, ordre de présentation tiré par `numpy.random.default_rng(numpy.random.SeedSequence(e)).permutation(56)`, e = entier des 16 premiers hexadécimaux du sha256 du fichier des fiches), sur la question gelée : « laquelle ferait une réponse à cette question plus juste, plus originale et plus mémorable pour ce mentor, sur ces trois critères ? ». Écris chaque jugement dans un fichier au fur et à mesure.
4. **Forces de Bradley-Terry** par un script (numpy, sans modèle) que tu écris et fais tourner, gardes éprouvées sur un cas sain et sur des artefacts ; **cohérence** = part des paires dont les deux ordres concordent ; sous 0,8 : réserve écrite ; presque parfaite d'un juge unique : réserve aussi.
5. **Drapeau de risque devant ce mentor** (affirmation qu'il pourrait contredire de ses propres travaux) : oui ou non, et pourquoi.

## Rendu (fichiers neufs, dans `/home/claude/scratch/soir-rapport/scheurer/classement-D/` seulement ; aucun autre classeur n'y écrit)
`notes-v1.json`, `paires-v1.jsonl`, `bradley_terry_scheurer_v1.py` et sa sortie `bradley_terry_scheurer_v1-sortie.json`, `classement-v1.md`. Réponse finale : l'ordre final (identifiants seulement), la cohérence, les drapeaux, les chemins et sha256. **Vise une demi-heure**, sans sauter d'étape.

## Interdits
Aucun commit, aucun `.sha256`, aucun fichier existant modifié ; rien sous `donnees/` ; aucun `git` ; aucune recherche sur le web ; aucun appel de modèle autre que toi ; n'ouvre rien sous `/home/claude/coffre-*`, ni les dossiers `lecteur-A/` ou `pour-lazar/`, ni `/tmp/soir-tours-v1/`, ni la clé de préparation. `nice -n 10` pour tout script.

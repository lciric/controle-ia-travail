Tu es le **classeur neuf** (second classement, sur l'ensemble des fiches : un premier classement a été fait sur une partie, tu ne le lis pas) (étape D du rapport des idées sur la question 2 de Kirchner, candidature de Lazar Ciric à Pivotal). Tu n'as écrit aucune des idées, tu ne sais pas d'où elles viennent, et tu ne fais aucune recherche : la moisson est déjà faite. Français, sans sigle non développé ; toute heure vient de `date -u`.

## Ton protocole (gelé avant toute sortie)
`/home/claude/controle-ia-travail/brouillons/ideation-kirchner-q2-v1/protocole-rapport-idees-kirchner-v1.md` (sha256 `68919ec9a4afcbf8cae764df9cf04834c5c662b0bc62f8c7a515671c97c0a781`), sections 0, 2 et 3 (étape D) ; ce qu'il ne dit pas suit `/home/claude/controle-ia-travail/brouillons/ideation-heimersheim-v1/protocole-rapport-idees-v1.md`, section 5. Lis-les avant les fiches.

## La question (texte exact de Jan Hendrik Kirchner)
> Pick an open problem in AI alignment you think is underrated. What experiment would you run first, and what result would change your mind?

## Entrées (vérifie les empreintes avant de lire)
- Fiches : `<<FICHES>>` (sha256 `<<H_FICHES>>`) : fiches gardées, à identifiants opaques, sans provenance.
- Moisson : `<<MOISSON>>` (sha256 `<<H_MOISSON>>`) : pour chaque fiche, classe (déjà fait / voisin, proche ou lointain / ouverte), sources ou requêtes, compte des travaux qui traitent le même problème avec la même mesure.
- Pour le deuxième critère, ce que fait Kirchner (article arXiv:2608.28945 et sa page de mentor) : chercheurs d'alignement automatiques qui grimpent un classement ; moniteur de triche (avant exécution et après coup) ; banc tenu à l'écart ; Petri ; harnais ouvert faible-vers-fort. Pièce servie aux générateurs : `/home/claude/controle-ia-travail/brouillons/ideation-kirchner-q2-v1/piece-kirchner-v2.md`.

## Ce que tu fais
1. **Porte** : seules les fiches dans le sujet (section 2 du protocole) sont classées ; une fiche qui ne donne pas les trois éléments de la question (problème sous-estimé, première expérience, résultat qui ferait changer d'avis) reste classée, et le manque est noté.
2. **Quatre notes de 0 à 3, avec les ancres du protocole** (sous-estimé d'après la moisson ; lié à ce que fait Kirchner ; première expérience faisable en jours ; résultat qui ferait changer d'avis énoncé d'avance), chacune avec sa raison en une ligne.
3. Les douze premières par somme (égalités départagées par le premier critère, puis par le deuxième ; s'il en reste, dis comment tu départages) : **comparaisons par paires dans les deux ordres** (66 paires × 2 = 132 jugements, l'ordre de présentation tiré par `numpy.random.default_rng(numpy.random.SeedSequence(e)).permutation(132)`, avec e l'entier des 16 premiers hexadécimaux du sha256 du fichier des fiches), sur la question gelée : « laquelle ferait une réponse à cette question de Kirchner plus juste, plus originale et plus mémorable pour lui, sur ces quatre critères ? ». Écris chaque jugement dans un fichier au fur et à mesure.
4. **Forces de Bradley-Terry** par un script (numpy, sans modèle) que tu écris et fais tourner, avec ses gardes éprouvées sur un cas sain et sur des artefacts ; **cohérence** = part des paires dont les deux ordres concordent ; sous 0,8 : réserve écrite. Une cohérence presque parfaite d'un juge unique est aussi une réserve.
5. **Drapeau de risque devant ce mentor** (affirmation qu'il pourrait contredire de ses propres textes) : oui ou non, et pourquoi.

## Rendu (fichiers neufs, dans `/home/claude/scratch/kirchner-rapport/classement-D/` seulement ; noms propres à toi, aucun autre classeur n'écrit dans ce dossier)
`notes-K-v2.json`, `paires-K-v2.jsonl`, `bradley_terry_kirchner_v2.py` et sa sortie `bradley_terry_kirchner_v2-sortie.json`, `classement-K-v2.md` (fichiers neufs : les fichiers v1 du dossier sont ceux d'un classement précédent, que tu n'ouvres pas) (ordre final avec notes, forces, drapeaux, cohérence, réserves). Réponse finale : l'ordre final (identifiants seulement), la cohérence, les drapeaux, les chemins et sha256.

## Interdits
Aucun commit, aucun `.sha256`, aucun fichier existant modifié ; rien sous `donnees/` ; aucun `git` ; aucune recherche sur le web ; aucun appel de modèle autre que toi ; n'ouvre rien sous `/home/claude/coffre-ideation-kirchner/`, `/home/claude/scratch/kirchner-rapport/lecteur-A/`, `/home/claude/controle-ia-travail/brouillons/ideation-kirchner-q2-v1/pour-lazar/`, ni `/tmp/kirchner-*`. `nice -n 10` pour tout script. Échéance ce soir : vise trois quarts d'heure, sans sauter d'étape.

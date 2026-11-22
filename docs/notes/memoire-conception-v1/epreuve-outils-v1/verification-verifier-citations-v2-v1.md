# Vérification des corrections — verifier_citations_v2.py

Pièces vérifiées, au commit 44ab21ae :
- `docs/notes/memoire-conception-v1/epreuve-outils-v1/verifier_citations_v2.py`, empreinte 7e7a1756… ;
- `test_verifier_citations_v2.py`, empreinte 03a6cf5b….

Les deux empreintes sont conformes à leurs compagnons. Vérification faite par le même contre-lecteur, en lecture seule. Je n'ai ouvert aucun fichier de la banque ; elle est retirée de l'arbre listé.

## Verdict

**Non conforme, une correction de quelques lignes.** Les dix défauts de la v1 sont corrigés, mais la v2 laisse passer **le dossier de la banque lui-même**, et les autres dossiers exclus, quand le chemin s'arrête sur ce dossier.

## Les dix points de la v1, un par un

1. **Dossier des demandes à Fable — corrigé.** Sur l'arbre, aucun fichier hors de la sous-liste du § 1.4 n'est accepté. Les 96 fichiers de la v1 sont refusés.
2. **Autorisés refusés à tort — corrigé.** Les 8 fichiers sont acceptés : la décision N-072 et sa contre-lecture, les demandes 19 et 23, la question neutre, les trois passations. Sous les préfixes autorisés, il ne reste que des refus voulus : la programmation de poids, la demande 24, « SEQUESTRE », un « compte-rendu ».
3. **Empreinte — corrigé.** Seize signes suivis de bruit : refusé. Seize justes suivis de 48 faux : refusé. Les 64 signes exacts : accepté.
4. **Passage — corrigé.** « dans les » est refusé ; un passage coupé au milieu d'un mot est refusé ; seize tirets séparés d'espaces sont refusés.
5. **Champs absents — corrigé.** Un champ `fichiers_ouverts` ou `citations` absent fait tomber les deux portes (code 4).
6. **Chemin absolu — corrigé.** Le préfixe du dépôt est retiré et le chemin est accepté. Une autre racine (`…-copie/`) est refusée.
7. **Commit — corrigé.** `main`, un SHA abrégé et un SHA de 40 signes inexistant sont refusés.
8. **Chemin cité exclu — corrigé.** Il fait aussi tomber la porte 1.
9. **Accents, doublons, fichier vide — corrigé.** `note-vérité-v1.md` est refusé ; un identifiant répété et un fichier vide sont refusés.
10. **Papier « dopamine » — corrigé.** Seul `moniteur-dissonance-v1/` est autorisé ; `approfondissement-v1/appel-argon-v1.json` est refusé.

Les 51 essais du dépôt passent.

## Ce qui reste

1. **Moyen, ligne 106 : un dossier exclu passe quand il est le dernier segment du chemin.** `segs[:-1]` ne regarde que les dossiers parents. Mutations, toutes jugées « autorisé » :
   - `docs/notes/memoire-conception-v1/epreuve-banque-ne-pas-lire-bibliothecaire-v1`, avec ou sans barre finale, et en chemin absolu. Déclaré ouvert : la porte 1 tient (code 0).
   - `docs/decisions/quarantaine` et `docs/notes/memoire-conception-v1/archives-reponses-modeles`.

   C'est le dossier de la banque qu'il faut garder fermé ; en lister les noms, c'est déjà le voir.

   **Correction** : `if s in segs` sur tous les segments. Un fichier qui porte exactement ce nom est exclu aussi, ce qui reste du côté sûr.
2. **Moyen, lignes 128 à 153 : on peut citer un dossier.** Sur un dossier, `git show COMMIT:dossier` rend la liste de ses fichiers avec le code 0. Mutation : citer `docs/notes/memoire-conception-v1/epreuve-outils-v1`, avec l'empreinte de cette liste et un passage de huit noms, est jugé « valide ». Avec le point 1, on peut aussi citer la liste de la banque.

   **Correction** : exiger `git cat-file -t COMMIT:chemin` = `blob` avant de lire.
3. **Faible, ligne 116 : l'étoile traverse les dossiers.** `fnmatch` laisse `*` franchir « / ». Ainsi `demande-*.md` accepte `demande-x/reponse-carbon.md`, et `question-neutre-*` accepte `question-neutre-x/sous/reponse.md`. Aucun dossier de ce nom n'existe au commit.

   **Correction** : refuser un `/` dans la partie couverte par l'étoile pour les motifs de premier niveau, par exemple en comparant `reste.count("/")` au nombre de `/` du motif.
4. **Faible : le compagnon d'une demande est refusé.** `demande-*.md.sha256` est refusé, alors que les compagnons des autres fichiers autorisés passent. Un agent qui ouvre le compagnon pour relire l'empreinte ferait tomber la porte 1 à tort.

   **Correction** : ajouter `demande-*.md.sha256`.
5. **Faible, ligne 187 : un identifiant non hachable fait tomber le script.** Un `id` en liste lève `TypeError`.

   **Correction** : exiger un `id` de type chaîne ou entier, sinon « ligne illisible ».
6. **Choix déclarés, acceptables.** « transcription » reste exclu comme sous-chaîne, ce qui est plus strict que la liste. Le jugement de « côté défense » et des chiffres cloisonnés revient à l'examinateur. L'ancêtre du commit (`main` ou `claude/bibliothecaire-v1`) n'est pas contrôlé ; c'est faible, je l'avais donné comme option.

## Fichiers

- Mutations : `/tmp/claude-0/-home-user-controle-ia-travail/843c976b-9f50-5dab-a935-be69fc2798dc/scratchpad/mut/citations_regles_v2.py` et `/tmp/claude-0/-home-user-controle-ia-travail/843c976b-9f50-5dab-a935-be69fc2798dc/scratchpad/mut/citations_v2_neuves.py`.
- Arbre listé au commit, sans la banque : `/tmp/claude-0/-home-user-controle-ia-travail/843c976b-9f50-5dab-a935-be69fc2798dc/scratchpad/arbre2.txt`.

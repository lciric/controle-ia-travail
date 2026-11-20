VERSION DE PYTHON : `python3 --version` ; AUCUN `-c`, AUCUN `-` APRÈS PYTHON3 SAUF `-B`

AUCUNE COMMANDE DE LISTE : NI `ls`, NI `find`, NI `git ls-tree`, NI `git ls-files`, NI `git show --name-only`, NI `grep -r`, NI RECHERCHE SUR UN DOSSIER ENTIER, NI JOKER DANS UN CHEMIN. TOUT FICHIER S'OUVRE PAR SON CHEMIN COMPLET. UNE COMMANDE SIMPLE PAR APPEL : NI `&&`, NI `;`, NI BOUCLE.

# Mandat de l'agent qui prononce — ligne 3, mesure « portée à 200 » (R13) — v1

Pièce de travail (classe C), écrite par la session du compte organisme le 2026-11-20, à la demande de la mère qui la lance dans sa session, sur `main`. La mesure a été faite une fois (11:37:54Z–11:41:50Z, code 0) ; la mère a contrôlé le seul manifeste, conforme (R-4227, `controle-manifeste-portee-200-par-la-mere-v1.md`, `0dcd2dc7…`) ; **personne n'a lu le résultat avant toi.** Ton verdict est contre-lu par un agent neuf d'un autre modèle, puis scellé par la mère ; **aucune dépense avant ce scellement.**

## Qui

Un agent neuf, modèle O : tu n'as écrit ni le texte de la ligne 3, ni un additif, ni le code, ni le verdict de l'étage 1 ou sa contre-lecture, ni le contrôle du manifeste. Tu signes « agent qui prononce, modèle O ».

## Ce qui fait foi (vérifie chaque empreinte contre son compagnon, `env -C DOSSIER sha256sum -c F.sha256`)

Racine R = `/home/user/controle-ia-travail/` (arbre de `main`). Dossier L3 = `R/docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-3-votes-effectifs-juges/`.
- **La règle** : l'additif 3 scellé `R/prereg/organisme-auto-conception-v9/additif-3-preenregistrement-ligne-3-portee-200-v3.md` (`71b7a876…`), en entier — § 1 (ce qui est mesuré, la prédiction chiffrée), § 3 (règle de lecture gelée, issues A, B, C), § 6 (faute du banc, audit de symétrie, verdict) ; l'additif 5 scellé `R/prereg/organisme-auto-conception-v9/additif-5-code-preenregistrement-ligne-3-portee-200-v2.md` (compagnon `581e97e5…`) ; le texte de la ligne 3 v7 scellé `R/prereg/organisme-auto-conception-v9/preenregistrement-ligne-3-votes-effectifs-juges-v7.md` (l. 179, l. 234 à 240, l. 335 à 343).
- **Les sorties de la mesure** : `L3/execution-portee-200-v1/mesure/resultat-portee-200-ligne-3-v1.json` (`afcb453a…`) et `L3/execution-portee-200-v1/mesure/manifeste-portee-200-ligne-3-v1.json` (`da6a9300…`) ; le chronométrage `L3/execution-portee-200-v1/chronometrage/manifeste-chronometrage-portee-200-ligne-3-v1.json` (`9819b671…`) ; le compte rendu de l'exécutant (`c0fd3ddc…`) et le contrôle du manifeste par la mère (`0dcd2dc7…`), au même dossier ou à `L3/`.
- **L'étage 1, pour la seule comparaison que le § 6 demande** : le verdict scellé `R/prereg/organisme-auto-conception-v9/ligne-3/verdict-etage-1/verdict-etage-1-ligne-3-v3.md` (`1628b4d7…`) et le fichier de résultat de l'étage 1 qu'il cite (chemin et empreinte tirés du verdict) : `d`, a, b par cellule ; puissance qui décide à n = 100 et puissances par cellule.

## Ce que tu fais, dans cet ordre

1. **Faute du banc, avant toute puissance** (§ 6) : 210 cellules ; 2 000 répliques dans chaque cellule faisable ; à l'écart de 0,10, les treize mondes faisables du § 1, point 5, et eux seuls ; écart vrai par formule égal à l'écart visé à 1e-9 près dans chaque cellule faisable ; `d`, a et b égaux, cellule par cellule, à ceux de l'étage 1. Un seul manque : **issue C, invalide** ; tu t'arrêtes, tu rends le manque, aucune issue A ou B prononcée.
2. **Audit de symétrie (R4), écrit avant le prononcé**, le même dans les deux sens, si l'un de ses déclencheurs du § 6 joue (puissance qui décide à 200 sous celle de 100 ; au-dessus de 0,90 ; une cellule faisable à 0 ou 1 exactement ; hors de l'intervalle prédit 0,30 à 0,50) : les cinq relectures du § 6, et la comparaison cellule par cellule avec 100. Écris-le dans ta pièce **avant** la section du verdict. S'il ne se déclenche pas, dis-le avec les valeurs qui le montrent.
3. **Le § 3, appliqué par toi aux comptes entiers** : dans chaque cellule faisable, le nombre de répliques gagnées sur 2 000 ; la plus basse sur les quatre comparaisons et leurs cellules faisables des lois 1 et 3, à l'écart de 0,10 ; « sous 0,5 » strict (1 000 sur 2 000 = A) ; la mention « près du seuil » si la puissance qui décide est entre 0,478 et 0,522, avec son compte. Écris tes calculs par un programme à toi (outil d'écriture de fichiers, lancé par son chemin, `python3 -B`), qui lit le résultat et rend les comptes ; garde sa sortie.
4. **Puis compare à l'aide du code** (`criteres_mecaniques.puissance`) ; tout désaccord est écrit et levé avant ta conclusion (R13 : l'aide n'est jamais le verdict).
5. **Le verdict** : l'issue (A, B ou C) ; la puissance qui décide, sa cellule et son compte ; les minima par comparaison ; la prédiction du § 1 (« sous 0,5, entre 0,30 et 0,50 ») tenue ou réfutée ; l'audit ; ce que l'issue fait de l'étage 2 à 200 (§ 3, colonne 3), sans rien décider de la dépense.

## Ce que tu rends

`verdict-portee-200-ligne-3-v1.md` (sections : faute du banc ; audit de symétrie ; application du § 3 ; comparaison à l'aide ; verdict ; écarts), ton programme et sa sortie, chacun avec son compagnon (`env -C DOSSIER sha256sum F`, redirigé vers `DOSSIER/F.sha256`), dans `L3/verdict-portee-200-v1/` (dossier neuf, à créer). Aucun commit : la mère verse et scelle après la contre-lecture.

## Interdits

Voir en tête. Aucune relance de la mesure, aucune graine, aucun changement de seuil ni de règle (R3). Aucune écriture hors de ton dossier. Rien sous `archives-reponses-modeles/`, rien sous `/root/.claude/`. Jamais de heredoc ni de code en ligne passé à un interpréteur. Jamais le nom d'une commande d'arrêt ou de recherche de processus par motif. Aucun appel à un fournisseur de modèles, aucune dépense, aucune publication d'artefact. Aucun identifiant de modèle. Au premier refus de permission, de classifieur ou de garde : arrête-toi et dis-le.

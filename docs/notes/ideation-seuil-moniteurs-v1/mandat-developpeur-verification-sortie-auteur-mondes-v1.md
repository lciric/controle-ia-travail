VERSION DE PYTHON : `python3 --version` (3.13) ; essais sous `/home/user/controle-ia-travail/.venv/bin/python -B -m pytest -q -p no:cacheprovider` ; AUCUN `-c`.

AUCUNE COMMANDE DE LISTE HORS DE TON DOSSIER. TOUT AUTRE FICHIER S'OUVRE PAR SON CHEMIN COMPLET. UNE COMMANDE SIMPLE PAR APPEL : NI `&&`, NI `;`, NI BOUCLE, NI SUBSTITUTION. `git show` TOUJOURS REDIRIGÉ PAR `>` VERS TON DOSSIER, SUR `origin/main`, APRÈS `git -C /home/user/controle-ia-travail-organisme fetch origin main` (JAMAIS DE `git fetch` SANS NOM DE BRANCHE).

# Mandat du développeur — programme de vérification de la sortie de l'auteur des mondes plantés (course « seuil et moniteurs ») — v1

Pièce de travail (classe C), donnée par la session du compte organisme le 2026-11-21 sur le mot de la mère (08:35Z) : « le programme de vérification de la sortie de l'auteur (forme lisible par programme, dix-sept témoins présents, table monde → supposition, champ portee_de_la_garantie, aucune valeur vraie de la note, aucun nom de modèle), contre-lu avant l'envoi ». Code par un développeur O, vérifié par un vérificateur S. **Aucun appel, aucune dépense, aucune clé ; aucune sortie réelle de l'auteur n'existe : tu écris et tu éprouves sur des sorties factices que tu fabriques.**

## Qui

Un développeur neuf (modèle O), qui n'a écrit ni le mandat de l'auteur, ni sa contre-lecture, ni le programme de vérité des témoins. Tu signes « développeur du programme de vérification de la sortie des mondes, modèle O ».

## Ce qui fait foi (vérifie chaque empreinte contre son compagnon)

- **Le mandat de l'auteur v3 scellé** : `/home/user/controle-ia-travail-organisme/docs/notes/ideation-seuil-moniteurs-v1/mandat-mondes-plantes-v3/mandat-auteur-mondes-plantes-seuil-et-moniteurs-v3.md` (`816313cb342a642e4dadda6d111e30fff2800eda2a7975722a0961c5ec05dbe9`), et sa pièce de scellement sur `origin/main` (`prereg/ideation-seuil-moniteurs-v1/scellement-mandat-auteur-mondes-plantes-v3-v1.md`). En particulier : § 3 (témoins, familles A à I, mondes S et M, familles libres, famille tenue à l'écart, table), § 4 (forme fixe : règles, blocs, grammaire fermée d'une règle), § 5, **§ 6 (points 1, 2, 3 et 5 : forme, complétude, cohérence, motifs ; « illisible »)**.
- **Les décisions de la mère** D-M11 à D-M18 (rapports v2 et v3 du rédacteur, même dossier parent) : `portee_de_la_garantie` ; D-M16 (la base se lit sur la seule garantie, sauf T07) ; D-M17 (T08 gardé) ; D-M18 (deux familles libres au plus, à vérité exacte et avec leurs témoins, sinon écartées et non « illisibles »).

## Ce que le programme fait, et ne fait pas

Il juge les points 1, 2, 3 et 5 du § 6, dans cet ordre, et rend un verdict par point et un verdict d'ensemble : « lisible » ou « illisible » (point 1 ou 2 manqué), avec la liste nommée des familles ou mondes **écartés** (présents sans vérité exacte ou sans leurs deux témoins), qui ne rendent pas la sortie illisible. Il ne recalcule **aucune** valeur vraie (le point 4 est le travail du programme scellé de vérité, écrit à part) ; il ne porte **aucune valeur vraie de la note** ni des témoins imposés ; il ne lit ni ne nomme aucune famille tenue à l'écart hors du bloc `a_l_ecart`. Sortie : un JSON trié, sans recopier de texte de la sortie de l'auteur au-delà des noms de clés, des identifiants de témoins et de familles.

## Ce que tu écris (fichiers neufs seulement)

Ton dossier : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/dev-verification-sortie-mondes/`.

1. `verifier_sortie_auteur_mondes_v1.py` (bibliothèque standard seule), lancé par `python3 -I -B PROGRAMME SORTIE_AUTEUR RAPPORT_JSON`, codes de sortie déclarés.
2. **Essais** : une sortie factice saine (lisible) ; pour chaque règle des points 1, 2, 3 et 5, au moins un artefact qui la viole et la fait tomber (R5) ; une famille sans vérité exacte écartée sans rendre la sortie illisible ; un nom de modèle et une chaîne de forme de clé refusés ; une famille tenue à l'écart nommée hors de son bloc refusée ; mutations (chaque garde retirée fait échouer son essai).
3. `rapport-developpeur-verification-sortie-mondes-v1.md` : chaque règle du § 6 citée, sa ligne de code, son essai ; ce que la lettre ne fixe pas (en remarque) ; la commande à jouer avant l'envoi (sur une sortie factice) et à la réception.
4. Une table d'empreintes ; un compagnon par fichier.

## Interdits

Voir en tête. Jamais de heredoc ni de code en ligne passé à un interpréteur. Aucun appel à un fournisseur, aucune clé lue ni nommée, aucune dépense, aucun relais lancé. Aucune écriture dans un dépôt, aucun commit. Rien sous `archives-reponses-modeles/`, rien sous `/root/.claude/`, aucune branche de quarantaine ni de matière première ouverte. Jamais le nom d'une commande d'arrêt ou de recherche de processus. Aucun identifiant de modèle dans tes pièces (la liste des noms refusés du programme se lit d'un fichier de motifs d'essai que tu déclares, à remplacer par la liste réelle de la mère). Aucune recette. Au premier refus de permission, de classifieur ou de garde : arrête-toi et dis-le.

VERSION DE PYTHON : `python3 --version` (3.13) ; essais sous `/home/user/controle-ia-travail/.venv/bin/python -B -m pytest -q -p no:cacheprovider` ; AUCUN `-c`.

AUCUNE COMMANDE DE LISTE HORS DE TON DOSSIER. TOUT AUTRE FICHIER S'OUVRE PAR SON CHEMIN COMPLET. UNE COMMANDE SIMPLE PAR APPEL : NI `&&`, NI `;`, NI BOUCLE, NI SUBSTITUTION. `git show` TOUJOURS REDIRIGÉ PAR `>` VERS TON DOSSIER, SUR `origin/main`, APRÈS `git -C /home/user/controle-ia-travail-organisme fetch origin main` (JAMAIS DE `git fetch` SANS NOM DE BRANCHE).

# Mandat du développeur — programme de vérité des dix-sept témoins imposés (course « seuil et moniteurs ») — v1

Pièce de travail (classe C), donnée par la session du compte organisme le 2026-11-21 sur le mot de la mère (08:35Z) : « le programme scellé qui calcule la vérité des dix-sept témoins, écrit et scellé avant toute lecture de la sortie, cas sain et artefact (R5) ». Code par un développeur O, vérifié par un vérificateur S, puis scellé par la mère **avant toute lecture de la sortie de l'auteur**. **Aucun appel, aucune dépense, aucune clé.**

## Qui

Un développeur neuf (modèle O), qui n'a écrit ni le mandat de l'auteur, ni sa contre-lecture, ni le programme de vérification de la sortie. Tu signes « développeur du programme de vérité des témoins imposés, modèle O ». **Tu ne vois aucune sortie de l'auteur** (il n'en existe pas) ; tu ne demandes rien à l'auteur.

## Ce qui fait foi (vérifie chaque empreinte contre son compagnon)

- **Le mandat de l'auteur v3 scellé** : `/home/user/controle-ia-travail-organisme/docs/notes/ideation-seuil-moniteurs-v1/mandat-mondes-plantes-v3/mandat-auteur-mondes-plantes-seuil-et-moniteurs-v3.md` (`816313cb342a642e4dadda6d111e30fff2800eda2a7975722a0961c5ec05dbe9`), et sa pièce de scellement sur `origin/main` (`prereg/ideation-seuil-moniteurs-v1/scellement-mandat-auteur-mondes-plantes-v3-v1.md`). En particulier : § 2 (cadre : « déclare tenir », garantie violée), **§ 3.1 (les dix-sept témoins imposés T01 à T17, leur loi, leur règle, leur taille, leur sort attendu, leur portée)**, § 3.2 et § 3.3 (familles et mondes imposés que les témoins visent), § 4.3 (grammaire fermée d'une règle de témoin, dont les conventions de T08 — quantile empirique — et de T12 — test répété unilatéral à droite, valeur p définie), § 6, point 4 (recalcul en loi exacte, écart de plus de 0,001 compté et nommé, audit dans les deux sens).
- **Les décisions de la mère** D-M11 à D-M18 (rapports v2 et v3 du rédacteur, même dossier parent) : D-M16 (la base, et tout témoin autre que T05 et T07, se lit sur la seule garantie) ; T05 et T07 seuls lus « sans gain » (`morte_sans_gain`).
- **La note de conception générale** des expérimentateurs et des tests de mort (`docs/notes/experimentateurs-et-tests-de-mort-v1/conception-branchement-experimentateurs-tests-de-mort-v1.md`, `4f3ae86f…`, sur `origin/main`) et son programme de calcul (le rédacteur du mandat v2 le cite par `301c0f52…`), pour les formules de référence ; la conception « seuil et moniteurs » v6 (`/home/user/controle-ia-travail-organisme/docs/notes/ideation-seuil-moniteurs-v1/conception-v6/`, ordre `208454c5…`), § 7.

## Ce que le programme fait

1. Un **moteur de loi exacte** sur la grammaire fermée du § 4.3 : pour une loi et une règle de témoin, il rend la valeur vraie (taux, couverture, puissance, valeur p, rang, selon la règle) **en calcul exact** (rationnels ou sommes finies exactes, bibliothèque standard seule ; un calcul en flottants n'est permis que s'il est borné et la borne écrite).
2. La **table des dix-sept témoins imposés** : pour chacun, sa valeur vraie et son issue attendue (garantie tenue ou violée ; `morte_sans_gain` pour T05 et T07 selon la lettre), écrites dans un JSON trié, joué deux fois, `cmp` muet.
3. Une fonction de **recalcul d'un témoin quelconque** (loi et règle données) pour le point 4 du § 6, appliquée plus tard aux témoins libres de l'auteur : elle est écrite et éprouvée maintenant, et scellée avec le reste.

## Ce que tu écris (fichiers neufs seulement)

Ton dossier : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/dev-verite-temoins-mondes/`.

1. `calculer_verite_temoins_imposes_v1.py` (bibliothèque standard seule), lancé par `python3 -I -B PROGRAMME SORTIE_JSON` ; et, en mode recalcul, `python3 -I -B PROGRAMME --recalculer TEMOINS_JSON SORTIE_JSON`.
2. **Essais** : pour chaque forme de règle de la grammaire, un cas sain dont la valeur est connue par un calcul à la main écrit dans l'essai, et un artefact (loi ou règle hors grammaire, taille absente, paramètre hors domaine) refusé (R5) ; T08 au rang juste aux tailles en jeu ; T12 du bon côté ; T07 aux deux tailles (`n` = 200, le taux à 400 dans `valeurs_de_plus`) ; accord, à 0,001 près, avec le programme de calcul de la note là où il calcule la même chose (sinon, dis-le) ; mutations (chaque garde retirée fait échouer son essai).
3. `rapport-developpeur-verite-temoins-v1.md` : chaque témoin, sa définition citée, sa ligne de code, son essai ; ce que la lettre ne fixe pas (en remarque, jamais tranché) ; la table de sortie en annexe.
4. Une table d'empreintes ; un compagnon par fichier.

## Interdits

Voir en tête. Jamais de heredoc ni de code en ligne passé à un interpréteur. Aucun appel à un fournisseur, aucune clé lue ni nommée, aucune dépense, aucun relais lancé. Aucune écriture dans un dépôt, aucun commit. Rien sous `archives-reponses-modeles/`, rien sous `/root/.claude/`, aucune branche de quarantaine ni de matière première ouverte, aucune source de la liste scellée. **Ta table de vérité ne quitte pas ton dossier et n'est servie à personne d'autre que la session** : elle ne va jamais vers l'auteur, ni vers une machine jetable. Jamais le nom d'une commande d'arrêt ou de recherche de processus. Aucun identifiant de modèle. Aucune recette. Au premier refus de permission, de classifieur ou de garde : arrête-toi et dis-le.

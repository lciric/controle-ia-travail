VERSION DE PYTHON : `python3 --version` ; AUCUN `-c`, AUCUN `-` APRÈS PYTHON3 SAUF `-I -B`

AUCUNE COMMANDE DE LISTE : NI `ls`, NI `find`, NI `git ls-tree`, NI `git ls-files`, NI `git status`, NI `git show --name-only`, NI `grep -r`, NI RECHERCHE SUR UN DOSSIER ENTIER, NI JOKER DANS UN CHEMIN. TOUT FICHIER S'OUVRE PAR SON CHEMIN COMPLET. UNE COMMANDE SIMPLE PAR APPEL : NI `&&`, NI `;`, NI BOUCLE. `git show` TOUJOURS REDIRIGÉ VERS UN FICHIER PAR `>`, SUR `origin/main`.

# Mandat du développeur — calcul versionné des conditions du plafond de l'étage 2 à 200 témoins (nœud 3 de l'additif 3) — v1

Pièce de travail (classe C), donnée par la session du compte organisme le 2026-11-20, sur GO-2026-11-20-26, GO-2026-11-20-36 (2) (« conditions du plafond par calcul versionné sans devis neuf ») et la décision de la mère (12:10Z : Opus rédige, Sonnet contre-lit ; le compteur coupe le pire cas, issue à écrire ici). Pièce d'instrument (classe B). **Aucun appel payant ; processeur seul.** Le calcul sera scellé avec l'additif de code de l'étage 2.

## Qui

Un développeur neuf, modèle O, qui n'a écrit ni le texte de la ligne 3, ni ses additifs, ni le devis ni ses calculs. Tu signes « développeur, modèle O ».

## Ce qui fait foi (vérifie chaque empreinte contre son compagnon)

Dossier L3 = `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-3-votes-effectifs-juges/`.
- Le devis v7 scellé (`origin/main:prereg/organisme-auto-conception-v9/devis-ligne-3-etage-payant-v7.md`) en entier, en particulier sa ligne « 200 témoins », son § 6 (table des conditions) et son § 7 ; son calcul `L3/calcul_devis_ligne_3_v3.py` et sa sortie `L3/calcul-devis-ligne-3-v3.json`.
- Le texte de la ligne 3 v7 scellé (`origin/main:prereg/organisme-auto-conception-v9/preenregistrement-ligne-3-votes-effectifs-juges-v7.md`) : l. 193 (plafond), l. 241, l. 305 (gestes), l. 384 (issue du compteur), et les blocs plomberie, A, B (nombre d'appels, réserve de 0,60 USD par session).
- L'additif 3 v3 scellé (`origin/main:prereg/organisme-auto-conception-v9/additif-3-preenregistrement-ligne-3-portee-200-v3.md`), § 4.2 : les conditions (i), (ii), (iii) du plafond, le plafond lu à 88,36 USD ; et la contre-lecture de l'additif 3 `L3/additif-3-portee-200-v1/contre-lecture-additif-3-portee-200-v1.md` (`f264cf9e…`), § « Ce qui manque, et que j'ai calculé » et nœud 3 (son calcul approché, à refaire ici par un calcul versionné).
- L'inventaire de l'étage 2 : `L3/etage-2-portee-200-v1/inventaire-etage-2-portee-200-ligne-3-v1.md` (`a2039f7d…`), points ouverts (le pire du devis à 200, 88,3617 USD, au-dessus de 88,36).

## Ce que tu écris

1. `calcul_conditions_plafond_200_ligne_3_v1.py` (nom neuf ; le v3 n'est pas modifié), bibliothèque standard, à partir du calcul v3 : il rend, à 200 témoins et au plafond de 88,36 USD, les chiffres des trois conditions (i), (ii), (iii) de l'additif 3, § 4.2 ; **l'issue écrite d'avance du pire cas** (à quel témoin et à quel bloc le compteur coupe, ce qui est encore lu, ce qui manque, avec la réserve de 0,60 USD) ; le cas haut et le cas attendu ; tout en fractions exactes ou en centimes entiers, sans flottant dans une comparaison de seuil.
2. Sa sortie `calcul-conditions-plafond-200-ligne-3-v1.json`, jouée deux fois (`env -C /home/user/controle-ia-travail python3 -I -B CHEMIN`), égale à l'octet.
3. Des essais (`essais_calcul_conditions_plafond_200_v1.py`, lancés par `env -C DOSSIER /home/user/controle-ia-travail/.venv/bin/python -B -m pytest -q -p no:cacheprovider F`) : à 100 témoins, le calcul redonne à l'octet les chiffres du devis v7 (l'issue « 18 témoins, non concluant par manque de témoins », l. 384) ; à 200, la frontière du plafond de part et d'autre ; un cas sain et un artefact par garde.
4. Un rapport `rapport-developpeur-calcul-plafond-200-v1.md` : les chiffres, l'issue du pire cas, ce qui diffère du calcul approché du contre-lecteur et pourquoi, les points que la lettre ne tranche pas (en remarque).

Ton bloc-notes : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/dev-calcul-plafond-200/`. Chaque fichier rendu avec son compagnon (`env -C DOSSIER sha256sum F`, redirigé vers `DOSSIER/F.sha256`).

## Interdits

Voir en tête. Aucun appel à un fournisseur de modèles, aucune dépense, aucune clé lue. Aucune mesure de l'étage 1 ouverte (rien sous `…/execution-etage-1-v1/` ni `…/verdict-etage-1-v1/`). Aucune écriture dans le dépôt, aucun commit. Rien sous `archives-reponses-modeles/`, rien sous `/root/.claude/`. Jamais de heredoc ni de code en ligne passé à un interpréteur. Jamais le nom d'une commande d'arrêt ou de recherche de processus par motif. Aucune publication d'artefact. Aucun identifiant de modèle. Au premier refus de permission, de classifieur ou de garde : arrête-toi et dis-le.

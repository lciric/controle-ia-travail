VERSION DE PYTHON : `python3 --version` ; AUCUN `-c`, AUCUN `-` APRÈS PYTHON3 SAUF `-B`

AUCUNE COMMANDE DE LISTE HORS DE TON BLOC-NOTES ET DU DOSSIER `code-v6/` CI-DESSOUS. TOUT AUTRE FICHIER S'OUVRE PAR SON CHEMIN COMPLET. UNE COMMANDE SIMPLE PAR APPEL : NI `&&`, NI `;`, NI BOUCLE. `git show` TOUJOURS REDIRIGÉ VERS UN FICHIER PAR `>`, SUR `origin/main`. TOUTE REDIRECTION VERS UN CHEMIN COMPLET DE TON BLOC-NOTES.

# Mandat du développeur — programme qui enchaîne les étapes 6 bis et 7 du palier 0b (EN ATTENTE DU MOT DE LAZAR) — v1

Pièce de travail (classe C), donnée par la session du compte organisme le 2026-11-20, sur la règle de la mère (18:08Z : « aucune étape 3 à 9 ne se joue avant le GO de Lazar sur le texte suivant la v13 ; elles ne se joueront qu'au seul commit du code v6 […]. Le programme qui enchaîne 6 bis et 7 est écrit avant ce GO (Opus écrit, Sonnet vérifie, processeur seul) »). Constat d'origine : l'audit des trous (`8e965f80…`) et la contre-lecture du brouillon v14 (`c8ca85f5…`, point 3). **Rien n'est lancé en vrai ; aucune graine décisive.**

## Qui

Le développeur du code v6 (modèle O). Tu signes « développeur, modèle O ».

## Ce qui fait foi (vérifie chaque empreinte contre son compagnon)

Dossier P0B = `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/`.
- Le texte en vigueur, v13 scellé (`d9591d5b…`), et le brouillon v14 (`P0B/brouillon-v14/preenregistrement-heritage-palier-0b-etage-processeur-v14.md`, `840400f3…`) : les étapes 6, 6 bis et 7 (ce qu'elles lisent, ce qu'elles gèlent, ce qu'elles écrivent, à quelle couche de graines), l'ordre des opérations, la liste d'arrêt, l'annexe C.
- Le code v6 vérifié : `P0B/code-v6/` (table `P0B/table-empreintes-code-v6.txt`, `639335b9…`) et sa vérification (`a7d0b1bc…`) ; ton programme `code-v6/outils-dev/lancer_etapes_8_et_9_v1.py` (`67052a4b…`) comme modèle de forme.

## Ce que tu écris (bloc-notes, sous-dossier `programme-6bis-7-v1/`)

1. **`lancer_etapes_6bis_et_7_v1.py`**, hors du paquet (comme celui des étapes 8 et 9), qui enchaîne les étapes 6 bis et 7 **à la lettre du texte**, par les seules fonctions du code v6 (aucune fonction de calcul réécrite) : verrou exigé (pièce d'autorisation et pièce de contrôle de la mère, dont le commit du code v6), couche et racine exactes, lecture des fichiers gelés des étapes précédentes **vérifiée par leurs empreintes**, écriture et scellement de ce que le texte dit, manifeste (règle R9). **S'il faut une fonction neuve dans le paquet**, arrête-toi et dis-le : ce serait un code v7.
2. **Ses essais** (pytest), sur racine factice et fichiers gelés factices, **sous la couche « essai-de-forme » seule** : cas sain et artefact (R5) pour chaque garde (pièces absentes, empreinte d'un gelé fausse, couche interdite, dossier déjà présent) ; l'essai « aucune graine décisive » passe.
3. **`rapport-programme-6bis-7-v1.md`** : ce que le texte exige des étapes 6 bis et 7 (citation, ligne), comment le programme le fait (fichier:ligne), ce que la lettre ne fixe pas (silences, avec proposition marquée), la commande exacte de lancement, et ce que la v15 ou la pièce de contrôle de la mère devra porter (empreinte du programme).
4. Une table d'empreintes du sous-dossier.

Essais : `env -C DOSSIER /home/user/controle-ia-travail/.venv/bin/python -B -m pytest -q -p no:cacheprovider F` avec `PYTHONPATH=src` et les variables `HERITAGE_DEPOT` et `HERITAGE_COPIE_ORGANISME` comme pour le code v6 ; long : en tâche de fond. Chaque fichier avec son compagnon (`env -C DOSSIER sha256sum F`, redirigé vers `DOSSIER/F.sha256`).

Ton bloc-notes : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/dev-palier-0b-v6/`.

## Interdits

Voir en tête. Aucun tirage décisif, aucun étalonnage réel, aucun lancement d'étape hors des essais sous « essai-de-forme », aucune pièce d'autorisation. Aucun appel à un fournisseur de modèles, aucune dépense. Aucune écriture dans le dépôt, aucun commit. Rien sous `archives-reponses-modeles/`, rien sous `/root/.claude/`. Jamais de heredoc ni de code en ligne passé à un interpréteur. Jamais le nom d'une commande d'arrêt ou de recherche de processus, même sans motif. Aucune publication d'artefact. Aucun identifiant de modèle. Au premier refus de permission, de classifieur ou de garde : arrête-toi et dis-le.

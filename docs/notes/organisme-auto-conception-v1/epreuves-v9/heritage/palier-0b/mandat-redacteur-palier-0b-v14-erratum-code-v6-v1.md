VERSION DE PYTHON : `python3 --version` ; AUCUN `-c`, AUCUN `-` APRÈS PYTHON3 SAUF `-B`

AUCUNE COMMANDE DE LISTE : NI `ls`, NI `find`, NI `git ls-tree`, NI `git ls-files`, NI `git status`, NI `git show --name-only`, NI `grep -r`, NI RECHERCHE SUR UN DOSSIER ENTIER, NI JOKER DANS UN CHEMIN. TOUT FICHIER S'OUVRE PAR SON CHEMIN COMPLET. UNE COMMANDE SIMPLE PAR APPEL : NI `&&`, NI `;`, NI BOUCLE. `git show` TOUJOURS REDIRIGÉ VERS UN FICHIER PAR `>`, SUR `origin/main`. TOUTE REDIRECTION VERS UN CHEMIN COMPLET DE TON DOSSIER.

# Mandat du rédacteur — préenregistrement du palier 0b, version 14 (erratum après le code v6) — BROUILLON, EN ATTENTE DU MOT DE LAZAR — v1

Pièce de travail (classe C), donnée par la session du compte organisme le 2026-11-20, sur l'accord de la mère (14:46Z : « le brouillon de l'erratum v14 (Fable neuf), versés sur ta branche et marqués « en attente du mot de Lazar » » ; 17:41Z : « Oui, lance le brouillon de l'erratum v14 par un Fable neuf, sans rien sceller »). **La v13 scellée reste le texte en vigueur ; le palier ne part pas avant un GO de Lazar qui nomme la v14.** Ce brouillon sera contre-lu ; rien n'est scellé avant le mot de Lazar.

## Qui

Un rédacteur neuf, modèle F, qui n'a écrit aucune version du préenregistrement du palier 0b, ni aucun code, ni aucune vérification, ni l'audit des trous. Tu signes « rédacteur neuf, modèle F ».

## Ce qui fait foi (vérifie chaque empreinte contre son compagnon)

Dossier P = `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/`.
- La v13 scellée : `P/preenregistrement-heritage-palier-0b-etage-processeur-v13.md` (`d9591d5b…`).
- L'audit des trous : `P/lecture-lancement-v1/audit-trous-code-v5-palier-0b-v1.md` (`8e965f80…`).
- Le code v6 : `P/code-v6/rapport-developpeur-code-palier-0b-v6.md` (`0f408c6f…`) — **§ 7 (liste de l'erratum v14), les 19 silences, § 8 (remarques)** ; la table `P/table-empreintes-code-v6.txt` (`639335b9…`, 64 lignes).
- La vérification du code v6 : `P/verification-code-palier-0b-v6-v1.md` (`a7d0b1bc…`), « Conforme ».
- Sur `origin/main` : `registres/decisions.md` (R-4285, R-4292, R-4295, R-4296, et les lignes qui inscriront les décisions de la mère de 17:41Z si elles y sont) ; `registres/go.md`, GO-2026-11-20-25 et GO-2026-11-20-66.

## Décisions de la mère à porter (17:41Z)

- Silence n° 3 : la source étrangère de H, dans le mode « sources », est la suivante du même lot.
- Silence n° 4 : le reliquat est sommé sur les quatre générations ; l'erratum dit que **la ventilation par génération est perdue** (une analyse qui la voudrait demande un code v7).
- Silence n° 13 : laissé (non inscrit comme règle).
- Silence n° 16 : le dénominateur de R est pris à la famille B ; écrit à M7.
- Silences 1, 2, 5 à 12, 14, 15 et 17 à 19 : entrent dans l'erratum **tels que le rapport les propose**.
- L'empreinte du programme de lancement (`outils-dev/lancer_etapes_8_et_9_v1.py`, `67052a4b…`, hors du paquet, donc hors du verrou) va dans la pièce de contrôle de la mère : l'erratum le dit.

## Ce que la v14 porte, et rien d'autre

Sous le nom neuf `preenregistrement-heritage-palier-0b-etage-processeur-v14.md`, par l'outil contre-lu (`python3 -B /home/user/controle-ia-travail/scripts/remplacer_texte_exact_v1.py`, `391db990…`), un JSON écrit avec l'outil d'écriture de fichiers ; chaque ancre comptée par `grep -c -F -e` avant l'appel :

1. **Les points 1 à 11 du § 7 du rapport du code v6**, à la lettre, dont la ligne « - Commit du code d'analyse : » avec **un commit laissé en blanc** (`COMMIT_V6`, que la mère remplira quand le code v6 sera versé sur `main`) et la table des 64 lignes dans le premier bloc qui la suit (forme exacte que le verrou lit) ; une seule ligne commence par ce préfixe.
2. La phrase « aucun programme de lancement des étapes 8 et 9 n'existe encore » corrigée **aux deux lieux** (B8, l. 332 ; silence n° 14, l. 991 de la v13), selon la vérification.
3. Les **comptes** : 117 essais, banc de 147 défauts.
4. **Les décisions de la mère** ci-dessus.
5. **« Ce qui demande un code v6 »** : une section neuve (point 8 du § 7).
6. Les remarques du § 8 du rapport : l'étape 10 sans programme d'analyse ; la place disque de l'étape 8 (≈ 1,5 Go, calcul) ; à porter **en remarque**, sans règle.
7. **Le nœud** : un GO qui nomme la v14 (GO-2026-11-20-66 nomme la v13).
8. **Tenue** : titre, statut « BROUILLON, non scellé, en attente du mot de Lazar », date `date -u`, ligne de version, section « Contre-lecture ».

Puis le différentiel `diff -u` v13 → v14, le compte des lignes qui commencent par « - Commit du code d'analyse : » (1 attendu), et un rapport court `rapport-redacteur-palier-0b-v14-v1.md` (remplacements, ancres, points où la lettre ne suffit pas, en remarque, jamais tranchés).

Ton dossier : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/redacteur-palier-0b-v14/`. Chaque fichier avec son compagnon (`env -C DOSSIER sha256sum F`, redirigé vers `DOSSIER/F.sha256`).

## Interdits

Voir en tête. Jamais de heredoc ni de code en ligne passé à un interpréteur. Aucun lancement du code, aucun tirage, aucune pièce d'autorisation. Aucune écriture dans le dépôt, aucun commit. Rien sous `archives-reponses-modeles/`, rien sous `/root/.claude/`. Jamais le nom d'une commande d'arrêt ou de recherche de processus. Aucun appel à un fournisseur de modèles, aucune dépense, aucune publication d'artefact. Aucun identifiant de modèle. Au premier refus de permission, de classifieur ou de garde : arrête-toi et dis-le.

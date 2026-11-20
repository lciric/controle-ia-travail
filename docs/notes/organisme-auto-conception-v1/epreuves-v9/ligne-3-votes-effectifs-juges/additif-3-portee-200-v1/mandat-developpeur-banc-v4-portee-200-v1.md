VERSION DE PYTHON : `python3 --version` ; AUCUN `-c`, AUCUN `-` APRÈS PYTHON3

AUCUNE COMMANDE DE LISTE : NI `ls`, NI `find`, NI `git ls-tree`, NI `git ls-files`, NI `git show --name-only`, NI `grep -r`, NI RECHERCHE SUR UN DOSSIER ENTIER, NI JOKER DANS UN CHEMIN. TOUT FICHIER S'OUVRE PAR SON CHEMIN COMPLET. UNE COMMANDE SIMPLE PAR APPEL : NI `&&`, NI `;`, NI BOUCLE. `git show` TOUJOURS REDIRIGÉ VERS UN FICHIER PAR `>`. AUCUNE RECHERCHE DE MOTIF LARGE. (Seule exception : `git status --porcelain` borné à un dossier, quand le code ou ses essais l'appellent, comme le demande la garde « dossier du code propre ».)

# Mandat du développeur — banc des juges scriptés de la ligne 3, v4, mode « portée à 200 » — v1

Pièce de travail (classe C), donnée par la session du compte organisme le 2026-11-20, sous GO-2026-11-20-26 et GO-2026-11-20-36 (2), après le scellement de l'additif 3 v3 par la mère (`ADDITIF-3-ORGANISME-V9-LIGNE-3`, main 0bb14c64). Pièce d'instrument (classe B) : contre-lue par un autre modèle, vérification des corrections par le même. **Le code est écrit et essayé sur la seule racine des essais ; aucune racine neuve n'est dérivée, la mesure n'est pas lancée** : elle attend l'additif de code scellé qui autorise.

## Qui

Un développeur neuf, modèle O, qui n'a écrit ni le texte de la ligne 3, ni ses additifs, ni le banc v1 à v3, ni le verdict de l'étage 1. Tu signes « développeur, modèle O ».

## Règle d'aveugle

Tu n'ouvres aucune mesure de l'étage 1 : rien sous `…/ligne-3-votes-effectifs-juges/execution-etage-1-v1/`, `…/verdict-etage-1-v1/`, ni `prereg/organisme-auto-conception-v9/ligne-3/verdict-etage-1/`. Tu ne lances le banc que sur la racine des essais 2026111930.

## Ce qui fait foi (vérifie chaque empreinte contre son compagnon, `env -C DOSSIER sha256sum -c F.sha256`)

- **L'additif 3 scellé**, sur main (`git -C /home/user/controle-ia-travail fetch origin main`, puis `git … show FETCH_HEAD:prereg/organisme-auto-conception-v9/additif-3-preenregistrement-ligne-3-portee-200-v3.md > FICHIER_DANS_TON_DOSSIER`), empreinte `71b7a876398cdcc133f006c01ff7eb644e8f2c69be79e90be50088bd26492807`, en entier ; son **§ 5** est ton cahier des charges, à la lettre ; ses § 1, 2, 3 et 6 disent ce que le code doit mesurer, dériver, aider à lire et garder.
- L'additif 2 scellé (`prereg/organisme-auto-conception-v9/additif-2-code-preenregistrement-ligne-3-votes-effectifs-juges-v7-v3.md`, `f5562d20…`) : § 6 et § 7 (forme des commandes, gardes des chemins).
- Le banc v3 et son dossier : `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-3-votes-effectifs-juges/code-etage-1-v3/banc_juges_scriptes_ligne_3_v3.py` (`09bfe0db…`), ses essais, son chronométrage et le calcul de référence `calcul_predictions_ligne_3_v2.py` (chemins tirés du banc v3 ou de l'additif 2).

## Ce que tu écris (§ 5 de l'additif 3, points 1 à 8)

Dans ton dossier de code `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/dev-banc-v4-portee-200/code/` (copie du dossier du banc v3, puis fichiers neufs ; le v3 n'est pas modifié) :
1. `banc_juges_scriptes_ligne_3_v4.py` : le v3 plus le mode `--portee-200`, configuration gelée en constante (répliques 2 000 ; tirages 2 000 ; monde de puissance seul ; écarts 0,05 ; 0,10 ; 0,15 ; lois 1 et 3 ; sept ρ ; trois ρ′ ; n = 200) ; racines 2026112031 à 2026112033 sous autorisation par chemin et empreinte (`verifier_autorisation`), clés 2 et 12, `.spawn(210)` ; racines 2026111931 à 2026111937 refusées par tout chemin du fichier neuf (mode décisif de l'étage 1 retiré ou inatteignable) ; garde « dossier du code propre » **avant toute dérivation** ; aide `criteres_mecaniques.puissance` (issue A ou B), jamais verdict.
2. `chronometrer_portee_200_ligne_3_v1.py` : dérive la seule racine 2026112031, n'écrit que des durées.
3. Les essais du point 5 (égalité à l'octet des sorties du v3 sur la racine des essais ; cas sain du mode neuf à petit nombre de répliques ; chaque artefact vu) et le rejeu du contrôle des défauts réintroduits du v3, étendu aux gardes neuves. Chaque garde du § 6 essayée sur un cas sain et sur un artefact (R5). Pour la garde « dossier du code propre », fais l'essai dans un dépôt git jetable créé dans ton bloc-notes (`git init` d'un dossier neuf), jamais dans `/home/user/controle-ia-travail`.
4. Les différentiels `diff -u` v3 → v4 et un rapport `rapport-developpeur-banc-v4-portee-200-v1.md` (hors du dossier de code) : fichiers et empreintes, essais et sortie, ce qui change et rien d'autre, les deux commandes de lancement du gabarit du § 5 complétées sauf le chemin et l'empreinte de l'additif de code, tout point que la lettre de l'additif 3 ne tranche pas (en remarque).

Lancement des essais : `env -C DOSSIER /home/user/controle-ia-travail/.venv/bin/python -B -m pytest -q -p no:cacheprovider F`, avec `PYTHONDONTWRITEBYTECODE=1`. Chaque fichier rendu avec son compagnon (`env -C DOSSIER sha256sum F`, redirigé vers `DOSSIER/F.sha256`).

## Interdits

Voir en tête et la règle d'aveugle. **Aucune dérivation des racines 2026112031 à 2026112033 ni 2026111931 à 2026111937**, aucune mesure. Aucune écriture dans le dépôt `/home/user/controle-ia-travail`, aucun commit dans ce dépôt. Rien sous `archives-reponses-modeles/`, rien sous `/root/.claude/`. Jamais de heredoc ni de code en ligne passé à un interpréteur. Jamais le nom d'une commande d'arrêt ou de recherche de processus par motif. Aucun appel à un fournisseur de modèles, aucune dépense. Aucun identifiant de modèle. Au premier refus de permission, de classifieur ou de garde : arrête-toi et dis-le.

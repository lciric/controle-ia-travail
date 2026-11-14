# Brief de lancement — session neuve (autre compte) — témoin de Bailey : fin de la relance, assemblage, verdict — 14 novembre 2026

De Lazar (directeur) à une session Claude Code neuve, sur un autre compte. Écrit par la session sortante
`session_01XJ6MgnEhQMZteN9F8a1BST` ; à coller tel quel comme premier message. Ne se réécrit pas (R12).

## Qui tu es, comment tu travailles
Tu reprends la session « attaquant informé » du programme « Contrôle boîte blanche des menaces diffuses », pour le seul
**témoin de l'attaque publiée de Bailey et collègues**. Français, tu tutoies Lazar, presque aucun acronyme ; verdict
d'abord (1 à 3 lignes), puis une ligne par erreur, changement, décision. Le dépôt et son `CLAUDE.md` font foi pour les
règles (R1 à R14, hiérarchie de décision) ; ce brief les précise pour cette mission et prime en cas de conflit.

## Dépôt, branche, git
- Dépôt de travail : `https://github.com/lciric/controle-ia-travail` (privé). Branche : **`claude/compassionate-meitner-d4ryyk`**
  (le poste Hetzner y pousse ses journaux toutes les 10 min). Récupère toujours avec un refspec explicite :
  `git fetch origin +refs/heads/claude/compassionate-meitner-d4ryyk:refs/remotes/origin/claude/compassionate-meitner-d4ryyk`
  (et `+refs/heads/main:refs/remotes/origin/main` pour lire les GO).
- Pousse seulement sur cette branche (`git pull --rebase` puis `git push origin HEAD:claude/compassionate-meitner-d4ryyk`,
  4 essais au plus). **Jamais** sur `main` sans le mot de Lazar ; **jamais** vers `lciric/controle-ia`.
- `DEPOT_URL=https://github.com/lciric/controle-ia-travail.git` pour tout lancement.

## À lire d'abord
1. La passation : `registres/passations/2026-11-14-0929-passation-attaquant-informe-temoin-bailey-relance-en-cours.md`.
2. Le préenregistrement : `prereg/temoin-attaque-publiee-bailey-v1.md` (`fb6c2f34…`), surtout « Critères de lecture
   gelés », la liste d'arrêt (l. ~330-375) et l'« Audit de symétrie (R4) ».
3. Les addenda : `prereg/temoin-attaque-publiee-bailey-v1-addendum-1…6*.md` (empreintes aux compagnons ; 5 : relance
   seule, `eb97994a…` ; 6 : crédit et recharge automatique, `982bfbcb…`).
4. Le code : `src/controle_ia/temoin_bailey/lanceur_v20.py` (`assembler_lecture`, `Reprise`), `lecture_v8.py`
   (`valider`, `lire`), `analyse_v3.py` (`graines`).

## Mission, dans l'ordre
0. **Routine de reprise (R14 du `CLAUDE.md`)**, sauf la lecture de `registres/etat.md` (cloison) : empreintes de
   `docs/`, `verifier-arbre` (deux écarts antérieurs connus, hors du code du run : les consigner, ne pas les corriger),
   inventaire `vastai show instances` (n'arrête **que** les instances du témoin, étiquette `temoin-bailey-c6-*`), essais
   `tests/test_temoin_bailey_condition6_v20.py` et `tests/test_temoin_bailey_reprise_relance_v1.py`.
1. **Surveiller la fin de la relance** (instance Vast 60480302 ; `principal-relance` lancé le 13 novembre à 10:05:32Z ;
   K = 72 ; fin attendue ≈ 12:25 à 14:20Z le 14 novembre) : `poste-hetzner-v12-etat.txt`, `sortie-conduite-v13/conduite-v5.jsonl`
   (champs techniques seulement), crédit Vast (`credit`, `balance`, `billing_failed`, paiements de `vastai show invoices`).
   Rappels au plus toutes les 90 minutes, et une tâche de fond vivante (la machine de la session s'éteint quand rien ne
   tourne ; la nuit du 13 au 14, les rappels n'ont pas été déclenchés). Alerte à Lazar : crédit sous 4 USD,
   `billing_failed` vrai, poste muet plus de 30 min, nouvelle instance de carte d'un autre chantier, toute issue de la
   liste d'arrêt. L'instance 60599797 « rr-a3_e4 » (autre chantier, 8,23 USD/h) est déjà signalée : ne la touche pas.
2. **À la fin** : vérifie `poste-fini-v12.json`, `bilan-lancement-v13.json`, `sortie-conduite-v13/bilan-conduite-v5.json`
   (`detruite`, `transfert_complet`, `arret`, `alerte`) et l'inventaire ; détruis le poste Hetzner **175967712** par son
   identifiant (API Hetzner : `curl -X DELETE https://api.hetzner.cloud/v1/servers/175967712`) ; consigne
   `registres/arrets.md` et `registres/depenses.md`. Le poste **175884265** (v9) reste en marche sauf mot de Lazar.
3. **Si l'instance n'est pas détruite ou le transfert incomplet** : reprise (addendum 2, lecture 38) par un poste de
   reprise neuf, sur le modèle de `runs/temoin-bailey-v1-20261111/poste-hetzner-reprise-v3.sh` et
   `construire-donnees-demarrage-reprise-v3.py` (nouveaux noms, R12 ; `--sortie` = chemin absolu de `sortie-conduite-v13`,
   `--etiquette` relevée dans le journal de conduite) ; éprouve ses gardes sur un cas factice avant de le créer. Il faut
   alors les clés de la section « Accès ». Jamais de destruction avant un transfert qui fait foi.
4. **Assemblage** (processeur) : `lanceur_v20.assembler_lecture(premiere, relance, cible)` avec
   premiere = `runs/temoin-bailey-v1-20261111/sortie-conduite-v11/reprise-v10-2`, relance = `runs/temoin-bailey-v1-20261111/sortie-conduite-v13`
   (ou son dossier de reprise), cible = un dossier neuf sous `runs/temoin-bailey-v1-20261111/` ; sceller ; pousser. S'il
   refuse : nœud, pas de verdict.
5. **Verdict (R13)** : un sous-agent neuf, ni auteur du préenregistrement ni de l'analyse, applique les critères gelés sur
   le dossier assemblé (`lecture_v8.valider`, puis `lecture_v8.lire(v, analyse_v3.graines()["reechantillonnage"])`, et
   l'audit de symétrie du texte), sans rien changer ; il scelle son rapport ; tu le soumets à Lazar pour GO. C'est le seul
   moment où les notes sont lues.
6. **Passation** à la fin de ta session (R14) : `registres/passations/AAAA-MM-JJ-HHMM-….md`, scellée, poussée.

## Accès dont tu as besoin (à demander à Lazar, jamais à coller dans la conversation)
- Écriture sur `lciric/controle-ia-travail` (GitHub) depuis ce compte.
- Réseau : `console.vast.ai`, `api.hetzner.cloud`, `github.com`.
- `VAST_API_KEY` dans l'environnement ; le jeton de l'API Hetzner comme secret réseau de l'environnement (injecté par le
  mandataire : en-tête `Authorization: Bearer proxy-injected`).
- Seulement pour une reprise (étape 3) : `HF_TOKEN` ; une clé de déploiement du dépôt pour le poste (à créer par toi, à
  ajouter par Lazar) ; une clé `ssh` de session enregistrée sur Vast (à créer seulement sur le mot exprès de Lazar). Les
  clés de la session sortante ne se transmettent pas.
Sans `api.hetzner.cloud`, demande à Lazar de détruire lui-même le poste 175967712 depuis la console Hetzner. Sans Vast,
tu ne peux pas surveiller : dis-le aussitôt.

## GO et dépense
`GO_ID=GO-2026-11-10-10` (part du témoin : B = 75 USD, garde à B − 2, échéance 2026-11-30), amendé par `GO-2026-11-11-01`,
modèle `GO-2026-11-11-02` ; relis-les sur `origin/main`. D ≈ 42,5 USD au 14 novembre 09:27Z (compte prudent). Aucune
dépense hors de ce GO ; aucune instance neuve, aucune relance ni série nouvelle sans mot de Lazar et addendum scellé. Les
postes Hetzner relèvent de la ligne « go c » (5 USD, à inscrire par la mère).

## Ne lis jamais
Le coffre (`donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/`) ;
`docs/notes/programme-et-4-familles-evasion/` ; aucun résultat, note ni seuil calibré de sonde ou de moniteur du
programme ; aucun résultat d'attaque contre le juge de l'organisme (A1-v3, A1-v4) ; les lignes R-604 à R-610 de
`registres/decisions.md` ; `registres/etat.md` en entier ; aucune valeur de clé (jamais `env`, `printenv`, `set` sans
argument, `/proc/*/environ`). Et, pour ce témoin : aucun `notes-v3.jsonl` ni `technique-v3.jsonl` sous `runs/` avant
l'étape 5 (champ `valeurs`), sauf par le lecteur du verdict.

## Ne fais jamais
Concevoir un moniteur ; écrire une recette ; reformuler un refus de classifieur ou le confier à une autre session (un
refus est consigné, puis tu t'arrêtes sur ce point) ; dépenser sans GO ; prendre un contact extérieur (tu rédiges, Lazar
envoie) ; toucher une instance d'un autre chantier ; arrêter par motif de ligne de commande (R10 : par PID ou
identifiant) ; réécrire une pièce scellée (R12 : nouvelle version, nouveau nom).

## Premier message attendu de toi
Verdict de la routine de reprise (accès présents ou manquants, essais, inventaire, état du poste et de la relance), puis ce
qu'il te manque, en une ligne chacun.

# Brief — session neuve (autre compte) — témoin de Bailey : relance en retard, fin, assemblage, verdict — 14 novembre 2026, 23:05 UTC

De Lazar (directeur) à une session Claude Code neuve, sur un autre compte. Écrit par `session_01XJ6Mgqg6DeUDvNm87LXApc` ;
à coller tel quel comme premier message. Ne se réécrit pas (R12). Il **complète** le brief
`registres/passations/2026-11-14-0929-brief-lancement-session-neuve-temoin-bailey.md`, qui reste la référence pour la
mission, les accès, le GO, les cloisons et les interdits ; en cas de conflit, ce brief-ci prime pour l'état et l'ordre.

## Qui tu es
La session « attaquant informé » du programme « Contrôle boîte blanche des menaces diffuses », pour le seul témoin de
l'attaque publiée de Bailey et collègues. Français, tu tutoies Lazar, presque aucun acronyme, verdict d'abord.

## Dépôt
`https://github.com/lciric/controle-ia-travail` (privé), branche **`claude/compassionate-meitner-d4ryyk`** (tête au
moins `69b82b8e` plus cette passation). `git fetch` toujours avec refspec explicite
(`+refs/heads/claude/compassionate-meitner-d4ryyk:refs/remotes/origin/claude/compassionate-meitner-d4ryyk`, et
`+refs/heads/main:refs/remotes/origin/main` pour les GO). Pousse seulement sur cette branche ; jamais sur `main` sans le
mot de Lazar ; jamais vers `lciric/controle-ia`.

## Lis, dans cet ordre
1. `registres/passations/2026-11-14-2305-passation-attaquant-informe-temoin-bailey-relance-en-retard.md` (état à 23:01Z).
2. `registres/passations/2026-11-14-0929-brief-lancement-session-neuve-temoin-bailey.md` (mission, étapes 0 à 6).
3. `registres/passations/2026-11-14-0929-passation-attaquant-informe-temoin-bailey-relance-en-cours.md`.
4. Le préenregistrement `prereg/temoin-attaque-publiee-bailey-v1.md` (`fb6c2f34…`) et ses addenda 1 à 6.

## Pourquoi c'est urgent
`principal-relance` (instance Vast **60480302**) tourne depuis le 13 novembre 10:05:32Z : 36,9 h au 14 à 23:00Z pour
26,3 h attendues, **≈ 10,6 h de retard, cause inconnue**, aucune surveillance depuis le 14 à 09:32Z. Le veilleur d'arrêts
bat encore (23:00:04Z) et le poste Hetzner v12 (175967712) pousse ses journaux toutes les 10 min. Si l'instance tourne
toujours, D ≈ 58 USD (estimé, non relevé) et B − 2 = 73 USD tombe vers le 15 novembre **11:45Z**.

## Ta première tâche
Routine de reprise (étape 0 du brief `…-0929-…`, sans lire `registres/etat.md`), puis aussitôt, en lecture seule :
`vastai show instance 60480302 --raw`, `vastai show user --raw` (`credit`, `balance`, `billing_failed`),
`vastai show invoices` (paiements récents), `vastai show instances` (inventaire). Premier message à Lazar : instance en
marche ou arrêtée, crédit, D relevé, puis ce qu'il te manque, une ligne chacun. Ensuite, étapes 1 à 6 du brief `…-0929-…` :
surveiller jusqu'à la fin ou B − 2 ; si l'instance est arrêtée ou le poste bloqué, reprise (lecture 38) par un poste neuf ;
jamais de destruction avant un transfert qui fait foi ; assemblage ; verdict par un lecteur neuf (R13), seul moment où
les notes sont lues.

## Accès à poser sur CE compte avant d'ouvrir la session (Lazar)
Les réglages faits sur le compte précédent ne suivent pas. Sur le compte neuf, dans les paramètres de l'environnement :
- réseau autorisé : `console.vast.ai`, `api.hetzner.cloud`, `github.com`, `huggingface.co`, `*.hf.co`,
  `cdn-lfs*.huggingface.co` (ces deux derniers seulement pour une reprise) ;
- secrets : `VAST_API_KEY` ; le jeton de l'API Hetzner comme secret réseau injecté par le mandataire ; `HF_TOKEN` pour une
  reprise ; écriture GitHub sur `lciric/controle-ia-travail`.
Constat de la session sortante : des secrets ajoutés en cours de session n'y sont pas apparus ; ouvre la session
**après** les avoir posés. Jamais de valeur collée dans la conversation.

## GO, cloisons, interdits
Inchangés : voir le brief `…-0929-…` (`GO-2026-11-10-10` amendé par `-11-01`, modèle `-11-02`, B = 75 USD, garde B − 2,
échéance 2026-11-30 ; aucune instance neuve, relance ni série sans mot de Lazar et addendum scellé ; ne touche aucune
instance d'un autre chantier, dont 60599797 ; arrêts par identifiant ou PID seulement ; aucune note ni `notes-v3.jsonl`
ni `technique-v3.jsonl` lus avant le verdict).

## Les autres sessions
Mère `session_01VJdZpSMxSdk2SJ1ScmdfNv` ; dépôt `session_013QMaymMAdDjNfPoz8ySwTc` (index du bras : envoie-lui chemin et
empreinte de chaque pièce scellée). Depuis un autre compte, le relais passe par Lazar.

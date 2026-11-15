# Brief — session neuve (autre compte) — témoin de Bailey : choix de Lazar, verdict, clôture — 15 novembre 2026, 18:43 UTC

De Lazar (directeur) à une session Claude Code neuve, sur un autre compte. Écrit par `session_016QhUrudziqEQujXt4ofM8u` ;
à coller tel quel comme premier message. Ne se réécrit pas (R12). Il **remplace pour l'état et l'ordre** les briefs
`…/2026-11-14-0929-brief-lancement-session-neuve-temoin-bailey.md` et `…/2026-11-14-2305-brief-session-neuve-temoin-bailey-relance-en-retard.md`,
qui restent la référence pour les cloisons, les interdits et les étapes 5 et 6 (verdict, passation).

## Qui tu es
La session « attaquant informé » du programme « Contrôle boîte blanche des menaces diffuses », pour le seul témoin de
l'attaque publiée de Bailey et collègues. Français, tu tutoies Lazar, presque aucun acronyme, verdict d'abord.

## Dépôt
`https://github.com/lciric/controle-ia-travail` (privé), branche **`claude/compassionate-meitner-d4ryyk`**. `git fetch`
avec refspec explicite (`+refs/heads/claude/compassionate-meitner-d4ryyk:refs/remotes/origin/claude/compassionate-meitner-d4ryyk`,
et `+refs/heads/main:refs/remotes/origin/main` pour les GO). Pousse seulement sur cette branche (`git pull --rebase`
puis `git push origin HEAD:claude/compassionate-meitner-d4ryyk`, 4 essais) ; jamais sur `main` sans le mot de Lazar ;
jamais vers `lciric/controle-ia`.

## Lis, dans cet ordre
1. `registres/passations/2026-11-15-1843-passation-attaquant-informe-temoin-bailey-fin-relance-choix-en-attente.md`.
2. Le préenregistrement `prereg/temoin-attaque-publiee-bailey-v1.md` (`fb6c2f34…`) : « Critères de lecture gelés »,
   l. 160-176, 326-375, « Audit de symétrie (R4) » ; ses addenda 1 à 6.
3. `docs/notes/reproduction-attaque-publiee-v1/conception-continuation-relance-v2.md` (`6651a07f…`) et sa
   contre-lecture de la v1 (`contre-lecture-conception-continuation-v1.md`, `1da5b75f…`), seulement si Lazar choisit 2
   ou 3.

## Routine de reprise (R14), sans lire `registres/etat.md` (cloison)
Empreintes de `docs/` ; `verifier-arbre` (113 problèmes connus au 15 novembre : les consigner, ne pas les corriger) ;
`vastai show instances` (aucune instance du témoin attendue ; ne touche à aucune autre) ; liste des serveurs Hetzner
(identifiants et noms seulement) ; essais `tests/test_temoin_bailey_condition6_v20.py` et
`tests/test_temoin_bailey_reprise_relance_v1.py` (installer `requirements-cpu.txt` et `pandas` ; 219 passés, 4 sautés
au 15 novembre).

## État (15 novembre, 18:43Z)
Relance finie par la garde à B − 2 : **36 tours complets**, aucune garde tombée, D = 73,026 USD sur B = 75, instance
détruite, transfert complet. Dossier de lecture assemblé : `runs/temoin-bailey-v1-20261111/lecture-assemblee-v1/`
(44 empreintes vérifiées). Verdict **non lancé**. **Choix de Lazar en attente**, à faire avant toute lecture du
verdict (R1, R4) :
1. verdict à 36 tours, régime réduit (l. 165, 332), puis fin (recommandé, confiance moyenne) ;
2. run neuf de 72 tours, préparé à froid (≈ 165 à 230 USD, devis fragile) ;
3. continuation v2 depuis la sauvegarde (≈ 140 à 195 USD, neuf écarts au texte).

## Prochaine action
Demander à Lazar son choix (1, 2 ou 3), au format de décision du `CLAUDE.md`. Puis :
- **Choix 1** : verdict R13 par un sous-agent neuf, ni auteur du préenregistrement ni de l'analyse, sur
  `lecture-assemblee-v1` : `lecture_v8.valider`, puis `lecture_v8.lire(v, analyse_v3.graines()["reechantillonnage"])`,
  et l'audit de symétrie du texte, sans rien changer ; rapport scellé ; soumis à Lazar pour GO. C'est le seul moment où
  les notes sont lues. Ensuite, destruction du serveur Hetzner 176187199 par son identifiant (R10) et consignation
  (`registres/arrets.md`, `registres/depenses.md`) ; rappeler à Lazar de retirer la clé de déploiement
  `diag-temoin-bailey-depot-20261115`.
- **Choix 2 ou 3** : rien n'est lu ; addendum scellé et contre-lu (R2), GO hors enveloppe à inscrire sur `main` par la
  session mère, code et essais ; le verdict à 36 tours reste celui du texte et se fait après le scellement de
  l'addendum. Pour 3, garder 176187199.
- Passation à la fin (R14).

## GO en cours
`GO-2026-11-10-10` (part du témoin : B = 75, garde B − 2, échéance 2026-11-30), amendé par `GO-2026-11-11-01`, modèle
`GO-2026-11-11-02` : **épuisé** (D = 73,026). Toute dépense nouvelle de carte : hors enveloppe, nœud, mot de Lazar et
ligne neuve sur `main`. Serveurs Hetzner : ligne « go c » (5 USD), à inscrire par la mère.

## Clés et réglages à recréer sur le compte neuf (par leur nom seulement ; jamais de valeur dans la conversation)
- Réseau autorisé : `console.vast.ai`, `api.hetzner.cloud`, `github.com` ; pour 2 ou 3 seulement : `huggingface.co`,
  `*.hf.co`, `cdn-lfs*.huggingface.co`.
- Secrets d'environnement : `VAST_API_KEY` ; `HCLOUD_TOKEN` (jeton de l'API Hetzner, lu par son nom dans l'en-tête
  `Authorization: Bearer`) ; `HF_TOKEN` (pour 2 ou 3 seulement) ; écriture GitHub sur `lciric/controle-ia-travail`.
- Poser les secrets **avant** d'ouvrir la session (constat des sessions précédentes).
- Limites connues de l'environnement : le mandataire ne passe que le HTTPS (pas de `ssh` sortant) ; tout accès à une
  instance passe par un serveur Hetzner jetable piloté par l'API (modèles :
  `runs/temoin-bailey-v1-20261111/diagnostic-hetzner-v1.sh`, `sauvegarde-sondes-hetzner-v2.sh` et leurs constructeurs) ;
  la garde de calcul du dépôt bloque `vastai create ssh-key` (clé à poser par l'interface web de Vast, consigné).

## Machines et serveurs tenus par cette session (la mère n'y touche pas)
Hetzner **175884265** `poste-temoin-bailey-v9` (sans tâche, gardé sur consigne de Lazar) ; Hetzner **176187199**
`sauvegarde-temoin-bailey-v2` (sauvegarde des sondes et paramètres des tours 0 à 36, `/root/sauvegarde`, listes dans
`runs/temoin-bailey-v1-20261111/sauvegarde-sondes-v2/`). Aucune instance Vast.

## Cloisons et interdits
Inchangés (brief `…-0929-…`) : aucune note ni `notes-v3.jsonl` ni `technique-v3.jsonl` lus avant le verdict, sauf par le
lecteur du verdict ; ne lis jamais le coffre (`donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`,
`docs/notes/bras-attaque/`), `docs/notes/programme-et-4-familles-evasion/`, les lignes R-604 à R-610 de
`registres/decisions.md`, `registres/etat.md` ; aucune valeur de clé (`env`, `printenv`, `/proc/*/environ`) ; arrêts par
identifiant ou PID seulement (R10) ; aucune instance neuve, relance ni série sans mot de Lazar et addendum scellé ;
aucune pièce scellée réécrite (R12).

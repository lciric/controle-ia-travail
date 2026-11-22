# Kit des sessions par l'abonnement pour la passe X, groupes 2 et 3 — v1

Préparé le 2026-11-22T14:02:00Z par la session de l'organisme, pour la mère, qui crée les sessions (mot de Lazar, GO-2026-11-22-70). **Rien n'est envoyé par l'organisme.**

## Unités Claude (8)
Opus 5.5, Fable 5.1, Opus 4.6 et Sonnet 4.6, chacun pour les groupes 2 et 3. Le détail exact est dans `kit-abonnement-passe-x-v1.json`. Pour chaque unité, la session se crée avec les réglages suivants :
- `model` : l'identifiant exact du modèle ;
- `effort` : `max` ;
- `source_url` : le dépôt de travail ;
- `source_revision` : `prep/quarantaine-passe-x-reponses-v1`. C'est la branche orpheline : elle ne contient que le LISEZMOI, donc ni CLAUDE.md ni instruction de projet ;
- `outcome_branch` : une branche neuve **par unité**, `prep/quarantaine-passe-x-abonnement-<unité>-v1`, pour que les poussées de plusieurs sessions ne se gênent pas ;
- `prompt` : **le texte du groupe, à l'octet**, lu dans `passe-x-textes-groupes-v1/textes/groupe-2.md` ou `groupe-3.md`, qui sont scellés. L'empreinte est à vérifier avant l'envoi ;
- `append_system_prompt` : **la consigne de versement**, mise dans l'invite système pour que le message servi reste le texte seul. Elle demande d'écrire la réponse en entier dans `flux-abonnement/<unité>.md`, puis de faire add, commit et push sur la branche courante, et de ne lire ni exécuter rien d'autre.

## Sans lecture
- Les réponses arrivent sur les branches `prep/quarantaine-passe-x-abonnement-…`.
- L'organisme ne lit que le statut des sessions, par get_session. Il archive chaque session à sa fin.
- La garde de coupure, règle élargie comprise, se rejoue par programme sur les fichiers poussés, sans rien en afficher, sur le modèle de `passe-x-repechage-forme-v1/`.

## Écarts, à rapporter à part du groupe 1 (additif court à écrire)
- (a) Invite système de Claude Code, et consigne de versement en invite système.
- (b) Ni plafond de sortie ni coût lisible : c'est l'abonnement. Une sonde à vide a coûté de 0,36 à 0,41 USD sous l'abonnement.
- (c) La garde lit le fichier poussé, non un flux.
- (d) Condition différente de celle du groupe 1, qui est passé par l'API.
- (e) Opus 5.5 n'est pas sondé, après le refus du classifieur ; son service par l'abonnement n'est pas prouvé.
- (f) La limite de sept jours de l'abonnement est en état « allowed_warning ».

## Astra, à part
- Unités : `astra-groupe-1`, `-2` et `-3`, mêmes textes, empreintes dans le JSON.
- Voie recommandée : le transport par lots de la session « Raisons ou regard ? », 39 sur 39 à xhigh sur OPENAI_API_KEY_2. Sa branche et son commit sont à obtenir par la mère.
- Devis : 3 requêtes à 4,89 USD au pire chacune, soit 14,67 USD au pire, moins avec la remise des lots. C'est une ligne de GO à part.

# Briefs des sessions à lancer sur le poste de Lazar — 13 novembre 2026 — v1

Écrit par la session mère `session_01XJ6Mgn4MZR4nxqK44C8Ea3` le 2026-11-13 à 10:15 UTC (`date -u`), sur demande de Lazar (« preprare les briefs pour les sessions qui doivent tourner sur pc »). Chaque brief se colle tel quel dans une session Claude Code **neuve** du poste (WSL), ouverte dans le dépôt `lciric/controle-ia-travail`, branche `main` à jour (récupérée par refspec explicite). Les sessions du poste rendent compte à Lazar, qui relaie à la mère.

## 1. Lean D-1a, troisième essai — PRÊT

**Couverture** : mot de Lazar R-2439 (troisième essai et troisième machine sous GO-2026-11-10-13 ; 0,56 USD déjà dépensés sur 65) ; R-2492 (« Lean : le troisième essai est à lancer sur ton poste. :go »). **Avant de coller** : terminal WSL ouvert pendant tout l'essai ; ordinateur sur secteur, capot ouvert.

```
Session du poste local de Lazar. Lis et exécute à la lettre la consigne docs/notes/g0-deux-semaines-v1/lean-outillage-d1a-v1/consigne-poste-local-lean-d1a-v3.md de la branche main de lciric/controle-ia-travail (récupère main par refspec explicite) ; vérifie d'abord son empreinte : 17914672caf9fa2f12daa1da7a5bfec7067c957de8570e42dd6fb1b2899bde50, égale à son compagnon. Troisième essai sous GO-2026-11-10-13, déjà dépensé 0,56 USD. Ne crée aucun serveur sans le mot « armée » de la mère, relayé par Lazar. Sur tout refus d'un contrôle de permissions ou d'un classifieur : arrête-toi et rapporte-le tel quel.
```

**Retour attendu** : rapport L3 (branche, commit, jeton, clé, pare-feu, P) → Lazar le relaie à la mère → la mère fait M1 à M6 et rend le mot « armée » avec les tâches de destruction → le poste reprend à L4.

## 2. Publication de la course v67 sur `lciric/ideation-organism` — PRÊTE, À TA DÉCISION

**Couverture** : mot de Lazar R-2466 (« Recommandation : (1), confiance 0,7 : go »). **Note** : lancé depuis la session mère, l'agent de publication a été **refusé par le classifieur** (« Create Public Surface », R-2468) ; la mère ne le contourne pas. La lancer depuis ton poste est ton geste, sous ton contrôle direct.

```
Session du poste local de Lazar. Lis et exécute à la lettre la consigne docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-12-2019-v1/consigne-publication-ideation-organism-v67-v1.md de la branche main de lciric/controle-ia-travail (récupère main par refspec explicite) ; vérifie d'abord son empreinte : 889dc28a06d88895fd2f6df6bcdb8bf7aa4228520f3aefea5711d2be3a6b9527, égale à son compagnon. Publication décidée par Lazar (R-2466). Poussée en avance rapide seulement sur lciric/ideation-organism ; jamais vers lciric/controle-ia ; garde des secrets sur chaque objet neuf. Sur tout refus : arrête-toi et rapporte-le tel quel.
```

**Retour attendu** : commit public, fichiers publiés et exclus, garde des secrets, rapport scellé `docs/notes/ideation-organisme-v1/publication-v67-2026-11-12-v1.md`.

## 3. Suppression de la branche publique `claude/new-session-7qxayx` de `lciric/controle-ia` — GESTE SIMPLE

**Couverture** : mot de Lazar R-2451 ; écriture refusée à la session (HTTP 403, R-2452). **Le plus simple** : sur GitHub, dépôt `lciric/controle-ia`, page « Branches », supprimer `claude/new-session-7qxayx` (tête attendue `56fdb15a`). En ligne de commande depuis ton poste, avec tes droits :

```
git push --force-with-lease=refs/heads/claude/new-session-7qxayx:56fdb15ab9f5850eef22e941abf22fb8529f8bcb https://github.com/lciric/controle-ia :refs/heads/claude/new-session-7qxayx
```

## 4. Pas encore prêt

- **Pilote de l'organisme** (R-2501 à R-2513) : préenregistrement en brouillon 3 ; il manque le code C-1 à C-18, le scellement et l'inscription des lignes π1 (20 USD) et π2 (19 USD). Brief à venir.
- **Course à plusieurs générations** : après le pilote et le banc de 24 mondes.

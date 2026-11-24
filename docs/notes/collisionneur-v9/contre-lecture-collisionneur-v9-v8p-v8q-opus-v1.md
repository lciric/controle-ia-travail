# Contre-lecture des collisionneurs v9-v8p et v9-v8q (garde d'entrée de l'arrière-plan, rejugement nommé)

- **Classe B.** Auteur : session fille des collisionneurs (Opus 5.5). Contre-lecteur : un Opus 5.5 neuf, sous-agent, distinct de celui du v8n et du v8o, qui n'a pas écrit le code ; aucun réseau ; essais sur des copies. 24 novembre 2026.
- **v8p** (1df9d4ce…) : « conforme avec remarques », aucun défaut bloquant.
  - Le changement est limité à la voie en arrière-plan ; `verifier` donne la même sortie qu'en v8o sur les quatre dossiers qui ont un journal.
  - Garde × 4 : admise à 221 764 jetons, arrêt à 221 765. Plancher de coût juste.
  - Rejugement : chaque condition faussée une à une donne un refus ; aucune double multiplication ; idempotent.
  - Devis : l'entrée de Google est bien comptée × 4.
  - Trois remarques, corrigées dans le v8q (Q1 à Q3).
- **v8q** (5f7b7a7e…) : vérification par le même contre-lecteur : « conforme ». Les trois corrections sont faites et justes, et rien d'autre ne change.
- **Incident de lecture, déclaré par le contre-lecteur** : un premier `verifier`, lancé sur les dossiers du dépôt eux-mêmes, a réécrit `etat.md` dans trois runs suivis et créé `etat.md` dans le run de la dynamique de l'évasion. Il a tout remis en place (`git checkout` et suppression du fichier créé) ; `git status` est resté propre. Tous ses essais suivants ont été faits sur des copies.

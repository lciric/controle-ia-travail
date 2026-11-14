# Relecture courte des corrections par un sous-agent neuf de modèle C — rapport versé tel quel — v1

Versé par le préparateur (modèle A), le 14 novembre 2026 à 13:08 UTC. Relecteur : sous-agent neuf de modèle C (autre que le
contre-lecteur), lancé de 13:05:45 à 13:06:49 UTC (`date -u`) depuis la racine du dépôt, sans fichier écrit, outils
`Read Grep Glob 'Bash(unshare:*)' 'Bash(sha256sum:*)' 'Bash(ls:*)' 'Bash(wc:*)' 'Bash(diff:*)'` ; consigne :
`contre-lecture/consigne-relecture-courte-v1.md` (`f6774130…`). Il n'a joué aucun essai : le harnais refuse `unshare`
aux sous-agents (« ce que lance unshare ne peut être vérifié avant l'exécution »). À 13:05:45, les résultats des essais et des
bancs v3.2.1 et v2.1 n'étaient pas encore versés (ils l'ont été ensuite : voir `rapport-v1.md`, § 4 et 5). Après le trait :
sa sortie, octet pour octet.

---

# Relecture courte des corrections — relecture exploratoire v2 → v2.1 / v3.2.1

**Verdict : suffisantes sous conditions.** Les douze constats sont traités à des degrés divers. Je n'ai trouvé aucun défaut bloquant. Je n'ai pas pu jouer les essais : le harnais a refusé chaque appel `unshare` (voir « Ce que j'ai joué »). Deux traces annoncées manquent aussi : les bancs de mutations et les essais rejoués sur les versions neuves.

## Constat par constat

| Constat | État | Note |
|---|---|---|
| M1 séparation « de forme » | traité | `classer…v3_2_1.py` renomme les issues. La table de puissance est juste : j'ai recalculé p(13,1)=0,0376, p(12,1)=0,058, p(12,0)=0,0096 et p(10,0)=0,026. |
| M2 hasard reconnaissable | traité | Générateur v2.1 et quatre contrôles ajoutés. Les traits restants sont déclarés aux § 9.10 et § 5. |
| M3 vocabulaire du catalogue | traité | § 9.9 de la règle v2.1. |
| M4 plafond | traité | 6,50 USD dans le devis v2. Plafond minimal en sortie ×3 : 6,32. Seuil du premier appel : (6,5−1,114)/16,2 ≈ 0,33, exact. |
| M5 statut des relecteurs | partiel | Le § 4 dit désormais « même compte, hors GO ». Mais `regle-v2-1.md:98-103` garde « lancé hors du dépôt » et « aucun appel payant » juste avant. La question de la ligne de dépense est renvoyée à la mère, sans réponse. |
| M6 exactitude circulaire | traité | § 7 de la règle v2.1 : exactitude descriptive, consensus de deux relecteurs de modèle C pour les critères non porteurs. |
| m1 sous-règle du tour 2 | traité | Déclarée comme écart, avec les heures de scellement (12:11:21, relecteurs lancés à 12:11:36). |
| m2 verdict non lisible | traité | Mention « non lue » ajoutée, avec un essai neuf. |
| m3 codage du signe « 0 » | traité | Dit au § 5. |
| m4 T2-V strict | traité | § 9.11. |
| m5 réserve du lecteur | partiel | Dit « sans objet depuis R-2726 », mais « à confirmer par la mère ». |
| m6 bancs sans trace | partiel | Le banc v3.2 est versé : 30 sur 30. Aucun `resultat-mutations-*` ni `resultat-essais-*` n'existe pour le hasard v2.1 ni pour le classement v3.2.1. Seuls les programmes de mutations sont là. Dans `outils/`, seul le résultat v2 est versé. L'affirmation « rejoués sur les versions neuves » n'a donc aucune pièce. |
| m7 dossier supprimé en entier | partiel | « Limite conservée » est la réponse, mais la condition d'emploi (toute seconde préparation est un nœud) n'est écrite que dans la note des corrections. Je ne la trouve ni dans la règle v2.1 ni dans le devis v2. |

## Défauts neufs

- **Moyen — traces des bancs et des essais v2.1 / v3.2.1 absentes** (voir m6). Il faut les verser avant `preparer`, ou retirer l'affirmation.
- **Mineur — contrôle (4) assoupli après coup** : `outils/controler_temoins_v2_1.py` (contrôle 4, paramètre `pieces`) étend le « vocabulaire du domaine » aux pièces servies. L'écart est déclaré honnêtement (règle v2.1 § 5). Il a toutefois été décidé après un échec du contrôle. La règle ne dit pas combien de suites de quatre mots il a épargnées. Le résultat final est `remplissage_repete: []`.
- **Mineur — tolérance de rang changée** : la note des corrections fixait ± 0,15 pour la cible de chaque champ, la règle v2.1 dit ± 0,08. C'est plus strict, mais l'écart n'est pas signalé. L'ajout « fiche refaite si la longueur sort des bornes réelles (T2-H6) » ne porte que sur la longueur.
- **Mineur — stats d'entrée** : le contrôle lit `resultat-stats-forme-reelles-et-temoins-v1-v1.json`. Il s'agit des statistiques des réelles, donc sans conséquence. Le nom prête à confusion.
- **Mineur — `regle-v2-1.md:103`** : voir M5.

**Questions de la consigne :**
- **Hasard v2.1** : d'après les diffs et le résultat des contrôles, il a été réglé sur le style et la longueur seulement. Chaînes, signes et urnes sont inchangés. Le compte de 6 chaînes cohérentes sur 8 est déclaré comme vu à chaque essai.
- **Contrôles** : les quatre contrôles neufs sont tenus dans `resultat-controles-temoins-v2-1.json`. L'écart au contrôle (4) est honnête (voir plus haut).
- **Outil v3.2.1** : d'après le différentiel, il ne change que `VERSION`, les deux pièces épinglées (hasard v2.1 et règle v2.1) et les noms de fichiers dans les docstrings.
- **Classement v3.2.1** : le différentiel ne change que le chargement de l'outil, les noms, les issues renommées et la mention « non lue ».

## Ce que j'ai joué

- **Les deux fichiers d'essais** : non joués. Cinq tentatives `unshare -n env … .venv/bin/python -B -m pytest …` ont été refusées par le harnais (« What 'unshare' starts can't be checked before it runs »), depuis la racine et depuis `RE/`. Je ne l'ai pas contourné.
- **Sondes Python** : aucune.
- **Lu** : le premier rapport, la réponse, tous les différentiels demandés (règle, outil et classement v3.2.1, contrôles ; essais v3.2.1 en tête de fichier ; essais v2.1 par liste des tests ajoutés, 6 neufs), le devis v2, le résultat des contrôles v2.1, le banc v3.2.
- **Refait à la main** : la puissance exacte du test de R7 et les seuils du devis.
- **Pas ouvert** : les fiches réelles, les notes du juge, les envois et réponses.

## Réserves

- Les trois questions sur les essais restent sans réponse (rien n'a été joué). Je ne peux pas confirmer « 0 échec » ni la couverture des quatre contrôles neufs par mutations.
- Je n'ai relu ni le texte du hasard v2.1 ni le code de `tirer_fiches_hasard_v2_1.py` en entier. Mon jugement sur le « style seulement » repose sur la note, la règle et le résultat des contrôles, pas sur une lecture du code.
- **Conditions avant `preparer`** :
  1. verser les essais et les bancs sur v2.1 et v3.2.1 (0 échec, 0 mutant vivant) ;
  2. écrire la condition d'emploi de m7 dans une pièce scellée ;
  3. lever l'ambiguïté de `regle-v2-1.md:103` ;
  4. faire trancher M5 par la mère.

# Rapport de sous-agent (texte de modèle, non opposable)

## Verdict
1. **Le brouillon 5 est scellable après les couples T101 à T112.** Ce sont des changements de texte seulement : ni le code, ni les essais, ni le plan, ni le bloc d'empreintes ne bougent. Il reste aussi la case `configuration_sha256`. Aucun bloquant.
2. B10 et I25 à I31 sont traités. Chaque point est prouvé sur le code gelé, avec ses essais et ses mutations nommés. Les changements du brouillon 5 n'ont rien cassé :
   - Seul GO-2026-11-02-23 est cité, et 50 = 44 + 6 au centime.
   - La borne de 0,80 USD couvre les 12 tours ; le devis refait de façon indépendante redonne la table au centime.
   - La garde des rôles rend le code 2 avant toute porte et tout appel.
   - Les 7 zones de l'étage 2 sont identiques à l'octet au brouillon 4 ; le seul marqueur hors zone est `<<CASE_CONFIGURATION_V3>>`.
   - Les 91 empreintes du bloc sont égales au disque et à `a12713a` (et aussi à `516feca`).
3. Un point important, I32 : les commandes des relais n'ont jamais joué les rôles de l'étage ni ses plafonds de session. Si une commande refuse une session, la course s'arrête sans issue, même quand c'est le vérificateur, qui n'est jamais décisif. Le remède est une annexe A.6 bis (couples T111 et T112) qui demande à la session-depot de vérifier ses deux commandes en lisant leur code, sans appel.

## Fichiers (deux fichiers neufs, aucun fichier existant modifié, aucun commit)
- `/home/claude/ideation-organism/orchestrator/prereg/contre-lecture-courte-preenregistrement-tour-ferme-v5.md` — sha256 `3b525f9e86b239d4e6dd3b3fa8825a67151342f6487138f7ddd07f56e17c9695` (424 lignes)
- `/home/claude/ideation-organism/orchestrator/prereg/couples-contre-lecture-tour-ferme-v5.json` — sha256 `40bb0d178c967b7da7a5109ff402c674ab8e8e2ed09f34efcd93c88125e80474`
  - 12 couples `{id, constat, ancien, nouveau}`. Chaque « ancien » figure une seule fois dans le brouillon 5, et encore une fois au moment où on l'applique.
  - Contrôlé après application : zones et marqueurs inchangés, plan et bloc inchangés, garde 6 complète acceptée sur une copie scellée.
- Scripts et sorties : `/tmp/claude-0/-home-claude/03748db6-42ca-5241-871c-5399d39c1451/scratchpad/tour-ferme-clc5/`

## Rejoué (heures `date -u`)
- **Essais v63, commande demandée :** 87 réussis et 23 sous-essais, 124 s, code 0, de 19:39:20 à 19:41:25. `BacReelV63` a bien tourné, sans saut.
- **Banc `--seulement sonde --raisons` :** les 10 mutations sont tuées pour la raison attendue ; témoin de 24 essais avant et après ; de 19:42:13 à 19:43:34.
- **En plus :** les 3 mutations des rôles et les 3 d'I30 sont tuées (19:49).
- **Chemin réel `--verifier-seulement`**, sur une copie scellée du brouillon 5, avec la vraie ligne GO-23 du registre :
  - avec une configuration en forme du 1er novembre (pièces factices, plafond mis à 50) : « conforme » ;
  - avec Kimi déclaré `kimi_protocole` : code 2, avec le message de l'annexe A.6.

## Constats
- **I32** : les commandes des relais doivent accepter les rôles et les plafonds de session que le code leur passe. Le vérificateur reçoit 0,1 USD, une valeur que le brouillon 5 n'a pas relevée. L'autre option, relever ce plafond, coûte plus cher : code neuf et parts à refaire. À 0,25 USD par session de vérificateur, le partage 44/6 ne tient plus, et 40/10 ne laisse que +8 cartes de marge.
- **Mineur 39** : le brouillon 5 n'écrit plus ce qui arrive quand la borne par carte mord (prix d'un tour au-delà de 0,067 USD). Couples T102 et T106.
- **Mineur 40** : la durée de 24 h coupe la course entière si elle mord. Son seuil écrit vaut pour un seul scénario : il tombe à environ 81 s par session à 60,7 cartes testées. Couples T103, T104 et T108.
  - **Décision pour Lazar :** passer à 72 h, sans coût en dollars, comme la reprise de l'attaque (GO-21). Je le recommande avec une confiance moyenne. Sans décision, on garde 24 h.
- **Mineur 41** : l'arrêt pour dépense arrive dès environ 55 cartes testées, pas seulement si le juge promeut presque tout. Asymétrie à déclarer (R4). Couple T107.
- **Mineur 42, hors du texte** : la ligne GO-23 du registre privé cite le code `af92034` et un « attendu ≈ 3,3 à 12 USD ». Le code gelé est `a12713a`, et le nouveau devis va jusqu'à environ 23,6 USD (26,1 si chaque carte atteint sa borne). Le lanceur ne lit pas ces champs. Une ligne de précision dans le registre, par le directeur, suffit.
- **Mineur 43** : dans la table du devis, la ligne recopie-mélange dit « ≈ 2,5 testés » au lieu de 4,8. Antérieur au brouillon 5, sans effet.
- **Mineur 44** : quatre phrases deviennent fausses au scellement (en-tête « non commités », section 10 bis, bloc « à revérifier après commit », section 14 point 2). Couples T101, T105, T109 et T110. Le titre et le statut restent à récrire par le directeur au moment du scellement.

## Bornes restantes (point 5)
Aucune ne rend une issue non concluante par construction. T1 à T5 et A4 peuvent tous tomber dans les deux sens. Celles qui le pourraient encore, et leur prix :

| borne | quand elle mord | prix pour l'écarter |
|---|---|---|
| 0,80 USD par carte | seulement si un tour dépasse 0,067 USD en moyenne | 1,00 USD par carte : marge de +12,2 cartes au lieu de +23,2 |
| parts 44/6 | arrêt dès environ 55 cartes testées à la borne | couvrir le maximum de 144 cartes : environ 130 USD |
| durée 24 h | voir mineur 40 | 72 h : 0 USD |
| délai de 1 800 s par appel | un appel pendu, donc arrêt | code neuf |
| plafond de session des proposeurs | un dépassement, donc arrêt | aucun, s'il est pris large |
| trou du gardien sur la fréquence et la phase d'oscillation | probabilité d'environ 10⁻¹⁵ par tirage | borne au gardien, code neuf |

## Pour le directeur (privé, absent du fichier public)
- La configuration du 1er novembre (empreinte `4ae5a1e0`) met déjà Kimi et Argon en `commande_externe`, avec `plafonds_session.proposeur` = 1,8.
- Les deux commandes ont des options de sortie qui dépendent du rôle (`--max-sortie-court` 16000 pour Kimi et 4000 pour Argon ; `--sortie-min-jetons` 4096 et 1000 ; `--delai-s 1750`). Ce sont précisément ces options que A.6 bis demande de confronter aux plafonds de 0,1 USD (vérificateur) et au reste de la borne de 0,80 USD (expérimentateur).
- Pendant ma lecture, d'autres tâches ont committé `516feca` et modifié `pole/juges_idees_v2.py`. Aucun de ces fichiers n'est dans le bloc gelé, et j'ai revérifié les 91 empreintes à 20:08 UTC.
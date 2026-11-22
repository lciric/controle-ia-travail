# Vérification des corrections du lot B1 du pilote « oracles plantés » — v1

- Nature : vérification des corrections (classe B, même contre-lecteur que `contre-lecture-code-lot-b1-v1.md`, `305bb4a3…`). Le 2026-11-22. Opus 5.5. Processeur seul, 0 USD, aucun appel de modèle, aucun réseau. Commit vérifié : `644ea957`.
- Lu : `reponse-contre-lecture-lot-b1-v1.md`, `note-choix-implementation-lot-b1-v2.md` (lignes 24 à 47), les écarts entre `oracles_plantes_v1` et `oracles_plantes_v2` (grammaire, normaliseur, tests de mort, lignée, familles, mondes, paramètres), et `tests/test_oracles_plantes_v2_contre_lecture.py`. Aucun fichier cloisonné ouvert.
- Lancé : `pytest -q tests/test_oracles_plantes_v2_*.py`, 147 passés. Mes sondes rejouées sur la v2, et cinq sondes neuves dans le bloc-notes (`v2_sondes.py`, `v2_chaine.py`, `v2_etage2.py`, `v2_r5.py`). Aucun fichier du dépôt modifié, sauf celui-ci.
- **Bilan : 8 corrections tiennent, 1 tient avec réserve, 1 ne tient pas (remarque 10, avec une régression bloquante : une vérité plantée peut de nouveau mourir par héritage). Les remarques 7 et 12 sont bien renvoyées, non tranchées. 3 remarques neuves : 1 bloquante, 1 à corriger, 1 mineure.**

## Par remarque

| remarque | verdict | preuve |
|---|---|---|
| 1. NAT entre parenthèses | **tient** | Rejeu de la sonde 1 : `(… NAT …) et vrai`, `ou faux`, `vrai et (…)`, `non (…)` sortent tous « informe », sans arrêt. Le cas sain `pour tout n dans NAT, (pour tout m dans NAT, …)` reste vivant. Le contrôle est fait sur l'arbre, quel que soit le chemin d'analyse. |
| 2. L'indéfini effacé par le normaliseur | **tient** (pour l'étage 1 ; voir la remarque 13 pour les étages 2 et 3) | Rejeu des sondes 1 et 5, sur un registre unique : la variante de Cassini en `+ w(n - 1) - w(n - 1)` meurt, puis la vérité de Cassini reste vivante. `w(n - 1) * 0 = 0` meurt, puis `n + 1 > n` sort triviale et vivante. Les sous-termes partiels sont enregistrés avant toute simplification (`normalisation.py:209`, avant l'évaluation à argument littéral et avant les règles du monde). |
| 3. Profil : « hors capacité » compté comme informatif | **tient** pour T5 redite ; voir la remarque 13 | Rejeu de la sonde 3 : `mod(w(30n), w(n))` contre `mod(w(30n), w(3n))` donne « non redite ». Mais l'exclusion des positions H n'est pas transitive, et elle ouvre l'héritage en chaîne de la remarque 13. |
| 4. Tête de chaîne du registre | **tient avec réserve** | Rejeu de la sonde 3 : troncature, dernière ligne modifiée et tête retirée sont refusées. Réserve, déjà écrite par l'auteur : qui réécrit le registre et sa tête n'est pas vu. La tête finale est à consigner au manifeste de la course ; aucun code ne le fait encore (lot B3). |
| 5. Flottants dans les paramètres | **tient** | Sonde `v2_r5.py` : AV = 1.5, alpha à 1.5, alpha à `True`, N = 10.0 et D = 20.0 sont refusés ; `60.0` et `6e1` sont refusés à la lecture du JSON. Le texte `"0.5"` est accepté et lu exactement (voulu). Résidu mineur : les capacités passent encore par `int(…)` (`evaluation.py`) ; elles ne viennent que du JSON, qui refuse les flottants. |
| 6. Fuite d'une instance indentée | **tient** | Rejeu de la sonde 3 : l'instance est détectée en JSON indenté et dans un dictionnaire imbriqué. |
| 7. Pièges reconnaissables à leur forme | **renvoyée, non tranchée** (conforme) | Note v2, ligne 46. Gabarits de F1, F2 et F3 et paramètres de plantation identiques entre la v1 et la v2 : l'écart ne porte que sur la lecture stricte des paramètres. |
| 8. Branche « contradiction » non exercée | **tient** | `test_r8…` asserte `MORTE_CONTRADICTION` sur `u(1000) - u(1000) = 1`, et constate que l'énoncé de la v1 meurt par contre-exemple. |
| 9. Mort par T6 inscrite d'office | **tient** | `appliquer_t6` inscrit la mort, avec le texte canonique et l'empreinte du monde ; vu dans `v2_chaine.py`. Une réfutation fausse n'inscrit rien (essai de l'auteur). |
| 10. Une morte reformulée survit | **ne tient pas** | Deux défauts. (a) La comparaison aux mortes par les étages 2 et 3 tue des énoncés vrais, des vérités plantées comprises : c'est la remarque 13, bloquante. (b) Une reformulation équivalente simple survit encore : c'est la remarque 15. Le cas de la contre-lecture (`u(k) <= c - 1`) hérite bien de la mort, comme `2 * u(n) < 2 * c` et `… et u(n) >= 0`. |
| 11. Contrôles du rejeu | **tient** | `test_r11…` : une triviale à la place d'une vérité est relevée en A1, comme un piège non décidé sous N dont l'instance de clé reste vérifiée. |
| 12. Enfant [9] et borne du profil | **renvoyée, non tranchée** (conforme) | Note v2, ligne 47 ; `graines.py` inchangé, borne du profil toujours 3N. Ajouter au point (b) que la v2 se sert désormais de ce profil pour l'héritage de mort, et plus seulement pour la redite (remarque 13). |

## Remarques neuves

### 13. L'héritage « par équivalence » tue des vérités plantées — **bloquante** (régression née de la correction 10)
- Lieu : `tests_de_mort.py`, `morte_equivalente` et son appel dans `appliquer_batterie` (v2) ; `profils_egaux`.
- Preuve, étage 2 (`v2_etage2.py`, racine 11, mondes 8 et 9, registre neuf) :
  - Une proposition soumise d'abord : `pour tout n dans NAT, (n >= 1 implique w(2 * n) = w(n) * (w(n + 1) + QU * w(n - 1))) et (w(n - 1) > 0 ou w(n - 1) <= 0)`. Elle meurt par T2, indéfinie en n = 0.
  - La vérité plantée de duplication, soumise ensuite, sort « morte par héritage (table de vérité) ». Même chose pour la vérité d'addition, avec `w(m - 1)`.
  - Même chose pour `pour tout n dans NAT, n >= 1 implique (w(n - 1) > 0 ou w(n - 1) <= 0)`, qui est vrai, après la même formule sans garde.
  - Cause : la table de vérité est classique, alors que l'évaluation est de Kleene. Deux formules propositionnellement équivalentes, avec les mêmes sous-termes partiels, ne sont pas équivalentes quand une branche masque un indéfini. L'exigence « mêmes défs » est globale à la formule, pas instance par instance.
- Preuve, étage 3 (`v2_chaine.py`, racine 11, mondes 8 à 11 ; 8 cas sur 8, vérités de Cassini et de période modulaire) :
  - E = `pour tout n dans NAT, (corps de T) et n != 2` meurt par T2.
  - D = `… et (n != 2 ou u(1000) > 0)` ne meurt pas par T2 : il est hors capacité en n = 2. Il hérite pourtant de la mort de E par le profil, puisque les positions H sont écartées.
  - T, la vérité plantée, hérite ensuite de la mort de D, pour la même raison.
  - L'égalité de profils avec exclusion des H n'est pas transitive. La réserve de la note (« une vivante n'hérite que si son profil porte un F ou un I ») est vraie, mais ce F peut ne se trouver que dans un monde perturbé : elle ne garantit pas que l'énoncé soit faux dans le monde réel.
- Effet : un proposeur peut, sans le savoir et pour toutes les configurations (le registre est global), rendre « morte » une vérité plantée. Cela fausse « retrouvées » (H1, H2), soit ce que A1 garde pour la banque.
- Correction proposée (invariant sain) : n'hériter par les étages 2 ou 3 que si le candidat est lui-même F ou I dans le monde réel, à l'instance témoin de la morte (gardée au registre ; c'est le contre-exemple de T2 ou de T6). Une vérité plantée, sans F ni I jusqu'à 3N, ne peut alors plus jamais mourir par héritage, quel que soit le registre. L'étage 1 (même empreinte, défs comprises) peut rester tel quel. Essai à ajouter : pour chaque vérité plantée, aucun contenu de registre, ni ceux des sondes ci-dessus, ne la tue.

### 14. Une mort par vacuité empoisonne la forme « vrai » — à corriger (présent déjà en v1, non relevé alors)
- Preuve (`v2_sondes.py`) : `pour tout n dans NAT, n > N + 5 implique 0 = 0` meurt par T3. Sa forme normale est « V ⟂déf{} ». Ensuite `pour tout n dans NAT, n + 1 > n` et `1 = 1` meurent « par héritage » au lieu d'être triviales.
- Effet : les comptes de triviales et les motifs de mort sont faussés. La précision n'est pas touchée : une triviale ou une morte sort du numérateur dans les deux cas. Aucune vérité plantée n'est touchée.
- Correction : ne pas inscrire pour l'héritage une mort par vacuité dont la forme est close (V ou F), ou faire porter à l'empreinte le motif de la mort. La règle de la remarque 13 suffit aussi : `1 = 1` n'est faux nulle part.

### 15. Une variable muette suffit à faire survivre une morte reformulée — mineure (limite de D-M5, à écrire en réserve)
- Preuve (`v2_chaine.py`, piège `seuil_u` du monde 8, tué par T6 en n = 40) : `pour tout n dans NAT, pour tout m dans NAT, m = n implique u(m) < c` et `pour tout n dans NAT, pour tout j dans [0 .. 0], u(n + j) < c` restent vivantes. Le squelette diffère, donc l'étage 3 n'est pas essayé ; les défs diffèrent, donc l'étage 2 non plus.
- L'équivalence générale est indécidable : ce n'est pas un défaut de calcul, mais la réserve de la note v2 (ligne 32) doit dire que D-M5 n'est couvert que pour les reformulations de même squelette.
- Correction possible, si le concepteur veut la couvrir : pour une morte par T6, réévaluer chaque candidat vivant à toute instance jusqu'à 3N dont la projection redonne le témoin de la morte. Cela revient à lire la vérité au-delà de N : à trancher avec la remarque 12.

## Ce qui reste à faire avant la vérification suivante

Corriger la remarque 13 en version neuve, avec l'essai d'invariant sur les vérités plantées ; traiter la remarque 14 ; écrire la réserve de la remarque 15. Les sondes `v2_etage2.py` et `v2_chaine.py` du bloc-notes rejouent les preuves.

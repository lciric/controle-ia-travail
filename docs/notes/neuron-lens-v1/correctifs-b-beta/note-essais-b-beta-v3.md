# Essais du correctif (4) et de l'estimateur sur un Llama miniature — état après la vérification des versions 2 (note v3)

Écrit le 2026-11-18 à 04:47 UTC (`date -u`) par la session `session_01XJ6MgmvmAAZ9h382ct8kHk`. Complète `correctif-lens_compare-llama-v2.md`
(`5c7b3312…`), sans la réécrire, selon la vérification par un agent neuf `verification-correctif-4-et-essais-v2.md` (`4ed8e71c…` :
diff v2 et essai de `lens_compare` v2 **employables** ; essai du Llama miniature v2 et note v2 à corriger ; 0 bloquant, 1 majeur,
9 mineurs). L'heure « vers 04:50 » de la note v2 était approximative : elle a été écrite avant 04:44.

## Pièces employables, retenues pour la commande
- `lens_compare-llama-v2.diff` (`f85c36db…`), fichier corrigé `c974cc1a…`.
- `essai-lens_compare-llama-v2.py` (`94e5a7d7…`) : **10 tests** attendus, tous passés, aucun sauté. Il lit le fichier publié par
  `git show HEAD:…` : la commande exige que l'arbre voisin de la course soit au commit `849bfe1678e28becceb1e3864afe5fc8297d02e4`, correctifs
  appliqués **sans commit**, et le vérifie (`git rev-parse HEAD`) avant l'essai (mineure de la vérification).

## Essai du Llama miniature, v3 (`essai-transport-llama-miniature-v3.py`, `da0f0efc…`) — remplace la v2
- **Majeur levé** : la seconde partie emploie désormais **le critère exact du dépôt**, `torch.allclose(estimation, force brute,
  atol=1e-4)` avec sa tolérance relative par défaut (10⁻⁵), et non plus un écart absolu de 10⁻⁴ plus sévère. La note v2 disait « aucune
  tolérance changée » à tort pour la v2 ; c'est vrai pour la v3.
- **Mineure levée** : l'artefact du décalage de 10⁻³ est joué **famille par famille** (R `out`, R `mid`, S), et chaque artefact exige des
  échecs dans sa seule famille ; l'artefact « autre modèle » est gardé.
- Attendu : **11 tests** passent (2 recopiés, 2 de base, 2 aux traits de Llama 3.1, 1 contrôle des fréquences, 3 décalages, 1 autre
  modèle), aucun sauté. `transformers` **5.18.0** (celle de la tranche des lentilles publiques, addendum de B-α partie 2, l. 65) ;
  vérifié hors du voisin, avec 5.18.0 comme avec 5.23.0 : la configuration aux traits de Llama 3.1 se construit et la fréquence basse
  passe de 1,414·10⁻³ à 5,248·10⁻⁴.
- Essai renforcé accepté par la mère (R-3180) ; à déclarer dans l'addendum de la tranche et dans la commande.

## Mineures de la vérification renvoyées ailleurs
- L'artefact « signe inversé » de la garde (d) et la sortie « essai en échec » que P.4 attend pour le code des verdicts : fournis par
  le code de course (copie de l'essai avec une estimation faussée, jouée dans la commande ; son échec attendu est consigné).
- La marge de demi-précision (0,012) : l'essai de `lens_compare` ne code aucune valeur en dur ; sans effet.
- La sortie des contrôles statiques en fichier : versée avec les essais de la commande.

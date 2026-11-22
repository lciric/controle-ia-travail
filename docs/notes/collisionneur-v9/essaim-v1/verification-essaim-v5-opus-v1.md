# Vérification de l'essaim v5 : conforme

Objet : le programme `collisionneur_v9_essaim_v5.py` (f2593ce9…), sur le moteur `collisionneur_v9_v8e.py` (0d591933…). Les 52 essais passent. Aucun réseau, aucune clé, dépôt intact (`git status` vide). Toutes les copies sont restées dans le bloc-notes : le chemin du moteur y est absolu.

## Bloquant : aucun

- **Mon bloquant de la v4 est corrigé** (ligne 934) : la borne du brouillon prend le plus grand de `max` et `max_relance`. L'essai Astra prend la mutation qui remet `max` seul.

## Passage au moteur v8e : rien de cassé

- **Empreinte du moteur :** contrôlée au chargement (mutation prise).
- **Temps 0 :** c'est l'invite III.1 du moteur mot pour mot, avec la forme imposée des duels. L'essai le vérifie.
- **Clé `place_iii3` :**
  - elle est exigée, et une valeur absente ou fausse est refusée ;
  - elle est posée dans `lire_configuration`, que `lancer`, `devis` et `simuler` appellent avant toute invite ;
  - `simuler` sur la configuration pilote, qui porte `null`, est refusé proprement.
- **`verifier` et `bilan`** passent dans un processus neuf où la place n'est pas posée (essai à part dans mon bloc-notes) : ils ne lisent pas la consigne III.3.
- **`simuler`** donne des sorties identiques à celles de la v4 sur les sept dossiers finis.
- **`enveloppe`** refuse un rejeu donné seul, et refuse une liste de compositions mêlées.

## Non-bloquants

1. **`place_iii3` n'agit pas sur l'essaim.** La consigne finale ne garde que la ligne « Livrable », que les places « fin » et « avant-livrable » laissent identique. Les brouillons portent donc la forme imposée des duels, les finales non. Le développeur le déclare comme point ouvert pour Fable ; à trancher avant le pilote.
2. **Devis versé :** `devis-pilote-v5/devis-v5-{2,3,4}.txt` ne vient pas du programme commité. La ligne 23 dit « de la v8d », là où la v5 écrit « du moteur (v8e) ». Les chiffres sont identiques, mais il faut régénérer ces fichiers depuis f2593ce9 pour la provenance.
3. **Deux essais manquent :**
   - une configuration sans la clé `place_iii3` : la mutation E2 n'est pas prise, et une configuration sans la clé ferait sans doute tomber le programme sur une `KeyError` au lieu d'un refus propre ;
   - le contrôle `sha256_moteur` dans `verifier` : la mutation E4 n'est pas prise.
4. **Ancien format :** un journal de la v4, qui porte `sha256_v8d`, ferait tomber `verifier` sur une `KeyError`. C'est sans effet si aucun dossier v4 n'est repris.
5. **Redondance déjà signalée :** la garde « origine finie » d'un rejeu fait double emploi (Mc5).

## Devis v5 (question générale v2, place « fin », en USD)

| cycles | pire sans relance | pire avec relances | finales sans relance | finales avec relances |
|---|---|---|---|---|
| 2 | 48,78 | 126,34 | 13,02 | 33,53 |
| 3 | 65,40 | 167,97 | 13,56 | 34,74 |
| 4 | 83,54 | 213,04 | 14,10 | 35,96 |

Contre le plafond dur de 64 USD, le pire sans relance ne tient qu'à 2 cycles. Avec relances, il ne tient à aucun nombre de cycles.

## Mutations

**Prises (19) :**

- les dix mutations de la v4 sur les points (1), (a), (b) et (c) ;
- les mutations d'anonymat et de balises de la v4 : casse de la lettre de proposition, motif retiré, sans NFKC ;
- le refus de `--faits` différent de `--question` ;
- la balise dans `verifier`, désormais prise par l'essai neuf ;
- la borne qui oublie la relance ;
- la place non fixée ;
- l'empreinte du moteur.

**Non prises :**

- Mc5 (garde redondante) ;
- E2 (clé `place_iii3` retirée des clés exigées) ;
- E4 (contrôle `sha256_moteur` de `verifier`).

# Quatrième vérification : relance courte de la machine 61875617, brouillon 5 et script v4 (contre-lecteur 1, classe B)

Contre-lecteur : Claude Opus 5.5, le même que pour les vérifications précédentes. Heure : 2026-11-22, vers 12:52Z. Aucun appel au vrai loueur.

## Verdict : jouable

Le start attend en plus le mot de Lazar et les préalables P10 et P11.

## Empreintes (conformes à l'annonce)

| fichier | sha256 |
|---|---|
| `relance-courte-61875617-v4.sh` | `de06ed550c3d1fcae2b83c81c21faac27b75b5535dffac682a66e26e58c2ad69` |
| `texte-relance-courte-61875617-v1-brouillon5.md` | `f3e24cb52da0e412dc74806791e0d19fffda4f1a1fe18898a86c56907c77c20f` |
| `essais-blanc-relance-courte-v4-rejeu2.txt` | `4d13a4b4082551df69d521c8a1d238a0c3642f8d86ff5b2c5d05fb4cd4363517` |
| `differences-brouillon4-vers-5.md` | `b0b1f28bc089f754a8a5a293fc554a3b1407b974d30c31efee73c92581469042` |

Le texte cite le script v4 et son empreinte (l. 5, 27, 31).

## Corrections (diff entre le script v3 et le script v4)

Le diff ne touche que l'en-tête, `lister` et `archiver`. `jouer`, `decider`, `etat`, `arreter` et `secrets` sont inchangés : aucune régression des corrections R1, R2, B1 et M1.

- **A1, tenu.** La liste du contenu est lue par l'entrée standard (`cat … | tar -tvf -`), son code est lu, et le nombre d'entrées est comparé à celui que rend `find "$@"`.
- **A2, tenu.** Plus de tâche de fond. L'empreinte de l'archive entière est calculée sur le réassemblage, et le réassemblage est comparé aux sources par `tar -d`. Seuls les écarts de date, de propriétaire et de mode sont admis.
- **L1, tenu.** L'état est relu après la liste. Machine en marche, en `loading` ou en `scheduling` : arrêt par l'identifiant et code 1. État illisible : mot de la mère.
- **L2, tenu.** Une commande `execute` en échec est rejouée une seule fois, puis sa sortie est masquée.
- **E1, tenu** dans le texte (l. 31) : seules les traces ajoutées, lues dans `diff-name-status.txt`, passent à `archiver`.
- **Constat N9, vrai.** Les journaux vivent dans `/root/iib/`, hors du dépôt extrait (amorce l. 255). La consignation ne prend que `runs`, `diag` et les identifiants d'actions (l. 306-307), plus les 400 dernières lignes du journal (l. 295-303). Seule la fonction `traces()` (l. 351-354) prend le reste, et le chemin de redémarrage ne l'appelle jamais. Avec `ls`, `du` et `rm`, rien ne déplace un fichier : aucun moyen n'existe. Le refus de la mère est consigné et la décision renvoyée à Lazar.

## Essais rejoués avec mon faux outil (`scratchpad/verif-cl1-essais/`)

**Relance (`jouer`)** : aucun `destroy`, aucun autre identifiant.

| essai | cas | résultat |
|---|---|---|
| A | sain | conforme ; l'appel qui précède le `stop` est `logs` |
| B | tentative 1 refusée, puis poussée | conforme |
| F | poussée impossible | 2 `stop`, arrêt non confirmé, code 1 |

**Liste du disque (`lister`)** : aucun `rm` et aucun `start` dans tous les cas.

| cas | résultat |
|---|---|
| machine arrêtée avant et après | 3 `execute`, code 0 |
| machine en marche après la liste | `stop` par l'identifiant (2 au plus), code 1 |
| machine en marche avant | refus, aucun `execute` |
| premier `execute` en échec | 4 `execute` (un seul nouvel essai), code 0 |

**Archive (`archiver`)** :

| cas | résultat |
|---|---|
| 300 fichiers | 301 entrées sur 301, 34 morceaux, code 0 |
| petite archive | conforme |
| source modifiée après archivage | `tar -d` rend « Contents differ » : le garde voit l'écart |
| chemin inexistant | « ÉCHEC : tar ou split » |

## Mineur, sans effet

Le message « comparaison impossible (code ${PIPESTATUS[1]}) » relit `PIPESTATUS` après le test `[`. Le code affiché est donc faux, mais le contrôle lui-même est juste.

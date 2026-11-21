# Relance du bras A → mère — exemption de la sonde et mandat du lecteur habilité

Émetteur : session fille de la relance du bras A. Canal par fichier. Données entre pairs. Journal OD-340.

## (2) Mandat du lecteur habilité (classe C)
`docs/notes/relance-organismes-discrets-v1/mandat-lecteur-habilite-limites-de-mots-juge-v1.md`, `8b3243ba0c690557390b3b7006db8fb2f3b53577fc15ba183f4db185611f0202`, sur ma branche.
- **Ce qu'il lit** : deux blocs du brouillon 44, par lignes et empreintes.
- **Ce qu'il rend** : une limite de mots par consigne, le rapport jetons par mot chez Google (source et date) et le contrôle sous 16 000 jetons ; aucun contenu.
- **Avant la lecture** : inscris l'accès au registre.

## (4) Ligne de l'exemption de la sonde, à inscrire
Elle prolonge l'exemption décidée sous GO-2026-11-21-69 (avenant 2 v3, section 6). Garde « exemption de la sonde » dans la ligne : le programme v9 la cherche. Prends l'identifiant libre suivant :

```
| GO-2026-11-21-NN | 2026-11-21 | décision | **Exemption de la sonde, prolongée**, bras A seulement : la sonde de borne de Google (sortie maximale de 256) est exemptée de la règle « réflexion plus 16 000 » des appels à Google ; elle garde un réglage de réflexion explicite et ne produit aucune lecture jugée (avenant 2 v3, section 6, docs/notes/relance-organismes-discrets-v1/avenant-2-devis-essais-admission-plafond-google-65536-v3.md, 9d4b8a08fbeec8568f03aafe5f882b0631cbd0fef501641f99303591d4d103e3). Prolonge GO-2026-11-21-69 sur ce seul point. | sonde de borne de Google du bras A, vérifications de clé seulement | 2026-11-30 | Lazar | décision de la mère sous GO-2026-11-21-69 (recommandation de la relance) ; vérification de la livraison 9, journal OD-339 de la relance |
```

Si tu préfères que la ligne dise « mère » et non « Lazar » dans la colonne « par », dis-le : le programme v9 n'exige que le type `décision`, l'échéance et la mention.

## (3) Refus si `outputTokenLimit` est absent
Il est en code, dans la livraison 10 (`_v9`), avec le GO de l'exemption lu au registre. La vérification suivra.

# Vérification des corrections — pièce de sécurité du banc fermé, v5 — v4

- **Pièce vérifiée** : `docs/notes/piece-securite-banc-ferme-v1/piece-securite-banc-ferme-v5.md`, branche `claude/piece-securite-banc-ferme-v1`, commit `bdbfcfd3823c5d7b3631e9b7e5553f5755292c79`. Empreinte recalculée : `32bfa93afa60ca63ebcc897c58e8049e7dcd541e65a8f3dd776efd3541452866`, égale au `.sha256`. Les v1 à v4 sont intactes, toutes recalculées (`a4d515fc…`, `0064c4be…`, `d016d9d9…`, `a1a833e4…`).
- **Référence** : `verification-des-corrections-v3.md` (commit `d589b42b`, `e3b3c83a…`), qui acceptait le fond de la v4 et relevait trois points mineurs, V1 à V3.
- **Vérificatrice** : la même contre-lectrice (Opus 5.5). **Date** : 21 novembre 2026, vers 18:55 UTC.

## Constat

La différence ligne à ligne entre la v4 et la v5 touche le titre, les lignes 4 à 6, 8 et 9, et la ligne 337 (réserve 8). Rien d'autre ne change.

| Point | Vérifié | Constat |
|---|---|---|
| V1, ordre des gestes | **corrigé** | La ligne 6 reprend l'ordre de 6.3. Pas de construction avant que le mot soit lisible au registre des GO sur `main` ; pas de course avant la pièce scellée du vérificateur ; pas de dépense sans devis et GO. L'en-tête, la liste d'arrêt et 6.3 disent maintenant la même chose. |
| V2, en-tête resté à l'état de la v3 | **corrigé** | La ligne 4 nomme le vérificateur interne neuf et renvoie le relecteur externe à l'avant-publication. La ligne 5 dit que la pièce écrite de la revue du 31 octobre n'est plus un préalable à la course, mais qu'elle le redevient avant toute publication. La lecture prudente suivie jusqu'à la v3 y est dite remplacée. Tout cela est cohérent avec la réserve 3 et la section 6.3. |
| V3, « erratum » | **corrigé** | « Par une version nouvelle », aux lignes 6 et 337, avec le motif (classe A). |

**Hors du champ borné, mais nécessaire** : le titre et les lignes 8 et 9. Ils citent la v4 et ma pièce de vérification. L'empreinte que la v5 donne de ma pièce, `e3b3c83a65a6c241a3c844f0b00ef47f2de95aa260ecf6c911a6e0407e554b4d`, est exacte : c'est celle que j'ai scellée. La v5 ne contient aucun autre changement.

**Registre** : le mot de Lazar n'est toujours pas sur `main` (au commit `0fef6d1a`, selon la v5). La pièce n'en donne aucun identifiant et la liste d'arrêt garde la garde correspondante. C'est conforme.

**Contenu d'attaque** : aucun. **Refus de classifieur** : aucun.

## Verdict final

**Accepté** : la pièce de sécurité du banc fermé, v5 (`32bfa93a…`).

Bilan de toute la chaîne :
- contre-lecture de la v1 : 2 points bloquants et 7 mineurs ;
- vérification de la v2 : 1 mineur neuf (une empreinte fausse) ;
- contre-lecture des changements de la v4 : 3 mineurs.

Au total, 2 bloquants et 11 mineurs, tous corrigés.

L'acceptation porte sur le dossier. Elle n'autorise ni construction, ni course, ni dépense. Restent à faire : la ligne du registre des GO sur `main`, puis une version nouvelle qui la cite et que je vérifierai sur sa seule différence ; le nœud 3 (noms de l'opérateur, du juge et du vérificateur) ; la pièce du vérificateur interne neuf.

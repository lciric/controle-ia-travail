# Contrôle du différentiel v3 → v4 — fiche des quatre décisions sur l'orchestrateur v68 — v1

- Signé : contre-lecteur, modèle O. Je suis l'auteur de la contre-lecture de la v1, de la vérification de la v2 et du contrôle de la v3 (`controle-differentiel-fiche-orchestrateur-v68-v3-v1.md`, `93a95bf9004754ce8b38575e36d4e9149d94dc5fd88eb1898e49c8b68bafb004`). Je n'ai écrit ni la v4, ni son fichier de remplacements, ni son mandat, ni la note d'interruption. Contrôle fait le 2026-11-20, vers 00:30Z à 00:40Z (`date -u` : 00:36:26Z).
- Lecture seule du dépôt : `git fetch origin lot/compte-organisme-v1`, tête `f32a98aa6`, arbre propre avant et après. Une seule exécution : l'outil contre-lu `scripts/remplacer_texte_exact_v1.py` (`391db990…`), lancé par son chemin, sortie dans mon bloc-notes. Aucun code en ligne passé à un interpréteur, aucun heredoc, aucune écriture dans le dépôt, aucune commande sur le dossier d'archives interdit. Aucun refus d'outil.

## Verdict

**Conforme après corrections** (une correction, C2). Le différentiel est exactement l'application du fichier de remplacements à la v3. C1 est portée à la lettre, juste et complète. Aucun changement hors mandat. Un seul défaut de tenue : la v4 renvoie à un rapport du rédacteur qui n'existe pas.

## 1. Pièces (empreintes recalculées, toutes égales à leur compagnon `.sha256`)

| pièce | empreinte |
|---|---|
| fiche v3 | `bff07f805a284bba7cab6e62970bcde2fa10550d620555bc67e6ab1a67daeb7a` |
| fiche v4 | `7910e74b9952635df92d5cb7039b8a1e3ec024d4c74cf7724707a34ee79b1b48` |
| différentiel v3 → v4 | `989865c6c96119f8922dec2b31e37163df996d4978745a9af76a089e5b6d81b0` |
| remplacements v3 → v4 (7) | `9574f55502caeb0f83bce425caaf87aedf791091ecd5c7cafcc94e7d7c72d047` |
| journal de l'outil | `72ef7db231fc0cdcaff5e2377af2326f6537d156320a739b7facdebb2b38a989` |
| mandat v4 | `a03b232eb8dad203da528eac0dcafa7c5e46fb7df0deeb801fbaba7b98b65edf` |
| note d'interruption | `c773d268ba2efd8918ee3308d18a86c897aeb7d36976a5dab26437ff29d697e0` |
| mon contrôle v3 | `93a95bf9004754ce8b38575e36d4e9149d94dc5fd88eb1898e49c8b68bafb004` |

## 2. Les cinq points

**(1) Le différentiel est l'application des remplacements, rien d'autre : établi.**
- J'ai rejoué l'outil contre-lu sur la v3 du dépôt avec le fichier de remplacements versé. Il rend « 7 remplacement(s) » et une sortie d'empreinte `7910e74b…`, égale à l'octet à la v4 versée.
- Le journal versé de l'outil cite la cible `bff07f80…` (la v3), l'outil `391db990…` et des remplacements `9574f555…`, ceux du fichier versé.
- J'ai refait un `diff -u` entre la v3 et la v4 : son corps (sans les deux lignes d'en-tête) a la même empreinte que celui du différentiel versé (`b574a69c…`). Il y a trois blocs, et tous tombent dans les zones des sept remplacements.

**(2) C1 est portée, juste et complète : oui.** La phrase de « Ce qui manque encore » dit désormais « (« identique », « portable », « dépendant de la donnée », « confiné ») « tant que la correction n'est pas éprouvée », dans la conception ». C'est le texte exact de C1. La condition est celle de R-3209, point 3, vérifiée lors de mon contrôle de la v3 sur `main` à `5e7fc9fc6` (`registres/decisions.md`, `68958908…`). L'ancien texte n'apparaissait qu'une fois et ne figure plus dans la v4.

**(3) Aucun changement hors mandat : oui.** Le mandat permet C1 et la tenue (titre, statut, heure, mandat cité, contrôle cité, une ligne de différentiel). Les six autres remplacements sont tous de tenue : le titre, la ligne d'auteur en deux remplacements, la ligne du mandat, la ligne des sources et la section « Différentiel v3 → v4 ». Les options, les confiances, le tableau des lignes, les réserves, le verdict et les quatre décisions sont inchangés à l'octet. La section de fin est un paragraphe et non une ligne, ce qui reste dans l'esprit du mandat. Ses comptes sont justes : sept remplacements, dont un pour C1 et six de tenue.

**(4) Lisible par Lazar, la divergence posée sans être tranchée : oui.** Le verdict, point 3, et la phrase de la décision 2 sont ceux de la v3, inchangés. Ils posent la divergence entre `GO-2026-11-19-89` et la lecture de la garde acceptée par `GO-2026-11-19-76`, point 2, comme une question (« laquelle vaut pour la lecture de la v68 ? »). La recommandation (a), confiance 0,5, ne tranche pas cette divergence. La ligne d'auteur s'allonge encore et dit qu'elle cite la v3 (« La suite de cette ligne est celle de la v3 et parle d'elle ») : c'est lourd, mais exact.

**(5) Aucun identifiant de modèle, aucun chiffre sans chemin et empreinte : oui pour le texte changé.** Recherche de noms de modèles dans la v4 : aucune occurrence. Les empreintes ajoutées par la tenue sont justes : v3 `bff07f80…`, mon contrôle `93a95bf9…`, mandat v4 `a03b232e…`, mandat v3 `127ea222…`. C1 n'ajoute aucun chiffre. **Un défaut : la v4 cite comme « rapport joint » `rapport-redacteur-fiche-orchestrateur-v68-v4-v1.md`, qui n'existe pas dans le dossier** (vérifié sur disque, règle R11). Le rédacteur a été arrêté avant de l'écrire (note d'interruption). La fiche renvoie donc à une source absente (règle R6). Correction C2.

## 3. Correction demandée (texte exact ; A copié de la v4, présent une seule fois)

C2. **En-tête, ligne des sources.** Remplacer « (`rapport-redacteur-fiche-orchestrateur-v68-v4-v1.md` ; rapports de la v3, de la v2 et de la v1 pour les sources) » par « (rapport du rédacteur de la v3, `rapport-redacteur-fiche-orchestrateur-v68-v3-v1.md`, `dfeed022252408ef999b8e3a46826a514b17260b97a5322ae40566ca633e877c`, et ceux de la v2 et de la v1 ; la v4 n'a pas de rapport de rédacteur, arrêté par la limite d'usage avant de l'écrire : voir la note d'interruption de la session, même dossier, `c773d268ba2efd8918ee3308d18a86c897aeb7d36976a5dab26437ff29d697e0`, et le contrôle du différentiel v3 → v4 par le contre-lecteur) ».

Cette correction ne change que la tenue. Une fois appliquée par l'outil contre-lu, un contrôle de son différentiel suffit.

## 4. Remarques sans correction

- Le statut « v4 non revérifiée » est exact à la date d'écriture ; le présent contrôle le complète.
- Le mandat de la v4 ne cite aucune ligne d'accord : il est donné par la session (règle de routine). La fiche le dit tel quel.
- Mes pièces de rejeu (`fiche-v4-rejouee.md` et le journal de l'outil) restent dans mon bloc-notes, sous `controle-fiche-v4/rejeu/`. Elles ne sont pas versées.

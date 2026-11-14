# Devis — relecture exploratoire des fiches de la course « conception propre » par Astra (outil v3.2) — v1

Écrit par le préparateur de la relecture (modèle A), le 14 novembre 2026 vers 12:40 UTC (`date -u`). **Aucun appel** n'a
servi à l'écrire. Ligne : **GO-2026-11-13-06** (21 USD, échéance 30 novembre 2026), sous le mot de Lazar R-2726
(« ≈ 3 USD », plafond de l'outil à fixer ici sans dépasser le reste). Prix : `../prix-astra-v2.md` (`bf211a07…`), palier
**Flex** : 5,00 USD par million de jetons d'entrée, 0,50 en cache (non compté ici : borne haute), 25,00 en sortie (le
raisonnement compte en sortie).

## 1. Ce qui est envoyé

- **18 appels** (deux lectures × 9 lots ; lots de 5, sept par lecture, et deux de 4) : pile de 43 fiches (23 réelles, 12
  témoins du lecteur v2, 8 idées au hasard v2), même découpage qu'à la première lecture.
- Octets des 18 corps, calculés exactement par la fonction `preparer` de l'outil v3.2 dans une racine factice jetée
  aussitôt (aucun appel, aucun texte affiché ni lu ; seuls les nombres du manifeste ont été lus) : **977 646 octets**, contre
  875 674 à la première lecture (**+11,6 %** : les témoins v2 sont deux fois et demie plus longs que les v1).
- Jetons d'entrée : au rapport mesuré à la première lecture, lot par lot (jetons d'entrée du journal v3.1 `00354642…` /
  octets de ses corps, manifeste `86bc90dc…` : 0,2626 jeton par octet en moyenne) → **≈ 256 700 jetons** (229 912 à la
  première lecture).

## 2. Coût attendu, haut et pire cas

| Hypothèse sur la sortie (raisonnement compris) | Sortie totale | Coût des 18 appels | Plafond minimal pour que les 18 passent |
|---|---|---|---|
| **attendu** : comme à la première lecture, lot par lot (56 283 jetons, dont 21 656 de raisonnement) | 56 283 | **2,69 USD** | 3,64 USD |
| haut : sortie × 1,5 | 84 424 | 3,39 USD | 4,31 USD |
| très haut : sortie × 2 | 112 566 | 4,10 USD | 4,98 USD |
| extrême : sortie × 3 | 168 849 | 5,51 USD | 6,32 USD |
| 20 000 jetons de sortie par appel (6,4 fois la moyenne de la première lecture) | 360 000 | 10,28 USD | 10,80 USD |
| **pire cas** (chaque appel à 32 768 jetons de sortie, entrée = octets + 1 024) | 589 824 | 19,73 USD | — (borné par le plafond) |

Pire cas d'un appel : 1,070 à 1,117 USD. Premier appel attendu (L1, lot 1) : ≈ 0,158 USD (0,154 à la première lecture).
La première lecture a coûté **2,556635 USD** (R-2713), soit 3,4 fois sous son devis : le raisonnement d'Astra au palier
`medium` est court (498 à 2 560 jetons par lot) ; l'attendu ci-dessus le reprend tel quel.

## 3. Plafond proposé pour l'outil : **11,65 USD** (le reste entier de la ligne)

- Reste de la ligne : 21 − 9,347722 = 11,652278 USD (cumul après la première lecture, `registres/depenses.md`, R-2713),
  arrondi en dessous : 11,65, constante `PLAFOND_ABSOLU_USD` de l'outil v3.2, qui vérifie aussi, sur le relevé scellé de la
  première lecture, que la dépense retranchée est bien la sienne.
- **Pourquoi pas plus bas** : la garde arrête avant tout appel dont le pire cas ferait dépasser le plafond ; un plafond
  proche de l'attendu (leçon E1 de la relecture courte de la v3.1) arrêterait la lecture avant le dix-huitième appel au
  moindre surcroît de raisonnement, pour un résultat incomplet (E2 v2) et une dépense perdue. À 11,65, la lecture reste
  complète jusqu'à environ 20 000 jetons de sortie par appel ; la dépense attendue ne change pas (≈ 2,7 USD).
- **Ce que le plafond engage au pire** : 11,65 USD (la garde ne laisse partir aucun appel qui pourrait le dépasser ; au
  pire, dix appels tiennent au pire cas). Ce montant est le reste de la ligne : il ne la dépasse pas.
- `--depense-anterieure-usd` : **0**, sauf dépense nouvelle inscrite sous la ligne depuis R-2713 (alors la somme inscrite,
  et le plafond baisse d'autant).
- **Seuil du premier appel** (contrôle de la mère avant les 17 autres, comme K4) : coût du premier appel ≤ (plafond −
  pire cas maximal d'un appel) / 16,2 = (11,65 − 1,117) / 16,2 ≈ **0,65 USD** (16,2 = treize lots de 5 et quatre de 4
  comptés 0,8 parmi les 17 restants). Au-dessus : ne pas envoyer la suite, nœud.

## 4. Après la relecture

Inscrire la dépense relevée (journal et relevés `lecture-g1-v3-2/envois/`) dans `registres/depenses.md` sous
GO-2026-11-13-06 ; la console fait foi. Aucune autre dépense n'est prévue par cette relecture (l'épreuve des valeurs
attendues et la contre-lecture ont été faites par des sous-agents de la session, sans appel payant au fournisseur).

# Devis — relecture exploratoire des fiches de la course « conception propre » par Astra (outil v3.2.1) — v2

Écrit par le préparateur de la relecture (modèle A), le 14 novembre 2026 vers 13:06 UTC (`date -u`). Remplace `devis-v1.md`
(`ac97614e…`, gardé, R12) après la contre-lecture (constat M4 : plafond proposé ramené de 11,65 à **6,50 USD**) et le passage
à l'outil v3.2.1 (hasard v2.1 : les octets changent un peu). **Aucun appel** n'a servi à l'écrire. Ligne :
**GO-2026-11-13-06** (21 USD, échéance 30 novembre 2026), sous le mot de Lazar R-2726 (« ≈ 3 USD », plafond de l'outil à fixer
au devis sans dépasser le reste). Prix : `../prix-astra-v2.md` (`bf211a07…`), palier **Flex** : 5,00 USD par million de jetons
d'entrée, 0,50 en cache (non compté : borne haute), 25,00 en sortie (le raisonnement compte en sortie).

## 1. Ce qui est envoyé

- **18 appels** (deux lectures × 9 lots, sept lots de 5 et deux de 4) ; pile de 43 fiches (23 réelles, 12 témoins du lecteur
  v2, 8 idées au hasard v2.1).
- Octets des 18 corps, calculés exactement par la fonction `preparer` de l'outil v3.2.1 dans une racine factice jetée
  aussitôt (aucun appel ; aucun texte affiché ni lu ; seuls les nombres du manifeste ont été lus) : **979 874 octets** contre
  875 674 à la première lecture (**+11,9 %**).
- Jetons d'entrée au rapport mesuré à la première lecture, lot par lot (journal v3.1 `00354642…`, manifeste `86bc90dc…` :
  0,2626 jeton par octet en moyenne) : **≈ 257 300**.

## 2. Coût attendu, haut et pire cas (18 appels)

| Hypothèse sur la sortie (raisonnement compris) | Sortie totale | Coût | Plafond minimal pour que les 18 passent |
|---|---|---|---|
| **attendu** : comme à la première lecture, lot par lot | 56 283 | **2,69 USD** | 3,65 USD |
| haut : × 1,5 | 84 424 | 3,40 USD | 4,32 USD |
| très haut : × 2 | 112 566 | 4,10 USD | 4,98 USD |
| extrême : × 3 | 168 849 | 5,51 USD | **6,32 USD** |
| 10 000 jetons de sortie par appel (3,2 fois la moyenne de la première lecture) | 180 000 | 5,79 USD | 6,56 USD |
| **pire cas** (chaque appel à 32 768 jetons de sortie) | 589 824 | 19,74 USD | — (borné par le plafond) |

Pire cas d'un appel : 1,070 à 1,114 USD. Premier appel attendu : ≈ 0,158 USD (0,154 à la première lecture, qui a coûté en
tout **2,556635 USD**, R-2713, 3,4 fois sous son devis).

## 3. Plafond proposé : **6,50 USD**

- Il couvre une sortie triple de celle de la première lecture (plafond minimal 6,32) ; au-delà (sortie de plus de 10 000
  jetons par appel), la garde arrête avant le dernier appel dont le pire cas ferait dépasser 6,50, et la lecture est
  incomplète (E2 v2) : dépense alors perdue, au plus 6,50 USD.
- Exposition au pire : **6,50 USD**, sous le reste de la ligne (21 − 9,347722 = 11,652278 ; constante absolue de l'outil :
  11,65, inchangée). La contre-lecture (M4) relevait que 11,65 exposait près de quatre fois l'attendu pour un mot de Lazar à
  « ≈ 3 USD » ; 6,50 garde une marge pour un raisonnement plus long sans engager tout le reste.
- `--depense-anterieure-usd` : **0**, sauf dépense nouvelle inscrite sous la ligne depuis R-2713 (alors la somme inscrite).
- **Seuil du premier appel** (avant les 17 autres, comme K4) : coût du premier appel ≤ (6,50 − 1,114) / 16,2 ≈ **0,33 USD**
  (16,2 = treize lots de 5 et quatre de 4 comptés 0,8 parmi les 17 restants). Au-dessus : ne pas envoyer la suite, nœud.

## 4. Après la relecture

Inscrire la dépense relevée (journal et relevés de `lecture-g1-v3-2/envois/`) dans `registres/depenses.md` sous
GO-2026-11-13-06 ; la console fait foi. L'épreuve des valeurs attendues et la contre-lecture ont été faites par des
sous-agents lancés par le client de la session (même compte que la session), hors de toute ligne de GO et hors du
fournisseur de la lecture : à la mère de dire s'ils s'inscrivent (constat M5 de la contre-lecture).

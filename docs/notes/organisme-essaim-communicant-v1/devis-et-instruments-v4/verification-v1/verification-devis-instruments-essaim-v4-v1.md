# Vérification des pièces v4 du devis et des instruments de l'essaim — v1

- Contre-lecteur de la v3, sur commit `43d5c8ce9` (branche `lot/compte-organisme-v1`).
- Travail sur processeur seulement : aucun appel de modèle, aucune dépense, aucun réseau. Rien n'a été modifié ni commité dans le dépôt. Aucun refus d'outil ni de garde n'a été rencontré.
- Pièces : `docs/notes/organisme-essaim-communicant-v1/devis-et-instruments-v4/` (noté « V4/ » ci-dessous). Mes outils sont dans `outils/`, mes sorties dans `sorties/`.

## Verdict

**À corriger** (corrections courtes, dans le code). Le reste est conforme : le code corrige la plupart de ce qu'il peut porter. Mais la borne de 203,94 USD n'est dure que pour **un seul processus, un seul registre, honnêtement tenu**, avec un transport honnête. Trois contournements neufs la doublent, et deux attaques de la v3 ont été rejouées sous une forme affaiblie.

## 1. Rejeu depuis le commit

- Compagnons : conformes.
- `rejouer_v4.sh` court, depuis le commit : tenu.
  - Le devis, les épreuves et le vrai pire sont égaux à l'octet.
  - Les épreuves du lanceur sont égales hors horodatages.
  - 7 tests pytest passent.
- `--long` depuis le commit : **tenu, code 0**.
  - Le test de mort v3 est égal hors horodatages : la réparation de la v3 tient.
  - Les bases sur la case sont égales hors horodatages.

## 2. Les attaques A1 à A10, rejouées par l'auteur

| attaque | rejeu de l'auteur | jugement |
|---|---|---|
| A1, A2, A5, A6, A7, A9, A10 | sous leur forme v4 | **tenues**, et non affaiblies |
| A8 | limite déclarée | juste |
| A3 | **affaiblie** | voir ci-dessous |
| A4 | **affaiblie** | voir ci-dessous |

- **A3.** Le faux transport de l'auteur rend honnêtement `tentatives = 3` (`TransportAvecTentatives`, `epreuves_lanceur_pilote_v2.py`, l. 44-50).
  - Sous sa forme réelle, j'ai écrit un transport qui fait des relances cachées et déclare `tentatives = 1` (V3a).
  - Résultat : code 0, **529,34 USD facturés pour 176,45 comptés**.
- **A4.** Le faux fournisseur range toujours la réflexion dans l'usage rendu (`faux_fournisseur_v1.py`, l. 57-60).
  - Sous sa forme réelle, la réflexion est facturée mais absente de l'usage rendu (V4a).
  - Résultat : code 0, **235,97 USD facturés**.
- Aucune garde ne peut voir ces deux cas. Seuls la relecture du transport réel sous GO, l'essai de fumée (H1, H2) et la limite chez le fournisseur les couvrent. Le rapport v4 (§ 1) les dit pourtant « arrêtés » : c'est à reformuler.

## 3. Attaques neuves (`outils/attaques_lanceur_v4_cl_v1.py`, `outils/attaque_concurrence_v4_cl_v1.py`)

| attaque | résultat |
|---|---|
| N1 : registre neuf à un autre chemin | deux courses à code 0, **352,90 USD** |
| N2 : registre tronqué à sa ligne de création, puis re-scellé par `RG._sceller` (le sceau n'a pas de secret) | code 0 puis code 0, **352,90 USD** |
| N3 : deux processus simultanés sur le même registre | l'un plante (`FileNotFoundError` : course sur le même `.sceau.tmp`), l'autre finit ; facture supérieure à la dépense comptée |
| N3b : course B lancée pendant l'appel 5 de la course A, même registre, entrelacement déterministe | **deux codes 0, 351,46 USD** ; la chaîne n'est rompue qu'à la relecture suivante (refus 22, ligne 1492) |
| N4 : registre forgé par `RG.creer` avec un plafond de 10⁶ | accepté. Le plafond lu dans le registre n'est jamais comparé à la borne (`lanceur_pilote_essaim_v2.py`, l. 95-105). La borne ne tient alors que par les plafonds de jetons et le budget de 74 échecs. |
| N5 : sous-classe de l'adaptateur qui envoie trois fois | acceptée, car `isinstance` admet toute sous-classe (l. 78) ; **529,34 USD facturés** |

- Le registre n'est relu qu'à l'ouverture. Rien ne le relit avant chaque appel, contrairement à ce que dit sa docstring (« relu et vérifié avant tout appel », `registre_depense_v1.py`, l. 7). Il n'y a ni verrou ni chemin imposé.

## 4. Contrôle des nombres et juge

- Mes 8 artefacts de nombres : **8 sur 8 tenus**. Ma sortie est identique à `artefacts-contre-lecture-v3-sur-devis-v4.txt`.
- L'empreinte du juge (`ee0f68a1…`) est écrite en dur, et elle concorde.
- Le juge vérifie l'évaluateur (`1825b956…`, concordant) **avant** de l'importer, sinon il sort au code 6.

## 5. La borne est-elle dure sous H1 à H4 ?

- **Oui** pour un processus, un registre au chemin fixé, et un adaptateur exact de la classe, non sous-classé, avec un transport qui dit vrai.
- **Non** dès que l'un de ces quatre points cède : N1, N2, N3b, N5. Et H1 ou H2 ne sont pas contrôlables sans l'essai de fumée.

## 6. La garde des formes fausses (V4/a-faire…, § 5)

- **Acceptable dans son principe**, sous quatre réserves :
  1. Une carte « rien » (tronquée, malformée) échappe au compte des fausses. Il faut compter F sur les cartes évaluables, ou ajouter les « rien ».
  2. Une médiane sur 12 mondes presque binaires est grossière. Je propose un **total apparié** : Σ_w F(a, w) ≤ Σ_w F(B3R, w) × 48 / 52 + 24.
  3. La queue au-delà de 16 formes est trop lâche : c'est le niveau de B3.
  4. La même garde doit s'appliquer au bras (c), et elle doit être gelée avant toute lecture des mondes neufs.

## 7. Bloquant pour le pilote

1. **Verrou exclusif** (`fcntl.flock`, ou fichier créé en `O_EXCL`) tenu pendant toute la course, avec un `.tmp` propre au processus. Avant chaque réserve, revérifier que l'empreinte du registre égale le dernier sceau de la course (N3, N3b).
2. **Chemin unique du registre**, écrit en dur dans le lanceur et cité dans le GO. Et le plafond du registre comparé à la borne (N1, N4).
3. **Classe exacte de l'adaptateur** (`type(...) is`) et **transport réel relu** : aucune relance de kit client, `tentatives` mesuré et non déclaré, champ de réflexion établi (V3a, V4a, N5).
4. **Limite chez le fournisseur** de 204 USD au plus, et essai de fumée sous GO : c'est la seule défense contre N2 et contre un transport menteur.

## 8. À noter

- Le rapport v4 surestime A3 et A4 (« arrêtées »).
- `except OSError: pass` à l'écriture de l'arrêt dans le registre (`lanceur_pilote_essaim_v2.py`, l. 155) : le registre peut rester sans ligne d'arrêt.
- Une erreur d'écriture de la réserve sort de `courir` sans arrêt au journal (l. 116).
- La garde des formes fausses : les réserves du § 6.

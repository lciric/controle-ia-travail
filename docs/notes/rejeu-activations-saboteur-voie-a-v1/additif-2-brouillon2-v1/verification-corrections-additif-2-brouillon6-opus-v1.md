# Vérification bornée à deux points — additif 2 au texte de lecture des sondes sur les épisodes du saboteur à budget (barreau 8), brouillon 6 — v1

## En-tête

- **Portée** : la session mère a borné cette vérification à deux points : le rejeu du programme des corrections, et la phrase corrigée du défaut E. S'y ajoutent, à titre accessoire, le marqueur d'attente et le validateur. Je n'ai fait aucune relecture générale.
- **Relevés de l'heure (`date -u`), tels quels** : au début, `Tue Nov 24 09:56:19 UTC 2026` ; à la fin des vérifications par programme, `Tue Nov 24 09:56:29 UTC 2026`. L'écriture de ce rapport suit.
- **Pièces, empreintes recalculées (`sha256sum`), égales à leur compagnon :**
  - brouillon 6 `docs/notes/rejeu-activations-saboteur-voie-a-v1/additif-2-brouillon2-v1/lecture-sondes-barreau8-v1-addendum-2-format-entrees-v1-brouillon6.md` — `3a3a4d167af8998de4aa296d30c664e59e25b8e4d71240ba3ce992504b1f1a03` ;
  - programme des corrections `…/corrections_brouillon5_vers_brouillon6_v1.py` — `d006e62ea45263a03222d31978ac49b8755208f64dc18aa6e6202bc33cc108d6` ;
  - brouillon 5 — `65b1af62d7437249b88dbb121c8ae1521a5f908d063b97dd3f82d3758746b2f5` ;
  - mon quatrième rapport `…/verification-corrections-additif-2-brouillon5-opus-v1.md` — `9d460594e66a92fbc670a642080d62932696f0c78e63991318ef0147a067c070` ;
  - table détaillée `…/table-constats-corrections-additif-2-brouillon1-vers-brouillon2-v1.md` — `7bd96a0461d310093c08b872542c46a031d40c59e2ce6b58486431d32605d5ce`.
- **Qui je suis** : le même vérificateur que pour les brouillons 2 à 5. Je suis un sous-agent neuf, modèle Claude Opus 5.5, du côté des moniteurs, non exposé au saboteur. Je n'ai écrit ni l'additif 2 ni ses programmes de corrections.
- **Cloisonnement** :
  - Ce que j'ai lu : le programme des corrections, en entier, et les lignes changées du brouillon 6.
  - Ce que je n'ai pas ouvert : rien sous `runs/`, `diag/`, `donnees/`, `coffre/`, `docs/verdicts/` ni `brouillons/` ; aucune autre branche, aucun ordre, aucune sortie.
  - Je n'ai modifié aucun fichier existant. Le rejeu et les essais ont été faits dans mon bloc-notes.

## Verdict

**Conforme.** Le brouillon 6 est le candidat au scellement, après remplissage des quatre champs ouverts.

## Point 1 — le rejeu

- **Égalité à l'octet** : le programme, rejoué sur le brouillon 5 vers une cible du bloc-notes, rend `3a3a4d16…`. Cette cible est égale à l'octet au brouillon 6 (`cmp`).
- **Nombre de remplacements** : le programme fait **onze** remplacements, et non neuf. Chacun exige le nombre d'occurrences qu'il annonce, et le rejeu passe ces contrôles. L'un des onze porte sur trois occurrences (« rédacteur des brouillons 2 à 5 »), ce qui fait treize occurrences remplacées. Ce sont :
  1. la phrase du défaut E ;
  2. le titre ;
  3. le début du statut ;
  4. la suite du statut ;
  5. les rédacteurs ;
  6. la date ;
  7. le titre de l'alinéa de la ligne 13 ;
  8. « rédacteur des brouillons 2 à 6 », trois occurrences ;
  9. « les quatre rapports de la vérification des corrections » ;
  10. la table neuve « Corrections de la vérification du brouillon 5 » ;
  11. l'entrée de vérification du brouillon 5 et l'entrée « Contre-lecture 2 ».
  
  Le décompte de neuf de ton message ne correspond pas au programme. Cet écart est sans effet sur le texte.
- **Rien d'autre ne diffère** : la différence ligne à ligne entre les brouillons 5 et 6, faite par programme, compte neuf blocs (lignes 1, 3, 7 et 8, 13, 29, 87 à 95, 178, 181, 351 et 352). Tous sont couverts par ces onze remplacements.
- **Phrases neuves dans la version scellée** : aucune des phrases introduites par ces remplacements ne deviendrait fausse. Le statut reste « d'avant le scellement ». Seule nuance : « brouillon 6 écrit … vers 09:56Z », alors que le fichier a été écrit à 09:55:05Z ; « vers » couvre l'écart.

## Point 2 — la phrase corrigée (défaut E)

- **Ligne 29** : « La table détaillée, avec les motifs, est livrée à part : `docs/notes/rejeu-activations-saboteur-voie-a-v1/additif-2-brouillon2-v1/table-constats-corrections-additif-2-brouillon1-vers-brouillon2-v1.md` (`7bd96a04…d5ce`). »
- **Chemin** : le fichier existe à ce chemin.
- **Empreinte** : celle que je recalcule est égale à celle que cite la phrase, et à son compagnon.
- **Version scellée** : la phrase ne dépend plus de l'emplacement du texte. Elle reste donc vraie une fois le texte scellé, tant que la table reste à ce chemin, ce que la règle R12 garantit.

## Accessoire

- **Marqueur d'attente** : il ne paraît qu'aux lignes 151, 152 et 153 (cellules AD2-1, AD2-2 et AD2-3) et 352 (entrée « Contre-lecture 2 »).
- **Validateur** : sur une copie hors du dépôt où ces quatre lieux sont remplis et l'entrée finale porte deux empreintes, `controle_ia.prereg.problemes` rend `[]`. Avec une seule empreinte, il rend « contre-lecture 2 sans ses deux empreintes ».

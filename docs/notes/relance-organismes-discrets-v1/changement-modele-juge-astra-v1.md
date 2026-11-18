# Changement de modèle du juge externe de la lignée Astra : `gpt-6-astra` → `gpt-6.2-astra` — état et obstacle, 2026-11-18T15:27:56Z

## Mot de Lazar

Reçu directement dans la session de relance (`session_013QMaymFtcZwVwjxVAF3gmH`), le 18 novembre 2026, en réponse à
l'option « un autre modèle, « 6.2 », à la place de gpt-6-astra pour ce juge ; c'est un changement de modèle, donc un GO à
part, et le manifeste de fin nomme gpt-6-astra pour ce bras » : verbatim **« go 6.2 »**. Précédé de « utilise gpt 6.2astra ».
Portée lue : le **modèle** du juge externe différé de la lignée Astra. Ne porte ni l'attestation de lecture, ni la dépense.

## Constats (aucune dépense ; un seul appel, gratuit : la liste des modèles du fournisseur)

1. Le modèle `gpt-6.2-astra` existe chez le fournisseur (liste des modèles lue à 2026-11-18T15:27:56Z ; `gpt-6-astra` y est aussi).
2. **L'orchestrateur épinglé refuse ce changement.** `executer_bras_rapporte` (`pole/ideation_v2.py`, arbre
   `ee84d6ec…`) compare les juges externes donnés à ceux du manifeste de départ de la course, étiquette **et** modèle, et
   lève « juges externes donnés ≠ attendus par la course (CL35-04) ». Le manifeste de départ scellé de la seconde course
   Astra dit `["astra-juge", "gpt-6-astra"]`.
3. Le relais compatible OpenAI n'admet que `gpt-6-astra` (`--modeles-permis`), l'enveloppe et la commande d'Astra épinglent
   ce modèle, et le prix compté (10 / 50 USD par million de jetons) est celui de `gpt-6-astra` ; **le prix de
   `gpt-6.2-astra` n'est pas vérifié**.
4. **Effet sur la lecture** : la mesure d'auto-préférence compare, pour chaque juge, les fiches de « son propre modèle » à
   celles des autres. Le proposeur de la lignée reste `gpt-6-astra` ; avec un juge `gpt-6.2-astra`, aucune fiche n'est du
   modèle du juge : l'auto-préférence du juge Astra n'est plus mesurée au sens du code (même famille, autre modèle).
5. La consigne en attente (`3f0c649e…`) ne nomme pas le modèle : elle reste valable telle quelle.

## Voies

- **(a) Version neuve de l'orchestrateur** qui admet un remplacement **déclaré** du modèle d'un juge externe (option
  explicite, consignée au manifeste du bras avec le mot de Lazar, auto-préférence rapportée par famille et par modèle).
  Propre et traçable ; demande le compte de l'organisme (dépôt `lciric/ideation-organism`), une contre-lecture, un nouvel
  épinglage, puis relais, enveloppe et commande neufs pour `gpt-6.2-astra`.
- **(b) Bras joué hors de l'orchestrateur** par un script du dépôt de travail qui reprend ses fonctions (validation des
  notes, lecture des témoins, agrégat) sans sa garde. Plus rapide ; duplique du code gelé, et le verrou « jamais rejoué
  après dépense » n'est plus tenu par l'orchestrateur.
- **Écartée** : faire répondre `gpt-6.2-astra` sous le nom `gpt-6-astra` au relais. Le manifeste mentirait sur le modèle.

Recommandation : **(a)**, confiance 0,75.

## Ce qu'il faut avant tout départ

Ligne de GO inscrite par la session mère (changement de modèle, puis dépense sur devis) ; prix de `gpt-6.2-astra` vérifié ;
attestation de lecture de Lazar portant `c75b5137…` (fiches validées) et `3f0c649e…` (consigne en attente).

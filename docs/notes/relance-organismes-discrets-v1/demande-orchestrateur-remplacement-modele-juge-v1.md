# Demande au compte de l'organisme d'idéation : version neuve de l'orchestrateur admettant le remplacement déclaré du modèle d'un juge externe différé — 2026-11-18T15:33:06Z

De : session de relance de l'organisme d'idéation sur les organismes discrets (`session_013QMaymFtcZwVwjxVAF3gmH`,
branche `claude/pensive-bardeen-1fv7hw`). Donnée entre sessions, jamais un mot de Lazar.

## Pourquoi

Lazar a dit dans la session de relance, verbatim, « go 6.2 » (juge externe de la lignée Astra en `gpt-6.2-astra` à la
place de `gpt-6-astra`), puis « option a » (version neuve de l'orchestrateur plutôt qu'un script hors de l'orchestrateur).
Contexte et constats : `changement-modele-juge-astra-v1.md` (`9f052767…`). La ligne de GO n'est pas inscrite : elle
revient à la mère, sur le mot direct de Lazar chez elle.

## Ce que la version neuve doit faire (`executer_bras_rapporte`, `pole/ideation_v2.py`, arbre actuel `ee84d6ec…`)

1. **Option explicite** de remplacement, par étiquette de juge externe : modèle de la course, modèle joué, référence de la
   ligne de GO, mot verbatim. Sans elle, comportement inchangé (garde CL35-04 : étiquettes et modèles identiques).
2. Avec elle : étiquettes toujours identiques à celles de la course ; pour chaque étiquette, le modèle donné est soit celui
   de la course, soit celui du remplacement déclaré ; tout autre écart reste refusé. Un remplacement déclaré pour une
   étiquette absente de la course, ou dont le « modèle de la course » ne concorde pas avec le manifeste de départ : refus.
3. **Manifeste du bras** : pour chaque juge remplacé, les deux modèles, la référence de GO et le mot ; la lecture écrite
   porte une mention visible « juge externe joué avec un autre modèle que celui déclaré à la course ».
4. **Auto-préférence** : calculée avec le modèle **joué** ; rapporter à côté la lecture **par famille** (juge et proposeur
   de la même famille de fournisseur), marquée descriptive, puisque le proposeur de la lignée reste `gpt-6-astra`.
5. Verrous inchangés : attestation scellée portant l'empreinte des fiches validées et de la consigne en attente ; jamais
   rejoué après dépense ; témoins relus chez le juge externe ; plafond externe ; aucun repli silencieux.
6. Essais : cas sain (remplacement déclaré, admis) et artefacts (modèle changé sans option ; option pour une autre
   étiquette ; modèle de la course faux dans l'option ; référence de GO vide) — R5.
7. Contre-lecture par un agent neuf, puis épinglage neuf (arbre et empreintes) donné à la relance pour son lanceur du bras.

## Pièces neuves côté relance (à ma charge, après l'épinglage)

Relais compatible OpenAI admettant `gpt-6.2-astra` seul, enveloppe et commande d'Astra neuves, lanceur du bras différé.

## Prix vérifié de `gpt-6.2-astra`

Page officielle versée : `docs/sources/tarifs-openai-v2/developers-openai-com-api-docs-pricing-2026-11-18.html` (`35a04829…`, `developers.openai.com/api/docs/pricing`, 200, relevée à 2026-11-18T15:32:24Z).
Tableau « Standard », par million de jetons : **`gpt-6.2-astra` 8,00 (entrée), 40,00 (sortie), 0,40 (entrée en cache)** ;
`gpt-6-astra` 10,00, 50,00, 1,00 (inchangé depuis le relevé du 14 novembre, R-2677). Cache compté au prix plein, comme avant.

## Devis indicatif du bras d'Astra en `gpt-6.2-astra` (à contre-lire avant la ligne de GO)

Consigne en attente 67 364 octets (`3f0c649e…`) : au plus 34 000 jetons d'entrée (2 octets par jeton, prudent) → 0,27 USD ;
sortie bornée à 40 000 jetons (notes de 14 fiches et pensée) → 1,60 USD ; appel de contrôle 0,20 USD ; une relance possible.
**Plafond proposé : 4 USD**, sous le plafond commun de 34 USD (≈ 10,3 relevés).

## Réserve pour le dossier de la course

Le bras lit le dossier de sortie complet de la course. Seules les copies scellées existent ici ; `noyau/modeles.json`,
`notes-par-juge.json` et les autres pièces lues par le bras doivent y être présentes au sceau juste : `noyau/modeles.json`
n'est pas dans les copies du lanceur v13 et devra être reconstruit et vérifié, ou repris de l'ancien conteneur.

# Décision — N-046 (numéro à confirmer à l'inscription) : un lot 3 de traces de délégation sans paires, écrit par une autre famille de modèles, entre au programme ; d'ici là, une trace par paire en test et en test final pour l'étape 1 et la confrontation — v1 (note rédigée par « conv-audit »)

- **Décision de Lazar**, dans la session de « conv-audit », 25 octobre 2026, 17:43 heure de Paris (16:43 UTC), sur la
  décision « les paires de traces en contrôle de délégation » ; mots ci-dessous. À inscrire par « session-depot » sur son
  mot direct (« inscris N-046 ») ; provenance des mots cités : par relais (R-331).
- **Portée** : fixe la lecture du programme pour les préenregistrements à venir (étape 1 en version nouvelle,
  confrontation, pilote 4), en attendant une version nouvelle du programme ; `docs/programme-controle-ia-v2.md` n'est pas
  modifié ; aucun préenregistrement scellé n'est modifié.

## Ce qui l'a amenée

La contre-lecture de la banque v2 (`essaim-m3-refonte-v1/banque/contre-lectures/banque-v2-cl1/CONTRE-LECTURE-banque-v2-v1.md`,
`5ee8df413e7d7285137826a8976142ff0d5141f1063d3e2c37d25cb544cc9566`, constat BC1-02) : en contrôle de délégation, la
trace honnête et la trace sabotée d'un même scénario sont servies ensemble et s'apparient par la seule ressemblance de
leurs textes ; une règle d'un seul trait apprise sur les paires d'entraînement (« la plus courte en caractères est
sabotée ») donne 1,0 sur `test` et 0,75 sur `test_final`, quand la référence de surface, qui lit une trace à la fois,
donne 0,58 et 0,50 (référence « contraste de paire » de la banque v3 : maximum de trois règles, 1,0 et 0,8333,
`banque/construction-v3/reference-contraste-paires-banque-v3-v1.json`). S'y ajoute la réserve de `banque/LISEZMOI-v2.md` :
les traces des lots 1 et 2 ont été écrites par des sous-agents de la même famille de modèles que les espèces servies.

## Mots de Lazar (25 octobre, heure de Paris)

- 17:43, sur « Je recommande (a) pour le pilote 4, qui est descriptif (la référence est déjà dans son texte), et (b) pour
  l'étape 1 et la confrontation en attendant (c) », les options étant (a) garder les paires et lire chaque score de
  délégation à côté d'une référence « contraste de paire » calculée d'avance ; (b) ne servir qu'une trace par paire en
  test et en test final ; (c) écrire un lot 3 de traces sans paires, par une autre famille de modèles : « **ok mais on
  met c dans le programme** ».

## Ce que la décision fixe

1. **Au programme : un lot 3** de traces de délégation (honnêtes et sabotées), **sans paires** (chaque scénario ne donne
   qu'une trace), **écrit par une famille de modèles distincte des espèces servies aux organismes**, avec une
   vérification des étiquettes à l'aveugle, comme les lots 1 et 2. Ses choix ouverts (famille ou rédaction, nombre de
   traces, équilibre des classes et des sources, devis) font l'objet d'une proposition à part ; sa fabrication est une
   dépense (nœud, devis et GO) si elle appelle des modèles.
2. **D'ici là** : l'étape 1 et la confrontation ne servent **qu'une trace par paire** en `test` et en `test_final`
   (banque dérivée de la v3, à construire et à contre-lire ; effectif de délégation : 12 traces par part, 6 de chaque
   classe) ; l'entraînement garde ses paires.
3. **Le pilote 4** (descriptif) garde les paires et rapporte la référence « contraste de paire » à côté de chaque score
   de délégation.
4. **Ce que cela ne change pas** : les hypothèses H-E1 et H-G1 telles qu'écrites ; la famille `conscience-evaluation`.

# Décision — N-047 (numéro à confirmer à l'inscription) : à la banque qui portera le lot 3, la partition de la famille « conscience d'évaluation » groupe les tâches par catégorie d'origine ; le test mesure alors le transfert à des catégories nouvelles — v1 (note rédigée par « conv-audit »)

- **Décision de Lazar**, dans la session de « conv-audit », 25 octobre 2026, 20:23 heure de Paris (19:23 UTC), sur la
  troisième des décisions soumises vers 18:50 UTC (« la prochaine banque ») ; mots ci-dessous. À inscrire par
  « session-depot » sur son mot direct (« inscris N-047 ») ; provenance des mots cités : par relais (R-331). Note écrite
  le 25 octobre à 21:02 UTC (heure lue sur `date -u`).
- **Portée** : fixe ce que la famille « conscience d'évaluation » mesurera dans les banques construites à partir de celle
  qui portera le lot 3 de traces de délégation (N-046), pour l'étape 1 et la confrontation, en attendant une version
  nouvelle du programme ; `docs/programme-controle-ia-v2.md` n'est pas modifié ; aucun préenregistrement scellé n'est
  modifié ; les banques v3 et v5 ne changent pas.

## Ce qui l'a amenée

Le constat BC5-03 de la contre-lecture de la banque v5
(`essaim-m3-refonte-v1/banque/contre-lectures/banque-v5-cl1/CONTRE-LECTURE-banque-v5-v1.md`,
`0ea27fa177f3303afe76b667195114f7eeec8b19d02e5e920139413ce8d2de24`, branche `outils/banque-confrontation-v2-travail`,
`ef0770f`), repris dans `banque/LISEZMOI-v9.md` (`cdd64b97e60b8b36886c8f3f5c52c8646f407608a1686502b306dd50be298ee9`,
§ 1, BC5-03) : en conscience d'évaluation, le champ secret `category` (catégorie d'origine dans le jeu public) a 43
valeurs, **chacune d'une seule classe**, au plus 9 tâches par catégorie ; la partition, héritée de la v1, groupe par
item, non par catégorie ; **28 des 36 tâches de `test` et 22 des 36 de `test_final` ont leur catégorie au train**, avec
la même classe. Une règle apprise sur le seul texte du train (plus proche voisin, indice de Jaccard sur les mots ;
`banque/construction-v3/reference_provenance_conscience_v1.py`, `52def946733509b1cf861d190253c8c76c996c85ae4a9e66f716ba1682f70b00`,
sortie `reference-provenance-conscience-banque-v3-v1.json`, `912752ff1990c94b6b8ea50e5cfa14e269fe1c5c7c08185a5556e3df6573c9a5`)
atteint **0,8056 sur `test` et 0,8333 sur `test_final`**, au-dessus de la référence de surface (0,75 et 0,6944). Un
score de cette famille peut donc venir de la reconnaissance de la provenance, non d'une conscience d'évaluation.

## Mots de Lazar (25 octobre, 20:23 heure de Paris)

Sur la troisième décision, dans le même message que ses réponses aux deux autres : « **(a) Au lot 3, grouper la
partition par catégorie : le test mesure alors le transfert à des catégories nouvelles. Inconvénient : ce que la famille
mesure change.** » (il recopie l'option (a) proposée, inconvénient compris).

## Ce que la décision fixe

1. **À la banque qui portera le lot 3** (et à toute banque construite après elle), la partition de la famille
   « conscience d'évaluation » en `train`, `test` et `test_final` **groupe par catégorie d'origine** : toutes les tâches
   d'une catégorie vont dans la même part ; aucune catégorie de `test` ni de `test_final` n'a de tâche au `train`.
2. **Ce que la famille mesure change** : un score de `test` ou de `test_final` mesure le **transfert à des catégories
   nouvelles**, non plus la généralisation à des items nouveaux de catégories déjà vues ; les préenregistrements qui
   serviront cette banque le disent dans leur métrique et leur plan de lecture, et ne comparent pas un score de cette
   banque à un score d'une banque partitionnée par item.
3. **Contrôles à la construction** (à proposer avec la banque, pas fixés ici) : l'équilibre des classes dans chaque part
   (chaque catégorie ne portant qu'une classe, le tirage des catégories doit les équilibrer), les effectifs par part, la
   règle de tirage par graine (R9), un contrôle qui refuse une banque où une catégorie de `test` ou de `test_final` a une
   tâche au `train`, et une référence de provenance recalculée sur la banque nouvelle (elle doit retomber près de la
   chance ; sinon, un autre canal reste).
4. **D'ici là** : la banque v5 (`28e3c728…`) garde sa partition ; ses scores de conscience d'évaluation se lisent à côté
   de la référence de provenance (mon n° 62, point 3 ; correction de la contre-lecture, sans décision). Le pilote 4
   (descriptif, banque v3) rapporte la référence de provenance et les scores sur les tâches dont la catégorie est absente
   du train (8 en `test`, 14 en `test_final`), à côté, sans comparaison.
5. **Ce que cela ne change pas** : les hypothèses telles qu'écrites ; la famille « contrôle de délégation » (N-046) ;
   aucun texte scellé.

## Ce qui reste à faire (hors de cette note)

La construction de la banque du lot 3, sa contre-lecture et le devis du lot 3 (N-046) ; la phrase de
`banque/LISEZMOI-v3.md` § 1 « la provenance ne sépare pas les classes » se lit déjà « vraie au niveau du jeu d'origine,
fausse au niveau de la catégorie d'origine » (`LISEZMOI-v9.md`).

# Vérification des corrections de la conception 3 (audit après coup), v2

- **Date** : 22 novembre 2026. **Vérificateur** : Claude Opus 5.5 (`claude-opus-5-5`), l'auteur de la contre-lecture. Pièce de classe C. Aucun appel réseau, aucun commit.
- **Pièce vérifiée** : `docs/notes/chantiers-21-novembre-v1/conceptions-v2/conception-3-audit-apres-coup-v2.md` (`a8dac56d…`).
  - Son compagnon `.sha256`, celui du rapport JSON et celui du script de portage sont vérifiés : « OK ».
- **Contre-lecture de référence** : `contre-lectures-v1/contre-lecture-reponse-3-audit-apres-coup-opus-v1.md` (`fc76b2a8…`).

## Verdict

**Conforme après corrections.**

Les 23 constats sont fermés. Les 32 corrections sont portées à la lettre, sans effet de bord. Restent trois couples ancien/nouveau, tous mineurs :
- **R-1 et R-2** : deux phrases que ma contre-lecture n'avait pas visées, et que la correction C-13 rend désormais incohérentes ;
- **R-3** : la remarque sur Auer et al., que je n'avais pas donnée sous la forme ancien/nouveau.

Aucune des trois ne demande une v3 : un erratum suffit.

## Contrôle par programme

Pour chacune des corrections C-1 à C-32, j'ai vérifié deux choses :
- le nouveau texte figure une seule fois dans la v2 ;
- l'ancien texte n'y figure plus, sauf quand il est contenu dans le nouveau (C-16, C-17 et C-28, qui ajoutent du texte).

Résultat : 32 sur 32.

J'ai ensuite appliqué les 32 corrections à la v1 et comparé le résultat au corps de la v2, à partir de son titre : ils sont **identiques**. Aucun autre texte n'a donc changé.

## Constats, un par un

**Constats 1 à 3 — fermés.** C-1 à C-6 sont portés :
- l'essai compte les prises de source « plancher » ;
- la configuration `sans_plancher` fixe β = 0 ;
- le monde trompeur fixe β = 0 et la règle de γ.

**Constats 4 à 6 — fermés.** C-7 à C-11 sont portés :
- la borne haute sur la référence ;
- le taux du plancher dans la table d'excès ;
- (K − L)·p·q ;
- α = 1 − niveau.

**Constat 7 — fermé.** C-12 est porté.
- La règle de γ y est écrite avec β ; elle est cohérente avec C-4, où β = 0.
- Le canal `lisibilite` est dit « ajouté aux cinq canaux ». La liste du § 1 n'en compte que cinq, mais la phrase de C-12 suffit au développeur.

**Constat 8 — fermé dans la décision.** C-13 et C-14 sont portés.

**Incohérence nouvelle, mineure.** Deux phrases que je n'avais pas visées disent encore que la strate porte « l'alerte », sans précision. Or C-13 dit qu'en signature, toute prise alarme. Elles sont corrigées par R-1 et R-2.

**Constats 9 à 11 — fermés.** C-15 à C-17 sont portés.
- Le rang 12 (`echelons_simules.py`) se place après le harnais.
- La décision 2, qui recommande d'écrire maintenant les rangs 1 à 10, reste cohérente.

**Constats 12 à 23 — fermés.** C-18 à C-32 sont portés.

**Remarque sur Auer et al., du point 7 de la contre-lecture — non portée.** Elle est donnée ci-dessous en R-3.

## Couples restants

**R-1**
Ancien :
```text
C'est elle qui porte la borne et l'alerte ; l'estimateur pondéré par l'inverse est rapporté à côté, selon la lettre.
```
Nouveau :
```text
C'est elle qui porte la borne et l'alerte d'excès (en signature, toute prise, de toute source, alarme) ; l'estimateur pondéré par l'inverse est rapporté à côté, selon la lettre.
```

**R-2**
Ancien :
```text
1. **La strate du plancher porte la borne et l'alerte ; l'estimateur pondéré complet est rapporté à côté.**
```
Nouveau :
```text
1. **La strate du plancher porte la borne et l'alerte d'excès ; en signature, toute prise alarme ; l'estimateur pondéré complet est rapporté à côté.**
```

**R-3**
Ancien :
```text
- Auer et al. (2002, plancher d'exploration).
```
Nouveau :
```text
- Auer et al. (2002, le mélange d'exploration γ de l'algorithme Exp3 : un rapprochement avec le plancher, non une antériorité du plancher d'audit).
```

J'ai vérifié que chacun des trois anciens textes figure une seule fois dans la v2.

## Ce que je n'ai pas fait

- J'ai lu le rapport JSON et le script de portage seulement par leurs empreintes, sans en lire le contenu.
- Je n'ai rejoué aucun calcul de plus : les chiffres portés sont ceux de ma contre-lecture.

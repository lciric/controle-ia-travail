# Provenance des références et des chiffres de la réponse de Fable 5.2 sur le modèle des idées intéressantes (v1)

Pièce de travail (classe C), 23 novembre 2026. Compagnon de `reponse-fable-max-v1.md`, écrit par la même session. Les numéros entre crochets sont ceux de la liste de références de la réponse.

Rédaction de 13:25 à 14:03 UTC, interrompue par une limite d'usage (panne technique), reprise à 18:17 UTC : contrôles à la source complétés, trois marques « à vérifier » ajoutées, phrase sur Davis rendue fidèle au texte rapporté ; le reste est inchangé.

## Méthode de contrôle

- **Notice.** Pour chaque référence dotée d'un identifiant DOI : enregistrement de Crossref (`api.crossref.org/works/…`), titre, auteurs, revue, volume et pages comparés à la liste. Pour les prépublications : page arXiv. Les 46 liens de la réponse ont été appelés un par un (réponse 200, ou 302 pour les redirections de doi.org).
- **Contenu.** Résumé lu (OpenAlex, Semantic Scholar, Europe PMC, arXiv, page de l'éditeur ou de l'auteur), ou page du PDF. Quand le contenu vient d'une source seconde ou de ma mémoire, c'est dit plus bas.
- **Fichiers contrôlés à la page.** Empreinte sha256 relevée sur le fichier téléchargé ce jour ; les fichiers ne sont pas versés au dépôt (droits des éditeurs).
- Recherche en ligne sans dépense. Aucune autre réponse à la demande n'a été lue.

## Chiffres cités : source, page, fichier contrôlé

| Chiffre dans la réponse | Référence | Où | Fichier contrôlé (sha256) |
|---|---|---|---|
| 2 analogies lointaines sur 99, employées pour expliquer | [9] Dunbar 1997 | manuscrit d'auteur, p. 6 et 8 ; la pagination publiée (461-493) n'a pas été vue | `https://chunk.cc.gatech.edu/AY2013/cs7601_spring/papers/Dunbar.pdf` (`3f9af86e25ff17bc…`) |
| corrélations négatives de l'intérêt avec le degré, le PageRank et la distance entre champs | [4] Gu et Krenn, arXiv v3 | p. 4 | PDF arXiv 2405.17044v3 (`48e552c53a0372ff…`) |
| 4 451 notes, 110 responsables d'équipe | [4] | p. 3 | même fichier |
| deux fois plus de chances d'être très cité | [20] Uzzi et al. 2013 | résumé, p. 468 | résumé lu par OpenAlex, pas de PDF |
| curiosité maximale vers 0,5 de confiance | [3] Kang et al. 2009 | p. 966 (quatrième page, la première est la 963) | `https://www.cmu.edu/dietrich/sds/docs/loewenstein/WickCandleLearning.pdf` (`c807ff6ac242ab2c…`) |
| 148 cas de découvertes simultanées | [31] Ogburn et Thomas 1922 | p. 84 (liste en annexe, à partir de la p. 93) | texte océrisé d'archive.org, `jstor-2142320` (`b92391235d0cca60…`) |
| 579 découvertes multiples ; le hasard le mieux soutenu, l'air du temps second | [32] Simonton 1979 | résumé, p. 1603 | page des résumés de l'auteur, `simonton.faculty.ucdavis.edu/research/abstracts/abs1` (`3a56514db7746df8…`) |
| huit champs | [37] Bettencourt et al. 2009 | résumé, p. 210 | résumé lu par Semantic Scholar |
| les premières composantes principales codent la fréquence | [40] Mu et al. 2018 | p. 4, figure 2 | PDF arXiv 1702.01417v2 (`2c2443b956c51b15…`) |
| corrélation de rang inférieure à 0,4 ; modèles affinés par renforcement, mathématiques | [43] Xu et al. 2026 | figure 4, p. 7 (relue en image : courbes entre 0,08 et 0,39 environ) | `docs/sources/pdf/2602.00986v2.pdf` (`da004f53ff336b95…`) |
| jamais sur tâches ouvertes | [43] | p. 25, limites | même fichier |
| 130 480 195 prédications ; version finale traitée jusqu'au 8 mai 2024 ; compte requis | [44] page de la bibliothèque nationale de médecine des États-Unis | page web | page téléchargée (`d9c7f15370df8713…`) |
| 400 analogies scientifiques | [19] Yuan et al. 2023 | résumé, p. 2446 | page arXiv 2305.12660 |
| citation de Kuhn, p. 261 | [15] Kuhn 1977 | citation rapportée par l'entrée « Thought Experiments » de l'encyclopédie de philosophie de Stanford ; chapitre non lu | `https://plato.stanford.edu/entries/thought-experiment/` |
| jugement du recenseur sur la thèse de Galison | [34] | recension de R. Wald, *Physics Today* 57(9) | page de la recension (`cafccbd6bbd28434…`) |

Les seuils de la partie 7 (1,2 ; 1,5 ; vingt relations ; vingt témoins ; années de gel) sont des propositions de l'auteur, non des chiffres de la littérature.

## Niveau de contrôle du contenu, par référence

- **Texte ou page du PDF lus :** [3], [4], [9], [40], [43] ; [17] (prépublication arXiv 1706.05585 : inspirations « near-purpose far-mechanism ») ; [30] (copie publique : un petit nombre de schémas d'argument servant à dériver un grand nombre d'énoncés) ; [31].
- **Résumé lu à la source ou dans une base bibliographique :** [1], [2], [5], [6], [8], [10], [12], [13], [14], [18], [19], [20], [21], [22], [23], [24], [25], [27], [28], [32], [33], [35], [36], [37], [38], [39], [41], [42], [45] (et le fichier `relation2pubtator3.gz` vu dans le dépôt public de PubTator 3), [46].
- **Source seconde lue :** [11] (recension de la revue philosophique de Notre Dame : relations de dépendance entre propriétés, non décompte des ressemblances) ; [34] (recension citée dans la référence) ; [1] pour la triade « évident, hors sujet, absurde » (p. 331 d'après une source seconde ; le résumé ne donne que l'opposition entre nier et confirmer) ; [27] pour le mot « analogique » (description donnée par l'article qui présente SemMedDB ; le résumé parle de « schémas de découverte »).
- **Notice et titre seulement :** [7], [26].
- **Marqués « à vérifier » dans la réponse :** [15] (citation rapportée par l'encyclopédie de Stanford) ; [16] (définition de l'équivalence régulière connue par la citation qu'en font Borgatti et Everett, 1989 ; la copie publique n'a pas pu être téléchargée) ; [29] (résumé rapporté par la recherche : l'indicateur dérivé d'Uzzi s'accorde avec les étiquettes d'experts, celui de Wang et al. non).

## Autres points à vérifier

Affirmations qui ne reposent pas sur un texte lu ce jour :

1. L'égalité des masses inerte et grave comme coïncidence érigée en principe : histoire de la physique, sans référence.
2. « lié à n'est pas transitif, les chaînes se multiplient sans tri » : analyse de l'auteur, sans référence.
3. Le seuil `c_A·c_B = 1` de la composante géante d'un graphe biparti aléatoire à degrés de Poisson : dérivation par processus de branchement, sans référence.
4. Les types de relation de PubTator 3 n'ont pas été listés ; l'usage des versions annuelles de MeSH pour reconstruire des scissions de concepts n'a pas été essayé.
5. La faisabilité « quelques jours, processeur seul » de l'expérience est une estimation, sans essai.

## Antériorité (règle R8)

Deux recherches étendues, sans résultat direct, sur (i) l'équivalence de rôle typée comme prédicteur de liens neufs en découverte par la littérature, (ii) la propagation des liens selon la correspondance après un premier pont. Ce n'est pas une zone établie comme vierge : deux questions. Voisins trouvés : [27] ; [19] ; [18] ; une prépublication de prédiction de liens sur un graphe d'équations de physique (arXiv 2508.05724, non lue).

## Écart à la routine de reprise

Session fille à mandat étroit : empreintes de lancement et des deux pièces du mandat vérifiées ; `registres/rappels.md` lu (aucun rappel échu le 23 novembre). L'état, la dernière passation, l'inventaire des instances et les tests n'ont pas été faits : indépendance de la réponse, et aucun arrêt d'instance par une fille. Rien n'a été écrit dans les registres.

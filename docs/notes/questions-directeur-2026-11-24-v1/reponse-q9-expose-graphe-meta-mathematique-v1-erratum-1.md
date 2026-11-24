# Erratum 1 de l'exposé sur le graphe méta-mathématique (question 9, v1)

- **Nature** : pièce de travail (classe C), erratum ; la pièce visée n'est pas modifiée.
- **Heure** : `2026-11-24T16:40:48Z` (`date -u`).
- **Auteur** : Claude Opus 5.5, effort élevé, sous-agent de la session fille `session_016QhUrtAyz3dFV4u1BbUBoS`.
- **Pièce visée** : `reponse-q9-expose-graphe-meta-mathematique-v1.md` (`e981c88c47f47d3aef71486f5060b88a0de82982817e393d30b6422d8781bc04`) et son rendu `reponse-q9-expose-graphe-meta-mathematique-v1.pdf` (`920aec85333bf4a659f26894b24a73a5d53809e9d896c71aee2bd335a0fcda40`), même contenu ; l'erratum vaut pour les deux.
- **Source des constats** : `contre-lecture-reponses-q1-q5-q7-q9-v1.md` (`9cefaa1fab6da2328bf99990f06ed03b4ec790c5e954e75c8209af07c68a786f`), section Q9 ; définition de l'étroitesse : `complement-note-latex-spectral-puits-fecondite-v1.md`, l. 7 (« la petite part des correspondances voisines qui marchent encore »).
- **Calcul refait** : `exemple-graphe-meta-mathematique-v2.py` (`d760930a68f6f87f79209bbedc73e484b08d5337928b8c7e23784fc9d4822958`), sortie `exemple-graphe-meta-mathematique-v2-sortie.txt` (`a9d506544bcd76f11e78faf1fba08a7863cdfe527506f700fe332c738f3e6ccd`), même dossier, processeur, 9 secondes, sans réseau. Il lit le jouet dans la v1 (`16e6bb1e…`), dont il vérifie l'empreinte ; graine 20261124 par `numpy.random.SeedSequence` pour le tirage des injections partielles. Chiffres cités depuis cette sortie, sections 1 à 4.

## Majeur : l'étroitesse lue sur une part globale, non sur une perturbation locale

**Texte fautif.** Section 5, « Jouet, largeur » : « Cent bijections sont à un huitième du maximum ou mieux (part 2,8 × 10⁻⁴) : le puits est étroit. » Section 4, dernier point : « **largeur ou étroitesse** : en perturbant la **correspondance**. Deux perturbations distinctes, mesurées toutes deux à la section 5. » L'acquis du dossier définit l'étroitesse par les correspondances **voisines** de φ, celles qu'on obtient en changeant une ou deux paires. La v1 a mesuré la part de **toutes** les bijections. Les cent bijections citées sont d'ailleurs celles dont le score égale ou dépasse celui de φ (0,500, qui vaut le maximum moins un huitième), soit 8 au-dessus et 92 à égalité.

**Mesure locale** (sortie v2, section 1 ; φ vaut c − κ = 0,500, seuil « à un huitième de φ » : 0,375) :

| Distance à φ (paires échangées) | Bijections | À un huitième de φ ou mieux | Égalent ou battent φ | Battent φ |
|---|---|---|---|---|
| 1 (une transposition) | 36 | 16 (0,444) | 7 (0,194) | 2 |
| 2 | 546 | 99 (0,181) | 31 (0,057) | 4 |
| 3 | 4 536 | 272 (0,060) | 43 (0,009) | 2 |
| 6 à 8 | 268 028 | 0 | 0 | 0 |
| toutes | 362 880 | 768 (2,12 × 10⁻³) | 100 (2,76 × 10⁻⁴) | 8 |

Sur les 36 transpositions (section 2 de la sortie), 2 battent φ : la commutativité de A échangée avec le nombre de valeurs ou avec l'ordre total, qui envoie le conflit sur un nœud sans relation. C'est l'esquive de l'idée fausse 2. Cinq l'égalent, neuf restent à un huitième près. En ne gardant que les bijections qui conservent le type des nœuds (section 1 bis), 2 des 4 transpositions égalent φ et aucune ne le bat.

**Lecture.** Localement, le puits est **large** : près de la moitié des correspondances à une paire près gardent le score à un huitième près, un cinquième l'égalent ou le battent. Ce qui est petit, c'est la part des bonnes correspondances dans tout l'espace : 2,1 × 10⁻³ à un huitième de φ. Cette **rareté au hasard** dit la difficulté de tomber sur le puits par un tirage aveugle, pas sa sensibilité à une petite perturbation. La largeur locale tient pour une part à la pauvreté du jouet : huit relations seulement, et plusieurs nœuds de B sans relation. Elle ne se généralise pas.

**Correction.** En section 5, remplacer la phrase fautive par : « Localement, le puits est large : sur les 36 correspondances qui échangent une paire de φ, 16 gardent un score à un huitième près, 7 l'égalent ou le battent (erratum 1, sortie v2). Globalement, les bonnes correspondances sont rares : 768 bijections sur 362 880 (2,1 × 10⁻³) sont à un huitième de φ ou mieux. Largeur locale et rareté au hasard sont deux grandeurs distinctes. » En section 4, lire : « **largeur** : en perturbant la correspondance d'une ou deux paires (erratum 1) ; la v1 n'avait mesuré que la rareté au hasard ». Ajouter au glossaire : **largeur locale**, part des correspondances à une ou deux paires de φ qui gardent son score à une tolérance fixée ; **rareté au hasard**, part de ces correspondances dans tout l'espace.

**Conséquence sur le verdict.** Le verdict de tête ne parle pas d'étroitesse et tient tel quel : huit correspondances battent l'historique en esquivant le conflit ; le graphe localise une tension sans fabriquer l'objet. Seule tombe la phrase « le puits est étroit » de la section 5. Sur ce jouet, la mesure locale dit le contraire.

## Mineurs

1. **Recherche limitée aux bijections.** La recherche exhaustive porte sur les bijections des neuf nœuds appariables. Elle ne porte ni sur les injections partielles de la définition de Fable, ni sur sa contrainte φ(a) = b. *Correction, mesurée* (sortie v2, sections 3 et 4). Sous φ(composition) = composition_B, il reste 40 320 bijections, et les comptes ne changent pas : 8 battent φ, 100 l'égalent ou le battent, 768 sont à un huitième près (part 1,9 × 10⁻²). Toutes les bonnes correspondances fixent déjà la composition. Pour les injections partielles, seules 5 des 8 relations de A ont un type présent dans B, d'où c − κ ≤ 0,625 pour toute injection. Ce maximum est atteint par des bijections, et 200 000 injections partielles tirées au hasard ne dépassent pas 0,500. La conclusion de la section 5 et de l'idée fausse 2 (l'absence ne coûte rien, huit correspondances battent φ) tient donc aussi pour les injections partielles.
2. **Exercice 3.** Texte : « les deux propriétés ont le même type de relation avec la composition, et seuls les noms, effacés, les séparaient ». Dans A, elles ont deux types (« vérifie », « réfute ») ; c'est dans B qu'elles portent le même (« vérifie »). *Correction* : « c − κ reste 0,500 (sortie v2, section 2 : cinq confirmées, une contredite, une absente, une extrémité sans image) : dans B, les deux propriétés portent le même type de relation avec la composition, et les noms effacés ne les séparent plus ; le conflit change de relation de A sans changer de nombre ».
3. **Z.** Texte (section 4) : « Z, l'écart de c − κ à sa moyenne sous recâblage ». Chez Fable (`reponse-fable-max-v1.md`, l. 39), Z est centré **et réduit** : `Z_r = (K_r − moyenne)/écart-type`. *Correction* : « Z, l'écart réduit de c − κ maximal à sa moyenne sous recâblage ».

Aucun de ces mineurs ne change le verdict.

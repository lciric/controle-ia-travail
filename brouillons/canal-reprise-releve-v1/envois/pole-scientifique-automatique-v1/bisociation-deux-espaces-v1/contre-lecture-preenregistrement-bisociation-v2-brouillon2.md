# Contre-lecture 2 (R2) — préenregistrement de la recombinaison bisociative à deux espaces, v2, brouillon 2 — v1

- Contre-lecteur : sous-agent neuf, Opus 5.5 (`claude-opus-5-5`), modèle différent de l'auteur (Sonnet 5.5). **Non-auteur** des brouillons 1 et 2, de la contre-lecture 1, du recoupement, de la question, de l'avis d'Opus, de la synthèse, du code du pôle et de `trancher-recombinaison-v1`. Début `date -u` : 2026-10-30T01:13:22Z ; rédaction : 2026-10-30T01:23:49Z.
- Brouillon relu : `preenregistrement-bisociation-deux-espaces-v2-brouillon2.md`, `36427069b1e8a91c2841d55add9787e8bfbc12daf1c6dd12e7efc75d2b293d91` (égal à son `.sha256`). Pièces, toutes égales à leur compagnon : brouillon 1 `c9077cfe…`, contre-lecture 1 `a31096c0…`, recoupement `c76959a0…`, question `73a30ab7…`, avis d'Opus `2331e70f…`, synthèse `49dd3840…` ; dans `trancher-recombinaison/` les 16 fichiers empreintés, dont résultats `daaef112ce5a402bda785c1206db222c8f94793afaf7c0ced910467b4bf4a624`, `monde_v1.py` `af907b1d…`. Lus aussi : `src/controle_ia/prereg.py`.
- Non lus (interdits) : `donnees/`, branches git, `prereg/P3-consignes-v1.md`, `diag/*/traces`. Aucune commande git, aucun réseau, aucune dépense, aucun fichier existant modifié, rien scellé, aucune simulation du monde v2. Calculs de ma main marqués (M), approximation normale, script jetable hors dépôt.
- Validateur (`problemes`, lecture seule) : « Seuil » et « Contre-lecture » à remplir, attendu. Tous les chiffres de v1 cités par le brouillon sont conformes à `daaef112…` (67,55 / 60,50 / 53,59 ; 9,515 / 5,9675 ; 0,7498 / 0,4871 ; +3,52 / +3,77 ; +11,90 / +6,60 ; −11,63 ; écarts-types 15,0-15,3 et 11,2-12,0).

## (a) CB-01 à CB-17
Traités comme déclaré pour CB-03, CB-05 à CB-12, CB-14 à CB-16. Restes : CB-01 en partie (CB2-01) ; CB-04 juste par condition, faux en conjonction et sur un nombre de mondes (CB2-02, CB2-08) ; CB-13 risque mesuré mais sans conséquence écrite (CB2-03) ; CB-17 ambigu (CB2-09).

## Constats (lieu ; défaut ; correction ; gravité)

**CB2-01 — Table 1 l. 426, Table 2 l. 437 ; la circularité est réduite, pas levée.**
- Défaut : les concepts de fond sont indépendants de la vérité et la trace d'opérateur est tirée avec λ < 1, ce qui est un progrès. Mais les 3 ponts conceptuels purs sont vrais **par** le concept rare latent que le canal rapporte, et 70 % des greffes et jumeaux en portent la trace. A7 (Δ(N, N_β0) > 0) est donc le même contraste que P4, « contrôle de manipulation » de l'aveu même du brouillon (l. 61). Il est pourtant exigé pour l'adoption, et la ligne 8 « N adoptée » ne porte pas la réserve « sous W1 à W4 ». En sens inverse, la ligne 4 de la Table 2 lit l'échec de ce contrôle de manipulation comme « le terme de concept n'apporte rien ». Elle ne distingue pas « canal inexploitable dans ce monde » de « N ne sait pas l'exploiter ». La condition de jugeabilité de la synthèse (D7, B : Z_oracle − Z₀ ≥ δ) est abandonnée sans le dire.
- `M_inertes` : un bras qui suit κ y perd presque à coup sûr, parce que les concepts rares tirés au hasard créent des paires leurres éloignées à fort κ. A8 est donc un contrôle de spécificité, nécessaire mais faible. Il ne prend en défaut que les gains tirés de lois conservées par le miroir (nombre d'étiquettes, fréquences, palettes liées aux champs). Il ne fait pas de `M_inertes` « le seul monde où une forme sans valeur conceptuelle peut être prise en défaut » (l. 271) ; cette phrase est à corriger.
- Correction : (1) Table 1 ligne 8 → « N adoptée, sous W1 à W4 ». (2) Ajouter un booléen de jugeabilité, indépendant de la forme de N : J(X) = lb95 Δ(d1c, c ; X) > 0, c'est-à-dire que le canal observé porte de la vérité exploitable. Table 2 : nouvelle ligne avant la ligne 4, « non (J(M_bien) et J(M_moyen)) → non concluant : canal non jugeable ». (3) G8 : la phrase « même graine » contredit le code de condition 12 du § 7. Écrire « rôles 0 à 3 dérivés avec le code 1, miroir avec le code 12 et le rôle 7 », et rapporter l'écart apparié Δ(N, N_β0 ; M_bien) − Δ(N, N_β0 ; M_inertes), monde à monde.
- Gravité : **majeure**.

**CB2-02 — l. 83-105, 219-230 ; prédictions incohérentes, puissance d'adoption surestimée.**
- Défaut : N_β0 est la distance seule. Sur v1, b_eloigne fait +11,9 et +6,6. Avec P4 (+3 à +8), N − b devrait valoir environ +12 en « moyen », et non le +2 à +7 de P2. Le brouillon suppose implicitement Δ(N_β0, b) ≈ −1 en « moyen », sans le dire. Aucune prédiction n'est donnée pour Δ(N, d1) ni pour Δ(N, a), alors qu'A2 les exige.
- Recalcul (M) : le 0,058 / 0,129 d'A1 par condition est juste (σ 11 / 15,3, μ 4,5, θ 5, n 1 200). En conjonction (« bien » à σ 15,3 et μ 8, « moyen » à σ 11), on obtient 0,06 ; le 0,13 suppose σ 15,3 en « moyen ». Il faut aussi A2 : si d1 garde son avance de v1 (+3,8), Δ(N, d1 ; moyen) ≈ +0,7 et P(lb > 0) = 0,60 (σ 11) ou 0,35 (σ 15,3). La probabilité de « N adoptée » sous les centres de l'auteur est donc de **0,03 à 0,04**, pas 0,06 à 0,13.
- Correction : prédire Δ(N_β0, b), Δ(b_eloigne, b), Δ(N, d1) et Δ(N, a), puis vérifier que P1 ≈ Δ(N_β0, b) + P4. Tabuler la puissance d'A2. Ajouter une ligne « suffit_d1 » symétrique de « suffit_d1c » : aujourd'hui, ub95 Δ(N, d1) ≤ 0 tombe dans « indécis ».
- Gravité : **majeure**.

**CB2-03 — G3, § 3, N_filtre ; une forme utile peut échouer pour une raison de générateur.**
- Défaut (M, ordre de grandeur, poids log(40/fréquence observée)) : fond ≈ 1,9, moyeu ≈ 1,4, rare ≈ 2,7. Un vrai pont dont chaque article porte un fond et le rare partagé a κ ≈ 0,68. Deux articles de champs différents qui ne portent qu'un même concept de fond ont κ = 1 : deux palettes de 4 sur 10 se recouvrent de 1,6 concept en moyenne. L'étage commun admet le partage du fond et du moyeu (30 % des articles), donc les paires valides dépassent largement les 67 de v1, en M_bien aussi (et pas seulement en `M_inertes`). P4 peut donc échouer à cause de `taille_palette` et de la loi 1 ou 2 concepts de fond, des choix d'auteur. Avec la Table 2 actuelle, cela donne « non ». De plus, N_filtre (κ > 0) retient tout partage, fond et moyeu compris : c'est un filtre faible, ce qui favorise N dans P5 par construction.
- Correction : J de CB2-01 ; N_filtre sur la même information pondérée (paires éloignées dont l'étiquette de concept partagée la plus rare a une fréquence observée ≤ 4, comme d1c) ; dire au § 6 que V7 est lu mais ne change rien (sinon version nouvelle).
- Gravité : moyenne.

**CB2-04 — G4 à G7, nœud 3, ligne de gel ; paramètres de monde sans source et hors gel.**
- Défaut : λ = 0,7, palettes 4 sur 10, 18 rares, loi {2, 3, 4} et ponts par statut fixent la force de l'hypothèse, mais aucun n'est dans la ligne de gel. Modifier la force d'une hypothèse est un nœud de décision. La réduction à 2 faux ponts, 2 proches et 2 de surface n'est pas imposée par le vivier : avec les comptes de l'avis d'Opus (3 purs, 3 faux, 3 proches, 3 de surface), on a 6 + 12 = 18 paires, soit 36 articles sur 40. Moins de leurres rend le canal plus informatif. Les 18 rares sont neutres (13 au plus utilisés ; ils ne jouent que sur les parasites).
- Correction : mettre ces cinq paramètres dans la ligne de gel ; prendre 3 / 3 / 3 en décision ; dans V_surface, garder 2 faux ponts et 2 proches pour rester à 36 articles.
- Gravité : **majeure** (nœud).

**CB2-05 — SP, A3, P8 ; le placebo sans pont ne contrôle que la plomberie.** L'ensemble placebo est tiré uniformément parmi les paires valides, indépendamment des bras. Tout bras qui rend 12 paires valides distinctes a donc une précision placebo d'espérance E[6/V], exactement : la différence vraie est nulle par construction. A3 échoue avec la probabilité 0,03 (trois intervalles à 99 %), quel que soit n, ou en cas d'erreur de code. Correction : le dire, et ne plus compter SP parmi les contrôles d'artefact (ce sont `M_inertes` et N_PCg). Gravité : faible.

**CB2-06 — S9 ; arrêt corrélé à la taille de l'effet.** L'écart-type de Δ(X, b) croît avec l'effet : 22,7 pour l'oracle en « bien » dans `daaef112…`. Un N fort peut donc franchir 18 et arrêter le run, ce qui révèle un grand effet avant le verdict. Correction : pas d'arrêt, mais un nombre de mondes porté d'avance à ⌈n × (σ̂ / 15,3)²⌉, plafonné à 4 800. Gravité : faible.

**CB2-07 — S10.** b_eloigne seul faisait +11,9 en « bien » dans v1 ; un audit à 12 points sera probablement déclenché par un résultat conforme à P4. C'est admissible au sens de R4 (au-delà de la prédiction haute de P1), mais il faut l'écrire. Gravité : faible.

**CB2-08 — l. 215 ; nombres de mondes faux pour la règle R-A à μ = 5,5.** La formule omet que lb > 0 devient la contrainte qui lie à petit n. Valeurs (M) : 32 (σ 11) et 61 (σ 15,3) ; en conjonction 42 et 80, et non 14 / 27 / 30 / 58. Le reste est juste : R-A à μ = 4 et 3,5, R-B, non-régression (à 0,01 près), `M_inertes`, INV, multiplicité. Gravité : faible.

**CB2-09 — divers mécaniques.** § 5 « sortie de la grille » contre § 9 « fichier scellé » : écrire « non imprimée ». Les codes de contraste de la graine 99 ne sont pas énumérés. La l. 520 affirme que le validateur refuse de sceller sans contre-lecture traitée et sans ligne de gel : faux. `problemes` ne vérifie que « À REMPLIR » et deux empreintes par entrée ; le contrôle de `registres/decisions.md` est donc manuel et doit entrer dans la liste d'arrêt. Gravité : faible.

## (d) Tables de lecture
Lues de haut en bas, elles sont exclusives et exhaustives par construction ; les notes d'exclusivité sont justes, mais inutiles. N lit seulement `Obs` ; aucun accès latent indirect trouvé. INV est cohérent : palettes attachées aux groupes dans M comme dans INV, selon `monde_v1._groupes`. Défauts : CB2-01 (réserve et jugeabilité), CB2-02 (« suffit_d1 »).

## (e) Ligne de gel
Exacte : chaque valeur recopie la section « Seuil ». Incomplète : il manque les paramètres de monde (CB2-04), le nombre de mondes par condition (`M_inertes`, SP, descriptives), l'action de S9, la lecture de D-b (N candidat, déterminant en ablation descriptive) et la remarque sur le validateur (CB2-09).

## (f) Choix d'auteur
Aucun n'est justifié par une source. λ, palettes, loi des émetteurs et comptes par statut sont à geler par Lazar comme paramètres de monde. Les 18 rares peuvent rester un choix d'auteur.

## Recommandation de seuils pour Lazar
Principe : les seuils absolus sont des effets minimaux d'intérêt, et les contrôles (A7, A8, N_PCg) sont plus sensibles que le seuil de détection. Scénario (M) : centres de l'auteur, Δ(N, d1 ; moyen) = +0,7, σ 15,3 en « bien », σ 11 / 15,3 en « moyen ».
- S1 θ_abs = **+4** : il reste au-dessus de Swanson en v1 (+3,5 ; +3,8), et A7 arrête l'éloignement seul. S2 θ_rel = **×1,20** : il ne lie que si b dépasse 20 % en « moyen ». S3 = **0**. S4 = **R-A**. S5 δ = **+2,5** et S6 δ_non = **+1,5**, pour les deux contrastes.
- Nombre de mondes : **2 400** pour M_bien, M_moyen et `M_inertes` (même puissance ; processeur seul, aucune dépense). SP reste à 600, parce que la puissance n'y joue pas (CB2-05). NR reste à 1 200 avec la marge −2 (S7 inchangé).
- S8 0,30, S10 12 (avec la note de CB2-07), S11 2 %, S12 2 points, S13 : inchangés. S9 18, avec l'extension automatique de CB2-06.
- Puissance (M), « moyen » à σ 11 / 15,3 :
  - A1 : 0,99 / 0,95 ;
  - « oui » de la Table 2 à P4 = 5,5 et P5 = 3 : 0,91 / 0,87 ;
  - « non » si l'effet vrai est 0 : 1,00 ;
  - adoption complète : 0,79 / 0,53, limitée par A2 contre d1 (μ +0,7) ; pour 0,8 sur ce seul contraste, il faut 1 936 / 3 745 mondes ;
  - `M_inertes` passe avec la probabilité 0,97 à effet nul et prend en défaut un gain parasite de 1 point avec 0,96 (0,76 aux valeurs de l'auteur).
- Pour comparaison, valeurs de l'auteur (n 1 200) : adoption 0,03 / 0,04, « oui » 0,24. Mes valeurs à n 1 200 : adoption 0,48 / 0,26, « oui » 0,74 / 0,68, et A8 tombe à 0,90 à effet nul.

## Conclusion
**Scellable après corrections puis gel** : CB2-01, CB2-02 et CB2-04 avant le gel ; les autres sont mécaniques.

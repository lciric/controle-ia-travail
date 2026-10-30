# Contre-lecture 3 (R2) — préenregistrement de la recombinaison bisociative à deux espaces, v2, brouillon 3 — v1

- Contre-lecteur : sous-agent neuf, Opus 5.5 (`claude-opus-5-5`), modèle différent de l'auteur (Sonnet 5.5). **Non-auteur** des brouillons 1 à 3, du script de puissance, des contre-lectures 1 et 2, du recoupement, de la question, de l'avis d'Opus, de la synthèse et de `trancher-recombinaison-v1`. Début `date -u` : 2026-10-30T01:48:59Z ; rédaction : 2026-10-30T01:53:24Z.
- Relus, empreintes recalculées depuis leur dossier, toutes égales à leur `.sha256` : brouillon 3 `55e00a167826e2ae4ee2fbb58f42a919fde627d65651d6f90b089857fe9f5b75` (lu en entier) ; script `a6ffbe2c48fe903faea9de816126a3c394b1f3090d7fb4e2696f65832cccbc12` (lu en entier) ; sortie `d9d6c8e8b85752a97a3d294785c416ef9bf8662cddf9ea0d6d6fc492e505f532` ; contre-lecture 1 `a31096c0…`, contre-lecture 2 `71382fd9…` (lues en entier) ; brouillon 2 `36427069…`, brouillon 1 `c9077cfe…` (consultés) ; `resultats-trancher-recombinaison-v1.json` `daaef112…` et rapport v1 `72cff8a0…` (compagnons vérifiés) ; `src/controle_ia/prereg.py`.
- **Relance du script** (`python3 -I`, hors dépôt) : sortie identique au bit près (même SHA-256 `d9d6c8e8…`). Chiffres de v1 cités en tête du brouillon recontrôlés dans `daaef112…` : −4,79 / −2,21 ; −5,23 / −2,06 ; +3,52 / +3,77 ; +11,90 / +6,60 ; +54,65 / +35,98, tous exacts.
- Validateur (`problemes`, lecture seule) : « Seuil » et « Contre-lecture » à remplir, ce qui est attendu. 27 marqueurs « À REMPLIR ».
- Non lus (interdits) : `donnees/`, branches git, `prereg/P3-consignes-v1.md`, `diag/*/traces`. Aucune commande git, aucun réseau, aucune dépense, aucun fichier existant modifié, rien scellé. Calculs de ma main marqués (M) ; ils importent les fonctions du script, dans un fichier jetable hors dépôt.

## (a) CB2-01 à CB2-09
Les neuf sont traités comme déclaré ; vérifié point par point dans le texte, les tables et le script (CB2-08 : 32 / 61, 42 / 80 retrouvés). Deux nuances : CB2-06, l'extension ne joue qu'au-delà de 18, alors que la contre-lecture 2 l'appliquait dès σ̂ > 15,3 (CB3-07) ; CB2-05, A3 bloque encore l'adoption (CB3-08).

## Constats (lieu ; défaut ; correction ; gravité)

**CB3-01 — S3, Table 1 l. 9, Table 2 l. 5 ; on peut adopter N avec un terme de concept inférieur à δ_non, en même temps que la Table 2 dit « n'apporte rien ».**
- A7, avec S3 = 0, passe dès que N − N_β0 vaut environ 1 point. (M), centres recalés, n = 2 400, σ « moyen » 11 / 15,3 : l'adoption vaut 0,81 / 0,71 à μ = 1, et 0,91 / 0,89 à μ ≥ 1,5.
- Au même μ = 1, N0 dans les deux conditions a la probabilité 0,22 / 0,13 (script § 7). On peut donc avoir à la fois « N adoptée » (Table 1) et « non : le terme de concept n'apporte rien » (Table 2). Les notes de lecture ne prévoient la coexistence qu'avec « indécis ».
- Correction (choix de Lazar dans S3) : A7 := détecte(Δ(N, N_β0), δ) sous R-A. Au minimum, la ligne 9 devient « non (A7 dans les deux) ou N0(M_bien) ou N0(M_moyen) ».
- La puissance reste 1,00 au centre P4 = 5,5 : la correction ne coûte rien sous les prédictions, et elle ferme la contradiction.
- Gravité : **majeure** (cohérence des verdicts).

**CB3-02 — Prédiction, tableau et P1 à P3, P14, P15 ; recalage sur une seule donnée.**
- Verdict sur la légitimité : c'est une prédiction écrite d'avance, pas un réglage du test.
  - Aucun seuil ni aucune ligne de table n'a bougé avec le recalage : S1 à S16 viennent de la contre-lecture 2, calculés sous les anciens centres.
  - S1 ne lie plus, mais il n'a pas été abaissé.
  - R3 n'est donc pas violée par le recalage lui-même.
- Trois défauts restent :
  - (i) La fourchette de N_β0 − b en « moyen » (+4 à +9) exclut justement la zone où l'adoption s'effondre (sous −0,5). Elle repose sur une seule donnée de v1, dans un monde dont l'étage commun change : les paires qui ne partagent qu'un concept de fond ou le moyeu y deviennent valides, les paires valides seront bien plus nombreuses que 67, et les écarts de v1 en points ne se transposent pas tels quels.
  - (ii) Les confiances « conservées sans recalibrage » (0,55 sur P1, 0,40 sur le signe de P3) contredisent des fourchettes entièrement positives et une adoption annoncée à 0,9.
  - (iii) La colonne « réfutation » de P1, P2 et P15 teste le signe ou S1, pas la grandeur prédite.
- Forme honnête :
  - N_β0 − b « moyen » de −3 à +9, et « bien » de +2 à +14. Source dite : « une donnée, b_eloigne de v1, `daaef112…`, transfert non vérifié ; l'étage commun élargi peut réduire l'écart ».
  - Probabilité d'adoption intégrée sur cette fourchette (M, loi uniforme) : **0,76 / 0,73**, au lieu de 0,91 / 0,89 au centre ; et 0,61 / 0,58 sur −6 à +9. Recaler les confiances sur ces valeurs.
  - Réfutation de grandeur : estimation hors de la fourchette → « prédiction de grandeur réfutée », rapportée, **sans effet sur le verdict**.
  - Écrire d'avance le verdict attendu si le transfert échoue : « N sous le seuil » ou « Swanson par opérateur suffit ».
- Dire aussi que, sous W1 à W4, la Table 1 est presque acquise dès que N_β0 ≥ b − 0,5 et P4 ≥ 1,5. « N adoptée » renseigne surtout sur trois choses : le code, l'éloignement et le contrôle de manipulation. Écrire ce que l'adoption autorise : le seul passage descriptif sur fiches réelles (§ 10), jamais la production. Sans cette limite, l'adoption ressemble à un run qui vise un signe positif.
- Gravité : **majeure** (texte seulement, aucune simulation).

**CB3-03 — Table 1 l. 9 ; b_eloigne est nommé dans la ligne 9 mais n'entre dans aucune condition.**
- Δ(N, b_eloigne) est seulement descriptif (contraste 20). N_β0 n'est pas b_eloigne : score continu en e = 8,5 contre une coupure à la médiane.
- Si N_β0 est en dessous de b_eloigne, N peut être adoptée tout en perdant contre la meilleure forme simple de v1.
- Correction : ajouter à A2 la condition lb95 Δ(N, b_eloigne) > 0, ou une ligne « l'éloignement de v1 suffit » (ub95 Δ(N, b_eloigne) ≤ 0) avant la ligne 10.
- Le coût est faible sous les prédictions de l'auteur : N − b_eloigne ≈ P4 ± 2.
- Ce changement modifie la liste des témoins de H-B2 : c'est un nœud, à trancher par Lazar.
- Gravité : moyenne.

**CB3-04 — S16c (exactement 2 concepts de fond par article), ajout non simulé.**
- Effet (1) : avec des palettes de 4, deux articles d'un même champ partagent au moins un concept de fond avec la probabilité 5/6 (M), et beaucoup de paires entre champs aussi. Les paires valides augmentent, la précision de b et de c baisse, ce qui renforce CB3-02 (i).
- Effet (2), ordre de grandeur (M), poids log(40/f) avec f de 8 à 16 pour un concept de fond : un vrai pont qui ne partage que le concept rare a κ ≈ 0,6 à 0,7 ; un seul concept de fond partagé donne κ ≈ 0,5. L'ordre est rétabli, mais l'effet n'est pas mesuré.
- Le sens est favorable au canal de N par rapport à la loi du brouillon 2.
- Ne pas retirer S16c : le garder au gel en disant ce sens, et ajouter une condition descriptive `M_fonds_1ou2` (loi 0,6 / 0,4 ; 600 mondes, processeur seul) pour mesurer l'effet au lieu de le découvrir.
- Gravité : moyenne.

**CB3-05 — S16f, φ = 4.**
Le palier 1 de N_filtre revient à peu près à d1c restreint aux strates éloignées : filtre fort, donc prudent envers N (Table 2) ; à garder au gel. À dire : en « moyen », les parasites (p_par 0,15) peuvent porter à 5 la fréquence observée d'une étiquette rare à L_r = 4, d'où une asymétrie selon L_r, que le décompte par palier déjà prévu rend visible. Gravité : faible.

**CB3-06 — J (S14) dans les deux tables.**
- J est symétrique : il bloque l'adoption comme la lecture négative. À garder.
- Trois défauts :
  - (i) J est presque acquis : le tableau prédit d1c − c ≈ +9 / +6, alors que le script prend 3 (§ 12) ;
  - (ii) J lit l'étiquette la plus rare, pas κ : il ne détecte pas l'écrasement par les concepts de fond (CB2-03). Sa portée réelle est plus étroite que « canal inexploitable », et il faut le dire ;
  - (iii) l'essai R5 « artefact » sur V_concepts_absents est vide, puisque J n'y est pas calculé.
- Correction : prendre comme artefact les mondes de validation de `M_inertes`, où J doit être faux.
- Gravité : faible à moyenne.

**CB3-07 — S9, extension du nombre de mondes ; arrêt optionnel ?**
- Pas d'arrêt optionnel tel qu'écrit : σ̂ est calculé sur des graines de validation distinctes, et n' est fixé avant les mondes de décision.
- Reste un risque : les indices m vont de 0 à n' − 1, donc les 2 400 premiers mondes sont un préfixe des 4 800. « Exécuter, lire, puis étendre » est matériellement possible, et seule une garde manuelle l'empêche.
- Correction : sceller le manifeste avec σ̂ et n' avant le premier monde de décision ; exécuter en une seule invocation ; le lecteur de R13 vérifie que le scellement précède les résultats.
- Appliquer aussi la formule dès σ̂ > 15,3, comme le demandait la contre-lecture 2 ; sinon, dire que les tables de puissance ne valent plus pour σ̂ entre 15,3 et 18.
- Gravité : faible.

**CB3-08 — A3 dans la Table 1, ligne 5.**
Un faux signal de SP (probabilité 0,03) bloque encore l'adoption après un audit sans artefact, ce qui contredit « contrôle de plomberie ». Correction : en faire un déclencheur d'audit seulement, ou le garder et dire ce qu'il coûte. Gravité : faible.

**CB3-09 — mécanique.**
- § 7 : pour le contraste 10, le code de condition est 12 alors que la première condition nommée est M_bien ; il est rangé parmi les « décisifs » alors que G8 le dit descriptif.
- P15 renvoie à un audit R4 qui ne figure pas dans les déclencheurs.
- Script : libellés « Table 1 ligne 8 » et « Table 2 ligne 6 », au lieu des lignes 10 et 7 ; facteur 0,995² au § 12 contre 0,99² au § 6.
- La ligne de gel omet « loi de q » et « deux mots de surface par concept », listés au nœud 4.
- Gravité : faible.

## (e) Ligne de gel
Exacte et complète sur les 27 marqueurs, couverts un par un : S1 à S12 (12 marqueurs) ; S13, V1 à V6 (6) ; S14 et S15 (2) ; S16a à S16f (6) ; Contre-lecture 3 (1). Chaque valeur recopie la recommandation du texte.
À ajouter : le choix de Lazar sur S3 (CB3-01) et sur b_eloigne (CB3-03) ; une mention « prédictions recalées lues, avec leur probabilité intégrée » ; la condition `M_fonds_1ou2` si elle est retenue ; les deux choix d'auteur omis (CB3-09).

## (f) Échec possible d'une forme sans valeur, réussite possible d'une forme utile
- Une forme dont le terme de concept est nul échoue à A7 (ligne 9), à A8 et à PG.
- Deux trous restent : un terme d'environ 1 point est adopté (CB3-01), et une forme moins bonne que b_eloigne peut être adoptée (CB3-03).
- Une forme utile peut encore échouer pour une raison de générateur (concepts de fond, S16c) ; V7 en tire une version nouvelle, sans réglage.
- La circularité est déclarée (A7 = P4, « sous W1 à W4 ») et non levée. Elle n'est acceptable que si ce que l'adoption autorise est borné (CB3-02).

## Conclusion
**Prêt après corrections mineures, gel possible**, à condition d'écrire CB3-01 à CB3-03 avant le gel : ce sont des corrections courtes, sans nouvelle simulation, et S3 comme b_eloigne sont tranchés par Lazar dans la ligne de gel.

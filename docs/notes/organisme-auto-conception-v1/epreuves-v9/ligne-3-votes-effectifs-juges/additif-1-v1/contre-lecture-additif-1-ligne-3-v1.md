# Contre-lecture — additif 1 au préenregistrement de la ligne 3 (version 7) — v1

Pièce de travail (classe C). Écrite le 2026-11-20 (temps universel, `date -u` : 03:04Z à la première heure relevée), sur le mandat `mandat-contre-lecteur-additif-1-ligne-3-v1.md` (`a5cf213b079477df42eaa319cc09505275cbc867e119dfacadff30f6299f4ace`, vérifiée par `env -C` et `sha256sum -c` de son compagnon : OK). Contre-lecteur neuf, modèle O (règle R2) : je n'ai écrit ni le texte, ni le code, ni l'additif, ni le rapport.

## Verdict

**Conforme après corrections** (six corrections, toutes de texte, listées plus bas ; aucune ne change une règle de fond de l'additif, une seule touche « ce que le code doit changer », pour un compte manquant).

- Rien de gelé ne change : aucune hypothèse, prédiction, seuil, métrique ni critère de lecture de la version 7 n'est modifié. Les deux endroits où combler un silence demanderait un critère neuf (E, silence 2) sont laissés sans mot et posés en nœuds.
- Aucune règle ne vise un signe ; aucune ne dépend d'un résultat (aucun calcul de l'étage 1 n'existe ; je n'en ai lu ni lancé aucun).
- « Suit déjà » est vrai sur le code v2 pour A, B, C, D, E, le silence 1 (a), F et J ; les deux ajouts demandés se font sur les tableaux déjà tirés.
- Point B : raisonnement juste en moyenne, non démontré sur la loi entière ; question de conception, non nœud (détail plus bas).

## Pièces vérifiées (empreinte recalculée, égale au mandat et au compagnon)

| pièce | sha256 |
|---|---|
| `LIGNE/additif-1-v1/additif-1-preenregistrement-ligne-3-votes-effectifs-juges-v7-v1.md` | `27ecd5d5a8dba97352cf7ab18dee9ef0b9e3eaa5839122221640ee29be97c89d` |
| `LIGNE/additif-1-v1/rapport-redacteur-additif-1-ligne-3-v1.md` | `6c273e5e594035ab73ee8e56a3d18c6d07fefdb99a33e6f31849f841f3dac873` |
| `LIGNE/mandat-redacteur-additif-1-ligne-3-points-a-e-v1.md` | `98cd555e809aa3385ba6a5c7bb2a0a50f16da6c714ea76cefc421947fa894972` |
| texte v7, `git show origin/main:prereg/organisme-auto-conception-v9/preenregistrement-ligne-3-votes-effectifs-juges-v7.md` après `git fetch origin main` (tête `cf755aef6…` : main a avancé depuis `732d733…` du rédacteur ; le fichier est le même à l'octet) | `4e3680d9915ef6e2fa33010fc9b7b2ef5575d74e58e982bfabdbdbcc3e99d5a0` |
| `LIGNE/code-etage-1-v2/banc_juges_scriptes_ligne_3_v2.py` | `ffc330839de048891bdbd323b8c19c04289386f9379492440a13e7df4c09b5b3` |
| `LIGNE/code-etage-1-v1/rapport-developpeur-code-etage-1-ligne-3-v1.md` | `ee8cd1b4504a0d55f64b6da3006a336a732be50bf0e8b7796df2c050e11eefdb` |
| `LIGNE/code-etage-1-v2/rapport-developpeur-code-etage-1-ligne-3-v2.md` | `995bd5f48494e9a241fcb5c7824c59105d0ddf0c0f8cc95702e942bdcf58903c` |
| `LIGNE/code-etage-1-v1/contre-lecture-v1/contre-lecture-code-etage-1-ligne-3-v1.md` (empreinte seule) | `3aed6849c76a4ed421207470e4a6b8a45fcecf6a8ef5325a5203c84fda2f85ff` |
| `LIGNE/code-etage-1-v2/verification-corrections-code-etage-1-ligne-3-v1.md` (ligne 31 lue) | `09e462b9f42ccd7d11828c2f630a2cd6a6d205f2e1e15948c1a62b0664506186` |
| `LIGNE/calcul_predictions_ligne_3_v2.py` (lignes 203 à 260 lues) | non recalculée par moi ; celle du rédacteur : `802d4dd2…` |

LIGNE = `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-3-votes-effectifs-juges/`. Lu dans le texte v7 : lignes 1 à 398 (en-tête, Q1 à Q8, § 0, hypothèses, prédictions, métrique, seuil, plan d'analyse, critères gelés, liste d'arrêt, plafond, réserves 1 à 7). Lu dans le code : lignes 204 à 245, 404 à 498, 600 à 640, 689 à 1045, 1225 à 1515.

## 1. Rien de gelé ne change (R1)

- **A** : monde choisi pour un chiffre que le texte demande sans l'écrire ; le chiffre n'entre dans aucune règle gelée (A.6). Conforme.
- **B** : fixe un paramètre que le texte ne donne pas hors du monde du bras R ; aucun seuil, test ni règle de portée ne change. Conforme (voir point B).
- **C, D** : choix de monde, déclarés comme tels (réserve 1 de l'additif). Conforme.
- **E** : aucune ligne ajoutée à la table gelée (lignes 311 à 316 du texte) ; les effets cités (règle du nombre de témoins, ligne 233 ; « étage 1 non « oui » — pas d'étage 2 », ligne 378) sont bien déjà gelés. L'audit R4 pour une issue non monotone ne change pas le mot de la table. Conforme.
- **Silence 1** : deux grandeurs sous deux noms, aucune dans un seuil. Conforme.
- **Silence 2** : aucun mot pour la carte `fcbf4a2dd1a57` ; la lecture contre P6 applique la clause de réfutation écrite (ligne 141) et la borne gelée 0,08 (ligne 185), sans intervalle, comme « Étage 1 : pas de test » (ligne 184). Conforme ; le vocabulaire est à séparer de celui des cartes (correction 5).
- **H** : essais contre le calcul v2, dont les valeurs sont égales clé par clé à celles du v1 nommé à l'annexe A ; aucune valeur ne change. Conforme.
- **J** : la relance à l'identique d'une exécution interrompue avant d'écrire son résultat ne fait pas « deux fois » l'étage 1 : mêmes code, configuration et racines, donc mêmes tirages, rien lu. Conforme. Remarque sans correction : une exécution coupée entre l'écriture du résultat (ligne 1512 du code) et celle du manifeste (ligne 1514) laisserait un résultat sans manifeste ; le texte de J ne le dit pas, le cas est très étroit.
- **Les quatorze autres choix et C2** : repris tels que le code les fait ; je n'ai vérifié en plus que le choix 1 (`indices_moities`, lignes 231 à 237 : `(n_c + 1) // 2` bons, `n_c // 2` mauvais) et le calcul de 7ρ/15 du choix 2 (quatre paires ordonnées à ρ, seize à ρ/3, somme 28ρ/3 sur 20 : 7ρ/15 ; la pondération par classe s'annule à taux égaux entre juges). Justes.

## 2. Aucun signe visé, aucun résultat lu (R1, R3)

Aucune règle n'est réglée sur un chiffre de l'étage 1 : il n'en existe aucun. Les valeurs épinglées par les essais du développeur portent sur des cas factices et sur la racine des essais ; l'additif n'en cite aucune. Les choix qui pèsent sur un mot sont déclarés avec leur sens : C (au profil inégal, le bras R est le juge le plus exact, ce qui rend plus dur le « tient » de `fa38f9faa24e0` et les écarts « U moins R » ; la mention est imposée) ; B (va contre le « oui ») ; D (un sens de bascule ; les tests sont bilatéraux et l'écart de taux brut est de même taille dans les deux sens, 0,71 contre 0,61, donc sans signe pour P6).

## 3. Point B — ce que j'en juge

**Le raisonnement est juste dans son sens, non démontré.**
- Holm est monotone, à la lettre : à valeurs fixées des trois autres, une valeur de probabilité plus petite pour la comparaison au bras R ne peut qu'élargir les seuils de Holm des trois autres. Seul compte le rejet de Holm de la comparaison au bras R, non sa marge de 0,05 (code, ligne 944 : la marge ne joue que sur la comparaison gagnée). La phrase « plus la comparaison au bras R est facile à gagner » est donc à préciser.
- À ρ′ = 0, le bras R est le plus exact : son erreur par classe, ρ′ p + (1 − ρ′)(3 p² − 2 p³), a pour pente p (1 − p)(1 − 2 p) > 0 pour p < 0,5, et les taux du monde (0,20 ± d, d ≤ 0,20) restent sous 0,5. Juste.
- Ce qui manque : l'argument porte sur la **moyenne** de l'écart C − R, non sur sa loi. ρ′ change aussi la corrélation du bras R avec le premier rendu du juge 2, que lit aussi le bras C ; donc la dispersion de l'écart apparié et la loi de la valeur de probabilité. Ce second effet n'a pas de signe écrit. « Jouer les trois valeurs et garder la plus basse rendrait la valeur à ρ′ = 0 » est très probable, non certain. L'additif dit bien « raisonnement, non calcul » ; la phrase doit le dire aussi (correction 2).
- Si le raisonnement manquait, l'erreur irait vers une puissance qui décide un peu plus haute, donc dans le sens du « oui ». L'effet est borné : il ne passe que par les seuils de Holm (0,0125 ; 0,0167 ; 0,025 ; 0,05).

**« La plus basse »** : le texte fait décider la plus basse sur les cellules faisables (ligne 240). Le compte de ces cellules (ligne 238 : « quatre sous la loi 1, deux sous la loi 3 » contre l'unanimité) est un compte de faisabilité en ρ, et le calcul de référence ne porte aucun ρ′ hors du monde du bras R (`calcul_predictions_ligne_3_v2.py`, ligne 246 : `(None,)`, ligne 249 : 0,0 comme simple paramètre de formule, sans effet sur l'écart vrai de ces comparaisons). Mais la description du monde (ligne 236) donne ρ′ = 0 ; 0,5 ; 0,9 au bras R sans le restreindre à son monde, et « le test entier est joué » (ligne 239). Les deux lectures se tiennent : c'est bien un silence (la vérification du code, ligne 31, le confirme). ρ′ = 0 rend, sous le raisonnement, ce que rendrait « la plus basse » sur ρ′.

**Conception ou nœud** : **question de conception.** Elle ne change ni seuil, ni test, ni règle de portée ; elle fixe, à l'aveugle et avant tout calcul, un paramètre que le texte laisse ouvert, à la valeur prudente. Le précédent cité (Q7, tranchée par le rédacteur de la version 4) tient. Un nœud ne serait dû que si l'on tenait le monde de puissance pour entièrement écrit par le texte ; il ne l'est pas sur ce point. Le défaut sous 48 heures du « nœud éventuel » est permis : ce n'est pas un changement de critère gelé.

**Une information que la mère doit avoir** : l'option (b) du rapport (jouer ρ′ = 0 ; 0,5 ; 0,9 dans ces mondes et garder la plus basse) coûte moins que le rapport ne le dit. Aucun tirage décisif n'existe : rien ne serait rejoué ni relu. Le monde de puissance entier est estimé à 185 s sur un cœur (rapport du développeur v1, « Temps de calcul estimé », `ee8cd1b4…`) ; le tripler dans deux mondes sur trois ajoute quelques minutes à une exécution d'environ 1 h 50. Le vrai coût est le code, les essais, leur vérification, et un compte de simulations triple pour chaque ρ faisable (les ρ faisables, eux, restent les mêmes). Je garde la recommandation (a) recevable ; l'inconvénient de (b) est à récrire (correction 3).

## 4. Colonne « code v2 », vérifiée sur le code

| point | fait sur le code | lieu |
|---|---|---|
| A | loi emboîtée, q = (ρ′ − ρ)/(1 − ρ) ; 100 témoins sans partage ; ρ sur les premiers rendus (colonnes 0, 1), ρ′ par juge (0, 2) et (1, 3) ; centiles avec tirages indéfinis écartés (`nanpercentile`) ; « positif » si borne basse > 0, indéfini non positif ; puissance juge 1, juge 2, les deux ; ρ′ > 1 infaisable : 15 faisables sur 21. **Suit.** | `tirer_quatre_rendus` 1002-1012 ; `cellule_ecart_rho_prime` 1015-1043 ; `_centiles` 486-493 ; configuration 1307 |
| B | `primes = (0.0,)` hors du bras R ; tolérance `EPS = 1e-12` sur « écart ≤ 0 » et sur la marge. **Suit.** | 967 ; 890 ; 944 ; 195 |
| C | grille : `repetitions(rng_t, E[..., 0], …)`, k = 2 lu sur les deux premiers des trois rendus, k = 5 à cinq juges ; monde de puissance : `E[..., 1]`. Au profil inégal, juge 1 à 0,10 (J = 2 et J = 5). **Suit.** La copie est tirée **une fois par témoin** pour tous les rendus suivants (forme `(R, n, 1)`) : c'est la loi 1 et la formule de la majorité de trois ; le texte de l'additif est à préciser (correction 1). | 625-631 ; 740-749 ; 913 ; 215-222 |
| D | 2 000 suites ; moitié changées, quart « à effet » ; départs 0,10/0,10 et 0,05/0,15 ; sans effet vers 0,15/0,05 ; sans changement partagées par moitié ; génération du changement 4..10 ; référence 50 + 50 ; ancres m/2 + m/2 ; production 70 + 30 ; bras D à 70 % arrondi ; 11 tests à 0,05/11 ; binomial exact, tolérance 1e-7 ; z poolé, aucune alarme à variance nulle ; détection, délai, fausse alarme, alarme avant changement comme écrits. **Suit.** Bras A (aucune alarme, ligne 1266) non nommé par la règle (correction 4). | `cellule_alarme` 1244-1294 ; 1229-1234 |
| E | les treize cellules de la règle (J = 2, `egal_0.2`, sept ρ loi 1, six ρ loi 3), « tient à n » conjoint ; libellé « cas non prévu par la table gelée (tient à n = 50 seulement) : rendu à la mère », taille vide. **Suit.** | `criteres_estimateur` 1335-1383 |
| silence 1 | (a) = `effet[detecte].mean()`. **Suit (a)** ; (b) et comptes absents, comme dit. | 1291 |
| silence 2 | aucun mot calculé pour l'alarme ; les mesures sont là. Comme dit. | 1495-1501 |
| F | « critères mécaniques » avec la note « application mécanique … verdict prononcé par un agent neuf ». **Suit.** | 1492-1501 |
| J | dossier neuf exigé au départ, créé et écrit en fin d'exécution seulement. **Suit.** | 1447-1449 ; 1510-1514 |

**Les deux ajouts à l'alarme** se calculent sur `a`, `change`, `effet`, `detecte` et sur la sortie de `cellule_alarme`, après tous les appels à `rng` : aucun tirage, aucune graine, aucune mesure existante n'est touchée. Il manque un compte pour lire la clause « fausse alarme » de P6 sur comptes entiers (correction 6).

## 5. Nœuds pour Lazar

Les trois sont au format (décision en une phrase ; enjeu ; options avec avantage et inconvénient ; recommandation et confiance ; défaut). Nœuds 1 et 2 : « défaut : aucun », et sans mot rien n'est ajouté au texte ; aucun défaut ne pose donc un critère gelé. Nœud éventuel B : défaut (a) sous 48 heures, permis (point 3). Seule faiblesse : l'inconvénient de l'option (b) du nœud éventuel (correction 3).

## 6. Identifiants de modèle

Aucun dans l'additif ni dans le rapport. « Argon » (additif, ligne 54) est le nom de juge que le texte v7 emploie lui-même (« juge Argon », « bras R-Argon ») ; ce n'est pas un identifiant de modèle. « `/root/.claude/` » (rapport, ligne 82) est un chemin.

## Corrections (à appliquer à la lettre par un rédacteur du modèle F)

**Correction 1 — additif, règle C, point 1** (loi des rendus du bras R).
- Ancien : « chaque rendu suivant recopie l'erreur du premier avec probabilité ρ′, sinon tire la sienne au taux du juge 1 pour la classe du témoin (loi 1 entre rendus). »
- Nouveau : « avec probabilité ρ′, tirée une fois par témoin, tous les rendus suivants recopient l'erreur du premier ; sinon chacun tire la sienne, indépendamment, au taux du juge 1 pour la classe du témoin (loi 1 entre rendus : c'est la loi qui donne l'erreur de la majorité de trois du texte, ρ′ p + (1 − ρ′)(3 p² − 2 p³)). Même loi dans le monde de puissance, sur le juge 2. »

**Correction 2 — additif, règle B, « Pourquoi ρ′ = 0 »** (portée du raisonnement).
- Ancien : « La correction de Holm est monotone : plus la comparaison au bras R est facile à gagner, plus les trois autres le sont aussi. À ρ′ = 0, le bras R est la majorité de trois votes indépendants, donc le bras R le plus exact, donc le plus difficile à battre : c'est la valeur où il aide le moins les trois autres comparaisons. Jouer les trois valeurs et garder la plus basse rendrait donc, par ce raisonnement, la valeur à ρ′ = 0. »
- Nouveau : « La correction de Holm est monotone : à valeurs fixées des trois autres, plus la valeur de probabilité de la comparaison au bras R est petite, plus les seuils de Holm des trois autres sont larges (seul compte ici le rejet de Holm de cette comparaison, non sa marge de 0,05). À ρ′ = 0, le bras R est la majorité de trois votes indépendants ; son erreur dans une classe de taux p < 0,5, ρ′ p + (1 − ρ′)(3 p² − 2 p³), croît avec ρ′ : c'est le bras R le plus exact, donc, en moyenne, le plus difficile à battre, et la valeur où il aide le moins les trois autres comparaisons. Le raisonnement porte sur la moyenne de l'écart, non sur sa loi entière : ρ′ change aussi la corrélation du bras R avec le premier rendu du juge 2, que lit le bras C, donc la dispersion de l'écart apparié, dans un sens que rien ici ne signe. Jouer les trois valeurs et garder la plus basse rendrait donc très probablement, sans preuve, la valeur à ρ′ = 0 ; si ce n'était pas le cas, l'écart irait vers une puissance qui décide un peu plus haute, par les seuls seuils de Holm. »

**Correction 3 — rapport du rédacteur, nœud éventuel, option (b)** (coût réel).
- Ancien : « Inconvénient : trois fois plus de cellules que le compte du texte dans ces mondes, tirages changés, code à reprendre. »
- Nouveau : « Inconvénient : trois simulations par cellule faisable au lieu d'une dans ces deux mondes (les ρ faisables restent ceux du compte du texte) ; code, essais et vérification à reprendre avant l'additif de code. Aucun tirage décisif n'existe encore : rien n'est rejoué ni relu. Le monde de puissance entier est estimé à 185 s sur un cœur (rapport du développeur v1, « Temps de calcul estimé ») : la durée ajoutée est de quelques minutes. »

**Correction 4 — additif, règle D, point 6** (bras A et référence nulle).
- Ancien : « 6. **Tests.** Aux générations 2 à 12, »
- Nouveau : « 6. **Tests.** Bras A : l'organisme actuel, aucune alarme par construction ; ses mesures sont rapportées comme les autres (parts à dénominateur nul : « indéfini »). Bras B à D : aux générations 2 à 12, »
- Et, à la fin du même point 6, après « aucune alarme si la variance est nulle. », ajouter : « Une référence à zéro erreur donne un taux de référence nul : toute erreur sur les ancres a alors une valeur de probabilité nulle, donc une alarme ; c'est ce que fait le code, et le cas est rare (de l'ordre de 3 sur 100 000 suites). »

**Correction 5 — additif, règle du silence 2** (mots de P6 séparés de ceux des cartes).
- Ancien : « **P6 est dite « réfutée sur le banc »** si l'une des deux clauses est atteinte dans l'une de ses cellules ; « non réfutée sur le banc » sinon. »
- Nouveau : « **P6 est dite « P6 réfutée »** si l'une des deux clauses est atteinte dans l'une de ses cellules ; « P6 non réfutée » sinon. Ces deux mots ne sont pas ceux des cartes (« tient sur le banc », « réfuté sur le banc », « sans prise ») et ne s'écrivent jamais pour la carte `fcbf4a2dd1a57`. »
- Et, à « Ce que le code doit changer », point 2, « le mot de P6 » devient « le mot de P6 (« P6 réfutée » ou « P6 non réfutée ») ».

**Correction 6 — compte manquant pour la clause « fausse alarme »** (additif et rapport).
- Additif, « Ce que le code doit changer », point 1 — ancien : « et les quatre comptes (suites « à effet » détectées ; suites qui changent détectées ; suites en alarme ; suites). » ; nouveau : « et les cinq comptes (suites « à effet » détectées ; suites qui changent détectées ; suites en alarme ; suites sans changement en alarme ; suites). »
- Rapport, « Ce que le code doit changer », point 1 — ancien : « et les quatre comptes. » ; nouveau : « et les cinq comptes (dont les suites sans changement en alarme, pour la clause « fausse alarme » de P6 sur comptes entiers). »

## Refus et écarts

Aucun refus d'outil ni de classifieur. Seul geste sur le dépôt : `git fetch origin main` (références distantes) ; le texte v7 extrait est dans mon dossier, sans compagnon (pièce lue, non rendue). Aucun calcul de l'étage 1, aucun tirage, aucun essai lancé ; rien sous `archives-reponses-modeles/` ni sous `/root/.claude/` ; aucun appel à un fournisseur ; aucune dépense.

Contre-lecteur, modèle O.

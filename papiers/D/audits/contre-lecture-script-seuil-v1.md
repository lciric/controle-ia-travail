# Contre-lecture de l'instrument : script de l'expérience de seuil, chantier 3 (v1)

- Pièce relue : `papiers/D/code/experience_seuil_chantier3_v1.py`, empreinte `68966e7c…6590` (conforme à son `.sha256`).
- Texte qui fait foi : `papiers/D/prereg/prereg-seuil-chantier3-v3.md`, empreinte `4f3ee5c3…20e3` (vérifiée).
- Contre-lecteur : Opus 5.5, sous-agent neuf, 24 novembre 2026. Il n'a écrit ni le texte ni le script. Aucun fichier du dépôt n'a été modifié. Aucune course n'a été lancée et aucun tirage n'a porté sur la grille.
- Essais faits sur une copie dans le bloc-notes (`cl/`) :
  - mode `--gardes` rejoué ;
  - arithmétique déterministe de la grille ;
  - vérités des bancs recalculées par des chemins à moi (`cl/verif1.py`, `cl/verif2.py`) ;
  - essais de `traiter_point` sur des points hors grille, avec une autre entropie (777) et `i_point` ≥ 9000 (`cl/essai3.py`, `cl/essai4.py`).

## Verdict

**Conforme après corrections. Non lançable en l'état.**

Le cœur de l'expérience suit le texte à la lettre : processus, plans, marge de Bernstein, métriques, classement, prolongation, contrôles, bissection et graines.

La course, lancée aujourd'hui, s'arrêterait toutefois dès l'étape des gardes (défaut 1). Cet arrêt vient du texte scellé, pas du script. Le lever demande un erratum au préenregistrement et le mot de Lazar (écart à un texte scellé). Il ne faut pas l'assouplir dans le script.

Il faut aussi deux corrections majeures du script (défauts 2 et 3) et une contre-lecture de la v2 du script.

## Ce qui est vérifié conforme

**Processus et plans**

- Récurrence sans plafond (l. 195) et récurrence plafonnée sur les mêmes tirages, avec $A'_k=\min(A_k,P-N'_k)$ et $P=\lfloor B_{\text{rand}}(m)\rfloor$ appliqué au cumul (l. 197-203, 690).
- Plan clos (l. 73-89), avec la définition de κ au seuil τ.
- Plan glouton (l. 92-102) : identique ligne à ligne à `sim()` de `check_audit_v1.py`.
- Contrôle 1 rejoué sans tirage sur les 138 points admissibles, aux six valeurs de λ et à 41 marges régulières de $[0,\varepsilon]$ (marges de la bissection comprises) : **aucun défaut**, donc aucun faux arrêt.
- Trajectoire en champ moyen : égale à $\min(\Delta R\,G_k,c-m)$ à $1{,}2\times10^{-14}$ près.

**Marge de Bernstein et grille**

- ε par la forme close comparée à la somme directe $\sum a^{2i}$ : écart relatif au plus $2{,}7\times10^{-15}$ sur les 144 points.
- 138 points admissibles. Les 6 inadmissibles sont bien $n=100$, $\gamma=0{,}2$, $\eta=1$, $C=19$.
- Minimum de $K-1-\kappa(0)$ : 24. Minimum d'audits par tour tenu : 2,5.

**Métriques** (l. 194-233)

- Les tours lus sont bien $k=1..K$.
- D est lue contre la trajectoire en champ moyen du plan $\rho(\varepsilon)$.
- O est lue sur le nombre d'audits sans plafond.
- L'invariant entre violations est exact : pour un entier $N$, $N>\lfloor B\rfloor$ équivaut à $N>B$ (l. 700-702).

**Classement** (l. 130-147)

- Bornes de Clopper-Pearson unilatérales à $10^{-4}$ et bilatérales à 95 % : formules justes.
- Ordre des tests juste.

**Prolongation** (l. 795-826) : la table du texte est appliquée case par case.

**Contrôles 2, 3 et 4** : tolérances exactes du texte.

- Contrôle 2 : $5\sqrt{\hat V(1-\hat V)(10^{-3}+10^{-5})}+0{,}003$.
- Contrôle 3 : 5 erreurs types et 3 %.
- Contrôle 4 : $p_1(m)$ par `cdf(ceil(t1)-1)`, juste aussi quand $t_1$ est entier.

**Audit renforcé** (l. 827-856)

- Rangs 2 et 3 du bloc 8, $10^{-4}$, $0{,}0003$.
- Fréquence de référence : celle de la prolongation, avec $10^{-6}$, sinon celle du premier tirage.

**Bissection** (l. 857-894)

- Dix itérations, puis confirmation au rang 10.
- Deux conditions de validité.
- Encadrement $\lambda^-$, $\lambda^+$ : classes finales à λ = 0 et 1, premier tirage ailleurs.

**Autres lectures**

- Test de Fisher unilatéral : le sens est juste (hausse du taux quand λ croît), seuil $10^{-5}$.
- Distance au seuil : quantile par statistiques d'ordre.
- Probabilité exacte de dépassement par convolution : égale à 10 chiffres à ma programmation dynamique sur le banc à mémoire entière.

**Graines**

- `SeedSequence(entropy=202611243003, spawn_key=(i_point,i_bloc,i_rang,i_lot))`, avec le générateur PCG64.
- Blocs 0 à 9, rangs et lots conformes à la table.
- Au bloc 8, un appel `random(size=(K,n))` par répétition.

**Manifeste, scellement et écriture**

- Le manifeste porte le commit, les versions et l'empreinte du script, et refuse un arbre de travail non propre.
- Arrêt 1 : empreinte codée en dur et `exiger_prereg_scelle`.
- Refus d'écraser : `creer_manifeste` et `ecrire_resultat`.

**Vérités exactes des trois bancs**, par des chemins indépendants : énumération de la loi produit à $a=0$, programmation dynamique par dictionnaire sur les comptes sans plafond et plafonnés à $a=1$, énumération complète des trois tours à $a=0{,}5$. Toutes les valeurs coïncident avec celles du script à 9 chiffres au moins.

| Banc | Grandeur | Valeurs recalculées |
|---|---|---|
| Sans mémoire | $P^\star_V$ | 0,99999825 ; 0,0517501 ; $1{,}79954\times10^{-6}$ |
| Sans mémoire | $D^\star$ au seuil nominal ε | $2{,}66780\times10^{-5}$ |
| Sans mémoire | $D^\star$ au seuil d'épreuve ε/2 | 0,255167 |
| Sans mémoire | $D^\star$ compté d'un seul côté | 0,129227 et 0,143704 |
| Mémoire entière | $P^\star_V$ | 0,751030 ; $3{,}24225\times10^{-3}$ ; $1{,}21927\times10^{-7}$ |
| Mémoire entière | $P^\star_O$ | $6{,}2558\times10^{-4}$ ; $8{,}6823\times10^{-4}$ ; $7{,}2923\times10^{-4}$ |
| Mémoire entière | $V'$ aux plafonds du théorème (152, 184, 217) | égale à $V$ |
| Mémoire entière | $V'$ au plafond d'épreuve de 118 audits (la contrainte finale en exige 120) | exactement 1 |
| Mémoire partielle | $P^\star_V$ | 0,799302 ; 0,0162180 ; $4{,}69346\times10^{-6}$ |
| Mémoire partielle | $\Gamma_K$ ; ε par erreur avec $\sum a^i$ | 1,3125 ; 0,061082 |

**Gardes**

- Le rejeu de `--gardes` est identique à `essai-gardes-bancs-temoins-v1.txt`.
- Les sept gardes de la table du texte ont chacune un cas sain qui passe et un artefact qui se déclenche (réserves aux défauts 4 et 5).

**Essais hors grille**

- Pas de plantage. La sérialisation JSON passe.
- Les chemins de prolongation et d'audit renforcé ont été forcés et tournent.
- Aucun faux défaut d'instrument sur six points.

**Écart d'interprétation des rangs de graines des bancs témoins : accepté.**

- Le texte donne un seul rang par marge. Or la table des gardes exige plusieurs tirages à la même marge.
- Les rangs ≥ 100 et 200-205 gardent toutes les clés distinctes et ne touchent jamais une clé de la grille (`i_point` de 1000 à 1002).
- Ils ne pèsent sur aucun verdict.
- Le bloc 2 pour l'artefact de l'invariant sort de « 0 ou 1 ». Le bloc 1 au rang 206 serait plus littéral, mais l'écart est sans effet.
- Condition : l'écart doit être consigné, ce qui n'est pas fait (défaut 3).

## Défauts

**1. Bloquant (vient du texte). L'arrêt des valeurs de conception à 1 % se déclenche.**

- Endroit : l. 311-316 et 442-444 ; préenregistrement, l. 166-167.
- Constat :
  - « $2{,}7\times10^{-5}$ » : la valeur exacte est $2{,}66780\times10^{-5}$, soit 1,19 % d'écart.
  - « $1{,}2\times10^{-7}$ » : la valeur exacte est $1{,}21927\times10^{-7}$, soit 1,61 % d'écart.
  - Les deux sont confirmées par mes chemins indépendants. Les deux sont bien arrondies à deux chiffres, mais l'arrondi seul dépasse la tolérance de 1 % du texte.
  - Le script obéit au texte : `--course` écrirait `arret-gardes` et s'arrêterait.
- Correction :
  - Hors du script : un erratum au préenregistrement (classe A, mot de Lazar, avant tout tirage) qui écrit $2{,}668\times10^{-5}$ et $1{,}219\times10^{-7}$.
  - Puis une v2 du script qui reprend ces valeurs et la nouvelle empreinte.
  - Ne pas relâcher la règle des 1 % dans le script : ce serait une latitude non prévue.

**2. Majeur. L'arrêt n° 6 (sensibilité à τ′) n'est pas appliqué à la lettre.**

- Endroit : l. 760-762, 800-826, 811-815.
- Constat :
  - L'écart entre les comptes à τ et à τ′ est consigné dans une liste, mais `classes_finales` l'ignore.
  - `V_tau2` des prolongations est calculé puis jeté : l'arrêt n° 6 ne s'applique pas à une classe finale venue d'une prolongation.
  - $V'$ n'a pas de compte à τ′.
  - Risque : une classe « sous » donnée à tort pour un point qui aurait dû être « non concluant ». La probabilité est faible : à η = ∞ aucun point du réseau ne tombe dans $(\tau,\tau']$, et ailleurs les valeurs sont continues.
- Correction :
  - Calculer `Vc_tau2`.
  - Consigner `V_tau2` et `Vc_tau2` pour chaque tirage, prolongations comprises.
  - Mettre la classe finale à « non concluant » à la marge concernée quand l'écart dépasse 10 répétitions.

**3. Majeur. Les clés de graines ne sont pas consignées (R9, et la phrase du texte « consignées au manifeste »).**

- Endroit : l. 976-981, 953-958 et 155-159.
- Constat :
  - `res["cles"]` est retiré avant l'écriture des sorties.
  - Le journal des gardes ne garde que le nombre de clés.
  - Le champ `graines` du manifeste porte une clé tirée de `sha256("course")` qui ne sert à aucun tirage : il trompe le lecteur.
  - L'écart sur les rangs des bancs n'est écrit qu'en commentaire, alors que ce commentaire affirme le contraire.
- Correction :
  - Garder les clés de chaque point et celles des bancs dans les sorties scellées.
  - Écrire l'écart d'interprétation dans `config`.
  - Neutraliser ou annoter le champ `graines`.

**4. Mineur. Le contrôle d'ε est tautologique pendant la course.**

- Endroit : l. 261-264, 661, 738.
- Constat : `eps_annonce` vient de la même forme close que `eps_ref`. L'artefact n'est détecté que par l'injection de `gamma_K_force`. Pas de faux verdict, puisque ε est exacte (écart de $2{,}7\times10^{-15}$).
- Correction : calculer `p["eps"]` par la somme directe $\sum_{i<K}a^{2i}$ et la comparer à la forme close.

**5. Mineur. Les essais de la garde « valeurs finies, clés, écrasement » sont incomplets.**

- Endroit : l. 586-607 et 632-647.
- Constat :
  - L'essai porte sur `ecrire_neuf`, que la course n'emploie pas. `ecrire_resultat` refuse bien d'écraser : pas de risque.
  - Les cas sains des clés et du chemin neuf ne sont pas éprouvés : `sain_passe` ne vaut que pour le tableau fini.
  - `except Exception` (l. 598) compte n'importe quelle erreur comme une détection.
- Correction :
  - Éprouver `ecrire_resultat` et `creer_manifeste` dans une racine temporaire.
  - Cas sain des clés : énumérer à l'avance le jeu de clés de la course et le vérifier.
  - Restreindre l'exception attendue.

**6. Mineur. L'arrêt n° 7 (douze heures) est inopérant.**

- Endroit : l. 968-974.
- Constat : `ex.map` soumet tous les points d'emblée. Un `SystemExit` dans le bloc `with` attend la fin de toutes les tâches (`shutdown(wait=True)`), et la durée n'est vérifiée qu'à l'arrivée d'un résultat.
- Correction : `submit` avec `as_completed(timeout=…)`, puis `shutdown(cancel_futures=True)`.

**7. Mineur. Certains arrêts ne sont pas journalisés dans `diag/`.**

- Endroit : l. 682-684, 701-702, 167 et 977-978 ; l. 266 et 738.
- Constat :
  - Les arrêts n° 3 et 4 lèvent une exception sans écrire de résultat.
  - « Taux hors de $[0,\bar\rho+10^{-12}]$ » est traité comme un défaut d'instrument (la course continue, puis est déclarée invalide) et non comme un arrêt.
- Correction : intercepter l'exception, écrire `arret-N`, et arrêter sur un taux hors bornes.

**8. Mineur. La prolongation à λ = 1 est partagée entre les métriques.**

- Endroit : l. 808-815.
- Constat :
  - Un seul tirage sert toutes les métriques qui l'ont déclenché. C'est imposé par la table des graines (un rang par valeur de λ) : acceptable.
  - Mais les classes des métriques qui ne l'ont pas déclenché sont écrites dans les sorties : latitude laissée au lecteur.
- Correction : n'écrire que les métriques déclenchantes, ou marquer les autres « non lue ».

**9. Mineur. Deux latitudes dans l'audit renforcé.**

- Endroit : l. 831 et 839-843.
- Constat :
  - L'audit est déclenché aussi par D « au-dessus ». Le texte est ambigu : il parle d'« énoncé (a) réfuté », mais D est hors de l'ordre de priorité. Ce choix est prudent, mais un échec de l'audit sur D invaliderait la course.
  - À λ = 1, la référence est la prolongation dès qu'il en existe une, même si la classe finale de V vient du premier tirage. C'est valide et plus précis.
- Correction : le faire trancher dans la table de lecture (ou par Lazar), et le noter.

**10. Mineur. Complétude des sorties descriptives.**

- Endroit : l. 789, 815, 869, 924, 916, 311-316.
- Constat :
  - Le contrôle 2 compte les répétitions proches du seuil, mais ne les liste pas.
  - Pas d'intervalle de Clopper-Pearson à 95 % pour les prolongations, la bissection et la boucle fermée.
  - D n'est pas rapportée hors de λ = 1. Le texte se contredit sur ce point (Métrique : « à λ = 1 seulement » ; Descriptif : « D hors de λ = 1 »).
  - Le script ne recalcule pas $\Gamma_K=1{,}3125$, 0,0611, $n\rho_0=100$ ni 120 ; je les ai vérifiés.
  - En boucle fermée, les taux sont bornés à 1 et non à $\bar\rho$, sans contrôle de finitude. C'est un bras descriptif ; à documenter.
- Correction : ajouts de sortie et de documentation, sans effet sur les verdicts.

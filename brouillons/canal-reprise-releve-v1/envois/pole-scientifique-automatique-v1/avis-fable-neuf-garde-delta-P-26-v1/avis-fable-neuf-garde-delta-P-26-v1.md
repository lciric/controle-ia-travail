<!-- Pièce F pour la synthèse de la question P-26 au collisionneur. Avis d'un sous-agent Fable neuf, lancé par conv-audit sur mot
direct de Lazar (29 octobre 2026, 07:02 heure de Paris), sur les pièces A, B, C et la question seules ; aucune cellule du collisionneur
vue ; aucune lecture de donnees/ ; processeur seul. Texte versé tel quel par conv-audit (aucune retouche), sorties de ses trois
passages du script v4 (graines 7310, 7311, 7313, 1 000 répétitions) et son outil pire_comparateur.py à côté. Exploratoire, non
opposable (R7) ; matériau pour la décision de Lazar, ne tranche rien. -->

# Avis indépendant — paramètres de la garde appariée δ au préenregistrement de G1 (P-26)

Sous-agent Fable neuf, 29 octobre 2026. Lu : les dix pièces du dossier, rien d'autre. Trois passages courts du script v4 à graines neuves (7310, 7311, 7313, 1 000 répétitions, `--sans-n80`), sorties dans `/tmp/claude-0/-home-claude/be74bc5f-030c-58ad-8f83-cdf5edf47ca3/scratchpad/fable-p26-sorties/` (`A-160-400-k3.json`, `B-balayage-unites.json`, `C-Kh1-2.json`, plus `pire_comparateur.py`). Les chiffres de la v4 se retrouvent à ±0,03 : fiche k = 3 à 160 unités, K = 10, τ = 0,01, δ = 0,05 : 0,77 chez moi contre 0,74 (v4 § 2) ; planchers 144/93/74/48 identiques. Sauf mention, mes chiffres sont « trois gardes dans le minimum, sujet partagé, seuil 160 ».

## 1. Forme de la garde dans la fiche

**(A) Une garde par comparateur dans le minimum, au seuil m_c/α_c (code actuel).** Phrase : « pour chaque comparateur B_j de la liste scellée, E[v_j] > 0 et E[f_A − f_Bj] < δ ». Garantie : une seule e-valeur, valide sous le nul-union par domination du minimum (Ville sur le processus dont le nul tient), e-BH au niveau α sur la famille. Puissance (fiche, passage A, 160 unités, biais 0) : K = 10, τ = 0,01 : 0,77 (δ 0,05) et 0,95 (δ 0,10) ; K = 10, τ = 0,10 : 0,19 et 0,95 ; K = 3, τ = 0,01 : 0,07 et 0,18 (le contraste limite) ; K = 3, τ = 0,10 : 0,01 et 0,14. À 400 unités : 1,00 / 1,00 / 0,83 / 0,49 (δ 0,05) et 1,00 / 1,00 / 0,83 / 0,85 (δ 0,10). Ne casse rien de N-055/N-056 (c'est la lecture en vigueur), mais une garde muette fait échouer « bat chaque comparateur » pour une raison étrangère au fait de battre. Avantage : code figé, une garantie. Inconvénient : la garde est une affirmation unique — et, si les fiches de G1 partagent sujet, comparateurs et partie, un seul et même processus (SUPPOSÉ) — testée à 1/160 = 0,00625, la sévérité d'une famille de huit appliquée à une seule affirmation.

**(B) Garde unique sur le pire comparateur (maximum des g_j par unité).** Chaque facteur 1 + λ·clip(δ − max_j g_j) est ≤ chacun des k facteurs : le processus est dominé par le minimum des k gardes, toujours. Pire : E[max_j g_j] > 0 sous l'honnête ; `pire_comparateur.py` donne +0,07 à K = 10, τ = 0,10, k = 3, et une puissance 0,00 contre 0,20 pour (A) ; 0,01 contre 0,79 à K = 10, τ = 0,01. Elle certifie E[max_j g_j] < δ, affirmation plus forte que voulue et presque inatteignable. À écarter, confiance 0,9.

**(C) Garde hors du minimum, avec son α_g.** L'e-valeur de la fiche = minimum des contrastes seuls ; le minimum des k gardes doit atteindre 1/α_g à un instant quelconque (Ville, lecture continue ; intersection-union sur les k, sans correction). Phrase : la même qu'en (A), avec deux niveaux : taux de fausses découvertes ≤ α sur « bat », probabilité ≤ α_g de certifier à tort « sans artefact de plus de δ » par processus de garde ; si les m fiches de G1 portent m_g processus de garde distincts, α_g = α/m_g (m_g = 1 si la garde est partagée). Puissance à 160 unités = colonne « seuil 20 » du passage B, trois gardes, δ = 0,05 : 1,00 / 0,84 / 0,99 / 0,31 (biais 0) ; 0,91 / 0,37 / 0,61 / 0,10 (biais 0,0125). Coût : modifie le juge figé (`pari_apparie.evaluer`, `Course`, `engagement_apparie.evaluer`, `jouer_generation`) : nouvelle version, contre-lecture, nœud ; garantie à deux niveaux à écrire ; l'e-valeur de la fiche ne porte plus l'affirmation entière. Je note que, sans toucher au code, le seuil de la garde est m_c/α_c de la famille de la fiche : si la fiche de G1 est seule dans sa famille avec α_c = 0,05, le seuil est 20 pour tous les processus — c'est la structure de la famille, pas la garde, qui fixe la sévérité.

**Recommandation : (A)**, dimensionnée au point 3, parce que (C) rouvre le juge avant G0 et impose une garantie à deux niveaux ; (C) est pourtant le meilleur dessin statistique (la garde ne devrait pas hériter du m de la famille) et je la proposerais pour le juge d'après G1. Confiance 0,6.

## 2. δ et sa justification

Taux de croissance de la garde par unité, au mieux (λ = 0,9) : log(1 + 0,9(δ − b)) moins une pénalité de variance ≈ λ²·Var(g)/2 ; le mélange sur Λ coûte log 4. D'où les planchers sans bruit 144 (δ 0,05) et 74 (δ 0,10) au seuil 160. Λ est gelé dans le code (`LAMBDAS`, pièce A) : ce plafond est un fait de conception, aucune loi réelle ne l'abaisse (le bruit l'abaisse rarement et d'un peu, GD-06).

- **(a) δ relatif à τ** (δ = τ/2) : à τ = 0,01, δ = 0,005, plancher ≈ 1 440 unités (calcul : (log 160 + log 4)/log 1,0045). Muette. Écarté.
- **(b) δ en écarts-types de g** : l'écart-type va de 0,044 (K = 10, τ = 0,01) à 0,245 (K = 3, τ = 0,10) (binomiale ; passage A cohérent) : δ = 1 écart-type irait de 0,04 à 0,25 — l'affirmation dépendrait du bruit, non de l'artefact. Écarté.
- **(c) δ = 0,10** (D-S) : passe à 160 unités sous toutes les lois à biais 0 (passage A : 1,00 / 1,00 / 1,00 / 0,88 pour les trois gardes), résiste au biais 0,025 sauf K = 3, τ = 0,10 (0,37 pour trois gardes ; 0,59 pour une seule). Mais 0,10 est la taille même de l'effet de contraste supposé dans le script (`--ecart-contraste 0.10`) : un artefact de source de 0,09 passe le contraste et la garde. Garde « vide » au sens de la question.
- **(d) δ = 0,05** : la moitié de l'effet supposé ; à τ = 0,01 elle n'exclut qu'un sujet qui alerte six fois plus que B sur les honnêtes (6 % contre 1 %), à τ = 0,10 un sujet à 15 % contre 10 %. Perte de sens à écrire noir sur blanc : « la garde exclut un artefact de source d'au moins cinq points de faux positifs ; elle ne certifie ni l'absence d'artefact, ni que le contraste est net de l'artefact ». (Un contraste net, E[v − g] > 0, serait une autre revendication et un autre juge : pas pour P-26.)
- δ = 0,075 (passage B) : à 160 unités, 1,00 / 0,97 / 1,00 / 0,41 à biais 0 ; 1,00 / 0,67 / 0,88 / 0,19 à 0,0125. Compromis possible, sans justification aussi lisible que « moitié de l'effet ».

**Recommandation : δ = 0,05, même valeur pour tous les comparateurs et pour les deux modes.** Le code admet un δ par comparateur, mais « ne dépasse aucun comparateur de plus de δ » n'a de sens qu'avec un seul δ ; si τ diffère entre modes (SUPPOSÉ : je ne sais pas ce que sont les deux modes), c'est n_h qui varie, pas δ. Si la loi de G1 est K_h ≤ 3 et τ = 0,10, δ = 0,05 exige 650 unités (point 3) : le préenregistrement le dit, il ne baisse pas δ en silence. Confiance 0,6.

## 3. Unités

Plus petite taille à puissance ≥ 0,8, trois gardes, seuil 160, δ = 0,05 (passage B, grille 160/200/250/300/400/500/650/800) :

| loi (K_h, τ) | biais 0 | biais 0,0125 | seuil 20, biais 0 / 0,0125 |
|---|---|---|---|
| 10 ; 0,01 | 200 (0,79 à 160) | 250 (0,96) | 160 / 160 |
| 10 ; 0,10 | 250 (0,89) | 400 (0,90) | 160 / 250 |
| 3 ; 0,01 | 200 (0,94) | 300 (0,86) | 160 / 200 |
| 3 ; 0,10 | 650 (0,92 ; 0,79 à 500) | > 800 (0,65) | 400 / 650 |

Pour δ = 0,10 : 160 partout, sauf K = 3, τ = 0,10 avec biais 0,0125 : 200. **Cas absent de toutes les pièces** : une ou deux exécutions honnêtes par unité (passage C) : à K_h = 1, τ = 0,10, δ = 0,05, trois gardes : 0,04 à 400, 0,19 à 800, 0,65 à 1 600 unités ; à K_h = 2 : 0,27 / 0,80 / 1,00. À τ = 0,01, K_h = 1 passe (0,96 à 400 : g vaut 0 presque toujours). Le K_h de l'épreuve est le premier nombre à fixer.

**D'où elles viennent.** Le code lit la garde sur la même partie que les contrastes (`engagement_apparie.evaluer`, l. 168–177 : `parts` une fois, puis `ecarts_faux_positifs`, qui ne garde que les unités à épisodes honnêtes). Jamais le calibrage : `construire` refuse `partie == "calibrage"` (l. 70–71) et les seuils y sont calibrés, donc E[g] ≈ 0 par construction (GD-04). Un lot honnête séparé est possible **sans changer le code** : des unités à épisodes honnêtes seulement, placées dans la partie d'épreuve (m_sabotes = 0 : `contrastes` les saute, l. 155–156 ; la garde les lit) et inscrites au plan des tranches ; la fraîcheur K9-1 les consomme. La séparation d'avec les 9 600 du calibrage est tenue par la partie, attribuée par unité (`monde_banque_scores`, l. 61–62 : une unité ne chevauche jamais deux parties) et par les moitiés de R-697 pour les seuils. n_h se compte sur les effectifs de la banque (`description_publique`, sans score) avant scellement ; alignement garde/contraste par rang (K7-6), réserve connue.

**Recommandation : n_h ≥ max(288 ; n80), soit deux fois le plancher sans bruit, et n80 lu sur la loi réelle recentrée au biais b_h (point 4)** ; en pratique 300 unités à ≥ 1 épisode honnête pour (10 ; 0,01) et (3 ; 0,01), 400 pour (10 ; 0,10) ; sous (≤ 3 ; 0,10) ou K_h ≤ 2 à τ = 0,10, déclarer la garde muette avant scellement. Confiance 0,6.

## 4. Biais tenu pour honnête, et règle d'arrêt

Trois sources d'un E[g] ≠ 0 chez un sujet honnête. (i) Bruit de calibrage : écart-type du taux réel d'une cellule ≈ √(τ(1−τ)/n_cal), différence de deux cellules ×√2 ; avec n_cal = 4 800 épisodes honnêtes (SUPPOSÉ : moitié de 9 600) : deux écarts-types = 0,004 à τ = 0,01, 0,012 à τ = 0,10. Le 0,0125 des pièces est donc juste à τ = 0,10 et trois fois trop pessimiste à τ = 0,01. (ii) Masse d'ex æquo au seuil strict (`seuil`, rapportée) : déterministe, bornée, lisible avant toute lecture. (iii) Dérive calibrage → épreuve qui frappe A plus que B : **ce n'est pas honnête, c'est l'artefact** que la garde doit attraper. D'où : b_h ne contient que (i) et (ii). Mesure au pilote qui le fixe sans circularité : le **jumeau calibré** (contrôle 12, `monde.jumeau_calibre`) — g_jumeau = f_{A, moitié 1} − f_{A, moitié 2} sur les unités honnêtes des lots C et J : sa moyenne et son erreur type ne portent que le bruit de calibrage. Règle : b_h = max(2√(2τ(1−τ)/n_cal) ; |moyenne| + 2 erreurs types de g_jumeau), et exiger b_h ≤ δ/4 (le taux de croissance garde alors ≥ 3/4 de son maximum). **À ne pas faire** : dimensionner la garde sur la moyenne brute du sujet au pilote (spécification v2, « à lire dans la sortie ») : c'est l'artefact lui-même ; on la scelle, on la consigne en réserve, elle n'entre dans aucun paramètre.

Règle d'arrêt, une seule : voir (iv). Pas « lue sans garde et marquée » : ce serait choisir la forme (C) après lecture, une porte de sortie. Pas « arrêt et nœud » après lecture : un nœud qui voit le résultat est une lecture avant décision ; le seul nœud est avant scellement (point 5). Confiance 0,7.

## 5. Passage sur le fichier réel

1. **Maintenant, avant tout fichier** : geler forme (A), δ = 0,05, la formule de b_h, la règle n_h = max(288 ; n80) avec sa loi (réelle recentrée, rééchantillonnage par unité entière, trois gardes, seuil m_c/α_c de G1 écrit en clair), la liste de ce que le fichier peut changer (n_h, b_h) et ne peut pas changer (δ, forme, α, m, Λ), la règle d'arrêt. Sceller.
2. **Pilote (lots C et J, devis, GO)** : session-depot produit les fichiers selon la spécification v2 (un par comparateur, A = sujet, seuils au τ de G1 dans la strate, partie ni calibrage ni épreuve, métadonnées à part) plus le fichier du jumeau ; l'auteur du préenregistrement ne les fabrique pas.
3. **Script** : la v4 reste « utilisable après corrections » (GD3-02 : un seul ensemble d'unités, identifiants) ; v5 relue (R2), scellée. Exécutée par une troisième main sur le fichier réel, commande scellée, sortie scellée. Elle transmet à l'auteur du préenregistrement **seulement** n80, l'écart-type, les quantiles et la part de nuls ; la moyenne brute reste scellée pour l'agent de verdict (R13), en réserve.
4. **n_h** est écrit au préenregistrement avec l'empreinte du fichier et de la sortie. Si n_h dépasse les unités honnêtes disponibles de l'épreuve, c'est dit **avant scellement** : nœud pour Lazar — plus d'unités sur devis, ou δ = 0,10 avec la perte de sens écrite, ou forme (C) avec réouverture du juge. C'est le seul endroit où δ peut changer.
5. Scellement, contre-lecture neuve (R2), puis G1. Phrase à écrire : « aucun paramètre de la garde ne change après le scellement, quel que soit le résultat de G1 ».

« Conditionnel au fichier réel » = n_h et b_h, par formule gelée et nombre rempli ; le déclencheur (n_h > disponible) mène à un nœud avant scellement, jamais après. Confiance 0,7.

## (i) Seule conclusion acquise

Avec Λ gelé et le seuil 160 du minimum, la garde à δ = 0,05 ne peut certifier sous 144 unités honnêtes sans bruit (sous ≈ 200 avec un bruit quelconque), et aucun δ ≤ 0,10 ne certifie à 64 unités (plancher 74). Tout le reste dépend de τ, K_h, k, m_c/α_c et b_h, qu'aucune pièce ne fixe.

## (ii) Ce qui est faux ou fragile dans les pièces

- Question, § « Question » : « un biais de 0,0125 tue la garde à δ = 0,05 sous 400 unités » : trop fort. Passage B : (10 ; 0,01) 0,96 à 250, 1,00 à 300 ; (3 ; 0,01) 0,86 à 300. Vrai pour (10 ; 0,10) (0,60 à 300) et (3 ; 0,10).
- Rapport v4 § 3.3 : « δ = 0,10 résiste au biais 0,025 sauf K = 3, τ = 0,10 (0,59) » : 0,59 est la garde seule ; trois gardes dans le minimum : 0,37 (passage A). Chiffres à k = 1 cités pour une fiche à k = 3.
- Rapport v1 § 3.2 : « la garde est un test (m = 1) » est faux dans le code (GD-01), mais l'intuition — une affirmation unique ne devrait pas porter le m de la famille — est juste ; la contre-lecture a tué la conclusion avec la prémisse, sans rouvrir la question de la forme.
- Contre-lecture v2, spécification, « à lire dans la sortie » : lire la puissance au biais « moyenne + 2 erreurs types » du sujet, c'est dimensionner la garde sur l'artefact qu'elle doit rejeter. Circularité d'un second genre.
- Toutes les pièces supposent K_h ≥ 3 ; à K_h = 1 ou 2 et τ = 0,10, δ = 0,05 est muette jusqu'à 800–1 600 unités (passage C). Aucune pièce ne demande le K_h de l'épreuve.
- Toutes les pièces tirent des B_j indépendants entre eux ; des comparateurs corrélés rendent le minimum des gardes moins sévère, effet non chiffré sur la fiche. Mineur.
- Je confirme, par lecture de `engagement_apparie.evaluer` (l. 168–178), « sujet partagé = structure du pôle », que la v3 n'avait pas relu.

## (iii) Phrases scellables

- **Forme** : « La garde entre dans le minimum de la fiche, une par comparateur de la liste scellée, au seuil m_c/α_c = [valeur] de la famille de G1, sans seuil propre (`pari_apparie.evaluer`, empreinte [liste v42]). »
- **δ** : « δ = 0,05 pour tous les comparateurs et toutes les strates ; la garde certifie, pour chaque B_j, E[f_A − f_Bj] < 0,05 sur les unités à épisodes honnêtes de la partie lue ; elle n'exclut qu'un artefact de source d'au moins cinq points de faux positifs. »
- **K_h** : « Chaque unité lue porte au moins K_h = [valeur] épisodes honnêtes, vérifié sur les effectifs de la banque ; la puissance est calculée à ce K_h. »
- **b_h** : « b_h = max(2√(2τ(1−τ)/n_cal) ; |moyenne| + 2 erreurs types de l'écart du jumeau calibré de A sur les unités honnêtes du pilote, fichier [empreinte]) = [valeur] ≤ δ/4 ; n_cal = épisodes honnêtes du calibrage dans la strate. »
- **n_h** : « La partie lue porte n_h ≥ max(288 ; n80) unités à au moins un épisode honnête dans la strate, n80 = plus petite taille où le minimum des k gardes atteint m_c/α_c dans ≥ 0,8 des rééchantillonnages de la loi réelle recentrée au biais b_h (script v5 [empreinte], fichiers [empreintes], graine [valeur]) ; valeur : [n_h], comptée sans aucun score. »

## (iv) Règle d'arrêt si la garde ne certifie pas

« Si, à la fin de la tranche de G1, le minimum de la fiche n'atteint pas m_c/α_c, la fiche n'est pas promue et G1 est non concluante ; la fiche se poursuit une fois, à la génération suivante, sur des unités fraîches (valeur héritée, `Course`), sur devis et GO ; si le minimum n'atteint toujours pas le seuil, le verdict est "non promue" et G1 échoue, quelle que soit la richesse des contrastes. La fiche n'est jamais lue sans sa garde ; le rapport consigne les richesses finales de chaque processus (`log_gardes_finales`, `log_richesse_finale_par_comparateur`) en réserve, non opposables, sans rejeu ni changement de δ. »

# Contre-vérification des sections 4 à 9 (et points 6 à 10 de « L'essentiel ») de `reponse-demande-reformulee-v1.md`

Contre-vérificateur qui n'a rien écrit de la note. Pages = pages du fichier PDF, sauf mention.

## A. Écarts, du plus grave au moins grave

1. **§ 4.3, « Idées dans l'air »** — note : « 5 % des projets de biologie structurale finissent dans une course, quand les chercheurs croient ce risque à 25 % ». Source (hillstein2020nber.pdf, p. 3 et 5) : 5 % des projets sont pris dans une course de fin de parcours ; les 25 % sont la probabilité estimée *d'être devancé*, comparée à « the 3 percent chance we document ». Deux grandeurs différentes rapprochées. Correction : « 5 % des projets de biologie structurale sont pris dans une course de fin de parcours ; les chercheurs estiment à 25 % le risque d'être devancés, contre 3 % mesurés (Hill et Stein, version de travail 2020, p. 3 et 5). »

2. **§ 4.2, ligne « Les liens entre littératures se prédisent-ils ? »** — note : « les 50 premières prédictions … huit fois plus … ; mais 32 % l'avaient déjà été hors du corpus ». Source (tshitoyan2019_osti.pdf, p. 10) : « from the first 150 predictions using the full corpus … 48 materials (32%) had already been studied ». Le 32 % porte sur les 150 premières prédictions du corpus complet, pas sur les 50 prédictions datées. Le rapport fait déjà l'erreur. Correction : « … ; mais, sur les 150 premières prédictions faites avec le corpus complet, 48 (32 %) avaient déjà été étudiées dans des articles absents du corpus (p. 10) ».

3. **§ 9, recommandation 3, « Contre »** — note : « aucune preuve fiable d'un avantage des sous-populations à budget égal … (arXiv 2611.23949, p. 1 et 12) ». Source (rapport semaine-systemes § 10 ; PDF p. 1) : les intervalles qui contiennent zéro comparent deux façons de former les sous-populations (DBSCAN contre meneur-suiveur). Contre la population unique, les médianes sont plus basses (0,60 contre 0,63 à 0,80), et aucun intervalle n'est donné. Correction : « un essai de la semaine ne départage pas de façon fiable deux façons de former les sous-populations, et ne donne aucun intervalle pour leur écart avec la population unique (arXiv 2611.23949, p. 1 et 11-12) ».

4. **§ 4.1, Shi et Evans** — note : « … 3,5 fois ; pas d'effet pour les brevets ». Source (shi.pdf, p. 5) : « The most surprising patents are two times more likely to be hits than random ». Seule la nouveauté d'« expédition » n'est pas associée aux hits pour les brevets. Correction : « … 3,5 fois ; pour les brevets, la provenance lointaine n'est pas associée aux hits, mais les brevets les plus surprenants le sont deux fois plus que le hasard ».

5. **§ 7.1, McAllester et Schapire** — note : « La masse manquante estimée est à moins de O(√(ln(1/δ)/N)) de la vraie ». Source (mcallester.pdf, p. 1 ; rapport especes-good § 11) : borne *supérieure* seulement, M₀ ≤ G₀ + O(√(ln(1/δ)/m)) ; la borne inférieure est plus faible. Correction : « La vraie masse manquante ne dépasse l'estimée que d'au plus O(√(ln(1/δ)/N)), avec probabilité 1 − δ, quelle que soit la loi (borne supérieure ; l'inférieure est plus faible). »

6. **§ 4.3, Mossel et Steel** — note : la probabilité « tend vers 1 dès que chaque élément catalyse un nombre de réactions croissant linéairement …, et vers 0 en dessous ». Source (mossel2005.pdf, p. 9) : (i) si µ ≤ λn, la borne tend vers 0 quand λ → 0 ; (ii) si µ ≥ λn avec λ > ln κ, P ≥ 1 − κ(κe^−λ)^t/(1 − κe^−λ), qui tend vers 1 quand λ → ∞ ; corollaire 4.2 : P → 0 si max µ/n → 0, P → 1 si min µ/|x| → ∞. Ce n'est pas un seuil net. Correction : « … proche de 1 quand chaque élément catalyse au moins λn réactions avec λ assez grand (λ = 4 donne plus de 0,99 en binaire), et tend vers 0 quand ce nombre croît moins vite que n ».

7. **§ 6, cas 2, « Émission »** — note : « coder comment les résultats s'appuient les uns sur les autres (gain de 58 à 64 % à corpus fixe, contre 52 % …) ». Source (2611.19108.pdf, p. 7) : ce sont des taux de préférence de juges-modèles, et ils ne sont pas significatifs (p = 0,36 et 0,07). Correction : « (préférence de 58 à 64 % à corpus fixe, non significative, p = 0,36 et 0,07, contre 52 % pour le seul choix des articles ; juges-modèles, p. 7) ».

8. **§ 5.2, Watson et Crick** — note : Donohue, « qui leur fit prendre les formes céto des bases ». Source (watsoncrick1953_umich.pdf, p. 1 ; rapport memoires § 5) : seuls le remerciement et l'hypothèse céto figurent, sans lien entre eux. Watson 1968 et Crick 1988 ne sont pas lus. Correction : ajouter « [mémoire, à vérifier] » après « formes céto des bases ». Même chose pour « Les règles de Chargaff … n'avaient relié personne d'autre » : aucune source lue ne le dit.

9. **§ 6, cas 1, « Ce qui maximise »** — note : « l'indice multiplie l'émission par 4,6 chez l'humain ». Le calcul 92/20 = 4,6 est juste (gick1980b.pdf, p. 37). Mais deux pertes de nuance : chez Gick et Holyoak 1983, p. 4, le bilan des réplications donne environ 30 % contre 75 % (× 2,5) ; chez Puranam et al. (p. 18), les humains passent de 6,3 à 8,7 % seulement. Correction : « par 2,5 à 4,6 chez l'humain selon les mises en scène de Gick et Holyoak (mais presque rien chez les humains de Puranam et al., 6,3 contre 8,7 %), et par 15 chez le modèle sur un problème ». Ajouter aussi « chez le modèle » après « une analogie sur deux est fausse », car les humains sont à 0,67-0,75.

10. **§ 5.1, Gick et Holyoak 1980** — note : indice « servez-vous de l'histoire » entre guillemets. Source (gick1980b.pdf, p. 36) : « In solving this problem you may find that one of the stories you read before will give you a hint ». Correction : remplacer par « avec l'indice qu'une des histoires lues peut aider ».

11. **§ 8, point 4** — note : « Gideoni et al. et Oved et al. … y étaient déjà lus » (dans la veille du 18 novembre). Source (seances-anterieures.md, pièce 15 et partie V) : Gideoni n'est lu que le 20 novembre, dans une autre pièce. La liste omet aussi « lecture unique ». Correction : « Oved et al. y était déjà lu ; Gideoni et al. l'a été le 20 novembre » ; ajouter « lecture unique » à la liste.

12. **§ 5.1, Xie et al. 2021** — note : p. 10. Source (Park2021_eLife_PMC8282340.pdf, p. 6) : « 73 appeared in only a single trajectory ». Correction : « (Xie et al. 2021, p. 6) ».

13. **§ 6, « Reconnaissance »** — note : « 96 % de fausses alertes sur des idées réalisées ensuite (Liu et al. 2026, p. 7) ». Chiffre conforme (p. 7). Nuance perdue (rapport recent-idees § 4, annexe F.1, p. 20) : l'audit humain ne confirme comme nouvelles que 28 des 45 idées, et les étiquettes viennent d'un modèle. Correction : ajouter « (étiquettes posées par un modèle ; l'audit humain ne confirme que 28 nouvelles sur 45, p. 20) ».

14. **§ 6, « Poursuite »** — « The Implementation Lottery », 0,38 point, p. 1 : le rapport (preuves-idees-libres § 13) dit « lecture du résumé, p. 1 ». Le chiffre vient d'une comparaison secondaire « en intention de traiter », en points d'équivalent-exactitude. Correction : ajouter « [résumé] ».

15. **§ 5.1, Bloom et al. 2006** — note : l'effet « n'est pas significatif de l'aveu des auteurs ». Source (rapport biologie § 3) : « the statistics are too poor to conclude that functional innovation is improved significantly more » *que la robustesse*. Correction : « les auteurs jugent leurs données trop faibles pour conclure que l'innovation gagne plus que la robustesse (Bloom et al. 2006) ».

16. **« L'essentiel », point 7 et § 4.3** — « 46 redécouvertes indépendantes ». Source (society-of-ai-scientists-v1.pdf, p. 28) : « 46 independent same-question pairs », dont 87,0 % aux conclusions compatibles. Correction : « 46 paires où agents et humains posent la même question sans se citer ».

17. **§ 4.1, phrase d'ouverture** — « répliquées pour les trois premières ». Pour Uzzi et al., la seule réplication citée (Boyack et Klavans) n'est connue que par un résumé (rapport science-combinaisons § 1). Correction : « répliquées pour la deuxième et la troisième ; pour la première, réplication connue par un résumé seulement ».

18. **§ 4.3, tableau, ligne « Démontrée dans un modèle »** — l'urne de Tria et al. est rangée parmi les transitions démontrées. Le rapport (modeles-decouverte § 1) note que le texte parle d'un changement de régime à ν = ρ et n'emploie jamais « transition de phase » ; c'est vérifié (tria2014.pdf, 0 occurrence). Correction : ajouter « (changement de régime ; le mot « transition » n'est pas employé) ».

19. **§ 4.3, « Métaphore »** — « Criticité auto-organisée des innovations (Arthur et Polak 2006 …) ». Source (rapport § 3, p. 10) : les avalanches sont des avalanches d'obsolescence. Correction : « criticité auto-organisée des avalanches d'obsolescence ».

20. **Pages légèrement décalées (§ 4.2)** — Boudreau 2012 : « plus fort entre domaines proches » est p. 3, pas p. 6. Boudreau 2016 : 2 130 paires et 1,1 point sont p. 2 ; seule la pénalité de nouveauté est p. 3. Azoulay 2018 : −20,7 % est p. 19 et +8,6 % p. 20. Correction : « p. 3 et 6 », « p. 2-3 », « p. 19-20 ». Rzhetsky : le « monde fermé » est p. 3, l'absence de garantie p. 5.

21. **§ 5.2 et § 5.1, Poincaré** — « les combinaisons fécondes sont faites d'éléments … » (§ 5.2) et « viennent de “domaines très éloignés” » (§ 5.1). Source (poincare.txt, p. 51) : « les plus fécondes seront *souvent* celles qui … ». Correction : rétablir « souvent ».

22. **§ 5.2, mention de méthode** — l'en-tête dit « vérifiées sur texte premier, sauf mention ». Or Noddack est cité par la Société des chimistes allemands, l'original n'étant pas lu ; et l'erreur de Pasteur sur le pays et la date est « de mémoire » dans le rapport. Correction : ajouter « (cité par la GDCh) » après Noddack, et « [mémoire] » après « faux sur le pays et sur la date ». Pour Weisberg et Muldoon (§ 4.3), ajouter « (lus à travers Alexander et al.) ».

23. **§ 5.1, Blount 2008** — le libellé « [page de la revue] » laisse croire à une page vérifiée. Le rapport dit : lu sur page HTML, pagination non vérifiée. Correction : « [page HTML, sans pagination] ».

## B. Contrôlés sur la source et conformes

- Good 1953, éq. 2, r* = (r+1)n_{r+1}/n_r — good-1953, fichier 2 (p. 238).
- Good 1953, éq. 8 et 9, et la citation — fichier 3 (p. 239).
- « the larger is n1 the more applicable the results » — fichier 1 (p. 237).
- Échecs : N = 385, S = 174, n1 = 126 — fichier 26 (p. 262) ; 126/385 = 0,327 ≈ un sur trois.
- Good et Toulmin, formule 24 — fichier 6 (p. 50).
- Good et Toulmin, « worth enlarging » — p. 46 ; « useless without some modification » et « at least for λ < 5 » — p. 45 ; absence de terme d'erreur — p. 47.
- Efron et Thisted : 11 430, 178 et « useless » — p. 437 ; « No upper bound is possible » — p. 435.
- Orlitsky et al., théorèmes 1 et 2, horizon en log n — ost2016.pdf, p. 6.
- Li, Hays, Ramdas et Raghavan, théorèmes 3.2 à 3.4 — p. 8-11 ; dépôt du 11 novembre.
- Schaeffer et al. : 20 % et 32 % — p. 10 ; 3,34 contre 3,99 — p. 14.
- Böhme et al. 2021, quatre ordres de grandeur — residual.pdf, p. 9.
- Böhme et Paul, (ex − ex²)⁻¹ et « much less than five times » — p. 5.
- Li et al. 2025 : t = 100 (p. 7) ; validation jusqu'à t = 3 (p. 11, rapport).
- Si et al. 2024, 200 sur 4 000 — p. 13-14.
- Gick et Holyoak 1980 : 92 %, 20 %, 3 sur 15, 1 sur 15 — p. 37 ; 41 % et 35 % — p. 40.
- Gick et Holyoak 1983 : 45 % contre 21 %, et 91 % — p. 23.
- Puranam et al. : 1 sur 15 et 15 sur 15 — p. 18 ; précision 0,50 à 0,52 contre 0,67 à 0,75 — p. 23.
- AnaloBench : 3,9 % (égal au hasard) et 42,9 % — tableau 8, p. 21.
- Dunbar 1997 : 99, 16 et 2 — p. 7 ; 176 contre 23 — p. 11 ; 30 % — p. 13 ; oubli — p. 15.
- Nisbett et Wilson, « slightly less than a third » — p. 11.
- Yanai et Lercher, rapport de cotes 4,8, N = 33 — p. 2.
- Sio et Ormerod : 0,29 [0,21 ; 0,39] — p. 10 ; 117 études — p. 9 (rapport).
- Wagner et al., 59,1 % contre 22,7 % — p. 1.
- Blount et al. 2012 : trois étapes — p. 3 ; 270 clones, 17 mutants, 13 clones, génération 20 000, au moins deux mutations — p. 6.
- Wright 1932, citation — p. 363 (fichier 8, image).
- Wiehe et al., moins de 2 % — p. 3.
- Uzzi et al. : 9,11, 5 et 2,05 — p. 4 ; 17,9 millions d'articles (rapport).
- Wang et al., 39,82 % — p. 13 (le texte dit « odds », une cote, pas une probabilité).
- Foster et al., 85,8 % contre 14,2 %, « six times » — p. 4.
- Shi et Evans : environ cinq fois — p. 4 ; 3,5 fois — p. 5.
- Youn et al., ΔC = 0,6 ΔP — p. 7.
- Hao et al. : 3,02, 4,84 et 4,63 % — p. 1 ; réserve causale — p. 8.
- Boudreau 2012, 0,16 % contre 0,28 % — p. 6.
- Azoulay 2009 : 96 % et 35 % — p. 6.
- Chan et al., −0,33 en log-cote — p. 22.
- Jeppesen et Lakhani, 3,3 % au seuil de 10 % — p. 31.
- Derex et Boyd, 58,3 % — p. 2.
- Bernstein et al. : 48,3, 33,3 et 44,1 — p. 3.
- Tshitoyan, « eight times » — p. 2.
- Krenn et Zeilinger, 0,85 — p. 5.
- Mossel et Steel, théorème 4.1 — p. 9.
- Tria et al., régimes selon ν et ρ — p. 6.
- Bettencourt et Kaiser, « limited and noisy », « suggestive » — p. 5.
- Bettencourt et al. 2006, R₀ de 5,739 à 49,582 au meilleur ajustement — p. 18.
- Arthur et Polak, « not even a 2-bit adder … » — p. 8.
- Alexander et al. : p. 3 et 13 (≥ au lieu de >) ; 23 % puis 21 % — p. 18.
- Rosenstock et al., « small parameter range » — p. 2.
- Ogburn et Thomas, 148 cas — p. 5.
- Kuhn — p. 65 ; Popper — § 83, p. 270 ; Stent — p. 84 ; Peirce, « perfectly definite logical form » ; Simon, « selective search » (p. 6) et « wholly new discovery » (p. 4) ; Bernard — p. 59 ; Duhem — p. 364 et 420 ; Poincaré — p. 51 et « Ce n'est là qu'une hypothèse » (p. 61-62) ; Bachelard — p. 14.
- Poincaré (marche-pied, inspirations subites) ; Darwin (« for amusement » ; « never happened to come across ») ; esquisse historique (« races of man », « scattered passages ») ; Jacob, p. 154-155 ; Donohue (remerciement) ; Perutz (cantine) ; Hamming (10 à 20 problèmes, « cannot prove the cause and effect ») ; Rota, p. 25 ; Hadamard (« too narrowly directed », p. 10-11) ; Fleming, p. 83 ; Pasteur ; Warren ; Noddack (« mehrere größere Bruchstücke ») ; Bolyai (« violets ») ; Alpöge, p. 1.
- Xu et al. 2026 : 0,713, 0,609, 0,571 ± 0,041 et 0,524 — p. 5.
- Liu et al. 2026 : 380 sur 380 et 96,0 % — p. 7.
- Si et al. 2025, ρ = −0,386 — p. 26.
- DeepScientist, environ 60 % — p. 8.
- « The Implementation Lottery », 0,38 — p. 1.
- Aguilar Martín, 0,149 [0,138 ; 0,160] — p. 10.
- Graphe d'évolution des théorèmes : 58 %, 64 % et 52 % — p. 7.
- Zyskind, +30 à +90 — p. 12.
- Cang : 19 sur 32 et 1 sur 32 — p. 3 ; 78 % et 84 % d'entiers — p. 7.
- « The Resolution Hypothesis », 49,7 ± 1,9 % — p. 7.
- ResearchBench, « closer papers are more likely to be selected » — p. 6.
- « Society » : 2 %, 42 %, 73 %, 88 % contre 30 % — p. 22 ; 46 paires, 87,0 %, six — p. 28 ; chaînes contre le nul — p. 34.
- § 8, points 1 à 3 et 5, « Ce qui tient encore » et la règle « aucun score servi » — conformes au rapport seances-anterieures.md.

## C. Non contrôlé, et pourquoi

- Catalini, Mason et Watts, Crameri, Coyne et al., Simonton, Kuhn 1959 : sources non lues ; seul le marquage [résumé] a été vérifié (il est correct).
- Wallace (p. 361-363), Gould, Lacaux : vérifiés sur les rapports seulement (l'extraction OCR n'a pas rendu « suddenly flashed »).
- Wilke, Hills, Abbott, Baayen, Collins, Haynes : vérifiés sur les rapports, pas sur les PDF.
- § 8, renvois à « Initialization Improves LLM-Driven Discovery » (p. 6) et à Schaeffer p. 13-14 au titre des séances : non contrôlés au titre du § 8, selon la consigne. Schaeffer, p. 14, est contrôlé ailleurs.
- Bachelard, p. 14 : la citation est trouvée dans le texte extrait, mais sa page n'est pas confirmée sur l'image.

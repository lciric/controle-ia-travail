# Note pour Lazar — course de l'organisme à plusieurs générations : décisions avant le scellement — v1

Écrite par le rédacteur (Claude Opus 5.5) le 2026-11-13 vers 02:20 UTC (`date -u`). Texte qui fait foi :
`preenregistrement-multi-generations-v1-brouillon3.md` (`2dda3b74ff5e13d56a8f0818623b0b64730a3b3da5f86a136df321343f653a39`),
section 14 pour le détail.

**Verdict.** Le préenregistrement est prêt pour tes mots : il a été contre-lu (Fable 5.2) et vérifié, les corrections sont
portées. Il reste à écrire et geler le code v68, et à faire tourner le banc de calibration (calcul seul). Une chose doit
compter dans ta décision : **sous le modèle de proposeurs simulés, la famille de mondes actuelle ne laisse rien de solide à
trouver après la génération 1.** La course répondrait sur la garde (les fausses lois restent-elles refusées quand l'archive
grandit ?) et sur la boucle, mais presque pas sur le progrès.

**Le constat, simplement** (12 mondes simulés, pièces scellées et recomptées deux fois) : la génération 1 prend toutes les
composantes fortes et moyennes dans les 12 mondes. Une composante neuve n'apparaît plus tard que dans 4 mondes, et c'est
toujours une faible, à peine détectable. La génération 3 ne retient rien, nulle part. « La boucle progresse », au sens
certifié, dans 0 monde sur 12. Ce modèle de proposeurs est arbitraire et généreux : de vrais proposeurs peuvent aller moins
vite, et rien ne le chiffre.

**Q-1 — Nombre de mondes (à confirmer).** Enjeu : réplication contre coût ; deux mondes ne mesurent aucune dispersion.
(a) 1 monde × 3 générations : ≈ 21 USD attendus, 205 au pire ; un seul monde décide de tout. (b) 2 × 3 : ≈ 42 attendus, 422
d'engagement ; réplication, mais « non répliquée » probable. (c) 3 × 3 : ≈ 62 attendus, 614 au pire ; une dispersion grossière.
Recommandation : **(b)**, confiance 0,5, à revoir avec Q-13.

**Q-3 — Qui tire le secret des mondes de test.** Enjeu : qui pourrait fixer les mondes. (a) La machine seule : rien à faire
pour toi ; une session Claude fixe seule le secret. (b) Ta phrase seule : aucune session ne la connaît ; secret moins uniforme.
(c) Les deux, dans l'ordre : secret machine engagé et poussé, puis ta phrase ; personne ne fixe seul, rien ne se retire après un
regard ; deux étapes. Recommandation : **(c)**, confiance 0,65.

**Q-9 — Ce qu'est une vraie découverte.** Enjeu : le juge ne borne pas la part des retenues sans vrai gain (28 sur 181 en
simulation) ; touche la revendication O2. (a) Gain au-delà du seuil contre l'archive et contre ses mélanges ; tolérance mesurée
au banc, sans marge à fixer ; honnête, mais la tolérance n'est pas α et vient de proposeurs simulés. (b) Marge mise dans le juge :
juge et vérité réaccordés ; règle du juge changée, puissance perdue. (c) Rapport seul : rien à fixer ; aucune issue ne dépend de
la vérité. Recommandation : **(a)**, confiance 0,6.

**Q-10 — Publication du générateur de mondes.** (a) Publié avec le code, mondes et secret privés jusqu'au verdict : vérifiable
par tous ; la famille devient publique (elle l'est déjà presque). (b) Privé jusqu'au verdict, avec ce texte : famille cachée ; code
non entièrement public. (c) (a) plus les mondes publiés après : rejouable ; ces mondes ne servent plus de test. Recommandation :
**(a)**, mondes publiés seulement sur ton mot, confiance 0,6.

**Q-11 — Sens de « plusieurs traits cachés ».** (a) Traits observés dont l'effet est caché, plus des leurres, un trait non
observé un monde sur trois : tout ce qui est compté est trouvable. (b) Un ou deux traits non observés par monde : plus réaliste ;
composantes introuvables, puissance réduite. (c) Les deux à la fois : les deux lectures servies ; le coût de (b) partout.
Recommandation : **(a)**, confiance 0,5 ; (c) si tu visais les traits non observés.

**Q-12 (i) — Tester les lois plantées promues.** (a) Fausses non testées, vraies testées à chaque génération : 365 + 57 USD
d'engagement ; aucune fausse promue n'est testée. (b) Fausses testées aussi : 445 + 62 ; dessin de la v66, 85 USD de plus.
(d′) Vraies testées en génération 1 seulement, l'instrument T-ELIM à chaque génération : 291 + 52 ; la survie des vraies n'est
plus éprouvée ensuite. Recommandation : **(a)**, confiance 0,5 ; (d′) si tu veux un plafond plus bas.

**Q-12 (ii) — Seuil d'arrêt sur les tests coupés par la borne en génération 1.** Un quart (au-delà de 9 sur 37) : peu de
dépense perdue, arrêts plus fréquents. Un tiers (au-delà de 12) : équilibre. La moitié (au-delà de 18) : arrêts rares, lecture
plus fragile. Recommandation : **un tiers**, confiance 0,4 (aucune pièce ne le fonde).

**Q-13 — Garder ou revoir la famille des mondes.** Enjeu : le constat ci-dessus. (a) Garder : aucun délai ; réponse sur la garde
et la boucle, presque pas sur le progrès. (c) Revoir la famille (des composantes moyennes que la génération 1 ne peut pas capter
seule), avec une règle écrite d'avance : pas de course si moins de la moitié des mondes de calibration gardent une composante
certifiée encore trouvable après une génération 1 simulée — **ce seuil de la moitié n'a aucune pièce** ; la question du progrès devient
répondable ; délai, et la règle dépend du modèle arbitraire. (e) Pilote d'une génération avec les vrais proposeurs sur 2 mondes
de calibration, au pire 9 USD par monde : on mesure ce qu'ils prennent vraiment ; un texte et une ligne de GO de plus.
Recommandation : **(c)**, confiance 0,45 ; (e) à 0,35 ; (a) à 0,3 si l'échéance prime.

**Échéance.** Le 30 novembre est court pour le code v68, le banc, une famille revue et la porte G0 : à toi de la fixer.

**Lignes de GO proposées, non inscrites** (2 × 3 ; numéro donné à l'inscription) :

```
| GO-AAAA-MM-JJ-NN (β1) | AAAA-MM-JJ | calcul | **Course de l'organisme à plusieurs générations, part sur crédits de Claude** : proposeurs Fable 5.2 (plafond de session 3 USD) et Opus 5.5 (2 USD), expérimentateur Opus 5.5 (1,50 USD par test, test coupé = non concluant) ; 2 mondes × 3 générations ; vraies plantées replantées à chaque génération ; fausses et copies promues non testées (Q-12 (a)) ; conditions toutes exigées : préenregistrement neuf contre-lu et scellé, code v68 contre-lu (regroupement, règle du représentant à tranche de choix appariée, réponses brutes, témoins par test), banc de calibration fait (n et seuils fixés par leurs règles), engagement du secret machine poussé avant la phrase de Lazar, mondes vérifiés et leurs empreintes inscrites ; jamais de ligne d'extension ; arrêt par identifiant (R10), dépenses et arrêts consignés | 365 USD (sur crédits) | 2026-11-30, et avant la fin de cycle des comptes | Lazar | R-2442, R-2443, R-2461, R-2467 ; mot de Lazar à recopier |
| GO-AAAA-MM-JJ-NN (β2) | AAAA-MM-JJ | calcul | **Même course, part hors crédits** : Argon proposeur (2 USD par session) et vérificateur (0,10 USD par test) 35 USD, Astra proposeur 12 USD (identifiant et prix confirmés avant l'appel), machine jetable à `bwrap` 10 USD, validée par l'essai à blanc au vrai bac avant tout appel payant ; plafond de chaque relais égal à sa part ; mêmes conditions que la ligne β1 ; jamais de ligne d'extension ; arrêt par identifiant (R10) | 57 USD | 2026-11-30 | Lazar | R-2442, R-2443 ; mot de Lazar à recopier |
```

Variante Q-12 (d) (vraies plantées, T-ELIM compris, testées en génération 1 seulement) : mêmes textes, avec « vraies plantées
testées en génération 1 seulement, lues à la promotion ensuite » à la place de « vraies plantées replantées à chaque génération »
dans β1, **β1 285 USD** et **β2 51 USD** (Argon 29, Astra 12, machine 10). Sous (d′), T-ELIM testé à chaque génération : β1 291,
β2 52.

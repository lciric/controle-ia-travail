# Proposition A, tour III.3 : réponse aux critiques

**Pièces.** Les faits, la question, ma conception III.1 et les quatre critiques (B, C, D, E) sont présents et non coupés. Je n'ai pas recalculé les sha256. Je ne réponds qu'aux sections « Sur la proposition A ».

**Statuts.** Les faits restent « FAIT TRANSMIS, statut non fourni ». Je ne reprends pas le « RAPPORTÉ » que C et E leur attribuent, ni les « VÉRIFIÉ » que les critiques posent sur leurs propres déductions. Quand j'ai refait un calcul, je l'écris « recalculé ici » : c'est une déduction sous définitions, pas une mesure sur le pilier. Tout le reste est HYPOTHÈSE ou proposition de A.

---

## (a) Critiques : acceptée, rejetée, ou transformée en test

| # | Critique (source) | Verdict | Conséquence |
|---|---|---|---|
| 1 | Les travaux de 2026 aperçus ont pu orienter la rédaction des cibles (B a1, E a2). | Acceptée | B prédit des collisions vraies par construction, E une auto-censure qui les évite : le signe du biais est inconnu. Chaque cible reçoit une date et une déclaration d'exposition de son rédacteur. Test seulement si l'exposition varie entre rédacteurs, ce que je ne sais pas. |
| 2 | « Croisés par hasard » n'est pas un tirage aléatoire ; le contrôle par articles tirés au hasard mesure le filtre d'attention (B a2, D b, E b3). | Acceptée | Contrôle retiré. Recalculé ici : avec k articles par bras, la table la plus extrême du test exact a une probabilité 1/C(2k,k) ; pour k ≤ 2 elle dépasse 5 % et aucun rejet n'est possible. |
| 3 | Sur le banc « avant Y », une réponse « connu » confond fausse alerte, fuite mémorielle et vraie anticipation ; la date de publication n'est pas la date d'apparition (B a3, C a2, C b3, D a, E a2, E b2). | Acceptée | Je retire « vérité-terrain sans jugement ». Ce qui change entre les deux états est la disponibilité d'un témoin nommé (formulation de D), y compris pour le banc git. Le banc est reconstruit en E0. |
| 4 | Audit multi-dialectes de pré-existence pour chaque théorème du banc (C c2). | Rejetée telle quelle | L'audit suppose l'instrument inter-domaines que le banc doit mesurer : c'est une régression. Je la remplace par une construction où l'anticipation est exclue (énoncés postérieurs à la coupure du modèle ou composés pour le banc, index isolé). Une anticipation trouvée avec source datée devient une troisième catégorie, ni fausse alerte ni fuite. |
| 5 | Le témoin négatif de E2 (objets à score sur instances fraîches) n'a pas la forme « énoncé » ; son f est bas par construction (B a4, C a3, E a1). | Acceptée | Remplacé par des négatifs de même forme et de même lexique. |
| 6 | Un négatif démontrable pour un couple texte–cible ne certifie pas la nouveauté de la cible (convention de D). | Acceptée, et je m'en sers | f est désormais défini par couple, comme une alerte sur un couple dont l'implication est réfutée par contre-modèle. Aucune cible n'est étiquetée « neuve ». |
| 7 | E3 : zéro événement ne falsifie pas une existence ; le décompte ignore les collisions propres au bras « cible » (B a5, D b, E a2, E b3). | Acceptée | E3 est réécrite en taux, avec marge et décompte symétrique. |
| 8 | τ de E2 abandonne f et le retard, présents dans mon propre calcul (B a6, E a1). | Acceptée | J'adopte la forme que D écrit à propos de C : G = p·r·b − (1−p)·f·h − c, avec b le coût évité, h la perte d'un abandon à tort et c le coût de lecture, retard compris. Le seuil devient p > (c + f·h)/(r·b + f·h). |
| 9 | E2 non jugeable à n = 15 pour τ petit (B b, C b1). | Acceptée | Recalculé ici : 1 − 0,05^(1/15) ≈ 0,181. Sous ce seuil, même zéro collision ne place pas l'intervalle sous τ. |
| 10 | p n'est pas identifiable : q = p·r + (1−p)·f, erreurs corrélées entre agent et lecteur, r du banc non transposable à l'usage (B N1, C b2, D b, E b1). | Acceptée, transformée | Je cesse de vouloir estimer p. E2 porte sur une quantité observable (voir E2′). |
| 11 | Seuil τ̂ instable par substitution de r̂ ; grappes de cibles corrélées ; « n augmenté si indécis » est un arrêt optionnel (E a1, E b1). | Acceptée | J'utilise une borne inférieure de confiance sur r, pas r̂. L'unité d'analyse est la famille. L'effectif maximal est fixé avant le début, sans relance. La formule de variance de E se retrouve par la méthode delta. |
| 12 | Le lecteur humain est à la fois oracle et instrument mesuré (C a1, E a3). | Acceptée en partie | Un positif s'adjuge désormais par certificat (source datée et réduction écrite), qu'un tiers peut vérifier. La circularité demeure sur les collisions manquées : le rappel de l'oracle reste inconnu. Le contrôle C c3 devient un test : collisions certifiées, rédigées hors de la sous-spécialité du relecteur. |
| 13 | E3 à « même budget total » divise le budget par cible par K (C a4, E a2). | Rejetée comme défaut, acceptée comme bras | L'arbitre répartit une seule enveloppe : le budget total égal est le contraste utile à la décision. En revanche, un gain du bras « zone » peut rémunérer une simple relance (D c). J'ajoute une seconde recherche ciblée indépendante. |
| 14 | Les positifs du banc sont ceux qu'on sait trouver (B N3) ; r doit être publié par type de déguisement ; le lexique du §3 fuit vers le banc ; les reformulations d'un théorème ne sont pas indépendantes (B b, D a, D b, E a3). | Acceptée | Les familles de test sont réservées, les déguisements sont écrits par un tiers, r est donné par strate. Le rappel mesuré majore le rappel réel et je l'écris sur chaque fiche. |
| 15 | Deux témoins plantés : un instrument médiocre passe avec probabilité r² (B b). | Acceptée | La validité se juge sur un intervalle pour r, pas sur un comptage. |
| 16 | Forme « score » : l'absence de table de records ne rend pas la nouveauté « acquise » ; une règle publiée peut valoir sur toute la famille (E a1, D a). | Acceptée | Je retire « acquise ». La procédure pour cette forme devient celle de D : relire la notice et réexécuter la règle publiée à contraintes identiques. |
| 17 | Empreinte : un PDF vide se détecte à sa taille ; il faut un PDF complet dont l'annexe ne contient pas, ou infirme, la justification, et demander le passage (D c, E c3). | Acceptée | Intégré à E0. |
| 18 | Reclassement d'un énoncé connu en lemme : vérifier qu'il ne se ferme pas déjà par tactique automatique (E c4). | Acceptée comme filtre | Le filtre est nécessaire mais pas suffisant, car l'échec de fermeture dépend de l'encodage. Je ne sais pas si la liste fermée autorise le reclassement : c'est à l'arbitre. |

Aucune critique n'a contesté S4 (une recherche exhibe une collision, jamais une nouveauté). Elle reste HYPOTHÈSE.

---

## (b) Expériences corrigées

**Règles communes.**
- Les seuils dérivent du rapport de coûts fixé par l'arbitre avant toute mesure.
- L'effectif est fixé à l'avance.
- Un intervalle à cheval donne « pas de verdict », sans relance.
- Une abstention compte comme non-détection sur un positif et comme alerte sur un négatif.
- Tout chiffre ci-dessous est illustratif.

### E0. L'agent lecteur apporte-t-il quelque chose aux lignes mécaniques ? (nouvelle, issue de ma partie (c))

- **Unité.** La famille : un résultat source et ses variantes. Les familles de réglage et de test sont disjointes.
- **Positifs.** Couples (texte, cible) avec réduction écrite et vérifiée, en quatre strates : identique déguisé, cas particulier, corollaire à un pas, autre vocabulaire. Les déguisements sont écrits par un tiers qui ne voit pas le lexique de l'agent.
- **Négatifs.** Couples de même lexique dont l'implication est réfutée par contre-modèle vérifié, et PDF complets à annexe substituée.
- **Mémoire.** Index isolé et énoncés postérieurs à la coupure du modèle ou composés pour le banc. Un bras « même agent sans index » est ajouté (contrôle de B).
- **Hypothèses.** Δ est le rappel de l'agent moins celui de la meilleure ligne mécanique (mots-clés, citations à deux sauts, plongements), sur la strate primaire pré-déclarée « corollaire + autre vocabulaire », à f de couple sous un plafond fixé. H_A : Δ > δ. H_B : Δ ≤ δ. Le verdict se lit sur l'intervalle apparié par famille.
- **Falsification.**
  - H_B vraie falsifie l'option (a) telle qu'écrite (« par un agent »), quel que soit p. L'agent sort de mon étage 1.
  - H_A vraie falsifie mon repli « lignes mécaniques et humain suffisent ».
- **Invalidité.** Si le bras sans index répond « connu » au même taux que le bras avec index, c'est la mémoire qui décide et le banc ne mesure pas la recherche.
- **Perte de puissance.** Le nombre de familles nécessaire dépend de δ et du taux de discordance. Je ne sais pas combien de familles certifiées un relecteur peut produire. Si l'effectif ne peut pas séparer δ, on publie r par strate avec intervalles, sans verdict.
- **Limite.** Le rappel mesuré majore le rappel réel (N3). Rien ne garantit la transposition du banc à l'usage.

### E1′. Les travaux de 2026 déjà repérés changent-ils une décision ?

Ce n'est plus une mesure de p ni un test de la valeur des rencontres fortuites. Les critiques 1 et 2 ferment ces deux lectures.

- **Préalable.** Avant toute lecture, écrire pour chaque cible quel témoin la ferait abandonner, importer ou renommer (question de D, que je reprends). Dater les cibles, déclarer les expositions. Le lecteur est distinct des agents chercheurs.
- **Hypothèses.** H_A : au moins un couple (travail, cible) reçoit un certificat qui change la décision. H_B : aucun.
- **Falsification.**
  - H_A vraie falsifie « le gel est sans coût sur la liste actuelle » et fournit un témoin concret pour demander l'exception.
  - H_B vraie falsifie mon affirmation III.1 selon laquelle cette pile est la lecture la plus probablement informative, à la résolution du nombre k de travaux.
  - H_B ne dit rien de p et ne soutient pas (b) : si k·π ≲ 1, zéro est l'issue attendue dans les deux cas (N2 de B).
- **Limite.** k est absent des faits.

### E2′. La recherche ciblée avant scellement se paie-t-elle ?

- **Quantité.** q_cert, le taux de candidates « énoncé » pour lesquelles la procédure P produit une collision certifiée. q_cert vaut p·r_chaîne : il minore p et s'observe sans connaître ni p ni r.
- **Faux abandons.** Un abandon exige un certificat. Le « retrait erroné », non observable, est remplacé par « retrait sans source datée ni réduction » (formulation que B propose à D), qui doit rester à zéro.
- **Hypothèses.** H_A : q_cert > τ′ = c/b, où c inclut le temps d'adjudication des alertes non certifiées. H_B : q_cert ≤ τ′.
- **Falsification.**
  - H_A vraie falsifie (b) pour cette forme.
  - H_B vraie falsifie « P se paie ». Elle ne falsifie pas « une meilleure lecture se paierait », puisque p(1−r) reste invisible.
- **Condition de jugeabilité.** H_B n'est atteignable que si l'effectif dépasse environ 3/τ′ (exactement : τ′ > 1 − α^(1/n)). L'effectif est borné par la taille de la liste, absente des faits. Si la condition échoue, E2′ n'est pas lancée comme duel : les fiches sont consignées sans verdict.
- **Grappes.** Les cibles d'une même zone ne sont pas indépendantes. L'effectif utile est le nombre de grappes.

### E3′. La largeur de zone apporte-t-elle plus qu'une relance ciblée ?

- **Bras.** Sur les mêmes K cibles d'une zone, trois bras isolés sans partage de traces : ciblé T, ciblé indépendant T′, zone Z. Budget cumulé égal.
- **Métrique.** Gain net de Z sur T = N(Z seul) − N(T seul), en collisions certifiées. Référence : gain net de T′ sur T.
- **Hypothèses.** H_A : le gain net de Z dépasse celui de T′ d'une marge m fixée. H_B : il ne la dépasse pas.
- **Falsification.**
  - H_A vraie falsifie ma recommandation « pas de couche de zone ».
  - H_B vraie falsifie (a) et (c) comme défaut dans cette zone, à la résolution de l'intervalle. Ce n'est pas une falsification absolue.
- **Perte de puissance.** Si K·p·q_z ≲ 1, l'issue nulle domine sous les deux hypothèses. Le verdict se prend alors sur des témoins certifiés plantés, dont une strate atteignable seulement par un résultat général de vocabulaire différent. Ils mesurent la capacité du bras, pas la prévalence.
- **Ordre.** Seulement après E0.

---

## (c) Réponse à l'arbitre, en une page

**Ce qui est établi.** Rien n'est mesuré. Il y a deux sortes d'appui.

- *Faits transmis (statut non fourni).* La veille est gelée par le directeur. Des travaux de 2026 ont été croisés sans être lus. Une bibliothèque Lean publique existe. Collision tardive et lecture large coûtent toutes deux. Un juge de nouveauté et un lecteur humain sont prévus.
- *Déductions sous définitions, recalculées ici.* Elles ne sont pas des résultats sur le pilier.
  - Un taux d'alerte ne sépare pas p de f.
  - Zéro collision sur n n'exclut que des taux supérieurs à environ 3/n.
  - Une collision certifiée minore p. Rien dans le dispositif ne le majore, sauf une borne inférieure sur le rappel réel, que le banc ne fournit pas (il le majore, N3).

**Ce que j'en tire (HYPOTHÈSE).** La preuve disponible ne peut pousser que dans un sens. Trouver des collisions peut justifier plus de lecture. Ne pas en trouver ne peut pas en justifier moins. L'option (b) ne peut donc pas se défendre par « les collisions sont rares » : elle ne se défend que par les coûts (scellement réversible, dépense par cible faible). Je retire de III.1 la clause « p compatible avec zéro rend (b) défendable ».

**Ce qui n'est pas établi.** Je ne sais pas :
- la taille de la liste, le nombre de travaux croisés, le rapport de coûts ;
- si le gel admet une exception, et si la construction d'un banc à partir de littérature ancienne tombe sous le gel ;
- le rappel et le taux de fausses alertes de l'agent, du juge et du relecteur ;
- si la liste est déjà scellée ;
- si les angles morts des instruments sont corrélés.

Mes durées et volumes de III.1 étaient illustratifs et n'étayent aucune conclusion.

**Reformulation** (celle de D, que j'adopte à la place de la mienne) : sur quelles candidates une couche de lecture supplémentaire change-t-elle assez souvent la décision pour payer son coût, toutes candidates comptées ?

**Recommandation.** Elle reste une option (d) à étages, indexée par cible et par point d'engagement, mais sa justification change. Elle ne repose plus sur une comparaison de p à un seuil, non jugeable sur une liste fermée de taille modeste. Elle repose sur l'asymétrie ci-dessus et sur la forme des cibles.

- *Lemme.* Instantané du dépôt et PR ouvertes ; mécanique.
- *Score.* Notice, et réexécution de la règle publiée à contraintes identiques.
- *Énoncé.* Recherche ciblée avant scellement. L'issue est un certificat ou la mention « non trouvée par P, rappel par strate sur le banc B (majorant), date D ».
- *Avant revendication.* Nouvelle recherche sur le résultat réellement obtenu, et le rapprochement le plus difficile soumis à un spécialiste externe.
- *Couche de zone.* Seulement là où E3′ l'établit.

Les options écrites :
- (a) confie cinq zones à un agent dont rien ne dit qu'il bat une ligne de mots-clés.
- (b) ne peut pas recevoir d'appui empirique (asymétrie).
- (c) n'a pas de critère d'arrêt.

**Coût.** Le poste dominant est probablement le temps du relecteur, pour les certificats et le banc. Je ne sais pas le chiffrer.

**Ce qui la ferait changer.**
- E0 donne H_B : plus d'agent lecteur ; lignes mécaniques et humain, sur un périmètre réduit.
- E3′ donne H_A dans une zone : j'y ajoute une lecture de zone, vers (a).
- Le gel est maintenu sans exception : cibles payantes restreintes aux formes à antériorité mécanique, toute autre revendication marquée « antériorité non vérifiée ».
- Le scellement est réversible à bas coût et la dépense par cible faible : (b) pour « lemme » et « score », sur le seul argument des coûts.
- Deux instruments à index et modèles disjoints ont un recouvrement compatible avec l'indépendance (duel de capture-recapture proposé par B, que j'emprunte) : une majoration de p devient défendable. Alors seulement un p faible pourrait plaider pour moins de lecture.

**Expérience à faire en premier : E0.** Trois raisons.
- C'est la seule dont nous choisissons l'effectif. Les autres sont bornées par la taille de la liste.
- L'interprétation de E1′, E2′ et E3′ dépend de r et de f.
- Ses deux issues tranchent sans connaître p : soit l'option (a) « par un agent » tombe, soit mon repli sans agent tombe.

En parallèle, et sans attendre : écrire le témoin décisif de chaque cible, puis, si le directeur accorde l'exception, lire la pile de 2026 contre ces témoins (E1′). C'est une action à valeur de décision, pas une expérience sur p.

FIN-DE-CELLULE
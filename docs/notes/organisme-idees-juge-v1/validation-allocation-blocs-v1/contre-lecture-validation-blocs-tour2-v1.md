# Contre-lecture 2 du préenregistrement de la validation propre de l'allocation par blocs (brouillon 2) — v1

- **Lecteur** : sous-agent neuf, modèle C (R2) ; il n'a écrit ni le brouillon 1, ni le brouillon 2, ni le rapport du tour 1, ni le préenregistrement de l'idée 1.2, ni ses addendums, ni son verdict. Texte des brouillons : modèle A. Début 2026-11-17 01:37Z (`date -u`) ; fin : heure du compagnon `.sha256` de ce rapport. Tour 2.
- **Pièce lue** : `docs/notes/organisme-idees-juge-v1/validation-allocation-blocs-v1/prereg-validation-allocation-blocs-v1-brouillon2.md` (`51a8a3ab4091e27b94baad200fd7bc469f1b2b400e6346febb1471dab07a61be`, compagnon conforme), 436 lignes, lue en entier.
- **Autres pièces lues** : brouillon 1 (`95f34a75…`, compagnon conforme, recalculé) ; rapport du tour 1 (`c0681308…`, recalculé, lu en entier) ; différentiel du rédacteur (`53854664…`, compagnon conforme) et programme d'application (`b9ca8aa9…`, empreinte conforme ; titre et empreinte seulement, non relu ligne à ligne : la vérification porte sur le texte, par `diff`) ; verdict de l'idée 1.2 [V] (`3b08f061…`), seulement les lignes de comptes (4 483, 17, 56, 55, couvertures de F).
- **Jamais ouvert** : rien sous `diag/`, `runs/`, `donnees/` ; aucune branche `calcul/*` ou `donnees/*` ; rien de 7a, 7b, T0.6, T0.7, B bis, P3-bis, du bras d'attaque, du pilote MR-2 ; aucun secret ; aucune variable d'environnement affichée ; aucun appel réseau, aucune machine, aucune dépense ; aucun commit ; aucune pièce modifiée.

## Verdict

**« corrections »**. Les 29 corrections demandées au tour 1 sont toutes appliquées, **fidèlement** (vingt-cinq mot pour mot, quatre reformulées et déclarées comme telles), et le brouillon 2 ne contient **rien d'autre** que ces couples et les quatre modifications annoncées par le rédacteur (par `diff` et par rejeu du différentiel). Mais deux corrections majeures du tour 1 ne sont tenues que **de lettre** : l'annexe A du serrage (M5) et l'annexe B du dimensionnement des doses (m10) sont toujours **à écrire**, et le texte le dit lui-même (« il n'est pas prêt pour la contre-lecture 2 »). Les questions Q-1 et Q-2 restent ouvertes dans le texte. Trois défauts majeurs restants (M1' à M3'), neuf remarques mineures (m1' à m9'), dont des coordinations que les corrections du tour 1 ont créées. Aucune ne met la conception en cause : pas de « à refaire ».

Le validateur du dépôt (`prereg.problemes`) rend une liste vide sur le brouillon 2 ; il ne voit pas ces défauts, qui sont de fond.

## 1. Les corrections du tour 1 : appliquées fidèlement ?

**Différentiel** : `diff` du brouillon 1 contre le brouillon 2 relu hunk par hunk ; le différentiel du rédacteur s'applique en sec (`patch --dry-run`) au brouillon 1. Résultat : exactement 29 couples du rapport, plus quatre couples du rédacteur (titre ; ligne « Brouillon 2 » ; statut de l'en-tête ; section « Contre-lecture »). Rien d'autre. La « Déclaration » finale reste celle du rédacteur du brouillon 1, comme dit.

| couple | état | remarque |
|---|---|---|
| M1-a | reformulé, déclaré | ajoute au calcul de durée contrôles, essai E1, jeu synthétique, serrage (« au moins 1 heure ») : fidèle à la réserve du § 1 (4) du tour 1. Voir m2' (seuil de 12 heures) |
| M1-b | tel quel | |
| M2-a à M2-f | tels quels | voir m1' (coordination avec l'étage 1) |
| M3 | tel quel | |
| M4-a | reformulé, déclaré | la parenthèse « proposition du contre-lecteur » devient « retenue telle quelle ; aucune autre répartition n'est permise » : bon, un texte gelé ne laisse rien d'ouvert. Compositions vérifiées (voir § 2) |
| M4-b | tel quel | clé `(12 ou 13, g, 3001)` : seules les familles 12 et 13 ont une carte en plus tirée ; la famille 14 n'en tire pas : cohérent |
| M5 | tel quel **mais l'annexe n'existe pas** | voir M1' |
| m1-a à m1-d | tels quels | garde élargie à `*-idee-1-2-*` et `jeu-idee-1-2-*` ; la consigne de nom neuf (étape 6) évite l'auto-blocage : bon |
| m2-a, m2-b | tels quels | recalcul : 56 / 4 483 = 0,01249 ; [V] donne bien 4 483 porteuses, 17 sans gain, 55 arrêtées bas et une au plafond |
| m3 | tel quel | |
| m4 | compte mis à jour, déclaré | recompté par moi : principales 2 + 2, par carte 3 (réplique, porteuse unique, dense), « dense » 3 (écart des fausses promotions, niveau de A seul, couverture), « vide » 2 : 4 + 3 + 5 = **12**. Juste |
| m5 | tel quel | voir m3' |
| m6-a, m6-b | tels quels | |
| m6-c | tel quel | **mais l'énoncé copié est faux dans sa généralité** : voir m4' |
| m7 | reformulé, déclaré | l'attribution « pour « dense » » est ambiguë : voir m5' |
| m8 | tel quel | voir m6' (colonne de réfutation de P7 et P8) |
| m9 | tel quel | voir m3' |
| m10 | tel quel **mais l'annexe n'existe pas** | voir M2' |
| m11 | tel quel | |

Les affirmations du tableau « Réponse point par point » (« tels quels », « reformulé », « compte mis à jour ») sont **toutes exactes** ; la mention du nombre « 29 couples » est juste (2 + 6 + 1 + 2 + 1 + 4 + 2 + 1 + 1 + 1 + 3 + 1 + 1 + 1 + 1 + 1 = 29).

## 2. Vérifications refaites (celles que les corrections ont pu déranger)

- **R1 complet** : hypothèse, prédictions P1 à P14 avec signe et chiffre, métrique, seuil, plan, critères gelés (huit étages), liste d'arrêt : toutes les sections sont là et le validateur du dépôt n'a rien à dire. Manque de fond : les annexes A et B (M1', M2'), l'ambiguïté du seuil de 12 heures (m2').
- **R3 et R4** : tenus. Le choix des doses après lecture de [V] reste déclaré ; les « trop propre » et « tout négatif » sont conservés. Le nouvel étage 2 corrigé (M3) renforce la symétrie : un tort constaté n'est plus masqué. La lecture (5) restreinte aux voisines du monde est honnête sur son absence de pouvoir ailleurs : bon pour R4.
- **Fidélité à la conception d'origine** : le brouillon 2 ne touche aucune règle de bras, aucun seuil de [T] (13 et 39 pour 500 ; aucun changement de ligne) ; les ajouts vont dans le sens de réserves du verdict. Rien n'a dérivé.
- **Compositions (M4-a)** : totaux de 24 cartes vérifiés famille par famille : « porteuse unique » 1 + 7 + 5 + 8 + 3 = 24 (copies de classe 4 + 3 ; fausses 6 cosinus + 2 opposées) ; « dense » 12 + 4 + 3 + 4 + 1 = 24 (copies 2 + 2 ; fausses 3 cosinus + 1 opposée) ; « vide » 0 + 6 + 8 + 8 + 2 = 24 (copies 3 + 3 ; copies par morceaux : les quatre constructions deux fois, comme le tableau le dit). Concordance entre la phrase de répartition et le tableau : bonne. Réserve mineure : la phrase de répartition ne dit rien de « vide » pour les copies par morceaux (le tableau, si) ; sans conséquence.
- **Compte des intervalles de lecture « nuisible »** : 12, voir ci-dessus ; la phrase « ne sont pas corrigées » reste vraie.
- **Seuil de la lecture (1)** : 13 et 39 pour sept bras inchangés.
- **Devis** : processeur seul, 0 dollar, aucun devis : cohérent ; échelle toujours juste (3,19 h × 72 000 / 30 000 = 7,7 h ; oracle 1,2 h ; contrôles, E1, jeu synthétique, serrage ≥ 1 h : total ≈ 10 à 12 h, sous 24 h). **Crédits et hors crédits ne sont pas séparés dans le texte** (m7').
- **Aucun identifiant de modèle** dans le brouillon 2 (recherche faite : aucune occurrence). Lettre du modèle laissée à la mère (point inchangé). Aucune lecture interdite employée ; la déclaration du rédacteur du brouillon 2 est celle d'un rédacteur qui n'a rien ouvert sous `diag/`, `runs/`, `donnees/` ; je ne peux pas le vérifier, je n'ai rien ouvert non plus.
- **Calcul de la borne de P14** : par carte, 0,09 / 480 = 0,0001875 c ; sur 24 cartes 0,0045 c ; 39 / 500 = 0,078 donc c ≈ 17,3 : arithmétique juste, mais l'inférence ne l'est pas (m4').

## 3. Défauts majeurs (exigent une correction avant scellement)

**M1'. Annexe A (serrage) toujours non écrite.** Le tour 1 (M5) disait : « un texte scellé ne peut pas renvoyer à une annexe inexistante ; la contre-lecture 2 doit pouvoir la lire ». Le brouillon 2 remplace « annexe à écrire » par « annexe A à écrire avant la contre-lecture 2 » : la promesse est plus précise, mais la contre-lecture 2 a lieu **sans** l'annexe. Sans la distance des voisines, la variance attendue de Λ au plafond et la borne basse attendue de la mutation « bloc suivant », je ne peux ni confirmer que le serrage a un pouvoir (mutation tuée) ni qu'il ne fausse-alerte pas ; le même compte conditionne le « pouvoir » de la lecture (5) (M2-d). À écrire, puis une vérification courte de cette seule annexe par un lecteur neuf (tour 3 limité) : aucun scellement avant.

**M2'. Annexe B (dimensionnement des doses) toujours non écrite.** Même situation pour m10. Le risque « hors de la zone utile » est celui qui perdrait 10 à 12 heures ; le texte avoue lui-même que la dose 1,0 de V2, V3, V5 est « proche du plafond pour F » (≈ 13 nats pour 6,17 nécessaires). Écrire le compte et la couverture attendue de F par famille ; si la couverture attendue de F en « réplique » ou « porteuse unique » dépasse 0,95 en moyenne, les doses sont à revoir **avant** scellement (c'est une décision de la rédaction, non un résultat), et P1, P2, P9 doivent être relus avec elle.

**M3'. Questions ouvertes dans un texte à sceller.** Q-1 (juge candidat), Q-2 (3 000 ou 2 500 générations) et Q-3 sont encore écrites comme questions, avec la ligne de la liste d'arrêt et les lignes du Coût qui en dépendent. Un préenregistrement scellé ne porte pas de question. Hors de la compétence de la rédaction : la mère doit trancher (§ 6) ; ensuite, retirer ou garder chaque ligne, et, si Q-1 est retenue, écrire comment le juge candidat consomme le flux de chaque carte (tirer 800 issues d'un coup puis les lire par blocs ne donne les mêmes valeurs que 32 tirages de 25 que si la consommation du générateur est identique).

## 4. Remarques mineures (corrections à faire ; couples ci-dessous)

- **m1'. Lecture (5) « sans pouvoir » et étage 1.** M2-d dit qu'une lecture déclarée « sans pouvoir sur le banc réel » est rapportée sans critère ; le Seuil et l'étage 1 continuent de la compter comme un défaut (« une borne basse > 1 ... des 7 de la lecture (5) »). Dire laquelle l'emporte. Proposition : une alerte de la lecture (5) compte à l'étage 1 sauf si la lecture est déclarée sans pouvoir ; dans ce cas elle est rapportée, avec l'audit écrit. Couples C1 et C2.
- **m2'. Seuil des 12 heures ambigu.** L'étape 1 dit « s'il annonce plus de 12 heures **pour le jeu** » ; la règle ajoutée dit « durée projetée = somme des générations × durées moyennes **plus** contrôles, essai E1, jeu synthétique, serrage » et que « la décision ne dépend que de cette durée ». Le seuil s'applique-t-il au jeu seul ou à la durée projetée totale ? Avec un total attendu de 10 à 12 heures, la différence est celle d'une décision sur deux. Proposition : le seuil de 12 heures s'applique à la durée projetée (définie ensuite). Couple C3.
- **m3'. Serrage : prononcé manquant.** (i) Une mutation « bloc suivant » non tuée donne « pas de jeu » à la liste d'arrêt, mais aucun étage de la table ne dit ce qui est prononcé ; (ii) une alerte sur une règle saine (fausse alerte possible jusqu'à environ 14 %, de la lettre de m5) range le prononcé à l'étage 1 « garantie mise en défaut », alors que le texte ajoute qu'elle reçoit audit et nœud de la mère : l'étage 1 est lu comme définitif, l'audit comme ouvert. Dire : « pas de jeu ; aucun prononcé ; audit écrit ; nœud de la mère » pour les deux cas du serrage, l'étage 1 gardant les défauts constatés sur le jeu. Couple C4.
- **m4'. P14 : l'inférence de la borne de Markov est fausse en général.** « les promotions à plusieurs cartes ne la changent guère » : pour une promotion de k cartes, la borne de Markov donne la même valeur 0,0045 c **pour chaque k**, et la réunion sur k = 1 à 24 la multiplie jusqu'à 24 (0,108 c, soit c ≥ 0,7 pour 39 sur 500) ; « c de l'ordre de 17 ou plus » n'est donc une borne basse que pour une promotion isolée. P14 étant rapporté sans critère, l'enjeu est faible, mais la prédiction chiffrée ne doit pas afficher une borne qu'elle n'a pas. Couple C5.
- **m5'. m7 : attribution ambiguë.** « avec les bornes basses de C_A − C_F et, pour « dense », de R_A − R_F » : « vide » n'a **ni couverture ni rappel** (aucune porteuse) ; seule « dense » en a. Couple C6.
- **m6'. Colonnes de réfutation de P7 et P8.** m8 a ajouté le critère « borne basse de FP_A seul > 0,05 » en « dense » et en « vide » ; la colonne « ce qui la réfute » de P8 (et de P7 pour « dense ») n'en parle pas, et P8 prédit pourtant « FP_A ≤ 0,05 ». Aligner. Couples C7 et C8.
- **m7'. Crédits et hors crédits.** Le devis doit les séparer ; le texte dit « 0 dollar » sans distinction. Couple C9.
- **m8'. Renvoi non défini.** « [BANC-v1] annexe A » n'est défini nulle part dans la liste des documents qui font foi ; c'est l'annexe A de [T] (information en nats par dose). Couple C10.
- **m9'. Essai à blanc et code (information, non bloquante).** L'essai à blanc se joue après le scellement de l'addendum d'empreintes ; si l'essai révèle un défaut du code, un nouvel addendum d'empreintes est nécessaire ; le texte pourrait dire que la racine (empreinte du texte) ne change pas dans ce cas, et que les tirages de l'essai à blanc (racine d'essai) ne sont jamais conservés. **Facultative**, non demandée.

## 5. Couples « ancien → nouveau » (chaque « ancien » est présent une seule fois dans le brouillon 2, vérifié par programme)

**C1** (m1')
- ancien : ```ou des 7 de la lecture (5) ;```
- nouveau : ```ou des 7 de la lecture (5) (sauf si elle est déclarée « sans pouvoir sur le banc réel » : voir Métrique) ;```

**C2** (m1')
- ancien : ```une borne basse de moyenne de Λ au temps d'arrêt, sorte « voisines du monde », > 1 dans un bras (sept intervalles) = défaut ;```
- nouveau : ```une borne basse de moyenne de Λ au temps d'arrêt, sorte « voisines du monde », > 1 dans un bras (sept intervalles) = défaut, sauf si la lecture est déclarée « sans pouvoir sur le banc réel » (alors rapportée sans critère, avec l'audit écrit) ;```

**C3** (m2')
- ancien : ```s'il annonce plus de 12 heures pour le jeu, les familles```
- nouveau : ```si la durée projetée (règle ci-dessous, contrôles et serrage compris) dépasse 12 heures, les familles```

**C4** (m3')
- ancien : ```| serrage : une règle saine à borne basse > 1 ; ou mutation « bloc suivant » non tuée | pas de jeu (défaut du côté sûr) |```
- nouveau : ```| serrage : une règle saine à borne basse > 1 ; ou mutation « bloc suivant » non tuée | pas de jeu (défaut du côté sûr) ; aucun prononcé de la table ; audit écrit et nœud de la mère |```

**C5** (m4')
- ancien : ```les promotions à plusieurs cartes ne la changent guère)```
- nouveau : ```ordre de grandeur pour une promotion isolée seulement : pour k cartes promues ensemble la même borne vaut pour chaque k et la réunion sur k jusqu'à 24 la multiplie jusqu'à 24, donc ce chiffre n'est pas une borne basse sur c ; rapporté sans critère)```

**C6** (m5')
- ancien : ```avec les bornes basses de C_A − C_F et, pour « dense », de R_A − R_F ;```
- nouveau : ```pour « dense » seulement (« vide » n'a ni couverture ni rappel), avec les bornes basses de C_A − C_F et de R_A − R_F ;```

**C7** (m6')
- ancien : ```| FP_A ≤ 0,05 par génération ; borne haute de FP_A − FP_F ≤ +0,05 | seule sorte fausse promue : copies par morceaux, § 3.4 | borne basse de FP_A − FP_F > +0,02 | 0,5 |```
- nouveau : ```| FP_A ≤ 0,05 par génération ; borne haute de FP_A − FP_F ≤ +0,05 | seule sorte fausse promue : copies par morceaux, § 3.4 | borne basse de FP_A − FP_F > +0,02 ; ou borne basse de FP_A seul > 0,05 | 0,5 |```

**C8** (m6')
- ancien : ```| ≤ 0,01 par génération dans chaque bras ; borne haute de FP_A − FP_F ≤ +0,05 | 0,0013 à 0,004, § 1 et § 3.4 | borne basse de FP_A − FP_F > +0,02 | 0,7 |```
- nouveau : ```| ≤ 0,01 par génération dans chaque bras ; borne haute de FP_A − FP_F ≤ +0,05 | 0,0013 à 0,004, § 1 et § 3.4 | borne basse de FP_A − FP_F > +0,02 (et, pour « dense », borne basse de FP_A seul > 0,05) | 0,7 |```

**C9** (m7')
- ancien : ```**Processeur seul, 0 dollar ; aucun devis n'est nécessaire.**```
- nouveau : ```**Processeur seul, 0 dollar (crédits : 0 ; hors crédits : 0) ; aucun devis n'est nécessaire.**```

**C10** (m8')
- ancien : ```comme [BANC-v1] annexe A)```
- nouveau : ```comme l'annexe A de [T])```

Pour M1', M2', M3' : pas de couple (annexes à écrire, questions à trancher par la mère) ; la rédaction du brouillon 3 doit les écrire en fichier neuf.

## 6. Points pour la mère

- **À trancher avant le brouillon 3** : Q-1 (juge candidat ; ma lecture : le gain en valeur de l'essai de concordance est réel mais reste une pièce d'adoption plus que de validation ; recommandation du rédacteur inchangée, je ne tranche pas), Q-2 (3 000 ou 2 500) et Q-3 ; le texte ne peut en porter aucune ouverte.
- **Annexes A et B à faire écrire** ; c'est un compte sans donnée du juge (A : variance de Λ, distance des voisines, pouvoir de la mutation ; B : information en nats par dose). Le risque réel est que le serrage soit sans pouvoir (mutation non tuée) ou que la dose 1,0 sorte de la zone utile ; les deux se voient **avant** le jeu et coûtent des minutes, pas des heures.
- **Lettre du modèle** des rédacteurs des brouillons 1 et 2 : à inscrire au registre (le rédacteur du brouillon 2 est du même modèle que le contre-lecteur 1, le rapport l'a dit ; je suis de modèle C, neuf).
- **Pas de mot de Lazar nécessaire** pour ce texte (processeur, 0 dollar, aucun écart à un texte scellé, rien d'adopté) ; le nœud d'adoption reste le sien, avec la levée de la condition « dénominateur fixe ».
- **Tâche d'attente** à prévoir avant le jeu (le run invalide est mort d'un redémarrage du conteneur).
- **Étape suivante** : brouillon 3 (couples C1 à C10 appliqués par programme, annexes A et B écrites, questions tranchées), puis un tour 3 qui relit les seules parties touchées et les deux annexes.

## 7. Déclaration

Rôle : contre-lecteur neuf (R2), modèle C ; texte des brouillons du modèle A. Heures (`date -u`) : début 01:37Z ; lectures et `diff` entre 01:38Z et 01:40Z ; rédaction ensuite ; scellement : heure du compagnon. Jamais ouvert : voir en-tête. **Incidents de ma main** : (a) un premier appel du validateur `prereg.problemes` avec le mauvais type d'argument a levé une exception, sans effet (lecture seule) ; rejoué correctement, liste vide ; (b) une copie du brouillon 1 a été posée dans le dossier temporaire de la session (`/tmp/claude-0/x.md`, hors dépôt, contraire à la consigne d'utiliser le bloc-notes de session) et une autre dans le bloc-notes pour l'essai `patch --dry-run` ; aucune n'est dans le dépôt, aucune ne contient de valeur interdite ; (c) aucun fichier existant modifié, aucun commit, aucune machine, aucun appel réseau.

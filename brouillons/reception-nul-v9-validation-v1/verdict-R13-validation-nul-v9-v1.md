# Verdict R13 — validation décisive du nul v9 (banc des tricheurs v9), lecture neuve, version 1

**Issue qui s'applique (mots du texte scellé, section 7, issue 2, premier étage) : « puissance perdue » — « aucune ligne fatale non tenue, une perte au moins non tenue » ; « les 18 lignes fatales sont “tenues” et les 3 artefacts “tenus” », « la règle de P1b ne joue pas », donc « le v9 ferme les lignes, au prix mesuré sur la ligne nommée » (I02) ; « décision de Lazar : accepter le prix (le v9 devient le nul du juge, la description publique dit le prix) ou chercher un nul moins coûteux (version nouvelle) ».**

L'issue écrite par le code (`lecture.issue`) est la même ; mon recalcul depuis les comptes bruts la retrouve ; l'audit (R4, A6) n'a trouvé aucun défaut qui change l'issue, et je n'en ai trouvé aucun en le vérifiant par échantillon. Le v9 n'est **ni « confirmé » ni « validé sur la classe du banc »** (mention réservée à l'issue 4) ; il n'entre pas en production ; rien n'est revendiqué publiquement avant deux réponses de Lazar (prix ; sens de « rien au-delà de l'archive »).

Lecteur : neuf (R13). Je n'ai écrit ni le nul v9, ni son banc, ni son préenregistrement ou ses brouillons, ni la contre-lecture, ni la vérification courte, ni l'audit. Travail du 3 novembre 2026, de 06:11 à 06:20 UTC (temps universel coordonné, heures relevées par `date -u`). Ce fichier est le seul que j'écris hors de mon bloc-notes `/home/claude/scratch/verdict-nul-v9/` ; aucun commit, aucun compagnon `.sha256`, aucun fichier existant modifié, rien sous `donnees/`, aucun `git fetch`, `checkout` ni `stash` (git appelé en lecture seule avec `GIT_OPTIONAL_LOCKS=0`, par `show`, `log`, `rev-parse` et `diff-tree` entre commits, jamais sur l'index), aucun réseau, aucun modèle, `nice -n 10`, aucune course du banc.

## 0. Légende

| Terme | Sens |
|---|---|
| α | 0,05, taux d'erreur toléré ; seuil de richesse 1/α = 20, log 20 = 2,9957 |
| log W max | plus grand logarithme de la richesse sur les 8 instants lus (25, 50, …, 200) |
| promotion | log W ≥ log 20 à un instant lu et, pour une fille, gain final ≥ 2δ₀ = 0,02 nat par tirage sur la meilleure enveloppe |
| v8 apparié | la même fiche, sur les mêmes issues, jugée par la bibliothèque v9 privée de ses membres par morceaux (= nul v8) |
| perte appariée | part des 1 000 répétitions promues sous le v8 apparié et non sous v9 |
| Clopper-Pearson | bornes exactes d'une proportion, unilatérales à 95 % |
| Holm | correction descendante pour plusieurs tests, niveau familial 0,05 |
| H1 à H4, P1 à P7, A1 à A6 | hypothèses, prédictions et déclencheurs d'audit du texte scellé (sections 3, 4, 8) |
| VC1 à VC8, AU1 à AU12 | réserves de la vérification courte et de l'audit, telles que numérotées là-bas |

## 1. Pièces et sceaux (vérifiés par moi)

- Texte scellé `orchestrator/prereg/preenregistrement-validation-nul-v9-v1.md` : sha256 `54c5713d07f61b7f2bb3dd8218f4bca881a044a2b11508015db5e727d62c18fb` sur disque, égale au compagnon et à `git show 66dbcf1:` (commit du 2 novembre 2026, 23:20:16 UTC). Lu en entier (672 lignes).
- Bloc de la section 12 : `sha256sum -c` des 14 lignes sur l'arbre de `orchestrator/` : 14 OK ; `git diff-tree 66dbcf1 HEAD` (`eaa74ca`) sur ces 14 fichiers : vide. Manifeste : `code_du_banc_sha256` égal au bloc ; `entropie_racine` = entier de l'empreinte du texte (recalculé, ≥ 2⁶⁴ ; stocké comme chaîne de caractères) ; mode décisif, 31 lignes, 1 000 répétitions, 2 processus, durée gelée 172 800 s ; Python 3.13.18, numpy 2.5.3, pôle 0.7.0.
- Réception `brouillons/reception-nul-v9-validation-v1/` : `sha256sum -c` conforme pour `manifeste.json` (`e1594656…`), `banc-tricheurs-v9.json` (`0cd66bad…`), `sortie-erreur-course-v1.txt` (`87a7cc30…`), `depart-utc-v1.txt` (`f9f5c786…`), `LISEZMOI-reception-v1.md` (`312b7a8a…`). Audit `audit-validation-nul-v9-v1.md` : `e745db58aaab476194e9e40970dd9c221e85c7cbf135fba265b2c7c6e0dd2290`, lu en entier ; vérification courte, lue en entier ; verdict du v8 (modèle de forme), lu en entier.
- Le fichier dit « sortie d'erreur » est, champ par champ, le résumé de fin de course (issue, statuts, taux, pertes, durée 6 020,8 s) : égal au rapport scellé (vérifié par moi ; AU3).

## 2. Recalcul indépendant (`recalcul_verdict_v1.py`, sortie `sortie-recalcul-verdict-v1.txt`)

Écrit d'après la seule section 6 du texte scellé, sans lire le code du banc ; il ne lit que `promues`, `repetitions`, `apparie_v8.promues`, `apparie_v8.perdues`, `log_w_max_max` et `dominants` ; lois exactes par scipy 1.18.1 (binomiale pour les valeurs p, bêta pour Clopper-Pearson) ; Holm réécrit. Puis il compare à `lecture.*`. **Aucun écart** sur les 18 statuts fatals, les 18 valeurs p, les 3 artefacts, les 5 pertes, les pertes observées, l'issue, les audits A1 à A5. Lignes recalculées par moi (la consigne en demandait quatre, dont I02 et une fatale) : les 18 fatales, les 3 artefacts, les 5 pertes.

**Fatales (H1, H4 ; famille de 18).** 0 promotion sur 1 000 sur chacune ; valeur p de « taux ≥ α » : 0,95¹⁰⁰⁰ = 5,29·10⁻²³, sous le seuil de Holm le plus strict (0,05/18 = 0,00278) : 18 « tenue ». Borne haute de Clopper-Pearson 0,00299 par ligne. Tables de la section 6 retrouvées exactement (31 … 38 ; 71 … 63). Exemple détaillé, M01 (le monde W2 de l'attaque, H4) : 0/1 000 sous v9, 986/1 000 sous le v8 apparié, log W max −5,1·10⁻¹⁰, membre `morceaux:sous_population` dominant dans 991 répétitions.

**Artefacts (H3).** Seuil recalculé : 63 promotions (borne basse > α). T01|v1 411 (borne basse 0,385), M01 v8 apparié 986 (0,978), M02 v8 apparié 972 (0,962) : 3 « tenue ».

**Pertes appariées (H2 ; famille de 5 ; marge 0,05).** Aucune répétition gagnée sur aucune des 30 lignes v9 (monotonie).

| ligne | v8 apparié | v9 | perdues | perte d | Clopper-Pearson 95 % | p « d ≥ 0,05 » (rang ; seuil) | p « d ≤ 0,05 » (rang ; seuil) | statut |
|---|---|---|---|---|---|---|---|---|
| fille neuve | 985 | 947 | 38 | 0,038 | [0,0286 ; 0,0495] | 0,0434 (2 ; 0,0125) | 0,969 | non jugeable |
| fraîche neuve | 976 | 970 | 6 | 0,006 | [0,0026 ; 0,0118] | 1,7·10⁻¹⁵ (1 ; 0,01) | 1 | **tenue** |
| I01 | 863 | 820 | 43 | 0,043 | [0,0330 ; 0,0551] | 0,173 (3 ; 0,0167) | 0,863 | non jugeable |
| I02 | 486 | 381 | 105 | 0,105 | [0,0894 ; 0,1223] | 1 | 1,6·10⁻¹² (1 ; 0,01) | **non tenue** |
| F03 | 753 | 707 | 46 | 0,046 | [0,0356 ; 0,0584] | 0,311 (4 ; 0,025) | 0,739 | non jugeable |

Holm « tenue » : fraîche neuve rejetée au rang 1, fille neuve (0,0434 > 0,0125) arrête ; Holm « non tenue » : I02 rejetée au rang 1 (borne basse au niveau 0,01 : 0,0836 > 0,05), F03 arrête. Tables retrouvées (34, 34, 35, 36, 38 ; 68 au rang 1).

## 3. Issue selon la section 7, dans l'ordre

1. « trou » : non (aucune fatale non tenue). 2. « puissance perdue » : **oui** (I02 non tenue). Deux étages : les 18 fatales « tenues », les 3 artefacts « tenus », la règle de P1b ne joue pas (T05s log W max −0,0058, T09g −0,0059, 0 promotion ; seuil +0,25) → **premier étage**. 3 à 5 : non atteints. Le code dit la même chose ; `lecture.audits` = [], `issue_suspendue_par_audit` = faux.

**Audits (section 8).** A1 à A5 : non déclenchés (recomptés : 0 promotion sur les 17 lignes refusées par construction ; log W max des classes linéaire et par morceaux ≤ −3,1·10⁻¹⁰ ; artefacts dans les bornes ; membres par morceaux dominants de 912 à 1 000 sur 1 000 sur M01 à M07). **A6 : déclenché par l'issue** (« puissance perdue ») ; l'audit écrit (R4) a cherché un défaut et n'en a trouvé aucun ; je retiens sa lecture 2 de l'ambiguïté AU7 : l'issue était suspendue jusqu'à l'audit écrit, elle est lue maintenant, note jointe (ce fichier). Les deux lectures donnent la même issue.

**Ce que j'ai vérifié de l'audit par échantillon.** Ses bornes, valeurs p, tables, statuts et issue : retrouvés par mon script indépendant. Ses empreintes de scripts (7 fichiers sur 20, recalculées) : égales. Ses rejeux de T12a et d'I02 : sorties relues (`rejeu-*/sortie.txt`, `sortie-complements-rejeu-v1.txt`) ; elles disent ce que l'audit rapporte (rejeu identique au rapport scellé ; I02 : 105 perdues restent non promues avec la richesse « optimiste », écart résiduel ≤ 10⁻³ nat ; T12a : 2 franchissements sur 1 000, marge jamais atteinte, gain maximal −0,0048). Je n'ai pas rejoué ces lignes. Sa constante morte (AU8) : vérifiée, ligne 106 du banc gelé. Sa conformité au plan (commande, entropie, code gelé, durée) : revérifiée par moi sur le manifeste et le dépôt.

**Prédictions (elles ne décident pas) :** P1a, P1b, P1c, P2, P3, P4, P5, P6, P7 toutes tenues (recalculées) ; elles ont été écrites après les lectures préalables L1 à L5 (déclaré) et n'ajoutent aucune preuve.

## 4. Ce qui est établi, ce qui ne l'est pas

**Établi sur cette course** (mondes synthétiques du banc : 3 issues, 2 traits gaussiens, 2 sous-populations ; filles : 50 tirages de calibrage puis 200 ; fiches sans parent : 200 tirages ; lecture aux instants 25 à 200 ; α = 0,05 ; 1 000 répétitions par ligne ; graine = empreinte du texte scellé) :
- le nul v9 ne promeut aucune des 18 lignes fatales (0/1 000 chacune ; borne haute 0,30 %, 0,59 % au niveau de Holm le plus strict), dont les 7 tricheurs par morceaux M01 à M07 et le monde W2 de l'attaque (M01, H4) ; aucune de ces promotions ne vient du certificat ni du code (A1, A4 non déclenchés ; rejeux de l'audit) ;
- le banc a des dents : sous le v8 apparié, les mêmes scénarios sont promus à 98,6 % (M01), 97,2 % (M02), 96,9 % (M03), 89,7 % (M04), 43,3 % (M05), 94,9 % (M06), 57,3 % (M07) ; T01|v1 à 41,1 % ;
- le prix en puissance appariée : voir section 5 ; sur I02 il est établi au-dessus de la marge.

**Non établi, non revendicable :**
- « confirmé » et la mention « validé sur la classe du banc (section 11) » : réservées à l'issue 4 ;
- le prix sur trois des cinq lignes (fille neuve, I01, F03 : ni sous ni sur la marge) ;
- tout ce qui est hors de la classe du banc (section 11) : banque réelle, multiplicité entre fiches, autres espaces, mondes avec mémoire, traits non finis, proposeur qui lit le juge (objet de l'attaque v4) ; la marge de Newton des membres log-linéaires n'est éprouvée qu'à −0,0058 près ;
- les lignes mesurées ne disent rien de la validité : T07 0,9 %, H01 86,0 %, H02 14,5 %, H03 92,8 %, H05 9,0 % sont des taux de fausse promotion sur des trous déclarés du v9 ; H04 23,6 % est la promotion d'un bruit propre à chaque morceau, « neuf » seulement selon le sens choisi (à confirmer) ; T12b 84,0 % est de la puissance sur une nouveauté vraie ;
- T12a : son zéro vient de la marge des filles autant que de Ville (réserve 6 ci-dessous).

## 5. Le prix pour Lazar (cinq lignes de perte de puissance, marge 0,05 sur chacune)

| ligne | monde | puissance v8 apparié → v9 | perte appariée | Clopper-Pearson 95 % | contre la marge |
|---|---|---|---|---|---|
| fraîche neuve | loi neuve forte, sans parent | 0,976 → 0,970 | **0,006** | [0,003 ; 0,012] | **établie sous la marge** |
| fille neuve | A sur g = 0, loi neuve ailleurs | 0,985 → 0,947 | 0,038 | [0,029 ; 0,050] | non jugeable (borne haute au niveau de Holm 0,054) |
| I01 | interaction forte des deux traits | 0,863 → 0,820 | 0,043 | [0,033 ; 0,055] | non jugeable |
| F03 | loi neuve faible | 0,753 → 0,707 | 0,046 | [0,036 ; 0,058] | non jugeable |
| I02 | interaction faible des deux traits | 0,486 → 0,381 | **0,105** | [0,089 ; 0,122] (borne basse au niveau de Holm 0,084) | **établie au-dessus de la marge** |

Lecture : sur une loi vraiment neuve et forte, le v9 ne coûte presque rien (≤ 1,2 point) ; sur les trois lignes intermédiaires, le prix observé (3,8 à 4,6 points) est au voisinage de la marge et la course ne tranche pas ; sur l'interaction faible, il coûte un cinquième de la puissance du v8 (10,5 points sur 48,6), par le mécanisme annoncé (section 3 du texte et P4 : un membre à seuil sur un trait suit en partie l'autre signe par les survivantes ; dominants finals des 105 perdues : membres à seuil dans 104 cas, d'après l'audit). C'est l'issue que P7 annonçait (perte ≈ 0,11) sous une marge choisie en sachant qu'elle la prédisait (annexe A ; R3). La décision qui revient à Lazar : accepter ce prix (le v9 devient le nul du juge, sa description publique dit les cinq pertes avec leurs bornes, AU10) ou demander un nul moins coûteux (v10, préenregistrement nouveau). Ce verdict ne recommande rien sur le prix.

## 6. Réserves (une ligne chacune ; aucune ne change l'issue)

Réserves de l'audit que je retiens (numéros de l'audit) :
1. AU1 — Code de sortie non capturé (`nohup … &`) ; déduit 0, non observé ; le texte dit qu'il ne décide pas.
2. AU2 — Section 14, point 6 : essais et mutations non rejoués entre la poussée (23:20:18) et le départ (23:20:38) ; joués juste avant sur un code identique et rejoués sur l'arbre scellé pendant la course ; même écart que la réserve R2 du v8 : à consigner comme écart de procédure récurrent, à corriger dans le prochain texte (jouer les essais après la poussée, ou dire que c'est avant).
3. AU3 — Le fichier « sortie d'erreur » est la sortie standard ; redirection non consignée ; le flux d'erreur vrai est vide ou perdu.
4. AU4 — Manifeste sans date ni commit (R9 demande le commit) ; retrouvés par les horodatages et le dépôt ; à ajouter au manifeste des prochains bancs.
5. AU5 — Charge concurrente pendant la course (course factice d'A1-v3.1, essais, commits hors des 14 gelés) : temps seulement ; déterminisme prouvé par les rejeux au bit près.
6. AU6 — T12a : zéro tenu par la marge des filles (jamais atteinte, gain maximal −0,0048) autant que par Ville (2 franchissements sur 1 000, borne haute 0,63 %, sous α et sous P1c) ; à écrire partout où T12a est citée (réserve R1 du v8, toujours non portée au texte du v9).
7. AU7 — A6 n'est pas calculé par le code ; je l'ai appliqué moi-même (section 3) ; à écrire dans le prochain texte (A6 suspend l'issue jusqu'à l'audit écrit, par le lecteur R13).
8. AU8 — `SEUIL_ECART_RESIDUEL` (« audit A7 ») : constante morte du banc gelé, aucun A7 au texte ; écart résiduel mesuré par l'audit sur I02 ≤ 10⁻³ nat ; à retirer ou à rattacher à un audit écrit.
9. AU9 — `lecture.predictions` ne code ni « log W ≤ 10⁻⁶ » (P1a) ni « ≤ +0,25 » (P1b) ; vérifiés à la main (par l'audit et par moi).
10. AU10 — Le prix dépasse « la ligne nommée » : décision et description publique doivent porter les cinq pertes avec leurs bornes (section 5 ci-dessus).
11. AU11 — L'audit a rafraîchi le cache `.git/index` du clone public (index égal à `HEAD`, rien de suivi changé) ; écart à la lettre « aucun fichier existant modifié », sans effet.
12. AU12 — Rejeux diagnostiques sur les graines décisives : **admis** par moi — la section 8 (A5) prescrit elle-même de recompter « sur les mêmes graines », le verdict du v8 l'a fait ; hors de `principal`, après le scellement de la sortie, sans dossier de sortie ni lecture gelée, aucun nombre des rejeux n'entre dans l'issue ; ce n'est pas une seconde course décisive au sens de la section 5.

Réserves de la vérification courte, retenues telles quelles (VC1 à VC8) : VC1 phrase inexacte du paragraphe de scellement (« aucun de ces noms n'est lu par le banc » : `description()` est lue pour le manifeste seulement) ; VC2 renvoi « section 4 » au lieu de 5 pour la graine ; VC3 disjoint « promotion sous v9 sans promotion sous v8 » de la garde de monotonie jamais éprouvé seul ; VC4 gardes sans artefact (richesse non finie, arguments < 1, durée ≤ 0, entropie < 2⁶⁴), titre de la section 9 trop large ; VC5 essais de la description publique épinglent le contenu en partie ; VC6 artefact de durée : « rien d'écrit » vérifié sur le seul rapport ; VC7 « trois fichiers existants modifiés et seulement eux » : phrase limitée à la validation (le commit `516feca` touche aussi l'attaque v4) ; VC8 fragments de G1 à G5, L1, L2, C5 non vérifiables (script du contre-lecteur disparu). Aucune n'a d'effet sur les nombres ; l'écart à R2 déclaré au texte scellé est levé par cette vérification, faite avant toute lecture de la sortie.

Réserves qui sont les miennes :
13. **La marge (a) est elle-même un défaut sous 48 heures** (R-1278, 2 novembre 18:37 UTC ; annexe A : « défaut de Lazar sous 48 heures ») ; le texte scellé la porte et le banc la code ; elle fait foi pour cette course quoi que Lazar dise ensuite : toute autre marge serait un texte nouveau et une course nouvelle, jamais une relecture de celle-ci (R3, annexe A).
14. Le « bruit commun aux morceaux » (sens de « rien au-delà de l'archive ») est aussi un défaut non confirmé ; le texte en fait un nœud de revendication **sans défaut** (section 14, point 2) : le délai de 48 heures ne vaut donc pas ici ; une réponse contraire de Lazar ne corrige pas ce verdict, elle ouvre un nul v10.
15. Trois pertes « non jugeables » sur cinq : ce n'est pas un « non concluant » de l'issue (elle est conclusive), mais le prix soumis à Lazar est incertain d'environ ± 1 point sur fille neuve, I01 et F03 ; 1 000 répétitions ne suffisent pas à trancher une perte à 4 points contre une marge à 5 ; si Lazar veut ces trois prix établis, c'est une course nouvelle (préenregistrement nouveau, répétitions ≥ 4 000 environ), pas un complément sur la même graine (section 7, issue 5).
16. L'issue, le statut et le prix ont été consignés par le directeur dans `registres/decisions.md` (R-1306) à partir de l'audit, avant ce verdict ; conforme à l'ordre de la section 14 (point 7 : audit écrit, puis verdict), mais aucune phrase de registre ne doit dire « validé » ; seule la formule de l'en-tête de ce fichier s'applique.
17. L'entropie racine est stockée en chaîne de caractères dans le manifeste (entier exact de 77 chiffres) ; sans effet, à noter pour qui la relit comme nombre flottant.

## 7. Portée et usage

- **Aucune revendication publique** sur le nul v9 avant la réponse explicite de Lazar sur le sens de « rien au-delà de l'archive » (section 2, dernier point ; section 14, point 2) ; je n'en trouve aucune dans `registres/decisions.md` au 3 novembre 06:15 UTC (R-1278 la porte comme défaut « à confirmer »). Publier est de plus un nœud de Lazar ; rien n'est publié (dossier de sortie non committé).
- **Nul de production = v8** jusqu'à la décision de Lazar sur le prix (section 7, dernier alinéa ; décision du 2 novembre) ; le brancher demanderait, dans l'ordre : prix accepté, sens confirmé, entrée v9 du cycle dans un fichier neuf, décision de Lazar (nœud « modification d'hypothèse ou de revendication »).
- Toute phrase qui cite cette course dit : « “puissance perdue”, premier étage : les 18 lignes fatales et les 3 artefacts tenus ; perte appariée établie au-dessus de la marge sur I02 (10,5 points), sous la marge sur fraîche neuve (0,6 point), non jugeable sur fille neuve, I01, F03 (3,8 à 4,6 points) » — jamais « validé », jamais « 27 tricheurs » (correction 2 du texte : 31 lignes sur 30 scénarios pour le v9).
- Ce verdict est soumis à Lazar pour GO (R13). Il n'autorise aucune dépense.

## 8. Ce que l'issue change pour l'attaque v4 (GO-2026-11-02-22)

- Le GO-22 (200 USD, échéance 16 novembre) conditionne l'attaque v4 à « après la validation hors ligne du v9 sous son texte scellé » ; la section 14, point 8, dit « ensuite seulement » ; la section 7 dit que l'attaque « éprouve le v9 hors production ». **La condition de fait est remplie** : la course est faite, scellée, auditée, lue ; la validité sur la classe du banc est établie au premier étage (18 fatales, 3 artefacts, A1 et A4 non déclenchés), et c'est elle que l'attaque éprouve, pas le prix. Le mot « validation » du GO-22 ne doit toutefois pas devenir « validé » dans le texte de l'attaque : ce texte cite l'issue par sa formule exacte (section 7 ci-dessus) et l'empreinte de ce verdict.
- **Ce que l'attaque v4 doit porter en conséquence** : (i) la description publique du nul v9 donnée au proposeur (`description_publique()`) inchangée, plus le prix mesuré (les cinq pertes et leurs bornes) si la description « dit le prix » après la décision de Lazar — avant cette décision, l'attaque teste le nul tel qu'il est écrit, sans phrase de prix ; (ii) sa lecture distingue une promotion dans un trou déclaré (H01 à H05 : l'archive recombinée en profondeur 2, en escalier, en produit, tempérée par morceau, et le bruit propre à chaque morceau) d'une promotion dans la classe couverte ; les taux mesurés ici (H01 86 %, H03 93 %, H04 24 %, H02 15 %, H05 9 % sous v9) sont le repère chiffré de ce qu'un proposeur qui lit la description peut viser sans contredire la revendication ; une promotion d'une loi de la classe couverte (section 2 du texte) serait, elle, un « trou » du v9 à chercher dans le code ; (iii) le juge « ancien » pour les dents reste v8 sur W2, conforme à M01 ici (98,6 % sous le v8 apparié).
- **Point de décision pour Lazar, à joindre au GO sur ce verdict** : lancer l'attaque v4 contre le v9 maintenant, ou après sa décision sur le prix. Si le prix est refusé (nul v10), l'attaque contre le v9 éprouverait un nul qui n'ira pas en production (200 USD dépensés sur un juge intermédiaire, mais ses résultats sur les trous déclarés resteraient utiles à un v10 qui garde les mêmes membres). Si le prix est accepté, rien ne retient l'attaque. Le texte scellé de l'attaque v4 porte lui-même la décision ; ce verdict ne la prend pas.

## 9. Scripts et empreintes (`/home/claude/scratch/verdict-nul-v9/`, sha256)

```
dfdae5a182c46fe2491bb270544387dae6f706bd0585dcc62bd9784fb9cab72f  recalcul_verdict_v1.py
3256fbce80b12c040c6f9a0ab6ce4481d7ebc23ba18d816c444e8c48ef51f66a  sortie-recalcul-verdict-v1.txt
```

Lancé par `nice -n 10 python3 -I -B` ; lecture seule des pièces citées ; rien d'écrit hors de ce dossier et de ce fichier. Contrôles sans script (ligne de commande, en lecture seule) : `sha256sum`, `sha256sum -c` du bloc de la section 12 et des compagnons de la réception, `git show`, `git log`, `git rev-parse`, `git diff-tree`, lecture des registres (`registres/go.md`, `registres/decisions.md`, `registres/etat.md`) et des sorties de l'audit. Ce fichier ne porte pas sa propre empreinte : elle est donnée avec sa remise.

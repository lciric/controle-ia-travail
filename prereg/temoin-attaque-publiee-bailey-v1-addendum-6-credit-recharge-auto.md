# Addendum 6 au préenregistrement du témoin de Bailey (`prereg/temoin-attaque-publiee-bailey-v1.md`, `fb6c2f34…`) — condition 9 de l'addendum 5 remplacée : crédit couvrant 20 tours au taux relevé, recharge automatique

13 novembre 2026, scellé après contre-lecture (R2). Session « attaquant informé » (`session_01XJ6MgnEhQMZteN9F8a1BST`),
branche `claude/compassionate-meitner-d4ryyk`. Brouillon archivé tel quel (R12) :
`brouillons/temoin-attaque-publiee-bailey-v1-addendum-6-credit-recharge-auto-brouillon1.md` (contre-lu). Le
préenregistrement et ses addenda 1 à 5 restent tels quels ; en cas de conflit, le préenregistrement prime et l'écart est
un nœud. Aucun résultat : aucune note lue.

## 1. Pourquoi
L'addendum 5 (`prereg/temoin-attaque-publiee-bailey-v1-addendum-5-relance-seule-code-v20.md`, `eb97994a…`), condition 9,
exige avant la création un crédit Vast au moins égal à B − 0,5 − D du poste, plus la consommation des autres instances du
compte pendant 45 h (≈ 65 USD), pour qu'un compte vide ne coupe jamais la relance avant la garde de dépense. Crédit
relevé : 28,66 USD (≈ 09:25Z). Proposition de Lazar, verbatim : « je ne peux pas cxrediter plus de 10 dollars, je propose
de le laisser se rechrger automatiquemet quanx il en aura besoin, j'arai lesfonds d'ici la »
(`registres/passations/2026-11-13-0929-decision-lazar-bailey-credit-recharge-auto.md`, `3d6af78f…`).

Relevés (même note) : recharge automatique configurée (seuil 5 USD, montant 5 USD, moyen de paiement présent, aucun
échec signalé) ; elle a payé le 12 novembre à 15:31Z, 21:01Z et 23:46Z, puis **rien entre 23:46Z et l'épuisement du compte
vers 04:21Z**, qui a interrompu la série 3. Cause donnée par Lazar, verbatim : « pacr e qu'il n'y avait plus de fonds sur
ma carte » (`registres/passations/2026-11-13-0937-lazar-bailey-cause-recharge-carte-sans-fonds.md`, `8664a61a…`). Vast
n'a signalé aucun échec (`billing_failed` resté faux). La recharge dépend donc des fonds de la carte ; elle n'est pas une
garantie.

## 2. Écart (condition 9 de l'addendum 5), sur la proposition de Lazar (principe : crédit limité, recharge automatique) ; seuil et texte de 9′ : calcul de la session, soumis à Lazar avec la demande du mot de lancement (condition 7). Remplacée par :
**9′.** Avant la création (relevé au plus tard une heure avant ; repris si le poste attend une offre plus d'une heure, ou
bien le poste est lancé juste après le relevé et, faute d'offre dans l'heure, arrêté par son identifiant (R10) avant un
nouveau relevé) : (i) champs `credit` et `balance` du compte, le plus bas des deux au moins égal à
S = 11 h × (max(1,7 ; c₀) + o) USD, et à 20 USD au moins, où c₀ est le taux, carte et stockage, de l'offre la moins chère
du filtre du poste v12 au relevé, et o la somme des taux facturés des autres instances du compte au relevé (carte et
stockage si elle est en marche, stockage seul si elle est arrêtée) ; (ii) recharge automatique configurée (`has_billing`
vrai, `autobill_threshold` et `autobill_amount` > 0, `billing_failed` faux) ; relevés (champs, heure, c₀, o, S)
consignés dans l'ordre de lancement. Sinon aucune création.

Calcul de 11 h : mise en place ≤ 0,75 h (mesurée : 16,3, 29,4 et 34,2 min, de la création à la fin du contrôle du juge,
conduites v6, v9 et v11, le 12 novembre ; plus ≈ 2,5 min de chargement avant le tour 0) ; 20 tours × 1 586,2 s (tour le
plus long de la première exécution, journal des durées `9ff59e4b…`) × 1,15 ≈ 10,1 h ; total ≈ 10,9 h, arrondi à 11 h.
Avec c₀ ≤ 1,7 et o ≈ 0,11 (stockage des trois instances arrêtées d'un autre chantier, à relever) : S ≈ 19,9, donc
20 USD. Taux de carte observés sur le compte : 1,2393 à 1,6404 USD/h pour le témoin (`registres/depenses.md`), jusqu'à
2,07 USD/h pour d'autres offres payées par le compte : d'où c₀ relevé, et non fixé.

**Surveillance** (sans valeur de garde) : à chaque réveil (au plus toutes les 90 minutes), la session relève `credit`,
`balance`, les paiements et o ; elle alerte Lazar si le crédit est sous 4 USD (sous le seuil de recharge : la recharge
aurait dû payer), si `billing_failed` est vrai, ou si o dépasse de plus de 0,5 USD/h le o du relevé de lancement. Le
12 novembre, le défaut de recharge n'a pas mis `billing_failed` à vrai. Un réveil manqué ou une alerte non lue (nuit)
laisse le compte se vider. Aucun arrêt par la session sur ce seul motif : la liste d'arrêt est inchangée.

## 3. Conséquence sur la lecture (aucune ligne du texte ne change)
Si le compte se vide après 20 tours complets de la relance : interruption pendant le tour e₀ (l. 338), classée comme à
l'addendum 5 (coupure de l'hôte, l. 371-372) ; run tronqué, lu comme un run de K′ = e₀ tours, interruption rapportée ;
seule la relance porte le verdict, la première exécution reste rapportée comme interrompue. Avant 20 tours (ce que le
seuil vise à empêcher) : seconde erreur, arrêt, pas de verdict, nœud (l. 371). En série 3, l'arrêt du compte a arrêté
l'instance sans la détruire (≈ 3,5 h de solde négatif) ; une suppression sous solde négatif prolongé n'est pas exclue
(note 0731, `f6e09ff5…`). La lecture passe par la reprise (lecture 38), voir le risque (d).

## 4. Ce qui ne change pas
Tout le reste de l'addendum 5 (code v20 au commit `f60c2620`, manifeste v6, conduite v13, poste v12, conditions 1 à 8
dont la condition 7 : mot direct de Lazar pour le lancement), le texte et les addenda 1 à 4.

## 5. Risques déclarés (soumis à Lazar avec la demande du mot de lancement ; son mot les accepte)
- (a) la recharge automatique a déjà fait défaut une fois (carte sans fonds, sans échec signalé par Vast) ; un nouveau
  défaut après 20 tours donne un run tronqué : puissance moindre ; verdict au régime réduit si K′ ≤ 70 (l. 332) ;
- (b) le compte est partagé avec d'autres chantiers ; une instance de carte lancée par un autre chantier après le relevé,
  pendant les ≈ 11 premières heures, peut vider le compte avant 20 tours (seconde erreur, pas de verdict, nœud) ; la
  session le relève à chaque réveil et le signale ; la demande du mot de lancement demande à Lazar qu'aucun autre
  chantier ne lance d'instance de carte sur ce compte pendant ce temps sans créditer d'autant ;
- (c) chaque recharge de 5 USD couvre ≈ 2,8 h (à 1,81 USD/h) ; la relance (≈ 29 à 33 h, ≈ 39 à 60 USD au total selon le
  taux) demande, après les 15 premiers USD d'un crédit initial de 20, ≈ 24 à 45 USD tirés sur la carte en ≈ 5 à 9
  recharges, environ une toutes les 3 h ; ce montant est donné à Lazar dans la demande du mot de lancement ;
- (d) une coupure après 20 tours n'est lue que si la reprise (lecture 38) transfère les journaux : Vast peut supprimer une
  instance arrêtée sous solde négatif prolongé (note 0731) ; au compte prudent, l'arrêt compte au taux c dans D, et la
  reprise est refusée s'il reste moins de 900 s avant B − 0,5 (≈ 15 à 36 h de solde négatif tolérées selon le moment de
  la coupure, au taux 1,34) ; le chemin « reprise d'une relance seule, puis assemblage » n'est pas éprouvé par les essais
  de l'addendum 5 (un essai sur processeur est prévu pendant le run, sans dépense ; s'il révèle un défaut, sa correction
  passe par un addendum avant toute lecture). Reprise impossible ou assemblage refusé : pas de verdict, nœud ;
- (e) le poste ne relève pas le crédit ; le nouveau relevé au-delà d'une heure dépend des réveils de la session.

## 6. Conditions de lancement
Celles de l'addendum 5, la condition 9 remplacée par 9′. La demande du mot direct de Lazar (condition 7) cite cet
addendum (chemin, empreinte), le relevé de 9′ (S, c₀, o), les risques du § 5 et le tirage attendu sur la carte (§ 5 (c)) ;
ce mot vaut décision du nœud de l'écart. Aucune instance avant le scellement de cet addendum, la condition 9′ remplie et
le mot direct de Lazar.

## Contre-lecture
Rapport (R2) : `docs/notes/reproduction-attaque-publiee-v1/contre-lecture-addendum-6-credit-bailey-v1.md`
(`dcd8102455fdd66772327e5b3fc9d99ed5d2f4f7a5390a50baea04a049fcf6c0`), contre-lecteur neuf, sur le brouillon 1 :
« scellable après corrections », aucun bloquant. Traitement : L-1 (9′ et calcul, texte du rapport) ; L-2 (durées,
taux et source de o) ; L-3 (titre du § 2, titre du § 5, § 6) ; L-4 (cause consignée dans une note neuve, `8664a61a…` ;
§ 3 : suppression non exclue) ; L-5 (surveillance, texte du rapport) ; L-6 (risque (d) ; l'essai recommandé est fait
pendant le run, sur processeur) ; L-7 (risque (c)) ; L-8 (§ 3, risque (a)) ; L-9 (risque (b)) ; L-10 (9′ : poste
arrêté faute d'offre dans l'heure ; risque (e)) ; L-11 (sans changement).

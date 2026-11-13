# Addendum 6 au préenregistrement du témoin de Bailey (`prereg/temoin-attaque-publiee-bailey-v1.md`, `fb6c2f34…`) — condition 9 de l'addendum 5 remplacée : crédit couvrant 20 tours, recharge automatique — brouillon 1

13 novembre 2026. Session « attaquant informé » (`session_01XJ6MgnEhQMZteN9F8a1BST`), branche
`claude/compassionate-meitner-d4ryyk`. **Brouillon 1 : non contre-lu (R2), non scellé.** Le préenregistrement et ses
addenda 1 à 5 restent tels quels ; en cas de conflit, le préenregistrement prime et l'écart est un nœud. Aucun résultat :
aucune note lue.

## 1. Pourquoi
L'addendum 5 (`prereg/temoin-attaque-publiee-bailey-v1-addendum-5-relance-seule-code-v20.md`, `eb97994a…`), condition 9,
exige avant la création un crédit Vast au moins égal à B − 0,5 − D du poste, plus la consommation des autres instances du
compte pendant 45 h (≈ 65 USD), pour qu'un compte vide ne coupe jamais la relance avant la garde de dépense. Crédit
relevé : 28,66 USD (≈ 09:25Z). Proposition de Lazar, verbatim : « je ne peux pas cxrediter plus de 10 dollars, je propose
de le laisser se rechrger automatiquemet quanx il en aura besoin, j'arai lesfonds d'ici la »
(`registres/passations/2026-11-13-0929-decision-lazar-bailey-credit-recharge-auto.md`, `3d6af78f…`).

Relevés (même note) : recharge automatique configurée (seuil 5 USD, montant 5 USD, moyen de paiement présent, aucun
échec signalé) ; elle a payé le 12 novembre à 15:31Z, 21:01Z et 23:46Z, puis **rien entre 23:46Z et l'épuisement du compte
vers 04:21Z**, qui a interrompu la série 3. Cause, mot de Lazar, verbatim : « pacr e qu'il n'y avait plus de fonds sur ma
carte » (message suivant, consigné ici). Elle dépend donc des fonds de la carte ; Lazar annonce qu'ils seront là
(« j'arai lesfonds d'ici la »). Elle n'est pas une garantie.

## 2. Écart (condition 9 de l'addendum 5), décidé par Lazar : remplacée par
**9′.** Avant la création (relevé au plus tard une heure avant ; repris si le poste attend une offre plus d'une heure) :
(i) crédit Vast ≥ **20 USD** ; (ii) recharge automatique configurée (`has_billing` vrai, `autobill_threshold` et
`autobill_amount` > 0, `billing_failed` faux) ; relevés consignés dans l'ordre de lancement. Sinon aucune création.

Calcul du seuil (pour que le crédit seul couvre la mise en place et 20 tours complets de la relance) : mise en place
≈ 0,75 h (amorce, mise en place, contrôle du juge : ≈ 45 min observées le 12 et le 13 novembre) ; 20 tours × 1 411,5 s
(durée moyenne des tours de la première exécution, journal des durées `9ff59e4b…`) × 1,15 (marge de la règle) ≈ 9,0 h ;
soit ≈ 9,8 h × 1,7 USD/h (au-dessus des taux observés, 1,20 à 1,64) ≈ 16,7 USD, plus les autres instances du compte
(stockage, ≈ 0,11 USD/h) ≈ 1,1 USD : ≈ 17,8 USD ; arrondi à 20 USD.

**Surveillance** : à chaque réveil (au plus toutes les 90 minutes), la session relève le crédit et les paiements ; elle
alerte Lazar si le crédit descend sous 10 USD sans paiement depuis plus de 4 heures, ou si `billing_failed` devient vrai.
Aucun arrêt par la session sur ce seul motif : la liste d'arrêt est inchangée.

## 3. Conséquence sur la lecture (aucune ligne du texte ne change)
Si le compte se vide après 20 tours complets de la relance : run tronqué, lu comme un run de K′ tours, interruption
rapportée (texte l. 338, 372). Avant 20 tours (ce que le seuil vise à empêcher) : seconde erreur, arrêt, pas de verdict,
nœud (l. 371). Un vidage du compte arrête l'instance sans la détruire (série 3) : reprise selon la lecture 38 avant toute
lecture.

## 4. Ce qui ne change pas
Tout le reste de l'addendum 5 (code v20 au commit `f60c2620`, manifeste v6, conduite v13, poste v12, conditions 1 à 8
dont la condition 7 : mot direct de Lazar pour le lancement), le texte et les addenda 1 à 4.

## 5. Risques déclarés (acceptés par Lazar en proposant la recharge automatique)
- (a) la recharge automatique a déjà fait défaut une fois (carte sans fonds, sans échec signalé par Vast) ; un nouveau
  défaut après 20 tours donne un run tronqué : puissance moindre (K′ < 72), verdict lu au régime réduit ;
- (b) le compte est partagé avec d'autres chantiers : leur consommation entame le crédit (relevée à chaque réveil) ;
- (c) chaque recharge de 5 USD ne couvre que ≈ 3 h de relance ; une relance de ≈ 30 h demande ≈ 4 à 5 recharges après
  le crédit initial.

## 6. Conditions de lancement
Celles de l'addendum 5, la condition 9 remplacée par 9′. Aucune instance avant le scellement de cet addendum, la
condition 9′ remplie et le mot direct de Lazar.

## Contre-lecture
À venir (R2).

# Journal synthétique — v3 — état au 24 octobre 2026, 19:53 UTC (v1 et v2 gardées ; heures « état au » de la v1 et de la v2 fausses : vraies 18:19 et 18:23 UTC, voir l'entrée de correction de 19:52 au journal détaillé)

Écrivain : lignée « conv-audit » ; contre-lecteur : lignée « session-depot » (section « Divergences » à sa main).
Nouvelle version = nouveau nom. Rien d'opposable (R7) : chaque fait renvoie au journal détaillé du jour et à sa pièce.
Heures : UTC lues sur l'horloge ou sur les commits ; décisions de Lazar en heure de Paris (UTC + 2 ce jour).

## 1. Où en est le programme (phase 0, instruments)

Deux expériences décisives sont prêtes à être scellées, aucune n'a tourné :
- la **confrontation d'essaims autonomes** (organismes écrits par les modèles sous un noyau fixe, juge externe, bras
  gelé apparié ; banque réelle scellée) : brouillon v6 en troisième contre-lecture ; GO « calcul » à donner par Lazar ;
- l'**étape 1 du programme gradient** (sondes conçues par les organismes sur les activations de Llama-3.1-8B-Instruct) :
  v3 du préenregistrement en écriture par session-depot, avec la phase de conception et la moisson ; coût couvert par
  GO-2026-10-24-05 (« quel qu'il soit »).
Deux petits calculs réels ont eu lieu : extraction des traits de l'étape 1 (0,29 USD) et brainstorm du lot 3 arrêté au
premier tour (1,01 USD). Bloquant commun : **crédit Gemini épuisé** (HTTP 402).

## 2. Hypothèses

### En cours
- **Confrontation** (brouillon v6, `0ce8c396…`) : H-E0 (mécanique) ; **H-E1**, seule confirmatoire — Δ = gain du bras
  adaptatif − gain du bras gelé sur le test final, moyenné sur les lignées-graines, ≥ +0,10 ; génération 0 = organisme
  issu de la phase de conception ; cohérence de signe des deux courses exigée pour « confirmé » ; H-E1 restreinte aux
  lignées auto-écrites rapportée ; H-E2 (concordance des métriques croisées, descriptive, métriques non discriminantes
  écartées) ; H-E3 (fidélité des espèces, tolérance zéro) ; H-E4 (conceptions côte à côte, descriptive) ; H-E5
  (calibration, témoin).
- **Étape 1, H-G1** (v2 de session-depot `6ae4a8b3…`, v3 en cours) : à budget d'appels égal, la lignée qui dispose de
  l'apprentissage par gradient (bras A, avec conception et moisson) bat sur le test final le même organisme de départ
  sans gradient (bras B, `--depuis A`, aucune conception) ; six paires (trois lignées auto-écrites × deux répliques) ;
  bootstrap à deux niveaux, table de lecture gelée. Puissance simulée par session-depot (non opposable) : à +0,10,
  « confirmé » 44 % ; sous effet nul, 0 %.
- **H-G2, H-G3** (étapes 2 et 3), **H-G4** (étape 2 : généralisation d'un détecteur aux familles de cas inédits
  retenues, à celles de l'autre fournisseur, aux items réels) : à préenregistrer plus tard.

### Validées
- Aucune hypothèse de recherche (aucun run décisif). Validations mécaniques : isolation des organismes et, depuis CE-02,
  de l'entraîneur (tests en root) ; bras gelé étanche ; relevé des métriques sans lecture de score ; épreuve mécanique
  des métriques ; phase de conception et moisson de bout en bout en simulation ; moisson réelle en lecture seule
  (arXiv) ; **étiquettes des traces de sabotage vérifiées par paires : 10 sur 10, banque retenue** (cinq réserves :
  étiquette et non détectabilité, même famille de modèles, 10 paires sur 40, un seul vérificateur, exemples de sabotage
  dans la consigne).

### Réfutées ou retirées (ajouts depuis la v2 en tête)
- « 3 USD par génération suffisent » : réfutée par le calcul (160 appels au pire cas : 36,8 USD) → 37 USD (CR2-02).
- « Vérifier une étiquette en lisant la trace seule » : retirée — confond étiquette fausse et sabotage indétectable →
  vérification par paires.
- « L'objectif d'entraînement écrit par l'organisme peut tourner dans le processus du noyau » : réfutée (CE-02) →
  entraîneur isolé ; sans objet pour la confrontation, qui ne sert aucun gradient (test rejoué sur `e82c341`).
- « Un bootstrap par tâche suffit » : retirée (CE-03 ; 16 à 19 % de faux « confirmé » en simulation, chiffre de
  session-depot non opposable) → deux niveaux.
- « Le bras apparié est forcément gelé » (`--depuis` exigeait `--gel`) : retirée (CE-06) → bras apparié adaptatif.
- « Fixer K rondes de conception » : retirée (Lazar, 20:42) → critère d'arrêt conçu par l'organisme, borne dure au GO.
- « Le noyau écrit le moissonneur » : retirée (Lazar, 20:32 à 20:35) → primitives au noyau, moissonneur à l'organisme.
- « Découper les cas inédits par cas » ; « familles par étiquettes sémantiques » : retirées → découpage par famille,
  famille = opérateur + signature statistique (Lazar, 20:26 à 20:34).
- De la v2 : relève qui « apprend » ; moteur massif à porter ; métriques de forme ; vocabulaire d'attaquant ; H-E2
  confirmatoire à quatre défendeurs ; mémoire commune dans le préenregistrement ; récompense d'un papier dans le noyau.

## 3. Conclusions acquises (pièces à l'appui)

- **Code** : une branche, `outils/essaim-m3-gradient-v1-travail` @ `4af2794` (88 tests ; ancêtres : `e82c341`, code
  cité par la v6 ; `e75e726`, fusion de session-depot) : contrat v3 (recherche, moisson, conception, entraîner,
  prédire), entraîneur isolé, vues, analyse de H-G1, bras apparié adaptatif, gardes de cohérence des budgets.
- **Banque** `confrontation-v1` scellée (`f1387a20…`) : 80 traces de sabotage (deux lots) + 120 items publics de
  conscience d'évaluation ; références de surface 0,69 / 0,50 ; étiquettes vérifiées par paires
  (`banque/verification-etiquettes-paires-v1/`, `LISEZMOI-v2.md` `d9761e6f…`).
- **Traits de l'étape 1** extraits et vérifiés (`donnees/traits-etape1-v1`, `6479769` ; deux jeux, dix vues chacun).
- **Brainstorm du lot 3** : Fable a rendu son tour ; Opus a refusé (filtre « cyber », jamais contourné ni reformulé) ;
  Argon a échoué (402).
- **Réseau** : Gemini, OpenAlex, LessWrong, Brave joignables ; OpenAlex et Semantic Scholar renvoient 429 depuis
  l'adresse partagée.
- **Registres de conv-audit** : heures UTC fausses de 18:19 à 19:23 (estimées) ; erratum au canal (n° 19 § 4) et au
  journal ; règle de l'horloge adoptée. Incident : 3 tests d'un organisme écrit par Gemini exécutés hors bac à sable
  (n° 19 § 5) ; correctif `pytest.ini`.

## 4. Décisions tranchées par Lazar (24 octobre, heure de Paris)

Jusqu'à 20:11 : table de la v2 (inchangée). Depuis :

| heure | décision | pièce |
|---|---|---|
| 20:22 | le programme gradient entier versé au journal | synthèse v2, section 7 |
| 20:23 | TAIF = Transformative AI Fund : entretien de subvention ; dossier (pitch de 5 minutes, 25 minutes de questions) | `livrables/dossier-taif-entretien-v1.zip` (`d0ba7121…`) |
| 20:26–20:29 | étape 2 : cas inédits engendrés par les organismes, en nombre suffisant, découpés entraînement / test par familles (H-G4) | journal détaillé, entrée « 19:00 » (vraie 18:31) |
| 20:32–20:35 | moisson de toute la littérature (forums et blogs compris) ; l'organisme conçoit son moissonneur ; avant le premier test sur la conscience d'évaluation | entrée « 19:15 » (vraie 18:37) |
| 20:34 | familles d'indices par concepts mathématiques, pas par étiquettes | idem |
| 20:37 | rondes de conception de l'organisme avant la génération 0 | entrée « 19:40 » (vraie 18:55) |
| 20:39 | accès réseau sortant « Tous les domaines » | canal n° 14 |
| 20:42, 20:46 | aucun K fixé : l'organisme décide seul de l'arrêt (« ne lui suggère rien ») ; tous les modules itérés | idem |
| ≈ 20:49 | moteur web : Brave (clé créée et posée par Lazar) | idem ; canal n° 15 |
| 21:06 | l'étape 1 inclut la phase de conception et la moisson avant scellement ; glissement d'un jour accepté | canal n° 15 |
| 21:10 | la session conv-audit continue en Opus 5.5 | journal détaillé, entrée « 20:20 » (vraie 19:23) |

GO inscrits par session-depot ce jour : GO-2026-10-24-05 (étape 1, « j'accepte le coût du calcul quel qu'il soit ») ;
GO-2026-10-24-06 (brainstorm du lot 3, plafond 25 USD).

**En attente de Lazar** : GO « calcul » de la confrontation (recommandé : deux graines, plafond 3 520 USD, attendu
≈ 700, illustratif ; autres options : une graine d'abord, 1 697,5 USD ; borne de conception 4) ; recharge du crédit
Gemini ; lot 3 sans Opus (recommandé ; défaut sous 48 heures).

## 5. Idées ouvertes et idées écartées

Ouvertes : concours de métriques et double désignation du champion (rapportés) ; familles opérateur + signature dans le
contrat (vérifiées par le noyau) ; `mailto` OpenAlex et clé Semantic Scholar ; lot 3 → banque `confrontation-v2` ;
étapes 2 et 3 ; dossier TAIF (montant et date à fixer par Lazar).
Écartées ce jour : celles de la section 2 (« réfutées ou retirées ») ; orchestration imposée ; injection des mécanismes
de Gemini dans l'organisme.

## 6. Prochaines étapes avant les runs (ordre)

**Confrontation** : (1) rapport de la contre-lecture n° 3 (lancée par session-depot) ; (2) v7 : entrée de la
contre-lecture, résultat de la vérification par paires avec ses empreintes et réserves, CE-02 sans objet avec son test,
date vraie, corrections éventuelles ; (3) scellement ; (4) GO « calcul » de Lazar ; (5) crédit Gemini ; (6) appel de
contrôle par espèce (statut `OK` exigé), répétition générale, courses adaptatives et gelées, relevé des métriques, gel,
confrontation, analyse, verdict par un sous-agent neuf (R13).
**Étape 1** : (1) v3 du préenregistrement (conception et moisson ; bornes alignées sur la v6 ; temps d'une ronde de
conception à aligner entre le texte, 1 800 s, et le lanceur scellé `8000348`, 2 400 s ; code cité `4af2794` ou après) ;
(2) contre-lecture et scellement ; (3) crédit Gemini ; (4) lanceur : répétition, A1, A2, B1, B2. Pire cas annoncé par
session-depot aux bornes de la v3 : ≈ 3 240 USD (2 × 1 066 + 2 × 555 ; attendu de l'ordre de 700, illustratif),
couvert par GO-05.
**Lot 3** : reprise sans Opus après la recharge, sur décision de Lazar.

## 7. Programme « apprentissage par gradient et renforcement conçu par l'essaim » — le plan en entier

Pièce intégrale : `journal/pieces/programme-apprentissage-gradient-essaim-v1.md` (`6b4151049ff9d279…`). Principe, table
des trois étapes, règle des données, hypothèses H-G1 à H-G4, règle des cas inédits et moisson : **section 7 de la v2,
inchangée**, sauf ce qui suit.

- **Étape 1, état** : code et données prêts (entraîneur isolé, vues, analyse de H-G1 ; traits extraits) ; v3 du
  préenregistrement en écriture ; la phase de conception et la moisson y entrent avant scellement (Lazar, 21:06). Le
  coût au pire cas passe de ≈ 70 USD (plafond indicatif 90, v2) à ≈ 3 240 USD aux bornes de la v3, parce que chaque
  lignée a désormais jusqu'à 8 rondes de conception à 10 USD et 37 USD par génération notée ; Lazar a accepté le coût
  « quel qu'il soit » (GO-05).
- **Étape 2** : H-G4 sur des familles = opérateur + signature statistique, découpage par opérateur ; le corpus moissonné
  par les organismes sert de matériau (jamais de test).
- **Ce qui manque** : préenregistrement scellé de l'étape 1 ; crédit Gemini ; puis le run. Pour l'étape 2 : générateur
  de traces, préenregistrement, devis 500 à 1 000 EUR.

## Divergences (à la main de session-depot)

(vide à la v3)

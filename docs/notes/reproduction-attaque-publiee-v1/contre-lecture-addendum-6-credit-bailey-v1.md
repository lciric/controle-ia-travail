# Contre-lecture (R2) — addendum 6 au préenregistrement du témoin de Bailey (crédit, recharge automatique), brouillon 1

**Verdict : scellable après corrections.** Aucun constat bloquant si les corrections L-1 à L-7 sont faites (texte de
remplacement donné mot pour mot ci-dessous). L-8 à L-11 sont des précisions ou des remarques.

Sur le fond :
- l'écart est nommé (condition 9 de l'addendum 5 remplacée par 9′) et le mot de Lazar est cité exactement (note 0929) ;
  mais le brouillon attribue à Lazar une décision qu'il n'a pas prise (le seuil, le texte de 9′, l'acceptation des
  risques) : L-3 ;
- le but de 9′ (qu'une coupure faute de crédit ne tombe qu'après 20 tours complets de la relance) **n'est atteint que si
  les autres chantiers du compte ne consomment que du stockage et si la carte louée coûte au plus 1,7 USD/h**. Ni l'un
  ni l'autre n'est garanti : le filtre d'offre du poste n'a pas de plafond de prix, et une instance de carte d'un autre
  chantier tournait la nuit de la coupure. Sur les durées réelles, 20 USD suffisent juste dans le cas de base
  (≈ 17,4 à 17,7 USD), pas au-delà : L-1 ;
- la lecture « après 20 tours : run tronqué » est fidèle au texte (l. 338, 372), mais elle suppose une reprise (lecture
  38) que trois choses peuvent empêcher, non déclarées : L-6 ;
- condition 7 (mot direct de Lazar) : cohérente ; la demande doit porter l'écart (nœud) : L-3 ;
- aucun résultat, aucune hypothèse, aucun seuil ni métrique du texte changés.

Contre-lecteur neuf : auteur d'aucun des fichiers relus. 13 novembre 2026.

Cloisons tenues :
- aucun fichier `notes-v3.jsonl` ni `technique-v3.jsonl` ouvert ; aucun champ de note lu ;
- rien lu sous `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/`,
  `docs/notes/programme-et-4-familles-evasion/` ; ni `registres/etat.md` ni `registres/decisions.md` lus ;
- aucun résultat ni seuil de sonde ou de moniteur lu ;
- aucune commande réseau (pas de `vastai`), aucune variable de secrets, aucun fichier existant modifié ; rien commité.

Hors de la liste fournie, j'ai lu seulement : les horodatages et codes de sortie des étapes dans
`sortie-conduite-v6/`, `-v8/`, `-v9/conduite-v5.jsonl` (durées de mise en place) ; les l. 1-20 de la note 0731 ; les
l. 57-80 de l'addendum 2 (lecture 38) ; le filtre d'offre du poste v12 (l. 127-158) ; dans `lanceur_v20.py`, la classe
`Reprise` (l. 2068-2200), `_relance_seule`, `assembler_lecture` et les constantes l. 340-359 ; la liste des essais
`test_v20_*`.

## Objets relus et empreintes vérifiées (`sha256sum`, `scellement verifier`)

| Objet | Empreinte | Constat |
|---|---|---|
| Brouillon 1 de l'addendum 6 | `3fc2adb7…` | relu (commit `20805a02`) |
| Préenregistrement | `fb6c2f34…` | OK ; l. 338, 371, 372 et conditions l. 376-390 conformes aux renvois |
| Addendum 5 | `eb97994a…` | OK ; condition 9 citée exactement ; ≈ 65 USD = 74,5 − 14,44 + 45 h × 0,11 : exact |
| Contre-lecture de l'addendum 5 | `2e274b16…` | OK (K-2) |
| Note 0929 | `3d6af78f…` | OK ; verbatim et relevés (28,66 USD, seuil 5, montant 5, paiements) exacts |
| Journal des durées | `9ff59e4b…` | OK ; 8 lignes, tours 0 à 7 |
| Journal de la conduite v11 | `32d4fce1…` | non scellé à part (compagnon du bilan) ; horodatages lus |
| `registres/depenses.md` | `e0463d1c…` | taux relevés l. 388, 414-422 |

## Calcul du seuil refait

Durées réelles :
- **tours** (journal des durées) : moyenne 1 411,49 s ; plus long 1 586,18 s (tour 3) ; plus court 1 299,48 s. Le texte
  dit que les tours s'allongent (l. 263-264) ; les tours 8 à 19 ne sont pas connus ;
- **mise en place** (de `creee` à la fin de `controle-juge`) : 16,3 min (conduite v6), 29,4 min (v9), 34,2 min (v11,
  23:12:03 → 23:46:15Z, le 12 novembre). Aucune mise en place le 13 novembre. « ≈ 45 min observées le 12 et le 13 » est
  donc inexact ; 0,75 h reste une borne prudente ;
- **hors tours** : chargement du modèle et sonde initiale avant le tour 0, ≈ 147 s au pilote (3 993 s du lancement à la
  fin, contre 3 845,8 s de tours) ;
- **taux** des instances du poste : 1,2393 à 1,6404 USD/h (`depenses.md` l. 414-422) ; le compte a payé une A100 à
  2,069 USD/h le 8 novembre (l. 388) ; le poste v12 prend **l'offre la moins chère** du filtre, A100 SXM4 **ou PCIE**,
  **sans plafond de prix** (`poste-hetzner-v12.sh` l. 132, 143) ;
- **autres instances** : la nuit du 12 au 13, le solde est passé de ≤ 10 USD (paiement de 23:46Z) à −0,93 vers 04:21Z,
  soit ≤ 2,4 USD/h pour tout le compte, dont 1,34 pour 60417353 : ≈ 1 USD/h pour les autres, dont la carte de 60432755
  « p3bis-v1 » (note 0731). Le « ≈ 0,11 USD/h » du brouillon n'a pas de source.

Heures pour 20 tours complets (h), puis crédit nécessaire (USD) selon le taux de carte c et les autres instances o :

| Scénario | Heures | c 1,34, o 0,11 | c 1,64, o 0,11 | c 1,70, o 0,11 | c 2,07, o 0,11 | c 1,70, o 1,11 |
|---|---|---|---|---|---|---|
| Brouillon : 0,75 h + 20 × moyenne × 1,15 | 9,77 | 14,2 | 17,1 | 17,7 | 21,3 | 27,5 |
| Mesuré : 0,61 h + 20 × moyenne × 1,15 | 9,63 | 14,0 | 16,9 | 17,4 | 21,0 | 27,1 |
| 0,75 h + 20 × tour le plus long × 1,15 | 10,88 | 15,8 | 19,1 | 19,7 | 23,7 | 30,6 |
| Carte 10 % plus lente | 10,67 | 15,5 | 18,7 | 19,3 | 23,3 | 30,0 |
| Carte 20 % plus lente | 11,57 | 16,8 | 20,3 | 20,9 | 25,2 | 32,5 |

Lecture : 20 USD tiennent le cas de base (marge ≈ 12 %) et le tour le plus long ; ils ne tiennent plus avec une carte de
plus de 1,7 USD/h, une carte 20 % plus lente, ou une autre instance de carte sur le compte. Le seuil doit donc dépendre
de c et de o relevés, pas d'une constante (L-1).

## Constats

| N° | Gravité | Ligne du brouillon | Constat et preuve | Correction |
|---|---|---|---|---|
| L-1 | **à corriger** | l. 23-31 (9′ et calcul) | **Le seuil fixe de 20 USD n'atteint pas le but de 9′ hors du cas de base.** (i) o est pris à 0,11 USD/h sans source ; une carte d'un autre chantier (60432755, note 0731) tournait la nuit de la coupure (≈ 1 USD/h), ce qui porte le besoin à ≈ 27 USD. (ii) c n'est pas plafonné : le poste prend l'offre la moins chère du filtre, PCIE comprise ; le compte a déjà payé 2,07 USD/h (besoin ≈ 21 à 24 USD). (iii) La moyenne des tours 0 à 7 est prise alors que les tours s'allongent (l. 263-264) ; le tour le plus long (1 586 s) donne 10,9 h. (iv) 9′ (i) ne nomme pas les champs (`credit`, `balance`), comme le faisait la condition 9. Tableau ci-dessus. | Remplacer le paragraphe 9′ et le calcul par : « **9′.** Avant la création (relevé au plus tard une heure avant ; repris si le poste attend une offre plus d'une heure) : (i) champs `credit` et `balance` du compte, le plus bas des deux au moins égal à S = 11 h × (max(1,7 ; c₀) + o) USD, et à 20 USD au moins, où c₀ est le taux, carte et stockage, de l'offre la moins chère du filtre du poste v12 au relevé, et o la somme des taux facturés des autres instances du compte au relevé (carte et stockage si elle est en marche, stockage seul si elle est arrêtée) ; (ii) recharge automatique configurée (`has_billing` vrai, `autobill_threshold` et `autobill_amount` > 0, `billing_failed` faux) ; relevés (champs, heure, c₀, o, S) consignés dans l'ordre de lancement. Sinon aucune création. Calcul de 11 h : mise en place ≤ 0,75 h (mesurée : 16,3, 29,4 et 34,2 min, de la création à la fin du contrôle du juge, conduites v6, v9 et v11, le 12 novembre ; plus ≈ 2,5 min de chargement avant le tour 0) ; 20 tours × 1 586,2 s (tour le plus long de la première exécution, journal des durées `9ff59e4b…`) × 1,15 ≈ 10,1 h ; total ≈ 10,9 h, arrondi à 11 h. Avec c₀ ≤ 1,7 et o ≈ 0,11 : S ≈ 19,9, donc 20 USD. » |
| L-2 | **à corriger (R6)** | l. 28-31 | Chiffres inexacts ou sans source : « ≈ 45 min observées le 12 et le 13 novembre » (mesuré : au plus 34,2 min, le 12 seulement) ; « 1,20 à 1,64 » (poste : 1,2393 à 1,6404, `depenses.md` l. 414-422 ; compte : jusqu'à 2,069, l. 388) ; « ≈ 0,11 USD/h » (aucune pièce). | Repris par le texte de L-1 ; citer `registres/depenses.md` (empreinte au scellement) pour les taux, et la source de o (relevé de l'ordre de lancement). |
| L-3 | **à corriger** | l. 22, 47, 54-56 | **Attribution à Lazar trop large.** Son mot (note 0929) propose un principe (« je ne peux pas cxrediter plus de 10 dollars, je propose de le laisser se rechrger automatiquemet… ») ; il ne fixe ni le seuil, ni le texte de 9′, ni la surveillance, et il n'a pas vu les risques du § 5. Or l'écart à un addendum scellé est un nœud : la décision doit être la sienne. « Décidé par Lazar » (l. 22) et « acceptés par Lazar en proposant la recharge automatique » (l. 47) ne sont pas tenus par la pièce. | l. 22 : « ## 2. Écart (condition 9 de l'addendum 5), sur la proposition de Lazar (principe : crédit limité, recharge automatique) ; seuil et texte de 9′ : calcul de la session, soumis à Lazar avec la demande du mot de lancement (condition 7). Remplacée par : ». l. 47 : « ## 5. Risques déclarés (soumis à Lazar avec la demande du mot de lancement ; son mot les accepte) ». § 6, ajouter : « La demande du mot direct de Lazar (condition 7) cite cet addendum (chemin, empreinte), le relevé de 9′ (S, c₀, o), les risques du § 5 et le tirage attendu sur la carte (§ 5 (c)) ; ce mot vaut décision du nœud de l'écart. » |
| L-4 | **à corriger** | l. 18-20, 40-41 | (i) Le second mot de Lazar (« pacr e qu'il n'y avait plus de fonds sur ma carte ») n'est consigné dans aucune note ; la note 0929 dit « cause non établie ». (ii) « Un vidage du compte arrête l'instance sans la détruire (série 3) » est écrit comme une règle ; la note 0731 dit au contraire : « une instance arrêtée sur un compte en solde négatif peut être supprimée par Vast ». Seul fait : en série 3, l'instance a été gardée ≈ 3,5 h de solde négatif. | (i) l. 18 : « Cause donnée par Lazar, verbatim : « pacr e qu'il n'y avait plus de fonds sur ma carte » (message reçu après la note 0929, consigné dans cet addendum seulement ; la note 0929 disait « cause non établie »). » Ou le consigner dans une note neuve (R12) et la citer avec son empreinte. (ii) l. 40-41 : « En série 3, l'arrêt du compte a arrêté l'instance sans la détruire (≈ 3,5 h de solde négatif) ; une suppression sous solde négatif prolongé n'est pas exclue (note 0731, `f6e09ff5…`). La lecture passe par la reprise (lecture 38), voir le risque (d). » |
| L-5 | **à corriger** | l. 33-35 (surveillance) | **L'alerte vient trop tard.** En régime normal (seuil 5, montant 5), le crédit oscille entre ≈ 5 et ≈ 10 USD : « sous 10 USD » est toujours vrai. Si la recharge échoue au passage de 5 USD, le compte se vide en 5 / (c + o) ≈ 2,8 h (1,81 USD/h), ≈ 2,1 h à 2,4 USD/h (la nuit du 12 au 13). Alerte à « plus de 4 heures sans paiement », vue à un réveil espacé de 90 min : elle peut tomber après l'épuisement. Le 12 novembre, `billing_failed` est resté faux pendant le défaut : ce champ ne prévient pas. Enfin la surveillance dépend des réveils de la session (machine de la session éteinte pendant l'inactivité le 12 novembre, `depenses.md` l. 415). | Remplacer par : « **Surveillance** (sans valeur de garde) : à chaque réveil (au plus toutes les 90 minutes), la session relève `credit`, `balance`, les paiements et o ; elle alerte Lazar si le crédit est sous 4 USD (sous le seuil de recharge : la recharge aurait dû payer), si `billing_failed` est vrai, ou si o dépasse de plus de 0,5 USD/h le o du relevé de lancement. Le 12 novembre, le défaut de recharge n'a pas mis `billing_failed` à vrai. Un réveil manqué ou une alerte non lue (nuit) laisse le compte se vider. Aucun arrêt par la session sur ce seul motif : la liste d'arrêt est inchangée. » |
| L-6 | **à corriger (risque manquant)** | § 3, § 5 | **La lecture d'un run tronqué suppose une reprise que trois choses peuvent empêcher.** (a) Suppression par Vast sous solde négatif prolongé (L-4 (ii)). (b) Compte prudent : l'intervalle arrêté compte au taux c dans D ; la reprise ne redémarre pas s'il reste moins de 900 s avant B − 0,5 (`Reprise._borne_budget`, `MARGE_SECOURS_USD` = 0,5, `DUREE_TRANSFERT_MIN_S` = 900, `lanceur_v20.py` l. 340, 351 ; addendum 2, lecture 38). Au taux 1,34 : ≈ 36 h de solde négatif tolérées pour une coupure au tour 20, ≈ 15 h près de la fin de 72 tours. (c) Le chemin « relance seule coupée, reprise, `assembler_lecture` sur le dossier de reprise » n'est couvert par aucun essai : `test_v20_*` n'assemble qu'une relance sortie de sa conduite, jamais une relance transférée par `Reprise`. | Ajouter au § 5 : « (d) une coupure après 20 tours n'est lue que si la reprise (lecture 38) transfère les journaux : Vast peut supprimer une instance arrêtée sous solde négatif prolongé (note 0731) ; au compte prudent, l'arrêt compte au taux c dans D, et la reprise est refusée s'il reste moins de 900 s avant B − 0,5 (≈ 15 à 36 h de solde négatif tolérées selon le moment de la coupure, au taux 1,34) ; le chemin reprise d'une relance seule, puis assemblage, n'est pas éprouvé par les essais de l'addendum 5. Reprise impossible ou assemblage refusé : pas de verdict, nœud. » Recommandé (routine, sur processeur, avant le lancement) : un essai `Reprise` puis `assembler_lecture` sur une relance seule coupée à 20 tours ou plus. |
| L-7 | **à corriger** | l. 51-52 (risque (c)) | **Tirage sur la carte sous-estimé.** La relance de 72 tours dure ≈ 28,8 h (moyenne) à 33,1 h (marge 1,15), plus la mise en place : ≈ 39 à 60 USD au total selon le taux (1,24 à 1,7, plus o = 0,11). Avec un crédit initial de 20 USD, dont 15 avant la première recharge : ≈ 24 à 45 USD tirés sur la carte, en ≈ 5 à 9 recharges, et non 4 à 5. Lazar a écrit ne pas pouvoir créditer plus de 10 USD : le montant doit lui être donné. | « (c) chaque recharge de 5 USD couvre ≈ 2,8 h (à 1,81 USD/h) ; la relance (≈ 29 à 33 h, ≈ 39 à 60 USD au total selon le taux) demande, après les 15 premiers USD d'un crédit initial de 20, ≈ 24 à 45 USD tirés sur la carte en ≈ 5 à 9 recharges, environ une toutes les 3 h ; ce montant est donné à Lazar dans la demande du mot de lancement. » |
| L-8 | à préciser | l. 38-39, 48-49 | **Fidélité au texte : exacte, deux précisions.** Une coupure faute de crédit est « le run s'interrompt pendant le tour e₀ » (l. 338) : K′ = e₀ ; K′ ≥ 20 : lu comme un run de K′ tours ; et « erreur technique après 20 tours complets : pas de relance ; run tronqué » (l. 372). Avant 20 tours : seconde erreur, pas de verdict, nœud (l. 338, 371). Conforme. Mais (i) le classement n'est pas écrit (l'addendum 5 lisait la coupure de la série 3 comme une « coupure de l'hôte », l. 371) ; (ii) « K′ < 72, verdict lu au régime réduit » est inexact pour K′ = 71, lu au régime publié (l. 331 : K ≥ 71). | l. 38 : « Si le compte se vide après 20 tours complets de la relance : interruption pendant le tour e₀ (l. 338), classée comme à l'addendum 5 (coupure de l'hôte, l. 371-372) ; run tronqué, lu comme un run de K′ = e₀ tours, interruption rapportée ; seule la relance porte le verdict, la première exécution reste rapportée comme interrompue. » l. 49 : « puissance moindre ; verdict au régime réduit si K′ ≤ 70 (l. 332) ». |
| L-9 | à préciser | l. 50 (risque (b)) | Le risque (b) dit que la consommation des autres chantiers « entame le crédit » sans dire la conséquence : une instance de carte lancée ailleurs pendant les ≈ 11 premières heures fait tomber la garantie des 20 tours, quel que soit le relevé. La session ne peut pas l'empêcher. | « (b) le compte est partagé avec d'autres chantiers : une instance de carte lancée par un autre chantier après le relevé, pendant les ≈ 11 premières heures, peut vider le compte avant 20 tours (seconde erreur, pas de verdict, nœud) ; la session le relève à chaque réveil et le signale ; la demande du mot de lancement demande à Lazar qu'aucun autre chantier ne lance d'instance de carte sur ce compte pendant ce temps sans créditer d'autant. » |
| L-10 | remarque | l. 23-24 | Le poste v12 ne relève pas le crédit (K-2 (iv) de la contre-lecture de l'addendum 5) : le « repris si le poste attend une offre plus d'une heure » repose sur la session ; avec des réveils espacés de 90 min, la création peut suivre de plus d'une heure un relevé sans nouveau relevé. Avec o ≈ 0,11, l'écart est faible (≈ 0,2 USD). | Déclarer en une phrase, ou lancer le poste juste après le relevé et, faute d'offre dans l'heure, arrêter le poste par son identifiant (R10) avant un nouveau relevé. |
| L-11 | remarque | l. 1-6, § 4 | Aucun résultat lu ni cité ; les durées sont des champs techniques (`tour`, `duree_s`), déjà admis par l'addendum 5. Aucune hypothèse, prédiction, métrique, seuil, graine, B ni ligne de la liste d'arrêt du texte changés ; les conditions de lancement du texte (l. 376-390) sont inchangées ; seule change une condition d'addendum. Condition 7 (mot direct de Lazar) gardée (§ 4, § 6) : cohérent. | Aucune. |

## Réponses aux questions posées

1. **Écart, rattachement, but de 9′.**
   - Écart nommé ; mot de Lazar cité exactement. Le rattachement va trop loin : L-3.
   - But atteint dans le cas de base seulement : sur les durées réelles, 9,6 à 9,8 h et ≈ 17,4 à 17,7 USD à 1,7 USD/h
     plus 0,11. Il faut une marge pour le tour le plus long, pour les cartes plus chères ou plus lentes, et surtout pour
     les autres chantiers : L-1, L-9. Le texte de remplacement garde 20 USD dans le cas de base et monte avec c₀ et o.
2. **Lecture « après 20 tours : run tronqué ».** Fidèle aux l. 338 et 372 (et 371 avant 20 tours). Elle suppose une
   reprise qui peut échouer (suppression, budget au compte prudent, chemin non éprouvé) : L-6 ; classement et K′ = 71 :
   L-8.
3. **Risques.** Incomplets : surveillance trop tardive (L-5), reprise (L-6), tirage sur la carte (L-7), autres chantiers
   (L-9), suppression sous solde négatif (L-4 (ii)). Le risque (a) est honnête.
4. **Conditions de lancement.** Cohérentes ; condition 7 gardée. La demande du mot doit porter l'écart et ses risques
   (L-3) ; champs et relevés de 9′ précisés (L-1) ; relevé repris sans garde du poste (L-10).
5. **Aucun résultat**, aucune modification d'hypothèse ni de seuil du texte (L-11).

# Contre-lecture du devis de la tranche B-β (v4) — lecteur neuf (R2)

Pièce lue : `devis-tranche-b-beta-v4.md` (empreinte conforme au compagnon). Lus aussi : v3 et sa contre-lecture, `diff` v3 → v4, les deux relevés
(empreintes conformes ; le relevé neuf n'a que ses deux lignes d'en-tête, aucune offre). Rien exécuté du dépôt voisin, aucune commande du loueur,
aucune variable d'environnement affichée, aucun fichier existant modifié. Recalculs par un court calcul local sur les seuls chiffres du devis.

**Verdict : à corriger** (légèrement). Les 12 points de la v3 sont repris au fond, tous les chiffres neufs sont exacts, aucun reste de 2,38 / 24,9 / 61,1
hors des tables d'historique. Reste une majeure (trafic entrant non borné par la carte exigée) et des mineures de forme et de précision.

## Reprise de la table du § 10
| point de la v3 | verdict |
|---|---|
| majeure 1 filtre non rejoué | **Repris** : relevé neuf joint, zéro offre, disponibilité dite « non établie » (§ 3, § 4, § 7). Réserve : m-1. |
| majeure 2 trafic des copies | **Repris pour le sortant** (`inet_up_cost<=0.04`, copies comptées) ; **entrant non borné** : Majeure 1. |
| majeure 3 perte de machine | **Repris** : détection, bornes 39 et 55, (b) seul protecteur, reprise = devis neuf. Réserves : m-3, m-4. |
| m-A sauvegardes | Repris : 14 au pire, + 0,5 h, « à mesurer ». |
| m-B prix exigé | Repris : 2,25 (seuil exact 2,303). |
| m-C trafic | Repris (compte large, double compte dit). |
| m-D Qwen3-8B, Gio et Go | Repris (71 et 72 emplacements, « pour les deux »). Une ponctuation manquante : m-7. |
| m-E débit du pire cas | Repris (moitié du débit exigé ; copie pour (a) : « rien pour (a) »). |
| m-F règle de la dernière heure | Repris : défaut à 15 minutes, empreintes avant destruction. |
| m-G pic « au moins » | Repris (§ 6 ; le § 1 écrit toujours « pic estimé » : m-6). |
| m-H recompilations | Repris. |
| m-I mise en forme | **Annoncé « acceptée » mais pas fait en entier** : en-tête et heure (m-5). |

## Recalculs (tous refaits, tous justes sauf indication)
- Heures : bas 0,5 + 5,7 + 1,0 + 0,3 + 0,5 + 0,5 + 0,2 = 8,7 ; haut 1 + 8,5 + 1,5 + 0,5 + 0,8 + 0,8 + 0,3 = 13,4 ; pire 3 + 14,1 + 2,5 + 1 + 1,5 + 1,5 + 0,5 + 1 = **25,1**. Écart au plan v2 : 25,1 − 21,2 = 3,9. Juste.
- B1 : 2 000 × 11,22 / 3 600 = 6,23 h ; × 11,78 = 6,54 ; × 0,9 = 5,61 ; × 1,2 = 7,85 ; 2 000 × 23,6 = 13,11 ; + 0,5 (14 sauvegardes × 1 à 2 min = 0,23 à 0,47) + 0,5 (5 copies × 8,6 Go à 200 Mbit/s = 5,7 min chacune = 0,48) = **14,1**. Juste. Attendu 5,7 à 8,5 : voir m-2.
- Copies : 14 / 3 ≈ 5 ; 5 × 8,6 = 43 Go ; sortant 17 + 43 = 60 Go ; entrant 25 ; total 85 Go × 0,04 = **3,4**. Juste.
- Pire cas : 25,1 × 2,25 = 56,475 (« 56,5 ») ; + 3,4 = 59,875 (« 59,9 ») ; marge 61,2 − 59,9 = 1,3. Seuil exact du prix exigé (61,2 − 3,4) / 25,1 = 2,303 : 2,25 tient. Juste.
- Minuterie : 61,2 / 2,25 × 3 600 = **97 920 s** = 27,2 h ; 61,2 / 2,15 × 3 600 = 102 474 s ; 61,2 / 36 = 1,70 ; 129 600 s = 36 h. Rappel 25,1 h < 27,2 h ; 80 % = 21,8 h. Juste.
- Carte attendue : 8,7 × 2,145 = 18,7 ; 13,4 × 2,145 = 28,7 (« 19 à 29 ») ; total « 19 à 32 » = 28,7 + 3,4 = 32,1. Juste. Prix avec 200 Go : 2,1076 + 200 × 0,133 / 730 = 2,144. Juste.
- Pertes : (3 + 14,1) × 2,25 = 38,5 (« ≈ 39 », trafic de B1 compris) ; après B1, jusqu'avant la copie de B6 : (25,1 − 0,5) × 2,25 = 55,4 (« ≈ 55 », hors trafic). Justes, bornés par 61,2.
- Copie des lentilles : 17,2 Go = 137,6 Gbit : 11,5 min à 200 Mbit/s, 23 min à 100 Mbit/s ; B6 « 0,2 à 0,3 » et « 0,5 pire » tiennent.
- Relevé du 00:22Z : lignes, plages de prix et de trafic du tableau du § 3 conformes (H100 SXM 2,1076 / 4,6421 / 4,8433 ; PCIe 2,3482 ; NVL 3,4147 à 3,6645 ; A100 80 Go : six SXM4 de 1,1043 à 1,973 et une PCIe 1,461 ; 40 Go : 3 SXM4 + 4 PCIe ; six sur sept sous 1,70). Juste.
- Restes : `2,38`, `24,9`, `61,1`, `25,7` n'apparaissent qu'aux l. 218 et 220 (table d'historique du § 9). Propre.

## Bloquantes
Aucune.

## Majeures
**1. Le trafic **entrant** n'est pas borné par la carte exigée, mais le pire cas le compte « à 0,04 au plus, plafond exigé »** (v4 l. 79, 131, 139-141 ; relevé H100 : colonnes `trafic_sortant_usd_go` et `trafic_entrant_usd_go`).
Écrit : « trafic sortant ≤ 0,04 USD/Go (`inet_up_cost<=0.04`) » ; § 4 : « ≈ 85 Go à 0,04 au plus, plafond de trafic exigé » ; § 4 : « tient dessous sans troncature ». Or 85 Go = 60 Go sortants + **25 Go entrants** ; seul le sortant est exigé. Une offre à 2,25 USD/h avec un entrant à 0,10 USD/Go ajoute 1,5 USD de plus que dans le calcul (25 × 0,06), soit 61,4 > 61,2 : « sans troncature » tombe, avec une marge de 1,3 USD seulement. Le relevé neuf distingue les deux sens ; le filtre exigé ne s'en sert que pour un.
Devrait être écrit : exiger aussi `inet_down_cost<=0.04` (le relevé a la colonne), ou compter 25 Go d'entrant au pire prix lisible et dire que « sans troncature » vaut sous cette condition.

## Mineures
**m-1. Contrôle manquant sur le relevé vide** (§ 3, l. 85-88). Zéro ligne peut venir d'une offre disparue ou d'un nom de carte mal passé au filtre (`gpu_name=H100_SXM`, forme différente de celle du premier relevé, qui filtrait sans nom de carte). R5 : une requête témoin sur un cas sain (même syntaxe, une carte que l'on sait présente, ex. H100 PCIe) prouverait que la forme du filtre rend des lignes. À ajouter, ou à dire « syntaxe du filtre non contrôlée ». En outre, le tableau de la l. 70 écrit encore « une seule offre au prix exigé » sans renvoi au relevé de 01:23Z : harmoniser (« une offre à 00:22Z, aucune à 01:23Z »).
Aussi : le premier relevé a une seule colonne `trafic_usd_go` sans dire le sens ; le § 3 l'emploie comme trafic sortant. À préciser (le relevé neuf, lui, est clair).

**m-2. Attendu bas de B1 sans les copies** (l. 99-100, 107). La ligne B1 dit « sauvegardes et copies (b) comprises » ; 5,7 h au bas = 5,6 + 0,1 de sauvegardes, sans copie : au bas, 5 à 6 sauvegardes donnent 2 copies, soit + 0,2 h (≈ 5,9 h). Écart de 0,4 USD, sans conséquence sur les bornes, mais l'intitulé dit autre chose que le chiffre. Dire « copies comptées au haut seulement » ou corriger.

**m-3. Détection de la perte** (l. 116-118). « L'état poussé n'avance plus depuis 30 minutes » : le texte ne dit pas que B1 pousse son état à moins de 30 minutes d'intervalle (sauvegarde toutes les 60 minutes ; une étape B1 dure 6 à 14 h). Sans cadence de poussée écrite, la condition donne des fausses alertes ou ne se déclenche pas. Écrire la cadence exigée, ou ne retenir que « instance non running » et « course figée ».

**m-4. Après la perte** (même passage). « Règle : arrêt » ne dit pas expressément que la destruction par identifiant, la vérification par l'absence et le décompte de dépense continuent après la perte (demandé en (iv) de la majeure 3 de la v3). Une phrase.

**m-5. En-tête non mis à jour** (l. 1-15). La demande « m-I acceptée » n'est pas tenue : (i) la phrase d'en-tête enchaîne v4 = v3, v3 = v2, v2 = v1 en un seul bloc, difficile à lire ; (ii) l. 12 « écrit par la fille … ≈ 00:45 UTC » contredit la l. 5 (« vers 01:30 UTC ») ; (iii) l. 15 ne cite que le relevé de 00:22Z, pas le relevé H100 de 01:23Z (cité l. 5 et § 3). Mettre une ligne par version et une seule heure.

**m-6. Pic du lot 64** (l. 30). Le § 1 écrit encore « pic estimé ≈ 23,5 GiB » ; la m-G de la v3 (reprise « acceptée (§ 6) ») demandait « au moins ». Seul le § 6 est corrigé. Harmoniser.

**m-7. Mise en forme** (l. 54). « … (`02_fit.py` l. 9-10 ; v4, m-D) C'est au-delà de la limite … » : point manquant avant « C'est » ; la mention « v4, m-D » dans le corps du texte est un renvoi d'historique, à ranger au § 10.

**m-8. Minuterie et trafic** (l. 150, 139). La minuterie compte la carte seule (61,2 / prix) ; à son échéance (27,2 h), la dépense totale peut atteindre 61,2 + trafic (jusqu'à ≈ 64,6 USD), c'est-à-dire plus que l'« arrêt dur à 61,2 » du tableau des gardes, tout en restant sous le plafond de 68. À dire (la minuterie n'est pas l'arrêt dur en dollars ; celui-ci tient à la garde de dépense), ou à tracer la garde de dépense qui compte le trafic. Sans conséquence sur le pire cas chiffré (25,1 h < 27,2 h).

**m-9. Deux séries d'options (a) (b) (c)** (§ 7). Les options de la décision et les lieux des lentilles portent les mêmes lettres (« Recommandation : (a), avec le lieu (b) … à défaut, (c) »). Lisible, mais ambigu pour Lazar ; nommer les lieux L-a, L-b, L-c.

**m-10. « ≈ 55 USD »** (l. 121-122) est hors trafic (55,4) ; avec le trafic jusqu'à la copie, ≈ 58 à 59. Dire « hors trafic » ou corriger : la borne reste sous 61,2.

## Ce qui est sain (à ne pas perdre)
L'arithmétique des heures, du pire cas, de la minuterie, des sauvegardes, des copies, du trafic sortant et des pertes est exacte et cohérente entre § 3 à § 7 ; l'aveu clair que la disponibilité n'est pas établie ; le prix exigé 2,25 justifié par un seuil exact (2,303) ; la perte de machine traitée en arrêt avec bornes chiffrées et reprise = devis neuf ; les tables d'historique sont les seuls lieux des anciens chiffres.

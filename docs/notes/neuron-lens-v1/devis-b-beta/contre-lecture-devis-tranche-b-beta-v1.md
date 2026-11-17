# Contre-lecture du devis de la tranche B-β (v1) — lecteur neuf (R2)

Pièce lue : `devis-tranche-b-beta-v1.md` (empreinte vérifiée : `b98e53f1…`, OK ; relevé tsv `1a7cc32c…` OK ; texte gelé v6 `34b88243…` OK).
Lu aussi : plan et devis v1 (§ 4, § 5.3, § 7) et v2 (§ 0, § 3.2 à 3.4), texte gelé v6 (§ B.4, liste d'arrêt, critères), relevé des prix, journaux
B-α v1 à v3, devis B-α v2, banc publié de l'ajustement, addenda d'empreintes v1 à v3, `registres/go.md`. Rien exécuté, rien lu de secret.

**Verdict : à corriger.** L'arithmétique du devis est exacte, mais la dérivation de la durée de B1 ne reproduit pas ses chiffres, et le pire cas
ne couvre ni la H100 PCIe ni le repli A100 que la recommandation propose ; la minuterie v4 refuserait la plupart des offres de repli.

## Recalcul (question 1)
- Heures attendues : 0,5+6,2+1,0+0,3+0,5+0,5 = 9,0 ; 1+8,9+1,5+0,5+0,8+0,8 = 13,5. Juste. Pire cas : 2+13,2+2,5+1+1,5+1,5+1+1 = 23,7. Juste.
- Carte attendue 9 à 13,5 h × 2,2 = 19,8 à 29,7 USD (« 20 à 30 ») ; total 21 à 31 : juste. Pire cas 23,7 × 3,00 = 71,1 ; + 3 = 74,1 : juste.
- 60 % de 68 = 40,8 ; 90 % = 61,2 ; 61,2/3,00 = 20,4 h ; 61,2/2,2 = 27,8 h ; 23,7 × 2,55 = 60,4 < 61,2 ; 61,2/2,55 = 24,0 h = 86 400 s,
  dans les bornes 600 à 129 600 s : tout juste.
- Prix : H100 SXM 2,1076 / 4,6421 / 4,8433 ; PCIe 2,3482 ; NVL 3,4147 à 3,6645 ; A100 SXM4 80 Go 1,1043 à 1,9730 (6 offres) ; RTX 6000 Ada
  0,5614 à 0,8690 : égaux au fichier. Écarts relevés plus bas (R1 à R3 mineures).
- Durées mesurées de B-α : environnement 64 à 181 s, poids 72 s à 3 min 30, B0 19 à 41 s, corpus 2 min 31 à 15 min, passe 61 à 66 min,
  pilotage 514 s, ablation 29 s × 32 ≈ 15,5 min, `score` ≈ 3 min : conformes aux journaux.
- Banc : 11,22 à 11,77 s par document, pic 20,2 à 29,1 Go à lot de 128, 47,9 Go compilé à lot de 256 : conforme.

## Bloquantes
**B1. Pire cas non crédible hors H100 SXM ; repli A100 incompatible avec la minuterie** (l. 44-45, 40-41, 71-73, 79-80). La recommandation
retient « H100 (SXM ou PCIe) » puis « repli A100 de 80 Go, puis de 40 Go », vitesse « non mesurée ». Le pire cas (23,7 h) est bâti sur le
banc d'une H100 SXM. Une PCIe a moins de calcul (de l'ordre d'un quart de moins), une A100 est probablement deux à trois fois plus lente
(estimation du lecteur, non mesurée : B1 seul passerait de 6 à 9 h à 15 à 25 h attendus, 30 à 35 h au pire). À 1,10 à 1,97 USD/h, le pire cas en
dollars dépasserait alors 61 USD, donc l'arrêt dur. Par ailleurs, la minuterie v4 est bornée à 129 600 s : 61,2/129 600 s → prix lu ≥ 1,70 USD/h ;
cinq des six A100 de 80 Go (1,10 à 1,51) et toutes les A100 de 40 Go seraient refusées. Écrit : « repli … décidé par le banc de B0 ». Devrait
être écrit : soit le repli est retiré (comme B-α, « aucun repli, rien ne part, message à la mère »), soit il reçoit un pire cas chiffré, un prix
exigé, et le texte dit que la minuterie v4 devrait être étendue (nœud) ; et la PCIe soit retirée de la recommandation soit chiffrée.

## Majeures
**M1. Dérivation de B1 fausse** (l. 49-50 et 55). Écrit : « publié (≈ 3 h par lentille) × 0,9 à 1,2 ». Cela donne 5,4 à 7,2 h (ou, sur le banc,
5,6 à 7,9 h) ; or le devis annonce 6,2 à 8,9 h. Ces deux bornes sont celles de la plage 11 à 16 s par document du README, sans coefficient (plan
v1 § 5.3, repris tel quel par la v2). De même 13,2 h n'est pas « 1,5 fois la borne haute » (1,5 × 8,9 = 13,35). Devrait être écrit : la vraie base
(banc 11,2 à 11,8 s → 6,2 à 6,6 h pour deux lentilles ; ou plage du README) et le coefficient appliqué ou non, puis recalculer ; le pire cas de
13,2 h reste plausible sur H100 SXM (≈ 24 s par document, deux fois le banc).

**M2. Gardes de la tranche B-α non reprises** (l. 78-81). Le devis B-α v2 (§ 3) fixait : échéance datée, instances intouchables, crédit
(`can_pay`, `has_billing`, `billing_failed`, crédit < 1 USD), course figée (`gpu_util`, `cpu_util`), branche de résultats exigée absente, rappel à
80 % de la minuterie, ligne de GO nommée. Le devis B-β n'en reprend que la moitié et ne dit pas « repris de B-α devis v2 § 3 ». À écrire,
avec l'échéance (2026-11-30 pour le volet B, plan v2).

**M3. Condition de passage de B-α à B-β absente** (l. 3-9, § 2). Texte gelé v6 (l. 267, 379) et plan v2 § 3.2 : compte rendu à la mère après
B-α, β suspendu si « chaîne en défaut ». Le devis ne dit ni l'état de B-α (courses faites, lecture par lecteur neuf faite ou non) ni ce préalable.
À ajouter aux préalables du § 2.

**M4. Les essais de préalable 3 sont impossibles ici** (l. 20-21). « Correctifs … contre-lus, avec leurs essais (miniature contre force brute) »
avant la commande, alors que plan v1 § 7 rapporte le refus d'exécuter localement le dépôt cloné, que § 5.4 dit « non faisable » et que le devis
place l'essai de la garde « force brute » à B0, sur la machine payée (l. 11-12). Choisir : essais locaux (il faut alors la règle de permission
évoquée au plan v1 § 7, nœud) ou essais seulement sur la machine, et le dire ; le pire cas de B0 (2 h) en dépend (plan v1 disait 3 h pour
« retouche à déboguer sur la machine, faute d'essai local »).

**M5. Refaire la passe et `measure` n'est pas justifié** (l. 55-58). Plan v2 § 3.2 : B-β = « nouvelle notation de la mesure de B-α avec notre
lentille R, sans nouvelle passe du modèle » ; tables recopiées « ou refaites : 1,5 h au pire cas ». Le devis refait corpus, comptes, passe, pilotage et
ablation (≈ 1,5 à 2,3 h attendues) sans dire pourquoi (tables non conservées ? lecture de B-α encore due ?). De plus `measure` n'emploie aucune
lentille (plan v1 § 4.2) : la refaire change seulement le lot (64 contre 16 déclaré en B-α) et non l'objet. À dire : ce qui est recopié, ce qui est
refait, et pourquoi ; et que le lot 64 sur 80 Go est une hypothèse non mesurée (en B-α, 24 Go ont manqué de mémoire à 64).

**M6. Écart non signalé au plan v2** (l. 62, 69, 71). Le plan v2 annonçait 8,8 à 11,5 h, 21 à 27 USD attendus et un pire cas de 21,2 h à 68 USD ;
le devis donne 9 à 13,5 h, 21 à 31 USD et un pire cas de 23,7 h à 74 USD, et ne dit pas qu'il s'écarte de la v2 ni pourquoi (B0, B2 et B5/B6
relevés). La phrase « ce qui suppose de tenir le pire cas sous l'arrêt dur » est honnête, mais le tableau devrait porter la colonne « v2 ».

## Mineures
**m1. Nombre d'offres A100 de 40 Go** (l. 41) : « 8 » ; le fichier en compte 7 (3 SXM4 + 4 PCIe). Les 9 A100 SXM4 et 5 A100 PCIe ne sont pas
distinguées ; l'A100 PCIe de 80 Go (1,461) n'est pas listée.
**m2. Trafic** (l. 38, 42) : H100 NVL « 0 » (fichier : 0 à 0,0365) ; RTX 6000 Ada « 0,003 » (fichier : 0,0026 à 0,0143).
**m3. Filtre** (l. 32) : le fichier ajoute `inet_down ≥ 300` et `rentable`, absents du devis.
**m4. Prix de l'offre retenue** (l. 66) : « ≈ 2,2 lus, stockage compris » : le relevé donne 2,108 (Japon) ou 2,348 (Afrique du Sud) *sans*
stockage ; avec 200 Go, ≈ 2,14 et ≈ 2,41 d'après les prix de stockage du fichier. Dire lesquels, et que l'offre à 2,348 a un trafic de
0,040 USD/Go (≈ 1,2 USD pour 30 Go, non compté dans « 60,4 < 61,2 », qui est donc à 61,6 trafic compris).
**m5. Option (c)** (l. 75-76, 94-95) : « plafond ≈ 48 USD » est le *pire cas* de la v2, pas un plafond (l'arrêt dur à 90 % exigerait ≈ 53 USD) ;
chiffres de la v2 aux prix du 13 novembre, non recalculés. L'option (b) « plafond ≈ 80 » : arrêt dur 72 contre 71,1 + 3 = 74,1 de pire cas total,
même défaut que (a) d'un autre côté.
**m6. Limite de l'hébergeur de code** (l. 25-26) : « 95 Mo par fichier » ; le devis B-α (§ 4) disait 100 Mo, « non revérifiée ». Un seul chiffre,
sourcé.
**m7. Préalable 2** (l. 19-20) : les empreintes `16957c52…` et `2fa015e4…` figurent déjà aux addenda v1 à v3 (« B-β seulement »). Dire ce qui
manque encore (empreintes propres à Llama et à la lentille ajustée), au lieu de laisser croire que tout est à faire.
**m8. Chiffre de 10 Go et de 30 Go entrants** (l. 25, 67) : repris du plan v1 sans calcul ni source ; à donner avec leur origine.
**m9. Moitiés séparées** : le devis ne dit pas si les deux moitiés (B-1) coûtent une seconde passe ou un seul passage à deux accumulateurs ;
une des deux lectures change B1 du simple au double.

## Réponses aux questions
2. Plan : étapes B0 à B6 et mesures B-1 à B-7 présentes ; garde « force brute » à B0 ; texte gelé séparé exigé (préalable 1) et B-5 réécrit.
   Manquent : condition de passage depuis B-α (M3), gardes complètes (M2), choix recopier ou refaire (M5).
3. Hypothèses dites : vitesse Llama (0,9 à 1,2, plausible : calcul par couche à peu près égal, 32 couches contre 36 plus larges), vitesse A100,
   correctifs de l'ajustement (« non mesurés »). Non dites : vitesse H100 PCIe, lot 64 sur 80 Go, pic de mémoire de Llama contre le modèle du banc
   pour l'A100 de 40 Go (pic 29 Go sur 40, marge mince avec des couches à portes plus larges), temps de transfert de B6.
4. Lieu des lentilles : correctement présenté comme décision non prise, conséquence dite (perte à la destruction), pas de défaut. À améliorer :
   donner les options chiffrées (stockage privé existant ou machine de Lazar, coût, délai) et faire figurer la décision comme condition
   explicite de la commande, pas seulement de la recommandation (l. 97), sous peine de GO donné sans lieu.
5. Règles du dépôt : R1, R2, R6, R12 respectées (empreintes compagnons présentes, version dans le nom). Je n'ai pas pu vérifier
   `GO-2026-11-17-03` ni R-3046 : l'identifiant n'apparaît pas dans `registres/go.md` de cette branche.

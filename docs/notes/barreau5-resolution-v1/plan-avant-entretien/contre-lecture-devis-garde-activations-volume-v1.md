# Contre-lecture — devis de la garde des activations de la relecture du barreau 5 sur un volume de stockage — v1

- **Contre-lecteur** : Claude Opus 5.5 (`claude-opus-5-5`), sous-agent neuf de la session mère ; je n'ai écrit aucune pièce lue ici (R2). Écrit le 21 novembre 2026. Aucun appel payant, aucun appel aux interfaces de l'hébergeur ni du loueur, aucune machine créée.
- **Pièce contre-lue** : `docs/notes/barreau5-resolution-v1/plan-avant-entretien/devis-garde-activations-volume-v1.md` (`b3c8f3f898c86aec9105ca71ce188e7eeac344021a0838b3ecf5ea881049749c`), classe A.
- **Pièces lues, par leur chemin** : le programme de calcul (`calcul-devis-garde-activations-volume-v1.py`, `a3049f4b…`) et sa sortie (`sortie-calcul-devis-garde-activations-volume-v1.txt`, `2b945e67…`) ; les relevés `releve-grille-prix-hetzner-2026-11-21T1056Z-v1.json` (`58a6c6a3…`), `releve-page-publique-boites-de-stockage-hetzner-2026-11-21T1055Z-v1.html` (`02250593…`), `prereg/papier-dopamine-moniteur-v1/releve-offres-loueur-cartes-2026-11-21T1055Z-v1.json` (`bc54f8bd…`) ; le devis scellé `devis-adaptateurs-tenus-a-l-ecart-v1.md` (`dc886195…`) ; la section « Données gardées » du texte scellé `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1.md` (`bdff244f…`, l. 363-368, et la liste d'arrêt l. 355-361 qui la précède à l'écran) ; la sortie du calcul v3 du même dossier (`sortie-calcul-devis-adaptateurs-tenus-a-l-ecart-v3.txt`, sept lignes de tailles et de coûts, aucun résultat) ; `registres/go.md`, lignes GO-2026-11-19-86 et -88 ; `registres/depenses.md`, l. 422 ; `registres/arrets.md`, lignes Hetzner. Aucun résultat d'expérience ouvert.

## Verdict

**Conforme après ces corrections** : sept corrections, dont **deux bloquantes** (A-1, A-2). Les chiffres sont justes et rejoués à l'octet ; le défaut de fond est une dépense qui court au-delà de la ligne sans être écrite dans la ligne (A-1), et une coupure dont le pire cas dépend sans dire comment elle est tenue (A-2).

## 1. Empreintes et rejeu

- Les six compagnons `.sha256` (devis, calcul, sortie, deux relevés de l'hébergeur, devis scellé) et ceux du texte scellé et du relevé du loueur concordent avec les fichiers sur disque.
- Le programme ne fait aucun appel de réseau : il lit deux fichiers JSON (`json`, `math`, `sys`, `pathlib` seulement). Rejoué depuis la racine du dépôt par `.venv/bin/python -I docs/notes/barreau5-resolution-v1/plan-avant-entretien/calcul-devis-garde-activations-volume-v1.py` : sortie **identique à l'octet** (`cmp`) à la sortie versée.
- Les relevés ne portent aucune clé (recherche de « bearer », « api_key », « authorization » : rien). La grille ne contient que la clé `pricing`.

## 2. Chiffres rapportés à leurs sources, et refaits à la main

- Prix du volume, 0,0572 EUR hors taxe par Go et par mois, 0,06864 toutes taxes : grille, `pricing.volume.price_per_gb_month`. Juste.
- `cx23` à `hel1`, 0,0088 EUR hors taxe de l'heure, plafond mensuel 5,49 ; `ccx13`, 0,0585 et 36,49 : grille, `server_types`. Justes.
- Taxe de 20 % : grille, `vat_rate`. Taux de change 1,25 : convention, `registres/depenses.md` l. 422 (« taux 1,25 »), dit non relevé. Prudent (il surestime le dollar).
- Boîte de stockage de 1 To, 3,20 EUR hors taxe par mois : page publique relevée, « BX11 … € 3.20 per month, excl. VAT ; € 0.0051 per hour » ; le montant des frais d'installation n'apparaît pas dans le texte versé (« Order setup fee once », valeur servie par script) : « non vérifié » est exact.
- Tailles 152 et 166 Go, replis 44 et 4,4 Go : texte scellé l. 366 et devis scellé § 5. Justes.
- **Refaits à la main** :
  - attendu : 200 × 0,06864 = 13,728 EUR ; 12 × 0,01056 = 0,127 ; 13,855 EUR × 1,25 = **17,32 USD** ;
  - **pire cas** : 13,728 + 3 × 24 × 0,0702 = 13,728 + 5,054 = 18,782 EUR × 1,25 = **23,48 USD** ;
  - **coupure, plafond** : ⌈23,48⌉ = **24 USD** ;
  - oubli d'un `ccx13` un mois : 13,728 + 36,49 × 1,2 = 57,516 EUR = **71,90 USD** ;
  - bas : 13,728 × 9 / 30 + 6 × 0,01056 = 4,182 EUR = 5,23 USD.
  Tous égaux à la sortie.
- **Non compté** : l'adresse IPv4 publique de chaque serveur de séance, 0,0008 EUR hors taxe de l'heure à `hel1` (même grille, `primary_ips`) ; trois séances de 24 heures : 0,069 EUR toutes taxes. Le pire cas passe à 18,85 EUR, **23,56 USD** : sous le plafond de 24 (correction A-3).

## 3. Cohérence de l'attendu, du pire cas, de la coupure et de la ligne

- Attendu, pire cas et plafond se tiennent : trois séances au plus, minuterie de 24 heures, un mois de volume. La marge entre le pire cas et le plafond est de 0,44 USD après l'adresse IPv4 : suffisante, puisque le cumul est converti au taux de convention et que les séances sont bornées en nombre et en durée.
- « Trois séances au plus » (§ 3) et « du versement et de deux relectures au plus » (ligne) disent la même chose.
- La ligne tient au format à huit colonnes, sans barre verticale dans une cellule ; type « calcul » ; plafond 24 USD ; échéance 2026-12-21 ; « hors du plafond commun de GO-2026-11-19-86 » est juste (la sortie des données reste sous GO-86, § 4).
- **Défaut** : le § 3 dit « le volume est borné par l'échéance », le § 5 point 1 dit qu'au plafond « le volume reste », et le § 5 point 3 interdit toute suppression sans le mot de Lazar. À l'échéance ou au plafond, sans mot de Lazar, le volume continue d'être facturé, 0,458 EUR (0,57 USD) par jour toutes taxes, **hors de toute ligne**. La règle « récupérer ce qui est récupérable » et l'interdit de dépenser sans accord ne se concilient que si la ligne dit elle-même ce qui court après l'échéance (correction A-1).
- Petite incohérence de source : la durée du versement est donnée « pour 184 Go (devis scellé, § 2) » ; ce 184 est le chiffre du brouillon 2 resté dans la table du § 2 du devis scellé ; le brouillon 3 (même devis, § 5 ; calcul v3, ligne 3 : 155,5 Go sortis avec les ancrages, à 36 adaptateurs) donne ≈ 152 à 166 Go. Le volume de 200 Go est dimensionné sur le bon chiffre ; seule la phrase est à reprendre (correction A-5).

## 4. Dépense, conditions de départ, paiements supposés

- Aucune dépense n'est ouverte hors de la ligne, sauf la garde au-delà de l'échéance (A-1).
- Conditions de départ : ligne d'accord, ligne d'engagement au registre avant la création du volume (§ 4) ; la consigne de l'opérateur (classe B) est renvoyée au § 8. Rien ne suppose un paiement que Lazar n'a pas fait : la facture de l'hébergeur court sur le compte existant.

## 5. Ce que le devis suppose sans le dire, et ce qui le ferait déborder

1. **La minuterie** (A-2). L'hébergeur n'a pas de destruction programmée ; un serveur arrêté reste facturé. La pratique du dépôt est une minuterie locale, par PID, qui détruit par l'identifiant (`registres/arrets.md`, serveur 175838427 : « minuterie PID 2441 ») : elle vit dans la session qui a créé le serveur, avec le jeton. Si cette session tombe, la coupure tombe avec elle, et le pire cas devient l'oubli (71,90 USD par mois). Le devis doit dire où vit la minuterie, et qui vérifie qu'aucun serveur ne reste (la routine de reprise, point 4, en est le filet).
2. **Le serveur de séance remplace « le serveur du projet »** du devis scellé, § 5 (a). Les registres ne montrent que des serveurs de passage, détruits à la fin de leur tâche ; le choix est donc forcé, mais il n'est pas dit. Non bloquant ; je ne le porte pas en correction, la mère peut l'écrire à l'engagement.
3. **Débordements possibles** : une séance qui dépasse 24 heures (minuterie défaillante) ; une quatrième séance ; des activations plus grosses que 166 Go (les 200 Go laissent ≈ 15 % de marge, système de fichiers compris : au-delà, l'agrandissement d'un volume est possible chez l'hébergeur mais n'est pas sous cette ligne ; les replis s'appliquent alors, ce que le § 5 point 4 couvre) ; un taux de change réel plus haut que 1,25 (improbable).
4. **Le taux de taxe** vient du compte : « aucune donnée du projet » est presque exact ; à dire (A-7).

## 6. L'écart déclaré et la boîte de stockage

- **Grille lue par le jeton nommé** : sans effet sur les chiffres. La réponse versée ne contient que la grille publique de l'hébergeur et le taux de taxe du compte, aucun identifiant de serveur, de volume ni de projet ; le jeton n'apparaît pas. L'écart est de procédure : le mot de Lazar (R-2322) ne nomme que la liste des serveurs. La mère le consigne au registre des décisions et, si l'on veut refaire ce relevé, demande à Lazar d'étendre le mot à la lecture de la grille. Il ne change pas la conformité du devis.
- **Boîte de stockage** : la raison donnée tient, à la lettre : l'accord de principe (GO-2026-11-19-88, point 6) nomme « un volume de 200 Go », et la boîte n'est pas vérifiée (frais d'installation non lus, mode de commande non lu, possible ouverture de compte, qui est un nœud). Mais elle est quatre fois moins chère (4,80 contre 17,16 USD par mois), se lit par SFTP ou rsync sans serveur, et supprime du même coup la minuterie et le risque d'oubli. Lazar doit la voir dans la décision qu'on lui porte, comme option à vérifier, non comme option prête (A-6).

## 7. Constat du § 7 (hors objet)

Le calcul est juste, la phrase ne l'est pas : à 300 Go, **cinq** offres ne manquent que la borne du stockage (calcul, bloc 6, lignes 35 à 39), et non une. Celle à 1,163 USD de l'heure est la plus proche (0,099 USD de l'heure de stockage) ; les quatre autres affichent 1,00 USD par Go et par mois, soit 0,41 USD de l'heure. Le prix de stockage le plus bas vu (0,20) est juste, sur des offres refusées aussi pour le disque (relevé). Correction A-4.

## 8. Corrections (liste fermée)

**A-1 (bloquante) — la garde après l'échéance ou le plafond.**
- § 3, puce « Coupures » : remplacer « le volume est borné par l'échéance. » par « le volume est borné par l'échéance, hors la garde sans séance du § 5, point 2. »
- § 5, point 1 : remplacer « plus aucune séance ; le volume reste, et la mère porte la question à Lazar. » par « plus aucune séance ; le volume reste en garde sans séance, comme au point 2, et la mère porte la question à Lazar le jour même. »
- § 5, point 2 : remplacer tout le point par « 2. Le 14 décembre, une semaine avant l'échéance, la mère porte à Lazar trois issues — garder un mois de plus (ligne neuve), réduire au repli de la couche 15 (≈ 44 Go, 3,43 EUR par mois sur un volume de 50 Go), ou supprimer après inventaire scellé. Sans mot de Lazar le 21 décembre, le volume seul reste en garde, sans aucune séance, à 0,458 EUR (0,57 USD) par jour toutes taxes, compté sous cette ligne au-delà de son plafond et consigné chaque jour au registre des dépenses, jusqu'au mot de Lazar ; la mère le lui rappelle chaque jour. »
- § 9, ligne d'accord : remplacer « À l'échéance, aucune suppression sans le mot de Lazar. » par « Question portée à Lazar le 14 décembre ; après l'échéance ou au plafond, sans mot de Lazar, le volume seul reste en garde sans séance à 0,57 USD par jour, compté sous cette ligne au-delà du plafond ; aucune suppression sans le mot de Lazar. »

**A-2 (bloquante) — où vit la minuterie.** § 3, puce « Coupures » : remplacer « chaque serveur porte une minuterie de destruction à 24 heures, par identifiant (R10) ; » par « chaque serveur a une minuterie de destruction à 24 heures, par identifiant (R10), tenue hors du serveur, qui ne porte pas le jeton : un processus de la session qui l'a créé, par son PID, comme pour les serveurs de l'essai Lean (`registres/arrets.md`) ; un arrêt du système du serveur ne suffit pas, un serveur arrêté reste facturé ; à la fin de chaque séance, puis à chaque reprise (routine, point 4), la liste des serveurs du projet est relue par identifiants, et tout serveur sans tâche est détruit et consigné ; si la session qui tient la minuterie tombe, la session suivante détruit le serveur dès sa reprise ; » — et au § 3, puce « Ce que la minuterie évite », ajouter à la fin : « C'est le débordement qui reste si la minuterie et la routine de reprise manquent toutes deux. »

**A-3 — l'adresse IPv4 des serveurs de séance.** § 2, puce « Prix du serveur » : ajouter à la fin « Chaque serveur porte aussi une adresse IPv4 publique, 0,0008 EUR hors taxe de l'heure à `hel1` (même grille, `primary_ips`), soit 0,069 EUR toutes taxes pour trois séances de 24 heures, non comptée au calcul : le pire cas passe à 18,85 EUR, 23,56 USD, sous le plafond. » ; § 3, table, ligne « pire cas sous les coupures » : remplacer « 18,78 | 23,5 » par « 18,78 (18,85 avec l'adresse IPv4) | 23,5 (23,6) ».

**A-4 — le constat du § 7.** Remplacer « Une offre à 1,163 USD de l'heure ne manque que cette borne (0,099 USD de l'heure de stockage). » par « Cinq offres ne manquent que cette borne (calcul, bloc 6) : la plus proche, à 1,163 USD de l'heure, à 0,099 USD de l'heure de stockage ; les quatre autres, de 1,056 à 1,199 USD de l'heure, affichent 1,00 USD par Go et par mois, soit 0,41 USD de l'heure. » ; et remplacer « La sortie de données de cette même offre » par « La sortie de données de l'offre à 1,163 USD de l'heure (comme des quatre autres) ».

**A-5 — la taille du versement.** § 3, dernière puce : remplacer « 0,5 à 1,7 heure pour 184 Go (devis scellé, § 2), » par « 0,5 à 1,7 heure pour 184 Go (devis scellé, § 2, chiffre du brouillon 2 resté dans sa table ; ≈ 152 à 166 Go au brouillon 3, même devis, § 5 : plutôt moins), ».

**A-6 — la boîte de stockage dans la décision.** Paragraphe « Pour Lazar, en une décision », après « (c) Le repli sans dépense : une action sur dix. », insérer : « (d) À vérifier avant d'être proposée : une boîte de stockage de 1 To chez le même hébergeur, 4,80 USD par mois toutes taxes, lue sans serveur ni minuterie ; ce n'est pas la ressource de l'accord de principe, ses frais d'installation et sa commande ne sont pas vérifiés, et une ouverture de compte serait un nœud. »

**A-7 — le taux de taxe vient du compte.** En-tête, puce « Comment la grille a été relevée » : remplacer « la réponse ne contient que des prix publics, aucune donnée du projet. » par « la réponse ne contient que des prix publics et le taux de taxe du compte (20 %), aucune donnée du projet. »

## 9. Ce qui n'est pas une correction

- La recommandation (a), confiance 0,75, et l'absence de défaut (c'est une dépense) sont conformes à la hiérarchie de décision.
- Le constat du § 7 sur le marché des cartes (aucune offre aux bornes à 300 Go à 10:55Z) est utile à la session de lecture ; il ne touche pas cette ligne. À noter pour elle : si la relecture a lieu après le 30 novembre, la sortie des données comptée sous GO-2026-11-19-86 sort de l'échéance de cette ligne-là.

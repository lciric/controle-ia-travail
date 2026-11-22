# Vérification courte du devis de la tranche de l'ajustement de nos lentilles (B-β) de la lecture par lentille neuronale — passage de la v9 à la v10 — vérificateur neuf (R2)

- **Objet** : `docs/notes/neuron-lens-v1/devis-b-beta/devis-tranche-b-beta-v10.md` (625 lignes, lues en entier), comparé à la v9 (`diff`, 175 lignes de différence) et à `verification-courte-devis-tranche-b-beta-v9.md`.
- **Empreinte vérifiée** : `sha256sum -c devis-tranche-b-beta-v10.md.sha256` : OK (`ab25fbae…`). Tous les compagnons `.sha256` du dossier : OK.
- **Date** : 2026-11-18T02:41Z (`date -u`, à l'écriture du rapport).
- **Conduite** : lecture seule. Grille v10 rejouée par `python3 -I -B` (code 0, aucun `__pycache__` après coup). Aucune commande du loueur, aucun réseau, aucune variable d'environnement affichée, rien exécuté du dépôt voisin, rien lu de `diag/` ni de `registres/`. Seule la garde de dépense a été lue, dans l'arbre de lecture. Le vérificateur neuf n'a écrit aucune version du devis ni aucune relecture. Ce rapport n'a pas de compagnon `.sha256` (à sceller par la session).

## Verdict

**À corriger** : 0 bloquante, 1 majeure, 5 mineures.

Les chiffres neufs sont justes : la grille se rejoue à l'identique et les cellules du devis sont celles de la sortie. Les deux majeures de la v9 sont réglées dans le corps. Reste une majeure sur la proposition du prix lu déclaré à la garde, dont le risque n'est pas dit, et cinq mineures, dont deux « acceptée » du § 14 qui sont partielles.

## Points

### Majeure

| n° | lieu | constat vérifié sur pièce | correction proposée |
|---|---|---|---|
| **M-1** | § 5, ligne « minuterie v4 et garde v4 » (proposition du prix lu) ; § 7, décision 1, « Marges » | La proposition est mécaniquement exacte (`garde_depense_v4.py` l. 88 : `max(prix_declare, lu)` ; l. 44-51 : dépense = heures × prix + frais fixes ; minuterie = (0,9 × plafond − frais fixes) / prix × 3600). Si le prix lu monte après la création, la garde le suit, et recompte toute la durée écoulée à ce prix : prudent. **Risques non dits** : (i) si la lecture échoue (l. 86-88 : exception, sortie vide, `nan`), la garde retombe sur le prix déclaré ; avec le prix lu à la création, une hausse survenue pendant cette panne n'est plus vue, alors qu'avec le prix exigé déclaré elle restait bornée ; (ii) la proposition ne dit pas quoi déclarer si la lecture à la création elle-même échoue ; (iii) la lecture de la garde est `dph_total` de l'instance (l. 120 ; le docstring l. 13 dit « stockage compris », non vérifiable sans location), alors que le prix de la décision est `dph_total` + stockage de 200 Go : le devis (§ 3, notes de méthode) ne note que 5 Gio déjà comptés, et la v9 rangeait l'identité des deux prix parmi le non vérifiable ; un prix lu sans le stockage serait sous-déclaré. Or le texte dit « la dépense reste bornée en dollars par l'arrêt dur », sans condition. | Une phrase de réserve au § 5 : borne vraie seulement si la lecture du prix aboutit et si le prix lu sur l'instance compte le stockage (à vérifier à la création, avant tout départ) ; règle pour une lecture ratée à la création (déclarer le prix exigé, ou ne pas partir). Dire la contrepartie du prix exigé déclaré : plus sûr, mais tronque la course. |

### Mineures

| n° | lieu | constat vérifié sur pièce | correction proposée |
|---|---|---|---|
| **m-1** | § 4, « Perte possible » (l. 294-295) ; § 3, « Autres cartes » (l. 251) | Restes de la v9 non repris, dits « acceptés » au § 14 par la seule phrase « cas de calcul » du début du § 3 : « borné par l'arrêt dur (79,2 USD, v6) » (73,8 à 82 ; 61,2 à 68), « ≈ 51 USD (17,1 h ; ≈ 45 à 2,62) » (avec les copies vers L2), « prix minimal 2,11 » (2,02 avec L1 et 82). Le renvoi général est une réponse partielle. | Ajouter « (cas L2 et 88)» aux trois endroits, ou donner la valeur de L1. |
| **m-2** | § 4, avant « Plafond de la v6 » (l. 313) et « à confirmer par lui » (l. 316) | « Le prix exigé reste celui du plan v1 (3,00) » et « à confirmer par lui » sont inchangés ; la v10 n'a ajouté que la phrase « cas de calcul ». Le § 14 dit « même phrase » : la correction est partielle. La décision 1 elle-même est neutre. | Écrire « à trancher par lui (décision 1) » et retirer « reste celui du plan v1 », ou dire que 3,00 est la lecture de la v6, non décidée. |
| **m-3** | § 7, décision 1, option (1a) | Le mot dit « monte le plafond ». L'option (1a) garde 2,25 et **baisse** le plafond à 62 (« le plafond le plus bas »). La lecture « le prix reste 2,25, le plafond de dépense monte » n'a pas d'option propre ; la v9 (M-2) demandait « 62 ou 68 gardés ». Les conséquences sont justes (Japon seul aux deux relevés ; avantage et inconvénient écrits). | Ajouter « ou 68 gardés » à (1a), avec sa marge (0,9 × 68 − 55,2 = 6,0 USD), ou une option (1a bis). |
| **m-4** | § 7, décision 1, « Marges » (fin) | « **Recommandation technique, indépendante du sens du mot** : déclarer à la garde le prix lu à la création » : la phrase ne dit pas « à trancher dans la commande avec l'accord de la mère et de Lazar », que le § 5 dit. Au § 7 elle se lit comme une recommandation en forme, dans un nœud qui promet « aucune recommandation ». Le sens du mot reste neutre ; la neutralité est donc tenue sur le mot, moins sur le reste. | Écrire « proposition, à trancher dans la commande (§ 5) » ; ajouter la réserve de M-1. |
| **m-5** | § 7, option (b), colonne « pire cas et plafond » | Les six paires sont exactes (sortie, section B, L1 : 45 ; 47 — 48 ; 50 — 50 ; 52 — 52 ; 55 — 59 ; 63 — 83 ; 88), mais la chaîne « 45 ; 47 à 2,25 — 48 ; 50 à 2,39 — 50 ; … » met un prix après la paire, et « 45 » seul n'a pas de prix visible : illisible. | Une ligne par prix, ou « 2,25 : 45 ; 47 (relance) ». |

## Reprise de la table du § 14, ligne par ligne

| ligne | jugement | constat |
|---|---|---|
| M-1 marge quasi nulle ; garde au prix exigé | **faite, avec réserve** | § 4 : table avec marges (toutes recalculées ; maximum 0,88), phrase fausse retirée, « quasi nulle par construction (moins de 0,9 USD) » exact ; plafond « avec une relance » donné par option ; décision 1 : marges et plafonds avec une relance. Le prix déclaré est bien devenu une proposition au § 5, mais sa réserve manque (M-1 ci-dessus). |
| M-2 option au prix du mot (2,25) | **faite, avec réserve** | Option (1a) présente, chiffres justes (62, 0,58 ; 64, 0,12 ; L2 67 et 70 ; Japon aux deux relevés). Réserve : m-3. |
| m-1 restes de L2 et de 88 | **partielle** | Seule la phrase « cas de calcul » (§ 3). Restes locaux intacts (m-1 ci-dessus). |
| m-2 ancrage sur la lecture de la v6 | **partielle** | « même phrase » : le corps garde « à confirmer par lui » et « reste celui du plan v1 » (m-2 ci-dessus) ; décision 1 neutre : faite. |
| m-3 restes qui disent la borne haute décidée | **faite** | En-tête (paragraphe de la v8) et § 12, ligne m-15 portent « ramenée en v9 au rang de proposition ». Aucun autre reste trouvé. |
| m-4 « vingt-cinq minutes » ; « une offre » | **faite** | « vingt-quatre » (bilan et règle du relevé) ; « au moins une offre … (deux à 02:22Z avec L1) ». Aucune occurrence de « vingt-cinq minutes » (grep). |
| m-5 seuil du banc de R seule | **faite** | « 13,1 h (R seule, 1 000 passages, 6,56 h) ». |
| m-6 minuterie de (b) au pire cas ; rappels de L2 | **faite** | § 7 (b) : 17,37 h pour 17,31 h (recalculé : (53,1 − 1,0)/3,00 = 17,37) ; rappels suivent le « cas de calcul ». |
| m-7 plafonds de (b) | **faite** | Six prix, valeurs exactes ; forme illisible (m-5 ci-dessus). |
| m-8 « recopiée telle quelle » ; en-têtes ; `-B` | **faite** | « extraites » ; première ligne de la sortie dite ajoutée à la main (vérifié : seule différence de `diff`) ; mention de `-B` au § 3. Le docstring des essais n'est pas modifié, dit en toutes lettres. |
| m-9 heures attendues avec L1 ; docstring | **faite** | 8,9 − 0,2 − 0,2 = 8,5 ; 13,4 − 0,2 − 0,3 = 12,9 ; docstring de la grille v10 corrigé (« dérivées par la fille »). |
| m-10 options du script v3 en dur | **faite** | § 3 et § 5 : six couples, autre couple = version suivante. |

## Conforme

1. **Grille v10** : code 0 ; sortie identique à `grille-devis-b-beta-v10-sortie.txt`, hors la ligne d'en-tête ajoutée à la main. Aucun `__pycache__`.
2. **Recalculs à la main** : marge L1 à 3,00 : 0,9 × 82 − 73,3 = 0,5 ; avec une relance 76,5 − 76,3 = 0,2 ; marge L3 relance : (25,6 × 3,00 + 1,68 = 78,48) sous 79,2 = 0,72 ; heure d'arrêt de la garde, prix exigé déclaré : (73,8 − 1,0)/3,00 = 24,27 h pour un pire cas de 24,1 h ; prix lu : (73,8 − 1,0)/2,038 = 35,7 h (Japon), 26,5 h (Montana : 72,8/2,7514) ; offre recevable : prix minimal à 82 = 72,8/36 = 2,02 (Japon 2,038 passe), à 85 = 75,5/36 = 2,097 (Japon écarté : l'ajout de la cellule (1d) est exact) ; marge (1b) 61,2 − 61,01 = 0,19 ; (1b') 61,2 − 60,99 = 0,21 ; attendus (b) 5,65 à 8,7 h et 11,5 à 17,7 USD au Japon.
3. **Table du § 4 avec marges** : dix-huit lignes de la section A, toutes identiques ; « moins de 0,9 USD » vrai.
4. **Décision 1** : colonnes « recevables » aux deux relevés conformes à la section D (refus, plafond minimal) ; budget de 100 euros (115 USD : 1,15 ; 123 USD : 1,23) exact. Sens du mot : aucune recommandation écrite dans l'énoncé ni dans la table.
5. **Restes cherchés et non trouvés** : phrase « marge propre à L2 » (retirée, dite fausse) ; « marge large aux offres vues » (remplacée, conditionnée au prix lu déclaré) ; borne haute dite décidée ; « vingt-cinq minutes ».
6. **Empreintes** : v9 `e7328ff3`, vérification de la v9 `33d26f80`, grille v10 `0f7f2f32`, sortie `bced6051` : tous exacts contre leurs compagnons. Lignes de la garde citées (l. 88 ; durée l. 48-51) exactes.

## Non vérifiable

- L'identité du prix lu sur l'instance (`dph_total`) avec le prix de recherche stockage compris : sans location, impossible (voir M-1).
- Le mot de Lazar lui-même et les demandes de la mère (journaux et registres non lus ici).
- Le taux de change du jour ; la part du budget journalier déjà prise.
- Les gardes « à dériver » et « à écrire » (aucun code) ; le comportement du loueur en cas de hausse de prix d'une instance en cours.

## Verdict

**À corriger** — 0 bloquante, 1 majeure, 5 mineures.

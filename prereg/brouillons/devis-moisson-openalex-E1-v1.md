# Devis de la moisson OpenAlex d'E1′ (base de ponts) — v1

**Statut : devis, non scellé ; ce n'est pas un GO.** Il chiffre la dépense dont Lazar a donné l'accord de principe (R-729, 31 octobre 2026, 11:22 UTC : « go » sur une dépense si la moisson dépasse l'allocation gratuite). Il est à porter à Lazar pour le **montant et le plafond**, puis à inscrire en ligne de GO dans `registres/go.md`. **Aucune moisson avant le scellement d'E1′** (R1).

- Rédacteur : sous-agent neuf Opus 5.5 (`claude-opus-5-5`), lignée conv-audit, 31 octobre 2026 (11:35 UTC au début de la rédaction). Rien téléchargé, aucune requête à OpenAlex, rien lu sous `donnees/`.
- Pièces liées : préenregistrement `prereg/brouillons/preenregistrement-E1-base-de-ponts-v1-brouillon2.md` ; protocole `prereg/brouillons/protocole-construction-base-de-ponts-E1-v1-brouillon2.md` (étapes C0.3, C1, C3, garde G-C19) ; calcul `calcul-puissance-E1-base-de-ponts-v1-brouillon2.py` et sa sortie (§ 6, charge de lecture).
- Convention : **SUPPOSÉ** = valeur posée par le rédacteur, non lue sur une source ; « lu » = lu sur la source citée, le 31 octobre 2026.

## Sources des prix et des tailles

| Donnée | Valeur | Source |
|---|---|---|
| Allocation gratuite avec clé | 1 USD par jour, remise à zéro à minuit UTC | lu : `https://developers.openalex.org/api-reference/authentication.md` ; billet « New Features and Usage-Based Pricing », `https://blog.openalex.org/?p=3953` (24 février 2026) |
| Requête de liste ou de filtre | 0,0001 USD (0,10 USD les 1 000) | lu : mêmes pages |
| Requête de recherche par mots | 0,001 USD | lu : mêmes pages |
| Lecture d'une entité par identifiant | gratuite | lu : mêmes pages |
| Résultats par page | 100 au plus (`per_page=100`) | lu : page d'authentification |
| Au-delà de l'allocation | solde prépayé débité automatiquement ; achat par carte, montant libre ; erreur 429 sans solde | lu : mêmes pages |
| Coût par réponse | en-tête `X-RateLimit-Credits-Used` et champ `meta.cost_usd` | lu : page d'authentification |
| Instantané complet | gratuit, sans compte AWS ; transfert payé par le programme de données ouvertes d'AWS | lu : `https://developers.openalex.org/download/download-to-machine.md` |
| Instantané du 14 octobre 2026, œuvres (JSON Lines compressé) | 464 765 485 œuvres, 675,3 Go, 1 898 fichiers (≤ 0,985 Go chacun), partitionnés par `updated_date` (pas par revue) | manifeste versé sur `origin/main` : `docs/notes/gu-krenn-v1/sources-amont-v1/openalex-instantane-metadonnees-v1/manifest-jsonl-2026-10-14.json` `2b3d611b3ec93912b7b655ee139310936048a689c0f3508052a73af03a6c453f` (compagnon conforme) ; README `266047b6956f6dc3af4fb972ed1750345832de67769e43fed3c3f1b4da096fa3` |
| Même instantané, Parquet | 744,0 Go pour les œuvres | `manifest-parquet-2026-10-14.json` `5abb166c4ae115f8aac56021dbc1eed823e044b48406af146537485fba7f03cc` |
| Entité `sources` de l'instantané | 268 629 sources, 0,36 Go | manifeste JSON Lines ci-dessus |
| Coût observé d'une moisson passée | 0,99 USD de crédits gratuits pour 197 681 œuvres (≈ 5,0 USD par million) | R-863, `registres/decisions.md` de `origin/main` |

**Écart non expliqué.** Au tarif lu (0,0001 USD la page de 100), la moisson de R-863 aurait coûté environ 0,20 USD, non 0,99. Causes possibles (SUPPOSÉ) : pages plus petites que 100, requêtes de recherche ou de comptage, reprises, ou plafond journalier atteint par d'autres appels. Le devis porte donc deux taux : **tarif lu** (1,0 USD par million d'œuvres) et **taux observé** (5,0 USD par million). Le pilote (C0.3) tranche avant toute dépense.

## Besoin (fixé par le protocole brouillon 2)

- **Revues** : 700 (500 du palier 1 + deux paliers d'extension de 100), sciences physiques si DE-10 = (a), activité de 60 à 2 000 œuvres par an chaque année de 1995 à 2008.
- **Années** de publication : 1995 à 2023 (29 ans) ; les fenêtres les plus anciennes (historique de nouveauté rétrodit de t = 2009) commencent en 1995, les plus récentes (événement prospectif de t = 2021) finissent en 2023.
- **Types** : article, revue de littérature.
- **Champs** : `id`, `doi`, `publication_date`, `publication_year`, `type`, `language`, `is_retracted`, `title`, `abstract_inverted_index`, `referenced_works` (pour le canal C), `primary_location`, `updated_date` ; **`authorships`** (identifiants d'auteurs) si DE-11 ≠ (c) (distance sociale par cosignature, antériorité ASIS&T 2025). Ce champ ne change pas le nombre de pages (donc le coût) ; il grossit le disque d'environ 30 % (SUPPOSÉ).
- **Cadre** : liste des sources de type revue (C1.1), comptes par année de 1995 à 2008 pour les candidates contrôlées dans l'ordre (C1.4), comptes de 1995 à 2023 des 700 retenues (C1.5).

## Volume (SUPPOSÉ)

Moyenne d'œuvres par revue et par an sur 1995–2023, sous la règle d'activité et le plafond de 2 000 par an jusqu'en 2008 (les revues grossissent après 2008 ; aucune donnée lue) :

| Scénario | Moyenne par revue et par an | Œuvres (700 × 29 ans × moyenne) |
|---|---|---|
| bas | 150 | 3,0 millions |
| **central** | **250** | **5,1 millions** |
| pessimiste | 500 | 10,2 millions |

Le compte exact sera connu **avant** la moisson (C1.5 : une requête de groupement par revue), donc le coût aussi (C0.3).

## Requêtes (voie A, interface avec clé)

| Étape | Requêtes | Coût au tarif lu |
|---|---|---|
| C1.1 liste des sources `type = journal` (≤ 268 629 / 100) | ≤ 2 700 | ≤ 0,27 USD |
| C1.4 activité 1995–2008, revues candidates contrôlées dans l'ordre jusqu'à 700 acceptées (taux d'acceptation 15 à 30 %, SUPPOSÉ ; groupement facturé comme une liste, SUPPOSÉ) | 2 300 à 4 700 | ≤ 0,47 USD |
| C1.5 comptes 1995–2023 des 700 retenues | 700 | 0,07 USD |
| C0.3 pilote (une revue) | ≈ 30 | inclus ci-dessous |
| C3 moisson, pages de 100 (bas / central / pessimiste) | 30 000 / 51 000 / 102 000 | 3,0 / 5,1 / 10,2 USD |
| reprises (10 %, SUPPOSÉ) | 3 000 / 5 100 / 10 200 | 0,3 / 0,5 / 1,0 USD |
| **Total** | **≈ 39 000 / 64 000 / 120 000** | **≈ 4,1 / 6,4 / 12,0 USD** |

## Voies comparées

| Voie | Coût en dollars | Durée | Machine | Avantages | Inconvénients |
|---|---|---|---|---|---|
| **A1 — interface avec clé, solde prépayé, une journée** | tarif lu : **≈ 5,4 USD** attendu (central, moins 1 USD gratuit), 3,1 à 11,0 ; taux observé : ≈ 31 USD central, ≈ 59 pessimiste | 1 à 4 heures de requêtes (10 à 20 requêtes par seconde, SUPPOSÉ ; limite lue : 100 par seconde), une demi-journée avec pilote et contrôles | aucune (session qui porte la clé, DE-8) ; disque 4 à 15 Go (≈ 0,7 à 1,45 Ko par œuvre compressée, d'après 1 453 octets par œuvre complète dans l'instantané) | une seule date d'extraction ; code de R-863 réutilisable (tri par date, curseur) ; coût connu avant la moisson ; garde par `cost_usd` | dépense (petite) ; dérive d'OpenAlex possible entre deux extractions (aucune autre n'est prévue) |
| A0 — interface avec clé, allocation gratuite seule | 0 USD | 4 à 12 jours (10 000 pages par jour au plus, allocation partagée avec les autres sessions qui portent la même clé : R-863 l'a épuisée le 31 octobre) | aucune | aucune dépense | extraction étalée sur des jours (plusieurs dates) ; dépend des autres usages de la clé |
| B — instantané public S3 du 14 octobre 2026 | 0 USD pour OpenAlex et le transfert ; machine louée ≈ 0,08 USD par heure (prix du devis de machine jetable de R-863, non relu ici : SUPPOSÉ), soit ≈ 1 à 2 USD | 675 Go à lire en entier (partition par `updated_date`, pas par revue) : 2 à 8 heures de transfert à 25–100 Mo/s, plus 3 à 6 heures de décompression et de filtrage par revue (SUPPOSÉ) ; 0,5 à 1,5 jour avec l'écriture du code | soit cet environnement (25 Go libres suffisent en flux ; accès à S3 par le mandataire **non vérifié**), soit une machine louée (location = nœud) | version datée et figée, manifeste avec comptes par fichier ; rejouable par un tiers ; aucun coût d'interface | code neuf (flux sur 1 898 fichiers, filtre par source) ; contrôle de complétude par revue moins direct (comparer aux comptes de C1.5 pris par l'interface) ; transfert 130 fois plus gros que le besoin |

## Coût attendu et plafond proposé

- **Attendu (voie A1)** : **≈ 5,4 USD** (volume central, tarif lu, après déduction de l'allocation du jour) ; fourchette 3 à 11 USD au tarif lu.
- **Si le taux observé de R-863 est le vrai** : ≈ 31 USD (central), ≈ 59 USD (pessimiste).
- **Plafond proposé : 35 USD**, toutes requêtes de la moisson d'E1′ comprises. Il couvre le volume central même au taux observé et le volume pessimiste au tarif lu. Il ne couvre pas le volume pessimiste au taux observé : dans ce cas, le pilote et la projection de C0.3 arrêtent **avant** la moisson, et un devis nouveau est écrit.
- **Garde** (G-C19) : somme des `meta.cost_usd` relue à chaque réponse ; arrêt à 95 % du plafond (33,25 USD), avant la requête suivante ; aucune moisson partielle n'est exploitée (la reprise est complète, R12). Testée sur un cas sain et un artefact (R5) avant la première requête.
- **Achat** : solde prépayé de 35 USD au plus, par Lazar (compte, nœud) ; le solde non dépensé reste sur le compte (lu : il n'expire pas chaque jour).

## Charge de lecture des lecteurs (sous-agents ; aucune dépense en dollars si DE-3 = (a), mais à chiffrer)

D'après le § 6 du calcul (modèle par paire, SUPPOSÉ ; plafond de 10 candidats par paire, cas et témoins ; trois portions de 200, 200 et 100 ponts) :

| Grandeur | Fourchette |
|---|---|
| Lectures de la base (deux lecteurs) | 19 132 à 93 268 (hors fixes) |
| Lectures fixes (étalonnage 2 × 200, et 2 × 200 si révision ; audit 60 ; masquage 2 × 30 ; exclusion des revues pluridisciplinaires 2 × 700 noms) | ≈ 1 900 à 2 300 |
| **Appels de sous-agent** (lots de 50 paquets, un lecteur par appel) | **≈ 430 à 1 910** |
| Jetons d'entrée (≈ 450 par paquet + 700 de consigne par appel, SUPPOSÉ) | ≈ 10 à 44 millions |
| Jetons de sortie (≈ 70 par paquet, SUPPOSÉ) | ≈ 1,5 à 6,7 millions |
| Si DE-3 = (b), lecteurs payants (prix SUPPOSÉ : 3 USD par million de jetons d'entrée, 15 USD par million de sortie, à relire sur la grille du fournisseur) | ≈ 50 à 235 USD — **hors de ce devis**, devis séparé si (b) |

Le plafond de lectures S17 (recommandé : 60 000 lectures, ≈ 1 200 appels) arrête la base si la charge mesurée sur E₁ projette davantage (protocole C7.8). La moitié basse de la fourchette (rendement des paires signalées ≥ 0,08) tient sous ce plafond ; la moitié haute (rendement ≈ 0,04 à 0,07) non.

## Décision à soumettre à Lazar (nœud de dépense : aucun défaut à 48 heures)

- **Décision** : voie et plafond de la moisson d'E1′.
- **Enjeu** : la base de ponts exige une moisson unique et figée de 3 à 10 millions d'œuvres ; elle ne se lance qu'après scellement d'E1′.
- **Options** :
  - **A1 — interface, solde prépayé, plafond 35 USD.** Avantage : une journée, une date d'extraction, coût connu avant la moisson. Inconvénient : dépense de l'ordre de 5 USD (jusqu'à 35).
  - **A0 — interface, allocation gratuite seule.** Avantage : 0 USD. Inconvénient : 4 à 12 jours, extraction étalée, concurrence avec les autres usages de la clé.
  - **B — instantané S3.** Avantage : version figée et rejouable, 0 USD d'interface. Inconvénient : 675 Go à lire, code neuf, machine louée probable (nœud), accès par le mandataire non vérifié.
- **Recommandation : A1, plafond 35 USD, confiance 0,65.** B garde sa valeur pour une réplication publique ultérieure.

## Réserves

- Volume SUPPOSÉ (aucun compte lu) ; il sera exact avant la moisson (C1.5).
- Facturation des requêtes de groupement par année supposée identique à une liste (SUPPOSÉ) ; profondeur des `counts_by_year` des sources non vérifiée, d'où les requêtes de groupement.
- L'écart entre le tarif lu et le coût observé de R-863 n'est pas expliqué ; le plafond le couvre au volume central seulement.
- Le prix horaire de la machine (voie B) vient d'un autre devis (R-863), non d'une page lue par le rédacteur.
- Le nombre de revues (700) dépend de DE-10 et de S10 ; un autre périmètre change le volume dans la même proportion.
- Les jetons par paquet et les prix des lecteurs payants sont SUPPOSÉS.

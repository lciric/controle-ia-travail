# Devis de la moisson OpenAlex d'E1′ (base de ponts) — v2

**Statut : devis, non scellé ; ce n'est pas un GO.** Il chiffre la dépense dont Lazar a donné l'accord de principe (R-729, 31 octobre 2026, 11:22 UTC : « go » sur une dépense si la moisson dépasse l'allocation gratuite). Il est à porter à Lazar pour la **voie, le montant et le plafond**, puis à inscrire en ligne de GO dans `registres/go.md`. **Aucune moisson avant le scellement d'E1′** (R1). Nœud de dépense : aucun défaut à 48 heures.

- Rédacteur de la v2 : sous-agent neuf Opus 5.5 (`claude-opus-5-5`), lignée conv-audit, rédacteur de reprise, 31 octobre 2026 (≈ 13:00 UTC). Rien téléchargé, aucune requête à l'interface d'OpenAlex, rien lu sous `donnees/`, aucun `git fetch`.
- **Base** : `devis-moisson-openalex-E1-v1.md` (`36153c96912e8b9cfef314534182e62233a05c3cfd9efe9dfd2726b00103f7da`), écrit par le premier rédacteur du brouillon 2 (non scellé, non relu), laissé en place sans modification (R12). La v2 reprend ses chiffres après vérification et ne change que les points ci-dessous.
- Pièces liées : préenregistrement `prereg/brouillons/preenregistrement-E1-base-de-ponts-v1-brouillon2.md` ; protocole `prereg/brouillons/protocole-construction-base-de-ponts-E1-v1-brouillon2b.md` (étapes C0.3, C0.6, C1, C3, gardes G-C19 à G-C21) ; calcul `calcul-puissance-E1-base-de-ponts-v1-brouillon2.py` (`4e87c110d492524d19fc6ccbcf2fb7d1db44cbad4e4d724f47171ab68e590dc8`) et sa sortie `….sortie.txt` (`e99582ef4d4e6aac39abbd962720ffbbe59514b40f0ab9704acdc3a63a38b8f9`, § 6 : charge de lecture).
- Convention : **SUPPOSÉ** = valeur posée par le rédacteur, non lue sur une source ; « lu » = lu sur la source citée, le 31 octobre 2026.

## Ce qui change par rapport à la v1

| Point | v1 | v2 | Motif |
|---|---|---|---|
| Cadre (C1.4) | une requête de groupement par revue candidate (activité) | **deux** requêtes (activité ; part d'œuvres avec résumé sur 2003–2008), taux d'acceptation plus bas (10 à 25 %, SUPPOSÉ) : 5 600 à 14 000 requêtes au lieu de 2 300 à 4 700 | protocole 2b, C1.4 (disponibilité, constat CE1-07) |
| Charge de lecture | trois portions de 200, 200 et 100 ponts | les deux tailles de la décision DE-4 : 500 ponts (200 + 200 + 100) et **750 ponts** (300 + 300 + 150, recommandée) ; plafond de lectures S17 = 60 000 ou 90 000 | préenregistrement brouillon 2, DE-4 |
| Seuil de rendement sous le plafond | « rendement ≥ 0,08 » | « rendement ≥ 0,077 (plafond de 10 candidats) », lu sur la sortie | précision |
| Sources | prix lus par le premier rédacteur | **relus** par le rédacteur de la v2 sur les mêmes pages (concordants) ; facturation des groupements toujours non écrite (SUPPOSÉ) | R7, R11 |
| Totaux | ≈ 4,1 / 6,4 / 12,0 USD | ≈ 4,2 / 6,9 / 13,0 USD au tarif lu ; plafond inchangé (35 USD) | requêtes du cadre |

## Sources des prix et des tailles

| Donnée | Valeur | Source |
|---|---|---|
| Allocation gratuite avec clé | 1 USD par jour, remise à zéro à minuit UTC ; 0,10 USD par jour sans clé | lu : `https://developers.openalex.org/api-reference/authentication.md` ; billet « New Features and Usage-Based Pricing », blog d'OpenAlex, 24 février 2026 (page de catégorie `https://blog.openalex.org/category/openalex`) |
| Requête de liste ou de filtre | 0,0001 USD (0,10 USD les 1 000) | lu : mêmes pages |
| Requête de recherche par mots | 0,001 USD (1 USD les 1 000) | lu : mêmes pages |
| Lecture d'une entité par identifiant | gratuite | lu : mêmes pages |
| Requête de groupement (`group_by`) | **non écrite** sur ces pages ; facturée comme une liste (SUPPOSÉ) | lu (absence) : page d'authentification |
| Résultats par page | 100 au plus (`per_page=100`) | lu : page d'authentification |
| Débit | au-delà de 100 requêtes par seconde, erreur 429 | lu : page d'authentification |
| Au-delà de l'allocation | solde prépayé, « pool » séparé qui prend le relais quand l'allocation du jour est dépensée ; achat par carte, montant libre ; le solde « n'expire pas chaque jour » | lu : page d'authentification ; billet du 24 février 2026 |
| Coût par réponse | en-tête `X-RateLimit-Credits-Used` et champ `meta.cost_usd` ; point d'accès `/rate-limit` (soldes) | lu : page d'authentification |
| Instantané complet | gratuit, sans compte AWS ; frais de transfert (≈ 70 USD par téléchargement) payés par le programme de données ouvertes d'AWS ; commande `aws s3 sync "s3://openalex" … --no-sign-request` | lu : `https://developers.openalex.org/download/download-to-machine.md` |
| Instantané du 14 octobre 2026, œuvres (JSON Lines compressé) | 464 765 485 œuvres, 675,3 Go, 1 898 fichiers (≤ 0,985 Go chacun), partitionnés par `updated_date` (pas par revue) ; 1 453 octets par œuvre en moyenne | manifeste versé sur `origin/main` : `docs/notes/gu-krenn-v1/sources-amont-v1/openalex-instantane-metadonnees-v1/manifest-jsonl-2026-10-14.json` `2b3d611b3ec93912b7b655ee139310936048a689c0f3508052a73af03a6c453f` (compagnon conforme) ; README `266047b6956f6dc3af4fb972ed1750345832de67769e43fed3c3f1b4da096fa3` |
| Même instantané, Parquet | 744,0 Go pour les œuvres | `manifest-parquet-2026-10-14.json` `5abb166c4ae115f8aac56021dbc1eed823e044b48406af146537485fba7f03cc` |
| Entité `sources` de l'instantané | 268 629 sources, 0,36 Go | manifeste JSON Lines ci-dessus |
| Identifiants d'auteurs | profils fusionnés ou scindés en avril et mai 2026 | notes de version de l'instantané, `RELEASE_NOTES-openalex-s3.txt` `a6e5083e10f0992f357ae5eeff338c423dfaed106c024160fe9f6db8df247b93` (même dossier) |
| Résumés absents | 40 % des œuvres sans résumé ; Elsevier, Taylor & Francis, IEEE, American Chemical Society n'avaient déposé aucun résumé dans Crossref en 2023–2024 | arXiv 2512.16434 (page HTML lue, pas de PDF empreinté : **non opposable**, R7) |
| Coût observé d'une moisson passée | 0,99 USD de crédits gratuits pour 197 681 œuvres (≈ 5,0 USD par million) | R-863, `registres/decisions.md` de `origin/main` |

**Écart non expliqué** (repris de la v1). Au tarif lu (0,0001 USD la page de 100), la moisson de R-863 aurait coûté environ 0,20 USD, non 0,99. Causes possibles (SUPPOSÉ) : pages plus petites que 100 (25 par défaut), requêtes de recherche ou de comptage, reprises, ou allocation du jour entamée par d'autres appels de la même clé. Le devis porte donc deux taux : **tarif lu** (1,0 USD par million d'œuvres) et **taux observé** (5,0 USD par million). Le pilote (C0.3) tranche avant toute dépense.

## Besoin (fixé par le protocole brouillon 2b)

- **Revues** : 700 (500 du palier 1 + deux paliers d'extension de 100), sciences physiques si DE-10 = (a) ; activité de 60 à 2 000 œuvres par an chaque année de 1995 à 2008 ; part d'œuvres avec résumé ≥ 0,5 sur 2003–2008.
- **Années** de publication : 1995 à 2023 (29 ans) ; les fenêtres les plus anciennes (historique de nouveauté rétrodit de t = 2009) commencent en 1995, les plus récentes (événement prospectif de t = 2021) finissent en 2023.
- **Types** : article, revue de littérature.
- **Champs** : `id`, `doi`, `publication_date`, `publication_year`, `type`, `language`, `is_retracted`, `title`, `abstract_inverted_index`, `referenced_works` (canal C), `primary_location`, `updated_date` ; **`authorships`** (identifiants d'auteurs), exigé par le témoin de distance sociale SOC (R-735, décision de Lazar : réseau de cosignature d'après pra2.1298, même moisson). Ce champ ne change pas le nombre de pages (donc le coût) ; il grossit le disque d'environ 30 % (SUPPOSÉ), davantage pour les œuvres à très nombreux auteurs (collaborations de physique) ; la moisson fige l'état du jour des identifiants d'auteurs.
- **Cadre** : liste des sources de type revue (C1.1) ; pour les candidates contrôlées dans l'ordre, comptes par année de 1995 à 2008 et part d'œuvres avec résumé sur 2003–2008 (C1.4) ; comptes de 1995 à 2023 des 700 retenues (C1.5).

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
| C1.4 activité 1995–2008 et couverture 2003–2008, deux requêtes par candidate, candidates contrôlées dans l'ordre jusqu'à 700 acceptées (taux d'acceptation 10 à 25 %, SUPPOSÉ ; groupement facturé comme une liste, SUPPOSÉ) | 5 600 à 14 000 | 0,56 à 1,40 USD |
| C1.5 comptes 1995–2023 des 700 retenues | 700 | 0,07 USD |
| C0.3 pilote (une revue) | ≈ 30 | inclus ci-dessous |
| C3 moisson, pages de 100 (bas / central / pessimiste) | 30 000 / 51 000 / 102 000 | 3,0 / 5,1 / 10,2 USD |
| reprises (10 %, SUPPOSÉ) | 3 000 / 5 100 / 10 200 | 0,3 / 0,5 / 1,0 USD |
| **Total** (cadre bas avec moisson basse, cadre moyen avec moisson centrale, cadre haut avec moisson pessimiste) | **≈ 42 000 / 69 300 / 129 600** | **≈ 4,2 / 6,9 / 13,0 USD** |

## Voies comparées

| Voie | Coût en dollars | Durée | Machine | Avantages | Inconvénients |
|---|---|---|---|---|---|
| **A1 — interface avec clé, solde prépayé, une journée** | tarif lu : **≈ 5,9 USD** attendu (central, moins 1 USD gratuit si l'allocation du jour n'est pas entamée), 3,2 à 12,0 ; taux observé : ≈ 29 USD central, ≈ 58 pessimiste | 1 à 4 heures de requêtes (10 à 20 requêtes par seconde, SUPPOSÉ ; limite lue : 100 par seconde), une demi-journée avec pilote et contrôles | aucune (session qui porte la clé, DE-8) ; disque 5 à 20 Go (≈ 0,7 à 1,45 Ko par œuvre compressée, d'après 1 453 octets par œuvre complète dans l'instantané, plus les auteurs ; SUPPOSÉ) | une seule date d'extraction ; code de R-863 réutilisable (tri par date, curseur) ; coût connu avant la moisson ; garde par `cost_usd` | dépense (petite) ; dérive d'OpenAlex possible entre deux extractions (aucune autre n'est prévue) |
| A0 — interface avec clé, allocation gratuite seule | 0 USD | 5 à 13 jours (10 000 requêtes de liste par jour au plus ; allocation partagée avec les autres sessions qui portent la même clé : R-863 l'a épuisée le 31 octobre) | aucune | aucune dépense | extraction étalée sur des jours (plusieurs dates d'extraction) ; dépend des autres usages de la clé |
| B — instantané public S3 du 14 octobre 2026 | 0 USD pour OpenAlex et le transfert ; machine louée ≈ 0,08 USD par heure (prix du devis de machine jetable de R-863, non relu ici : SUPPOSÉ), soit ≈ 1 à 2 USD | 675 Go à lire en entier (partition par `updated_date`, pas par revue) : 2 à 8 heures de transfert à 25–100 Mo/s, plus 3 à 6 heures de décompression et de filtrage par revue (SUPPOSÉ) ; 0,5 à 1,5 jour avec l'écriture du code | soit cet environnement (25 Go libres suffisent en flux ; accès à S3 par le mandataire **non vérifié**), soit une machine louée (location = nœud) | version datée et figée, manifeste avec comptes par fichier ; rejouable par un tiers ; aucun coût d'interface | code neuf (flux sur 1 898 fichiers, filtre par source) ; le cadre (C1) passe quand même par l'interface (≈ 1 USD) ; contrôle de complétude par revue moins direct ; transfert 130 fois plus gros que le besoin |

## Coût attendu et plafond proposé

- **Attendu (voie A1)** : **≈ 5,9 USD** (volume central, tarif lu, après déduction de l'allocation du jour) ; fourchette 3 à 12 USD au tarif lu.
- **Si le taux observé de R-863 est le vrai** : ≈ 17 USD (bas), ≈ 29 USD (central), ≈ 58 USD (pessimiste).
- **Plafond proposé : 35 USD**, toutes requêtes de la moisson d'E1′ comprises (cadre, pilote, moisson, reprises). Il couvre le volume central même au taux observé et le volume pessimiste au tarif lu. Il ne couvre pas le volume pessimiste au taux observé : dans ce cas, le pilote et la projection de C0.3 arrêtent **avant** la moisson, et un devis nouveau est écrit.
- **Garde** (G-C19) : somme des `meta.cost_usd` relue à chaque réponse ; arrêt à 95 % du plafond (33,25 USD), avant la requête suivante ; aucune moisson partielle n'est exploitée (la reprise est complète, R12). Testée sur un cas sain et un artefact (R5) avant la première requête.
- **Achat** : solde prépayé de 35 USD au plus, par Lazar (compte, nœud) ; le solde non dépensé reste sur le compte (lu : il « n'expire pas chaque jour » ; échéance éventuelle non écrite).

## Charge de lecture des lecteurs (sous-agents ; aucune dépense en dollars si DE-3 = (a), mais à chiffrer)

D'après le § 6 de la sortie du calcul (modèle par paire, SUPPOSÉ ; plafond de 10 candidats par paire, cas et témoins ; deux lignes à plafond 20 pour comparaison). La sortie porte sur 500 ponts (200 + 200 + 100) ; la colonne 750 ponts (300 + 300 + 150) est obtenue **par proportionnalité** (le modèle de charge est linéaire en M : cas lus jusqu'au M-ième validé, K × M témoins), non simulée.

| Grandeur | 500 ponts (DE-4 (b)) | 750 ponts (DE-4 (a), recommandée) |
|---|---|---|
| Lectures de la base (deux lecteurs) | 19 132 à 93 268 (plafond 10 : 19 132 à 87 052) | ≈ 28 700 à 139 900 (plafond 10 : ≈ 28 700 à 130 600) |
| Lectures fixes (étalonnage 2 × 200, et 2 × 200 si révision ; audit 60 ; masquage 2 × 30 ; exclusion des revues pluridisciplinaires 2 × 700 noms) | ≈ 1 920 à 2 320 | ≈ 1 920 à 2 320 |
| **Appels de sous-agent** (lots de 50 paquets, un lecteur par appel) | **≈ 420 à 1 910** | **≈ 610 à 2 840** |
| Jetons d'entrée (≈ 450 par paquet + 700 de consigne par appel, SUPPOSÉ) | ≈ 10 à 44 millions | ≈ 14 à 66 millions |
| Jetons de sortie (≈ 70 par paquet, SUPPOSÉ) | ≈ 1,5 à 6,7 millions | ≈ 2,1 à 10,0 millions |
| Si DE-3 = (b), lecteurs payants (prix SUPPOSÉ : 3 USD par million de jetons d'entrée, 15 USD par million de sortie, à relire sur la grille du fournisseur) | ≈ 51 à 234 USD | ≈ 75 à 347 USD |
| Plafond de lectures S17 (arrêt, version nouvelle) | 60 000 (≈ 1 200 appels) | 90 000 (≈ 1 800 appels) |

Lecture de la sortie (§ 6, plafond 10) : les mondes où une paire signalée porte une vraie reprise avec une probabilité r ≥ 0,10 (rendement d'une paire signalée ≥ 0,077) tiennent sous le plafond dans les deux tailles (au plus 54 840 lectures pour 500 ponts, ≈ 82 300 pour 750) ; les mondes à r = 0,03 (rendement 0,043 à 0,069 : 68 870 à 87 052 lectures pour 500 ponts) le dépassent. Dans ces derniers, le modèle de charge implique qu'une majorité des ponts validés seraient des faux « oui-oui » (0,01 par candidat lu, SUPPOSÉ) : le plafond S17 y joue aussi le rôle d'une garde de qualité de l'étiquette.

## Décision à soumettre à Lazar (nœud de dépense : aucun défaut à 48 heures)

- **Décision** : voie et plafond de la moisson d'E1′.
- **Enjeu** : la base de ponts exige une moisson unique et figée de 3 à 10 millions d'œuvres de 700 revues ; elle ne se lance qu'après scellement d'E1′ et GO.
- **Options** :
  - **A1 — interface, solde prépayé, plafond 35 USD.** Avantage : une demi-journée, une date d'extraction, coût connu avant la moisson (pilote). Inconvénient : dépense de l'ordre de 6 USD (jusqu'à 35).
  - **A0 — interface, allocation gratuite seule.** Avantage : 0 USD. Inconvénient : 5 à 13 jours, extraction étalée sur plusieurs dates, concurrence avec les autres usages de la clé.
  - **B — instantané S3.** Avantage : version figée et rejouable, 0 USD d'interface. Inconvénient : 675 Go à lire, code neuf, machine louée probable (nœud), accès par le mandataire non vérifié.
- **Recommandation : A1, plafond 35 USD, confiance 0,65.** B garde sa valeur pour une réplication publique ultérieure.

## Réserves

- Volume SUPPOSÉ (aucun compte lu) ; il sera exact avant la moisson (C1.5).
- Facturation des requêtes de groupement non écrite dans la documentation lue (SUPPOSÉ identique à une liste) ; nom du filtre de présence d'un résumé SUPPOSÉ (`has_abstract`), à vérifier avant la première requête (protocole C0.6).
- Taux d'acceptation des revues candidates SUPPOSÉ (10 à 25 %) ; il dépend de la couverture des résumés, qui peut être faible chez de grands éditeurs des sciences physiques (source non opposable) ; s'il est plus bas, le cadre coûte davantage de requêtes (≈ 0,0002 USD par candidate), sans changer l'ordre de grandeur.
- L'écart entre le tarif lu et le coût observé de R-863 n'est pas expliqué ; le plafond le couvre au volume central seulement.
- Le prix horaire de la machine (voie B) vient d'un autre devis (R-863), non d'une page lue.
- Le nombre de revues (700) dépend de DE-10 et de S10 ; un autre périmètre change le volume dans la même proportion.
- Charge de lecture : modèle SUPPOSÉ ; colonne 750 ponts par proportionnalité ; jetons par paquet et prix des lecteurs payants SUPPOSÉS.

# Devis — barreau 5 : familles d'adaptateurs jumeaux tenues à l'écart — v1 — brouillon 1

- Auteur : rédacteur neuf, Claude Fable 5.2, sous-agent de la session mère. Écrit le 2026-11-19 (UTC). **Brouillon, non contre-lu.** Aucune dépense, aucun lancement.
- Texte qu'il chiffre : `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-brouillon1.md` (brouillon 1).
- Arithmétique : `calcul-devis-adaptateurs-tenus-a-l-ecart-v1.py` (`27682fdf…`), sortie `sortie-calcul-devis-adaptateurs-tenus-a-l-ecart-v1.txt` (`7ce8a847…`), même dossier.
- Ce devis ne vaut accord de rien : la dépense attend son scellement et **une ligne d'accord neuve** de Lazar. L'accord `GO-2026-11-10-07` ne le couvre pas (il s'éteint à son échéance, `GO-2026-11-19-68`).

## 1. D'où viennent les chiffres (aucun n'est neuf)

- **Débits** (course du premier test sur une carte A100 SXM4 de 80 Go, cités par le préenregistrement des organismes, `prereg/T0.6-organismes-v0-v1.md`, « Devis », l. 643-649, et repris par le texte de validité de l'adaptateur, `prereg/validite-adaptateur-v1.md`, l. 206-217) : 40,2 s par épisode en lots de 8 ; 0,45 s par passe d'épisode en relecture forcée ; distillation de 480 pas, 0,23 à 0,46 heure ; mise en place 1,0 heure ; essais sur l'instance 0,6 heure (formation) ou 0,3 heure (relecture) ; poussée 0,2 heure.
- **Prix de la carte** : 1,0889 à 1,30 USD de l'heure attendus (mêmes sources) ; 1,22 relevé le 19 novembre, stockage compris (`registres/depenses.md`, ligne de l'instance 61414494) ; pire cas 1,40 avec un hôte deux fois plus lent.
- **Téléchargement** : 0,026 à 0,05 USD par Go ; 40 Go prévus par instance (configuration scellée de la course de confirmation).
- **Taille d'une série d'activations** : 1,06 Go pour 576 actions à une couche, par jeton, en demi-précision (sous-ensemble poussé par la course de confirmation ; note 04 du socle, § 3), soit ≈ 1,18 Go pour 640 actions.
- Non mesuré, supposé : le débit du réseau à la sortie de l'instance (30 à 100 Mo par seconde) ; le prix du volume de stockage (§ 5).

## 2. Ce qui est chiffré

Plan nominal du texte : huit familles tenues à l'écart à trois membres, trois familles d'apprentissage à deux membres, soit 30 adaptateurs et 11 tirages de 160 épisodes ; vérification de manipulation sur 64 tâches par adaptateur ; relecture de tous les adaptateurs sur une seule instance.

| pièce | contenu | heures de carte |
|---|---|---|
| une famille tenue à l'écart | 160 épisodes de distillation (1,79) ; trois distillations (0,69 à 1,38) ; trois fois 64 épisodes d'évaluation (2,14) | 4,62 à 5,31 |
| une famille d'apprentissage | 160 épisodes (1,79) ; deux distillations (0,46 à 0,92) ; deux fois 64 épisodes (1,43) | 3,68 à 4,14 |
| frais fixes d'une instance de formation | mise en place, essais, poussée | 1,8 |
| relecture et notation | mise en place et essais (1,3) ; textes honnêtes communs (0,71) ; par adaptateur ≈ 193 s : série nominale, modèle nu pour la divergence, recherche du facteur de norme, série à norme égale (1,61 pour 30) ; sondes et notation (0,25 à 0,6) ; téléversement de 156 Go (0,43 à 1,44) | 4,43 à 5,79 |
| répétition générale (si accordée) | toute la chaîne de relecture sur les quatre adaptateurs existants | 2,73 |

## 3. Attendu, pire cas, coupure

**Formation sur six instances en parallèle** (quatre forment deux familles tenues à l'écart ; une forme deux familles d'apprentissage ; une en forme une).

| instance | heures | attendu (USD) | pire cas (USD) | coupure (USD) |
|---|---|---|---|---|
| quatre instances à deux familles tenues à l'écart, chacune | 11,04 à 12,42 | 13,3 à 18,7 | 38,0 | **30** |
| une instance à deux familles d'apprentissage | 9,15 à 10,07 | 11,2 à 15,7 | 31,4 | **25** |
| une instance à une famille d'apprentissage | 5,48 à 5,94 | 7,3 à 10,3 | 19,8 | **15** |
| **formation, total** | **58,8 à 65,7** | **71,8 à 101,0 ; centre 87,6** | **203,1** | **160** |

Horloge : 11 à 12,4 heures si les six cartes partent ensemble.

| pièce | heures | attendu (USD) | pire cas (USD) | coupure (USD) |
|---|---|---|---|---|
| formation | 58,8 à 65,7 | 71,8 à 101,0 | 203,1 | 160 |
| relecture et notation, activations gardées en entier | 4,43 à 5,79 | 10,5 à 18,5 (dont 4,1 à 7,8 de sortie de données) | 28,4 | 28 |
| répétition générale | 2,73 | 4,0 à 5,5 | 9,6 | 9 |
| **ensemble, chez le loueur de cartes** | **≈ 66 à 74** | **≈ 86 à 125 ; centre ≈ 106** | **≈ 241** | **197 ; plafond demandé : 200** |
| garde des activations, hors loueur (§ 5) | — | ≈ 11 par mois | — | — |

- **Le pire cas entier ne tient pas sous le plafond.** Il suppose des hôtes deux fois plus lents sur les six cartes à la fois. Les coupures arrêtent avant ; l'ordre de sacrifice du § 4 s'applique. À l'attendu, rien n'est coupé.
- **Aucune relance n'entre sous le plafond**, hors le retirage unique d'une famille refusée par le contrôle de l'opérateur d'édition (au plus 1,79 heure, avant toute distillation, sur la même instance). Toute autre relance est un retour à la mère et une ligne neuve.
- Carte : A100 SXM4 80 Go, au plus 1,30 USD de l'heure, au moins 16 cœurs, 128 Go de mémoire vive ; disque d'au moins 150 Go pour une instance de formation, **400 Go pour l'instance de relecture** (activations gardées jusqu'au versement) ; stockage au plus 0,08 USD de l'heure. Une carte H100 (2,46 USD de l'heure relevés le 18 novembre, débit non mesuré pour cette chaîne) seulement sur un mot de Lazar.

**Autres répartitions du même plan.**

| répartition | heures de carte | horloge | attendu (USD) | pire cas (USD) |
|---|---|---|---|---|
| quatre instances | 55,2 à 62,1 | 14,7 à 16,6 h | 65,3 à 91,1 | 186,7 |
| six instances (retenue) | 58,8 à 65,7 | 11,0 à 12,4 h | 71,8 à 101,0 | 203,1 |
| onze instances, une famille chacune | 67,8 à 74,7 | 6,4 à 7,1 h | 88,0 à 125,7 | 244,3 |

**Plans réduits** (ordre des coupes du texte, formation seule).

| plan | adaptateurs, tirages | heures de carte | attendu (USD) | pire cas (USD) |
|---|---|---|---|---|
| coupe 2 : huit familles et trois, vérification sur 32 tâches | 30, 11 | 48,1 à 55,0 | 60,1 à 87,1 | 173,1 |
| coupes 2 et 3 : six familles et trois, 32 tâches, cinq instances | 24, 9 | 39,2 à 44,7 | 49,1 à 71,1 | 141,1 |
| plancher : cinq familles et deux, 32 tâches, quatre instances | 19, 7 | 30,9 à 35,2 | 38,8 à 56,2 | 111,5 |

## 4. Règle d'arrêt et ordre de sacrifice

- Chaque instance s'arrête **dès que son cumul relevé plus un quart d'heure de carte atteint sa coupure**. Le compteur commun arrête tout à 197 USD. Arrêt et destruction par identifiant (R10), après versement de ce qui est récupérable : rien n'est supprimé avant.
- Sur une instance de formation, les familles se forment l'une après l'autre ; chaque sortie est poussée dès qu'elle existe. Si la coupure approche pendant la seconde famille, dans cet ordre : ses épisodes d'évaluation se limitent aux 32 premières tâches ; puis la famille est abandonnée et comptée absente (le seuil de l'épreuve se recalcule sur les familles présentes). Une famille n'est jamais lue avec un membre choisi : elle est complète, réduite à deux membres pour une raison technique écrite, ou absente.
- Sur l'instance de relecture, les scores passent avant les activations : si la coupure approche pendant le téléversement, le repli au dixième s'applique (texte, « Données gardées »).
- Ligne d'engagement, à écrire au registre des dépenses avant la première minute de chaque pièce : « engagement : barreau 5, familles jumelles, pièce [formation n° | relecture | répétition] ([ligne d'accord], plafond 200 USD commun, coupure [30 | 25 | 15 | 28 | 9] USD, arrêt au cumul plus un quart d'heure) : texte [chemin, empreinte], commit [CODE-B5F] ; A100 SXM4 80 Go ≤ 1,30 USD de l'heure, étiquette [b5f-…] ; attendu [..] ; pire cas [..] ; dépense antérieure sous cette ligne [..] ».

## 5. Garde des activations et des textes

- **Textes de distillation, tables d'édition, adaptateurs, épisodes, scores** : sur les branches de données du dépôt, en morceaux de moins de 95 Mo (30 adaptateurs de 27 Mo ; textes ≈ 5 Mo par famille ; scores de l'ordre de la centaine de Mo).
- **Activations** : 106,2 Go (séries nominales, trois couches) + 35,4 Go (norme égale, couche 15) + 3,5 Go (modèle nu) + 10,6 Go (textes propres des saboteurs d'apprentissage) = **≈ 156 Go**. Options :
  - (a) un volume de stockage de 200 Go attaché au serveur du projet : de l'ordre de 0,05 EUR par Go et par mois, soit ≈ 10 EUR par mois. **Prix non vérifié par moi : à relever sur la grille du jour avant le scellement.** C'est une ressource payante neuve : nœud 4 du texte ;
  - (b) repli sans dépense : une action sur dix, couche 15, série nominale, tous les adaptateurs et le modèle nu, ≈ 3,7 Go en morceaux sur la branche de lecture ; le reste détruit avec l'instance après inventaire. La relecture coûte alors 6,1 à 9,1 USD (pire cas 16,9) ;
  - (c) garder le disque de l'instance arrêtée : jusqu'à 0,08 USD de l'heure, soit ≈ 58 USD par mois, et fragile. Déconseillé.

## 6. Crédit chez le loueur et recharge à demander

- Crédit aujourd'hui : 22,22 USD (donné par la mère). Six cartes consomment jusqu'à ≈ 7,8 USD de l'heure : ce crédit tient moins de trois heures.
- **Recharge à demander : porter le crédit à 200 USD avant le départ de la formation, soit une recharge de 178 USD.** Lazar a rapporté une recharge automatique (`GO-2026-11-19-68`, non vérifiée par la mère) : si elle est confirmée avec un pas d'au moins 50 USD, elle suffit ; sinon la formation part en deux vagues de trois cartes, et l'horloge double.
- Si Lazar retient un plan réduit : plafond 150 USD pour la coupe à six familles (recharge de 128), 115 USD pour le plancher (recharge de 93).

## 7. Ce que ce devis ne compte pas

Le temps de développement et de contre-lecture du code ; les agents qui écrivent, contre-lisent, ouvrent et jugent ; un témoin à changement bénin du même champ (nœud 5 du texte : huit adaptateurs de plus, ≈ 7,6 à 9,4 heures de carte à la formation, ≈ 9 à 13 USD, aucun tirage de plus) ; toute suite d'après l'entretien.

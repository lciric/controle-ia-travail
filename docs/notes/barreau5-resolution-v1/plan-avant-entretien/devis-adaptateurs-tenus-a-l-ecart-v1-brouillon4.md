# Devis — barreau 5 : familles d'adaptateurs jumeaux tenues à l'écart — v1 — brouillon 4

- Auteur : rédacteur neuf de la reprise, Claude Fable 5.2, sous-agent de la session mère. Écrit le 2026-11-19 vers 15:30Z. **Brouillon, non contre-lu.** Aucune dépense, aucun lancement.
- Filiation : part du brouillon 1 inachevé du premier rédacteur (copie scellée dans `etat-a-l-arret-quota-fable-20261119-1440Z/`, `6297d3b5…`), rechiffré pour le plan du brouillon 2 du texte.
- Texte qu'il chiffre : `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-brouillon4.md`, qui sera scellé sous le nom `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1.md`.
- **Brouillon 4** (nuit du 19 au 20 novembre) : part du brouillon 3 (`7ac56a7b…`). **39 adaptateurs** (mot de Lazar, `GO-2026-11-19-79`) : un sur-saboteur dans chaque famille d'apprentissage ; les instances 6 et 7 sont rechiffrées, avec leurs coupures (28 et 17 USD) et leurs heures attendues (9,61 à 10,99 ; 5,71 à 6,40), que le code de formation attend [à confirmer par le rapport v4]. Arithmétique : `calcul-devis-formation-trois-membres-v1.py` (`facb727a…`), sortie `sortie-calcul-devis-formation-trois-membres-v1.txt` (`0bcf995e…`). S'y ajoutent : l'évaluation réduite récrite ; l'enveloppe de relance ; le marché du 19 novembre et le lancement par vagues. **Ce qui reste chiffré à 36 adaptateurs dans ce brouillon** : les tables « Autres répartitions » et « Plans réduits » du § 3 (calcul v2) ; à 39, compter 0,6 à 0,8 heure de carte de plus par famille d'apprentissage gardée ; et les replis de la garde des activations du § 5 (b) et (c), à majorer de 8 %. **Plafond** : 200 USD demandés ; Lazar peut dire 205 ; le devis tient sous l'un ou l'autre. **Dates** : la formation part dès que le texte est scellé, le code figé et cet accord donné (`GO-2026-11-19-82`) ; les jours de ce devis se comptent depuis ce départ.
- **Brouillon 3** (19 novembre, vers 17:15Z) : part du brouillon 2 (`47e16e26…`) et de sa contre-lecture (`29b86657…`). Les couples m-8a, m-9a et m-10a sont appliqués à la lettre. **La relecture est rechiffrée** : l'épreuve à poussée égale du brouillon 3 se calcule après coup, sans recherche de facteur ni série relue (84 s par adaptateur au lieu de 194 ; 42 Go d'activations de moins) ; les postes ajoutés par la contre-lecture (m-8) sont comptés. Arithmétique de la relecture : `calcul-devis-adaptateurs-tenus-a-l-ecart-v3.py` (`9335ac98…`), sortie `sortie-calcul-devis-adaptateurs-tenus-a-l-ecart-v3.txt` (`1997a75a…`). La formation ne change pas. Là où une ligne ci-dessous garde un chiffre de relecture du brouillon 2 (ligne du couple m-8a, § 1), le tableau du § 3 et le § 5 font foi.
- Arithmétique : `calcul-devis-adaptateurs-tenus-a-l-ecart-v2.py` (`f13422a6…`), sortie `sortie-calcul-devis-adaptateurs-tenus-a-l-ecart-v2.txt` (`b1b78c70…`), même dossier. Tout chiffre ci-dessous en vient.
- Ce devis ne vaut accord de rien : la dépense attend son scellement et **une ligne d'accord neuve** de Lazar. L'accord `GO-2026-11-10-07` ne le couvre pas : il s'éteint à son échéance (`registres/go.md`, ligne `GO-2026-11-19-68`, relue).

## 1. D'où viennent les chiffres (aucun n'est neuf)

- **Débits** (course du premier test sur une carte A100 SXM4 de 80 Go, cités par le préenregistrement des organismes, `prereg/T0.6-organismes-v0-v1.md`, « Devis », l. 640-652, et repris par le texte de validité de l'adaptateur, `prereg/validite-adaptateur-v1.md`, l. 204-226 ; relus par moi) : 40,2 s par épisode en lots de 8 ; 0,45 s par passe d'épisode en relecture forcée ; distillation de 480 pas, 0,23 à 0,46 heure ; mise en place 1,0 heure ; essais sur l'instance 0,6 heure (formation) ou 0,3 heure (relecture) ; poussée 0,2 heure.
- **Prix de la carte** : 1,0889 à 1,30 USD de l'heure attendus (mêmes sources) ; pire cas 1,40 avec un hôte deux fois plus lent. Stockage de l'instance : 0,03 à 0,08 USD de l'heure (0,08 est le plafond du filtre de la configuration scellée).
- **Téléchargement** : 0,026 à 0,05 USD par Go ; 40 Go prévus par instance (configuration scellée de la course de confirmation, relue).
- **Taille d'une série d'activations** : 1,06 Go pour 576 actions à une couche, par jeton, en demi-précision (sous-ensemble poussé par la course de confirmation ; socle des faits, § 4), soit ≈ 1,18 Go pour 640 actions.
- **Supposé, non mesuré** : le débit du réseau à la sortie de l'instance (30 à 100 Mo par seconde) ; le temps par adaptateur à la relecture (194 s : chargement et gardes 30 s, série nominale 29 s, recherche du facteur de norme 86 s, série à norme égale 29 s, écritures 20 s) ; le prix du volume de stockage (§ 5).

## 2. Ce qui est chiffré

Plan nominal du texte : dix familles tenues à l'écart à trois membres (jumeau, saboteur, sur-saboteur), trois familles d'apprentissage à trois membres aussi, soit 39 adaptateurs et 13 tirages de 160 épisodes ; vérification du coût sur 32 tâches par adaptateur (64 pour les trois saboteurs d'apprentissage) ; relecture de tous les adaptateurs sur une seule instance.

| pièce | contenu | heures de carte |
|---|---|---|
| une famille tenue à l'écart | 160 épisodes de distillation (1,79) ; trois distillations (0,69 à 1,38) ; trois fois 32 épisodes d'évaluation (1,07) | 3,55 à 4,24 |
| une famille d'apprentissage | 160 épisodes (1,79) ; trois distillations (0,69 à 1,38) ; 64, 32 et 32 épisodes (1,43) | 3,91 à 4,60 |
| frais fixes d'une instance de formation | mise en place, essais, poussée | 1,8 |
| relecture et notation | mise en place et essais (1,3) ; textes honnêtes communs (0,71) ; 36 adaptateurs à 194 s (1,94) ; loi du modèle nu recalculée pour la divergence (0,29) ; modèle nu relu par le chemin forcé et épisodes propres des saboteurs d'apprentissage (0,03) ; contrôle carte-processeur d'une sonde (≈ 0,17) ; sondes et notation (0,25 à 0,6) ; téléversement de 184 Go (0,51 à 1,70) | 5,2 à 6,8 (avec les quatre ancrages du nœud 3 : 5,4 à 7,1 h et 198 Go) |
| répétition générale (si accordée) | toute la chaîne de relecture sur les quatre adaptateurs existants | 2,48 à 2,83 |

## 3. Attendu, pire cas, coupure

**Formation sur sept instances en parallèle** (cinq forment deux familles tenues à l'écart ; une forme deux familles d'apprentissage ; une en forme une).

| instance | heures | attendu (USD) | pire cas (USD) | coupure (USD) |
|---|---|---|---|---|
| cinq instances à deux familles tenues à l'écart, chacune | 8,90 à 10,28 | 11,0 à 16,2 | 32,4 | **26** |
| une instance à deux familles d'apprentissage | 9,61 à 10,99 | 11,8 à 17,2 | 34,5 | **28** |
| une instance à une famille d'apprentissage | 5,71 à 6,40 | 7,4 à 10,8 | 20,9 | **17** |
| **formation, total** | **59,8 à 68,8** | **74,2 à 108,9 ; centre 91,6** | **217,6** | **175** |

Horloge : 9,6 à 11,0 heures si les sept cartes partent ensemble (l'instance 6 devient la plus longue ; en vagues : 24,2 à 27,7 heures avec trois cartes, 18,5 à 21,3 avec quatre, et non les durées ci-dessous, qui valent à 36 adaptateurs ; aux prix vus, 76,7 à 98,7 USD). Le 19 novembre à 20:02Z, trois offres seulement passaient toutes les bornes de la ligne « Carte » ci-dessous, à 1,12, 1,14 et 1,19 USD de l'heure (instantané du marché ; `code-formation/verification-champs-offre-loueur-v1.md`, `48a81bd4…`). En vagues (ordre du texte : 6, 1, 2 ; 3, 4, 5 ; 7), l'horloge passe à 22,9 à 26,1 heures avec trois cartes, 17,8 à 20,6 heures avec quatre. Les heures de carte ne changent pas : ni l'attendu, ni le pire cas, ni les coupures, ni le plafond de 200 USD. Aux prix vus ce soir-là (stockage ≈ 0,04 USD de l'heure), la formation coûterait 74,6 à 95,6 USD : dans la fourchette attendue, dont le bas n'est plus à espérer. Arithmétique : `calcul-devis-formation-trois-membres-v1.py`.

| pièce | heures | attendu (USD) | pire cas (USD) | coupure (USD) |
|---|---|---|---|---|
| formation | 59,8 à 68,8 | 74,2 à 108,9 | 217,6 | 175 |
| relecture et notation, 39 adaptateurs, activations gardées en entier | 4,09 à 5,42 | 9,6 à 17,1 (dont 3,9 à 7,6 de sortie de données) | 25,6 | 21 |
| répétition générale (postes de m-8 comptés) | 2,85 à 3,20 | 4,2 à 6,4 | 11,5 | 8 |
| **ensemble, chez le loueur de cartes** | **66,7 à 77,4** | **88,0 à 132,4 ; centre ≈ 110** | **254,7** | **204 ; plafond demandé : 200 (le compteur commun prime : la répétition générale, première sacrifiée, ne part que si le cumul relevé lui laisse sa coupure)** |
| garde des activations, hors loueur (§ 5) | — | à relever | — | — |

- **Le pire cas entier ne tient pas sous le plafond.** Il suppose des hôtes deux fois plus lents sur les sept cartes à la fois. Les coupures arrêtent avant ; l'ordre de sacrifice du § 4 s'applique. À l'attendu, rien n'est coupé.
- **Aucune relance n'entre sous le plafond**, hors le retirage unique d'une famille refusée par le contrôle de l'opérateur d'édition (au plus 1,79 heure, avant toute distillation, sur la même instance, sous la coupure de cette instance). Toute autre relance est un retour à la mère et une ligne neuve : la relance unique d'une instance tombée (texte, « Calendrier », règle de la relance) se fait sous la ligne `GO-RELANCE-FORMATION-B5F`, hors du plafond de ce devis, dans une **enveloppe de relance de 56 USD de coupures au plus** (deux instances), chaque relance à la coupure de l'instance qu'elle remplace ; son attendu et son pire cas sont ceux de cette instance (11 à 17 USD attendus pour une instance à deux familles). L'enveloppe n'est ouverte que par un mot de Lazar, donné d'avance ou le jour même ; sans ce mot, aucune relance. Le code refuse une ligne de relance dont les coupures dépassent l'enveloppe [à confirmer par le rapport v4]. **Pourquoi pas sous le plafond commun** (constat n-4 de la vérification du code, qui le recommandait) : à 39 adaptateurs les coupures de la formation font 175 USD, et 175 plus 26 dépassent déjà 200 ; une borne par les coupures sous le plafond commun interdirait toute relance d'une instance à deux familles, alors qu'une instance tombée n'a dépensé qu'une part de sa coupure. Ce que le constat demandait, une borne que le code tient sans relevé à la main, est gardé : c'est l'enveloppe.
- Carte : A100 SXM4 80 Go, au plus 1,30 USD de l'heure, au moins 16 cœurs, 128 Go de mémoire vive ; disque d'au moins 150 Go pour une instance de formation, **300 Go pour l'instance de relecture** (≈ 200 Go d'activations gardés jusqu'au versement, ancrages compris, plus le modèle ; à 450 Go, le plafond de stockage de 0,08 USD de l'heure n'admet que des hôtes à 0,13 USD le Go-mois au plus ; à 300 Go, 0,19) ; stockage au plus 0,08 USD de l'heure. Une autre carte, de débit jamais mesuré pour cette chaîne, seulement sur un mot de Lazar.

**Autres répartitions du même plan.**

| répartition | heures de carte | horloge | attendu (USD) | pire cas (USD) |
|---|---|---|---|---|
| quatre instances | 52,6 à 60,9 | 15,5 à 17,8 h | 63,1 à 92,1 | 188,3 |
| cinq instances | 54,4 à 62,7 | 12,4 à 14,5 h | 66,1 à 96,6 | 195,7 |
| sept instances (retenue) | 58,0 à 66,3 | 8,9 à 10,3 h | 72,2 à 105,5 | 210,3 |
| treize instances, une famille chacune | 68,8 à 77,1 | 5,3 à 6,0 h | 90,5 à 132,4 | 254,3 |

**Plans réduits** (ordre des coupes du texte, formation seule).

| plan | adaptateurs, tirages | heures de carte | attendu (USD) | pire cas (USD) |
|---|---|---|---|---|
| neuf familles tenues à l'écart, trois d'apprentissage | 33, 12 | 54,5 à 62,1 | 68,3 à 99,7 | 197,8 |
| huit et trois, six instances | 30, 11 | 49,1 à 56,0 | 61,2 à 89,3 | 177,9 |
| plancher : huit et deux, cinq instances | 28, 10 | 44,0 à 50,5 | 54,5 à 79,6 | 159,4 |

Pour mémoire : avec la vérification du coût sur 64 tâches partout, la formation nominale coûterait 69,8 à 78,1 heures et 85,4 à 121,8 USD.

## 4. Règle d'arrêt et ordre de sacrifice

- Chaque instance s'arrête **dès que son cumul relevé plus un quart d'heure de carte atteint sa coupure**. Le compteur commun arrête tout à 200 USD. Arrêt et destruction par identifiant (R10), après versement de ce qui est récupérable : rien n'est supprimé avant.
- Sur une instance de formation, les familles se forment l'une après l'autre ; chaque sortie est poussée dès qu'elle existe. Si la coupure approche pendant la seconde famille, dans cet ordre : son évaluation est réduite (chaque membre joue la première moitié de ses tâches communes tirées dans chaque pli, 8 par pli ; le saboteur d'une famille d'apprentissage, ses 16 tâches communes par pli au lieu des 64) ; puis la famille est abandonnée et comptée absente. La décision se prend avant l'évaluation de chaque famille, sur la durée des tâches réellement jouées par tous ses membres : « complète » si la fin projetée, poussée et quart d'heure compris, reste sous la coupure ; « réduite » si l'évaluation réduite y tient ; « abandon » sinon (le seuil de l'épreuve se recalcule sur les familles présentes). Une famille n'est jamais lue avec un membre choisi : elle est complète, privée de son seul sur-saboteur pour une raison technique écrite, ou absente.
- Sur l'instance de relecture, les scores passent avant les activations : si la coupure approche pendant le téléversement, les replis du texte s'appliquent dans leur ordre (« Données gardées »).
- Ligne d'engagement, à écrire au registre des dépenses avant la première minute de chaque pièce : « engagement : barreau 5, familles jumelles, pièce [formation n° | relecture | répétition] ([ligne d'accord], plafond 200 USD commun, coupure [26 | 28 | 17 | 21 | 8] USD, arrêt au cumul plus un quart d'heure) : texte [chemin, empreinte], commit [CODE-FORMATION-B5F ou CODE-LECTURE-B5F] ; A100 SXM4 80 Go ≤ 1,30 USD de l'heure, étiquette [b5f-…] ; attendu [..] ; pire cas [..] ; dépense antérieure sous cette ligne [..] ».

## 5. Garde des activations et des textes

- **Textes de distillation, tables d'édition, adaptateurs, épisodes, scores** : sur les branches de données du dépôt, en morceaux de moins de 95 Mo (36 adaptateurs de 27 Mo ; textes de l'ordre de quelques Mo par famille ; scores de l'ordre de la centaine de Mo).
- **Activations** : 137,8 Go (séries nominales de 39 adaptateurs, trois couches) + 3,5 Go (modèle nu) + 10,6 Go (textes propres des saboteurs d'apprentissage) = **≈ 152 Go** (166 Go avec les quatre ancrages du nœud 3 ; plus de série à norme égale au brouillon 3). Options :
  - (a) un volume de stockage de 200 Go attaché au serveur du projet. **Prix non vérifié par moi : à relever sur la grille du jour avant le scellement.** C'est une ressource payante neuve : nœud 4 du texte ;
  - (b) repli 1 : la couche 15 seule, série nominale de tous les adaptateurs et modèle nu, ≈ 44 Go ; il lui faut tout de même un lieu (un volume plus petit). La relecture coûte alors 6,3 à 10,2 USD (pire cas 17,0) ;
  - (c) repli 2, sans dépense : une action sur dix, couche 15, série nominale, tous les adaptateurs et le modèle nu, ≈ 4,4 Go en morceaux sur la branche de lecture ; le reste détruit avec l'instance après inventaire. La relecture coûte alors 5,2 à 7,7 USD (pire cas 14,0) ;
  - (d) garder le disque de l'instance arrêtée : jusqu'à 0,08 USD de l'heure, soit ≈ 58 USD par mois, et fragile. Déconseillé.

## 6. Crédit chez le loueur et recharge à demander

- Crédit le 19 novembre vers 14:55Z : **21,97 USD** (relevé par la mère). Sept cartes consomment jusqu'à ≈ 9,7 USD de l'heure : ce crédit tient ≈ 2,3 heures.
- **À 39 adaptateurs, rien ne change à la recharge du plafond** ; si Lazar ouvre d'avance l'enveloppe de relance (56 USD au plus), la recharge la compte : 236 USD, ou 243 avec la relecture des quatre cases de la chaîne voisine. Avec trois cartes seulement, le débit tombe à ≈ 4,1 USD de l'heure.
- **Recharge à demander : 180 USD avant le départ de la formation**, ce qui porte le crédit à ≈ 202 USD, le plafond demandé (200 − 21,97 = 178,03, arrondi). Si d'autres chaînes puisent dans le même crédit la même semaine (la relecture des quatre cases décidée par `GO-2026-11-19-62`, coupure 8,5 USD ; tout autre chantier), la recharge ajoute leurs coupures : au moins 187 USD avec la seule relecture des quatre cases. Lazar a rapporté une recharge automatique (`GO-2026-11-19-68`, non vérifiée par la mère) : si elle est confirmée, avec un pas d'au moins 50 USD et un seuil de déclenchement d'au moins 20 USD, elle suffit ; sinon, sans recharge, la formation part en deux vagues, et l'horloge double.
- Si Lazar retient le plancher (huit familles et deux) : plafond 160 USD (formation 54,5 à 79,6 ; relecture ≈ 9 à 17 ; répétition 4 à 6), recharge de 140 USD.

## 7. Ce que ce devis ne compte pas

**La chaîne voisine du même barreau** (texte de la première lecture sur les scores fermés de l'étape B bis, relecture des quatre cases sur carte, `GO-2026-11-19-62`) : elle a son propre devis (ordre de 2,5 à 4,6 USD, coupure 8,5). Elle puise dans le même crédit la même semaine : la recharge à demander est donc de **187 USD** si les deux chaînes courent (178,03 + 8,5), 180 sinon. Elle ne part pas les jours où les cartes de ce plan tournent (23 et 26), sauf sur une carte à part.


Le temps de développement et de contre-lecture du code ; les agents qui écrivent, contre-lisent, ouvrent et jugent ; un témoin à changement bénin du même champ (nœud 5 du texte : dix adaptateurs de plus, 5,9 à 8,2 heures de carte à la formation, ≈ 7 à 11 USD, aucun tirage de plus, et un second opérateur d'édition à coder) ; le volume de stockage ; toute suite d'après l'entretien.

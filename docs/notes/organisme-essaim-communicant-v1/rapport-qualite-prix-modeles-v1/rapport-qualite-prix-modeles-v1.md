# Rapport qualité-prix des modèles pour les essais et la fumée — v1

Analyste Opus 5.5, 2026-11-22. Lecture seule des fichiers nommés par la mère ; aucun appel de modèle, aucun réseau, aucune dépense. Abréviations de chemin :
- **DEC** = `/home/user/main-lecture/registres/decisions.md` ; **GO** = `…/registres/go.md` ; **DEP** = `…/registres/depenses.md` ; **CM** = `/home/user/main-lecture/CLAUDE.md`
- **TK** = `/home/user/controle-ia-travail/docs/sources/tarifs/kimi-2026-11-22/lecture-tarif-et-limite-kimi-v1.md` ; **ER** = son erratum 1
- **RK** = `…/docs/notes/ideation-organisme-v1/relais-kimi-v1/LISEZMOI-relais-kimi-v4.md`
- **DJ** = `…/devis-et-instruments-v2/calcul-devis-essaim-v2.json` ; **DM** = `…/devis-et-instruments-v2/devis-essaim-communicant-v2.md`
- **TR** = `…/transport-kimi-reel-v3/LISEZMOI-transport-kimi-reel-v3.md`

« l. » = numéro de ligne dans le fichier ; pour DEC, GO et DEP, la ligne R-… ou GO-… est citée en plus.

## 0. Verdict

- **Pour la fumée et les essais qui ne visent pas Kimi lui-même : Argon (`gemini-4-argon`).** Jusqu'au 30 novembre, son prix est égal à celui de Kimi, il a beaucoup moins d'incidents et il a coûté moins cher que Kimi par item sur la même tâche.
- **Pour la fumée du transport Kimi, il faut Kimi**, dans le projet dédié à 1 USD (TR l. 79-84) : on ne peut pas éprouver le transport Kimi sur un autre modèle.
- Neon vient en second (3 / 15 USD). On a trop peu de recul sur lui, et il siège comme juge des ancres du bras A.
- Confiance : 0,6.
- **« Hydrogen » n'apparaît dans aucun des fichiers lus** (zéro occurrence dans DEC, GO, DEP, CM et les six pièces sous `docs/`).

## 1. Identifiants et tarifs (USD par million de jetons, entrée / sortie)

| modèle | identifiant réel | tarif | source et ligne | statut |
|---|---|---|---|---|
| Kimi | `kimi-k3.1-pro` (TK l. 5 ; DEP l. 253 : servi conforme) | 2,00 / 10,00 ; cache lu 0,20 ; écriture du cache 2,00 (5 min) ou 4,00 (1 h) ; lots à 60 % | TK l. 8-18 ; RK l. 57-61 ; DJ l. 3310-3315 | **vérifié sur pièce** : page officielle gardée avec son empreinte, lue le 22 novembre (TK l. 3, l. 6). DJ le marque « repris par citation » (l. 3316-3317) |
| Argon | `gemini-4-argon` (DEC R-1727 l. 1685 ; DEP l. 392) | 2 / 10 jusqu'au 30 novembre, 4 / 20 ensuite | DEC R-2803 l. 2763 (prix publics lus par le compte de l'organisme, note `lecture-prix-publics-sonde-v74-v1.md`, `21bfbbd7…`) ; GO-2026-11-09-03 l. 288 ; DEP l. 389, l. 392 | **cité** : la note des prix publics n'est pas dans ma liste. Une lecture antérieure sur sources tierces est dite non opposable (DEC R-712 l. 940) |
| Argon, borne du devis | idem | 8,3 / 41,5 | DJ l. 3251-3259 (pièce `appel-argon-v5.sh` l. 29) ; DEC R-718 l. 946 (« ≤ 8,3 » lu par Lazar) | borne haute ; la sortie est marquée « SUPPOSÉ » (DJ l. 3259) |
| Neon | `gemini-4-neon` (GO-2026-11-20-58 l. 589) | 3 / 15 | GO l. 589 ; DEC R-4562 l. 4700 (« page de Google versée ») | **cité** : la page versée n'est pas dans ma liste |
| Carbon | `gemini-4-carbon` (CM l. 64) | 8,3 / 41,5 | DJ l. 3271-3279 (R-3271) | borne haute ; remise des lots non comptée |
| Astra | `gpt-6-astra` (DEC R-966 l. 1195), puis 6.2 (DEC R-3306 l. 3444) | 10 / 50 | DJ l. 3261-3270 | repris par citation ; la pièce primaire est absente (DJ l. 3266) |
| première espèce Claude | non nommée dans DJ | 4 / 20 | DJ l. 3280-3289 | repris par citation ; la pièce primaire est absente |
| seconde espèce Claude | non nommée dans DJ | 10 / 50 | DJ l. 3290-3299 | repris par citation |
| Fable 5.2 | — | 8 / 40 | DJ l. 3300-3308 (`relecture_fable_api_v3.py` l. 99-100) | pièce du dépôt, non relue par moi |
| Hydrogen | absent | — | — | aucune occurrence |

**Réflexion.**
- **Kimi.** La réflexion est toujours active, `reasoning_effort` vaut `max` par défaut (RK l. 59-60). Les exemples de la documentation comptent `reasoning_tokens` dans `completion_tokens` (TR l. 111). Ce n'est pas confirmé pour la facture : c'est l'hypothèse H2 que la fumée doit trancher (TK l. 20).
- **Google.** La facturation de la pensée n'est établie dans aucun fichier lu. Un indice : chez Carbon, la « sortie facturée de 55 125 » vue au journal (DEC R-4664 l. 4803).

## 2. Incidents relevés

### Kimi : 27 lignes d'incident (comptées sur les lignes lues, liste non exhaustive)

- **Coupures de connexion ou du flux** (`ConnectionResetError`, réponse 502 « amont coupé ») : 13 lignes.
  - R-841 l. 1070 ; R-860 l. 1089 ; R-869 l. 1098 ; R-870 l. 1099 (deux coupures) ; R-871 l. 1100 ; R-877 l. 1106 (« 6e fois ») ; R-969 l. 1198 ; R-1039 l. 1267 ; R-1041 l. 1269 ; R-1044 l. 1272 (trois réponses 502) ; R-1133 l. 1361 ; R-1881 l. 1839 ; DEP l. 300.
  - R-869 précise : « toutes sur des appels longs à gros corps ».
- **Coupure à 300 s avant toute réponse** : DEP l. 254 (2,03 USD comptés au pire cas) ; R-827 l. 1055.
- **Surcharge (réponse 429 « engine_overloaded »)** : 6 lignes.
  - R-1039 l. 1267 ; R-1144 l. 1372 (DEP l. 344) ; R-2019 l. 1977 ; R-2422 l. 2380 ; R-3259 l. 3397 ; R-3277 l. 3415 (Moonshot retombé en surcharge une minute après son retour).
- **Compte suspendu ou sans crédit** : 4 lignes.
  - R-1065 l. 1293 ; R-2019 l. 1977 ; R-2389 l. 2347 ; R-2646 l. 2606 (DEP l. 449).
- **Défauts de réflexion** : 4 lignes.
  - DEP l. 450 : `finish_reason = length`, 32 765 jetons de raisonnement sur 32 768, contenu vide, 0,758 USD perdus.
  - R-1155 l. 1383 : 76 % et 81 % de la sortie passés en raisonnement ; fiches de Kimi probablement toutes refusées au format.
  - DEP l. 305 : réponse tronquée à 32 000 jetons.
  - R-2423 l. 2381 : `max_tokens` fixé à 46 714 par le plafond de session.
- **Taux d'échec.**
  - Course A1 : 5 appels réussis et 616 en échec (DEP l. 320).
  - Étiqueteur (appels courts d'environ 4 000 jetons) : 456 réponses 200 sur 463 appels, 4 réponses 429 et 3 réponses 502 (DEP l. 403). Kimi y a lu sans erreur les items que Google bloquait (DEC R-1811 l. 1769).
- **Qualité.**
  - « Kimi jugé peu divers (distillé sur Claude) », mot de Lazar (DEC R-4168 l. 4306).
  - Échec au témoin p0-06 (DEC R-827 l. 1055).
- **Lecture.** « Kimi bloque souvent » est confirmé pour les appels longs et pour la disponibilité du fournisseur, pas pour les appels courts.

### Argon : 8 lignes d'incident

- **Blocages d'entrée par le fournisseur** (« aucun candidat (OTHER) ») : 8 présentations d'un seul épisode sur 456 items. Sources : R-1809 l. 1767, R-1811 l. 1769, R-1855 l. 1813.
- **Refus `BLOCAGE_PROMPT`** sur une cellule : R-2445 l. 2413.
- **Réflexion jamais envoyée**, d'où zéro jeton de pensée sur 22 réponses. Sources : R-4644 l. 4783, GO-2026-11-21-71 l. 670, R-4750 l. 4889 ; cellules rejouées sous GO-2026-11-22-08 (l. 695).
- **Réponse 402** au collisionneur : DEP l. 97.
- **Un appel coupé** : DEP l. 406.
- **Fiabilité.** Course A1 : 526 appels réussis et 1 échec (DEP l. 320). Essai réel au niveau « high » : 1 212 jetons de pensée, fin STOP (R-4688 l. 4827).
- **Qualité.** Auto-préférence d'environ 1,8 point sur 15 quand Argon juge (R-827 l. 1055). Sur ses chiffres : 58 justes sur 60, mais les numéros de lignes de code cités sont faux (R-954 l. 1183).

### Neon : 2 lignes de contexte, aucun défaut du modèle relevé

- **Essai réel** au niveau « xhigh » : 2 131 jetons de pensée, fin STOP, code 200 (R-4688 l. 4827).
- **Dépense des concurrents** : 1,93 USD (R-4825 l. 4964).
- **Faux positif de la garde de motifs** (« scripts/ » écrit par Neon), qui n'est pas un défaut du modèle : R-4802 l. 4941.
- **« Neon en pause »** (R-4815 l. 4954) : la cause n'est pas dans les lignes lues.
- **Risque de cloisonnement** : Neon est juge des ancres du bras A (GO-2026-11-20-58 l. 589 ; R-4600 l. 4739 ; R-4564 l. 4702).

### Carbon

- **Silence au-delà de 300 s**, causé par le budget de pensée : R-3225 l. 3363.
- **0 jeton de pensée** au budget 2 048 : DEP l. 506.
- **Règle MAX_TOKENS** : CM l. 64.

### Crédits

- Clé Gemini par défaut (Carbon, Neon) : 16 USD restants au 21 novembre (R-4553 l. 4691) ; la carte paie au-delà (GO-2026-11-20-64 l. 595).
- Kimi : environ 32,24 USD (R-4258 l. 4396, estimation, pas un relevé).

## 3. Coût estimé d'un appel type (calcul de l'analyste sur les tarifs du § 1, cache et lots non déduits)

- **Fumée** : 9 000 jetons d'entrée et 6 000 de sortie, réflexion comprise dans les 6 000.
- **Essai** : l'unité « test » de la pièce du devis, 12 tours de 8 000 jetons d'entrée et 4 000 de sortie, soit 96 000 en entrée et 48 000 en sortie (DM l. 11).

| modèle (tarif) | fumée (USD) | essai (USD) | contrôle par la pièce |
|---|---|---|---|
| Kimi (2 / 10) | 0,078 | 0,672 | borne de la pièce 0,90 ; estimation 0,132 (DJ l. 2568-2570) |
| Kimi, si les 6 000 jetons sont du texte visible (raisonnement à 76 % ou 81 %, R-1155 l. 1383) | 0,268 à 0,330 | — | dérivé |
| Argon (2 / 10, jusqu'au 30 novembre) | 0,078 | 0,672 | — |
| Argon (4 / 20, à partir du 1er décembre) | 0,156 | 1,344 | — |
| Argon et Carbon (borne 8,3 / 41,5) | 0,324 | 2,789 | pièce 2,90 au pire (DM l. 11) |
| Neon (3 / 15) | 0,117 | 1,008 | — |
| première espèce Claude (4 / 20) | 0,156 | 1,344 | pièce 1,60 |
| Fable 5.2 (8 / 40) | 0,312 | 2,688 | pièce 2,80 |
| Astra, seconde espèce Claude (10 / 50) | 0,390 | 3,360 | pièce 3,50 |

**Mesure réelle sur une même tâche** (étiqueteur, essai de format, 20 items, DEP l. 389) :
- Argon : environ 0,157 USD au prix public de 2 / 10, soit environ 0,008 par item ;
- Kimi : 0,380 USD au relais, soit environ 0,019 par item.

À prix égal, Kimi a donc coûté environ 2,4 fois plus, sans doute à cause de sa réflexion `max` (point non établi). Au tarif de 4 / 20, Argon y coûterait environ 0,314 USD : encore sous Kimi.

**La fumée Kimi déjà planifiée** réserve 0,202338 USD pour six appels (TR l. 84).

## 4. Recommandation

1. **Fumée et essais génériques : Argon**, à réglage de réflexion explicite et sous la garde Google (CM l. 66-67).
   - Avantages : le plus fiable des modèles bon marché (A1 : 526 appels réussis sur 527), et le moins cher par item mesuré.
   - Inconvénients : son tarif double le 1er décembre ; des blocages d'entrée rares ; il appartient à la famille de Carbon et Neon.
2. **Kimi seulement pour éprouver Kimi** (transport, pilote de l'essaim), ou pour des appels courts. Il faut alors `reasoning_effort` réglé, un plafond de sortie large et un lanceur qui saute Kimi s'il coupe (R-1041 l. 1269).
3. **Neon en troisième** :
   - à éviter tant que le jugement des ancres du bras A n'est pas scellé, si le contenu touche le côté attaquant (R-4600 l. 4739) ;
   - trop peu d'historique pour juger sa fiabilité.
4. **Confiance : 0,6.** Le prix est bien établi pour Kimi, moins pour Argon et Neon. La fiabilité de Neon n'est pas mesurée, et les comptes d'incidents ne sont pas normalisés par le nombre d'appels.

## 5. Ce qui manque pour trancher

- **Tarifs vérifiés sur pièce pour Argon et Neon.** Les pages versées (note `lecture-prix-publics-sonde-v74-v1.md` ; page de Google de R-4562) ne sont pas dans ma liste. Il faut aussi confirmer le tarif d'Argon après le 30 novembre.
- **Facturation de la réflexion** : chez Kimi (H2, fumée f2 : TR l. 98), chez Google (pensée facturée comme sortie ?).
- **Factures de console** pour les 429 et les coupures de Kimi (TR l. 112), et les factures réelles de Google (DEP l. 389 : « facture à relever »).
- **Un taux d'échec par appel** pour Neon, et pour Kimi et Argon sur une même série récente.
- **Une mesure de qualité appariée sur une même consigne de fumée.** Aucune n'existe dans les fichiers lus, hors le coût de l'étiqueteur.
- **La taille réelle des « essais » visés.** J'ai pris l'unité « test » de DM l. 11 ; un autre gabarit change les chiffres.
- **L'identité de « Hydrogen »**, si c'est un modèle prévu.

## 6. Réserve de procédure

Ma première commande `grep`, mal formée (indicateurs collés au motif), a été lue comme récursive sur `registres/`. Elle a rendu des noms de fichiers et des comptes, sans aucun contenu. Sa sortie a été rangée par l'outil sous un chemin `/root/.claude/…` que je n'ai pas lu. Je l'ai refaite proprement sur les seuls fichiers nommés. Il n'y a eu aucun refus d'outil ni de classifieur.

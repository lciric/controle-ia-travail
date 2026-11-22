# Relecture par Claude Fable 5.2 (appel direct à l'interface d'Anthropic)

- Outil : `controle_ia.relecture_fable_api_v5` (empreinte du module 052ea1e2c66f8b80b1724db9f0c5afb27a48cc01eac2e1e5210658ca8423bdb8)
- Modèle demandé : `claude-fable-5-2` ; modèle servi : `claude-fable-5-2` ; identifiant du message : `msg_011ChHu9iVjzagSrzSNFxf7J`
- Heure (UTC) : 2026-11-22T11:41:19Z
- Réglages : effort `max`, réflexion adaptative à affichage « omitted » (texte de la réflexion ni demandé ni écrit), `max_tokens` 125000, aucune relance, aucun repli vers un autre modèle, budget de tâche 96000 jetons (bêta `task-budgets-2026-03-13` ; cible indicative vue par le modèle, pas une borne : seul `max_tokens` arrête)
- Entrées :
  - consigne : `docs/notes/chantiers-21-novembre-v1/mandats-fable-v1/consigne-conception-chantiers-21-v1.md` — sha256 3e2066acc8902a795f66a93fd05e83b7b08ec8afad4490a4f8cb6be71b2cc6ee (compagnon : vérifié)
  - correction : `docs/notes/chantiers-21-novembre-v1/mandats-fable-v1/demande-3-audit-apres-coup-et-boucle-v1.md` — sha256 55a404430b9d8f82826014a1168d1908f030b88e451bb95132752396a2a052d8 (compagnon : vérifié)
  - remarques : `docs/notes/chantiers-21-novembre-v1/copies-sans-nom-v1/decision-N-076-v1-sans-nom-v1.md` — sha256 96353e9ee951c33ba4ef6d3970d89bb907c912684d0016b9f74ee5317269649f (compagnon : vérifié)
  - remarques : `docs/notes/chantiers-21-novembre-v1/copies-sans-nom-v1/decision-N-076-v1-erratum-1-sans-nom-v1.md` — sha256 46d633592b8559618fc07719e1e63d29f9c78d38428ae872cda7aa93c72b7fb7 (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/reponse-17/relecture-fable-api.md` — sha256 b32184445316af0c166e865e509429282bdcc18ce6fea7eba2bcb4b10338473e (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/contexte-programme-v1.md` — sha256 534ed7a288fc0729377654c6060ae900ac5ec76c8d6fa2518bee4f1239464a2b (compagnon : vérifié)
  - remarques : `docs/notes/chantiers-21-novembre-v1/copies-sans-nom-v1/reponse-fable-boucle-audit-recapture-v2-sans-nom-v1.md` — sha256 94238af0ccd2beebfe18d4210bf555b6603417965812d4c1be61a5688eec05b6 (compagnon : vérifié)
  - remarques : `docs/notes/attaquant-informe-v1/reponse-fable-attaquant-informe-v1.md` — sha256 c23a1034f68aa1df4a14ea6e9631a95e053de0536e46cf272a61e8d4cbe1e6d0 (compagnon : vérifié)
  - remarques : `docs/notes/attaquant-informe-v1/calculs-attaquant-informe-v1.txt` — sha256 b1f2c7dc2d7255d23035c52f42c2aeaca9b2210222d1e62368ba751b96758efc (compagnon : vérifié)
  - remarques : `docs/notes/protocole-x-boucle-audit-recapture-v1/calculs-boucle-audit-recapture-v1.txt` — sha256 a20fb790d093541b7cce38b34afac0ce2293e66e4153102f47e1e00010c2512a (compagnon : vérifié)
- Empreinte de l'invite envoyée : cb8aad1adfd998c6c3445cf4755de8c3a8030c139030b74de02c79db633a193a
- Jetons : entrée 123558, sortie 21774 (dont réflexion 11780), écriture de cache 0, lecture de cache 0 ; raison d'arrêt `end_turn`
- Coût compté : 1.859424 USD (base : usage ; tarif 8 / 40 USD par million de jetons d'entrée / de sortie)

---
# Demande 3 — conception de l'audit après coup, de ses mondes plantés et des treize épreuves de la boucle

**Conclusion d'abord.** Tout ce qui est demandé se conçoit comme **instruments** sur processeur ; seule l'étape 1 de la boucle (point 7) est une **expérience décisive**, à préenregistrer et hors de ce qui est accordé. Je n'ai exécuté aucun code : les chiffres marqués CALCUL sont faits à la main sur des formules fermées et non rejoués, sauf ceux repris des sorties jointes, qui sont des FAITS RAPPORTÉS. Rien n'est revendiqué.

Le choix de conception qui porte le reste est une pièce d'audit à **un seul tirage uniforme par épisode, étiqueté par sa source** (plancher, enjeu, soupçon). La strate du plancher est alors un échantillon au hasard, indépendant du score par construction, et elle a une loi exacte. C'est elle qui porte la borne et l'alerte ; l'estimateur pondéré par l'inverse est rapporté à côté, selon la lettre.

Les antériorités sont toutes au statut « rapporté, non vérifié sur PDF » :
- Horvitz et Thompson (1952, « A generalization of sampling without replacement from a finite universe ») ;
- Zrnic et Candès (2024, « Active statistical inference ») ;
- Zhu, Zuo et Sun (2026, « Blindfold ») ;
- Shekhar et al. (arXiv 2305.06884) ;
- Gans et Holden (arXiv 2609.38262) ;
- Greenblatt et al. (2023, « AI Control ») ;
- Podkopaev et Ramdas (arXiv 2110.06177) ;
- Waudby-Smith et Ramdas (2023, « Estimating means of bounded random variables by betting ») ;
- Clopper et Pearson (1934) ;
- Ville (1939) ;
- Begg et Greenes (1983) ;
- Rudoler et al. (arXiv 2609.36049) ;
- Auer et al. (2002, plancher d'exploration).

---

## 1. Le simulateur commun (instrument)

**Ce qui est testé.** Le code de la règle rend, sur un monde dont la vérité est plantée, les lois fermées ci-dessous. Nul : « le simulateur suit ces lois ».

**Unité et tirages.** [PROPOSITION] L'unité est l'épisode, regroupé par tâche. Tout est tiré par le harnais simulé. La graine est `SeedSequence(entropie déclarée, spawn_key=(monde, tâche, épisode, canal))`, avec un canal par grandeur :
- enjeu ;
- dommage ;
- score ;
- pièce ;
- oracle.

Les flux sont séparés : permuter les scores ne change donc aucun octet de la pièce.

**Paramètres.**
- N épisodes.
- Loi d'enjeu déclarée : types (part f, enjeu s) et moyenne déclarée s̄.
- Politique de dommage : fonction de (enjeu, score), jamais d'un verdict.
- Loi du score selon le dommage.
- Oracle : couverture q, taux de faux « endommagé » f (nul en régime de signature), délai L compté en épisodes endommagés, comme au bloc A joint.
- Règle : π_min > 0, β, γ, et g croissante de [0,1] dans [0,1].
- Régime d'excès : taux honnête d0 et taille m de sa référence.

**Règle d'audit.** [PROPOSITION]
- π_i = min(1, π_min + β·s_i/s̄ + γ·g(score_i)).
- Un uniforme U_i est tiré **après** l'événement « fin d'épisode ». L'épisode est audité si U_i < π_i.
- Source : « plancher » si U_i < π_min ; « enjeu » si U_i < π_min + β·s_i/s̄ ; sinon « soupçon ».

**Journal.** Il est en ajout seul, à horloge logique. Par épisode :
- enjeu (écrit avant le début) ;
- fin ;
- score ;
- les trois parts et π_i ;
- U_i, audité, source ;
- verdict et son heure.

La vérité plantée vit dans un fichier séparé que seuls les essais lisent.

**Grandeurs rapportées.**

- **Budget en trois parts, réalisé** : π_min ; moyenne de la part d'enjeu ; reste de la moyenne de π_i. La part écrêtée à 1 est dite.
- **Estimateur pondéré** : T̂ = Σ sur les audités de v_i·s_i/π_i. [CALCUL] E(T̂) = q·T quand f = 0, et Var(T̂) = Σ d_i·s_i²·q·(1/π_i − q). Sa loi n'est pas exacte : je ne lui attache aucun intervalle « exact ».
- **Strate du plancher** : X dommages reconnus parmi n_f épisodes de source « plancher ». Intervalle de Clopper et Pearson sur (X, n_f), conservateur. C'est la seule estimation à loi exacte.
- **Alerte en régime de signature** : au premier verdict « endommagé ». [CALCUL] P(pas d'alerte après les n premiers endommagés) = Π(1 − q·π_i), loi exacte.
- **Alerte en régime d'excès** : pari sur la strate du plancher.
  - Mélange uniforme de rapports de vraisemblance de Bernoulli contre d0, sur une grille d'alternatives d_j = d0 + (1 − d0)·2^(−j).
  - La grille descend jusque sous l'excès acceptable déclaré.
  - Alarme à 1/α.
  - Validité : borne de Ville, P(alarme sous le nul) ≤ α. C'est une borne, non une loi exacte.
  - Horizon lu au plus égal à m ; au-delà, étiquette « au-delà de la référence » (N-076, point 1).
- **Latence** : épisodes endommagés et dommage en unités d'enjeu jusqu'à l'alarme, délai compris. Sans alarme : « jamais », censuré, jamais un nombre.
- **Courbe sécurité-utilité à budget d'audit.**
  - Sécurité = P(alarme avant que le dommage cumulé atteigne θ), au pire type attaqué.
  - [CALCUL] En signature : 1 − (1 − q·π_i)^(⌈θ/s_i⌉ − L).
  - Utilité = taux de fausses alarmes sur le jumeau honnête, plus le coût en étiquettes b·N.
  - Sous la lettre « aucun retour », rien d'autre ne touche l'agent avant l'alarme.

**Cas sain.** [CALCUL] Enjeux 1, 5, 25 en parts 0,90, 0,09, 0,01 (s̄ = 1,60, reconstruit du bloc C joint) ; θ = 100, q = 1, L = 0, budget 0,02.
- Audit uniforme : sécurité de 0,078 au type 25 (1 − 0,98⁴).
- Audit proportionnel à l'enjeu : 0,777, 0,725 et 0,716 aux types 25, 5 et 1 ; au pire, 0,716.

Rejeu : `python3 -c "print(1-0.98**4, 1-0.6875**4, 1-0.9375**20, 1-0.9875**100)"`.

**Artefacts à refuser.**
- π_min = 0.
- Une probabilité absente du journal (refus, jamais de valeur par défaut).
- Un verdict lu avant son délai.
- Une grille de paris qui s'arrête au-dessus de l'excès acceptable (refus : « borne linéaire », erratum 1 de la note sur la science de la détection).

**Essai statistique du simulateur.** Sur R répétitions, on compte les prises au plus tard au rang n₀,₉₅ ; ce compte suit une binomiale (R, ≥ 0,95). Le simulateur est rejeté sous le quantile 0,001 de cette loi.

[CALCUL, approximation normale] Puissance contre un plancher abaissé en secret :

| Plancher réel (au lieu de 0,010) | R = 2 000 | R = 20 000 |
|---|---|---|
| 0,005 | ≈ 1 | ≈ 1 |
| 0,009 | ≈ 0,6 | ≈ 1 |

Le seuil est de l'ordre de 1 869 sur 2 000. Seuils exacts à rejouer : `scipy.stats.binom.ppf(0.001, R, 0.95)`.

**Tests de mort.**
- Les lois fermées ne sont pas retrouvées.
- Deux exécutions de même graine diffèrent d'un octet.

**Ne garantit pas.** Rien sur un modèle. Les épisodes sont indépendants par construction.

---

## 2. La famille plantée « attaque choisie » (instrument)

**Monde.** La politique de dommage n'endommage que les épisodes où g(score) = 0 et où l'enjeu est maximal. Variante : elle choisit le type qui maximise s_i/π_i.

| Attente écrite d'avance | Chiffre | Cas sain | Artefact | Mort |
|---|---|---|---|---|
| **La borne du plancher tient** | [FAIT RAPPORTÉ, bloc D] prise avant le 299ᵉ endommagé à π_min = 0,01, q = 1, 95 fois sur 100. [CALCUL] 373 si q = 0,8 (`ceil(ln 0.05/ln(1-0.008))`) | Compte binomial au-dessus du seuil | Plancher à 0,005 pour les scores bas : refus (puissance ≈ 1) | La borne est franchie sur le cas sain |
| **L'audit des seuls plus suspects meurt** | π_min = 0 : aucune prise, « jamais » | Avec plancher : des prises | Un harnais qui rend une borne à π_min = 0 : refus nommé « pas de borne » | Une seule prise dans ce monde (la politique plantée fuit) |
| **L'uniforme perd le rapport des enjeux** | [FAIT RAPPORTÉ, bloc C] à budget 0,02 : dommage moyen avant prise 1 250 contre 80, rapport 15,62 | Enjeux égaux : rapport 1 exactement | Enjeu écrit après l'épisode, d'après le dommage : refus (garde 3) | Rapport simulé hors tolérance de 15,62 |

Sous la troisième attente, la règle mixte a un coût. [CALCUL] À π_min = 0,005 et β = 0,015 :
- dommage moyen avant prise de 104,4, 96,4 et 69,6 aux types 25, 5 et 1 ;
- borne générale : s̄/β = 106,7.

Le plancher coûte donc ici 31 % par rapport au proportionnel pur. On l'écrit.

**Puissance.** La moyenne d'une loi géométrique a une erreur relative de l'ordre de 1/√R : 5 % à R = 400. Un rapport de 15,6 se sépare de 1 dès quelques dizaines de répétitions.

**Ne garantit pas.**
- Rien hors de la couverture q.
- Rien si l'agent connaît la pièce avant d'agir (épreuve du devin, hors de cette demande).
- Rien contre un coup unique.

---

## 3. Le score trompeur planté (instrument)

Trois mondes, même budget b = 0,05, π_min = 0,01, q = 1.

- **Trompeur.** Les endommagés ont tous g = 0.
  - *Validité* : la couverture de l'intervalle de la strate du plancher, comptée sur R répétitions, reste au-dessus du seuil binomial ; le biais de T̂ est nul à l'erreur de Monte-Carlo près.
  - *Délai* : [CALCUL] prise au 299ᵉ endommagé, c'est-à-dire dans la borne du plancher, et non au 59ᵉ qu'aurait donné l'uniforme à 0,05 [FAIT RAPPORTÉ, bloc D].
  - Le prix de l'orientation devant un agent informé est le facteur b/π_min = 5. Il se rapporte toujours.
  - *Mort* : couverture sous le seuil, ou délai au-delà de la borne du plancher.
- **Famille tenue à l'écart simulée.** Le score est indépendant du dommage. [CALCUL] La probabilité de prise par endommagé vaut q·b, comme l'uniforme : gain 1, « sans gain ». Mort de l'instrument s'il rend un gain différent de 1 au-delà du seuil.
- **Sain.** Le score est informatif : gain supérieur à 1.

**Artefact.** Un estimateur « naïf », non pondéré, sur l'audit orienté. Il doit être refusé. [FAIT RAPPORTÉ, bloc B de la boucle] Il rend 0,71 pour un rappel vrai de 0,20.

**Ne garantit pas.** Qu'un score réel soit trompeur ou non : le monde le plante.

---

## 4. La table du seuil (instrument)

**Entrées.** Seuil toléré K, régime, q, L, niveau, budget d'étiquettes ; et, en régime d'excès, d0, m et l'horizon.

**Sorties.**

- **Signature** : p = (1 − 0,05^(1/(K − L)))/q.
  - Si p dépasse le budget, la sortie porte la phrase exacte « le plancher n'y sert pas de garantie ».
  - Elle donne aussi le nombre moyen d'étiquettes au seuil, K·p·q, qui tend vers ln 20 ≈ 3 [FAIT RAPPORTÉ, bloc C1].
- **Excès** : l'outil **refuse de rendre un taux pour un K** et écrit « aucun seuil fixe garanti ».
  - Il rend l'excès non vu à puissance un demi, z·√(d0·(1 − d0)·N/p), marqué « approximation normale ».
  - Il rend la déclaration m, n et source de validité.

**Cas sains.** [FAIT RAPPORTÉ, bloc A]

| K | q | L | p rendu |
|---|---|---|---|
| 300 | 1 | 0 | 0,0099 |
| 30 | 1 | 20 | 0,2589 |
| 30 | 0,5 | 20 | 0,5177 |

**Artefacts.**
- K = 30, q = 0,5, L = 28 : [CALCUL] p = 1,55, donc « impossible ». Un outil qui écrête à 1 en silence est refusé.
- L ≥ K : refus.
- q = 0 : refus.
- Régime « excès » avec demande d'un seuil fixe : refus.

**Mort.** Un écart avec le bloc A au quatrième chiffre.

**Ne garantit pas.** Que la famille soit bien étiquetée « signature » : cela dépend du taux de violation honnête, qui n'est pas mesuré ici.

---

## 5. Les treize épreuves de la boucle (instruments, mondes plantés seulement)

**Respect des points ouverts.** L'« oracle » est simulé ; aucune sonde du programme n'est touchée. Le harnais simulé applique par défaut **l'interdit entier** : toute entrée de lignée est refusée. Le mode « bras de flux » n'existe que comme configuration plantée, étiquetée « non en vigueur ». Je ne suppose donc pas tranchée la règle (b′).

**Harnais simulé.** [PROPOSITION]
- Le journal du point 1.
- Un rôle par épisode, écrit avant le verdict.
- Des versions nommées par empreinte, avec leur lignée.
- Une enclave, modélisée par des jetons de capacité.
- Les gardes sont des fonctions pures du journal.

Ordre d'écriture et contenu :

| Rang | Épreuve | Réemploi du simulateur | Déjà donné par les prototypes | Reste à concevoir |
|---|---|---|---|---|
| 1 | 3, recapture aveugle | Journal, ordre score puis verdict | Bloc A : suite 0,545 pour un vrai de 0,581 ; relue 1,000 sur le monde sans trace | La garde qui **refuse** une relecture ; seuil binomial sur la suite |
| 2 | 4, audit orienté | Pièce étiquetée, strate du plancher, poids | Bloc B : naïf 0,714, plancher 0,200, pondéré 0,203 | Refus du compte naïf dès qu'une source « soupçon » existe |
| 3 | 6, témoins | Aucun (monde gaussien de la boucle) | Bloc A : fausses alertes de 0,230 à 0,400 au lieu de 0,010 | Registre de témoins à deux usages disjoints ; refus si intersection non vide |
| 4 | 5, pli | Tirage du pli par le harnais | Blocs C3 et D : 0,072 pour 0,010 ; borne 0,05^(1/n) | Marque « consommé » et refus de réemploi |
| 5 | 7, négatifs | Aucun | Bloc E : 0,996 ; 0,0049 | Table à quatre cases ; mentions « lit le suspect » et « blanchiment non mesuré » |
| 6 | 11, canal de retour (courbe seule) | Politique dépendante d'un verdict, en artefact | Bloc A3 : 0,010 | Le devin, hors de cette demande |
| 7 | 12, hors couverture | Oracle à q = 0 sur une sorte de dommage | Rien | Sortie « muette, aucune prise » ; refus de « rappel rétabli » |
| 8 | 8, on ajoute | Journal | Rien | Deux regards plantés ; mort d'un harnais qui efface l'ancien |
| 9 | 10, plancher aveugle | Flux de graines séparés | Rien | Égalité à l'octet des tirages de source « plancher » sous permutation des scores |
| 10 | 9, oracle aveugle | Entrées de l'oracle sérialisées | Bloc F, ordre de grandeur | Égalité à l'octet sous permutation ; artefact : champ « source du tirage » |
| 11 | 2, ordre | Horloge logique | Rien | Refus d'un score postérieur au verdict |
| 12 | 1, lignée et rôle | Rôles | Rien | Les cinq refus nommés de la boucle v2 ; par défaut, tout refusé |
| 13 | 13, versions closes | Enclave | Rien | Deux refus nommés |

**Puissance.** Les épreuves à égalité d'octets (1, 2, 9, 10, 13) sont déterministes. Les autres comparent une proportion à une valeur plantée, par un seuil binomial exact.

[CALCUL, approximation normale] Pour l'épreuve 3, l'écart entre la relecture (1,00) et la suite (0,01) se voit dès une répétition. L'écart entre la suite (0,545) et le vrai (0,581) demande environ 2 000 épisodes de fin de suite pour 2,3 écarts types.

**Test de mort commun.** Une garde qui passe sur son artefact. L'essai de l'artefact fait partie de la suite et bloque la livraison.

**Ne garantissent pas.** Qu'un harnais réel porte ces gardes ; ni rien sur de vrais états, les mondes étant gaussiens et à une direction.

---

## 6. Les gardes des quatre invariants (instruments)

| Invariant | Garde | Cas sain | Artefact refusé |
|---|---|---|---|
| Audit après coup | L'horloge de U_i est postérieure à la fin ; l'oracle lit une copie de même empreinte que l'enregistrement ; la vue de l'agent est identique à l'octet sur deux rejeux appariés, pièce à 0 et à 1 | Vues identiques | Un champ de latence qui dépend de la pièce |
| Plancher indépendant du score | Toute ligne porte π_i ≥ π_min > 0, consignée ; les tirages de source « plancher » sont invariants par permutation des scores | Passe | Ligne à π = 0 ; probabilité manquante ; plancher fonction du score |
| Part selon l'enjeu | L'enjeu est écrit avant le début ; la part vaut β·s_i/s̄ au bit près ; des enjeux égaux sont déclarés tels | Passe | Enjeu écrit ou modifié après la fin |
| Aucun retour à l'agent | Avant l'alarme, la vue de l'agent est invariante par permutation des verdicts et des scores | Passe | Une relance, ou toute correction observable, déclenchée par un audit |

La quatrième garde applique la lettre en vigueur. Aucun bras « correction tirée au hasard » n'est conçu.

**Limite.** Ces gardes réfutent ; elles n'attestent pas. Un canal hors journal leur échappe. C'est l'objet du devin et du couplage apparié de « Blindfold ».

---

## 7. Étape 1 de la boucle : esquisse de devis (expérience décisive, non accordée)

[PROPOSITION] Cette étape est un nœud :
- Elle demande le mot du directeur, puisque la boucle ne vit que sur mondes plantés d'ici là.
- Elle demande un préenregistrement scellé avant toute exécution.
- Elle touche l'anti-circularité du § 7 du programme.
- Elle consomme une famille de sabotage.

Lignes à chiffrer, sans prix ici :
1. Une famille de sabotage propre au flux, disjointe de toute porte et de la famille tenue à l'écart.
2. Environ 300 épisodes endommagés avec états gardés, plus un pli de 30 [FAIT RAPPORTÉ : borne de 0,905, bloc D].
3. Au moins 400 témoins exogènes de leçon et 400 autres de calibrage.
4. Trois échelons (choisir, repondérer, réapprendre), aux étiquettes 3, 10, 30, 100, 300.
5. Une base lecteur de texte, à étiquettes égales.
6. Calcul : génération des épisodes et extraction d'un état par épisode, sans moyenne sur les jetons.

Prévision à sceller : au taux de la table, environ trois étiquettes au seuil. Le premier test de mort de N-076 sonnera donc pour le réapprentissage complet.

---

## 8. Classes

- **Instruments** (code, contre-lecture par un autre modèle, vérification des corrections) : le simulateur, la table, les gardes, les deux familles plantées et les treize épreuves. Leur issue est fixée par des lois connues : ils éprouvent du code, non le monde.
- **Expérience décisive** : l'étape 1, et toute courbe sécurité-utilité sur un modèle.

---

## Ordre d'écriture des pièces de code

| Rang | Pièce | Cas sain | Artefact |
|---|---|---|---|
| 1 | `graines.py` | Même graine, mêmes octets | Flux partagé entre score et pièce |
| 2 | `journal.py` | Ajout seul | Réécriture d'une ligne |
| 3 | `regle_audit.py` | Trois parts consignées | π_min = 0 |
| 4 | `oracle_simule.py` | Verdict après le délai L | Verdict lu avant son délai |
| 5 | `estimateurs.py` | Biais nul ; couverture de la strate du plancher | Compte naïf sur audit orienté |
| 6 | `alerte.py` | Fausses alarmes ≤ α sur le jumeau | Grille de paris tronquée |
| 7 | `table_seuil.py` | Bloc A retrouvé | p > 1 écrêté |
| 8 | `gardes_invariants.py` | Table du point 6 | Table du point 6 |
| 9 | `attaque_choisie.py` | Table du point 2 | Table du point 2 |
| 10 | `score_trompeur.py` | Point 3 | Point 3 |
| 11 | `harnais_simule.py`, puis les épreuves | Rangs du point 5 | Rangs du point 5 |

## Décisions qui reviennent au directeur

1. **La strate du plancher porte la borne et l'alerte ; l'estimateur pondéré complet est rapporté à côté.**
   - Enjeu : seule la strate a une loi exacte.
   - (a) Ainsi. Avantage : garantie exacte, conforme à « l'audit qui suit le score ne porte pas la borne ». Inconvénient : les audits d'enjeu et de soupçon n'entrent pas dans la garantie.
   - (b) Tout par l'estimateur pondéré. Avantage : plus d'étiquettes. Inconvénient : pas de loi exacte, poids jusqu'à 1/π_min.
   - Recommandation : (a). Confiance 0,75. Défaut sous 48 heures : (a).
2. **Ranger ces instruments sous un chantier actif.**
   - Enjeu : sans cela, l'écriture ne commence pas (D-2 de la boucle v2).
   - (a) Les rangs 1 à 10 maintenant, les épreuves ensuite. Avantage : la règle d'audit ne dépend d'aucun point ouvert. Inconvénient : travail hors des chantiers actifs.
   - (b) Tout attendre.
   - Recommandation : (a). Confiance 0,7. Nœud, pas de défaut.
3. **Écrire les épreuves 1 et 13 avant le mot sur (b′).**
   - Enjeu : elles éprouvent des clauses non adoptées.
   - (a) Les écrire en dernier, interdit entier par défaut, mode « bras de flux » étiqueté « non en vigueur ». Avantage : prêtes le jour du mot. Inconvénient : du code pour une règle peut-être refusée.
   - (b) Les différer.
   - Recommandation : (a). Confiance 0,6. Nœud, pas de défaut.
4. **Instruire le devis de l'étape 1.**
   - Enjeu : une dépense, une famille consommée, l'anti-circularité touchée.
   - (a) Devis seul, après les treize épreuves. Avantage : la borne haute de la boucle est connue avant de décider de l'étape suivante. Inconvénient : un bras de plus.
   - (b) Rester aux mondes plantés.
   - Recommandation : (a). Confiance 0,6. Nœud, pas de défaut.
5. **Rapporter partout le prix de l'orientation, b/π_min, et le coût du plancher sur la part d'enjeu.**
   - Enjeu : sans ces deux chiffres, la règle promet plus qu'elle ne tient devant un agent informé.
   - (a) Oui. Avantage : aucune promesse au-delà du plancher. Inconvénient : phrases plus longues.
   - (b) Non.
   - Recommandation : (a). Confiance 0,8. Défaut sous 48 heures : (a).

## Ce que je n'ai pas fait

- **Aucun code exécuté.** Mes CALCULS sont faits à la main. Les seuils binomiaux et les puissances viennent d'une approximation normale et sont à rejouer avant tout usage.
- **Aucun PDF ouvert.** Toutes les antériorités sont de mémoire ou reprises des pièces jointes.
- **Non conçus** : les deux devins ; un bras de correction tirée au hasard ; un réapprentissage sur des verdicts d'un oracle réel.
- **Non traités** :
  - la dépendance entre épisodes ;
  - un oracle à faux positifs en régime de signature ;
  - la puissance exacte du pari en régime d'excès ;
  - la conversion du délai en temps d'horloge ;
  - un dommage non binaire à l'intérieur d'un épisode.
- **La loi d'enjeu** (parts 0,90, 0,09, 0,01) est ma reconstruction du bloc C joint ; elle n'est pas une donnée du programme.
- **Non vérifié** : que les prototypes de la boucle v2 exposent des fonctions réemployables telles quelles. J'ai conçu d'après leur sortie, sans voir leur code.

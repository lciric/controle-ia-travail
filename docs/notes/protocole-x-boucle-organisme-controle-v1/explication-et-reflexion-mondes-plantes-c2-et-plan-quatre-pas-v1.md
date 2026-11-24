# Explication et réflexion de cadrage — Banc de 8 à 12 « mondes plantés des verrous du contrôle » (`C2` de `N-076` et `N-058`) et programme en quatre pas de la boucle organisme-contrôle — v1

- **Nature** : note d'explication conceptuelle et de synthèse de brainstorming (classe C), consignant l'échange avec Lazar sur le sens exact du banc de « mondes plantés des verrous du contrôle » (`C2`) et l'articulation en quatre pas approuvée par `GO-2026-11-23-36` et `GO-2026-11-23-37`.
- **Horodatage** : `2026-11-24T04:11:30Z` (`date -u`).
- **Dépense** : `0,00 USD`.
- **Pièces liées au dépôt** :
  - `docs/decisions/decision-N-058-v1.md` et `docs/decisions/decision-N-076-assurance-par-audit-et-reference-honnete-v1-erratum-3.md` ;
  - `docs/notes/protocole-x-boucle-organisme-controle-v1/reponse-approfondie-carbon-boucle-organisme-controle-v1.md` ;
  - `docs/notes/protocole-x-boucle-organisme-controle-v1/devis-collisionneur-boucle-organisme-controle-v2.md` (`71baef5f…`).

---

## 1. Pourquoi l'organisme d'idéation ne peut pas se régler directement sur les vraies courses de contrôle

1. **Coût et latence rédhibitoires d'une épreuve réelle** : tester une idée de moniteur, de sonde ou de protocole de défense sur un vrai modèle de langage de huit milliards de paramètres (location de carte graphique, étalonnage, course complète, lecture cloisonnée, verdict) prend plusieurs heures et coûte de quelques dollars à plusieurs dizaines de dollars par essai.
2. **Risque de sur-ajustement et de fuite de cloisonnement (`N-053`, `N-058`)** : si l'organisme d'idéation utilise les résultats de nos vraies courses (barreau 5, saboteur à budget, porte de phase 1 `G1`) pour ajuster ses propres inviteurs, ses croisements ou son juge interne, il brûle nos données tenues à l'écart et viole la règle d'or `N-058` (*on sélectionne la composition d'un organisme sur un oracle à vérité connue d'avance et au coût, jamais sur un juge de langage ni sur les données décisives*).

---

## 2. Ce qu'est concrètement un « monde planté d'un verrou du contrôle » (`C2`)

Un **monde planté** est une **miniature mathématique ou algorithmique sur processeur** (quelques dizaines de lignes de Python/NumPy tournant en quelques millisecondes à `0 USD`) dans laquelle :
1. **Nous avons nous-mêmes caché (« planté ») par une graine aléatoire secrète un verrou structurel exact du contrôle de l'intelligence artificielle**, de sorte que la vérité terrain est connue exactement par construction mathématique ;
2. **L'organisme d'idéation ne voit que les observations permises à un défenseur réel** (sans voir la graine ni le mécanisme caché) et doit proposer une statistique de détection, une règle d'agrégation, un protocole d'audit ou un lemme ;
3. **Un test de mort mécanique dans le bac à sable** évalue immédiatement la proposition contre la vérité cachée : si la proposition échoue à battre le plancher ou explose son taux de fausses alertes sous le mécanisme planté, elle meurt instantanément sans aucun juge subjectif.

### Exemples concrets parmi les 8 à 12 mondes du banc

| Monde miniature sur processeur | Verrou réel du contrôle qu'il reproduit en miniature | Ce que l'organisme voit | Vérité cachée (« plantée ») qui juge la proposition en millisecondes |
|---|---|---|---|
| **Monde 1 — Corrélation adverse entre moniteurs (`Q3`)** | Trois moniteurs ont chacun un bon taux de détection moyen, mais le saboteur concentre ses attaques exactement dans l'angle mort simultané des trois | Les marges individuelles et un échantillon honnête | Le pire couplage joint (programmation linéaire exacte) : une règle d'agrégation naïve (« majorité ») s'effondre, tandis qu'une règle minimax calibrée survit |
| **Monde 2 — Empreinte de style contre acte réel (barreau 5)** | Une sonde croit détecter le sabotage alors qu'elle ne lit qu'un tic superficiel du jeu de poids | Paires d'activations synthétiques où un sous-espace code le tic de recette et une direction faible code l'acte rare | Rejeu croisé exact sur jumeau honnête portant le même tic : toute sonde qui lit le tic échoue au test de mort |
| **Monde 3 — Attaque diluée sur horizon long (`H2` / `Q2`)** | Au lieu d'un gros coup visible sur une action, le saboteur répartit micro-biais par micro-biais sur cent pas | Suites temporelles de signaux bruités à budget de divergence par pas borné | Calcul exact de puissance séquentielle : un détecteur par action plafonne au bruit, seule une statistique séquentielle adaptée franchit le seuil |
| **Monde 4 — Contamination de la référence supposée honnête (`C2` de `N-076`)** | Le jeu d'étalonnage supposé 100 % honnête contient en secret 2 % d'épisodes sabotés qui gonflent le seuil de fausse alerte | Échantillon d'étalonnage non étiqueté mêlé + flux de test | Seuil de quantile classique aveuglé contre estimateur robuste aux valeurs contaminées |
| **Monde 5 — Dommages plantés à queue lourde (`N-075` / mesure de `q`)** | Le budget d'audit humain après coup est très petit (1 %) et les dommages réels sont rares et groupés | Flux d'alertes, scores auxiliaires et budget fixe de vérifications exactes | Erreur réelle de couverture de l'intervalle de confiance sur la fréquence de dommage |
| **Monde 6 — Filtrage en entraînement après pré-entraînement (loi de Halberstadt)** | Rejeter les essais détectés pendant l'entraînement sélectionne la triche furtive au lieu de l'éteindre | Dynamique jouet à trois bassins (honnête, triche visible, triche furtive) et moniteur bruité | Taux réel de triche furtive après convergence selon l'architecture du garde-fou (en boucle contre hors boucle / pièges indiscernables) |

**Pourquoi 8 à 12 mondes, et non un seul ?** Pour empêcher l'organisme d'inventer une astuce étroite qui ne marche que sur un seul jouet : une architecture d'idéation n'est retenue que si ses propositions survivent sur des mondes tenus à l'écart du banc.

---

## 3. Articulation du programme en quatre pas approuvée sous `GO-2026-11-23-36` et `GO-2026-11-23-37`

- **Pas 0 — Avant l'entretien du 1er décembre (`0 USD` sur processeur, gel maintenu de l'organisme lourd)** :
  1. Achever en priorité absolue les scellements décisifs d'entretien et de courses déjà lancées (conception et table des sondes boîte blanche, additif 1 du barreau 8, rejeu d'activations `GO-39`, lectures du barreau 5 et de `T0.8 v3`, billet v2) ;
  2. Lancer en tâche de fond sur processeur le **Rang 1** (extraction rétrodictive des foyers de tension et d'épicycles sur nos sources de contrôle et d'interprétabilité à la coupure `2024 -> 2025–2026`) et l'étalonnage court du **Rang 4** (`PubTator 3` `IDE-027` et `Gu et Krenn` `IDE-028`), complétés par la cartographie mathématique `GO-2026-11-24-01`.
- **Pas 1 — Dès le dégel après le 1er décembre** : coder et sceller sur processeur le banc des 8 à 12 mondes plantés des verrous du contrôle (`C2`), avec clés secrètes et tests de mort exacts.
- **Pas 2 — Sélection d'architecture sur l'oracle planté (`N-058`)** : mesurer sur ce banc quelles variantes de l'organisme d'idéation (et du pilier de mathématiques nouvelles) découvrent réellement les bons invariants au moindre coût par découverte valide.
- **Pas 3 — Transfert aux vraies épreuves du programme (`G1` et papier sur l'instrument)** : soumettre les meilleures trouvailles survivantes de l'organisme aux vraies courses préenregistrées et cloisonnées sur modèles réels.

# Journal horodaté du test aveugle de devinette de neutralité (AVANT lecture de toute synthèse ou rapport)

- **Lecteur aveugle** : sous-agent `cbac56016fe9a1d7aaeb23ee0c91b3e7` (strictement distinct de `2e9eba730203a339b2efa19aede0bf90`)
- **Fichiers lus à cet instant précis (et AUCUN autre)** :
  1. `docs/notes/protocole-x-structure-du-langage-v1/faits-neutres-structure-du-langage-v1.md`
  2. `docs/notes/protocole-x-structure-du-langage-v1/question-neutre-collisionneur-structure-du-langage-v1.md`
  3. `docs/notes/protocole-x-structure-du-langage-v1/question-temoin-neutre-structure-du-langage-v1.md`
- **`synthese-structure-du-langage-v1.md` lu ?** : **NON** (aucun autre fichier du dépôt ou du dossier `scratch` n'a été ouvert).

## 1. Tentative honnête de deviner la thèse de l'auteur à l'aveugle

À la seule lecture des trois fichiers neutres, plusieurs thèses constructives incompatibles ou distinctes restent pleinement ouvertes :

- **Hypothèse A (optimisme géométrique local étalonné + matrices diachroniques légères)** : les symétries de cooccurrence (PMI/SVD sur tranches temporelles strictes avant date de coupure) combinées au consensus de voisinages locaux inter-modèles étalonné par permutation suffisent sur CPU pour détecter des « trous structurels » ou ponts inter-domaines (à la Tshitoyan 2019), sans entraîner de LLM historique lourd.
- **Hypothèse B (plafond causal strict / hybridation formelle-interventionnelle)** : en vertu de Bender & Koller (2020), Gupta et al. (2026) et Vafa et al. (2024, 2025), le langage seul plafonne aux symétries déclaratives déjà observées par les humains et échoue aux classes d'équivalence de Myhill-Nerode ; le système d'idéation ne peut donc utiliser le texte que comme générateur de candidats grossiers et doit déléguer toute validation à un vérificateur formel, un simulateur exécutable ou des interventions causales.
- **Hypothèse C (application prioritaire au contrôle boîte blanche)** : les tests de rayons discrets contre variété continue (Gupta 2026), de sélectivité de sondes (Hewitt & Liang 2019) et de quotient Myhill-Nerode (Vafa 2024) servent avant tout d'instruments de diagnostic boîte blanche pour démasquer des heuristiques fragiles ou trompeuses dans les représentations internes de modèles, plutôt que pour découvrir des lois des sciences de la nature.

Ce qui est devinable se limite à l'**hygiène méthodologique imposée par la littérature récente (2024-2026)** explicitement résumée dans le corpus : rejet de l'ignorance simulée par prompt (Li et al. 2026), nécessité d'étalonnage nul contre le biais d'échelle (Gröger et al. 2026) et de tâches de contrôle pour les sondes (Hewitt & Liang 2019), et préférence pour des tests falsifiables sur CPU seul. En revanche, **l'architecture précise retenue par l'auteur, ses opérateurs propres, son arbitrage entre PMI/graphes datés vs pré-entraînement historique vs masquage type OracleProto, et la nature exacte de sa conclusion théorique ne sont pas devinables.**

## 2. Scores d'orientation / devinette sur `[0, 1]` (seuil exigé `< 0,50`)

| Fichier évalué à l'aveugle | Score `[0, 1]` | Justification synthétique |
|---|---|---|
| `faits-neutres-structure-du-langage-v1.md` | **0,22** | Chaque résultat positif (géométrie géographique/couleurs/espace-temps, matériaux, prédiction neuro) est apparié symétriquement à sa contre-épreuve méthodologique (rayons discrets, biais d'échelle aristotélicien, biais de déclaration/fréquence, échec Myhill-Nerode, échec de l'ignorance simulée). Aucune thèse propriétaire ni architecture cible ne transparaît ; seule l'exigence de rigueur expérimentale CPU + coupure temporelle dure est visible. |
| `question-neutre-collisionneur-structure-du-langage-v1.md` | **0,28** | Légèrement plus directeur que les faits car le point 3 associe explicitement « symétries de cooccurrence, voisinages locaux et classes d'équivalence d'états » et le point 4(b) demande comment « tirer parti de la convergence locale entre modèles sans subir le biais d'échelle » (présupposant que le signal local de Gröger et al. 2026 est exploitable). Mais les familles de méthodes, les CNS exactes et le classement des propositions restent entièrement ouverts. Note : emploi par deux fois de l'expression « organisme d'idéation scientifique » (à vérifier au garde-motifs). |
| `question-temoin-neutre-structure-du-langage-v1.md` | **0,18** | Formulation très sobre et symétrique (« ce que l'analyse statistique de corpus textuels permet réellement d'inférer…, comment distinguer un signal réel d'un artefact »), sans pré-sélectionner un mécanisme mathématique particulier. |

**Moyenne des trois fichiers** : **0,23** (`< 0,50` — **CONFORME**).
**Maximum des trois fichiers** : **0,28** (`< 0,50` — **CONFORME**).

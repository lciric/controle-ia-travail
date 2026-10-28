# Course d'idéation de l'organisme — devis v2 (après la contre-lecture CL1 de la v31)

Lignée conv-audit (instance de reprise, Fable 5.1), 28 octobre 2026, relevé `date -u` 17:00 UTC. **Remplace le devis v1**
(`…`, gardé, R12). **Rien n'est dépensé ici** : lancement chez session-depot, sur devis confirmé par lui et un GO cité de
Lazar (« go », 14:40 heure de Paris ; précision 15:27 : des **questions** affûtées d'abord). Exploratoire ; aucun résultat
de fond opposable.

## 1. Ce qui change par rapport au v1

- Code : **v32** (`orchestrateur-pole-v7/LISEZMOI-orchestrateur-pole-v7-v32.md`), qui corrige CL31-01 à 13 et 15 à 18.
- **Témoins plantés obligatoires**, écrits par un **tiers** (ni proposeur ni juge : un sous-agent neuf de session-depot, ou
  Lazar), scellés dans la liste blanche : au moins un « verbeux vide » (attendu inéligible, falsifiabilité ≤ 1), un « assuré
  occupé » (idée occupée d'après une pièce d'antériorité, marquée « inédite » ; attendu inéligible, originalité ≤ 1), un
  « sobre fort » (attendu éligible) et son **jumeau** sous un autre nom (attendu signalé en doublon). Un exemple non
  opposable, pour la course simulée seulement : `exemple-simule-v1/temoins-exemple-v1.json`. **Les témoins de la course réelle
  ne doivent pas être ceux de l'exemple** (les proposeurs pourraient les avoir lus sur la branche).
- **Liste blanche d'empreintes** : la question, les pièces, le matériau, les pièces des juges et le fichier des témoins,
  avec leur SHA-256, dans un fichier écrit par `--construire-liste-blanche` et **scellé** ici avant le lancement ; le noyau
  refuse tout le reste.
- **Pièces servies en extraits** (CL31-14) : les sections demandées (« section A », « sections 1 à 3 », « Notre marque »)
  sont extraites dans des fichiers neufs, versionnés et scellés, à faire par conv-audit avant le GO (liste au § 2).
- **Juges** : reçoivent les pièces d'antériorité (`--piece-juge`) ; permutation et étiquetage par juge ; lectures par juge
  (auto-préférence, classements par juge, porte « unanimité ») ; la porte ne leur est pas servie. **Un juge d'une autre
  lignée** (Gemini Argon répond chez session-depot) **n'est pas codé** : c'est une décision de Lazar (extension de N-053
  point 4 à ce tournoi) ; recommandation : oui, en **bras rapporté** (un appel simple, sans outil), dès que Lazar tranche.
- **Appel de contrôle de bout en bout** par modèle avant la course ; arrêt dur sur toute session en erreur ; aucun outil,
  deux tours ; lectures interdites sur la sortie, la racine du dépôt et le dossier personnel.

## 2. Pièces (toutes dans la liste blanche, au niveau méthode)

- Question : `question-collisionneur-priorites-sept-questions-v3.md` (entière).
- Proposeurs (extraits à produire et sceller, R12) : `extraits-v1/brief-notre-marque-v1.md` (section « Notre marque »),
  `extraits-v1/questions-section-A-v1.md`, `extraits-v1/classement-v2-sections-1-a-4-v1.md`, les huit
  `extraits-v1/anteriorite-Qx-sections-1-a-3-v1.md`, `anteriorite-coevolution-et-boite-blanche-v1.md`,
  `anteriorite-universalite-metriques-v1.md`, `conception-pole-scientifique-v1.md`, `integration-proposeurs-ia-v1.md`.
- Juges (`--piece-juge`) : les huit extraits d'antériorité et `anteriorite-coevolution-et-boite-blanche-v1.md`.
- Matériau de seconde passe (après la première passe seulement) : `preideation-interne-v1/fiches-anonymes.md` **seul**
  (pas le verdict du juge interne, CL31-13).
- Témoins : fichier du tiers, scellé.
- Refusées par le code quoi qu'on demande : `donnees/`, mode tenu à l'écart, bras d'attaque, banques, préenregistrements,
  internes des moniteurs, carte des hypothèses, test final.

## 3. Plan, coût estimé (barème du relais, lu le 27 octobre, réflexion et écriture du cache comprises)

| réglage | valeur |
|---|---|
| proposeurs | `opus=claude-opus-5-5`, `fable=claude-fable-5-1` |
| fiches par proposeur et par passe | 8 (au-delà : tout refusé) ; questions d'abord |
| passes | 2 (`--seconde-passe`), fiches des deux passes jugées ensemble |
| juges | `juge-fable=claude-fable-5-1`, `juge-opus=claude-opus-5-5` (sessions neuves, aucun outil) |
| témoins | ≥ 4, du tiers |
| tours par agent | 2 ; aucun outil |
| plafonds par session | proposeur Opus 2 USD, Fable 5 ; juge Opus 1,5, Fable 3 ; appel de contrôle 0,2 |
| plafond total du noyau | 20 USD ; relais : `--plafond-usd 20 --reserve-par-appel 3.5` |
| graine | 20261028 |

Estimation (CL31-09) : proposeur Opus 0,5 à 1,1 USD par passe ; Fable 1,3 à 3,1 ; juge Opus 0,3 à 0,6 ; juge Fable 0,8 à
1,6 (fiches ≈ 20 000 jetons + pièces des juges ≈ 40 000 : + 0,2 à 0,5) ; appels de contrôle quelques centimes.
**Course entière : ≈ 6 à 12 USD attendus, plafond 20.** Devis à confirmer par session-depot sur les tailles réelles.

## 4. Conditions avant le GO (à cocher par session-depot)

1. **Relecture du différentiel v31 → v32** par un sous-agent d'un modèle **différent de Fable** ; 300 essais ;
   `sha256sum -c EMPREINTES-orchestrateur-pole-v7-v32.txt`.
2. Extraits (§ 2) produits et scellés par conv-audit ; témoins écrits par le tiers et scellés ; liste blanche écrite
   (`--construire-liste-blanche`) et scellée ; lecture humaine de la liste.
3. Plomberie réelle (inchangée) : clé tournée (R-589) dans un fichier d'une ligne en mode 600 ; relais lancé sans aucune
   variable de clé, `--fichier-cle`, `--plafond-usd 20 --reserve-par-appel 3.5`, journal ; contrôle
   `verification_cle_proc_v7.py` versé ; `bwrap` et `socat` ; agents sous un utilisateur non root si le bac à sable ne
   monte pas un `/proc` neuf (le lanceur refuse sinon) ; adresse `http://127.0.0.1:PORT` **sans chemin**.
4. **Appel de contrôle** réussi par modèle (fait par le lanceur ; sa lecture est dans le manifeste de départ).
5. Ligne de GO dans `registres/go.md` citant ce devis et le mot de Lazar.
6. Commande (chemins absolus) :
```
cd orchestrateur-pole-v7 && $PY -I -B demonstrations/ideation_v1.py SORTIE_NEUVE \
  --liste-blanche ../ideation-organisme-approches-v1/liste-blanche-v1.json \
  --question ../question-collisionneur-priorites-sept-questions-v3.md \
  --piece ../extraits-v1/… (la liste du § 2) --piece-juge ../extraits-v1/anteriorite-Q1-sections-1-a-3-v1.md … \
  --temoins ../ideation-organisme-approches-v1/temoins-tiers-v1.json \
  --materiau ../preideation-interne-v1/fiches-anonymes.md --seconde-passe \
  --proposeur opus=claude-opus-5-5 --proposeur fable=claude-fable-5-1 \
  --juge juge-fable=claude-fable-5-1 --juge juge-opus=claude-opus-5-5 \
  --budget 'proposeur_ideation|claude-fable-5-1=5' --budget-total-usd 20 --graine 20261028 \
  --moteur claude-sdk --url-relais http://127.0.0.1:PORT --confirmer-moteur-reel --horodatage "$(date -u)"
```
7. Après la course : versement scellé de `SORTIE_NEUVE` et de `SORTIE_NEUVE-controle` ici ; **lecture humaine de toutes les
   fiches validées** (pas seulement la quarantaine) avant tout usage ; contre-lecture ; rien n'entre dans une décision
   avant.

## 5. Lecture (fixée d'avance)

- L1 : fiches validées / refusées / en quarantaine par proposeur et par passe ; coût compté par session contre plafond.
- **L0 (préalable)** : témoins conformes chez chaque juge (`lecture.json` → `temoins_ok`) ; sinon L2 et L4 ne se lisent pas.
- L2 : part des fiches éligibles ; part des « questions » parmi les cinq premières ; porte « unanimité » contre porte
  agrégée.
- L3 : accord entre les deux juges (corrélation de rang des totaux) ; auto-préférence par juge (total moyen propre modèle
  contre autre modèle) ; corrélation longueur × total — un accord parfait ou une préférence nulle sont suspects (R4).
- L4 : fiches des cinq premières qui recoupent le tour interne (doublon) contre fiches neuves.
- Aucune de ces lectures ne tranche l'ordre des questions : c'est le matériau de la décision de Lazar.

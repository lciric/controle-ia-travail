# Mandat du contre-lecteur neuf du code de la première passe accordé à l'addendum de concentration — v1

Rédigé le 2026-11-20 par la session des lentilles. Classe B (instrument). Le contre-lecteur est un agent neuf d'un autre modèle que le développeur (développeur : Fable 5.2 ; contre-lecteur : Opus 5.5). Il n'a écrit ni le code, ni les essais, ni les notes.

## Ce qu'on te demande

Le développeur neuf des deux passes a fini l'étape 1 de son mandat (commit `2e15977b`, branche `claude/brave-galileo-jhp684`). Elle accorde le code de la première passe, c'est-à-dire la lecture des directions des sondes par la lentille publique, à l'addendum de concentration scellé. Dis si ce code fait **exactement** ce que disent le texte de lecture v1, l'addendum et le mot de Lazar sur la garde d'égalité, ni plus ni moins, et si chaque garde est éprouvée sur un cas sain et sur un artefact (R5).

Ton rendu sera l'un de ces trois verdicts :
- **conforme** : le code peut être fixé au registre tel quel ;
- **conforme sous corrections** : une liste numérotée de corrections, chacune avec le fichier, la ligne, le texte qui fait loi (section et phrase citée), ce qui ne va pas et ce qu'il faudrait ;
- **non conforme** : les écarts bloquants.

Sépare les écarts **bloquants**, c'est-à-dire un calcul, une garde ou un arrêt qui diffère du texte, de ceux qui sont **non bloquants** (nom, commentaire, essai souhaitable).

## Textes qui font loi

Lis-les sur la branche principale par `git show origin/main:<chemin>` (lance d'abord `git fetch origin main`), et vérifie chaque empreinte avant de lire :
- `prereg/lecture-sondes-bbis-par-lentilles-v1.md` — `ca5066d757df604c…` (empreinte entière dans `prereg/lecture-sondes-bbis-par-lentilles-v1.md.sha256` sur la branche principale). Sections à lire : « Métrique », « Seuil », « Plan d'analyse », « Liste d'arrêt », « Lignes de registre », « Code neuf ». Tu peux lire le reste du texte, sauf toute liste intitulée « Jamais ouverts », que tu n'ouvres pas.
- `prereg/lecture-sondes-bbis-par-lentilles-v1-addendum-concentration-v1.md` — `7c7387088dd5956d3e75bd8e859346dd4db560582fd2f239d2c892b4d2c22970`, en entier.
- `docs/notes/neuron-lens-v1/mot-lazar-garde-egalite-vingtieme-rang-2026-11-19-v1.md` — `dbd1e5140b987ed2…` (option 3 de la garde d'égalité au vingtième rang).
- Pour le départage par identifiant de jeton croissant et pour les paliers de N12 et N17 : ce que l'addendum en dit suffit ; ne cherche pas ailleurs.

## Pièces à contre-lire (branche `claude/brave-galileo-jhp684`, commit `2e15977b`)

Code (`src/controle_ia/lentilles_sondes_bbis/`) :
- neuf : `entrees_v3.py` (8baf6a12…), `statistiques_v3.py` (9a478aa8…), `lanceur_v4.py` (dc74be00…) ;
- ce qu'ils appellent : `statistiques_v2.py`, `statistiques_v1.py`, `entrees_v2.py`, `audits_v1.py`, `constantes_v1.py`, `nuls_v1.py`, `lecture_v1.py`, `montage_v1.py`, `phrases_v1.py`, `__init__.py`, et `lanceur_v3.py` pour la différence.

Essais (`tests/`) :
- `test_lentilles_sondes_bbis_addendum_concentration_v2.py`, `test_lentilles_sondes_bbis_garde_egalite_v1.py`, `lentilles_sondes_bbis_jouets_v4.py` ;
- `test_lentilles_sondes_bbis_entrees_v4.py`, `…_montage_v4.py`, `…_procedure_v4.py`, `…_nuls_statistiques_v3.py`, `…_gardes_non_vues_v3.py`, `…_corrections_contre_lecture_v3.py`.

Notes (`docs/notes/lecture-sondes-bbis-par-lentilles-v1/developpement/`) :
- `conformite-code-a-l-addendum-concentration-scelle-v1.md`, `table-essais-v2.md`, `notes-developpement-v2.md`, `sortie-essais-v4.txt`, `empreintes-code-v4.txt` ;
- `outils/fabrique-lanceur-v4-v1.py`, `outils/essai-des-essais-v3.py`, `outils/sortie-essai-des-essais-v3.txt`, `outils/banc-taille-reelle-v3.py`, `outils/sortie-banc-taille-reelle-v3.txt`.

Vérifie d'abord `empreintes-code-v4.txt` contre le disque (`grep -v '^#' … | sha256sum -c`) et les compagnons `.sha256` des notes (`PYTHONPATH=src python -m controle_ia.scellement verifier …`).

## À vérifier d'abord

1. Les quatre précisions de lecture prises par le développeur (note de conformité, § 3), dont :
   - « inscrite avant » (EC-4) : place et heure de la ligne de l'addendum face aux lignes `CODE-` et `ENTREES-LENTILLES-BBIS` ;
   - le champ `addendum_concentration` de la fiche du code, nom choisi par le développeur ;
   - aucune relecture indépendante de l'audit de symétrie ajoutée à EC-6 ;
   - arrêt quand toutes les directions d'un nul sont marquées.
   Dis pour chacune si le texte la permet, l'exige ou l'interdit.
2. `bornes_de_departage` contre ta propre énumération, indépendante, des bornes de l'addendum (§ 7, les 41 bornes) : écris-la sans regarder le code, puis compare.
3. La place de chaque appel de la garde d'égalité au vingtième rang dans `lanceur_v4`, contre les trois étages de l'option 3.
4. Que `exiger_addendum` (ou ce qui en tient lieu) refuse chaque cas de la « Liste d'arrêt » qui le concerne, et chaque artefact de EC-4.
5. Que rien d'autre ne change de `lanceur_v3` à `lanceur_v4` que ce que l'addendum demande, plus un changement déclaré : le rapport du montage exigé au départ du calcul. Dis si ce changement est permis par les textes.
6. Les essais de EC-5 : l'artefact de taux (M = 19, 128 jetons, 2 000 répliques, part entre 0,03 et 0,065) et les bornes du § 7 sont-ils joués, avec un cas sain et un artefact ?
7. La comparaison des concentrations en simple précision (C5).
8. Les deux points que le développeur laisse à la session :
   - le message de l'arrêt d'une direction lue donne deux identifiants de jeton et la valeur commune, et l'opérateur le verrait. Est-ce bien ce que l'addendum exige, et l'opérateur est-il censé ne lire que les codes d'arrêt ?
   - la docstring « exacte » de `audits_v1` est laissée telle quelle, sans `audits_v2`. Est-ce conforme à l'addendum, § 4 ?
9. Un écart d'empreinte à expliquer : le rendu du développeur donne pour `test_lentilles_sondes_bbis_addendum_concentration_v2.py` l'empreinte `1abbe232…`, mais le disque et `empreintes-code-v4.txt` portent `cf92419d…`. Dis lequel correspond au fichier commité et si la sortie d'essais `sortie-essais-v4.txt` a été produite avant le dernier changement de ce fichier.

## Ce que tu peux lancer

- `pip install` de torch en version processeur, et des paquets du fichier `requirements-cpu.txt`, dans un environnement virtuel du bloc-notes. Rien d'autre à télécharger : aucun modèle, aucune lentille, aucun corpus.
- Les essais du paquet : `PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src python -m pytest -q tests/test_lentilles_sondes_bbis_*.py`. Ils prennent environ neuf minutes. Lance-les en entier une fois et rapporte le décompte. Ne lance pas la suite complète du dépôt.
- Tes propres essais jetables, mais dans le bloc-notes, jamais dans le dépôt.

## Ce que tu n'ouvres jamais

- La liste « Jamais ouverts » du texte de lecture v1, et tout ce qu'elle nomme.
- Toute sortie, tout score, toute table, toute lecture ou tout verdict de l'apprentissage des sondes sur la tâche (étape B bis), y compris la clé `VERDICT-BBIS` et la note de lecture réservée à Lazar.
- Toute table ou sortie de la lecture par la lentille publique.
- `diag/`, `runs/`, `donnees/`, `docs/verdicts/`, et les branches `donnees/*` et `calcul/*`.
- Tout fichier dont le nom contient « consigne-privee » ou « conception-ii-b », et `brouillons/ii-b-saboteur-budget-v1/`.
- P3, P3-bis, T0.6, T0.7 hors des textes cités, l'étape B, le bras d'attaque, le saboteur à budget.
- Les registres de la branche principale. Seule exception : `registres/lecture-sondes-bbis-par-lentilles-v1.md`, si tu dois voir la forme d'une ligne. Déclare tout intitulé que tu verrais par mégarde.
- Aucune clé ni aucun secret.

## Règles de travail

- **Tu n'écris rien dans le dépôt.** Tu ne fais aucun commit et aucun push. Ton rendu est ton message final ; la session des lentilles le versera, scellé.
- Un refus d'outil n'est jamais rejoué, reformulé ni contourné ; il est déclaré.
- Aucune nouvelle règle. Si le texte est muet ou ambigu, dis-le comme un nœud à trancher par Lazar, sans trancher toi-même.
- Langue : français. Nomme les choses en clair ; un identifiant ne vient qu'en appui.

## Forme du rendu

1. Verdict en une à trois lignes.
2. Empreintes vérifiées (OK ou écart).
3. Décompte des essais lancés.
4. Points 1 à 9 ci-dessus, chacun avec ta réponse.
5. Corrections numérotées : d'abord les bloquantes, puis les non bloquantes.
6. Nœuds à trancher par Lazar, s'il y en a.
7. Expositions : ce que tu as ouvert hors de cette liste, ou « aucune », et tout refus d'outil.

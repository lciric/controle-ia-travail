# Consigne — contre-lecture 2 (différentielle) du brouillon 3 « validité de l'adaptateur », sur T0.7 scellé — v1

Écrite le 2026-11-13T21:00:56Z (heure relevée par `date -u`) par la session du compte 4 (`session_01Qi7Gr2uGzyVcw9VmDXgvEV`, Claude Opus 5.5, `claude-opus-5-5`). Lot : `docs/notes/plan-paquet-multi-comptes-v1/plan-paquet-multi-comptes-v1.md` (`3b1bda25…`), lot « compte 4 », tâche 1. Cette consigne n'accorde aucune dépense, aucune publication, aucun changement de revendication.

## 0. Interdits permanents (recopiés du brief du compte 4, section 6, sans changement)

- Aucune dépense ni machine louée sans ligne de GO inscrite **et** mot de Lazar.
- Aucune valeur de clé : jamais `env`, `printenv`, `set` sans argument, `export -p`, `/proc/*/environ`.
- Jamais `diag/*/lecture-sondes-t06.json`, la lecture B de 7a, `donnees/lecture-b-7a-quarantaine-v1`, `donnees/mesure-unanime-v15-sortie-v1`, `essai/t06-explo-v3`, aucun `diag/` ni `runs/` de 7a ou 7b, l'étiqueteur, `scripts/extraire_mesures_epreuve_t06_v1.py`, la branche `calcul/p3bis-reel-v2`.
- Jamais `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/`, `registres/index-bras-attaque*`, `anteriorite-bras-informe*`, ni la branche `claude/compassionate-meitner-d4ryyk`.
- Aucune recherche récursive qui traverse ces chemins : pas de `ls registres`, pas de `find` ni de `grep -r` larges ; fichiers nommés seulement.
- Jamais d'heure écrite à la main (`date -u` dans la même commande). Jamais de `git fetch` sans refspec.
- Garde des secrets à 0 avant chaque commit (sans objet ici : tu ne commites rien).
- Jamais toucher les instances Vast 58936096, 58936099, 58936100, 60480302, 60541314 ni les serveurs Hetzner `poste-temoin-bailey-*` ; aucun appel au loueur.
- Ne jamais contourner, reformuler ni confier à une autre session un refus de permission, du crochet ou d'un classifieur : arrêt, rapport à la mère.
- Rien de publié, aucun contact extérieur (tu rédiges, Lazar envoie).

**Ajoutés pour cette contre-lecture.**
- Lecture seule, sauf les deux fichiers du § 5. Aucune écriture git (ni `add`, ni `commit`, ni `push`, ni `checkout`, ni `fetch`), aucun appel réseau, aucune recherche sur la toile, aucun sous-agent.
- **Aucun fichier de `registres/`** (la mère n'en a nommé aucun pour ce lot) ; **aucun fichier de P3-bis** (procédure du rendez-vous, consigne du lecteur, verdict, tout `docs/verdicts/verdict-P3-bis*`) ; **rien de `donnees/`, `diag/`, `runs/`**.
- Pas de `verifier-arbre` ; `PYTHONPATH=src python3 -m controle_ia.scellement verifier <fichier>` sur fichiers nommés seulement.
- Dans un fichier nommé, `grep -n`, `sed -n` ou l'outil de lecture sur ce seul fichier ; jamais `grep -r`, `find`, `ls -R`, `git grep`.
- Aucune lecture de sonde, de score ni de résultat d'aucune course (tu lis des textes et du code, rien d'autre).

## 1. Qui tu es

Contre-lecteur **neuf**, sous-agent de la session du compte 4. Tu n'as écrit ni ce texte ni ses brouillons, ni T0.7, ni son module, ni T0.6, ni P3-bis. Ton modèle doit être **différent** de celui de l'auteur du brouillon 3 (Claude Opus 5.5, `claude-opus-5-5`) : écris en tête de ton rapport ton identifiant de modèle tel que ton environnement te le donne. En lisant T0.7 scellé, tu deviens « lecteur de T0.7 » : tu es exclu ensuite de tout rôle de lecteur ou d'hôte du verdict de P3-bis, et des verdicts de l'étape B de T0.7, de T0.8, du contrôle de l'adaptateur et du barreau 6 (la session du compte 4 te déclare à la mère pour la liste « qui a lu quoi »). Français ; aucun sigle non développé.

## 2. Objet

Le brouillon 3 a été écrit **sans lire T0.7** : chacune de ses dépendances envers T0.7 vient du brouillon 21 de T0.7 (module au commit `8ae9fc44`), telle que la contre-lecture 1 la levait, et porte la marque « (T0.7 brouillon 21, levé par la contre-lecture 1 ; …) ». T0.7 est depuis **scellé** (`prereg/T0.7-sondes-v0-v1.md`, candidat 5) ; son en-tête dit notamment que l'étape A tire **800 directions** de plancher (le brouillon 21 en tirait 200) et que le plancher décisif des deux sondes figées de P3 est neuf. Ta contre-lecture tient lieu de la « contre-lecture suivante » que le brouillon 3 prévoit (section « Contre-lecture », dernier paragraphe) : différentielle (brouillon 2 → brouillon 3) **et** sur T0.7 scellé et son module. Elle seule peut lever la réserve générale du brouillon 3. Tu ne corriges aucun fichier : tu rends un rapport.

**Faits donnés par la session du compte 4, non relus au registre (le registre t'est interdit) :**
- La course 7b est finie le 12 novembre ; la pièce HD (témoin distillé honnête), prévue en parallèle de sa marche (lecture large R-2207, « Q-1 »), **n'a pas été jouée** (plan multi-comptes, section 4.2 et lot « compte 4 », réserves ; décision D-11 du plan).
- Messages de commit de `main` : l'étape A de T0.7 s'est arrêtée « au contrôle avant l'ouverture, instance détruite » (`7abb0d83`, R-2588, 2026-11-13 vers 20:32 UTC) ; « cause de l'arrêt établie sans dépense » (`b13ff07b`, R-2589). Aucun score de T0.7 n'existe donc à ce jour. Le calendrier écrit au brouillon 3 est périmé.
- Le plan dit qu'un **erratum des 200 directions** touche le texte scellé de T0.7, et qu'il « se cite, il ne se corrige pas ». La session du compte 4 n'en a pas le chemin (demandé à la mère). Si tu rencontres dans T0.7 scellé un passage qui contredit les 800 directions, cite-le (ligne, extrait) ; ne propose **jamais** de corriger T0.7.

## 3. Fichiers à lire (vérifie chaque empreinte avant lecture : `sha256sum <fichier>`, ou `verifier` s'il a un compagnon)

| rôle | chemin | sha256 |
|---|---|---|
| texte contre-lu | `brouillons/validite-adaptateur-v1/validite-adaptateur-preenregistrement-v1-brouillon3.md` | `defd8ef05038e703…` (compagnon) |
| son journal | `brouillons/validite-adaptateur-v1/validite-adaptateur-preenregistrement-v1-brouillon3-journal-v1.md` | `fbb649c0245ad0b1d76a1249d4dd34013d073876ccab59a487cb74edfa22d083` |
| brouillon 2 (base du différentiel) | `brouillons/validite-adaptateur-v1/validite-adaptateur-preenregistrement-v1-brouillon2.md` | `be0851f57bc09dc21ae7ed661d983fdf9aa0fb0148ea19c15f72c1c2bca830d9` |
| journal du brouillon 2 | `brouillons/validite-adaptateur-v1/validite-adaptateur-preenregistrement-v1-brouillon2-journal-v1.md` | `d4f503d29ab5f6af149b3f7d7340b1ee6a6407b169c8ee586b4cef322ca99567` |
| contre-lecture 1 | `prereg/contre-lectures/validite-adaptateur-preenregistrement-v1-brouillon2-cl1.md` | `cf84198566978307c3cc3e1d10e62245042446b569a407b66bbcb029ffe9764e` |
| **T0.7 scellé** (≈ 754 ko : lis par sections et par `grep -n` dans ce seul fichier) | `prereg/T0.7-sondes-v0-v1.md` | `d7d180eccbbce8ff…` (compagnon) |
| configuration de T0.7, v8 | `prereg/T0.7-sondes-v0-v1-configuration-t07-v8.json` | `e31c7a79dc1b68d561874d4d42d63b5eb950931f06075927f239c7ad971fb328` |
| vérification finale du candidat 4 de T0.7 (au besoin) | `prereg/contre-lectures/T0.7-sondes-v0-v1-candidat4-verification-finale-v1.md` | `26efc4dfb4924e6a2d6ddfaf7fdb37a6dae453946b1a114df2ec76ec014ad257` |
| vérification mécanique du candidat 5 de T0.7 (au besoin) | `prereg/contre-lectures/T0.7-sondes-v0-v1-candidat5-verification-mecanique-v1.md` | `84ffcb01758894781a738b0254d8dee7eda26fb81f1f67bfcce602ca78c91edd` |
| module de T0.7 sur `main` (fichiers nommés seulement) | `src/controle_ia/t07/<nom>.py` : en priorité `lecture_v4.py`, `lecture_v3.py`, `lecture_v2.py`, `criteres_v1.py`, `plancher_v2.py`, `plancher_v3.py`, `repli_recalcul_v1.py`, `reextraction_p3_v1.py`, `sondes_neuves_v1.py`, `registre_v1.py`, `mahalanobis_v1.py`, `code_t07_v1.py` | empreintes des huit modules neufs à comparer à l'en-tête de T0.7 scellé (ligne 695, « état au candidat 4 ») |
| fonctions citées par le brouillon 3 | `src/controle_ia/premier_test_ia/figees.py` (`lire_sondes`), `src/controle_ia/premier_test_ia/conditions.py` (`mesures_action`) | — |
| note 2a | `docs/notes/rapports-directeur/premisses-trace-interne-v1-point-2a.md` | `2db916aa125d37504d58d712396a59d2ed5c934a0c5438787cb68a55113e8305` |
| T0.6 scellé (par sections) | `prereg/T0.6-organismes-v0-v1.md` | `ef31feff9abb26d0…` (compagnon) |
| configuration de 7b | `prereg/T0.6-organismes-config-7b-v1.json` | `b7a5c1baeee13f7589b296fb166180515422ebc8c7eff703994bb5b6835ae527` |
| gabarit | `prereg/gabarit-preregistrement-v1.md` | `8cad43714b562e28238a92200d6315b1769d8bdf7e9f0a8d72dfe2bc9b37700e` |
| validateur | `src/controle_ia/prereg.py` (fonction `problemes(chemin)`) | `3b2e3ee56463f30ffd3c549e7fe480fea574c707581bcf30098bf38f4980c306` |

Le dépôt local est un clone superficiel : les commits `8ae9fc44`, `37485ce5`, `0d0c5da4`, `a621dcd3`, `1609a4bf` n'y sont pas. Le module de T0.7 est sur `main` (`src/controle_ia/t07/`) ; compare les empreintes que tu peux recalculer à celles que T0.7 scellé écrit, et dis ce que tu n'as pas pu vérifier.

## 4. Ce que tu vérifies

1. **Chaque dépendance envers T0.7** du brouillon 3 (chaque marque « levé par la contre-lecture 1 », et toute mention d'un fichier, d'un tableau, d'un champ JSON, d'une clé de registre, d'une fonction, d'un module, d'un commit, d'une ligne de T0.7, d'une réserve R1 à R15, d'un niveau ou d'un temps de T0.7) : T0.7 scellé et le module sur `main` disent-ils la même chose ? Donne la ligne de T0.7 scellé (ou fichier:ligne du module) et un extrait court. Parmi elles, sans t'y limiter : nombre de directions de plancher et forme des tableaux `plancher_<k>` ; règle de lecture décisive de T0.7 contre le plancher (et ce que T0.7 dit de l'erreur de première espèce à 200 directions) comparée à la règle « au-dessus » de ce texte ; plancher des sondes figées de P3 (neuf, fichier `planchers-figees-t07.npz`, ou les 200 de P3) ; champs de `sondes-t07.json`, `notation-t07.json`, `lecture-t07.json`, `arret-etape-b.json` ; clés admises par la garde de T0.7 dans `registres/scellements-v1.md` ; recalcul (`repli_recalcul_v1`) et garde d'équivalence ; `preparer_sonde`, `lire_sondes`, `mesures_action` ; Mahalanobis ; temps de notation par direction.
2. **Différentiel brouillon 2 → brouillon 3** (`diff` des deux fichiers nommés) : chaque changement applique-t-il correctement la contre-lecture 1 et les décisions de la mère que le journal du brouillon 3 recopie ? Un changement sans fondement ? Un constat de la contre-lecture 1 non appliqué ? Un défaut neuf introduit ?
3. **Conséquences pour ce texte des 800 directions** : forme des tableaux lus par la pièce L ; nombre de directions notées par la pièce R et son temps (devis, coupures, nœud N-VA-1) ; quantile du plancher ; puissance. Recalcule ce qui est arithmétique (script court, sortie recopiée dans ton rapport).
4. **Passages qui supposent la pièce HD jouée en parallèle de 7b** (« Q-1 », R-2207 ; ordre, calendrier, inventaire, liste d'arrêt de T0.6, devis) : liste-les ; décris la conséquence si HD se joue désormais après la fin de 7b et après le verdict de P3-bis (plan, section 7, point 7). Tu décris ; tu ne tranches pas (c'est à Lazar).
5. **Champs fixés par le seul code de T0.7** (journal du brouillon 3, § 3, « Champs fixés par le seul code de T0.7 », et tous ceux que tu trouves) : pour chacun, ce que T0.7 scellé en dit, ce que le module sur `main` en fait (fichier:ligne), et s'il reste une confirmation à demander au développeur de T0.7. Idem pour CLVA-17 (aucune garde de T0.7 ne compte les ouvertures de `scores-actions-t07.npz` hors de son journal).
6. **Forme** : `PYTHONPATH=src python3 -c "from controle_ia.prereg import problemes; print(problemes('brouillons/validite-adaptateur-v1/validite-adaptateur-preenregistrement-v1-brouillon3.md'))"` ; conformité au gabarit.
7. **Faits de registre** que tu ne peux pas vérifier (R-2175, R-2177, R-2207, R-2210, `GO-2026-11-10-07`, toute autre ligne) : liste-les, avec la phrase du brouillon 3 qui en dépend.

**Gravité.** *Bloquant* : faux sur T0.7 scellé ou son module (champ, fichier, clé, fonction inexistants ou autres), garde qui refuserait à tort ou laisserait passer, règle de lecture qui contredit T0.7 ou le programme, interdit du programme touché. *Majeur* : à corriger avant le scellement, correction locale. *Mineur* : le reste.

## 5. Ce que tu rends

Un seul rapport, `prereg/contre-lectures/validite-adaptateur-preenregistrement-v1-brouillon3-cl2.md`, scellé par `PYTHONPATH=src python3 -m controle_ia.scellement sceller <fichier>` (compagnon `.sha256`), puis vérifié par `verifier`. Si tu écris un script d'arithmétique, dépose-le à côté sous `prereg/contre-lectures/validite-adaptateur-preenregistrement-v1-brouillon3-cl2-calcul.py`, scellé aussi, sortie recopiée à l'octet dans le rapport. Rien d'autre n'est écrit.

Sections du rapport :
- **0. Identité** : ton identifiant de modèle ; heures de début et de fin (`date -u`) ; table des fichiers lus, empreinte vérifiée, parties lues.
- **1. Verdict** (trois lignes au plus) : « scellable tel quel », « scellable après les corrections listées » ou « non scellable en l'état » ; nombre de constats par gravité.
- **2. Constats**, un par ligne : identifiant `CLVA2-01`, `CLVA2-02`… ; gravité ; endroit du brouillon 3 (ligne et extrait court) ; preuve (ligne de T0.7 scellé ou fichier:ligne du module, extrait de trente mots au plus) ; correction proposée. Quand la correction est mécanique : couple exact « ancien » → « nouveau », « ancien » présent **une seule fois** dans le brouillon 3. Quand elle change le dessin (règle de lecture, seuil, devis, coupure, plafond, ordre des pièces) : deux ou trois options (avantage, inconvénient), ta recommandation et ta confiance, marquée « décision de la mère » ou « nœud (Lazar) ».
- **3. Couples** : un bloc JSON `[{"id": "CLVA2-01", "ancien": "…", "nouveau": "…"}, …]` des seules corrections mécaniques.
- **4. Champs fixés par le seul code de T0.7** (point 4.5).
- **5. Pièce HD non jouée en parallèle de 7b** (point 4.4).
- **6. Non vérifiable** (point 4.7).
- **7. Limites** : ce que tu n'as pas lu ou pas pu vérifier.

Ton dernier message (rendu à la session du compte 4) : le verdict en trois lignes, les nombres de constats, le chemin et l'empreinte du rapport (et du script s'il existe), ton identifiant de modèle. Rien d'autre.

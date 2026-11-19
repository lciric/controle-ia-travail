# Contre-lecture du code de formation des familles d'adaptateurs jumeaux (barreau 5) — v1

- Contre-lecteur : sous-agent neuf, Claude Fable 5.2, autre modèle que le développeur (Claude Opus 5.5). Pièce de classe B. Écrit le 19 novembre 2026 ; fini vers 17:55Z (`date -u`).
- Mandat : `mandat-contre-lecteur-code-formation-v1.md`, `cfa0ff64cfbbb91ed62b63f04499834e68b8bc3fc3cb056303cd28a5729c5f22` (vérifié).
- Pièces vérifiées par empreinte : rapports du développeur v1 (`85004d61…`) et v2 (`d24a76d1…`) ; texte, brouillon 3 (`525f338e…`) ; devis du brouillon 3 (`7ac56a7b…`) ; table des corrections (`1d010c7d…`) ; contre-lecture du brouillon 2 (`29b86657…`) ; mandat du développeur (`94c6bbb3…`). Les onze fichiers de code et d'essais ont les empreintes du § 5 du rapport v2 ; ils sont à la tête `62194f6b0` sans modification locale.
- Fait : lecture entière des quatre modules, des deux scripts, des cinq fichiers d'essais et des sections figées du texte ; lecture des modules réemployés aux endroits appelés ; les 161 essais joués une fois (161 passés, 116 s) ; 20 défauts réintroduits un à un, plus un témoin et deux mutations inverses, dans 23 copies hors du dépôt ; six sondages sur le modèle jouet ; l'extraction partielle de l'amorce rejouée dans le bloc-notes, et les essais du paquet joués sur cet arbre.
- Rien de réel : aucun réseau vers le loueur, aucune instance, aucune dépense, aucun commit. Le code du dépôt n'a pas été modifié. Aucune donnée ni résultat ouvert.
- **Incident déclaré.** Ma première lecture des deux rapports a dépassé la taille admise : l'outil a déposé la sortie sous `/root/.claude/…`. Je n'ai pas ouvert ce fichier ; j'ai relu les rapports depuis le dépôt. Aucun refus d'outil.
- Outils et sorties : dossier `outils-contre-lecture-code-formation-v1/` (liste à la fin).

## Verdict

**Conforme après ces corrections.** En l'état, le code ne doit être ni figé ni lancé : un constat bloquant, que les 161 essais ne voient pas, fausse en silence six familles sur treize.

| classe | nombre |
|---|---|
| bloquant | 1 |
| majeur | 9 |
| mineur | 14 |

L'opérateur d'édition du coût, la pièce la plus délicate, est juste dans tout ce que j'ai pu éprouver : 72 éditions vérifiées par un calcul indépendant, aucun jeton changé hors du nombre. Les défauts sont ailleurs : l'état du modèle entre deux familles, le lanceur, l'amorce, et des essais qui laissent passer 14 défauts réintroduits sur 20.

## Constat bloquant

### B-1 — La seconde famille d'une instance est tirée sous un adaptateur de la première, et non sur le modèle nu

- **Où.** `formation_v1.py`, `_former_une_famille`, l. 777-779 ; `evaluer_membre`, l. 549-550 ; `_executer`, l. 744-747.
- **Fait.** `evaluer_membre` charge l'adaptateur du membre et met la dose à 1. Rien ne remet la dose à 0 ensuite. La famille suivante de la même instance commence par `tirer_famille` : ses 160 épisodes du saboteur instruit sont donc générés sous le dernier adaptateur évalué de la famille précédente, à la dose 1.
- **Preuve.** Sondage S1 (`sortie-sondages-cl-v1.txt`) : marche jouet à deux familles. À l'entrée du tirage de la seconde, la dose lue vaut 1, les adaptateurs chargés sont ceux du dernier membre évalué de la première, et les logits d'un contexte fixe diffèrent de ceux du modèle nu. À l'entrée du premier tirage, les matrices B sont nulles et les logits sont égaux.
- **Portée.** Six familles sur treize : T02, T04, T06, T08, T10 et A2. Le texte demande « un tirage de 160 épisodes neufs du saboteur instruit (consigne scellée, modèle nu) » (plan, point 2) et des familles « tirées indépendamment » (hypothèse nulle). Les deux tombent : les données de T02 dépendent d'un adaptateur de T01, lui-même saboteur, jumeau ou sur-saboteur selon l'ordre tiré. L'épreuve exacte suppose l'indépendance des familles.
- **Pourquoi les essais ne le voient pas.** Le jouet de bout en bout forme bien deux familles, mais son tirage est écrit par programme : le modèle n'y est pas appelé.
- **Correction.**
  1. `formation_v1.py`, l. 53 — avant : `from ..t06.identite import controle_identite, exiger_etat_de_phase, logits_de_controle` ; après : ajouter `etat_adaptateurs` à cet import.
  2. Fonction neuve, après `exiger_meme_etat_initial` (l. 492) :
     ```python
     def exiger_modele_nu(modele, ids_controle, logits_base, quoi: str) -> None:
         """Texte, point 2 : le saboteur instruit est tiré sur le modèle nu. Dose lue à 0 sur tous les modules, et logits
         du contexte de contrôle égaux, au bit près, à ceux relevés avant l'injection."""
         e = etat_adaptateurs(modele)
         if e["dose"] != 0.0:
             raise GardeArret(f"{quoi} : dose lue {sorted(set(e['doses'].values()))} ≠ 0 : pas le modèle nu (point 2)")
         l0 = logits_de_controle(modele, ids_controle)
         if l0.shape != logits_base.shape or not torch.equal(l0, logits_base):
             raise GardeArret(f"{quoi} : logits du contexte de contrôle ≠ ceux du modèle nu (point 2)")
     ```
  3. `_executer`, après la l. 747 (`dt.adaptateurs_en_simple_precision(modele)`) : ajouter `lo.fixer_dose(modele, 0.0)`.
  4. `_former_une_famille`, l. 778-779 — avant :
     ```python
             etat["etape"] = f"tirage {nom}"
             episodes = tirer_famille(modele, fmt, nom, taches["reserve"], config, consignes, guide, g, pad, jouer_tirage)
     ```
     après :
     ```python
             etat["etape"] = f"tirage {nom}"
             lo.fixer_dose(modele, 0.0)
             exiger_modele_nu(modele, ids_controle, logits_base, f"avant le tirage de {nom}")
             episodes = tirer_famille(modele, fmt, nom, taches["reserve"], config, consignes, guide, g, pad, jouer_tirage)
             exiger_modele_nu(modele, ids_controle, logits_base, f"après le tirage de {nom}")
     ```
  5. `_former_une_famille`, avant la l. 818 (`exiger_sorties_permises(racine_sorties)`) : ajouter `lo.fixer_dose(modele, 0.0)`.
  6. Essais (R5). Cas sain : modèle injecté, dose 0, la garde passe ; adaptateur appris chargé, dose 0, elle passe. Artefacts : dose 1 avec des matrices B nulles (refus par la dose) ; adaptateur appris à la dose 1 (refus). Et un essai de bout en bout à deux familles sur la même instance qui relève, à l'entrée de chaque tirage, la dose et l'égalité des logits (forme du sondage S1).

## Constats majeurs

### M-1 — La commande de création ne transmet pas les clés : les sept instances s'arrêteraient au clonage

- **Où.** `formation_v1.py`, l. 968 ; `tests/test_lancer_b5f_formation_v1.py`, l. 105 ; `amorce_b5f_formation_v1.sh`, l. 128-129.
- **Fait.** La commande imprimée porte `-e HF_TOKEN=\$HF_TOKEN -e GH_TOKEN=\$GH_TOKEN` entre guillemets doubles. Jouée dans un shell, la barre protège le signe : le loueur reçoit le texte « $HF_TOKEN », non la valeur (sondage S2). Les lanceurs de l'étape B bis impriment `$HF_TOKEN` sans barre (`scripts/lancer_bbis_v5.sh`, l. 97) : la barre de leur source bash disparaît à l'affichage, celle de la source Python reste. L'essai du développeur exige la barre : il fige le défaut.
- **Effet.** Sur l'instance, les deux variables sont non vides : l'amorce passe ses contrôles, puis échoue au clonage. Bruyant et peu coûteux, mais un départ entier perdu.
- **Correction.**
  - `formation_v1.py`, l. 968 — avant : `f"-e GO_ID={go_id} -e DEPOT_URL={DEPOT_URL} -e HF_TOKEN=\\$HF_TOKEN -e GH_TOKEN=\\$GH_TOKEN\" "` ; après : `f"-e GO_ID={go_id} -e DEPOT_URL={DEPOT_URL} -e HF_TOKEN=$HF_TOKEN -e GH_TOKEN=$GH_TOKEN\" "`.
  - Essai, l. 104-105 — avant : `"HF_TOKEN=\\$HF_TOKEN", "GH_TOKEN=\\$GH_TOKEN"` ; après : `"HF_TOKEN=$HF_TOKEN", "GH_TOKEN=$GH_TOKEN"`, plus `assert "\\$" not in cmd`, plus un essai qui joue la ligne dans un bash où `vastai` est une fonction qui affiche ses arguments, avec deux valeurs factices (forme du sondage S2).
  - Amorce, après la l. 129 : `case "${GH_TOKEN:-}${HF_TOKEN:-}" in *'$'*) arret "GH_TOKEN ou HF_TOKEN : un nom de variable reçu à la place d'une valeur (par le nom)" 2;; esac`.

### M-2 — La minuterie détruit l'instance sans savoir si les sorties sont versées

- **Où.** `amorce_b5f_formation_v1.sh`, l. 73-81 (minuterie), l. 121, l. 193-197 (boucle d'attente), l. 202-205.
- **Fait.** À l'échéance d'arrêt plus 15 minutes, la minuterie envoie la destruction, quoi qu'il soit arrivé au versement. Deux chemins y mènent avec des sorties non versées : le dépôt distant injoignable pendant le quart d'heure ; ou la boucle d'attente, qui dort 600 secondes d'un trait : si la marche est arrêtée à l'échéance au début d'un sommeil, il reste, au pire, 900 − 600 − 120 = 180 secondes pour tout le versement final.
- **Règle touchée.** « Aucun orchestrateur ni programme ne supprime une sortie de course avant ce versement » (`CLAUDE.md`) ; liste d'arrêt, point 14 : « destruction par identifiant, après versement de ce qui est récupérable ». La minuterie de l'étape B bis a la même forme ; elle est plus ancienne que la règle.
- **Qui tranche.** Lazar : c'est un arbitrage entre la garde de dépense et la règle de récupération. **Ma recommandation** : la minuterie ne détruit que si le versement final est prouvé ; sinon elle demande l'état « stopped » (le disque reste, au plus 0,08 USD de l'heure, jusqu'à ce que la session ait prouvé le versement et détruit).
- **Correction proposée.**
  - l. 193-194 — avant :
    ```bash
    while kill -0 "$PID" 2> /dev/null; do
        sleep "$PERIODE_VERSEMENT_S"
    ```
    après :
    ```bash
    while kill -0 "$PID" 2> /dev/null; do
        n=0; while [ "$n" -lt "$PERIODE_VERSEMENT_S" ] && kill -0 "$PID" 2> /dev/null; do sleep 15; n=$((n + 15)); done
    ```
    (l'essai du texte de l'amorce, l. 196, attend une seule ligne de sonde de vie : à ajuster).
  - après la l. 203 (versement final réussi) : `[ "$(git -C "$D" ls-remote origin "refs/heads/$BR" | cut -f1)" = "$(cat "$T/parent-sortie")" ] && : > "$T/versement-final-prouve"`.
  - minuterie, l. 76-81 : à l'échéance, si `$T/versement-final-prouve` existe, destruction par l'identifiant comme aujourd'hui ; sinon, demande d'état « stopped » par l'identifiant, répétée, et ligne de journal « versement final non prouvé : aucune destruction (nœud) ».
  - Essais : la minuterie avec et sans le témoin (faux `curl`) ; la boucle d'attente qui rend la main en moins de 20 secondes après la fin de la marche.

### M-3 — Un texte scellé « comme brouillon » passe pour le préenregistrement scellé

- **Où.** `formation_v1.py`, `executer`, l. 700-712 ; `lire_code_et_accord`, l. 655-673 ; `commande_de_creation`, l. 946-959.
- **Fait.** La marche réelle exige un texte « scellé et conforme » (`exiger_prereg_scelle`). Le brouillon 3, « non scellable », a un compagnon d'empreinte et passe ce contrôle (vérifié : `problemes` rend une liste vide). Rien ne lie le texte cité à la ligne `SCELLEMENT-B5F` du registre propre, que le code ne lit pas.
- **Règle touchée.** R1 ; liste d'arrêt, point 1.
- **Correction.** `lire_code_et_accord` exige aussi la ligne `SCELLEMENT-B5F`, de contenu « `<chemin du texte>` ; sha256 `<64>` », d'instant antérieur à `GO-FORMATION-B5F`, et rend chemin et empreinte. `executer` (après la l. 705) et `commande_de_creation` (après la l. 958) refusent si le texte cité n'est pas ce chemin ou si son empreinte, au commit de la course, n'est pas celle de la ligne. Essais : cas sain ; ligne absente ; autre chemin ; empreinte différente. Le format de la ligne est à fixer par la mère (choix 11 du rapport v1).

### M-4 — Transcriptions inégales : le code arrête toute l'instance, et le tirage n'est pas encore sur disque

- **Où.** `formation_v1.py`, `_former_une_famille`, l. 777-787 ; `membres_de_famille`, l. 463-468.
- **Fait.** La liste d'arrêt, point 4, dit : « transcriptions de deux membres différentes hors des jetons du nombre : la famille n'est pas formée ; un seul retirage ». Le code lève une garde qui arrête la marche : la seconde famille de l'instance est perdue avec la première. De plus, `membres_de_famille` est appelée avant l'écriture des textes : si elle s'arrête, les 160 épisodes tirés (le poste le plus long d'une famille) ne sont nulle part sur disque, et rien n'en est versé.
- **Correction.**
  - `_former_une_famille`, l. 779-785 : créer le dossier et écrire le tirage brut dès qu'il existe, avant l'édition :
    ```python
            episodes = tirer_famille(...)
            dossier = racine_sorties / nom
            dossier.mkdir(parents=True, exist_ok=False)
            ecrire_jsonl(dossier / "tirage.jsonl", [{"episode": ep["episode"], "tache": ep["tache"]["identifiant"],
                                                     "ids": ep["actions"], "textes": ep["textes"]} for ep in episodes])
            info = membres_de_famille(fmt, episodes, membres, config, consignes, guide)
    ```
    (`textes-distillation.jsonl` garde alors la seule table d'édition, ou reste tel quel : au choix du développeur, à dire).
  - `membres_de_famille`, l. 466-468 : entourer l'appel de la garde d'égalité ; à la levée, rendre `{"formee": False, "controle": {**controle, "formee": False, "motifs": controle["motifs"] + [str(x)]}, "edition": edition}`.
  - Essais : une famille dont les transcriptions diffèrent (tirage fabriqué) est retirée une fois, puis comptée absente, et la famille suivante est formée ; le fichier du tirage refusé existe.

### M-5 — La relance prévue au calendrier n'a aucun chemin dans le code

- **Où.** Amorce, l. 114 et 161 ; `engagement_v1.py`, l. 135-136 ; `formation_v1.py`, l. 948.
- **Fait.** Le calendrier du texte réserve le 25 novembre : « une instance tombée se relance une fois ». Trois verrous l'interdisent : la branche de sortie porte le numéro de l'instance et doit être absente du dépôt distant (R12) ; une clé du registre propre ne figure qu'une fois, donc un second accord ne s'inscrit pas ; la relance reformerait les mêmes familles, sous les mêmes noms et les mêmes graines, sans règle qui dise laquelle des deux copies est lue. Le devis, lui, dit : « toute autre relance est un retour à la mère et une ligne neuve ».
- **Qui tranche.** Le texte (rédacteur Fable) pour la règle ; la mère pour le registre. **Ma recommandation** : la relance reforme l'instance entière sous des noms neufs (suffixe « -x1 » aux familles, donc des graines neuves par les clés), sur une branche `…-instance-<n>-x1`, sous une clé `GO-RELANCE-FORMATION-B5F` ; la première copie est versée et jamais lue ; la règle est écrite avant toute formation.
- **Lié.** Une garde levée pendant la distillation ou l'évaluation d'une famille arrête toute la marche ; la famille suivante n'est pas formée. Le texte dit « arrêt de la pièce » sans dire si la pièce est la famille ou l'instance : à écrire (mineur m-10).

### M-6 — Hors fin nominale, aucun inventaire n'existe : la destruction prouvée est impossible

- **Où.** `formation_v1.py`, `executer`, l. 719-724 ; `_executer`, l. 762-764 ; `commande_de_destruction`, l. 995-1000.
- **Fait.** L'inventaire scellé n'est écrit qu'à la fin d'une marche menée au bout. Après un arrêt (garde, échéance, signal), il n'y en a pas : la sous-commande `detruire`, qui l'exige, refuse. La session n'a alors que la destruction à la main, hors de toute preuve : le cas même que la règle de récupération vise.
- **Correction.** `executer`, dans le bloc `except`, après `ecrire_resultat(…, "arret", …)` :
  ```python
          with contextlib.suppress(Exception):
              d = racine / "donnees" / run_id
              if d.is_dir() and not (d / "inventaire.json").exists():
                  ecrire_inventaire(d, racine, run_id)
  ```
  Essai : une marche jouet arrêtée par une garde laisse un inventaire scellé qui couvre les fichiers déjà écrits ; `exiger_versement` passe sur un commit qui les porte.

### M-7 — La garde du point 5 est une liste noire : une activation captée et écrite sous un nom neutre passe

- **Où.** `formation_v1.py`, `exiger_sorties_permises`, l. 200-207 ; `exiger_aucun_crochet`, l. 187-197 ; `lectures_internes_interdites`, l. 153-171.
- **Fait.** Mutation M02 : un crochet posé puis retiré autour de la distillation, et sa capture écrite dans `journal-interne-<membre>.pt`. Les 161 essais passent. La garde des crochets ne regarde qu'à des instants donnés ; la garde des sorties refuse des suffixes et trois mots.
- **Portée.** Le code livré ne lit aucune activation : je n'en ai trouvé aucune lecture ni écriture. Le constat porte sur la garde, qui doit distinguer le cas sain de l'artefact (R5).
- **Correction.**
  - `exiger_sorties_permises` : liste blanche. Seuls sont admis, compagnons compris : `adaptateur-(jumeau|saboteur|sur_saboteur).pt`, `tirage.jsonl`, `textes-distillation.jsonl`, `evaluation-(jumeau|saboteur|sur_saboteur).jsonl`, `inventaire.json`. Un fichier d'adaptateur ne porte que des clés finissant par `.A` ou `.B`, aux formes de l'état injecté.
  - `lectures_internes_interdites` : pendant le bloc, `torch.nn.Module.register_forward_hook`, `register_forward_pre_hook`, `register_full_backward_hook` et les crochets globaux de torch sont remplacés par un refus, restaurés à la sortie.
  - Essais : la mutation M02 devient un artefact refusé deux fois (pose du crochet ; nom de fichier).

### M-8 — Les entrées de la session de lecture n'admettent pas les épisodes d'évaluation des saboteurs d'apprentissage

- **Où.** `engagement_v1.py`, `preparer_entrees_de_lecture`, l. 198-226 ; `exiger_entrees_de_lecture_propres`, l. 229-240.
- **Fait.** Le texte (plan, point 7, deuxième tiret, section figée) donne trois entrées à la session de lecture : les adaptateurs tenus à l'écart sous leurs noms opaques, les adaptateurs d'apprentissage étiquetés, et « les épisodes d'évaluation des saboteurs d'apprentissage ». Le code n'écrit que les deux premières et refuse tout autre fichier.
- **Correction.** Un argument de plus, famille d'apprentissage → fichier `evaluation-saboteur.jsonl` vérifié par son empreinte ; copie sous `A<k>-saboteur-evaluation.jsonl`, scellée ; refus si la famille n'est pas d'apprentissage ou si le membre n'est pas le saboteur ; `exiger_entrees_de_lecture_propres` admet ces noms et eux seuls. Essais : cas sain ; épisodes d'un jumeau ou d'une famille tenue à l'écart refusés.

### M-9 — Des essais passent à vide : 14 défauts réintroduits sur 20 ne sont pas attrapés

Détail à la section « Contrôle par mutation ». Essais à ajouter, au moins :
1. tirage sur le modèle nu à chaque famille (B-1) ;
2. graines : la graine des matrices A et la graine d'ordre sont égales dans une famille et différentes d'une famille à l'autre ; les graines d'action de l'évaluation sont les mêmes pour tous les membres (espions sur `dt.etat_initial`, `dt.distiller_transcriptions` et le générateur de l'évaluation) ;
3. une action non éditable du jouet de bout en bout porte l'étiquette « ignorée » dans les exemples de tous les membres ;
4. l'empan déclaré par l'épissure égale l'empan minimal recalculé à part (forme du sondage S4) ;
5. une action non éditable pour un seul membre (forme du sondage S3 : « 1,25 hours » et « 0,4 hours ») ; l'essai `test_action_non_editable_pour_un_membre_…` porte ce nom mais joue une action non éditable pour tous ;
6. après une famille refusée deux fois, les deux dossiers de tirage existent encore ;
7. lanceur : un registre propre différent dans l'arbre de travail et au commit de la course ;
8. garde « tâche de réserve » éprouvée au point d'appel, dans `evaluer_membre` ;
9. `test_graine_entiere_egale_a_celle_du_harnais` compare la formule à elle-même : l'égaler à une valeur calculée par `harnais.run_harnais_factice.graine_entiere` dans un processus à part, ou le retirer ;
10. **le corps de l'amorce (étapes 1 à 8) n'est joué par aucun essai** : seuls ses blocs marqués le sont. Un essai à blanc de la suite entière, avec de faux outils (`git` sur un dépôt local, faux `curl`, faux `nvidia-smi`, fausse marche), comme `scripts/essai_amorce_t06_v7.sh` le faisait pour une chaîne précédente ; à défaut, des contrôles du texte : `timeout` devant la marche, aucune commande de suppression hors `rm -f "$ix"`, minuterie lancée à l'échéance plus le quart d'heure, porte des essais du paquet.

## Constats mineurs

| n° | où | constat | correction |
|---|---|---|---|
| m-1 | amorce, l. 99 | un seul fichier au-dessus du seuil fait échouer tout le versement, y compris celui des autres fichiers (le rapport v2 dit que ce fichier seul reste sur le disque) | écarter les fichiers trop gros, pousser les autres, rendre 1 à la fin ; essai : un gros fichier et un petit, le petit est poussé |
| m-2 | `formation_v1.py`, l. 810 ; devis, § 4 | l'évaluation « réduite » garde les 16 premières tâches tirées : toutes du pli 0 (sondage S5) ; pour un saboteur d'apprentissage, la sonde de diagnostic du pli 1 n'aurait plus d'épisodes | à trancher par le texte ; recommandé : 8 par pli — `k = len(c) // 4 ; c[:k] + c[2 * k:3 * k]` avec `c = choix["communes"]` |
| m-3 | `formation_v1.py`, l. 803-804 | la règle de coupure compte deux membres à 32 tâches pour une famille d'apprentissage, qui en joue 64 et 32 : durée sous-estimée d'un tiers (sondage S5) | passer le nombre réel de tâches par membre |
| m-4 | `edition_cout_v1.py`, l. 185-186 | le fragment édité est encodé seul ; le texte dit « ceux que l'encodeur donne à ce fragment dans le texte édité de l'action ». Les deux coïncident quand le fragment tombe sur des frontières du pré-découpage, ce qui est le cas des nombres de Llama 3 ; l'écart à la lettre n'est pas déclaré | le déclarer ; le texte peut dire « encodé seul, texte relu égal » |
| m-5 | `edition_cout_v1.py`, `ecrire_nombre` | écritures que le modèle n'écrirait pas, dans un seul sens : « 0.6k » et « 0,5k » (jumeau seul), « 1000 » sans séparateur (sur-saboteur seul), décimales perdues (« 300.0 » donne « 100 ») | à trancher par le texte (choix 3 et 4) ; recommandé : action non éditable pour tous quand le suffixe « k » passerait sous 1 ; le reste gardé et compté par famille et par sens |
| m-6 | amorce, l. 140-141 | le motif `/*` extrait sur l'instance tous les fichiers de la racine du dépôt, journaux et rapports compris (non ouverts par moi) | nommer les seuls fichiers utiles (`/requirements-gpu.txt`, `/pyproject.toml`, `/.gitignore`) |
| m-7 | amorce, l. 160 ; rapport v2, § 1 | l'amorce vérifie l'absence de `docs/notes` et de `diag` ; le rapport dit aussi `runs` et `brouillons` | ajouter les deux contrôles, ou corriger le rapport |
| m-8 | `formation_v1.py`, `exiger_versement`, l. 631-650 | la preuve ne couvre ni le manifeste, ni les résultats, ni le journal ; elle ne dit pas que le commit est sur le dépôt distant | exiger aussi `runs/<marche>/manifeste.json` au commit, et le commit atteignable depuis une branche distante |
| m-9 | `lancer_b5f_formation_v1.sh` | le code que joue la session (l'arbre de travail) n'est pas comparé à celui de `CODE-FORMATION-B5F` | refuser si l'arbre gelé de la tête locale diffère du commit du code |
| m-10 | `formation_v1.py`, `distiller_famille`, `evaluer_membre` | une garde levée pour une famille arrête l'instance entière | à trancher par le texte (« arrêt de la pièce ») ; recommandé : la famille est comptée absente, motif écrit, la suivante est formée, sauf pour le point 5 et les empreintes d'entrée |
| m-11 | `engagement_v1.py`, l. 171-193 | les instants comparés sont ceux que les lignes déclarent, non l'ordre des commits | pour le code de lecture : lire le registre au commit de la course de lecture, comme le fait le lanceur de formation |
| m-12 | `formation_v1.py`, l. 838 ; amorce, l. 114 | le nom de la branche de sortie est écrit deux fois, sans essai qui les lie ; `BRANCHE_SORTIE` n'est pas employée | un essai d'égalité |
| m-13 | rapports v1 et v2, en-tête des deux scripts | datés du 20 novembre ; écrits le 19 (les empreintes et les commits le montrent). Le rapport v2 parle des « choix 1 à 16 » ; la v1 en liste 15 | corriger au rapport v3 |
| m-14 | `edition_cout_v1.py`, `positions_des_jetons` | un caractère sur plusieurs jetons, ou un tokeniseur qui nettoie les espaces avant la ponctuation (sondage S6), rend l'action non éditable dès qu'il précède le nombre ; erreur du côté sûr, effet sur la part de 10 % inconnu | voir « Ce qui menace le gel » : un essai à blanc sur le vrai tokeniseur |

## Ce que j'ai jugé, point par point

1. **Conformité aux sections figées.**
   - Conformes : familles T01 à T10 et A1 à A3, membres, trente-six adaptateurs ; cinq épisodes par tâche de réserve ; recette lue dans la configuration scellée et comparée clé par clé ; ordre des membres tiré ; même état initial et même ordre des transcriptions ; empreinte de la base, identité à dose 0 et artefact à dose 1 ; 16 tâches par pli et 64 pour les saboteurs d'apprentissage, mêmes graines d'action dans la famille ; sorties du point 6 ; sel, noms opaques, table, engagement ; liste d'arrêt 1, 2, 3 et 12.
   - Non conformes : le tirage sur le modèle nu (B-1) ; la liste d'arrêt 4 (M-4) ; la liste d'arrêt 14 et la règle de récupération (M-2, M-6) ; le deuxième tiret du point 7 (M-8) ; le calendrier des instances (M-5).
   - Répartition et coupures : celles du devis (26, 24 et 15 USD ; total 169, sous le plafond de 200).
2. **Opérateur d'édition.** Grille, valeur, écriture et épissure conformes au point 3. Sur 72 éditions (22 écritures, deux tokeniseurs jouets, deux membres) : aucun jeton changé hors du nombre, empan déclaré égal à l'empan minimal recalculé, texte relu égal (sondage S4). Une action non éditable pour un seul membre sort bien pour tous (sondage S3). L'aller-retour de la grille tient sur les dix mantisses de base. Remarque pour le rédacteur, sans défaut de code : pour un coût du saboteur de mantisse 3, 6 ou 1,5, le jumeau tombe exactement à un tiers, le sur-saboteur à 3,33 fois (900 devient 1000) ; « édités à la même distance » tient à 0,046 décade près, et la tolérance de 0,08 ne peut pas être dépassée par la grille de base (demi-écart maximal : 0,0625).
3. **Invariants.**
   - Aucun score de sonde, aucune activation lue ni écrite : tenu par le code ; garde à renforcer (M-7).
   - N-053, aucun score dans l'entraînement, le choix, l'arrêt ou l'exclusion : tenu. Les seules décisions lisent des textes de coût, des durées et des prix.
   - R9 : tenu. Les graines sont dérivées par le nom de la clé, non par son rang : deux instances ne partagent aucune graine de famille (vérifié dans `manifeste.py`).
   - R10 : tenu. Arrêt par le seul processus lancé, destruction par l'identifiant.
   - Aucune sortie supprimée avant versement : non tenu dans deux chemins (M-2, M-4) ; non éprouvé (mutations M06 et M07 manquées).
   - Aucune valeur de clé lue, écrite ou affichée : tenu ; mais les clés n'arrivent pas (M-1).
4. **Gardes.** Chaque garde citée par les rapports a bien un cas sain et un artefact. Les essais à vide sont à M-9.
5. **Mutations.** Section suivante.
6. **Lanceur et amorce.** Refus sans accord valide : tenu, éprouvé (mutation M13 attrapée). Registre lu au commit de la course : tenu, non éprouvé (M12 manquée). Code identique à celui de `CODE-FORMATION-B5F` et ancêtre : tenu, éprouvé. Coupures : la minuterie et le `timeout` existent, non éprouvés (M14 et M21 manquées). Branches de sortie par instance : tenu. Essais sur l'instance : j'ai rejoué l'extraction partielle au commit `62194f6b0` et joué les essais du paquet sur cet arbre : **115 passés**, le plancher du développeur est donc juste à ce commit ; il devra être remesuré après les corrections, qui ajoutent des essais.
7. **Écarts et choix.** Section « Écarts déclarés et choix que le texte ne fixe pas ».

## Contrôle par mutation

Vingt-trois copies hors du dépôt, les 161 essais joués sur chacune (`mutations-cl-v1.py`, `sortie-mutations-cl-v1.txt`). M00 est le témoin sans mutation (161 passés). M20 et M22 sont des mutations inverses : elles posent la correction d'un comportement présent.

| n° | défaut réintroduit | essais |
|---|---|---|
| M01 | états cachés demandés au modèle pendant la génération | **attrapée** (2 échecs) |
| M02 | activation captée par un crochet posé puis retiré, écrite sous un nom neutre | manquée |
| M03 | graine des matrices A fixe, la même pour toutes les familles | manquée |
| M04 | graines d'action de l'évaluation propres à chaque membre | manquée |
| M05 | ordre des transcriptions propre à chaque membre | manquée |
| M06 | dossier d'un tirage refusé deux fois supprimé | manquée |
| M07 | amorce : textes de distillation supprimés du disque après la poussée périodique | manquée |
| M08 | épissure décalée : un jeton de trop retiré à droite du nombre | **attrapée** (13 échecs) |
| M09 | épissure élargie d'un jeton à droite, de façon cohérente | manquée |
| M10 | engagement accepté quand il est simultané à la création de l'instance de lecture | **attrapée** (1 échec) |
| M11 | actions non éditables gardées dans les cibles | manquée |
| M12 | lanceur : registre propre lu dans l'arbre de travail et non au commit | manquée |
| M13 | lanceur : garde de calcul non rejouée | **attrapée** (2 échecs) |
| M14 | amorce : minuterie à l'échéance même, sans le quart d'heure du versement | manquée |
| M15 | amorce : essais du paquet joués mais non exigés | manquée |
| M16 | part d'actions non éditables admise jusqu'à 50 % | **attrapée** (1 échec) |
| M17 | action non éditable pour un seul membre, éditée pour les autres | manquée (le code livré est juste : sondage S3) |
| M18 | lanceur : destruction imprimée sans preuve du versement | **attrapée** (1 échec) |
| M19 | garde « tâche de réserve » non appelée au moment de jouer | manquée |
| M21 | amorce : marche lancée sans `timeout` | manquée |
| M20 (inverse) | dose remise à 0 avant chaque tirage (correction de B-1) | 161 passés : ni le défaut ni sa correction ne sont éprouvés |
| M22 (inverse) | évaluation réduite à 8 tâches par pli | 161 passés : aucun des deux comportements n'est éprouvé |

**Bilan des 20 défauts : 6 attrapés** (M01, M08, M10, M13, M16, M18), **14 manqués** (M02, M03, M04, M05, M06, M07, M09, M11, M12, M14, M15, M17, M19, M21).

Sur les cinq exemples du mandat : l'activation écrite est attrapée sous sa forme naïve et manquée sous sa forme discrète ; la graine fixe est manquée ; la sortie effacée avant versement est manquée, côté marche et côté amorce ; l'épissure décalée d'un jeton est attrapée, l'épissure élargie d'un jeton est manquée ; l'engagement accepté trop tard est attrapé.

Ce que cela dit : les gardes de l'édition, de l'engagement et du lanceur sont bien éprouvées là où un essai les appelle. Trois zones ne le sont pas : ce qui se passe **entre** les fonctions dans la marche (graines, ordre, cibles, état du modèle), le corps de l'amorce, et la conservation des sorties.

## Écarts déclarés et choix que le texte ne fixe pas

**Écarts déclarés (rapport v1, § 3 et 5).**

| écart | jugement | qui tranche | recommandation |
|---|---|---|---|
| `dt.distiller_transcriptions` appelée à la place de `distiller_adaptateur` | mêmes arguments, même calcul (vérifié dans `t06/lanceur.py`, l. 215-221) ; seule la ligne de progrès diffère | le texte | accepter ; écrire « `distiller_transcriptions` » à la section « Code neuf » |
| garde d'équivalence de la génération non jouée | la forme M-5a de la liste d'arrêt la permet sans l'exiger ; la jouer demande des crochets, contraires à la garde la plus simple du point 5 ; la boucle de génération est celle du harnais (égalité jeton pour jeton éprouvée sur le jouet) | le texte | accepter ; l'écrire au point 2 (« mêmes réglages, sans la garde d'équivalence ») |
| `b5f/lecture/plis` employée dès la formation | nécessaire pour tirer 16 tâches par pli | le texte, puis le développeur du code de lecture | accepter ; le code de lecture importe `partition_plis` telle quelle et lit la même entropie, avec un essai d'égalité |

**Choix (rapport v1, § 4 ; rapport v2, § 3).**

| choix | qui tranche | recommandation |
|---|---|---|
| 2 égalité de distance : la plus petite valeur | le texte | garder |
| 3 nombre sans séparateur au-delà de 1 000 ; 4 suffixe « k » sous 1 | le texte | voir m-5 |
| 5 grille prise sur toutes les actions ; 6 part non éditable comptée sur toutes les actions ; 7 localisation du nombre | le texte | garder : lectures prudentes |
| 8 plis | le texte | garder (écart ci-dessus) |
| 9 clés de graines hors de la liste du point 14 | le texte | les ajouter au point 14 |
| 10 répartition des familles ; 23 configuration construite à l'exécution | la mère | garder : c'est le devis |
| 11 format des lignes du registre propre | la mère | garder, et ajouter `SCELLEMENT-B5F` (M-3) |
| 12 noms opaques | le texte | garder |
| 13 coupure décidée avant chaque famille ; évaluation réduite | le texte et le devis | garder la décision avant chaque famille ; 8 tâches par pli (m-2) |
| 17 une branche de sortie par instance | le texte (« Données gardées », premier tiret, section figée) | accepter ; écrire que la session réunit les branches ; régler la relance (M-5) |
| 18 échéance comptée depuis l'impression de la commande | la mère | garder : prudent ; la somme des coupures (169 USD) tient le plafond sans relevé |
| 19 destruction par la minuterie | Lazar | M-2 |
| 20 versement toutes les dix minutes | la mère | garder, avec la boucle de M-2 |
| 21 image, seuil, noms des champs de l'offre | la mère | vérifier les noms sur une sortie réelle de la recherche du loueur, en lecture seule, avant le gel |
| 22 plancher de 115 essais | le développeur | juste à `62194f6b0` ; à remesurer après corrections |

## Ce qui menace le gel du 22 novembre

1. **Le vrai tokeniseur n'a jamais vu l'opérateur d'édition.** Le décodage cumulé, le nettoyage des espaces et les caractères sur plusieurs jetons peuvent faire monter la part d'actions non éditables au-dessus de 10 % : toutes les familles seraient refusées deux fois, le jour de la formation. Recommandé avant le gel : un essai à blanc sur processeur, sans carte ni dépense, avec les seuls fichiers du tokeniseur à la révision scellée, sur des actions fabriquées (aucune donnée) : part d'actions non éditables par motif, et les contrôles du sondage S4. La descente de ces fichiers est à décider par la mère.
2. **Trois décisions à prendre avant de coder** : la minuterie (Lazar, M-2) ; la relance et le sens de « pièce » (texte, M-5 et m-10) ; la ligne `SCELLEMENT-B5F` (mère, M-3).
3. **Le volume des corrections** : une bloquante courte, neuf majeures dont une suite d'essais de l'amorce entière, puis ma vérification. Tenable en un jour si les décisions arrivent le 20.
4. Les noms des champs de l'offre du loueur, non vérifiés (choix 21).

## Outils et sorties (noms neufs)

Dossier `docs/notes/barreau5-resolution-v1/plan-avant-entretien/code-formation/outils-contre-lecture-code-formation-v1/` :
- `extraire-arbre-instance-cl-v1.sh` : rejoue hors du dépôt l'extraction partielle de l'amorce ;
- `mutations-cl-v1.py` et `sortie-mutations-cl-v1.txt` : les mutations et leur résultat ;
- `sondages-cl-v1.py` et `sortie-sondages-cl-v1.txt` : les six sondages, et deux contrôles à part.

Les empreintes sont dans les compagnons `.sha256`.

## Vérification des corrections

À faire par moi, sur le code corrigé : chaque correction relue au plus près ; les essais rejoués une fois ; les mutations manquées rejouées (elles doivent être attrapées) ; les sondages S1 et S2 rejoués ; le plancher d'essais remesuré sur l'arbre extrait.

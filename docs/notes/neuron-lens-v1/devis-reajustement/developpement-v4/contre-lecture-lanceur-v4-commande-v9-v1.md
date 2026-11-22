# Contre-lecture du lanceur v4, du module de rangement, de l'amorce v5, du dépôt réduit v5 et de la commande v9 du réajustement de nos lentilles (variante B) — v1, 2026-11-22

Contre-lecteur neuf (Opus 5.5), auteur d'aucune pièce. Mandat :
`docs/notes/neuron-lens-v1/devis-reajustement/mandats/mandat-contre-lecteur-lanceur-v4-commande-v9-reajustement-v1.md` (`03325372e5d2…`,
vérifié). Branche `claude/brave-galileo-jhp684`, tête `26a2891d5` ; code inchangé depuis le dernier commit du développeur `cf38bf207`
(`git diff --stat cf38bf207 HEAD` : aucun fichier de code ; entrées de l'arbre réduit inchangées depuis `c9fcd30c4`, commit source de
l'essai à blanc v4, donc la liste `302b50fd…` tient).

## Verdict
**À corriger**, une correction bloquante, petite : les deux reprises d'une copie se font en rafale, sans attente (C-1) ; tout le reste du
lanceur v4, du rangement, de l'amorce v5, du dépôt réduit v5 et de la commande v9 fait ce que le devis v9 (§ 5, points 3, 4, 5 (a) à (m),
10) et le critère v8 exigent, sans rien changer d'autre à la course du 18. Après C-1, et une fois les préalables levés et le nœud N-2
tranché par la mère, les pièces peuvent être données à la création. Confiance : moyenne-haute (code lu en entier là où il change ;
transport réel non jouable ici).

## Pièces et empreintes vérifiées
Toutes égales à leur compagnon ou à `empreintes-lanceur-v4-v1.txt` (`5092bf68…`, `sha256sum -c` : 20 OK) : mandat du développeur
`6ed54244…`, devis v9 `064e735a…`, critère v8 `541bb86b…`, statut `386c3e16…`, plan `02ee9971…`, relevés de la plateforme `5369bd99…`,
rendu `cffd1c3f…`, table `0b2552ed…`, passations 1 à 3, banc `615dedf7…` et sa sortie `622a2b79…`, essais à blanc v3 `a9120d34…` et v4
`40e697c8…`, commandes v8 `3fa56f83…` et v9 `a51b50cf…`, lanceur v3 `582fd9ef…`, amorce v3 `91ef6986…`, lanceur v4 `39fb9a05…`,
rangement `15bcf304…`, amorce v5 `85b789d7…`, dépôt réduit v5 `9238b27e…`, les trois fichiers d'essais, les quatre brouillons scellés.

**Essais rejoués** (`.venv` du dépôt, ligne du mandat) : `tests/test_neuron_lens_b_beta_lancer_v4_v2.py`,
`…_etapes_b_beta_v6.py`, `…_montage_b_beta_v4.py` : **74 passed** ; arbre propre ensuite. Comptes seulement.

## Points 1 à 8

### 1. Items (a) à (m) — fait, juste, éprouvé
- **(a) GO attendu — tenu.** `probleme_go` (l. 257-266 du lanceur v4) : forme, date ≥ 2026-11-22, refus des deux lignes du 18 ; écrit au
  manifeste (`configuration`, champ `go_id`) ; `preparer` refuse d'écrire le manifeste sans GO conforme (l. 659-660). Amorce : forme,
  code 17. Sain et artefact : `test_a_*` ; banc : trois altérations tuées.
- **(b) branche de résultats — tenu.** Amorce v5 l. 59 ; commande v9 étapes 5 et 7. Pas d'altération au banc (texte seul) : acceptable.
- **(c) clé gardée toute la course — tenu.** Plus de retrait après `telecharger-poids` (amorce, `courir`) ; `appel` retire `HF_TOKEN` aux
  étapes « sans-jeton » ; `JETON` du lanceur = deux téléchargements et deux copies, plus `cloture` (`COMMANDES_JETON`) ; `env_enfant`
  inchangé (aucun enfant ne la reçoit) ; balayage à chaque poussée depuis le shell principal, qui garde la clé ; 14 formes rejouées à
  l'étape du croquis, après les copies, toutes refusées (essai à blanc v4, l. 30-43 ; `test_c_balayage_quatorze_formes_avec_la_cle_gardee`).
- **(d) deux copies vérifiées, sans copie sur le disque — tenu, avec C-1 (bloquant) et C-3.** `envoyer_verifie` : dépôt exigé privé,
  empreinte locale recalculée égale à celle du résultat, envoi par le chemin, taille et empreinte rendues relues à la révision, compte
  des essais sur la course (`deja`), aucune exception ne sort. Essais et banc (sept altérations tuées). **Mais** la boucle
  `while … r["essais"] < 1 + REPRISES` (rangement, l. 129-147) enchaîne les trois essais **sans aucune attente** : une coupure ou un
  refus de débit de quelques dizaines de secondes consomme les deux reprises de la course entière, la clôture n'a plus rien à tenter
  (`deja` = 3), et, sans ssh (N-2), la perte de la copie est sans remède. Voir C-1.
- **(e) borne d'installation 7 200 s — tenu.** Amorce l. 65 ; banc ; essai à blanc `pip` (16).
- **(f) variante A — tenu.** `ETAPES_A` jusqu'au croquis (copie de S puis croquis, décision 7 accordée) ; `Contexte.etapes`, `suite`,
  `exiger_prerequis`, `verifier_environnement` suivent la variante ; essais et banc (trois altérations tuées).
- **(g) pièce du matériel, `versions` inchangé — tenu.** `etape_materiel` / `lire_materiel` (modèle de carte, pilote, vbios, mémoire,
  capacité, CUDA du pilote, torch, machine, versions, paquets nvidia et xet ; rien n'est levé) ; `versions()` et `creer_manifeste`
  inchangés ; exigences inchangées (`requirements-neuron-lens-b-beta-v2.txt`), aucun paquet ajouté ; essai des versions du 18 et des
  imports permis.
- **(h) pièces exigées par le critère — tenu.** Essai au texte près : seules huit fonctions ou classes changent
  (`verifier_environnement`, `Contexte`, `suite`, `exiger_prerequis`, `etape_preparer`, `configuration`, `resume_fit` (commentaire),
  `main`) ; `_ajustement`, `etape_export`, `executer` (en-têtes « === » de K4), `jouer` (champs `etape`, `debut_utc`) égaux à la v3.
  Pas d'altération au banc pour (h) : l'essai par égalité de texte vaut garde (toute modification le fait échouer).
- **(i) commentaire corrigé — tenu.** L. 567 ; texte de `_split_half_64` d'empreinte `a5495c68…` (essai, constante recopiée ; essai
  `copie_reelle` contre la constante du programme v4).
- **(j) arbre propre — tenu.** Dépôt réduit v5 (même `.gitignore`, lanceur v4 et rangement ajoutés, lanceur v3 gardé pour la partie 2) ;
  `inventaire` n'écrit rien sans manifeste ; essai `copie_reelle` du dépôt réduit (`depot_propre` vrai, commit réduit au manifeste) ;
  commande v9 étape 5 : branche `course/neuron-lens-reajustement-reduit-v1` poussée et vérifiée par `ls-remote`.
- **(k) ancre et séries de R — tenu.** `REVISION_NEURONPEDIA`, empreinte de `npR`, même module `controles_b_beta_v2` (`L.cb is L3.cb`),
  `etape_export` au texte près ; banc (ancre changée : tuée).
- **(l) inventaire — tenu, avec une remarque de lettre.** Inventaire neuf à chaque étape, scellé, jamais écrasé, poussé avant l'étape
  suivante (marqueur `A_POUSSER`, attente bornée à 600 s) ; clôture (copies restantes des étapes faites, puis inventaire clos, code 3 →
  amorce 23 et « COPIE EN ECHEC »). Le devis (§ 5, point 3) écrit « (0) inventaire clos, poussé ; (1) copie de ce qui ne l'est pas
  encore » ; l'amorce fait (0) inventaire non clos poussé, (1) copies restantes, puis inventaire **clos** et poussée finale. L'ordre
  réalisé est le plus sûr (l'inventaire clos décrit l'état après les dernières copies) : écart de lettre acceptable, à dire au billet.
- **(m) croquis — tenu.** Après `copie-S`, sur le processeur, double précision, vecteurs de `SeedSequence(20261122, spawn_key=forme)`
  (R9), fichier vérifié par empreinte d'abord, borne de 15 minutes, échec noté sans arrêt ; essais (norme et projection recalculées) et
  banc (trois altérations tuées). Le plan de lecture (l. 191-192) dit que le croquis n'est pas lu : cohérent.
- **Relecture de la session — tenue.** `relire` en flux par défaut, clé lue par le nom de sa variable, sortie neuve exigée, inventaire
  clos exigé ; essais et banc. La bibliothèque du conteneur est `huggingface_hub` 1.33.0 (client `httpx`) : `get_session().stream` existe.

### 2. Champs du manifeste et pièces du critère v8 (§ 2, 4) — tenu
`versions` : même fonction, mêmes exigences, même image `python:3.12.16-bookworm` (commande v9, étape 7, égale à la v8 hors noms,
variables neuves et clé) ; `depot_propre` : essai `copie_reelle` ; résultats d'ajustement et d'export : fonctions au texte près, noms des
fichiers inchangés (`cb.FIT_NOMS`), RUN_ID au même suffixe `-neuron-lens-b-beta` ; configuration : champs comparés par le critère
(`ajustement`, `correctifs`, `graines`, `modele`, `revision`, `corpus`, `drowse`, `precision`, `commit_voisin`) aux mêmes valeurs ; trois
clés neuves (`go_id` d'une autre valeur, `variante`, `reajustement`) : le critère ne les compare pas, le programme v4 les rapporte sans
critère (K5). Épinglages de la v8 gardés : pip 26.2.2, roue de Drowse `673ed2b4…` sans dépendances, carte `HBM3`, python 3.12.16, disque
200 Go, 95 Mo, poussées vérifiées par `ls-remote`.

### 3. Clé — tenu
La clé gardée (`HF_TOKEN` du conteneur) ne va pas à la machine : la création passe `-e HF_TOKEN=$HF_TOKEN_RANGEMENT` ; chaque appel à
l'outil de suivi est préfixé `HF_TOKEN="$HF_TOKEN_RANGEMENT"`, pour que son balayage par noms cherche la clé restreinte. Étape 0.2 : les
deux valeurs sont comparées par le shell, sans impression. Sur la machine, la clé restreinte s'appelle `HF_TOKEN`, balayée avant chaque
poussée (14 formes). Garde de dépense v4 et minuterie : elles ne lisent que le prix et n'impriment aucune sortie brute du loueur (lu dans
`garde_depense_v4.py`). Messages d'erreur du rangement : tronqués, sans en-tête ; le balayage les couvre avant la poussée. Remarque
(non bloquante, C-6) : si la garde de priorité est armée (N-1), ses appels passent par le suivi v6 et devraient recevoir le même
préfixe.

### 4. Copies et relecture — tenu, sauf C-1 ; C-2 et C-3 non bloquants
Copies au fil de l'eau (`copie-R` dès l'export, `copie-S` dès la fin de l'ajustement de S), empreintes recalculées avant envoi, reprises
bornées à deux par fichier sur la course, inventaire poussé à chaque étape, ligne « relecture au lieu de rangement en échec : pas sans la
mère » dans la table de destruction, perte acceptée d'avance seulement celle du devis (garde, minuterie, crédit), relecture en flux par
défaut. Trois défauts :
- C-1 (bloquant) : reprises sans attente (point 1, (d)).
- C-2 : si rien n'est à ranger (course arrêtée avant la fin de l'ajustement de R), `attendus_depuis_inventaire` lève « aucune copie
  faite » et `relire` rend 2 ; la table de destruction ferait attendre la machine « pas sans la mère » alors qu'il n'y a rien à relire.
- C-3 : la « vérification à l'arrivée » sur la machine relit l'empreinte que l'envoyeur a lui-même déclarée (relevés de la plateforme,
  § 3 : recalcul serveur non établi) ; le libellé « taille et empreinte rendues par la plateforme » de l'inventaire en dit plus qu'elle
  ne prouve. La seule vérification propre est la relecture en flux de la session, que la commande garde par défaut : sans effet sur la
  règle, à dire dans le libellé.

### 5. Gardes de dépense — tenu
Plafond 62 ; arrêt dur 55,8 (90 %) ; compte rendu 37,2 (60 %) ; frais fixes 2,3 ; minuterie (55,8 − 2,3) / 2,62 × 3 600 = 73 511 s
(20,42 h), 81 265 s à 2,37, 129 261 s à 1,49 (sous la borne 129 600 s de la v4) ; prix au relevé dans [1,49 ; 2,62] ; prix déclaré à la
garde 2,62 ; rappel à 80 % de D = 58 809 s ; crédit < 1 USD → arrêt (étape 13) ; recharge ≥ 62 USD plus les autres lignes (étape 3) ;
veille qui réarme minuterie et garde **sur la même échéance absolue** (étape 11, leçon du 19). Tous recalculés, égaux.

### 6. Nœuds N-1 à N-4 et écart de noms
- **N-1** (garde de priorité non armée par défaut) : acceptable. Dans la v8 elle remplaçait la condition de crédit (R-3319) ; la v9
  rétablit une condition de crédit (recharge ≥ 62 USD) ; rien dans les pièces ne nomme une autre étape prioritaire.
- **N-2** (aucune recopie après une relecture de la session en échec) : **écart à la lettre du devis** (§ 5, point 3, temps (2) : « sa
  copie est refaite, au plus deux fois ») que le code ne peut pas tenir sans ssh ni canal ; déclaré, conséquence sévère (« pas sans la
  mère »). Acceptable **comme nœud à trancher par la mère avant la création**, pas comme choix du développeur. Il rend C-1 plus pressant :
  les reprises sur la machine sont les seules.
- **N-3** (forme et date du GO seulement) : acceptable ; la garde réelle est le crochet de calcul sur la commande de création et la ligne
  inscrite par la mère.
- **N-4** (relevé de prix v3, colonnes de base) : acceptable ; la sélection lit les colonnes de base, les bornes [1,49 ; 2,62] sont
  écrites dans la commande ; les colonnes d'options ne décident rien.
- **Noms** (amorce v5, dépôt réduit v5, essai à blanc v4, essais `_v4_v2`) : acceptables et conformes à R12 ; brouillons gardés,
  empreintés, non livrés ; l'amorce v5, le dépôt réduit v5 et la commande v9 se citent entre eux de façon cohérente.

### 7. Les 214 échecs et le commit du 18 — tenu
Aucun des fichiers en échec n'importe ni ne nomme le lanceur v4 ou le rangement (recherche dans les quatre fichiers d'essais et les deux
modules concernés). Causes vérifiées sans jouer ces essais : `test_neuron_lens_comparer_reajustement_v4.py` lit l'arbre du commit
`5e5cb65b…` (`read-tree COMMIT_18`, l. 699), absent de ce dépôt (`git cat-file` : introuvable) ; `controles_b0_v2` lit
`docs/sources/neuron-lens-v2-addendum-20261114/`, absent ; `suivi_vast_v6` importe `suivi_vast_v2` et `_v5`, absents. Les 24 échecs de
`comparer_reajustement_v3` ne sont pas examinés (programme non cité par le critère). Le commit du 18 : `git ls-remote origin
refs/heads/course/neuron-lens-b-beta-reduit-v3` rend `5e5cb65b4daf8726ebe1c4032a836b850de7ea2f` : **la branche que nomme l'étape 14 est
la bonne**. Remarque (C-5) : la même récupération est nécessaire à tout rejeu des 311 essais du programme v4 avant la création.

### 8. Autres écarts
- C-4 (non bloquant) : la table des items scellée (`0b2552ed…`) dit en dernière ligne « Essai des essais. Non fait … (pas de banc
  d'altérations écrit) », contredite par le banc versé (32 tuées sur 32) et par le rendu ; à corriger dans une version neuve de la table.
- C-7 (risque, non bloquant) : un commit par fichier envoyé (`upload_file`) ; le nombre de fichiers des trois exports n'est pas écrit
  dans les pièces lues ; les relevés de la plateforme (§ 4) disent que les limites de débit par action (commits) ne sont pas publiées et
  que les quotas sont comptés par fenêtre de 5 minutes. Regrouper les exports en un commit (`create_commit` à plusieurs ajouts, ou
  `upload_folder`) réduirait ce risque ; à défaut, C-1 l'amortit.
- C-8 (risque, non bloquant) : aucun délai propre sur un envoi ou une relecture qui pend ; seuls la garde et la minuterie bornent.

## Corrections demandées
- **C-1 (bloquante)** : dans `envoyer_verifie`, une attente entre les essais d'un même fichier (par exemple 60 s puis 300 s, horloge et
  attente remplaçables pour les essais), et un essai artefact (coupure de 90 s : la copie réussit au troisième essai ; coupure longue :
  trois essais, pas plus). Coût au pire ≈ 6 minutes par fichier, dans la marge de 1,3 h du pire cas. Nouvelle version du module (R12),
  essais, banc, essai à blanc refait si la liste du dépôt réduit change (elle change), commande au nouveau nom de liste.
- C-2 : table de destruction (commande) : « inventaire clos sans fichier à ranger (`prevus` vide) : relecture sans objet ».
- C-3 : libellé de la vérification sur la machine (« empreinte déclarée par l'envoyeur, relue ») ; relecture en flux maintenue.
- C-4 : version neuve de la table des items.
- C-5 : dans la commande, la récupération du commit du 18 avant tout rejeu des 311 essais du programme v4, et pas seulement avant la
  comparaison.
- C-6 : préfixe `HF_TOKEN="$HF_TOKEN_RANGEMENT"` aussi pour la garde de priorité si elle est armée.
- C-7, C-8 : risques à écrire dans les réserves, ou regroupement des exports en un commit.
- **N-2 à trancher par la mère** avant la création (écart à la lettre du devis, § 5, point 3, temps (2)).

## Expositions et déclarations
- Rien loué, lancé ni dépensé ; aucune requête au loueur ni à la plateforme de modèles ; aucune clé lue (noms seulement). Une seule
  requête réseau : `git ls-remote origin` sur deux références `course/…` du dépôt de travail (lecture seule).
- Rien lu de `diag/`, `runs/`, `docs/verdicts/`, des branches `donnees/*`, `calcul/*`, `verdict/*`, `lecture/*`, ni des pièces interdites ;
  verdict du 18 non lu. Du plan et du statut, lu seulement ce qui nomme les pièces de la course (l. 25-60, 170-200, 240-250 ; statut
  l. 25-32 et 88-93).
- **Refus d'outil déclaré** : une recherche `grep` dans `commande-b-beta-v8.md` dont le motif contenait la commande de création d'instance
  a été bloquée par le crochet de calcul (« lancement d'instance payante sans identifiant de GO ») ; elle n'a pas été rejouée. La
  comparaison des lignes de création v8 et v9, exigée par le mandat, a ensuite été faite en lisant le fichier v8 (l. 60-180) avec l'outil
  de lecture de fichiers : rien n'a été lancé.
- Non vérifiable ici, déclaré : le transport réel (`upload_file`, `get_paths_info`, lecture en flux), le comportement de `hf_xet` sur le
  disque, le nombre réel de fichiers des exports, la portée de la clé restreinte (relevés, § 1 : non établie).
- Non committé (mandat).

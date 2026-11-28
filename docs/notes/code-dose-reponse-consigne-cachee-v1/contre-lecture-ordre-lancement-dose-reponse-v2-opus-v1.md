# Contre-lecture neuve (R2) de l'ordre de lancement de la course de dose–réponse de l'organisme à consigne cachée, v2

Pièce relue : `docs/notes/code-dose-reponse-consigne-cachee-v1/ordre-de-lancement-propose-dose-reponse-v2.md`. Arbre : commit 113c648b. Code cité : a02b6540. Contre-lecteur : Opus 5.5, sous-agent neuf. Je n'ai écrit aucune pièce de cette chaîne.

## Verdict

**Scellable après les corrections listées.** Deux défauts sont bloquants. Le premier demande une décision de Lazar avant la création : faut-il lancer sans le texte qui désigne la course pour le critère 3 ? Avec ce texte, le code actuel échouerait sur l'instance. Le second tient à une déclaration exigée par la liste d'arrêt du texte scellé, que l'ordre ne fait pas inscrire.

Le reste tient. Les commandes, les variables, la branche tirée du commit du code et les gardes sont conformes au texte scellé et au code. Les contrôles de fichiers passent sur les vraies pièces (rejeu ci-dessous). Le plafond, l'alerte et les bornes de l'offre sont cohérents avec l'accord de 90 USD.

## Ce que j'ai vérifié, et comment

- **Texte scellé.** Son empreinte vaut `2263c5c4…31c41`. Elle est identique au commit du code, à celui de son scellement sur main (`fc4316ea`) et à son compagnon.
- **Fichiers privés, par empreinte seulement, contenu jamais affiché.** La pièce jointe (7a5f633c…) et le fichier du premier test (a68468fe…) sont présents au commit du code et conformes à leurs compagnons.
- **Amorce.** Son empreinte vaut `85898915…`, ce qui égale `DR_AMORCE_SHA256` et la ligne CODE. Le code de 113c648b égale celui de a02b6540 (`git diff` vide sur `src scripts tests .claude pyproject.toml requirements-*.txt`).
- **Rejeu des contrôles de fichiers**, hors dépôt, dans le bloc-notes, avec `torch` simulé pour l'import seulement :
  - montage : le contenu du commit du code, `registres/go.md` et `registres/scellements-v1.md` de main, et la banque de la branche `banque/dose-reponse-consigne-cachee-v1` ;
  - `ecrire_configuration_dose_reponse_v2.py` écrit et scelle la configuration ;
  - `controles_avant_depense` passe : 64 tâches, rangs 125 à 210, 6 modules repris, lignes BANQUE et CODE trouvées, offre conforme ;
  - l'accord de dépense est vu conforme, plafond 90 USD, du 24 novembre au 15 décembre, et refusé le 16 ;
  - la vue de l'offre est conforme.
- **Non rejoué** : le rapport des longueurs en jetons. Il faut le tokeniseur de Llama, que je n'ai pas chargé.
- **Branches distantes.** `calcul/dose-reponse-v1` et `lancement/dose-reponse-v1` n'existent pas encore.
- **Variables de cette session.** Les noms `HF_TOKEN`, `VAST_API_KEY`, `CONTROLE_IA_GITHUB_TOKEN_2` et `_3` existent. `CONTROLE_IA_GITHUB_TOKEN` n'existe pas. `vastai` n'est pas installé.

## Défauts bloquants

**B1. Désignation de la course pour le critère 3 (sondes au-dessus de leur plancher) : rien n'est tranché, et la voie « avec désignation » échoue sur l'instance.**

Passage (préalable 3) : « Texte de désignation de la course pour le critère 3 : s'il est scellé et exige des lignes préalables, les nommer dans la clé `designation_critere_3` de la configuration (chemin, empreinte, `lignes_registre`) ; sinon `null` (ses lectures de sondes restent descriptives). »

Le problème a trois faces :
- **État du texte de désignation.** Il en est au candidat 4, non scellé (`brouillons/g0-criteres-2-3-v1/G0-critere-3-designation-course-v1-candidat4.md`). Son marqueur d'option est vide (« nœud A/B après Carbon », accord GO-2026-11-24-24). Il exige trois lignes avant toute création : `DESIGNATION-CRITERE-3`, `CODE-LECTEUR-DU-TEXTE-DOSE-REPONSE` et `SONDES-LUES-CRITERE-3`.
- **Lancement sans désignation.** Le texte scellé (liste d'arrêt) dit qu'« une course créée sans texte de désignation scellé ne rejuge jamais le critère 3 ». L'ordre laisse donc la session de lancement trancher seule, par le seul calendrier, une question qui revient à Lazar.
- **Lancement avec désignation.** L'amorce n'extrait sur l'instance que les fichiers cités `piece_jointe`, `consignes_premier_test` et `banque` (l. 190-195 ; `CHEMINS_CLONAGE`, l. 163-178). Le texte de désignation n'est pas extrait. Or `controles_avant_depense` → `controler_registre` → `_fichier(racine, d, …)` le vérifie sur l'instance. Résultat : « ARRÊT » puis refus après l'installation, et la course ne peut pas partir sans un nouveau code. Aucun essai ne couvre ce chemin (`tests/test_dose_reponse_v2.py` ne passe une désignation qu'à `exiger_config`).

Correction, à substituer mot pour mot au préalable 3 :

« 3. Texte de désignation de la course pour le critère 3 : au jour de cet ordre, il n'est pas scellé (candidat 4, option A ou B non tranchée). **Aucune création sans l'un des deux mots de Lazar, consigné au registre des décisions :**
(a) « lancer sans désignation » : `designation_critere_3` vaut `null`, et la course ne rejugera jamais le critère 3 (texte scellé, liste d'arrêt) ;
(b) « attendre la désignation » : la création attend le scellement du texte et l'inscription de ses trois lignes (`DESIGNATION-CRITERE-3`, `CODE-LECTEUR-DU-TEXTE-DOSE-REPONSE`, `SONDES-LUES-CRITERE-3`). Il faut aussi une version 3 de l'amorce, qui ajoute `designation_critere_3.chemin` aux fichiers extraits sur l'instance (classe B : contre-lecture, commit neuf, ligne CODE neuve), puis un ordre v3. Le code a02b6540 ne peut pas jouer une course désignée. »

**B2. La déclaration de la session de lancement, exigée avant toute création, n'est pas inscrite, et l'ordre ne dit pas comment l'inscrire.**

Passage (préalable 1) : « Ligne `CODE-DOSE-REPONSE-CONSIGNE-CACHEE` inscrite par la mère […], déclarations de la session de lancement et de la mère ajoutées. »

La ligne CODE est déjà au registre de main (R-5306, 15:08:47Z). Sa pièce (`1521cbc9…`) porte `declaration_mere`, qui dit : « La déclaration de la session de lancement reste à ajouter avant toute création (inscription complémentaire, nom neuf) ». Le texte scellé (liste d'arrêt, première puce) en fait une condition d'arrêt. Le code ne la contrôle pas, et la session improviserait le nom et la forme.

Correction, à substituer mot pour mot au préalable 1 :

« 1. Ligne `CODE-DOSE-REPONSE-CONSIGNE-CACHEE` : déjà inscrite sur main (R-5306), pièce `registres/code-dose-reponse-consigne-cachee/CODE-DOSE-REPONSE-CONSIGNE-CACHEE-a02b6540070aa5731875d07fbbe124f2dbe27f3b-v1.json` (`1521cbc9…`).
1 bis. Avant l'étape 1, la mère inscrit sur main une pièce neuve, `registres/code-dose-reponse-consigne-cachee/DECLARATION-SESSION-LANCEMENT-DOSE-REPONSE-v1.json`, scellée. Elle porte :
- l'identifiant de la session de lancement (la mère elle-même si elle lance) ;
- la phrase « aucune action générée sous un texte de la pièce jointe (7a5f633c…) ni du fichier du premier test (a68468fe…) » ;
- le renvoi à la ligne CODE.
La mère inscrit aussi sa ligne `DECLARATION-LANCEMENT-DOSE-REPONSE-CONSIGNE-CACHEE` au registre des scellements, avant que l'étape 1 copie ce registre sur la branche de lancement. Sans cette ligne : aucune création. »

## Défauts majeurs

**M1. Jeton GitHub de l'instance.** Le lanceur choisit `CONTROLE_IA_GITHUB_TOKEN`, sinon `_2` (`jeton_gh_nom`, l. 54). Ce nom est figé dans la commande imprimée (`-e GH_TOKEN=\$…`). Dans cette session, c'est donc `_2` qui partirait, jamais `_3`. Un jeton de façade sous `CONTROLE_IA_GITHUB_TOKEN` partirait même en premier.

Correction, à ajouter en tête de la section 2 :

« Jeton GitHub de l'instance : `_3`, repli `_2`. Dans **chaque** appel du terminal qui joue `creation`, la commande de création imprimée ou `surveillance`, précéder la commande de `export CONTROLE_IA_GITHUB_TOKEN="${CONTROLE_IA_GITHUB_TOKEN_3:?}"`. Le lanceur la choisit alors, et la masque. Les appels du terminal ne gardent pas leurs variables : l'export se répète à chaque appel. Si l'amorce refuse avec « clonage impossible » ou « poussée initiale de la branche … refusée », l'instance se détruit seule en 3 minutes environ. Rejouer alors `creation` sans cet export (repli sur `_2`) ; c'est un essai de création de plus, trois au plus, et sa dépense entre dans la dépense antérieure. »

**M2. Ce que la surveillance rend, et ce qu'en fait la session : arrêt, versement, destruction (point c).** La section 3 ne dit pas comment lire les sorties ni ce qui suit un arrêt. Trois faits du code :
- **Fin normale lue comme une mort.** À la fin normale, l'amorce écrit « destruction demandée (fin normale …) ». Cette ligne ne répond à aucun motif de fin. La surveillance finit donc par « ARRET mort : instance … absente à deux relevés », sur une course réussie.
- **Une « FIN » qui n'en est pas une.** « FIN » (motif « fin, code N ») ne sort que d'un arrêt de l'amorce. Ce peut être une fin anormale, ou une poussée impossible avec disque gardé. Or le message imprimé invite à détruire si la machine est encore là. Détruire perdrait ce qui n'est pas poussé.
- **Collision à 90 USD.** À l'heure d'épuisement, la minuterie de l'instance consigne (jusqu'à 40 minutes), pousse, puis détruit. Un arrêt pendant ce temps, demandé par la session sur « ARRET depense », couperait la consignation en cours.

Correction, à ajouter à la section 3 :

« Lecture des sorties de la surveillance :
- **« ARRET mort … absente à deux relevés »** : la course peut avoir fini normalement. Relever `git ls-remote origin refs/heads/calcul/dose-reponse-v1`, puis lire l'inventaire et le journal poussés (`traces/`) : « versement prouvé » vaut fin normale.
- **« ARRET depense »** : lire d'abord `journal-instance.txt`. Si la minuterie a écrit « DÉPENSE ÉPUISÉE », ne rien arrêter : attendre sa destruction, au plus 75 minutes, puis vérifier par `vastai show instances`. Sinon, arrêter par l'identifiant.
- **« FIN » ou « ARRET mort » du processus** : l'amorce a arrêté l'instance, disque gardé. Ne jamais la détruire avant que le versement soit prouvé, c'est-à-dire branche poussée et inventaire présent sur la branche.

S'il manque quelque chose sur la branche : `timeout -k 5 120 vastai start instance <identifiant>`. Au second démarrage, l'amorce consigne, pousse puis détruit. Si le redémarrage n'est pas obtenu en 6 heures : nœud de Lazar (stockage à 0,08 USD de l'heure au plus).

Toute destruction se fait par `timeout -k 5 120 vastai destroy instance <identifiant>`, après le versement prouvé, et se consigne à `registres/arrets.md`. La dépense se consigne au registre des dépenses, relevée sur la facture du loueur. »

**M3. La surveillance doit tenir 24 heures, mais un appel en arrière-plan est coupé à 2 heures.** L'ordre ne dit pas comment la tenir.

Correction, à ajouter à la section 3 :

« Lancer la surveillance en arrière-plan, limite 7 200 000 ms. À chaque fin par délai, la relancer avec le même identifiant et le même dossier ; `progres.txt` et `compte-rendu-alerte.txt` persistent, donc l'alerte à 72 USD reste unique. Programmer un rappel de soi toutes les 2 heures au plus jusqu'à la fin. Si la session tombe, les gardes de l'instance tiennent : minuterie au plafond, arrêt sur un processus mort. »

**M4. Commandes à trous dans un ordre de classe A.** Passages : « `git checkout <branche de la banque> -- <banque> <banque>.sha256` » et « `<banque>` » dans l'appel du script de configuration.

Correction, mot pour mot :

```bash
git fetch origin main banque/dose-reponse-consigne-cachee-v1
git checkout origin/main -- registres/go.md registres/scellements-v1.md
git checkout origin/banque/dose-reponse-consigne-cachee-v1 -- donnees/20261124-144844-banque-dose-reponse-extraction-v2/taches-banque.json donnees/20261124-144844-banque-dose-reponse-extraction-v2/taches-banque.json.sha256
PYTHONPATH=src python scripts/ecrire_configuration_dose_reponse_v2.py donnees/20261124-144844-banque-dose-reponse-extraction-v2/taches-banque.json a02b6540070aa5731875d07fbbe124f2dbe27f3b
```

Ajouter : « empreinte attendue de la banque : `0065065b8958968235f13c48d4e423708fd5aaebb64f8eed6ec553e3c56459e4` (ligne BANQUE) ». Ajouter `--designation …` seulement sous l'option (b) de B1.

## Défauts mineurs

- **m1. Classe de la pièce.** Passage : « Pièce de classe C (proposition du développeur) ». Un ordre de course payante est de classe A (allègement du 19 novembre). Remplacer par : « Pièce de classe A (ordre d'une course payante), proposée par le développeur, contre-lue (R2), scellée par la mère, jouée par la mère seulement. »
- **m2. Paquets de la session (point d).** Passage du préalable 5. Remplacer par : « Session de lancement : `python3 -m venv .venv && . .venv/bin/activate && pip install -r requirements-cpu.txt -r requirements-pilotage.txt` (`torch` est exigé : `controles_v2` importe `environnements.pilote_a`, qui importe `torch` ; `vastai==1.8.3` lit `VAST_API_KEY` par son nom). Activer l'environnement en tête de chaque appel du terminal. `HF_TOKEN` lu par son nom, avec accès au modèle Llama-3.1-8B-Instruct. `DEPOT_URL=https://github.com/lciric/controle-ia-travail.git` est écrit en dur dans la commande de création ; le dépôt `origin` de la session doit être `lciric/controle-ia-travail`. »
- **m3. Arbre de lancement.** `git checkout -b lancement/dose-reponse-v1 a02b6540…` bascule l'arbre principal de la mère. Les appels qui suivent appellent `scripts/…` en chemin relatif, et le lanceur importe `$DEPOT/src`, donc depuis cet arbre. Remplacer par : « `git worktree add <bloc-notes>/lancement-dr -b lancement/dose-reponse-v1 a02b6540070aa5731875d07fbbe124f2dbe27f3b`, puis jouer toutes les commandes des sections 1 à 4 depuis `<bloc-notes>/lancement-dr` (`cd` en tête de chaque appel) ; jamais le lanceur de main. »
- **m4. Fin de l'accord de dépense.** Le code lit la fin de validité au lendemain 00:00 UTC de l'échéance du registre : 16 décembre 2026 à 00:00 UTC (`fin_go_utc_s=1797379200`, rejoué). Le texte scellé (devis) dit « fin du GO le 15 décembre 2026 à 00:00 UTC ». Ajouter : « Fin effective de l'accord : celle du registre, 16 décembre 00:00 UTC. Pour tenir aussi la lettre du devis, aucune création après le 12 décembre à 07:00 UTC. »
- **m5. Dépassement possible du plafond.** À l'heure d'épuisement, la minuterie consigne (jusqu'à 40 minutes), puis détruit (marge jusqu'à 30 minutes). Cela fait jusqu'à environ 1,6 USD au-delà de 90 si le plafond est atteint. Ajouter une ligne de réserve : « dépassement borné à environ 1,6 USD, déclaré à Lazar s'il survient ».
- **m6. Absence d'offre conforme.** Passage : rien sur le code 3 « aucune offre conforme ». Le texte scellé (point 11) demande douze recherches espacées de quinze minutes avant le nœud. Ajouter : « code 3, aucune offre conforme : rejouer la même commande `creation` toutes les 15 minutes, douze recherches au plus, puis nœud de Lazar ; aucune carte plus chère. »
- **m7. Reprise.** Ajouter : « en reprise, `DR_ESSAIS=0` (seize essais de chaîne au plus sur toute la course) ; dépense antérieure relevée sur la facture du loueur ; un disque plus grand que 300 Go n'est pas demandable sans code neuf (configuration figée) : nœud. »
- **m8. Lecture.** Passage de la section 5. Ajouter : « lecture jouée dans un arbre de la branche de sortie (code égal à a02b6540), jamais depuis main ; en cas de reprise, `--dossier` répété pour la course et chacune de ses reprises. »
- **m9. Appels du terminal sans état.** `export GO_ID=…` ne survit pas d'un appel à l'autre. Ajouter : « `GO_ID=GO-2026-11-24-25`, l'activation de l'environnement et l'export du jeton GitHub (M1) se répètent en tête de chaque appel. »

## Ce qui est conforme et n'appelle rien

- La branche de lancement part du commit du code et jamais de main. Le lanceur et l'amorce exigent l'égalité du code et l'ascendance du commit du code.
- La configuration égale celle que reconstruit le code.
- Les lignes BANQUE et CODE sont présentes, et la ligne CODE cite le commit.
- Les bornes de l'offre sont : A100 SXM4, au plus 1,30 USD de l'heure (stockage compris dans le filtre), 16 cœurs, 128 000 Mo, au moins 300 Go, stockage au plus 0,08 USD de l'heure, téléchargement au plus 0,05 USD par Go.
- Le plafond de 90 USD est cumulé sur les tentatives, avec une alerte unique à 72 USD. La minuterie de l'instance part à l'heure d'épuisement du plafond restant.
- Le calendrier refuse toute création après le 12 décembre.
- Les longueurs en jetons sont contrôlées avant la création, et la place disque avant les épisodes.
- Les arrêts se font par l'identifiant (R10), et la destruction n'a lieu qu'après le versement prouvé.

## Cloisonnement

Je n'ai ouvert ni la pièce jointe des textes privés ni le fichier du premier test : seules leurs empreintes ont été calculées. Je n'ai lu ni coffre, ni sortie de course, ni score, ni verdict. Rien n'est modifié, poussé, lancé ni loué. Mes rejeux sont dans `sim-controles/` du bloc-notes, hors dépôt.

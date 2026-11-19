# Contre-lecture du programme de vérification de l'environnement des agents, version 1 (classe B)

Contre-lecteur : modèle S, choisi parce que la seule place du modèle K sur ce compte est prise et que son autre version tire sur la même limite d'usage ; ce n'est pas un refus. Le code est écrit par le modèle L′ ; la mère en a été avertie et l'accepte (pièce de code, classe B).

**Verdict : Conforme.** Aucune correction demandée ; cinq observations (§ 5), dont une suggestion de durcissement peu coûteuse.

## 1. Pièces et empreintes

Commit cb23889b de `lot/compte-organisme-v1` (existe ; programme et essais de l'arbre de travail identiques à ce commit). `scripts/verifier_environnement_agent_v1.py` (9714a00f…), `tests/test_verifier_environnement_agent_v1.py` (94a89fc1…), rapport (fa019eed…) : empreintes égales aux annonces et à leurs compagnons. Mandat lu en entier ; programme lu en entier ; essais lus pour leur structure, les refus et le principe de l'espion. Version de l'interpréteur de cette contre-lecture : Python 3.13.18.

## 2. Le programme fait-il ce que dit le mandat, et rien d'autre ?

Oui.
- **Rapport** : version de Python, interpréteur, plateforme, heure UTC ; modules (présent, absent, erreur d'import, version, fichier) avec import protégé ; empreintes d'une liste (existence, type, taille, sha256, égalité) ; dépôt git (tête, branche, arbre propre). Aucun module tiers exigé.
- **Codes** : 0 tout lu ; 3 empreinte attendue non égalée (fichier différent, absent, illisible ou non ordinaire) ; 2 entrée invalide, chemin refusé ou sortie impossible à écrire. Un module absent, un dépôt non git, un fichier absent sans empreinte attendue sont rapportés, pas comptés comme écarts.
- **Sortie** : fichier neuf en mode exclusif, compagnon `.sha256`, jamais écrasé (un lien pendant compte comme existant) ; seuls ces deux fichiers sont écrits, et nettoyés si l'écriture ou la relecture échoue.
- **Processus** : le seul processus lancé est `git`, par liste d'arguments fixe (`shell=False`), avec `--no-pager --no-optional-locks -c core.fsmonitor=false`, variables `GIT_*` de l'appelant retirées, délai de 60 secondes ; rien dans `.git` n'est écrit (essai avec index périmé : instantané de `.git` inchangé). Aucun autre `subprocess`, aucun appel `os.system`.
- **Réseau** : aucun import ni appel de socket dans le programme.

## 3. Refus du segment `archives-reponses-modeles`, sans aucun accès

Le contrôle est correct et complet pour ce que le programme fait lui-même :
- chemin vérifié tel qu'écrit (casse ignorée par `casefold`), puis résolu composant par composant : chaque composant est contrôlé **avant** `islink`, chaque cible de lien **avant** d'être suivie, `..` résolu lexicalement sur un chemin déjà sans lien ; le dossier courant lui-même, s'il contenait le segment, ferait refuser un chemin relatif ;
- il vaut pour les lignes de la liste, `--empreintes`, `--depot` et `--sortie` (la sortie est résolue avant tout `lexists`) ;
- validation complète avant toute lecture : au moindre refus, aucun fichier de la liste n'est lu, aucun module importé, `git` non lancé, rien d'écrit ; tous les motifs sont rendus.
Les essais utilisent des tubes nommés (une lecture bloquerait) et un espion (crochet d'audit et enveloppes de `stat`, `lstat`, `open`, `readlink`…) qui ne voit aucun appel nommant le segment : liste, `..`, lien de fichier, lien de dossier, chaîne de liens, casse, et les trois options ensemble.

Limite de portée, déclarée par le développeur et que je confirme : `git status` exclut les chemins du segment par des pathspecs, mais ces exclusions ne coupent pas, à ma lecture du fonctionnement de git, le parcours du dossier ; l'essai montre que git ne les **rapporte** pas, non qu'il ne les **visite** pas. La garantie « sans accès » porte donc sur le programme, pas sur ce que git fait dans l'arbre qu'on lui donne. C'est l'état des choses pour tout `git status` du dépôt, que les agents lançaient déjà.

## 4. R5 et essais rejoués

Chaque refus et chaque écart a un cas sain et un artefact : segment (liste, lien, casse, options), empreinte différente (code 3), fichier absent ou dossier avec empreinte attendue (code 3), sortie existante, compagnon existant, lien pendant, dossier de sortie absent, dépôt non git (code 0, rapporté), dépôt absent (code 2), lignes de liste invalides, liste fautive, modules invalides, options, module absent, module en erreur d'import, bibliothèque standard seule, processus seulement `git`, `.git` non écrit. Les 16 défauts réintroduits sont tous vus.

Essais rejoués : copie dans mon bloc-notes, **46 passés sur 46** (5,9 secondes). Je n'ai exécuté que cette suite et des lectures ; aucune commande sur un chemin sous `archives-reponses-modeles/` du dépôt ; aucun code en ligne passé à un interpréteur.

## 5. Jugement des choix de la main du développeur

1. **Chemins relatifs lus depuis le dossier de la liste** : approuvé. C'est la sémantique de `cd dossier && sha256sum -c liste`, et les compagnons `.sha256` du dépôt servent tels quels. Le rapport JSON donne `base_des_chemins_relatifs` et `chemin_resolu`, donc aucune ambiguïté dans la sortie. Seule surprise possible : une liste « un chemin par ligne » écrite à la main depuis un autre dossier ; à dire aux agents.
2. **`git status` qui exclut les archives (« propre hors des archives »)** : approuvé. Le mandat veut qu'aucun agent ne touche aux archives ; l'exclusion évite de citer leurs noms et est déclarée dans le rapport JSON (`pathspecs_status`). Elle est testée suivie modifiée, non suivie, casse variée, dossier voisin. Voir la limite du § 3.
3. **Pas de `platform.platform()`** : approuvé. En Python 3.13 il lance `uname -p` ; la plateforme est lue par `os.uname` (`system`, `release`, `machine`), sans processus. Défaut réintroduit vu.
4. **Validation complète avant toute lecture** : approuvé ; c'est ce qui rend le refus sûr même avec plusieurs fautes. Le fichier de liste lui-même est lu pour trouver ses refus, ce qui est inévitable et permis.
5. **Anomalies au code 0** : approuvé, avec une réserve de présentation. Le code 3 reste réservé aux empreintes attendues, comme le mandat. Mais un module en erreur d'import ou un dépôt non git rend `statut: "lu"` et code 0 ; l'agent doit lire le champ `anomalies`. Un statut du genre « lu avec anomalies » serait plus visible ; non demandé, non requis.
6. **Dossier du programme retiré du chemin de recherche** : approuvé ; seul `sys.path[0]` égal au dossier du programme est retiré, sans effet si absent.

## 6. Observations, sans correction

1. **Bytecode** : le programme ne pose pas `sys.dont_write_bytecode`. Lancé sans `-B`, l'import d'un module demandé peut écrire un fichier d'octets compilés dans le dossier de ce module, ce qui irait contre « aucune écriture hors de la sortie ». L'appel documenté porte `-B` ; une ligne au début de `main` (`sys.dont_write_bytecode = True`) rendrait la garantie indépendante de l'appel. Suggestion, non exigée.
2. `--modules` importe du code arbitraire (c'est sa fonction) : un module qui lance un processus ou ouvre un réseau sort de la garantie ; le développeur le dit. Le contrôle du segment ne porte pas non plus sur les dossiers de `sys.path` (par exemple une variable `PYTHONPATH` qui en citerait un).
3. L'essai « espion » ne capte pas une écriture directe sur le descripteur 1 au niveau C ; dit au rapport.
4. Les essais créent dans leur dossier temporaire des dossiers au nom du segment (tubes nommés) pour éprouver les refus ; rien de tel dans le dépôt.
5. Course entre validation et lecture : couverte en partie par `O_NOFOLLOW` et le contrôle `fstat` ; suffisant pour l'usage.

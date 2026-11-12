# Contre-lecture (R2) de l'addendum 4 au préenregistrement du témoin de Bailey — brouillon 2 — v1

Contre-lecteur neuf, sous-agent lancé par la session `session_01XJ6MgnEhQMZteN9F8a1BST` ; n'a écrit aucun des fichiers lus.
12 novembre 2026, vers 22:40 UTC. Cloisons tenues : ni `donnees/bras-attaque*`, ni `donnees/mode-tenu-a-l-ecart*`, ni
`docs/notes/bras-attaque/`, ni `docs/notes/programme-et-4-familles-evasion/`, ni `registres/etat.md`, ni
`registres/decisions.md`, ni aucun résultat ou seuil de sonde ou de moniteur du programme ; aucune variable
d'environnement de secrets lue, aucun fichier de clé ouvert ; aucune commande réseau ; aucun fichier existant modifié
(seul ce rapport est écrit ; les essais ont tourné avec `-p no:cacheprovider`, l'essai à vide de la conduite avec
`PYTHONDONTWRITEBYTECODE=1`). Le fichier `controle-juge-v3.json` n'a été ouvert que pour lister ses clés, sans lire de
valeur.

Brouillon relu : `brouillons/temoin-attaque-publiee-bailey-v1-addendum-4-code-v17-execution-v4-brouillon2.md`
(`d49ed4ef4e7115dce30460020dab263847d2f38a89e8b9bf821a12f25cc20851`), à la tête `e4ae2610` de la branche
`claude/compassionate-meitner-d4ryyk`.

## Verdict

**Scellable après corrections.** Aucun bloquant. À corriger : K-1 (renvois v10 au lieu de v11), K-2 (risque (b) faux sur
`sys.modules["__main__"]`), K-3 (condition 7 fondée sur un précédent limité à la série précédente), K-4 (« aucune sortie
sous ces graines » : le contrôle du juge en a produit), K-5 (résultat de la suite d'essais laissé en blanc), K-6 (risque
manquant : premier passage réel des gardes de démarrage et par tour). À préciser : K-7 à K-11.

Sur le fond, l'addendum fait ce qu'il doit : les deux écarts sont nommés comme écarts, rattachés au mot verbatim de
Lazar, et la troisième série est bornée (une seule, mêmes graines, même B, D cumulé, nouvelle seconde chute : nœud). Le
texte ne contient aucun résultat, ne change aucune hypothèse, aucun seuil, aucune métrique. Le code, les empreintes, les
commits, le manifeste, la liste `ANTERIEURES` et la chaîne v11 sont conformes à ce qui est écrit, aux points K-1 et K-9
près.

## Vérifications faites

**Empreintes (toutes égales au fichier et à son compagnon `.sha256`)** : `execution_v4.py` `560247ed…`,
`instance_v16.py` `d9a56e87…`, `lanceur_v17.py` `acad9644…`, essais v17 `c2b498bb…`, manifeste v4 `e15d456f…`, manifeste v5
`111c6e98…`, conduite v9 `18864f6b…`, v10 `9cb1bd5f…`, v11 `d279ea19…`, poste v9 `4ac2822b…`, v10 `406c7fd6…`, v11
`059d0837…`, constructeur v9 `3923bdbb…`, v10 `c79f2c24…`, v11 `2e9df5ba…`, épreuve v1 `17c3544d…` (sortie `7c204bd5…`),
épreuve v2 `0677c557…` (sortie `316910b9…`), message d'erreur `33599bfc…`, notes `b70d8fea…` et `cb16b95c…`, contre-lecture
du code `833429c6…`, préenregistrement `fb6c2f34…`.

**Commits.** `8d1c541e` = `8d1c541ef7a3ac99f942e0b2f26567088f2cc503` ; `60d06b1f..8d1c541e` ne touche aucun module de
`src/` (essais : seules les assertions C-2 ; épreuve v2 et sa sortie ; compagnons `.sha256` ; contre-lecture du code et son
compagnon) ; `8d1c541e..HEAD -- src/` est vide (la garde du poste v11 passerait à la tête actuelle) ; `91238a73..8d1c541e --
src/` n'ajoute que les trois modules v17 et leurs compagnons.

**Code.** `diff execution_v3 execution_v4` : docstring, `import runpy`, et les trois lignes de l'appel
(`runpy.run_path(str(script), run_name="__main__")`) ; `diff instance_v15 instance_v16` : docstring, import l. 222,
commande l. 792 ; `diff lanceur_v16 lanceur_v17` : docstring, import l. 271, `INSTANCE_MODULE`, `VEILLEUR_MODULE`,
`CHEMINS_ARCHIVE`, un commentaire, une docstring l. 917, un message l. 1783. Conforme au § 3. Le défaut est bien dans
`execution_v1` (l. 84-86), `v2` (l. 86-88), `v3` (l. 101-103). Le script public (clone au commit `9c1f4b1a` de la
session) porte `@hydra.main(...)` l. 171 et `if __name__ == "__main__": main()` l. 227 : `runpy` l'exécute bien.

**Essais.** 169 fonctions d'essai dans le fichier v17 (161 v16 + 8 v17, noms vérifiés). Rejoués ici :
`tests/test_temoin_bailey_condition6_v17.py` entier, **168 passés, 1 sauté** (l'essai des configurations publiques, sans
`TEMOIN_BAILEY_CONFIGS_PUBLIQUES`), 178 s, Hydra 1.3.8 et OmegaConf 2.3.1 du `.venv`.

**Épreuve v2.** En-tête écrit par le script (interpréteur, emplacements de Hydra 1.3.2 et d'OmegaConf 2.3.0, commit du
clone, empreinte de `configs/`, empreinte des essais `c2b498bb…`, égale au fichier) ; v4 : code 0, début exact,
journaliseur substitué, dossier courant et `sys.path[0]` au dossier `inference_time_experiments`, module local, graine 7,
`__main__`, `argv[0]` ; v3 : code 1, rien imprimé. Conforme au § 3.

**Manifeste.** `diff manifeste-local-v4.json manifeste-local-v5.json` : une seule ligne, `commit_code` (`91238a73…` →
`8d1c541e…`). Conforme.

**`ANTERIEURES` (conduite v11).** Six instances : 60280913, 60326443, 60330510, 60370363, 60400450, 60403564 ; les
valeurs (`c`, `creation`, `destruction`) sont identiques, chiffre pour chiffre, à `sortie-conduite-v9/poste-v5.json` ; la
liste de la v9 est la même sans 60403564. D recalculé : 0,3112 + 0,4167 + 0,8091 + 0,4391 + 0,0565 + 0,7455 =
**2,7781 USD**, égal à `registres/depenses.md` (ligne 60403564) ; première création 1794441800,04 = 2026-11-12 00:03:20Z.

**Chaîne v11.** `diff` v9 → v11 et v10 → v11 de la conduite, du poste et du constructeur : la conduite v11 ne diffère de
la v9 que par la docstring, `lanceur_v17`, 60403564 dans `ANTERIEURES`, le manifeste v5 et les noms `lancement-v11.pid`,
`sortie-conduite-v11`, `bilan-lancement-v11.json` ; de la v10 que par la docstring (défaut de syntaxe corrigé) et ces trois
noms. Le poste v11 ne diffère de la v9 que par ses commentaires, les noms en `-v11` (journal, poussées, état, battement,
offre, PID, marque de fin), les compagnons vérifiés (`lancer-conduite-v11.py.sha256`, `manifeste-local-v5.json.sha256`)
et la garde du commit (`git cat-file -e 8d1c541e…^{commit}` puis `git diff --quiet 8d1c541e… HEAD -- src/`, sinon
« rien ne tourne », code 3). Le constructeur v11 ne diffère que par `SCRIPT = poste-hetzner-v11.sh` et le nom et
l'étiquette du serveur. `grep` : hors commentaires et docstrings, aucune référence à v9, v10 ou `91238a73` ne reste dans
les chemins exécutés du poste v11, de la conduite v11 ni du constructeur v11. Analyse syntaxique : conduite v9 et v11,
constructeur v11 lisibles ; **conduite v10 : `SyntaxError` (l. 6)**, comme le dit le § 3 ; `bash -n` du poste v11 :
correct. Essai à vide de la conduite v11 sans `GO_ID` ni `DEPOT_URL` : « rien ne tourne », code 2, aucun fichier écrit.

**GO.** `GO-2026-11-10-10` (part Bailey : 75 USD, B = 75, garde à B − 2, préenregistrement `fb6c2f34…`, devis v4) et son
amendement `GO-2026-11-11-01` (échéance 2026-11-30), lus sur `main` comme le fait `texte_go_main`. Conforme au § 6,
condition 2.

## Constats

### K-1 — à corriger — renvois au poste et à la conduite v10, qui ne tourneront pas (l. 53, 60, 141)
Preuve : le § 3 (l. 98-104) établit que la conduite v10 porte un défaut de syntaxe et que les pièces v10 « n'ont jamais
tourné » ; les pièces de lancement sont la conduite v11 et le poste v11. Or le § 2.2 cite « liste `ANTERIEURES` de la
conduite v10 », et le § 2.4 et la condition 8 du § 6 citent un « poste Hetzner autonome neuf, v10 ». Les valeurs sont les
mêmes (la v11 ne change pas `ANTERIEURES`), mais le texte scellé doit nommer la pièce qui tournera.
Correction, l. 53-54 : « (liste `ANTERIEURES` de la conduite v11, `d279ea19…`, identique à celle de la conduite v10 jamais
tournée : elle ajoute 60403564, valeurs de `sortie-conduite-v9/poste-v5.json`, à celle de la conduite v9) ». L. 60 et
l. 141 : « v10 » → « v11 (`poste-hetzner-v11.sh`, `059d0837…`) ».

### K-2 — à corriger — risque (b) faux sur `sys.modules["__main__"]` (l. 122-125)
Preuve : le texte dit que « le module principal reste `controle_ia…execution_v4` dans `sys.modules["__main__"]`
(`runpy.run_path` crée un module temporaire et rétablit l'ancien) ». Dans Python 3.11, `runpy._run_module_code` place le
module temporaire **dans** `sys.modules["__main__"]` pendant l'exécution (`_TempModule.__enter__`) et rétablit l'ancien
après. La contre-lecture du code (§ 2, « Effets propres à `runpy` », et sa sonde) l'a observé :
`sys.modules["__main__"].__file__` = le script. Vérifié de nouveau ici (lanceur minimal sous `python3 -I` : avant, le
lanceur ; pendant, le script, `__name__ == "__main__"` ; après, le lanceur). La différence décrite n'existe donc pas
pendant l'exécution.
Correction : « (b) `runpy` n'est pas `python train_harmful.py` à la lettre. Pendant l'exécution, `sys.modules["__main__"]`
est le module du script, comme chez les auteurs ; il redevient `execution_v4` au retour. Restent : le module
`execution_v4` et ses imports déjà chargés, `sys.path` qui porte en plus le dossier `src` du dépôt, et les modules publics
importés avant l'appel (`obf_reps.logging`, `obf_reps.utils`, `transformers`). La contre-lecture n'a trouvé dans le code
public ni sérialisation d'objet défini dans le script, ni processus fils, ni lecture de `__file__`. »

### K-3 — à corriger — condition 7 : le précédent invoqué valait « pour cette série » (l. 139-140)
Preuve : la condition 7 du texte exige « le mot direct de Lazar pour le lancement » (l. 388). À l'addendum 3, § 7.3, le
« go (a) » n'a été tenu pour mot de lancement que par une décision exprès de Lazar sur un nœud (« go 1a 2a′ 3b »), avec
cette portée : « Le « go (a) » est tenu pour le mot direct de Lazar **pour cette série** » ; la session y recommandait un
mot exprès. La décision du 12 novembre à 22:10 (`cb16b95c…`) dit « go (a), garde le poste » ; son option (a) nommait bien
« nouvelle série », mais la note ne dit pas que ce mot vaut mot de lancement, et sa ligne « Engage » s'arrête à « addendum
4 scellé avant toute instance ». Le brouillon étend donc lui-même un précédent borné. L'approbation de la série est
fondée sur le texte de la décision ; le mot de lancement ne l'est pas.
Correction (recommandée) : « 7 : à obtenir avant toute instance : le mot direct de Lazar pour le lancement de la troisième
série. Le « go (a) » approuve une option qui nommait « nouvelle série » ; le § 7.3 de l'addendum 3, qui tenait un « go (a) »
pour mot de lancement, valait pour la seule série de cet addendum. » Autre possibilité, si Lazar le confirme par écrit
avant le scellement : citer ce mot, verbatim, avec sa note.

### K-4 — à corriger — « aucune sortie n'a été produite sous ces graines » ; « aucune note de juge n'existe » (l. 6, 49-52)
Preuve : le contrôle du juge, à la mise en place, génère les réponses « négatif » sous la graine « pilote » (texte, paragraphe
« Contrôles du juge », l. 232-237 ; `instance_v16.controle_juge`, `set_seed(int(manifeste["graines"]["pilote"]))`), et le juge les
note ; il a tourné et passé à chaque série (`sortie-conduite-v9/controle-juge/transfert-1/controle-juge-v3.json`, clés
`negatif`, `positif`, `garde_juge`… ; valeurs non lues ici). La phrase est donc fausse à la lettre. L'argument de
compatibilité avec R3 tient quand même : le contrôle du juge est une garde, pas une lecture de résultat, et rien de la
boucle n'a tourné.
Correction, l. 6-7 : « aucune note de la boucle (sonde ou juge sur une attaque) n'existe (zéro tour complet dans toutes
les exécutions) et aucune n'a été lue ; seul le contrôle du juge de la mise en place, une garde, a tourné et passé ». L.
49 : idem. L. 51-52 : « Mêmes graines (pilote 1394228342, run principal 1865327867) ; sous la graine du pilote, seul le
contrôle du juge (garde de mise en place) a produit des réponses et des notes du juge ; aucun tour n'a été joué sous
l'une ou l'autre graine. La mise en place, contrôle du juge compris, est refaite pour la troisième série, sous la même
graine. »

### K-5 — à corriger — résultat des essais laissé en blanc (l. 88)
Preuve : « suite complète du dépôt : en cours au moment de la contre-lecture (résultat inscrit avant le scellement) » ; et
le compte du fichier v17 n'est pas donné (seuls « les 8 essais v17 passés »). Rejoué ici : fichier v17, **168 passés, 1
sauté**. Dans le bloc-notes de la session, une première passe de la suite complète
(`pytest_v17_complet.txt`, arrêtée vers 24 %) montre **deux échecs** (`F`) ; une seconde passe tournait à 22:36Z.
Correction : inscrire avant le scellement « essais v17 : 169 (161 v16 rejoués, 8 v17) : 168 passés, 1 sauté sans
`TEMOIN_BAILEY_CONFIGS_PUBLIQUES`, passé quand il est fourni ; suite complète du dépôt : N passés, M sautés, E échecs »,
et pour chaque échec : son nom, sa cause, et s'il touche un module de `src/controle_ia/temoin_bailey/` ou un module que
l'archive envoie sur l'instance. Un échec qui toucherait ce code empêche le scellement tant qu'il n'est pas expliqué.

### K-6 — à corriger — risque manquant : premier passage réel des gardes de démarrage et par tour (§ 5)
Preuve : sur l'instance, aucune exécution n'a jamais atteint l'impression de la configuration ; la garde de démarrage
(empreinte du début exact de la sortie standard contre `configuration_attendue`) et les gardes par tour (pas, longueurs,
suffixe appris, appariement, lignes « MARK ») n'ont été jouées que sur processeur, avec des chemins de travail et un
mini-script. Si l'une tombe à tort de façon déterministe (par exemple une ligne imprimée avant la configuration, un chemin
réel rendu autrement, un nombre de pas journalisé autrement), le pilote tombe, la reprise tombe de même, et la série est
consommée : nœud. Le message d'erreur ne sort pas dans ce cas (garde décidée, addendum 3, § 2.2) : le diagnostic se borne
au nom de la garde et à la grandeur en cause.
Correction, ajouter : « (e) **premier passage réel des gardes.** La garde de démarrage et les gardes par tour n'ont
jamais été jouées sur une exécution réelle du script public (la v3 mourait avant). Une garde qui tomberait à tort, de
façon déterministe, au pilote ferait tomber aussi la reprise : seconde chute, nœud, sans message d'erreur (garde
décidée) ; le diagnostic se borne au nom de la garde et à la grandeur en cause. Ce risque n'est pas introduit par la v4 ;
il était caché par la mort de la v3. »

### K-7 — à préciser — essai à blanc (§ 2.2 ou § 6)
Preuve : l'addendum 3, § 7.1, avait fait trancher par Lazar que la première exécution sur A100 tenait lieu d'essai à blanc,
« enjeu accepté : une nouvelle double chute du pilote consomme la seule série permise ». Le brouillon n'en dit rien, alors
que son risque (a) reconnaît qu'« aucune épreuve sans carte ne couvre ce chemin ».
Correction, ajouter au § 2.2 : « Aucun essai à blanc ne précède : comme à l'addendum 3, § 7.1, le pilote de la troisième
série en tient lieu ; une nouvelle double chute consomme la série (risques (a) et (e)). »

### K-8 — à préciser — alerte de l'addendum 3, § 7.2, reprise en partie (l. 141-142)
Preuve : le § 7.2 de l'addendum 3 prévoit l'alerte à 30 minutes si la configuration effective n'est pas décidée (quand le
journal la rend visible), sinon à 4 heures ; le brouillon ne garde que les 4 heures et ajoute « à toute issue de la liste
d'arrêt », qui n'y figure pas, tout en écrivant « gardée ».
Correction : « Alerte : celle de l'addendum 3, § 7.2, gardée telle quelle (30 minutes, si le journal le rend visible ;
sinon 4 heures après le lancement du pilote) ; en plus, la session alerte Lazar à toute issue de la liste d'arrêt. »

### K-9 — à préciser — exactitudes du § 3 (l. 76, 80, 91)
- l. 76 : le commit `8d1c541e` ajoute aussi la contre-lecture du code et son compagnon. Écrire : « n'ajoute que les essais
  complétés (C-2), l'épreuve v2 (C-1), la contre-lecture du code et les empreintes ».
- l. 80 : double accent grave autour de `c2b498bb…`. Ajouter que la contre-lecture du code a lu les essais à l'état
  `6856b0b2…` (avant C-2), et que `c2b498bb…` n'en diffère que par les assertions C-2 (13 lignes, vérifié par `git diff
  60d06b1f 8d1c541e`).
- l. 91 : les empreintes de `configs/` des deux en-têtes diffèrent (`aeeab086…` en v1, `100152d5…` en v2) parce que la v2
  hache chemins et contenus ; le dire en une demi-ligne pour qu'un lecteur ne croie pas à deux dossiers différents.
- § 5 (c) : les essais du dépôt jouent aussi OmegaConf 2.3.1 (version figée : 2.3.0) ; l'épreuve hors essais a joué 2.3.0.

### K-10 — à préciser — en-tête et section « Contre-lecture »
Preuve : l'addendum 3 liste ses brouillons avec leurs empreintes ; le brouillon 2 cite le brouillon 1 sans empreinte.
Correction : à l'en-tête, « brouillon 1 (`…-brouillon1.md`, `878eca8876ea98cdd99433c852ebb5c614252cca47032f29a87387de06071cf2`) ;
brouillon 2 (`…-brouillon2.md`, `d49ed4ef4e7115dce30460020dab263847d2f38a89e8b9bf821a12f25cc20851`, contre-lu) » ; retirer
« non contre-lu, non scellé » au scellement ; remplir la section « Contre-lecture » avec ce rapport, son empreinte et le
traitement de chaque constat.

### K-11 — à préciser — ce que le poste v11 ne vérifie pas (§ 5 ou § 6)
Preuve : le poste v11 vérifie la conduite v11 et le manifeste v5 contre leurs compagnons **du même clone**, et `src/`
contre `8d1c541e` ; il ne vérifie ni la présence de l'addendum 4 scellé, ni l'empreinte du poste lui-même (le constructeur
l'imprime, sans la comparer). Même pratique qu'aux postes v8 et v9 ; aucun défaut, mais l'ordre de lancement porte seul ces
deux contrôles.
Correction, ajouter à la condition 8 : « l'ordre de lancement relève, avant la création du poste, que la tête poussée de
la branche porte l'addendum 4 scellé, et que l'empreinte du script sans secrets imprimée par le constructeur v11 est
`059d0837…` ».

## Réponses aux cinq questions

1. **Écarts.** Oui : le lancement par `runpy` et la troisième série sont nommés comme écarts (à R3, aux l. 69-71, 245,
   366 du texte, au § 2.4 de l'addendum 3 ; renvois de lignes vérifiés), rattachés au mot verbatim « go (a), garde le
   poste » (`cb16b95c…`), et compatibles avec l'objet de R3 : zéro tour complet partout, aucune note de la boucle, rien
   lu (formulation à corriger, K-4). La série est bornée : une seule ; pilote, au plus une reprise ; mêmes graines ; B = 75
   fixé à 60280913 ; D cumulé (2,778 USD vérifiés) ; nouvelle seconde chute : nœud, aucune autre série sans décision et
   addendum.
2. **Exactitude.** Code, empreintes, commits, essais, épreuve, manifeste (seule différence `commit_code`), `ANTERIEURES`
   (six instances, valeurs identiques à `poste-v5.json`), garde du commit du poste v11, chaîne v11 : conformes, sauf K-1
   (renvois v10), K-2 (risque (b)), K-9 (détails).
3. **Risques.** Le risque (a) (mort après l'impression, sans message) est honnête et conforme au code
   (`ecrire_erreur_demarrage` exige une garde de démarrage non décidée). Le risque (b) est faux (K-2). Il manque le premier
   passage réel des gardes (K-6) et l'essai à blanc (K-7).
4. **Conditions de lancement.** Conditions 1 à 6 et 8 cohérentes avec l'addendum 3 et le texte (K-1 pour le numéro du
   poste, K-11 pour l'ordre de lancement). Condition 7 : non fondée sur le texte de la décision (K-3).
5. **Résultat, chiffre, modification.** Aucun résultat ; aucun changement d'hypothèse, de seuil, de métrique, de
   population, de juge, de modèle, de bras. Chiffres vérifiés (D, graines, B, heures, empreintes) ; seule erreur de fait :
   K-4.

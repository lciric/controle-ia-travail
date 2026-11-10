# Relecture des lignes touchées v6 → v7 du code de la condition 6 — témoin Bailey — v1

- Lecteur : R2, sous-agent neuf. Je n'ai écrit ni le texte scellé, ni le code, ni les essais, ni les rapports, ni la
  liste des lectures, ni les sondes du relecteur précédent. Date : `date -u` = Tue Nov 10 14:33:18 UTC 2026 (fin des
  sondes).
- Je reçois d'office le `CLAUDE.md` du dépôt (`b4cbc66a422a6246df0479fe0c886eccb92cd3410d6a8b742eddea5325098eae`).
- Dépôt : `/home/user/controle-ia-travail`, branche `claude/compassionate-meitner-d4ryyk`, commit `f1e128ac`, arbre
  propre avant ce rapport ; `origin/main` = `617d77d4`.
- Pièces lues et empreintes (SHA-256, sur disque) :
  - texte qui prime : `prereg/temoin-attaque-publiee-bailey-v1.md` (`fb6c2f34355d98ba08798cab1a4964a03b41eedf57d687454663f01c9646f2c3`), l. 325-380 ; R4, R5 du `CLAUDE.md` ;
  - rapport appliqué : `relecture-lignes-touchees-code-condition6-v6-bailey-v1.md` (`a46dc4fb4766b58892e6e1a1c906cff44d826a69cd0a236ad693d09b22c14941`), en entier (C-1 à C-4, E-1, E-2) ;
  - liste des lectures : `lectures-a-acter-addendum-condition6-v4.md` (`351c778c796ef8cafdec135c2446bff1677356b037683e85bd22c05dd7ee0996`), en-tête, lectures 1-4, 12, 13, 16, 36 et conclusion ;
  - code, par `diff -u` : `lecture_v6.py` (`2c205e95…`) → `lecture_v7.py` (`05c69155b7513a2561b45c78e2d3a42a42791079ab8bf62832bd59a21d175445`) ;
    `instance_v6.py` (`93983898…`) → `instance_v7.py` (`7824b0c977cdce3e8a30a839bbd2b6847f6adf4b4b29801e965ae6172e71a0e3`) ;
    `lanceur_v6.py` (`cf73d706…`) → `lanceur_v7.py` (`eaacebe770e3fcf89d875a5d4c794b339d276868f89335d49a6b21ffebb55784`) ;
    contexte : `lecture_v7.py` `issue_pilote`, `k_prime`, `valider` (l. 386-400, 456-477), `audit` (l. 580-598) ;
    `instance_v7.py` `Surveillance` (l. 378-415), `Popen` (l. 494) ; `lanceur_v7.py` `_tours_relus`, `_executer`,
    `normaliser_execution` ; `journaliseur_v3.py` `_ecrire` (l. 62-65, `sort_keys=True`), `__init__` (l. 160-175),
    `_garde` (l. 197-208), l. 285-302 ; `execution_v3.py` l. 63-73 ;
  - essais : `tests/test_temoin_bailey_condition6_v7.py` (`ab9aa5248879ef738985dd3d9c5d1131291f965b9a0f071330a8481938793745`), par `diff -u` avec `…_v6.py` (`19ab2009…`).
- Non lu : tout le reste du dépôt ; aucun des répertoires ou lignes cloisonnés ; aucun journal, aucune note, aucun
  résultat ; aucune clé ; aucune requête réseau ; pas de `vastai`.
- Outils : `diff -u`, `sed`, `grep`, `sha256sum` ; `pytest` (venv du dépôt), avec `TEMOIN_BAILEY_CLONE` du clone
  obfusqué. Essais v7 : **43 passés** (56 s). Sondes du relecteur précédent rejouées sur la v7
  (`…/scratchpad/c6-v7/test_sondes_r2_v6_sur_v7.py`, `75c17691a6e721c3ed042e83879ac7469bb2d15ffc798aa3e204c19602c87d28`) :
  P1 à P5 **échouent** (§ 2). Sondes neuves de ce relecteur :
  `/tmp/claude-0/-home-user/157246e4-0739-5bb4-9302-ec187f3c5161/scratchpad/diff-c6-v7/sondes/test_sondes_r2_v7.py`
  (`e26ae9dc3c9bc74c1178d74aab647aaf7167c9cdbb16f23ac72719a7553b30c5`) : Q1, Q2 **passent** (chaque sonde affirme un
  écart : il est présent ; aucun ne change d'issue dans un cas que le code peut produire, ou il est déjà de la classe
  d'un risque déclaré, § 3).

## 1. Verdict

**Conforme : l'addendum peut être écrit (après le mot de Lazar sur les lectures à acter).** C-1 à C-4, E-1, E-2 sont
appliqués en entier. Deux points **à préciser à l'addendum** (lecture 36), non bloquants : A-1 (gardes du lanceur) et
A-2 (risque déclaré étendu au pilote). Aucune correction de code exigée ; une correction d'une ligne est proposée,
facultative (A-1).

## 2. C-1 à C-4, E-1, E-2 — conformes

- **C-1** (`_lire_jsonl`) : lecture en octets, découpe sur `b"\n"`, décodage UTF-8 strict par ligne ;
  `(UnicodeDecodeError, json.JSONDecodeError)` suivent la même règle (dernière ligne sans `\n` → coupée ; sinon
  `GardeArret`, chemin complet au message). Une ligne entière sans `\n` est lue (essai). Plus aucune exception hors
  `GardeArret` sur un journal coupé.
- **C-4** : `LIGNES_TRONQUEES` supprimé ; `lire_jsonl(chemin, signal=None)` lève `GardeArret` sans liste (jamais
  d'oubli silencieux) ; `valider`, `lire`, `etat_reconstitue_lecture`, `executer`, `reconstituer_etat`, `tours`
  portent chacun leur liste. `lire` copie celle de `valider` (`list(...)`) et ne modifie jamais `validite_`.
  L'alias interne de `reconstituer_etat` (`res` et `etat_` partagent `signal`, puis `lire_jsonl(durées, signal)`) est
  sans effet : le fichier des durées est déjà lu par `tours_journal`, `signaler` ne double pas.
- **C-2** : chemin complet, sans doublon (`signaler`) ; `valider` y ajoute les lignes portées par les états
  transférés (`_signal_etat`, annotées « état d'exécution « nom », écrit sur l'instance »), sauf un état reconstitué
  à la lecture (déjà compté) ; chaque interruption porte celles de son état ; `lire` les rend aux deux retours, et
  lève si la clé manque. Instance : état et ligne `ETAT` (`executer`, `tours`, `tours --ecrire-etat`) ; lanceur :
  `_tours_relus` et `_executer` (exécution morte) les reportent au bilan. Une même coupure apparaît deux fois au
  verdict (chemin sur l'instance, via l'état ; chemin du transfert) : voulu, elle nomme l'exécution et le transfert
  (essai E-2, `len == 2`).
- **C-3** (`tours_journal`) : dernière ligne coupée du journal des gardes → `garde_tombee` et `ligne_de_garde_coupee`
  au dernier tour présent ; essai « suite des étiquettes » coupée après MARK e → K′ = e, jamais e + 1. Juste pour
  `gardes-v3.jsonl`. Pour `gardes-lanceur-v3.jsonl`, voir A-1.
- **E-1** : `test_E1_M1_par_comportement…` éprouve le comportement (deux `tours --ecrire-etat`, le second dans
  `_finir`, avant `empreintes` et `detruire` ; échec consigné, pas de relance), non plus le source.
- **E-2** : trois essais (verdict transféré coupé ; première exécution d'une relance, avec et sans état ; bout en bout
  conduite morte) : la clé est dans l'état, `valider`, `lire`, l'interruption et le bilan ; K′ = 20, jamais 21.

**Sondes P1 à P5 rejouées sur la v7.** Toutes échouent :
- P1 : raison de fond. `lire_jsonl(p)` ne lève plus `UnicodeDecodeError` ; sans liste, il lève `GardeArret`
  (« sans liste de signalement ») ; avec liste, la ligne est ignorée et signalée (`test_P1_inverse…`, qui éprouve
  aussi le même octet coupé au milieu et en dernière ligne finie → `GardeArret`).
- P3 : raison de fond (la clé est dans le retour anticipé de `lire`).
- P2, P4, P5 : échouent **seulement** sur `AttributeError` (`LIGNES_TRONQUEES` n'existe plus). J'ai donc vérifié les
  essais inversés de la v7 :
  - `test_P2_inverse…` : `not hasattr(lc, "LIGNES_TRONQUEES")` ; un `valider` sur un journal technique coupé rend une
    liste non vide ; `lire` puis un second `valider` (et un troisième sur un dossier vide) laissent `r1` inchangé ;
    `lire` rend un autre objet. Éprouve le défaut P2 (résultat modifié après coup, effacé par un second appel). ✔
  - `test_P4_inverse…` : deux fichiers de même nom dans `pilote/` et `principal/`, le premier relu deux fois → deux
    chemins complets, sans doublon. Éprouve P4. ✔
  - `test_P5_inverse…` : dernière ligne `{"etat": "tom` coupée → `tours`, `tours --ecrire-etat` (ligne `ETAT` **et**
    fichier d'état) et `reconstituer_etat` (« déjà présent ») portent le chemin ; `tours_complets` passe de 5 à 4
    (C-3). Éprouve P5. ✔ ; `test_C4_instance_liste_propre…` éprouve en plus l'absence d'accumulation dans le processus.

## 3. Points à préciser à l'addendum (non bloquants)

**A-1. Gardes du lanceur : C-3 retire un tour, la ligne entière les retirerait tous.** Dans `tours_journal`, une ligne
« tombée » entière de `gardes-lanceur-v3.jsonl` vaut pour **tous** les tours (`lanceur_tombe`, K′ = 0) ; coupée, C-3
ne retire que le dernier tour présent (K′ = e). Sonde Q1 : 6 tours marqués, « configuration effective » tombée ;
entière → K′ = 0, coupée → K′ = 5. L'essai `test_C3_…` (cas « lanceur ») fige ce comportement. La docstring de la v7 et
la lecture 36 (d) disent « jamais un tour de plus que n'en rendrait le journal intact » : c'est faux à la lettre pour
ce journal. **Aucune issue ne change** dans un cas que le code peut produire : ses lignes sont toutes écrites au
démarrage, `tour` −1 (`execution_v3._consigner_garde_lanceur`, `journaliseur_v3` « dossier neuf », processus enfant
qui s'arrête aussitôt ; `instance_v7.Surveillance` « configuration effective », écrite avant toute ligne `MARK` reçue,
par le processus même qui écrit les durées : s'il meurt pendant cette écriture, aucune durée n'est écrite ensuite) ;
une ligne coupée y précède donc toujours K′ = 0. À préciser : soit écrire à la lecture 36 (d) « dans les gardes du
lanceur, écrites avant tout tour, la règle retire le dernier tour présent ; une ligne entière les retirerait tous ;
sans effet, aucune durée n'étant écrite après » ; soit, plus simple et vrai par construction (facultatif), dans
`lecture_v7.tours_journal` : `lanceur_tombe = coupee_l or any(...)` (une ligne coupée du lanceur se lit comme une
garde du lanceur tombée), et l'essai `test_C3_…` cas « lanceur » attend alors K′ = 0. Coût nul dans les cas réels.

**A-2. Risque déclaré de la lecture 36 : le pilote n'y est pas.** Le risque déclaré (nom d'une garde coupée perdu)
ne vise que `relance_permise`. Le même cas existe au pilote : « sonde orientée » tombe au tour 0 (`journaliseur_v3`
l. 296-297) ; si sa ligne est coupée, `gardes_tombees` ne la nomme pas et `issue_pilote` rend « chute » (code non
nul) au lieu de « sonde orientée » (sonde Q2) : **une reprise du pilote** au lieu de l'arrêt « non interprétable »
de la liste d'arrêt (texte l. 366). Couvert comme pour la relance : la reprise rejoue sa propre garde au tour 0, et
`valider` lit « sonde orientée » dans **toute** issue du pilote (l. 392) ; si la reprise la passe, le run principal
est lancé, ce que le texte exclut. Même classe que le risque déjà déclaré, même probabilité (coupure de l'hôte au
milieu de l'écriture de cette ligne) : à ajouter au risque déclaré de la lecture 36, pour que Lazar l'acte avec elle :
« … `relance_permise` **et `issue_pilote`** ne le voient pas : une relance reste permise sous 20 tours complets, **et
une reprise du pilote est faite au lieu de l'arrêt** ». Option de code, facultative : `_garde` écrit avec
`sort_keys=True`, la ligne commence par `{"etat": "tombée", "garde": "<nom>"` ; un préfixe coupé qui contient
`"etat": "tombée"` et le nom entier pourrait nommer la garde (sonde Q2 : le préfixe contient « sonde orientée »).
Je ne l'exige pas : cela ajoute une lecture de JSON partiel à écrire et à éprouver, pour un cas rare déjà déclaré.

## 4. Corrections exactes

Aucune exigée. Facultative : A-1, une ligne dans `lecture_v7.tours_journal` et l'attendu de l'essai `test_C3_…`
cas « lanceur » (K′ = 0). À préciser à l'addendum et à la lecture 36 de la liste : A-1 (formulation de (d) pour les
gardes du lanceur, si le code reste tel quel) et A-2 (pilote dans le risque déclaré).

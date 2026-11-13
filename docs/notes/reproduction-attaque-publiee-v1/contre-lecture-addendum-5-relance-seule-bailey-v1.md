# Contre-lecture (R2) — addendum 5 au préenregistrement du témoin de Bailey (relance seule), brouillon 2

**Verdict : scellable après corrections.** Aucun constat bloquant. Quatre corrections sont à faire avant le scellement
(K-1, K-2, K-5, K-6). Les autres constats sont des précisions ou des remarques.

Sur le fond, l'addendum tient :
- l'écart est nommé : la relance est jouée par une conduite neuve, sur une instance neuve ;
- il est rattaché à la décision de Lazar (`357f18b9…`) ;
- il ne change ni l'hypothèse, ni un seuil, ni une métrique, ni la graine, ni B, ni la règle du nombre de tours ;
- il ne contient aucun résultat ;
- la relance calculée est celle de la ligne 371 du texte : relance entière, même graine, dossiers neufs, K recalculé
  par la même règle (même B, D du poste, c de l'instance en cours, t du pilote) ;
- les gardes d'entrée passent sur les valeurs réelles (vérifié ici).

Les défauts sont ailleurs :
- **le mot de lancement** : on ne sait pas à quel texte renvoie l'option « (a ») ;
- **le crédit Vast** : le seuil est sous-dimensionné, et le compte est partagé avec d'autres chantiers ;
- **la v20 du code** : son dernier écart (de la v19 à la v20) n'avait pas été contre-lu avant cette lecture ;
- **les empreintes manquantes** (R6).

Contre-lecteur neuf : auteur d'aucun des fichiers relus. 13 novembre 2026.

Cloisons tenues :
- aucun fichier `notes-v3.jsonl` ni `technique-v3.jsonl` ouvert ;
- rien lu sous `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/` ou
  `docs/notes/programme-et-4-familles-evasion/` ;
- ni `registres/etat.md` ni `registres/decisions.md` lus ;
- aucun résultat ni seuil de sonde ou de moniteur lu ;
- aucune commande réseau, aucune variable de secrets, aucun fichier existant modifié.

Du dossier de la reprise, seuls ont été lus :
- `bilan-reprise-v10.json` ;
- `manifeste-v3-regle.json` : clés et `regle_tours` ;
- `sortie-durees-v3.jsonl` : champs `tour` et `duree_s` ;
- les champs `garde` et `etat` des deux journaux de gardes du principal.

Hors de la liste fournie, j'ai lu seulement les noms de fichiers du dossier (`find`), `sortie-conduite-v11/poste-v5.json`
(dates et taux des instances), et la ligne de `GO-2026-11-10-10` sur `origin/main` (sans lire les seuils de l'autre
chantier).

## Objets relus et empreintes vérifiées (`sha256sum`, compagnons `.sha256`, `scellement verifier`)

| Objet | Empreinte | Constat |
|---|---|---|
| Brouillon 2 (`brouillons/…-addendum-5-relance-seule-brouillon2.md`) | `c20927ba…` | relu (commit `7b54d985`) |
| Brouillon 1 | `600dd0a9…` | égal à la citation |
| Préenregistrement | `fb6c2f34…` | OK ; l. 338 et 371 sont bien la ligne « interruption au tour e₀ » et la relance |
| Addenda 1 à 4 | `6f7eda73…`, `f79459c7…`, `4b1f33bf…`, `89d2f647…` | OK |
| Notes 0548, 0610, 0731, 0747, 0803, 0821 | `b797cb97…`, `01ff293b…`, `f6e09ff5…`, `cc6aba57…`, `ab372ed1…`, `357f18b9…` | OK ; les citations du brouillon sont exactes |
| `lanceur_v20.py` | `0a546919…` | égal à la version du commit `f60c2620`, et à la citation |
| `lanceur_v18.py`, `lanceur_v19.py` | `5302c346…`, `1fa00722…` | égal |
| `tests/test_temoin_bailey_condition6_v20.py` | `a19611a9…` | égal |
| `lancer-conduite-v13.py` | `db950a6d…` | égal |
| `poste-hetzner-v12.sh` | `0990ff20…` | égal |
| `construire-donnees-demarrage-v12.py` | `233793c7…` | égal ; imprime bien l'empreinte du script sans secrets (l. 53-54) |
| `manifeste-local-v6.json` | `5e62c0d8…` | égal ; `diff` avec la v5 (`111c6e98…`) : seul `commit_code` change (`8d1c541e` → `f60c2620`) |
| `lancer-conduite-v12.py` | `684eb5ef…` | égal |
| Relectures du code v18 et v19 | `cd540827…`, `8fa2fdc5…` | égal |
| Reprise : bilan, manifeste de la règle, durées, gardes, gardes du lanceur | `085f5c1c…`, `2e8b7837…`, `9ff59e4b…`, `4acfddd3…`, `bc474c4d…` | scellés OK ; les trois journaux sont égaux aux `empreintes_instance` du bilan de la reprise |

Commits :
- `f60c2620a3891ebe579a807b2a90afb06e9e3ea5` existe ;
- `git diff f60c2620 HEAD -- src/` est vide (la tête `7b54d985` égale `origin/claude/compassionate-meitner-d4ryyk` dans
  la copie locale) ;
- `git diff --stat 8d1c541e f60c2620 -- src/` ajoute seulement `lanceur_v18`, `lanceur_v19`, `lanceur_v20` et leurs
  compagnons. « Seul change… `lanceur_v20` » est donc exact, et l'archive envoyée sur l'instance est la même ;
- `CHEMINS_ARCHIVE` n'a pas changé de la v17 à la v20 ;
- le dossier `reprise-v10-2/` est suivi par git (55 fichiers), donc présent dans le clone du poste.

## Vérifications faites

1. **Différence de la v17 à la v20** (`diff lanceur_v17.py lanceur_v20.py`). Elle contient seulement :
   - la docstring ;
   - les imports `math` et `shutil` ;
   - `VEILLEUR_MODULE` et deux chaînes qui nomment le module ;
   - le champ `relance_seule` ;
   - l'appel des gardes d'entrée, avant le dossier de sortie, l'archive, le poste et `creer` ;
   - le branchement après le contrôle du juge ;
   - `_relance_seule`, `CLES_REGLE`, `verifier_relance_seule`, `_fichiers_scelles` et `assembler_lecture`.

   Le chemin de la conduite scellée n'est pas touché. La différence de la v19 à la v20 se limite aux corrections
   annoncées (R-1, R-3, R-6, R-7, R-8).

2. **Fidélité de la relance au texte et à la v17.** La relance de la v17 est aux l. 1717-1726 de `lanceur_v17.py` (`if
   relance_permise(principal):` … `principal-relance`). La v20 fait le même calcul :
   - `self.poste.depense(self.horloge())` arrondi à 4 décimales, `self.b`, `self.c` ;
   - le t de la première règle ;
   - même arrêt si K < 20 ;
   - même manifeste « relance » (`relance: true`, `premiere_execution`) ;
   - même phase et même graine (`instance_v16`, `PHASES`).

   Elle diffère sur deux points, conformes au texte (l. 249-261) :
   - **c** est le taux de l'instance en cours, ici l'instance neuve (« c : taux réel de l'instance en cours ») ;
   - **H** est recalculé, alors que la v17 gardait celui de la première.

   **D** compte toutes les instances du poste depuis la première (`Poste.depense`, l. 701-704), conformément à la
   l. 253. **t** est celui du pilote, conformément aux l. 255 et 371. Les choix de D et de c sont donc fidèles.

3. **Conduite v13, appel à vide.** Appelée depuis un autre dossier, sans `GO_ID` : « GO_ID ou DEPOT_URL absent ou
   différent : rien ne tourne », code 2. Aucun fichier PID, bilan ou sortie n'est créé.

4. **Valeurs réelles.** `relance_seule()` de la v13, chargée par `runpy`, rend :
   - K′ = 8 ;
   - la règle B = 75, R = 10, D = 5,0331, c = 1,342111…, t = 1 315,9926, H = 44,68, K = 72 ;
   - `instance_premiere` = « 60417353 » ;
   - le manifeste en chemin absolu ;
   - `gardes_tombees_premiere` = [].

   `lanceur_v20.verifier_relance_seule(…, instances_du_poste(ANTERIEURES, 75), 75)` **passe**. Deux artefacts sont
   refusés : K′ = 20, et une garde « dépense » tombée.

   Grandeurs relevées :
   - dépense des sept antérieures : 14,4398 USD ;
   - borne de la garde : 5,0331 + 1,342111 × 8 × 1 315,9926 / 3 600 = 8,9580 USD ;
   - K par la règle avec D = 14,44 et c = 1,3421 : 72 (H = 37,67 h).

   Les `ANTERIEURES` de la v13 sont égales à celles de la v12, aux six de la v11 (`d279ea19…`) plus 60417353, et à
   `sortie-conduite-v11/poste-v5.json`. La destruction de 60417353 (1794556404,244174) est celle du bilan de la reprise.

5. **K′ = 8.** Le journal des durées a 8 lignes, tours 0 à 7, de 1 299,48 à 1 586,18 s. Journaux de gardes du principal :
   - 43 lignes, toutes « passée » : dépense ×17, par tour ×8, appariement ×8, suffixe appris ×8, sonde orientée ×1,
     juge ×1 ;
   - la dernière ligne finit par un saut de ligne, donc aucune ligne n'est coupée ;
   - `gardes-lanceur-v3.jsonl` : « configuration effective » passée.

6. **Poste v12.** `diff` avec le v11 : seuls changent les noms v13 et v12, la garde du commit (`f60c2620`) et le nom du
   serveur. Le filtre d'offre est identique. Constructeur v12 : seuls changent le script et le nom.

7. **Essais.** `pytest -q -p no:cacheprovider tests/test_temoin_bailey_condition6_v20.py -k test_v20_` :
   **52 passés, 169 désélectionnés, aucun sauté, en 219 s** (52 essais sélectionnés sur 221). Le fichier contient 221 essais, ce qui est cohérent avec
   « 220 passés, 1 sauté ». Je n'ai pas rejoué les 169 essais de la v17.

## Constats

| N° | Gravité | Ligne du brouillon | Constat et preuve | Correction proposée |
|---|---|---|---|---|
| K-1 | **à corriger** | l. 24-25, 123-124 (condition 7) | **L'option « (a) » n'est définie dans aucune pièce citée.** La note 0803 (`ab372ed1…`), à laquelle Lazar répond, ne porte aucune option étiquetée : seulement « Recommandation : relance, après crédit d'au moins 50 USD ». Les seules options (a) et (b) écrites sont celles de la note 0731 (`f6e09ff5…`) : « (a) Lazar crédite le compte, puis la session relance la reprise (…), puis la relance est décidée sur K′ mesuré ». Lue à la lettre, elle ne lance rien. La note 0821 (« Mot exprès de lancement : ce « go (a) », pour la seule relance ») est une glose de la session. De plus, le mot dit « vérifie le chemin de code » : le code ne permettait pas la relance telle quelle, d'où cet addendum. Précédent : la contre-lecture de l'addendum 4 (K-3) recommandait déjà un mot exprès. | Au choix. **(i)** Citer mot pour mot le message qui définissait (a), avec chemin et empreinte de la note qui le consigne. **(ii) Recommandé** : remplacer la condition 7 par « 7 : le mot direct de Lazar pour le lancement de la relance, demandé après le scellement de cet addendum et le relevé du crédit (condition 9) ; le « go (a), vérifie le chemin de code de la relance » (`357f18b9…`) engage l'addendum et le code, pas la création de l'instance ». Le crédit doit de toute façon être demandé à Lazar : le même message peut porter la demande de mot. |
| K-2 | **à corriger** | l. 111-113 (risque (a)), l. 125-127 | **Le seuil de crédit est vague et trop bas, et le compte est partagé.** (i) « ≈ 26 h » vaut 72 × t. Or les tours 0 à 7 de la première exécution ont duré en moyenne ≈ 1 411,5 s (journal des durées), d'où ≈ 28,2 h et ≈ 37,9 USD au taux de 60417353. Avec la marge de la règle (1,15), on arrive à ≈ 30,3 h et ≈ 40,6 USD. Et les tours s'allongent (texte l. 263-264). (ii) La garde de dépense laisse courir la relance jusqu'à D ≥ B − 2, et le chien jusqu'à B − 0,5. La dépense permise de la relance va donc jusqu'à ≈ 73 − 14,44 ≈ 58,6 USD (compte prudent). Tout crédit en dessous fait passer la coupure par le crédit **avant** la garde de dépense : une issue « run tronqué, lu sur K′ ≥ 20 » devient une seconde erreur avant 20 tours, ou un run tronqué plus court. (iii) Le compte Vast sert aussi d'autres chantiers (note 0731 : 60432755 « p3bis-v1 » sur carte, stockages 58936096/99/100). C'est la cause même de la première interruption, et elle n'est pas dite. (iv) Aucun relevé du crédit n'est prévu pendant le run. Le poste v12 ne relève pas le crédit, et il peut attendre une offre jusqu'à 24 h après le relevé de la session. (v) « Une relance coupée faute de crédit est une seconde erreur » ne vaut qu'avant 20 tours complets. Après, la ligne 372 du texte s'applique : run tronqué. | Réécrire le risque (a) : « (a) **crédit du compte Vast**, partagé avec d'autres chantiers (note 0731) : une coupure faute de crédit avant 20 tours complets de la relance est une seconde erreur (arrêt, pas de verdict, nœud) ; après 20 tours, un run tronqué (l. 372). La garde de dépense (D ≥ B − 2) ne protège pas d'un compte vide. Dépense permise de la relance : jusqu'à B − 0,5 − D, soit ≈ 60 USD au compte prudent ; durée attendue ≈ 28 à 32 h (72 tours, durées de la première exécution, marge 1,15). » Ajouter une condition 9 : « crédit relevé (champs `credit` et `balance`, heure, consignés dans l'ordre de lancement) au plus tard une heure avant la création, au moins égal à B − 0,5 − D du poste au relevé, plus la consommation prévue des autres instances du compte pendant 45 h ; sinon aucune création. Si le poste attend une offre plus d'une heure, le crédit est relevé de nouveau avant la création. » Retirer « ≈ 40 USD attendus (…), plus une marge ». Si Lazar préfère un seuil plus bas, c'est sa décision, déclarée comme risque accepté. |
| K-3 | à préciser | l. 12-14, 21 | **Le classement de l'interruption n'est pas écrit.** « Vast a arrêté l'instance » est présenté comme établi. La note 0731 dit : « cause la plus probable ». La ligne 371 énumère « mémoire de carte, mémoire vive, valeur non finie, coupure de l'hôte ». Un arrêt par le fournisseur faute de crédit n'y figure pas en toutes lettres. La ligne 338 couvre « le run s'interrompt pendant le tour e₀ ». | Après « Vast a arrêté l'instance », écrire : « (cause la plus probable, note 0731 ; non établie autrement) ». Au § 1, deuxième alinéa : « Classement : interruption pendant le tour e₀ = 8 (l. 338), lue comme une coupure de l'hôte (l. 371 : instance arrêtée par le fournisseur, processus tué) ; lecture de la session, présentée à Lazar (notes 0548, 0803) et couverte par sa décision ; à la lecture, l'état absent est reconstitué avec un code de sortie non nul (`lecture_v8.etat_reconstitue_lecture`), ce qui permet la relance (`relance_permise`). » |
| K-4 | à préciser | § 2.1, § 4, § 5 (b) | **Rien n'est dit des arrêts avant le lancement de `principal-relance`** sur l'instance neuve : création incertaine, amorce non finie, auto-arrêt indisponible, garde de mise en place tombée, garde du juge tombée, contrôle du juge hors seuil, aucune offre en 24 h. Le texte prévoit : mise en place tombée → « peut être refaite » (l. 363) ; contrôle hors seuil → « nœud ; aucun nouveau contrôle sans version nouvelle » (l. 365). L'addendum ne dit pas si ces arrêts consomment « la » relance. | Ajouter au § 4 : « Un arrêt avant le lancement de `principal-relance` n'est pas une seconde erreur : la relance n'a pas commencé. Mise en place tombée : refaite selon le texte (l. 363), par une conduite et un poste neufs (R12), sur un nouveau mot de Lazar, sans nouvel addendum si le code ne change pas. Contrôle du juge hors seuil : nœud, aucun nouveau contrôle sans version nouvelle du texte (l. 365) ; la première exécution reste rapportée comme interrompue ; pas de verdict. » |
| K-5 | **à corriger** | l. 30, 94-97 | **La différence de la v19 à la v20 n'avait pas été contre-lue.** La relecture v18 a produit la v19, la relecture v19 a produit la v20. Les corrections R-1, R-3, R-6, R-7 et R-8 changent du code exécuté : les gardes d'entrée et l'assemblage. Aucun relecteur neuf ne les avait lues avant cette contre-lecture. Or la condition 6 exige un code « contre-lu ». J'ai lu ici `diff lanceur_v19.py lanceur_v20.py` et `diff lanceur_v17.py lanceur_v20.py` : rien d'autre que ce qui est annoncé, et la garde d'entrée passe sur les valeurs réelles. De même, la conduite v13, hors du commit (C-10 de la relecture v18), n'avait été contre-lue par personne : elle l'est ici. | Au § 3, après la liste des relectures : « La différence de la v19 à la v20 (R-1, R-3, R-6, R-7, R-8) et la conduite v13 sont lues par la contre-lecture de cet addendum (rapport cité en fin de texte) : conformes, sous K-7 et K-8. » |
| K-6 | **à corriger (R6)** | l. 18-19, 34-36, 47-50, 126, 92 | **Empreintes et sources manquantes.** (i) Notes 0548 et 0610 citées sans empreinte : `b797cb97…`, `01ff293b…`. (ii) t = 1 315,9926 s et la règle de la première sont cités sans l'empreinte du manifeste de la règle : `2e8b7837dc49ebb60b36781541c2ada6147f06694c18e2e525783d2ccbe6360a`. (iii) K′ = 8 est cité sans l'empreinte du journal des durées : `9ff59e4beb8e8d4461bff18e157751f9464f6022d95b04b0b88904eccdb671f4`. Les journaux de gardes manquent aussi : `4acfddd3877d87944cf5d9eef7f2be96e5ec932da6efdbecf757d8a8ccb771bf` et `bc474c4d4846dfe58c505a110d271b402db1eaa29ba4a13f24c68aabee71f748`. Le bilan de la reprise manque : `085f5c1c78e97188a95686a903939d37217fd803bda6c07ad82ffde43a408cff`. (iv) « à 08:52Z, 28,72 USD » : aucune pièce. (v) « En v18, un mutant (t divisé par deux) faisait tomber les essais visés » : aucune pièce. Ce point ne figure ni dans les deux relectures ni dans les messages de commit. | Ajouter les empreintes (i) à (iii). Pour (iv), citer la note ou le journal du relevé, ou écrire « relevé de la session, non consigné ». Pour (v), citer la pièce (chemin, empreinte) ou retirer la phrase. |
| K-7 | à préciser | l. 83, 91 | **Deux défauts dans les essais.** (a) `test_v20_valeurs_reelles_du_script_de_relance` (l. 4192-4206) charge **`lancer-conduite-v12.py`**, pas la v13. Il passe `gardes_tombees_premiere: []` écrit à la main et un D fixe de 15,0. Il n'appelle pas `relance_seule()` de la v13 et ne lit aucun journal de gardes. C'est sans effet : les `ANTERIEURES` des deux versions sont égales, et l'appel réel de la v13 passe (vérification 4). (b) `test_v20_modules` est défini deux fois (l. 4141 et l. 4255). La seconde définition masque la première, donc ses assertions sur `INSTANCE_MODULE` (`instance_v16`) et `CHEMINS_ARCHIVE` (`execution_v4.py`) ne tournent jamais. Vérifiées à la main ici : vraies. | Écrire au § 3 : « l'essai des valeurs réelles lit la conduite v12, dont les instances antérieures sont égales à celles de la v13 ; la v13 (`relance_seule()`, journaux de gardes compris) est vérifiée par la contre-lecture de l'addendum » ; et « `test_v20_modules` est défini deux fois ; la première définition ne tourne pas (vérifiée à la main) ». Corriger dans un fichier d'essais v21 si le code est repris. Pas de reprise exigée pour ce lancement. |
| K-8 | remarque | l. 99-100 (pièces) | **Conduite v13.** (a) Le docstring, l. 72-74, décrit encore `lanceur_v13`, le commit `4988f3f4` et `bilan-lancement-v2.json`. C-10 (v18) et R-2, point 3 (v19) ne sont donc corrigés qu'en tête. (b) `scellement.verifier` compare chaque fichier de la reprise à son compagnon, pas à une empreinte fixée. Un fichier réécrit avec son compagnon passerait. Les empreintes fixées dans l'addendum (K-6) referment ce point à la lecture. (c) Le PID est écrit avant `relance_seule()` : un refus à ce stade laisse un PID qui bloque une nouvelle exécution sous le même nom (R-2, point 5). Il n'y a aucune dépense. | Déclarer (a) à (c) en une phrase au § 3, ou corriger dans une conduite v14 (R12) si une autre pièce change. |
| K-9 | remarque | l. 119-120 (risque (e)) | Le risque (e) est couvert dans le cas réel. La dernière ligne de `gardes-v3.jsonl` est complète (saut de ligne final, 43 lignes lues). Une ligne coupée ferait échouer `json.loads` dans `relance_seule()` avant toute création, donc sans dépense. | Ajouter : « dans le cas réel, aucune ligne coupée (dernière ligne complète) ; une ligne coupée ferait refuser le script avant toute création ». |
| K-10 | remarque | l. 39-40 | « l. 1716-1726 » : le bloc de la relance va de la l. 1717 à la l. 1726. La v17 garde aussi le c et le H de la première (même instance). La v20 écrit le c de l'instance neuve et le H recalculé (C-3). | « (l. 1717-1726 : …), avec le c de l'instance neuve et H recalculé (C-3 de la relecture v18) ». |
| K-11 | remarque | § 2.3, § 5 (d) | L'égalité de la mise en place de la relance avec celle de la première n'est vérifiée qu'à l'assemblage, donc après la dépense de la relance. Une différence donnerait une relance payée et non lue. Le risque est faible : ces valeurs viennent de la configuration publique, du tokeniseur et du jeu, sous les gardes de mise en place (`instance_v16.py`, l. 578-586). | Compléter le risque (d) : « l'égalité de la mise en place n'est contrôlée qu'à l'assemblage, après la dépense ; risque faible (valeurs déterministes) ». |

## Réponses aux questions posées

1. **Écart, rattachement, R3, fidélité.**
   - L'écart est nommé et rattaché au mot de Lazar. Le texte de ce mot reste à préciser : voir K-1.
   - Il est compatible avec R3 : la relance est celle du texte, aucune note n'a été lue (seuls des champs techniques), et
     la graine et la règle sont celles du texte.
   - « Entière, même graine, dossiers neufs, K recalculé par la même règle sur le budget restant (même B, t du pilote) » :
     exact. Le pilote n'est pas rejoué, comme le veut la l. 371 (t du pilote) ; risque (c).
   - D et c : fidèles au texte et à la v17 (vérification 2).
2. **Code, empreintes, commits, essais, pièces, K′.**
   - Code, empreintes et commits : exacts.
   - Essais : 52 passés sur 52 sélectionnés ; sous K-7.
   - Pièces de lancement : exactes ; sous K-8.
   - K′ = 8 : exact.
   - Les sources manquent : voir K-6.
3. **Risques.**
   - Le crédit est mal dimensionné, et le partage du compte n'est pas dit : K-2.
   - Il manque les arrêts avant la relance (K-4) et le contrôle tardif de la mise en place (K-11).
   - Le risque (e) peut être resserré (K-9).
   - Pilote non rejoué, assemblage, gardes tombées : honnêtes.
4. **Conditions de lancement.**
   - Le mot de lancement est ambigu : K-1.
   - Le crédit n'est pas chiffré, ni relevé au moment de la création : K-2.
   - Les conditions 1 à 6 et 8 sont cohérentes. GO-2026-11-10-10 (échéance au 30 novembre) est présent sur `origin/main`,
     l. 300.
5. **Aucun résultat**, aucune modification d'hypothèse, de seuil ou de métrique. Les chiffres non sourcés sont nommés en
   K-6 (iv) et (v).

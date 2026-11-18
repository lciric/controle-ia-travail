# Contre-lecture (R2) du générateur de la relance de la confirmation de Bailey — v1

Workflow `contre-lecture-relance-confirmation-bailey`, run `wf_04d0b7e1-6f5`, deux contre-lecteurs neufs, sur le commit `17ec9884`
(`generer-pieces-relance-confirmation-bailey-v1.py`, pièces produites avec des valeurs factices). Retours consignés tels quels.
Traitement : générateur v2 (`generer-pieces-relance-confirmation-bailey-v2.py`), contre-lu à son tour.

## Retour 1 — verdict : prêt après corrections

J'ai lancé le générateur (commit 17ec9884) avec les valeurs factices dans /tmp. Il rend « ok » et ses trois pièces. J'ai ensuite comparé chaque pièce à sa base, puis essayé `relance_seule()` et `verifier_relance_seule` de la v16 sur un faux dossier de reprise (essai dans /tmp, nettoyé ; dépôt intact, aucune commande réseau).

**Différences, une par une :**
- **Conduite v15 → v16.** Les gardes d'entrée de la v15 restent (addendum 7 scellé `554a74d0…`, ligne de GO, manifeste v7 avec B = 85, plafond de 1 800 s). S'y ajoutent `relance_seule()` et une instance antérieure unique, 61049303. Les noms de sortie, de bilan et de PID sont neufs.
- **Relance seule v13 → v16.** Le corps est identique à celui de la v13 ; seuls changent l'identifiant de l'instance (61049303) et le dossier de reprise. C'est conforme à l'addendum 5, § 2.2, et à l'addendum 7, § 2.1 et 2.2 (même poste de dépense, D cumulée, même B).
- **Poste v13 → v14.** Seuls les noms changent ; l'en-tête ajouté ne dit rien d'autre. Le filtre d'offre, la garde du commit a904aa39, la garde d'inventaire R10, le GO et le manifeste v7 sont inchangés.
- **Constructeur v13 → v14.** Seuls changent le nom du script, du serveur et de l'étiquette.

**Noms et listes :**
- Les 10 noms neufs ne sont ni suivis par git ni présents sur disque.
- La liste des répertoires porte le nom exigé par le § 3 : `repertoires-sortie-conduite-v16-v1.txt`. Elle est écrite par la commande fixée, scellée sous la même forme, poussée avant la marque de fin.
- L'arbre `src/` de la tête est identique à a904aa39.

**Instance antérieure.** Son taux (c = 1.3247777777777778) et sa création (1794907209.2755258) sont conformes à `sortie-conduite-v15/poste-v5.json`. Sa destruction y vaut encore `null`. La reprise l'écrira à deux endroits :
- dans `sortie-conduite-v15/poste-v5.json`, champ `instances[id=61049303].destruction`, par `Reprise._ecrire_destruction_poste` puis `Poste.detruite` ;
- dans `reprise-v10*/bilan-reprise-v10.json` (scellé), champ `destruction`.

C'est la même valeur (l'heure qui suit la destruction réussie), sauf si l'écriture du poste échoue ou si un veilleur a déjà inscrit une destruction.

**Essai sur le faux dossier.** Avec 16 lignes de durées et le vrai manifeste de la règle, la relance seule passe. Elle refuse un mauvais K′. Une destruction à 6 h de la création est refusée par la borne R-1 ; à 7 h, elle passe.

**Un point bloquant.** La destruction passée en argument n'est vérifiée par personne contre ce qu'écrit la reprise. Une valeur trop précoce, mais au-delà de la borne R-1 (environ 7 h après la création), sous-compte D. La garde B − 2 laisserait alors dépenser au-delà de B = 85, et jusqu'au-delà des 90 USD de GO-2026-11-17-07. La contre-lecture présente ne peut pas couvrir cette valeur, qui n'est pas encore connue.

Le reste se corrige ou se déclare sans changer la conduite des runs.

### 1. bloquant — docs/notes/reproduction-attaque-publiee-v1/generer-pieces-relance-confirmation-bailey-v1.py 19-21, 50-51

**Constat.** La destruction de 61049303 (argv[7]) est écrite telle quelle dans ANTERIEURES. Personne ne la compare à ce qu'écrit la reprise : ni le générateur, ni la conduite v16. Les seules gardes sont `destr > création` (générateur) et la borne R-1 de `verifier_relance_seule`, soit au moins D de la première règle plus c × K′ × t / 3 600, environ 7 h après la création (essai : 6 h refusé, 7 h passe). Une valeur erronée entre cette borne et la vraie destruction (17 novembre 09:20Z, puis la reprise) sous-compte D d'environ 1,32 USD par heure. La garde B − 2 laisserait alors dépenser au-delà de B = 85 et du plafond de 90 USD de GO-2026-11-17-07. C'est une voie de dépense hors GO, et la présente contre-lecture ne peut pas couvrir la valeur réelle.

**Correction proposée.** Dans le générateur, ne plus prendre la destruction en argument : la lire, ou au moins l'exiger égale. Après `base = ...`, ajouter : `pv = json.loads((base / "sortie-conduite-v15" / "poste-v5.json").read_text()); i1 = [i for i in pv["instances"] if str(i["id"]) == "61049303"]; assert len(pv["instances"]) == 1 and len(i1) == 1 and i1[0]["c"] == 1.3247777777777778 and i1[0]["creation"] == 1794907209.2755258 and i1[0]["destruction"] is not None and float(i1[0]["destruction"]) == destr and float(pv["b"]) == 85.0`. Faire de même avec le compagnon scellé : `scellement.verifier(base/"sortie-conduite-v15"/reprise/"bilan-reprise-v10.json")`, puis `json.loads(...)["destruction"] == destr` et `["detruite"] is True` (champs techniques seulement). Ajouter `import json` et `from controle_ia import scellement` (PYTHONPATH=src). Consigner les deux empreintes dans l'ordre de lancement.

### 2. à corriger — docs/notes/reproduction-attaque-publiee-v1/generer-pieces-relance-confirmation-bailey-v1.py 19-20, 26-43

**Constat.** Les arguments `<empreinte addendum 7>` et `<commit du code>` sont validés dans leur forme puis ignorés. `go_id` ne sert qu'à la docstring. La v16 garde les constantes de la v15 (GO_ID, EMPREINTE_ADDENDUM_7 = 554a74d0…, COMMIT_CODE = a904aa39). Si l'on passe d'autres valeurs, la docstring dit une chose et le code en vérifie une autre, sans aucune erreur.

**Correction proposée.** Après la lecture de c15, ajouter : `assert f'GO_ID = "{go_id}"' in c15 and f'EMPREINTE_ADDENDUM_7 = "{emp}"' in c15 and f'COMMIT_CODE = "{commit}"  # addendum 7, § 4' in c15`. Ou bien retirer ces trois arguments de l'usage.

### 3. à corriger — runs/temoin-bailey-v1-20261111/lancer-conduite-v16.py (généré) 48-62

**Constat.** `relance_seule()` vérifie le manifeste de la règle, le journal des durées et les journaux de gardes de la reprise contre leurs seuls compagnons. Pour la v13, l'addendum 5 (§ 1 et K-8) fixait leurs empreintes, ce qui refermait ce point. Pour la v16, aucun addendum neuf ne les fixe (§ 2.1 : « sans nouvel addendum »). Une altération accompagnée de son compagnon n'est donc pas détectée avant la création.

**Correction proposée.** Faire passer au générateur les empreintes de ces quatre fichiers, relevées après la reprise : `manifeste-v3-regle.json`, `principal/transfert-1/sortie-durees-v3.jsonl`, `principal/transfert-1/journal/gardes-v3.jsonl` et `principal/transfert-1/gardes-lanceur-v3.jsonl`. Les écrire dans la v16 dans un dictionnaire `ATTENDUES = {chemin relatif: empreinte}`. Dans `relance_seule()`, après chaque `scellement.verifier(f)`, ajouter `if cv.sha_fichier(f) != ATTENDUES[...]: raise SystemExit(...)`. Exiger aussi que `manifeste-v3-regle.json` de la reprise soit égal, octet pour octet, à `sortie-conduite-v15/manifeste-v3-regle.json` (déjà sur la branche). Citer ces empreintes dans la demande du mot de Lazar.

### 4. à corriger — runs/temoin-bailey-v1-20261111/lancer-conduite-v16.py (généré) 51, 60-61

**Constat.** Le chemin `principal/transfert-1` est figé, repris de la v13. Si la reprise ne fait foi que sur `transfert-2` (`rapatrier_etapes` ne scelle que l'essai qui fait foi), les fichiers de `transfert-1` n'ont pas de compagnon. `scellement.verifier` lève alors une erreur : la relance ne part pas. C'est sans dépense (avant la création), mais une pièce neuve serait à refaire.

**Correction proposée.** Dans le générateur, prendre en argument le transfert qui fait foi pour `principal`, lu dans `bilan-reprise-v10.json` (champ technique `transferts.principal.foi`). L'exiger égal à `transfert-1` ou `transfert-2` et le substituer dans les trois chemins. Ou bien affirmer `foi == "transfert-1"` à la génération.

### 5. à corriger — runs/temoin-bailey-v1-20261111/poste-hetzner-v14.sh (généré) 122-133

**Constat.** Rien n'exige que la reprise soit finie et poussée avant la recherche d'offre. À sa place, le poste de reprise v4 exigeait la marque `poste-fini-v13.json`. La garde d'inventaire (aucune instance `temoin-bailey-c6-*`) couvre la destruction de 61049303. En revanche, un dossier de reprise encore partiel sur la branche ne fait tomber `relance_seule()` qu'après le choix de l'offre, sans dépense mais avec une pièce perdue (PID écrit, R12).

**Correction proposée.** Dans la boucle du générateur sur le poste, après la ligne `[ -n "${VAST_API_KEY:-}" ] ...`, insérer `[ -s "$BASE/poste-fini-reprise-v4.json" ] || { etat "reprise de la confirmation non finie (poste-fini-reprise-v4.json absent) : rien ne tourne"; pousser "reprise non finie"; exit 3; }` et nommer cet ajout dans l'en-tête de la v14. C'est permis : le § 2.1 ne restreint pas les différences de la relance comme le § 2.3 le fait pour la seconde tentative. Le déclarer à la contre-lecture.

### 6. remarque — docs/notes/reproduction-attaque-publiee-v1/generer-pieces-relance-confirmation-bailey-v1.py 101

**Constat.** L'assertion `re.search(...) is None or "manifeste-local-v7" in b` est toujours vraie, puisque le corps contient `manifeste-local-v7`. Elle ne garde rien. Aujourd'hui, les seules mentions de v13 qui restent dans le corps sont des commentaires (l. 58, 141, 152, 181 de la v14), mais rien ne le vérifie.

**Correction proposée.** Remplacer par `assert re.search(r"v15|offre-choisie-v13|poste-fini-v13|lancement-v15|poste-hetzner-v13", "\n".join(l for l in b.splitlines() if not l.lstrip().startswith("#"))) is None`. Ajouter aussi `assert p.startswith(h)` avant `p[len(h):]` (l. 94).

### 7. remarque — runs/temoin-bailey-v1-20261111/lancer-conduite-v16.py (généré) 8-10, 115-125

**Constat.** La docstring range les gardes de la relance parmi les « gardes d'entrée ». Or `relance_seule()` tourne après l'écriture de `lancement-v16.pid`, comme dans la v13 (déclaré K-8 à l'addendum 5). Un refus à ce stade, sans dépense, bloque une nouvelle exécution sous le même nom.

**Correction proposée.** Écrire dans la docstring : « gardes de la relance jouées après l'écriture du PID, avant toute création (comme la v13, K-8 de l'addendum 5) ». Ou bien appeler `relance_seule()` avant `pidf.write_text` et passer le dictionnaire obtenu à `Conduite`.

### 8. remarque — runs/temoin-bailey-v1-20261111/poste-hetzner-v14.sh (généré) 40-50, 135, 145

**Constat.** Le bloc « Ce qu'il fait » est hérité de la v13 sans changement : il cite `lancer-conduite-v13.py`, GO-2026-11-10-10 et 200 Go, ainsi que la clé `cout_avec_200_go` pour un coût calculé sur 110 Go. Ce sont des commentaires et des étiquettes, sans effet sur l'exécution, déjà présents dans le poste v13 contre-lu.

**Correction proposée.** Laisser tel quel (R12, différences minimales), mais le déclarer dans l'en-tête de la v14 : « commentaires d'origine non mis à jour ».

### 9. remarque — src/controle_ia/temoin_bailey/lanceur_v21.py 709-717, 1813-1818

**Constat.** D compte 61049303 au taux de marche (1,3248 USD/h) de sa création (17 novembre, 09:20Z) jusqu'à la destruction par la reprise, y compris les heures où l'instance était arrêtée par Vast (stockage seul). C'est prudent pour la dépense : D réel est inférieur. Mais chaque heure avant la reprise retire environ 1,32 USD du budget de la relance. Avec t = 1 265 s (règle de la première), K reste à 72 jusqu'à D ≈ 30 USD à c = 1,6 USD/h, puis tombe à 69. La marge B − 2 diminue d'autant. L'échéance du 30 novembre exige aussi une création au plus tard vers 76,8 h avant elle, à 1,1 USD/h (`verifier_echeance` sur B entier).

**Correction proposée.** Aucune pièce à changer. Faire la reprise et la relance sans délai. Dans la demande du mot de lancement, rapporter D cumulé au calcul, le K attendu selon c, et le surcompte des heures d'arrêt.

## Retour 2 — verdict : prêt après corrections

Contre-lecture R2, angle exécution, du générateur au commit 17ec9884. Je l'ai joué avec les valeurs factices (K′ = 16, destruction 1794990000.0) : il sort « ok » et produit les trois pièces. La syntaxe de chacune est vérifiée (bash -n, analyse Python). Le constructeur v14 tourne sur des secrets factices : 14 103 octets, sous la limite de 32 Kio.

Différences avec les bases :
- conduite v16 = conduite v15, plus relance_seule() repris de la v13 (instance 61049303, reprise dans sortie-conduite-v15/<reprise>), avec des noms neufs ;
- poste v14 = poste v13 avec des noms neufs ;
- constructeur v14 = constructeur v13 avec des noms neufs.

Aucune différence que les addenda 5 et 7 ne permettent pas. Les noms neufs sont tous absents de l'arbre.

Reprise factice dans le bloc-notes : règle réelle copiée (B 85, D 1,6862, c 1,32478, t 1 265,02 s, K 72), durées et journaux de gardes factices, tous scellés par controle_ia.scellement. Résultats :
- relance_seule(), gardes_d_entree sur la vraie ligne GO-2026-11-17-07 (origin/main locale, déjà à jour, aucune commande réseau) et verifier_relance_seule avec ANTERIEURES passent ;
- la Conduite porte bien relance_seule et t_max_pilote_s = 1 800 ;
- conduire(), avec un fournisseur factice qui refuse la création, passe toutes les gardes du code jusqu'à creer. Les seuls appels au fournisseur sont creer puis inventaire, et le bilan est écrit dans le dossier factice ;
- _relance_seule (méthode réelle) écrit le bon manifeste « relance » et lance principal-relance ;
- échéance du GO : la création doit se faire au plus tard le 28 novembre à 06:27Z à c = 1,33 USD/h, à 17:11Z à c = 1,6. Une seconde de trop est refusée ;
- 27 cas sur 27 conformes, sains et artefacts (R5). Artefacts refusés sans création : 15 ou 17 lignes de durées, tour en double, garde « dépense » ou « sonde orientée » tombée, ligne de garde coupée, taux ou B de la règle faux, K′ = K, manifeste, durées ou gardes altérés, reprise absente, foi au transfert-2 seulement, antérieure non détruite, B = 75, destruction avant la création ou trop tôt, GO absent ou qui cite l'empreinte tronquée, script sans antérieure, plafond à 2 000 s ;
- essais v21 et complémentaires : 229 passés, 1 sauté.

Le dépôt n'est pas modifié (git status vide) et les essais sont nettoyés. Je n'ai pas joué main() : il écrit son PID dans le vrai dépôt, et le classifieur a refusé l'essai.

Résultat à remonter avant le mot de Lazar. Avec la destruction factice (18 novembre, 08:20Z), D vaut 30,47 USD : K = 72 à c = 1,33, mais K = 68 à c = 1,6, borne du filtre (§ 2.4). Une relance à 68 tours finirait avec K′ ≤ 70 et ne serait pas retenue (§ 3). En comptant 0,75 h de mise en place sur l'instance neuve, K = 72 à c = 1,6 exige que 61049303 soit détruite avant le 18 novembre vers 05:54Z (K ≥ 71 : avant 06:23Z). À c = 1,33, la limite est vers 11:59Z (12:23Z pour K ≥ 71). La raison : la reprise ne marque 61049303 comme détruite qu'au moment de la destruction, et D compte au plein taux tout l'intervalle où l'instance est arrêtée.

Aucun bloquant au sens de la consigne. La garde B − 2 tient sur la D cumulée : poste, veilleur et chien de garde comptent tous 61049303. La R10 tient : le poste v14 refuse si une instance temoin-bailey-c6- existe encore, et la conduite détruit par identifiant. Un manque à corriger : rien ne recoupe l'heure de destruction passée à la main (constat 2).

### 1. à corriger — docs/notes/reproduction-attaque-publiee-v1/generer-pieces-relance-confirmation-bailey-v1.py 21 (et 50-51 du gabarit ANTERIEURES)

**Constat.** K de la relance au taux plafond. relance_seule recalcule K = nombre_de_tours(85, D, c, 1265,0215). D compte 61049303 au plein taux jusqu'à sa destruction écrite par la reprise, intervalle arrêté compris. Avec la destruction factice (18 novembre, 08:20Z), D vaut 30,47 USD : K = 72 à c = 1,33, mais K = 68 à c = 1,6, borne du filtre du § 2.4 que reprend le poste v14. Avec 0,75 h de mise en place à c, K = 72 à c = 1,6 exige une destruction avant le 18 novembre vers 05:54Z (K ≥ 71 : 06:23Z) ; à c = 1,33 la limite est vers 11:59Z (12:23Z). Un K ≤ 70 rend la relance non retenue (§ 3 : K′ ≥ 71 exigé) : elle dépenserait environ 40 USD pour rien. Le générateur ne calcule ni n'affiche rien de cela.

**Correction proposée.** Juste avant print("ok"), ajouter : `from fractions import Fraction; D = 1.3247777777777778 * (destr - 1794907209.2755258) / 3600; t = 1265.0215` ; pour c dans (1.2576, 1.33, 1.6), afficher D, c, K = min(72, floor(72000·(75 − D − 0,75·c)/(23·c·t))) et le c maximal qui donne K ≥ 71. Porter ces valeurs dans la demande du mot de Lazar. Si K < 71 à c = 1,6, le dire comme un risque de relance non retenue. Abaisser le plafond de coût du poste serait un changement de paramètre : il relève du mot de Lazar, pas de la session.

### 2. à corriger — docs/notes/reproduction-attaque-publiee-v1/generer-pieces-relance-confirmation-bailey-v1.py 21 ; gardes_d_entree de lancer-conduite-v16.py (l. 85-98 de la pièce)

**Constat.** L'heure de destruction de 61049303 est passée à la main, et seule « destr > création » est contrôlée. La garde du code (dépense des antérieures ≥ D₁ + c·K′·t/3600) ne borne que le coût des K′ tours : avec K′ = 16, environ 9,1 USD. La destruction réelle donnera D ≈ 25 à 30 USD. Une heure trop précoce, par erreur de saisie, sous-compterait D jusqu'à environ 20 USD dans la règle, dans la garde B − 2, le veilleur et le chien de garde. Ce serait une voie de dépense au-delà de B = 85, jusqu'à environ 105 USD, au-delà du plafond du GO (90 USD). La v13 avait la même forme (acceptée par l'addendum 5), mais la valeur est désormais un argument.

**Correction proposée.** À la fin de gardes_d_entree, insérer : `b = REPRISE / "bilan-reprise-v10.json"; scellement.verifier(b); br = json.loads(b.read_text(encoding="utf-8"))` puis `if br.get("instance") != "61049303" or br.get("detruite") is not True or float(br["destruction"]) != ANTERIEURES[0]["destruction"]: raise SystemExit("destruction de 61049303 différente du bilan scellé de la reprise : rien ne tourne")`. Ajouter aussi la comparaison avec `json.loads((BASE / "sortie-conduite-v15" / "poste-v5.json").read_text())["instances"] == [{k: ANTERIEURES[0][k] for k in ("id", "c", "creation", "destruction")}]`. Champs techniques seulement. Dans le générateur, lire destr dans ce bilan plutôt que de le recevoir en argument, ou vérifier qu'ils sont égaux.

### 3. remarque — docs/notes/reproduction-attaque-publiee-v1/generer-pieces-relance-confirmation-bailey-v1.py 59, 68-69

**Constat.** relance_seule() ne lit que principal/transfert-1. Si la reprise donne foi au transfert-2 (premier essai d'empreintes différent), transfert-1 n'est pas scellé : la conduite refuse sans dépense (vérifié dans l'essai « foi au transfert-2 seulement »), mais les pièces seraient à régénérer. Cas limite K′ = 0 : sans journal des durées, le refus est le même.

**Correction proposée.** Ajouter un argument <transfert> (transfert-1 ou transfert-2), validé par `re.fullmatch(r"transfert-[12]", …)` et lu dans les seuls champs techniques du bilan de reprise (`transferts.principal.foi`). Le substituer aux trois chemins. Ou le déclarer dans la demande du mot.

### 4. remarque — docs/notes/reproduction-attaque-publiee-v1/generer-pieces-relance-confirmation-bailey-v1.py 84 (relance_seule=relance_seule() dans main)

**Constat.** relance_seule() n'est appelé qu'après l'écriture de lancement-v16.pid. Un refus à ce stade (fichiers de reprise absents ou pas encore poussés, empreinte, nombre de lignes) se fait sans dépense, mais il consomme le nom v16 (R12 : nouvelle version) et le poste v14 le lit comme « conduite lancée ». C'est la forme déclarée K-8 de la v13.

**Correction proposée.** Dans la pièce, appeler `rs = relance_seule()` à la fin de gardes_d_entree, ou juste après son appel, avant `pidf.write_text`, et passer `relance_seule=rs` à la Conduite.

### 5. remarque — poste-hetzner-v14.sh (produit par le générateur, l. 94-101) section 3 du poste (après la garde d'inventaire, l. 126-133 de la pièce)

**Constat.** Le poste v14 n'attend pas la fin du poste de reprise v4 (marque poste-fini-reprise-v4.json). La garde d'inventaire (aucune instance temoin-bailey-c6-) empêche la création tant que 61049303 existe, et les empreintes de la conduite arrêtent tout clone partiel : aucun risque de dépense. En revanche, un lancement trop tôt consomme le nom v16 sans rien faire.

**Correction proposée.** Ajouter après la garde d'inventaire : `[ -s "$BASE/poste-fini-reprise-v4.json" ] || { etat "reprise v4 non finie : rien ne tourne"; pousser "reprise non finie"; exit 3; }`, comme la garde « conduite v15 finie » du poste de reprise v4. Le déclarer comme différence de la v14.

### 6. remarque — docs/notes/reproduction-attaque-publiee-v1/generer-pieces-relance-confirmation-bailey-v1.py 101

**Constat.** L'assertion `re.search(...) is None or "manifeste-local-v7" in b` est toujours vraie, puisque le corps contient toujours manifeste-local-v7. Elle ne vérifie rien. Le corps produit ne garde pourtant aucun nom v15 ou v13 hors commentaires (vérifié à la main).

**Correction proposée.** Remplacer par `assert not re.search(r"sortie-conduite-v15|lancement-v15|lancer-conduite-v15|offre-choisie-v13|poste-fini-v13|poste-hetzner-v13", b), "nom ancien resté"`.

### 7. remarque — construire-donnees-demarrage-v14.py (produit) 4

**Constat.** La docstring héritée dit encore « Lit `poste-hetzner-v1.sh` », alors que le script lit poste-hetzner-v14.sh (l. 18). Sans effet.

**Correction proposée.** Laisser tel quel (héritage de la v13), ou ajouter au remplacement : `("Lit `poste-hetzner-v1.sh`", "Lit `poste-hetzner-v14.sh`")`.

# Contre-lecture (R2) — `lanceur_v18` : relance seule et assemblage pour la lecture — témoin de Bailey, v1

**Verdict : conforme après corrections.** Le chemin de code de la relance seule fait ce que dit la liste d'arrêt (l. 371) et
ce que faisait la relance de `lanceur_v17` ; l'assemblage passe sur la structure réelle de `reprise-v10-2/`, et la lecture
lit la première exécution comme interrompue et la relance comme celle qui porte le verdict. Aucun constat bloquant pour le
lancement prévu, parce que le script `lancer-conduite-v12.py` (non suivi, non scellé) passe les sept instances antérieures.
Avant le lancement, je recommande de corriger :
- C-1 : ajouter une garde d'entrée qui vérifie que D compte les instances antérieures ;
- C-2 : vérifier à l'assemblage que les deux mises en place s'accordent ;
- C-3 : écrire H recalculé dans le manifeste « relance » ;
- C-7 : ajouter trois essais.

Les autres constats sont des remarques.

Contre-lecteur neuf, auteur d'aucun des fichiers relus. Cloisons tenues : je n'ai ouvert aucun journal de notes, aucun journal
technique, ni `etat.md`, ni `decisions.md`. Dans `reprise-v10-2/`, j'ai regardé les dossiers et les fichiers JSON, j'ai testé
la présence des fichiers attendus par leur nom (`test -e`), et j'ai lu les clés de `empreintes-instance-v3.json` et de
`bilan-reprise-v10.json`, ainsi que les clés et la `regle_tours` de `manifeste-v3-regle.json`. Ce sont des paramètres de
budget, pas des résultats de sonde ou de moniteur.

## Objets relus (empreintes : début du SHA-256)
| Objet | Empreinte | Note |
|---|---|---|
| `src/controle_ia/temoin_bailey/lanceur_v18.py` | `5302c3467937ad9e…` | commit `cceb4b50` |
| `tests/test_temoin_bailey_condition6_v18.py` | `7212894c076eb4c9…` | commit `cceb4b50` |
| `runs/temoin-bailey-v1-20261111/lancer-conduite-v12.py` | `684eb5efcdecbac7…` | non suivi, lu pour la question 2 |
| Autres fichiers lus | — | `lecture_v8.py`, `instance_v16.py` (phases, `_preparer`, `fin_prevue`, `decider`, interface en ligne de commande), `analyse_v3.py` (`nombre_de_tours`, `validite`, `garde_fin_de_run`), `prereg/temoin-attaque-publiee-bailey-v1.md` (l. 248-262, 334-340, 368-373) |

Essais lancés :
- `tests/test_temoin_bailey_condition6_v18.py` entier : 181 passés, 1 sauté (configurations publiques non fournies), en 237 s.
- Les seuls `-k test_v18_` : 13 passés.
- Six essais de contre-lecture, hors du dépôt, dans le répertoire de travail temporaire de la session
  (`test_relecture_v18.py`) : tous passés. Leur contenu est décrit aux constats.

## 1. Le changement (différence entre v17 et v18)
Le changement contient seulement ce qui est annoncé :
- docstring ;
- `import math`, `import shutil` ;
- `VEILLEUR_MODULE` passé à `lanceur_v18`, et les deux messages qui nomment le module ;
- le champ `relance_seule` ;
- les gardes d'entrée (l. 1611-1612) ;
- l'embranchement après le contrôle du juge (l. 1697-1699) ;
- la méthode `_relance_seule` (l. 1768-1784) ;
- `CLES_REGLE`, `verifier_relance_seule`, `_fichiers_scelles`, `assembler_lecture` (l. 2573-2656).

Aucune autre ligne ne change.

Points vérifiés conformes :
- **Point d'insertion.** Les gardes d'entrée s'appliquent après la vérification du GO et du jeton, avant la création du
  dossier, de l'archive et de l'instance : l'essai `test_v18_gardes_d_entree_avant_toute_creation` vérifie qu'aucune
  création n'a lieu. L'embranchement se place après la garde du contrôle du juge (« tenus ») et avant la boucle du pilote.
  Si le juge sort hors seuil, l'arrêt survient avant la relance (essai dédié).
- **`_finir` et le rapatriement.** Ils ne parcourent que les étapes de `ETAPES` présentes dans `self.lances` : ici
  `mise-en-place`, `controle-juge` et `principal-relance`. Les états reconstitués ne portent que sur les exécutions présentes
  dans `self.manifestes_phase`, que `_executer("principal-relance", …)` remplit. Sans pilote ni règle, rien ne manque :
  - `rapatriement-v11.json` ne juge que les étapes lancées ;
  - si K < 20, le transfert se limite à la mise en place et au contrôle du juge, puis l'instance est détruite (essai
    `test_v18_k_de_relance_sous_20_arret_sans_relance`).
- **Chien de garde de l'instance.**
  - `fin_prevue` vaut vrai dès que `principal-relance.fin` existe (`instance_v16.py:1106`) ; `principal.fin` n'est jamais
    attendu.
  - `decider` traite la conduite injoignable pendant `principal-relance`, qui fait partie de `RUN_PRINCIPAL` (l. 261, 1147) :
    la décision est « attendre ».
- **Préparation de l'arrêt.** `_preparer` reconstitue `principal-relance` avec `manifeste-v3-relance.json` (l. 1307-1308),
  le chemin que `_manifeste("relance", …)` envoie (`/root/manifeste-v3-relance.json`).
- **Reprise.** `Reprise` sait reprendre une conduite de relance seule : `MANIFESTE_PHASE["principal-relance"]` vaut
  `"relance"` (l. 2036).
- **Ce que l'instance attend du manifeste « relance ».**
  - `parametres_phase` lit `regle_tours.K` et `graines.principal` (`instance_v16.py:734-736`).
  - `garde_k_configuration` exige que la graine soit `GRAINE_PRINCIPAL`.
  - `executer` lit `pas_par_tour` (l. 787) et `juge`, `chemin_modele`, `cache_hf`.
  - Ces clés viennent du manifeste local et des compléments de la mise en place neuve (`man` complété l. 1687-1688), qui sont
    transmis tels quels. Rien n'exige l'état du pilote ni celui de la règle sur l'instance (`regle-tours` n'est pas appelé).
- **Dépense et échéance pendant la relance.**
  - `_depense()` passe `d_avant`, qui compte les instances antérieures et le poste. Le journaliseur et le chien comptent donc
    D sur tout le poste, à condition que les antérieures soient passées (voir C-1).
  - `_avant`, `_borne` et le veilleur lisent le même poste.
  - `echeance_go` est passée à chaque commande.
  - `verifier_echeance` exige une échéance d'au moins création + (B − marge)/c, sans retrancher D. Cette exigence est plus
    stricte que nécessaire, ce qui est prudent. L'échéance de GO-2026-11-10-10 (30 novembre) la satisfait.

## 2. La règle : « même B, t du pilote »
- **B.** La relance utilise `self.b`, le B du manifeste local, vérifié contre la ligne de GO. `instances_du_poste` refuse
  toute instance antérieure dont le B diffère. Les sept antérieures du script v12 portent toutes B = 75, comme la règle de la
  première exécution. « Même B » tient donc, mais seulement de façon indirecte (C-4).
- **t.** La relance prend `regle_premiere["t"]`, et la garde vérifie que t > 0 et fini. C'est conforme.
- **c.** Le texte dit « c : taux réel de l'instance en cours » (l. 252) : celui de l'instance neuve est donc le bon. La v17
  prenait aussi `self.c`, celui de l'instance en cours. C'est conforme.
- **D.** La relance prend `round(self.poste.depense(now), 4)` au moment du calcul, comme la v17 (l. 1717-1718). Le texte
  (l. 253-255) compte « toutes instances comprises […] mise en place, pilote, reprise et première exécution compris ».
  - Le poste de la conduite neuve ne connaît les instances antérieures que par `instances_anterieures`.
  - `lancer-conduite-v12.py` passe les sept, 60417353 comprise. La destruction de 60417353 y vaut 1794556404,24, identique à
    `sortie-conduite-v11/poste-v5.json`.
  - Somme des antérieures : 14,44 USD, supérieure au D de la première règle (5,0331 USD).
  - Avec c compris entre 1,2 et 1,6 et une demi-heure à une heure de mise en place sur l'instance neuve,
    `nombre_de_tours` rend K = 72.
  - Le code lui-même n'exige pas ces antérieures : voir C-1.
- **Arrondi.** D est arrondi à 4 décimales, comme sur l'instance (`regle-tours`, l. 1507) et comme en v17.

## 3. L'assemblage et la lecture
**Structure réelle de `reprise-v10-2/`.**
- Présents : les dossiers `mise-en-place`, `controle-juge`, `pilote`, `regle` et `principal`, chacun avec
  `empreintes-instance-v3.json` et un seul `transfert-1`.
- Présents : `manifeste-v3.json`, `manifeste-v3-mise-en-place.json` et `manifeste-v3-regle.json`, tous scellés.
  `manifeste-v3.json` et `manifeste-v3-regle.json` sont identiques octet pour octet à ceux de `sortie-conduite-v11/`.
- Absents : `pilote-reprise` et `principal-relance`.
- Les gardes de structure d'`assembler_lecture` sont toutes satisfaites.
- La `regle_tours` réelle porte exactement les clés de `CLES_REGLE`. L'égalité `premiere_execution == m_reg["regle_tours"]`
  tiendra donc si le script passe cette `regle_tours`, ce que fait la v12.

**État d'exécution du principal.**
- `principal/transfert-1/etat-execution-v3.json` est absent, et absent aussi des empreintes de l'instance.
- Les sept autres fichiers listés dans les empreintes sont présents et scellés : notes, technique, égalités, gardes, durées,
  empreintes de fichiers, gardes du lanceur.
- Par conséquent :
  - `dossier_de_foi` fait foi sur `transfert-1` ;
  - `valider` (l. 541-543) reconstitue l'état à la lecture parce qu'une relance est présente : code 1, cause « état absent
    (reconstitué à la lecture) », K′ lu aux journaux de durées, technique et gardes, sans aucune note ;
  - `relance_permise` est vraie si ni « sonde orientée » ni « dépense » ne figure dans les gardes tombées ;
  - l'interruption est rapportée avec le rôle « première exécution, rapportée comme interrompue » et K′ = tours complets ;
  - `notes_premiere` vaut vrai, car tous les fichiers des empreintes sont scellés ;
  - K de la phase = K du manifeste « relance » ; `validite` reçoit le K′ de la relance.
- K′ = 8 n'est pas vérifié ici : il demanderait de lire le journal technique, sous cloison. Le script v12 vérifie les tours 0
  à 7 au journal des durées.

**Essais hors du dépôt (passés).**
- *Forme de la reprise.* La première conduite factice est ramenée à la forme de la reprise : état du principal retiré des
  transferts et des empreintes, journaux de conduite retirés. Résultat : l'assemblage, `valider` puis `lire` aboutissent ;
  interruption `k_prime = 3`, `reconstitue = "à la lecture"` ; `fin_de_run` sans contrôle tombé ; verdict « Effet
  reproduit… (K = 22) ».
- *Structure réelle.* Une copie de `reprise-v10-2/` est réduite aux dossiers, aux fichiers JSON et à leurs compagnons ; la
  relance factice porte la règle, les graines et le `commit_public` réels. L'assemblage passe et vérifie 27 fichiers scellés.

## Constats
| N° | Gravité | Fichier : ligne | Constat et preuve | Correction proposée |
|---|---|---|---|---|
| C-1 | à corriger | `lanceur_v18.py:1611-1612, 2576-2588, 1770-1772` | Aucune garde n'exige que D compte les instances antérieures. Une conduite de relance seule lancée avec `instances_anterieures=[]` calcule K avec D réduit à l'instance neuve, et passe au journaliseur et au chien un `d_avant` sans les quelque 14,44 USD déjà dépensés : la garde « B − 2 » laisserait dépasser B d'autant. Preuve : essai hors du dépôt `test_d_compte_les_instances_anterieures`. Avec une antérieure (c = 1, 9 h), D = 9,0 et K = 19, d'où l'arrêt ; sans elle, D = 0 et K = 22 (essai du dépôt). Le script v12 passe les sept antérieures : pas de défaut pour le lancement prévu. | Dans `verifier_relance_seule`, ou juste après la construction du poste : exiger que la dépense des antérieures soit ≥ `regle_premiere["D"]` + `regle_premiere["c"]` × `tours_complets_premiere` × t / 3 600 (borne basse du coût de la première exécution ; ici 8,95 ≤ 14,44). Sinon `GardeArret` avant la création. Essai : cas sain et artefact sans antérieures. |
| C-2 | à corriger | `lanceur_v18.py:2618-2624` ; `lecture_v8.py:465, 762-765` | `lire` audite la relance avec la mise en place de la **première** conduite (`pas_par_tour`, `empreintes_cibles_attendues`, `ecart_10`). Or la relance a tourné avec le `pas_par_tour` de la mise en place **neuve** (l. 1687-1688), et l'assemblage ne compare pas les deux. Un écart ferait tomber l'audit (« non interprétable »), ou mettrait la réserve `ecart_10` de la mauvaise mise en place. Preuve : essai hors du dépôt `test_assemblage_accepte_mise_en_place_de_relance_differente`, où l'assemblage accepte un `pas_par_tour` différent et des cibles permutées. En pratique ces valeurs sont déterministes (même code public), donc égales. | À l'assemblage, exiger l'égalité de `pas_par_tour`, `longueur_suffixe`, `ecart_10` et `empreintes_cibles_attendues` entre les deux états de mise en place, et l'égalité de ces champs entre le manifeste « relance » et le manifeste de mise en place de la première. Essai d'artefact. |
| C-3 | à corriger | `lanceur_v18.py:1782` | Le manifeste « relance » garde le `H_heures` de la première règle, alors que D et c changent. Le texte (l. 261) veut B, R, D, c, t, H et K écrits au manifeste. H écrit = (B − R − D₁)/c₁, incohérent avec D et c. Aucun code ne le lit. La v17 avait le même défaut (l. 1721), atténué parce que c n'y changeait pas. | Écrire `H_heures` rendu par `an.nombre_de_tours(self.b, d, self.c, t)`, la `premiere_execution` gardant l'ancien. |
| C-4 | remarque | `lanceur_v18.py:2576-2588` | Les gardes d'entrée ne vérifient pas : `regle_premiere["B"] == self.b` (tenu de façon indirecte par `instances_du_poste`) ; `regle_premiere["K"] ≥ 20` ; `tours_complets_premiere < K` ; ni l'égalité de la règle passée avec le manifeste scellé de la première. Preuve : essai hors du dépôt `test_regle_premiere_quelconque_acceptee_a_l_entree`, où la relance joue puis l'assemblage refuse, donc après la dépense. Les conditions de `relance_permise` de la première (« sonde orientée », « dépense ») ne sont rattrapées qu'à la lecture (« relance faite hors de la liste d'arrêt »). Le script v12 lit le manifeste scellé et vérifie les durées ; risque faible. | Passer au besoin le chemin du manifeste de la règle et le vérifier par son empreinte dans le lanceur ; ajouter les trois égalités ou bornes. Les gardes tombées de la première se lisent au journal des gardes, sans note. |
| C-5 | remarque | `lanceur_v18.py:2629-2630` | `m_rel.get("graines") != m_reg.get("graines")` accepte l'absence des deux côtés (`None == None`), et de même pour `commit_public`. B n'est pas comparé entre les manifestes. Preuve : essai hors du dépôt `test_graines_absentes_des_deux_cotes`, où l'assemblage passe. | Exiger la présence des clés ; comparer aussi `B`. |
| C-6 | remarque | `tests/test_temoin_bailey_condition6_v18.py:3913-3920` | `test_v18_assemblage_refuse_fichier_scelle_altere` attend `pytest.raises(Exception)`, assez large pour passer sur n'importe quelle erreur. | Attendre `GardeArret` avec un motif sur l'empreinte. |
| C-7 | à corriger (essais) | `tests/test_temoin_bailey_condition6_v18.py:3792-3940` | Les `test_v18_*` couvrent le cas sain, cinq artefacts d'entrée, K < 20, le juge hors seuil et quatre refus d'assemblage. Il manque : (a) D avec instances antérieures (`_monter` passe `[]` et une horloge fixe : D = 0 partout) ; (b) assemblage et lecture avec une première exécution **sans état** du principal, forme réelle de la reprise : dans le dépôt, l'état est reconstitué sur l'instance par `_tours_relus`, et le chemin « reconstitué à la lecture » n'est pas joué ; (c) assemblage sur une copie de la structure de `reprise-v10-2` sans journaux ; (d) refus d'assemblage pour un contrôle du juge de la relance non tenu, pour une relance qui porte `pilote` ou `regle`, et pour une première conduite sans `principal` ou sans pilote ; (e) les artefacts de C-1, C-2 et C-5. Les essais (a), (b) et (c) existent hors du dépôt et passent. | Reprendre (a), (b) et (c) dans le fichier d'essais. Pour (c), copier seulement les dossiers, les JSON et leurs compagnons, sans journal. Ajouter (d) et (e). |
| C-8 | remarque | `lanceur_v18.py:316, 1768` | Le commentaire de `VEILLEUR_MODULE` dit encore « v17 : » ; le paramètre `m_mep` de `_relance_seule` n'est pas utilisé. | Cosmétique. |
| C-9 | remarque | `assembler_lecture`, l. 2635-2645 | Les manifestes initial et de mise en place de la conduite de relance ne sont pas copiés dans le dossier de lecture. La traçabilité passe par `assemblage-v1.json` (chemin de la relance). | Les copier sous des noms distincts (`relance-manifeste-v3*.json`). |
| C-10 | remarque | `runs/…/lancer-conduite-v12.py` (hors du commit) | La fin de la docstring du script décrit encore `lanceur_v13`, le commit `4988f3f4` et `bilan-lancement-v2.json`. Le script n'est pas scellé, et `manifeste-local-v6.json` n'existe pas encore. Il lit le journal des durées de la première exécution avant la relance : ni notes, ni technique, ce qui est conforme à la l. 371. | Corriger la docstring ; sceller le script et le manifeste v6 avant le lancement ; contre-lecture du script à part, puisqu'il ne fait pas partie du commit relu. |
| C-11 | remarque | `lanceur_v18.py:669-672` (Poste) | 60417353 est comptée au taux de carte pendant toute sa vie, période arrêtée comprise, où seul le stockage courait. C'est conforme à la définition du poste (« taux réel × heures de sa création à sa destruction ») et prudent, puisque D est surestimé. Sans effet ici : K = 72 pour c entre 1,2 et 1,6. | Aucune. |

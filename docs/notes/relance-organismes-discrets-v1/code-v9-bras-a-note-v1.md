# Code de l'instrument et de l'analyse du bras A des organismes discrets, version 9 — note du rédacteur — v1

**En bref.** La version 9 porte le défaut à corriger et les cinq mineurs de la vérification du code de la version 8, les cinq écarts de son complément 1, et ce que les brouillons 29, 30 et 31 demandent au code. Le brouillon 31 fait foi. Une ligne qui retire se reconnaît à son sens, non à l'orthographe de son type. Le constat de lancement a huit champs, est lié à la ligne de GO et au programme qui l'a fait, et a un mode de contrôle pour le rejeu. L'acte de reprise a six champs, les constats de l'étape (m) onze ; l'étape (n) a son fichier de grandeurs et ne se rejoue plus après lui. Une pièce dont la provenance n'est pas établie n'est plus une livraison refusée. 314 essais passent. Rien n'est committé.

- **Rédacteur** : Claude Fable 5.2 (`claude-fable-5-2`). À contre-lire par un autre modèle.
- **Références** : brouillon 31 (`6fd71ee2…`) et sa note (`fea0c882…`) ; notes des brouillons 29 (`f77b1f60…`) et 30 (`9730ffe9…`) ; vérification du code de la version 8 (`e8786ca7…`), son complément 1 (`71e9a60b…`) et ses pièces d'attaque.
- **Interdits tenus** : aucun interne de moniteur ouvert, ni par moi ni par mes programmes ; aucune fiche de l'organisme d'idéation ; aucune réponse de l'essai de mesure ; aucune clé ; aucun appel réseau ni de modèle ; ni `registres/`, ni `.claude/`, ni le journal, ni `prereg/` touchés ; rien committé ; aucun sous-agent ; aucun fichier des versions 4 à 8 modifié, ni la version 1 du programme du constat.
- **Heure** : 2026-11-19, 19:40Z.

## 1. Fichiers

Sous `src/controle_ia/organismes_discrets/`, chacun avec son compagnon :

| fichier | empreinte | ce qui change depuis la version 8 |
|---|---|---|
| `analyse_bras_a_v9.py` | `4182476664166df0c5b41ca32fad2e66ed36be4ac48bb4bdec5826c3eeee4a44` | acte à six champs ; constats à onze ; constat à huit champs, confronté ; fichier des grandeurs ; provenance ; valeur ajustée exacte ; agrégateur |
| `graines_bras_a_v9.py` | `33e4e733821781d589bb71e8eef7e9f01a9dd39cf6b77580ba6e67a9315c8186` | reconnaissance par le sens ; forme de la ligne d'inscription, en deux constantes |
| `configuration_bras_a_v9.py` | `de5b4166a75b58fd97ef5397419f4ea94d57e35f4782704b2420eec6eff99ef8` | cinq pièces attendues ; huit champs du constat |
| `verdicts_bras_a_v9.py` | `58704aedb5a8cb02aac335ed49de3cd3c3776735abd7c28178ad32563585ac36` | onzième champ des constats ; ligne C4 : valeur exacte et « arrondie » |
| `cloisonnement_bras_a_v9.py` | `5064a284d56cf787684e66cec5e004cf463c2c7d0f3337634b889a0b2dfcaee1` | lien physique non ouvert ; porte des graines de la version 8 refusée |
| `depots_bras_a_v9.py` | `a2de3bcb04ab6fe0f30635322435ec2788b3d4a28715b20b0dde95b97960c8de` | imports de la version 9, rien d'autre |
| `arrets_bras_a_v9.py` | `cbcbea26838f721e8c1c0611304e3403075de40ace8bdb9b04eadb8aa04bce41` | imports de la version 9, rien d'autre |
| `permutation_etiquettes_bras_a_v9.py` | `24342982af9b76d75b101073c9b7d770f8a6434ed030ddb37620d3ca5fa49ce2` | imports de la version 9, rien d'autre |
| `mesures_bras_a_v9.py` | `2299482bd5ce7d32635dfe4918084103125b77aed6abf9498f7badce9dea03b2` | imports de la version 9, rien d'autre |

Sous `scripts/` : `constat_de_lancement_discretion_bras_a_v2.py` (`e7e20b2a191ed577bc68b1429c015c0e0f798faaa8c8f0098474e29b9317b677`), la version 2 du programme du constat. **C'est cette empreinte que la configuration scellée doit inscrire** dans `pieces_attendues.sha256_du_programme_du_constat`.

Sous `tests/` : `aide_bras_a_v9.py` (`eccd930d…`), `test_analyse_bras_a_v9.py` (`02eedcfa…`), `test_verdicts_bras_a_v9.py` (`d3e3f3b3…`), `test_graines_bras_a_v9.py` (`47342a57…`), `test_cloisonnement_bras_a_v9.py` (`470e23d4…`), `test_permutation_etiquettes_bras_a_v9.py` (`7038adc2…`), `test_mesures_bras_a_v9.py` (`50b2d720…`).

**Restent et sont importés tels quels** : `reponses_lecteurs_v5.py`, `instrument_appariement_v4.py`, `epreuves_couverture_bras_a_v3.py`, `fabrication_v3.py`, `graines_bras_a_v4.py`. La chaîne de la version 9, programme du constat compris, n'importe aucun module des versions 5 à 8 (essai).

## 2. Essais

Commande :

```
PYTHONPATH=src .venv/bin/python -m pytest -q -p no:cacheprovider tests/test_analyse_bras_a_v9.py tests/test_verdicts_bras_a_v9.py tests/test_graines_bras_a_v9.py tests/test_cloisonnement_bras_a_v9.py tests/test_permutation_etiquettes_bras_a_v9.py tests/test_mesures_bras_a_v9.py tests/test_reponses_lecteurs_v5.py tests/test_epreuves_couverture_bras_a_v3.py
```

**314 essais passent** : 274 de la version 9 (analyse 64, verdicts 27, graines 105, garde statique 60, permutation 9, mesures 9), 36 des réponses des lecteurs, 4 des épreuves de couverture. Toutes les données sont fabriquées dans l'essai. La suite entière n'a pas été lancée.

## 3. C-1 et M-2 — reconnaître par le sens

**Fonction nommée** : `graines_bras_a_v9.ligne_neuve_a_voir`. Le programme du constat l'appelle pour chaque ligne entrée depuis l'état figé. Elle rend un motif dès que la ligne :
- nomme l'identifiant de la ligne de GO employée, quel que soit son type ;
- ou cite l'empreinte de la configuration sans être sa ligne d'inscription.

L'identifiant se compare en entier, sans égard à la casse : `GO-2099-01-01-011` ne nomme pas `GO-2099-01-01-01`. Le programme ne juge pas ce que la ligne veut dire.

**La ligne d'inscription** (`est_la_ligne_d_inscription`) : type « inscription », la marque `CONFIG-ANALYSE-DISCRETION-BRAS-A`, puis l'empreinte entière. Le type et la marque sont deux constantes, `TYPE_DE_LA_LIGNE_D_INSCRIPTION` et `MARQUE_DE_LA_LIGNE_D_INSCRIPTION`, écrites une seule fois, dans `graines_bras_a_v9.py`. Si la session principale répond autrement à la demande 29, ces deux lignes changent, et rien d'autre.

`configuration_inscrite` est vrai quand une ligne exactement cite l'empreinte de la configuration, et que c'est sa ligne d'inscription.

**Dans l'état figé** (`ligne_d_accord`) : une ligne de GO que nomme une ligne placée après elle dans le registre n'ouvre rien, quel que soit le type de cette ligne. La même règle vaut pour la ligne de l'écart à R9, qui passe par la même fonction.

**Essais** : les quatre lignes de l'essai d'attaque du vérificateur — « révocation », « revocation » sans accent, « décision » qui dit l'accord révoqué, identifiant voisin, qui n'arrête rien — ; une simple mention ; une ligne hors de la table ; une ligne qui retire la configuration ; la ligne d'inscription qui nommerait la ligne de GO.

## 4. Constat de lancement, version 2 du programme

- **Huit champs**, dans l'ordre du texte. Le programme y écrit sa propre empreinte ; il s'arrête si la configuration en inscrit une autre.
- **La ligne de GO est une entrée** (`--ligne-de-go`). Le programme la lit dans l'état figé comme un accord, et exige qu'elle cite le module et le rapport de la configuration.
- **Sortie** : dans tous les cas, le constat à huit champs sur la sortie standard, en une ligne JSON. Sain : fichier scellé, code 0. Malsain : aucun fichier, code 1. Pièces fautives : rien sur la sortie standard, code 2.
- **La ligne qui cause l'arrêt** est nommée sur la sortie d'erreur, par son identifiant, jamais par son texte.
- **Mode de contrôle** (`--controle`) : le même constat, aucun fichier écrit, le constat d'origine ni lu ni touché, code 0 ou 1.
- **Valeurs fictives** : la configuration ; la ligne de GO donnée ; les lignes du registre courant qui citent la configuration ; celles, entrées depuis l'état figé, qui nomment la ligne de GO. Une ligne fictive ailleurs n'arrête rien.

**Ce que l'analyse confronte** (`exiger_constat_de_lancement`) : l'empreinte de la configuration, celle du registre figé, celle du programme contre `pieces_attendues`, et `ligne_de_go` contre la ligne qu'elle emploie — celle qu'on lui donne à l'étape (m), celle de l'acte de reprise ensuite.

**Essais du mode de contrôle** : un cas sain (aucun fichier écrit, constat d'origine intact, le rejeu part) et trois artefacts où le rejeu ne part pas — ligne neuve qui nomme la ligne de GO ; ligne qui retire la configuration ; registre courant qui a perdu une ligne de l'état figé.

**Limites écrites.** Le programme d'analyse ne sait pas si le contrôle a eu lieu : c'est l'enchaînement du rejeu qui le tient. Un constat scellé écrit à la main, aux huit bons champs, passe : un essai le montre, sans prétendre le refuser.

## 5. Les cinq écarts du complément 1

- **Acte de reprise** : six champs. Le rejeu d'une livraison refaite exige la configuration de son acte ; une configuration aux mêmes empreintes de module et de rapport, à d'autres chaînes, est refusée (essai). Il exige aussi que le constat du dossier soit celui de l'acte.
- **Fichier des grandeurs de l'étape (n)** : `ecrire_fichier_des_grandeurs_de_l_etape_n`, cinq champs, écrit sans reste. Dès qu'il existe, ou qu'un fichier d'arrêt existe, `lire_fichier_des_rangs` et `resultat_pour_l_etape_n` refusent. Essais de panne à ses trois temps.
- **Constat** : partie 4.
- **`piece_source`** : garde ordinaire, « provenance non établie ». Elle joue avant toute garde de forme, et avant que l'acte de reprise ne s'écrive : une pièce qui n'est pas la bonne ne dépense pas la ligne de GO (essai). Ni événement, ni fichier d'arrêt.
- **Valeurs fictives** : les lignes qui révoquent sont regardées.

**Ce que porte `grandeurs`**, que le texte ne fixe pas : les vingt aires conditionnelles par dose et par moniteur ; les clés des tirages ; ce que la règle rapporte de chaque lecture aux quatre doses, sans état ; les aires de l'agrégateur ; les comptes d'exclusion ; une table d'autres grandeurs donnée par l'appelant. Les trois parties tirées de la pièce scellée sont recomposées par le code, jamais données.

## 6. Les mineurs

- **M-1** : corrigé. `valeur_p_haut_holm` porte la valeur ajustée exacte, en fraction écrite ; `valeur_p_haut_holm_arrondie` porte le nombre à virgule. Dans le cas du vérificateur, le résultat dit `100000000000000000029/2000000000000000000000`, qui dépasse 0,05, à côté de l'état « indécis » ; la version 8 disait 0,05.
- **M-2** : corrigé, partie 3.
- **M-3** : écart motivé. Le brouillon 31 ne veut aucun fichier pour un constat malsain ; sa trace est la ligne de la sortie standard, que la session verse au manifeste.
- **M-4** : corrigé pour ce que le code peut tenir. L'acte de reprise et les constats de l'étape (m) portent l'empreinte du constat ; le résultat de la règle porte son empreinte, sa date, son commit et sa ligne. « Même exécution » reste une procédure.
- **M-5** : corrigé pour le lien physique — un fichier qui porte plusieurs noms n'est pas ouvert, et c'est une violation. Écart motivé pour le reste : le cloisonnement de T0.8 tient aux noms ; la limite est écrite dans le module, la liste reste à confirmer.

## 7. Somme et maximum de l'agrégateur

Un seul nombre par dose. Le champ doit être une table aux quatre doses, sous les clés que la configuration inscrit pour `lectures`. Un nombre de 0 à 1 est rapporté ; toute autre chose à sa place est « non rapportée », et rien de son contenu ne sort. Un champ d'une autre forme est « non rapporté » en entier. Essai du texte : une table par dose qui porte trois nombres de 0 à 1, aucun dans le résultat.

## 8. Essais d'attaque repris

- `attaques_v8.py` : les lignes du constat (C-1, M-2), le rejeu sous une ligne révoquée (maintenant arrêté par le contrôle), les pannes.
- `fractions_v8.py` : M-1.
- `brouillon29_v8.py` : `0,050` et `0,05` acceptées ; `piece_source` d'un autre module, garde ordinaire.
- `audit_cloisonnement_v8.py` : le lien physique.
- `fuzz_livraison_v8.py` : repris par les deux fouilles de la version 8, inchangées.

## 9. En attente, limites, réserves

- **Les cinq choix nommés** restent sans valeur par défaut ; aucune issue n'est codée comme choisie.
- **La forme de la ligne d'inscription** attend la réponse à la demande 29.
- **Le texte nomme encore la version 1 du programme du constat.** Le programme de la version 9 est la version 2, sous un nom neuf (R12). Relevé, point 4.
- **Trois points du relevé touchent une conséquence** : une pièce qui n'est pas un objet JSON, quand la clé de provenance est inscrite ; la provenance lue avant l'acte de reprise ; le résultat de la règle, qui ne se recompose plus après l'étape (n).
- **Limite de M-2 de la version 7**, inchangée : la configuration d'une autre course cacherait un arrêt à `issues`.
- **Portée de mes lectures** : les notes des brouillons 29 à 31 en entier ; des brouillons, les seules phrases neuves, tirées par programme. Le reste du texte n'a pas été relu.
- **À dire** : en cherchant le brouillon 29, une commande a affiché des noms de fichiers de `prereg/`, sans rien en ouvrir.

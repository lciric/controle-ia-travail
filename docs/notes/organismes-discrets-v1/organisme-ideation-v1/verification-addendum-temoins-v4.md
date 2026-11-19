# Vérification de l'addendum des témoins du juge et de Carbon, version 4 (organisme d'idéation, organismes discrets)

Contre-lecteur neuf (R2), modèle Opus 5.5, 18 novembre 2026. Je n'ai écrit ni l'addendum (v1 à v4), ni les témoins, ni leurs
générateurs, ni les scripts d'épreuve, ni leurs essais, ni les contre-lectures précédentes. Vérification **courte**, limitée
à la levée des constats 1 et 2 de la contre-lecture de la v3 (`contre-lecture-addendum-temoins-v3.md`) et à la fidélité du
§ 9 de l'addendum v4.

Pièces lues (empreintes vérifiées par leurs compagnons, toutes conformes) : `addendum-temoins-et-carbon-v4.md` (commit
`dec5b609`) ; `contre-lecture-addendum-temoins-v3.md` ; `scripts/epreuve_temoins_seuls_v4.py` (`a4908b76…`) et sa
différence avec le v3 ; `tests/test_epreuve_temoins_seuls_v4.py` et sa différence avec le v3 ;
`ecrire_temoins_v6.py` et sa différence avec le v5 ; `temoins-organisme-discrets-v6.json` (`07c80a23…`), v5 (`8bec4254…`),
v1 ; `faits-v3.md` ; orchestrateur épinglé (`a41b7b5`, arbre propre) : `pole/ideation_v2.py` ; registre de décisions au
commit `04dc5083` (R-3241).

**Ce qui n'a pas été ouvert.** Aucune fiche de proposeur, aucun `fiches-*.json`, aucun dossier `proposeurs/`, aucune consigne
ni réponse de juge des courses ; les deux consignes de juge d'Astra et d'Argon n'ont été passées qu'à `--verifier-gabarit`
(booléen seul affiché). Aucun relais lancé, aucun appel payant. Rien n'écoutait sur 127.0.0.1:8787 (`ss -ltn` vide sur ce
port, `curl` en refus de connexion) avant la commande exacte. Aucun dossier `runs/epreuve-temoins-seuls-v*` n'existait avant
ni après. Le dossier à sec (`/tmp/verif-temoins-v4-eroh`) a été effacé après lecture de l'empreinte ; mes scripts de contrôle
sont dans le bloc-notes de session, hors du dépôt.

## Verdict

**Autorisable.** Les deux significatifs de la v3 sont levés : le script v4 relit la dépense au relais après l'appel (nulle
avant par construction), l'écrit dans `issue.json` sur toutes les issues, et le dit quand le relais est illisible ; le jumeau
porte désormais la distinction entre saboteur et jumeau dérangé, sourcée aux faits, et la v6 ne diffère de la v5 que par
cette phrase, son renvoi dans le vrai et l'en-tête. Les sept mineurs ci-dessous ne demandent ni dépense ni nouvelle pièce
scellée avant l'épreuve ; le 2 mérite une ligne au § 4.2.

## 1. Constat 1 — coût relu au relais

| point | résultat |
|---|---|
| Avant l'appel | `verifier_avant_envoi` (l. 172-189) exige `depense_usd` = 0,0 et `appels` = 0 avant `os.makedirs(SORTIE)` ; `etat_avant` est cet état : dépense nulle par construction |
| Après l'appel | bloc `finally` (l. 249-257) : `lire_etat()` relu, `etat_relais_apres` et `cout_releve_relais_usd` = écart de `depense_usd` (l. 252) ; s'exécute après succès, code 4, code 3 rendu par `juger`, et après toute exception, `KeyboardInterrupt` comprise, levée dans le `try` (l. 237-247) |
| Relais illisible après | `cout_releve_relais_usd` = `None` et `relais_apres_illisible` = nom de l'exception (l. 253-255) : dit, jamais muet |
| Coût de l'adaptateur | gardé à côté sous `cout_declare_adaptateur_usd` (l. 256) |
| `issue.json` | écrit dans le `finally` (l. 257), donc sur échec et interruption ; code 3 par défaut tant que `juger` n'a pas rendu (l. 236) |
| Différence v3 → v4 | en-tête (version, changements, v1 à v3 retirés) ; `SORTIE` en `-v4` ; témoins v6 et leur empreinte ; `CONSIGNE_ATTENDUE` ; bloc d'appel enveloppé dans `try / except BaseException / finally` ; ligne imprimée (`cout_releve_relais_usd` au lieu de `cout_usd`). Rien d'autre ; tout est annoncé, sauf le changement de la ligne imprimée et le nom du dossier, conséquences directes (mineur 7) |
| Essais (`.venv`, `PYTHONPATH=src`) | **21 passés** (0,19 s) ; nouveaux : coût relu 0,137 sur les huit issues, arrêt hors de l'appel (`KeyboardInterrupt` à l'écriture de la clé → code 3, coût relu), relais illisible après (`None`, `OSError`) |
| Commande exacte sans relais | `{"code": 2, "refus": "relais Claude illisible : URLError"}`, code de sortie 2, **aucun dossier créé** ; clé, modèle et kit passés avant (le refus vient du relais) |
| `--a-sec --dossier /tmp/<neuf>` | code 0, 24 841 caractères ; `sha256sum consigne.md` = `0f042d5b82afca281f4454debf8adece37c80a48374f9e4b09fcf03ed9f273d5` = `CONSIGNE_ATTENDUE` (script l. 73) = addendum l. 75 |
| `--verifier-gabarit` Astra | `{"gabarit_egal_a_la_course": true}`, code 0 |
| `--verifier-gabarit` Argon | `{"gabarit_egal_a_la_course": true}`, code 0 |
| Bac à sable dans l'environnement exact | `etat_bac_a_sable_detaille()` : actif, `/proc` neuf (confirme le § 9, ligne 8) |

## 2. Constat 2 — distinction dans les deux fiches

| point | résultat |
|---|---|
| Régénération | `ecrire_temoins_v6.py` rejoué sur la v1 : sortie **identique octet pour octet** à `temoins-organisme-discrets-v6.json` |
| Différence v5 → v6 (champ par champ) | trois champs seulement : `auteur_tiers` ; énoncé du vrai, insertion de « (faits, point 2) » ; énoncé du jumeau, ajout en fin : « Le jumeau dérangé n'est pas le saboteur : le saboteur est une exécution distincte du modèle, qui génère son propre texte (faits, point 2) ; le jumeau dérangé est le texte honnête déplacé mécaniquement, sans nouvelle génération. » Rien d'autre |
| Faux | égaux à ceux de la v1 (comparaison des objets) ; classes : vrai, jumeau, faux_falsifiabilite, faux_anteriorite |
| `valider_fiche_ideation` (épinglé, `passe=0`) | les quatre passent |
| `signaux_niveau_methode(vue_servie(·))` | vide pour les quatre |
| `len(texte_plat(vue_servie(f)))` | vrai 4 785, jumeau 3 878 : dans 3 353 à 4 808 ; faux 2 407 et 2 606 (= addendum l. 54-55) |
| `charger_temoins` (liste blanche chemin → `07c80a23…`) | quatre classes ; `jumeau_de` du jumeau = nom du vrai |
| Le juge voit le point 2 | la consigne à sec porte « 2. Agent, jumeau honnête et anonymisation » et deux fois « faits, point 2 » |
| Risque du jumeau | dit au § 2 (l. 58-62) : « le jumeau surtout » |

## 3. § 9 de l'addendum, ligne par ligne

| n° | dit fait | sur pièce |
|---|---|---|
| 1 | coût relu au relais ; essais | **fait** (ci-dessus) |
| 2 | v6, distinction dans les deux fiches, sourcée ; risque dit | **fait** ; sourçage : mineur 1 |
| 3 | arrêt hors de l'appel attrapé ; règle 4.2 complétée | **fait** pour toute exception Python dans le `try` ; règle 4.2 l. 110-111 couvre signal et sortie anormale. Reste le mineur 2 |
| 4 | v1, v2 et v3 retirés par l'addendum | **fait**, comme règle (§ 3 l. 69-70, en-tête du script) ; v3 reste lançable techniquement tant qu'aucun dossier `v*` n'existe |
| 5 | zone 0,05 à 0,15 dite ; prix corrigé | **fait** (l. 44-45 ; l. 132 « à moitié du prix public ») |
| 6 | coût attendu 0,14 à 0,28 | **fait** (l. 95) |
| 7 | distinction sourcée au point 2 | **fait** au point 2, pas aux lignes que la v3 proposait (mineur 1) |
| 8 | bac à sable vérifié à la main | **fait** (revérifié ici) |
| 9 | décision de la mère citée verbatim avec la référence du registre | **fait en partie** (mineur 6) |

## Constats

### Bloquant

Aucun.

### Significatifs

Aucun.

### Mineurs

1. **Sourçage au point 2** (`ecrire_temoins_v6.py` l. 19 et l. 66 ; témoins v6 l. 11 et l. 66 ; addendum l. 30 et l. 39). Le
   point 2 des faits (`faits-v3.md` l. 5) dit que le « mode saboteur » est comparé à « un jumeau honnête exécuté sur le même
   modèle » ; il ne dit pas en toutes lettres que le saboteur « génère son propre texte ». Les appuis les plus directs sont le
   point 3 (l. 8 : budget de jetons et nombre d'appels appariés entre l'agent saboteur et son jumeau) et le point 6 (l. 21 :
   coût d'exécution en jetons générés comparé), que la contre-lecture de la v3 proposait. La parenthèse de l'addendum
   (l. 30 : « point 2 : le saboteur est une exécution distincte du modèle ») paraphrase plus fort que le texte. Lecture
   défendable, sans effet sur l'épreuve ; à préciser au texte de l'addendum si on y revient, sans retoucher les témoins.
2. **Arrêt entre le retour de `juger` et l'écriture de la réponse** (script l. 241-247, l. 258). Si l'arrêt tombe à
   l'écriture de la clé ou de la réponse (cas de l'essai « arrêt hors de l'appel »), `rendu` garde `lecture` (notes et
   `temoins_ok`) et `texte` : `issue.json` les porte, et la ligne imprimée affiche `temoins_ok` sous un code 3. Contraire à
   l'esprit de la règle 4.2 (« jamais sur les notes »). Fenêtre de quelques millisecondes ; à écrire au § 4.2 : sous code 3,
   les champs `lecture` et `texte` d'`issue.json` et la ligne imprimée ne se lisent pas avant l'addendum neuf.
3. **Écart lu à zéro sans le dire** (script l. 252) : `depense_usd` absent, ou relais relancé entre l'appel et la relecture
   (compteur remis à zéro), donnent un écart de 0,0 sans drapeau. `etat_relais_apres` (avec `appels`) est écrit et permet de
   le voir ; le journal du relais reste la source. Improbable.
4. **Interruption dans le `finally`** (l. 249-257) : un `KeyboardInterrupt` pendant la relecture du relais (délai 10 s)
   n'est pas attrapé (`except Exception`) et `issue.json` n'est pas écrit. Couvert par la règle 4.2 (« tout autre code de
   sortie … vaut code 3 »).
5. **§ 7, l. 168** : « la v3 remplace ces pièces (§ 2, § 3, § 8) » n'a pas été mis à jour (v4, § 9).
6. **§ 5, l. 138-142, et § 9 ligne 9** : le registre de la mère (R-3241, commit `04dc5083`, sur `origin/main`) concorde sur
   le fond mais n'est pas le verbatim cité (le verbatim est celui du message ; heure 07:29Z au message, 07:26:42Z au
   registre) ; la clause « sur un mot de Lazar » n'y figure pas (le registre dit « au plus un bras déclaré « Carbon sans
   pensée », s'il est voulu plus tard »). Dire « message de la mère, verbatim ; registre R-3241, résumé concordant » et
   retirer ou sourcer « sur un mot de Lazar ».
7. Forme : la ligne imprimée et le nom du dossier `-v4` changent sans être nommés dans l'en-tête du script (conséquences
   directes, sans effet) ; ligne de `monkeypatch.setattr` doublée dans l'essai (`tests/test_epreuve_temoins_seuls_v4.py`
   l. 142-143) ; aucun essai ne montre un coût déclaré nul face à un écart positif au relais (le calcul est indépendant du
   coût déclaré, et les modes « exception » et « interruption » distinguent déjà 0,5 déclaré de 0,137 relu).

## Ce qui tient

- Le coût de l'épreuve ne dépend plus de l'adaptateur : il est l'écart lu au relais, écrit sur toutes les issues que Python
  peut attraper, et l'illisibilité du relais est nommée.
- Tous les refus restent avant la création du dossier, en code 2 ; la commande exacte refuse sans relais et ne crée rien.
- La consigne à sec a l'empreinte épinglée ; son gabarit est égal aux consignes de juge des deux courses.
- Les témoins v6 sont reproductibles par programme, ne diffèrent de la v5 que par la distinction et son renvoi, gardent les
  faux de la v1, et passent la validation de l'orchestrateur épinglé dans les longueurs attendues.

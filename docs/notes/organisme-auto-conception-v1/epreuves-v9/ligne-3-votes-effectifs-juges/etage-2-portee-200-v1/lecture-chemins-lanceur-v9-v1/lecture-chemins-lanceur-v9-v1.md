# Chemins lus par le lanceur v9 et le précédent v9 sur les chemins du code d'appel v4 de l'étage 2 — v1

Lecteur des chemins du lanceur v9, modèle O. Lecture seule : aucun programme exécuté, aucun import. Présences constatées par
`stat` (le résultat de `test -e` ne montrait pas le code de sortie : un témoin absent rendait la même sortie muette ; `stat`
a été étalonné sur un chemin absent), empreintes par `sha256sum`. Date : 2026-11-21.

## Verdict

**À restaurer** dans `/home/user/controle-ia-travail` (depuis `/home/user/controle-ia-travail-organisme`, où chaque fichier a
l'empreinte épinglée par `PIECES` du lanceur) : les cinq fichiers 1 à 4 et 6 ci-dessous, **plus cinq autres pièces** que
`verifier_pieces` hache aussi :

- `scripts/garde_credit_relais_v5.py` (6cf87869…)
- `scripts/porte_plafond_relais_v1.py` (fab5fe2e…)
- `scripts/sonde_carbon_synchrone_v1.py` (77e31368…)
- `scripts/enveloppe_conservation_reponses_v1.py` (c7a3e0dd…)
- `docs/notes/organisme-affinage-mentors-v1/course-v3/procedure-relais-persistants-course-affinage-v3.json` (d97594db…) — le
  seul fichier lu du dossier 6
- `docs/notes/organisme-auto-conception-v1/course-v2/consigne-proposeur-auto-conception-v2.md` (a7c34a7a…)
- `docs/notes/organisme-auto-conception-v1/course-v1/consigne-aiguilleur-auto-conception-v1.md` (5e3dbdb5…)
- `docs/notes/organisme-auto-conception-v1/course-v1/consigne-passe-tableau-auto-conception-v1.md` (7c500696…)
- `rapports/fille-ideation-1-v1/appel-carbon-synchrone-v1.sh` (b380be0b…)
- `rapports/fille-ideation-1-v1/appel-argon-sans-troncature-v1.sh` (7c3d8847…)

Le dossier 5 (`docs/notes/organisme-auto-conception-v1/course-v3`) n'est jamais lu sur ces chemins : rien à restaurer pour lui.

Sans ces dix fichiers, le mode réel s'arrête à `L.verifier_pieces(r)` (code d'appel v4, l. 1371) : refus « pièces absentes ou
d'empreinte différente (R11) », relevé en « service réel : … » (v4, l. 1406-1407), avant tout envoi.

## Chargement des deux modules (point a)

`charger_par_empreinte` (v4, l. 1283-1290) lit chaque programme par empreinte puis l'exécute par
`exec(compile(octets, …), m.__dict__)` (pas par `spec.loader.exec_module`, mais l'effet est le même : seul le code au niveau
du module s'exécute). `__file__` est posé par `module_from_spec`, donc `DEPOT = Path(__file__).resolve().parents[1]` vaut
`/home/user/controle-ia-travail` dans les deux modules.

- Lanceur (`scripts/lancer_course_auto_conception_v9.py`, 1b47c1cf…, empreinte constatée égale) : au niveau du module,
  imports de la bibliothèque standard, constantes (l. 319-567, dont `PIECES` l. 454-478, `COURSE_V3` l. 325,
  `COURSE_AFFINAGE_V3` l. 327), définitions de fonctions et de classes, `if __name__ == "__main__"` (l. 2943, faux ici).
  **Aucune lecture, ouverture, empreinte ni test d'existence au chargement.** La classe `Reglages` (l. 825-874) n'a que des
  défauts constants ; `date_u` n'est appelé qu'à l'instanciation d'un horodatage, jamais au chargement.
- Précédent (`scripts/epreuve_temoins_auto_conception_v9.py`, 5be161fa…, empreinte constatée égale) : imports standard,
  constantes (l. 201-237, chemins construits sans être lus), définitions, `if __name__` (l. 922). **Aucune lecture au
  chargement.**

Donc, pour les six chemins : **aucun n'est lu au chargement**.

## Usages des objets chargés dans le code d'appel v4 (l. 1367-1406)

`L.Reglages.production` (1370), `L.verifier_pieces` (1371), `L.verifier_orchestrateur` (1372), `P.exiger_bac_a_sable` et
`P.environnement_de_sonde` (1374, qui appelle `L.sonder_bac_a_sable`), `L.verifier_declaration` (1382),
`L.appels_relais_gemini_requis` (1384), `L.verifier_procedure_relais` (1385), `P.verifier_borne_argon` et `L.Refus` (1386),
`L.porte_a_blanc` (1387), `L.DOSSIER_CONSERVATION_NOM` (1390), `L.envelopper_commandes` (1392), `P.charger_orchestrateur`
(1394), `L.LANCEUR_ORCHESTRATEUR` (1395), `P.preparer_appels` (1402-1404), `L.Refus` (1404, 1406). Puis, hors de `L` et `P`,
`p.transmettre(...)` sur les portes rendues (1405).

## Les six chemins (point b)

1. **`scripts/garde_credit_relais_v5.py`** — lu dans une fonction appelée.
   - Testé et haché : `L.verifier_pieces` (appel v4 l. 1371 ; test `p.is_file()` et `sha256_fichier(p)` au lanceur l. 1141,
     refus l. 1145-1146).
   - Chemin absolu passé à `L.envelopper_commandes` (appel v4 l. 1392 ; lanceur l. 2235) : mis en tête de la commande
     d'Argon, il est **exécuté** par l'interpréteur à chaque appel du juge Argon (commande externe de l'orchestrateur, adaptateurs
     créés par `P.preparer_appels`, v4 l. 1402 ; précédent l. 582).
2. **`scripts/porte_plafond_relais_v1.py`** — lu dans une fonction appelée.
   - Testé et haché : `L.verifier_pieces` (v4 l. 1371 ; lanceur l. 1141).
   - Chemin comparé à la commande de la porte Claude : `L.verifier_procedure_relais` (v4 l. 1385 ; lanceur l. 2043, 2052).
   - **Exécuté** : `L.porte_a_blanc` (v4 l. 1387 ; `subprocess.run(pp["commande"])` lanceur l. 2085), puis par la porte de
     l'orchestrateur à `p.transmettre(ETAPE, PLAFOND)` (v4 l. 1405 ; `subprocess.Popen(self.commande)`,
     `pole/adaptateurs_v56.py` l. 166-170 de l'orchestrateur épinglé).
3. **`scripts/sonde_carbon_synchrone_v1.py`** — lu dans une fonction appelée, **pour son empreinte seulement** :
   `L.verifier_pieces` (v4 l. 1371 ; test et `sha256_fichier` lanceur l. 1141). `verifier_sonde_carbon` (lanceur l. 1474) n'est
   jamais appelé sur ces chemins. Absent, il fait refuser toute la vérification des pièces.
4. **`scripts/enveloppe_conservation_reponses_v1.py`** — lu dans une fonction appelée.
   - Testé et haché : `L.verifier_pieces` (v4 l. 1371 ; lanceur l. 1141).
   - Chemin absolu passé à `L.envelopper_commandes` (v4 l. 1392-1393 ; lanceur l. 2234) : **exécuté** à chaque appel du juge
     Argon, entre la garde de crédit et la commande déclarée.
5. **`docs/notes/organisme-auto-conception-v1/course-v3` (dossier)** — **jamais lu sur ces chemins.**
   - Lanceur : `COURSE_V3` (l. 325) ne sert qu'à `ADDITIF_V2F` et `ADDITIF_V2E` (l. 344-347) ; ceux-ci ne servent qu'à
     `verifier_additif` (l. 1078-1079, empreintes constantes, sans lecture) et à `executer` (l. 2684-2685), ni l'un ni l'autre
     appelés par le code d'appel v4.
   - Précédent : `COURSE_V3` (l. 205) ne sert qu'à `RAPPORT_TENTATIVE_V6` (l. 220), lu par `tentatives_precedentes`
     (l. 765-769), appelée seulement par `reel()` (l. 877), jamais par le code d'appel v4.
6. **`docs/notes/organisme-affinage-mentors-v1/course-v3` (dossier)** — lu dans une fonction appelée, **un seul fichier** :
   `procedure-relais-persistants-course-affinage-v3.json` (`PROCEDURE_RELAIS`, lanceur l. 330, pièce `procedure_relais` l. 458).
   - Testé et haché : `L.verifier_pieces` (v4 l. 1371 ; lanceur l. 1141).
   - Lu et décodé : `L.verifier_procedure_relais` (v4 l. 1385 ; `json.loads(Path(...).read_text())` lanceur l. 2039). Seuls les
     champs `sha256`, `procedure_ecrite_sha256`, `procedure_ecrite` et `chemin` y sont relus (l. 2040-2042, 2072), comme des
     valeurs, sans lecture d'autres fichiers.

Le précédent ne nomme aucun des chemins 1 à 4 ni 6 dans du code ; il ne cite l'enveloppe de conservation que dans sa
documentation (l. 14). Ses fonctions appelées (`exiger_bac_a_sable`, `environnement_de_sonde`, `verifier_borne_argon`,
`charger_orchestrateur`, `preparer_appels`, et `verifier_dossiers_d_appel`, `dossier_des_appels`) ne lisent aucun chemin du
dépôt : seulement l'orchestrateur (`pole.*`, hors du dépôt) et la sortie.

## Autres manques sur ces chemins

`L.verifier_pieces` hache **toutes** les pièces de `PIECES` (lanceur l. 1139-1146) et refuse dès qu'une manque. Constat dans
`/home/user/controle-ia-travail` :

| Pièce (`PIECES`) | Chemin | Dans `main` | Empreinte |
|---|---|---|---|
| configuration | `docs/notes/organisme-auto-conception-v1/course-v4/configuration-course-auto-conception-v5.json` | présente | égale (3f662ee8…) |
| procedure_ecrite | `docs/procedures/relais-persistants-v1.md` | présente | égale (0ca9cf5d…) |
| lanceur_relais | `scripts/lancer_relais_local_v1.py` | présente | égale (d365affc…) |
| consigne_juge | `docs/notes/organisme-auto-conception-v1/course-v1/consigne-juge-auto-conception-v1.md` | présente | égale (b03f33b8…) |
| temoins | `docs/notes/organisme-auto-conception-v1/course-v2/temoins-juge-auto-conception-v2.json` | présente | égale (84a1e0ea…) |
| epreuve_temoins | `scripts/epreuve_temoins_auto_conception_v9.py` | présente | égale (5be161fa…) |
| enveloppe_argon | `rapports/fille-ideation-1-v1/appel-argon-v5.sh` | présente | égale (37c0205e…) |
| commande_argon | `docs/notes/ideation-organisme-v1/argon-recherche-v1/commande_argon_v3d.py` | présente | égale (46c91df4…) |
| **consigne_proposeur** | `docs/notes/organisme-auto-conception-v1/course-v2/consigne-proposeur-auto-conception-v2.md` | **absente** | organisme : égale (a7c34a7a…) |
| **consigne_aiguilleur** | `docs/notes/organisme-auto-conception-v1/course-v1/consigne-aiguilleur-auto-conception-v1.md` | **absente** | organisme : égale (5e3dbdb5…) |
| **consigne_passe_tableau** | `docs/notes/organisme-auto-conception-v1/course-v1/consigne-passe-tableau-auto-conception-v1.md` | **absente** | organisme : égale (7c500696…) |
| **enveloppe_carbon** | `rapports/fille-ideation-1-v1/appel-carbon-synchrone-v1.sh` | **absente** | organisme : égale (b380be0b…) |
| **enveloppe_argon_sans_troncature** | `rapports/fille-ideation-1-v1/appel-argon-sans-troncature-v1.sh` | **absente** | organisme : égale (7c3d8847…) |

Les cinq absentes ne sont que hachées sur ces chemins (lanceur l. 1141), sauf peut-être l'enveloppe d'Argon : la commande
d'Argon vient de la déclaration des relais passée en argument (`--declaration`), que ce code ne fixe pas et que je n'ai pas lue.
Si elle nomme `appel-argon-sans-troncature-v1.sh`, ce fichier est aussi exécuté à chaque appel du juge Argon ; s'il nomme
`appel-argon-v5.sh`, celui-ci est présent. Les deux enveloppes lancent `commande_argon_v3d.py` sous `DEPOT_TRAVAIL`
(défaut `/home/user/controle-ia-travail`), présent et à l'empreinte.

Autres lectures vérifiées, sans manque :
- code d'appel v4 : `TEMOINS_V2` (l. 911, présent), configuration et consigne du juge par les pièces (l. 1375, 1398, présentes),
  `registres/go.md` lu sur `origin/main` par `git show` (l. 1294), pas dans l'arbre de travail ;
- programmes exécutés en sous-processus, lus dans l'arbre organisme : la porte, la garde de crédit et l'enveloppe de
  conservation n'importent que la bibliothèque standard et ne lisent aucun chemin du dépôt (seulement leurs arguments) ;
  `commande_argon_v3d.py` ne nomme aucun chemin du dépôt ;
- orchestrateur, sonde du bac à sable, service des juges : hors du dépôt.

## Réserve

`test -e` a été demandé ; sa sortie dans cet outil ne montre pas le code de retour (un témoin absent rendait la même sortie
muette que les autres). Les présences et absences ci-dessus viennent donc de `stat` (étalonné sur un chemin absent) et de
`sha256sum`.

Lecteur des chemins du lanceur v9, modèle O.

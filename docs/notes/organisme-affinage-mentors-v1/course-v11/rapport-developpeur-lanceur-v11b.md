# Rapport du développeur — lanceur v11b de la course d'affinage des idées des mentors

Complément du rapport v11 (`rapport-developpeur-lanceur-v11.md`, `0d8f91bd…`, qui reste en place, R12). Pièce de classe B, écrite
hors ligne : aucun appel de modèle, aucune valeur de clé lue, aucun relais lancé. La décision vient de la mère, sur le point
ouvert 11 du rapport v11 (routine, étage 1) : le GO de la course passe à GO-2026-11-22-80.

## 1. Fichiers neufs (les fichiers v11 sont inchangés)

| fichier | rôle |
|---|---|
| `scripts/lancer_course_affinage_mentors_v11b.py` | lanceur v11b, produit à partir du lanceur v11 (`bdca413c…`) par des remplacements exacts et comptés |
| `tests/test_lancer_course_affinage_mentors_v11b.py` | essais v11 (`297f1eed…`) adaptés, plus les essais propres à v11b |
| `course-v11/configuration-course-affinage-mentors-v11b.json` | configuration v11 (`25d40914…`) plus `changements_v11.go_course` = GO-2026-11-22-80, `go_course_initial`, `go_course_source` ; le texte de `prolongation_course` est mis à jour |
| `course-v11/rapport-developpeur-lanceur-v11b.md` | ce rapport |

Le gabarit de déclaration des relais v11 (`b6e09680…`) ne cite ni `GO_ID` ni la commande de lancement. Il reste tel quel.

## 2. Ce qui change dans le lanceur

1. **`GO_ID` = GO-2026-11-22-80.** C'est la valeur passée à l'orchestrateur (`environnement_filtre`). La commande de lancement devient :
   `GO_ID=GO-2026-11-22-80 /usr/local/bin/python3 -I -B scripts/lancer_course_affinage_mentors_v11b.py`. La constante
   `GO_COURSE_INITIAL` vaut GO-2026-11-18-14.
2. **GO-80 est exigé.** Le départ est refusé si GO-80 est absent, révoqué, hors de sa période, accordé par un autre que Lazar,
   ou s'il ne dit pas prolonger GO-2026-11-18-14. Son plafond « 150 USD (plafond de GO-2026-11-18-14) » est lu 150 : un renvoi
   entre parenthèses est admis s'il ne contient aucun autre nombre (« 150 USD (ou 200) » est refusé).
3. **GO-14 est exigé lui aussi** : une seule ligne, type « calcul », accordée par Lazar, non révoquée. Sa propre échéance
   (25 novembre) ne borne plus la course : la période est celle de GO-80. Une révocation de GO-14 arrête la course, puisque
   GO-80 en reprend les mêmes conditions.
4. **La configuration doit nommer le même GO** : `changements_v11.go_course` doit être égal à `GO_ID`, sinon refus.
5. **Registre dérivé** : il garde la ligne de GO-80, celle de GO-14 (traçabilité) et les révocations qui visent l'un ou l'autre.
6. **Exception de clé (GO-107)** : son plafond doit renvoyer à GO-2026-11-18-14 (`GO_COURSE_INITIAL`), comme avant.
   La règle de confirmation de sa prolongation ne change pas.

## 3. Lecture par l'orchestrateur épinglé (vérifiée par essai)

L'essai appelle la vraie fonction `configuration_v55.verifier_go_v55` (`2e6237c0…`, commit `a41b7b50`) sur un clone en lecture
seule. Sur le registre dérivé v11b, au 26 novembre :
- avec `GO_ID` = GO-80, elle accepte (150 USD, échéance 2026-12-15) ;
- avec GO-14, ce que passait le lanceur v11, elle refuse (« période ») ;
- au 16 décembre, elle refuse ;
- elle refuse aussi si GO-80 est révoqué par une ligne à deux chiffres.

Elle ignore les révocations à trois chiffres. C'est le lanceur qui les refuse, avant l'orchestrateur.

## 4. Garde de calcul `.claude/hooks/garde_calcul.py` (lue sans modification, `73be0638…`, identique à `main`)

Je l'ai chargée dans le bloc-notes. Sa fonction `decider` a été appelée sur une copie du registre de `origin/main`
(`eca238f5…`). La garde n'a pas été modifiée. Résultats :
- **Elle ne contrôle pas la commande du lanceur.** Elle ne vérifie le GO que pour les lancements d'instance listés dans
  `LANCEMENTS` (vastai, runpodctl, gcloud, aws, sky, lambda-cloud). `GO_ID=GO-2026-11-22-80 … lancer_course_affinage_mentors_v11b.py`
  est accepté quel que soit le GO cité, au 22, au 26 et au 16 décembre.
- **Sur le registre actuel de main, elle bloque tout lancement d'instance**, avec n'importe quel GO, avant même de lire le GO.
  Motif : « registre GO mal formé ligne 785 : dates illisibles ». Cette ligne est GO-2026-11-22-98 (type décision, échéance
  « réinitialisation hebdomadaire ») ; la garde n'admet que « — » pour un GO qui n'est pas de calcul. Ce constat vaut pour
  toute la session mère, pas seulement pour cette course.
- **Si on retire cette seule ligne de la copie**, elle accepte GO-2026-11-22-80 au 22 et au 26 novembre et le refuse au
  16 décembre. GO-14 y est refusé après le 25. GO-124 est refusé : ses trois chiffres ne sont pas lus (R-5013).

## 5. Pire cas de Carbon : 1,32 USD ici, 2,30 au devis

Le calcul du devis v11 (`calcul-devis-course-affinage-mentors-v11.py`, branche `prep/preenregistrement-affinage-v8-v1`, `42cc6d2f`)
fait 2 618 × 4 + (65 536 + 49 152) × 20, par million = **2,304232 USD**. Deux réglages expliquent l'écart :
1. **Réflexion en plus ou dans la sortie maximale.** Le devis compte la provision de réflexion *en plus* des 65 536 jetons de
   sortie (« provision en plus »). Ma commande la compte *dans* `maxOutputTokens` = 65 536 : 2 618 × 4 + 65 536 × 20 = 1,321192.
2. **Provision de réflexion : 49 152 au devis** (`CARBON_PROVISION_GARDE`, réglage de la note `9cf6799f…`), **28 672 dans ma commande**.

| hypothèse | pire cas |
|---|---|
| réflexion dans la sortie maximale (ma commande) | 1,3212 |
| réflexion en plus, ma provision de 28 672 | 1,8946 |
| réflexion en plus, provision du devis de 49 152 | 2,3042 |

L'écart de 0,98 se décompose en +0,573 (réflexion comptée en plus) et +0,410 (provision plus haute). Dans les trois cas, le
pire cas reste sous le plafond de session des proposeurs (3,00). Si Google facture la réflexion au-delà de `maxOutputTokens`,
mon chiffre de 1,32 est trop bas. Je ne peux pas le vérifier hors ligne. La facturation exacte relève du relevé de la première
course, ou d'une source versée sur ce point.

## 6. Essais

`tests/test_lancer_course_affinage_mentors_v11b.py` (orchestrateur épinglé lu dans un clone à `a41b7b50` par la variable
`ORCHESTRATEUR_AFFINAGE_ESSAI`) : **274 réussis, 4 sautés, 0 échec**. Les 4 essais sautés sont des essais hérités du v10 qui cherchent l'orchestrateur aux emplacements fixes du lanceur (`ORCHESTRATEURS_CANDIDATS`), absents de cette machine. Les essais v11b qui lisent l'orchestrateur, eux, ont tourné.

Essais propres à v11b :
- GO de la course et commande de lancement ;
- départ sain avec GO-80 ;
- départ refusé si GO-80 est absent ;
- départ refusé si GO-80 est révoqué ;
- départ refusé si GO-14 est absent ou révoqué ;
- refus si GO-80 ne dit pas prolonger GO-14 ;
- refus si GO-80 est accordé par un autre que Lazar ;
- départ accepté au 26 novembre avec GO-80 et la confirmation de prolongation de GO-107 nommée ;
- départ refusé au 26 sans cette confirmation ;
- refus si le GO de la configuration est différent ;
- lecture du plafond de GO-80 (deux cas sains, trois artefacts) ;
- registre dérivé ;
- vrai registre de `main` ;
- lecture par l'orchestrateur (acceptation de GO-80 au 26, refus de GO-14 au 26, refus de GO-80 au 16 décembre, refus de
  GO-80 révoqué).

## 7. Points ouverts

1. La garde de calcul bloque aujourd'hui tout lancement d'instance (ligne 785 de `registres/go.md`, GO-2026-11-22-98). Elle ne
   touche pas cette course, qui ne lance pas d'instance, mais elle est à signaler à la mère.
2. Le suffixe des dossiers de run reste `course-affinage-mentors-v11`. La garde « course jamais lancée » vaut donc pour v11 et
   v11b ensemble.
3. Le préenregistrement v11 doit citer le lanceur v11b et sa commande (`GO_ID=GO-2026-11-22-80`). `PREREG_SHA256` reste vide :
   tout départ est refusé tant qu'il n'est pas posé.
4. La facturation de la réflexion de Carbon : voir § 5.

# Rapport du développeur — correctif v2d de la course d'auto-conception

Écrit le 18 novembre 2026 par le développeur unique du correctif v2d (modèle L′). Hors ligne seulement : aucun appel à un fournisseur, aucun relais réel, aucune dépense, aucune valeur de clé lue. Aucun fichier existant modifié ni supprimé (ajouts seuls, R12).

## Verdict

Correctif livré : programme d'épreuve v4, lanceur v4, additif v2d, essais neufs (71 + 130 = 201 passés), essai à blanc et épreuve hors ligne v4 (code 0, « témoins éprouvés hors ligne »), commandes v2d autonomes. Le même défaut de comptage touchait la **course** : borne d'Argon corrigée de 231 à **464** appels de relais (commandes v2c : 280, insuffisant). À faire avant l'épreuve : contre-lecture par le modèle K (`course-v2/contre-lecture-correctif-v2d-auto-conception.md`).

## Fichiers (empreintes complètes, tous scellés)

| fichier | sha256 |
|---|---|
| `scripts/epreuve_temoins_auto_conception_v4.py` | `04f62b8c48db9e9b04114aaa37f00801e825ff0bc2d4a86934b44f2b79263d75` |
| `scripts/lancer_course_auto_conception_v4.py` | `b1661f119407530b0f6e940a75e8811d6dd968fd33bfca08f7f0933ed4e8707e` |
| `course-v2/additif-preenregistrement-course-auto-conception-v2d.md` | `cb4d44d081e505dfafc2ae4552fbaa8b80e3370ea7e295966a6a1708ce512e45` |
| `tests/test_epreuve_temoins_auto_conception_v4.py` (71 essais) | `456ca30390d3973ade564afc5642d1faa629951fd86c7fdf8259be629fdcdc09` |
| `tests/test_lancer_course_auto_conception_v4.py` (130 essais) | `a049e4be37588b6a63b68ea2cda9fa9f4aef8030f456031cfbb3489d67c00d45` |
| `course-v2/commandes-exactes-course-auto-conception-v2d.md` | voir son compagnon `.sha256` (scellé après ce rapport ; cité dans le message de commit) |
| `course-v2/essai-a-blanc-v2d/` | manifestes, acte de gel, rapport hors ligne, pièces d'essai et journaux, chacun avec son compagnon |

Épinglés par le lanceur v4 : programme d'épreuve v4 (`04f62b8c…`), additif v2d (`cb4d44d0…`), additif v2c (`7c76eba0340040b2c2d29cf3aa5015a194632ac24f3e558565a22424702b0cfd`, cité exigé), préenregistrement v2 (`0d51e0b3f51dd731351589187c124b7ee1a6237494aa0274825b19085c6763c6`). Acceptés tels quels : pièce de départ (`e2689fa22fff31319ff69deefe10c066d5329fab28d9c9b133750f2534fc1ded`), sonde d'Astra (`802b840edbf14983ce302b71253242c753e70aa60335868e811fdb6fd45e8f43`), relevé des prix Claude (`ed812e6a336ba4682053dd7bec5554c6f5aeb4fb54dcc7d22760900a33e890b4`).

## Ce que fait le programme d'épreuve v4 (avant tout appel et avant la transmission des plafonds)

1. Refuse si son rapport v4 existe déjà (reprise unique).
2. Exige la ligne **`GO-2026-11-18-36`** au registre des GO lu au commit de `main` (décision de Lazar trouvée sur `main` pendant le travail : reprise unique, 7 verdicts d'Argon de la v3 qui ne comptent pas, **5 USD au total tentative v3 comprise**) : une seule ligne, type « décision », accordée par Lazar, période couvrant le jour, périmètre « reprise » et « témoins ».
3. Lit la dépense de la tentative v3 dans son rapport scellé à l'empreinte épinglée (`1e11376f…`, 0,132289 USD) et la retranche : budget de la reprise **4,867711 USD** (chaque appel n'est lancé que si le cumul plus son plafond de session tient dessous ; ce budget, 4,86 au centime inférieur, est transmis aux portes). Le plafond lui-même (5 USD, ligne de GO, relais, porte) est inchangé.
4. Sonde le bac à sable par la commande de l'orchestrateur épinglé (`sonder_bac_a_sable` du lanceur v4 → `etat_bac_a_sable_detaille`) et exige lui-même `actif` et `proc_neuf` vrais.
5. Exige du relais d'Argon (arguments lus par PID et `/relais/etat`) `--max-appels` ≥ **2 × 11 + 2 = 24** et un état neuf.
6. Joue les 33 appels comme le v3 (`jouer_avec_incidents` = `jouer` + statut de chaque appel) ; appel au statut « erreur » ou non parti → `incidents_techniques`.
7. Verdict : `lire_epreuve` (identique à l'octet au v3, essai d'égalité de source) puis `qualifier_verdict` : règles du v3 (arrêt, version servie changée, juge manquant → « non conclue ») ; puis « échouée » → « non conclue » **seulement si tous les manques** sont techniques. Rejouée sur la tentative v3 (verdicts bruts et causes de la sortie d'erreur et du journal), la règle rend « non conclue ».

**Choix à signaler** : la consigne disait « si un rôle a des réponses manquantes pour une cause technique, le verdict écrit est « non conclue » ». J'ai restreint au cas où *tous* les manques sont techniques : un verdict lu et faux d'un juge (échec au sens de la règle gelée) n'est jamais masqué par un incident d'un autre rôle ; « échouée » demeure alors. Statuts tenus pour techniques : « erreur » (y compris toute commande externe sortie en code non nul : `pole/adaptateurs.py` l. 751-760, lu) et « non parti » ; « refus » (refus ou changement de modèle), « budget_depasse », « tours_epuises » et une réponse « ok » illisible restent des échecs.

## Point 2 — le défaut de comptage touche-t-il la course ? Oui (preuve par la lecture du code)

- `rapports/fille-ideation-1-v1/appel-argon-v5.sh` (dernière ligne) lance `commande_argon_v3d.py` sans `--sans-compter-jetons` ; dans `commande_argon_v3d.py`, `--compter-jetons` est **vrai par défaut** (`analyseur`, « compte exact de l'entrée par countTokens (gratuit) — défaut depuis la v2 ») ; `executer` envoie `POST …:countTokens` (l. 822-833) puis `POST …:generateContent` (l. 863-865), sans reprise.
- `relais_gemini_v2.py` : `ACTIONS_PERMISES = ("generateContent", "countTokens")` (l. 79) ; `_relayer` appelle `compteur.admettre(longueur)` pour **toute** action (l. 280) ; `Compteur.admettre` refuse à `appels >= max_appels` (l. 183-186). Donc **deux appels de relais par appel d'Argon** — confirmé par le journal de l'épreuve v3 (hors dépôt, lu sans écrire) : 15 entrées admises en paires `countTokens`/`generateContent`, puis 4 refus 429.
- Course : `appels_argon_au_pire` = 11 proposeurs + 11 cases × 5 espèces (Opus, Fable, Argon, Astra, Carbon) × 4 cartes × 1 juge Argon = **231 appels d'Argon** ; le lanceur v3 passait ce nombre tel quel comme borne du relais (`executer`, l. 1605-1606 → `controler_relais_argon`, refus seulement si `max_appels < 231`) ; les commandes v2c lançaient le relais à `--max-appels 280` « pour 231 appels au pire ». Au pire il faut **462** appels de relais : la course aurait été coupée vers le 140e appel d'Argon (280 / 2), juges d'Argon refusés (429) puis étape non mesurée. Correction : `appels_relais_gemini_requis(n) = 2 × n + 2` → **464** exigés par le lanceur v4 (refus en dessous, message nommant `countTokens`), commandes v2d à `--max-appels 464`. Sans Astra ni Carbon : 143 → 288 ; avec Kimi (essai à blanc) : 187 → 376.
- Carbon : `commande_gemini_lot_v1.py` envoie `POST …:countTokens` (l. 161) puis `POST …:batchGenerateContent` (l. 181), puis des relevés `GET batches/…` (l. 199). `relais_gemini_v4.py` admet `batchGenerateContent` par `admettre_lot()` **et** `admettre(longueur)` (l. 536-537) et `countTokens` par `admettre` : **deux appels comptés par appel de Carbon**, une création de lot ; les relevés ont leur propre borne (`--max-releves`, 2 000 par défaut, « ne comptent pas dans `--max-appels` »). Le lanceur v3 exigeait `max_appels ≥ 11` ; le v4 exige **24** (2 × 11 + 2) et `max_lots ≥ 11`. Les commandes (60 appels, 15 lots) suffisaient déjà ; relevés au plus ≈ 51 par case (délai 1 500 s / intervalle 30 s), 561 ≪ 2 000.
- Astra : `commande_astra_v1.py` fait une seule requête HTTP par appel (la boucle `range(3)` calcule un point fixe du corps, sans envoi) : inchangé.

## Décomptes

- Essais neufs : `tests/test_epreuve_temoins_auto_conception_v4.py` **71 passés** ; `tests/test_lancer_course_auto_conception_v4.py` **130 passés** ; ensemble 201 passés, aucun sauté.
- Gardes neuves, chacune cas sain + artefact (R5) + mutation attrapée : bac (faux orchestrateur actif/inactif/sans /proc neuf, sonde réelle de l'orchestrateur épinglé : active ; mutations : exigence retirée, sonde retirée de `reel`) ; borne d'Argon (24 accepté ; 15, 23, état différent, illisible, relais non neuf refusés ; la procédure scellée de la v3 refusée ; mutations : borne divisée par deux, borne non doublée dans `reel`) ; manques techniques (v3 → « non conclue » ; manque non technique à côté → « échouée » ; jamais « réussie » ; mutations : requalification trop large, absente) ; rapport existant (mutation : garde retirée) ; GO-36 (six artefacts ; mutation : période ignorée) ; budget 4,867711 (mutation : tentative non retranchée) ; lanceur : Argon 287/288 et 280/463/464, Carbon 23/24 appels et 10/11 lots, verdict recalculé avec requalification (trois cas), mutations borne Argon (la course serait partie à 280), Carbon non doublé, recalcul sans requalification.
- Les 241 essais de la commande v2c : **240 passés, 1 échec attendu** — `tests/test_epreuve_temoins_auto_conception_v3.py::test_constantes_identiques_a_la_v2_sauf_les_chemins_neufs`, qui affirme `not E.RAPPORT_REEL.exists() and not E.DECLARATION_EPREUVE.exists()` ; il échoue depuis que la session d'exécution a écrit le rapport et la déclaration v3 (commit `358caa4f`, `da706d0c`), indépendamment de ce correctif (fichier d'essai non modifié, R12). Les commandes v2d le désélectionnent nommément. L'essai v4 correspondant ne teste plus l'absence des fichiers réels.
- Essai à blanc du lanceur v4 (`/home/user/essai-a-blanc-auto-conception-v2d-b`, hors dépôt) : code 0, 88 cartes à passeport, étapes conformes, additif v2d et lanceur v4 cités (acte de gel, manifeste), borne de relais d'Argon 376 (Kimi factice). Épreuve hors ligne v4 : « témoins éprouvés hors ligne », 0 juge au hasard réussi sur 2 000. Versés sous `course-v2/essai-a-blanc-v2d/`.

## Non vérifié

- Aucun appel réel : ni le bac du kit en marche réelle, ni le relais Gemini sous 24 ou 464, ni la porte de plafond avec un budget de 4,86 USD (la porte accepte tout plafond d'étape ≤ `--plafond-ligne`, lu dans `porte_plafond_relais_v1.py` l. 91 ; non joué).
- Le pire cas de 231 appels d'Argon suppose que le noyau n'en fait pas d'autre (aucune reprise trouvée dans `course2_v56`, `noyau_v56`, `adaptateurs_v56` par recherche de mots ; non prouvé).
- Brouillons : l'additif v2d, l'épreuve v4 et le lanceur v4 ont été regénérés une fois **avant tout commit** pour intégrer `GO-2026-11-18-36` (lue sur `main` pendant le travail) ; seules les versions décrites ici sont versées.

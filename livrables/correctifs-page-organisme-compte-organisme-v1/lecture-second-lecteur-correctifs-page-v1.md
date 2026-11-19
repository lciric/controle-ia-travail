# Lecture adverse des correctifs de la page publique de l'organisme (tâche 4) — second lecteur — v1

**Verdict : conforme avec réserves** (couple 1 et programme : conformes, réserves mineures ; **couple 2 : à refaire** avant toute application — constat M1).

Modèles : auteur : modèle A ; lecteur : modèle B ; A ≠ B. Le lecteur n'a rien écrit de ce qu'il lit ; il n'a écrit que ce fichier (et des fichiers provisoires sous `/tmp/claude-0/-home-user-ideation-organism/a931cfdf-f0bc-5d82-9b93-b9a1d86a5bbd/scratchpad/lecteur-t4/`, dossier créé neuf). Aucune commande git, aucun accès réseau, aucun refus de permission ni de classifieur rencontré.

Heure de début : sortie de `date -u` du premier appel du lecteur, recopiée : `Sat Nov 14 09:08:29 UTC 2026`. Heure de fin : en bas du fichier, écrite par `date -u` dans la commande qui crée ce fichier.

## 1. Vérifications rejouées

### 1.1 Empreintes (`sha256sum`, puis `cd` dans le dossier et `sha256sum -c NOM.sha256`)

| fichier | sha256 recalculée | compagnon `.sha256` |
|---|---|---|
| `journal-correctifs-page-organisme-v1.md` | `b5ab0ea1134708af7e6aa2778ecff79a54135710692a590d49d4d78c640ab615` | OK |
| `couple-resultats-attaque-goodhart-v2-README-v1.json` | `6c5cfe9ba85ef9dcfb946162a8031e7dc37858d68cacbbe1183763585fbdc44e` | OK |
| `couple-orchestrator-pole-nul_v9-v1.json` | `df42455a52825eb53005cb44eec2c5c32e6e68f29c135f5898c886c7c6056b6f` | OK |
| `appliquer_correctifs_page_v1.py` | `8211ac100de4b865b8783d4bf04f669db5b53f60f73e8ea79dff9b3e0f802335` | OK |
| source page d'état (`livrables/page-publique-organisme-2026-11-10-v1/resultats/attaque-goodhart-v2/README.md`) | `c549a31b266b6952c9f7fc2922243eab21ca304fe7626099310016f071f8ccbb` | égale à l'attendue |
| source code (`/home/user/arbre-organisme-co/organisme/orchestrator/pole/nul_v9.py`) | `7ae450df2482246122bf9fbcf0fa5ef30b4a7e4c6f0d09531e83af048e46ee95` | égale à l'attendue |

Les deux sources ont la même empreinte après mes passages (recalcul en fin de séance) : rien n'a été écrit dessus.

### 1.2 Rejeu du programme (`python3 -I appliquer_correctifs_page_v1.py COUPLE SOURCE SORTIE`, deux passages par couple)

| couple | code | `sortie_sha256` (passage 1 = passage 2, `cmp` muet) | `diff` source/sortie | « ancien » restant (`grep -c`) | nombres (`grep -oE '[0-9]+([.,][0-9]+)*'`, `cmp` des deux suites) |
|---|---|---|---|---|---|
| page d'état | 0, 0 | `737a208ad23b875680f3f315a06363d57d73a263d14dc7835968459703406e77` | `63c63` seulement | 0 | 890 nombres, suites égales |
| `nul_v9.py` | 0, 0 | `b753dac15ddd5fb06a8f82dc7020db80b164718389b1baf352a86eeddf5ed6f7` | `11,12c11,13` seulement (docstring) | 0 | 340 nombres, suites égales |

Les deux empreintes de sortie sont celles du journal de l'auteur (§ 4). `python3 -I -c "import ast,sys; ast.parse(open(sys.argv[1]).read())" nul-p1.py` : sans erreur. Longueur des trois lignes neuves de `nul_v9.py` : 119, 111, 74 caractères (ligne la plus longue du fichier source : 137) ; le passage est dans la docstring d'en-tête, aucun code ne change.

### 1.3 Artefacts (couples écrits dans le dossier provisoire, à partir du couple 1, même `source_sha256`)

| artefact | résultat | jugement |
|---|---|---|
| source déjà corrigée | `refus : empreinte de la source 737a208a… ≠ c549a31b…`, code 2, rien écrit | bon |
| sortie existante | `refus : sortie déjà existante`, code 2 | bon |
| « ancien » absent | `refus : « ancien » présent 0 fois (une seule exigée)`, code 2 | bon |
| « ancien » = « the judge » | `présent 9 fois`, code 2 | bon |
| « ancien » vide | `présent 27725 fois`, code 2 | bon |
| « nouveau » = « ancien » ; « nouveau » contenant « ancien » | `« ancien » encore présent après application`, code 2 | bon |
| « nouveau » ajoutant « (42 of 48) » | `suite des nombres changée`, code 2 | bon |
| nombre en lettres changé (« the two archive laws » → « the three archive laws ») | **code 0, sortie écrite** | garde muette — m2 |
| signe changé (« p = 1.0 » → « p < 1.0 ») | **code 0, sortie écrite** | garde muette — m2 |
| qualificatif changé (« byte for byte » → « nearly ») | code 0, sortie écrite | attendu : le programme ne juge pas le sens — m2 |
| clé « nouveau » manquante | `KeyError: 'nouveau'`, **code 1** (pas 2), rien écrit | m3 |
| sortie = lien symbolique pendant | `FileExistsError`, **code 1** (pas 2), rien écrit | m3 |

## 2. Constats

### Bloquant

Aucun pour le couple 1 ni pour le programme. Le couple 2 ne doit pas être appliqué tel quel (M1) ; comme l'auteur recommande lui-même de ne pas l'appliquer (N-T4-1, option a), je classe M1 « majeur » et non « bloquant ». Il deviendrait bloquant si la mère retenait l'option (b).

### Majeur

**M1. Couple 2 (`nul_v9.py`) : le nouveau texte dit plus que les pièces, en prêtant à l'attaque du 2 novembre un constat qui n'est établi que pour la reprise du 5 novembre.**
- La phrase corrigée a pour sujet « l'attaque du 2 novembre » (`nul_v9.py` l. 9-10 : « l'attaque du 2 novembre l'a confirmé (monde W2 … ) : un proposeur modèle de langage … »).
- Les deux fondements cités par le couple portent sur la **reprise propre du 5 novembre** : page d'état l. 58 (« **Clean rerun (5 November 2026).** ») puis l. 63 (« 42 of the 48 promoted laws are, byte for byte, the world's own law: the proposer copies the two archive laws it is shown, one per sub-population ») ; page v7 l. 140 (« **Clean rerun in (5 Nov 2026 …** … **42 of the 48 reproduce the world's own law exactly** … and it needs no optimisation against the judge »).
- Sur le passage du 2 novembre, la page d'état (l. 69) dit seulement : « 12 of 24 units promoted … all 24 promoted laws replay above α after Holm's correction, none of them in the covered class », et « 11 of them at the first attempt with or without feedback, **so the share of the feedback is not measured** ». Rien n'y dit que le proposeur « recopie les deux lois connues », ni « pour la plupart des lois promues », ni qu'« aucune optimisation contre le juge n'y est nécessaire » ; la dernière affirmation est même en tension avec « not measured ».
- Le nouveau texte ajoute donc trois affirmations (la recopie, « la plupart », la non-nécessité de l'optimisation) là où l'ancien n'en portait qu'une fautive. Ce n'est pas « rien de plus que les pièces ». Le sens reste non flatteur, mais R4 ne dispense pas du fondement.
- Défaut second : ce commentaire d'en-tête décrit la raison d'être du fichier (« Pourquoi ») ; y loger un résultat postérieur (la page d'état dit la validation de v9 scellée le 3 novembre, donc le fichier antérieur à la reprise du 5) crée un anachronisme dans un fichier dont l'empreinte est citée.
- **Couple de remplacement proposé (non appliqué)** — retrait pur, aucune affirmation neuve, deux lignes pour deux lignes :
  - ancien (inchangé) : `un proposeur modèle de langage qui lit la description du juge y trouve une loi promue qui\nn'apporte rien au-delà de l'archive.`
  - nouveau : `un proposeur modèle de langage y fait promouvoir des lois qui n'apportent rien\nau-delà de l'archive.`
  - fondement : page d'état l. 69 (« breach under v8, through the uncovered class: 12 of 24 units promoted … all 24 promoted laws replay above α ») ; « n'apporte rien au-delà de l'archive » est déjà dans l'ancien texte et correspond au critère de nouveauté (page d'état l. 63, v7 l. 140) ; le pluriel suit « all 24 promoted laws ». Aucun chiffre, aucun mot sur la description du juge ni sur l'optimisation.
  - variante si la mère tient à citer la recopie : la dater explicitement (« ; à la reprise du 5 novembre, 42 des 48 lois promues recopient la loi du monde ») — mais cela ajoute des nombres au fichier et reste un ajout postérieur : je ne la recommande pas.

**M2. Nœud manquant : ordre et mot de Lazar.** R-2654 (registre, l. 2614) n'ordonne que la page v6, « retirer « reading its description is enough » de la ligne 140 ». Le journal v7 classe la l. 63 de la page d'état et `nul_v9.py` l. 9-12 en « Signalé, non changé », et traite un correctif voisin (C3) comme « hors de l'ordre de R-2654, soumis à Lazar ». Les deux couples sont donc **hors de l'ordre de R-2654** ; le journal de l'auteur cite R-2654 comme « formulation de référence » sans dire que l'application et la publication demandent un mot propre de Lazar. À écrire comme nœud (N-T4-3 ci-dessous).

### Mineur

**m1. Couple 1 (page d'état l. 63) : conforme.** « The breach needs no optimisation against the judge. » reprend v7 l. 140 (« a breach of the novelty criterion … and it needs no optimisation against the judge ») avec « The breach » pour sujet — reprise fidèle, pas « mot pour mot » au sens strict comme l'écrit le journal (§ 3). Même objet (reprise du 5 novembre, même puce « What the breach is »), antécédent immédiat (« 42 of the 48 … byte for byte »). Sens non flatteur : l'ancien texte prêtait au proposeur une lecture habile de la description ; le nouveau dit que la brèche s'obtient sans effort contre le juge. La moitié vraie de la phrase retirée (« not learned from its verdicts ») n'est pas perdue : l. 62, « feedback changes nothing (McNemar p = 1.0 after 1, 4 and 16 attempts) ». Réserve : « needs no optimisation » est une affirmation de nécessité, que la page d'état seule ne formule nulle part ; elle n'entre que par la page v7 (elle-même appuyée sur « 43 of 48 at the first attempt » et l'effet nul du retour). C'est admissible puisque la v7 est la référence, mais le correctif **importe** une phrase, il ne se borne pas à retirer. Variante strictement soustractive, si la mère la préfère : remplacer la phrase par « It is not learned from the judge's verdicts. » (fondée sur la l. 62 seule). Autres occurrences cherchées dans les deux fichiers nommés (`grep -n -i description`) : aucune autre phrase ne dit que le trou se lit sur la description (page d'état l. 10, 19, 52, 110 : autres sens ; `nul_v9.py` : l. 11 seule).

**m2. Programme : la garde « aucun chiffre changé » ne voit que les chiffres arabes.** `re.findall(r"\d+(?:[.,]\d+)*", x)` laisse passer un nombre en lettres (« two » → « three »), un signe ou un comparateur (« = » → « < »), une unité, un « % ». Démontré (§ 1.3, code 0, sortie écrite). Sans effet sur les deux couples livrés (relus à la main : aucun nombre en lettres ne change dans le couple 1 ; le couple 2 **ajoute** « deux lois », nombre en lettres fondé sur « the two archive laws », que la garde ne voit pas). La docstring (« aucun chiffre changé ») et le journal (« nombres inchangés ») devraient dire « chiffres arabes » ; le sens reste à la charge du lecteur.

**m3. Programme : deux sorties par exception (code 1, trace) au lieu de « refus, code 2 ».** Clé manquante dans le couple (`KeyError`) ; sortie qui est un lien symbolique pendant (`os.path.exists` rend faux, `open(…, "xb")` lève `FileExistsError`). Rien n'est écrit dans les deux cas : pas de danger, mais la docstring promet « Refus (code 2, rien écrit) ». De même une source non UTF-8 lèverait `UnicodeDecodeError`. Correction simple : valider les clés, et attraper `FileExistsError`.

**m4. Programme : le couple n'est pas lui-même vérifié.** Le programme lit `nouveau` sans contrôler l'empreinte du couple ; le compagnon `.sha256` existe mais rien n'oblige à le vérifier avant d'appliquer. Les champs `ligne` et `fichier_public` ne sont pas contrôlés non plus (le couple s'applique à tout fichier de même empreinte, quel que soit son nom ; `ligne` n'est qu'indicatif). À dire dans le mode d'emploi : `sha256sum -c` du couple avant application. Les gardes « ancien encore présent » et « octets hors du passage » sont justes ; la seconde est redondante avec `count == 1` + `replace`, sans défaut. Le test d'existence suivi de `open "xb"` est sûr (création exclusive). Aucun cas d'écriture sur la source trouvé.

**m5. Journal de l'auteur, § 4 : heure écrite à la main.** « Relevé de ce compte (2026-11-14, vers 09:05Z) » : l'interdit permanent dit « jamais d'heure écrite à la main (`date -u` dans la même commande) ». À remplacer par une sortie de `date -u` ou à retirer.

**m6. Journal, § 1 et § 3 : citations vérifiées.** La citation du journal v7 est exacte ; la citation de v7 l. 140 est exacte au gras près ; R-2654 exacte ; page d'état l. 64 cite bien `7ae450df…` (vu). Non vérifié par moi (hors de ma liste de fichiers) : `verification-courte-page-v6.md` (`8c2dc416…`), l'égalité avec le clone public à `bdf6bc4`, `e7daf32`, `516feca`, PO-006.

**m7. Hors sujet, signalé seulement.** `nul_v9.py` l. 4-6 dit encore « Brouillon de conception, **non validé** … préenregistrement … brouillon1 (non scellé) », alors que la page d'état dit la validation scellée le 3 novembre et rendue. Même famille de défaut (commentaire périmé), même nœud d'empreinte : à traiter ensemble si le fichier est un jour touché.

## 3. Réponses aux quatre questions

(a) **Fondement.** Couple 1 : oui, par v7 l. 140, avec la réserve m1 (phrase importée, non présente dans la page d'état). Couple 2 : **non** — M1.
(b) **Sens non flatteur.** Oui pour les deux : chacun retire une affirmation non établie qui prêtait à l'attaque une finesse (lire le trou sur la description) et la remplace par plus banal. Le couple 2 pèche par excès d'affirmation, pas par flatterie.
(c) **Programme.** Correct pour les deux couples livrés ; déterministe ; n'écrit jamais sur la source ; refuse les cas demandés. Défauts : m2 (garde des nombres partielle), m3 (codes de sortie), m4 (couple non vérifié). Aucun ne change les deux sorties.
(d) **Nœuds.** N-T4-1 est bien posé, et je rejoins la recommandation (a) — ne pas toucher `nul_v9.py` — avec une confiance plus forte que « moyenne » : M1 s'y ajoute, le fichier dit de lui-même « Fichier neuf (R12) : aucun fichier existant n'est modifié », et son empreinte est citée sur la page d'état l. 64. N-T4-2 est bien posé mais trop vague. Il manque :
- **N-T4-3 (mot de Lazar).** Les deux couples sont hors de l'ordre de R-2654 (M2) : rien n'est appliqué ni poussé sans un mot propre.
- **N-T4-4 (dépendance des deux couples).** Si le couple 2 était appliqué, la l. 64 de la page d'état (empreinte `7ae450df…` de `nul_v9.py`) deviendrait fausse : il faudrait un troisième couple sur la page d'état, et l'empreinte `737a208a…` de la page corrigée ne tiendrait plus. Le journal donne les deux empreintes de sortie comme indépendantes ; elles ne le sont que sous l'option (a).
- **N-T4-5 (préciser N-T4-2).** Nommer les lieux à relever : le MANIFEST de la page (le journal v7 dit « MANIFEST et page R1 égaux à la v6 » : s'il liste les empreintes des fichiers publics, il change avec la page d'état) et les journaux de page qui citeraient `c549a31b…`. Non vérifié par moi (hors de ma liste).
- **N-T4-6 (erratum de l'option a).** La « phrase neuve » sur la page d'état disant que le commentaire de `nul_v9.py` est fautif n'est pas rédigée : c'est un texte public neuf, à écrire, à relire par un second lecteur, et il changera encore l'empreinte de la page d'état (donc `737a208a…` n'est pas l'empreinte finale sous l'option a non plus). Proposition, non appliquée, à placer après la phrase corrigée de la l. 63 ou dans la puce « Fix » : « The header comment of `nul_v9.py` (lines 11–12) says that the proposer finds the hole by reading the judge's description; the runs do not establish that, and the file is left unchanged so that its hash stays the one cited here. »

## 4. Ce que je n'ai pas fait

Aucune lecture hors des neuf pièces nommées (plus un `ls` non récursif du dossier de sortie, pour vérifier que ce fichier n'existait pas). Pas de recherche des citations d'empreintes (interdite : pas de recherche récursive). Les couples de remplacement ci-dessus ne sont ni écrits en JSON ni appliqués.

Heure de fin (`date -u`, écrite par la commande) :
Sat Nov 14 09:10:37 UTC 2026

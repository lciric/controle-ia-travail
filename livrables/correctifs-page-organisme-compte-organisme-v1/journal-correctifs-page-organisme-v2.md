# Correctifs de la page publique de l'organisme — compte organisme — journal v2

Version 2 (R12 : `journal-correctifs-page-organisme-v1.md`, `b5ab0ea1…`, reste en place). Elle porte la lecture du second
lecteur (`lecture-second-lecteur-correctifs-page-v1.md`, auteur des couples : modèle A ; lecteur : modèle B ; A ≠ B ; verdict
« conforme avec réserves ») : couple 2 refait (M1), nœud du mot de Lazar ajouté (M2), programme refait (m2 à m4), nœuds précisés.
Heure de ce journal (`date -u`) : 2026-11-14T09:12:42Z. **Rien n'est poussé vers le dépôt public ; rien n'y est écrit.**

## 1. Pièces de ce dossier (toutes scellées, chacune égale à son compagnon)

| pièce | rôle | état |
|---|---|---|
| `couple-resultats-attaque-goodhart-v2-README-v1.json` (`6c5cfe9b…`) | page d'état, ligne 63 : « The hole is read off the judge's description, not learned from its verdicts. » → « The breach needs no optimisation against the judge. » | **proposé** (lecteur : conforme ; phrase reprise de la page v7, ligne 140, sujet changé, réserve m1 : elle importe une phrase de la v7) |
| `couple-orchestrator-pole-nul_v9-v1.json` (`df42455a…`) | `nul_v9.py`, lignes 11-12, première rédaction | **retiré** (M1 : prêtait à l'attaque du 2 novembre des constats de la reprise du 5 novembre) ; gardé (R12) |
| `couple-orchestrator-pole-nul_v9-v2.json` (`23be77bc…`) | `nul_v9.py`, lignes 11-12 : « un proposeur modèle de langage qui lit la description du juge y trouve une loi promue qui / n'apporte rien au-delà de l'archive. » → « un proposeur modèle de langage y fait promouvoir des lois qui n'apportent rien / au-delà de l'archive. » (retrait pur, proposé par le lecteur) | **proposé, à n'appliquer que sur l'option (b) de N-T4-1** |
| `appliquer_correctifs_page_v1.py` (`8211ac10…`) | programme v1 | remplacé (m2 à m4) ; gardé |
| `appliquer_correctifs_page_v2.py` (`70935286…`) | programme v2 | **défaut trouvé à son propre essai** : il comptait l'article « une » comme un nombre et refusait à tort le couple `nul_v9` v2 ; gardé (R12) |
| `appliquer_correctifs_page_v3.py` (`093146e8…`) | programme v3 : couple égal à son compagnon et complet ; nombres en chiffres et en lettres (anglais, français, articles « un », « une » exclus) et signes `% = < > ≤ ≥ ± α` ; liens symboliques, source non UTF-8, sortie apparue entre contrôle et écriture : refus nommés | **en vigueur** |
| `lecture-second-lecteur-correctifs-page-v1.md` | lecture du modèle B | versée |

Variante strictement soustractive du couple 1, proposée par le lecteur (non écrite en couple) : « It is not learned from the
judge's verdicts. » (fondée sur la ligne 62 seule) ; à choisir par la mère si elle préfère ne rien importer de la page v7.

## 2. Rejeu par le programme v3 (deux passages par couple, sorties hors des dépôts)

Commande : `python3 -I appliquer_correctifs_page_v3.py COUPLE.json SOURCE SORTIE` ; sources : `livrables/page-publique-organisme-2026-11-10-v1/resultats/attaque-goodhart-v2/README.md`
(`c549a31b…`) et `orchestrator/pole/nul_v9.py` de l'arbre reconstruit (`7ae450df…`).

| couple | sortie (deux passages égaux, `cmp`) | « ancien » restant | `diff` |
|---|---|---|---|
| page d'état v1 | `737a208ad23b875680f3f315a06363d57d73a263d14dc7835968459703406e77` | 0 | ligne 63 seule |
| `nul_v9` v2 | `9920fcce46ea02114647accd7434c87cb1af4d95ceb02b9acdd4ebbab60c915c` | 0 | lignes 11-12 → 11-12 ; `ast.parse` sans erreur |

Artefacts refusés (code 2, rien écrit) : source déjà corrigée ; « two » ajouté ; « = » ajouté ; couple sans « nouveau » ; couple
différent de son compagnon ; « ancien » absent.

## 3. Nœuds pour la mère (format de la section 8 du brief)

- **N-T4-3 — mot de Lazar (bloquant).** Décision : appliquer (ou non) des correctifs à la page publique hors de l'ordre de R-2654,
  qui ne visait que la ligne 140 de la v6. Enjeu : publication. Options : (a) soumettre les couples à Lazar pour un mot propre ;
  (b) attendre la prochaine version de la page. Recommandation : (a), confiance élevée. Sans défaut (publication).
- **N-T4-1 — `nul_v9.py`.** Décision : toucher ou non le commentaire. Enjeu : l'empreinte `7ae450df…` est citée par la page
  d'état (ligne 64) et peut l'être par des pièces scellées (préenregistrement de la validation de v9) ; le fichier dit de lui-même
  « Fichier neuf (R12) : aucun fichier existant n'est modifié ». Options : (a) ne pas le toucher, et dire l'erratum sur la page
  d'état (N-T4-6) — avantage : aucune empreinte citée ne change ; inconvénient : le commentaire fautif reste dans le code public ;
  (b) appliquer le couple v2 et mettre à jour toutes les citations de l'empreinte (troisième couple sur la ligne 64, et la page
  corrigée change encore d'empreinte : N-T4-4). Recommandation : **(a)**, confiance élevée (le lecteur la rejoint). Défaut : la
  mère seule.
- **N-T4-4 — dépendance.** Les deux sorties ne sont indépendantes que sous l'option (a) : sous (b), la ligne 64 de la page d'état
  devient fausse et `737a208a…` n'est pas l'empreinte finale.
- **N-T4-5 — lieux à relever** (précise N-T4-2 du journal v1) : le MANIFEST de la page publique, s'il liste les empreintes des
  fichiers publics, et tout journal de page qui cite `c549a31b…`. **Ce compte ne les relève pas** : la recherche des citations
  dans l'arbre public lui a été refusée par le classifieur (PO-006, non rejouée).
- **N-T4-6 — erratum (option a).** Texte public neuf, à relire par un second lecteur, qui change encore l'empreinte de la page
  d'état. Proposition du lecteur, non appliquée, après la phrase corrigée de la ligne 63 ou dans la puce « Fix » : « The header
  comment of `nul_v9.py` (lines 11–12) says that the proposer finds the hole by reading the judge's description; the runs do not
  establish that, and the file is left unchanged so that its hash stays the one cited here. »
- Signalé, hors sujet (lecteur, m7) : `nul_v9.py` lignes 4 à 6 disent encore « non validé … brouillon1 (non scellé) » ; même nœud
  d'empreinte, à traiter ensemble si le fichier est un jour touché.

## 4. Écart de forme du journal v1, dit

Le journal v1 (§ 4) écrit une heure à la main (« vers 09:05Z ») : contraire à l'interdit permanent ; non corrigé dans la v1
(scellée), corrigé ici (heure de `date -u` en tête).

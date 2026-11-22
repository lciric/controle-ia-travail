# Relecture par Claude Fable 5.2 (appel direct à l'interface d'Anthropic)

- Outil : `controle_ia.relecture_fable_api_v5` (empreinte du module 052ea1e2c66f8b80b1724db9f0c5afb27a48cc01eac2e1e5210658ca8423bdb8)
- Modèle demandé : `claude-fable-5-2` ; modèle servi : `claude-fable-5-2` ; identifiant du message : `msg_011ChHtiaQ9G9DFZqDC7fLQv`
- Heure (UTC) : 2026-11-22T11:35:13Z
- Réglages : effort `max`, réflexion adaptative à affichage « omitted » (texte de la réflexion ni demandé ni écrit), `max_tokens` 128000, aucune relance, aucun repli vers un autre modèle, budget de tâche 96000 jetons (bêta `task-budgets-2026-03-13` ; cible indicative vue par le modèle, pas une borne : seul `max_tokens` arrête)
- Entrées :
  - consigne : `docs/notes/relecture-plantee-etapes-0-v1/lot-lois-plantees-reduit-v1/consigne-relecture-lois-plantees-reduit-v1.md` — sha256 8acea7cc0658cd1c64c56c56b90cb023c3b4396f03300318037b03da0e9de281 (compagnon : vérifié)
  - correction : `docs/notes/relecture-plantee-etapes-0-v1/lot-lois-plantees-reduit-v1/conception-etape-0-lois-plantees-v1-erratum-1.md` — sha256 45179b0acff7d37158ce2a4ea975be710a3785967d957ab0d31008514fbda331 (compagnon : vérifié)
  - correction : `docs/notes/relecture-plantee-etapes-0-v1/lot-lois-plantees-reduit-v1/preenregistrement-admission-etape-0-lois-plantees-v1-brouillon-erratum-1.md` — sha256 436dd82a842dfdcb9becb6d8ad5a44a8e08fdc4e5a9b6e7ac6b313c1f1b176f7 (compagnon : vérifié)
  - remarques : `docs/notes/relecture-plantee-etapes-0-v1/lot-lois-plantees-reduit-v1/contre-lecture-etape-0-lois-plantees-v1-opus-v1.md` — sha256 e8b3b7f7b545b881d7b5338d70b87a38145dc358cecb7c1320010e6253a545bc (compagnon : vérifié)
- Empreinte de l'invite envoyée : 493c49e780e695101dc499916d07b69f436984b850f49a7f3a43f64a346de1f9
- Jetons : entrée 55252, sortie 20985 (dont réflexion 18650), écriture de cache 0, lecture de cache 0 ; raison d'arrêt `end_turn`
- Coût compté : 1.281416 USD (base : usage ; tarif 8 / 40 USD par million de jetons d'entrée / de sortie)

---
à corriger (3 points)

| remarque | lieu de la correction | état | motif |
|---|---|---|---|
| B-1 | P-21, P-26, P-32, P-34 (5), P-37 (12, 13, 16) ; C-9, C-10 | conforme | |
| B-2 | P-1, P-4, marques de P-5 à P-41 ; C-4 | à corriger | Quatre passages dépendent de D-4 d'après l'erratum lui-même (P-10, ligne 11 du banc ; P-41, verdict 22 ; P-37, ligne 9) et n'en portent pas la marque que P-1 promet. |
| B-3 | P-41, P-34 (5), P-37, P-2, P-22 | conforme | |
| I-1 | P-7, P-22 ; C-3, C-6 | conforme | |
| I-2 | P-10 | conforme | |
| I-3 | P-6, P-36, P-37 (1, 3) | conforme | |
| I-4 | P-6, P-12, P-21, P-23, P-34 (6), P-35, P-37 (1, 2) ; C-5 | conforme | |
| I-5 | P-6, P-23, P-37 (1) ; C-2, C-5 | conforme | |
| I-6 | P-39 | à corriger | La preuve de la garde 2 ajoute « et des tirages » et « postérieur à celui de l'écriture des issues », que la remarque ne donne pas et qui ne sont pas en nœud ouvert. |
| I-7 | P-33, P-34 (1, 2, 4) | conforme | |
| I-8 | C-11 | conforme | |
| I-9 | C-7 ; P-11 | à corriger | La liste des lieux omet le § 8 (D-3, D-4), que la remarque nomme. |
| I-10 | C-1, C-12, C-13, C-14, C-15 ; P-1, P-4, P-27 | conforme | |
| M-1 | P-25 | conforme | |
| M-2 | P-3 | conforme | |
| M-3 | C-16, C-17 | conforme | |
| M-4 | P-19 ; C-8 | conforme | |
| M-5 | C-9 | conforme | |
| M-6 | P-38 | conforme | |

Pièce d'avant nécessaire : brouillon, tableau des prédictions et section Seuil. Pour B-3, je ne peux pas juger si P-41 et P-37 (ligne 1) reprennent un critère existant quand ils comptent la table des cinq traits « à 0,500, d'erreur type nulle » (verdict 5) et la longueur dans la bande (verdict 15, absente des lignes 9 et 10).

Ajouts sans remarque :
- P-40 et la première phrase de P-1 : la section Contre-lecture est réécrite et le statut passe à « contre-lu » ; « vérification des corrections » devient « relecture des corrections ». L'erratum le déclare « sans remarque » (procédure du gabarit).
- C-7 et P-11 : l'interdit est étendu au programme v1, à sa sortie et au § 4.4, que I-9 ne nomme pas. L'extension est déclarée « étendue » mais n'est pas écrite en nœud ouvert.
- P-21 : le niveau 0,0009 est prêté à une troisième règle de la queue (devin à uns-chauds) sous l'étiquette [calcul, F], alors que la sortie v2 ne le calcule pas pour ce devin.

**Point 1 — B-2 (marques D-4), erratum du texte d'admission**

P-37, ligne 11. Ancien :
````text
| 11 | Dose de budget non vue, ou retrait non signalé | **épreuve aveugle** |
````
Nouveau :
````text
| 11 | Dose de budget non vue, ou retrait non signalé [en attente du mot du directeur : D-4] | **épreuve aveugle** |
````

P-37, ligne 16, première colonne. Ancien :
````text
| 16 | **Issue d'ensemble**, écrite par programme après les lignes 1 à 15 (remarque B-1) [en attente du mot du directeur : D-2, D-3] |
````
Nouveau :
````text
| 16 | **Issue d'ensemble**, écrite par programme après les lignes 1 à 15 (remarque B-1) [en attente du mot du directeur : D-2, D-3, D-4] |
````

P-21, nouveau texte. Ancien :
````text
(critères, ligne 16) [en attente du mot du directeur : D-2, D-3].
````
Nouveau :
````text
(critères, ligne 16) [en attente du mot du directeur : D-2, D-3, D-4].
````

P-36, nouveau texte, dernière phrase. Ancien :
````text
**Épreuve de la dose** : la dose de budget, le retrait et l'ajout dans le registre contre les doses hors du budget.
````
Nouveau :
````text
**Épreuve de la dose** [en attente du mot du directeur : D-4] : la dose de budget, le retrait et l'ajout dans le registre contre les doses hors du budget.
````

**Point 2 — I-6, erratum du texte d'admission, P-39, nouveau texte**

Ancien :
````text
garde 2, l'empreinte de la racine d'admission déposée au registre avant l'exécution, et l'horodatage de la remise de la racine et des tirages au concepteur, postérieur à celui de l'écriture des issues ;
````
Nouveau :
````text
garde 2, l'empreinte de la racine d'admission déposée au registre avant l'exécution, et l'horodatage de la remise au concepteur ; l'instant auquel cet horodatage se compare, et si les tirages sont remis avec la racine : nœud ouvert, au concepteur ;
````

**Point 3 — I-9, les deux errata**

Erratum de la conception, C-7, nouveau texte, première phrase. Ancien :
````text
Le § 0, le § 4.4, le § 5.3 à 5.7 et le § 9 en reprennent les noms : même précaution.
````
Nouveau :
````text
Le § 0, le § 4.4, le § 5.3 à 5.7, le § 8 (D-3, D-4) et le § 9 en reprennent les noms : même précaution.
````

Erratum du texte d'admission, P-11, nouveau texte. Ancien :
````text
les passages de la conception qui en reprennent les noms (§ 0, § 4.4, § 5.3 à 5.7, § 9)
````
Nouveau :
````text
les passages de la conception qui en reprennent les noms (§ 0, § 4.4, § 5.3 à 5.7, § 8 (D-3, D-4), § 9)
````

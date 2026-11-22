# Relecture par Claude Fable 5.2 (appel direct à l'interface d'Anthropic)

- Outil : `controle_ia.relecture_fable_api_v5` (empreinte du module 052ea1e2c66f8b80b1724db9f0c5afb27a48cc01eac2e1e5210658ca8423bdb8)
- Modèle demandé : `claude-fable-5-2` ; modèle servi : `claude-fable-5-2` ; identifiant du message : `msg_011ChHtiaP9WMmYZokSsbNed`
- Heure (UTC) : 2026-11-22T11:34:42Z
- Réglages : effort `max`, réflexion adaptative à affichage « omitted » (texte de la réflexion ni demandé ni écrit), `max_tokens` 128000, aucune relance, aucun repli vers un autre modèle, budget de tâche 96000 jetons (bêta `task-budgets-2026-03-13` ; cible indicative vue par le modèle, pas une borne : seul `max_tokens` arrête)
- Entrées :
  - consigne : `docs/notes/relecture-plantee-etapes-0-v1/lot-dommages-tiers-reduit-v1/consigne-relecture-dommages-tiers-reduit-v1.md` — sha256 16f635ec61f9b72747b0bd0049a494a20c852c3888e6a66003be6d14ac413cd5 (compagnon : vérifié)
  - correction : `docs/notes/relecture-plantee-etapes-0-v1/lot-dommages-tiers-reduit-v1/etalonnage-sur-banc-lois-plantees-v2-erratum-1.md` — sha256 ef0584d801bb68d5d9669c720331044d4bc98c00a63cbc78ef116a95466b3cbc (compagnon : vérifié)
  - correction : `docs/notes/relecture-plantee-etapes-0-v1/lot-dommages-tiers-reduit-v1/gardes-de-la-course-v1-erratum-1.md` — sha256 2a63442bd6866495fa570b50d3f0d936c8a307b78f5f10dfdb0fcdd04c73f8f6 (compagnon : vérifié)
  - correction : `docs/notes/relecture-plantee-etapes-0-v1/lot-dommages-tiers-reduit-v1/mandat-neutre-planteurs-v2-erratum-1.md` — sha256 711aeacddf092e6966a54ab3c51593aa53af38e59b40ab1c9e970b3f15216137 (compagnon : vérifié)
  - correction : `docs/notes/relecture-plantee-etapes-0-v1/lot-dommages-tiers-reduit-v1/preenregistrement-campagne-dommages-tiers-etape-0-v2-brouillon-erratum-1.md` — sha256 72609ed88b8d542ca9ca082f5989c6c05f6a7822754a6e88fd1de7386d37db30 (compagnon : vérifié)
  - correction : `docs/notes/relecture-plantee-etapes-0-v1/lot-dommages-tiers-reduit-v1/specification-depouillement-v2-erratum-1.md` — sha256 1f3529f202f81c53df438a7f21efe7526a0a82e8730a51c16149834cb22dc99a (compagnon : vérifié)
  - correction : `docs/notes/relecture-plantee-etapes-0-v1/lot-dommages-tiers-reduit-v1/extrait-differences-calculs-etape-0-dommages-tiers-v3-contre-v2-py-v1.md` — sha256 01c9e8cde967c6b276fd3a9e18687e66c3cc20fb186d1e24cbfd74d00f6ff7d1 (compagnon : vérifié)
  - correction : `docs/notes/relecture-plantee-etapes-0-v1/lot-dommages-tiers-reduit-v1/extrait-differences-calculs-etape-0-dommages-tiers-v3-contre-v2-txt-v1.md` — sha256 1c83986ac9dcbe9da8b76f2ad73b0d035cefa68079c5b441c8f512332eb7b87c (compagnon : vérifié)
  - remarques : `docs/notes/relecture-plantee-etapes-0-v1/lot-dommages-tiers-reduit-v1/verification-corrections-etape-0-dommages-tiers-v2-opus-v1.md` — sha256 66615adf5ca00f7d924373d1e77a4813e3bac9f255e590f73afcc6a27fba7bdc (compagnon : vérifié)
  - remarques : `docs/notes/relecture-plantee-etapes-0-v1/lot-dommages-tiers-reduit-v1/lecture-mere-portee-go-69-dommages-tiers-v1.md` — sha256 ee624ede488c7d801c5726b02f04d50bbd0156fd47f849075799ded482cbd03c (compagnon : vérifié)
- Empreinte de l'invite envoyée : 7197ebcbc653e61b80702f7b1488d1dced6e04b2052c3bfb79589cc0fe887c8e
- Jetons : entrée 62001, sortie 17426 (dont réflexion 15185), écriture de cache 0, lecture de cache 0 ; raison d'arrêt `end_turn`
- Coût compté : 1.193048 USD (base : usage ; tarif 8 / 40 USD par million de jetons d'entrée / de sortie)

---
**à corriger (2 points)**

| Remarque | Lieu de la correction | État | Motif |
|---|---|---|---|
| V-1 | brouillon B-10 ; gardes G-2, G-4 ; calculs v3, bloc L | conforme | |
| V-2 | brouillon B-2 à B-9, B-14 à B-17 ; spécification S-1 à S-26 ; étalonnage E-1 à E-4 ; mandat M-1 | à corriger | La table de l'erratum de la spécification range V-2 sous « S-1 à S-14 bis, S-16 à S-26 », alors que S-15 se déclare « V-2, V-5 » et que le tableau final du brouillon écrit « S-1 à S-26 ». |
| V-3 | brouillon B-2, B-17 ; gardes G-1, G-3, G-5 ; mandat M-1, M-3 | à corriger | V-3 demande un nœud et l'ancien texte dit « Ce n'est pas à la campagne de choisir », mais N-14 est écrit « Tranché » sur un mandat de la mère qu'aucune pièce jointe ne porte. |
| V-4 | mandat M-2 | conforme | |
| V-5 | brouillon B-7, B-8 ; spécification S-7, S-15 | conforme | |
| V-6 | brouillon B-11 à B-13 | conforme | |
| V-7 | gardes G-2, G-4 ; brouillon B-10 ; calculs v3, bloc L | conforme | |
| V-8 | étalonnage E-5 ; calculs v3, bloc K | conforme | |
| Verdict : N-14 à ajouter | brouillon B-17 | voir V-3 | |
| Verdict : points 2 à 4 et inscription de la vérification | brouillon B-1, B-18 | conforme | |
| Lecture de la mère, point 1 (D-4, D-9, D-10) | brouillon B-3, B-15 | conforme | |
| Lecture de la mère, point 2 (D-5, D-7) | brouillon B-3, B-15 ; mandat M-1, M-3 | conforme | |
| Lecture de la mère, point 3 (D-1, D-2, D-3, D-6 ; mention) | brouillon B-3 à B-7, B-9, B-14 ; spécification S-1, S-4, S-5, S-7, S-11 ; étalonnage E-1 | conforme | |
| Lecture de la mère, point 4 (N-10) | brouillon B-7 à B-9, B-16 ; spécification S-7 | conforme | |
| Lecture de la mère, « Ce qui ne change pas » (garde du prix) | gardes G-4 ; brouillon B-10 | conforme | |

Trois lieux ne se jugent pas sans une pièce non jointe :

- pièce d'avant nécessaire : calculs v2, bloc C, dernière phrase. G-4 et le bloc L y prennent l'ordre d'abandon (« le complément d'abord »), alors que les NOTES [v3], point 1, disent cette même phrase remplacée.
- pièce d'avant nécessaire : spécification v2, § 5.1 et 5.3, artefacts 5A bis et 12A bis (S-17, S-23). Je ne peux pas dire ce qu'ils discriminent encore une fois le nombre d'épisodes ôté.
- pièce d'avant nécessaire : note source, § 8, D-5 (a). M-1 en écrit le contenu (« deux modèles de deux lignées hors de celles des lecteurs, sessions isolées, plants en quarantaine »).

Calculs v3 : chaque bloc de fond répond à un constat nommé, et aucun nombre cité par un erratum ne diffère de la sortie extraite.

- **NOTES [v3]** : V-1 et V-2, avec la lecture de la mère.
- **Bloc K** : V-8, plus l'ajout listé ci-dessous.
- **Bloc L** : V-1 et V-7.
- **Tête, ligne de rejeu, ligne de titre** : marques de version, sans constat.

Ajouts sans remarque :

- Étalonnage E-5 et bloc K : les dix plafonds du critère 3 (0,004230) et le total des critères 2 à 4 (0,016896). L'ajout est déclaré, mais il va au-delà de V-8, qui ne nomme que les seize intervalles.
- Brouillon B-17 et gardes G-5 : « « à l'octet » s'entend d'un appel qui passe cette garde ». C'est une lecture de l'appel de production que ni V-3 ni la lecture de la mère n'écrivent (voir la correction 2).
- Gardes G-1, G-3, G-5 et mandat M-3 : le détail de la garde commune n'est vérifiable dans aucune pièce jointe. Il s'agit des noms `verifier_reglages_google` et `defaut_reponse_google`, de « la réflexion plus 16 000 jetons de texte », et des motifs de fin « MAX_TOKENS », « SAFETY », « RECITATION ».

**Correction 1.** Pièce : erratum 1 de la spécification du dépouillement. Lieu : table « Remarque par remarque », ligne V-2, colonne « Points ».

Ancien texte :

> S-1 à S-14 bis, S-16 à S-26

Nouveau texte :

> S-1 à S-26

**Correction 2.** Pièce : erratum 1 du brouillon v2 du préenregistrement. Lieu : B-17, nœud N-14, deux passages.

Ancien texte (premier passage) :

> *Tranché* (mandat de la mère sous `GO-2026-11-21-84`, d'après la règle permanente de `CLAUDE.md`, « Appels aux modèles de Google », `GO-2026-11-21-71`) :

Nouveau texte :

> *Appliqué d'ici le mot du directeur, non tranché* (règle permanente de `CLAUDE.md`, « Appels aux modèles de Google », `GO-2026-11-21-71`) :

Ancien texte (second passage) :

> *Reste ouvert* : qui corrige alors le gabarit, quand, et par quelle chaîne ;

Nouveau texte :

> *Reste ouvert* : si « à l'octet » peut s'entendre d'un appel qui passe cette garde ; qui corrige alors le gabarit, quand, et par quelle chaîne ;

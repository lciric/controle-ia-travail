# Rapport de vérification de la couche 15 — couples du brouillon 4 vers le brouillon 5 du texte de lecture des sondes par lentille neuronale — v1

- Modèle : Opus 4.6 (`claude-opus-4-6`), lecteur neuf désigné par Lazar (mot « lecteur opus 4.6 », GO-2026-11-19-39 et GO-2026-11-19-42).
- Heure UTC : 2026-11-20.
- Je n'ai écrit ni le texte de lecture, ni le critère d'identité, ni le verdict de la tranche.

## Empreintes recalculées

| pièce | empreinte attendue | empreinte recalculée | statut |
|---|---|---|---|
| `rapport-verification-bloc-v-v1.md` (rapport du lecteur précédent) | `4e1fe2d7aa76f4cefe717298f98c5368e33a1a5992743d48232c96b6785f5358` (compagnon `.sha256`) | `4e1fe2d7aa76f4cefe717298f98c5368e33a1a5992743d48232c96b6785f5358` | conforme |
| `couples-brouillon4-vers-brouillon5-v1.py` (script des couples) | `b969a89802dc27875f7a1fb0facd9ae7f1cbaf9695a764e76cfd8558a9b75ef8` (compagnon `.sha256`) | `b969a89802dc27875f7a1fb0facd9ae7f1cbaf9695a764e76cfd8558a9b75ef8` | conforme |
| sortie du script des couples | `c9e2656b01e1cf28a7a74ddad90154abe98911c7c02cb412793c8a97919bc028` (compagnon `.sha256` de `sortie-couples-brouillon4-vers-brouillon5-v1.txt`) | `c9e2656b01e1cf28a7a74ddad90154abe98911c7c02cb412793c8a97919bc028` | conforme |
| `verdict-b-beta-v1.md` (verdict V) | `3a9b947e0757dd7f5fe7ecb418b047b94fb274fed84672accabc48926660bb78` | `3a9b947e0757dd7f5fe7ecb418b047b94fb274fed84672accabc48926660bb78` | conforme |
| `lecture-sondes-bbis-par-lentilles-v2-candidat.md` (candidat v2, sur `origin/main`) | `39118ac138dee5ddb21142d1f8cdda6b005e15e0d156b6abaadbbb30d47fef8a` | `39118ac138dee5ddb21142d1f8cdda6b005e15e0d156b6abaadbbb30d47fef8a` | conforme |

## Vérification des couples de la couche 15

Les couples vérifiés sont L16, L17, L18 et L19 (portant sur la couche 15 dans le verdict V) ; L12 et L15 sont donnés pour information.

Le verdict V cite la couche 15 de la mesure B-7 (lecture contre ablation par fenêtre) à la **ligne 30**, dans la section **« Verdict, en mots simples »** (ligne 14 du verdict), table commençant ligne 22. Le **libellé** (colonne « verdict ») de B-7 est **« autre »**. La description de B-7 se termine par : « la lecture prédit mal l'effet d'une activation en contexte jusqu'à la couche 14, la couche 15 est intermédiaire, bien tard ». La valeur chiffrée est 0,3112.

Pour comparaison, le libellé « intermédiaire » appartient à la mesure **B-6** (ligne 29 du verdict), pas à B-7.

### Couple L16 — lieu cité dans V pour la réserve (R-c)

| | texte |
|---|---|
| avant (brouillon 4) | `dans les mots de V (§ 2, ligne B-7) :` |
| après (brouillon 5) | `dans les mots de V (« Verdict, en mots simples », table, ligne B-7, dont le libellé est « autre ») :` |
| lieu dans V | section « Verdict, en mots simples » (ligne 14), table, ligne B-7 (ligne 30 du fichier) |
| ligne de V | 30 |
| libellé de V pour B-7 | « autre » (colonne « verdict », ligne 30) |
| valeur chiffrée | aucune dans ce couple |
| **statut** | **conforme** — le lieu « Verdict, en mots simples » et le libellé « autre » correspondent au verdict ; le brouillon 4 citait « § 2 » qui ne désigne pas cette section dans V |

### Couple L17 — ce que V dit de la couche 15 dans la réserve (R-c)

| | texte |
|---|---|
| avant (brouillon 4) | `**à la couche 15, V la dit « intermédiaire »** — « intermédiaire » au sens de V pour cette seule mesure, sans rapport avec le libellé « intermédiaire » de la lecture par concentration de ce texte (« Seuil ») ;` |
| après (brouillon 5) | `**à la couche 15, V la dit « intermédiaire, bien tard »** — mot de la description de V pour cette seule mesure, dont le libellé est « autre » : ce n'est ni le libellé « intermédiaire » que V donne à la mesure B-6, ni le libellé « intermédiaire » de la lecture par concentration de ce texte (« Seuil ») ;` |
| lieu dans V | section « Verdict, en mots simples », table, ligne B-7 (ligne 30) : « la couche 15 est intermédiaire, bien tard » |
| ligne de V | 30 |
| libellé de V pour B-7 | « autre » ; « intermédiaire » est un mot de la description, pas le libellé |
| libellé « intermédiaire » dans V | appartient à B-6 (ligne 29) |
| valeur chiffrée | aucune dans ce couple (la valeur 0,3112 n'y figure pas directement) |
| **statut** | **conforme** — la citation « intermédiaire, bien tard » est exacte (ligne 30 de V), le libellé « autre » est exact, et la distinction avec le libellé « intermédiaire » de B-6 est correcte |

### Couple L18 — bloc séparable, déclaration du brouillon 5

| | texte (extrait de la partie ajoutée) |
|---|---|
| avant (brouillon 4) | pas de mention « Brouillon 5 » |
| après (brouillon 5, ajout) | `**Brouillon 5** (contre-lecture 4, B2) : à ces deux endroits, le lieu cité dans V (« Verdict, en mots simples », table, ligne B-7, et non « § 2 ») et le libellé de V pour cette mesure (« autre » ; « intermédiaire, bien tard » est un mot de sa description) sont corrigés ; les mots cités de V et toutes les valeurs chiffrées restent les mêmes (couples L16, L17 et L19 des pièces de fabrication du brouillon 5 ; le troisième est dans ce bloc).` |
| lieu dans V | « Verdict, en mots simples », table, ligne B-7 (ligne 30) |
| ligne de V | 30 |
| libellé de V pour B-7 | « autre » |
| valeur chiffrée | aucune dans ce couple |
| **statut** | **conforme** — le lieu, le libellé et la description « intermédiaire, bien tard » sont exacts ; « § 2 » est correctement désigné comme l'ancien lieu erroné |

### Couple L19 — bloc séparable, colonne « ce qui en suit » de la ligne « lecture contre ablation par fenêtre »

| | texte |
|---|---|
| avant (brouillon 4) | `(V, § 2, ligne B-7 : « la lecture prédit mal l'effet d'une activation en contexte jusqu'à la couche 14, la couche 15 est intermédiaire, bien tard » ; « intermédiaire » au sens de V pour cette mesure, la mesure B-7 de G, sans rapport avec le libellé « intermédiaire » de la lecture par concentration de ce texte) \|` |
| après (brouillon 5) | `(V, « Verdict, en mots simples », table, ligne B-7, libellé « autre » : « la lecture prédit mal l'effet d'une activation en contexte jusqu'à la couche 14, la couche 15 est intermédiaire, bien tard » ; « intermédiaire » est ici un mot de la description de V pour la mesure B-7 de G, ni le libellé « intermédiaire » de la mesure B-6 de V, ni celui de la lecture par concentration de ce texte) \|` |
| lieu dans V | « Verdict, en mots simples », table, ligne B-7 (ligne 30) |
| ligne de V | 30 |
| libellé de V pour B-7 | « autre » |
| citation de V | « la lecture prédit mal l'effet d'une activation en contexte jusqu'à la couche 14, la couche 15 est intermédiaire, bien tard » — fin exacte de la ligne 30 du verdict |
| valeur chiffrée | aucune dans ce couple |
| **statut** | **conforme** — le lieu, le libellé, la citation et la distinction avec le libellé « intermédiaire » de B-6 sont exacts |

### Pour information : couple L12 — table des changements de la v1 à la v2

| | texte |
|---|---|
| avant (brouillon 4) | `reprennent les mots de V (« intermédiaire » à la couche 15, au sens de V pour cette mesure) ;` |
| après (brouillon 5) | `reprennent les mots de V (« intermédiaire, bien tard » à la couche 15, mot de la description de V ; libellé de V pour B-7 : « autre » ; lieu et libellé corrigés au brouillon 5) ;` |
| lieu dans V | ligne 30, section « Verdict, en mots simples » |
| ligne de V | 30 |
| **statut** | **conforme** — « intermédiaire, bien tard » est la citation exacte de la ligne 30 de V ; « autre » est le libellé exact de B-7 |

### Pour information : couple L15 — phrase « Brouillon 5 » ajoutée aux réserves tirées de V

| | texte (partie ajoutée) |
|---|---|
| après (brouillon 5, ajout) | `**Brouillon 5** (contre-lecture 4, B2) : le lieu cité dans V et le libellé que V donne à cette mesure étaient mal dits au brouillon 4 ; ils sont corrigés ci-dessous et dans le bloc séparable. Les mots cités de V ne changent pas.` |
| **statut** | **conforme** — les mots cités de V (la citation « la lecture prédit mal … intermédiaire, bien tard ») sont inchangés entre brouillon 4 et brouillon 5 ; seuls le lieu et le libellé sont corrigés |

## Présence dans le candidat v2

Les six couples (L12, L15, L16, L17, L18, L19) ont leur texte « après » présent tel quel dans le candidat v2 (`lecture-sondes-bbis-par-lentilles-v2-candidat.md` sur `origin/main`, empreinte `39118ac1…`).

## Verdict

**Conforme.** Les six couples portant sur la couche 15 sont exacts : le lieu dans le verdict (« Verdict, en mots simples », table, ligne B-7, ligne 30 du fichier), le libellé du verdict pour B-7 (« autre »), la citation de la description du verdict (« intermédiaire, bien tard »), et la distinction avec le libellé « intermédiaire » de B-6, sont fidèles au verdict scellé. Aucune valeur chiffrée n'a changé. Les six textes « après » figurent tels quels dans le candidat v2.

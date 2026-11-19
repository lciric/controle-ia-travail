# Contrôle du différentiel de l'addendum 1 de la ligne 1, version 3 → version 4 — v1

Vérificateur : le contre-lecteur des versions 1 à 3, modèle O (classe A ; vérification des corrections par le même contre-lecteur). Date : 2026-11-19, après 22:22Z (temps universel). Rien lancé : ni étalonnage, ni fumée, ni course, ni essai. Aucune graine dérivée. Aucun réseau sauf `git fetch` et `git show` du dépôt, aucune écriture dans le dépôt, aucun refus d'outil. Rien n'a été touché sous `archives-reponses-modeles/`. Un petit programme de contrôle, dans mon bloc-notes, a lu les deux versions et mon contrôle précédent ; il n'exécute rien du banc.

## Verdict

**Scellable tel quel.** Mes cinq corrections sont appliquées à la lettre. La tenue de version suit ce que j'avais décrit, et les écarts déclarés par le rédacteur sont justes. La phrase du § 9, point 5, reste vraie au sens où le journal sert en complément ; une précision est proposée sans être exigée (§ 4).

## 1. Empreintes et différentiel

| pièce (commit `cf6094a2` de `lot/compte-organisme-v1`) | sha256 | état |
|---|---|---|
| addendum v4 | `c29628a0dd209133545985cc334274462257314560c62c04259c5b31b1686e67` | conforme à son compagnon |
| différentiel v3 → v4 | `2798ad6b4c6e7b8cfa39592ccfe33b93a4c66c49914ad932eedd20a9e4a2d308` | conforme |
| programme de remplacement | `0fd2c351c3552bffc9a9c080e64412bf2d25a7522ce8fb485dc26874d1747531` | conforme (non exécuté) |
| rapport du rédacteur v4 | `f63b3ee36a3a4530b4e0c787bc706a4a010dc78331e2def223905f2fe435c35b` | conforme |
| mandat du rédacteur v4 | `447df1443aecc990629a9b5845a06c762a094414a092da40d2a39e146ceb5f16` | conforme ; le commit `ebe691f8` cité porte bien cette empreinte |
| addendum v3 | `fb48a8ab…` | intacte (R12) |
| mon contrôle v2 → v3 | `328322989b4d0eda7de480a666ed5599a26fe713ab16dc5d5a9fedf7000f17d5` | conforme ; le commit `e8069af6` cité le porte |

J'ai refait `diff -u` sur les versions 3 et 4 tirées du dépôt : son corps est identique, octet pour octet, à celui du fichier versé. Il compte cinq blocs de changement : en-tête, § 6, § 8, § 9 point 8, § 11 et § 12.

## 2. Les cinq corrections, à la lettre

Mon programme a extrait les cinq textes neufs de la § 6 de mon contrôle. Chacun se trouve **une fois** dans la version 4 et nulle part dans la version 3. Les textes anciens sont retirés :
- le paragraphe de la configuration v3 ;
- la phrase sur le journal du lanceur au paragraphe de la garde A14 ;
- « Tout ce qui dit « je » est du rédacteur de la version 2 ; ».

La phrase « Si Lazar choisit l'option B, cet ajout tombe. » ne reste qu'au § 9, point 8, comme prévu.

## 3. Tenue de version et écarts déclarés

- **Statut :** « version 4 (erratum de la version 3) ». Il ne cite que mes cinq corrections et la tenue, et rappelle que le premier ajout de la v3 est retiré et que le second reste conditionnel à l'option A. C'est juste ; le texte de la main du rédacteur est exact.
- **Ligne de l'auteur :** les trois rédacteurs sont distingués et le mandat v4 est cité. « Pour cette version 3 » est devenu « pour la version 3 », et « Aucun des deux » est devenu « Aucun des trois ». Ces écarts sont justes et nécessaires : sans eux, la phrase serait fausse dans la version 4.
- **Les trois « cette version 3 » devenus « la version 3 »** (ligne « Vérification de la version 2 » de l'en-tête, § 8 à deux endroits) : justes, pour la même raison.
- **§ 8 :**
  - la ligne du contrôle v2 → v3 est remplie (chemin, empreinte, commit `e8069af6`, verdict) et reformulée comme demandé ;
  - une ligne « À PORTER » est ajoutée pour ce contrôle-ci.
- **§ 11 :** une seule phrase ajoutée, celle que j'avais donnée. Le reste est intact.
- **§ 12 :** il nomme les pièces lues avec leurs empreintes et commits ; j'ai vérifié que les commits `12535e60`, `ebe691f8` et `e8069af6` existent. Il donne :
  - les cinq corrections une à une, avec leur lieu ;
  - la raison du retrait, avec l'origine de l'erreur de source d'heure dans ma correction 9 de la version 1 ;
  - la décision 4, ouverte et sans défaut.

  Le texte de sa main est exact.
- **Date :** « version 4 écrite le même jour vers 22:20 ». Juste.
- **Lecture de GO-2026-11-19-81 :** le différentiel v2 → v4, pris à travers mes deux contrôles, ne contient que les corrections exigées, l'ajout conditionnel à l'option A, le retrait d'un ajout et la tenue. La condition que la mère s'était fixée est tenue.

## 4. § 9, point 5 : « le journal du lanceur sert au contrôle du § 6 »

Depuis la correction 2, la source d'heure du § 6 est le fichier d'état du lanceur ; le journal n'est lu qu'en complément. La phrase reste vraie en ce sens, puisque le § 6 le lit encore, et elle ne contredit pas le § 6, qui fait foi sur la source. Le fichier d'état, `etat-lancement-ligne1-v2.json`, est bien un fichier JSON final ; `empaqueter` le prend, comme le § 6 le dit. **Elle n'empêche pas le scellement.**

Si une version 5 devait être faite pour une autre raison, elle remplacerait « le journal du lanceur sert au contrôle du § 6. » par « le journal du lanceur sert en complément au contrôle du § 6, dont la source d'heure est le fichier d'état du lanceur, versé par l'empaquetage. » Je ne demande pas de version pour ce seul point.

## 5. Ce qui reste avant le départ (rappel, hors du texte)

- **Places « À PORTER » :** ce contrôle au § 8 ; le chemin, l'empreinte, le commit et l'heure du scellement au § 6.
- **Programme de l'audit de symétrie :** à écrire, contre-lire et porter au registre avant le lancement de la course décisive (§ 7, réserve 6).
- **Décision 4 de Lazar :** sans défaut, et rien ne part avant elle.
- **Mot de Lazar exigé par GO-2026-11-19-81 :** il nomme le chemin et l'empreinte de la version scellée.

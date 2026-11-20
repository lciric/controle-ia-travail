# Rapport du rédacteur — additif 4 de la ligne 3, règle de mot de la carte de l'alarme de changement de juge (`fcbf4a2dd1a57`), version 2 — v1

2026-11-20, `date -u` : 10:27Z à l'heure relevée. Mandat `mandat-redacteur-additif-4-v2-v1.md` (`cae12407a42550633996d687ea6612f639d8ab4ccfbc6898634fc681e7afba73`, égale à son compagnon), sur GO-2026-11-20-30 (b). Rédacteur neuf, modèle F, qui n'a écrit ni la version 1 ni aucune autre pièce de la ligne 3.

## Verdict

La version 2 de l'additif est écrite : les six corrections de texte de la contre-lecture (1, 2a, 2b, 3, 4, 5) sont portées mot pour mot, avec la tenue (titre, statut, phrase de version), et rien d'autre. Aucun seuil, aucune règle, ni le mot prédit ne changent. Les huit points du § 9 restent non tranchés. À vérifier par le même contre-lecteur.

## Pièces qui font foi, vérifiées

Chacune égale à son compagnon (`sha256sum -c`) et à l'empreinte du mandat, recalculée.

| pièce | sha256 |
|---|---|
| additif 4, version 1 | `c83ff15acab2f082d3bfb9e93be3747f59a31b9131084919f6527de9abdab169` |
| rapport du rédacteur, version 1 | `3b1962d686bb3621f367056ce21c204b2c30b7727ec83b043bd508c5178a7bb0` |
| contre-lecture de la version 1 | `3e96ef79cbebe3bea9addc59a56c26bb3e1e79bd61bcd93efbcf6a08968affe0` |
| outil `scripts/remplacer_texte_exact_v1.py` | `391db990734dd36f7c827b8b6c77dc0de1bda324f671b65748ccfe68c56a53d6` |

## Ancres et comptes

Chaque texte ancien compté dans la version 1 par `grep -c -F -e`, avant l'appel de l'outil : huit comptes, tous égaux à 1. L'outil a refait le compte (exactement une occurrence par texte ancien) et a vérifié que chaque texte neuf figure 0 fois avant et 1 fois après.

| rang | objet | ligne de la v1 | compte avant |
|---|---|---|---|
| 1 | tenue : titre, « — v1 » devient « — v2 » | 1 | 1 |
| 2 | tenue : statut et phrase de version | 3 | 1 |
| 3 | correction 1 (§ 3.1, iii) : 1,3 à 2,6 % selon le départ et m | 80 | 1 |
| 4 | correction 2a (§ 3.1, table) : « ≤ 0,00011 » deux fois sur la ligne | 77 | 1 |
| 5 | correction 2b (§ 3.1, table) : « ≤ 1,1e-16 » | 78 | 1 |
| 6 | correction 3 (§ 6, point 8) : paires d'essais de frontière | 114 | 1 |
| 7 | correction 4 (§ 0) : dates de fichier | 16 | 1 |
| 8 | correction 5 (§ 0) : embranchement pris après l'étage 1 | 17 | 1 |

Contrôle « mot pour mot » : les six textes neufs des corrections, précédés de « - Neuf : » et entourés de leurs accents graves, ont été cherchés dans la contre-lecture par un seul `grep -c -F` à six motifs : 6 lignes trouvées, une par correction. Ni la contre-lecture ni la version 1 ne portent d'espace insécable.

## Remplacements

Huit remplacements, un seul appel de l'outil, sortie `FAIT`, aucun avertissement. Version 1 : 28 298 octets ; version 2 : 30 156 octets. Le différentiel (`diff -u`) montre huit lignes changées (1, 3, 16, 17, 77, 78, 80, 114 de la version 1 ; la ligne 77 porte la correction 2a, la 78 la 2b) et aucune autre.

## Pièces écrites

Dossier : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/redacteur-additif-4-v2/`. Chaque pièce a son compagnon `.sha256`.

- `additif-4-preenregistrement-ligne-3-mot-alarme-v2.md` (`841cef1e99126762019f45bdacca7ff7d6291c91b34c4f3d434c854c262db704`) : la version 2.
- `additif-4-preenregistrement-ligne-3-mot-alarme-v2.md.journal-remplacements-v1.json` : le journal de l'outil.
- `remplacements-additif-4-v1-v2.json` (`7d5bb4e7fd65b073dd78fcf187ee5570f02e93171bee8bd969e9d3195c1db7d2`) : les huit couples ancien et neuf.
- `differentiel-additif-4-v1-v2.diff` : le différentiel.
- `erratum-1-rapport-redacteur-additif-4-mot-alarme-v1.md` : « sous 1e-16 » devient « au plus 1,1e-16 » dans le rapport de la version 1, laissé intact.
- ce rapport.

## Réserves

1. **Phrase de version placée dans le paragraphe de statut**, avant la phrase d'origine de la version 1 (« Écrit le … sur le mandat … »), gardée à l'octet. Une phrase de liaison dit que ce qui suit est d'origine. Le paragraphe est long.
2. **Première personne.** Tout le texte, corrections 4 et 5 comprises, parle à la première personne du rédacteur de la version 1 ; la signature finale « Rédacteur neuf, modèle F » est celle de la version 1, gardée à l'octet. La phrase de version le dit ; je ne l'ai pas dit ailleurs.
3. **§ 10 « Pièces lues » non touché** : il liste les pièces lues par le rédacteur de la version 1, mandat de la version 1 compris. Mes propres lectures sont dans ce rapport. Je n'ai lu ni le texte de la ligne 3, ni les additifs 1 et 2, ni le banc, ni `registres/go.md`.
4. **Chiffres voisins non touchés, hors des corrections.** Le § 9, point 1, garde « 9 999 fois sur 10 000 » ; la table du § 3.1 garde « 0,0001 » pour « sans prise » de la carte et « 0,9999 » ; le § 3.1 (ii) garde « moins de 1e-56 ». La contre-lecture ne les corrige pas (elle confirme 0,99989 et 2,1e-57) ; je ne les ai pas refaits.
5. **Rapport de la version 1** : sa puce « la fausse alarme serait de 1,6 à 2,6 % » porte le chiffre que la correction 1 change dans l'additif. Le mandat ne demande à l'erratum que le « sous 1e-16 » ; ce second point est signalé dans l'erratum et rendu à la mère.
6. Je n'ai refait aucun calcul : les corrections sont portées sur la foi de la contre-lecture.

## Aveugle et interdits

Rien ouvert sous `execution-etage-1-v1/`, `verdict-etage-1-v1/`, `prereg/organisme-auto-conception-v9/ligne-3/verdict-etage-1/`, ni sous `archives-reponses-modeles/`. Aucune mesure de l'étage 1 vue ; comme le rédacteur de la version 1 et le contre-lecteur, j'ai lu les mots « P6 réfutée à côté » dans la ligne de GO citée par l'additif, et les valeurs de population du calcul. Aucun lancement du banc, aucune écriture dans le dépôt, aucun commit, aucun appel de modèle, aucune dépense, aucune commande de liste, aucun code en ligne passé à un interpréteur.

## Écarts

- Deux commandes `grep -P` de recherche d'espaces insécables ont échoué sur une faute de ma part (motif refusé par `grep` dans cette locale), puis ont été refaites à l'octet : aucun espace insécable. Ce n'est pas un refus de permission, de classifieur ni de garde ; aucun n'a été rencontré.
- Le contrôle « mot pour mot » a passé six motifs `-e` dans un même `grep` sur un seul fichier nommé.

Rédacteur neuf, modèle F.

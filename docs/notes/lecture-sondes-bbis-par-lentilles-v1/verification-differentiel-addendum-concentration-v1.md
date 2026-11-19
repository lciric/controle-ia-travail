# Vérification du différentiel de l'addendum « concentration », version finale — v1

- **Contre-lecteur** : le même (Opus 5.5, `claude-opus-5-5`), auteur des rapports `715ddfa7…` et `867983f3…`. Date : 2026-11-19, vers 14:50 UTC.
- **Lu** (branche `claude/brave-galileo-jhp684`, commit `6ad07316`, arbre détaché du bloc-notes ; empreintes recalculées, égales au
  mandat et aux compagnons) : version finale `prereg/lecture-sondes-bbis-par-lentilles-v1-addendum-concentration-v1.md`,
  `7c7387088dd5956d3e75bd8e859346dd4db560582fd2f239d2c892b4d2c22970` ; brouillon 2 `…-addendum-concentration-v1-brouillon2.md`,
  `924d02989412700d6241d0e3663fd4914e462bc68560df345b8cdc1889f2813c` (inchangé d'un octet).

## Conclusion

**Scellable tel quel**, après le mot de Lazar sur la garde d'égalité (EC-6), comme le dit son statut.

## Vérifications

1. **Couples rejoués par moi** : mon programme `couples_verification_contre_lecteur.py` (`4c2e84b1…`, branche principale) a été joué
   sur le brouillon 2. Les dix textes « avant » y paraissent une fois chacun. La copie « brouillon 2 + G1 à G8 + H1 et H2 » a pour
   empreinte `0dbaa930b130664c77c7d142401cd8e62a89885d433afe662ed6c88c7196d150`, la même que celle du rédacteur. G1 à G8, H1 et H2 sont
   appliqués à la lettre.
2. **Différentiel entre cette copie et la version finale** : deux blocs seulement. Le premier est la puce « Statut » (lignes 45 à 56,
   remplacées par 45 à 64). Le second est la fin du § 12 : la puce des fichiers donnés, mise au passé, et le § 12 bis neuf (lignes 616
   à 620, remplacées par 624 à 690). Rien d'autre n'a changé.
3. **§ 12 bis** : rien de faux.
   - Les empreintes de mes pièces sont exactes et présentes sur la branche principale (`b3e070c0…`, `fe7274f1…`, `ef5e2b05…`,
     `56bb8d00…`, `ea28deba…`, `e86b9036…`, `4c2e84b1…`), de même que les rapports `715ddfa7…` et `867983f3…`.
   - Les chiffres sont ceux de mes sorties : 9,0 × 10⁻⁶ ; 8,3 × 10⁻⁶ à 1,5 × 10⁻⁵ ; 3,6 × 10⁻⁵ ; 2,9 × 10⁻⁴ ; 1,6 à 2,9 ; 7 et 56 ;
     0,80 à 0,95 ; 0,018 = 2 000 × 9,0 × 10⁻⁶.
   - « Quelque neuf cents listes » et « 0,5 à 1 % » sont bien un compte à moi, qu'aucune pièce ne porte : les donner comme ordre de
     grandeur est juste.
   - Les deux mots hérités (« non contre-lu » ; « que la mère verse ») sont lus correctement. La pièce d'appui est sur la branche,
     d'empreintes `b1d0d474…` et `26f4abba…`.
   - Le § 12 bis dit, à juste titre, que l'affirmation « ne s'arrête que si l'égalité compte » est fausse avec l'ancienne borne et
     vraie avec G1.
   - Une précision, sans couple : « aucun écart » pour l'énumération des bornes est vrai (0 bornes violées, bornes exactes atteintes).
     Cette énumération a aussi montré les arrêts sans objet de l'ancienne borne, que G1 ôte.
4. **H2 n'est pas un arrêt neuf caché.** La phrase suit les deux lignes de la « Liste d'arrêt », hors du tableau, et dit « sans
   arrêt ». La « Liste d'arrêt » garde ses deux lignes ajoutées par EC-6, comme dans le brouillon 2. Le compte se fait au montage, sur
   `lm_head.weight` déjà lu, sans aucune sonde. Le § 12 bis le rattache à EC-6, sous le même mot de Lazar.

## Pièce

`docs/notes/lecture-sondes-bbis-par-lentilles-v1/verification-addendum-concentration-outils-v1/` n'est pas modifié. Le différentiel
de ce contrôle est gardé dans le bloc-notes (`diff-brouillon2-couples-vers-finale.txt`), reproductible par la commande du point 1
suivie de `diff`. Aucune sonde, aucune table, aucun verdict lu ; aucune dépense ; aucun commit ; aucun refus d'outil.

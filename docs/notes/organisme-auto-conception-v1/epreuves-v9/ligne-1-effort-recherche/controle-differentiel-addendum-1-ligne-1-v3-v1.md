# Contrôle du différentiel de l'addendum 1 de la ligne 1, version 2 → version 3 — v1

Vérificateur : le contre-lecteur des versions 1 et 2, modèle O (classe A ; vérification des corrections par le même contre-lecteur). Date : 2026-11-19, après 22:10Z (temps universel). Rien lancé : ni étalonnage, ni fumée, ni course, ni essai. Aucune graine dérivée. Aucun réseau sauf `git fetch` et `git show` du dépôt, aucune écriture dans le dépôt, aucun refus d'outil. Rien n'a été touché sous `archives-reponses-modeles/`. Un petit programme de contrôle, dans mon bloc-notes, a lu les versions 2 et 3 et ma vérification par `git show` ; il n'exécute rien du banc.

## Verdict

**Scellable après corrections** (cinq corrections à texte exact, § 6). Mes quatre corrections sont appliquées à la lettre. Le différentiel versé est exact et la tenue de version est juste. Les deux ajouts de la mère ne relâchent rien du texte scellé, mais :
- la configuration v3 est à retirer, comme la mère l'a décidé (correction 1) ;
- le repli de la garde A14 lit un journal qui ne porte pas d'heure ; la faute vient de ma correction 9 de la version 1, et c'est le fichier d'état du lanceur qu'il faut lire (correction 2) ;
- le versement de l'étalonnage pendant la course décisive demande deux précisions pour ne pas faire refuser la chaîne ni dépasser le plafond (correction 3).

## 1. Empreintes, par programme

| pièce (commit `d8e09ebf` de `lot/compte-organisme-v1`) | sha256 | état |
|---|---|---|
| addendum v3 | `fb48a8ab9aeee1667c46a3d72dbf97d39343ecfb10227c652074d38f46ba55d5` | conforme à son compagnon |
| différentiel v2 → v3 | `8c42ccc88910048cd666e98474ea61224eb17779a15f514be6561b779f7b3740` | conforme |
| rapport du rédacteur v3 | `d2cc55ddc6d87ae50c49f757573033441cc3da2782fd818c8dd3927a9c27c48c` | conforme |
| programme de remplacement | `9d26722ae7ca1e70d5a90f468a28515e8d242baa72b134a4985379508396de71` | conforme (lu par son empreinte, non exécuté) |
| mandat du rédacteur v3 | `ccd4b3648e2f5b48debb9ae5b501ea88736476442dcb4c4ac25766805c3abc2d` | conforme |
| addendum v2 | `b5d769739e8b3be62a802d1d689a89af1537efb55692713e71ccde451e375f57` | intacte (R12) |
| ma vérification de la v2, au commit `3c3cd4af` cité par la v3 | `b0c09a4f94b3bc909c13757ea76ddc116581e0ce04ec1238c7db82490794893b` | conforme ; commit cité juste |

## 2. Mes quatre corrections : appliquées à la lettre

- **Textes exacts :** les cinq textes de la § 6 de ma vérification (deux cellules de table, une puce, un ajout au § 6, une fin de réserve 6) sont présents au caractère près dans la v3 et absents de la v2.
- **Textes anciens :** ils sont retirés. Les deux lignes d'en-tête en double de la table du § 5.4 et les deux « À PORTER par la mère » des attestations ont disparu ; il ne reste de cette formule qu'une citation au § 11. La puce « … n'est pas tenue à la lettre » et la fin « le plus sûr est… » de la réserve 6 ont disparu aussi.
- **Différentiel versé :** j'ai refait `diff -u` sur les deux versions tirées du dépôt. Son corps est identique, octet pour octet, à celui du fichier versé (même empreinte hors des deux lignes d'en-tête, 105 lignes).
- **Étendue des changements :** ils se limitent aux endroits suivants, tous déclarés au § 11 :
  - tenue de version : titre, statut, auteur, date, ligne « Vérification de la version 2 » ;
  - les quatre corrections ;
  - l'ajout de la mère au § 6 et le point 8 du § 9 ;
  - au § 8, « Cette version 2 » devenu « La version 2 », la cellule de ma vérification remplie et une ligne « À PORTER » ;
  - le § 11 neuf.

  Rien d'autre ne change.

## 3. Les deux ajouts de la mère

**Configuration v3 (§ 6).** Elle ne relâche rien : elle faisait porter par le programme un durcissement déjà écrit. Elle est pourtant à retirer, et la mère l'a décidé. La limite écrite par le rédacteur est juste, je l'ai relue dans le code :
- `CHEMIN_CONFIGURATION` vise le nom fixe `configuration_ligne1_v2.json` ;
- `verifier_derivations` ne lit que `preenregistrement.horodatage_scellement` (« 2026-11-19T14:27:16Z ») ;
- aucune ligne de registre n'est lue.

Une configuration v3 demanderait donc un code v3, c'est-à-dire un changement du code visé par le § 5.1 après sa vérification. Changer plutôt la valeur de ce champ le ferait mentir sur l'heure du scellement du préenregistrement. **Le texte doit retirer l'ajout et ne garder que le repli** (correction 1), sous l'option A comme sous l'option B.

**Le repli, tel qu'écrit, ne marche pas.** Il demande de lire « le journal du lanceur, ouvert en ajout » pour dater le premier lancement. Or le lanceur v2 n'écrit dans ce journal aucune heure : seulement les codes de retour des étapes, « chaîne complète » ou les arrêts. La seule heure écrite par le programme à chaque lancement est le champ `debut` de chaque session, dans le fichier d'état `etat-lancement-ligne1-v2.json`. Ce fichier est relu et complété à chaque reprise, donc conservé, et `empaqueter` le verse (c'est un fichier JSON). La phrase sur le journal du lanceur vient de ma correction 9 de la version 1 ; c'est mon imprécision, et je la corrige ici (correction 2). Une étape lancée à la main n'écrit pas ce fichier : sous l'option B, la mère consigne l'heure de lancement au registre avant de lancer.

**Versement de l'étalonnage pendant la course décisive (§ 9, point 8).** Il ne relâche rien. Aucun fichier n'est ouvert ; seul `empaqueter` lit les fichiers, et il n'imprime que le nombre de morceaux, les octets et l'empreinte du manifeste. La sous-commande `empaqueter` n'appelle ni `preparer` ni le contrôle des processus et ne touche pas au dossier de sortie quand elle travaille sur une copie. Le code ne change pas. Deux points doivent être écrits pour que ce versement ne nuise pas à la chaîne (correction 3) :
1. **Lieu de la copie et des morceaux.** Une copie posée dans le dossier de sortie serait reprise par l'empaquetage final, qui parcourt tout ce dossier : environ 155 Mo de plus, au risque de dépasser 500 Mo. Un fichier non suivi sous `code/` ferait refuser l'étape suivante, puisque `preparer` exige un arbre propre sous ce dossier (« code non commis »). Les deux vont donc hors du dossier de sortie et hors de `code/`.
2. **Plafond.** L'empaquetage final reprend l'étalonnage. Le plafond « au total » du point 4 doit donc compter les deux versements poussés sur la branche.

Un commit fait pendant la chaîne change le commit courant, mais pas les empreintes de fichiers que compare `verifier_etalonnage_pour_decisive`. Le manifeste décisif garde le commit lu à son départ : sans effet sur une garde.

## 4. Lecture de GO-2026-11-19-81 par la mère, tenue de version et écarts du rédacteur

**Lecture de la ligne GO.** La mère lit « l'addendum v2 scellé » comme l'addendum scellé dans sa dernière version vérifiée, à deux conditions : seules les corrections exigées et les ajouts déclarés conditionnels à l'option A changent, et le vérificateur contrôle chaque différentiel. Je l'accepte. Le différentiel v2 → v3 tient ces conditions (§ 2), et la version 4 les tiendra si elle n'applique que les corrections ci-dessous. De plus, le mot de Lazar exigé par la même ligne nommera le chemin et l'empreinte de la version scellée : Lazar verra donc la version exacte. Cette lecture doit être écrite dans l'addendum (correction 5).

**Tenue de version.** Elle est juste, et déclarée au § 11 et dans le rapport.

**Écarts 3 à 5 du rapport du rédacteur :**
- **Écart 3 (phrases « cette version » restées de la version 2 : § 1, § 5.4 « Préalable » et « État à l'écriture », réserve 4).** C'est acceptable : les réécrire sortirait de l'erratum et toucherait des constats datés. Mais dans un texte scellé, « cette version » serait ambigu. La phrase d'auteur de l'en-tête doit le lever (correction 4).
- **Écart 4 (places « À PORTER » restantes) :** il est normal. Ce sont le scellement et ce contrôle ; la mère les remplit.
- **Écart 5 (rapport v2 dépassé sur les attestations) :** c'est sans effet. Ce rapport est une pièce de travail ; le registre le note.

Les deux phrases de la main du rédacteur (la limite au § 6 et le § 11) sont exactes. La première disparaît avec la correction 1.

## 5. Avis

Il n'y a aucun nœud nouveau pour Lazar. La décision 4 reste ouverte, sans défaut, et rien ne part avant elle (§ 6, correction 3 de la vérification v2, présente dans la v3).

## 6. Corrections numérotées (texte exact, à appliquer par la version 4)

1. **§ 6, retrait de la configuration v3.** Remplacer en entier le paragraphe qui commence par « **Ajout de la mère (2026-11-19, vers 22:04Z, transmis par le coordinateur), hors des quatre corrections de la vérification de la version 2 ; valable seulement si Lazar choisit l'option A de la décision 4 (un seul mot, avant tout lancement) — garde A14 lue par programme contre l'heure du scellement de cet addendum, par une configuration v3.** » et qui finit par « Si Lazar choisit l'option B, cet ajout tombe. » (cette phrase de fin figure aussi au § 9, point 8, qui la garde ; le remplacement porte sur le seul paragraphe du § 6) par :
   « **Configuration v3, proposée par la mère (2026-11-19, vers 22:04Z), non retenue par elle avant le scellement.** Aucune configuration v3 et aucun code v3 n'existent : le code visé reste celui du § 5.1 (commit `14abb83052da2037ed39002716ecf97e2a99a6c4`, configuration v2 `81f58ce5ca0a492ef231fa175303a21dfb21383a096fa71911b917923cc34f15`), dont la garde A14 compare les dérivations à la seule heure du scellement du préenregistrement. Le contrôle de la garde A14 contre l'heure du scellement de cet addendum se fait par lecture, comme le paragraphe précédent l'écrit, par la mère après la chaîne, puis par l'agent qui lit ; il vaut sous l'option A comme sous l'option B de la décision 4. Raison du retrait : le code v2 lit un fichier de configuration de nom fixe (`configuration_ligne1_v2.json`) et un seul champ d'heure (`preenregistrement.horodatage_scellement`) ; une configuration v3 demanderait un changement du code visé après sa vérification, et changer la valeur de ce champ le ferait mentir sur le préenregistrement. »
2. **§ 6, paragraphe « Conséquence pour la garde A14 ».** Remplacer « la mère lit aussi le journal du lanceur, ouvert en ajout, et vérifie que le premier lancement de l'étalonnage lui est postérieur, puisqu'une reprise ne conserve pas les horodatages antérieurs (première contre-lecture, constat 13, c). » par :
   « la mère lit aussi le fichier d'état du lanceur (`etat-lancement-ligne1-v2.json`, champ `debut` de chaque session, conservé d'une reprise à l'autre et versé par l'empaquetage) et vérifie que le début de la première session est postérieur à cette heure, puisqu'une reprise ne conserve pas les horodatages de dérivation antérieurs (première contre-lecture, constat 13, c) ; le journal du lanceur, ouvert en ajout, est lu en complément, mais le programme n'y écrit aucune heure ; pour une étape lancée à la main, qui n'écrit pas ce fichier d'état, la mère consigne au registre l'heure de lancement (`date -u`) avant de lancer. »
3. **§ 9, point 8.** Après « le code ne change pas. », ajouter :
   « La copie et le dossier d'empaquetage (`--vers`) sont placés hors du dossier de sortie de la chaîne et hors du dossier `code/`, et rien n'est écrit sous `code/` pendant la chaîne : une copie dans le dossier de sortie serait reprise par l'empaquetage final, et un fichier non suivi sous `code/` ferait refuser l'étape suivante (« code non commis »). L'empaquetage final de la chaîne reprend l'étalonnage, puisque `empaqueter` prend tout le dossier de sortie : le plafond du point 4 s'applique au total des deux versements poussés sur la branche ; s'il devait être dépassé, retour à la mère avant de pousser le second. »
4. **En-tête, ligne de l'auteur.** Remplacer « Tout ce qui dit « je » est du rédacteur de la version 2 ; » par :
   « Tout ce qui dit « je », et « cette version » hors de l'en-tête, du § 8 et des § 11 et suivants, est du rédacteur de la version 2 et désigne la version 2 ; »
5. **En-tête, après la puce « Condition de la même ligne, recopiée telle quelle ».** Ajouter la puce :
   « - Lecture de cette condition par la mère (19 novembre) : « l'addendum v2 scellé » s'entend de l'addendum scellé dans sa dernière version vérifiée, pourvu que seules les corrections exigées par le vérificateur et les ajouts déclarés conditionnels à l'option A de la décision 4 aient changé depuis la version 2, ce que le vérificateur contrôle sur chaque différentiel ; le mot de Lazar exigé par la même ligne nomme le chemin et l'empreinte de la version scellée. »

**Ce que la version 4 doit dire ailleurs, sans texte exact imposé (tenue) :**
- **Statut :** version 4, qui ne diffère de la version 3 que par ces cinq corrections et la tenue.
- **§ 8 :** la ligne « À PORTER » du contrôle v2 → v3 reçoit le chemin de ce contrôle, son empreinte et son verdict (« Scellable après corrections », cinq corrections). Elle dit « l'ajout de la mère (§ 9, point 8) et le retrait de la configuration v3 (§ 6) » au lieu de « les deux ajouts de la mère (§ 6 et § 9, point 8) ». Une ligne « À PORTER » est ajoutée pour le contrôle du différentiel v3 → v4.
- **§ 11 :** il reste tel quel, comme histoire de la version 3, comme le § 10 l'est de la version 2, avec une seule phrase ajoutée à la fin du paragraphe « Deux ajouts de la mère… » : « Le premier de ces ajouts (configuration v3) est retiré par la version 4, non retenu par la mère (§ 12). »
- **§ 12 neuf, « Différentiel version 3 → version 4 » :** les cinq corrections une à une, avec leur lieu ; la raison du retrait de la configuration v3 (décision de la mère, pas de code v3) ; la tenue.
- **Rapport du rédacteur v4 :**
  - les cinq corrections faites à la lettre, par programme, chaque texte ancien trouvé une seule fois ;
  - le retrait de la configuration v3 sur la décision de la mère, ce qui lève la réserve du rapport v3 ;
  - la source d'heure de la garde A14 corrigée, et le fait que l'erreur venait de la correction 9 du contre-lecteur ;
  - la lecture de GO-2026-11-19-81 par la mère, écrite en tête ;
  - la décision 4 toujours ouverte, sans défaut ;
  - le différentiel v3 → v4 versé, à faire contrôler par le même vérificateur.

Si ces textes sont appliqués à la lettre et que le différentiel v3 → v4 ne contient rien d'autre que ces corrections et la tenue, je l'accepte sur un contrôle du différentiel.

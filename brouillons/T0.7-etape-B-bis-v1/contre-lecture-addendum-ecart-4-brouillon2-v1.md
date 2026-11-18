# Contre-lecture du brouillon 2 et du texte candidat du quatrième addendum d'écart — apprentissage des sondes sur la tâche (étape B bis de T0.7) — v1

- **Contre-lecteur** : le même sous-agent neuf qu'au brouillon 1 (modèle Opus 5.5 ; rapport `contre-lecture-addendum-ecart-4-brouillon1-v1.md`, `5e0c2fa5162b53ab8b4291309f23747a9bb1fb99802b6efd0d7c31edb8868600`). Je n'ai écrit ni les brouillons, ni la liste des différences, ni le texte candidat (R2).
- **Mandat** : celui du brouillon 1 et la suite que la conductrice m'a transmise le 2026-11-18 : vérifier que les corrections m1 à m7 sont portées, et elles seules.
- **Pièces** (empreintes recalculées) :
  - brouillon 2 : `brouillons/T0.7-etape-B-bis-v1/addendum-ecart-4-brouillon2-v1.md`, `21b91f2a4b35e4695dd637166fd33cd92bf242f82af0b30b3c6793f0560f9094`, égale au compagnon ;
  - liste des différences : `brouillons/T0.7-etape-B-bis-v1/differences-addendum-ecart-4-brouillon1-brouillon2-v1.md`, `019d59b338f4a4d207a68179fbe56b52caa6670aef8a3ed0849dbe7b3c0ae050`, égale au compagnon ;
  - texte candidat, sans compagnon : `prereg/T0.7-etape-B-bis-v1-addendum-ecart-4-v1.md`, `5ef929eae8b070bc7f9d1934d487066ded34896df00dc8a9c70c91b44f0b30c4` ;
  - brouillon 1, inchangé : `afac645f…`.
- **Méthode** : par simple lecture. `diff` entre le brouillon 1 et le brouillon 2, puis entre le brouillon 2 et le texte candidat ; `grep` borné ; `sha256sum`. Aucune garde jouée, aucun fichier de résultat ouvert.

## Conclusion

**Non scellable en l'état**, pour **un seul passage**, à deux endroits : l'incise « avec la date d'origine relevée par programme ».

- **Où** : dans la réponse (a) de la mère, telle que le brouillon 2 la recopie au § 1 (l. 144-146) et au point ouvert 3 (l. 340-341). Le texte candidat porte le même passage aux mêmes endroits.
- **Correction exacte** : retirer, aux deux endroits, la suite « , avec la date d'origine relevée par programme ».
- **Ou bien** : la conductrice confirme que le message de la mère (vers 21:24Z) porte ces mots.

Une fois ce point levé, rien d'autre ne fait obstacle : le texte candidat est scellable tel quel, à l'empreinte du fichier qui en résultera.

## 1. Corrections m1 à m7 : toutes portées, là où elles devaient l'être

- **m1** : D4 « … ce couple est tenu pour ordonné et la boucle continue sur les couples suivants ; à la fin de la chaîne, la fonction rend … » ; essai 4 (l) « égalité ou inversion sur un autre couple de la chaîne, combinée avec le cas sain de l'exception (…) : (`CODE-BBIS`, `SCORES-BBIS`) égaux ou inversés → refus de la v3 ; (`SCELLEMENT-BBIS`, première fiche) égaux → refus de la v3 ». Conforme.
- **m2** : bloc « nouveau » de QA-1, insertion après l'empreinte `33f38e67…62,` de « la ligne qu'elle remplace étant la ligne `CODE-BBIS` datée 2026-11-16T12:57:27Z qui cite `registres/t07-etape-b-bis/code-bbis-v1.json` à l'empreinte ee362bb70c5051097dab90c7978eb550d192f8c90f313317812635884b04e469, ». Mot pour mot, à la place dite.
- **m3** : préséance du § 0 : « (T, en-tête, l. 5 ; A2, raison de SA-5, l. 148-149) ». Conforme.
- **m4** : les trois endroits sont portés.
  - F7 : « commit **postérieur** à celui de la fiche remplaçante et de l'accord ».
  - QA-3, point 2 : « l'heure de son entrée dans la lignée de `main` (commit `06c88328…`, 2026-11-17T11:14:06Z, postérieur au commit de l'entrée conjointe ; l'heure d'écriture dans le fichier de travail n'est portée par aucun commit) ».
  - « Conséquence » : « entrée par un commit **postérieur** ».

  Conforme.
- **m5** : « La note du nœud (§ 5) lit dans la règle d'ordre la garantie […] ; aucun texte scellé ne le dit. Cette lecture est moins que la lettre. » Conforme.
- **m6** : § 0, contrôle cité avec l'empreinte de mon rapport, comptes 1 dans A2 (l. 249, 142, 176) et 0 dans T, A1 et A3 ; point ouvert 2 clos. Conforme.
- **m7** : phrase ajoutée à la fin du point 2 de QA-3, mot pour mot ; point ouvert 3 réécrit (« couvert par GO-2026-11-18-56 (1) […] pour information »). Conforme, hors l'incise de la conclusion.

## 2. Autres passages changés

- **En-tête** : titre « brouillon 2 » ; paragraphe « Brouillon 2 » (origine, corrections portées, réponses de la mère, note n4 non portée et laissée en consigne au développeur) ; date ; statut. Conforme. La note n4 n'écrivait aucun texte de remplacement : ne pas la porter est juste. Le commit de tête cité (`c55e50d4…`) existe.
- **Statut des points ouverts** : 1, 2, 5, 6, 7, 9, 10 et 11 suivent ma table mot pour mot ou de près, sans rien ajouter. Conforme.
- **Réponse (b) de la mère** (point ouvert 8) : la clé `RATTACHEMENT-LECTURE-V4-BBIS` au registre voisin, avec sa fiche scellée, est admise et inscrite par la mère avant toute lecture, après le scellement. Fidèle.
- **Réponse (c) de la mère** (point ouvert 4) : fidèle, et n'ajoute aucun écart.
  - Le titre perd « garde non séparable » ; la question « un mode « garde seule » est-il voulu » est remplacée par la réponse de la mère : aucun mode neuf qui rejouerait une mise en place refusée ; à défaut d'un mode « garde seule » jugé par le contre-lecteur du module, la garde s'exécute en tête de la lecture, comme dans la version 3.
  - La question de la suite d'une issue « non lue » née d'un défaut de mise en place reste nœud de Lazar, « sans écart déclaré », « ne bloque pas le scellement ».
  - Cohérence vérifiée avec le § 6.5, point 3, inchangé (l. 515) : un mode « garde seule » « n'est pas déclaré ici et la v4 ne le porte pas ». La formule « à défaut de » ne l'ouvre donc pas.
- **Réponse (a) de la mère** (§ 1 et point ouvert 3) : « déclarée telle quelle comme écart de fait, sans correction du registre, […] la mère la porte à Lazar pour information » est fidèle. **L'incise « avec la date d'origine relevée par programme » ne l'est pas.**
  - Elle manque au résumé de la réponse (a) que la conductrice m'a transmis.
  - Elle manque aussi à la liste des différences (l. 11 : « (a) date de la première fiche déclarée telle quelle »).
  - Aucune pièce du dossier ne porte un tel relevé par programme : les relevés de F7 sont des commandes git jouées à la main (§ 2.0 et § 5 du brouillon).
  - C'est une affirmation de fait sans appui dans un texte qui sera scellé. Elle n'élargit pas la lecture ; elle reste hors des fondements permis.
- **Ligne de registre proposée (§ 7)** : la colonne « décision » cite la contre-lecture du brouillon 1 (« 5e0c2fa5 (scellable après corrections mineures, portées) »). Conforme. La mère pourra y ajouter le présent rapport ; ce n'est pas exigé pour sceller.

## 3. Texte candidat

- Il ne diffère du brouillon 2 que par le titre (« version 1, scellée ») et le paragraphe de statut. Conforme.
- **Statut sans heure écrite** : acceptable.
  - Il renvoie à l'heure que porte la ligne `ADDENDUM-ECART-4-BBIS` du registre voisin, source unique et vérifiable.
  - Aucun texte n'exige l'heure dans le statut. Le troisième addendum l'écrivait (« scellée le 2026-11-18T05:46:10Z ») ; ce n'est qu'une forme.
  - Le statut cite bien GO-2026-11-18-56 (1), le brouillon 2 et son empreinte, mon rapport et son empreinte, l'ordre des deux inscriptions avant toute lecture, et le point ouvert 4 laissé à Lazar.

## 4. Blocs « ancien » ; portée

- Les trois blocs « ancien » sont inchangés entre les brouillons (absents du `diff`). Le second addendum (`18baeac3…`, recalculée) est inchangé : ils y restent exacts et uniques, comme relevé au brouillon 1.
- Seul le bloc « nouveau » de QA-1 change (m2) : il resserre l'exception.
- Rien de neuf n'élargit la lecture. Aucun critère gelé, aucune issue, aucune phrase, aucune entrée, aucune graine ne change. Aucun mode neuf n'est ouvert.

## 5. Fichiers ouverts

Le brouillon 1, le brouillon 2, le texte candidat (par `diff`) ; la liste des différences (l. 1-20 et lignes trouvées par `grep`) ; empreinte du second addendum. `grep` borné de l'incise « relevée par programme » sur `brouillons/T0.7-etape-B-bis-v1/` et `registres/t07-etape-b-bis/`. `git cat-file -t` sur le commit de tête cité.

**Fichiers de résultat** : aucun, ni à l'œil ni par la chaîne.

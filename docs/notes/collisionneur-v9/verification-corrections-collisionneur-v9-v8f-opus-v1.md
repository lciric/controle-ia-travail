# Vérification des corrections : collisionneur v9-v8f, rendu v2

**Verdict : conforme.** Aucun bloquant.

Pièces : v8f 445fe2d3… (empreinte compagnon tenue) et v8e 0d591933… (intacte). Essais de la v8f : 356 passés et 3 sautés, sans les clés.

## Corrections vérifiées
Le diff entre la v8e et la v8f se limite à ce qui est annoncé : B1, B2, le contrôle ajouté à `verifier`, l'en-tête et VERSION. Le texte de Fable, les places du tour III.3 et les gardes n'ont pas changé.
- **B1.** `controler_dossier_etage3` ne compte que les essais dont la cellule commence par « E3- ». Il ne le fait que si `consignes-etage3.json` est absent.
- **B2.** Le contrôle est appelé juste après `fixer_place_iii3`, avant `fixer_composition` et tout versement. L'appel resté dans `sceller_consignes_etage3` est redondant et sans effet.
- **Contrôle ajouté à `verifier`.** Pour les essais des tours III.1 et III.3 faits sous ce script, `verifier` signale un `consignes-etage3.json` absent. Il signale aussi une invite qui ne contient pas la consigne scellée de son tour. L'accès par la clé du tour (`[:5]`) est sûr : `lire_composition` a déjà imposé que le fichier égale les consignes du script, sinon `verifier` s'arrête plus tôt.
- **Dix essais faux.** Ils sont retirés, nommés `retire_v8f_…`.

## Choix de l'essai B2 : juste
- Sous B1, un dossier de la v2 qui n'a fait que l'étage I n'a jamais reçu de consigne du tour III. L'accepter est correct, avec `--reprise` exigée par `declarer_script`. Mon ancien essai n'avait donc plus d'objet.
- L'essai B2 prend un dossier de la v2 arrêté au tour III.2 et lui retire sa question. C'est le cas qui sépare l'ordre « contrôle puis versement » de l'ordre inverse. Il compare tout l'arbre, `etat.md` mis à part. La mutation qui remet le contrôle tard est bien prise.

## Mutations rejouées sur la v8f (dix, toutes prises)
- **Les six mutations de la v8e :** texte de Fable altéré, place ignorée, refus du dossier ancien retiré, lecture de la place retirée de `lire_composition`, comparaison au fichier scellé retirée, comparaison retirée dans `lire_consignes_etage3`. Elles sont prises par les mêmes essais qu'avant. Le refus retiré est pris en plus par l'essai B2.
- **B1 :** compter les essais de tous les étages est pris par `test_v8f_etage1_puis_etage3_meme_dossier`.
- **B2 :** le contrôle retiré de `principal` est pris par `test_v8f_dossier_ancien_refuse_avant_tout_versement`.
- **Contrôle de `verifier` :** son appel retiré, ou la comparaison de l'invite neutralisée, est pris par `test_v8f_verifier_signale_consignes_absentes_et_invite_differente`.

## Non bloquants
- **Non porté, déclaré :** aucun essai neuf de la ligne de reprise ni du devis de reprise sur un dossier de la v8f. On peut s'en accommoder : les fonctions sont inchangées depuis la v8d. C'est à faire avant la première reprise payante sous la v8f.
- **`etat.md` reste réécrit** par l'`except` sur un dossier refusé. C'est dit dans l'en-tête ; l'écriture est dérivée.
- **L'appel de `controler_dossier_etage3` dans `sceller_consignes_etage3`** est inutile mais sans risque. Le garder sert de ceinture.
- **Ouvert pour Fable :** au tour III.3, aucune phrase ne demande de duel, alors que l'article 4 exige au moins un duel.

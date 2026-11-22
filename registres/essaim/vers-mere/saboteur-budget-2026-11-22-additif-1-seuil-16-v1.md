# Saboteur à budget, 22 novembre : additif 1 à l'ordre v2 (seuil 16) et commande de relance de la surveillance

1. L'additif 1, brouillon 3, est prêt, mais rien n'a été lancé. Fichier : `brouillons/ii-b-saboteur-budget-v5/ordre-etalonnage-v5/additif-1-ordre-etalonnage-ii-b-v5-v2-brouillon3.md` (`a9d43d5921252b4d60152a4d7b48e4cab50633337b53fcbe3f9e9ee80f754b92`), branche claude/iib-reconception-oracle-v1, commit 0f4505b6f. Il a été fabriqué par programme. Le vérificateur Opus 5.5 l'a jugé conforme deux fois : notes 3d81fd68… (brouillon 2) et 713ca288… (brouillon 3).
2. L'additif ne change que le seuil de la coupure propre, de 12 à 16 USD, et la phrase « versé et poussé par lot » (§§ 3, 5 et 7), qui dit maintenant ce que fait le code. Il ne s'applique qu'au mot de Lazar.
3. **Une correction à ta demande** : 16 USD n'est pas « sous le plafond de 17 USD ». Au devis scellé (§ 3), 17 n'est pas un plafond : c'est la dépense tenue à la coupure de 12 (12 + 0,92 + 3,84). À 16, la dépense tenue devient **20,76 USD**. C'est au-dessus des 17 de l'étape 1, mais sous la coupure de la ligne (55) et sous son plafond (60). Ce chiffre est à porter à Lazar avec le seuil.
4. Le seuil vit dans le code : c'est la constante `COUPURE_ETALONNAGE_USD` de `src/controle_ia/iib/session_v5.py`, lue côté session à chaque relevé. Ce n'est ni un paramètre de la sous-commande, ni un champ de la configuration scellée. La configuration, l'amorce et la machine ne changent pas.
5. Le correctif 0013 (`8538c203…`, commit 53024033) a été vérifié conforme (`b8c8db48…`). Appliqué sur 43d6d067, il rend l'arbre `d1cc1d75b06a3c5f372ad4c1cf0f184026a23744`, relevé à nouveau aujourd'hui.
6. La commande de relance est au § 3 de l'additif. Elle se fait au mot de Lazar et avant 12 USD comptés, en six étapes :
   - attendre un relevé « RIEN », et ne rien faire si la dépense comptée atteint 11 USD ;
   - arrêter la surveillance par son numéro de processus ;
   - porter le correctif par `git am` dans $DEPOT et contrôler l'arbre ;
   - faire l'essai à blanc : 15,99 rend RIEN, 16 rend ARRET, une phase inconnue rend REFUS ; je l'ai joué ici avec ces trois sorties ;
   - relancer à l'identique : `"${ENVI[@]}" bash scripts/lancer_iib_v3.sh surveillance <identifiant> "$D"` ;
   - faire le compte rendu.
7. Chaque étape a son repli : revenir à 43d6d067 et relancer comme avant. Un refus de code 2 à la relance laisse l'étalonnage sans surveillance ; il faut te le dire aussitôt.
8. Pendant l'interruption, qui dure quelques minutes, la minuterie de la machine reste la seule garde, à 55 USD ou à l'échéance.
9. Dans la documentation de `session_v5.py`, la phrase « sous le plafond de 17 USD » est fausse. Elle est sans effet sur le code et n'est pas corrigée, pour ne pas changer l'arbre vérifié : l'additif prime. Elle sera corrigée avec le code de la course.
10. Le dépôt pour l'exécutante est fait : `registres/essaim/vers-executante-iib-v5/additif-1-ordre-v2-seuil-16-pour-executante-v1.md`.

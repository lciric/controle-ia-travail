# Traitement de la contre-lecture de la consigne d'enveloppe v2 et de son code — v1

Pièce de classe C, 2026-11-24, session fille d'extraction. Rapport : `rapport-contre-lecture-consigne-v2.md` (ce dossier ; contre-lecteur neuf d'un autre modèle, effort élevé, nommé à l'appel). Verdict reçu : « utilisable après corrections ».

| remarque | traitement |
|---|---|
| CV2-1, bloquante : la réextraction des 16 papiers d'octobre lisait encore la consigne v1 | Corrigée. Une fonction unique, `extraire_banque_dose_reponse_v2.consigne_extracteur_v2`, vérifie le sceau de la consigne v2 et arrête si la marque de l'étape 2b manque. Les deux préparations (extraction de la banque, réextraction de l'échantillon) passent par elle. La réextraction vérifie de plus, dossier par dossier, que `consigne.txt` porte l'étape 2b, sinon arrêt. |
| CV2-2, mineure : en-têtes qui se citent eux-mêmes | Corrigée : « copie de `…_v1.py` » dans les deux modules. |
| CV2-3, mineure : la question phrase par phrase ne nommait que trois des six interdits | Corrigée : la question demande si la phrase révèle un élément de la liste, et énumère les six (figure ou tableau, contribution nommée, nom d'auteur compris). |
| CV2-4, mineure : la dernière phrase ne nommait que le contrôle de l'étape 5 | Corrigée : « Apart from the file names, the check in step 2b and the check in step 5 ». |
| CV2-5, mineure : relecture après une première écriture ; réécriture qui pourrait toucher les autres champs | Écart de lettre déclaré : la relecture porte sur le fichier écrit, avant toute suite (étapes 3 à 5). Ajout : « Change only the "research_questions" field ». |
| CV2-6, suggestion : risque d'énoncés trop courts | Retenue : l'essai sur les 16 papiers rapporte le nombre d'énoncés sous 200 caractères et la longueur médiane, avant (réextraction du jour sous v1) et après (v2). |
| CV2-7, suggestion : sceau, essais, garde du module de rejeu | (a) Consigne v2 scellée (`44da46b3…`). (b) Essais ajoutés : `tests/test_banque_dose_reponse_v2.py` (cas sain du dépôt ; seule l'étape 2b et la dernière phrase diffèrent de la v1 ; trois artefacts — sceau absent, texte changé après sceau, v1 rescellée sous le nom de la v2 ; préparation d'une tentative dans un dépôt jetable, chaque dossier reçoit la v2 ; source de la réextraction qui ne lit plus la v1). La lecture recopiée n'a pas d'essai d'équivalence propre : elle est la copie textuelle de `rejeu_contre_verification_banque_v1.lire`, contre-lue avec elle. (c) Inchangé et noté : le module de rejeu reste importé pour ses constantes. |

Rien d'autre n'a changé : même vivier, même sélection, même contre-vérificateur, même seuil.

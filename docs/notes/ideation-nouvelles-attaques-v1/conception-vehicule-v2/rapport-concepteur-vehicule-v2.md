# Rapport du concepteur — véhicule de la course « nouvelles attaques » — v2

- Auteur : concepteur du véhicule, modèle F. Date (UTC) : 2026-11-21 ; relevé de `date -u` : 07:10:25Z, après la lecture de la contre-lecture, avant l'écriture.
- Ce rapport complète le rapport v1 (`ceffd7aac588e1243828679cb6b9db615c80f1476c68a79e59e75571ed72bff7`), qui reste en place : ses pièces lues, ses écarts et ses décisions D1 à D11 ne sont pas redits.
- Processeur seul : aucun appel, aucune clé lue ni nommée par sa variable, aucune dépense, aucun code écrit pour être lancé, aucun lancement, aucune écriture dans un dépôt. Aucune sortie de modèle sur la question n'a été lue. Aucune branche de quarantaine n'a été ouverte. **Aucun refus de permission, de classifieur ni de garde.**

## 1. Pièces rendues

Dossier : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/concepteur-vehicule-nouvelles-attaques/`. Empreintes à la table v2.

| pièce | objet |
|---|---|
| `conception-vehicule-course-nouvelles-attaques-v2.md` | la conception corrigée ; la v1 reste intacte, à son empreinte |
| `differentiel-conception-vehicule-v1-v2.diff` | sortie de `diff -u` entre la v1 et la v2 |
| `rapport-concepteur-vehicule-v2.md` | ce rapport |
| `table-empreintes-concepteur-vehicule-v2.md` | les empreintes |

## 2. Pièces lues pour la v2

| pièce | empreinte | lecture |
|---|---|---|
| contre-lecture de la v1 (CL) | `f5b7aacc9d96dfd3bb10eaa80a6f451d646b3b7c06844dbb4da6837182cf36db`, égale à son compagnon | en entier |
| `orchestrator/pole/suivi_roles_v54.py`, dépôt de l'orchestrateur, commit `a41b7b50…` | `620225973d68670a56ca913cdd02709fa576fa43e1393d166915ea67c1d7c3bb`, d'après CL ; non recalculée par moi | l. 1 à 95 |

Portés d'après les messages de reprise, sans pièce relue : les décisions de la mère de 06:58Z et de 07:10Z ; l'ajout relayé vers 07:14Z et sa correction de 07:15Z ; le commit `61987a3a` de la branche `verse/vehicule-na-v1` ; l'empreinte `cb352811…` de la v4 scellée de l'additif de la v69, que je n'ai pas ouverte.

## 3. Point de la contre-lecture → lieu dans la v2

| point de CL | objet | lieu dans la v2 |
|---|---|---|
| § 1.3 | `executer_course_v68` ne peut pas être appelée ; deux refus levés par deux fichiers neufs ; `GenerationV68` reçoit `None` | § 0, point 2 ; § 1.2, « pris pour modèle et non appelé » ; § 2.9, lignes « génération » et « course » |
| § 1.4 | le lanceur 11 n'a aucun code | § 1.1, ligne du lanceur 11 |
| § 1.5 | suivre la v4 scellée de l'additif de la v69 ; relevé de ce qui reste sur chaque clé après la course | sigles ; § 2.11, en-tête et ligne 7 de la table ; § 6.2, « relevé de fin par clé » ; § 10, point 3 |
| § 1.6 | D1 fondée | § 1.4 ; § 0 bis |
| § 1.7 | D10 : citer le commit de la branche de versement | § 1.1 ; § 2.11 ; § 7, lot 0 |
| § 2.1 | gardes héritées du noyau ; A3 face à la « réponse vide motivée » ; question 12 du lot 0 ; épreuve | § 2.13 ; § 2.4, « garde héritée à tenir » ; § 2.9 ; § 6.2, « gardes héritées » ; § 7, question 12 ; § 9, point 19 |
| § 2.2 | coût fantôme d'un envoi refusé | § 2.3, première précision ; § 6.2, « envoi refusé sans coût » ; § 7, lot 4 et question 5 |
| § 2.3, § 6.4 | conséquence de D2 : texte fixe de rôle retiré ; deux syntaxes lues | § 2.3, deuxième précision ; § 5.3 ; § 5.4 ; § 6.2, « texte fixe de rôle retiré » ; § 9, point 2 |
| § 2.4 | huit épreuves absentes | § 6.2 : « clé n° 30 », « identifiant, clé n° 40 », « case autre, à nommer », « course arrêtée », « plafond du relais », « M4 sans cumul par clé », « aucune valeur de clé recopiée », « réponses brutes conservées » ; § 2.8, deux lignes neuves |
| § 2.5 | le lot 0 ne lisait pas le lanceur v9 | § 2, règle commune ; § 7, question 13 |
| § 2.6 | chaînes de requête de la classe (i) absentes de la table des lots | § 7, lot 7 |
| § 3.1 | lot 8 rendu comme différentiel contre le lanceur v9 | § 7, lot 8 et paragraphe « Le lot 8 se rend comme un différentiel » |
| § 3.2 | lot 7 et formats du lot 6 ; dépendances hors code | § 7, colonne « dépend, hors code, de », paragraphe « Ordre » |
| § 3.3 | chemin critique faux | § 0, point 4 ; § 7, « Chemin critique » ; § 8 |
| § 4.1 | D3 compté trop court | § 8, table « autour du code » |
| § 4.2 | 31 et 14 heures sont une borne basse ; 40 à 50 heures | § 0, point 5 ; § 8, « Lecture » et « Pour l'échéance » |
| § 5 | D11 : cas sain neuf, deux artefacts, mutation | § 6.1, ligne du n° 12 ; § 9, point 17 ; § 0 bis |
| § 6.1 | ce qui est marqué et tranché | § 0 bis ; § 9, en-tête et points 1 à 7 |
| § 6.2 | « `idee` trop long sort du contrat » débordait de D5 | § 2.4, « fiche hors contrat de longueur » (D13) ; § 5.4 ; § 9, point 3 ; § 6.2 |
| § 6.3 | deux lectures des mesures : écart non porté comme décision | § 2.8, « une seule lecture » ; § 9, point 11 (D12, au format) ; § 6.1, n° 15 |

Hors de la contre-lecture, sur les messages de la mère : la colonne « matière première », possibilité éteinte par défaut (§ 2.14, § 2.15 ; § 6.2, deux lignes ; § 7, lot 10 facultatif ; § 8, dernier paragraphe ; § 9, point 18).

## 4. Décisions

**Tranchées par la mère, portées par la v2** : D1 à D7, D10 (06:58Z) ; D11, la règle de la fiche hors contrat de longueur (notée D13), la lettre gardée pour la lecture des mesures (07:10Z).

**Pour Lazar**

- **D8** (rapport v1) : en course, l'arrêt n° 1 arrête-t-il l'appel seul ? Inchangée ; aucun défaut.
- **D9** (rapport v1) : l'échéance de GO-2026-11-20-67. La mère demande le 2026-11-27 : demandée, non accordée. Attente du concepteur : 40 à 50 heures d'horloge, départ le 24 ou le 25.
- **D12 — Les mesures sont-elles lues en deux fois, M5 plus tard que les autres ?**
  - *Enjeu.* La V9 dit « lues une fois » (l. 315) ; M5 dépend de la lecture d'antériorité, qui suit de loin la relecture ; à la lettre, les autres mesures l'attendent.
  - *Options.* (a) Garder la lettre : une lecture, après la lecture d'antériorité ; aucun écart ; les mesures attendent. (b) Deux lectures scellées, chacune unique ; les premières connues plus tôt ; écart à un texte scellé, par additif contre-lu.
  - *Recommandation.* (a), confiance 0,6.
  - *Défaut.* Aucun. D'ici son mot, le véhicule porte (a), la lettre.
- **La colonne « matière première »** : son allumage est un écart à la V9 ; la matière n'existe pas à ce jour ; rien n'est demandé au véhicule tant que Lazar n'a pas tranché.

**Propositions qui restent à la mère** (conception v2, § 9) : la fiche hors contrat de longueur comptée comme fiche rendue ; les lignes de compte pour un compte non nul seulement ; le lieu où se porte la clé n° 40 ; l'effet d'A2 et d'A11 en course ; la voie du refus sans coût ; la case des témoins ; l'affinage de la colonne, voie (a) par défaut.

## 5. Ce qui dépend du lot 0

Marqué « [lot 0] » dans la v2 : la voie du refus sans coût et le retrait du texte fixe de rôle (§ 2.3) ; les trois étapes seules d'une génération (§ 2.9) ; le sort de chaque garde héritée (§ 2.13) ; le lecteur de fiches (§ 5.4) ; la conservation des réponses brutes (§ 6.2) ; le découpage du lot 8 (§ 7).

## 6. Mes écarts, pour la v2

1. La v2 est faite par copie de la v1 (`cp`), puis par remplacements à l'outil d'édition ; la v1 est relue à son empreinte après coup, inchangée.
2. `diff -u` rend le code 1 quand les fichiers diffèrent : ce n'est pas un refus. Ses deux lignes d'en-tête portent l'heure des fichiers.
3. Les heures par lot de la table du § 8 ne sont pas rechiffrées pour les ajouts de la v2 : c'est dit dans le texte.
4. Je n'ai relu aucun registre depuis la v1 : les décisions et les accords cités depuis sont portés d'après les messages reçus.
5. Les quatre fichiers vides laissés dans `lu/` à la v1 y sont encore.

— concepteur du véhicule, modèle F

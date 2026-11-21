# Vérification du lot 6 v3 du véhicule NA-1 — v1

**Verdict : Conforme.** Les corrections demandées sont portées et éprouvées : sous-classe, `__class__` falsifiée, imitation plate, envoi posé sur l'instance et envoi de la classe remplacé après l'import sont refusés aux états 1 et 2 ; aucun refus à tort à l'état 0 ; V8 et V10 sont tuées ; la chaîne entière et les 57 mutations passent sur une copie neuve à moi. Restent quatre contournements par modification du processus lui-même (classe modifiée avant l'import, code de la méthode échangé, méthode de la colonne vidée, `depart` remplacé après le contrôle) : le rapport en dit deux (F-1, F-2), les deux autres sont de même nature ; ils ne sont refusés ni éprouvés comme refusés (§ 2). Ce sont des points pour la mère, non des défauts de la lettre.

Vérificateur neuf, hostile ; je n'ai écrit aucun lot. Processeur seul : aucun fournisseur, aucune clé, aucune dépense, aucun commit, aucune attache de dépôt. Je n'ai pas listé le dossier parent. Aucune coupure ni refus rencontré.

## 1. Les quatre questions

1. **Sonde de câblage : TENU.** Refusés par `ArretCablageColonneNA`, ligne plantée non partie, aux états 1 et 2 : sous-classe qui surcharge l'envoi (S1), sous-classe muette (S1m), imitateur plat (S2), imitateur à `__class__` falsifiée (S3), sous-classe du lot 3 au départ juste (S4), journal ordinaire (S3c), envoi posé sur l'instance (S9) ; envoi de la classe remplacé après l'import (S10) ; état 1, journal de la colonne d'un autre état (renforcement). Journal exact (S0) : la garde de la colonne arrête la ligne plantée, comme voulu. État 0 : journal ordinaire, sous-classe qui surcharge, journal exact éteint, sous-classe muette : trois générations, aucun refus (S5, S6, S5b, S5c). Classe mère modifiée par enveloppe (S11) : la garde de la colonne s'exécute avant `super()`, la ligne ne part pas. Limites, non refusées : voir § 2.
2. **V8 et V10 : TUÉES.** Mes mutations (mêmes textes que celles du v2, rejouées sur `course_na_v3.py`) : V8 tuée par `test_au_coffre_par_refus_du_portier_porte_a_la_ligne_de_generation` (`0 != 1`) ; V10 tuée par `TestRefusDeSceauDuJournalG1::test_sceau_refuse_dit_a_la_ligne_d_arret` (`KeyError: 'journal_requetes_g1'`).
3. **Chaîne entière et mutations : TENU.** Copie neuve (v68, lots 2 v5, 3 v3, 4 v1, 5 v1, 10 a par leurs programmes, puis le programme du lot 6 v3, `--lancer-essais`) : **770 passés, 92 sous-essais, 0 échec**. Essais du lot 6 v3 collectés : 54 + 44 + 29 = **127** (égal au rapport). Mutations du lot rejouées par son programme : **59 jouées, 57 tuées, 0 survivante, 0 invalide**, T0 passe, T1 survit. Table d'empreintes du lot : `sha256sum -c` code 0.
4. **La v3 casse-t-elle autre chose ? NON.** `diff` v2 → v3 : `course_na_v3.py` ne change que la version, les deux noms de sortie, la version du journal, la référence `_ENVOI_DE_LA_COLONNE` (l. 96), le bloc du refus (l. 186-196) et le nom de la course ; le lanceur ne change que les noms ; les fichiers d'essais portés ne perdent aucune ligne (la seule suppression de l'essai de câblage est le renommage des imports) et gagnent les essais neufs. Aucun nom de sortie `-na-v1.` ou `-na-v2.` ne survit dans le paquet, hors le texte cherché par la mutation N23. Aucune régression sur les essais du v2.

## 2. Ce que la v3 ne refuse pas (sonde, § 3 : tout est hostile et dans le processus)

| cas | état | rendu | ligne partie ? |
|---|---|---|---|
| P1 classe de la colonne modifiée **avant** l'import de `course_na_v3` | 1 et 2 | course finie | **oui** |
| S12 `Colonne.examiner_octets` vidée sur la classe après l'import | 1 | course finie | **oui** |
| S13 `__code__` de la méthode d'envoi échangé après l'import (l'identité de la fonction ne change pas) | 1 | course finie | **oui** |
| S14 `depart` du journal remplacé après la construction (F-2) | 1 | course finie | **oui** |
| S11 classe mère `jn.JournalRequetes.journaliser_envoi` enveloppée | 1 | `ArretColonneNA`, ligne non partie | non |

P1 et S14 sont les limites F-1 et F-2 du rapport, dites. S12 et S13 ne le sont pas : le contrôle par identité de fonction ne voit pas un échange de `__code__`, et rien ne protège les méthodes de `Colonne`. Il s'agit de code qui modifie le processus où tourne la course : le contrôle de câblage ne peut pas tenir contre cela ; un contrôle d'empreinte du code chargé (hors de ce lot) serait l'outil. Je ne les compte pas comme défauts de la décision de la mère (« type exact »).

## 3. Mutations à moi, prédites avant lancement

Programme `sondes/mes_mutations_v3.py` ; journal `journal-mes-mutations-v3.txt`. Essais joués : les trois fichiers du lot 6 v3, `-x`.

| id | faute | prédit | rendu | cause |
|---|---|---|---|---|
| V8 | « au coffre par refus du portier » à 0 | tuée | tuée | `0 != 1` |
| V10 | refus de sceau tu | tuée | tuée | `KeyError` |
| X3 | envoi posé sur l'instance admis | tuée | tuée | arrêt non levé |
| X4 | envoi de la classe remplacé admis | tuée | tuée | arrêt non levé |
| X5 | type exact → `isinstance` | tuée | tuée | hostiles non refusés |
| X6 | type exact → `journal.__class__ is` | tuée | tuée | `__class__` falsifiée non refusée |
| X7 | `type_journal` lu par `__class__` | tuée | tuée | `ImitateurClasse` attendu |
| X8 | nom du bilan revenu au v1 | tuée | tuée | `test_noms_de_sortie_en_v3` |
| X9 | refus trop large (état 0) | tuée | tuée | départ refusé à tort |
| X10 | renforcement : état du journal supérieur admis | tuée | tuée | essai de renforcement |
| X11 | commentaire inerte ajouté près de la référence | survit | survit | (témoin inerte) |
| X12 | fabrique absente : repli sur le journal ordinaire | tuée | tuée | message de cause |

Douze sur douze prédictions tenues ; la mutation X6 (`__class__`) montre que l'essai d'imitation de classe est bien celui qui la tue.

## 4. Relevé de méthode

**Chaîne de raisonnement.**
1. Mandat v1 et erratum lus au tour précédent ; message de la coordination (décisions de la mère : type exact ; sorties en v3) ; rapport du lot 6 v3 lu en entier (`rapport-developpeur-lot-6-na-v3.md`).
2. `diff` v2 → v3 du module, du lanceur, des trois fichiers d'essais : changements bornés (§ 1, question 4).
3. Lecture de `course_na_v3.py:173-201` : `isinstance` du lot 3, puis `type(journal) is`, puis identité de la méthode d'envoi de la classe et absence de `journaliser_envoi` dans `vars(journal)`, puis contrôle de départ de même état.
4. Rejeu de la chaîne (770 passés), des 57 mutations, collecte des 127 essais.
5. Sonde `sondes/sonde_cablage_v3.py` (modes `base` et `avant-import`) : résultats du § 1 et § 2, rejouables.
6. Mutations X3 à X12, V8, V10 : prédictions écrites dans le fichier avant lancement (§ 3).

**Objets de contrôle.** Faux par construction : sous-classe, imitateurs, envoi sur l'instance ou la classe, journal ordinaire, aux états 1 et 2 ; attendu : refus nommé, ligne non partie ; rendu : conforme. Vrai : journal exact aux états 1 et 2 (S0, la garde de la colonne arrête la ligne), états 0 (S5 à S5c, départ) ; conforme. Mécanisme éprouvé jusqu'à son échec : S12, S13, P1, S14 (non refusés, § 2).

**Premier pas non justifié.** Pas 3 pour la portée : que la modification du processus lui-même soit hors du modèle de menace. Le justifierait le mot de la mère.

**Mode d'échec affecté.** Épreuve qui ne peut pas échouer ou pas réussir, appliquée au refus de type exact : tenu pour les sept cas de l'état 1 et 2 testés et pour l'état 0 ; non tenu pour quatre modifications du processus (§ 2).

**Dérivation de l'énoncé seul.** Sans objet : je suis vérificateur, non agent de re-dérivation.

**Trouvaille de côté.** (a) La garde E7 de `configuration_course_na_v1.py:300-301` est redondante (dite par le rapport, § 3, W1). (b) Le contrôle de la méthode d'envoi par identité se trompe sur un échange de `__code__` ; un contrôle d'empreinte du code serait plus fort.

**Évaluateur et conseil.** Ce qui juge mon verdict : la sonde (témoins S0, S3c, S5 admis avant les cas hostiles) et douze mutations prédites. Je pourrais être jugé trop clément si la mère juge les modifications du processus dans le modèle de menace ; trop sévère si elle les juge hors du modèle.

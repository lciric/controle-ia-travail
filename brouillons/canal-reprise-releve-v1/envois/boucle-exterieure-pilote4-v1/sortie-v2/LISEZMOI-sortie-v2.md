# LISEZMOI de la sortie — registre v2, protocole et briefs de la boucle extérieure du pilote 4 — v2

Fichier ouvert le 2026-10-26 à 03:47:59 UTC (heure lue sur `date -u` dans la commande qui écrit cette ligne), après la lecture complète des pièces fournies et avant l’écriture des autres fichiers de `sortie/`.

Auteur : un sous-agent neuf de la lignée conv-audit, sur le brief v2 (`LISEZMOI-brief-v2.md`) et le brief v1 qu'il remplace
en partie. Je n'ai écrit aucune des pièces fournies. Je n'ai lu aucun score ni aucun fait de course. Rien de ce dossier
n'est servi à un organisme. Écriture de ce fichier achevée le 2026-10-26 à 03:59:16 UTC (heure lue sur `date -u` dans la commande qui
écrit cette ligne).

## 1. Ce que j'ai fait

- **Vérifié** l'empreinte du brief v2 : `bb472681e1bd1216ad2e3b4ea4364d8b07f6b23c5fabbd52673eaa117f47a661`, égale à celle
  de la demande. Vérifié les douze fichiers de `fournis/` contre `../EMPREINTES-fournis-v1.txt` : douze sur douze égaux.
- **Lu en entier** : le brief v2 ; le brief v1 ; le registre v1 ; le texte v4 du pilote (`782b858c…`) ; la contre-lecture 7
  (`68daac56…`), dont P4C7-01 et P4C7-02 ; la v3 du texte (« P4v3 », `de7a5559…`) ; le brief du script de lecture
  (`c86be1a1…`) ; la synthèse « neuron explorer » v2 (`2642bd8a…`) ; la synthèse « lecture du pilote » (`a8e1ed64…`) ; la
  question « agents sur le noyau » (`6de36af7…`) ; le relevé v7 des mots de Lazar (`a99eb306…`) ; et, pour information
  seulement, les hypothèses du pilote décisif (b) (`903c6b51…`) et le dessin de la primitive d'expérience (`9c5ada0c…`).
- **Calculé sans aucun score** (Python, bibliothèque standard, mode isolé, aucun fichier écrit) : z = 2,2414 au niveau
  97,5 % ; bornes basses maximales 0,7818 et 0,7049 ; tailles de classe minimales 26, 21 et 16 ; valeurs p exactes du test
  de McNemar pour des comptes hypothétiques ; 1/48 − 1/72 = 1/144.
- **Écrit**, dans `sortie/` seulement : le registre v2, le protocole v1, les briefs des agents v1, ce LISEZMOI, et le
  compagnon `.sha256` de chacun.
- **Fiches** : gardées HC-P4-01, 07, 09 ; corrigées HC-P4-03, 04, 05, 06, 08, 11, 12 ; déclarées « indécidable par ce
  pilote » HC-P4-02 (l'issue « au-dessus » de (ii) est inatteignable) et HC-P4-10 (comparaison des deux objets). Le détail
  est dans la table « v1 → v2 » du registre.

## 2. Choix faits seul (une ligne chacun)

1. Point 4 du brief v2 lu au sens du texte v4, point 3 (« du script de lecture, ils ne voient que la sortie ») : les faits mécaniques hors de l'archive restent lisibles, par un relevé dérivé seulement.
2. Les agents ne lisent ni l'extrait mécanique brut, ni `LANCEMENT.md`, ni les journaux d'appels : tout passe par le relevé (B), sans texte ni score.
3. Sous la retenue, la boucle ne lit rien, fiches mécaniques comprises, car plusieurs portent un bit sur les scores de `test` (canaux (b) et (d), retour arrière).
4. « Indécidable sans graines de plus » renommé « indécidable par ce pilote » (mots de P4C7-02), et étendu à HC-P4-02.
5. Sous-verdict « indécidable (non observable) » de la v1 gardé, avec la cause « seulement dans l'archive fermée ».
6. Opération (2) permise aux agents pour HC-P4-04 et 05 seulement (différence de deux scores de `test` rendus, dans une course, contre un seuil du code), sous réserve de conv-audit.
7. Aucune valeur numérique de `test_final` dans une pièce de la boucle : la cellule et son libellé seulement.
8. Branche « éliminée si borne haute sous la référence » de HC-P4-02 retirée : ce n'est pas un libellé du point 4 bis.
9. Clause « les intervalles de g0 et de g3 se recouvrent » de HC-P4-11 retirée, pour la même raison.
10. Affirmation de la v1 « pas minimal toujours plus que 0,01 » corrigée : une différence nette peut valoir 1/144 ≈ 0,007 (illustratif).
11. Exception du retour arrière lue par P4v3 (génération 0 sans mise à jour) ajoutée à HC-P4-05.
12. HC-P4-04 n'est « tenue » que si au moins une différence est ≤ 0,01 (déclenchement éprouvé).
13. Ligne « Entrées » ajoutée à chaque fiche.
14. Après la seule v6.2.1 : rejet provisoire tenu pour final (sous 0,0125, Holm rejette quel que soit le rang) ; non-rejet final seulement au-dessus de 0,05 ; sinon « en attente ».
15. L'agent qui « casse exprès » est le contre-lecteur, et tout agent d'audit chargé d'attaquer un verdict.
16. Aucune valeur par défaut pour sa famille de modèle ; sans valeur fixée par Lazar, aucune proposition ne sort d'une ronde.
17. La ronde 1 de la boucle est la course du pilote 4 : au plus deux relances par objet.
18. Règle d'arrêt : « indécidables sans graines de plus » lu comme « tout indécidable, ou tenue sans correction attachée ».
19. Un désaccord entre l'analyste et le contre-lecteur empêche la fiche de motiver une correction dans la ronde.
20. Dossiers d'audit donnés à un agent distinct de l'analyste réel, avec le même brief ; aucune erreur tolérée sur les fiches que des faits déterminent.
21. Contre-lecteur en deux parties ; la partie A, à l'aveugle, est empreintée avant toute lecture de l'analyse.
22. Liste close des fichiers d'accompagnement d'une correction, sur le modèle de la correction de la v6.2.1.
23. Les deux seuils du critère de fin comptés comme un seul facteur.
24. Noms proposés : `ouverture-lecture-<course>-v1.txt`, `MANIFESTE-DOSSIER-v1.txt`, `releve-mecanique-<course>-v1.txt`, `verdicts-…`, `correction-…`, `contre-lecture-…`, `journal-essais-boucle-pilote4-v<N>.md`.
25. « dollars » écrit à la place du code de devise ; « UTC » gardé, comme la sortie de `date -u` et toutes les pièces.

## 3. Points à trancher par conv-audit (une ligne chacun)

1. Pousser ces quatre fichiers et leurs compagnons ; vérifier que la poussée précède la fin de la première course (texte v4, § Décisions, 02:17), sinon l'écrire au journal.
2. Faire contre-lire le registre, le protocole et les briefs par un agent neuf avant le premier usage (relecture gardée).
3. Confirmer ou refuser le choix 1 (faits mécaniques lisibles par un relevé dérivé).
4. Confirmer ou refuser l'opération (2) (HC-P4-04 et 05) ; le champ `<opération-2>` des briefs en dépend.
5. Obtenir de session-depot le relevé (B) et son script, essayés sur la série v13 (cas sain) et sur un artefact.
6. Demander une version du script de lecture qui rende : le score de `test` rendu par génération ; le nombre sans réponse par cellule ; b et c ; un fichier par course, sans les valeurs p de l'autre course.
7. Désigner les auteurs des gardes G1 à G8 et des dossiers d'audit ; les essayer avant la première lecture.
8. Fixer la forme d'un texte de relance et celle des noms de course.
9. Dire si un passage purement mécanique serait admis sous la retenue (le protocole dit non).
10. Confirmer « ronde 1 = course du pilote 4 » et la règle d'arrêt étendue (choix 17 et 18).
11. À l'ouverture : si un texte nouveau (graines) change la règle de lecture, faire un registre v3 avant la première lecture.

## 4. Points à soumettre à Lazar (une ligne chacun)

1. La famille de modèle de l'agent qui « casse exprès » (le contre-lecteur) : même famille ou famille différente ; aucune valeur par défaut (synthèse « neuron explorer », décision 2).
2. La question des graines de plus (02:05), qui tient la retenue : la boucle ne démarre qu'à sa décision, ou sur un « lis ».
3. Un plafond de dépense pour les relances de la boucle (règle d'arrêt, protocole, § 7) : aucun n'est fixé.

## 5. Écarts à ce brief, déclarés

1. Lu un fichier hors de `fournis/` en plus du brief v2 : `../EMPREINTES-fournis-v1.txt`, que le brief v2 désigne pour les empreintes. Listé `sortie/`, vide, avant d'écrire. Rien d'autre hors de `fournis/`.
2. Corrections du registre v1 au-delà des points 1 à 6 du brief v2 (choix 10 à 12) : faites parce qu'elles ne tenaient pas ; déclarées dans la table « v1 → v2 ».
3. Aucune poussée sur le canal : sans `git`, elle revient à conv-audit.
4. L'heure du début de ma lecture n'est pas consignée : la seule heure de début écrite est celle de l'ouverture de ce fichier.
5. Python lancé une fois, en mode isolé, pour vérifier des nombres sans score ; aucun fichier écrit par lui.

## 6. Empreintes (format « empreinte, deux espaces, nom nu »)

```
3881fa16070be8824f9b4d7987a432dc23ad34d31df7a3d971ffbc65ab433623  registre-hypotheses-conception-pilote4-v2.md
23e4e1ba07b04f43021a39cc66cc41711c0244649597a0bb420b04d488b090a4  protocole-boucle-exterieure-pilote4-v1.md
b5f61890ac40b3f232f6b92a4f1c6d15742e2e19bf845798525f6d1c209bbdfd  brief-agents-fin-de-course-v1.md
```

L'empreinte de ce fichier est dans son compagnon, `LISEZMOI-sortie-v2.md.sha256`.

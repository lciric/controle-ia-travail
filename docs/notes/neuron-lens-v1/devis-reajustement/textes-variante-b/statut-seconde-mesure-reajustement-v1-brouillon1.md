# Statut de la seconde mesure — réajustement de nos lentilles R et S (lecture par lentille neuronale, Llama 3.1 8B Instruct), variante B — v1, brouillon 1

- **Pièce de classe A**, à contre-lire (R2) puis à sceller **avant la création de la machine** (devis v9, § 5, point 7). Ce brouillon
  est scellé tel quel ; une correction est un brouillon neuf (R12).
- Rédacteur : rédacteur neuf, sous-agent de la session des lentilles (`session_01Qi7Gr3vedYVukbyqBbHd7z`), sur le mandat
  `docs/notes/neuron-lens-v1/devis-reajustement/mandats/mandat-redacteur-statut-et-plan-seconde-mesure-v1.md`
  (`26af6c39dcb4b989f53109e62ea96f792258c34781b5ca35a77efcf12413a9ce`, empreinte vérifiée par `controle_ia.scellement verifier`) ;
  modèle servi : celui que nomme le mot de Lazar du 22 novembre pour les pièces délicates écrites en autonomie (§ « Écart d'usage
  déclaré »). Il n'a écrit ni le texte gelé de la tranche, ni son addendum, ni le plan de lecture de la tranche, ni le verdict du 18,
  ni le devis, ni le critère d'identité, ni le code, ni les commandes, ni aucune course.
- Heure (`date -u`) à l'ouverture du travail : 2026-11-22T04:56:13Z ; l'heure du scellement est celle du fichier compagnon.
- Branche `claude/brave-galileo-jhp684`, écrit sur le commit `33371746d`.

## Déclaration : ce que je savais avant d'écrire (R4)
- Lu en entier : `CLAUDE.md` ; le mot de Lazar du 22 novembre (`mot-lazar-go-reajustement-autonomie-2026-11-22-v1.md`, `ed47f2e3…`) ;
  le devis v9 (`devis-reajustement-lentilles-b-beta-v9.md`, `064e735a…`) ; le critère d'identité v8
  (`critere-identite-reajustement-lentilles-v8.md`, `541bb86b…`) ; le texte gelé de la tranche (`texte-gele-tranche-b-beta-v1.md`,
  `f5d46860…`) ; le plan de lecture de la tranche v2 (`lecture-b-beta/plan-de-lecture-b-beta-v2.md`, `391c3b1a…`) et sa contre-lecture
  (`lecture-b-beta/contre-lecture-plan-de-lecture-b-beta-v1.md`, `bf3e2d75…`) ; **le verdict du 18** (`lecture-b-beta/verdict-b-beta-v1.md`,
  `3a9b947e…`) et l'accord de Lazar (`lecture-b-beta/accord-lazar-verdict-b-beta-v1.md`, `8469add5…`) ; la décision posée sur l'entrée
  des lentilles (`decision-entree-lentilles-programme-v1.md`, `6aaf54e7…`) ; le gabarit de préenregistrement
  (`prereg/gabarit-preregistrement-v1.md`, `8cad4371…`) ; les lignes 1 à 60 de l'addendum partie 1 v3
  (`addendum-texte-gele-tranche-b-beta-v1-partie1-v3.md`, `bd8067dc…`). Empreintes recalculées, égales à celles que citent le mot de
  Lazar, le devis et le plan.
- **Je connais donc le verdict du 18** : « partiel » (rang 5) ; B-1 « autre » (différence entre moitiés au-dessus de 0,10 aux couches
  0, 1, 2 de R `mid`, 0 et 1 de R `out`, 31 de S `out`) ; B-2 « autre » (seule condition manquée : `pass` 0,8594 à la couche 8) ; B-3
  et B-5 « reproduit » ; B-6 « intermédiaire » (20 couches sur 21) ; B-7 « autre » (couche 15) ; aucun audit, aucune chaîne en défaut.
- Noms de fichiers seulement, sans contenu : la liste des dossiers `docs/notes/neuron-lens-v1/`, `devis-reajustement/` et
  `lecture-b-beta/`. Rien lu de `diag/`, `runs/`, `docs/verdicts/`, des branches `donnees/*`, `calcul/*`, `verdict/*`, `lecture/*`, ni de
  rien de l'apprentissage des sondes sur la tâche, de P3, P3-bis, T0.6, T0.7, de l'étape B, du bras d'attaque, du saboteur à budget,
  des fichiers « consigne-privee » ou « conception-ii-b ». Aucune seconde course n'existe.
- Ce statut ne contient aucune règle choisie en vue de ce verdict ; il recopie la décision 4 de Lazar et les règles du critère v8.

## 1. Objet
Ce texte fixe le **statut de la seconde mesure** — la course de la tranche rejouée en entier sur une autre machine (variante B du
devis v9, § 2) — tel que la décision 4 du mot de Lazar du 22 novembre l'accepte : « le verdict du 18 reste ; la seconde course est
rapportée à côté ; tout désaccord est un nœud de Lazar ». Il ne fixe ni l'identité des lentilles (critère d'identité v8, qui
**prime** sur ce texte), ni les règles de lecture de la seconde course (plan de lecture,
`plan-lecture-seconde-course-reajustement-v1-brouillon1.md`, dans ce dossier, ou la version scellée qui le remplace).

## 2. Statut, en cinq règles
1. **Le verdict scellé et accepté du 18 reste celui de la tranche.** Le verdict « partiel » (`verdict-b-beta-v1.md`, `3a9b947e…`),
   accepté par Lazar le 19 novembre (« go accepter », `8469add5…`), n'est ni remplacé, ni révisé, ni suspendu, ni moyenné par la
   seconde course, quel que soit son résultat. La tranche reste close (accord, « tranche de l'ajustement de nos lentilles close »).
2. **La seconde course est lue par un lecteur neuf, sur un plan scellé avant la création de la machine, et rapportée à côté.**
   Le lecteur n'est ni auteur (du texte gelé, de l'addendum, du plan de lecture de la seconde course, de ce statut, du devis, du
   critère, du code, des commandes, du lanceur) ni opérateur (de la session des lentilles ou de la course), ni celui qui a appliqué le
   critère d'identité. Il applique les seuls critères gelés de la tranche, recopiés avec leur source dans le plan.
3. **Aucun critère de concordance n'est fixé après coup.** Ce qu'est un « désaccord » entre la seconde course et le 18 est fixé
   **d'avance** par le plan (son § 6), sur les seuls libellés des critères gelés, sans seuil, sans tolérance et sans qualificatif :
   aucun chiffre ne dit « concordant » ou « proche ».
4. **Tout désaccord est un nœud de Lazar** (hiérarchie de décision, `CLAUDE.md` : arrêt, attendre le mot). Le lecteur le rapporte, il
   ne le tranche pas ; aucun texte de lecture qui emploie la lentille concernée n'est scellé avant le mot de Lazar sur ce nœud.
   Un désaccord **de lecture** (entre le verdict du lecteur et le fichier des verdicts de la seconde course) est autre chose : il suit
   la règle du texte gelé, § P.7 (« rapporté et tranché par un second lecteur neuf, sans nouvelle mesure »).
5. **Rien de ce texte ne fait monter une mention d'identité** : la seconde course ne dit jamais que la lentille rangée est celle du 18
   (critère v8, § 1 et § 5 : « seul le premier palier établit l'identité »).

## 3. Ce que vaut la seconde course, selon le verdict d'identité de chaque lentille
Chaque lentille est jugée seule (critère v8, § 4) ; cas mixte : chacune suit sa ligne.

| verdict d'identité (critère v8) | ce que la seconde course est pour cette lentille | ce qui décrit la lentille rangée | lecture avec cette lentille |
|---|---|---|---|
| **palier 1** (octets identiques) | une **seconde mesure de la même lentille** sur un autre exemplaire du même modèle de carte ; rapportée à côté | le verdict du 18 et ses mesures, avec leurs limites (critère v8, § 5) | selon le critère v8, § 5 ; un désaccord (plan, § 6) est un nœud de Lazar et retient tout texte de lecture qui l'emploie jusqu'au mot de Lazar |
| **palier 2**, seconde course **complète** | **la seule mesure de la lentille rangée** | la seconde course seule, lue par le lecteur neuf ; **le verdict du 18 ne se transporte pas** | seulement **après** la lecture de la seconde course, **dans les limites que fixe le plan** (son § 5 : critères gelés et couches), par un texte de lecture neuf et contre-lu, sous l'accord GO-2026-11-19-33 |
| **palier 2**, seconde course **arrêtée avant la fin de ses mesures** (plan, § 4) | aucune mesure propre | rien : la lentille **reste sans mesure propre** | **traitée comme en variante A** : aucune lecture sans nœud de Lazar (critère v8, § 5) ; le billet le dit |
| « différente », « non comparable », mention suspendue, non réajustée | aucune | rien | aucune sans nœud de Lazar (critère v8, § 5) ; la seconde course est lue et rapportée comme fait, sans rien prononcer sur cette lentille |

**Au palier 2, cette seconde course est la seule mesure de la lentille rangée.** Ses mesures ne s'ajoutent pas à celles du 18 et ne
se comparent à elles que pour rapporter un désaccord ; elles ne valent que pour la lentille rangée, dans les limites de la lecture.

## 4. Parole
- **Palier 1, phrase permise** : « Les mesures de la tranche ont été refaites, avec la même lentille (fichier d'ajustement identique à
  l'octet), sur une autre machine ; elles sont rapportées à côté du verdict du 18 novembre, qui reste celui de la tranche. »
  (*“The slice's measurements were repeated with the same lens (byte-identical fit file) on another machine; they are reported
  alongside the 18 November verdict, which remains the slice's verdict.”*) Suivie, s'il y a lieu, de la liste des désaccords (plan,
  § 6) et de l'état du nœud.
- **Palier 2, phrase permise** : « Les seules mesures de la lentille [R | S] rangée sont celles de la seconde course, lues par un
  lecteur neuf sur un plan scellé avant la course ; le verdict du 18 novembre, qui reste celui de la tranche, ne la décrit pas. »
  (*“The only measurements of the stored lens [R | S] are those of the second run, read by a fresh reader under a plan sealed before
  the run; the 18 November verdict, which remains the slice's verdict, does not describe it.”*) Elle accompagne la phrase du palier 2
  du critère v8, § 5, dont la fin se remplit par « ont été refaites sur elle et sont rapportées à côté ».
- **Phrases interdites** : « la seconde course confirme (ou infirme) le verdict du 18 novembre » ; « le verdict est révisé »,
  « remplacé », « consolidé » ; « la mesure est robuste au changement de machine », « stable d'une machine à l'autre » ; toute phrase qui
  tire de deux courses un effet du matériel mesuré en général (une seule paire de courses) ; toute phrase qui prête à la lentille du
  palier 2 une mesure du 18. À libellés égaux (plan, § 6), seule est permise : « la seconde course rend les mêmes libellés que le 18 ».
- Les règles de parole du critère v8, § 5 (chiffres obligatoires, aucun qualificatif, phrases interdites) s'appliquent en plus.

## 5. Ce que ce texte ne fait pas
Il ne change aucune règle du critère d'identité v8, aucun seuil ni aucune issue du texte gelé, aucune décision du devis v9. Il ne fait
entrer aucun résultat dans le programme : aucun résultat n'entre dans T0.7, T0.8, G0, G1 ni dans un préenregistrement du programme
sans nœud de Lazar (texte gelé, « Portée et séparations ») ; chaque usage d'une lentille dans une expérience le dit dans son
préenregistrement (R1). Il n'ajoute ni hypothèse ni revendication. Il ne lance rien et ne dépense rien.

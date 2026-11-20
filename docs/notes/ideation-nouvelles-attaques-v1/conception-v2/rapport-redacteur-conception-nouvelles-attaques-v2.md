# Rapport du rédacteur — conception de la course « nouvelles attaques », trois générations — v2

- Auteur : rédacteur neuf, modèle F. Écrit le 2026-11-20 ; relevés de `date -u` : 01:01:43Z avant l'écriture des pièces.
- Version : la v2 remplace la v1 (`61a35c2bfa92b3e311c25cfc1a9291725e796c4e61d17acfb67b50fdf6a30969`) après la contre-lecture `contre-lecture-conception-nouvelles-attaques-v1.md` (`ae9d4ae44027476bee4821e72c4e9f9b12f39d10f3dc6749ae60ae61d07c1fed`, verdict « Conforme après corrections ») : corrections C9, C14, C18 et C20 appliquées à texte exact ; la v1 reste archivée, non modifiée. Les § 2, § 3 et § 7 décrivent la session qui a écrit les pièces v1 et ne sont pas retouchés : le § 7, point 5, garde le chiffre de la v1, que le § 5, D7, corrige en 162,56 USD. Les pièces v2 et leurs empreintes sont au rapport des corrections, `rapport-redacteur-corrections-nouvelles-attaques-v2-v1.md`. La v2 elle-même n'est pas contre-lue.
- Processeur seul. Aucun appel à un fournisseur de modèles, aucune dépense, aucune machine, aucun lancement de l'organisme ni de l'orchestrateur, aucune écriture dans le dépôt, aucun commit. Réseau : un seul `git fetch origin main`. **Aucun refus d'outil ni de classifieur.**
- Mandat (`8fd94f6f78e51665eccfd2bc11c634f7bce207f9ed70d237e464e2d9b3eda294`) et complément 1 (`226ea15243c947164d4c3595c350d90fea980694f7d4903cf8dac33e56b81fdd`) : les deux empreintes sont vérifiées contre leurs compagnons.

## 1. Verdict

1. Les trois pièces sont écrites : la question, l'ordre de course, le devis avec son programme et sa sortie. Aucune ne contient de méthode, de procédé ni de détail opérant ; la question demande des idées, et interdit tout champ « comment faire ».
2. **Ligne de course proposée : 450 USD exactement ; plafond total 456 USD** (cinq espèces, trois générations à 150 USD ; plus 5 USD d'épreuve des témoins et 1 USD de sonde de refus). Attendu 218,72 USD.
3. **La course est portée par une version de l'orchestrateur postérieure à celle que ton mot GO-2026-11-20-05 (1a) réserve au palier 1 de l'héritage, et qui lit le registre des tentatives (2b) ; elle reste à écrire.** La version 68 ne joue plusieurs générations qu'en moteur simulé. Il manque aussi un lanceur qui suit le 11, un additif scellé et une configuration propre. La course ne joue aucun test de mort : ni interrupteur des tests de mort, ni machine jetable.

## 2. Pièces rendues

Dossier : `/tmp/claude-0/-home-user-controle-ia-travail/227b647d-2ece-5654-bf04-8493b3ed2f19/scratchpad/redacteur-nouvelles-attaques-v1/`. Chaque fichier a son compagnon `.sha256` ; les empreintes sont dans ces compagnons et dans ma réponse.

- `question-course-nouvelles-attaques-v1.md`
- `ordre-course-nouvelles-attaques-v1.md`
- `devis-course-nouvelles-attaques-v1.md`
- `calcul_devis_course_nouvelles_attaques_v1.py` et sa sortie `calcul-devis-course-nouvelles-attaques-v1.json` : joué deux fois, sorties comparées à l'octet par `cmp`, égales (`216cfbfceb026c7d83e153182232ee6f95a680cefd60e54bfaa0a1193b4ba3e4` les deux fois)
- ce rapport

Le sous-dossier `lectures/` garde les pièces extraites de `main` et le second jeu du calcul ; ce ne sont pas des pièces rendues.

## 3. Sources lues, avec empreinte recalculée

| pièce | empreinte | lu |
|---|---|---|
| question pilier attaque v1 | `29870ac9a8091c165375c51f4b74d6e0f38ae60d2e8754872ff70fb3077820c4` | en entier |
| question pilier attaque v2 | `2dbad4b75d20fadc3147be9eff07f2e77c2f82fe4f609ab1c29388ab46c4bb42` | en entier |
| question du coffre v2 | `7d22b64e64c41cac4100d0dfbe825c598daeedfb0f515e0aab3f17ffe661db8c` | en entier |
| N-044 v1 | `2b70bdac014d366d058a530680d016663b35ed73b8ca0cae9f2369206f5004bf` | en entier |
| N-045 v2 | `c7b05e39de381cee1d5ec2276745a0310bd3cc0857a6be0e0fb14eeb5042261d` | en entier |
| N-049 v1 | `8a5bf5e57e2bb447467388acb572e032d1a6a578a868db1b7304263a1c9d4460` | en entier |
| N-058 v1 | `854f2724864f1e45394e001f4aca7b0248753e5d2b0a66991e2ee8a7be87de9d` | en entier |
| N-065 v1 | `f820e90da0920d505d22bc7b33fad4906181d43bd5af7e79418a3c161a8a65c4` | en entier |
| note de décision de 22:00 (`main`) | `b7f148a8794cddfc4b98a746c113063837f1fc72e52a3fed22a0cd9a3b4bd03e` | en entier |
| note de 22:41 (`main`) | `574c2fc8c3a713a7988e7b7d7d176fa699c0ebd7e71841c1937b1922a2282c02` | en entier |
| `registres/go.md` (`main`, commit `af32512da992eabef9129f7cd3dc96380af49c35`) | `7fce43740a5965a72bd5315da45e44346c6742ead5293c332eb4a4fbd554d9a1` | lignes `GO-2026-11-19-19` à `-21`, `-89` à `-98`, `GO-2026-11-20-01` à `-03` |
| `registres/decisions.md` (`main`) | `74f002388e9697cc892c5e5b144c219e0cbf80b8d432501dfbb3b5b694351704` | R-606 à R-611, R-3735 |
| `registres/depenses.md` (`main`) | `43cad7c041ba7f5da3547fa52bcfcf004a3768ebfedb202f86386e20adfe2879` | lignes 534 à 539 |
| fiche des quatre décisions v7 | `5ddfae1887c14a950b1f05d274364930aeb50c216540ce881797f0acdb3f6bac` | en entier |
| contrôle du différentiel de la fiche v7 | `522a3c46aa588b72cae3ff723451166337f2181c7600560e40af686a12725a09` | empreinte seulement |
| rapport du développeur de la version 68 | `ad42b7229a8e37aae823b1041a3acf1db91ee4053f5fec61136b6fd178b59aa6` | en entier |
| contre-lecture de la version 68 | `d2cfeac1a8d96a732c2cd9341aecc96a12778fff9b20ccfa0fef1edb2d47e325` | empreinte seulement ; ses constats sont pris de la fiche v7 |
| contre-lecture de la fiche v1 de la version 68 | `af90dae48d9e35770f00d1ee66becd26986caea13d76ea2f930cb5d83ec8e247` | empreinte seulement ; la fiche v7 l'applique |
| devis v2i de la course d'auto-conception | `a8c033cdc66b14f666a6a45bb6184e9e902369d6a330b672ac82a4fe13f64ba0` | en entier |
| devis v1 de la course d'auto-conception | `50e7d2f1dc713098edf5d69b6f46ded96a42423f6c50c528b02cf3781f96a80b` | en entier |
| devis v2 et v2b de la course d'auto-conception | `fa39c545…`, `b2319472…` (entières au devis) | empreinte seulement |
| devis de la course d'idéation sur le pilier attaque v2 | `531849e3e4f55de3ae5f097033fdcb50bd209ac88670547b3060fb869b10eea3` | en entier |
| devis de l'héritage v5 | `30c87fa68d9d6fa5e961edc45764fe58172b1a1b20d45fd3065a678b42f2880d` | en entier |
| synthèse d'antériorité v2b | `b828d800913c8960d04b6822de8f10fc51ee573c660c84f6658ea6ba68796b8d` | empreinte seulement |

Non lu : le code de l'orchestrateur ; toute sortie d'une course passée ; le coffre.

## 4. Choix du rédacteur, et pourquoi

1. **La question demande des menaces, par case.** Une case croise ce que le moniteur suppose, une menace du programme et un étage de lecture. Les valeurs viennent de pièces du dépôt. C'est ce qui la sépare des trois questions scellées, et ce qui rend la nouveauté jugeable par classe.
2. **« Inédite » est une étiquette bornée** : « inédite au périmètre vérifié le [date] », à deux lecteurs, aux sources de l'ordre de course, § 9. Non tranchée : non dite inédite.
3. **Aucun test de mort.** Une idée n'est pas une loi sur des données ; la fiche v7 le dit déjà des cartes d'auto-conception (décision 3). La course s'épargne ainsi l'interrupteur, la machine et le mot « survit ».
4. **Tâches fraîches = cases tirées sans remise**, onze par génération, et une famille entière tenue à l'écart.
5. **Héritage : le registre des tentatives de ton mot 2b**, sans verdict ni tri ; sa forme dans cette course est D2. Les mesures de l'héritage sont dites descriptives : la course n'a pas de bras témoin.
6. **Régime d'usage.** Code et composition figés ; ce que N-045 appelle « appris » se lit après la course et nourrit la conception suivante. Je l'écris sans le gonfler.
7. **L'oracle de la course est l'épreuve des témoins plantés** ; les juges sont joués pour information.
8. **Le devis prend la course v9 pour unité**, sans rabais, avec une garde sur la longueur des consignes.
9. **Une règle que j'ajoute** : aucune carte de cette course ne nourrit le mode tenu à l'écart, parce que la mère, qui conçoit les moniteurs, lit toutes les fiches.

## 5. Ce qui te revient

### D1 — La ligne de course et la composition
**Décision.** Quelle ligne de course accordes-tu, à quelle composition ?
**Enjeu.** La dépense ; la diversité des proposeurs ; la charge de relecture de la mère ; le crédit de la clé du premier relais.
**Options.** (a) cinq espèces, ligne 450 USD, total 456 : la composition mesurée et la diversité entière, mais la dépense la plus haute, 282 fiches à relire et un crédit à recharger d'au moins 287,44 USD. (b) trois espèces, ligne 195, total 201 : le tiers du prix, mais deux espèces retirées sans preuve. (c) deux espèces, ligne 150, total 156 : le crédit lu suffit, mais la diversité la plus pauvre.
**Recommandation.** (a), confiance 0,55. **Défaut.** Aucun : dépense.

### D2 — La forme du registre servi, sous ton mot 2b
**Décision.** Dans cette course, qui n'exécute aucune épreuve, le registre des tentatives de ton mot 2b sert-il aussi le compte des tentatives au coffre ?
**Enjeu.** Ton mot 2b (GO-2026-11-20-05) fixe la règle : toutes les tentatives et leur classe d'issue, sans verdict ni tri. Ici la seule issue est l'aiguillage du portier, un modèle ; ce qui est au coffre n'est jamais relu (R-607). Ce qui est servi à un agent reste ton nœud.
**Options.** (a) le registre entier : les tentatives passées avec leurs champs fermés, leur nom et leur énoncé ramené à une ligne, et celles du coffre en compte par case seulement. C'est la lettre de 2b, mais le compte dit où la question a glissé vers le concret. (b) le même registre sans les comptes du coffre : rien du coffre n'est servi, mais c'est un écart à la lettre de 2b.
**Recommandation.** (a), confiance 0,55. **Défaut.** Aucun : ce qui est servi à un agent est un nœud ; sans ton mot, la course ne part pas.

### D3 — Le véhicule de la course
**Décision.** Donnes-tu le mot d'activation de principe d'un régime de plus, « trois générations, sans étage de tests de mort, lecture du registre des tentatives », qui fait écrire en routine la version de l'orchestrateur, le lanceur et l'additif qui le portent ?
**Enjeu.** Ton mot GO-2026-11-20-05 (1a) réserve la version suivante de l'orchestrateur, le lanceur version 11 et leur additif au seul palier 1 de l'héritage, tests de mort sans rien servir ; 2b demande une version de plus pour la lecture du registre. Aucune version prévue ne porte cette course : la version 68 refuse la lecture sans étage et le moteur réel. L'allumage reste soumis au devis et à une ligne d'accord qui nomme ce régime.
**Options.** (a) oui, pour ce seul régime, écrit après la version du palier 1 et sur elle, numéros fixés par les mandats : la course peut partir dès ton accord de calcul ; cela prend de la place du modèle F. (b) attendre la lecture du palier 1 de l'héritage : une base éprouvée en réel, mais la course attend un résultat qui ne la concerne pas. (c) trois courses d'une génération par le lanceur en place, le registre porté à la main : rien à écrire, mais le code n'est plus figé (N-044) et il faut trois lignes ; je ne la recommande pas.
**Recommandation.** (a), confiance 0,7. **Défaut sous 48 heures.** Aucun pour l'allumage, qui est un nœud ; écrire le code éteint, sans dépense, reste de la routine.

### D4 — Qui lit les fiches, et le mode tenu à l'écart
**Décision.** Toutes les fiches sont-elles relues par la mère, ou une part l'est-elle par un lecteur hors de la défense ?
**Enjeu.** Ce que la mère a lu est un mode vu pour la défense, et ne peut plus fonder un mode tenu à l'écart.
**Options.** (a) tout est relu par la mère, et aucune carte de cette course ne nourrit le mode tenu à l'écart : la lettre de `GO-2026-11-19-94`, simple. (b) une part scellée d'avance est relue par un lecteur isolé : des cartes inconnues de la défense, mais un écart à cette lettre et une cloison de plus.
**Recommandation.** (a), confiance 0,65. **Défaut sous 48 heures.** (a).

### D5 — La famille de cases tenue à l'écart
**Décision.** Tient-on à l'écart, sans jamais la servir, une famille entière de cases ?
**Enjeu.** Garder un terrain que l'organisme n'a pas exploré, pour une mesure d'universalité ultérieure (N-044).
**Options.** (a) oui, vingt cases, tirées par graine et scellées : un terrain neuf gardé, pour un sixième du vivier. (b) non : tout le vivier est ouvert, mais rien ne reste inédit pour l'organisme.
**Recommandation.** (a), confiance 0,6. **Défaut sous 48 heures.** (a).

### D6 — Les juges
**Décision.** Joue-t-on les juges, pour information seulement ?
**Enjeu.** 27,81 USD au cas bas sur la course ; la lecture des témoins plantés ; l'ordre de lecture de la mère.
**Options.** (a) joués, jamais servis, jamais critère. (b) non joués : moins cher, mais les témoins plantés ne sont lus que par le portier.
**Recommandation.** (a), confiance 0,55. **Défaut.** Aucun : les juges sont une part de la dépense de D1 et se tranchent avec elle.

### D7 — Le crédit
**Décision.** Recharges-tu la clé du premier relais avant la course ?
**Enjeu.** Au dernier chiffre lu, il reste environ 162,56 USD ; le lanceur refuse le départ sous la part au pire (450, 195 ou 150 selon D1).
**Options.** (a) recharge à la part au pire de la ligne retenue. (b) pas de recharge : seule la ligne à deux espèces part.
**Recommandation.** (a), après un relevé du jour. **Défaut.** Aucun : compte et dépense.

## 6. Ce qui reste à faire avant ton accord de calcul

Contre-lecture des trois pièces par le modèle O ; scellement de la question par la mère ; puis, si D3 est (a) : mandats de la version de l'orchestrateur et du lanceur du régime de la course (après ceux du palier 1, ton mot 1a), de l'additif et de la configuration ; témoins plantés par la mère ; mesure des consignes sans appel ; devis final récrit sur cette mesure et sur le relevé des crédits.

## 7. Écarts et réserves

1. Une commande `find` à parenthèses a échoué sur une erreur de syntaxe du shell ; rien n'a été exécuté.
2. **Deux commandes `find` récursives** ont cherché des noms de devis sous `docs/notes/organisme-auto-conception-v1/`, `rapports/fille-ideation-1-v1/` et `docs/notes/organisme-auto-conception-v1/epreuves-v9/` (profondeur 2 pour la dernière). Le filtre qui écartait les chemins sous `archives-reponses-modeles/` portait sur l'affichage, non sur le parcours : si un tel dossier existe sous ces racines, la première commande a pu le traverser. Rien n'en a été affiché, lu, ni compté. Je le signale comme un écart possible à l'interdit du mandat.
3. La contre-lecture de la version 68, celle de la fiche v1, le contrôle de la fiche v7, les devis v2 et v2b et la synthèse v2b sont vérifiés par empreinte, non lus en entier.
4. L'addition des rôles de la course v9 donne 72,51 et non 72,50 : un centime par génération dans les totaux « bas » (devis, § 1).
5. Le crédit de 162,57 USD est une soustraction sur deux chiffres lus ; toute dépense postérieure sur cette clé le fausse.
6. Je n'ai pas lu le code : deux points de ce qui manque sont marqués « non vérifié » (ordre de course, § 2).
7. Les pièces ne sont ni contre-lues ni scellées.

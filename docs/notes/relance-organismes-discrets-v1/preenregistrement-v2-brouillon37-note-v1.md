# Note du rédacteur — brouillon 37 du texte neuf du bras A des organismes discrets — v1

- **Rédacteur** : Claude Fable 5.2 (`claude-fable-5-2`), le même que pour les brouillons 21 à 36. Je conçois ; je ne consigne pas au registre et je ne committe pas.
- **Texte** : `prereg/T0.7-organismes-discrets-v-a-v2-brouillon37.md`, `8f3a38c06b77cbc392de4faa8bb3c177076ef0a8f08923d959c0783c55b7f7fb`, scellé. 2 318 lignes.
- **Point de départ** : le brouillon 36 (`42adbbeef82625592dfd27d5b6f71c0bca67007f29894c6de8b823e0c77f9ee8`), inchangé.
- **Heures (UTC)** : commencé le 2026-11-20T05:06:44Z ; texte scellé à 05:11:13Z.
- **Méthode** : 25 remplacements exacts ; 24 sur une ancre trouvée une seule fois, un sur une chaîne trouvée cinq fois et remplacée partout (la citation du mot « a a »). Texte construit dans le bloc-notes, contrôlé, posé une fois sans écrasement, comparé octet pour octet, puis scellé, chaque étape conditionnant la suivante.
- **Pièces traitées** :
  - `docs/notes/relance-organismes-discrets-v1/verification-code-v13-bras-a-v1.md`, `0b8b51e2419e4831dd5c82dc8a8cc6caa09fcdaf4199f68b1b28013253a52d66` ;
  - `docs/notes/relance-organismes-discrets-v1/code-v13-bras-a-note-v1.md`, `e25f8a58a3487a63ad8528675398d3059742aa6cb13830453db9830588bc346d` ;
  - `docs/notes/relance-organismes-discrets-v1/verification-brouillon36-bras-a-v1.md`, `de72c464db08a78bb3b19978443ce3a3661d954dd89b1d60f1715fcc8d750571` ;
  - `docs/notes/relance-organismes-discrets-v1/mot-de-lazar-a-a-bras-a-2026-11-20-v1.md`, `ae279572bd089141be5737096e6a357685a6e0fabee259e88c56d4f61068a7fd`.
- **Aucune fiche n'est ajoutée** : aucun point ne fixe l'issue d'une hypothèse.

## 1. Points traités

| point demandé | ce que le texte écrit | où |
|---|---|---|
| 1. Modules et empreintes | trois modules en version 13 (analyse, verdicts, garde statique), six en version 12, programme du constat en version 5, chacun avec son empreinte entière. La case reste marquée pour le seul commit | 13.1, case « commit du code » ; en-tête ; 13.2 |
| 1, suite. Le module d'analyse employé | la configuration ne l'épingle pas ; le manifeste de course consigne son empreinte, et sa contre-lecture la confronte à 13.1. Ligne neuve de la table des gardes de procédure | 8.7 ; 13.2 |
| 2. Sortie refaite incohérente | un constat scellé, aucune issue, compté au rapport ; aucun plafond ; un compte non nul est une réserve du rapport | 6.9 |
| 2. Ordre des gardes | écrit tel que le code le joue : constat de lancement, rangement, ligne de GO, provenance, sortie d'origine, confrontation, contrôles de lancement, acte. Un constat d'incohérence peut se sceller sous un contrôle malsain, sans danger | 6.9 |
| 2. Confrontation et révocation | la confrontation n'est pas une lecture de la discrétion au sens de la règle « si une révocation est entrée, la lecture ne part pas » | 6.9 |
| 3. Brouillon 36, M-1 | l'enchaînement committe et pousse lui-même le dossier de course, dans la même exécution, avant de rendre quoi que ce soit ; si le poussage échoue, il s'arrête sans rien rendre. La limite qui reste est écrite | 8.7 ; 13.2 |
| 3. Brouillon 36, M-2 | le mot « a a » est cité partout par sa pièce scellée ; sa ligne au registre reste à inscrire, et la case « nœuds » le dit | cinq endroits ; 13.1 |
| 3. Brouillon 36, M-3 | le dossier de l'essai de mesure est à verser sur la branche principale avant toute dépense : ligne neuve de 13.2. La liste complétée est en partie 3 de cette note | 13.2 |

**En plus**, tiré de la même vérification : un même arrêt n'ouvre jamais deux reprises (une ligne restée inutilisée devient sans objet dès qu'un acte reprend l'arrêt qu'elle cite).

**Les empreintes inscrites**, recalculées par programme sur les fichiers, sans en ouvrir aucun :

| module | version | empreinte |
|---|---|---|
| `src/controle_ia/organismes_discrets/analyse_bras_a_v13.py` | 13 | `a7ebf29f653d417a4f211f9809576a0e70b91ae7840759607c6f3cb7f84946cf` |
| `src/controle_ia/organismes_discrets/verdicts_bras_a_v13.py` | 13 | `ae6562893d9d709ce386538d8fbe2d1d1600f7e93ae9bcfbed33841aee2e8920` |
| `src/controle_ia/organismes_discrets/cloisonnement_bras_a_v13.py` | 13 | `fa915de2a81b27751860479d2cfe6472dabb004d4790dafd186210aacd0604d6` |
| `src/controle_ia/organismes_discrets/arrets_bras_a_v12.py` | 12 | `cc632df30501129003041ac74baa5b54646ce5b82d66a88473a3e3c99a18425d` |
| `src/controle_ia/organismes_discrets/configuration_bras_a_v12.py` | 12 | `8373851eef8723000871551a338a495d423f58bb345361cf5f19bbe8b768cca8` |
| `src/controle_ia/organismes_discrets/depots_bras_a_v12.py` | 12 | `db0aa22f0a7ef6d17a97ff5200603afabb543233a768582248224d1843519ffc` |
| `src/controle_ia/organismes_discrets/graines_bras_a_v12.py` | 12 | `381878cd7ef7e23c6edb9fb4cf826fd8a1eb652b5497da8a39e99b2bd5146a8b` |
| `src/controle_ia/organismes_discrets/mesures_bras_a_v12.py` | 12 | `7a1e6aab5e3e42169584daf91660cb42ad00444fae9536b078d3db8b5064601d` |
| `src/controle_ia/organismes_discrets/permutation_etiquettes_bras_a_v12.py` | 12 | `20b78a8a3ecd7b19ba3144ffc2bcb4dc097640ff079f63495d8fdbfabd0c5b58` |
| `scripts/constat_de_lancement_discretion_bras_a_v5.py` | 5 | `fd5fddcd893e2cee91765ced911948009eb09ebd3b2382bc585fb7e4700ce290` |

Elles s'accordent avec les abrégés que donnent la vérification du code de la version 13 et la note de ce code.

## 2. Contrôles par programme

| contrôle | résultat |
|---|---|
| sections 12, 7.1 à 7.8 et 10 | **identiques** au brouillon 36 |
| hypothèse au seuil ; 6.3 à 6.8 ; 6.10 à 6.12 ; 8.1 à 8.6 ; sections 9 et 11 | identiques |
| titres | 54, identiques hors le titre de niveau 1 |
| consignes figées (3.2 et 3.3) | égales à celles du brouillon 20 ; `98a9bd34d280fc7d9db07a733bc78557ff350538a3ace7a2926999ecf14c9248`, `ecf590eae0c06d413d173f7f03c5575e52d6034613e0a1a30d681149435a1816` |
| citations entre guillemets du brouillon 36 | 1 353, aucune absente |
| citations du brouillon 20 | 935 ; les deux mêmes absentes que depuis le brouillon 32 |
| marque des cases | 6 lignes, toutes en 13.1, les mêmes cases ; aucune en 8.7 |
| table d'en-tête | 201 empreintes recalculées, toutes égales ; 14 lignes cloisonnées sautées, **aucune empreinte prise sur elles** |
| validateur `problemes()` | les deux problèmes attendus |
| mot « a a » | plus aucune citation par le journal seul |

**Registre relu** : registre des GO de la branche principale distante, au commit `6fd14f3ba`, lignes 542 à 545 (GO-2026-11-20-11 à -14). Aucune ne touche le bras A ni ne nomme GO-2026-11-19-97. Les mots « go recos » et « a a » n'ont toujours pas leur ligne.

## 3. Ce qui sépare encore le texte du scellement

Liste définitive, par qui doit agir. Elle remplace celle de la note du brouillon 36.

### Ce qui attend Lazar

1. **Un mot** : la lecture du juge d'une autre lignée, sur un sous-échantillon de 2 560 actions ou sur les 6 400. Il attend le chiffrage de la session principale (case « lecture du juge d'une autre lignée »).
2. **Une information, sans décision** : quand le développeur habilité aura répondu sur ce qui déclenche l'intervalle impossible, Lazar en est informé avant que la rédaction non retenue du point 19 soit retirée.
3. **Après le scellement** : ses lignes de GO de dépense, sur devis (13.2). Aucune n'est demandée avant.

### Ce qui attend la session principale

1. **Au registre de la branche principale**
   - la ligne du mot « go recos » du 19 novembre vers 22:00Z, et son identifiant ;
   - la ligne du mot « a a » du 20 novembre, et son identifiant ;
   - ces deux lignes ne nomment pas GO-2026-11-19-97, et celle de « go recos » ne recopie pas ce que décident les réponses du développeur aux points 19 et 20 ;
   - le type « inscription » des lignes de configuration, confirmé et déclaré à l'en-tête du registre ;
   - les formes d'inscription et de révocation, et les consignes de tenue : empreintes entières en minuscules ; une révocation seulement pour une configuration jamais ouverte.
2. **Par le développeur habilité, sur la pièce des demandes**
   - sa réponse sur l'intervalle impossible (point 19) et sur le moniteur appris non ajustable (point 20) ; si le point 20 va à sa rédaction (c), le module est corrigé et contre-lu avant la course ;
   - le champ de `piece_source` qui porte l'empreinte du module : **bloquant** ;
   - la version du module qui respecte la table des formes et permute par échange dans chaque paire : chemin, empreinte entière, commit, essais ;
   - l'épreuve par retrait et sa notice ; l'épreuve de forme, avec un seul nombre par dose ;
   - les valeurs de `motif` et de `calculable`, les chaînes de `reglages`, la forme de `lectures`, la pleine précision, les valeurs du fichier des scores par unité, le nom de la sortie de la lecture commune, les chemins à élaguer ;
   - le lanceur de l'étape de discrétion, écrit et contre-lu : sa configuration inscrit l'empreinte et le commit de l'état figé du registre où se lit la ligne de l'écart à R9, et il donne à la porte le registre courant.
3. **Par le lecteur habilité**
   - la confirmation sur le code des deux réponses du développeur ;
   - le renvoi de la base : rapport scellé, ou « non vérifié : discrétion non lue » ;
   - les quatorze empreintes héritées de la table d'en-tête ;
   - ses attestations qu'aucun calcul de moniteur ne change.
4. **Le chiffrage** de la lecture du juge d'une autre lignée, pour le mot de Lazar.

### Ce qui attend la session de relance

1. **Le commit du code arrêté**, à inscrire à la case « commit du code » : c'est la seule chose qui manque à cette case.
2. **Les pièces des demandes mises à jour**, puis leur relecture de cloisonnement avant toute sortie. Elles sont en version 8, en retard de quatre brouillons. À y porter : nom du programme du constat en version 5 ; quatrième cellule ; gras et type des lignes d'accord ; pièces que le lanceur donne à la porte de l'écart à R9 ; type « inscription » ; empreintes en minuscules ; tenue du registre pour GO-2026-11-19-97 ; révocation d'une configuration jamais ouverte ; ligne du mot « a a ».
3. **Un dernier brouillon**, quand les réponses seront là : une seule rédaction pour chacun des points 19 et 20 ; la valeur « en attente » et ses suites retirées ; toutes les cases remplies.
4. **Les contre-lectures et vérifications**, à lancer par la relance, faites par d'autres :
   - la contre-lecture 10, par un agent Claude Opus 5.5 neuf, sur le texte aux cases remplies ;
   - la vérification indépendante du code et du texte ensemble (8.7), par un agent neuf d'un autre modèle que les rédacteurs.
5. **Au scellement**
   - l'entier racine, tiré une fois par `numpy.random.SeedSequence().entropy`, inscrit, la marque retirée ;
   - le contrôle par programme que le texte scellé ne diffère du texte contre-lu que par cet entier et par les inscriptions ;
   - le validateur sans aucun problème ;
   - le scellement (R1) et la ligne `SCELLEMENT-BRAS-A-V2`.

### Après le scellement, avant toute dépense (13.2)

- le dossier de l'essai de mesure des lecteurs, versé sur la branche principale ;
- les tarifs et le devis, contre-lu ; les lignes de GO ;
- les configurations scellées, dont celle de l'analyse de la discrétion ;
- les lanceurs ;
- l'épreuve de forme de bout en bout, par la session qui lancera ;
- pendant la course : le versement par l'enchaînement, le manifeste de course et sa contre-lecture.

## 4. Réserves

1. **La limite du versement reste, et le texte la dit.** Une session qui ouvrirait le fichier de l'étape (m) hors de l'enchaînement, ou qui l'interromprait entre l'écriture et le poussage, pourrait le lire puis le détruire sans rien verser. La garde tient contre le choix entre deux courses versées, non contre ce cas. Ce qui le borne : la lecture ne se lance que par l'enchaînement, et l'épreuve de bout en bout vérifie qu'il pousse avant de rendre.
2. **L'enchaînement n'est pas écrit.** Le texte lui demande de committer et de pousser avant de rendre quoi que ce soit, et de s'arrêter sans rien rendre si le poussage échoue. C'est un programme de la session qui lance, hors du code arrêté. Il devra être écrit et contre-lu avant l'épreuve de bout en bout.
3. **Le dossier de l'essai de mesure** : je l'ai mis « avant toute dépense », comme demandé, et non avant le scellement. Les empreintes de ses rapports sont déjà citées en 13.1 ; tant qu'il n'est pas sur la branche principale, le lecteur habilité ne peut pas les recalculer de son côté.
4. **L'heure du mot « a a »** : sa pièce scellée le date « entre 03:30Z et 04:00Z environ », et l'entrée du journal qui le consigne est de 04:49:51Z. Le texte ne donne plus d'heure : il cite la pièce.
5. **Je n'ai ouvert aucun module du code.** Les précisions sur l'ordre des gardes et sur la confrontation sont reprises de la vérification du code, qui les a éprouvées.
6. **Je n'ai pas relu le texte en entier** : seulement les passages touchés (en-tête, 6.9 pour trois phrases, 8.7, 13.1 pour deux cases, 13.2, 14.48, « Contre-lecture »).

## 5. Fichiers ouverts

- Les quatre pièces nommées en tête, en entier.
- Les neuf modules du code de la relance et le programme du constat : leur empreinte seulement, par programme.
- Le brouillon 36, par programme et par recherche ; le brouillon 20 et le fichier des fiches du brouillon 23, par programme.
- Le registre des GO de la branche principale distante, par `git show` après un `git fetch`, seul appel réseau : ses lignes 542 à 545.
- **Non ouverts** : aucun module du code ; aucun interne de moniteur, aucun module habilité, rien sous `bases/`, `sondes/` ou `t07*/`, rien de T0.8 ; aucune fiche de l'organisme d'idéation ; aucune réponse de l'essai de mesure ; aucune clé. Aucun appel de modèle, aucun sous-agent, aucune dépense. Rien de committé ; `registres/`, `.claude/` et le journal non touchés.

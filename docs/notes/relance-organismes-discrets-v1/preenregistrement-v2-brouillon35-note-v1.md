# Note du rédacteur — brouillon 35 du texte neuf du bras A des organismes discrets — v1

- **Rédacteur** : Claude Fable 5.2 (`claude-fable-5-2`), le même que pour les brouillons 21 à 34. Je conçois ; je ne consigne pas au registre et je ne committe pas.
- **Texte** : `prereg/T0.7-organismes-discrets-v-a-v2-brouillon35.md`, `e62b4caec484f53c2afde2c7361136434eaa15ddb15b2f0e609c64edc3f757a2`, scellé. 2 238 lignes.
- **Point de départ** : le brouillon 34 (`0b6413d9d75a838f17aabf46ff714a34c5b086f939e44d6a864326a7e1b247a3`), inchangé.
- **Heures (UTC)** : commencé le 2026-11-20T00:57:56Z ; texte scellé à 01:03:37Z.
- **Méthode** : 34 remplacements exacts, chacun sur une ancre trouvée une seule fois ; texte construit dans le bloc-notes, contrôlé, posé une fois sans écrasement, comparé octet pour octet, puis scellé, chaque étape conditionnant la suivante.
- **Pièces traitées** :
  - `docs/notes/relance-organismes-discrets-v1/verification-corrections-code-v11-bras-a-v1.md`, `15b3f8528efb72d7d62df2d5ec638786f63c38e31847a56a6428e8dfdac5c6cc` ;
  - `docs/notes/relance-organismes-discrets-v1/defauts-du-texte-trouves-en-codant-v11.md`, `2ef9e8f95233ea473091f434c262bc4ee1781a719055975e7a4a6c29bd6241fe` ;
  - `docs/notes/relance-organismes-discrets-v1/verification-brouillon34-bras-a-v1.md`, `3350ab12b2bddb079179adeb718ee87fb8d0980481f3e07857209be13fe086bb`.
- **Aucune fiche n'est ajoutée** (partie 5, réserve 1).

## 1. Points traités

| point demandé | ce que le texte écrit | où |
|---|---|---|
| 1. Code, C-1 : périmètre d'une reprise après un arrêt à l'étape (n) | seule l'étape (n) se rejoue : aucune lecture de l'étape (m) sous la ligne de GO ; de la sortie refaite, le programme ne lit que ce qui la reconnaît et la clé `scores_par_unite` ; l'étape (n) se joue sur le fichier de l'étape (m) du rang d'origine. Une course n'a jamais deux fichiers de l'étape (m) | 6.9 ; 8.4 |
| 2. Relevé, A.1 | une ligne de type « révocation » qui cite l'empreinte entière d'une configuration retire son inscription ; la configuration retirée ne sert plus | conventions ; 8.4 |
| 2. A.2 | les mêmes choix pour toutes les livraisons, sauf le passage de « en attente » à une rédaction du point 20 à un rang supérieur ; l'exception disparaît au scellement | conventions |
| 2. A.3 | un constat de pièce donnée n'ouvre que la première lecture de la course | 6.9 ; 8.4 |
| 2. A.4, et code, M-1 | l'ouverture de lecture et l'acte de reprise portent l'empreinte du contrôle sous lequel le premier départ est parti, ou `null` ; un rejeu refuse tout contrôle que porte une ouverture, un acte ou une trace de rejeu | conventions ; 8.4 |
| 2. A.5 | après la phrase d'accord, un point final, seul | 13.2 ; 8.4 |
| 3. Code, M-2 | pour lever la garde du registre, une ligne de reprise cite l'empreinte entière d'un fichier d'arrêt ou d'un constat de pièce donnée | conventions ; 8.4 |
| 4. Brouillon 34, M-1 | le programme du constat refuse une configuration de rang 1 quand une autre est inscrite, ni retirée ni suivie d'une reprise | conventions ; 6.9 ; 8.4 |
| 4. Brouillon 34, M-2 | une ligne d'accord est d'un type autre que « révocation » ; le gras est ôté avant de comparer, et lui seul ; la porte de l'écart à R9 regarde aussi le registre courant, et n'ouvre pas si une ligne neuve nomme la ligne de l'écart | 13.2 ; 8.4 |
| 4. Brouillon 34, M-3 | la liste de ce qui se retire avec la valeur « en attente » est écrite, et la case « nœuds » y renvoie | conventions ; 13.1 |
| 5. Nom du programme du constat | `scripts/constat_de_lancement_discretion_bras_a_v4.py`, `8ca94b7c9109cdd315457f0d5cbd7f1d5d4ad38b48ece9010b13244da3e73fee` | en-tête ; conventions ; 13.2 |
| 6. Cellule d'objet | la quatrième de la ligne, celle que l'en-tête du registre nomme « périmètre » | 13.2 |

**En plus**, parce qu'ils tiennent aux mêmes passages : les points B.3, B.6, B.7, B.10 et B.12 du relevé. Les points B.8, B.9 et B.11 nomment des champs du résultat et du rapport que le texte ne nomme pas : rien au texte.

**Changements de forme de fichiers scellés** :
- l'ouverture de lecture passe de quatre à cinq champs (`sha256_du_controle_de_lancement`) ;
- l'acte de reprise passe de six à sept champs (le même).

## 2. Registre relu

Registre des GO de la branche principale distante, au commit `f9624953e`, lignes 526 à 534.
- **La ligne de l'écart à R9 est inscrite** : GO-2026-11-19-97, ligne 530, de type « décision ». Sa quatrième cellule est, à la lettre, « écart à R9 accordé pour la table des identifiants opaques ». Sa référence cite un mot de Lazar dans la session principale, vers 23:46Z.
- Elle ne recopie rien de ce que décident les réponses du développeur habilité : la consigne de cloisonnement tient.
- Le mot « go recos » du 19 novembre vers 22:00Z n'a toujours pas sa ligne. La case « nœuds » garde sa marque pour cet identifiant.
- L'en-tête du registre nomme ses huit cellules ; la quatrième s'appelle « périmètre ».

## 3. Contrôles par programme

| contrôle | résultat |
|---|---|
| sections 12, 7.1 à 7.8 et 10 | **identiques** au brouillon 34 |
| hypothèse au seuil ; 6.3 à 6.8 ; 6.10 à 6.12 ; 8.1 à 8.3 ; 8.6 ; sections 9 et 11 | identiques |
| titres | 53, identiques hors le titre de niveau 1 |
| consignes figées (3.2 et 3.3) | égales à celles du brouillon 20 ; `98a9bd34d280fc7d9db07a733bc78557ff350538a3ace7a2926999ecf14c9248`, `ecf590eae0c06d413d173f7f03c5575e52d6034613e0a1a30d681149435a1816` |
| citations entre guillemets du brouillon 34 | 1 287, aucune absente |
| citations du brouillon 20 | 935 ; les deux mêmes absentes que depuis le brouillon 32 |
| marque des cases | 6 lignes, toutes en 13.1, les mêmes cases |
| table d'en-tête | 180 empreintes recalculées, toutes égales ; 14 lignes cloisonnées sautées, **aucune empreinte prise sur elles** |
| validateur `problemes()` | les deux problèmes attendus |
| restes cherchés dans le texte actif | plus aucune version 2 ni 3 du programme du constat ; plus de « ponctuation finale » ; plus de cellule d'objet « à confirmer » |

## 4. Ce que le code de la version 12 doit porter

1. **Reprise après un arrêt à l'étape (n)** :
   - quand le fichier d'arrêt que cite la ligne de GO est de l'étape (n), refuser toute lecture de l'étape (m) sous cette ligne : aucune lecture rangée dans un cas, aucun état, aucun fichier ni constat de l'étape (m) ;
   - de la sortie refaite, ne lire que le compagnon, la provenance et la clé `scores_par_unite` ;
   - jouer l'étape (n) sur le fichier de l'étape (m) du rang d'origine, la sortie d'origine et le fichier des scores par unité refait ;
   - écrire le fichier des grandeurs dans le dossier de la livraison refaite, avec l'empreinte du fichier de l'étape (m) d'origine.
2. **Un seul fichier de l'étape (m) par course** : refuser d'en écrire un second dès qu'un est scellé dans un dossier de livraison de la course.
3. **Contrôle du premier départ** : un champ de plus, `sha256_du_controle_de_lancement` (empreinte ou `null`), à l'ouverture de lecture et à l'acte de reprise. Un rejeu refuse tout contrôle que porte une ouverture, un acte ou une trace de rejeu.
4. **Programme du constat, version de plus** :
   - une ligne de type « révocation » qui cite l'empreinte entière d'une autre configuration retire son inscription : la garde ne la compte plus ;
   - une inscription n'est « suivie d'une reprise » que si la ligne de reprise cite l'empreinte entière d'un fichier d'arrêt ou d'un constat de pièce donnée.
5. **Constat de pièce donnée** : il n'ouvre que la première lecture de la course. C'est déjà codé ; l'essai le fixe.
6. **Phrases d'accord** : quatrième cellule, gras ôté, point final seul, type autre que « révocation ». C'est déjà codé.
7. **Porte de l'écart à R9** : elle reçoit le registre courant. C'est déjà codé.
8. **Mêmes choix** : l'exception « en attente » vers une rédaction du point 20 est déjà codée.
9. **Essais (R5)**, cas sain et artefact, pour les points 1 à 4. Les lignes de 8.4 qui les énumèrent : « périmètre d'une reprise après un arrêt à l'étape (n) », « garde du registre au constat : une autre configuration inscrite », « une seule première livraison par course ».

## 5. Réserves

1. **Le périmètre d'une reprise après un arrêt à l'étape (n) m'a paru une précision de l'option (c), sans rien d'autre.** La fiche du point 21 dit qu'un tel arrêt « laisse la table de discrétion déjà scellée telle qu'elle est ». Le brouillon 32 écrivait déjà qu'après cet arrêt, ce sont « les grandeurs de cette étape » qui se lisent sur la livraison refaite. Ce brouillon dit seulement ce que le programme ne fait pas sous cette ligne. Rien de ce que Lazar a choisi ne change.
2. **Ce que j'ai conçu au-delà des mots demandés**, à faire voir :
   - pour reconnaître le fichier des scores par unité refait, le programme lit la clé `scores_par_unite` de la sortie refaite, et elle seule. Je n'ai pas vu d'autre source pour son empreinte, la configuration étant scellée avant la réception ;
   - le fichier des grandeurs se range dans le dossier de la livraison refaite et cite le fichier de l'étape (m) d'origine ;
   - je n'ai **pas** écrit de contrôle qui confronterait les vingt lectures de la sortie refaite à celles d'origine. Il vérifierait par programme que rien n'a changé à l'étape (m). Mais c'est une cause d'arrêt de plus, à peser avant de l'écrire.
3. **La dispense « suivie d'une reprise » de la garde du registre.** Je l'ai écrite comme demandé, resserrée selon le vérificateur du code. Je n'ai pas su construire un cas légitime où une configuration de rang 1 se présente après une autre inscription suivie d'une reprise : une reprise ouvre toujours un rang supérieur à 1. La dispense ne sert peut-être à rien. Sans elle, la garde serait plus simple : une seconde configuration de rang 1 ne passerait qu'après le retrait de la première. À faire juger.
4. **La ligne GO-2026-11-19-97 répond à la phrase d'accord.** Je l'ai inscrite au texte comme ligne de l'écart à R9. Je ne l'ai pas passée par le programme : c'est une lecture à l'œil, sur la cellule.
5. **Les pièces des demandes en version 8 sont en retard de deux brouillons** : nom du programme du constat (version 4), quatrième cellule, registre figé et registre courant donnés à la porte par le lanceur, gras admis et lui seul, type des lignes d'accord.
6. **Je n'ai pas relu le texte en entier** : seulement les passages touchés (en-tête, conventions, 6.2 pour une phrase, 6.9, lignes de 8.4, 13.1 pour la case « nœuds », 13.2, 14.46, « Contre-lecture »).

## 6. Fichiers ouverts

- Les trois pièces nommées en tête, en entier.
- `scripts/constat_de_lancement_discretion_bras_a_v4.py` : son empreinte seulement.
- Le brouillon 34, par programme ; le brouillon 20 et le fichier des fiches du brouillon 23, par programme.
- Le registre des GO de la branche principale distante, par `git show` après un `git fetch`, seul appel réseau : son en-tête, ses lignes 526 à 534.
- **Non ouverts** : aucun module du code ; aucun interne de moniteur, aucun module habilité, rien sous `bases/`, `sondes/` ou `t07*/`, rien de T0.8 ; aucune fiche de l'organisme d'idéation ; aucune réponse de l'essai de mesure ; aucune clé. Aucun appel de modèle, aucun sous-agent, aucune dépense. Rien de committé ; `registres/` et `.claude/` non touchés.

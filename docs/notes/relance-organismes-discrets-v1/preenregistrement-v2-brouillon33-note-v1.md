# Note du rédacteur — brouillon 33 du texte neuf du bras A des organismes discrets — v1

- **Rédacteur** : Claude Fable 5.2 (`claude-fable-5-2`), le même que pour les brouillons 21 à 32. Je conçois ; je ne consigne pas au registre et je ne committe pas.
- **Texte** : `prereg/T0.7-organismes-discrets-v-a-v2-brouillon33.md`, `dc3bc0236e9103454c988fa24997c698306ef78a2328587430bed553a5020c4a`, scellé. 2 182 lignes.
- **Point de départ** : le brouillon 32 (`a053eeb8754e53c485ffaf9b3097b823a548b78a3a386cf6243ea2641653a196`), inchangé.
- **Heures (UTC)** : commencé le 2026-11-19T22:34:06Z ; texte scellé à 22:39:55Z.
- **Méthode** : 50 remplacements exacts, chacun sur une ancre trouvée une seule fois ; texte construit dans le bloc-notes, contrôlé, posé une fois sans écrasement, comparé octet pour octet, puis scellé, chaque étape conditionnant la suivante.
- **Objet** : la vérification du brouillon 32 (`verification-brouillon32-bras-a-v1.md`, `0d7b0dff6e91bff677d16b3b2927af0a8027f62a5be61cad465cca260e04cc38`) et la vérification de cloisonnement des demandes en version 7 (`verification-cloisonnement-demandes-v7-bras-a-v1.md`, `57f7276d7e2b53c697e5a83034a7fc087976bff44c3dfe0b0bc0b1c9f8655f4d`). **Aucune fiche n'est ajoutée.**
- **Pièces écrites dans le même tour** :
  - `docs/notes/relance-organismes-discrets-v1/demandes-au-developpeur-habilite-bras-a-v8.md`, `ba81227fcea1b6419fad012f83711e61a54c7c01dce6a34d3319266d4aaaf579` ;
  - `docs/notes/relance-organismes-discrets-v1/demandes-au-lecteur-habilite-et-a-lazar-bras-a-v8.md`, `83c0822bd45740b7628bd9265aad1dd23806454644c38e129721c976f8e64f12`. Elle cite le brouillon 33 par son empreinte entière ; le brouillon ne la cite que par son chemin, pour ne pas faire de boucle.

## 1. Points traités

| point | traitement | où |
|---|---|---|
| vérification du brouillon 32, C-1 | corrigé par les voies (i) et (ii) du vérificateur (partie 2) | conventions ; 6.9 ; 8.4 ; 13.1 |
| M-1, clause du point 19 | Lazar est informé de la réponse du développeur habilité avant le retrait de la rédaction non retenue | 6.9 ; marque du point 19 ; case « nœuds » |
| M-2, rédaction (b) du point 20 | retirée de 6.9 et de la ligne de 8.4. Avec elle : le nom de règle d'arrêt « moniteur appris non ajustable », et « les deux cas tenus pour une anomalie », qui n'en font plus qu'un | 6.9 ; 8.4 ; marque du point 20 |
| M-3, pièces des demandes | version 8 ; les noms sont mis à jour dans l'en-tête et à la case du module | en-tête ; 13.1 |
| consigne de cloisonnement | jusqu'à sa dernière livraison, rien de ce que décident ses deux réponses n'est dit au développeur ; la ligne de GO du mot de Lazar ne le recopie pas et renvoie au mot consigné ; le lecteur habilité confirme les deux réponses sur le code | 13.1, cases « nœuds » et du module |

**Sections à modification bornée**, vérifiées par programme contre le brouillon 32 :
- **section 12** : 2 lignes changées sur 172. Ce sont deux marques posées au brouillon 32, en tête des points 19 et 20. Le corps des fiches est intact : les fiches 9 à 12 envoyées à Lazar s'y retrouvent mot pour mot.
- **7.1 à 7.8** : identiques.
- **section 10** : identique.
- Identiques aussi : l'hypothèse au seuil, 6.3 à 6.8, 6.10 à 6.12, 8.1 à 8.3, 8.6, les sections 9 et 11.

## 2. Ce que dit la correction de C-1

- **La clé de provenance est obligatoire.** `cle_du_module_dans_piece_source` est un texte non vide dans toute configuration ; une configuration où elle manque ou vaut `null` est refusée. Le point (18) de la case du module devient bloquant. La branche « clé `null`, `piece_source` non lu » disparaît du texte.
- **Tout remplacement de la sortie de la lecture commune passe par la règle d'octroi.** Seule une erreur de rangement se corrige sans elle.
- **Erreur de rangement** : la sortie donnée sous un autre nom ou sans son compagnon. Ces défauts jouent avant la garde de provenance. On redonne la même pièce, octet pour octet ; la session qui lance consigne son empreinte.
- **Constat de provenance**, fichier neuf : `provenance-non-etablie-bras-a-<seize signes>.json`, scellé, dans le dossier des arrêts, à quatre champs (`evenement`, `constat`, `sha256_de_la_piece`, `sha256_de_la_configuration`). Le programme l'écrit quand la garde de provenance l'arrête sur une pièce au bon nom et au compagnon juste. Il fixe quelle pièce a été donnée. Ce n'est pas un fichier d'arrêt : il ne dit aucun arrêt de la lecture et n'emporte aucune issue.
- **Première livraison** : après ce constat, plus aucune sortie d'une autre empreinte n'est lue sous sa configuration. La pièce qui remplace est une livraison refaite : configuration neuve, ligne de GO selon la règle d'octroi, acte de reprise. La ligne cite le constat de provenance à la place du fichier d'arrêt.
- **Livraison refaite** : la ligne de GO n'est pas dépensée, et la pièce qui remplace se lit sous elle si elle porte l'empreinte du module que la ligne cite. Le vérificateur tenait ce cas pour déjà borné.
- **Aucune issue n'est dite** : tant que rien ne remplace la pièce par cette voie, la discrétion n'est pas lue, et ce que cela vaut reste un nœud de Lazar, comme au brouillon 32.

## 3. Contrôles par programme

| contrôle | résultat |
|---|---|
| titres | 53, identiques hors le titre de niveau 1 |
| consignes figées (3.2 et 3.3) | égales à celles du brouillon 20 ; `98a9bd34d280fc7d9db07a733bc78557ff350538a3ace7a2926999ecf14c9248`, `ecf590eae0c06d413d173f7f03c5575e52d6034613e0a1a30d681149435a1816` |
| citations entre guillemets du brouillon 32 | 1 229 ; une absente, « mal formé », dans une phrase récrite (le mot reste, sans guillemets) |
| citations du brouillon 20 | 935 ; les deux mêmes absentes qu'au brouillon 32 |
| marque des cases | 6 lignes, toutes en 13.1, les mêmes cases qu'au brouillon 32 |
| table d'en-tête | 168 empreintes recalculées, toutes égales ; 14 lignes cloisonnées sautées, **aucune empreinte prise sur elles** |
| points de la section 12 | 1 à 21, dans l'ordre |
| validateur `problemes()` | les deux problèmes attendus |
| restes cherchés dans le texte actif | aucune rédaction (b) du point 20 ; aucune clé de provenance `null` admise ; aucun nom de pièce de demandes en version 6 ou 7 hors de l'en-tête |

## 4. Ce qui sépare encore le texte du scellement

La liste de la note du brouillon 32 (partie 5) vaut toujours, avec ces changements.
1. **Registre** : la ligne de GO du mot de Lazar, qui ne recopie pas la suite des points 19 et 20 avant la dernière livraison du développeur.
2. **Développeur habilité** : ses réponses aux demandes 6 et 7, **confirmées sur le code par le lecteur habilité** ; pour la demande 7, **Lazar informé avant le retrait** d'une rédaction du point 19. Sa réponse à la demande 13 (`piece_source`) est maintenant **bloquante**.
3. **Lazar** : la lecture du juge d'une autre lignée, après son chiffrage. Inchangé.
4. **Session principale** : les pièces de la case du module, le renvoi de la base, les formes du registre. Inchangé, plus la demande 33 de la pièce du lecteur.
5. **Session de relance** : la relecture de cloisonnement des demandes en version 8 avant leur sortie ; le code en version 10 ; un dernier brouillon à une seule rédaction pour chacun des points 19 et 20.
6. **Contre-lecture 10, vérification habilitée, entier racine, scellement** : inchangés.

## 5. Ce que le code de la version 10 doit porter

En plus de la partie 6 de la note du brouillon 32, qui vaut toujours sauf son point 4, remplacé par le point 1 ci-dessous.
1. **Configuration** : `cle_du_module_dans_piece_source` obligatoire, texte non vide. Une valeur `null` ou une clé absente arrête le programme sans lecture. La branche « clé `null` » est retirée.
2. **Constat de provenance** : quand la garde de provenance arrête le programme sur une pièce au nom attendu et au compagnon juste, il écrit et scelle `provenance-non-etablie-bras-a-<seize signes>.json` dans le dossier des arrêts, aux quatre champs, par l'écriture sans reste. Le champ `constat` est pris dans la liste fermée de cinq natures. Si le fichier existe déjà pour cette pièce, rien n'est réécrit.
3. **Première livraison, après un constat de provenance** : une sortie d'une autre empreinte n'est pas lue sous cette configuration (garde ordinaire).
4. **Livraison refaite, après un constat de provenance** : une pièce d'une autre empreinte se lit sous la même ligne si sa provenance passe ; chaque pièce arrêtée laisse son constat.
5. **Ligne de GO d'une reprise** : elle peut citer un constat de provenance à la place d'un fichier d'arrêt. L'acte de reprise porte alors, dans `sha256_de_la_livraison_refusee`, l'empreinte de la pièce arrêtée.
6. **Rapport** : il compte les constats de provenance avec les fichiers d'arrêt.
7. **Moniteur appris non ajustable** : deux valeurs du choix restent, (a) et (c). La valeur « anomalie » est refusée dans une configuration, et le nom de règle d'arrêt correspondant disparaît de ce que rend le programme qui refuse.
8. **Essais (R5)**, cas sain et artefact, pour : la configuration sans clé ; le constat de provenance (écrit ; jamais avec un champ de la pièce) ; la sortie d'une autre empreinte après un constat, sous une première livraison (refusée) et sous une livraison refaite (lue) ; la ligne qui cite un constat ; la sortie redonnée octet pour octet après un défaut de nom.

## 6. Réserves

1. **La correction de C-1 dit plus que la phrase du vérificateur.** Trois choix sont les miens, à faire voir :
   - un fichier neuf, le constat de provenance. La garde reste sans arrêt de la lecture et sans issue, mais elle laisse maintenant une trace scellée ;
   - une lecture stricte de l'erreur de rangement : la même pièce, octet pour octet, donc les seuls défauts de nom et de compagnon. Une pièce étrangère donnée par erreur sous le bon nom et avec un compagnon juste coûte une ligne de GO ;
   - quand le module ne change pas, les conditions (3) et (4) de la règle d'octroi se lisent « même module, même empreinte ».
2. **Aucune issue n'est fixée par cette correction** : le cas où rien ne remplace la pièce reste un nœud de Lazar. Si le vérificateur y voit une règle de jugement, c'est une fiche.
3. **Le texte lui-même dit la suite des réponses 6 et 7.** Le développeur ne l'ouvre pas avant sa dernière livraison. La consigne sur le registre dépend de la session principale ; si la ligne de GO est déjà inscrite et recopie cette suite, la demande 27 demande de le dire.
4. **Le registre des GO de la branche principale n'a pas été relu** pour ce brouillon.
5. **Le nom du programme du constat** reste celui de la version 2, avec la phrase sur la version qui fait foi.
6. **Je n'ai pas relu le texte en entier** : seulement les passages touchés (en-tête, conventions, 6.9, lignes de 8.4, marques des points 19 et 20, 13.1, 14.44, « Contre-lecture »).

## 7. Fichiers ouverts

- Les deux vérifications nommées en tête, en entier.
- Mes pièces des demandes en versions 6 et 7, en entier.
- Le brouillon 32, par passages et par programme ; le brouillon 20 et le fichier des fiches du brouillon 23, par programme.
- `src/controle_ia/prereg.py`, par son appel.
- **Non ouverts** : aucun interne de moniteur, aucun module habilité, rien sous `bases/`, `sondes/` ou `t07*/`, rien de T0.8 ; aucun module du code de l'analyse ; aucune fiche de l'organisme d'idéation ; aucune réponse de l'essai de mesure ; aucune clé. Aucun appel réseau, aucun appel de modèle, aucun sous-agent, aucune dépense. Rien de committé ; `registres/` et `.claude/` non touchés.

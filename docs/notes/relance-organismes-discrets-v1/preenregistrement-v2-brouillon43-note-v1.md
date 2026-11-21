# Note du rédacteur — brouillon 43 du texte neuf du bras A des organismes discrets — v1

- **Rédacteur** : Claude Fable 5.2 (`claude-fable-5-2`), le même rôle que pour les brouillons 21 à 42. Je conçois ; je ne consigne pas au registre et je ne committe pas.
- **Texte** : `prereg/T0.7-organismes-discrets-v-a-v2-brouillon43.md`, `4f91b535ad91581510615c97039a4cae0a96f4d788088b2aff666d4c3d3f97b3`, scellé comme brouillon. 2 493 lignes.
- **Point de départ** : le brouillon 42 (`c5dbd28eca7b2a244a494400ae0180bcace68b76d3861d7e35822decd68ef0de`), inchangé ; sa note (`67f554f9eddc27bab7855314f516c2647f17fb49e800299e1f14a26252b85a1e`). Empreintes vérifiées avant d'écrire.
- **Heures (UTC, relevées par `date -u`)** : premier relevé 2026-11-21T11:12:16Z ; texte scellé à 11:14:15Z ; note écrite ensuite.
- **Méthode** : celle du brouillon 42. 19 remplacements exacts, chacun sur une ancre trouvée une seule fois. Texte construit dans le bloc-notes, contrôlé, posé une fois sans écrasement, comparé octet pour octet, puis scellé.
- **Pièces traitées** :
  - la vérification du brouillon 42, `docs/notes/relance-organismes-discrets-v1/verification-brouillon42-bras-a-v1.md`, `dcf742d5d1025cefec91032cc236cbc4bffdf36cacd301a9eda8c01f7340ed3b` : « engageable après corrections », deux corrections, quatre mineurs ;
  - le registre des GO, par `git show origin/main:registres/go.md`, tête locale `e77fa0d9`, sans appel réseau, 636 lignes : lignes 631 (GO-2026-11-21-32) et 632 (GO-2026-11-21-33) ;
  - le journal de la relance, lignes 273 et 274 (OD-255 et OD-256).
- **Aucune fiche n'est ajoutée.**

## 1. Points traités

| point | ce que le texte écrit | où |
|---|---|---|
| **C-1** | GO-2026-11-21-32 porte le mot « 1a 2a 3b4c 5a » ; GO-2026-11-21-33 porte le mot « b a b go ». Les deux identifiants sont inscrits. La phrase du brouillon 42 reste à la ligne des commits, comme histoire, suivie de sa correction | en-tête (statut, ligne des commits) ; 13.1, case « lecteurs et juge des ancres » |
| **C-2** | point d'accès européen de Mistral, code 200 avec un nom servi autre que `mistral-large-4-0` : nœud de Lazar, non un repli. Le signe de « ne sert pas ce modèle » est fixé au devis des essais d'admission, avant tout appel ; lui seul déclenche le repli sur le point d'accès global | 3.4, conditions d'envoi ; 3.4, vérification de la clé |
| m-1 | l'arrêt de la file du juge sur un nom servi différent est une garde, portée par le programme qui conduit les ancres à la course, éprouvée sur un cas sain et sur un artefact (R5). 8.4, gelée, n'est pas touchée | 3.4 ; 13.2, case « version des modèles » |
| m-2 | « Labs » ajouté aux exceptions de Mistral à l'exclusion de l'entraînement | 3.4 |
| m-3 | « que le rédacteur n'a pas rouverte » | 3.4 |
| m-4 | la question de la note du brouillon 42 devient une information, sans décision demandée. Le texte dit la limite, et que le nœud ouvert par le mot « b a b go » la traitera | 3.4 ; cette note, partie 3 |

**Case « nœuds » de 13.1 : non touchée.** Sa marque attend la ligne des mots « go reocs » et « repere permis », non celles des deux mots de C-1.

## 2. Sections de jugement touchées

**Aucune. Aucune règle de jugement, aucun seuil, aucune issue des sections gelées, aucune prédiction ne change.**

| section | lignes changées |
|---|---|
| hypothèse, prédiction, métrique, seuil | 0 |
| 6.1 à 6.12 | 0 |
| 7.1 à 7.8 (liste d'arrêt et ligne A12 comprises) | 0 |
| 8.1 à 8.7 (8.4 comprise) | 0 |
| 9, 10, 11 | 0 |
| 12 | 0 |

Sections sans jugement qui changent :
- en-tête : 6 lignes changées (titre, statut, auteur, date, commits, note du rédacteur) et 3 lignes neuves à la table ;
- 3.4 : 4 lignes changées sur 41 (tête du paragraphe ; identifiant figé et issue du juge ; conditions d'envoi ; vérification de la clé) ;
- 13.1 : 1 case (lecteurs et juge des ancres) ;
- 13.2 : 1 case (version des modèles) ;
- 14 : 11 lignes neuves (14.55) ;
- contre-lecture : 2 lignes.

Le préambule de 13 et les règles d'admission 1 à 8 de 3.4 sont identiques au brouillon 42.

## 3. Information pour Lazar — aucune décision demandée

- Le mot « b a b go », choix 2 (a), dit : si la version servie du juge change pendant les ancres, sa file s'arrête, aucune ancre jugée n'est lue, et c'est ton nœud.
- **Limite** : si l'arrêt tombe à la seconde partie des ancres, les jugements de la première ont déjà servi, par programme, aux critères de l'étape (e), scellés avant.
- Le texte ne dit pas d'avance ce qu'ils deviennent. Le nœud que ton mot ouvre le traitera, le jour où il s'ouvre. Rien n'avance avant lui.
- Le vérificateur tient cela pour tenable. Le cas est rare : 152 appels au plus, sur un nom dit stable.

## 4. Contrôles par programme

| contrôle | résultat |
|---|---|
| titres | 54, identiques hors le titre de niveau 1 |
| lignes changées | 1, 3, 5, 6, 8, 9 ; 494 ; 510 ; 513 ; 514 ; 1438 ; 1458 ; 2476 ; 2477 (numéros du brouillon 42). Neuves : 3 après la ligne 194 ; 11 après la ligne 2464 |
| sections changées | en-tête, 3.4, 13.1, 13.2, 14, contre-lecture ; rien d'autre |
| consignes figées (3.2 et 3.3) | égales : `98a9bd34d280fc7d9db07a733bc78557ff350538a3ace7a2926999ecf14c9248`, `ecf590eae0c06d413d173f7f03c5575e52d6034613e0a1a30d681149435a1816` |
| marque des cases | 7 lignes, 8 occurrences, toutes en 13.1 : les mêmes cases qu'au brouillon 42 |
| validateur `problemes()` | les deux problèmes attendus, les mêmes qu'au brouillon 42 |
| table d'en-tête | 249 lignes à empreinte entière (246, plus 3 neuves : le brouillon 42, sa note, sa vérification). Aucune ligne existante ne change. Sous la consigne restreinte : **183 recalculées, toutes égales** (dossier de la relance, `prereg/T0.7-organismes-discrets-v-a-v2-*`, dossier sans interne, les 3 neuves comprises) ; 1 absente du disque (ligne 179), vérifiée par `git show origin/main:` (`f7090b5d…`, égale) ; 16 cloisonnées, reprises telles quelles ; 49 hors périmètre, reprises telles quelles — mais voir le débord, partie 7 |
| GO-2026-11-19-97 au registre | une seule ligne la nomme, la sienne (ligne 530) ; décompte sans affichage |

## 5. Ce qui sépare encore le texte du scellement

- **Vérification du brouillon 43** par un contre-lecteur d'un autre modèle, puis la contre-lecture 10.
- **Réglages des deux consoles, par Lazar**, et leur **constat daté**, versé et scellé avant le premier envoi.
- **Devis des deux essais d'admission**, contre-lu : tarifs (point d'accès européen à 1,1 fois selon le relevé), plafonds, sortie maximale envoyée, champs de jetons et de nom servi, **et le signe de « ne sert pas ce modèle »** (C-2). Ses lignes de calcul : une par file, une par vérification de clé, une de plus si Mistral se replie.
- **Fichier des règles** scellé ; **programme qui conduit les essais**, contre-lu ; vérifications de clé et point d'accès retenu ; les deux files ; les deux rapports ; case « lecteurs et juge des ancres » remplie. Pas de scellement tant que les deux rôles ne sont pas pourvus.
- **Programme qui conduit les ancres à la course** : il porte l'arrêt du juge, avec son cas sain et son artefact (m-1).
- **Cases de 13.1 encore marquées** (7 lignes) : nœuds ; familles ; lecteurs et juge des ancres ; entropie ; renvoi de la base ; commit du code ; module des cinq moniteurs.
- **Côté habilité** : inchangé depuis la note du brouillon 42.
- **Code arrêté en version 13 : rien à changer.**

## 6. Réserves

1. **Le préambule de la section 13 n'est pas touché.** Sa liste de ce que porte le devis ne nomme pas le signe de « ne sert pas ce modèle ». 3.4 le porte, deux fois. La tâche bornait C-2 à 3.4 et à la vérification de la clé ; je m'y suis tenu.
2. **« Seul ce signe déclenche le repli »** : c'est ma lecture de la correction. Une réponse du point d'accès européen qui n'est ni saine, ni ce signe, ni un nom servi différent, retombe sur la règle générale de la vérification de la clé (cause corrigée et vérification refaite, ou nœud). Le texte n'écrit pas de cas de plus.
3. **Cas sain et artefact de la garde du juge** : je les ai nommés (nom servi égal à chaque appel ; une réponse à un autre nom servi). La vérification demandait seulement de dire la garde éprouvée. Si c'est de trop, les deux descriptions se retirent sans autre effet.
4. **Le programme des ancres n'existe pas encore, à ma connaissance.** Le texte dit ce qu'il doit porter. Je n'ai ouvert aucun module pour le constater.
5. **m-2** : « sans effet » repose sur la vérification, qui dit Mistral Large 4 en disponibilité générale. Je ne l'ai pas recoupé ; 14.55 le dit.
6. **Section 12** : sa marque du brouillon 42 cite encore la tête `761710a7` pour GO-2026-11-20-58. C'est exact et daté ; je n'y ai pas touché. De même en 3.4 et en 13.1 pour cette ligne 589.
7. **Lignes 633 à 636 du registre** : non lues. Je les dis « d'autres chantiers » d'après la vérification.
8. **L'identifiant de session** de la ligne « Sessions » de l'en-tête : toujours pas touché (réserve 10 de la note du brouillon 42).
9. **Je n'ai pas relu le texte en entier.**

## 7. Fichiers ouverts, et débords

- En entier : la vérification du brouillon 42 ; la note du brouillon 42.
- Le brouillon 42, par passages et par programme : lignes 1 à 10, 186 à 195 (extraits), 494, 508, 510, 512 à 523, 929, 1424, 1425, 1435 (extrait), 1438, 1458, 2443 à 2467, 2476, 2477, 2479 ; recherches de chaînes dans ce seul fichier.
- Le journal de la relance : lignes 273 et 274.
- Par `git show origin/main:`, sans appel réseau, tête `e77fa0d9` : le registre des GO, lignes 631 et 632 en entier ; nombre de lignes, empreinte de la lecture (`65ba1a97…`), décompte de « GO-2026-11-19-97 » ; la recherche de la session principale (ligne 179 de la table), pour son empreinte seulement.
- Le relevé documentaire des conditions d'envoi, lignes 5 à 16 (900 premiers caractères), pour m-2.
- `controle_ia.prereg` : validateur exécuté, signature affichée. `controle_ia.scellement` : exécuté.
- Les scripts de construction et de contrôle du brouillon 42, restés au bloc-notes.

**Débord, déclaré.**
- **Empreintes prises hors du périmètre fixé.** J'ai d'abord relancé le script de contrôle du brouillon 42 tel quel. Il recalcule toutes les lignes non cloisonnées de la table. Il a donc pris l'empreinte de **49 fichiers hors du périmètre de cette tâche**, dont **une ligne sous `docs/sources/`** et **une configuration de T0.6** (`prereg/T0.6-organismes-config-7b-v1.json`) ; les autres : 20 sous `src/controle_ia/`, 7 sous `docs/decisions/`, 6 textes `prereg/T0.7-organismes-discrets-v-a-v1*`, 5 sous `runs/`, 4 sous `scripts/`, 3 sous `docs/notes/`, le gabarit, et deux brouillons d'addendum et de consigne.
- Ce que cela a fait : lecture des octets pour l'empreinte, rien d'affiché, rien d'ouvert autrement. Toutes égales à la table. Je n'en tire rien dans le texte : ces 49 lignes sont reprises telles quelles.
- **Aucune ligne cloisonnée n'a été touchée** : le script saute les 16, par le motif du brouillon 42.
- J'ai ensuite refait le contrôle sous la consigne restreinte ; c'est lui que la partie 4 rapporte.

**Incident sans effet** : une commande d'affichage est restée bloquée ; je l'ai arrêtée par ses identifiants de processus (R10). Elle ne lisait que le brouillon 42.

**Aucun autre débord.** Aucun franchissement du cloisonnement : rien sous `bases/`, `sondes/`, `t07*/`, rien de T0.8, aucun interne de moniteur, aucun module habilité, aucun envoi ni réponse de l'essai de mesure. La ligne de la pièce sans interne (ligne 189) est reprise telle quelle, sans relecture. Aucune clé, aucun appel de modèle ni appel réseau, aucun sous-agent, aucune dépense. Rien de committé ni poussé ; `registres/`, `.claude/` et le journal non touchés.

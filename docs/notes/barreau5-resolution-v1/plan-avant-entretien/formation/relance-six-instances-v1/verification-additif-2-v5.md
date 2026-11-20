# Vérification de l'additif 2 v5 (recréation des relances tombées avant leur marche)

Pièces :
- additif v5, sha256 a3cacd68f98a76b350ea6db45f964fb32b50daf59e9017adf6c29eee0afc1bef (vérifiée) ;
- différentiel v4 → v5, sha256 6b09c8d216b3ab5cb6602bebe565ad29e8bf2b9b1b1fed74509e46aee1545685 (vérifiée) ;
- v4 de départ : 307255c2….

Le différentiel, refait par `diff -u`, est fidèle. J'ai lu l'amorce au commit de course 4bdf0d22e4246b4fe431bd8754e26fea4ccd037f, et ce seul fichier.

**Verdict : scellable après ces couples.** Il y a un couple important, la réserve, qui vient de ma propre phrase du couple 4 de la v4. Les deux autres sont mineurs.

## Mes sept couples de la v4

| couple | levé ? | constat |
|---|---|---|
| 1. 198,34 dollars n'est pas une borne haute | levé | « Estimation au relevé de 15:18Z … Ce n'est pas une borne haute » ; le stockage des premières tentatives non détruites est ajouté à la somme ; « la quatrième recréation est donc probablement un nœud » |
| 2. Relance muette | levé | échéance mécanique au clonage plus 3600 secondes plus 15 minutes, arrêt au titre de la garde d'instance ; inventaire du disque à la condition 2 ; « leur état n'est pas connu » ; nœud ajouté. Voir N2. |
| 3. Citation du texte et exclusion de la machine | levé | la vraie phrase du texte est citée dans la section 2 et dans la table ; « aucune autre préférence » est rendue au plan de marche, retouché à part ; la phrase de l'en-tête est retirée |
| 4. Ordre des recréations | levé dans la lettre, mais ma phrase était fausse | voir N1 |
| 5. Arrêts admis renvoyés à l'amorce | levé | numéros de ligne cités, vérifiés ci-dessous ; condition « même étape passée sur une autre machine » ajoutée |
| 6. Plancher | levé | coupes 4 et 5 et point 13 cités à la lettre, conformes aux extraits du texte |
| 7. Stockage de la tentative 1 | levé | par le terme de stockage ajouté à la réserve |

## Numéros de ligne de l'amorce, au commit 4bdf0d22…

Tous exacts. La fonction d'arrêt est `arret() { terminer "${2:-4}" "ARRET : $1"; }` (ligne 239) : les libellés « ARRET : … » sont donc littéraux.

| citation de l'additif | ligne lue | exact ? |
|---|---|---|
| « ARRET : clonage », ligne 252 | `git … clone … \|\| arret "clonage" 2` | oui |
| « ARRET : extraction partielle », ligne 277 | `sparse-checkout … \|\| arret "extraction partielle" 2` | oui |
| « ARRET : installation des paquets », ligne 286 | `timeout -k 10 3600 … pip install … \|\| arret "installation des paquets" 2` | oui ; la borne de 3600 secondes est bien là |
| « ARRET : descente du modèle », lignes 297 à 300 | `timeout -k 10 3600 … precharger_modele … \|\| arret "descente du modèle" 2` | oui |
| « marche : début », ligne 317 | `j "marche : début (run $RUN_B5F, $DUREE s au plus)"` | oui |
| ligne 282, déjà vérifiée | `ls-remote --exit-code` puis `[ $? = 2 ]` | oui |

## Le point ouvert du rédacteur : non, ce n'est pas voulu

Ma phrase du couple 4 compte deux fois une relance non tranchée : par son reste en cours, puis par la coupure entière d'une recréation possible. Elle bloquerait la recréation de l'instance 1, la première dans l'ordre, pour protéger des recréations des instances 2, 3 et 4, qui viennent après elle. Les coupes du plan ne départagent d'ailleurs pas les instances 1 à 4 : les familles tenues à l'écart ont chacune la même coupure, et seules l'instance 5 et la troisième famille d'apprentissage ont un rang de coupe. Le pire cas d'une relance non tranchée est déjà couvert par son reste jusqu'à sa coupure. Si elle tombe, sa recréation est comptée au relevé qui la précède.

## Couples neufs

**N1. Important : remplacer ma phrase sur la relance non tranchée.**
- Constat. C'est ce qui précède : la phrase compte deux fois une relance non tranchée et peut bloquer à tort la recréation de l'instance 1, jusqu'à ce que les relances 2, 3 et 4 soient tranchées. Il faut corriger deux endroits.
- Correction, en section 2. Remplacer la phrase « Une relance dont l'état n'est pas encore tranché ne retient pas les suivantes, mais sa coupure entière est comptée dans la réserve tant qu'elle peut encore être recréée. » par :
  > « Une relance dont l'état n'est pas encore tranché ne retient pas les autres ; tant qu'elle tourne, elle est comptée parmi les marches en cours, par ce qui lui reste jusqu'à sa coupure, et rien d'autre ; sa recréation n'est comptée qu'une fois la relance tombée, au relevé qui précède cette recréation. »
- Correction, en section 5. Remplacer « stockage des premières tentatives et coupure des relances non tranchées compris » par « stockage des premières tentatives et reste en cours des relances non tranchées compris ».
- Gravité : important.

**N2. Mineur : l'heure de référence et les échéances exactes.**
- Constat. Le « clonage » dont part l'échéance est, en fait, la ligne « B5F » « dépôt au commit … », que l'amorce écrit à la ligne 284, après le contrôle de la ligne 282. Les heures attestées donnent :
  - relance 2 : 16:00:03Z ;
  - relance 3 : 16:01:10Z ;
  - relance 4 : 16:00:50Z.

  « Entre 16:00Z et 16:01Z » est donc faux de dix secondes pour la relance 3.
- Correction. Écrire « au clonage (ligne « dépôt au commit … » du journal, amorce ligne 284) plus 3600 secondes plus 15 minutes ». Remplacer « cette échéance tombe entre 16:00Z et 16:01Z » par « relance 2 : 16:00:03Z ; relance 3 : 16:01:10Z ; relance 4 : 16:00:50Z ».
- Gravité : mineur.

**N3. Mineur, facultatif : le silence après une ligne neuve.**
- Constat. L'échéance ne vaut qu'une fois, depuis le clonage. Une relance qui écrit « essais du paquet » puis se tait n'est plus couverte. Les essais (ligne 291) n'ont pas de minuterie ; la descente du modèle est bornée à 3600 secondes. En outre, la ligne 278 (« commit … introuvable ») peut tenir au réseau, parce que l'extraction partielle va chercher les fichiers à la demande ; elle n'est pas dans la liste des arrêts admis. Elle tombe donc en nœud, ce qui est sans danger.
- Correction. Écrire « avant « marche : début », 3600 secondes plus 15 minutes sans aucune ligne « B5F » neuve depuis la dernière ».
- Gravité : mineur.

## Aucune autre erreur introduite

La section 3 et le nœud « l'arrêt d'une relance avant l'échéance mécanique » sont cohérents avec la condition 1. La section 4 ne change pas.

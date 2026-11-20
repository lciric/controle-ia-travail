# Erratum 1 — question de la course « nouvelles attaques », v5 scellée : la revue de sécurité externe

- Auteur : rédacteur neuf, modèle F. Écrit le 2026-11-20 ; relevé de `date -u` : 12:50:45Z, après la lecture des pièces et avant l'écriture.
- Nature : pièce de travail (classe C), décidée par la session mère en routine (12:49Z). Non contre-lue.
- Pièce corrigée : `prereg/ideation-nouvelles-attaques-v1/question-course-nouvelles-attaques-v5.md`, empreinte `eaf5db8a558547aa8f5df45008a34eebf4cb7a163e12ca400176401de6f5ce0f`, tirée de `origin/main` au commit `b09e483c405544a8bce91f42b9f3a440e40d263c` et vérifiée par empreinte.
- **La question v5 scellée reste intacte ; cet erratum se lit avec elle.** Là où ils diffèrent, sur le seul lieu ci-dessous, l'erratum prime.
- Cet erratum porte des identifiants de registre : il n'est pas à servir à un modèle.

## 1. Raison unique

La question v5 dit encore qu'une épreuve du bras d'attaque vient « après la revue de sécurité externe ». Le directeur du programme a décidé autrement, par deux accords de `registres/go.md` (sur `origin/main`, même commit, empreinte du fichier `7799734ead8e32ec838727ef7911ac858e628cc0d3c8190d32d3b380da9223df`), cités à la lettre :

- `GO-2026-11-20-46` (ligne 577), colonne de la décision : « **Course « nouvelles attaques », dix nœuds de la note de périmètre v3 (dd6fea0e…) : recommandations, sauf le point 8.** Point 1 : (b) d'abord, une question v5 qui fait nommer le mode et reste au niveau de l'idée, puis le procédé est permis pour les modes jugés inédits (lecture de la mère : « go recos puis procede permis ») ; points 2 à 7, 9 et 10 selon les recommandations ; point 8, revue de sécurité externe avant tout usage d'un mode : **non**. Avis de Fable 5.1 et de Fable 5.2 demandés par Lazar sur ces choix. » Mot consigné : « go recos puis procede permis , Revue de sécurité externe avant tout usage d’un mode non. demande a fable 5.1 et 5.2 ce qu'ils en pensent ».
- `GO-2026-11-20-50` (ligne 581), colonne de la décision : « **Course « nouvelles attaques » : six garde-fous internes en place de la revue de sécurité externe pour la mesure interne** (avis de Fable 5.1 0b50e643… et de Fable 5.2, docs/notes/ideation-nouvelles-attaques-v1/). (1) Le procédé n'est demandé qu'après le verdict d'antériorité, par une session à part, jamais dans la conversation qui a rendu l'idée ; la mère ne le lit jamais. (2) Quarantaine sur branche orpheline, règle d'ouverture écrite, liste nominative des lecteurs, chaque lecture consignée. (3) Registre servi aux générations suivantes : nom et énoncé seulement, vérifié par programme avant envoi. (4) Aucun procédé exécuté hors du banc de mesure scellé ; chaque exécution citée par un GO. (5) Un lecteur interne d'une autre lignée que les moniteurs répond par oui ou non « ce procédé sert-il à autre chose que mesurer ? » ; un oui bloque l'usage. (6) Revue externe fixée avant toute sortie hors quarantaine (papier, billet, dépôt public, partage). Complète GO-2026-11-20-46, point 8 ; à porter au préenregistrement court v7. » Mot consigné : « go garde-fous ».

## 2. Lieu corrigé

Un seul lieu : **§ 7, « Ce que la question ne tranche pas », ligne 74** (partie non servie).

Texte ancien, mot pour mot :

> Elle ne dit pas qu'une menace existe, qu'elle réussirait, ni qu'elle est nouvelle : la course rend des idées, la règle d'antériorité rend une étiquette bornée, et seule une épreuve du bras, sous ses scellements et après la revue de sécurité externe, dirait si un moniteur la voit.

Lecture juste : les mots « et après la revue de sécurité externe » se lisent « et sous les six garde-fous internes de `GO-2026-11-20-50`, qui tiennent lieu de la revue de sécurité externe pour la mesure interne ; la revue de sécurité externe reste fixée avant toute sortie hors quarantaine (papier, billet, dépôt public, partage) ». La phrase entière se lit donc :

> Elle ne dit pas qu'une menace existe, qu'elle réussirait, ni qu'elle est nouvelle : la course rend des idées, la règle d'antériorité rend une étiquette bornée, et seule une épreuve du bras, sous ses scellements et sous les six garde-fous internes de `GO-2026-11-20-50`, dirait si un moniteur la voit ; la revue de sécurité externe reste fixée avant toute sortie hors quarantaine (papier, billet, dépôt public, partage).

Le reste de la phrase ne change pas : la question ne tranche toujours ni l'existence, ni la réussite, ni la nouveauté d'une menace.

## 3. Ce que cet erratum ne touche pas

- Le § 4, la question servie, et toute la partie servie (gabarit `4cd360ba…`) : rien n'y change, pas un octet.
- Le § 3, « Garde permanente » : relu en entier (lignes 33 à 38), il ne porte aucune mention de la revue de sécurité externe ; il n'a donc aucun lieu à corriger. Ses quatre gardes restent entières, dont « niveau de l'idée, jamais du procédé » pour les fiches de cette course et « un refus d'un classifieur de sûreté n'est jamais contourné ».
- Les § 2, § 5 et § 6, l'en-tête et le § 1 : aucune mention de la revue externe (recherche de « revue », « externe » et « quarantaine » sans égard à la casse : la ligne 74 seule).
- Aucune case, aucun champ, aucun seuil, aucune règle de lecture, aucune règle d'antériorité.

## 4. Réserves

1. L'en-tête de la v5 (ligne 8) et son titre disent encore « à sceller » et « non scellée » : ce sont les mots du rédacteur d'avant le scellement ; l'empreinte lue est bien celle que la mère donne pour scellée. Hors de l'objet de cet erratum, non corrigé ici.
2. La pièce corrigée est un texte de préenregistrement scellé ; l'erratum ne fait que porter au texte deux décisions déjà prises par le directeur du programme. Si la mère juge qu'un erratum sur une pièce de cette classe demande une vérification, elle en décide.

— modèle F

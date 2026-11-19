# Vérification de cloisonnement des demandes v3 du bras A — v1

- **Pièces vérifiées.**
  - Pièce du développeur : `docs/notes/relance-organismes-discrets-v1/demandes-au-developpeur-habilite-bras-a-v3.md`, `7bfbf09081a00bf3120da5147320b38e6c59ec4a196395bf625c8c0ef4860493`.
  - Pièce du lecteur habilité et de Lazar : `docs/notes/relance-organismes-discrets-v1/demandes-au-lecteur-habilite-et-a-lazar-bras-a-v3.md`, `0cd051eb733e635e3bbe8a17086e1bec9dd6740d633f58bd8dcd86d399e6897e`.
  - Les deux compagnons sont conformes.
- **Vérification de référence** : `verification-cloisonnement-demandes-v2-bras-a-v1.md`, `5266f64e299b456b144ab1d497a713873c546a6b9433b57bc58b8c6229414bb0`, avec cinq retouches et une remarque non bloquante.
- **Relecteur** : le même agent Claude Opus 5.5, qui n'a écrit aucune des deux pièces. Classe C. Mêmes interdits : aucun interne de moniteur ouvert, ni la note du développeur citée à la demande 25.
- **Recherches de mots** : pour le point 3, j'ai cherché par `grep` des mots exacts dans les notes de la relance et dans les brouillons du texte du bras A. Ce sont des pièces de la relance, pas des internes. Je n'en ai lu que les lignes trouvées.
- **Diffusion** : cette pièce ne doit pas être transmise au développeur des moniteurs.

## Verdict : peut sortir après retouches

Les deux pièces sont propres. Les cinq retouches de la v2 sont tenues. Le contrôle par programme ne trouve dans la pièce du développeur aucune empreinte, et aucun chemin d'un fichier qu'il ne doit pas ouvrir.

**Une seule retouche reste, sur la ligne 6 de la pièce du développeur.** Sa liste de fichiers à ne pas ouvrir est trop étroite. Au moins trois notes de la relance qu'elle ne couvre pas portent la considération retirée de l'ancienne demande 25 : le journal, et les notes de décisions des brouillons 22 et 23. Les brouillons 22 à 28 du texte la portent aussi ; ils sont couverts, mais le texte scellé ne le sera pas. La retouche est d'une ligne ; elle ne demande pas de relecture nouvelle.

## 1. Les cinq retouches de la v2

| n° | retouche | tenue ? | où |
|---|---|---|---|
| 1 | Pièce du développeur, ligne 5 : retirer les renvois à la première version et à la relecture ; lister les fichiers à ne pas ouvrir | **oui pour les renvois** : la ligne 5 ne nomme plus aucune version ni relecture. **La liste est posée mais incomplète** : voir le point 3.2 | développeur, l. 5-6 |
| 2 | Demande 8 : la chaîne qui nomme un trait ou une méthode est changée dans le module | **oui** : « change-la dans le module », avec la raison (l'analyse lit ce champ dans chaque livraison) | développeur, demande 8 |
| 3 | Demande 9 (b) : une étiquette fixe dans le module pour `statistique_agregateur` | **oui** | développeur, demande 9 |
| 4 | Demande 29 : exemple fictif dans la réponse seulement, `GO-0000-00-00-00`, soixante-quatre zéros, refus par le constat et épreuve | **oui** : il est ajouté que l'exemple n'est écrit ni au registre ni dans un fichier que le constat lit | lecteur, l. 71 |
| 5 | Demande 25 : juger sur le code et non sur les conclusions de la note ; citer l'empreinte entière lue ; « ce qui en dépend » neutre | **oui, pour les trois** | lecteur, l. 48-50 |
| (remarque) | Ligne 58 du développeur : « la ligne de GO renvoie à cette lecture » | **oui** | développeur, demande 1 |

## 2. Les deux ajouts du rédacteur

**2.1 — Le cinquième motif : sa propre pièce dans une autre version.**
- *Jugement* : utile et juste.
- *Raison.* La version 2 de sa pièce portait, à sa ligne 5, le chemin et l'empreinte entière de la première version et de la relecture v1. L'exclure ferme ce chemin de retour. Le motif « d'une autre version que celle-ci » est clair.
- *Rien à retoucher.*

**2.2 — La table de correspondance réduite à deux colonnes (demande, case).**
- *Jugement* : bonne retouche, sans perte.
- *Raison.* La colonne retirée (« ce qui change depuis la v1 ») racontait la séparation elle-même : par exemple « plus de “quelles conditions” », « la part du lecteur habilité est passée dans l'autre pièce ». Elle laissait deviner ce qu'on avait voulu ne pas lui dire.
- Les deux colonnes restantes ne disent que des numéros. La ligne 12 précise qu'il n'a pas à connaître les cases autrement. Les numéros 22 à 30 sont annoncés comme absents, sans contenu.
- *Rien à retoucher.*

## 3. La pièce du développeur, relue une dernière fois comme lui

**3.1 — Contrôle par programme.**
- *Empreintes.* Aucune chaîne hexadécimale de 8 signes ou plus dans la pièce, donc aucune empreinte, entière ou abrégée.
- *Fichiers interdits, cherchés par leur nom et par les 8 premiers signes de leur empreinte, avec 0 occurrence pour chacun :*
  - la première version des demandes ;
  - les pièces du lecteur v2 et v3 ;
  - la pièce du développeur v2 ;
  - la relecture v1 ;
  - la vérification v2 ;
  - le brouillon 28 du texte.
- *Chemins et noms de fichiers.* Les seuls jetons de chemin sont :
  - les motifs à joker de la ligne 6, nécessaires pour dire quoi ne pas ouvrir ;
  - le nom du fichier livré `rangs-par-unite-moniteurs-bras-a.jsonl`, qui est de la forme ;
  - les motifs d'élagage de la demande 20.
- *Résultat :* aucun chemin exact ni aucune empreinte d'un fichier qu'il ne doit pas ouvrir.

**3.2 — La ligne 6 couvre trop peu (seule retouche).**
- *Constat.* J'ai cherché, par mots exacts, la considération retirée de l'ancienne demande 25. Je ne la recopie pas ici. On la trouve, hors des fichiers que couvrent les motifs, dans :
  - `journal-relance-organismes-discrets-v1.md` ;
  - `decisions-bras-a-brouillon22-v1.md` ;
  - `decisions-bras-a-brouillon23-v1.md`.
- On la trouve aussi dans les brouillons 22 à 28 du texte (`prereg/T0.7-organismes-discrets-v-a-v2-brouillon*`). Ceux-là sont couverts.
- Plus largement, le dossier `docs/notes/relance-organismes-discrets-v1/` compte 117 fichiers que les motifs ne couvrent pas : notes, décisions, devis, contre-lectures, journal. Beaucoup portent le plan d'analyse et les recommandations de la relance.
- Enfin, le texte scellé du bras A ne s'appellera pas `…-brouillon*` : aucun motif ne le couvrira. Or son brouillon 28 contient la même considération, dans l'avis joint à la fiche du schéma de permutation.
- *Retouche, ligne 6.* Remplacer la liste par :
  > « N'ouvre aucun fichier sous `docs/notes/relance-organismes-discrets-v1/`, hors cette pièce ; aucun fichier dont le nom commence par `prereg/T0.7-organismes-discrets-v-a-` (brouillons et texte scellé) ; aucune passation de la relance (`registres/passations/passation-relance-*`). Si tu en as ouvert un, dis-le dans ta réponse. »
- Les motifs nominaux actuels peuvent rester en plus. Le motif de dossier les couvre tous, sauf l'exception de sa propre pièce.
- *Point pour la mère, non bloquant pour la sortie.* Si le développeur doit un jour lire le texte scellé du bras A, la considération retirée de la demande 25 lui parviendra par là. La séparation de la demande 25 n'est alors qu'un délai. Dire avant la course si le développeur lit le texte scellé, et quand.

**3.3 — Peut-il en tirer une attente sur ce que ses moniteurs devraient repérer, ou sur ce qui ferait conclure « discret » ?**
- Non, au-delà de ce que la forme impose : la valeur de la famille décide de « repère », la borne haute sert à « ne repère pas ». C'est admis, il le savait par les versions 7 et 8.
- Aucune dose, aucun résultat, aucune recommandation de schéma de permutation : les deux schémas sont nommés sans préférence dans la demande 9.
- La ligne 6 nomme l'existence de relectures et de vérifications de cloisonnement, sans leur contenu. C'est sans effet.

**3.4 — Une réponse bornée peut-elle encore faire entrer un interne dans la relance ?**
- Non. Chaque demande fixe sa forme de réponse. La ligne 8 donne la sortie « ne peut pas se dire sans interne ». Les demandes 8 et 9 font corriger le module, et plus seulement la réponse. La session principale relit avant de transmettre.

## 4. Autres contrôles

- **Pièce du lecteur, ligne 4.** Elle dit justement ce qui est demandé au développeur. À aligner si la ligne 6 du développeur est élargie : « …ni les notes de la relance, ni le texte du bras A ».
- **Données personnelles et clés.** Aucun nom de personne hors de Lazar, aucun courriel, aucune clé, aucun identifiant de session dans les deux pièces.

## Retouches, liste courte

1. Pièce du développeur, ligne 6 : exclure tout le dossier `docs/notes/relance-organismes-discrets-v1/` (hors sa pièce), tout `prereg/T0.7-organismes-discrets-v-a-*`, texte scellé compris, et les passations de la relance (3.2).
2. Pièce du lecteur, ligne 4 : l'aligner sur cette liste (4).
3. Pour la mère : dire si et quand le développeur lit le texte scellé du bras A (3.2).

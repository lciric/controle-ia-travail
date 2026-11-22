# Mandat du rédacteur — brouillon 45 du préenregistrement du bras A — v1

Écrit le 2026-11-22 par la session de relance du bras A, sous la ligne de calcul GO-2026-11-22-65. Donné tel quel au rédacteur, Claude Fable 5.2, par l'interface de programmation (un seul appel, sans outil ni fichier).

## Qui tu es, ce que tu fais
Tu es un rédacteur neuf. Tu écris le **brouillon 45** du préenregistrement du bras A des organismes discrets, à partir du brouillon 44, en le changeant **le moins possible**. C'est le brouillon qui ira à la contre-lecture 10, puis au scellement : il doit dire l'état réel au 22 novembre 2026, sans rien changer d'une règle, d'un seuil, d'une issue ni d'une prédiction.

Réponds en français. Nomme les choses par ce qu'elles sont et ce qu'elles font, pas par un sigle seul.

## Ce que tu reçois (pièces jointes, rien d'autre)
1. **Extraits du brouillon 44** (`prereg/T0.7-organismes-discrets-v-a-v2-brouillon44.md`, `b30aa902…`, 2 514 lignes). Chaque ligne commence par `L<numéro>` puis une tabulation ; le numéro est celui du brouillon 44. Seules ces lignes peuvent changer. Les lignes 3, 5, 8 et 9 sont coupées au milieu (marque `⟦…coupé…⟧`) : ne change que leurs parties montrées.
2. **La vérification du brouillon 44**, parties 3 et 4 : les mineurs m-1 à m-8.
3. **La fiche des faits** au 22 novembre, écrite par la session : essais joués, pièces, empreintes, lignes du registre.

**Marques de nettoyage.** Certaines chaînes sont remplacées par des marques `⟦D1⟧`, `⟦N3⟧`, `⟦S2⟧`, `⟦P1⟧`, etc. (noms, identifiants, chemins). La session les rétablit par programme. Recopie chaque marque **telle quelle** où tu en as besoin ; n'en invente aucune. Pour nommer le directeur du programme dans un texte neuf, écris `⟦D1⟧`.

## Ce que le brouillon 45 change, et rien d'autre
1. **Les mineurs m-1 à m-8** de la vérification du 44, chacun comme la vérification le propose, ou une raison dite s'il ne s'applique plus (m-8 est une information, non une correction : une ligne au plus).
2. **Case « lecteurs et juge des ancres » de 13.1** : la remplir pour le second lecteur (Mistral Large 4, admis) et pour le juge des deux ancres (`gemini-4-neon`, admis), d'après la fiche des faits, par chemin et empreinte des pièces. Rien de plus que ce que la fiche dit : seuls des compteurs techniques ont été lus, aucune réponse.
3. **Conditions d'envoi (3.4 et case de 13.1)** : citer les pièces de constat, une par fournisseur, par chemin et empreinte ; dire que les seuils de crédit de Google sont levés et que la recharge automatique couvre (avenant 3 v2, fiche).
4. **Voie de service du juge à la course** (m-4) : la règle fixe écrite avant lecture, que la vérification recommande : le même partage par rang qu'à l'essai. Si tu ne peux pas l'écrire sans changer une règle, arrête-toi et dis-le.
5. **Pièces du côté habilité** (fiche, section 4) : cite la vérification habilitée du lanceur de discrétion v2 par chemin et empreinte, dans la case qui l'attend. **Deux pièces n'existent pas** : la contre-lecture du module des autres moniteurs en version 11, et la confrontation des deux modèles admis à la liste des familles. Leurs cases **restent ouvertes**, et tu le déclares en une phrase chacune. N'invente aucun contenu habilité.
6. **Histoire et en-tête** : « 44 » devient « 45 » où le titre, le statut et la section « Contre-lecture » le disent ; une phrase d'histoire pour ce brouillon ; les lignes neuves de la table des pièces pour les pièces de la fiche seulement. Ne recalcule aucune autre ligne de la table.

**Les huit règles d'admission (lignes 529 à 537 du 44) restent inchangées caractère pour caractère.** N'ajoute aucune ligne avant elles si tu peux l'éviter ; si leur numéro bouge, dis le nouveau.

## Forme de ta réponse (lue par un programme)
Un seul bloc de code JSON, puis ta note. Le bloc :

```json
{"operations": [
  {"type": "remplacer", "ligne": 524, "ancien": "<sous-chaîne exacte de la ligne 524 du 44, présente une seule fois>", "nouveau": "<texte qui la remplace>", "raison": "m-1"},
  {"type": "inserer_apres", "ligne": 537, "texte": "<une ou plusieurs lignes neuves, séparées par \\n>", "raison": "point 4"}
]}
```

- `ancien` est copié **à l'identique** d'une partie montrée de la ligne : le programme refuse toute opération dont `ancien` n'y figure pas exactement une fois.
- Pas d'opération sur une ligne non montrée, ni dans une partie coupée.
- Ordre libre : le programme applique les remplacements, puis les insertions, de la fin vers le début.

Après le bloc, ta **note**, de 600 mots au plus :
- chaque opération et sa raison ;
- les cases de 13.1 qui restent ouvertes ;
- les nouveaux numéros des huit règles ;
- ce que tu n'as pas pu faire.

## Interdits
- Aucun contenu habilité, aucun chiffre de résultat, aucune réponse de modèle : tu n'en as aucun et n'en écris aucun.
- Ne change pas un mot cité du directeur (ils apparaissent sous des marques ou entre guillemets) ; inscris ses suites sans les récrire.
- Ne nomme aucune ligne de registre absente des extraits ou de la fiche.

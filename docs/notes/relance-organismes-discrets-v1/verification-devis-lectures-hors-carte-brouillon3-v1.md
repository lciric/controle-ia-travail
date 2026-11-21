# Vérification du devis des lectures hors carte du bras A, brouillon 3 — v1

**Verdict : engageable.** Contre le brouillon 2, seuls changent les cinq passages de la correction que j'avais demandée, et chacun porte mon texte de remplacement à la lettre. Le reste du fichier ne bouge pas, ni l'en-tête de deux lignes ajouté par la mère. Ce que le brouillon 2 avait de juste le reste donc : volumes, attendu d'environ 255 USD, plafonds de 670 USD en huit lignes, dont 130 au premier engagement, et décisions bien posées. Trois mineurs, non bloquants.

- **Vérificateur** : le même agent (Claude Opus 5.5), le 2026-11-21. Rien n'est scellé ni committé.
- **Objet** : `docs/notes/relance-organismes-discrets-v1/devis-lectures-hors-carte-bras-a-v1-brouillon3.md`, sha256 `ae045231c1388a880b01da3677a6a739eabdace657762aa1e77d25bdc17ec50c`, égale à son compagnon. Comparé au brouillon 2 (`d5e814b4…`).
- **Interdits** : ceux du mandat du rédacteur ; aucun réseau ; rien d'ouvert d'autre que les deux brouillons.

## 1. Contrôle par programme

Le programme part du brouillon 2. Il y applique, à la lettre, les quatre remplacements de ma correction D-1, chacun sur un passage qu'il trouve une seule fois ; le remplacement de la décision 6 porte aussi la phrase ajoutée sur le versement. Il compare ensuite le résultat au corps du brouillon 3, l'en-tête de deux lignes retiré : **les deux textes sont égaux**.

| passage | état |
|---|---|
| 0, point 7 | mon texte, à la lettre |
| 4.4, dernier point | mon texte, à la lettre |
| décision 6, enjeu | mon texte, à la lettre |
| décision 6, phrase sur le versement | ajoutée, à la lettre |
| réserve 9 | précision ajoutée, à la lettre |
| reste du fichier | inchangé |

Il ne reste plus « porte à 89,67 » nulle part.

## 2. Mineurs

- **o-1 : « 145,81 » reste une fois**, à la sortie du programme (section 13, ligne 759) : « avec le pire cas des essais : 145,81 ». Le calcul est juste, mais il ne sert plus à rien. À retirer, ou à marquer comme écarté, au prochain brouillon.
- **o-2 : le titre et la ligne « État » disent encore « brouillon 2 ».** Seul l'en-tête de la mère dit « brouillon 3 ». C'est sans effet sur le fond ; à mettre au juste au prochain brouillon.
- **o-3 : mon mineur n-1 n'est pas porté**, et c'est dit. Je le maintiens comme mineur : la question 3 de la section 10 peut recevoir la réponse « 128, par la lettre de 6.11 ».

Aucun de ces trois points n'empêche d'engager le devis.

## 3. Ce que j'ai ouvert

Les brouillons 2 et 3 du devis (lecture de leurs empreintes, `diff`, programme de comparaison), et rien d'autre.

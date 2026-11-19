# Vérification de la différence entre la v1 et la v2 du plan de lecture de la tranche de l'ajustement de nos lentilles (B-β) de la lecture par lentille neuronale (« Neuron Lens », Llama 3.1 8B Instruct)

- Heure (UTC, `date -u`) : ouverture **2026-11-19 07:33:47 UTC** ; écriture de ce rapport **2026-11-19 07:35:00 UTC**.
- Vérificateur : le contre-lecteur de la v1 (sous-agent, modèle servi Fable 5.2, `claude-fable-5-2`), autre modèle que l'auteur du plan (Opus 5.5).
- Empreintes SHA-256 recalculées :

| pièce | empreinte recalculée | attendue et compagnon |
|---|---|---|
| plan v2 `docs/notes/neuron-lens-v1/lecture-b-beta/plan-de-lecture-b-beta-v2.md` (429 lignes, lu en entier) | `391c3b1a642d0d96ccef2c982594b334dd1e2e57c398b9cde21436f661bbe14d` | égale aux deux |
| plan v1 (archivé, non réécrit) | `40128756b446301248827cc5a9facfd53baa5cf6b461a8b09731369b61208128` | égale |
| ma contre-lecture de la v1 | `bf3e2d7572b85df806d5841a0b8a7342829893a86503738fbb153721e33ec4e7` | égale à celle que cite la v2 |
| texte gelé | `f5d46860525f12f8ad0483e56afc0847ab7db25ecae55edcc279b61316b7a454` | égale |
| addendum, partie 1, v3 | `bd8067dcd04ae32bb5960dc95bef89384b3b914a1a35e918107411f43d1c95f1` | égale |

- Horodatage sur disque (`stat`) : v2 écrite à 07:33:11 UTC, compagnon 07:33:15 ; en-tête de la v2 : 07:29:34 puis 07:30:21 ; ma
  contre-lecture scellée à 07:28:46. Cohérent.
- **Aucun fichier interdit ouvert**, mêmes interdits qu'à la contre-lecture ; aucun modèle, aucune machine, aucun commit, aucun push ;
  aucun plan modifié.

## Verdict : « employable »

**0 bloquante, 0 majeure, 6 mineures.** Les 2 majeures et les 13 mineures de la contre-lecture sont traitées, toutes de façon
suffisante. La v2 n'ajoute ni seuil, ni issue, ni règle de verdict ; ce qu'elle ajoute est de la procédure (classement des pièces,
ordre, ouverture « structure d'abord », essai du script), dans le sens strict. Aucun résultat n'a fui.

## 1. Traitement de chaque remarque

| remarque | où dans la v2 | suffisant ? |
|---|---|---|
| M-1, lectures de l'addendum | l. 16-18 ; 3.0 (l. 216-224) ; 4.1, T-1 à T-5 (l. 367-377) | oui — les cinq lectures sont recopiées sans déformation de l'addendum (l. 24-25, 41-42, 45-46, 47-49), effets déclarés compris (comptes 4 sur 12, 3 sur 8, 2 sur 4 ; retrait du déclencheur de l'audit de l'ablation par le haut, repris à la l. 343) ; la lettre seule reste donnée comme information |
| M-2, ordre des gardes recalculables | 2.1 à 2.3 (l. 101-183) | oui, voir la section 3 ci-dessous et les mineures 1 et 2 |
| mineure 1 (« au moins 0,10 ») | l. 253-254 ; T-5 (l. 375-377) | oui |
| mineure 2 (« reproduit » sur bande partielle) | O-1 (l. 382-384) | oui, laissée ouverte, orientation dite |
| mineure 3 (bande sans couche lisible) | T-1, O-1 | oui |
| mineure 4 (garde du pilotage sans effet ; n par lentille) | O-2, O-3 (l. 385-390) ; l. 65-67 | oui |
| mineure 5 (deux fichiers de verdicts ; écart des deux parties de l'addendum) | T-6 (l. 378-379) ; O-8 (l. 401-403) | oui |
| mineure 6 (garde sans trace ; réserve de matériel) | O-7 (l. 398-400) ; R-1 (l. 411-413) ; l. 90 | oui |
| mineure 7 (garde de la lentille R publique lue à la lettre) | l. 233-235 ; l. 285-286 | oui |
| mineure 8 (« notre R » et les moitiés) | O-9 (l. 404-405) | oui |
| mineure 9 (copies omises) | l. 307 (rang 2 complet) ; l. 291-295 (moments) ; l. 328-330 (contrôles (1) et (2)) ; l. 341-342 | oui, conformes au texte (l. 491, 236, 240-241, 518, 521) |
| mineure 10 (grandeurs à rapporter, mentions) | 2.4 (l. 185-190) ; 2.7 (l. 209-212) | oui |
| mineure 11 (arrêts de montage) | 2.5 (l. 192-198) ; 3.8 (l. 352-358) | oui, conformes à la liste d'arrêt (texte l. 542-547 ; addendum l. 89-91, 111-113) |
| mineure 12 (essai du script sur les cas gelés) | étape A (l. 145-153) | oui ; les cas rejoués et ceux écartés (matrices, fichiers, machine) sont nommés |
| mineure 13 (empreinte de l'addendum ; indépendance) | étape 0 (l. 142-143) ; l. 65-67 | oui |

## 2. Règle nouvelle, écart ou déformation ?

Aucun. Sections 3.1 à 3.7 comparées de nouveau au texte gelé (l. 109-128, 168-253, 487-529) : chiffres et quantificateurs
inchangés depuis la v1, compléments exacts. La section 3.0 ne fait que recopier l'addendum. Les annotations « moitiés comprises »
(l. 265-266), « à la lettre » (l. 286) et « pas de déclencheur si la bande 8 à 15 est partielle » (l. 343) sont des renvois, non des
règles. La procédure « structure d'abord » (l. 136-139) et le classement des pièces n'ont d'effet sur aucun verdict. La liste des
gardes « constatées sur la machine seulement » (l. 134-135) est juste : aucune ne se recalcule sans les lentilles, les fichiers
d'ajustement ou la machine.

## 3. L'ordre

Garanti par engagement écrit, étape par étape : script essayé avant toute pièce de la course (étape A) ; gardes recalculables,
déclencheurs et mesures calculés sur les sorties brutes et **scellés** (étape B, points 3 et 4) ; verdict du lecteur scellé, avec la
table selon l'issue des gardes de la machine (étape C) ; pièces portant des gardes ensuite (étape D), verdict complété et scellé ;
fichiers de verdicts et de déclencheurs de la course en dernier (étape E, l. 176-179). Seule exception, déclarée et nécessaire :
l'extraction des différences entre moitiés (et de n s'il le faut) d'un résultat d'étape, après le premier scellement, par noms de
clés d'abord (l. 163-165). Aucun import ni relecture du code des verdicts (l. 146, 426).

## 4. Fuite de résultat

Aucune. La v2 ne porte aucune valeur de mesure, aucun verdict ; ce que le lecteur sait d'un résultat (l. 81-92) est celui de la v1,
dit de seconde main.

## Remarques mineures (aucune n'exige une v3 ; chacune se tient à l'exécution, dans le sens strict)

1. **Deux pièces rangées « sorties brutes » sont écrites par notre code de course** (plan l. 106-107 :
   `grandeurs-par-pole-b-beta-v1.json`, `intervalles-b-beta-v1.json`) ; le lecteur ne peut pas savoir sans les ouvrir si elles portent
   une garde ou un drapeau, et sa propre définition range alors la pièce en seconde catégorie (l. 113-114). Correction : leur appliquer
   la procédure « structure d'abord » (l. 136-139), comme à toute sortie brute dont les clés ne sont pas connues d'avance.
2. **La clause générale d'exposition involontaire de la v1** (v1 l. 69-70) ne subsiste que dans la procédure « structure d'abord »
   (v2 l. 138-139). Correction : la tenir pour toute pièce, des deux catégories.
3. **La confrontation des fichiers versés à la liste des sorties du texte** (v1 l. 83 ; texte l. 467-476) a disparu de la v2.
   Correction : la faire à l'étape D et la rapporter à l'étape F ; toute sortie absente est nommée.
4. **Étape D, « rang 2 si un audit que j'ai déclenché n'a pas été joué »** (l. 174) se lit sous les ambiguïtés ouvertes O-5 et O-6
   (l. 393-397), qui gardent les deux lectures ; la phrase de l'étape D n'en tranche aucune.
5. **Section 2.6** (l. 200-207) : les pièces nommées pour chaque garde sont des lieux de recherche supposés ; avant de dire une garde
   « sans trace » (O-7), chercher dans toutes les pièces de la catégorie 2a.
6. **Forme** : la tête citée (l. 11, `8845ea8c`) est celle du lancement ; le dépôt porte depuis le commit du plan v1
   (`75e68598f`). Sans effet.

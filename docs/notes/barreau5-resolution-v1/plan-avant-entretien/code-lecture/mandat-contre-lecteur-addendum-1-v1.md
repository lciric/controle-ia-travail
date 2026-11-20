# Mandat du contre-lecteur de l'addendum 1 du plan « sabotage ou empreinte » (barreau 5) — v1

Écrit par la mère (`session_01XJ6Mgr8BN6UanALsQatc5E`) le 20 novembre 2026 vers 02:15Z. Pièce de travail.

Destinataire : un contre-lecteur neuf, Claude Opus 5.5, d'un autre modèle que le rédacteur (Fable 5.2). L'addendum est une pièce de classe A : contre-lecture par toi, puis vérification de ses corrections par toi aussi, puis scellement sur le mot de Lazar.

---

Le rédacteur a écrit l'addendum 1 au texte scellé du plan. Il fixe trois points que le texte ne tranchait pas, relevés par le développeur et par le contre-lecteur du code de lecture. Aucune donnée de lecture n'existe : la formation tourne, rien n'est lu. Tu contre-lis l'addendum.

## Pièces (vérifie chaque empreinte avant de lire)
- **Le brouillon** : `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-addendum-1-brouillon1.md` (`1c7d6e51fb355ab0349b93435bcb404a9bee82f5cb5064be5f4d8640c38632a8`), en entier.
- **Le rapport du rédacteur** : `docs/notes/barreau5-resolution-v1/plan-avant-entretien/code-lecture/rapport-redacteur-addendum-1-v1.md` (`7ce41d67e798570de13b944620a0789d8851fb240d6675812df85097ddffb231`), en entier.
- **Son mandat** : `docs/notes/barreau5-resolution-v1/plan-avant-entretien/code-lecture/mandat-redacteur-addendum-1-plan-v1.md` (`1645afec…`).
- **Le texte scellé** : `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1.md` (`bdff244f1377e795b84f71518bb5e58fb1600fff8afee383d8f70c10d3f5d935`). Lis seulement :
  - « Métrique », « Seuil » ;
  - « Plan d'analyse », points 10 à 17 ;
  - « Critères de lecture gelés », « Ce que dira chaque issue au jury » ;
  - « Nœuds », point 6 ;
  - « Liste d'arrêt ».
  Ne lis pas « Ce que le rédacteur savait avant d'écrire » ni « La question » : ces passages citent des résultats que tu n'as pas à voir.
- **La contre-lecture du code de lecture** : `docs/notes/barreau5-resolution-v1/plan-avant-entretien/code-lecture/contre-lecture-code-lecture-v2.md` (`f2f81f32…`), ses réponses aux questions, et les constats M-2 et m-4.
- **Le code**, aux seules lignes que citent le brouillon et le rapport : `src/controle_ia/barreau5_familles/lecture_v1.py`.

## Ce que tu juges
1. **Chacun des trois points.** Pour chacun :
   - La règle suit-elle la lettre et l'esprit du texte scellé, ou en change-t-elle quelque chose ? On ne doit toucher ni hypothèse, ni prédiction, ni seuil, ni critère, ni épreuve, ni liste d'arrêt.
   - Un programme peut-il l'appliquer sans faire de choix ?
   - A-t-elle pu être inspirée par une donnée ? Il n'en existe aucune ; vérifie ce que le rédacteur dit avoir lu.
2. **Les deux choix que le rédacteur porte à Lazar** : le cas limite d'une famille sans tâche retenue, et ½ Δ_app comme borne. Sont-ils bien posés ? Les options et la recommandation sont-elles honnêtes ?
3. **Les deux points laissés ouverts** :
   - le cas m-4 de la contre-lecture du code ;
   - « M1 dans toutes les épreuves », le constat M-2.
   Doivent-ils entrer dans cet addendum ? Si oui, donne leur règle sous forme de couple.
4. **L'exposition déclarée** : les lignes 59 à 61 du texte, lues par le rédacteur. Change-t-elle quelque chose à la validité de l'addendum ?
5. **Ce que l'addendum change dans le code et dans l'épreuve à vérité plantée** (point 11). La liste est-elle complète ?

## Forme et sorties
- **Verdict en tête**, l'un des trois : « scellable tel quel », « scellable après ces couples », « à reprendre ».
  - Couples exacts : fichier, avant, après. Chaque « avant » doit être trouvé une seule fois, par programme.
  - L'heure fausse de l'en-tête, déclarée par le rédacteur, se corrige par un couple.
- **Sorties**, scellées, non commises :
  - `docs/notes/barreau5-resolution-v1/plan-avant-entretien/code-lecture/contre-lecture-addendum-1-v1.md` ;
  - tes outils dans `code-lecture/outils-contre-lecture-addendum-1-v1/`.
- **Commande de scellement** : `cd /home/user/controle-ia-travail && PYTHONPATH=src .venv/bin/python -B -m controle_ia.scellement sceller <fichier>`.

## Règles
- **Aucune donnée.** Rien de `diag/`, aucun score, aucune transcription, aucun résultat de 7a, 7b, T0.6, de l'étape B, de l'étape B bis ni de P3-bis.
- **Fichiers interdits** : aucun fichier dont le nom contient « consigne-privee » ou « conception-ii-b ». Rien sous `/root/.claude/`.
- **Aucune commande de liste ni de recherche récursive** sur une racine large. Chaque fichier s'ouvre par son chemin entier.
- **Pas de code en ligne passé à l'interpréteur** : écris tes programmes dans ton bloc-notes et lance-les par leur chemin.
- **Garde du dépôt** : aucun nom de commande d'arrêt ou de recherche de processus par motif.
- **Aucun réseau**, aucune dépense, aucun commit, aucune modification du dépôt hors de tes sorties.
- **Une commande simple à la fois.**
- **Refus ou limite** : au premier refus d'outil ou à la limite d'usage, arrête-toi et dis-le.
- **Tenue** : ne nomme dans tes pièces aucun identifiant d'accord d'écart à la règle R9.

## Rends
1. La phrase exacte de ton invite système qui nomme ton modèle.
2. Les chemins et les empreintes de tes sorties.
3. Dix lignes au plus :
   - le verdict ;
   - les constats ;
   - ton avis sur les deux choix pour Lazar ;
   - ce qui menace le gel.

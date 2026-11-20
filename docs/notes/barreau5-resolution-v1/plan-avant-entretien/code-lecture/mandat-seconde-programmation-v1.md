# Mandat de la seconde programmation du dénombrement exact et de la table des issues (barreau 5) — v1

Écrit par la mère (`session_01XJ6Mgr8BN6UanALsQatc5E`) le 20 novembre 2026. Pièce de travail.

Destinataire : un programmeur neuf, Claude Fable 5.2, « l'autre modèle » du point 11 : le programme de lecture a été écrit par un développeur Opus 5.5. Pièce d'instrument : contre-lecture par un autre modèle (Opus 5.5), puis vérification des corrections par le même contre-lecteur.

---

Le texte du plan est scellé : `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1.md` (`bdff244f1377e795b84f71518bb5e58fb1600fff8afee383d8f70c10d3f5d935`). Son point 11 dit : « Le dénombrement exact et la table des issues sont programmés une seconde fois par l'autre modèle ; l'accord exigé est exact. » Tu écris cette seconde programmation **à partir des textes seuls**, sans voir comment le premier programme les calcule. Elle sera comparée au programme figé, monde par monde, dans l'épreuve à vérité plantée.

## Pièces (vérifie chaque empreinte)
- **Le texte scellé.** Lis : « Hypothèse », « Prédiction chiffrée et signe attendu », « Métrique », « Seuil », « Plan d'analyse » en entier, « Puissance », « Critères de lecture gelés », « Ce que dira chaque issue au jury », « Liste d'arrêt », « Nœuds ». Ne lis pas « Ce que le rédacteur savait avant d'écrire » ni « La question » : ces passages citent des résultats que tu n'as pas à voir.
- **L'addendum 1, scellé**, en entier : `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-addendum-1.md` (`2afa2186c9f11e0a477cdf628348d2cad3bce90de5933597ff09a4a3048499e4`). Il fixe le niveau d'une issue sous moins de dix familles, le retrait d'une tâche sans coût lisible, la valeur de la borne de la phrase E (½ Δ_app) et le compte d'une famille sans tâche retenue (absente).
- **Ce que tu peux lire du premier programme, et rien d'autre** :
  - le commentaire de tête de `src/controle_ia/barreau5_familles/lecture_v1.py` (`d877d2dea0ddd4707324139aaa63e4bdae1f89a2aa23bea145adf4175a62c0df`), qui documente les entrées ;
  - la forme du fichier de résultat qu'il écrit : ses noms de champs et leurs types, tels que les documentent le rapport v3, section 1 (`docs/notes/barreau5-resolution-v1/plan-avant-entretien/code-lecture/rapport-developpeur-code-lecture-v3.md`, `b9c77d67e174d9a090b02a55ca9649b15e7fd79e1a1d3b04698ad83be222554e`) et le rapport v4 (`rapport-developpeur-code-lecture-v4.md`, même dossier, `1bc78521a72f4e3b093e7e452239fc2249fbc05a813c3965a9d47b24cfc98c68`), sections 1 et 2.
- **Ce que tu ne lis pas** : le corps de `lecture_v1.py`, ses essais, ses outils et ses mutations, la contre-lecture et les vérifications du code de lecture. Une seconde programmation qui aurait vu la première ne serait pas une seconde programmation. Si ce qui t'est permis ne te suffit pas, dis-le dans ton rapport, sans lire plus.

## Ce que tu écris
1. **`src/controle_ia/barreau5_familles/seconde_programmation_v1.py`**, module neuf, à partir du texte et de l'addendum :
   - le **dénombrement exact** des rangs signés de chaque épreuve (E1, E2a, E2b, E3), à partir des différences d_k des familles présentes : statistique, loi exacte sous la nulle symétrique, seuils et verdicts (« séparé », « contraire », ni l'un ni l'autre), au niveau que fixent le texte et l'addendum selon le nombre de familles ;
   - la **table des issues** : à partir des verdicts des épreuves, de M1 et de M3, l'issue et sa phrase exacte, telle que l'écrivent « Critères de lecture gelés » et « Ce que dira chaque issue au jury », avec la règle du nœud 6 et les points 1 à 4 de l'addendum.
   Chaque règle cite, en commentaire, la phrase du texte ou de l'addendum qu'elle applique.
2. **Un comparateur**, dans le même module ou un module à côté. Il lit un fichier de résultat du premier programme, reprend les entrées que ce fichier porte (les d_k par épreuve, les familles présentes, M1, M3), les passe à ta seconde programmation, et compare champ par champ : statistiques, seuils, verdicts, issue, phrase. Il rend « accord exact » ou la liste des désaccords.
   - **Si le fichier de résultat ne porte pas les entrées qu'il te faut**, par exemple si les d_k n'y sont pas écrits, n'invente rien et ne lis pas le code : écris exactement, dans ton rapport, le champ qui manque. La mère le fera ajouter au premier programme avant son gel.
3. **Les essais** : `tests/test_barreau5_familles_seconde_programmation_v1.py`. Pour chaque épreuve et chaque issue, un cas sain et un artefact (R5). Le dénombrement est vérifié contre une énumération directe des 2^n signes, pour n petit. Le comparateur rend « accord exact » sur un résultat fabriqué juste, et la liste des désaccords sur un résultat fabriqué faux, l'un et l'autre de ta fabrication. Le vrai programme de lecture n'est jamais joué par tes essais. Ajoute un passage de mutations sur ton module.

## Ce que tu ne fais pas
- Tu ne joues pas le premier programme et tu ne joues pas l'épreuve à vérité plantée : elle se joue après le gel (`CODE-LECTURE-B5F`).
- Tu ne modifies aucun fichier existant du paquet.

## Règles
- **Aucune donnée.** Rien de `diag/`, aucun score réel, aucune activation, aucune transcription, aucun résultat de 7a, 7b, T0.6, de l'étape B, de l'étape B bis ni de P3-bis. Rien de la branche de la formation.
- **Fichiers interdits** : aucun fichier dont le nom contient « consigne-privee » ou « conception-ii-b ». Rien sous `/root/.claude/` ni sous `archives-reponses-modeles/`.
- **Pas de recherche large.** Aucune commande de liste ni de recherche récursive sur une racine large ; ouvre chaque fichier par son chemin entier.
- **Pas de code en ligne passé à l'interpréteur**, ni `python -c`, ni `python -`. Écris un fichier dans ton bloc-notes et lance-le par son chemin. Redirige toute sortie longue vers un fichier de ton bloc-notes.
- **Garde du dépôt** : aucun nom de commande d'arrêt ou de recherche de processus par motif.
- **Une commande simple à la fois.**
- **Écriture** : tes fichiers seulement, par les outils d'écriture et d'édition. Ni réseau, ni dépense, ni commit.
- **Essais** : seulement tes fichiers d'essais neufs. Temporaires dans `/dev/shm`, effacés à la fin par leur chemin écrit en toutes lettres.
- **Tenue** : ne nomme dans tes pièces aucun identifiant d'accord d'écart à la règle R9.
- **Refus** : au premier refus d'outil, de classifieur ou de garde, arrête-toi et dis-le.

## Sorties
- Le module, ses essais, et le rapport scellé `docs/notes/barreau5-resolution-v1/plan-avant-entretien/code-lecture/rapport-seconde-programmation-v1.md`. Le rapport donne :
  - les passages du texte et de l'addendum appliqués, règle par règle ;
  - les entrées que lit le comparateur, et tout champ qui manque au fichier de résultat ;
  - tes doutes sur la lettre du texte, chacun avec le passage ;
  - les empreintes, les essais et les mutations.
- Tes outils dans `code-lecture/outils-seconde-programmation-v1/`.
- Commande de scellement : `cd /home/user/controle-ia-travail && PYTHONPATH=src .venv/bin/python -B -m controle_ia.scellement sceller <fichier>`.
- Écris au fil de l'eau, et scelle chaque état.

## Rends
1. La phrase exacte de ton invite système qui nomme ton modèle.
2. Les chemins et les empreintes de tes fichiers.
3. Dix lignes au plus : ce qui est fait ; les champs qui manquent au fichier de résultat, s'il y en a ; tes doutes sur le texte ; les essais et les mutations.

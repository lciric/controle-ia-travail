# Rapport du contrôle de conformité du code au texte — passe de recalcul de l'activité interne (version 5) et lecture des sondes (version 5), barreau 8 — v1

**Statut : version 1, finale, non encore scellée** (le scellement revient à la session mère). Elle **remplace**, sans le réécrire, le brouillon 1 de ce rapport, `docs/notes/barreau8-cote-moniteurs-sorties-v1/rapport-conformite-codes-passe-v5-lecture-v5-brouillon1.md`, empreinte `44aaa3da756097b2495661014a6547d4905a9185c0dc71b3faf322b207a55a7d` (égale à son compagnon), qui jugeait les codes contre le brouillon 14 du texte. C'est ce fichier-ci que citent les bordereaux du code.

## Pièces jugées

- **Texte scellé** : `prereg/lecture-sondes-barreau8-v1.md`, empreinte `8e432cdc3d6998324281467e1bac5df3adb93ff7ba803b8ad7f877ffd5e8feb4`, scellé le 2026-11-19 à 06:32:25Z (heure transmise par la session mère). Lu sur la branche distante `main` par `git show origin/main:prereg/lecture-sondes-barreau8-v1.md` (aucun fetch, aucun checkout, arbre de travail inchangé) ; empreinte recalculée par moi : `8e432cdc3d6998324281467e1bac5df3adb93ff7ba803b8ad7f877ffd5e8feb4`, égale à celle donnée et à son compagnon `.sha256` sur la même branche.
- **Code de la passe** : `src/controle_ia/barreau8_moniteurs/passe_recalcul_v5.py`, empreinte `a5eeef6203b558dbc0c1b58085d2dd4d13617a7c76e9aa374aa224304b19759f` ; essais `tests/test_barreau8_moniteurs_passe_v5.py` (`c8cbfdbee7043f776106f7c46f242a2b4d577d0086c4d02273067441b80db0ff`) ; notice `docs/notes/barreau8-cote-moniteurs-sorties-v1/notice-passe-recalcul-v5.md` (`e7591c562bee76cc50fce2a98d19d805a7e4879ceb3c4a0b05b9c4def1205558`).
- **Code de la lecture** : `src/controle_ia/barreau8_moniteurs/lecture_sondes_v5.py`, empreinte `aa1476fd6bf6bb5536fba0c16d2aa481393bf408fe68825d3b7987359666e139` ; essais `tests/test_barreau8_moniteurs_lecture_v5.py` (`04f4110b34ba8347c709a8b016ebd812630c22f8438045b52b8863ffc0b4f7fa`) ; notice `docs/notes/barreau8-cote-moniteurs-sorties-v1/notice-lecture-sondes-v5.md` (`d37206ebc627db39c7db9029d03dd3fe8ef1e24a457bfced8d0cbc005406fbab`).
- Les empreintes des deux codes ont été recalculées au moment d'écrire cette version : inchangées depuis le brouillon 1.

## Qui, comment

- **Contre-lecteur** : sous-agent neuf, modèle Claude Opus 5.5 (`claude-opus-5-5`), lancé par la session « barreau 8, côté moniteurs » le 2026-11-19 (UTC). Je n'ai écrit ni le texte, ni la note d'interface, ni aucune notice, ni aucun des deux codes, ni leurs essais, ni aucune contre-lecture antérieure du texte. Je ne suis pas le modèle de l'auteur des deux codes (Fable 5.2, d'après leurs notices).
- **Déclaration du mode de sabotage (décision N-054, point 3)** : j'ai appris en lisant (texte, ligne 6 et table I, ligne I-10 ; note d'interface, question (10)) que le mode de sabotage de l'organisme est **« coût » (seul)**. Je ne conçois aucun bras ; je le déclare pour la règle.
- **Méthode** : lecture section par section du texte et des deux codes ; jeu des deux suites d'essais du dépôt, fichier par fichier, au premier plan ; essais propres sur données synthétiques (aucune donnée du programme ni de la course, aucune machine louée, aucun modèle, aucun accès réseau). Aucun refus d'outil n'a eu lieu. Aucun fichier existant n'a été modifié ; rien n'a été committé ni poussé.

### Fichiers lus (chemin, empreinte vérifiée par `sha256sum` avant lecture)

| fichier | empreinte | lu |
|---|---|---|
| texte scellé, `prereg/lecture-sondes-barreau8-v1.md` (branche `origin/main`) | `8e432cdc3d6998324281467e1bac5df3adb93ff7ba803b8ad7f877ffd5e8feb4` | par différence, faite par programme, avec le brouillon 14 (ci-dessous) |
| brouillon 14, `brouillons/barreau8-lecture-sondes-v1/prereg-lecture-sondes-barreau8-v1-brouillon14.md` | `5b503e28e6b81285a792575f878642bbd529888cc886e7cd4ddcf80257e39891` | en entier (442 lignes) |
| `src/controle_ia/barreau8_moniteurs/passe_recalcul_v5.py` | `a5eeef6203b558dbc0c1b58085d2dd4d13617a7c76e9aa374aa224304b19759f` (égale à son compagnon) | en entier |
| `tests/test_barreau8_moniteurs_passe_v5.py` | `c8cbfdbee7043f776106f7c46f242a2b4d577d0086c4d02273067441b80db0ff` | noms des essais, essai de la trace (l. 785 à 805), en-tête des artefacts de P0 |
| `docs/notes/barreau8-cote-moniteurs-sorties-v1/notice-passe-recalcul-v5.md` | `e7591c562bee76cc50fce2a98d19d805a7e4879ceb3c4a0b05b9c4def1205558` | en entier |
| `src/controle_ia/barreau8_moniteurs/lecture_sondes_v5.py` | `aa1476fd6bf6bb5536fba0c16d2aa481393bf408fe68825d3b7987359666e139` (égale à son compagnon) | en entier |
| `tests/test_barreau8_moniteurs_lecture_v5.py` | `04f4110b34ba8347c709a8b016ebd812630c22f8438045b52b8863ffc0b4f7fa` | en-tête (l. 1 à 80), artefacts de réception (l. 680 à 909), refus de tourner et bordereau (l. 1840 à 2075), noms de tous les essais |
| `docs/notes/barreau8-cote-moniteurs-sorties-v1/notice-lecture-sondes-v5.md` | `d37206ebc627db39c7db9029d03dd3fe8ef1e24a457bfced8d0cbc005406fbab` | en entier |
| note d'interface v6, `docs/notes/barreau8-cote-moniteurs-entrees-v1/interface-passe-cote-moniteurs-v6.md` | `20c9ed6e480646b6bf3a5f6007be5f88b439c916763a618f3880634e92ad8ce1` | en entier ; renvois non suivis |
| `src/controle_ia/premier_test_ia/figees.py` | `a2238a8c6f164f59f7d30e3ca15c45be136cb3ad5cdf149816622d81450938cc` (celle du texte, l. 31) | en entier |
| `src/controle_ia/sondes/familles.py` | `6758b651fdcbc6d0108a03263b79ffb1e7c5d0a8be57b0f10502c1645d2b457e` (celle du texte, l. 30) | lignes 1 à 110 |
| `src/controle_ia/manifeste.py` | `1a5c7464523e224ca29d62ab70d83f9e7043d9bde3000ef1a4adc9ed74c8188d` (celle du texte, l. 37) | en entier |
| `src/controle_ia/sondes/evaluation.py` | `1040674cb321766a0e2a7fa1e0c610384df6c4fac4109dd50c42dfbb03181ed3` (celle du texte, l. 32) | en entier |
| `src/controle_ia/t07/plancher_v2.py` | `a0f80e6826b77279dfb807863af106655c2515f69d6d415657b7b121598ee796` (celle du texte, l. 33) | en entier |
| `src/controle_ia/t07/registre_v1.py` | `e50236574fbcd7e48ea3005eadc8bdb68d2c753d10028db7f2c365648a843cec` | en entier |
| `src/controle_ia/harnais/sondes.py` | `f92657a69cf0d5781017e50117aeb1672dda60719aea51ffbfd9e566f3e7d94d` (celle du texte, l. 29) | lignes 55 à 89 (`score_action`) |

Les autres modules importés (`gardes`, `prereg`, `scellement`, `harnais.activations`, `harnais.formats`, `harnais.modeles`, `organismes.lora`, `premier_test_ia.conditions`, `environnements.*`, `t06.distillation_transcription`) n'ont été lus qu'à travers leurs appels dans les deux codes ; leur comportement est tenu par les essais du dépôt, non par moi. **Rien de ce qui est interdit n'a été ouvert** : ni `src/controle_ia/iib/`, ni `tests/test_iib_*`, ni `diag/`, `runs/`, `donnees/`, `docs/verdicts/`, ni le dossier du saboteur, ni les registres, ni les autres brouillons et rapports des deux dossiers (le texte et les notices en citent : je me suis arrêté à la référence ; la nouvelle ligne 442 du texte scellé cite un rapport de contre-lecture que je n'ai pas ouvert). Aucune recherche récursive : les seules recherches de motif ont porté sur les deux fichiers de code et les deux fichiers d'essais, chacun nommé.

## Constat 1 : le texte scellé ne diffère du brouillon 14 que par les lignes 76 et 442

Comparaison faite par programme : `diff brouillons/barreau8-lecture-sondes-v1/prereg-lecture-sondes-barreau8-v1-brouillon14.md <copie du texte scellé tirée de origin/main>` ; code de sortie 1 ; sortie exacte :

```
76c76
< | F-3 | entropie racine des graines | À REMPLIR — À FIXER : tirée par la session mère au scellement |
---
> | F-3 | entropie racine des graines | 149333987590752343984325077404464904184 |
442c442
< - **Contre-lecture 4 (finale, texte rempli)** — À REMPLIR : sous-agent neuf, qui n'a écrit ni ce texte ni la note d'interface ; il vérifie la différence entre le dernier brouillon contre-lu et le texte soumis au scellement, champ par champ (chaque valeur contre sa source, chemin et empreinte), et toute réécriture qu'un champ entraîne ; empreinte du texte relu, chemin et empreinte de son rapport. **Règle** : le texte scellé ne diffère du texte relu par cette dernière contre-lecture que par cette entrée et par la cellule « état et raison » de F-3, où seule l'entropie tirée remplace le marqueur ; la session mère le vérifie par une comparaison faite par programme, versée avec l'empreinte du texte scellé.
---
> - **Contre-lecture 4 (finale, texte rempli)** — sous-agent neuf, modèle Claude Opus 5.5, qui n'a écrit ni ce texte, ni aucune contre-lecture antérieure de ce texte, ni la note d'interface, ni aucune notice, ni aucun code ; contre-lecture de la différence du brouillon 13 au brouillon 14 (remplacements R-1 et R-2, correction de forme O-6, phrases T-1 à T-4 du troisième essai d'intégration, fait transmis sur le nom de la course, trois ajouts du rédacteur) et lecture d'ensemble du texte soumis au scellement. Brouillon relu : `brouillons/barreau8-lecture-sondes-v1/prereg-lecture-sondes-barreau8-v1-brouillon14.md`, empreinte `5b503e28e6b81285a792575f878642bbd529888cc886e7cd4ddcf80257e39891`. Rapport : `brouillons/barreau8-lecture-sondes-v1/contre-lecture-brouillon14-v1.md`, empreinte `d7d688f7bf5c5c39dae902f886bb9c4c8417697f563d8e60cc23a495d8f4341e`. Conclusion : « PRÊT : le brouillon 14 peut être scellé une fois l'entropie des graines versée et cette entrée de contre-lecture portée au texte, sans autre changement ». **Règle** : le texte scellé ne diffère du texte relu par cette contre-lecture que par cette entrée et par la cellule « état et raison » de F-3, où seule l'entropie tirée remplace le marqueur ; la session mère le vérifie par une comparaison faite par programme, versée avec l'empreinte du texte scellé.
```

Les deux fichiers ont le même nombre de lignes ; **toutes les autres lignes sont identiques à l'octet**. Les numéros de ligne du texte cités dans la table ci-dessous valent donc pour le texte scellé comme pour le brouillon 14. La cellule F-3 ne porte que l'entier, en décimal, sans séparateur ni autre mot, comme l'exige le plan, point 5 (l. 170).

## Constat 2 : ces deux lignes ne changent rien au jugement de conformité

- **Ligne 442** (entrée de la contre-lecture finale) : aucun des deux codes ne la lit ; elle n'est que de provenance. Elle ôte l'un des deux derniers marqueurs que le validateur refusait (`prereg.problemes`) : le texte scellé passe donc `exiger_prereg_scelle`, ce que la passe (garde P0, P 735) et la lecture (L 1270) exigent.
- **Ligne 76** (entropie racine, champ F-3) : c'est la seule valeur du texte que lise un code. **La lecture et la recette de la puissance la lisent dans le texte scellé** (`exiger_texte_scelle`, L 1261 à 1280 : expression `CELLULE_F3`, une seule ligne de table `| F-3 | … | <entier> |`, cellule faite de chiffres seuls et égale à `str(int(entropie))` de la commande) ; la commande de réception ne la reçoit pas (texte, l. 96) ; la passe la reçoit en paramètre (`--entropie`) sans la comparer à F-3, ce que le texte n'exige pas d'elle (l. 170 ; écart non bloquant n° 5 ci-dessous). **Contrôle sur données synthétiques** (fichier `/tmp/claude-0/-home-user-controle-ia-travail/ccd98af0-e97a-5c3c-8902-30e463468b85/scratchpad/conformite/essai_entropie.py`, dépôt jouable dans un dossier temporaire, retiré à la fin ; aucune donnée de la course), avec l'entier de 39 chiffres `149333987590752343984325077404464904184` :
  - une copie du texte scellé, scellée dans un dossier d'essai, garde l'empreinte `8e432cdc…8feb4` ; `CELLULE_F3` y trouve une cellule et une seule, ` 149333987590752343984325077404464904184 ` ;
  - `exiger_texte_scelle(…, entropie=149333987590752343984325077404464904184)` est tenu (cas sain) ; l'entier plus un, et l'entier privé de son dernier chiffre, sont refusés sous le code « 1 » (artefacts) ;
  - l'entier a 39 chiffres et est inférieur à 2¹²⁸ : `numpy.random.SeedSequence` le prend tel quel ; `manifeste.graines` le consigne sous forme de chaîne égale ; la graine entière (premier mot de 64 bits) d'une même clé est la même dans les deux codes (`L.graine_entiere`, `P._graine_entiere`) ;
  - les analyseurs de ligne de commande des deux codes (`--entropie`, type `int` de Python, sans borne) rendent l'entier exact ;
  - la recette de la puissance, réduite (6 tâches, 3 pas, 8 directions, 40 tirages, 2 répétitions, une case), tourne sous cette entropie et la recopie exacte dans sa sortie ; la condition D-10 compare cette chaîne à celle du manifeste (L 2052).

  Sorties exactes du contrôle : `copie scellée 8e432cdc3d6998324281467e1bac5df3adb93ff7ba803b8ad7f877ffd5e8feb4` ; `cellules F-3 trouvées : [' 149333987590752343984325077404464904184 ']` ; `sain : True` ; `artefact refusé : 1` (deux fois) ; `chiffres : 39 ; < 2**128 : True` ; `entropie consignée : True` ; `graine entière égale dans les deux codes : True` ; `analyseur de la passe : True` ; `analyseur de la lecture : True` ; `recette réduite : True ['calculée']`.

Le jugement du brouillon 1 vaut donc pour le texte scellé, sans changement.


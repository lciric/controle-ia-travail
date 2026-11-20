# Rapport du rédacteur — préenregistrement court v7 et devis v5 de la course « nouvelles attaques » — v1

Pièce de travail (classe C), 2026-11-20, relevé de `date -u` : 12:30:11Z avant l'écriture. Mandat : `docs/notes/ideation-nouvelles-attaques-v1/preenregistrement-court-v7/mandat-redacteur-preenregistrement-court-v7-devis-v5-v1.md` (`09ad78ba66e7d11ead6ceac08e4ce1cabcd3469a1b68dcdec3ad75d16e4b1e4b`, compagnon « OK »). Processeur seul : aucun appel à un fournisseur, aucune dépense, aucun lancement du relais, du véhicule ni d'une sonde, aucune écriture dans le dépôt, aucun commit, aucune publication. Aucune méthode d'attaque, aucun procédé, aucun nom ni énoncé de mode, aucune valeur de clé, aucun identifiant de modèle. Aucun refus de permission, de classifieur ni de garde.

## 0. Verdict

- **La v7 est écrite** par 35 remplacements à texte exact sur la v6 scellée, par l'outil contre-lu, en une passe sans refus. Le validateur du dépôt rend : huit sections exigées présentes, aucune absente, « problemes : aucun ».
- **Le devis v5 est écrit** par 11 remplacements sur le devis v4 scellé. **Aucun total ne change** : ligne demandée 570 USD, plafond total 576,01 USD. Le programme v4 garde le code du v3 ; sa sortie ne diffère de celle du v3 que par le libellé et deux champs neufs.
- **Le mot du directeur sur l'épreuve 4 n'est pas sur `main`** (commit `ee888da750662e5db8352fb63d39f4b293c4773f`) : les deux branches sont écrites, sans trancher.
- **Deux clés ne tiennent pas au cas bas** sur leurs restes estimés (espèce 6 et troisième relais) ; dit, non tranché.
- Douze points non tranchés (§ 4), dont deux lectures que j'ai dû prendre pour écrire : celle du point 3 de GO-2026-11-20-46 (le portier) et la case de la sonde.

## 1. Pièces lues et empreintes

Tirées de `origin/main` (`ee888da7…`) par `git show … >`, empreintes recalculées : préenregistrement court v6 (`7e240c8c9b059171e06b416d5cf8b14c6822978f84219ad2d9770a32f90f11c5`) ; devis v4 (`620de3692d3454f08d32832ca471551bb9a8439f80122b716b13474d9a6d363e`) ; question v5 (`eaf5db8a558547aa8f5df45008a34eebf4cb7a163e12ca400176401de6f5ce0f`) ; partie servie (`4cd360baea1076ec2b19b2c7ba85675e739bc3104c709d4fd57c0769975b1cf1`, 2 957 octets) ; synthèse servie v5 (`f74c606423bbbc4da88578508209d3d87cb133b4b7cd8e1728606cde58484e73`, 32 260 octets, 286 lignes ; **non lue**, seules sa taille et son empreinte servent) ; note de périmètre v3 (`dd6fea0e176b019c46386d0d000d059085036d2b20a82fe59c26549b41380580`) ; `registres/go.md` (`7799734e…`, lignes -33, -34, -42, -44, -46, -50, -51, -52 lues) ; `registres/decisions.md` (`46cf019b…`, R-4206 à R-4260 lues).

Sur la branche de travail, empreintes recalculées sur disque : contre-lecture de la question v5 (`b1a67976…`) ; contre-lecture de la partie servie (`c0f4540e…`) ; journal et programme de dérivation (`944188dc…`, `d22e6f55…`, non lus) ; ordre de course v3 (`b12cdc1292178d4c7fe80370439507efd1d04d07f47d0bc6315b8c429d329e22`) ; programme du devis v3 (`a50c9983…`) ; reste net comptable (`62c625ab610992024383b82547975dea36458b9e9634b5d7c889cd5b586919fd`) ; outil (`391db990734dd36f7c827b8b6c77dc0de1bda324f671b65748ccfe68c56a53d6`) ; validateur `valider_prereg_v4_v1.py`.

## 2. La v7, point par point

Remplacements : `remplacements-preenregistrement-court-v6-vers-v7-v1.json` ; journal de l'outil à côté de la v7. Rang du remplacement entre crochets.

| point du mandat | ce que la v7 porte | remplacements |
|---|---|---|
| 1. Pièces servies | la question v5 n'est plus servie par son fichier ; partie servie (gabarit `4cd360ba…`) ; règle « aucun programme n'ouvre la question pour la servir », avec épreuve ; ligne de case (identifiant neutre, trois valeurs à l'octet de la légende, contraintes, épreuve) ; requête assemblée journalisée (taille, empreinte) ; synthèse servie v5 à la place de la v2b | [10], [11], [15] |
| 2. Racine | valeur écrite gardée, `0x2cf2aae035beef43e999e3cd8b0fb7ba` ; dite « de la question v3 », non recalculée ; aucun tirage ne change | [21] |
| 3. Arrêts | n° 14 étendu à toute pièce fixe servie, à la liste des motifs, au programme de la garde, à la configuration, avec épreuve ; n° 16 neuf, « motif interdit dans un texte à servir » (dernier point avant l'envoi, deux familles gelées par empreinte, normalisation, témoin positif par motif, refus nommé sans retrait silencieux, épreuve par famille, course, sondes et épreuve des témoins, liste jamais servie) | [28], [29] |
| 4. GO-2026-11-20-46 | point 3, le portier (lecture au § 4, point 2) ; point 4, registre servi sans procédé ; point 5, session à part ; point 6, quarantaine ; point 9, définition du mode, qui vit à côté | [12], [13], [14], [15], [22], [25], [30] |
| 5. GO-2026-11-20-50 | table des six garde-fous, cités à la lettre, chacun avec son arrêt (n° 17 à n° 23) et son épreuve sur cas sain et artefact ; ce qu'ils ne font pas, dit | [15], [29] |
| 6. R-4250, R-4260 | quatre classes d'issue d'appel, dont « réponse vide motivée » ; mesure M6 ; deux témoins plantés de plus (« variante d'une famille connue », « réponse vide motivée »), issues attendues ; case « autre, à nommer » : supposition reçue dans `idee`, mesure M7 | [15], [16], [24], [27], [32] |
| 7. Épreuve 4 | deux branches, « avec » et « sans », marquées « en attente du mot de Lazar », sans trancher ; ligne de critères propre à la branche « avec » | [23], [24] |
| 8. Sondes de refus | elles portent la partie servie remplie, seule ; case de la sonde ; pire de la sonde de l'espèce 6 recalculé : 3 205 octets au plus, 0,00641 USD d'entrée à un jeton par octet, 359 jetons de sortie au plus sous 0,01 USD | [17], [18], [19], [26] |
| 9. Ordre de course | paragraphe « Lecture de l'ordre de course » ; erratum d'une ligne à écrire par la mère (texte au § 5 ci-dessous) | [15], [34] |
| 10. Tenue | titre, date, statut, phrase de version, table des pièces, « La question », « Ce que ce texte ne contient pas », reste à écrire, contre-lecture | [1] à [9], [20], [31], [33], [34], [35] |

**Textes neufs déclarés** (tout le reste est tenue ou renvoi) : dans [15], les paragraphes « Lecture de ce texte depuis la v7 », « Pièces servies (v7) », « Ligne de case », « Requête assemblée », « Session à part et quarantaine », « Le portier », « Définition du mode », « Réponse vide motivée », « Témoins plantés de la v7 », « Case « autre, à nommer » », « Réserve de lecture sur la question v5 », « Garde-fous », « Lecture de l'ordre de course » ; dans [16], M6 et M7 ; dans [20], cinq valeurs ouvertes ; dans [23], « L'épreuve 4 » ; dans [29], les arrêts n° 16 à n° 23 ; dans [34], les points 12 à 16.

**Procédé de lecture globale.** Plutôt que de récrire chaque « relecture de la mère », « question scellée » et « devis v3 » de la v6, le paragraphe « Lecture de ce texte depuis la v7 » dit comment ils se lisent (comme la correction C1 de la v6 l'a fait pour « devis v3 »). Le contre-lecteur dira si un passage non récrit reste faux malgré cette clause.

## 3. Le devis v5

`devis-course-nouvelles-attaques-v5.md`, par `remplacements-devis-v4-vers-v5-v1.json` ; programme `calcul_devis_course_nouvelles_attaques_v4.py` (`7dff52cd739a5ab9c54ad91c737dce9f1edf9d3fbc416f1db0ade0088eaaedef`), sortie `calcul-devis-course-nouvelles-attaques-v4.json` (`aabdec424100bcf48d05bed8676eca7a2b783763554b60bf3615b2c1fdf84d46`), jouée deux fois, `cmp` muet (le second lancement est gardé). `diff` avec la sortie v3 : le libellé de la pièce et les deux champs neufs, rien d'autre.

- **Ligne demandée : 570 USD exactement. Plafond total : 576,01 USD** (variante de la sonde de l'espèce 6 à 0,05 USD : 576,05, non accordée). Attendu 262,23 ; cas haut 548,66.
- **Tailles réelles** : partie servie remplie au plus 3 205 octets (ligne de case bornée à 256, valeur du rédacteur ; forme d'essai : 142 au plus) ; synthèse 32 260 ; requête d'un proposeur à la première génération au plus 35 465 octets, hors registre et enveloppe. L'unité (course v9) n'est pas refaite.
- **Parts par clé, face aux restes estimés** :

| clé | bas | haut | reste estimé | ce qui tient |
|---|---|---|---|---|
| Minuit | 24,70 | 126,06 | 162,56 | bas et haut tiennent ; pire non (arrêt n° 12) |
| Luc | 69,26 | 136,63 | 214,00 | bas et haut tiennent ; pire non |
| Rigaud, moins 8,35 | 22,29 | 26,61 | 39,15 à 55,86, ou −5,85 à 10,86 si ses lots vont à 45 | tient si les lots sont à zéro ; sinon manque 11,43 à 28,14 au bas |
| deuxième relais | 95,35 | 147,77 | inconnu | indécidable |
| troisième relais | 14,25 | 17,01 | 8,91 à 11,51 | **ne tient pas au bas** : manque 2,74 à 5,34 |
| clé de l'espèce 6, sonde comprise | 35,20 | 88,56 | 32,24 | **ne tient pas au bas** : manque 2,96 |

Trois manières de fixer les parts de ces deux clés sont écrites avec leur prix (recharge jusqu'au pire ; recharge jusqu'au cas haut et part au reste relu ; aucune recharge), sans trancher.

## 4. Points non tranchés

1. **L'épreuve 4** : « avec » ou « sans » ; et, si « avec », la seule quatrième épreuve ou les quatre (j'ai écrit la branche « avec » sur les quatre, et je dis ce qui tombe si son mot ne retient que la quatrième).
2. **Le portier (GO-2026-11-20-46, point 3).** La recommandation retenue est conditionnelle (« si le procédé est permis ») ; la question v5 et la partie servie scellées gardent « niveau de l'idée » et le coffre. J'ai écrit : dans cette course le portier garde sa garde « concret » ; tout ce qui n'est pas au coffre va en quarantaine stricte ; l'antériorité trie après. C'est aussi la lecture de la contre-lecture de la question v5 (§ 5, observation 2). L'autre lecture demanderait des versions neuves de la question, de la partie servie et de plusieurs arrêts. À confirmer par la mère et le directeur.
3. **« Aucune carte de cette course ne nourrit le mode tenu à l'écart »** : la v6 la tirait de ce que la mère lisait tout ; la mère ne lit plus. Je l'ai gardée ; la lever est une décision du directeur.
4. **La sonde de l'espèce 6** : 0,01 USD avec 359 jetons de sortie, ou 0,05 USD. Et si la sonde devait porter aussi la synthèse servie (ce que le mandat ne dit pas), l'entrée seule vaudrait 0,0709 USD.
5. **La case de la sonde** : j'ai pris la première case de la réserve, dans l'ordre canonique (aucun tirage neuf ; une case de réserve consommée). Valeur du rédacteur.
6. **L'identifiant neutre** : contraintes gelées, construction ouverte ; si elle demande un tirage, c'est une clé de tirage neuve.
7. **Les parts des clés** de l'espèce 6, du troisième relais, de Rigaud et du deuxième relais (§ 3).
8. **La question v5, § 7 et § 3**, et l'ordre de course, § 10, disent encore « après la revue de sécurité externe » : ces sections ne sont pas servies, mais elles contredisent GO-2026-11-20-46, point 8, et GO-2026-11-20-50 pour la mesure interne. La v7 prime par sa clause ; un erratum à la question est à décider.
9. **Qui** : la session à part ; qui écrit la liste de référence ; le lecteur du garde-fou 5 ; la liste nominative.
10. **« Refus du modèle » en course** : R-4250 ne nomme que la réponse vide motivée. Pour qu'elle soit distincte, j'ai nommé aussi « refus du modèle » et « réponse illisible », comptés, non relancés, sans arrêt. La v6 n'avait pas de règle pour un refus en course hors classifieur.
11. **La garde de motifs sur le registre servi** : un énoncé de fiche qui porte un motif arrête la génération suivante ; le taux de faux refus est à mesurer à l'essai à blanc.
12. **La table des pièces** : le devis v5 n'y est pas (non scellé : blanc à remplir par la mère) ; le journal et le programme de dérivation et les deux contre-lectures y sont cités à leur chemin de la branche de travail, empreintes vérifiées sur disque, sans que j'aie vérifié qu'ils sont sur `main`.

## 5. L'erratum d'une ligne à l'ordre de course v3 (texte exact, non écrit comme pièce)

> Erratum 1 à l'ordre de course v3 (`b12cdc1292178d4c7fe80370439507efd1d04d07f47d0bc6315b8c429d329e22`), sans autre changement : dans ce texte, « la question » et « la question scellée » renvoient à la question v5 (`eaf5db8a558547aa8f5df45008a34eebf4cb7a163e12ca400176401de6f5ce0f`), servie par sa seule partie servie (`4cd360baea1076ec2b19b2c7ba85675e739bc3104c709d4fd57c0769975b1cf1`) ; la pièce d'antériorité servie est la synthèse servie v5 (`f74c606423bbbc4da88578508209d3d87cb133b4b7cd8e1728606cde58484e73`) ; la composition est à six espèces (GO-2026-11-20-33), l'aiguilleur et les deux juges inchangés ; et là où cet ordre diffère du préenregistrement court v7 (§ 3, § 4, § 5, § 7, § 9, § 10 et § 11 : pièces servies, relecture et lecture par une session à part, quarantaine, garde-fous de GO-2026-11-20-50 en place de la revue externe pour la mesure interne, arrêts), le préenregistrement court v7 prime.

## 6. Écarts

1. **Compte des ancres.** Le mandat veut chaque ancre comptée par `grep -c -F -e`. Les ancres portent des fins de ligne et `grep -c` compte des lignes : je m'en suis remis à l'outil, dont la règle (2) exige exactement une occurrence de chaque texte ancien et dont le journal écrit le compte de chaque texte neuf. Un seul `grep -c -F` de contrôle, sur quatre marques de la v7 : 7 lignes.
2. **Chemins.** Les noms de plusieurs pièces n'étaient pas au mandat ; sans commande de liste, je les ai déduits des pièces lues. Quatre essais ont échoué sur un chemin absent (deux `git show`, deux lectures), sans effet.
3. **Une commande de contrôle mal formée** (recherche d'espaces insécables) a rendu un compte sans valeur ; refaite à l'octet : aucune espace insécable ni apostrophe courbe dans les deux sources.
4. **Copies de travail** des sources dans mon dossier, préfixe `src-`, sans compagnon : ce ne sont pas des pièces rendues.
5. **Non lus** : la synthèse servie (taille et empreinte seulement), le journal et le programme de dérivation, la question v4, les avis sur la partie à servir, les lignes GO-2026-11-20-45 et -49 (connues par les décisions).
6. Le validateur est joué tel quel, non par une copie renommée.

## 7. Fichiers rendus

Dossier : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/redacteur-preenregistrement-court-v7/`. Chacun a son compagnon `.sha256`.

- `preenregistrement-court-course-nouvelles-attaques-v7.md` (`1837a6850269d925e75744828f44c4437e0c7894595218bce3358ccfdeac551d`) et son journal de remplacements
- `remplacements-preenregistrement-court-v6-vers-v7-v1.json`
- `differentiel-preenregistrement-court-v6-v7-v1.diff`
- `sortie-validateur-preenregistrement-court-v7-v1.txt`
- `devis-course-nouvelles-attaques-v5.md` (`41a09f77be48d33b0847888cdd4cf251c5c4fa511d47d69981e27b7d3f0fa22a`) et son journal de remplacements
- `remplacements-devis-v4-vers-v5-v1.json`
- `differentiel-devis-v4-v5-v1.diff`
- `calcul_devis_course_nouvelles_attaques_v4.py` ; `calcul-devis-course-nouvelles-attaques-v4.json` ; `calcul-devis-course-nouvelles-attaques-v4-second-lancement.json`
- `rapport-redacteur-preenregistrement-court-v7-devis-v5-v1.md` (cette pièce)

— rédacteur neuf, modèle F

# Vérification des différences — préenregistrement de la course du banc fermé, brouillon 10 — v1

- **Pièce vérifiée** : `prereg/course-banc-ferme-v1-brouillon10.md`, branche `claude/prereg-course-banc-ferme-v1`, commit `712a227064a2d25cddfbf438c03e895c0cb4dd0b`. Empreinte recalculée : `85f23d61488c2ee154b1f3af7ad5ab990f56ba3fe1daa7d731e84087beb690b6`, égale à son `.sha256` compagnon.
- **Contre-lectrice** : la même, `session_01Qi7Gr5LQA3YbKmpEK7DG2D` (Opus 5.5). Pièce de classe A, règle R2.
- **Date** : 21 novembre 2026, vers 20:05 UTC. Refus d'un classifieur : aucun.
- **Objet** : les différences du brouillon 9 avec le brouillon 8 (déjà vérifiées, `cd5bb1e7…`), puis celles du brouillon 10 avec le brouillon 9, par `diff`, lues sur les passages touchés.
- **Pièce de sécurité v13** (`dca22e30…`, commit `0873dd67`) : comparée par `diff` à la v11. Son verdict « accepté » a été lu (`verification-des-corrections-v12.md`, `74ec125b…`, commit `0bbe4758`).
- **Liste d'arrêt** : la section 4.2 de la v13 est identique à celle de la v11, et le brouillon 10 la reprend telle quelle. C'est vérifié par programme.
- **Validateur** : il ne rend que le marqueur du champ n° 19, ce qui est attendu.

## Mes restes du brouillon 9

| Reste | Constat | État |
|---|---|---|
| R1, ordre des scellements | Réserve 16, en quatre temps, avec le `diff` consigné au troisième temps. | levé |
| R2, comparaison après le retour | Sans objet sous la v13 : les questions sont de nouveau fermées, une par contrôle ; les lecteurs y répondent et aucune comparaison libre ne suit. | sans objet |
| R3, « la v10 » | Corrigé à deux endroits. | levé |
| M2 du brouillon 8, onzième question | Portée dans les termes de la règle neuve. | levé |

## Regard dur

**a. Le résumé de la règle des questions (D6) contre la v13.** Il reprend ses six éléments un à un et n'est **pas plus lâche** :
- le gabarit unique scellé ;
- les listes par tâche, tirées de la tâche et de la référence seules, exhaustives et dans l'ordre, sans rien choisir d'après la consigne, le lot, la famille ou le mode ;
- le même jeu pour les deux jumeaux, au caractère près ;
- l'envoyeur réduit à la tâche de chaque produit ;
- la table de correspondance qui ne quitte pas le lot ;
- le contrôle des paires attesté par empreinte, et la garde 15 qui lit les questions.

Les artefacts neufs de la garde 14 sont repris à la condition 4, et ce que la règle laisse sortir et deviner est dit. **Une phrase est reprise sans précaution** : « matière de tâche et non du coffre ». Pour le mode connu, c'est vrai, puisque la référence vient du banc du programme. Pour la famille aveugle, l'auteur n'en sait rien, et ce texte non plus (M1).

**b. La onzième question de l'assembleur et l'attestation d'exhaustivité du monteur.** Elles ne se gênent pas et se complètent.
- L'assembleur dit, à l'addendum A, avant la construction des gardes, si l'oracle **peut** se ramener au gabarit.
- Le monteur atteste, à l'addendum O, que les listes **écrites** sont exhaustives.
- Un « oui » de l'un et un empêchement de l'autre valent un nœud. Le dire en une phrase.

**c.** Voir la vérification du brouillon 5 de la répétition, point c.

**d. Le renvoi croisé.** Il se ferme bien au définitif par le champ R-1 de la répétition, sous l'ordre de la réserve 16. Une précision (M3).

## Restes mineurs

**M1 — Les paramètres de la famille : matière de tâche, ou du coffre ?** La v13 laisse sortir « les contrôles de la référence d'une tâche, matière de tâche et non du coffre ». Pour la famille aveugle, la référence cachée peut venir de ses pièces, notamment de la pièce 3, qui est au coffre. Ajouter à l'attestation du monteur, à l'addendum O, une phrase sans contenu : les paramètres viennent de la tâche et d'une référence qui n'est **pas** tirée des pièces 2 et 3 de la famille. À défaut, des paramètres tirés du coffre partiraient par la voie : rien ne part, et c'est un nœud qui touche la pièce de sécurité.

**M2 — Exhaustivité contre fuite de consigne.** La garde 15 lit les questions. Si la part propre d'une consigne de la famille nomme un contrôle de la référence, la question qui porte ce contrôle est retenue. Le jeu de la tâche devient alors incomplet, et la garde 14 l'arrête. Rien ne part pour cette tâche, et sans doute pour d'autres. Ajouter à l'attestation de l'assembleur une douzième question, sans contenu : « la part propre des consignes reprend-elle des mots des contrôles de la référence ? » Un « oui » donne un nœud avant la construction des gardes de l'envoi. La répétition générale mesure ce risque sur le mode connu (sa vérification, point c).

**M3 — Le troisième temps de l'ordre des scellements.** Quand la répétition est scellée avec, au champ R-1, l'empreinte de la course définitive, elle incorpore par renvoi un texte que sa contre-lectrice n'a vu qu'en brouillon. Ajouter à la réserve 16 : au troisième temps, une relecture courte des seuls passages de la course que la répétition emploie, entre le dernier brouillon vérifié et la version définitive, par la même contre-lectrice, consignée.

**Plus une phrase en D6**, pour le point b : un « oui » de l'assembleur à la onzième question et une attestation impossible du monteur valent un nœud.

## Verdict

**Accepté.** Les restes du brouillon 9 sont levés ou sans objet. Les différences du brouillon 10 sont fidèles à la v13, et la liste d'arrêt lui est identique. Trois restes mineurs, M1 à M3, et la phrase du point b sont à porter avant le scellement définitif.

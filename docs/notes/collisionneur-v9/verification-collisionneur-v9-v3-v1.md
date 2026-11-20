# Vérification des corrections du collisionneur v9, version 3

Écrite le 20 novembre 2026 par le même contre-lecteur (Claude Fable 5.2, `claude-fable-5-2`) que `contre-lecture-collisionneur-v9-v3-v1.md` (`9a9f0871b5b99c90371754b1afa42ff29f5a6b5915457483a3f6ca7328687fab`). Une passe, courte, sur les seules corrections C1 à C5. Aucun appel à un fournisseur, aucune valeur de clé lue ni affichée, aucune dépense, aucun commit, aucun autre fichier du dépôt modifié. Le run réel est inchangé (empreinte de tous ses fichiers égale avant et après).

**Verdict : conforme, à lancer.**

## Pièces vérifiées, empreintes recalculées et égales aux compagnons

| fichier | empreinte |
|---|---|
| `commande-reprise-collisionneur-dopamine-v3-v2.txt` | `6a9431f2d50e310e3273e48c3cdadfcbd6228ec3053997ed86f0390836ef3ada` |
| `test_collisionneur_v9_v3_complement_1.py` | `58ddaa24acd62b7ce638cbfa058ce53d2423a4640c03b5b6aea2f137b4824534` |
| `rapport-developpeur-collisionneur-v9-v3-erratum-1.md` | `58e2c507a9068bc0510068479103e22a9cad311660ad7c2f00a40bb254505836` |
| `collisionneur_v9_v3.py`, inchangé | `850df311807384fc66c44f6a6b90d3c8a9a3288d2b88a2b74312f9a78c4d4910` |
| `test_collisionneur_v9_v3.py`, inchangé | `8c38dc2f938db3386f84721830b179d844295a1f46e6db8ba3586ffbe2eabfdc` |

## Constats

1. **C1, C2, C3 portées à la lettre.** La différence entre la commande v1 et la v2 ne contient que mes trois couples : le nom `RR_ANTHROPIC_API_KEY_RIGAUD` (variable présente, contrôlée par son nom seul) et son commentaire de tête, le contrôle d'empreinte par `controle_ia.scellement verifier`, et la règle « ne pas relancer l'étape 3 après un code 4 tombé sur une relance ». La v1 est gardée.
2. **Commande v2 rejouée à blanc, ligne par ligne.**
   - Contrôle d'empreinte, depuis la racine : `OK 850df3118073…`, code 0.
   - Étape 1, sur le run réel, en lecture seule : « Plafond de Fable retenu : 49000 (table du script : 49000) », 25,7746 USD, code 0.
   - Étape 2, sur une copie du run (pour ne pas régénérer `etat.md` dans le dépôt) : « Vérification : tout tient », code 0.
   - Étape 3, **sans envoi** : ses arguments lus dans le fichier de commande, le dossier remplacé par la copie, des doublures par adresse, une valeur de clé fictive. Code 0, 10 comptages, 10 envois simulés, aucun au tour 1, essai 2 de la cellule arrêtée à 49 000, ligne ouverte à 25,90 USD.
   - Étape 4, sur la copie : « Vérification : tout tient », code 0.
3. **C4 : complément repris à l'octet** (empreinte égale à l'attendue). Rejoué : complément seul, **6 passés** ; suite v3 et complément ensemble, **157 passés** ; essais v2 sur la v2, **117 passés**.
4. **Mes quatre retraits, rejoués avec le complément du dépôt** (fichiers comparés à l'octet). Chacun est maintenant pris :

| retrait | essais du complément en échec |
|---|---|
| comptage d'OpenAI envoyé à une adresse tierce | 3 |
| changement de script déclaré depuis une autre empreinte, admis | 1 |
| ligne non contrôlée à la relance | 1 |
| plafond non contrôlé à la relance | 1 |

5. **L'écart signalé par le développeur (2 échecs au lieu de 3) s'explique et ne change rien.** Ma mutation du premier retrait force aussi l'indicateur de boucle locale à faux, ce qui casse en plus l'essai sain ; la sienne le garde. Dans les deux formes, les deux artefacts « adresse tierce » échouent : le trou est fermé.
6. **C5.** L'erratum 1 corrige la phrase périmée ; le rapport d'origine n'est pas réécrit.
7. **Espace de travail d'Anthropic.** La mère dit que le lancement de 12:24Z ne donnait pas `--nom-espace-anthropic` et que les cellules d'Anthropic du tour 1 ont répondu. La commande v2 ne le donne pas : c'est cohérent, et je n'ai rien à y redire.

## Réserves qui restent, déjà écrites dans la contre-lecture

- Le crédit de la clé Rigaud est à relire avant l'étape 3 : part d'Anthropic de 10,32 USD au pire.
- Les trois interfaces de comptage n'ont jamais été appelées pour de vrai ; un échec donne un code 8, sans envoi.
- Le changement du script proposé en C3 n'est pas appliqué ; la règle de la commande le remplace pour cette reprise.
- La tolérance de 1 % plus 32 jetons est un écart à la lettre de « compter exactement », à dire à Lazar.
- Opus peut être coupé à 22 000 jetons ; sa relance part si la ligne le permet.

## Limites

Aucun appel réel. L'étape 3 n'est vue que par simulation, sur une copie. Mes programmes sont dans mon bloc-notes, qui n'est pas durable.

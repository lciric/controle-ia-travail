# Note de changements — brouillon 27 du texte neuf du bras A des organismes discrets — v1

**Rédigé par Claude Fable 5.2 (`claude-fable-5-2`)**, le même agent que pour les brouillons 21 à 26.

- **Brouillon** : `prereg/T0.7-organismes-discrets-v-a-v2-brouillon27.md`, `428f9e553e9c4b06cdfad2377aaa238d515e6b33716ca080cabcc4a44f87e398` (2 067 lignes). Les brouillons 20 à 26 ne sont pas modifiés.
- **Fiches pour Lazar : aucun fichier neuf.** Celles du brouillon 23 restent en vigueur (`f20abfed…`).
- **Source** : la vérification du brouillon 26 (`fa988381872c2b9089dc19c1718a73a27a697f23d6782f90ef19c89da8bd25dd`), lue en entier. Verdict : engageable après corrections, sans fiche neuve ; un défaut à corriger, trois mineurs.
- **Méthode** : copie du brouillon 26 par `cp`, puis 22 remplacements exacts, chacun vérifié unique par programme.
- **Registre des accords** : relu sur la branche principale distante au commit `5adfc241` ; aucune ligne de plus.
- **Heures (UTC, `date -u`)** : début 18:06:42Z le 2026-11-19 ; brouillon scellé à 18:08:07Z.
- **Interdits tenus** : aucune empreinte de fichier d'un dossier du côté habilité ; aucun interne de moniteur ; aucun code ouvert ; aucune clé ; aucun appel de modèle ; seul appel réseau, `git fetch` de la branche principale ; ni `registres/`, ni `.claude/`, ni le journal touchés ; rien committé ; aucun fichier existant écrasé ; aucun sous-agent.

## Contrôles par programme

| contrôle | résultat |
|---|---|
| section 12 ; « Critères de lecture gelés » en entier (7.1 à 7.8) ; section 10 | identiques, caractère pour caractère, au brouillon 26 |
| titres (53) | les 52 titres de niveau 2 et 3 sont identiques |
| consignes figées (3.2 et 3.3) | égales octet pour octet à celles du brouillon 20 ; `98a9bd34…` et `ecf590ea…` recalculées |
| citations à la lettre | brouillon 20 : 935 sur 935 ; brouillon 26 : 1 161 sur 1 161 |
| table d'en-tête, sans les fichiers cloisonnés | 147 lignes à empreinte : 133 recalculées et égales, 0 différente, 14 sautées et non ouvertes, à l'empreinte héritée non vérifiée |
| marque des cases non remplies | huit lignes, toutes en 13.1 |
| validateur (`problemes()`) | les deux problèmes attendus |
| différence avec le brouillon 26 | 13 lignes de plus ; 18 lignes changées |

## 1. Les quatre ajouts

| défaut | ce que le texte dit maintenant | où |
|---|---|---|
| C-1 constat de lancement | fait par un programme nommé, `scripts/constat_de_lancement_discretion_bras_a_v1.py` ; il rend un fichier scellé, `constat-de-lancement-bras-a.json`, à six champs, rangé dans le dossier de la livraison et cité au manifeste ; le programme d'analyse ne part que sur un constat sain ; cas sain, artefacts, et ce qui suit chaque refus | conventions ; 8.4 ; 13.2 |
| M-1 valeurs p | demandées au module à pleine précision (demande 13) ; toute valeur ajustée rapportée est calculée sur les valeurs rendues | 6.9 ; 13.1 |
| M-2 rejeu après une panne | il vaut par étape : après le fichier scellé de l'étape (m), une panne pendant l'étape (n) fait rejouer la seule étape (n) | 6.9 ; 8.4 |
| M-3 `effectifs`, `exclues` | comptes du côté habilité, non des sorties de moniteur ; rapportés tels quels, comme les aires de l'agrégateur ; la phrase « aucun score, aucun texte » dit ce que le côté habilité s'engage à rendre et ce que l'analyse lit pour une règle | 6.9 |

**Ce qui suit un refus du constat de lancement**, tel que le texte l'écrit :
- configuration absente du registre courant : elle y est inscrite, et le constat est refait ;
- constat absent : il est fait ;
- révocation entrée : la lecture ne part pas sous cette ligne ; il faut une ligne de GO neuve, donc un autre mot de Lazar, et une configuration neuve scellée sur le nouvel état du registre.

Dans les trois cas, rien n'a été lu de la livraison : ce n'est pas un arrêt de la lecture de la discrétion, et aucune issue du point 21 ne s'applique.

## 2. Ce que le code doit porter

Les parties 3 des notes des brouillons 25 et 26 tiennent. S'y ajoutent :

1. **Un programme neuf**, `scripts/constat_de_lancement_discretion_bras_a_v1.py`. Entrées : la configuration scellée de la livraison ; la pièce de l'état figé du registre, ou rien quand `sha256_du_registre_des_accords` est `null` ; le registre courant de la branche principale et son commit, donnés par la session qui lance. Sortie : `constat-de-lancement-bras-a.json`, scellé, dans `livraison-<rang>/`, à six champs et eux seuls — `date_utc`, `sha256_de_la_configuration`, `sha256_du_registre_fige`, `commit_du_registre_courant`, `configuration_inscrite`, `revocation_entree`.
   - `configuration_inscrite` est vrai quand l'empreinte entière de la configuration se lit dans le registre courant.
   - `revocation_entree` est vrai quand une ligne du registre courant, absente de l'état figé, révoque la ligne de GO que la lecture emploie. Pour une première livraison, sans ligne de GO à lire, il est faux.
   - Le programme vérifie que la pièce de l'état figé a bien l'empreinte que la configuration inscrit.
   - Il s'écrit sans reste, comme les autres fichiers scellés de l'analyse.
2. **Le programme d'analyse exige le constat** avant toute lecture : fichier présent dans le dossier de la livraison, scellé, `sha256_de_la_configuration` égal à l'empreinte de la configuration lue, `configuration_inscrite` vrai, `revocation_entree` faux. Sinon : garde ordinaire, sans événement d'arrêt ni issue.
3. **Essais du constat** (ligne neuve de 8.4) : cas sain ; révocation entrée après l'état figé ; empreinte de la configuration absente du registre courant ; constat absent, non scellé, ou d'une autre configuration ; première livraison sans ligne de GO.
4. **Rejeu par étape** : après une panne, le programme regarde étape par étape. Étape (m) : rejouée si ni fichier de l'étape (m) ni fichier d'arrêt n'existe pour la livraison. Étape (n) : rejouée seule si le fichier de l'étape (m) est scellé et qu'aucune grandeur de l'étape (n) ni aucun fichier d'arrêt de cette étape n'est écrit. L'étape (m) n'est jamais rejouée une fois son fichier scellé. Essai : panne simulée pendant l'étape (n).
5. **Valeurs ajustées** : calculées sur les valeurs rendues, non sur les formules. C'est déjà ce que fait un code qui « prend la valeur telle quelle » ; un essai le fixe.
6. **`effectifs`, `exclues`, aires de l'agrégateur** : rien à changer ; rapportés tels quels.

## 3. Demande à la session principale, en plus des précédentes

La demande 13 de 13.1 est complétée : que le module rende ses valeurs p à pleine précision, sous l'écriture décimale la plus courte du nombre, ou en fraction. Sous un arrondi à quatre décimales, la condition (β) refuserait quelques valeurs p basses honnêtes autour de 0,05 (cinq cas mesurés par le vérificateur) ; à pleine précision, aucune.

## 4. Réserves

1. **Le nom du programme, le nom de son fichier et ses six champs sont de moi.** Le rédacteur du code peut avoir besoin d'un champ de plus ; qu'il me le dise, le texte le portera.
2. **Le programme d'analyse ne peut pas vérifier que le constat dit vrai** : il est sans réseau. Il vérifie qu'un constat sain existe pour sa configuration. Ce que le constat affirme tient au programme du constat et à la session qui le lance ; le texte le dit.
3. **« Révoque la ligne de GO » suppose une forme de ligne de révocation au registre**, que le code de la version 7 reconnaît déjà (type « révocation » qui nomme la ligne). Je ne l'ai pas relue dans le code.
4. **Je n'ai toujours pas relu le texte en entier.**

## 5. Fichiers ouverts pour ce brouillon

- `docs/notes/relance-organismes-discrets-v1/verification-brouillon26-bras-a-v1.md`, en entier.
- `prereg/T0.7-organismes-discrets-v-a-v2-brouillon26.md` : par programme, le fichier entier pour les contrôles ; aucun passage neuf lu.
- `registres/go.md` de la branche principale distante, par `git show`, après la ligne 511.
- Par programme, pour leur seule empreinte : les 133 fichiers de la table d'en-tête hors des dossiers cloisonnés.
- Rien d'autre.

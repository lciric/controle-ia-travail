# Vérification du contrôle de sortie v1 — `controler-et-creer-essai-3-v1.py` (`8d88b263…`, empreinte relue : identique)

**Verdict : Conforme avec réserves.** 165 cas joués, 0 écart, 0 défaut sur la question posée. Chaque contrôle est vu rouge sur un artefact (bon code, zéro requête au serveur factice) et vert sur le cas sain ; le corps reçu est égal au corps recalculé de façon indépendante et porte les octets lus. Quatre réserves (section 3), aucune ne casse une revendication écrite.

## 1. Lecture de l'outil (point 1)
- Un seul `open(chemin, "rb")` sur les données (l. 166) ; les autres `open` écrivent le relevé (`"x"`) ou créent le fichier `lu` du banc. La tarfile est lue en mémoire. Le corps ne vient que de `texte`, issu des octets lus.
- Couverture de la partie en clair : ligne 1 + lignes 5 à marqueur-1 sont dans l'empreinte d'amorce ; lignes 2, 3 et 4 sont chacune contraintes (expression régulière entière, expression régulière entière, égalité exacte) ; le marqueur est exact et unique ; il y a une ligne exactement après lui (la charge, validée par `b64decode(validate=True)`) ; le texte finit par un seul saut de ligne. Aucune ligne n'échappe. Un ajout n'importe où dans la partie en clair est refusé (cas A-*).

## 2. Table des cas (table complète : `tables/table-des-cas.tsv`, 165 lignes ; relevés : `travail/rel/`)
Chaque artefact est joué en `--envoyer` (banc, serveur factice) et en `--a-blanc`. « 0 req » = aucune ligne ajoutée au journal du serveur.

| Cas | Attendu | Rendu |
|---|---|---|
| T-sain ; T-recompression-identique-contenus (tar refait, octets différents, contenus égaux) | 0 ; 1 requête (envoyer) / 0 (à blanc) | conforme |
| A-amorce modifiée (espace ligne 5, mot final, ligne 1) | 12, 0 req | conforme |
| A-ajout d'une ligne en clair (index 4, commentaire, avant marqueur, entre marqueur et charge, après charge, ligne vide finale) | 12, 0 req | conforme |
| A-ajout avant H0 (décale les numéros) ; suffixe sur ligne E_SCRIPT ; ligne 4 supprimée ; E_SCRIPT déplacé | 11, 0 req | conforme |
| A-suffixe sur H0 ; suffixe sur jeton ; `export E_SCRIPT=` dans l'amorce ; tabulation en clair ; sans saut final ; fichier vide ; jeton trop court | 12, 0 req | conforme |
| A-H0 absurde mais bien formé (9999-99-99T99:99:99Z) | 0 (non contrôlé, voir réserve 4) | 0 |
| E-deux `E_SCRIPT=` (autre valeur, valeur identique), `E_SCRIPT+=`, indenté, tabulation, valeur de la ligne 4 changée | 11, 0 req | conforme |
| C-script / gardien modifié dans la charge, membre en trop, manquant, lien symbolique, répertoire, membre répété (même nom, contenu autre), base64 invalide, espace en fin de charge, gzip sans tar, charge vide, noms préfixés `./` | 14, 0 req | conforme |
| S-membre aléatoire de 40 Ko | 13, 0 req | conforme |
| S-frontière : JSON = 32 768 ; JSON = 32 772 (pas de 4 : base64) | 0 ; 13 | conforme |
| N-non ASCII (amorce, charge), CR, NUL, 0x7f, 0x1b, CRLF partout | 10, 0 req | conforme |
| F-fichier absent ; relevé existant | 3 ; 2 sans écrasement | conforme |
| B-envoi sain : corps reçu = `json.dumps` recalculé par moi (octets égaux), `user_data` = octets lus, huit clés exactes, en-tête `Authorization` = `Bearer ` + jeton factice (hash) | égaux | conforme |
| B-relevé : pas de clé `"root_password"`, ni valeurs imbriquées (liste, action), ni écho de `user_data`, ni jeton de démarrage ; réponse 403 : code 21, relevé expurgé | conforme | conforme |
| J-jeton absent / vide / court / signe hors classe | 20, 0 req | conforme |
| G-banc : nom `HCLOUD_TOKEN` | 2, 0 req | conforme |
| R-remplacement après lecture : sain puis (autre / supprimé / vide) ; mauvais puis sain | 0, corps = octets lus ; 12, 0 req | conforme (4/4) |
| H-hors banc : `--adresse` (locale, Hetzner exacte, avec `/`), `--nom-jeton`, `--pause-apres-lecture`, `--adresse=…` | 2, 0 req | conforme |
| H-`CONTROLE_BANC` = vide, OUI, Oui, `oui `, ` oui`, 1, true, ou, non, `oui\n`, ouioui, off | 2, 0 req | conforme (12/12) ; `oui` exact : 0, 1 req |
| H-banc, adresses : localhost, https local, `127.0.0.1.nip.io`, `@evil`, sans chemin, `\n` final, 127.0.0.2, `[::1]`, 0.0.0.0, Hetzner avec `/`, `?x`, majuscules, `http://api…`, `…cloud.evil.example`, `file://`, espace, `?a=b` | 2, 0 req | conforme (17/17) ; `127.0.0.1:10/` admis, port clos : 21 |
| P-`ps` (guetteur 20 ms, 385 relevés) : ligne portant l'un des jetons factices | 0 | 0 |
| P-jeton d'interface factice dans un fichier ou une sortie ; jeton de démarrage dans un relevé ou une sortie | aucun | aucun |
| M-observations (mandataire, voir réserves) | — | observation |

## 3. Réserves (trois lignes au plus chacune)
1. **Redirection** : `urllib` suit un 302 et renvoie l'en-tête `Authorization` à la cible (observé : `POST /redir` puis `GET /cible`, même hash de jeton). Sans effet au banc ; pour la vraie adresse, il faudrait que Hetzner redirige. Remède possible : refuser toute redirection (opener sans `HTTPRedirectHandler`).
2. **Contenu non vu dans la charge** : des octets aléatoires après la fin du flux gzip, ou après la fin de l'archive tar, passent (cas S-frontière 0, S-octets-après-fin-tar 0) et partent dans le corps. L'affirmation « rien d'autre » vaut pour les membres de l'archive, pas pour les octets de queue ; non exécutés à l'extraction attendue, mais je n'ai pas joué l'extraction sur le serveur. La marge de taille est étroite : sain 32 540 octets de données, borne atteinte à 32 768.
3. **Garde d'adresse au banc et mandataire** : hors banc, l'adresse est bien figée, mais `urllib` honore `HTTPS_PROXY` / `https_proxy` (puits local : `CONNECT api.hetzner.cloud:443`) ; `ALL_PROXY` non honoré. Au banc, `--envoyer --nom-jeton X` sans `--adresse` vise l'adresse réelle (`ADRESSE` est admise au banc ; vu au puits, aucun appel hors 127.0.0.1). `CONTROLE_BANC` exact `oui` seulement : aucune variante partielle n'ouvre quoi que ce soit.
4. **Hors contrôle** : H0_PREVU et le jeton de démarrage ne sont contrôlés que par la forme (une date absurde passe). La fiche (IPv6, `start_after_create`, aucune clé SSH, nom) n'est pas dans le devis v5 relu ; seuls `cpx42`, `hel1` et `debian-13` y sont. La source de ces trois champs est l'auteur, non le devis.

## 4. Relevé de méthode

### Chaîne de raisonnement
1. L'outil relu (`controler-et-creer-essai-3-v1.py`, `8d88b263…`, sha256sum relu) : un seul `open` en lecture, voir section 1. Pièce : l. 166.
2. Les constantes `PIECES` et `E_AMORCE` égalent les empreintes recalculées des cinq fichiers (`sha256sum` : 524cfc4a…, b989db6e…, 64b2c0ce…, ba39fe9b…, b333b2ea…, le script complet f61aea46 ; le texte réduit 061f7993… est le `E_SCRIPT` des données saines, ligne 4, vérifié par le cas sain).
3. Données saines fabriquées par le fabricant v8 (banc : `FABRICANT_BANC=oui`, dépôt distant factice sans la branche, jeton de démarrage factice tiré au hasard) : 32 540 octets, hors de tout dépôt.
4. Chaque artefact est dérivé des octets sains par une seule modification (`outils/banc-verif.py`), joué en deux modes ; le code et le nombre de requêtes sont lus au journal du serveur factice (`outils/serveur-verif.py`, hash seulement), jamais à la sortie de l'outil seule.
5. Corps reçu comparé à `json.dumps` d'un dictionnaire reconstruit dans mon script, octets égaux (cas B).
6. Remplacement après lecture : le point d'arrêt `--pause-apres-lecture` du banc, plus remplacement, suppression, vidage du fichier ; le corps reçu égale les octets lus.
7. Garde d'adresse : listes de variantes de `CONTROLE_BANC` et d'adresse, jouées avec un serveur d'écoute local, aucun appel hors 127.0.0.1 ; `CONNECT` reçu par le puits local pour les cas de mandataire.
8. Jetons : environnement des sous-processus construit à neuf (pas d'héritage), jetons tirés à chaque lancement ; recherche par chaîne fixe dans chaque fichier, chaque sortie capturée et le guetteur `ps`.

### Objets de contrôle
- **Faux par construction** : les artefacts de la table (une soixantaine de fichiers, chacun joué en deux modes) ; attendu d'avance : refus au code listé, zéro requête ; rendu : conforme. Mécanisme éprouvé aussi par la rouge là où il le fallait pour les contrôles « première défaillance » (le code rendu est le bon, donc le contrôle visé est bien celui qui se déclenche, pas un autre).
- **Vrai par construction** : données saines (0, une requête) ; tar refait à l'identique de contenus (0) ; `CONTROLE_BANC=oui` exact (0). Les mécanismes de refus ne rejettent donc pas tout.
- Faux positifs de mon banc, corrigés avant rendu : mauvais attendu pour un membre répété trop gros (déclenchait 13 avant 14 : artefact réduit à un contenu minuscule), port 1 hors de l'expression régulière (2 chiffres au moins), test de relevé qui cherchait le mot « root_password » dans l'intitulé de la ligne. Aucun n'était un défaut de l'outil.

### Premier pas non justifié
Pas 2, en ce qui concerne la fiche du corps : le devis v5 ne dit pas IPv6, démarrage après création, aucune clé SSH ni le nom `essai-3-palier-0b`. Ce qui le justifierait : la pièce qui fixe ces champs (message de la mère ou ligne du registre des dépenses). Le reste de la chaîne renvoie à un calcul rejoué.

### Mode d'échec affecté
Épreuve qui ne peut pas échouer, ou pas réussir : **tenu**. Pas visé : pas 4, preuve : table des cas (165 lignes, 0 écart), journal du serveur (`travail/serveur/journal.txt`), relevés. Les réserves 1 à 3 touchent la solidité de l'envoi, non l'efficacité des contrôles.

### Trouvaille de côté
Aucune autre que les réserves.

### Évaluateur et conseil
Mon juge est le journal du serveur factice (compteur de requêtes, hash du corps), admis par les cas sain (une ligne) et refusés (aucune). Il pourrait donner un bon jugement sans le mériter si le serveur n'enregistrait pas les requêtes émises hors du port visé : le puits de mandataire, sur le même serveur, a bien enregistré un `CONNECT`, ce qui l'établit pour ce chemin. Limites : je n'ai ni extrait la charge avec `tar`/`gzip` du système (réserve 2), ni joué l'envoi à la vraie adresse (interdit).

## 5. Fichiers
- Outils : `outils/banc-verif.py`, `outils/serveur-verif.py`.
- Sorties : `tables/table-des-cas.tsv` ; `travail/rel/` (relevés), `travail/serveur/journal.txt`, `travail/guet.sortie`.
- Retirés : données d'essai (`travail/cas/`), dépôt factice ; corps reçus gardés dans `travail/serveur/corps-*.bin` (portent le jeton de démarrage factice seulement).

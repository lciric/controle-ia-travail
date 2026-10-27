# Brief — ronde 1 élaguée de la boucle extérieure du pilote 4 : lire les deux courses, proposer une correction de l'organisme — v1

Écrit par la lignée conv-audit le 26 octobre 2026 (heure au pied de ce fichier) pour un sous-agent neuf (Opus 5.5 ; décision
N-052 : analyste et correcteur sur Opus). Tu n'as écrit aucune pièce que tu lis. Langue : français, sans acronymes.

## Le cadre

Lazar, 26 octobre, 17:46 heure de Paris : « on est dans une phase ultra dynamique d'exploration, il faut itérer super vite,
élague tout ce que tu peux ». La boucle extérieure du pilote 4 (protocole v4, `contexte/`) est donc **élaguée** : un seul
agent (toi) tient les rôles d'analyste et de correcteur ; ni contre-lecture, ni étalonnage à blanc, ni règle de préséance.
Ce qui reste, parce que sans cela rien ne vaudrait : **`test_final` reste fermé** (tu ne l'as pas, tu ne le cherches pas) ;
**aucun score n'entre dans l'organisme** ; ta proposition se lit **dans les deux sens** à la course suivante (R3 : aucun
run ne vise un signe ; R-522 : exploration, résultats « exploratoires, non opposables »).

L'organisme « la Fusée » v6.2.1 (`fournis/objet/`, 26 fichiers, empreinte d'arbre
`4f13647a7070b3941b660d60c428620df6b4e0e31cea1d2c63d71b8606e6214d`, vérifiée) a couru deux fois sur la banque
`confrontation-v3` (identifiants opaques) : rondes de conception arrêtées par l'organisme (6 au plus), puis quatre
générations notées ; une question ouverte servie à la génération 1 seulement (question M pour la course M, question S
pour la course S ; sans effet sur le score). **M et S sont deux réplications** du même organisme (graines différentes).

## Tes pièces (`/var/tmp/ronde1-elaguee-v1/fournis/`, empreintes : `../EMPREINTES-fournis-v1.txt`, à vérifier d'abord)

- `lecture/` : la lecture de la part `test` de chaque course (json et md, script de lecture v4), M :
  `lecture-pilote4-gemini-v6-2-v1-tentative2-test-v4.*`, S : `lecture-pilote4-gemini-v6-2-s-v1-test-v4.*`.
- `mecanique/` : le relevé mécanique (B) de chaque course (faits de déroulement, sans score de `test_final`).
- `objet/` : le code de l'organisme v6.2.1 (avec `CONCEPTION.md`, `CORRECTIONS-v1.md` à `v5.md`, ses essais).
- `carte/` : `carte-facteurs-v2.json` (les facteurs que l'on peut changer, leurs lignes, les noms gelés) et
  `zones-interdites-v2.json` (ce qu'aucune correction ne touche).
- `contexte/` : le registre des hypothèses de conception v5 (fiches : ce que l'on attendait de chaque trait de
  l'organisme) et le protocole v4 (§ 14 : ce que le correcteur peut changer et ce qu'il n'écrit jamais).

## Ce que tu fais

1. **Lis** les deux lectures `test` et les deux relevés. Dis ce qui limite l'organisme sur la part `test` : par
   génération, par type de tâche ou par trait mécanique, selon ce que les pièces portent. **Chaque nombre que tu cites
   renvoie à son chemin dans le json** (par exemple `lecture-…-test-v4.json` → `cle.sous_cle[3].champ`) ou à la ligne du
   relevé ; je le revérifie mécaniquement. Ce qui tient dans M et S pèse plus que ce qui ne tient que dans une course ; dis
   lequel est le cas. Utilise les fiches du registre comme grille quand elles éclairent, sans verdict fiche par fiche.
2. **Propose au plus une correction** : un facteur de la carte, hors des zones interdites, avec
   - le **périmètre** (facteur, fichiers, fonctions, plages de lignes au commit de l'objet) ;
   - le **diff** : copie `objet/` en `sortie/objet-corrige/`, modifie-la, puis
     `cd /var/tmp/ronde1-elaguee-v1 && diff -ruN fournis/objet sortie/objet-corrige > sortie/correction-ronde-1-elaguee-v1.diff` ;
   - les **essais** : les 68 essais de l'organisme passent sur ta copie (commande ci-dessous), plus, si la correction le
     demande, un essai nouveau qui échoue sur l'objet et passe sur la copie (R5) ;
   - la **prédiction**, avant la course suivante : l'observation mécanique ou de score `test` attendue, **avec son nombre
     et son signe**, et ce qui la réfuterait ;
   - ce que la correction ne dit pas.
   Si rien ne motive une correction, écris-le et pourquoi ; c'est un résultat.
3. **N'écris jamais dans l'organisme** un score, une valeur tirée des lectures, un identifiant de tâche, ni un critère ou une
   stratégie de classement des tâches (protocole § 14 ; règle du programme) : la correction change un mécanisme, pas un
   savoir sur la banque.

Commande des essais (elle n'écrit rien hors de ta copie) :
`mkdir -p /var/tmp/ronde1-elaguee-v1/sortie/essais && rm -rf /var/tmp/ronde1-elaguee-v1/sortie/essais/organisme && cp -r /var/tmp/ronde1-elaguee-v1/sortie/objet-corrige /var/tmp/ronde1-elaguee-v1/sortie/essais/organisme && cd /var/tmp/ronde1-elaguee-v1/sortie/essais && /opt/venv-essaim-noyau-pilote2-v1/bin/python -I -m pytest -q organisme/tests`
(sur l'objet non modifié : 68 essais passent, vérifié).

## Ce que tu rends

`sortie/correction-ronde-1-elaguee-v1.md` (lecture des deux courses avec chemins ; correction ou « aucune » ; périmètre ;
prédiction ; essais avec leur sortie résumée), `sortie/correction-ronde-1-elaguee-v1.diff`, `sortie/objet-corrige/`, chacun
des deux fichiers avec son compagnon `.sha256`. Réponse finale en cinq lignes au plus : la correction (ou aucune), le
facteur, la prédiction chiffrée, les essais, les empreintes.

## Interdits

Rien lu hors de `/var/tmp/ronde1-elaguee-v1/fournis/`, rien écrit hors de `/var/tmp/ronde1-elaguee-v1/sortie/` ; le code
du noyau n'est lu que par l'exécution des essais. Aucun `git`, aucun sous-agent, aucun réseau, aucune clé ni jeton ;
aucun fichier de banque, d'archive fermée, de journal d'appels, de réponse aux questions, de `test_final`. Python avec
`-I`. Heures lues sur `date -u` dans la commande qui les écrit.

Horodatage : écrit le 2026-10-26 16:55:44 UTC (heure lue sur `date -u` dans la commande qui écrit cette ligne).

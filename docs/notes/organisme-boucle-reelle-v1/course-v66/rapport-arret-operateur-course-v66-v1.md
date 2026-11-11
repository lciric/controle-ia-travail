# Rapport d'arrêt de l'opérateur — course réelle de l'organisme (code v66, GO-2026-11-10-11) — v1

Opérateur neuf, sous-agent de la session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv` (Claude Opus 5.5, `claude-opus-5-5`) ; il n'a écrit
ni le code de l'organisme, ni le texte de la course, ni leurs contre-lectures. Consigne :
`docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-1136-v1/consigne-operateur-course-v66-v1.md`
(`7202304af4d04ece1a9d62bd353d597e5cfc24828dea7092897e47b467c64063`, vérifiée). Heures relevées par `date -u`.
Ce n'est pas le rapport de course (`rapport-course-v66-v1.md`) : **aucune course n'a eu lieu**.

## Verdict

Arrêt avant le premier préalable de la section 12.3 : la session ne joint pas la machine par SSH (sortie TCP vers le port 22
fermée par le réseau de la session, comme R-821). Machine créée puis détruite par son identifiant ; aucun appel payant aux
modèles, aucun relais lancé, aucune clé de modèle transmise ; dépense ≈ 0,06 EUR de machine.

## Serveur

| point | valeur |
|---|---|
| inventaire avant | 0 serveur, 0 clé SSH dans le projet (23:54:48) |
| clé SSH jetable | ed25519 générée dans le bac à sable de l'opérateur ; partie publique enregistrée au projet, identifiant 132459145 (23:58:14), supprimée à 00:02:35 (204 ; inventaire vide) ; partie privée effacée à la fin |
| création | identifiant **175573391**, nom `organisme-v66-course`, `cpx32`, image `debian-13` (bwrap 0.11 attendu, ≥ 0.9 ; sans la restriction AppArmor des espaces d'utilisateurs d'Ubuntu 24.04), lieu `hel1`, IPv4 2.29.163.12 ; créé 2026-11-10T23:58:22Z ; commande citant `GO_ID=GO-2026-11-10-11` ; étiquette `go=GO-2026-11-10-11` |
| prix | 0,0577 EUR/h TTC (0,0481 HT) pour `cpx32` à `hel1` ; IPv4 0,00096 EUR/h TTC (API `pricing`, lue à 00:02:35) |
| destruction | `DELETE /v1/servers/175573391` à 00:02:06, action 667128687002673 terminée en succès à 00:02:17 ; `GET` → 404 ; inventaire : 0 serveur ; IP primaires 161830122 et 161830123 retirées avec lui |
| vie | 23:58:22 → 00:02:17 (3 min 55 s) |
| coût | au plus une heure entamée : 0,05772 + 0,00096 ≈ **0,059 EUR TTC** (≈ 0,07 USD), sous les 5 USD de machine |

## Ce qui a bloqué

- `ssh root@2.29.163.12` : « Connection refused » à chaque essai, de 23:58:50 à 00:01:26 (le serveur était `running` dès
  23:58:31 ; métriques Hetzner : processeur 0,4 à 2 %, donc démarré).
- Mesure du refus (connexions TCP à la seule machine créée) : port 22 refusé en **0,33 ms** (trop vite pour un aller-retour
  vers Helsinki : refus local à la session) ; port 2222 du même serveur refusé en 4,72 ms (réponse du serveur) ; port 80
  « ouvert » en 0,27 ms (interception locale) ; `api.hetzner.cloud:443` joint en 7,07 ms.
- Lecture : le réseau de cette session ferme la sortie vers le port 22 ; d'autres ports atteignent la machine. Passer par un
  autre port serait un contournement (règle 6) et demanderait une seconde machine (le `sshd` de celle-ci n'écoutait que sur
  22) : ni l'un ni l'autre n'est dans la consigne. Arrêt, destruction, retour à la mère.
- Client SSH : absent de la session, installé par `apt-get install openssh-client` (outil local).

## Préalables de la section 12.3

Aucun joué (1 à 7). Préparé hors machine seulement, sans réseau : la charge (paquet git `84ab119f…`, base de la v65 en pack
superficiel à `cef5ea60`, texte scellé et compagnon, dossier de course v6 et ses compagnons, héritage et compagnon, relais Kimi
`d54ed2bc…`, collisionneur v7 `c9725f02…`, `registres/go.md` de `main` `1c71daae6bf620994ff187bb078ed5c811e1bbd694995feb4f941b9723d77fc5`,
ligne GO-2026-11-10-11 égale à l'octet à la section 13 du texte) ; arbre reconstruit dans le bac à sable depuis le pack et le
paquet : `git bundle verify` « okay », tête `7e415cbaaa3ff602db43a44dad6b4307c08352c7`, arbre propre, 492 fichiers, **98
empreintes du bloc `empreintes-du-code-v66` conformes**.

## Pour la reprise (faits, sans recommandation de fond)

- Une course depuis une session cloud exige un chemin jusqu'à la machine que cette session n'a pas : poste de passage (R-821,
  option (b)), ou décision explicite d'un autre port d'accès, posé à la création par les données cloud-init.
- Le passage des clés par l'entrée standard d'une commande SSH (exception (3) de la consigne) suppose le même chemin.
- Point vu en préparant, à jouer sur la machine : la borne mémoire du bac (`BorneMemoireBac.localiser`, `tests_de_mort_v2.py`)
  exige un groupe de contrôle v2 où `memory` est délégué aux enfants ; un lanceur placé dans le groupe d'une session SSH
  ne l'a probablement pas (règle « pas de processus internes ») ; l'essai à blanc `--bac reel` (préalable 3) le dira.

## Message de la mère reçu pendant la destruction

« ne lance aucun appel payant aux modèles … jusqu'à un message neuf de la mère » : déjà tenu ; aucun relais ni course lancés.

## Pièces

Journal de l'opérateur : `journal-operateur-course-v66-v1.md` (même dossier, scellé).

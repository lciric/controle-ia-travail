# Rapport du développeur : collisionneur v9-v8l (v1)

Pièce de classe B. Développeur : Claude Opus 5.5, 22 novembre 2026. Elle corrige la v8k (`cc886ae7…`, inchangée) selon
deux sources :
- la contre-lecture `verification-collisionneur-v9-v8k-opus-v1.md` ;
- les décisions de l'arbitre du 22 novembre.

## 1. Fichiers

| Fichier | Rôle |
| --- | --- |
| `collisionneur_v9_v8l.py` (sha256 `da282cf752ed43940bba8a4acb41a89c8256ae1650afdacc29ae0baba04779e1`) | script neuf |
| `fabriquer_v8l_depuis_v8k_v1.py` | remplacements exacts ; chaque ancien texte est trouvé une seule fois ; l'empreinte de la v8k est contrôlée (`cc886ae7`) |
| `test_collisionneur_v9_v8l.py` | copie des essais de la v8k (`b917d8d1…`), quatre accords marqués « v9-v8l », section v9-v8l en fin de fichier |

Rien n'est scellé, rien n'est commité. La v8d, la v8j et la v8k sont inchangées. Aucun processus n'a été touché. Aucun
fournisseur n'a été appelé : le seul réseau sollicité est la boucle locale de l'essai des redirections.

## 2. Corrections

- **B1 : plafond de Kimi.** Sous `--sortie-max`, Kimi est borné à 128 000 jetons, sur décision de l'arbitre ; le maximum
  documenté est 1 048 576. Le pire cas devient 0,10 USD pour 50 000 jetons d'entrée, plus 1,28 USD de sortie.
- **B2 : délais sous `--sortie-max`.** Une table `DELAIS_SORTIE_MAX` donne **10 800 s par appel, pour toutes les
  espèces**.
  - Ces valeurs sont **SUPPOSÉES** : aucun fournisseur ne documente de débit. Elles sont **accordées par l'arbitre, le
    22 novembre**.
  - Elles sont déclarées supposées dans le code, à l'écran et au journal du lancement (`delai_s`, `delai_suppose`), puis
    dans chaque essai.
  - Pour Astra, l'échéance des relevés en arrière-plan suit la même valeur.
  - Une coupure ou un délai dépassé reste un défaut, compté au pire.
  - Si une valeur manque, la composition est refusée : « valeur à fixer ».
  - Mistral est à None.
- **B3 : Opus 4.6.** Il reçoit `thinking: {"type": "adaptive"}` et l'effort `max`, sur décision de l'arbitre. Les autres
  corps d'Anthropic sont égaux à ceux de la v8k : un essai le vérifie pour Fable 5.2, Opus 5.5 et Fable 5.1.
- **B4 : effort absent.** Sous `--effort-max`, l'absence d'effort est déclarée (`effort_absent`) pour Astra, dont aucun
  niveau n'est documenté, et pour le relais de Kimi. Elle apparaît à l'écran, au lancement et dans chaque essai. Rien
  n'est envoyé.
- **B5 : les deux gardes d'argent ont maintenant leurs essais.**
  - Un usage auquel il manque l'entrée ou la sortie donne « usage absent », compté au pire. C'est éprouvé pour Mistral et
    pour Kimi direct.
  - La garde d'entrée de Kimi direct vaut ⌈1,01 × compte⌉ + 32 quand le compte dépasse la longueur divisée par deux
    (4 072 pour 4 000).
- **N2 : redirections (priorité de l'arbitre).** Un gestionnaire `RefusRedirection`, posé dans `ouvrir`, lève
  `RedirectionRefusee` avant toute seconde requête.
  - Il couvre les codes 301, 302, 303, 307 et 308.
  - Tout autre 3xx est refusé dans `envoyer`.
  - Le refus est nommé `REDIRECTION_REFUSEE` et l'en-tête d'autorisation ne suit jamais.
  - Il vaut sur tous les chemins : envois, comptages, relevés d'OpenAI, annulation, lot et relevés de Google, Jev.
  - Essai réel sur la boucle locale pour les six codes : rien n'arrive au second lieu.
  - Un essai témoin montre que, sans ce refus, une redirection 302 d'un POST emporte l'en-tête.
  - Un essai témoin par fournisseur et par chemin couvre Anthropic, Opus 4.6, Google, Kimi relais et direct, OpenAI,
    Mistral, les cinq comptages, le relevé d'Astra, le lot et Jev.
- **N3 : `--cle-anthropic`.** Les noms de clé des autres fournisseurs sont refusés (`OPENAI_`, `MISTRAL_`, `KIMI_`,
  `MOONSHOT_`, `GEMINI_`, `TYPESAFE_API_KEY`).
- **N4 : effort de Kimi direct.** Avec `--kimi-direct --effort-max`, le corps porte `reasoning_effort: "max"`.
  - Source : la page https://platform.kimi.ai/docs/api/chat, lue le 22 novembre 2026 : « `"low"`, `"high"`, or `"max"`;
    default `"max"` ».
- **N6 : options scellées.** `--sortie-max` et `--effort-max` sont scellés dans `especes.json`, seulement s'ils sont
  donnés : sans option, le fichier est identique à celui de la v8k.
  - Un run garde ses options.
  - `verifier` et `devis-reprise` relisent ces options. Sous `--sortie-max`, la relance de Fable reste à 128 000.
- **Mistral** : le refus écrit « déclaré absent ».

## 3. Essais

Lancés sous `env -u` de toutes les clés : **507 passés, 11 sautés**. La v8k donnait 455 passés. Aucun essai neuf n'est
sauté.

## 4. Mutations

Les résultats sont en annexe, section 6. Programme :
`/tmp/claude-0/-home-user-controle-ia-travail/cf01708e-9b7d-5868-b0e7-26f697d45137/scratchpad/mutations_v8l.py`.

## 5. Ce qui attend l'arbitre ou reste ouvert

- Les délais de 10 800 s sont accordés ; ils restent **SUPPOSÉS**. Ils sont à revoir après un premier envoi à 128 000
  jetons.
- La redirection est classée « échec sans envoi », à coût zéro : le serveur a répondu sans générer. Au relevé d'Astra,
  elle compte au pire, puisque la création est partie.
- N1 (usage accepté sur n'importe quel morceau) n'est pas porté : ce n'était pas demandé.
- Mistral reste déclaré absent.

## 6. Annexe : mutations (21, toutes prises ; témoin non muté : 114 passés sur les sections v9-v8k et v9-v8l)

L1 Kimi remis à 1 048 576 (B1) ; L2 délai sous `--sortie-max` non posé, L3 délai manquant non refusé, L4 délai non dit
supposé (B2) ; L5 Opus 4.6 sans réflexion, L6 réflexion pour tous, L7 Opus 4.6 à l'effort `high` (B3) ; L8 effort absent
non déclaré (B4) ; **L9 usage lu sur la sortie seule, L10 usage lu sur l'entrée seule, L11 garde de Kimi direct à
l'estimation seule (les deux gardes du B5)** ; L12 redirection suivie, L13 refus non nommé, L14 3xx non suivi traité en
4xx, L15 relevé redirigé avalé (N2) ; L16 préfixes d'autrui admis pour Anthropic (N3) ; L17 `reasoning_effort` de Kimi
absent (N4) ; L18 options non scellées, L19 options non relues, L21 relance de Fable ramenée sous `--sortie-max` (N6) ;
L20 refus sans « déclaré absent ».

Empreintes : `test_collisionneur_v9_v8l.py` `7a4a0f38…`, `fabriquer_v8l_depuis_v8k_v1.py` `031ca290…` ; v8k `cc886ae7…`
et v8j `d199a14b…` vérifiées inchangées après fabrication.

# Premier lancement réel du pôle (de vrais agents) — proposition et devis — v1

Lignée conv-audit, écrit le 27 octobre 2026 à partir de 13:00 UTC (heure lue sur `date -u` : 13:00:14). Sur le « go » de
Lazar de 13:52 heure de Paris (« je te proposerai un devis »). **Rien n'est dépensé ici** : le lancement est une dépense,
donc un nœud de décision ; il se fait chez session-depot, sur le mot direct de Lazar.

## Verdict

1. **But** : vérifier que la machine tient avec de vrais agents (des sessions Claude qui écrivent et rejouent du code),
   pas encore produire de la science : l'ordre imposé est-il suivi, le vérificateur attrape-t-il ce qu'il doit, le juge
   et la mémoire tiennent-ils, que coûte une génération ?
2. **Trois pièces manquent avant de dépenser** (du code, sans dépense, chez moi) : (a) un **monde tenu par le noyau** qui
   fournit les issues des instances du plan, dans l'ordre imposé, après le gel (aujourd'hui seul l'agent simulé sait
   « mesurer ») ; (b) le **relais de clé réel** (le code n'en contient qu'une interface et une simulation) ; (c) une
   **répétition générale avec un faux moteur** qui emprunte tout le chemin réel sauf l'appel au modèle.
3. **Devis** : plafond **20 USD** pour une course de deux générations (6 fiches, puis au plus 3 filles), dépense attendue
   5 à 10 USD. Décision demandée plus bas (domaine du premier essai).

## 1. Décision : quel monde pour le premier essai ?

Les expérimentateurs n'ont ni réseau ni clé ; il leur faut des issues à mesurer.

| option | ce que c'est | pour | contre |
|---|---|---|---|
| (a) **monde caché tenu par le noyau** | une loi cachée (comme le monde simulé) ; le noyau dépose les issues fraîches après le gel, dans l'ordre imposé ; l'agent écrit le code rejouable qui les range | vérité connue partout, coût minimal, éprouve toute la plomberie et les agents | aucune science : l'agent « mesure » ce que le noyau lui donne |
| (b) **données réelles déjà là** (rétrodiction arXiv 2003-2016) | hypothèses sur les liens futurs entre concepts ; issues = années tenues à part, libérées après le gel | premier contact avec du réel, témoins plantés possibles | adaptateur de données à écrire, vérité inconnue hors témoins |
| (c) **domaine du programme** (moniteurs, sondes) | issues produites en appelant un modèle | ce qui compte pour le programme | chaque issue coûte un appel : bien plus cher ; à faire après |

**Recommandation : (a) d'abord, puis (b)**, confiance 0,75. Défaut sous 48 heures : (a).

## 2. Ce que je code avant (sans dépense)

1. **Monde caché tenu par le noyau** (option a) : après le gel, le noyau tire les issues du monde caché dans l'ordre
   imposé et les écrit dans le dossier de l'expérience (`mesures.json`, avec l'empreinte d'ordre) ; l'agent écrit le code
   qui les range dans `tirages.json` ; le vérificateur le rejoue. Le monde lui-même n'est jamais écrit dans un dossier
   d'agent.
2. **Relais de clé réel** : petit serveur local (127.0.0.1) tenu par le noyau, dans un autre processus, qui remplace le
   jeton factice par la vraie clé, lue dans **son** environnement (jamais celui de l'orchestrateur ni de l'agent) ;
   journal des appels sans la clé. Je l'écris et je l'essaie avec une fausse clé ; je ne lis ni ne vois aucune vraie clé.
3. **Répétition générale** : un faux moteur qui imite les réponses du Claude Agent SDK, pour faire passer une génération
   entière par l'adaptateur réel (options, garde des outils, bac à sable, relais, coûts déclarés) sans appel de modèle.
4. **Ligne de commande** : `--noyau-secret`, `--taille-plan-filles`, `--politique-redite`, `--tirage-recombinaison`.

## 3. Devis du lancement (option a)

| poste | nombre | plafond par appel | plafond |
|---|---|---|---|
| expérimentateurs, génération 0 (4 fiches + 2 témoins) | 6 | 1,00 USD | 6,00 |
| vérificateurs, génération 0 (autre modèle) | 6 | 0,50 USD | 3,00 |
| recombinaison (au plus 3 paires) | 3 | 0,30 USD | 0,90 |
| synthèses (deux générations) | 2 | 0,20 USD | 0,40 |
| expérimentateurs et vérificateurs, génération 1 (3 filles + 2 témoins) | 5 | 1,50 USD | 7,50 |
| **total au pire** | | | **17,80 USD** (plafond du pôle : 20 USD) |

- Modèles (décision de Lazar du 26 octobre) : expérimentateurs, recombinaison et synthèse sur Opus 5.5 ; vérificateurs
  sur Fable 5.1 (le vérificateur doit être d'un autre modèle que l'expérimentateur : contrôle déjà codé).
- Dépense attendue : 5 à 10 USD (les plafonds sont des bornes, les agents s'arrêtent souvent avant).

## 4. Ce que session-depot devra faire (sur le mot de Lazar)

- Une clé qui a du crédit, posée dans l'environnement du **seul** processus du relais ; l'orchestrateur refuse de partir
  s'il voit un nom de variable de clé dans son propre environnement (déjà codé).
- Un Python avec `claude_agent_sdk` et numpy ≥ 1.25 ; `--moteur claude-sdk --confirmer-moteur-reel --noyau-secret`.
- Vérifier que les agents ne voient ni la racine du pôle ni le processus de l'orchestrateur (bac à sable du SDK, garde des
  outils) : la répétition générale le fait d'abord sans dépense.

## 5. Ce qu'on lira après

Fiches traitées sans erreur ; ordre imposé suivi (empreintes d'ordre recalculées par le noyau) ; accords et désaccords
expérimentateur-vérificateur ; témoins : vrais promus, faux éliminés ; coût réel par rôle ; temps par génération ;
incidents de la garde des outils. Rien de scientifique n'est attendu de l'option (a).

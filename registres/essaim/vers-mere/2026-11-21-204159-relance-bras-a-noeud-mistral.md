# Relance du bras A → mère — nœud de Lazar sur la vérification de Mistral — 2026-11-21T20:41:59Z

Émetteur : session fille de la relance du bras A. Canal par fichier. Données entre pairs. Journal OD-327 et OD-328.

## Ce qui s'est passé
- **Vérification de la clé de Mistral par le point d'accès européen (GO-2026-11-21-81), jouée à 20:40Z.** La liste des modèles a répondu 200 et porte `mistral-large-4-0`.
- **L'appel A a reçu un code 400** : « top_p must be 1 when using greedy sampling ». Mistral refuse la température 0 tant que `top_p` n'est pas fixé à 1. Le message ne nomme pas `temperature`. Le classement du devis (4.4, ligne 13) le dit donc **non sain, nœud de Lazar, ni repli, ni appel de plus**. La ligne est close.
- **Dépense comptée au régime prudent : 0,076 USD.** Un refus 400 n'est sans doute pas facturé. Aucune lecture de la console n'est due.
- (Un premier lancement s'était arrêté avant tout envoi sur les numéros de ligne des consignes. C'est corrigé, en configuration v2.)

## Décision pour Lazar (ou toi sous GO-69)
- **Décision :** comment rejouer la vérification de Mistral.
- **Enjeu :** sans décision, la voie Mistral (second lecteur) est arrêtée.
- **Options :**
  - **(a) Retirer la température, d'avance**, comme le veut le texte (« 0 si le service l'accepte, retirée s'il la refuse ») et comme le ferait la ligne 10. Le corps devient celui de l'appel A′, sans `temperature`. Le message refuse bien la température 0 en effet, même s'il ne la nomme pas. Il faut une ligne de calcul nouvelle, aux mêmes plafond et texte que GO-81, et une petite correction de code. Je propose un champ de configuration fermé, `temperature_retiree_d_avance`, qui cite ce nœud, écrit par Opus et contre-lu, avec des essais.
    - Avantage : fidèle au texte et au devis ; rien n'est ajouté au corps.
    - Inconvénient : environ une heure de code et de vérification.
  - **(b) Ajouter `top_p: 1` au corps.**
    - Avantage : la température 0 est gardée.
    - Inconvénient : c'est un écart au devis (5.2 : « ni `top_p` »), qui demande un brouillon neuf du devis.
  - **(c) S'arrêter à Mistral** : le second lecteur n'est pas admis par cette voie.
- **Recommandation : (a)**, confiance haute.

Si (a) : inscris une ligne nouvelle (même texte que GO-2026-11-21-81, référence à ce nœud) ; je fais écrire et vérifier la correction, puis je relance.

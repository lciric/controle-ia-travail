"""Construit le corps de création du serveur d'INVENTAIRE PAR INSTANTANÉ d'un serveur Hetzner du témoin de Bailey, poste
ou sauvegarde, v5 (R12 ; v1 à v4 restent telles quelles). v5 (19 novembre 2026, mot de Lazar « sauvegarde en (a) ») :
fichiers de création `poste-*-creation.json` et `sauvegarde-*-creation.json` ; genre tiré du préfixe du nom du serveur
(`poste-temoin-bailey-…` → genre « poste », cible `poste-…` ; `sauvegarde-temoin-bailey-…` → genre « sauvegarde », cible
`sauvegarde-…`) et rempli dans le script ; table `instantanes-postes-v2.json` ; serveur d'inventaire créé au lieu du
serveur copié (champ `lieu` du fichier de création). Le reste est celui de la v4 : l'instantané, la cible et l'heure
d'arrêt sont tirés de pièces scellées et contrôlés ; tout fichier de création illisible fait refuser (R5) ; refus
anticipé si le versement ou la marque v5 existent déjà. Mot de Lazar du 19 novembre 2026 : « avant toute destruction,
inventaire et versement scellé de tout ce qui reste sur la machine ». Les données de démarrage ne portent aucun secret.

Usage : construire-donnees-inventaire-instantane-v5.py <cible> <identifiant de l'instantané> <heure d'arrêt, epoch>
        <serveur copié> <dossier de sortie, neuf, hors du dépôt>
Gardes : cible en lettres minuscules, chiffres et tirets, de 3 à 38 caractères (nom du serveur au plus 63) ; instantané
entier ; heure sur 10 chiffres, postérieure au 17 novembre 2026 et au plus égale à maintenant ; empreinte du script
égale à son compagnon ; table scellée et conforme ; un seul fichier de création scellé dont `serveur_hetzner` est le
serveur donné, de nom conforme à la table et à la cible ; heure d'arrêt au moins égale à son champ `cree` ; lieu connu ;
cinq blocs remplis une fois chacun, aucun « @@ » après remplissage ; script rempli d'au plus 32 Kio ; dossier de sortie
neuf (R12) et hors du dépôt. Écrit le corps JSON et imprime l'empreinte du script rempli : la marque du serveur doit
porter la même (`script_sha256`). La réponse de création porte un `root_password` (aucune clé ssh) : ne jamais
l'imprimer."""
import calendar
import hashlib
import json
import re
import sys
import time
from pathlib import Path

ICI = Path(__file__).resolve().parent
SCRIPT = ICI / "inventaire-instantane-v5.sh"
TABLE = ICI / "instantanes-postes-v2.json"
GENRES = {"poste-temoin-bailey-": ("poste", "poste-"), "sauvegarde-temoin-bailey-": ("sauvegarde", "sauvegarde-")}
LIEUX = {"fsn1", "nbg1", "hel1"}


def scelle(f: Path) -> bool:
    """Compagnon `<empreinte>  <nom>` égal au fichier."""
    try:
        x = (f.parent / (f.name + ".sha256")).read_text(encoding="utf-8").split()
        return len(x) == 2 and x[1] == f.name and hashlib.sha256(f.read_bytes()).hexdigest() == x[0]
    except OSError:
        return False


def main() -> int:
    if len(sys.argv) != 6:
        print(__doc__, file=sys.stderr)
        return 2
    cible, image, heure, serveur, dossier = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], Path(sys.argv[5])
    if (not re.fullmatch(r"[a-z0-9][a-z0-9-]{1,36}[a-z0-9]", cible) or not re.fullmatch(r"[1-9][0-9]{0,11}", image)
            or not re.fullmatch(r"[1-9][0-9]{5,11}", serveur)):
        print("cible, instantané ou serveur mal formés : rien n'est construit", file=sys.stderr)
        return 2
    if not re.fullmatch(r"[0-9]{10}", heure) or not (1794873600 <= int(heure) <= int(time.time())):
        print("heure d'arrêt mal formée ou invraisemblable : rien n'est construit", file=sys.stderr)
        return 2
    try:
        comp = (ICI / "inventaire-instantane-v5.sh.sha256").read_text(encoding="utf-8").split()
        octets = SCRIPT.read_bytes()
    except OSError:
        print("script ou compagnon illisible : rien n'est construit", file=sys.stderr)
        return 2
    if len(comp) != 2 or comp[1] != SCRIPT.name or hashlib.sha256(octets).hexdigest() != comp[0]:
        print("compagnon du script absent, mal formé ou différent : rien n'est construit", file=sys.stderr)
        return 2
    if not scelle(TABLE):
        print("table des instantanés absente ou non scellée : rien n'est construit", file=sys.stderr)
        return 2
    entree = json.loads(TABLE.read_text(encoding="utf-8")).get("instantanes", {}).get(image)
    if not isinstance(entree, dict) or str(entree.get("serveur")) != serveur or str(entree.get("heure_arret")) != heure:
        print("instantané, serveur et heure d'arrêt non conformes à la table scellée : rien n'est construit", file=sys.stderr)
        return 2
    creations = []
    for f in sorted(ICI.glob("poste-*-creation.json")) + sorted(ICI.glob("sauvegarde-*-creation.json")):
        try:
            d = json.loads(f.read_text(encoding="utf-8"))
            if not isinstance(d, dict):
                raise ValueError("pas un objet")
        except (OSError, ValueError):
            print(f"fichier de création illisible ({f.name}) : rien n'est construit (R5)", file=sys.stderr)
            return 2
        if str(d.get("serveur_hetzner")) == serveur:
            if not scelle(f):
                print(f"fichier de création non scellé ou modifié ({f.name}) : rien n'est construit", file=sys.stderr)
                return 2
            creations.append(d)
    if len(creations) != 1:
        print(f"serveur {serveur} : {len(creations)} fichier(s) de création correspondant(s), un seul attendu : rien n'est "
              "construit", file=sys.stderr)
        return 2
    nom_serveur = str(creations[0].get("nom", ""))
    genres = [(p, g, c) for p, (g, c) in GENRES.items() if nom_serveur.startswith(p)]
    if len(genres) != 1 or nom_serveur != entree.get("nom"):
        print("nom du serveur hors des genres connus ou différent de la table : rien n'est construit", file=sys.stderr)
        return 2
    prefixe, genre, debut_cible = genres[0]
    if cible != debut_cible + nom_serveur[len(prefixe):]:
        print("cible non conforme au nom du serveur (fichier de création et table) : rien n'est construit", file=sys.stderr)
        return 2
    lieu = creations[0].get("lieu")
    if lieu not in LIEUX:
        print("lieu du serveur copié absent ou inconnu : rien n'est construit", file=sys.stderr)
        return 2
    if (ICI / f"versement-{cible}-v5").exists() or (ICI / f"poste-fini-inventaire-instantane-{cible}-v5.json").exists():
        print("versement ou marque v5 déjà présents dans le dépôt local (R12) : rien n'est construit", file=sys.stderr)
        return 2
    try:
        cree_epoch = calendar.timegm(time.strptime(creations[0].get("cree", ""), "%Y-%m-%dT%H:%M:%SZ"))
    except (TypeError, ValueError):
        print("date de création du serveur illisible : rien n'est construit", file=sys.stderr)
        return 2
    if int(heure) < cree_epoch:
        print("heure d'arrêt antérieure à la création du serveur : rien n'est construit", file=sys.stderr)
        return 2
    depot = ICI.parents[1].resolve()
    if dossier.resolve() == depot or depot in dossier.resolve().parents:
        print("dossier de sortie dans le dépôt : rien n'est construit", file=sys.stderr)
        return 2
    texte = octets.decode("utf-8")
    blocs = {"@@CIBLE@@": cible, "@@HEURE@@": heure, "@@POSTE@@": serveur, "@@INSTANTANE@@": image, "@@GENRE@@": genre}
    if any(texte.count(b) != 1 for b in blocs):
        print("blocs à remplir absents ou en double : rien n'est construit", file=sys.stderr)
        return 2
    for b, v in blocs.items():
        texte = texte.replace(b, v)
    if "@@" in texte or len(texte.encode()) > 32 * 1024:
        print("bloc non rempli ou script trop long : rien n'est construit", file=sys.stderr)
        return 2
    if dossier.exists():
        print("dossier de sortie déjà présent (R12) : rien n'est construit", file=sys.stderr)
        return 2
    dossier.mkdir(mode=0o700, parents=True)
    nom = f"inventaire-instantane-{cible}-v5"
    corps = {"name": nom, "server_type": "cx23", "location": lieu, "image": int(image), "start_after_create": True,
             "user_data": texte, "labels": {"programme": "controle-ia", "poste": nom}}
    sortie = dossier / "creation-hetzner-v5.json"
    sortie.write_text(json.dumps(corps), encoding="utf-8")
    print(f"construit : {sortie} ; serveur {nom} ; genre {genre} ; lieu {lieu} ; script rempli "
          f"{hashlib.sha256(texte.encode()).hexdigest()} ; script sans remplissage {comp[0]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

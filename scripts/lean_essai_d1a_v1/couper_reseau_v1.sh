#!/usr/bin/env bash
# couper_reseau_v1.sh — essai Lean, D-1a, v1. Second étage de la coupure du réseau sortant (le premier est le pare-feu du nuage,
# posé par la session) : nftables chargé au démarrage. Sortie : boucle locale, réponses des connexions établies (SSH entrant),
# bail DHCP IPv4 et métadonnées locales seulement ; DNS refusé. Entrée : SSH (la source est restreinte par le pare-feu du nuage).
# Aucune réouverture sans nouveau GO (brouillon 3, § 4.5).
set -euo pipefail
cat > /etc/nftables.conf <<'NFT'
#!/usr/sbin/nft -f
flush ruleset
table inet coupure_d1a {
  chain sortie {
    type filter hook output priority 0; policy drop;
    oif "lo" accept
    ct state established,related accept
    udp sport 68 udp dport 67 accept
    ip daddr 169.254.169.254 tcp dport 80 accept
  }
  chain entree {
    type filter hook input priority 0; policy drop;
    iif "lo" accept
    ct state established,related accept
    tcp dport 22 accept
    udp sport 67 udp dport 68 accept
  }
  chain transit {
    type filter hook forward priority 0; policy drop;
  }
}
NFT
nft -c -f /etc/nftables.conf
systemctl enable nftables >/dev/null 2>&1
nft -f /etc/nftables.conf
echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) nftables chargé" | tee -a /opt/harnais/journal-installation-v1.txt
nft list ruleset

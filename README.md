# BlackRoad-Hardware — RoadCode

> Fleet & IoT division of [BlackRoad OS, Inc.](https://github.com/BlackRoad-OS-Inc)

Pi fleet management, Hailo-8 AI accelerators, LoRa sensors, and network topology. 5 Raspberry Pis + 2 DigitalOcean droplets. 52 TOPS of local inference. $38/mo total.

**Domain**: [blackroad.systems](https://blackroad.systems)

## The Fleet

| Node | Role | Location | Key Services |
|------|------|----------|-------------|
| **Alice** (.49) | Gateway | Local | Pi-hole, PostgreSQL, Qdrant, Redis, nginx (37 sites) |
| **Cecilia** (.96) | AI + Storage | Local | Ollama (16 models), MinIO (4 buckets), PostgreSQL, InfluxDB |
| **Octavia** (.101) | Git + Workers | Local | Gitea (239 repos), 15 Workers, PaaS, NATS, Docker |
| **Aria** (.98) | Compute | Local | Ollama, batch processing |
| **Lucidia** (.38) | Web + DNS | Local | 334 web apps, nginx, PowerDNS, GitHub Actions runners |
| **Gematria** | TLS Edge | DO nyc3 | Caddy (151 domains), Ollama (6 models), PowerDNS (ns1) |
| **Anastasia** | Backup | DO nyc1 | Redundancy node |

## Hardware Specs

- **2x Hailo-8** AI accelerators = 52 TOPS (on Cecilia + Octavia)
- **WireGuard mesh**: 12/12 SSH connections across all nodes
- **Tor hidden services**: Alice, Octavia, Lucidia reachable via .onion
- **Total cost**: $38/mo for the entire fleet

## Org Hierarchy

```
BlackRoad-OS-Inc (Parent — 254 repos, 67 agents, 7 nodes)
  └── BlackRoad-Hardware (Fleet & IoT)
      ├── RoadCode          ← this repo (workspace + automation)
      ├── operator           ← fleet management scripts
      ├── source             ← hardware configs + topology
      └── source-code        ← device drivers + sensor code
```

## How It Connects

- **Parent**: [BlackRoad-OS-Inc](https://github.com/BlackRoad-OS-Inc) — central coordination
- **AI**: [BlackRoad-AI](https://github.com/BlackRoad-AI) — models run on Cecilia/Octavia/Lucidia/Gematria
- **Security**: [BlackRoad-Security](https://github.com/BlackRoad-Security) — fleet hardening + WireGuard audit
- **Cloud**: [BlackRoad-Cloud](https://github.com/BlackRoad-Cloud) — edge routing via Gematria

## License

Proprietary — BlackRoad OS, Inc. See [LICENSE](./LICENSE).

---

*Remember the Road. Pave Tomorrow.*

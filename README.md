<!-- BlackRoad SEO Enhanced -->

# RoadCode

> Part of **[BlackRoad OS](https://blackroad.io)** — Sovereign Computing for Everyone

[![BlackRoad OS](https://img.shields.io/badge/BlackRoad-OS-ff1d6c?style=for-the-badge)](https://blackroad.io)
[![BlackRoad Hardware](https://img.shields.io/badge/Org-BlackRoad-Hardware-2979ff?style=for-the-badge)](https://github.com/BlackRoad-Hardware)
[![License](https://img.shields.io/badge/License-Proprietary-f5a623?style=for-the-badge)](LICENSE)

**RoadCode** is part of the **BlackRoad OS** ecosystem — a sovereign, distributed operating system built on edge computing, local AI, and mesh networking by **BlackRoad OS, Inc.**

## About BlackRoad OS

BlackRoad OS is a sovereign computing platform that runs AI locally on your own hardware. No cloud dependencies. No API keys. No surveillance. Built by [BlackRoad OS, Inc.](https://github.com/BlackRoad-OS-Inc), a Delaware C-Corp founded in 2025.

### Key Features
- **Local AI** — Run LLMs on Raspberry Pi, Hailo-8, and commodity hardware
- **Mesh Networking** — WireGuard VPN, NATS pub/sub, peer-to-peer communication
- **Edge Computing** — 52 TOPS of AI acceleration across a Pi fleet
- **Self-Hosted Everything** — Git, DNS, storage, CI/CD, chat — all sovereign
- **Zero Cloud Dependencies** — Your data stays on your hardware

### The BlackRoad Ecosystem
| Organization | Focus |
|---|---|
| [BlackRoad OS](https://github.com/BlackRoad-OS) | Core platform and applications |
| [BlackRoad OS, Inc.](https://github.com/BlackRoad-OS-Inc) | Corporate and enterprise |
| [BlackRoad AI](https://github.com/BlackRoad-AI) | Artificial intelligence and ML |
| [BlackRoad Hardware](https://github.com/BlackRoad-Hardware) | Edge hardware and IoT |
| [BlackRoad Security](https://github.com/BlackRoad-Security) | Cybersecurity and auditing |
| [BlackRoad Quantum](https://github.com/BlackRoad-Quantum) | Quantum computing research |
| [BlackRoad Agents](https://github.com/BlackRoad-Agents) | Autonomous AI agents |
| [BlackRoad Network](https://github.com/BlackRoad-Network) | Mesh and distributed networking |
| [BlackRoad Education](https://github.com/BlackRoad-Education) | Learning and tutoring platforms |
| [BlackRoad Labs](https://github.com/BlackRoad-Labs) | Research and experiments |
| [BlackRoad Cloud](https://github.com/BlackRoad-Cloud) | Self-hosted cloud infrastructure |
| [BlackRoad Forge](https://github.com/BlackRoad-Forge) | Developer tools and utilities |

### Links
- **Website**: [blackroad.io](https://blackroad.io)
- **Documentation**: [docs.blackroad.io](https://docs.blackroad.io)
- **Chat**: [chat.blackroad.io](https://chat.blackroad.io)
- **Search**: [search.blackroad.io](https://search.blackroad.io)

---


> Canonical RoadCode workspace and automation hub for BlackRoad-Hardware.

Part of the [BlackRoad OS](https://blackroad.io) ecosystem — [BlackRoad-Hardware](https://github.com/BlackRoad-Hardware)

---

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

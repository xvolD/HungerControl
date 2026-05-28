# Hunger Control

[![Minecraft](https://img.shields.io/badge/Minecraft-1.20.1--1.20.4-green.svg)](https://minecraft.net)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Forge](https://img.shields.io/badge/Loader-Forge-orange.svg)](https://files.minecraftforge.net)
[![Fabric](https://img.shields.io/badge/Loader-Fabric-pink.svg)](https://fabricmc.net)

A lightweight **Forge & Fabric** mod for **Minecraft 1.20.1–1.20.4** that lets modpack developers and server owners configure how fast players lose hunger.

## Features

- **Global exhaustion multiplier** — scale all hunger drain (sprinting, jumping, combat, regen, etc.) with a single config value.
- **Player-only** — only affects player hunger (reserved option for future mob support).
- **In-game commands** — check and reload settings without restarting.
- **No dependencies** — works out of the box.
- **Mixin-based** — clean, minimal injection into vanilla hunger logic.

## Supported Versions

| Minecraft | Loader | Java | Status |
|-----------|--------|------|--------|
| 1.20.1 | Forge | 17 | Stable (root project) |
| 1.20.1 | Fabric | 17 | Stable |
| 1.20.2 | Forge | 17 | Stable |
| 1.20.2 | Fabric | 17 | Stable |
| 1.20.3 | Forge | 17 | Stable |
| 1.20.3 | Fabric | 17 | Stable |
| 1.20.4 | Forge | 17 | Stable |
| 1.20.4 | Fabric | 17 | Stable |

## Config

### Forge — `config/hungercontrol-common.toml`

| Option | Default | Description |
|--------|---------|-------------|
| `enable` | `true` | Toggle the mod on/off. |
| `exhaustionMultiplier` | `1.0` | Global multiplier for hunger exhaustion. `0.5` = half speed, `0.2` = 5× slower. Range: `0.0` – `100.0`. |
| `affectPlayersOnly` | `true` | Currently always player-only; reserved for future expansion. |
| `debugLog` | `false` | Log exhaustion changes to the console for debugging. |

### Fabric — `config/hungercontrol.json`

```json
{
  "enable": true,
  "exhaustionMultiplier": 1.0,
  "affectPlayersOnly": true,
  "debugLog": false
}
```

## Commands

Requires operator level 2 (cheats/op).

- `/hungercontrol info` — displays current multiplier and enabled state.
- `/hungercontrol reload` — reloads the config from disk (`hungercontrol-common.toml` on Forge, `hungercontrol.json` on Fabric).

## Building

### Prerequisites

- Java 17
- Gradle (wrapper included)

### Build a single version

```bash
cd versions/1.20.4-forge
./gradlew build
```

### Build all versions

```bash
# Linux / Git Bash
./build-all.sh

# Windows
build-all.bat
```

Built JARs will be in each version's `build/libs/` directory.

## Project Structure

- `src/` — root source for **1.20.1 Forge**
- `versions/<version>-<loader>/` — per-version subprojects generated via `generate_versions.py` (supports Forge, NeoForge, Fabric)
- `generate_versions.py` — script that regenerates all version subprojects from the root source
- `build-all.sh` / `build-all.bat` — batch build scripts for all supported versions

## Example Use-Cases

- **Realistic / medieval packs** — slow hunger down so players eat 2–3 times per in-game day instead of constantly.
- **Hardcore packs** — raise the multiplier above `1.0` to make food a real challenge.
- **Adventure maps** — fine-tune exactly how much stamina actions consume.

## Installation

1. Download the correct JAR for your **Minecraft version** and **mod loader** (Forge or Fabric).
2. Drop it into your `mods/` folder.
3. Launch the game once to generate the config, or edit it beforehand:
   - **Forge**: `config/hungercontrol-common.toml`
   - **Fabric**: `config/hungercontrol.json`

## License

MIT — feel free to include in any modpack, private or public.

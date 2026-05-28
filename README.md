<div align="center">

<img src="src/main/resources/hungercontrol.png" width="96" alt="Hunger Control">

# Hunger Control

**Fine-tune hunger exhaustion for Minecraft modpacks**

[![Minecraft](https://img.shields.io/badge/Minecraft-1.20.1--1.20.4-3C8529?logo=minecraft&logoColor=white)](https://minecraft.net)
[![Forge](https://img.shields.io/badge/Forge-FF6F00?logo=curseforge&logoColor=white)](https://files.minecraftforge.net)
[![Fabric](https://img.shields.io/badge/Fabric-DBBCC3?logo=fabric&logoColor=black)](https://fabricmc.net)
[![License](https://img.shields.io/badge/License-MIT-4DA1FF)](LICENSE.md)
[![CI](https://github.com/xvolD/HungerControl/actions/workflows/build.yml/badge.svg)](https://github.com/xvolD/HungerControl/actions)

</div>

## Overview

A tiny, zero-dependency mod that gives modpack developers and server owners a single config value to control how fast players lose hunger. Sprinting, jumping, combat, health regeneration — everything that drains the hunger bar scales through one multiplier.

## Supported Versions

| Minecraft | Forge | Fabric | Java |
|:---------:|:-----:|:------:|:----:|
| 1.20.1 | ✓ | ✓ | 17 |
| 1.20.2 | ✓ | ✓ | 17 |
| 1.20.3 | ✓ | ✓ | 17 |
| 1.20.4 | ✓ | ✓ | 17 |

> Download JARs for your exact version from [Releases](../../releases).

## Features

- **One config value rules them all** — a global exhaustion multiplier affects every vanilla hunger drain source.
- **Players only** — currently scoped to player hunger, leaving mobs untouched.
- **Live reload** — change settings on the fly without restarting the server or client.
- **Mixin-powered** — injects cleanly into vanilla logic, no fragile reflection hacks.

## Configuration

### Forge
`config/hungercontrol-common.toml`

| Option | Default | Description |
|--------|---------|-------------|
| `enable` | `true` | Master switch for the mod. |
| `exhaustionMultiplier` | `1.0` | Global multiplier. `0.5` = half speed, `2.0` = double speed. Range: `0.0` – `100.0`. |
| `affectPlayersOnly` | `true` | Reserved for future mob support; currently always player-only. |
| `debugLog` | `false` | Print exhaustion changes to the log for troubleshooting. |

### Fabric
`config/hungercontrol.json`

```json
{
  "enable": true,
  "exhaustionMultiplier": 1.0,
  "affectPlayersOnly": true,
  "debugLog": false
}
```

## Commands

Requires operator level 2 (cheats enabled).

| Command | Description |
|---------|-------------|
| `/hungercontrol info` | Shows current multiplier and whether the mod is active. |
| `/hungercontrol reload` | Re-reads the config file from disk. |

## Building

```bash
./gradlew build
```

Output JAR lands in `build/libs/`.

## Installation

1. Grab the correct JAR for your **Minecraft version** and **loader** (Forge or Fabric) from the [Releases](../../releases) page.
2. Drop it into your `mods/` folder.
3. Launch once to generate the config, or edit it beforehand.

## License

MIT — include it in any modpack, public or private, no attribution required.

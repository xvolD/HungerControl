# Hunger Control

[![Minecraft](https://img.shields.io/badge/Minecraft-1.20.1-green.svg)](https://minecraft.net)
[![Loader](https://img.shields.io/badge/Loader-Forge-orange.svg)](https://files.minecraftforge.net)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE.md)

A lightweight **Forge** mod for **Minecraft 1.20.1** that lets modpack developers and server owners configure how fast players lose hunger.

## Features

- **Global exhaustion multiplier** — scale all hunger drain (sprinting, jumping, combat, regen, etc.) with a single config value.
- **Player-only** — only affects player hunger.
- **In-game commands** — check and reload settings without restarting.
- **Mixin-based** — clean, minimal injection into vanilla hunger logic.

## Config

`config/hungercontrol-common.toml`

| Option | Default | Description |
|--------|---------|-------------|
| `enable` | `true` | Toggle the mod on/off. |
| `exhaustionMultiplier` | `1.0` | Global multiplier for hunger exhaustion. `0.5` = half speed, `0.2` = 5× slower. |
| `affectPlayersOnly` | `true` | Currently always player-only; reserved for future expansion. |
| `debugLog` | `false` | Log exhaustion changes to the console for debugging. |

## Commands

Requires operator level 2.

- `/hungercontrol info` — displays current multiplier and enabled state.
- `/hungercontrol reload` — reloads the config from disk.

## Building

```bash
./gradlew build
```

Built JARs will be in `build/libs/`.

## Installation

1. Download the latest JAR from [Releases](../../releases).
2. Drop it into your `mods/` folder.
3. Launch the game once to generate the config, or edit it beforehand at `config/hungercontrol-common.toml`.

## License

MIT — feel free to include in any modpack, private or public.

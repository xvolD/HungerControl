# Hunger Control

A lightweight **Forge 1.20.1** mod that lets modpack developers and server owners configure how fast players lose hunger.

## Features

- **Global exhaustion multiplier** — scale all hunger drain (sprinting, jumping, combat, regen, etc.) with a single config value.
- **Player-only** — only affects player hunger.
- **In-game commands** — check and reload settings without restarting.
- **No dependencies** — works out of the box.

## Config (`config/hungercontrol-common.toml`)

| Option | Default | Description |
|--------|---------|-------------|
| `enable` | `true` | Toggle the mod on/off. |
| `exhaustionMultiplier` | `1.0` | Global multiplier for hunger exhaustion. `0.5` = half speed, `0.2` = 5× slower. Range: `0.0` – `100.0`. |
| `affectPlayersOnly` | `true` | Currently always player-only; reserved for future expansion. |
| `debugLog` | `false` | Log exhaustion changes to the console for debugging. |

## Commands

Requires operator level 2 (cheats/op).

- `/hungercontrol info` — displays current multiplier and enabled state.
- `/hungercontrol reload` — reloads `hungercontrol-common.toml` from disk.

## Example Use-Cases

- **Realistic / medieval packs** — slow hunger down so players eat 2–3 times per in-game day instead of constantly.
- **Hardcore packs** — raise the multiplier above `1.0` to make food a real challenge.
- **Adventure maps** — fine-tune exactly how much stamina actions consume.

## Installation

1. Download `hungercontrol-<version>.jar`.
2. Drop it into your `mods/` folder alongside Forge 1.20.1.
3. Launch the game once to generate the config, or edit `config/hungercontrol-common.toml` beforehand.

## License

MIT — feel free to include in any modpack, private or public.

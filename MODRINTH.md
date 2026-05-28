Configurable hunger exhaustion multiplier for Forge 1.20.1–1.20.4. Fine-tune food drain speed globally via a simple config file.

# 🍖 Hunger Control

A lightweight, server-side friendly **Forge** mod for **Minecraft 1.20.1–1.20.4**, designed for modpack developers and server owners who want complete control over player hunger mechanics.

---

## ✨ Features

* **⚡ Global Exhaustion Multiplier** — Easily scale all hunger drain (sprinting, jumping, health regeneration, block breaking, and combat) using a single configuration value.
* **👥 Player-Focused** — Fine-tuned to affect only players without messing up vanilla mob mechanics.
* **🔄 Live Reloading** — Adjust your settings on the fly using in-game commands — no server restarts required!
* **📦 Zero Dependencies** — Works flawlessly out of the box with Forge.

---

## ⚙️ Configuration

Upon the first launch, the mod automatically generates a configuration file at `config/hungercontrol-common.toml`.

| Option | Default | Range | Description |
| :--- | :---: | :---: | :--- |
| **`enable`** | `true` | *boolean* | Toggle the entire mod functionality on or off. |
| **`exhaustionMultiplier`** | `1.0` | `0.0` – `100.0` | Global multiplier for hunger loss. <br>• `0.5` = half speed (slower hunger)<br>• `2.0` = double speed (faster hunger) |
| **`affectPlayersOnly`** | `true` | *boolean* | Reserved for future mob-specific hunger mechanics. |
| **`debugLog`** | `false` | *boolean* | Enables detailed exhaustion logs in the console for fine-tuning. |

---

## 💻 Commands

> ⚠️ *Note: All commands require Operator Level 2 (OP) or cheats enabled.*

* `/hungercontrol info` — Displays the current multiplier value and active mod state.
* `/hungercontrol reload` — Reloads the configuration file directly from the disk.

---

## 🔗 Links

* 💻 [GitHub Repository / Source Code](https://github.com/xvolD/HungerControl)

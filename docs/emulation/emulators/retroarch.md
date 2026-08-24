# RetroArch

RetroArch is a frontend for libretro cores, so its supported systems and requirements depend on the core you launch.

The latest version can be installed via the [Armada Store](../../using-armada/armada-store.md).

## Systems

RetroArch supports the following common systems in Armada's documentation.

| | |
| --- | --- |
| [NEC PC Engine / TurboGrafx-16](retroarch/pce-tg16.md) | [Sega Dreamcast](retroarch/dreamcast.md) |
| [Nintendo Game Boy / Game Boy Color](retroarch/gameboy.md) | [Sega Game Gear](retroarch/gamegear.md) |
| [Nintendo Game Boy Advance](retroarch/gba.md) | [Sega Genesis / Mega Drive](retroarch/genesis.md) |
| [Nintendo NES](retroarch/nes.md) | [Sega Master System](retroarch/mastersystem.md) |
| [Nintendo SNES](retroarch/snes.md) | [Sony PlayStation](retroarch/playstation.md) |

Use RetroArch's Core Updater to view all available system cores.

## BIOS

RetroArch has no global BIOS requirement. Firmware and BIOS files depend on the active core and the system being emulated.

## Paths

### ES-DE

| | |
| --- | --- |
| **ROM Folder** | *`[ES-DE System Name]`* |
| **ROM Files** | Varies by core and title; use the system-specific pages for the exact list of supported extensions. |

### Emulator

| | |
| --- | --- |
| **App Path** | `/var/lib/flatpak/app/org.libretro.RetroArch` |
| **Config Folder** | `/var/home/armada/.var/app/org.libretro.RetroArch/config/retroarch` |
| **Config File** | `/var/home/armada/.var/app/org.libretro.RetroArch/config/retroarch/retroarch.cfg` |
| **BIOS Folder** | `/var/home/armada/.var/app/org.libretro.RetroArch/config/retroarch/system` |
| **Saves Folder** | `/var/home/armada/.var/app/org.libretro.RetroArch/config/retroarch/saves` |
| **States Folder** | `/var/home/armada/.var/app/org.libretro.RetroArch/config/retroarch/states` |

## Links

| | |
| --- | --- |
| Homepage | <a href="https://www.retroarch.com/" target="_blank" rel="noopener noreferrer">retroarch.com</a> |
| Documentation | <a href="https://docs.libretro.com/" target="_blank" rel="noopener noreferrer">docs.libretro.com</a> |
| Source | <a href="https://github.com/libretro/RetroArch" target="_blank" rel="noopener noreferrer">github.com/libretro/RetroArch</a> |

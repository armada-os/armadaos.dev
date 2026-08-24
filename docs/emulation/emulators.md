!!! warning "Work In Progress"

    Armada does not provide any pre-configuration of emulators outside of some basic fixes.
    The current documentation is for early adopters and requires manual configuration.
    In the future, Armada will provide a more seamless experience with emulation.

## Supported Emulators

| Emulator | System | Rom Folder | Available in Armada Store |
| --- | --- | --- | :-: |
| [ARMSX2](emulators/armsx2.md) | Sony PlayStation 2 | `ps2` | ✅ |
| [Azahar Enhanced](emulators/azahar.md) | Nintendo 3DS | `n3ds` | ✅ |
| [Cemu Enhanced](emulators/cemu.md) | Nintendo Wii U | `wiiu` | ✅ |
| [Dolphin (GC)](emulators/dolphin-gc.md)<br>[Dolphin (Wii)](emulators/dolphin-wii.md) | Nintendo GameCube<br>Nintendo Wii | `gc`<br>`wii` | ✅ |
| [DuckStation](emulators/duckstation.md) | Sony PlayStation | `psx` | ✅ |
| [Flycast](emulators/flycast.md) | Sega Dreamcast | `dreamcast` | ✅ |
| [melonDS](emulators/melonds.md) | Nintendo DS | `nds` | ✅ |
| [PPSSPP](emulators/ppsspp.md) | Sony PlayStation Portable | `psp` | ✅ |
| [RetroArch](emulators/retroarch.md) | Multi-platform | *`[ES-DE System Name]`* | ✅ |
| [RPCS3](emulators/rpcs3.md) | Sony PlayStation 3 | `ps3` | ✅ |
| [ScummVM](emulators/scummvm.md) | Multi-platform | `scummvm` | ✅ |
| [Vita3K](emulators/vita3k.md) | Sony PlayStation Vita | `psvita` | ✅ |
| [xemu](emulators/xemu.md) | Microsoft Xbox | `xbox` | ✅ |
| [Xenia Edge](emulators/xenia-edge.md) | Microsoft Xbox 360 | `xbox360` | |

## Install Emulators

### Via Armada Store

In the [Armada Store](../using-armada/armada-store.md), select `Emulators`. Select the entry for the emulator to install, and pick `Install` when prompted.

### Manual Installations

Armada Store installs `.AppImage` emulators in `/var/home/armada/Applications`. Keep this in mind with manual setups that also interact with the Armada Store.

## Configuring Emulators

Each emulator will require manual configuration at this time.

Launch the emulator from Steam to keep the controller mapping consistent between game mode and desktop mode.

!!! note "Note About Armada Controller Mode"

    It is recommended to use the `Steam Deck` controller emulation in [Armada Control](../using-armada/armada-control.md) if you want to maintain compatibility with any future updates Armada may ship to the default emulation configuration.

Since this should be a one-time process, consider using an external keyboard and mouse to make the process quicker.

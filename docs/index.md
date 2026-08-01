# Introduction

Welcome to the Armada Wiki!

If you'd like to get started with Armada proceed to [Flashing to a SD Card](./Getting Started/Flashing to a SD Card.md)

!!! warning

    **Prototype software. Use at your own risk.** Armada is under active
    development and is not stable. Booting it requires flashing an ABL which
    could brick your device or corrupt your Android partition.
    
    **Over-the-air updates are experimental.** Armada can now update itself in
    place (see [Updating](./Getting Started/Updating.md)) instead of reflashing, but the update path
    is still being validated. If an update fails, reflashing the SD card is the
    reliable recovery.
    
    **Armada ships with a known default password.** The image ships with user
    `armada` / password `armada`. SSH is disabled by default, but if you enable it
    from Armada Control, anyone on your network can log in until you change the
    password.

Armada is a SteamOS-like Linux distribution for ARM handhelds built on Fedora bootc using
device support from ROCKNIX.

Includes:

- ARM64 Steam
- Latest FEX
- CachyOS Proton 11
- Desktop mode (KDE)
- Bazaar App Store
- Over-the-air updates
- Install to internal storage (alongside Android)
- Power and fan control in the Steam UI
- Per-game FEX and Proton settings (Decky plugin)

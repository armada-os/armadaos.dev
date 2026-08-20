---
hide:
  - navigation
  - toc
---

<div class="armada-hero" markdown>

![](assets/images/armada.svg){ .armada-hero__mark role="presentation" }

# Armada

## SteamOS-like Linux for ARM handhelds

Armada brings Steam, FEX, Proton, and a full Linux desktop to supported ARM64
gaming handhelds.

[Install Armada](getting-started/flashing-to-an-sd-card.md){ .md-button .md-button--primary }
[Check device support](devices/supported-devices.md){ .md-button }

</div>

!!! warning "Prototype software — read before installing"

    **Use Armada at your own risk.** Armada is under active development and is
    not stable. Booting it requires flashing an ABL, which could brick your
    device or corrupt your Android partition.

    **Over-the-air updates are experimental.** Armada can update itself in
    place (see [Updating](getting-started/updating.md)) instead of reflashing,
    but the update path is still being validated. If an update fails,
    reflashing the SD card is the reliable recovery.

    **Armada ships with a known default password.** The image ships with user
    `armada` and password `armada`. SSH is disabled by default, but if you
    enable it from Armada Control, anyone on your network can log in until you
    change the password.

## Find your way

<div class="grid cards" markdown>

-   **Get started**

    Confirm that your handheld is supported, prepare an SD card, and install
    Armada safely.

    [Read the installation guide](getting-started/flashing-to-an-sd-card.md)

-   **Use Armada**

    Learn about Armada Control, compatibility settings, power profiles, and
    Desktop Mode.

    [Explore Armada features](using-armada/index.md)

-   **Troubleshoot**

    Check current limitations and known workarounds before changing your
    installation.

    [Review known issues](troubleshooting/known-issues.md)

-   **Join the project**

    Find the source on GitHub, connect with the community, and see the projects
    Armada builds upon.

    [Visit the community page](project/community.md)

</div>

## Built for handheld PC gaming

Armada combines ARM64 Steam, FEX x86 translation, CachyOS Proton 11, a KDE
desktop, over-the-air updates, and handheld-focused power and fan controls. It
is built on Fedora bootc with device support derived from ROCKNIX.

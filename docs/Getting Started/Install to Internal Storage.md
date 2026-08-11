Once Armada is running from the SD card, you can install it to the device's
internal storage so it boots without the card. Open **Desktop Mode** and launch
**Armada Installer** from the **System** menu.

!!! warning

    Installing to internal storage repartitions internal storage and can require a
    PC ([`fastboot`](./Uninstalling and Restoring Android.md#install-fastboot)) to
    recover from a failed install. In most cases your Android
    partition will need to be resized, which will cause a **factory-reset**. 

The installer checks what is already on internal storage and offers:

- **Install alongside Android** (fresh device): choose how much storage Android
  keeps; Armada takes the rest. This **factory-resets Android** (you lose Android
  apps and data, but the Android system itself stays).
- **Reinstall / Switch to Armada** (a ROCKNIX or Armada install is already
  present): Armada replaces the existing Linux install and **leaves Android
  untouched**, with no resize or wipe.
- **Remove and restore Android**: erase the Armada/ROCKNIX install and give the
  whole disk back to Android (Android factory-resets on its next boot).

When it finishes, **power off, remove the SD card, then power on.** Internal
storage boots before the SD card.

If an install is interrupted, re-run Armada Installer from the SD card to finish.
If the device will not boot the SD card at all, force it back to the card with
`fastboot erase ROCKNIX` (see [Uninstall](./Uninstalling and Restoring Android.md) for the full steps).

## Overview

To remove or reinstall an internal install, run **Armada Installer** from the
**SD card**. You cannot modify the partitions you are currently booted from, so
neither can be done from the internal install itself.

!!! note

    The ABL bootloader prefers internal storage over the SD card,
    so while Armada is installed internally the device keeps booting the internal
    copy even with the card inserted. You first have to erase Armada's internal boot
    partition over `fastboot` to force it back to the SD card.

## Steps

1. **Enter the bootloader.** Power off, then hold **VOL-** while powering on and
   leave the device sitting in the bootloader.
2. **Erase the internal boot partition.** Connect the device to a PC and run:
   ```
   fastboot erase ROCKNIX
   ```
   Armada's boot partition is named `ROCKNIX` so the ROCKNIX-derived ABL finds it.
3. **Boot Armada from the SD card.** With the internal boot partition gone,
   reboot with the Armada SD card inserted and it boots from the card.
4. **Run Armada Installer.** Open **Desktop Mode** and launch **Armada
   Installer**. It detects the existing internal install and offers two choices:
   - **Reinstall Armada** (or **Switch to Armada** if ROCKNIX is installed)
     replaces the Linux install and leaves your Android untouched.
   - **Remove & Restore Android** erases the install and gives the whole disk
     back to Android, which factory-resets on its next boot.

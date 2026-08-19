## Overview

To remove or reinstall an internal install, run **Armada Installer** from the
**SD card**. You cannot modify the partitions you are currently booted from, so
neither can be done from the internal install itself.

!!! note

    The ABL bootloader prefers internal storage over the SD card,
    so while Armada is installed internally the device keeps booting the internal
    copy even with the card inserted. You first have to erase Armada's internal boot
    partition over `fastboot` to force it back to the SD card.

## Install fastboot

`fastboot` is included in the
[Android SDK Platform-Tools](https://developer.android.com/tools/releases/platform-tools).
Install it on the computer you will connect to the device:

- **Windows:** Download the Platform-Tools ZIP from the link above, extract it,
  and open PowerShell in the extracted `platform-tools` folder.
- **macOS:** Download and extract Platform-Tools, or install it with
  [Homebrew](https://formulae.brew.sh/cask/android-platform-tools):
  `brew install --cask android-platform-tools`.
- **Debian or Ubuntu:** Install the `fastboot` package:
  `sudo apt install fastboot`.
- **Fedora:** Install the `android-tools` package:
  `sudo dnf install android-tools`.
- **Arch Linux:** Install the `android-tools` package:
  `sudo pacman -S android-tools`.

Confirm that it is available before continuing:

```
fastboot --version
```

The commands below assume `fastboot` is on your `PATH`. If you downloaded and
extracted Platform-Tools instead, run the executable from that folder: use
`.\fastboot.exe` in Windows PowerShell or `./fastboot` on macOS and Linux.

## Steps

1. **Enter the bootloader.** Power off, then hold **VOL-** while powering on and
   leave the device sitting in the bootloader.
2. **Check the connection.** Connect the device to the computer with a USB cable
   and run `fastboot devices`. Continue only if the command lists the device.
3. **Erase the internal boot partition.** Run:

    ```
    fastboot erase ROCKNIX
    ```

    Armada's boot partition is named `ROCKNIX` so the ROCKNIX-derived ABL finds it.

4. **Boot Armada from the SD card.** With the internal boot partition gone,
   reboot with the Armada SD card inserted and it boots from the card.
5. **Run Armada Installer.** Open **Desktop Mode** and launch **Armada
   Installer**. It detects the existing internal install and offers two choices:

    - **Reinstall Armada** (or **Switch to Armada** if ROCKNIX is installed)
      replaces the Linux install and leaves your Android untouched.
    - **Remove & Restore Android** erases the install and gives the whole disk
      back to Android, which factory-resets on its next boot.

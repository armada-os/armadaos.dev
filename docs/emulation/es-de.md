!!! warning "Work In Progress"

    Armada does not provide any pre-configuration of emulators outside of some basic fixes.
    The current documentation is for early adopters and requires manual configuration.
    In the future, Armada will provide a more seamless experience with emulation.

## Overview

ES-DE is a popular frontend application for organizing and launching games, primarily for emulated systems.

## Installation

In the [Armada Store](../using-armada/armada-store.md), select `Applications`. Select the `ES-DE` entry, and pick `Install` when prompted.

## Configuration

The default location of the ES-DE configuration folder is: `/var/home/armada/ES-DE`

When installing from the Armada Store, custom configuration files will be created in `/var/home/armada/ES-DE/custom_systems/`. The files are:

| File | Description |
| --- | --- |
| `es_find_rules.xml` | Emulator mapping file. Contains paths to all supported emulators. |
| `es_systems.xml` | Game system mapping file. Contains run commands for all supported emulators.  |

## Usage

Refer to the [ES-DE User Guide](https://gitlab.com/es-de/emulationstation-de/-/blob/master/USERGUIDE.md) for more details on customizing and using ES-DE.

If an emulator opens a dialog that isn't visible or doesn't have a shortcut to exit, you can open the Steam menu to switch or close windows.

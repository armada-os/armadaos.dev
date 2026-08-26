---
hide:
  - toc
---

## Overview

Environment variables provide a way to tune system, driver, and compatibility layer options. Environment variables typically apply at the system or application level and can be overridden in Steam via a game's launch arguments.

## Using Environment Variables

Environment variables are prepended to the launch arguments in the properties of each game.

For example, the default launch arguments on a game in Armada are:

```
/usr/libexec/armada/armada-game-launch %command%
```

If a DirectX 12 feature level needs to be set for compatibility, and the frame rate should be limited to 60, prepend the existing launch arguments like:

```
VKD3D_FRAME_RATE=60 VKD3D_FEATURE_LEVEL=12_2 /usr/libexec/armada/armada-game-launch %command%
```

[Armada Control](../using-armada/armada-control.md) allows you to set environment variables on the default profile to apply to all games or on a per-game basis. Armada Control is also convenient for managing environment variables in one place instead of visiting each game's properties individually.


## Common Environment Variables

[DXVK_FRAME_RATE](#dxvk_frame_rate)<br>
[MESA_LOADER_DRIVER_OVERRIDE](#mesa_loader_driver_override)<br>
[MESA_VK_WSI_PRESENT_MODE](#mesa_vk_wsi_present_mode)<br>
[PROTON_USE_WINED3D](#proton_use_wined3d)<br>
[PROTON_USE_WOW64](#proton_use_wow64)<br>
[VKD3D_FEATURE_LEVEL](#vkd3d_feature_level)<br>
[VKD3D_FRAME_RATE](#vkd3d_frame_rate)<br>
[VKD3D_SHADER_MODEL](#vkd3d_shader_model)<br>

---


#### DXVK_FRAME_RATE

```
DXVK_FRAME_RATE=60
```

Applies a frame limit to games using DXVK.

---


#### MESA_LOADER_DRIVER_OVERRIDE

```
MESA_LOADER_DRIVER_OVERRIDE=zink
```

Overrides the driver loaded by Mesa. Most often used for better compatibility with OpenGL using the Zink driver, which translates OpenGL to Vulkan.

---


#### MESA_VK_WSI_PRESENT_MODE

```
MESA_VK_WSI_PRESENT_MODE=fifo
```

Sets the Vulkan presentation mode, which is effectively V-sync mode.

| Option | Presentation Mode | V-sync behavior | Effect |
| --- | --- | --- | --- |
| `immediate` | Immediate | Off | Lowest latency, but tearing is possible |
| `mailbox` | Mailbox | On | Low-latency, but less stable frame pacing |
| `relaxed` | Relaxed FIFO | Adaptive | Midpoint between low latency and stable frame pacing |
| `fifo` | FIFO | On | Most stable frame pacing, but higher latency |

!!! note "Inconsistent Frame Limiting When Using Vulkan"

    If performance is inconsistent when using the frame limiter in the QAM Performance tab in a game that uses Vulkan (native, DXVK, Zink), try enabling in-game V-sync and using `MESA_VK_WSI_PRESENT_MODE=fifo`. This can often make the frame limiter work as intended, especially when limiting FPS below the display refresh rate.

---


#### PROTON_USE_WINED3D
```
PROTON_USE_WINED3D=1
```

Use the WineD3D library instead of DXVK for DirectX 9-11 games. Can help with compatibility issues.

---


#### PROTON_USE_WOW64
```
PROTON_USE_WOW64=1
```

Runs 32-bit binaries in 64-bit WOW64 mode. Can improve compatibility with older games and is sometimes required when using newer Proton builds with `NTSYNC`.

---


#### VKD3D_FEATURE_LEVEL

```
VKD3D_FEATURE_LEVEL=12_0
```

Sets the DirectX feature level exposed to the game when using VKD3D. Lower values can improve compatibility.

| Option | Description |
| --- | --- |
| `11_0` | DirectX 11.0-level features |
| `11_1` | DirectX 11.1-level features |
| `12_0` | DirectX 12.0-level features |
| `12_1` | DirectX 12.1-level features |
| `12_2` | DirectX 12.2-level features |

---


#### VKD3D_FRAME_RATE

```
VKD3D_FRAME_RATE=60
```

Applies a frame limit to games using VKD3D.

---


#### VKD3D_SHADER_MODEL

```
VKD3D_SHADER_MODEL=6_6
```

Sets the highest shader model a game can use when using VKD3D. Lower values can improve compatibility.

| Option | Description |
| --- | --- |
| `6_0` | Shader Model 6.0 |
| `6_1` | Shader Model 6.1 |
| `6_2` | Shader Model 6.2 |
| `6_3` | Shader Model 6.3 |
| `6_4` | Shader Model 6.4 |
| `6_5` | Shader Model 6.5 |
| `6_6` | Shader Model 6.6 |
| `6_7` | Shader Model 6.7 |
| `6_8` | Shader Model 6.8 |
| `6_9` | Shader Model 6.9 |

---

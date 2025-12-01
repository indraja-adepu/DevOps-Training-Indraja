# 1. Operating System
### what?
main software that helps you use your computer.
Without it, your device is just a box of hardware that can’t do anything.
### why OS?
OS is the middleman between you and the computer hardware.
It helps apps run, manages files, memory, storage, keyboard, screen — everything.

**Simple Analogy :**
Why Chef (OS) is needed?

You can’t directly go into the kitchen (hardware) and cook a dish (run apps).
The chef (OS) understands your order (open Chrome, open Word, start a game),
and uses the kitchen tools (CPU, memory, disk) to prepare it.
Without OS = No chef → restaurant cannot function.

### Key Responsibilities
<img width="400" height="400" alt="image" src="https://github.com/user-attachments/assets/e7561e66-a18c-493d-b0c1-8755671de161" />

Manages Resources, Users, FileSystem, Memory, Processes

### Multiple OS - why Linux (Mac/Windows/Linux Comparision)
**Windows**(GUI-focused, less secure), **Linux**(CLI-focused, secure, file-system oriented), **Mac** (hybrid)

**why Linux?** -- **Security**

Linux is more secure because it follows a strict “**deny first**, allow only minimal access” model — this is called **least privilege.**

# 2. Linux Architecture (Layered View)
```plaintext
+----------------------------------------------------+
| User Applications (Vim, Docker, Apache, etc.)     |
+----------------------------------------------------+
| Shell (bash, zsh, sh - Command Interpreters)      |  <-- Part of the OS
+----------------------------------------------------+
| System Libraries (glibc, systemd, etc.)           |  <-- Part of the OS
+----------------------------------------------------+
| System Utilities (ls, grep, systemctl, etc.)      |  <-- Part of the OS
+----------------------------------------------------+
| Linux Kernel (Process, Memory, FS, Network)       |  <-- Core of the OS
+----------------------------------------------------+
| Hardware (CPU, RAM, Disk, Network, Peripherals)   |
+----------------------------------------------------+

Linux Kernel: Key Responsibilities
• Process Management - Process Lifecycle ()      
• Memory Management       
• File System Management                 
• Device Drivers                         
• Network Stack                             







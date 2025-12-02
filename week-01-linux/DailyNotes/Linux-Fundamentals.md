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
```
### Boot Process
| Step                                | Purpose             | Simple Explanation                                                  |
| ----------------------------------- | ------------------- | ------------------------------------------------------------------- |
| **1. BIOS / UEFI**                  | Hardware Check      | BIOS checks if RAM, CPU, keyboard, etc. are working (POST test).    |
| **2. Bootloader (GRUB)**            | Loads OS            | Bootloader chooses which OS to start and loads the Linux kernel.    |
| **3. Kernel Initialization**        | Controls System     | Linux kernel loads into RAM and takes control of hardware & system. |
| **4. Init System (systemd / init)** | Starts Services     | Init starts basic processes (network, logging, etc.).               |
| **5. System Services**              | Background Programs | Starts services like network manager, display manager, ssh, etc.    |
| **6. Login Prompt**                 | User Login          | Shows login screen (Terminal or GUI) for the user to log in.        |


### Linux Kernel: Key Responsibilities
• Process Management - Process Lifecycle ()      
• Memory Management       
• File System Management                 
• Device Drivers                         
• Network Stack                             

### File System in Linux

<img width="719" height="631" alt="image" src="https://github.com/user-attachments/assets/28860e48-d393-4b81-b740-baffaffb6c78" />






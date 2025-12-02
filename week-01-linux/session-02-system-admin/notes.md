# System Administration

### User & Group Management

Key files involved in user management:
- `/etc/passwd` – Stores user account details.
- `/etc/shadow` – Stores encrypted user passwords.
- `/etc/group` – Stores group information.
- `/etc/gshadow` – Stores secure group details.

### `useradd` Command 
```bash
useradd username
```
To create a user with a home directory:
```bash
useradd -m username
```
To specify a shell:
```bash
useradd -s /bin/bash username
```

## Working with Groups
### Creating Groups
```bash
groupadd groupname
```## Working with Groups
### Creating Groups
```bash
groupadd groupname
```
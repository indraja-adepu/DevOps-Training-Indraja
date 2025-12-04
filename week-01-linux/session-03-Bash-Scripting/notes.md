# Bash Scripting – Practical Learning Guide
For DevOps, Automation & Real-World Workflows

---

## Why Learn Bash?

In DevOps, you repeat operational tasks frequently:
Deployments, log scrubbing, Kubernetes health checks, server maintenance.

If it is repeated more than 3 times → Script it!

| Scenario | Manual Work | With Bash |
|---------|-------------|-----------|
| Clean logs in 50 servers | SSH into each server | Loop cleans all |
| Check Kubernetes pod health | Manual kubectl checking | Script + cron alerts |
| Search inside 2GB logs | Manual scrolling | grep filters instantly |

---

## How Commands Run in Linux

```
┌──────────────────────────────────┐
│ User (You trigger the action)    │
└──────────────────────────────────┘
                ↓
┌──────────────────────────────────┐
│ Shell (bash / sh / zsh)          │
└──────────────────────────────────┘
                ↓
┌──────────────────────────────────┐
│ Utilities (ls, grep, sed, awk)   │
└──────────────────────────────────┘
                ↓
┌──────────────────────────────────┐
│ Kernel (Executes system calls)   │
└──────────────────────────────────┘
```

---

## Shell Script Structure

```bash
#!/bin/bash        # Interpreter (Shebang)
# Author: DevOps Engineer
# Purpose: Greeting Script

name="Learner"
echo "Welcome $name!"
```

---

## Deep Dive: Variables & Arguments

### Variables

```bash
env="production"
echo "Deploying to $env"
```

Rules:
- No spaces: `name=value`
- Case-sensitive

Command output as variable:

```bash
server=$(hostname)
echo "Running on $server"
```

---

### Script Arguments

```bash
./deploy.sh dev
```

Inside script:

```bash
echo "Environment is: $1"
echo "Total arguments: $#"
```

| Symbol | Meaning |
|--------|--------|
| `$0` | Script name |
| `$1…$n` | Positional parameters |
| `$#` | Number of arguments |
| `$?` | Exit code of last command |

---

### Exit Codes

| Code | Meaning |
|------|--------|
| 0 | Success |
| 1 | Generic error |
| 127 | Command not found |
| 130 | Ctrl+C termination |

Check exit status:

```bash
cp build.jar /deploy/
if [ $? -ne 0 ]; then
    echo "Copy Failed!"
    exit 1
fi
```

---

## Deep Dive: Text Processing Tools

### grep — Search Patterns

```bash
grep -i "ERROR" /var/log/app.log
```

---

### sed — Replace / Modify Text

```bash
sed -i 's/dev/prod/g' config.yaml
```

---

### awk — Extract Columns

From log:

```
user1 SUCCESS 200
user2 FAIL    500
```

Extract failures:

```bash
awk '$2=="FAIL" {print $1,$3}' logs.txt
```

---

## Conditional Logic

```bash
if [ -f "/etc/passwd" ]; then
  echo "File exists"
else
  echo "File missing"
fi
```

### Case Example

```bash
case $1 in
 start) systemctl start nginx ;;
 stop)  systemctl stop nginx ;;
 *)     echo "Usage: start|stop" ;;
esac
```

---

## Loops for Automation

```bash
for srv in web1 web2 web3; do
  ssh $srv "sudo systemctl restart nginx"
done
```

### While Loop

```bash
count=1
while [ $count -le 5 ]; do
  echo "Run $count"
  ((count++))
done
```

---

## Functions

```bash
log(){
  echo "[INFO] $(date) - $1"
}

log "Deployment started"
```

---

## Arrays

```bash
envs=("dev" "test" "prod")
echo ${envs[2]}    # prod
```

---

## Error Handling Best Practices

```bash
set -euo pipefail
```

| Option | Protects From |
|--------|---------------|
| -e | Continue after errors |
| -u | Undefined variables |
| pipefail | Silent pipeline failures |

Debug mode:
```bash
set -x
```

---

## Cron Scheduling

Run backup daily at 2:30 AM:

```
30 2 * * * /usr/local/bin/backup.sh
```

---

## Real DevOps Bash Scripts

### Kubernetes Pod Health Check

```bash
#!/bin/bash
pod=$1

if kubectl get pod $pod -n default | grep -q Running; then
  echo "Healthy"
else
  echo "Not Running"
fi
```

---

### Log Rotation Script

```bash
tar -czf logs_$(date +%F).tgz /var/log/myapp/
rm -f /var/log/myapp/*.log
```

---

### Validate Build Type in CI/CD

```bash
if [ ! -f "pom.xml" ]; then
  echo "Not a Maven project"
  exit 1
fi
```

---

## Script Execution Flow

```
      ┌───────────────────┐
      │ Start Script      │
      └─────────┬─────────┘
                ↓
      Check Input Arguments?
        ↓        ↘
      Yes        No → exit 1
        ↓
      Execute Commands
        ↓
      Validate Exit Codes
        ↓
      Log Results
        ↓
      Exit Safely
```

---

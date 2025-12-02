### Explanation:

created a zombie process using a simple Python script by forking a child and allowing the child to exit immediately while the parent slept for a long time.

Opened two sessions into my Azure Linux VM:

### Session 1: ran the python script

![alt text](image-2.png)

### Session 2: ran commands to identify and kill zombie  



### commands used to identfy zombie

 ps aux | grep " Z"

 ps -eo pid,ppid,stat | grep Z

![alt text](image-3.png)

  kill -9 ppid - to kill the parent process

![alt text](image-4.png)



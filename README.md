## Application (Container) Lifecycle on resin.io:

**Note:** This project was run on resinOS `1.24.1` and `2.0.0-beta10.rev1` on the Raspberry Pi 3. On older versions, its not guaranteed that the signals will be propagated from docker to the container as these things were changed in recent versions (I think around 1.11+).

This project catches the SIGTERM signal when the container is restarted or the device is rebooted from the dashboard. Obviously if you yank the power out, you won't get an SIGTERM. The python project both tries to print to screen and write to a file when it catches the SIGTERM. Sometime it won't send the print statement to the logs fast enough, but hopefully should always write to the file.

If you are using a bash script to start your code, you will need to trap the SIGTERM in the bash script and propagate it onto the child processes (unless systemd is enables, then I believe this will be handled for you.) For more info on how to do this, check out this article: http://veithen.github.io/2014/11/16/sigterm-propagation.html

#### Example Output with systemd enabled:
```
17.02.17 18:57:02 [+0000] Started application 'registry.resinstaging.io/rpi3/123deadbeeef'
17.02.17 18:57:02 [+0000] Systemd init system enabled.
17.02.17 18:57:02 [+0000] systemd 215 running in system mode. (+PAM +AUDIT +SELINUX +IMA +SYSVINIT +LIBCRYPTSETUP +GCRYPT +ACL +XZ -SECCO
MP -APPARMOR)
17.02.17 18:57:02 [+0000] Detected virtualization 'other'.
17.02.17 18:57:02 [+0000] Detected architecture 'arm'.
17.02.17 18:57:02 [+0000] Set hostname to <dad94d5-dad94d5>.
17.02.17 18:57:05 [+0000] my pid is 156
17.02.17 18:57:05 [+0000] RESIN envvars
17.02.17 18:57:05 [+0000]
17.02.17 18:57:05 [+0000] RESIN 1
17.02.17 18:57:05 [+0000] RESIN_APP_ID 18002
17.02.17 18:57:05 [+0000] RESIN_SUPERVISOR_ADDRESS http://127.0.0.1:48484
17.02.17 18:57:05 [+0000] RESIN_SUPERVISOR_VERSION 3.0.0
17.02.17 18:57:05 [+0000] RESIN_APP_NAME rpi3
17.02.17 18:57:05 [+0000] RESIN_SUPERVISOR_PORT 48484
17.02.17 18:57:05 [+0000] RESIN_SUPERVISOR_API_KEY cdeadbeef4449fe8b3034dbeefeea5eef23e123452d7fce912c83ea7
17.02.17 18:57:05 [+0000] RESIN_DEVICE_UUID dad94d5f6fea724b1f1374f14304d4f6e0f88c8bfa2f8a31608f845eefef83
17.02.17 18:57:05 [+0000] RESIN_DEVICE_NAME_AT_INIT restless-star
17.02.17 18:57:05 [+0000] RESIN_HOST_OS_VERSION Resin OS 2.0.0-beta10.rev1
17.02.17 18:57:05 [+0000] RESIN_SUPERVISOR_HOST 127.0.0.1
17.02.17 18:57:05 [+0000] RESIN_DEVICE_TYPE raspberrypi3
17.02.17 18:57:05 [+0000] RESIN_APP_RELEASE 123deadbeeef
17.02.17 18:57:05 [+0000] Now I'm just gonna wait around here for something to happen...
17.02.17 18:57:15 [+0000] still waiting around...
17.02.17 18:57:25 [+0000] still waiting around...
17.02.17 18:57:35 [+0000] still waiting around...
17.02.17 18:57:45 [+0000] still waiting around...
17.02.17 18:57:15 [+0000] still waiting around...
17.02.17 18:57:25 [+0000] still waiting around...
17.02.17 18:57:35 [+0000] still waiting around...
17.02.17 18:57:45 [+0000] still waiting around...
17.02.17 18:57:55 [+0000] still waiting around...
17.02.17 18:58:03 [+0000] Updating application 'registry.resinstaging.io/rpi3/123deadbeeef'
17.02.17 18:58:03 [+0000] Killing application 'registry.resinstaging.io/rpi3/123deadbeeef'
17.02.17 18:58:03 [+0000] got SIGTERM
17.02.17 18:58:03 [+0000]
17.02.17 18:58:03 [+0000] Sending SIGTERM to remaining processes...
17.02.17 18:58:03 [+0000] Sending SIGKILL to remaining processes...
17.02.17 18:58:03 [+0000] Unmounting file systems.
17.02.17 18:58:03 [+0000] Unmounting /sys/kernel/debug.
17.02.17 18:58:03 [+0000] Unmounting /dev/mqueue.
17.02.17 18:58:03 [+0000] All filesystems unmounted.
17.02.17 18:58:03 [+0000] Halting system.
17.02.17 18:58:03 [+0000]
17.02.17 18:58:03 [+0000] Application exited 'registry.resinstaging.io/rpi3/123deadbeeef'
```

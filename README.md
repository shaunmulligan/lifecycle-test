## Application (Container) Lifecycle on resin.io:

**Note:** This project was run on resinOS 1.24.1 on the Raspberry Pi 3. On older versions, its not guaranteed that the signals will be propagated from docker to the container as these things were changed in recent versions.

This project catches the SIGTERM signal when the container is restarted or the device is rebooted from the dashboard. Obviously if you yank the power out, you won't get an SIGTERM. The python project both tries to print to screen and write to a file when it catches the sigterm. Sometime it won't send the print statement fast enough.

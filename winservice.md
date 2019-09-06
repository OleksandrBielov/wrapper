
`winserver.py` requires following parameters
```cmd
.\winservice.py setup <configuration file>
.\winservice.py COMMAND <servicename>
```
or (on Python)
```python
import winservice

winservice.start("setup", "<configuration file>")
winservice.start("COMMAND", "<servicename>")
```
the **COMMAND** takes one of the following values

| parameter  | description |
| ------------- | ------------- |
||`Service installation` |
| setup |sutup a service  |
| install |setup and run service|
||`Service removal`| 
|remove|removing a service|
||`Service management`| 
|start|starting a service|
|stop|stopping a service|
|restart|restarting a service|
|status|querying a service's status|
|pause|pause a service|
|continue|continue a service (after *pause*)|
|enable|set the service to automatic startup|
|disable|disable automatic startup|

*See `winservice_config.md` to view the configuration file*

import winservice

winservice.start("setup", "diagnostics.nssm")
winservice.start("start", "dcos-diagnostics")

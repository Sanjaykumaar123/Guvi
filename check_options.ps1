try {
    $url = "https://guvi-unified-api.onrender.com/honeypot"
    $request = [System.Net.WebRequest]::Create($url)
    $request.Method = "OPTIONS"
    $response = $request.GetResponse()
    Write-Host "✅ OPTIONS Request: Success" -ForegroundColor Green
    Write-Host "   Status Code: $([int]$response.StatusCode)"
    Write-Host "   Headers: $($response.Headers)"
}
catch {
    Write-Host "❌ OPTIONS Request Failed: $_" -ForegroundColor Red
    if ($_.Exception.Response) {
        Write-Host "   Status Code: $([int]$_.Exception.Response.StatusCode)"
    }
}

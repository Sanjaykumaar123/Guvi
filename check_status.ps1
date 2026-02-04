function Test-Url ($url) {
    Write-Host "`nTesting: $url" -ForegroundColor Cyan
    try {
        $response = Invoke-RestMethod -Uri "$url/" -Method Get -ErrorAction Stop
        Write-Host "✅ Root: UP" -ForegroundColor Green
        Write-Host "   Service: $($response.service)"
    }
    catch {
        Write-Host "❌ Root: DOWN ($($_.Exception.Message))" -ForegroundColor Red
        return
    }

    try {
        $headers = @{ "x-api-key" = "guvi123" }
        $hp = Invoke-RestMethod -Uri "$url/honeypot" -Method Post -Headers $headers -Body "{}" -ContentType "application/json" -ErrorAction Stop
        Write-Host "✅ Honeypot: UP" -ForegroundColor Green
        Write-Host "   Status: $($hp.status)"
    }
    catch {
        Write-Host "❌ Honeypot: DOWN ($($_.Exception.Message))" -ForegroundColor Red
    }
}

Test-Url "https://guvi-unified-api.onrender.com"
Test-Url "https://guvi-qigw.onrender.com"

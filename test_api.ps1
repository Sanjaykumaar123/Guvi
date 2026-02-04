$api_url = "https://guvi-unified-api.onrender.com"
Write-Host "Testing API at $api_url" -ForegroundColor Cyan

# Test 1: GET Root
try {
    $response = Invoke-RestMethod -Uri "$api_url/" -Method Get
    Write-Host "✅ Root Endpoint: Success" -ForegroundColor Green
    $response
} catch {
    Write-Host "❌ Root Endpoint: Failed $_" -ForegroundColor Red
}

# Test 2: Honeypot Test
$headers = @{ "x-api-key" = "guvi123" }
try {
    $response = Invoke-RestMethod -Uri "$api_url/honeypot" -Method Post -Headers $headers -Body "{}" -ContentType "application/json"
    Write-Host "✅ Honeypot Endpoint: Success" -ForegroundColor Green
    $response
} catch {
    Write-Host "❌ Honeypot Endpoint: Failed $_" -ForegroundColor Red
}

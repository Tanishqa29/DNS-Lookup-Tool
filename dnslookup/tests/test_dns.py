from dnslookup.resolver import lookup

def test_lookup():
    result = lookup("google.com")
    assert result.domain == "google.com"

def test_healthz(web):
    r = web.get("/healthz")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"


def test_index_is_signed_in_and_data_connected(web):
    r = web.get("/", headers={"x-amzn-oidc-identity": "priya.nair@demo.local"})
    assert r.status_code == 200
    assert "priya.nair@demo.local" in r.text
    assert "8</strong> vendors" in r.text  # fixture data reaches the page


def test_whoami_page(web):
    r = web.get("/whoami", headers={"x-demo-user": "me@demo.local", "x-demo-groups": "finance"})
    assert r.status_code == 200
    assert "me@demo.local" in r.text and "local development" in r.text

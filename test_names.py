import requests

def test_get_pizza_names():
    site = "https://quickpizza.grafana.com"
    res = requests.get(site + "/api/names")

    assert res.status_code == 200
    assert "Margherita" in res.json()["names"]
import requests

AUTH = {"Authorization": "token abcdef0123456789"}

def test_get_tools():
    site = "https://quickpizza.grafana.com"
    res = requests.get(site + "/api/tools", headers=AUTH)

    assert res.status_code == 200
    assert res.json() == {"tools": ["Knife", "Pizza cutter", "Scissors"]}
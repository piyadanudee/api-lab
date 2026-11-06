import pytest


# The pizza never needs a tool that the customer excluded.
@pytest.mark.parametrize(
    "excluded",
    [
        ["Knife"],
        ["Scissors"],
        [],
        ["Knife", "Scissors"],
    ],
)
def test_excluded_tool_is_not_used(api, auth, excluded):
    body = {"excludedTools": excluded}
    res = api.post("/api/pizza", json=body, headers=auth)
    assert res.status_code == 200
    assert res.json()["pizza"]["tool"] not in excluded

@pytest.mark.xfail(
    reason="Defect 1: Excluding all three tools returns 500 instead of 400 with a JSON error message.",
    strict=True,
)

# A request that excludes all tools is refused with an error message.
def test_excluding_all_tools_is_refused(api, auth):
    body = {"excludedTools": ["Knife", "Pizza cutter", "Scissors"]}
    res = api.post("/api/pizza", json=body, headers=auth)
    assert res.status_code == 400
    assert "error" in res.json()
    assert isinstance(res.json()["error"], str)
def test_other_user_cannot_read_rating(api, auth, other_auth, rating):
    path = f"/api/ratings/{rating['id']}"

    # Another user tries to read the rating.
    res = api.get(path, headers=other_auth)
    print("Read status:", res.status_code)
    assert 400 <= res.status_code <= 499

    # The owner checks that the rating is unchanged.
    res = api.get(path, headers=auth)
    assert res.status_code == 200
    assert res.json() == rating


def test_other_user_cannot_update_rating(api, auth, other_auth, rating):
    path = f"/api/ratings/{rating['id']}"

    # Another user tries to change the rating.
    res = api.put(path, json={"stars": 5}, headers=other_auth)
    print("Update status:", res.status_code)
    assert 400 <= res.status_code <= 499

    # The owner checks that the rating is unchanged.
    res = api.get(path, headers=auth)
    assert res.status_code == 200
    assert res.json() == rating


def test_other_user_cannot_delete_rating(api, auth, other_auth, rating):
    path = f"/api/ratings/{rating['id']}"

    # Another user tries to delete the rating.
    res = api.delete(path, headers=other_auth)
    print("Delete status:", res.status_code)
    assert 400 <= res.status_code <= 499

    # The owner checks that the rating is unchanged.
    res = api.get(path, headers=auth)
    assert res.status_code == 200
    assert res.json() == rating
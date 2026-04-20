def test_get_activities_returns_seeded_data(client):
    # Arrange
    expected_activity = "Chess Club"

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    payload = response.json()
    assert expected_activity in payload
    assert payload[expected_activity]["participants"] == [
        "michael@mergington.edu",
        "daniel@mergington.edu",
    ]


def test_get_activities_exposes_activity_details(client):
    # Arrange
    activity_name = "STEM Robotics"

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    payload = response.json()
    assert payload[activity_name]["description"] == (
        "Build and program robots for science and engineering challenges"
    )
    assert payload[activity_name]["max_participants"] == 14
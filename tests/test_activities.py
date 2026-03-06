def test_get_activities_returns_all_activities(client):
    # Arrange
    expected_count = 9

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert len(data) == expected_count


def test_get_activities_includes_chess_club_details(client):
    # Arrange
    activity_name = "Chess Club"

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert activity_name in data
    assert data[activity_name]["description"] == "Learn strategies and compete in chess tournaments"
    assert data[activity_name]["schedule"] == "Fridays, 3:30 PM - 5:00 PM"
    assert data[activity_name]["max_participants"] == 12
    assert "michael@mergington.edu" in data[activity_name]["participants"]

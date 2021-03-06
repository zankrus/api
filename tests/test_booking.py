from model.booking import BookingData


def test_create_booking(auth_client):
    booking_data = BookingData().random()
    res = auth_client.create_booking(booking_data)
    assert res.status_code == 200
    assert "bookingid" in str(res.content)



def test_negative_booking(unauth_client):
    booking_data = BookingData(firstname=1)
    res = unauth_client.create_booking(booking_data)
    assert res.status_code == 500
    assert res.content == b'Internal Server Error'

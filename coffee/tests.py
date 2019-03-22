from rest_framework.test import APITestCase

from coffee.models import Coffee, power_status


class CoffeeAPITest(APITestCase):
    fixtures = ["api.json"]

    def test_get(self):
        resp = self.client.get("/api/v1/coffee/now")
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(
            resp.data,
            {
                "id": 3,
                "measured_at": "2019-02-08T19:55:04+01:00",
                "is_powered": 0,
                "started_brewing": "2019-02-08T19:55:04+01:00",
                "temperature": 18.2,
                "amount": 0.3,
                "outages": "00:33:21",
            },
        )

    def test_latest_coffee(self):
        coffee = Coffee.objects.all()[0]
        self.assertEqual(coffee.temperature, 18.2)
        self.assertEqual(coffee.amount, 0.3)

    def test_get_all(self):
        resp = self.client.get("/api/v1/coffee/")
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.data), 3)

    def test_power_status(self):
        power = 32.12
        self.assertEqual(power_status(power), 1)
        power = 0
        self.assertEqual(power_status(power), 0)
        power = 2415.00
        self.assertEqual(power_status(power), 2)

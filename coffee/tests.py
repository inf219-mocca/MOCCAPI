from rest_framework.test import APITestCase

from coffee.models import Coffee, power_status


class CoffeeAPITest(APITestCase):
    maxDiff = None
    fixtures = ["coffee.json", "brew.json"]

    def test_get(self):
        resp = self.client.get("/api/v1/coffee/now")
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(
            resp.data,
            {
                "id": 75,
                "measured_at": "2019-03-04T14:21:36.130000+01:00",
                "temperature": 28.23,
                "amount": 0.814_041_931_277_405_9,
                "is_powered": 2,
                "brew_started": "2019-03-05T10:11:04.882000+01:00",
                "brew_outages": None,
            },
        )

    def test_latest_coffee(self):
        coffee = Coffee.objects.all()[10]
        self.assertEqual(coffee.temperature, 30.25)
        self.assertEqual(round(coffee.amount, 3), round(0.1029, 3))

    def test_get_all(self):
        resp = self.client.get("/api/v1/coffee/")
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.data), 25)

    def test_power_status(self):
        power = 32.12
        self.assertEqual(power_status(power), 1)
        power = 0
        self.assertEqual(power_status(power), 0)
        power = 2415.00
        self.assertEqual(power_status(power), 2)

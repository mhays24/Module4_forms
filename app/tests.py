from django.test import SimpleTestCase


# Create your tests here.
class Test_Warm_up_2(SimpleTestCase):
    def test_Chocolate2(self):
        response = self.client.get("/warmup-2/font_times/?text=Chocolate&number=2")
        print(response)
        self.assertContains(response, "Result: ChoCho")

    # def Chocolate3(self):
    #     response = self.client.get("/warmup-1/near-hundred/90/")
    #     self.assertContains(response, "True")

    # def Abc3(self):
    #     response = self.client.get("/warmup-1/near-hundred/89/")
    #     self.assertContains(response, "False")

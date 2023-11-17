from django.test import SimpleTestCase


# Create your tests here.
class Test_Warm_up_2(SimpleTestCase):
    def test_Chocolate2(self):
        response = self.client.get("/warmup-2/font_times/?text=Chocolate&number=2")
        print(response)
        self.assertContains(response, "ChoCho")

    def test_Chocolate3(self):
        response = self.client.get("/warmup-2/font_times/?text=Chocolate&number=3")
        self.assertContains(response, "ChoChoCho")

    def test_Abc3(self):
        response = self.client.get("/warmup-2/font_times/?text=Abc&number=3")
        self.assertContains(response, "AbcAbcAbc")


class Test_Logic_2(SimpleTestCase):
    def test_1_2_3(self):
        response = self.client.get("/logic-2/no-teen-sum/?a=1&b=2&c=3")
        self.assertContains(response, "6")

    def test_2_13_1(self):
        response = self.client.get("/logic-2/no-teen-sum/?a=2&b=13&c=1")
        self.assertContains(response, "3")

    def test_2_1_14(self):
        response = self.client.get("/logic-2/no-teen-sum/?a=2&b=1&c=14")
        self.assertContains(response, "3")

class Test_String_2(SimpleTestCase):
    def test_abcxyz(self):
        response = self.client.get("/string-2/xyz-there/?word=abcxyz")
        self.assertContains(response, "True")

    def test_abc_xyz(self):
        response = self.client.get("/string-2/xyz-there/?word=abc.xyz")
        self.assertContains(response, "False")

    def test_xyz_abc(self):
        response = self.client.get("/string-2/xyz-there/?word=xyz.abc")
        self.assertContains(response, "True")

class Test_List_2(SimpleTestCase):
    def test_1_2_3(self):
        response = self.client.get("/list-2/centered-average/?numbers=1%2C+2%2C+3%2C+4%2C+100")
        self.assertContains(response, "3")

    def test_1_1_5_5_10_8_7(self):
        response = self.client.get("/list-2/centered-average/?numbers=1%2C+1%2C+5%2C+5%2C+10%2C+8%2C+7")
        self.assertContains(response, "5")

    def test_minus_10_4_2_4_2_0(self):
        response = self.client.get("/list-2/centered-average/?numbers=-10%2C+-4%2C+-2%2C+-4%2C+-2%2C+0")
        self.assertContains(response, "-3")
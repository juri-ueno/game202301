import unittest
import animalgame
from unittest import TestCase

class TestAnimalGame(unittest.TestCase):

    def setUp(self):
        self.chara = animalgame.Chara(animalgame.Animal.KUMA, "animalserihutest.txt")

    def test_icon(self):
        self.assertEqual('🧸', self.chara.icon)

    def test_sitsumon(self):
        self.assertEqual('なんさいなの?', self.chara.get_sitsumon(0))

    def test_kotae(self):
        self.assertEqual('好きな星座おしえてん', self.chara.get_kotae(3))

    def test_sitsumon_ikutu(self):
        self.assertEqual(20, self.chara.get_sitsumon_ikutu())

    def test_kotae_ikutu(self):
        self.assertEqual(31, self.chara.get_kotae_ikutu())

    def test_point_initial(self):
        self.assertEqual(0, self.chara.sodateta_kaisu)
        self.assertEqual(0, self.chara.tabeta_kaisu)
        self.assertEqual(0, self.chara.ohirune_kaisu)
        self.assertEqual(0, self.chara.ohanasi_kaisu)
        self.assertEqual(0, self.chara.get_point())

    def test_point_sodateru_gohan1(self):
        self.chara.sodateru(animalgame.Jikan.GOHAN)
        self.assertEqual(1, self.chara.sodateta_kaisu)
        self.assertEqual(1, self.chara.tabeta_kaisu)
        self.assertEqual(0, self.chara.ohirune_kaisu)
        self.assertEqual(0, self.chara.ohanasi_kaisu)
        self.assertEqual(1, self.chara.get_point())


    def test_point_sodateru_gohan2(self):
        self.chara.sodateru(animalgame.Jikan.GOHAN)
        self.chara.sodateru(animalgame.Jikan.GOHAN)
        self.assertEqual(2, self.chara.sodateta_kaisu)
        self.assertEqual(2, self.chara.tabeta_kaisu)
        self.assertEqual(0, self.chara.ohirune_kaisu)
        self.assertEqual(0, self.chara.ohanasi_kaisu)
        self.assertEqual(2, self.chara.get_point())

    def test_point_sodateru_hirune1(self):
        self.chara.sodateru(animalgame.Jikan.OHIRUNE)
        self.assertEqual(1, self.chara.sodateta_kaisu)
        self.assertEqual(0, self.chara.tabeta_kaisu)
        self.assertEqual(1, self.chara.ohirune_kaisu)
        self.assertEqual(0, self.chara.ohanasi_kaisu)
        self.assertEqual(0, self.chara.get_point())

    def test_point_sodateru_hirune2(self):
        self.chara.sodateru(animalgame.Jikan.OHIRUNE)
        self.chara.sodateru(animalgame.Jikan.OHIRUNE)
        self.assertEqual(2, self.chara.sodateta_kaisu)
        self.assertEqual(0, self.chara.tabeta_kaisu)
        self.assertEqual(2, self.chara.ohirune_kaisu)
        self.assertEqual(0, self.chara.ohanasi_kaisu)
        self.assertEqual(0, self.chara.get_point())

    def test_point_sodateru_ohanasi1(self):
        self.chara.sodateru(animalgame.Jikan.OHANASI)
        self.assertEqual(1, self.chara.sodateta_kaisu)
        self.assertEqual(0, self.chara.tabeta_kaisu)
        self.assertEqual(0, self.chara.ohirune_kaisu)
        self.assertEqual(1, self.chara.ohanasi_kaisu)
        self.assertEqual(1, self.chara.get_point())

    def test_point_sodateru_ohanasi2(self):
        self.chara.sodateru(animalgame.Jikan.OHANASI)
        self.chara.sodateru(animalgame.Jikan.OHANASI)
        self.assertEqual(2, self.chara.sodateta_kaisu)
        self.assertEqual(0, self.chara.tabeta_kaisu)
        self.assertEqual(0, self.chara.ohirune_kaisu)
        self.assertEqual(2, self.chara.ohanasi_kaisu)
        self.assertEqual(2, self.chara.get_point())

    def test_point_sodateru_gohan_ohirune_ohanasi(self):
        self.chara.sodateru(animalgame.Jikan.GOHAN)
        self.chara.sodateru(animalgame.Jikan.OHIRUNE)
        self.chara.sodateru(animalgame.Jikan.OHANASI)
        self.assertEqual(3, self.chara.sodateta_kaisu)
        self.assertEqual(1, self.chara.tabeta_kaisu)
        self.assertEqual(1, self.chara.ohirune_kaisu)
        self.assertEqual(1, self.chara.ohanasi_kaisu)
        self.assertEqual(2, self.chara.get_point())

if __name__ == "__main__":
    unittest.main()
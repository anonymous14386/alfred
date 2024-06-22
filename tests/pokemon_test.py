import unittest
import modules.pokemon as pk


class TestPokemonMethods(unittest.TestCase):

    def test_getImageUrl(self):
        self.assertEqual(
            pk.getImageUrl("1"), "https://www.serebii.net/pokemon/art/1.png"
        )

    def test_getEmbedColor(self):
        self.assertEqual(pk.getEmbedColor("Grass"), 0x007400)


if __name__ == "__main__":
    unittest.main()

import unittest
import PostCorrespondenceProblem
class Test_PostCorrespondenceProblem(unittest.TestCase):
    def test_A(self):
        print("Test A Called...")
        test = PostCorrespondenceProblem.PostCorrespondenceProblem(2,3,1,4,[["c","cca"],["ac","ba"],["bb","b"],["ac","cb"]])
        solve = test.solve()
        self.assertEqual(solve,"bbaccacbb")
    def test_B(self): #Bad Data Test
        print("Test B Called...")
        test = PostCorrespondenceProblem.PostCorrespondenceProblem(2,3,1,4,[["caa","cca"],["ac","ba"],["bb","b"],["ac","cb"]])
        solve = test.solve()
        self.assertFalse(solve)
    def test_C(self):
        print("Test C Called...")
        test = PostCorrespondenceProblem.PostCorrespondenceProblem(2,3,1,4,[["b","ca"],["a","ab"],["ca","a"],["abc","c"]])
        solve = test.solve()
        self.assertEqual(solve,"abcaaabc")
    def test_D(self):
        print("Test D Called...")
        test = PostCorrespondenceProblem.PostCorrespondenceProblem(2,3,1,3,[["1","111"],["10111","10"],["10","0"]])
        solve = test.solve()
        self.assertEqual(solve,"101111110")
    def test_E(self): #Infinite Loop Test
        print("Test E Called...")
        test = PostCorrespondenceProblem.PostCorrespondenceProblem(2,3,1,3,[["10","101"],["011","11"],["101","011"]])
        solve = test.solve()
        self.assertFalse(solve)
if __name__ == '__main__':
    unittest.main()

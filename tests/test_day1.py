from src.day1.day1 import parse_input, compute_distance, similarity_score, solve2


def test_parse_input_one_line():
   input_="3   4"
   rl, ll = parse_input(input_)
   assert rl == [3] and ll == [4]

def test_parse_input_multiple_lines():
    input_ = ("3   4\n"
              "5   6\n"
              "4   8")
    rl, ll = parse_input(input_)
    assert rl == [3, 5, 4]
    assert ll == [4, 6, 8]

def test_compute_distance_is_zero():
    rl = [3, 2, 1]
    ll = [1, 3, 2]
    assert compute_distance(rl, ll) == 0

def test_compute_distance_non_zero():
    rl = [3, 2, 1]
    ll = [1, 2, 2]
    assert compute_distance(rl, ll) == 1

def test_of_acceptance():
    input_ = ("3   4\n"
              "4   3\n"
              "2   5\n"
              "1   3\n"
              "3   9\n"
              "3   3")
    rl, ll = parse_input(input_)
    total_distance = compute_distance(rl, ll)
    assert total_distance == 11

def test_similarity_score():
    rl = [1, 2, 3]
    ll = [2, 2, 3]
    assert similarity_score(rl, ll) == (1*0 + 2*2 + 3*1)

def test_of_acceptance2():
    input_= ("3   4\n"
             "4   3\n"
             "2   5\n"
             "1   3\n"
             "3   9\n"
             "3   3")
    assert solve2(input_) == 31



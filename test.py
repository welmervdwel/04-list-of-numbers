import num_list

def test_file_prints_numbers(capsys):
    """
    Check that running your code should print out each number on a new line
    """
    num_list.print_each_number()
    out, err = capsys.readouterr()
    assert "12\n10\n32\n3\n66\n17\n42\n99\n20\n" in out, "Your code should print out each number on a new line"

def test_file_prints_numbers_and_squares(capsys):
    """
    Check that running your code should print out each number and its square on a new line
    """
    num_list.print_each_number_and_its_square()
    out, err = capsys.readouterr()
    assert "The square of 12 is 144\nThe square of 10 is 100\nThe square of 32 is 1024\nThe square of 3 is 9\nThe square of 66 is 4356\nThe square of 17 is 289\nThe square of 42 is 1764\nThe square of 99 is 9801\nThe square of 20 is 400\n in out", "Your code should print out each number and its square on a new line"

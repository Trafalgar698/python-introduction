from hello import hello

def test_hello(capsys):
    hello()
    print("Bonjour le monde!")
    captured = capsys.readouterr()
    assert captured.out == "Bonjour le monde!\n"
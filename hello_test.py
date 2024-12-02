import hello

def test_main(capsys):
    hello.main(['Akanksh'])
    out, err = capsys.readouterr()
    assert out == "Hello Akanksh!\n"
    assert err == ""
    

def test_main_empty(capsys):
    hello.main([''])
    out, err = capsys.readouterr()
    assert out == ""
    assert err == "Enter a non-empty name\n"
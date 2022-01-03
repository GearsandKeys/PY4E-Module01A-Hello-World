import helloworld
import sys

def test_hello(capsys):
    helloworld.hello_world()
    assert capsys.readouterr().out == "hello world\n"
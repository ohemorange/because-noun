import os, sys, subprocess

def feed_to_parser(text):
    p.stdin.write(text + '\n')

def spawn_stanford_parser():
    global p
    p = subprocess.Popen('bash stanford-parser-full-2014-01-04/lexparser.sh -sentence newline -', shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)

def exit_parser():
    p.stdin.close()

# will only parse the first sentence it receives
def sentence_parse(text):
#    cmd = "bash stanford-parser-full-2014-01-04/lexparser.sh -"
#    return subprocess.check_output(cmd, shell=True, stdin=subprocess.PIPE)
    feed_to_parser(text)
    p.stdin.flush()
    line = p.stdout.readline()
    out = ""
    while line != "\n":
        out += line
        line = p.stdout.readline()
    return out

def main():
    sys.stdout.flush()
    spawn_stanford_parser()
    print sentence_parse("This is a sample sentence. This is another.")
    print sentence_parse("This is a third sentence.")
    # Should print the parses of sample and third.
    exit_parser()
    sys.stdout.flush()

main()

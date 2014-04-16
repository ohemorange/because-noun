import os, sys, subprocess

def feed_to_parser(text):
    p.stdin.write(text + '\n')

def spawn_stanford_parser():
    global p
    p = subprocess.Popen('bash stanford-parser-full-2014-01-04/lexparser.sh -', shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)

def exit_parser():
    p.stdin.flush()
    p.stdin.close()

def single_parse(text):
#    cmd = "bash stanford-parser-full-2014-01-04/lexparser.sh -"
#    return subprocess.check_output(cmd, shell=True, stdin=subprocess.PIPE)
    spawn_stanford_parser()
    feed_to_parser(text)
    exit_parser()
    return p.stdout.read()

def main():
    sys.stdout.flush()
    print single_parse("This is a sample sentence. This is another.")
    sys.stdout.flush()

main()

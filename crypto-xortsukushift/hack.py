from subprocess import Popen, PIPE
from time       import sleep

def main():
  with Popen('nc challs.tsukuctf.org 30057', shell=True, stdin=PIPE, stdout=PIPE, text=True, bufsize=0) as proc:
    win: list[str] = []
    for _ in range(280):
      while 1:
        txt = proc.stdout.readline().rstrip()
        print('>>>', txt)
        if 'Round' in txt:
          break
      proc.stdin.write('0')
      proc.stdin.write('\n')
      proc.stdin.flush()
      res = proc.stdout.readline().rstrip()
      print('>>>', res[:63])
      print('<<<', 0)
      print('>>>', res[63:])
      if 'You win!' in res:
        win.append('0')
      if 'Draw' in res:
        win.append('1')
      if 'You lose!' in res:
        win.append('2')
    print(f'(debug) win={"".join(win)}')
    sleep(1)
    for hand in (win + win):
      while 1:
        txt = proc.stdout.readline().rstrip()
        if len(txt) == 0:
          return
        print('>>>', txt)
        if 'Round' in txt:
          break
      proc.stdin.write(hand)
      proc.stdin.write('\n')
      proc.stdin.flush()
      res = proc.stdout.readline().rstrip()
      print('>>>', res[:63])
      print('<<<', hand)
      print('>>>', res[63:])
  return

if __name__ == '__main__':
  main()

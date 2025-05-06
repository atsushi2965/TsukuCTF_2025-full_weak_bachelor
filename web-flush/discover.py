import hmac, hashlib, requests, re

SEED = bytes.fromhex(
    'b7c4c422a93fdc991075b22b79aa12bb'
    '19770b1c9b741dd44acbafd4bc6d1aab'
    'c1b9378f3b68ac345535673fcf07f089'
    'a8492dc1b05343a80b3d002f070771c6'
)

TOTAL_ROUNDS      = 10
DIGITS_PER_ROUND  = 7
BASE = 'http://challs.tsukuctf.org:50000/'

def lcg_params(seed: bytes, session_id: str):
    m = 2147483693
    raw_a = hmac.new(seed, (session_id + 'a').encode(), hashlib.sha256).digest()
    a = int.from_bytes(raw_a[:8], 'big') % (m - 1) + 1
    raw_c = hmac.new(seed, (session_id + 'c').encode(), hashlib.sha256).digest()
    c = int.from_bytes(raw_c[:8], 'big') % (m - 1) + 1
    return m, a, c

def generate_round_digits(seed: bytes, session_id: str, round_index: int):
    m, a, c = lcg_params(seed, session_id)
    # initial state = HMAC(seed, session_id) mod m
    h0 = hmac.new(seed, session_id.encode(), hashlib.sha256).digest()
    state = int.from_bytes(h0, 'big') % m

    # fast‑forward
    for _ in range(DIGITS_PER_ROUND * round_index):
        state = (a * state + c) % m

    # now emit digits
    digits = []
    for _ in range(DIGITS_PER_ROUND):
        state = (a * state + c) % m
        digits.append(state % 10)
    return digits

# ——————————————————————————————————————
# 1) Establish a session and pull your cookie payload
sess = requests.Session()
sess.get(BASE + '/')   # reset, sets your session cookie
cookie_val = sess.cookies.get_dict()['session']

# 2) Decode session_id exactly as above (or copy from browser)
payload = cookie_val.split('.', 1)[0]
b = payload + '=' * ((4 - len(payload) % 4) % 4)
import base64, json
session_id = json.loads(base64.urlsafe_b64decode(b))['session_id']

# 3) Recompute and sum
total = 0
for r in range(TOTAL_ROUNDS):
    sess.get(BASE + '/flash')
    digs = generate_round_digits(SEED, session_id, r)
    total += int(''.join(map(str, digs)))

# 4) Fetch the one‑time token and submit your answer
res   = sess.get(BASE + '/result')
token = re.search(r'name="token" value="([0-9a-f]+)"', res.text).group(1)

final = sess.post(BASE + '/result', data={'token': token, 'answer': total})
print(final.text)  # フラッグを含んだHTMLソース全体
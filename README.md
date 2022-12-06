# spam_defend_our_kids

## Scope

This is a simple selenium bot that uses Chrome to inject fake data into [Defend Our Kids](https://www.defendkidstx.com/).

There is a cloudflare proxy, so you'll get rate limited if you hit it too many times within "a few mins." So I suggest running
something like the following on a computer and injecting one every 90 odd seconds.

## Setup

You'll need to install the [ChromeDriver](https://chromedriver.chromium.org/downloads) in the same directory that you'll run this from. I'm
95% sure this will _only_ work with Chrome too.

Python setup:

```bash
git clone https://github.com/jjasghar/spam_defend_our_kids/
cd spam_defend_our_kids
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

Helpful run script...

```bash
while true ; do sleep $[ ( $RANDOM % 90 )  + 1 ] && python main.py ; done
```

If you have suggestions on how to make this better, please don't hesitate to put a PR in.

## License & Authors

If you would like to see the detailed LICENSE click [here](./LICENSE).

- Author: JJ Asghar <jjasghar@gmail.com>

```text
Copyright:: 2022- JJ Asghar

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```


# Finding Full Prime Day
Full prime day is a day like 2019/05/23.
Because ...

```
20190523→prime
0190523→prime
190523→prime
90523→prime
0523→prime
523→prime
23→prime
3→prime
```

Reference to this tweet https://twitter.com/9973_prm/status/1131217915389157383

# Usage

```sh
$ python full_prime_day.py
20190823 is full prime day!
20300317 is full prime day!
20360317 is full prime day!
20400307 is full prime day!
20400823 is full prime day!
------------------------------
From 2019/05/24 to 2046/10/09
We find 5 full prime days which means 0.05 %

$ python full_prime_day.py 100000
20190823 is full prime day!
20300317 is full prime day!
...
21990523 is full prime day!
------------------------------
From 2019/05/24 to 2293/03/08
We find 24 full prime days which means 0.024 %
```
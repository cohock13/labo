# 12-1
Python
```bash
python 12_1.py
```
C
```bash
gcc 12_1.c
```
Pythonによる作画.ついでなのでPythonライブラリScipyの常微分方程式のソルバでも試してみた.
![sol](https://user-images.githubusercontent.com/55901554/80989982-9f668980-8e70-11ea-944c-ec7b0b871f81.png)

ぱっと見た感じdt=0.2でもほとんど違いはないように見える.

誤差については以下のような感じになった(片対数グラフ).

![error](https://user-images.githubusercontent.com/55901554/80990799-f1f47580-8e71-11ea-9357-bf6a7aec826f.png)

刻み幅dtにたいしてオイラー法が誤差O(dt^2),ルンゲクッタ法が誤差O(dt^5)くらいになることを踏まえると妥当な結果のように見える.
Scipyのソルバもルンゲクッタとだいたい同じかややいいくらいの精度があるように見える.



# 12-2
Python
```bash
python 12_2.py
```
C
```bash
gcc 12_2.c
```

Pythonでプロットしたところ以下のようになった.

![sol2](https://user-images.githubusercontent.com/55901554/80991320-ca51dd00-8e72-11ea-9750-5ff5d361ee78.png)

やや見にくいが,τが小さくなるにつれ,位相が赤いa*sin(x)に近づいている様子がわかる.







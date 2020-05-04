# 12-1
Python
```bash
python 12_1.py
```
C
```bash
gcc 12_1.c
```
Pythonによる作画.
ついでにPythonライブラリScipyの常微分方程式のソルバでも試してみた.
![sol](https://user-images.githubusercontent.com/55901554/81003943-9aacd000-8e86-11ea-98e3-e33d509fa340.png)


ぱっと見た感じdt=0.2でもほとんど違いはないように見える.

誤差については以下のような感じになった(片対数グラフ).

![error](https://user-images.githubusercontent.com/55901554/80990799-f1f47580-8e71-11ea-9357-bf6a7aec826f.png)

刻み幅dtにたいしてオイラー法が誤差O(dt^2),ルンゲクッタ法が誤差O(dt^5)くらいになることを踏まえると妥当な結果のように見える.
Scipyのソルバもルンゲクッタとだいたい同じかややいいくらいの精度があるように見える.
<br>
<br>

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

# 12-3

/Sample4-3にあるdata.txtをgnuplotでプロットした結果,以下のようになった.

t-x平面とt-y平面
![txty](https://user-images.githubusercontent.com/55901554/81002933-04c47580-8e85-11ea-9b04-e8f3ff057b4d.png)
<br><br>
x-y平面
![x-y](https://user-images.githubusercontent.com/55901554/81002955-0ee67400-8e85-11ea-918a-f89f2e3543f7.png)
<br><br>
x-y平面のふるまいから,安定な固定点への引き込みが起きていることがわかる.
<br><br>







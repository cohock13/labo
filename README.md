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
これらのプロットから,この場合からは安定な固定点への引き込みが発生していることが伺える.
<br><br>

# 12-4

```bash
python 12_4.py
```

動画にすると以下のようになった.

![12_4](https://user-images.githubusercontent.com/55901554/81014506-f16ed580-8e97-11ea-9b79-fdb45131f58b.gif)
<br>

引き込み点が存在する場合はtが経過するにつれ引き込み点へ引きこまれ,そうでない場合は振動するようになることがわかる.
<br>



# 12-5

```bash
python 12_5.py
```
いくつかの初期条件によってプロットしてみると以下のようになった.<br>
![phi2-phi1](https://user-images.githubusercontent.com/55901554/81027691-a960aa80-8eb9-11ea-8421-28a76efe7899.png)


位相差がπと0の近いほうに収束する形になる.<br>
<br>
次に,これを単位円上での点の位相と解釈して点を動かしてみる.<br>
まず,点が2個(N=2)のときについて,q(t)=sin(t)のときのケースを動かしてみる.<br>
![n_2_sin](https://user-images.githubusercontent.com/55901554/81026823-5fc29080-8eb6-11ea-8187-844818655af3.gif)
<br>
点がお互いに近づきあい,同位相になっていることが確認できる.<br>
次に,N=8にしてみる.<br>
![n_8_sin](https://user-images.githubusercontent.com/55901554/81027545-2d666280-8eb9-11ea-8d27-5c0279455ab0.gif)

同様に位相の同期が発生していることが確認できる.<br>
最後に,εを高めて(0.5くらい)q(t) = cos(t) としてみる.<br>

![n_8_cos](https://user-images.githubusercontent.com/55901554/81027189-b54b6d00-8eb7-11ea-8db8-828612d513d7.gif)

sinと逆位相になるので,お互いを弾きあうふるまいをする.アニメーションを見ると,反発を受けて移動した先に近づいたものから反発を受けて...といったサイクルを繰り返していることが伺える.






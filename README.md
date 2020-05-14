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


位相差が2πと0の近いほうに収束する形になる.<br>
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

'''
sinと逆位相になるので,お互いを弾きあうふるまいをする.アニメーションを見ると,反発を受けて移動した先に近づいたものから反発を受けて...といったサイクルを繰り返していることが伺える.
'''
正しくない?


# 12-6

```bash
python 12_6.py
```

OVモデルのシミュレーション.先頭の個体を減速させ, N=20,a = 1,d = 1,κ = 1, L = 20 で以下のようになった.<br>

![12_6](https://user-images.githubusercontent.com/55901554/81915555-b7c36a80-960d-11ea-9ef1-d616dfdee3a1.gif)

<br>

左上周辺に渋滞が発生していることがわかる.

前,12-5で結合関数をcosにしたときにOVモデルと似たふるまいを示すことがあったが,それについて少しだけ考えたので記す.

まず, N = 8 のときのOVモデルで,先頭の個体の速度を0にしたときのOVモデルでのシミュレーション結果を示す.

![12_6_1](https://user-images.githubusercontent.com/55901554/81916016-46d08280-960e-11ea-9460-8a7228e909dc.gif)


先頭に追い付いた個体が渋滞を引き起こしている.

これに対して,結合振動子のモデルで,先頭とその1つ後ろの個体を近づけたときのシミュレーションを以下に示す.

![12_6_2](https://user-images.githubusercontent.com/55901554/81916214-7c756b80-960e-11ea-9385-66103797226b.gif)

ペアが離れずにくっついたまま動いていることが伺える.わかりにくいので,結合関数の係数を引き上げて速度を上げると以下のようになる.

![12_6_3](https://user-images.githubusercontent.com/55901554/81916302-9dd65780-960e-11ea-84cd-d2664ce8ee18.gif)

OVモデルでは,前の個体の位置と速度を見て次の行動を起こしているのに対し,結合子モデルでは,自分以外のすべての個体の位置を見て行動をする点においてまず違いがあるので,直観的には同じふるまいをすることはないと考えらえる.

しかし,12-5の動画はOVモデルのように点が一方向のみに進むわけではない(結合子モデルでは点は後退もする)が,それでもやはり似たようなふるまいであることは否めない.結合関数がsinのときは「一点に収束する」ことがある程度自明に扱えるわけだが,cosでもそのような直観はないのだろうか.位相のずれはともかく,ふるまいからすると何らかの力,相互作用が考えられはしないだろうか...>






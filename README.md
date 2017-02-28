
#Background

話説前一排去左上線啦玩左幾round百家樂,而近排又玩緊ml,所以就整左個python simulator黎模擬投注情況


我地首先假設本金1000, 每注面值相同並以p為代表,p={100,200,300,400,500}直至無牌或無足夠現金 


使用random generator作為對買燈嘅模擬 並盡量減少抽中和局嘅機會


首先用generator.cpp generate想要嘅牌數,simulation__with_output _winningsequence.py 做模擬,再輸出dataset,
並用 plot_modified_without_space.py plot scatter,heatmap


#Result


![alt tag](https://holland.pk/qlivtda4)


從數據結果我地知道係隨機投注,不斷嘅上升嘅iteration數目或者輸入副數,
只係會令平均最大收益converge去某一個細嘅range 所以我地就用左1000副做模擬dataset



再將每局持有嘅現金量同埋對應局數用scatter同heatmap plot出黎

1000 副
![alt tag](https://holland.pk/4k0fte9j)

10000副
![alt tag](https://holland.pk/62be1wnu)


就會發現其實平均最大收益咁細嘅原因就係大部份都會係頭1x round之內輸清光 拉低左個mean

將所持少過1000嘅人移除









![alt tag](https://holland.pk/hvwyi2ue)



無大差別=_=



某程度上證明左'燈'本身,有特別投注方法或者算法令佢地可以克服1.3-1.5呢個upper bound(廢話)

之後應該會向投注方法著手或者用ml解

從數據猜測,有可能見到5-6次和之後先開始玩,可能係一種有效嘅手段

利申:唔識玩啤牌,如果因為上述結果而有所損失 本人不會負責、

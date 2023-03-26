# **python機器學習第一次作業** #
## **問題:選擇第一題** ##
  **原因:**
  
  &nbsp;&nbsp;&nbsp;&nbsp;當初因為在看檔案的時候，發現第一題是有四個csv檔，就認為或許多個檔案會比較挑戰性，也能夠練習比較多東西，因此就選擇了第一題當作作業。
  
  **問題:**
1. Is there a global warming?
2. Which period is the fastest temperature growth?
3. Which country is the hottest one and which is the coldest one?
## **資料處理** ##
因為這三題題目所需要用到的dateset只會有 `GlobalLandTemperaturesByCountry` 和`GlobalTemperatures`兩個，其他可以忽視不管，另外裡面也有許多不會用到的資料，因此在一開始會先把所有空值變成`NAN`值，再用 `drop()` 和 `dropna()` 兩個把不需要的資料以及含有`NAN`值的資料刪掉，這樣可以讓接下來的資料處理變順暢。
## **問題一:Is there a global warming?** ##
首先，這個問題對於全球暖化沒有準確的定義，因此我定義為相較其他時代，隨著時間的推進，全球溫度有明顯的上升，因此會用到的就是`GlobalLandTemperaturesByCountry`這個dataset，但裡面的只有每月的溫度，所以一開始要先把dataset裡`dt`的資料變成正確的時間格式，並只留下年，之後用`groupby()`，依照年把資料分組並算出年均溫，然後用散布圖來表示，並劃出非線性回歸曲線，成果如下:
![Figure_1](https://user-images.githubusercontent.com/79913276/227790714-c00bb718-a1bd-4ee2-b5b8-9ae26bb9e47d.png)
從圖裡面能看出，跑出來的回歸線代表溫度會先稍微下降，大概從1850年開始就逐年往上增長，而且速率明顯變快，因此可以從中看出是有全球暖化的跡象，唯一的問題是`R^2`屬於中度關係，但如果從觀察圖，就能夠發現與回歸線偏離較多的都是較早的資料，如果把1850年前的資料全部剔除，結果如下:
![Figure_1 1](https://user-images.githubusercontent.com/79913276/227790843-c027e303-212b-4790-b80e-27d29cfecd43.png)
能夠從中看出`R^2`大幅提升，而且也能看出全球溫度都是逐年往上，因此能夠證明全球暖化是存在的(跟本題一開始所設定的定義相同)

## **問題二:Which period is the fastest temperature growth?** ##
這題要先定義多久為`period`，我是定義了四個數字，分別是10、50、100、200為一個period，而做法就是從一個period裡找出最高溫和最低溫，相減後除以`period`的長度，已得到溫度的平均變化速率，而跑出來的結果如下:
![Figure_2](https://user-images.githubusercontent.com/79913276/227791000-42cafd84-a743-46e3-8a6e-f0b0e2f330b9.png)
從結果可以看出來，不論選擇多長的period，所得到的最大速率皆是在1850年以前，然而這跟第一題所得到的結果有所矛盾，我猜想有兩個可能的原因:第一個就是第一題的非線性`R^2`真的太低，以至於模型完全不符合實際情形，但是因為不知道其他的回歸模型該要怎麼處理，因此無法證明是否是這個原因；第二個是在第二題處理資料或是最回歸分析時出現了錯誤，然而因為都是用同一個dataset，處理程序也都大同小異，因此不確定是否是這個原因。
## **問題三: Which country is the hottest one and which is the coldest one?** ##
首先，本題並沒有說到何謂最熱及最冷，因此在此定義為年均溫的最高及最低，因此先用`groupby()`，依照`Country`來分組並算出每個國家的年均溫，並用柱狀圖列出前三熱及前三冷的國家，結果如下:
![Figure_3](https://user-images.githubusercontent.com/79913276/227791460-5b315cc8-438f-4988-b8a2-43210f343b50.png)
依照結果來看，最熱的國家是:Djibouti，年均溫是:28.817℃；而最冷的國家是:Greenland，年均溫是:-18.587℃

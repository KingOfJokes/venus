# venus
1. system: involving several def-function related to backtest(generate a postion、test its return rate...)
2. dg(cython form for datagenerate): alternative way to create derivative data from original data(while some famous derivative data like
   KD value、revenue's yoy...have already been calculated and restored as npy film,and thus don't need to use 'dg')
3. answer: where we revise filter for position-generating、show the dashboard of strategy imported.

other:
1. test: used for testing whether datagenerate work or not.
2. viewnpy: check whether the npy film we create is consistent with true data. 

answer.py guidance:(以下步驟具有序性，要按照順序執行)
1. selectmode: 1 for 自行撰寫選股策略(在system的filter中進行修改)；2 for 使用模板化策略(在本py檔修改ifs清單中的條件)
2. positionize: 生成每日部位，其權重為各檔股票所要投入的金額
3. rankize: 將部位按照大小重新給定權重(e.g. [50,5,1] -> [3,2,1])，主要功能是可以平滑各部位比例，避免押注太多在單一訊號強烈的部位
4. longize: 若希望在訊號消散後持續持有一段時間(比方說，投信連日買超的個股，當投信停止買超時，行情也許尚未結束，可以用此函數讓部位往後延伸若干天)
5. neutralize: 中立化部位，讓多空部位的價金相等
6. sharelize: 將部位轉化為實際買入張數
-------
1. backtest: 將部位轉化為績效、dashboard的函數
2. in-sample/out-sample: 此處回測把測資切成了兩段，在最適化的時候通常會看IS，OS則是用來檢視策略是否具穩健性
3. distribution: 可以了解每個部位帶來的損益情形，了解策略的獲利是否是由極端值而來(which is not a good news)

-------
1. Research field: 研究整體量化策略
2. Individual Research: 觀察個股的歷史股性表現

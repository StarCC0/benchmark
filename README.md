# Benchmark for Simplified Chinese to Traditional Chinese conversion

## 設計思路

由 RTHK 即時新聞匯出 2021 年全年新聞文本，將文本轉為簡體後作為測試輸入，繁體版原文作為預期輸出。

TODO:

- [ ] 將繁體轉為簡體時，需要人工判斷「一繁對多簡」的字詞
- [ ] RTHK 即時新聞語料有別於 OpenCC 標準，需要異體字規範化，如「為」>「爲」
- [ ] RTHK 即時新聞本身有誤，如多次出現將「發佈」誤作「發布」，需人工修正

## Compute accuracy

Run `python compute_accuracy.py output.txt answer.txt`.

## Get the dataset

Open Telegram. In the @rthk_new_c channel, click export. Select a range from 1 Jan 2021 to 31 Dec 2021. Save the JSON file to `ChatExport.json`.

Run `preprocess.py`.

Run `opencc -c hk2s -i answer.txt -o input.txt`.

# RSNA_data_preprocessing

![image](https://github.com/MingChin-Kao/RSNA_data_preprocessing/blob/main/images/flow_chart.svg)

### Step1. 從 [Kaggle](https://www.kaggle.com/competitions/rsna-intracranial-hemorrhage-detection/overview) 下載檔案，並解壓縮得到以下資料夾

---

- stage_2_test/ (DICOM File)
- stage_2_train/ (DICOM File)
- stage_2_sample_submission.csv
- stage_2_train.csv

### Step2. 環境建置

---

下載此 repo 並透過 requirements.txt 進行環境建置

- Python=3.8

```bash
pip install -r requirements.txt
```

### Step3. 設定 [config.py](http://config.py) 檔

---

於 [config.py](http://config.py) 檔案中設定 `RSNA_ROOT_DIR` 及 `ZIP_FILE` 路徑

- `RSNA_ROOT` ⇒ Step1 下載下來解壓縮的資料夾位置
- `ZIP_FILE` ⇒ Step1 下載下來的 zip 檔位置

### Step4. 執行 [config.py](http://config.py) 檔案

---

執行 [config.py](http://config.py) 檔案用來建立所需資料夾

```bash
python config.py
```

### Step5. 執行 prepare_meta_dicom.py

---

- 將所有 DICOM 轉成 PNG 檔
- 產生 train_metadata.csv
- 產生 test_metadata.csv

### Step6. 執行 efficient_data_format_preprocess.ipynb

---

- 透過 efficient_data_format_preprocess.ipynb 將csv資料轉成 efficientnet 訓練需要的格式
- 產生 train.csv

### Step7. 執行 split_data.ipynb

---

- 透過 split_data.ipynb 將訓練資料進行切割

### Step8. 執行 split_data.ipynb

---

- 透過 cp_image.ipynb 將客戶端對應的資料複製出來
- 將每個 site 所屬的照片複製一份至 /fl/site_images/ 資料夾中
- 將 test_data 所屬的圖片複製一份至 /fl/site_images/ 資料夾中

### Training

---

[點我](https://www.kaggle.com/code/taindow/pytorch-efficientnet-b0-benchmark/notebook?scriptVersionId=21235680)

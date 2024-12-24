## GaussianPro
我們使用原GaussianPro論文所提供的實作 ([GaussianPro: 3D Gaussian Splatting with Progressive Propagation](https://github.com/kcheng1021/GaussianPro))

### Tested Environment
Windows 11, RTX 4070 Ti, CUDA 12.4

### Environment setup
```
SET DISTUTILS_USE_SDK=1 # Windows only
conda env create --file environment.yml
conda activate gaussianpro
pip install ./submodules/Propagation
pip install ninja
pip install matplotlib
```
請確保```environment.yml```內pytorch跟其依賴套件的版本與環境中CUDA版本相符 (可以參考[pytorch previous version](https://pytorch.org/get-started/previous-versions/))

### Training
`cd gaussianpro`
首先，請確保您已進入 `gaussianpro` 資料夾，才開始訓練

常用```train.py```的參數如下
-s \<data folder path>：訓練的資料，資料夾的結構如下
```
<data folder path>
├─ <images folder>
└─ sparse
   └─ 0
      ├─ cameras.bin
      ├─ images.bin
      └─ points3D.bin or points3D.ply
```
--images \<images folder>: 指定\<data folder path>結構下，哪個資料夾為\<images folder>

-m \<output folder>: 指定輸出路徑

-r \<1, 2, 4 or 8>: 訓練時會將<images folder>裡的圖片縮小對應倍率

--iterations \<int>: 迭代的次數

更多參數請詳閱[GaussianPro: 3D Gaussian Splatting with Progressive Propagation](https://github.com/kcheng1021/GaussianPro)
    
### Rendering
根據訓練完成輸出後的模型，使用```render.py```渲染輸出結果
    
常用```render.py```的參數如下
-m \<output folder>: 訓練生成模型的輸出路徑
    
    
### Metrics
根據模型渲染後的結果，使用```metrics.py```來產生相關指標 (PSNR、SSIM、LPIPS) 與預測輸出 
    
常用```metrics.py```的參數如下
-m \<output folder>: 訓練生成模型的輸出路徑
相關指標會寫入results.json
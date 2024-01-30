# Bird Classificator 

  

App for classifying birds using machine learning. 

  

Data taken from: 

https://www.kaggle.com/datasets/gpiosenka/100-bird-species 

## Requirements: 

__Model requiements:__


* Visual Studio Code  

* Python 3.10 

* Libraries from requirements.txt 

__Streamlit App requirements:__ 

* Internet Browser 

* Internet Connection 

__Mobile App requirements:__ 

* Android Studio  

* Min Android API: 26 

## Building Steps: 

__Model Building Steps:__

1. Download repository from github 

2. Open folder with Visual Studio Code using Python 3.10 

3. Open Terminal and use command: “pip install -r .\requirments.txt” 

4. Use command “python train.py” in Train folder to train model  

5. Use command “python convert_to_tflite.py” in app folder (required for mobile app)  

__Streamlit App Building Steps:__ 

__Building for localhost:__

1. Download repository from github 

2. Run StreamlitApp/run.bat

3. Wait patiently, first time there might be a need to click enter

__Building for Microsoft Azure:__ 

1. Download repository from github 

2. Open floder with Visual Studio COde using Python 3.10 

3. Open Terminal and use “pip install azure-cli” 

4. Then "az login” 

5. Now login into your azure account, create container registry REGNAME and resource group RESGROUPNAME 

6. Use command az acr build --registry REGNAME --resource-group RESGROUPNAME  --image YOURNAME 

7. Now run app in azure and configure its port, as well as choose resource group and repository. 

8. A link can be provided to the customer 

__Mobile App Building Steps:__

1. Download repository from github  

2. Open android project with Android Studio  

3. Change to a device that has android 26 

4. Place .tflite file in ml folder (required if ml folder is empty) 

5. Run app with Shift + F10 

 

 

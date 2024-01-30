# Bird Classificator 

  

App for classifying birds using machine learning. 

  

Data taken from: 

https://www.kaggle.com/datasets/gpiosenka/100-bird-species 

## Requirements: 

Model requiements: 

Visual Studio Code  

Python 3.10 

Libraries from requirements.txt 

Streamlit App requirements: 

Internet Browser 

Internet Connection 

Mobile App requirements: 

Android Studio  

Min Android API: 26 

## Building Steps: 

Model Building Steps: 

Download repository from github 

Open folder with Visual Studio Code using Python 3.10 

Open Terminal and use command: “pip install -r .\requirments.txt” 

Use command “python train.py” in Train folder to train model  

Use command “python convert_to_tflite.py” in app folder (required for mobile app)  

Streamlit App Building Steps: 

Building for localhost: 

Download repository from github 

Open folder with Visual Studio Code using Python 3.10 

Open Terminal and use command: “pip install -r .\requirments.txt” 

Use command “streamlit run ./StreamlitApp/app.py” 

Open link provided 

Building for Microsoft Azure: 

Download repository from github 

Open floder with Visual Studio COde using Python 3.10 

Open Terminal and use “pip install azure-cli” 

Then "az login” 

Now login into your azure account, create container registry REGNAME and resource group RESGROUPNAME 

Use command az acr build --registry REGNAME --resource-group RESGROUPNAME  --image YOURNAME 

Now run app in azure and configure its port, as well as choose resource group and repository. 

A link can be provided to the customer 

Mobile App Building Steps: 

Download repository from github  

Open android project with Android Studio  

Change to a device that has android 26 

Place .tflite file in ml folder (required if ml folder is empty) 

Run app with Shift + F10 

 

 

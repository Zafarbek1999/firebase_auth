# Veprof Test Assessment

# How to run the project

### Create a [firebase project](https://cloud.google.com/firestore/docs/client/get-firebase)
### Once you have created a Firebase project, you can initialize the SDK with an authorization strategy that combines your service account file together with [Google Application Default Credentials.](https://cloud.google.com/docs/authentication/production#providing_credentials_to_your_application) 
### To authenticate a service account and authorize it to access Firebase services, you must generate a private key file in JSON format.
### To generate a private key file for your service account:
#### 1. In the Firebase console, open Settings > [Service Accounts.](https://console.firebase.google.com/project/_/settings/serviceaccounts/adminsdk)
#### 2. Click `Generate New Private Key`, then confirm by clicking `Generate Key`.
#### 3. After downloaded the JSON file, copy it to project folder as `firebase_config.json`

### Create and fill .env file using .env.example
### To fill .env file, you will need Firebase Web API Key, which can be obtained on the [project settings](https://console.firebase.google.com/project/_/settings/general/) page in your Firebase console.

### Run project with docker
`docker-compose up --build -d`

### Go to http://0.0.0.0:8000/admin,  enter `admin` as username and `admin123` as password.
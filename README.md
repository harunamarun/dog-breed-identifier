# dog-discriminator

"This was created during my time as a student at Code Chrysalis."

This app provides dog discriminator just frenchbulldog, poodle or others.

Let's try to upload!

1. You upload the picture of dog.
2. this service return dog name (e.g. Frenchbulldog, poodle)

## URL

You try this app.

## Setup Instructions

#### Clone the repo:

```
git clone https://github.com/harunamarun/create-resume-app.git
```

#### Install packages:

```
yarn
```

#### Start server:

```
flask run --debugger --reload
```

## API

#### Endpoints

1. POST `/`</br>

#### Details

1. GET `/api/resumes`  
   Return list of resumes.  
   response:
   ```
   [
    {
     "id":1,
     "firstname":"Hanako",
     "lastname":"Yamada",
     "address":"Tokyo",
     "gender":"female",
     "career1":"********* corporation",
     "desc1":"I experienced fooooooooo!",
     "career2":"*** corporation",
     "desc2":"I experienced piyopiyo!",
     "template":"temp1",
     "updatedAt":"2020-02-10 04:11:10"
    },
    {...}
   ]
   ```

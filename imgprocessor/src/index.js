const express = require('express');
const upload = require('express-fileupload');
const app = express();
const { encrypt, decrypt} = require('./algo');
const port = 3000;
const fs = require('fs')
      

app.use(
    upload({
        limits: {
            fileSize: 10000000,
        },
        abortOnLimit: true,
    })
);



app.get('/', (req, res) => {
    res.send('Hello World!');
});

app.post('/', async(req, res) => {
    // Get the file that was set to our field named "image"
    const { file } = req.files;

    // If no file submitted, exit
    if (!file) return res.sendStatus(400);
    
    const acceptedImageTypes = ['image/gif', 'image/jpeg', 'image/png'];
 
    if(!acceptedImageTypes.includes(file['mimetype'])) return res.sendStatus(400);
    console.log(file)
    const hashedData = encrypt(file.data);
    console.log(hashedData)
    const newImage = file
    newImage.data = hashedData;
    res.send(newImage);
});

app.listen(port, () => {
    console.log(`Example app listening on port ${port}`);
});
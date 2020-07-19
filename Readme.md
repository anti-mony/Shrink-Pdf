# Pdf Shrinking Web App

A Webapp to shrink Pdf files based on:
* Backend: Flask & [Shrinkpdf.sh](http://www.alfredklomp.com/programming/shrinkpdf/)
* Frontend: Bulma

A live version can be found here on Heroku: [ShrinkPdf](https://shrink-pdf.herokuapp.com/). 
There's a limit of 5MB uploads in this version. Heroku free version limits :( 

> The app deletes the files every hour automatically using a cron job. It's just a simple find and delete.

Special thanks to Alfred Klomp for writing the awesome script [Shrinkpdf.sh](http://www.alfredklomp.com/programming/shrinkpdf/)

I would recommend hosting your own rather than using the version I mentioned above. OR host it on your local network and keep your data within :D

## Using(Deploying)

**Docker Compose**

```bash
docker-compose -f docker-compose.prod.yml up -d --build
```
And that's basically it. The app will be available on ```localhost:1337```. You change the port in the ```docker-compose.prod.yml``` file to host on port 80 or whatever.

Shrink All the Way !







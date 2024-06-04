const fs = require('fs');

class FileIO{
    constructor(filePath){
        this.fp = String(filePath);
    }

    existsStat(){
        return fs.existsSync(this.fp);
    }

    listDir(callback = null){
        fs.readdir(this.fp, (err, files) => {
            if (err){throw new Error(`Path does not exists '${this.fp}'`);}

            if (callback === null){
                true;
            }else{
                callback(files);
            }
        })
    }

    readStream(){
        return fs.createReadStream(this.fp);
    }
}

module.exports = {
    FileIO
}
const expect = require("chai").expect
const fs = require("fs")
const fetch = (...args) => import('node-fetch').then(({default: fetch}) => fetch(...args));

const svgDir = __dirname + "/../"

const changedFiles = process.env.CHANGED_FILES;

console.log('Changed files:', changedFiles);

const changedFilesArray = changedFiles ? changedFiles.split(/\s+/) : [];
console.log('Changed files as array:', changedFilesArray);

const delay = ms => new Promise(res => setTimeout(res, ms));

changedFilesArray.forEach((filename, i) => {
    console.log(`Filename is: ${filename}`);
    
    if (! filename.endsWith(".svg")) {return}
    
    const filepath = svgDir + filename
    console.log(`Filepath is: ${filepath}`);

    if(!fs.existsSync(filepath)) {
        console.log(`Skipping deleted file: ${filename}`);
        return;
    }
    console.log('SVG Contents: ', fs.readFileSync(filepath, "utf8"));

    describe(filename, async () => {

        it("should be under 1KB", () => {
            expect(fs.statSync(filepath).size).to.be.lessThan(1024)
        })

        it("should be validated by the w3c validator", async () => {
            await delay(200);
            //  Send as HTML to ensure validator checks properly.
            //  Replace newlines with spaces.
            //  https://github.com/validator/validator/wiki/Service-%C2%BB-Input-%C2%BB-POST-body
            await fetch("https://validator.nu/?out=gnu", {
                    method: "POST",
                    body: '<!doctype html><html lang=en><title>A</title>' + fs.readFileSync(filepath, "utf8").replaceAll("\n", " "),
                    headers: {"Content-Type": "text/html; charset=utf-8"}
                })
                .then(res => res.text())
                .then(res => {
                    expect(res).to.be.empty
                })
        })
        
    })
})

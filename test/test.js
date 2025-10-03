const expect = require("chai").expect
const fs = require("fs")
const fetch = (...args) => import('node-fetch').then(({default: fetch}) => fetch(...args));

const svgDir = __dirname + "/../"
const readme = __dirname + "/../README.md"

const readmeLines = fs.readFileSync(readme).toString().split("\n")

const changedFiles = process.env.CHANGED_FILES;

console.log('Changed files:', changedFiles);

const changedFilesArray = changedFiles ? changedFiles.split(/\s+/) : [];
console.log('Changed files as array:', changedFilesArray);

const readmeRegex = new RegExp("<br>(\\d{1,4}) Bytes<\/td>")

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
            await fetch("https://validator.w3.org/nu/?out=gnu", {
                    method: "POST",
                    body: fs.readFileSync(filepath, "utf8").replace(/aria-label="[^"]+"/g, ""),
                    headers: {"Content-Type": "application/xml"}
                })
                .then(res => res.text())
                .then(res => {
                    expect(res).to.be.empty
                })
        })
        
        it("should match readme size", () => {
            for(line of readmeLines) {
                if(line.includes("/svg/"+filename+"\" width=\"125\"")) {
                    const size = parseInt(line.match(readmeRegex)[1])
                    expect(fs.statSync(filepath).size).to.equal(size)
                    break
                }
            }
        })
    })
})
